#!/usr/bin/env python3
"""
Extract 2000bp upstream regions (promoters) for OSCA genes.
"""

import subprocess
from pathlib import Path

# --- Project Paths ---
SCRIPT_DIR = Path(__file__).resolve().parent
OSCA_DIR = SCRIPT_DIR.parents[1]
PROJECT_ROOT = OSCA_DIR.parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = OSCA_DIR / "04_promoters" / "results"
OSCA_IDS_FILE = OSCA_DIR / "01_gene_identification" / "results" / "oscasIDs.txt"

RESULTS_DIR.mkdir(parents=True, exist_ok=True)

def load_mapping(species):
    mapping = {}
    with open(OSCA_IDS_FILE) as f:
        for line in f:
            parts = line.strip().split()
            if parts and parts[0].startswith(species):
                if len(parts) != 2:
                    raise ValueError(f"Invalid mapping line: {line.rstrip()}")
                mapping[parts[0]] = parts[1]
    expected = 14 if species == "Vper" else 13
    if len(mapping) != expected or len(set(mapping.values())) != expected:
        raise ValueError(f"Expected {expected} unique {species} mappings")
    return mapping


def extract_coords(species):
    gff_file = DATA_DIR / "genomes" / species / f"{species}.hapA.v1.softmasked.gff3"
    mapping = load_mapping(species)
    
    # Extract BED coords from GFF
    bed_data = []
    with open(gff_file) as f:
        for line in f:
            if line.startswith("#"): continue
            parts = line.strip().split("\t")
            if len(parts) < 9: continue
            
            if parts[2] == "mRNA":
                attr = parts[8]
                for target, short_name in mapping.items():
                    if f"ID={target}" in attr or f"Parent={target}" in attr:
                        chrom = parts[0]
                        start = int(parts[3]) - 1 # 0-indexed
                        end = int(parts[4])
                        strand = parts[6]
                        bed_data.append(f"{chrom}\t{start}\t{end}\t{short_name}\t.\t{strand}")
                        break

    if len(bed_data) != len(mapping):
        raise ValueError(
            f"Expected {len(mapping)} {species} loci in the GFF, found {len(bed_data)}"
        )
    
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


def combine_fastas():
    output = RESULTS_DIR / "allOSCAs.promoters.2k.fasta"
    with output.open("w", encoding="utf-8") as combined:
        for species in ["Vper", "Vtub"]:
            fasta = RESULTS_DIR / f"{species}.promoters.2k.fasta"
            combined.write(fasta.read_text(encoding="utf-8"))
    print(f"✅ Generated: {output}")

if __name__ == "__main__":
    for sp in ["Vper", "Vtub"]:
        print(f"Processing {sp}...")
        bf = extract_coords(sp)
        get_promoters(sp, bf)
    combine_fastas()
