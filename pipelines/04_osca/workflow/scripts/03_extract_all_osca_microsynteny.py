#!/usr/bin/env python3
"""
Extracts micro-synteny block and layout files for all chromosomes containing OSCA genes,
runs the JCVI plotting utility, and stores resulting PDFs in results/microsynteny_plots/.
"""

import os
import subprocess
import shutil

# Define paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYNTENY_DIR = os.path.dirname(SCRIPT_DIR)
PROJECT_DIR = os.path.dirname(os.path.dirname(SYNTENY_DIR))

BED_VPER = os.path.join(SYNTENY_DIR, "data", "Vper.bed")
BED_VTUB = os.path.join(SYNTENY_DIR, "data", "Vtub.bed")
ANCHORS_FILE = os.path.join(SYNTENY_DIR, "intergenomic", "intermediates", "Vper.Vtub.anchors")
OSCA_IDS_FILE = os.path.join(PROJECT_DIR, "analyses", "01_gene_identification", "results", "oscasIDs.txt")

MICRO_DIR = os.path.join(SYNTENY_DIR, "microsynteny")
RESULTS_DIR = os.path.join(SYNTENY_DIR, "results", "microsynteny_plots")


def read_osca_ids(path):
    """Reads OSCA IDs from oscasIDs.txt and groups them by species and chromosome."""
    oscas = {"Vper": {}, "Vtub": {}}
    if not os.path.exists(path):
        print(f"Error: {path} not found.")
        return oscas
    with open(path, "r") as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                gene_id = parts[0]
                name = parts[1]
                
                if gene_id.startswith("Vper"):
                    species = "Vper"
                elif gene_id.startswith("Vtub"):
                    species = "Vtub"
                else:
                    continue
                
                fields = gene_id.split(".")
                if len(fields) >= 4:
                    chrom = fields[3]
                    if chrom not in oscas[species]:
                        oscas[species][chrom] = []
                    oscas[species][chrom].append((gene_id, name))
    return oscas


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
    print("Reading OSCA genes grouped by chromosome...")
    oscas = read_osca_ids(OSCA_IDS_FILE)
    
    all_chroms = sorted(list(set(oscas["Vper"].keys()) | set(oscas["Vtub"].keys())))
    print(f"Chromosomes containing OSCA genes: {', '.join(all_chroms)}")

    print("Reading BED files...")
    vper_genes, vper_map = read_bed_genes(BED_VPER)
    vtub_genes, vtub_map = read_bed_genes(BED_VTUB)

    # Make sure output directories exist
    os.makedirs(MICRO_DIR, exist_ok=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)

    for chrom in all_chroms:
        print(f"\n==================================================")
        print(f"Processing chromosome {chrom}...")
        
        vper_oscas = [g[0] for g in oscas["Vper"].get(chrom, [])]
        vtub_oscas = [g[0] for g in oscas["Vtub"].get(chrom, [])]
        
        print(f"  Vper OSCA genes: {', '.join([oscas['Vper'][chrom][i][1] for i in range(len(vper_oscas))])}")
        print(f"  Vtub OSCA genes: {', '.join([oscas['Vtub'][chrom][i][1] for i in range(len(vtub_oscas))])}")

        vper_idxs = [vper_map[g] for g in vper_oscas if g in vper_map]
        vtub_idxs = [vtub_map[g] for g in vtub_oscas if g in vtub_map]

        if not vper_idxs or not vtub_idxs:
            print(f"  Warning: Missing genes in BED for chromosome {chrom}. Skipping micro-synteny.")
            continue

        min_vper_idx = max(0, min(vper_idxs) - 15)
        max_vper_idx = min(len(vper_genes) - 1, max(vper_idxs) + 15)

        min_vtub_idx = max(0, min(vtub_idxs) - 15)
        max_vtub_idx = min(len(vtub_genes) - 1, max(vtub_idxs) + 15)

        vper_local_genes = set(vper_genes[i][3] for i in range(min_vper_idx, max_vper_idx + 1))
        vtub_local_genes = set(vtub_genes[i][3] for i in range(min_vtub_idx, max_vtub_idx + 1))

        print(f"  Vper local window: {len(vper_local_genes)} genes (indices {min_vper_idx} to {max_vper_idx})")
        print(f"  Vtub local window: {len(vtub_local_genes)} genes (indices {min_vtub_idx} to {max_vtub_idx})")

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

        print(f"  Found {len(local_anchors)} local syntenic gene connections.")

        # Write .blocks file into microsynteny/
        out_blocks_path = os.path.join(MICRO_DIR, f"osca_{chrom}.blocks")
        with open(out_blocks_path, "w") as f:
            for g1, g2 in local_anchors:
                f.write(f"{g1}\t{g2}\n")
        print(f"  Wrote local blocks to: {out_blocks_path}")

        # Write .layout file into microsynteny/
        out_layout_path = os.path.join(MICRO_DIR, f"osca_{chrom}.layout")
        layout_content = f"""# x,   y, rotation,   ha,     va,   color, ratio,            label
0.5, 0.6,        0, left, center,       m,     1,       vp_{chrom}
0.5, 0.4,        0, left, center, #fc8d62,     1,       vt_{chrom}
# edges
e, 0, 1
"""
        with open(out_layout_path, "w") as f:
            f.write(layout_content)
        print(f"  Wrote micro-layout to: {out_layout_path}")

        # Plot local synteny
        print(f"  Generating plot for {chrom}...")
        plot_command = [
            "/home/mfcaval/.local/share/mamba/envs/jcviEnv/bin/python",
            "-m", "jcvi.graphics.synteny",
            os.path.join("microsynteny", f"osca_{chrom}.blocks"),
            os.path.join("data", "all.bed"),
            os.path.join("microsynteny", f"osca_{chrom}.layout"),
            "--notex"
        ]
        
        try:
            result = subprocess.run(
                plot_command,
                cwd=SYNTENY_DIR,
                capture_output=True,
                text=True,
                check=True
            )
            
            # Move the generated PDF from SYNTENY_DIR to RESULTS_DIR
            pdf_name = f"osca_{chrom}.pdf"
            generated_pdf = os.path.join(SYNTENY_DIR, pdf_name)
            final_pdf_path = os.path.join(RESULTS_DIR, pdf_name)
            if os.path.exists(generated_pdf):
                shutil.move(generated_pdf, final_pdf_path)
                print(f"  Successfully generated and stored: results/microsynteny_plots/{pdf_name}!")
        except subprocess.CalledProcessError as e:
            print(f"  Error plotting {chrom}:")
            print(e.stderr)

    print("\n==================================================")
    print("All micro-synteny plots processed successfully!")
    print("==================================================")


if __name__ == "__main__":
    main()
