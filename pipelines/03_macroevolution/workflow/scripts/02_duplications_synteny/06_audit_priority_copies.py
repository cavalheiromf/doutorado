#!/usr/bin/env python3
"""Audit copies without changing counts. All paths are explicit and cwd-relative.

CLI: --gene-evidence FILE --run-dir DIR [--families OG1,OG2]
     [--proteins Species=FASTA ...] [--cds Species=FASTA ...]
     [--support TSV]
Support TSV: Species, GeneID, Domain_Evidence, Coverage_Evidence,
Expression_Evidence, Organelle_Homology, Genomic_Context. Values are retained
as supplied evidence, never interpreted as proof of artifact or absence.
Each invocation creates copy_qc/<UTC timestamp + random suffix>/.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone
import uuid


def read_table(path):
    with Path(path).open(newline='') as handle:
        return list(csv.DictReader(handle, delimiter='\t'))


def fasta(path):
    records = {}
    current = None
    with Path(path).open() as handle:
        for line in handle:
            line = line.strip()
            if line.startswith('>'):
                current = line[1:].split()[0]
                if current in records:
                    raise ValueError(f'Duplicate FASTA ID: {current}')
                records[current] = ''
            elif line:
                if current is None:
                    raise ValueError('Sequence before FASTA header')
                records[current] += line.upper()
    return records


def translate(sequence):
    # Standard nuclear genetic code; organellar translation requires separate review.
    bases = 'TCAG'
    amino = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    code = dict(zip((a+b+c for a in bases for b in bases for c in bases), amino))
    return ''.join(code.get(sequence[i:i+3], 'X') for i in range(0, len(sequence)-2, 3))


def without_terminal_stop(sequence):
    return sequence[:-1] if sequence.endswith('*') else sequence


def sequence_qc(cds, protein):
    result = {'CDS_Length': '', 'Protein_Length': '', 'CDS_Ambiguous_Bases': '',
              'Protein_Ambiguous_Residues': '', 'Internal_Stops': '',
              'Translation_Match': 'not_assessed', 'CDS_Integrity': 'not_assessed',
              'Protein_Integrity': 'not_assessed'}
    if cds is not None:
        translated = translate(cds)
        stops = without_terminal_stop(translated).count('*')
        ambiguous = sum(x not in 'ACGT' for x in cds)
        flags = []
        if len(cds) % 3: flags.append('frame_length')
        if not cds.startswith('ATG'): flags.append('start_not_ATG')
        if not translated.endswith('*'): flags.append('terminal_stop_missing')
        if stops: flags.append('internal_stop')
        if ambiguous: flags.append('ambiguous_bases')
        result.update(CDS_Length=len(cds), CDS_Ambiguous_Bases=ambiguous,
                      Internal_Stops=stops, CDS_Integrity=';'.join(flags) or 'standard_code_complete')
        if protein is not None:
            result['Translation_Match'] = 'match' if without_terminal_stop(translated) == without_terminal_stop(protein) else 'mismatch'
    if protein is not None:
        ambiguous = sum(x not in 'ACDEFGHIKLMNPQRSTVWY*' for x in protein)
        flags = []
        if without_terminal_stop(protein).count('*'): flags.append('internal_stop')
        if ambiguous: flags.append('ambiguous_residues')
        if not protein: flags.append('empty')
        result.update(Protein_Length=len(protein), Protein_Ambiguous_Residues=ambiguous,
                      Protein_Integrity=';'.join(flags) or 'sequence_intact_completeness_unknown')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gene-evidence', required=True)
    parser.add_argument('--run-dir', required=True)
    parser.add_argument('--families', help='Comma-separated IDs; default audits all supplied loci')
    parser.add_argument('--proteins', nargs='*', default=[])
    parser.add_argument('--cds', nargs='*', default=[])
    parser.add_argument('--support')
    parser.add_argument('--coordinate-system', choices=['0-based-half-open', '1-based-inclusive'], help='Use only when confirmed from coordinate source')
    args = parser.parse_args()
    rows = read_table(args.gene_evidence)
    required = {'Species', 'GeneID', 'ProteinID', 'TranscriptID', 'FamilyID'}
    if not rows or not required.issubset(rows[0]):
        raise ValueError(f'Gene evidence must contain {sorted(required)}')
    paths = [args.gene_evidence]
    sequences = {}
    for kind in ('proteins', 'cds'):
        sequences[kind] = {}
        for value in getattr(args, kind):
            species, path = value.split('=', 1)
            if species in sequences[kind]: raise ValueError(f'Duplicate species: {species}')
            sequences[kind][species] = fasta(path)
            paths.append(path)
    support = {}
    if args.support:
        paths.append(args.support)
        for row in read_table(args.support):
            key = (row['Species'], row['GeneID'])
            if key in support: raise ValueError(f'Duplicate support locus: {key}')
            support[key] = row
    selected = set(args.families.split(',')) if args.families else None
    seen = set()
    output = []
    evidence_fields = ['Domain_Evidence', 'Coverage_Evidence', 'Expression_Evidence', 'Organelle_Homology', 'Genomic_Context']
    for row in rows:
        if selected is not None and row['FamilyID'] not in selected: continue
        key = (row['Species'], row['GeneID'])
        if key in seen: raise ValueError(f'Duplicate selected locus: {key}; reconcile isoforms first')
        seen.add(key)
        cds = sequences['cds'].get(key[0], {}).get(row['TranscriptID'])
        protein = sequences['proteins'].get(key[0], {}).get(row['ProteinID'])
        item = dict(row)
        measured = sequence_qc(cds, protein)
        for field, value in measured.items():
            if field in ('CDS_Integrity', 'Protein_Integrity'):
                item['Input_' + field] = row.get(field, 'not_assessed')
                if value == 'not_assessed': value = row.get(field) or value
            item[field] = value
        item['CDS_Sequence_Status'] = ('available' if cds is not None else 'id_not_found') if key[0] in sequences['cds'] else 'asset_not_supplied'
        item['Protein_Sequence_Status'] = ('available' if protein is not None else 'id_not_found') if key[0] in sequences['proteins'] else 'asset_not_supplied'
        for field in evidence_fields:
            item[field] = support.get(key, {}).get(field) or row.get(field) or 'not_assessed'
        item['Context_Flag'] = 'review_unplaced' if row.get('Anchoring') == 'unplaced' else 'unknown'
        item['Overlapping_Loci'] = ''
        item['Identical_Protein_Loci'] = ''
        item['Copy_Decision'] = 'retain_pending_review'
        item['Translation_Code'] = 'standard_nuclear_assumption'
        output.append(item)
    if selected is not None:
        missing_families = selected - {row['FamilyID'] for row in output}
        if missing_families:
            raise ValueError(f'Requested priority families absent from gene table: {sorted(missing_families)}')
    for item in output:
        overlaps = []
        convention = args.coordinate_system or item.get('Coordinate_System', 'unknown')
        overlap_assessed = convention in ('0-based-half-open', '1-based-inclusive')
        try:
            a, b = int(item.get('Start', '')), int(item.get('End', ''))
            valid_span = b >= a if convention == '1-based-inclusive' else b > a
            overlap_assessed = overlap_assessed and bool(item.get('Chrom')) and valid_span and a >= (1 if convention == '1-based-inclusive' else 0)
        except (ValueError, TypeError): overlap_assessed = False
        comparisons = 0
        for other in rows:
            if (item['Species'], item['GeneID']) == (other['Species'], other['GeneID']): continue
            if item['Species'] != other['Species'] or item.get('Assembly') != other.get('Assembly'): continue
            if not item.get('Chrom') or item.get('Chrom') != other.get('Chrom'): continue
            if not overlap_assessed: continue
            if (args.coordinate_system or other.get('Coordinate_System', 'unknown')) != convention: continue
            try:
                a, b, c, d = [int(x) for x in (item.get('Start', ''), item.get('End', ''), other.get('Start', ''), other.get('End', ''))]
            except (ValueError, TypeError): continue
            if (d < c if convention == '1-based-inclusive' else d <= c) or c < (1 if convention == '1-based-inclusive' else 0): continue
            comparisons += 1
            overlap = max(a, c) < min(b, d) if convention == '0-based-half-open' else max(a, c) <= min(b, d)
            if overlap: overlaps.append(other['GeneID'])
        item['Overlap_Coordinate_System'] = convention
        item['Overlap_Comparisons'] = comparisons
        item['Overlapping_Loci'] = ';'.join(sorted(set(overlaps))) or ('none_detected_in_assessed_comparisons' if overlap_assessed and comparisons else 'not_assessed')
        proteins = sequences['proteins'].get(item['Species'], {})
        sequence = proteins.get(item['ProteinID'])
        identical = [other['GeneID'] for other in rows if other['Species'] == item['Species'] and other['GeneID'] != item['GeneID'] and sequence and proteins.get(other['ProteinID']) == sequence]
        comparison_rows = [other for other in rows if other['Species'] == item['Species'] and other['GeneID'] != item['GeneID']]
        available = sum(bool(proteins.get(other['ProteinID'])) for other in comparison_rows)
        item['Protein_Comparison_Total'] = len(comparison_rows)
        item['Protein_Comparison_Available'] = available
        item['Identical_Protein_Loci'] = ';'.join(sorted(set(identical))) if identical else ('none_detected' if sequence and comparison_rows and available == len(comparison_rows) else 'not_assessed_or_partial_coverage')
    if not output: raise ValueError('No selected loci')
    directory = Path(args.run_dir) / 'copy_qc' / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '_' + uuid.uuid4().hex[:8])
    directory.mkdir(parents=True, exist_ok=False)
    with (directory / 'copy_evidence.tsv').open('w', newline='') as handle:
        fields = list(dict.fromkeys(k for row in output for k in row))
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter='\t')
        writer.writeheader(); writer.writerows(output)
    manifest = [{'path': str(Path(p).resolve()), 'sha256': hashlib.sha256(Path(p).read_bytes()).hexdigest()} for p in paths]
    (directory / 'manifest.json').write_text(json.dumps({'inputs': manifest, 'arguments': vars(args), 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'counts_changed': False, 'coordinate_convention': args.coordinate_system or 'per_row_explicit_or_unknown'}, indent=2) + '\n')
    print(directory)


if __name__ == '__main__':
    main()
