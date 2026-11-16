#!/usr/bin/env python3
"""Compare current focal protein inputs to the sequences used by OrthoFinder."""
import argparse,csv,json,hashlib
from pathlib import Path
from Bio import SeqIO


def verify(run):
    manifest=json.loads((run/'manifest.json').read_text())
    def read(path):
        with open(path) as handle: return list(csv.DictReader(handle,delimiter='\t'))
    rows=read(run/'selected_pairs.tsv')
    paths=[Path(p) for p in manifest['inputs']]
    source=next(p for p in paths if p.name=='Vper.pep__v__Vtub.pep.tsv').parents[2]
    proteins={sp:SeqIO.to_dict(SeqIO.parse(next(p for p in paths if p.name==f'{sp}.hapA.v1.softmasked.proteins.fasta'),'fasta')) for sp in ('Vper','Vtub')}
    byog={}
    for r in rows: byog.setdefault(r['Orthogroup'],[]).append(r)
    n=0; differences=[]; hashes=[]
    for og, group in byog.items():
        path=source/f'Orthogroup_Sequences/{og}.fa'
        records=SeqIO.to_dict(SeqIO.parse(path,'fasta'))
        hashes.append({'Orthogroup':og,'Path':str(path),'SHA256':hashlib.sha256(path.read_bytes()).hexdigest()})
        for r in group:
            for sp in ('Vper','Vtub'):
                gene=r[sp+'_Gene']; a=str(records[gene].seq).removesuffix('*'); b=str(proteins[sp][gene].seq).removesuffix('*')
                n+=1
                if a!=b:
                    kind='ORTHOFINDER_X_RESOLVED' if len(a)==len(b) and all(x==y or x=='X' for x,y in zip(a,b)) else 'SEQUENCE_DISAGREEMENT'
                    differences.append({'Pair_ID':r['Pair_ID'],'Orthogroup':og,'Gene':gene,'Status':kind,
                        'OrthoFinder_Length':len(a),'Current_Length':len(b),
                        'Different_Positions_1based':','.join(str(i) for i,(x,y) in enumerate(zip(a,b),1) if x!=y)})
    fields=['Pair_ID','Orthogroup','Gene','Status','OrthoFinder_Length','Current_Length','Different_Positions_1based']
    for filename,data,keys in [('orthofinder_protein_differences.tsv',differences,fields),('orthofinder_sequence_checksums.tsv',hashes,['Orthogroup','Path','SHA256'])]:
        with (run/filename).open('w') as handle:
            w=csv.DictWriter(handle,fieldnames=keys,delimiter='\t'); w.writeheader(); w.writerows(data)
    conflicts=sum(r['Status']=='SEQUENCE_DISAGREEMENT' for r in differences)
    result={'status':'PASS_WITH_DOCUMENTED_X_DIFFERENCES' if differences and not conflicts else 'REVIEW_REQUIRED' if conflicts else 'PASS',
        'protein_sequences_checked':n,'orthogroups_checked':len(byog),'identical_proteins':n-len(differences),
        'orthofinder_x_resolved':sum(r['Status']=='ORTHOFINDER_X_RESOLVED' for r in differences),
        'sequence_disagreements':conflicts}
    (run/'orthofinder_protein_verification.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('run_dir',type=Path)
    verify(parser.parse_args().run_dir.resolve())
