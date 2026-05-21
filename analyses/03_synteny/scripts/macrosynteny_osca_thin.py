#!/usr/bin/env python3
"""
Generate a macrosynteny karyotype figure with THIN red lines marking
the positions of OSCA ortholog genes under organized subfolders.
"""

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYNTENY_DIR = os.path.dirname(SCRIPT_DIR)
PROJECT_DIR = os.path.dirname(os.path.dirname(SYNTENY_DIR))

BED_VPER = os.path.join(SYNTENY_DIR, "data", "Vper.bed")
BED_VTUB = os.path.join(SYNTENY_DIR, "data", "Vtub.bed")
SIMPLE_FILE = os.path.join(SYNTENY_DIR, "intergenomic", "intermediates", "Vper.Vtub.simple")
ANCHORS_FILE = os.path.join(SYNTENY_DIR, "intergenomic", "intermediates", "Vper.Vtub.anchors")
OSCA_IDS_FILE = os.path.join(
    PROJECT_DIR, "analyses", "01_gene_identification", "results", "oscasIDs.txt"
)

OUT_SIMPLE = os.path.join(SYNTENY_DIR, "intergenomic", "intermediates", "Vper.Vtub.orthologs_thin.simple")

FLANK = 1


def read_osca_ids(path):
    osca_map = {}
    with open(path, "r") as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                osca_map[parts[0]] = parts[1]
    return osca_map


def read_bed_ordered(bed_path):
    gene_to_idx = {}
    idx_to_gene = {}
    gene_to_chrom = {}
    with open(bed_path, "r") as f:
        for idx, line in enumerate(f):
            parts = line.strip().split("\t")
            if len(parts) >= 4:
                gene_id = parts[3]
                gene_to_idx[gene_id] = idx
                idx_to_gene[idx] = gene_id
                gene_to_chrom[gene_id] = parts[0]
    return gene_to_idx, idx_to_gene, gene_to_chrom


def extract_chrom_suffix(prefixed_chrom):
    if "_" in prefixed_chrom:
        return prefixed_chrom.split("_", 1)[1]
    return prefixed_chrom


def find_ortholog_anchors(anchors_path, osca_vper_ids, osca_vtub_ids):
    pairs = []
    with open(anchors_path, "r") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                g1, g2 = parts[0], parts[1]
                if g1 in osca_vper_ids and g2 in osca_vtub_ids:
                    pairs.append((g1, g2))
    return pairs


def main():
    print("Reading OSCA gene list...")
    osca_map = read_osca_ids(OSCA_IDS_FILE)

    osca_vper = {g: n for g, n in osca_map.items() if g.startswith("Vper")}
    osca_vtub = {g: n for g, n in osca_map.items() if g.startswith("Vtub")}

    print("Reading BED files...")
    vper_g2i, vper_i2g, vper_g2c = read_bed_ordered(BED_VPER)
    vtub_g2i, vtub_i2g, vtub_g2c = read_bed_ordered(BED_VTUB)

    print("Finding OSCA ortholog anchors in Vper.Vtub.anchors...")
    anchor_pairs = find_ortholog_anchors(ANCHORS_FILE, osca_vper, osca_vtub)

    ortho_pairs = []
    for g1, g2 in anchor_pairs:
        c1 = extract_chrom_suffix(vper_g2c.get(g1, ""))
        c2 = extract_chrom_suffix(vtub_g2c.get(g2, ""))
        if c1 == c2:
            ortho_pairs.append((g1, g2, c1))

    paired_vper = {g1 for g1, _, _ in ortho_pairs}
    paired_vtub = {g2 for _, g2, _ in ortho_pairs}

    for vp_id, vp_name in osca_vper.items():
        if vp_id in paired_vper:
            continue
        vt_name = vp_name.replace("Vp", "Vt")
        for vt_id, vt_n in osca_vtub.items():
            if vt_n == vt_name and vt_id not in paired_vtub:
                c1 = extract_chrom_suffix(vper_g2c.get(vp_id, ""))
                c2 = extract_chrom_suffix(vtub_g2c.get(vt_id, ""))
                if c1 == c2:
                    ortho_pairs.append((vp_id, vt_id, c1))
                    paired_vper.add(vp_id)
                    paired_vtub.add(vt_id)
                break

    mini_blocks = []
    for g1, g2, chrom in ortho_pairs:
        idx_a = vper_g2i[g1]
        idx_b = vtub_g2i[g2]

        start_a = max(0, idx_a - FLANK)
        end_a = min(max(vper_g2i.values()), idx_a + FLANK)
        start_b = max(0, idx_b - FLANK)
        end_b = min(max(vtub_g2i.values()), idx_b + FLANK)

        ga_start = vper_i2g[start_a]
        ga_end = vper_i2g[end_a]
        gb_start = vtub_i2g[start_b]
        gb_end = vtub_i2g[end_b]

        orientation = "+"
        mini_blocks.append((ga_start, ga_end, gb_start, gb_end, orientation))

    # Read original block counts
    total_orig = 0
    with open(SIMPLE_FILE, "r") as f:
        for line in f:
            if line.strip() and not line.startswith("StartGene"):
                total_orig += 1

    print(f"\nWriting {OUT_SIMPLE}...")
    with open(SIMPLE_FILE, "r") as infile, open(OUT_SIMPLE, "w") as outfile:
        for line in infile:
            outfile.write(line)
        for ga_s, ga_e, gb_s, gb_e, orient in mini_blocks:
            outfile.write(f"r*{ga_s}\t{ga_e}\t{gb_s}\t{gb_e}\t1\t{orient}\n")

    print(f"Done! Written {len(mini_blocks)} red mini-blocks appended to "
          f"{total_orig} original gray blocks.")


if __name__ == "__main__":
    main()
