import os
import subprocess
from pathlib import Path
from Bio import SeqIO

# Dynamic paths resolution
SCRIPT_DIR = Path(__file__).resolve().parent
OSCA_DIR = SCRIPT_DIR.parents[1]
PROJECT_ROOT = OSCA_DIR.parent.parent

ID_MAPPING = OSCA_DIR / "01_gene_identification" / "results" / "oscasIDs.txt"
VPER_PROTEINS = PROJECT_ROOT / "data" / "genomes" / "Vper" / "Vper.hapA.v1.softmasked.proteins.fasta"
VPER_CDS = PROJECT_ROOT / "data" / "genomes" / "Vper" / "Vper.hapA.v1.softmasked.cds.fasta"
VTUB_PROTEINS = PROJECT_ROOT / "data" / "genomes" / "Vtub" / "Vtub.hapA.v1.softmasked.proteins.fasta"
VTUB_CDS = PROJECT_ROOT / "data" / "genomes" / "Vtub" / "Vtub.hapA.v1.softmasked.cds.fasta"
OUTPUT_DIR = OSCA_DIR / "04_evolutionary_rates" / "results"

# OSCA Pairs to analyze (VpOSCAx.y, VtOSCAx.y)
pairs = [
    ('VpOSCA1.1', 'VtOSCA1.1'), ('VpOSCA1.2', 'VtOSCA1.2'), ('VpOSCA1.3', 'VtOSCA1.3'),
    ('VpOSCA1.4', 'VtOSCA1.4'), ('VpOSCA1.5', 'VtOSCA1.5'), ('VpOSCA2.1', 'VtOSCA2.1'),
    ('VpOSCA2.2', 'VtOSCA2.2'), ('VpOSCA2.3', 'VtOSCA2.3'), ('VpOSCA2.4a', 'VtOSCA2.4'),
    ('VpOSCA2.4b', 'VtOSCA2.4'), ('VpOSCA2.5', 'VtOSCA2.5'), ('VpOSCA3.1', 'VtOSCA3.1'),
    ('VpOSCA3.2', 'VtOSCA3.2'), ('VpOSCA4.1', 'VtOSCA4.1'), ('VpOSCA2.4a', 'VpOSCA2.4b')
]

def load_mapping(path):
    mapping = {}
    with open(path) as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                mapping[parts[1]] = parts[0]
    return mapping

def extract_sequences(ids, fasta_file):
    seqs = {}
    with open(fasta_file) as f:
        for record in SeqIO.parse(f, "fasta"):
            # Split by space to get just the ID if needed
            rec_id = record.id.split()[0]
            if rec_id in ids:
                seqs[rec_id] = record
    return seqs

def main():
    mapping = load_mapping(ID_MAPPING)
    
    # Collect all needed IDs
    vper_ids = set()
    vtub_ids = set()
    for p1, p2 in pairs:
        if p1.startswith('Vp'): vper_ids.add(mapping.get(p1))
        if p1.startswith('Vt'): vtub_ids.add(mapping.get(p1))
        if p2.startswith('Vp'): vper_ids.add(mapping.get(p2))
        if p2.startswith('Vt'): vtub_ids.add(mapping.get(p2))

    # Remove None if any
    vper_ids.discard(None)
    vtub_ids.discard(None)

    print(f"Extracting {len(vper_ids)} sequences from Vper and {len(vtub_ids)} from Vtub...")
    
    vp_prot = extract_sequences(vper_ids, VPER_PROTEINS)
    vp_cds = extract_sequences(vper_ids, VPER_CDS)
    vt_prot = extract_sequences(vtub_ids, VTUB_PROTEINS)
    vt_cds = extract_sequences(vtub_ids, VTUB_CDS)

    for p1, p2 in pairs:
        id1 = mapping.get(p1)
        id2 = mapping.get(p2)
        
        if not id1 or not id2:
            print(f"Skipping {p1}-{p2}: ID missing")
            continue
            
        pair_name = f"{p1}_{p2}"
        pair_dir = os.path.join(OUTPUT_DIR, pair_name)
        os.makedirs(pair_dir, exist_ok=True)
        
        # Get sequences
        s1_prot = vp_prot.get(id1) if p1.startswith('Vp') else vt_prot.get(id1)
        s1_cds = vp_cds.get(id1) if p1.startswith('Vp') else vt_cds.get(id1)
        s2_prot = vp_prot.get(id2) if p2.startswith('Vp') else vt_prot.get(id2)
        s2_cds = vp_cds.get(id2) if p2.startswith('Vp') else vt_cds.get(id2)

        if not (s1_prot and s2_prot and s1_cds and s2_cds):
            print(f"Skipping {p1}-{p2}: Sequences missing for {id1} or {id2}")
            continue

        # Write fasta files
        prot_file = os.path.join(pair_dir, "pep.faa")
        cds_file = os.path.join(pair_dir, "cds.fna")
        
        SeqIO.write([s1_prot, s2_prot], prot_file, "fasta")
        SeqIO.write([s1_cds, s2_cds], cds_file, "fasta")
        
        print(f"Prepared files for {pair_name}")

if __name__ == "__main__":
    main()
