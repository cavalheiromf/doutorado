#!/usr/bin/env python3
"""Gene-level reciprocal 1:1 orthologs ONLY between Vper and Vtub, then YN00.
Other species' copy numbers are irrelevant to inclusion. Multiple independent
1:1 pairs may belong to the same orthogroup. No significance test is performed.
"""
import argparse
import csv
import json
import shutil
import statistics
import sys
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import Bio
from Bio.Align import PairwiseAligner, substitution_matrices
import calculate_kaks_1to1 as kaks


def genes(cell):
    return [s.strip() for s in cell.split(',') if s.strip()]


def relationship_edges(rows):
    return {(a, b) for r in rows for a in genes(r['Vper.pep']) for b in genes(r['Vtub.pep'])}


def select_pairs(rows):
    left, right = defaultdict(set), defaultdict(set)
    for a, b in relationship_edges(rows):
        left[a].add(b)
        right[b].add(a)
    singleton = set()
    for r in rows:
        a, b = genes(r['Vper.pep']), genes(r['Vtub.pep'])
        if len(a) == len(b) == 1:
            singleton.add((r['Orthogroup'], a[0], b[0]))
    accepted, rejected = [], []
    for og, a, b in sorted(singleton):
        r = {'Orthogroup': og, 'Vper_Gene': a, 'Vtub_Gene': b,
             'Vper_Degree': len(left[a]), 'Vtub_Degree': len(right[b])}
        if len(left[a]) == len(right[b]) == 1:
            r['Pair_ID'] = f'PAIR{len(accepted)+1:06d}'
            accepted.append(r)
        else:
            r['Reason'] = 'Additional ortholog(s) in the other focal Vellozia species'
            rejected.append(r)
    if len({r['Vper_Gene'] for r in accepted}) != len(accepted) or len({r['Vtub_Gene'] for r in accepted}) != len(accepted):
        raise ValueError('A gene was assigned to multiple accepted pairs/orthogroups')
    return accepted, rejected


def align_proteins(a, b):
    aligner = PairwiseAligner(mode='global')
    aligner.substitution_matrix = substitution_matrices.load('BLOSUM62')
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    alignment = aligner.align(a, b)[0]
    return {'Vper': alignment[0], 'Vtub': alignment[1]}, alignment.score, aligner.algorithm


def calculate(task):
    row, protein, cds, out, executable, min_codons, max_ds = task
    row = dict(row)
    directory = out / 'work' / row['Pair_ID']
    directory.mkdir()
    row.update(QC_Status='INPUT_FAILURE', Screen='not_interpretable', Flags='', Error='')
    try:
        for sp in kaks.FOCAL:
            # Validate the input itself before any alignment or trimming.
            kaks.thread_cds(protein[sp], cds[sp])
        (directory/'proteins.fa').write_text(''.join(f'>{sp}\n{protein[sp]}\n' for sp in kaks.FOCAL))
        (directory/'cds.fa').write_text(''.join(f'>{sp}\n{cds[sp]}\n' for sp in kaks.FOCAL))
        full, score, algorithm = align_proteins(protein['Vper'], protein['Vtub'])
        # With two taxa, the 50% mask retains all single-gap columns; paired
        # complete deletion then removes those codons. No seven-species mask.
        sequences, qc = kaks.prepare_pair(full, full, cds)
        qc.update(alignment_score=score, alignment_algorithm=algorithm)
        (directory/'protein_alignment.fa').write_text(''.join(f'>{sp}\n{full[sp]}\n' for sp in kaks.FOCAL))
        (directory/'alignment_qc.json').write_text(json.dumps(qc, indent=2))
        row.update(Codons=qc['codons'], Protein_Identity=qc['protein_identity'],
            Vper_Length=len(protein['Vper']), Vtub_Length=len(protein['Vtub']),
            Vper_Coverage=qc['codons']/len(protein['Vper']), Vtub_Coverage=qc['codons']/len(protein['Vtub']),
            Removed_Pair_Gaps=qc['removed_pair_gap_columns'], Removed_Invalid_Codons=qc['removed_invalid_codons'])
        if qc['codons'] < min_codons:
            row['QC_Status'] = 'TOO_SHORT'
            return row
        (directory/'seq.phy').write_text(f'2 {qc["codons"]*3}\n'+''.join(f'{sp}      {sequences[sp]}\n' for sp in kaks.FOCAL))
        (directory/'yn00.ctl').write_text('seqfile = seq.phy\noutfile = yn00.out\nverbose = 0\nicode = 0\nweighting = 0\ncommonf3x4 = 0\n')
        _, estimate, error, version = kaks.run_yn00((directory, executable, 120))
        if estimate is None:
            row.update(QC_Status='YN00_FAILURE', Error=error)
        else:
            status, screen, flags = kaks.classify_estimate(estimate, max_ds)
            if row['Protein_Identity'] < 0.7:
                flags.append('PROTEIN_IDENTITY_LT_0.7')
            if min(row['Vper_Coverage'], row['Vtub_Coverage']) < 0.7:
                flags.append('COVERAGE_LT_0.7')
            row.update(QC_Status=status, Screen=screen, Flags=';'.join(flags), YN00_Version=version,
                Ka_dN=estimate['dN'], Ks_dS=estimate['dS'], Omega_KaKs=estimate['omega'],
                dN_SE=estimate['dN_SE'], dS_SE=estimate['dS_SE'], Kappa=estimate['kappa'])
    except (ValueError, KeyError, OSError) as exc:
        row['Error'] = str(exc)
        (directory/'input_error.txt').write_text(str(exc))
    (directory/'result.json').write_text(json.dumps(row, indent=2))
    return row


