#!/usr/bin/env python3

import os
import shutil

# Define paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYNTENY_DIR = os.path.dirname(SCRIPT_DIR)
PROJECT_DIR = os.path.dirname(os.path.dirname(SYNTENY_DIR))

GFF_VPER = os.path.join(PROJECT_DIR, "data", "genomes", "Vper", "Vper.hapA.v1.softmasked.gff3")
GFF_VTUB = os.path.join(PROJECT_DIR, "data", "genomes", "Vtub", "Vtub.hapA.v1.softmasked.gff3")

CDS_VPER = os.path.join(PROJECT_DIR, "data", "genomes", "Vper", "Vper.hapA.v1.softmasked.cds.fasta")
CDS_VTUB = os.path.join(PROJECT_DIR, "data", "genomes", "Vtub", "Vtub.hapA.v1.softmasked.cds.fasta")

OUT_BED_VPER = os.path.join(SYNTENY_DIR, "Vper.bed")
OUT_BED_VTUB = os.path.join(SYNTENY_DIR, "Vtub.bed")

OUT_CDS_VPER = os.path.join(SYNTENY_DIR, "Vper.cds")
OUT_CDS_VTUB = os.path.join(SYNTENY_DIR, "Vtub.cds")


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
                
                # Write standard 6-column BED format for JCVI:
                # chrom, start, end, gene_id, score (0), strand
                outfile.write(f"{prefixed_chrom}\t{start}\t{end}\t{gene_id}\t0\t{strand}\n")
                count += 1
                
    print(f"Successfully wrote {count} mRNA features to {bed_path}")


def prepare_cds():
    """Copies/links the CDS fasta files to the synteny folder."""
    print("Preparing CDS FASTA files...")
    
    # We copy them to ensure they exist locally and are named exactly as expected
    print(f"Copying {CDS_VPER} -> {OUT_CDS_VPER}")
    shutil.copy2(CDS_VPER, OUT_CDS_VPER)
    
    print(f"Copying {CDS_VTUB} -> {OUT_CDS_VTUB}")
    shutil.copy2(CDS_VTUB, OUT_CDS_VTUB)
    
    print("CDS files prepared successfully.")


def main():
    # Make sure target directory exists
    os.makedirs(SYNTENY_DIR, exist_ok=True)
    
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
