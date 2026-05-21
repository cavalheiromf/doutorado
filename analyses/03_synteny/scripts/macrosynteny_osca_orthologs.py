#!/usr/bin/env python3
"""
Generate a macrosynteny karyotype figure highlighting only the direct
orthologous syntenic blocks that contain OSCA genes inside organized paths.
"""

import os

# Define paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYNTENY_DIR = os.path.dirname(SCRIPT_DIR)
PROJECT_DIR = os.path.dirname(os.path.dirname(SYNTENY_DIR))

BED_VPER = os.path.join(SYNTENY_DIR, "data", "Vper.bed")
BED_VTUB = os.path.join(SYNTENY_DIR, "data", "Vtub.bed")
SIMPLE_FILE = os.path.join(SYNTENY_DIR, "intergenomic", "intermediates", "Vper.Vtub.simple")
OSCA_IDS_FILE = os.path.join(
    PROJECT_DIR, "analyses", "01_gene_identification", "results", "oscasIDs.txt"
)

OUT_SIMPLE = os.path.join(SYNTENY_DIR, "intergenomic", "intermediates", "Vper.Vtub.orthologs.simple")


def read_osca_ids(path):
    """Reads OSCA IDs from oscasIDs.txt and maps gene ID to common name."""
    osca_map = {}
    with open(path, "r") as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                osca_map[parts[0]] = parts[1]
    return osca_map


def read_bed_genes(bed_path):
    """Reads BED file and returns:
       - gene_to_info: gene_id -> (chrom, index)
       - chrom_to_genes: chrom -> [gene_id, ...]
    """
    gene_to_info = {}
    chrom_to_genes = {}
    with open(bed_path, "r") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 4:
                chrom = parts[0]
                gene_id = parts[3]
                if chrom not in chrom_to_genes:
                    chrom_to_genes[chrom] = []
                chrom_to_genes[chrom].append(gene_id)
                gene_to_info[gene_id] = (chrom, len(chrom_to_genes[chrom]) - 1)
    return gene_to_info, chrom_to_genes


def extract_chrom_suffix(prefixed_chrom):
    """Extract the chromosome suffix (e.g., 'chr1A') from prefixed name."""
    if "_" in prefixed_chrom:
        return prefixed_chrom.split("_", 1)[1]
    return prefixed_chrom


def main():
    print("Reading OSCA gene list...")
    osca_map = read_osca_ids(OSCA_IDS_FILE)
    print(f"Loaded {len(osca_map)} OSCA genes.")

    print("Reading BED files...")
    vper_info, vper_chroms = read_bed_genes(BED_VPER)
    vtub_info, vtub_chroms = read_bed_genes(BED_VTUB)

    print("Analyzing Vper.Vtub.simple blocks...")
    highlighted_count = 0
    skipped_paralog = 0
    total_blocks = 0

    with open(SIMPLE_FILE, "r") as infile, open(OUT_SIMPLE, "w") as outfile:
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

            g1_start, g1_end = parts[0], parts[1]
            g2_start, g2_end = parts[2], parts[3]

            chrom_a = None
            chrom_b = None

            if g1_start in vper_info:
                chrom_a = extract_chrom_suffix(vper_info[g1_start][0])
            if g2_start in vtub_info:
                chrom_b = extract_chrom_suffix(vtub_info[g2_start][0])

            contained_oscas_a = []
            contained_oscas_b = []

            if g1_start in vper_info and g1_end in vper_info:
                ca, idx_start = vper_info[g1_start]
                _, idx_end = vper_info[g1_end]
                start_a, end_a = min(idx_start, idx_end), max(idx_start, idx_end)
                block_genes_a = vper_chroms[ca][start_a : end_a + 1]
                for g in block_genes_a:
                    if g in osca_map:
                        contained_oscas_a.append((g, osca_map[g]))

            if g2_start in vtub_info and g2_end in vtub_info:
                cb, idx_start = vtub_info[g2_start]
                _, idx_end = vtub_info[g2_end]
                start_b, end_b = min(idx_start, idx_end), max(idx_start, idx_end)
                block_genes_b = vtub_chroms[cb][start_b : end_b + 1]
                for g in block_genes_b:
                    if g in osca_map:
                        contained_oscas_b.append((g, osca_map[g]))

            has_osca = bool(contained_oscas_a or contained_oscas_b)
            is_orthologous = chrom_a is not None and chrom_b is not None and chrom_a == chrom_b

            if has_osca and is_orthologous:
                highlighted_count += 1
                parts_copy = list(parts)
                parts_copy[0] = "r*" + parts_copy[0]
                outfile.write("\t".join(parts_copy) + "\n")
            elif has_osca and not is_orthologous:
                skipped_paralog += 1
                outfile.write(line)
            else:
                outfile.write(line)

    print(f"\nDone! Parsed {total_blocks} blocks.")
    print(f"  Highlighted (orthologous + OSCA): {highlighted_count}")
    print(f"  Skipped (paralogous + OSCA):      {skipped_paralog}")
    print(f"  Output: {OUT_SIMPLE}")


if __name__ == "__main__":
    main()
