#!/usr/bin/env python3
"""
Prepares the BED and CDS fasta files from GFF3 and original fasta,
placing them into the data/ subdirectory for organization.
"""

import os
import shutil

# Define paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYNTENY_DIR = os.path.dirname(SCRIPT_DIR)
PROJECT_DIR = os.path.dirname(os.path.dirname(SYNTENY_DIR))

GFF_VPER = os.path.join(PROJECT_DIR, "data", "genomes", "Vper", "Vper.hapA.v1.softmasked.gff3")
GFF_VTUB = os.path.join(PROJECT_DIR, "data", "genomes", "Vtub", "Vtub.hapA.v1.softmasked.gff3")

CDS_VPER = os.path.join(PROJECT_DIR, "data", "genomes", "Vper", "Vper.hapA.v1.softmasked.cds.fasta")
PROJECT_CDS_VTUB = os.path.join(PROJECT_DIR, "data", "genomes", "Vtub", "Vtub.hapA.v1.softmasked.cds.fasta")

OUT_BED_VPER = os.path.join(SYNTENY_DIR, "data", "Vper.bed")
OUT_BED_VTUB = os.path.join(SYNTENY_DIR, "data", "Vtub.bed")

# For JCVI, CDS files are usually placed in the same folder during indexing
# We'll save them inside data/ to keep things tidy
OUT_CDS_VPER = os.path.join(SYNTENY_DIR, "data", "Vper.cds")
OUT_CDS_VTUB = os.path.join(SYNTENY_DIR, "data", "Vtub.cds")


def gff_to_bed(gff_path, bed_path, prefix):
    """
    Parses GFF3, extracts mRNA features, prefixes chromosomes,
    converts to 0-indexed BED coordinates, and writes output.
    """
    print(f"Parsing {gff_path} -> {bed_path} with prefix '{prefix}'")
    count = 0
    with open(gff_path, "r") as infile, open(bed_path, "w") as outfile:
        for line in infile:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.strip().split("\t")
            if len(parts) < 9:
                continue
            
            chrom, source, feature, start_str, end_str, score, strand, frame, attributes = parts
            
            # Extract only mRNA features to match the CDS sequence names
            if feature == "mRNA":
                start = int(start_str) - 1  # 1-indexed to 0-indexed
                end = int(end_str)
                
                # Parse attributes to find ID
                attr_dict = {}
                for attr in attributes.split(";"):
                    if "=" in attr:
                        k, v = attr.split("=", 1)
                        attr_dict[k] = v
                
                gene_id = attr_dict.get("ID")
                if not gene_id:
                    continue
                
                # Prefix chromosome to avoid MCscan layout clashes
                prefixed_chrom = f"{prefix}_{chrom}"
                
                # Write standard 6-column BED format for JCVI
                outfile.write(f"{prefixed_chrom}\t{start}\t{end}\t{gene_id}\t0\t{strand}\n")
                count += 1
                
    print(f"Successfully wrote {count} mRNA features to {bed_path}")


def prepare_cds():
    """Symlinks the CDS fasta files to the data folder to avoid duplication."""
    print("Preparing CDS FASTA files via symlinks...")
    
    for src, dst in [(CDS_VPER, OUT_CDS_VPER), (PROJECT_CDS_VTUB, OUT_CDS_VTUB)]:
        if os.path.lexists(dst):
            os.remove(dst)
        print(f"Symlinking {src} -> {dst}")
        os.symlink(src, dst)
        
    print("CDS files prepared successfully.")


def main():
    # Make sure target directories exist
    os.makedirs(os.path.join(SYNTENY_DIR, "data"), exist_ok=True)
    
    # 1. Convert GFFs to BED with species-specific chromosome prefixes
    gff_to_bed(GFF_VPER, OUT_BED_VPER, "vp")
    gff_to_bed(GFF_VTUB, OUT_BED_VTUB, "vt")
    
    # 2. Copy the CDS sequences
    prepare_cds()
    
    print("\n==================================================")
    print("Files successfully prepared for MCscan (JCVI)!")
    print(f"BED Files: {OUT_BED_VPER}, {OUT_BED_VTUB}")
    print(f"CDS Files: {OUT_CDS_VPER}, {OUT_CDS_VTUB}")
    print("==================================================")


if __name__ == "__main__":
    main()
