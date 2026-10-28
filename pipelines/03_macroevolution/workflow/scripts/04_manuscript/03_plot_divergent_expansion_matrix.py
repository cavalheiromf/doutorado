#!/usr/bin/env python3
"""Generate publication-ready Figure 5 for the Velloziaceae macroevolution manuscript.
Figure 5: Focal Gene Family Expansions in Sister Vellozia Species:
Contrasting Genomic Architectures of Desiccation Avoidance versus Desiccation Tolerance.

Adheres strictly to scientific-visualization standards:
- 300 DPI PNG + vector PDF exports
- Colorblind-safe palette (Okabe-Ito: #D55E00 for Vper, #0072B2 for Vtub)
- Diverging effect size (CAFE5 net gain) aligned with phylogenetic copy-count heatmap
- Exact integer counts printed inside heatmap cells for complete baseline transparency
- 100% canonical nuclear genes anchored on pseudochromosomes (chr1A-chr9A)
- Perfect typographic hierarchy and horizontal guide alignment
"""

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
from matplotlib.colors import Normalize
import numpy as np

# Set publication style defaults
plt.rcParams.update({
    "font.sans-serif": ["DejaVu Sans", "Helvetica", "Arial"],
    "font.family": "sans-serif",
    "font.size": 9.5,
    "axes.titlesize": 10.5,
    "axes.labelsize": 9.5,
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 9.0,
    "legend.fontsize": 8.5,
    "figure.titlesize": 12.5,
    "lines.linewidth": 1.2,
    "axes.linewidth": 0.8,
    "xtick.major.width": 0.8,
    "ytick.major.width": 0.8,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "figure.autolayout": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 42
})

BASE_DIR = Path(__file__).resolve().parents[3]
FIG_DIR = BASE_DIR / "04_manuscript" / "figures"
PROJECT_ROOT = BASE_DIR.parent.parent
DOCS_FIG_DIR = PROJECT_ROOT / "docs" / "03_chapter_3_macroevolution" / "manuscripts" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)
DOCS_FIG_DIR.mkdir(parents=True, exist_ok=True)

# Curated data: V. peripherica top expansions (all canonical nuclear chr1A-chr9A)
VPER_FAMILIES = [
    ("OG0000001", "LRR receptor-like kinases (LRR-RLK)", 49, 98, 43, 56, 5),
    ("OG0000014", "F-box protein with DUF295 domain", 37, 67, 27, 30, 4),
    ("OG0000042", "Disease resistance NB-ARC (NLRs)", 26, 36, 9, 7, 6),
    ("OG0000079", "F-box protein with Kelch repeats", 24, 34, 8, 9, 2),
    ("OG0000139", "DEK C-terminal chromatin factor", 21, 33, 11, 9, 0),
    ("OG0000067", "Plant mobile domain (PMD)", 18, 35, 17, 10, 0),
    ("OG0000476", "Pentatricopeptide repeat (PPR cluster)", 18, 20, 2, 2, 1),
    ("OG0000012", "Wall-associated receptor kinases (WAK)", 17, 45, 27, 25, 11),
    ("OG0000058", "Cytochrome P450 monooxygenases", 17, 29, 9, 14, 5)
]

# Curated data: V. tubiflora top expansions (strictly canonical nuclear chr1A-chr9A)
VTUB_FAMILIES = [
    ("OG0001778", "Ribonuclease III-like (RTL1 / dsRNA endoribonuclease)", 10, 1, 13, 0, 1),
    ("OG0000643", "Tudor / Agenet domain chromatin reader", 7, 3, 12, 1, 1),
    ("OG0000010", "Plant mobile domain (PMD / FHY3-FAR1)", 6, 46, 59, 58, 0),
    ("OG0000581", "Ent-copalyl diphosphate synthase (GA1 / Diterpene)", 5, 5, 11, 3, 2),
    ("OG0000127", "Terpene synthase (TPS10 / Cineole synthase)", 3, 9, 13, 1, 4),
    ("OG0001439", "DnaJ / Hsp40 molecular chaperone", 3, 2, 5, 1, 1),
    ("OG0000962", "Chalcone-flavanone isomerase (CHI-like / Flavonoid)", 2, 2, 8, 8, 1),
    ("OG0000362", "Pyrophosphate-fructose-6-P 1-phosphotransferase (PFP)", 2, 4, 8, 6, 5),
    ("OG0001749", "Jasmonic acid carboxyl methyltransferase (JMT)", 2, 1, 5, 3, 0)
]


