#!/usr/bin/env python3
"""Validated pairwise YN00 screen. Omega thresholds are NOT significance tests.
Full AA alignment -> exact CDS validation -> codon threading -> verified mask.
Original results remain untouched; a new output directory is mandatory.
"""
import argparse
import csv
import hashlib
import json
import math
import shutil
import statistics
import subprocess
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import Bio
from Bio.Seq import Seq

FOCAL = ('Vper', 'Vtub')
STOPS = {'TAA', 'TAG', 'TGA'}


def parse_fasta(filepath):
    records, key = {}, None
    with open(filepath) as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                key = line[1:].split()[0]
                if key in records:
                    raise ValueError(f'Duplicate FASTA ID: {key}')
                records[key] = ''
            elif key is None:
                raise ValueError('Sequence before FASTA header')
            else:
                records[key] += line.upper()
    return records


def thread_cds(prot_aln, cds_unaligned):
    """Thread a COMPLETE protein alignment after exact translation validation."""
    cds = cds_unaligned.upper()
    protein = prot_aln.upper().replace('-', '')
    if not cds or len(cds) % 3:
        raise ValueError('CDS length is not a positive multiple of three')
    translated = str(Seq(cds).translate(table=1))
    if '*' in translated.removesuffix('*'):
        raise ValueError('Internal stop in CDS')
    if translated.removesuffix('*') != protein.removesuffix('*'):
        matches = sum(a == b for a, b in zip(translated, protein))
        raise ValueError(f'CDS/protein mismatch: {matches}/{len(protein)} positions match')
    if len(protein) > len(translated):
        raise ValueError('Protein terminal stop is absent from CDS')
    index, codons = 0, []
    for aa in prot_aln.upper():
        if aa == '-':
            codons.append('---')
        else:
            codons.append(cds[index:index + 3])
            index += 3
    return ''.join(codons)


def prepare_pair(full, trimmed, cds, max_gap=0.5):
    if set(full) != set(trimmed) or not set(FOCAL).issubset(full):
        raise ValueError('Alignment taxa differ or focal taxa missing')
    lengths = {len(seq) for seq in full.values()}
    if len(lengths) != 1:
        raise ValueError('Unequal full alignment lengths')
    ncol = lengths.pop()
    keep = [i for i in range(ncol) if sum(s[i] == '-' for s in full.values()) / len(full) <= max_gap]
    if not keep:  # Reproduce the historical builder's empty-mask fallback.
        keep = list(range(ncol))
    if any(''.join(seq[i] for i in keep) != trimmed[sp] for sp, seq in full.items()):
        raise ValueError('Trimmed alignment does not match reconstructed gap mask')
    threaded = {sp: thread_cds(full[sp], cds[sp]) for sp in FOCAL}
    out, retained = {sp: [] for sp in FOCAL}, []
    bad_gap = bad_codon = 0
    for i in keep:
        pair = {sp: threaded[sp][3*i:3*i+3] for sp in FOCAL}
        if any('-' in c for c in pair.values()):
            bad_gap += 1
        elif any(len(c) != 3 or set(c) - set('ACGT') or c in STOPS for c in pair.values()):
            bad_codon += 1
        else:
            retained.append(i + 1)
            for sp, c in pair.items():
                out[sp].append(c)
    sequences = {sp: ''.join(codons) for sp, codons in out.items()}
    for sp in FOCAL:
        expected = ''.join(full[sp][i - 1] for i in retained)
        if str(Seq(sequences[sp]).translate()) != expected:
            raise ValueError('Final codon alignment fails translation invariant')
    qc = {'raw_columns': ncol, 'trimmed_columns': len(keep),
          'removed_pair_gap_columns': bad_gap, 'removed_invalid_codons': bad_codon,
          'kept_columns_1based': retained, 'codons': len(retained),
          'protein_identity': sum(full['Vper'][i-1] == full['Vtub'][i-1] for i in retained) / len(retained) if retained else None}
    return sequences, qc


def parse_yn00_output(txt):
    """Parse section B, keeping SEs and boundaries; NEVER switch estimators."""
    if '(B)' not in txt:
        raise ValueError('Missing Yang-Nielsen section; no fallback allowed')
    section = txt.split('(B)', 1)[1].split('(C)', 1)[0]
    for line in section.splitlines():
        fields = line.replace('+-', ' ').split()
        if len(fields) == 11 and fields[:2] == ['2', '1']:
            return dict(zip(('S_sites', 'N_sites', 't', 'kappa', 'omega', 'dN', 'dN_SE', 'dS', 'dS_SE'), map(float, fields[2:])))
    raise ValueError('Missing/invalid Yang-Nielsen estimate row')


