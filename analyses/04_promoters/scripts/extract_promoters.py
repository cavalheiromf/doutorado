#!/usr/bin/env python3
"""
Extract 2000bp upstream regions (promoters) for OSCA genes.
"""

import os
import subprocess
from pathlib import Path

# --- Project Paths ---
PROJECT_ROOT = Path("/home/mfcaval/github/doutorado")
DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "analyses" / "04_promoters" / "results"
OSCA_IDS_FILE = PROJECT_ROOT / "analyses" / "01_gene_identification" / "results" / "oscasIDs.txt"

RESULTS_DIR.mkdir(parents=True, exist_ok=True)

def extract_coords(species):
    gff_file = DATA_DIR / "genomes" / species / (f"{species}.hapA.v1.softmasked.gff3" if species == "Vper" else f"Vtub.hapA.v1.softmasked.gff3")
    
    # Load target IDs for this species
    targets = []
    with open(OSCA_IDS_FILE) as f:
        for line in f:
            parts = line.strip().split()
            if parts and parts[0].startswith(species):
                targets.append(parts[0])
    
    # Extract BED coords from GFF
    bed_data = []
    with open(gff_file) as f:
        for line in f:
            if line.startswith("#"): continue
            parts = line.strip().split("\t")
            if len(parts) < 9: continue
            
            if parts[2] == "mRNA":
                attr = parts[8]
                for target in targets:
                    if f"ID={target}" in attr or f"Parent={target}" in attr:
                        chrom = parts[0]
                        start = int(parts[3]) - 1 # 0-indexed
                        end = int(parts[4])
                        strand = parts[6]
                        bed_data.append(f"{chrom}\t{start}\t{end}\t{target}\t.\t{strand}")
                        break
    
    bed_file = RESULTS_DIR / f"{species}.osca.coords.bed"
    with open(bed_file, "w") as f:
        f.write("\n".join(bed_data) + "\n")
    return bed_file

def get_promoters(species, bed_file):
    chrom_sizes = DATA_DIR / "genomes" / species / "chrom.sizes"
    genome_fa = DATA_DIR / "genomes" / species / (f"{species}.hapA.v1.softmasked.fasta" if species == "Vper" else f"Vtub.hapA.v1.softmasked.fasta")
    promoter_bed = RESULTS_DIR / f"{species}.promoters.2k.bed"
    promoter_fa = RESULTS_DIR / f"{species}.promoters.2k.fasta"
    
    # Step 1: Get 2000bp upstream using bedtools flank
    # Note: Using bedtools directly as it is in the path
    flank_cmd = f"bedtools flank -i {bed_file} -g {chrom_sizes} -l 2000 -r 0 -s > {promoter_bed}"
    subprocess.run(flank_cmd, shell=True, check=True)
    
    # Step 2: Extract FASTA
    fasta_cmd = f"bedtools getfasta -fi {genome_fa} -bed {promoter_bed} -fo {promoter_fa} -s -name"
    subprocess.run(fasta_cmd, shell=True, check=True)
    
    print(f"✅ Generated: {promoter_fa}")

if __name__ == "__main__":
    for sp in ["Vper", "Vtub"]:
        print(f"Processing {sp}...")
        bf = extract_coords(sp)
        get_promoters(sp, bf)
