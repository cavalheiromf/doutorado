#!/usr/bin/env python3
"""
Finds and highlights syntenic blocks containing OSCA genes inside
the organized intergenomic/intermediates/ directory structure.
"""

import os

# Define paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYNTENY_DIR = os.path.dirname(SCRIPT_DIR)
PROJECT_DIR = os.path.dirname(os.path.dirname(SYNTENY_DIR))

BED_VPER = os.path.join(SYNTENY_DIR, "data", "Vper.bed")
BED_VTUB = os.path.join(SYNTENY_DIR, "data", "Vtub.bed")
SIMPLE_FILE = os.path.join(SYNTENY_DIR, "intergenomic", "intermediates", "Vper.Vtub.simple")
OSCA_IDS_FILE = os.path.join(PROJECT_DIR, "analyses", "01_gene_identification", "results", "oscasIDs.txt")

OUT_SIMPLE = os.path.join(SYNTENY_DIR, "intergenomic", "intermediates", "Vper.Vtub.oscas.simple")


def read_osca_ids(path):
    """Reads OSCA IDs from oscasIDs.txt and maps gene ID to common name."""
    osca_map = {}
    if not os.path.exists(path):
        print(f"Error: {path} not found.")
        return osca_map
    with open(path, "r") as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                osca_map[parts[0]] = parts[1]
    return osca_map


def read_bed_chroms(bed_path):
    """Reads a BED file and returns:
       - a map of gene_id -> (chrom, index)
       - a dict of chrom -> list of gene_ids in order
    """
    gene_to_info = {}
    chrom_to_genes = {}
    
    with open(bed_path, "r") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 4:
                chrom, _, _, gene_id = parts[0], int(parts[1]), int(parts[2]), parts[3]
                if chrom not in chrom_to_genes:
                    chrom_to_genes[chrom] = []
                chrom_to_genes[chrom].append(gene_id)
                idx = len(chrom_to_genes[chrom]) - 1
                gene_to_info[gene_id] = (chrom, idx)
    return gene_to_info, chrom_to_genes


def main():
    print("Reading OSCA gene list...")
    osca_map = read_osca_ids(OSCA_IDS_FILE)
    print(f"Loaded {len(osca_map)} OSCA genes.")

    print("Reading BED files...")
    vper_info, vper_chroms = read_bed_chroms(BED_VPER)
    vtub_info, vtub_chroms = read_bed_chroms(BED_VTUB)

    print("Analyzing Vper.Vtub.simple blocks...")
    highlighted_count = 0
    total_blocks = 0

    with open(SIMPLE_FILE, "r") as infile, open(OUT_SIMPLE, "w") as outfile:
        # Read header
        header = infile.readline()
        outfile.write(header)

        for line in infile:
            if not line.strip():
                continue
            total_blocks += 1
            parts = line.strip().split("\t")
            if len(parts) < 6:
                outfile.write(line)
                continue

            g1_start, g1_end, g2_start, g2_end, score, orientation = parts[:6]

            # Find chromosome and index bounds for Species A (Vper)
            contained_oscas_a = []
            if g1_start in vper_info and g1_end in vper_info:
                chrom_a, idx_start_a = vper_info[g1_start]
                _, idx_end_a = vper_info[g1_end]
                
                # Make sure indices are in correct order
                start_a, end_a = min(idx_start_a, idx_end_a), max(idx_start_a, idx_end_a)
                
                # Get all genes in this block range
                block_genes_a = vper_chroms[chrom_a][start_a:end_a+1]
                
                # Check for overlap with OSCA genes
                for g in block_genes_a:
                    if g in osca_map:
                        contained_oscas_a.append((g, osca_map[g]))

            # Find chromosome and index bounds for Species B (Vtub)
            contained_oscas_b = []
            if g2_start in vtub_info and g2_end in vtub_info:
                chrom_b, idx_start_b = vtub_info[g2_start]
                _, idx_end_b = vtub_info[g2_end]
                
                start_b, end_b = min(idx_start_b, idx_end_b), max(idx_start_b, idx_end_b)
                block_genes_b = vtub_chroms[chrom_b][start_b:end_b+1]
                
                for g in block_genes_b:
                    if g in osca_map:
                        contained_oscas_b.append((g, osca_map[g]))

            # If block contains any OSCA genes, highlight it with a red 'r*' prefix
            if contained_oscas_a or contained_oscas_b:
                highlighted_count += 1
                oscas_desc = []
                if contained_oscas_a:
                    oscas_desc.append("Vper: " + ", ".join([f"{name} ({gid})" for gid, name in contained_oscas_a]))
                if contained_oscas_b:
                    oscas_desc.append("Vtub: " + ", ".join([f"{name} ({gid})" for gid, name in contained_oscas_b]))
                
                print(f"Block {total_blocks}: Highlighted!")
                print(f"  Coordinates: {g1_start}..{g1_end} <-> {g2_start}..{g2_end}")
                print(f"  OSCAs in Block: {' | '.join(oscas_desc)}")
                
                # Prefix the first gene with 'r*'
                parts_copy = list(parts)
                parts_copy[0] = "r*" + parts_copy[0]
                outfile.write("\t".join(parts_copy) + "\n")
            else:
                outfile.write(line)

    print(f"\nAnalysis complete. Total blocks parsed: {total_blocks}")
    print(f"Highlighted {highlighted_count} blocks containing OSCA genes.")
    print(f"Saved highlighted blocks to: {OUT_SIMPLE}")


if __name__ == "__main__":
    main()