def classify_estimate(estimate, max_ds=2.0):
    flags = []
    if not all(math.isfinite(estimate[k]) for k in ('dN', 'dS', 'omega', 'dN_SE', 'dS_SE')):
        return 'NONFINITE_ESTIMATE', 'not_interpretable', flags
    if estimate['dS'] <= 0:
        return 'ZERO_OR_NEGATIVE_DS', 'not_interpretable', flags
    if any(estimate[k] < 0 for k in ('dN', 'omega', 'dN_SE', 'dS_SE')):
        return 'INVALID_ESTIMATE', 'not_interpretable', flags
    if estimate['omega'] >= 99:
        return 'OMEGA_BOUNDARY', 'not_interpretable', flags
    if estimate['dS'] >= max_ds:
        return 'HIGH_DS', 'not_interpretable', flags
    if estimate['dS'] <= estimate['dS_SE']:
        flags.append('DS_SE_GE_DS')
    if estimate['dS'] < 0.01:
        flags.append('LOW_DS_LT_0.01')
    if estimate['dN'] >= 2:
        flags.append('HIGH_DN_GE_2')
    screen = 'omega_gt_1' if estimate['omega'] > 1 else 'omega_lt_1' if estimate['omega'] < 1 else 'omega_eq_1'
    return 'PASS', screen, flags