def plot_figure_5():
    print("Generating Figure 5: Diverging expansion bar chart & phylogenetic copy matrix...")
    
    n_vper = len(VPER_FAMILIES)
    n_vtub = len(VTUB_FAMILIES)
    
    # Y positions from top to bottom:
    # Vper: rows 19 down to 11 (9 rows)
    # Gap / Divider / Subtitle: row 10 & 9
    # Vtub: rows 8 down to 0 (9 rows)
    y_vper = list(range(19, 19 - n_vper, -1))
    y_vtub = list(range(8, 8 - n_vtub, -1))
    
    fig = plt.figure(figsize=(14.6, 10.6), dpi=300)
    gs = GridSpec(1, 2, width_ratios=[1.28, 1.0], wspace=0.34, figure=fig,
                  left=0.29, right=0.91, top=0.86, bottom=0.12)
    
    ax_bar = fig.add_subplot(gs[0, 0])
    ax_mat = fig.add_subplot(gs[0, 1])
    
    c_vper = "#D55E00"  # Vermilion / terracotta
    c_vtub = "#0072B2"  # Deep blue
    
    # Background alternating row tracks & horizontal guide lines
    for y in (y_vper + y_vtub):
        bg_col = "#F9FAFB" if y % 2 == 0 else "#FFFFFF"
        ax_bar.axhspan(y - 0.45, y + 0.45, facecolor=bg_col, edgecolor="none", zorder=0)
        ax_mat.axhspan(y - 0.45, y + 0.45, facecolor=bg_col, edgecolor="none", zorder=0)
        ax_bar.axhline(y, color="#E8ECEF", lw=0.5, zorder=1)
        ax_mat.axhline(y, color="#E8ECEF", lw=0.5, zorder=1)
    
    # -------------------------------------------------------------------------
    # PANEL A: Net Copy Gain Bar Chart
    # -------------------------------------------------------------------------
    vper_labels = []
    for y, (og, name, gain, vper_c, vtub_c, xvis_c, abra_c) in zip(y_vper, VPER_FAMILIES):
        ax_bar.barh(y, gain, height=0.64, color=c_vper, edgecolor="#801500", lw=0.6, alpha=0.92, zorder=3)
        ax_bar.text(gain + 0.8, y, f"+{gain}", va="center", ha="left",
                    fontsize=8.5, weight="bold", color=c_vper, zorder=4)
        vper_labels.append(f"{name}\n({og})")
        
    vtub_labels = []
    for y, (og, name, gain, vper_c, vtub_c, xvis_c, abra_c) in zip(y_vtub, VTUB_FAMILIES):
        ax_bar.barh(y, gain, height=0.64, color=c_vtub, edgecolor="#003E6B", lw=0.6, alpha=0.92, zorder=3)
        ax_bar.text(gain + 0.8, y, f"+{gain}", va="center", ha="left",
                    fontsize=8.5, weight="bold", color=c_vtub, zorder=4)
        vtub_labels.append(f"{name}\n({og})")
        
    ax_bar.set_xlim(0, 56)
    ax_bar.set_ylim(-0.8, 21.2)
    ax_bar.set_xlabel(r"Lineage-Specific Net Expansion (CAFE5 $\Delta$ Gene Copies)", weight="bold", labelpad=8)
    
    all_y = y_vper + y_vtub
    all_labels = vper_labels + vtub_labels
    ax_bar.set_yticks(all_y)
    ax_bar.set_yticklabels(all_labels, fontsize=8.2)
    
    # Clean section banners above blocks (explicitly emphasizing canonical nuclear genes)
    ax_bar.text(0, 20.1, "V. peripherica Canonical Nuclear Expansions (chr1–chr9)",
                fontsize=9.2, weight="bold", color=c_vper, ha="left", va="bottom")
    ax_bar.text(0, 9.1, "V. tubiflora Canonical Nuclear Expansions (chr1–chr9)",
                fontsize=9.2, weight="bold", color=c_vtub, ha="left", va="bottom")
    
    # Horizontal divider between Vper and Vtub blocks
    ax_bar.axhline(9.8, color="#B0BEC5", linestyle="--", lw=1.0, zorder=2)
    
    # Grid lines & styling
    ax_bar.grid(axis="x", linestyle=":", color="#D0D7DE", lw=0.7, zorder=2)
    ax_bar.set_axisbelow(True)
    ax_bar.spines["top"].set_visible(False)
    ax_bar.spines["right"].set_visible(False)
    ax_bar.spines["left"].set_color("#666666")
    ax_bar.spines["bottom"].set_color("#666666")
    
    # Panel tag A
    ax_bar.text(-0.35, 1.04, "A", transform=ax_bar.transAxes,
                fontsize=14, weight="bold", va="top", ha="left")
    
    # -------------------------------------------------------------------------
    # PANEL B: Aligned Phylogenetic Copy-Count Heatmap
    # -------------------------------------------------------------------------
    species_labels = [
        "V. peripherica (Avoidant)",
        "V. tubiflora (Resurrection)",
        "X. schlechteri (Resurrection)",
        "A. bracteata (Relict)"
    ]
    
    matrix_data = np.full((21, 4), np.nan)
    for y, item in zip(y_vper, VPER_FAMILIES):
        matrix_data[y, :] = item[3:7]
    for y, item in zip(y_vtub, VTUB_FAMILIES):
        matrix_data[y, :] = item[3:7]
        
    cmap = plt.cm.YlGnBu
    cmap.set_bad(color="white")
    norm = Normalize(vmin=0, vmax=98)
    
    # Plot matrix cells
    for row_idx in (y_vper + y_vtub):
        for col_idx in range(4):
            val = matrix_data[row_idx, col_idx]
            if np.isnan(val):
                continue
            int_val = int(val)
            color = cmap(norm(int_val))
            rect = plt.Rectangle((col_idx - 0.42, row_idx - 0.38), 0.84, 0.76,
                                 facecolor=color, edgecolor="#FFFFFF", lw=1.4, zorder=3)
            ax_mat.add_patch(rect)
            
            text_color = "white" if norm(int_val) > 0.45 else "#1A1A1A"
            ax_mat.text(col_idx, row_idx, str(int_val), ha="center", va="center",
                        fontsize=8.5, weight="bold", color=text_color, zorder=4)
            
    ax_mat.set_xlim(-0.6, 3.6)
    ax_mat.set_ylim(-0.8, 21.2)
    ax_mat.set_yticks([])  # Synchronized with panel A
    
    # Bottom labels rotated diagonally
    ax_mat.set_xticks(range(4))
    ax_mat.set_xticklabels(species_labels, rotation=28, ha="right", weight="bold", fontsize=8.5)
    
    # Horizontal divider matching panel A
    ax_mat.axhline(9.8, color="#B0BEC5", linestyle="--", lw=1.0, zorder=2)
    
    # Draw Cladogram above the matrix (y = 19.8 to 20.8)
    tree_base_y = 19.8
    # Stem from col 0 and 1
    ax_mat.plot([0, 0], [tree_base_y, tree_base_y + 0.25], color="#4B5563", lw=1.0)
    ax_mat.plot([1, 1], [tree_base_y, tree_base_y + 0.25], color="#4B5563", lw=1.0)
    ax_mat.plot([0, 1], [tree_base_y + 0.25, tree_base_y + 0.25], color="#4B5563", lw=1.0)
    
    # Sister node to Core Velloziaceae
    ax_mat.plot([0.5, 0.5], [tree_base_y + 0.25, tree_base_y + 0.55], color="#4B5563", lw=1.0)
    ax_mat.plot([2, 2], [tree_base_y, tree_base_y + 0.55], color="#4B5563", lw=1.0)
    ax_mat.plot([0.5, 2], [tree_base_y + 0.55, tree_base_y + 0.55], color="#4B5563", lw=1.0)
    
    # Core Velloziaceae to Velloziaceae Crown
    ax_mat.plot([1.25, 1.25], [tree_base_y + 0.55, tree_base_y + 0.85], color="#4B5563", lw=1.0)
    ax_mat.plot([3, 3], [tree_base_y, tree_base_y + 0.85], color="#4B5563", lw=1.0)
    ax_mat.plot([1.25, 3], [tree_base_y + 0.85, tree_base_y + 0.85], color="#4B5563", lw=1.0)
    ax_mat.plot([2.125, 2.125], [tree_base_y + 0.85, tree_base_y + 1.1], color="#4B5563", lw=1.0)
    
    # Header above cladogram
    ax_mat.text(1.5, 21.0, "Cross-Taxon Canonical Nuclear Repertoires (Gene Counts)",
                fontsize=8.8, weight="bold", color="#374151", ha="center", va="bottom")
    
    # Clean spines on matrix
    for spine in ax_mat.spines.values():
        spine.set_visible(False)
    ax_mat.tick_params(left=False, bottom=True, color="#CCCCCC")
    
    # Panel tag B
    ax_mat.text(-0.15, 1.04, "B", transform=ax_mat.transAxes,
                fontsize=14, weight="bold", va="top", ha="left")
    
    # Add Colorbar for copy count heatmap
    cbar_ax = fig.add_axes([0.925, 0.16, 0.015, 0.28])
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, cax=cbar_ax)
    cbar.set_label("Nuclear Gene Copies (chr1–chr9)", weight="bold", fontsize=8.2, labelpad=6)
    cbar.ax.tick_params(labelsize=7.5)
    cbar.outline.set_linewidth(0.6)
    
    # Super title & subtitle
    fig.suptitle("Contrasting Genomic Architectures of Desiccation Avoidance versus Tolerance in Sister Vellozia Species",
                 fontsize=12.2, weight="bold", y=0.96)
    fig.text(0.5, 0.93,
             "Curated canonical nuclear gene family expansions anchored to pseudochromosomes (chr1–chr9; organellar contigs strictly excluded)",
             fontsize=9.2, ha="center", color="#4B5563")
    
    # Save figure to both directories
    png_path = FIG_DIR / "Figure5_focal_family_expansions.png"
    pdf_path = FIG_DIR / "Figure5_focal_family_expansions.pdf"
    svg_path = FIG_DIR / "Figure5_focal_family_expansions.svg"
    fig.savefig(png_path, dpi=300)
    fig.savefig(pdf_path)
    fig.savefig(svg_path)
    
    fig.savefig(DOCS_FIG_DIR / "Figure5_focal_family_expansions.png", dpi=300)
    fig.savefig(DOCS_FIG_DIR / "Figure5_focal_family_expansions.pdf")
    fig.savefig(DOCS_FIG_DIR / "Figure5_focal_family_expansions.svg")
    plt.close(fig)
    print(f"Figure 5 saved successfully:\n  - {png_path}\n  - {pdf_path}\n  - {svg_path}")


if __name__ == "__main__":
    plot_figure_5()

