#!/usr/bin/env python3
"""Independent verification of saved codons, YN00 parsing and input checksums."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
from Bio import SeqIO
from Bio.Phylo.PAML import yn00
from Bio.Seq import Seq


def verify(run):
    rows = list(csv.DictReader((run / 'pairwise_kaks_all.tsv').open(), delimiter='\t'))
    parsed = alignments = 0
    for row in rows:
        directory = run / 'work' / row['Orthogroup']
        if not (directory / 'seq.phy').exists():
            continue
        aln = SeqIO.to_dict(SeqIO.parse(directory / 'seq.phy', 'phylip-sequential'))
        protein = SeqIO.to_dict(SeqIO.parse(directory / f"{row['Orthogroup']}_aligned.fa", 'fasta'))
        cds = SeqIO.to_dict(SeqIO.parse(directory / 'focal_cds.fa', 'fasta'))
        qc = json.loads((directory / 'alignment_qc.json').read_text())
        columns = qc['kept_columns_1based']
        assert len(columns) == int(row['Codons'])
        assert columns == sorted(set(columns))
        for sp in ('Vper', 'Vtub'):
            raw_aa = str(protein[sp].seq)
            dna = str(cds[row[sp + '_Gene']].seq)
            # Map each full alignment column directly to its original CDS offset.
            offset, coordinate_map = 0, {}
            for i, aa in enumerate(raw_aa, 1):
                if aa != '-':
                    coordinate_map[i] = dna[offset:offset + 3]
                    offset += 3
            expected_dna = ''.join(coordinate_map[i] for i in columns)
            observed_dna = str(aln[sp].seq)
            assert observed_dna == expected_dna, (row['Orthogroup'], sp, 'CDS coordinates')
            assert set(observed_dna) <= set('ACGT')
            assert str(Seq(observed_dna).translate()) == ''.join(raw_aa[i-1] for i in columns)
        alignments += 1
        if row['QC_Status'] == 'YN00_FAILURE':
            continue
        independent = yn00.read(str(directory / 'yn00.out'))['Vper']['Vtub']['YN00']
        for column, key in [('Ka_dN', 'dN'), ('Ks_dS', 'dS'), ('Omega_KaKs', 'omega'),
                            ('dN_SE', 'dN SE'), ('dS_SE', 'dS SE')]:
            assert float(row[column]) == independent[key], (row['Orthogroup'], column)
        parsed += 1
    hashes_checked = 0
    for row in csv.DictReader((run / 'input_checksums.tsv').open(), delimiter='\t'):
        assert hashlib.sha256(Path(row['Path']).read_bytes()).hexdigest() == row['SHA256']
        hashes_checked += 1
    result = {'status': 'PASS', 'alignment_coordinate_checks': alignments,
              'independent_biopython_yn00_parses': parsed, 'input_hashes_checked': hashes_checked}
    (run / 'independent_verification.json').write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run_dir', type=Path)
    args = parser.parse_args()
    verify(args.run_dir.resolve())