def read_rows(path):
    with open(path) as handle:
        return list(csv.DictReader(handle, delimiter='\t'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--threads', type=int, default=4)
    parser.add_argument('--min-codons', type=int, default=30)
    parser.add_argument('--max-ds', type=float, default=2)
    parser.add_argument('--only', nargs='+', help='Pilot Pair_IDs or Vper transcript IDs')
    parser.add_argument('--base-dir', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--yn00', default=str(Path.home()/'.local/bin/yn00'))
    args = parser.parse_args()
    if args.threads < 1 or args.min_codons < 1 or args.max_ds <= 0:
        parser.error('Positive threads, min-codons and max-ds required')
    executable = shutil.which(args.yn00)
    if not executable:
        parser.error('YN00 not found')
    executable = str(Path(executable).resolve())
    base = args.base_dir.resolve()
    orthodir = base/'01_orthology/results/Results_Aug30'
    forward = orthodir/'Orthologues/Orthologues_Vper.pep/Vper.pep__v__Vtub.pep.tsv'
    reverse = orthodir/'Orthologues/Orthologues_Vtub.pep/Vtub.pep__v__Vper.pep.tsv'
    orthorows = read_rows(forward)
    if relationship_edges(orthorows) != relationship_edges(read_rows(reverse)):
        raise ValueError('Forward and reverse OrthoFinder relationships differ')
    all_pairs, rejected = select_pairs(orthorows)
    pairs = [r for r in all_pairs if not args.only or r['Pair_ID'] in args.only or r['Vper_Gene'] in args.only]
    if not pairs:
        parser.error('No pairs selected')
    out = args.output_dir.resolve()
    out.mkdir(parents=True, exist_ok=False)
    (out/'work').mkdir()
    provenance = out/'provenance'
    provenance.mkdir()
    paths = [forward, reverse, Path(__file__).resolve(), Path(kaks.__file__).resolve()]
    for path in paths:
        shutil.copy2(path, provenance/path.name)
    old_path = base/'05_selection/corrected_2026-09-10/pairwise_kaks_all.tsv'
    if old_path.is_file():
        old = {(r['Vper_Gene'],r['Vtub_Gene']):r for r in read_rows(old_path)}
        paths.append(old_path)
        shutil.copy2(old_path, provenance/'seven_taxon_subset.tsv')
    else:
        old = {}
    proteins, cds, annotations = {}, {}, {}
    for sp in kaks.FOCAL:
        directory = base.parent/f'data/genomes/{sp}'
        pp = directory/f'{sp}.hapA.v1.softmasked.proteins.fasta'
        cp = directory/f'{sp}.hapA.v1.softmasked.cds.fasta'
        ap = directory/f'{sp.lower()}_master_annotation.tsv'
        paths.extend([pp, cp, ap])
        proteins[sp] = kaks.parse_fasta(pp)
        cds[sp] = kaks.parse_fasta(cp)
        annotations[sp] = {r['transcript_id']:r['eggnog_desc'] for r in read_rows(ap)}
    for r in pairs:
        for sp in kaks.FOCAL:
            if r[sp+'_Gene'] not in proteins[sp] or r[sp+'_Gene'] not in cds[sp]:
                raise ValueError(f'Missing exact transcript in protein/CDS: {r[sp+"_Gene"]}')
            desc = annotations[sp].get(r[sp+'_Gene'], '')
            r[sp+'_Description'] = desc
        r['Functional_Description'] = next((r[sp+'_Description'] for sp in kaks.FOCAL
            if r[sp+'_Description'] not in ('', 'None', 'NA', 'nan')), 'Uncharacterized protein')
        r['In_Seven_Taxon_Subset'] = (r['Vper_Gene'],r['Vtub_Gene']) in old
    pairfields = ['Pair_ID','Orthogroup','Vper_Gene','Vtub_Gene','Vper_Degree','Vtub_Degree',
                  'In_Seven_Taxon_Subset','Vper_Description','Vtub_Description','Functional_Description']
    kaks.write_tsv(out/'selected_pairs.tsv', pairs, pairfields)
    kaks.write_tsv(out/'excluded_nonunique_singleton_rows.tsv', rejected,
        ['Orthogroup','Vper_Gene','Vtub_Gene','Vper_Degree','Vtub_Degree','Reason'])
    manifest = {'started_utc':datetime.now(timezone.utc).isoformat(),'status':'running','command':sys.argv,
        'python':sys.version,'biopython':Bio.__version__,'yn00_executable':executable,
        'yn00_sha256':kaks.sha256(executable),'inputs':{str(p):kaks.sha256(p) for p in paths},
        'criteria':'Exactly one partner in each focal species across all Vper-Vtub relationships; other species unconstrained',
        'parameters':{'protein_alignment':'Gotoh global','matrix':'BLOSUM62','gap_open':-10,'gap_extend':-0.5,
            'terminal_gaps':'same affine penalties','optimal_alignment_tie':'first deterministic alignment',
            'min_codons':args.min_codons,'max_ds':args.max_ds,'threads':args.threads,
            'weighting':0,'commonf3x4':0,'icode':0,'timeout_seconds_per_yn00':120},
        'orthology_counts':{'source_rows':len(orthorows),'unique_singleton_rows':len(all_pairs)+len(rejected),
            'strict_pairs':len(all_pairs),'excluded_nonunique_singletons':len(rejected),
            'distinct_orthogroups':len({r['Orthogroup'] for r in all_pairs})}}
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2))
    print(f'Selected {len(pairs)} reciprocal focal 1:1 pairs; starting alignment and YN00',flush=True)
    results=[]
    with ThreadPoolExecutor(max_workers=args.threads) as pool:
        futures=[]
        for r in pairs:
            aa={sp:proteins[sp][r[sp+'_Gene']].removesuffix('*') for sp in kaks.FOCAL}
            dna={sp:cds[sp][r[sp+'_Gene']] for sp in kaks.FOCAL}
            futures.append(pool.submit(calculate,(r,aa,dna,out,executable,args.min_codons,args.max_ds)))
        for count,future in enumerate(as_completed(futures),1):
            results.append(future.result())
            if count%500==0 or count==len(futures):
                print(f'Finished {count}/{len(futures)} pairs',flush=True)
    results.sort(key=lambda r:r['Pair_ID'])
    fields=pairfields+['Codons','Ka_dN','Ks_dS','Omega_KaKs','dN_SE','dS_SE','Kappa','QC_Status','Screen','Flags',
        'Protein_Identity','Vper_Length','Vtub_Length','Vper_Coverage','Vtub_Coverage',
        'Removed_Pair_Gaps','Removed_Invalid_Codons','YN00_Version','Error']
    passed=[r for r in results if r['QC_Status']=='PASS']
    candidates=sorted([r for r in passed if r['Screen']=='omega_gt_1'],key=lambda r:r['Omega_KaKs'],reverse=True)
    kaks.write_tsv(out/'pairwise_kaks_all.tsv',results,fields)
    kaks.write_tsv(out/'omega_gt1_screen.tsv',candidates,fields)
    comparisons=[]
    for r in results:
        previous=old.get((r['Vper_Gene'],r['Vtub_Gene']))
        if previous:
            comparisons.append({'Pair_ID':r['Pair_ID'],'Orthogroup':r['Orthogroup'],
                'SevenTaxon_omega':previous['Omega_KaKs'],'Pairwise_omega':r.get('Omega_KaKs',''),
                'SevenTaxon_Codons':previous['Codons'],'Pairwise_Codons':r.get('Codons',''),
                'SevenTaxon_Screen':previous['Screen'],'Pairwise_Screen':r['Screen'],'QC_Status':r['QC_Status']})
    kaks.write_tsv(out/'comparison_1513.tsv',comparisons,
        ['Pair_ID','Orthogroup','SevenTaxon_omega','Pairwise_omega','SevenTaxon_Codons','Pairwise_Codons','SevenTaxon_Screen','Pairwise_Screen','QC_Status'])
    ppr=[r for r in results if any(s in (r['Vper_Description']+' '+r['Vtub_Description']).lower() for s in ('ppr','pentatricopeptide'))]
    summary={'pairs':len(results),'distinct_orthogroups':len({r['Orthogroup'] for r in results}),
        'qc_counts':dict(Counter(r['QC_Status'] for r in results)),
        'screen_counts':dict(Counter(r['Screen'] for r in results)), 'omega_gt1_count':len(candidates),
        'omega_gt1_without_flags':sum(not r['Flags'] for r in candidates),
        'previous_subset_overlap':len(comparisons),
        'previous_subset_omega_gt1_now':sum(r['Pairwise_Screen']=='omega_gt_1' for r in comparisons),
        'previous_subset_candidates_retained':sum(r['SevenTaxon_Screen']==r['Pairwise_Screen']=='omega_gt_1' for r in comparisons),
        'ppr_annotation_pairs':len(ppr),'ppr_omega_gt1':sum(r['Screen']=='omega_gt_1' for r in ppr),
        'medians_qc_pass':{key:statistics.median(r[key] for r in passed) if passed else None for key in ('Ka_dN','Ks_dS','Omega_KaKs')},
        'yn00_versions':sorted({r['YN00_Version'] for r in results if r.get('YN00_Version')}),
        'interpretation':'Descriptive screen only, no p-values or lineage-specific positive selection test'}
    (out/'summary.json').write_text(json.dumps(summary,indent=2))
    manifest.update(status='complete',completed_utc=datetime.now(timezone.utc).isoformat())
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2))
    print(json.dumps(summary,indent=2),flush=True)


if __name__=='__main__':
    main()