def sha256(path):
    digest = hashlib.sha256()
    with open(path, 'rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def write_tsv(path, rows, fields):
    with open(path, 'w') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t', extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)


def run_yn00(task):
    directory, executable, timeout = task
    try:
        completed = subprocess.run([executable, 'yn00.ctl'], cwd=directory,
            capture_output=True, text=True, timeout=timeout, stdin=subprocess.DEVNULL)
        (directory / 'stdout.log').write_text(completed.stdout)
        (directory / 'stderr.log').write_text(completed.stderr)
        if completed.returncode:
            raise ValueError(f'YN00 return code {completed.returncode}')
        raw = (directory / 'yn00.out').read_text()
        version = next((line for line in completed.stdout.splitlines() if 'paml version' in line), 'UNKNOWN')
        return directory.name, parse_yn00_output(raw), '', version
    except (ValueError, OSError, subprocess.TimeoutExpired) as exc:
        return directory.name, None, str(exc), ''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-dir', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--output-dir', type=Path, required=True, help='Must not already exist')
    parser.add_argument('--orthofinder-dir', type=Path)
    parser.add_argument('--yn00', default=str(Path.home() / '.local/bin/yn00'))
    parser.add_argument('--threads', type=int, default=4)
    parser.add_argument('--min-codons', type=int, default=30)
    parser.add_argument('--max-ds', type=float, default=2.0)
    parser.add_argument('--timeout', type=int, default=120)
    parser.add_argument('--only', nargs='+', help='Optional pilot orthogroup IDs')
    args = parser.parse_args()
    if args.threads < 1 or args.min_codons < 1 or args.max_ds <= 0:
        parser.error('threads, min-codons and max-ds must be positive')
    base = args.base_dir.resolve()
    executable = shutil.which(args.yn00)
    if not executable:
        parser.error('yn00 executable not found')
    executable = str(Path(executable).resolve())
    ofdirs = sorted((base / '01_orthology/results').glob('Results_*'))
    if args.orthofinder_dir:
        ofdir = args.orthofinder_dir.resolve()
    elif len(ofdirs) == 1:
        ofdir = ofdirs[0]
    else:
        parser.error('Specify --orthofinder-dir when zero or multiple results exist')
    legacy_path = base / '05_selection/vellozia_pairwise_kaks_annotated.tsv'
    with legacy_path.open() as stream:
        old = {r['Orthogroup']: r for r in csv.DictReader(stream, delimiter='\t')}
    ids = sorted(args.only or old)
    if not ids or set(ids) - old.keys():
        parser.error('IDs must belong to the historical 1:1 analysis')
    out = args.output_dir.resolve()
    out.mkdir(parents=True, exist_ok=False)
    work, provenance = out / 'work', out / 'provenance'
    work.mkdir()
    provenance.mkdir()
    shutil.copy2(__file__, provenance / Path(__file__).name)
    shutil.copy2(legacy_path, provenance / legacy_path.name)
    cds_paths = {sp: base.parent / f'data/genomes/{sp}/{sp}.hapA.v1.softmasked.cds.fasta' for sp in FOCAL}
    cds = {sp: parse_fasta(path) for sp, path in cds_paths.items()}
    manifest = {'started_utc': datetime.now(timezone.utc).isoformat(), 'command': sys.argv,
        'python': sys.version, 'biopython': Bio.__version__, 'yn00_executable': executable,
        'yn00_sha256': sha256(executable), 'status': 'running', 'orthogroups': ids,
        'orthofinder_dir': str(ofdir),
        'parameters': {'min_codons': args.min_codons, 'max_ds': args.max_ds, 'max_gap_fraction': 0.5,
                       'threads': args.threads, 'timeout': args.timeout, 'genetic_code': 1,
                       'weighting': 0, 'commonf3x4': 0, 'icode': 0},
        'inputs': {str(p): sha256(p) for p in [*cds_paths.values(), legacy_path, Path(__file__)]}}
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2))
    rows, tasks, hashes = {}, [], []
    ctl = 'seqfile = seq.phy\noutfile = yn00.out\nverbose = 0\nicode = 0\nweighting = 0\ncommonf3x4 = 0\n'
    for og in ids:
        previous = old[og]
        row = {k: previous[k] for k in ('Orthogroup', 'Vtub_Gene', 'Vper_Gene', 'Ath_Gene', 'Functional_Description')}
        row.update(QC_Status='INPUT_FAILURE', Screen='not_interpretable', Flags='', Error='')
        rows[og] = row
        directory = work / og
        directory.mkdir()
        try:
            paths = [base / f'02_phylogenomics/gene_alignments/{og}_aligned.fa',
                     base / f'02_phylogenomics/trimmed_alignments/{og}_trimmed.fa',
                     ofdir / f'Single_Copy_Orthologue_Sequences/{og}.fa']
            full, trimmed, proteins = (parse_fasta(p) for p in paths)
            if len(full) != 7 or len(proteins) != 7:
                raise ValueError('Expected seven taxa in single-copy orthogroup and alignment')
            pair_cds = {}
            for sp in FOCAL:
                gene = previous[f'{sp}_Gene']
                matches = [key for key in proteins if key.startswith(sp)]
                if matches != [gene]:
                    raise ValueError(f'Unexpected focal orthogroup IDs: {sp}: {matches}')
                if proteins[gene].removesuffix('*') != full[sp].replace('-', '').removesuffix('*'):
                    raise ValueError(f'Full alignment differs from OrthoFinder protein: {sp}')
                pair_cds[sp] = cds[sp][gene]  # Exact transcript ID; never collapse isoforms.
            sequences, qc = prepare_pair(full, trimmed, pair_cds)
            row.update(Codons=qc['codons'], Raw_AA_Columns=qc['raw_columns'],
                Trimmed_AA_Columns=qc['trimmed_columns'], Protein_Identity=qc['protein_identity'],
                Removed_Pair_Gaps=qc['removed_pair_gap_columns'], Removed_Invalid_Codons=qc['removed_invalid_codons'])
            (directory / 'alignment_qc.json').write_text(json.dumps(qc, indent=2))
            (directory / 'focal_cds.fa').write_text(''.join(f'>{previous[sp+"_Gene"]}\n{pair_cds[sp]}\n' for sp in FOCAL))
            for path in paths:
                hashes.append({'Orthogroup': og, 'Path': str(path), 'SHA256': sha256(path)})
                shutil.copy2(path, directory / path.name)
            if qc['codons'] < args.min_codons:
                row['QC_Status'] = 'TOO_SHORT'
                continue
            (directory / 'seq.phy').write_text(f'2 {qc["codons"] * 3}\n' +
                ''.join(f'{sp}      {sequences[sp]}\n' for sp in FOCAL))
            (directory / 'yn00.ctl').write_text(ctl)
            tasks.append((directory, executable, args.timeout))
            row['QC_Status'] = 'PENDING'
        except (ValueError, KeyError, OSError) as exc:
            row['Error'] = str(exc)
            (directory / 'input_error.txt').write_text(str(exc))
    write_tsv(out / 'input_checksums.tsv', hashes, ['Orthogroup', 'Path', 'SHA256'])
    print(f'Validated {len(tasks)}/{len(ids)} codon alignments; starting YN00', flush=True)
    versions = set()
    with ThreadPoolExecutor(max_workers=args.threads) as pool:
        futures = [pool.submit(run_yn00, task) for task in tasks]
        for count, future in enumerate(as_completed(futures), 1):
            og, estimate, error, version = future.result()
            row = rows[og]
            if estimate is None:
                row.update(QC_Status='YN00_FAILURE', Error=error)
            else:
                versions.add(version)
                status, screen, flags = classify_estimate(estimate, args.max_ds)
                row.update(Ka_dN=estimate['dN'], Ks_dS=estimate['dS'], Omega_KaKs=estimate['omega'],
                    dN_SE=estimate['dN_SE'], dS_SE=estimate['dS_SE'], Kappa=estimate['kappa'],
                    S_sites=estimate['S_sites'], N_sites=estimate['N_sites'],
                    QC_Status=status, Screen=screen, Flags=';'.join(flags))
            if count % 100 == 0 or count == len(tasks):
                print(f'YN00 complete {count}/{len(tasks)}', flush=True)
    all_rows = [rows[og] for og in ids]
    fields = ['Orthogroup', 'Vtub_Gene', 'Vper_Gene', 'Ath_Gene', 'Codons', 'Ka_dN', 'Ks_dS',
        'Omega_KaKs', 'dN_SE', 'dS_SE', 'Kappa', 'S_sites', 'N_sites', 'QC_Status', 'Screen',
        'Flags', 'Raw_AA_Columns', 'Trimmed_AA_Columns', 'Protein_Identity', 'Removed_Pair_Gaps',
        'Removed_Invalid_Codons', 'Functional_Description', 'Error']
    candidates = sorted([r for r in all_rows if r['QC_Status'] == 'PASS' and r['Screen'] == 'omega_gt_1'],
                        key=lambda r: r['Omega_KaKs'], reverse=True)
    write_tsv(out / 'pairwise_kaks_all.tsv', all_rows, fields)
    write_tsv(out / 'omega_gt1_screen.tsv', candidates, fields)
    comparisons = []
    for r in all_rows:
        previous = old[r['Orthogroup']]
        comparisons.append({'Orthogroup': r['Orthogroup'], 'Old_omega': previous['Omega_KaKs'],
            'New_omega': r.get('Omega_KaKs', ''), 'Old_dN': previous['Ka_dN'], 'New_dN': r.get('Ka_dN', ''),
            'Old_dS': previous['Ks_dS'], 'New_dS': r.get('Ks_dS', ''),
            'Old_candidate': previous['Selection_Regime'] == 'Positive_Selection',
            'New_candidate': r['Screen'] == 'omega_gt_1', 'QC_Status': r['QC_Status'],
            'Functional_Description': r['Functional_Description']})
    write_tsv(out / 'comparison_with_legacy.tsv', comparisons, list(comparisons[0]))
    passed = [r for r in all_rows if r['QC_Status'] == 'PASS']
    summary = {'orthogroups': len(ids), 'validated_alignments': len(tasks),
        'qc_counts': dict(Counter(r['QC_Status'] for r in all_rows)),
        'screen_counts': dict(Counter(r['Screen'] for r in all_rows)), 'omega_gt1_count': len(candidates),
        'old_candidates': sum(r['Old_candidate'] for r in comparisons),
        'old_candidates_retained': sum(r['Old_candidate'] and r['New_candidate'] for r in comparisons),
        'medians_qc_pass': {k: statistics.median(r[k] for r in passed) if passed else None
                            for k in ('Ka_dN', 'Ks_dS', 'Omega_KaKs')},
        'yn00_version_headers': sorted(versions),
        'interpretation': 'Descriptive pairwise screen only; no p-values, FDR or lineage-specific selection inference.'}
    (out / 'summary.json').write_text(json.dumps(summary, indent=2))
    manifest.update(status='complete', completed_utc=datetime.now(timezone.utc).isoformat(),
                    yn00_version_headers=sorted(versions))
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2))
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == '__main__':
    main()
