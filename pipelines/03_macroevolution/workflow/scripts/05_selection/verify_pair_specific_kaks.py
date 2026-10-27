#!/usr/bin/env python3
"""Independently verify focal orthology, saved codons, and Biopython YN00 parsing."""
import argparse
import csv
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path
from Bio import SeqIO
from Bio.Phylo.PAML import yn00
from Bio.Seq import Seq


def table(path):
    with open(path) as handle:
        return list(csv.DictReader(handle, delimiter='\t'))


def verify(run):
    manifest = json.loads((run/'manifest.json').read_text())
    source = run/'provenance/Vper.pep__v__Vtub.pep.tsv'
    left, right = defaultdict(set), defaultdict(set)
    for row in table(source):
        for a in row['Vper.pep'].split(', '):
            for b in row['Vtub.pep'].split(', '):
                left[a].add(b)
                right[b].add(a)
    expected={(a,next(iter(bs))) for a,bs in left.items()
              if len(bs)==1 and len(right[next(iter(bs))])==1}
    rows=table(run/'pairwise_kaks_all.tsv')
    selected={(r['Vper_Gene'],r['Vtub_Gene']) for r in rows}
    assert selected <= expected
    if '--only' not in manifest['command']:
        assert selected==expected, 'Selected pairs differ from independent reciprocal graph'
    assert len(selected)==len(rows)==len({r['Pair_ID'] for r in rows})
    assert len({r['Vper_Gene'] for r in rows})==len({r['Vtub_Gene'] for r in rows})==len(rows)
    parsed=aligned=0
    for row in rows:
        directory=run/'work'/row['Pair_ID']
        if not (directory/'seq.phy').exists():
            assert row['QC_Status'] in ('TOO_SHORT','INPUT_FAILURE')
            continue
        aa=SeqIO.to_dict(SeqIO.parse(directory/'protein_alignment.fa','fasta'))
        cds=SeqIO.to_dict(SeqIO.parse(directory/'cds.fa','fasta'))
        proteins=SeqIO.to_dict(SeqIO.parse(directory/'proteins.fa','fasta'))
        dna=SeqIO.to_dict(SeqIO.parse(directory/'seq.phy','phylip-sequential'))
        qc=json.loads((directory/'alignment_qc.json').read_text())
        columns=qc['kept_columns_1based']
        assert len(columns)==int(row['Codons'])
        assert columns==sorted(set(columns))
        for sp in ('Vper','Vtub'):
            full=str(aa[sp].seq)
            original=str(cds[sp].seq)
            assert full.replace('-','')==str(proteins[sp].seq)
            assert str(Seq(original).translate()).removesuffix('*')==full.replace('-','')
            offset=0
            mapping={}
            for i, residue in enumerate(full,1):
                if residue!='-':
                    mapping[i]=original[offset:offset+3]
                    offset+=3
            expected_dna=''.join(mapping[i] for i in columns)
            assert str(dna[sp].seq)==expected_dna
            assert set(expected_dna)<=set('ACGT')
            assert str(Seq(expected_dna).translate())==''.join(full[i-1] for i in columns)
        aligned+=1
        if row['QC_Status']=='YN00_FAILURE':
            continue
        other=yn00.read(str(directory/'yn00.out'))['Vper']['Vtub']['YN00']
        for column,key in [('Ka_dN','dN'),('Ks_dS','dS'),('Omega_KaKs','omega'),('dN_SE','dN SE'),('dS_SE','dS SE')]:
            a,b=float(row[column]),other[key]
            assert a==b or (math.isnan(a) and math.isnan(b)), (row['Pair_ID'],column)
        if row['QC_Status']=='PASS':
            assert float(row['Ks_dS'])>0 and float(row['Ks_dS'])<manifest['parameters']['max_ds']
            assert 0<=float(row['Omega_KaKs'])<99
        parsed+=1
    for path,expected_hash in manifest['inputs'].items():
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==expected_hash, path
    result={'status':'PASS','pairs_with_reciprocal_uniqueness_checked':len(rows),
            'independently_reconstructed_strict_pairs':len(expected),
            'codon_alignments_checked':aligned,'independent_biopython_yn00_parses':parsed,
            'input_hashes_checked':len(manifest['inputs'])}
    (run/'independent_verification.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run_dir',type=Path)
    verify(parser.parse_args().run_dir.resolve())
