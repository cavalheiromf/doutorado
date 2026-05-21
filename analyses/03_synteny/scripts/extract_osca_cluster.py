#!/usr/bin/env python3
"""
Extracts local synteny block for the core OSCA1.3/1.4/1.5 cluster on chr7A,
writing outputs into the microsynteny/ subdirectory.
"""

import os

# Define paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYNTENY_DIR = os.path.dirname(SCRIPT_DIR)
PROJECT_DIR = os.path.dirname(os.path.dirname(SYNTENY_DIR))

BED_VPER = os.path.join(SYNTENY_DIR, "data", "Vper.bed")
BED_VTUB = os.path.join(SYNTENY_DIR, "data", "Vtub.bed")
ANCHORS_FILE = os.path.join(SYNTENY_DIR, "intergenomic", "intermediates", "Vper.Vtub.anchors")

OUT_BLOCKS = os.path.join(SYNTENY_DIR, "microsynteny", "osca_cluster.blocks")
OUT_LAYOUT = os.path.join(SYNTENY_DIR, "microsynteny", "osca_cluster.layout")


def read_bed_genes(bed_path):
    """Reads BED file and returns list of gene IDs and a map of gene -> index."""
    genes = []
    gene_to_idx = {}
    with open(bed_path, "r") as f:
        for idx, line in enumerate(f):
            parts = line.strip().split("\t")
            if len(parts) >= 4:
                gene_id = parts[3]
                genes.append((parts[0], int(parts[1]), int(parts[2]), gene_id, parts[5]))
                gene_to_idx[gene_id] = idx
    return genes, gene_to_idx


def main():
    print("Reading BED files...")
    vper_genes, vper_map = read_bed_genes(BED_VPER)
    vtub_genes, vtub_map = read_bed_genes(BED_VTUB)

    # Core OSCA1.3/1.4/1.5 genes on chr7A
    vper_osca_core = [
        "Vper.hapA.v1.chr7A.g186390.t1",  # OSCA1.3
        "Vper.hapA.v1.chr7A.g186400.t1",  # OSCA1.4
        "Vper.hapA.v1.chr7A.g186410.t1"   # OSCA1.5
    ]

    vtub_osca_core = [
        "Vtub.hapA.v1.chr7A.g166590.t1",  # OSCA1.3
        "Vtub.hapA.v1.chr7A.g166600.t1",  # OSCA1.4
        "Vtub.hapA.v1.chr7A.g166610.t1"   # OSCA1.5
    ]

    # Find the indices in BED lists
    vper_idxs = [vper_map[g] for g in vper_osca_core if g in vper_map]
    vtub_idxs = [vtub_map[g] for g in vtub_osca_core if g in vtub_map]

    if not vper_idxs or not vtub_idxs:
        print("Error: Could not locate core OSCA genes in BED files.")
        return

    # Define window of 15 genes upstream and downstream of the cluster
    min_vper_idx = max(0, min(vper_idxs) - 15)
    max_vper_idx = min(len(vper_genes) - 1, max(vper_idxs) + 15)

    min_vtub_idx = max(0, min(vtub_idxs) - 15)
    max_vtub_idx = min(len(vtub_genes) - 1, max(vtub_idxs) + 15)

    vper_local_genes = set(vper_genes[i][3] for i in range(min_vper_idx, max_vper_idx + 1))
    vtub_local_genes = set(vtub_genes[i][3] for i in range(min_vtub_idx, max_vtub_idx + 1))

    print(f"Vper local window: {len(vper_local_genes)} genes (indices {min_vper_idx} to {max_vper_idx})")
    print(f"Vtub local window: {len(vtub_local_genes)} genes (indices {min_vtub_idx} to {max_vtub_idx})")

    # Read anchors and extract local links
    print(f"Reading anchors from {ANCHORS_FILE}...")
    local_anchors = []
    with open(ANCHORS_FILE, "r") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                g1, g2 = parts[0], parts[1]
                if g1 in vper_local_genes and g2 in vtub_local_genes:
                    local_anchors.append((g1, g2))

    print(f"Found {len(local_anchors)} syntenic connections in this local region.")

    # Write the .blocks file
    with open(OUT_BLOCKS, "w") as f:
        for g1, g2 in local_anchors:
            f.write(f"{g1}\t{g2}\n")
    print(f"Wrote local blocks to {OUT_BLOCKS}")

    # Write the micro-synteny layout file
    layout_content = """# x,   y, rotation,   ha,     va,   color, ratio,            label
0.5, 0.6,        0, left, center,       m,     1,       vp_chr7A
0.5, 0.4,        0, left, center, #fc8d62,     1,       vt_chr7A
# edges
e, 0, 1
"""
    with open(OUT_LAYOUT, "w") as f:
        f.write(layout_content)
    print(f"Wrote micro-layout to {OUT_LAYOUT}")


if __name__ == "__main__":
    main()
