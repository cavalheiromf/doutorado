#!/usr/bin/env python3
"""Generate all four publication-ready figures for the Velloziaceae macroevolution chapter.
Adheres to high-standard scientific visualization guidelines:
- 300 DPI PNG + vector PDF exports
- Colorblind-safe palette (Okabe-Ito / ColorBrewer)
- Clear multi-panel layouts with panel tags (A, B, C)
- Fully annotated values matching chapter_macroevolution_review results
"""

import csv
import json
import math
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
import numpy as np
import pandas as pd

# Set publication style defaults
plt.rcParams.update({
    "font.sans-serif": ["DejaVu Sans", "Helvetica", "Arial"],
    "font.family": "sans-serif",
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 8.5,
    "figure.titlesize": 13,
    "lines.linewidth": 1.5,
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
FIG_DIR.mkdir(parents=True, exist_ok=True)
PROJECT_ROOT = BASE_DIR.parent.parent
DOCS_FIG_DIR = PROJECT_ROOT / "docs" / "03_chapter_3_macroevolution" / "manuscripts" / "figures"
DOCS_FIG_DIR.mkdir(parents=True, exist_ok=True)

def save_publication_figure(fig, filename_stem):
    for directory in [FIG_DIR, DOCS_FIG_DIR]:
        fig.savefig(directory / f"{filename_stem}.png", dpi=300)
        fig.savefig(directory / f"{filename_stem}.pdf")
        fig.savefig(directory / f"{filename_stem}.svg")

# Color palette definitions (Okabe-Ito & Nature-compatible)
C_VPER = "#D55E00"       # Vermilion / terracotta (Avoidant / evergreen)
C_VTUB = "#0072B2"       # Blue (Resurrection / DT)
C_EXP = "#009E73"        # Green (Expansion)
C_CONT = "#D55E00"       # Red/Vermilion (Contraction)
C_ANC = "#7570B3"        # Purple (Ancestral nodes)
C_GRAY = "#7F7F7F"
C_LIGHT_BG = "#F8F9FA"



def read_current_results():
    convergence = pd.read_csv(
        BASE_DIR / "04_gene_families/cafe5/summary/M5_gamma_convergence_summary.tsv", sep="\t"
    )
    selected = convergence[convergence["selected_primary"].astype(bool)].iloc[0]
    turnover = pd.read_csv(
        BASE_DIR / "04_manuscript/tables/Table2_node_expansions_contractions.tsv", sep="\t"
    )
    duplication = pd.read_csv(
        BASE_DIR / "04_manuscript/tables/Table3_duplication_modes.tsv", sep="\t"
    )
    return selected, turnover, duplication


def percentage_value(value):
    return float(str(value).split("%")[0])


SELECTED_M5, TURNOVER, DUPLICATION = read_current_results()

# =============================================================================
# FIGURE 1: Chromosome-Scale Macrosynteny, Depth Dosage & Block Architecture
# =============================================================================
def plot_figure_1():
    print("Generating Figure 1: Chromosome-scale macrosynteny & structural stasis...")
    from jcvi.graphics.karyotype import Karyotype

    synteny_dir = BASE_DIR / "04_gene_families/synteny"
    layout_file = str(synteny_dir / "layout_abs")
    seqids_file = str(synteny_dir / "seqids")

    fig = plt.figure(figsize=(12.5, 9.5), dpi=300)

    # Panel A: Chromosome-scale macrosynteny ribbon plot
    ax_a = fig.add_axes([0.02, 0.52, 0.96, 0.44])
    Karyotype(ax_a, seqids_file, layout_file, gap=0.015, height=0.018)
    ax_a.set_axis_off()
    ax_a.text(0.138, 0.68, r"$\it{V.\ peripherica}$ (hap1)", transform=ax_a.transAxes,
              fontsize=9.5, weight="bold", color="#C8523A", ha="right", va="center")
    ax_a.text(0.138, 0.28, r"$\it{V.\ tubiflora}$ (hap1)", transform=ax_a.transAxes,
              fontsize=9.5, weight="bold", color="#3D6898", ha="right", va="center")
    ax_a.text(0.03, 0.96, "A   Chromosome-Scale Macrosynteny (hap1)", transform=ax_a.transAxes,
              fontsize=11.0, weight="bold", va="top")

    # Panel B: Pairwise Syntenic Depth Dosage
    ax_b = fig.add_axes([0.08, 0.08, 0.40, 0.37])
    depth_categories = ["Depth 0\n(Unmapped)", "Depth 1\n(1:1 Ortholog)", "Depth 2\n(2:2 Shared)", "Depth ≥3\n(Multi-copy)"]
    vper_depths = [1.54, 39.94, 55.67, 2.85]
    vtub_depths = [7.00, 34.86, 55.37, 2.77]

    x = np.arange(len(depth_categories))
    w = 0.36
    b1 = ax_b.bar(x - w/2, vper_depths, width=w, color=C_VPER, alpha=0.9, label="V. peripherica (hap1)", edgecolor="#333333", lw=0.7)
    b2 = ax_b.bar(x + w/2, vtub_depths, width=w, color=C_VTUB, alpha=0.9, label="V. tubiflora (hap1)", edgecolor="#333333", lw=0.7)

    for bar in b1:
        h = bar.get_height()
        ax_b.text(bar.get_x() + bar.get_width()/2, h + 1.0, f"{h:.1f}%", ha="center", va="bottom", fontsize=7.5, color=C_VPER, weight="bold")
    for bar in b2:
        h = bar.get_height()
        ax_b.text(bar.get_x() + bar.get_width()/2, h + 1.0, f"{h:.1f}%", ha="center", va="bottom", fontsize=7.5, color=C_VTUB, weight="bold")

    ax_b.set_xticks(x)
    ax_b.set_xticklabels(depth_categories, fontsize=8.5)
    ax_b.set_ylabel("Proportion of Annotated Proteome (%)", weight="bold", fontsize=9.0)
    ax_b.set_ylim(0, 68)
    ax_b.spines["top"].set_visible(False)
    ax_b.spines["right"].set_visible(False)
    ax_b.legend(frameon=False, fontsize=8.5, loc="upper right")
    ax_b.set_title("B   Pairwise Syntenic Depth Dosage", loc="left", weight="bold", fontsize=10.5)
    ax_b.text(0.04, 0.93, "Strict 1:1 / 2:2 Diploid Dosage\n(Zero Unshared Polyploidies)",
              transform=ax_b.transAxes, va="top", fontsize=8.0, weight="bold", color="#1A3B5C",
              bbox=dict(boxstyle="round,pad=0.3", facecolor="#EBF3FA", edgecolor=C_VTUB, lw=0.8))

    # Panel C: Syntenic Block Size Distribution
    ax_c = fig.add_axes([0.56, 0.08, 0.39, 0.37])
    simple_file = synteny_dir / "vper.vtub.simple"
    df_simple = pd.read_csv(simple_file, sep="\t")
    chr_mask = df_simple.iloc[:, 0].astype(str).str.contains(r"\.chr") & df_simple.iloc[:, 2].astype(str).str.contains(r"\.chr")
    df_chr = df_simple[chr_mask]
    counts = pd.to_numeric(df_chr.iloc[:, 4], errors="coerce").dropna().to_numpy()

    bins = np.logspace(np.log10(4), np.log10(4500), 22)
    ax_c.hist(counts, bins=bins, color="#4A6572", edgecolor="#232F34", lw=0.7, alpha=0.85)
    ax_c.set_xscale("log")
    ax_c.set_xlabel("Collinear Gene Pairs per Syntenic Block (log scale)", weight="bold", fontsize=9.0)
    ax_c.set_ylabel("Number of Syntenic Blocks", weight="bold", fontsize=9.0)
    ax_c.spines["top"].set_visible(False)
    ax_c.spines["right"].set_visible(False)
    ax_c.set_title("C   Syntenic Block Size Distribution", loc="left", weight="bold", fontsize=10.5)

    med = np.median(counts)
    mean_val = np.mean(counts)
    max_val = np.max(counts)
    n_total = len(counts)

    ax_c.axvline(med, color="#D95F02", linestyle="--", lw=1.4, label=f"Median: {med:.0f} genes/block")
    ax_c.legend(frameon=False, fontsize=8.5, loc="upper right")

    metrics_text = (
        f"Pseudochromosome Blocks (N = {n_total}):\n"
        f"• Median: {med:.0f} genes/block\n"
        f"• Mean: {mean_val:.1f} genes/block\n"
        f"• Max span: {max_val:.0f} genes (Chr1)\n"
        f"• Collinear anchors: 18,690 pairs"
    )
    ax_c.text(0.42, 0.80, metrics_text, transform=ax_c.transAxes, va="top", fontsize=7.8,
              bbox=dict(boxstyle="round,pad=0.3", facecolor="#F8F9FA", edgecolor="#CCCCCC", lw=0.8))

    save_publication_figure(fig, "Figure1_macrosynteny_architecture")
    plt.close(fig)
    print("Figure 1 generated successfully.")


# =============================================================================
# FIGURE 2: Chronogram, Branch Lambdas & Evolutionary Turnover Across Nodes
# =============================================================================
def plot_figure_2():
    print("Generating Figure 2: Macroevolutionary landscape & chronogram...")
    fig = plt.figure(figsize=(15.5, 7.6), dpi=300)
    gs = GridSpec(1, 2, width_ratios=[1.25, 1.0], wspace=0.36, figure=fig,
                  left=0.05, right=0.965, top=0.87, bottom=0.13)
    
    # ----------------- PANEL A: Dated Species Tree -----------------
    ax1 = fig.add_subplot(gs[0, 0])
    
    # Taxa definition
    taxa = [
        {"name": r"$\it{Vellozia\ peripherica}$ (Avoidant)", "y": 5.0, "color": C_VPER, "weight": "bold"},
        {"name": r"$\it{Vellozia\ tubiflora}$ (Resurrection)", "y": 4.0, "color": C_VTUB, "weight": "bold"},
        {"name": r"$\it{Xerophyta\ schlechteri}$ (Resurrection)", "y": 3.0, "color": "#222222", "weight": "normal"},
        {"name": r"$\it{Acanthochlamys\ bracteata}$ (Alpine)", "y": 2.0, "color": "#222222", "weight": "normal"},
        {"name": r"$\it{Pandanus\ tectorius}$ (Outgroup)", "y": 1.0, "color": "#555555", "weight": "normal"},
        {"name": r"$\it{Dioscorea\ alata}$ (Outgroup)", "y": 0.0, "color": "#555555", "weight": "normal"},
    ]
    
    def draw_branch(x_parent, y_parent, x_child, y_child, color="#333333", lw=1.8):
        ax1.plot([x_parent, x_child], [y_child, y_child], color=color, lw=lw, solid_capstyle="round")
        ax1.plot([x_parent, x_parent], [y_parent, y_child], color=color, lw=lw, solid_capstyle="round")
    
    # Draw tree backbone
    draw_branch(121.90, 0.96875, 0, 0.0, lw=2.0)
    draw_branch(121.90, 0.96875, 101.26, 1.9375, lw=2.0)
    draw_branch(101.26, 1.9375, 0, 1.0, lw=2.0)
    draw_branch(101.26, 1.9375, 78.21, 2.875, lw=2.0)
    draw_branch(78.21, 2.875, 0, 2.0, lw=2.0)
    draw_branch(78.21, 2.875, 31.91, 3.75, lw=2.0)
    draw_branch(31.91, 3.75, 0, 3.0, lw=2.0)
    draw_branch(31.91, 3.75, 9.74, 4.5, lw=2.0)
    
    # Terminal sister branches (highlighted)
    ax1.plot([9.74, 9.74], [4.0, 5.0], color="#333333", lw=2.0, solid_capstyle="round")
    ax1.plot([9.74, 0], [5.0, 5.0], color=C_VPER, lw=3.2, solid_capstyle="round")
    ax1.plot([9.74, 0], [4.0, 4.0], color=C_VTUB, lw=3.2, solid_capstyle="round")
    
    # Annotate turnover rate on focal branches
    ax1.text(4.87, 5.22, r"$\bf{\lambda = 0.00820}$ (3.9×)", color=C_VPER, fontsize=7.8, ha="center", va="bottom")
    ax1.text(4.87, 3.78, r"$\bf{\lambda = 0.00209}$ (stasis)", color=C_VTUB, fontsize=7.8, ha="center", va="top")
    
    # Terminal labels
    for t in taxa:
        ax1.text(-3.0, t["y"], t["name"], va="center", ha="left", fontsize=9.5,
                 color=t["color"], weight=t["weight"])
        
    # Geological epoch background shading
    ax1.axvspan(0, 2.58, color="#EEEEEE", alpha=0.45, zorder=0)
    ax1.axvspan(2.58, 23.03, color="#E3F2FD", alpha=0.45, zorder=0)
    ax1.axvspan(23.03, 66.0, color="#FFF8E1", alpha=0.45, zorder=0)
    ax1.axvspan(66.0, 135.0, color="#FBE9E7", alpha=0.45, zorder=0)
    
    # Epoch banner bar at bottom
    epoch_y_bottom = -0.52
    epoch_y_top = -0.28
    epochs = [
        (0, 2.58, "", "#E0E0E0"),
        (2.58, 23.03, "Neogene", "#BBDEFB"),
        (23.03, 66.0, "Paleogene", "#FFE082"),
        (66.0, 135.0, "Cretaceous", "#FFCCBC")
    ]
    for x_start, x_end, name, col in epochs:
        rect = mpatches.Rectangle((x_start, epoch_y_bottom), x_end - x_start, epoch_y_top - epoch_y_bottom,
                                 facecolor=col, edgecolor="#BDBDBD", lw=0.6, zorder=3)
        ax1.add_patch(rect)
        if name:
            ax1.text((x_start + x_end) / 2, (epoch_y_bottom + epoch_y_top) / 2, name,
                     ha="center", va="center", fontsize=7.5, weight="bold", color="#333333", zorder=4)

    # Explicit clear label for Quaternary to the right of the bar (no squished text inside 2.6 Ma box)
    ax1.text(-1.2, (epoch_y_bottom + epoch_y_top) / 2, "Quaternary (2.6–0 Ma)",
             ha="left", va="center", fontsize=7.8, weight="bold", color="#333333", zorder=4)
        
    # Node markers & callout boxes
    turnover_by_node = TURNOVER.set_index("Node_ID")
    node_info = [
        {"x": 9.74, "y": 4.5, "title": "Crown Vellozia (Node 11)",
         "sub": f"9.74 Ma (+{turnover_by_node.loc['Node 11', 'Expansions_Sig']} / -{turnover_by_node.loc['Node 11', 'Contractions_Sig']})",
         "box_xy": (23.0, 4.8), "ha": "center"},
        {"x": 31.91, "y": 3.75, "title": "Core Velloziaceae (Node 10)",
         "sub": f"31.91 Ma (+{turnover_by_node.loc['Node 10', 'Expansions_Sig']} / -{turnover_by_node.loc['Node 10', 'Contractions_Sig']})",
         "box_xy": (44.0, 3.42), "ha": "center"},
        {"x": 78.21, "y": 2.875, "title": "Velloziaceae s.l. (Node 9)",
         "sub": f"78.21 Ma (+{turnover_by_node.loc['Node 9', 'Expansions_Sig']} / -{turnover_by_node.loc['Node 9', 'Contractions_Sig']})",
         "box_xy": (88.0, 3.25), "ha": "center"},
        {"x": 101.26, "y": 1.9375, "title": "Pandanales", "sub": "101.26 Ma",
         "box_xy": (108.0, 2.3), "ha": "center"},
        {"x": 121.90, "y": 0.96875, "title": "Monocot Root", "sub": "121.90 Ma",
         "box_xy": (126.0, 1.35), "ha": "center"}
    ]
    for n in node_info:
        ax1.scatter(n["x"], n["y"], s=45, color="white", edgecolor="#222222", lw=1.5, zorder=6)
        text_content = f"{n['title']}\n{n['sub']}"
        ax1.annotate(
            text_content,
            xy=(n["x"], n["y"]),
            xytext=n["box_xy"],
            ha=n["ha"], va="center",
            fontsize=7.2, weight="bold",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor="#999999", alpha=0.92, lw=0.7),
            arrowprops=dict(arrowstyle="->", color="#666666", lw=0.7, shrinkA=3, shrinkB=4),
            zorder=7
        )
        
    # Model M5 & turnover rate summary box (top-left empty zone)
    rate_summary_text = (
        r"$\bf{CAFE5\ Macroevolutionary\ Rates\ (\lambda)}$" "\n"
        f"• V. peripherica:  λ = {SELECTED_M5.lambda_Vper:.5f} ({SELECTED_M5.Vper_to_Vtub_ratio:.1f}× accelerated)\n"
        f"• V. tubiflora:      λ = {SELECTED_M5.lambda_Vtub:.5f} (evolutionary stasis)\n"
        f"• Background:   λ = {SELECTED_M5.lambda_background:.5f} | Core Vell.: λ = {SELECTED_M5.lambda_velloziaceae:.5f}\n"
        f"Model M5 (4-λ gamma, ΔlnL = 0.0; Vper at ceiling)\n"
        f"Phylogenomics: 1,513 nuclear loci (UFBoot = 100%, LPP = 1.00)"
    )
    ax1.text(
        132.0, 5.5, rate_summary_text,
        va="top", ha="left", fontsize=7.4, fontfamily="sans-serif",
        bbox=dict(boxstyle="round,pad=0.45", facecolor="#F8F9FA", edgecolor="#B0BEC5", alpha=0.95, lw=0.9),
        zorder=8
    )
    
    # Custom bottom time axis: only from 135 to 0 (no bare line extending under taxa)
    ax1.plot([135, 0], [epoch_y_bottom, epoch_y_bottom], color="#333333", lw=0.9, zorder=5)
    for t_val in [120, 100, 80, 60, 40, 20, 0]:
        ax1.plot([t_val, t_val], [epoch_y_bottom, epoch_y_bottom - 0.07], color="#333333", lw=0.9, zorder=5)
        ax1.text(t_val, epoch_y_bottom - 0.12, str(t_val), ha="center", va="top", fontsize=8.5, color="#222222")
        
    ax1.text(67.5, epoch_y_bottom - 0.36, "Divergence Time (Million Years Ago, Ma)",
             ha="center", va="top", fontsize=9.5, weight="bold", color="#111111")
    
    # Axis styling
    ax1.set_xlim(135, -45)
    ax1.set_ylim(-0.75, 5.65)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.spines["left"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.spines["top"].set_visible(False)
    ax1.spines["bottom"].set_visible(False)
    ax1.set_title("A   Fossil-Calibrated Chronogram (1,513 Nuclear Loci)", loc="left", weight="bold", fontsize=11, pad=18)
    
    # ----------------- PANEL B: Lineage & Node Gene-Family Turnover -----------------
    ax2 = fig.add_subplot(gs[0, 1])
    
    display_order = [
        "Terminal Vper",
        "Terminal Vtub",
        "Node 11",
        "Terminal Xvis",
        "Node 10",
        "Terminal Abra",
        "Node 9",
    ]
    current = turnover_by_node.loc[display_order]
    clades = [
        r"$\it{V.\ peripherica}$",
        r"$\it{V.\ tubiflora}$",
        "Crown Vellozia (Node 11)",
        r"$\it{X.\ schlechteri}$",
        "Core Velloziaceae (Node 10)",
        r"$\it{A.\ bracteata}$",
        "Velloziaceae s.l. (Node 9)",
    ]
    expansions = current["Expansions_Sig"].astype(int).tolist()
    contractions = (-current["Contractions_Sig"].astype(int)).tolist()
    y_pos = np.arange(len(clades))
    
    bar_height = 0.36
    # Green expansions (positive)
    b_exp = ax2.barh(y_pos - bar_height/2, expansions, height=bar_height, color=C_EXP,
                     label="Expansions (p < 0.05)", edgecolor="#004D40", lw=0.8)
    # Vermilion contractions (negative)
    b_cont = ax2.barh(y_pos + bar_height/2, contractions, height=bar_height, color=C_CONT,
                      label="Contractions (p < 0.05)", edgecolor="#801500", lw=0.8)
    
    # Annotate numbers cleanly on the outside of each bar
    for val, y in zip(expansions, y_pos - bar_height/2):
        ax2.text(val + 6, y, f"+{val}", va="center", ha="left", fontsize=8.5, weight="bold", color="#004D40")
    for val, y in zip(contractions, y_pos + bar_height/2):
        ax2.text(val - 6, y, f"{val}", va="center", ha="right", fontsize=8.5, weight="bold", color="#801500")
        
    ax2.axvline(0, color="#333333", lw=1.0)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(clades, fontsize=9.2)
    ax2.invert_yaxis()
    ax2.set_xlabel("Number of Significant Gene Families (p < 0.05)", fontsize=9.5, weight="bold", labelpad=6)
    ax2.set_xlim(-125, 255)
    ax2.spines["right"].set_visible(False)
    ax2.spines["top"].set_visible(False)
    
    # Title at the top
    ax2.set_title("B   Gene Family Expansions and Contractions", loc="left", weight="bold", fontsize=11, y=1.08)
    
    # LEGEND: Placed cleanly below the title and strictly OUTSIDE the plot area!
    ax2.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=2, frameon=False,
               fontsize=9.0, handlelength=1.4, handletextpad=0.5, columnspacing=1.6)
    
    save_publication_figure(fig, "Figure2_phylogenomics_dating_turnover")
    plt.close(fig)
    print("Figure 2 generated successfully.")


# =============================================================================
# FIGURE 3: Duplication Modes Across Genomes and Expanding Gene Families
# =============================================================================
def plot_figure_3():
    print("Generating Figure 3: Physical duplication mechanisms...")
    fig = plt.figure(figsize=(13.5, 4.8), dpi=300)

    # Panel A: Baseline duplication modes across all genes
    ax_a = fig.add_axes([0.06, 0.18, 0.25, 0.70])
    dup_modes = ["Tandem", "Proximal", "WGD / Seg.", "Dispersed", "Singleton"]
    mode_columns = ["Tandem_pct", "Proximal_pct", "WGD_Segmental_pct", "Dispersed_pct", "Singleton_pct"]
    vper_all_row = DUPLICATION[(DUPLICATION.Species == "Vellozia peripherica") & DUPLICATION.Gene_Set.str.startswith("Genome-wide")].iloc[0]
    vtub_all_row = DUPLICATION[(DUPLICATION.Species == "Vellozia tubiflora") & DUPLICATION.Gene_Set.str.startswith("Genome-wide")].iloc[0]
    vper_all = [percentage_value(vper_all_row[column]) for column in mode_columns]
    vtub_all = [percentage_value(vtub_all_row[column]) for column in mode_columns]

    x = np.arange(len(dup_modes))
    w = 0.36
    ax_a.bar(x - w/2, vper_all, width=w, color=C_VPER, alpha=0.88, label="V. peripherica (all genes)", edgecolor="#333333", lw=0.7)
    ax_a.bar(x + w/2, vtub_all, width=w, color=C_VTUB, alpha=0.88, label="V. tubiflora (all genes)", edgecolor="#333333", lw=0.7)
    ax_a.set_xticks(x)
    ax_a.set_xticklabels(dup_modes, rotation=22, ha="right", fontsize=8.5)
    ax_a.set_ylabel("Proportion of Genome (%)", weight="bold", fontsize=9.0)
    ax_a.set_ylim(0, 42)
    ax_a.spines["right"].set_visible(False)
    ax_a.spines["top"].set_visible(False)
    ax_a.legend(frameon=False, fontsize=8.0, loc="upper left")
    ax_a.set_title("A   Genome-Wide Duplication Baseline", loc="left", weight="bold", fontsize=10.0, pad=10)

    # Function for forest plots B and C
    def forest(ax, species_file, title, focal_color, panel_letter):
        stats = pd.read_csv(species_file, sep="\t")
        labels = stats["DuplicationMode"].replace({"WGD/Segmental": "WGD / Seg."}).tolist()
        y = np.arange(len(stats))
        odds = stats["OddsRatio"].astype(float).to_numpy()
        lows, highs = [], []
        for row in stats.itertuples(index=False):
            cells = np.array([
                row.Genes_in_Expanded_Families,
                row.Other_Genes_in_Expanded_Families,
                row.Genes_in_Background_Families,
                row.Other_Genes_in_Background_Families,
            ], dtype=float)
            if np.any(cells == 0):
                cells += 0.5
            estimate = cells[0] * cells[3] / (cells[1] * cells[2])
            se = np.sqrt(np.sum(1.0 / cells))
            lows.append(np.exp(np.log(estimate) - 1.96 * se))
            highs.append(np.exp(np.log(estimate) + 1.96 * se))
        for i, (value, low, high, pvalue) in enumerate(zip(odds, lows, highs, stats.Fisher_Pval)):
            color = focal_color if value > 1 else C_GRAY
            ax.errorbar(value, y[i], xerr=[[value - low], [high - value]], fmt="o", color=color,
                        ecolor=color, capsize=3, markersize=6)
            ax.text(high * 1.10, y[i], f"{value:.2f}", va="center", fontsize=8.0, color=color, weight="bold")
        ax.axvline(1, color="#777777", ls="--", lw=0.9)
        ax.set_yticks(y)
        ax.set_yticklabels(labels, fontsize=8.5)
        ax.set_xscale("log")
        ax.set_xlim(0.08, max(highs) * 2.2)
        ax.set_xlabel("Odds ratio (95% Wald CI; log scale)", weight="bold", fontsize=8.5)
        ax.spines[["right", "top"]].set_visible(False)
        ax.set_title(f"{panel_letter}   {title}", loc="left", weight="bold", fontsize=10.0, pad=10)

    summary_dir = BASE_DIR / "04_gene_families/cafe5/summary"
    ax_b = fig.add_axes([0.39, 0.18, 0.26, 0.70])
    forest(ax_b, summary_dir / "duplication_enrichment_Gamma_Vper_Avoidant.tsv",
           "Mode Enrichment: V. peripherica Expansions", C_VPER, "B")
    ax_b.text(0.36, 0.94, "66.5% Local Duplicates\n(46.2% Tandem, 20.2% Proximal)",
              transform=ax_b.transAxes, va="top", fontsize=7.5, weight="bold", color="#801500",
              bbox=dict(boxstyle="round,pad=0.25", facecolor="#FFF3E0", edgecolor=C_VPER, lw=0.8))

    ax_c = fig.add_axes([0.72, 0.18, 0.25, 0.70])
    forest(ax_c, summary_dir / "duplication_enrichment_Gamma_Vtub_DT.tsv",
           "Mode Enrichment: V. tubiflora Expansions", C_VTUB, "C")
    ax_c.text(0.04, 0.94, "42.6% Singletons\n(OR = 3.60, p < 1e-11)",
              transform=ax_c.transAxes, va="top", fontsize=7.8, weight="bold", color="#12283E",
              bbox=dict(boxstyle="round,pad=0.25", facecolor="#EBF3FA", edgecolor=C_VTUB, lw=0.8))

    save_publication_figure(fig, "Figure3_duplication_mechanisms")
    plt.close(fig)
    print("Figure 3 generated successfully.")

# =============================================================================
# FIGURE 4: Functional Specialization Landscape & Odds Ratio Forest Plot
# =============================================================================
def plot_figure_4():
    print("Generating Figure 4: Dual integrated dotplot and odds ratio forest plot (Option 1)...")
    from matplotlib.ticker import ScalarFormatter
    from matplotlib.colors import Normalize
    from matplotlib.lines import Line2D

    reduced = pd.read_csv(
        BASE_DIR / "04_gene_families/functional_enrichment/results/enrichment_results_reduced_for_plotting.tsv",
        sep="\t",
    )
    accepted = {"Confirmatory", "Suggestive", "Suggestive_Imbalanced_Opportunity"}
    terms = reduced[
        reduced["Is_Primary_Inferential"].astype(bool)
        & reduced["Is_Representative"].astype(bool)
        & reduced["Evidence_Class"].isin(accepted)
    ].copy()

    if terms.empty:
        raise RuntimeError("No representative enrichment terms passed the reporting gate")

    contrast_order = [
        "BranchSig_Exp_Vper_Avoidant",
        "BranchSig_Exp_Core_Velloziaceae",
        "FamilyWide_Rapid_Evolution",
    ]

    contrast_meta = {
        "BranchSig_Exp_Vper_Avoidant": {
            "header": "V. peripherica Lineage Expansions (Avoidant Specialist)",
            "color": "#D55E00",
            "tint": "#FDF6F2",
        },
        "BranchSig_Exp_Core_Velloziaceae": {
            "header": "Core Velloziaceae Ancestral Expansions",
            "color": "#009E73",
            "tint": "#F2FAF7",
        },
        "FamilyWide_Rapid_Evolution": {
            "header": "Velloziaceae Family-Wide Rapid Turnover",
            "color": "#6A3D9A",
            "tint": "#F8F4FC",
        },
    }

    # Restrict strictly to the selected phylogenetic hierarchy clades
    terms = terms[terms["Contrast_ID"].isin(contrast_order)].copy()

    terms["Contrast_Rank"] = terms["Contrast_ID"].map({cid: i for i, cid in enumerate(contrast_order)})
    evidence_rank = {"Confirmatory": 0, "Suggestive": 1, "Suggestive_Imbalanced_Opportunity": 2}
    terms["Evidence_Rank"] = terms["Evidence_Class"].map(evidence_rank)

    # Sort logically: contrast order -> confirmatory first -> odds ratio descending
    terms = terms.sort_values(
        ["Contrast_Rank", "Evidence_Rank", "Conditional_OR"],
        ascending=[True, True, False]
    ).reset_index(drop=True)

    # Build top-down Y coordinates (matching Figure 5 architecture)
    # Within each group, rows step down by 1.0; between groups, step down by 2.4
    # to leave clean vertical space for the dashed divider and horizontal group banner.
    n_groups = sum(1 for cid in contrast_order if not terms[terms["Contrast_ID"] == cid].empty)
    total_span = len(terms) + (n_groups - 1) * 2.4
    current_y = total_span

    y_coords = []
    group_headers = []
    group_dividers = []
    group_spans = {}

    first_group = True
    for cid in contrast_order:
        sub = terms[terms["Contrast_ID"] == cid]
        if sub.empty:
            continue
        if not first_group:
            # Step down extra 1.4 (since previous loop already stepped down 1.0 -> total 2.4 gap)
            current_y -= 1.4
            group_dividers.append(current_y + 1.55)
        first_group = False

        y_top = current_y
        group_headers.append((cid, y_top + 0.68))
        for _ in range(len(sub)):
            y_coords.append(current_y)
            current_y -= 1.0
        y_bot = current_y + 1.0
        group_spans[cid] = (y_bot, y_top)

    terms["y_pos"] = y_coords

    cat_tags = {
        "GO_BP_Propagated": "[BP]",
        "GO_MF_Propagated": "[MF]",
        "GO_CC_Propagated": "[CC]",
        "KEGG_Direct": "[KEGG]",
    }

    clean_names = []
    for row in terms.itertuples():
        tag = cat_tags.get(row.Ontology_Category, "")
        tname = str(row.Term_Name).strip()
        if "carbon-oxygen lyase" in tname.lower():
            tname = "Carbon-oxygen lyase (phosphates)"
        else:
            tname = tname[0].upper() + tname[1:]
        clean_names.append(f"{tname}  {tag}")
    terms["Clean_Name"] = clean_names

    # Figure Setup (matching Figure 5 margins & proportions)
    fig = plt.figure(figsize=(15.0, 9.2), dpi=300)
    gs = GridSpec(
        1, 2,
        width_ratios=[1.12, 1.0],
        wspace=0.12,
        figure=fig,
        left=0.28,
        right=0.84,
        top=0.88,
        bottom=0.09,
    )

    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1], sharey=ax1)

    y_min = min(y_coords) - 0.85
    y_max = max(y_coords) + 1.65
    ax1.set_ylim(y_min, y_max)

    # Subtle group background blocks and row guide lines across both panels
    for cid, (y_bot, y_top) in group_spans.items():
        tint = contrast_meta[cid]["tint"]
        ax1.axhspan(y_bot - 0.42, y_top + 0.42, facecolor=tint, edgecolor="none", alpha=0.85, zorder=0)
        ax2.axhspan(y_bot - 0.42, y_top + 0.42, facecolor=tint, edgecolor="none", alpha=0.85, zorder=0)

    for y in y_coords:
        ax1.axhline(y, color="#E5E9F0", lw=0.6, zorder=1)
        ax2.axhline(y, color="#E5E9F0", lw=0.6, zorder=1)

    # Horizontal dashed dividers between groups
    for y_div in group_dividers:
        ax1.axhline(y_div, color="#B0BEC5", linestyle="--", lw=1.0, zorder=2)
        ax2.axhline(y_div, color="#B0BEC5", linestyle="--", lw=1.0, zorder=2)

    # Horizontal Group Banners above each block (Figure 5A style)
    for cid, y_hdr in group_headers:
        meta = contrast_meta[cid]
        ax1.text(
            0.008, y_hdr, meta["header"],
            fontsize=9.1, weight="bold", color=meta["color"],
            ha="left", va="bottom", zorder=5
        )

    # -------------------------------------------------------------------------
    # PANEL A: Functional Specialization Dotplot
    # -------------------------------------------------------------------------
    gene_ratio = terms["FG_Count"].astype(float) / terms["FG_Total"].astype(float)
    log_q = -np.log10(terms["q_value"].clip(lower=1e-10))
    sizes = 48 + terms["FG_Count"].to_numpy() * 7.2

    norm_q = Normalize(vmin=float(log_q.min()), vmax=float(log_q.max()))
    sc = ax1.scatter(
        gene_ratio, terms["y_pos"],
        s=sizes, c=log_q, cmap="viridis", norm=norm_q,
        edgecolor="#1A1A1A", lw=0.9, alpha=0.94, zorder=4
    )

    ax1.set_yticks(terms["y_pos"])
    ax1.set_yticklabels(terms["Clean_Name"], fontsize=8.8)
    # Highlight Confirmatory Y-tick labels in bold
    for tick_label, is_conf in zip(ax1.get_yticklabels(), terms["Evidence_Class"] == "Confirmatory"):
        if is_conf:
            tick_label.set_fontweight("bold")
            tick_label.set_color("#111111")
        else:
            tick_label.set_color("#2B2B2B")

    ax1.set_xlabel("Gene Ratio (Foreground Families / Category Total)", weight="bold", fontsize=9.8, labelpad=8)
    ax1.set_xlim(0, max(gene_ratio) * 1.16)
    ax1.grid(axis="x", linestyle=":", color="#CBD5E1", lw=0.8, zorder=1)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.spines["left"].set_color("#666666")
    ax1.spines["bottom"].set_color("#666666")
    ax1.set_title("A   Functional Specialization Landscape", loc="left", weight="bold", fontsize=11.5, pad=10)

    # -------------------------------------------------------------------------
    # PANEL B: Effect Size & Confidence Intervals (Conditional Odds Ratio)
    # -------------------------------------------------------------------------
    ax2.axvline(1.0, color="#64748B", linestyle="--", lw=1.1, zorder=2)

    for row in terms.itertuples():
        cid = row.Contrast_ID
        col = contrast_meta[cid]["color"]
        y = row.y_pos
        low, high, or_val = row.CI_95_Low, row.CI_95_High, row.Conditional_OR

        # Horizontal 95% CI bar with subtle vertical end-caps (matching Figure 3B/C)
        ax2.plot([low, high], [y, y], color=col, lw=1.9, zorder=3)
        ax2.plot([low, low], [y - 0.14, y + 0.14], color=col, lw=1.4, zorder=3)
        ax2.plot([high, high], [y - 0.14, y + 0.14], color=col, lw=1.4, zorder=3)

        if row.Evidence_Class == "Confirmatory":
            ax2.scatter(or_val, y, marker="D", s=68, color=col, edgecolor="#111111", lw=1.1, zorder=5)
            ax2.text(
                high * 1.14, y, f"{or_val:.1f}× ★",
                va="center", ha="left", fontsize=8.4, weight="bold", color=col, zorder=5
            )
        else:
            ax2.scatter(or_val, y, marker="o", s=46, color="white", edgecolor=col, lw=1.8, zorder=5)
            ax2.text(
                high * 1.14, y, f"{or_val:.1f}×",
                va="center", ha="left", fontsize=8.1, weight="medium", color="#475569", zorder=5
            )

    ax2.set_xscale("log")
    ax2.set_xlim(0.75, 950)
    ax2.set_xticks([1, 2, 5, 10, 20, 50, 100, 200])
    ax2.get_xaxis().set_major_formatter(ScalarFormatter())
    ax2.tick_params(labelleft=False)
    ax2.set_xlabel("Conditional Odds Ratio (95% CI; log scale)", weight="bold", fontsize=9.8, labelpad=8)
    ax2.grid(axis="x", linestyle=":", color="#CBD5E1", lw=0.8, zorder=1)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.spines["left"].set_color("#666666")
    ax2.spines["bottom"].set_color("#666666")
    ax2.set_title("B   Enrichment Magnitude & Evidence Calibration", loc="left", weight="bold", fontsize=11.5, pad=10)

    # -------------------------------------------------------------------------
    # RIGHT MARGIN: Colorbar & Clean Legends (No Overlap with Data)
    # -------------------------------------------------------------------------
    # 1. Vertical Colorbar for -log10(FDR q-value)
    cbar_ax = fig.add_axes([0.865, 0.56, 0.016, 0.26])
    cbar = fig.colorbar(sc, cax=cbar_ax, orientation="vertical")
    cbar.set_label(r"$-\log_{10}(\mathrm{FDR}\ q\mathrm{-value})$", weight="bold", fontsize=8.8, labelpad=6)
    cbar.ax.tick_params(labelsize=8.0)
    cbar.outline.set_linewidth(0.7)

    # 2. Dedicated Legend Axis below Colorbar on the right margin
    leg_ax = fig.add_axes([0.85, 0.10, 0.14, 0.41])
    leg_ax.axis("off")

    # Bubble Size Legend
    size_handles = [
        plt.scatter([], [], s=48 + cv * 7.2, c="#94A3B8", edgecolor="#1A1A1A", lw=0.8, label=f"{cv} families")
        for cv in [5, 25, 50]
    ]
    leg1 = leg_ax.legend(
        handles=size_handles,
        title="Foreground Count",
        loc="upper left",
        bbox_to_anchor=(0.0, 1.0),
        frameon=True,
        facecolor="#FFFFFF",
        edgecolor="#CBD5E1",
        fontsize=8.2,
        title_fontsize=8.6,
        labelspacing=1.65,
        handletextpad=1.1,
        borderpad=0.95,
    )
    leg1.get_title().set_fontweight("bold")
    leg_ax.add_artist(leg1)

    # Evidence Tier Legend
    ev_handles = [
        Line2D([0], [0], marker="D", color="w", label="Confirmatory (★)\n(10k perm. + gate)",
               markerfacecolor="#334155", markeredgecolor="#111111", markersize=7.5),
        Line2D([0], [0], marker="o", color="w", label="Qualified Suggestive\n(imbalanced opp.)",
               markerfacecolor="white", markeredgecolor="#334155", markeredgewidth=1.8, markersize=7.0),
    ]
    leg2 = leg_ax.legend(
        handles=ev_handles,
        title="Evidence Tier",
        loc="upper left",
        bbox_to_anchor=(0.0, 0.42),
        frameon=True,
        facecolor="#FFFFFF",
        edgecolor="#CBD5E1",
        fontsize=8.0,
        title_fontsize=8.6,
        labelspacing=1.05,
        borderpad=0.85,
    )
    leg2.get_title().set_fontweight("bold")

    # Super title & subtitle (matching Figure 5 style)
    fig.suptitle(
        "Functional Specialization Landscape and Covariate-Balanced Enrichment Across Evolutionary Contrasts",
        fontsize=12.2, weight="bold", y=0.96
    )
    fig.text(
        0.5, 0.93,
        "Representative GO and KEGG terms after local FDR control, 10,000 size-stratified permutations, and opportunity-balance gating",
        fontsize=9.2, ha="center", color="#4B5563"
    )

    save_publication_figure(fig, "Figure4_functional_enrichment_dotplot")
    plt.close(fig)
    print("Figure 4 generated successfully.")

# =============================================================================
# FIGURE 6: Lineage-Polarized Coding Sequence Selection (Outgroup-Calibrated)
# =============================================================================
def plot_figure_6():
    print("Generating Figure 6: Lineage-polarized coding sequence selection...")
    
    tsv_path = BASE_DIR / "04_manuscript" / "tables" / "TableS6_trio_branch_selection_polarization.tsv"
    if not tsv_path.exists():
        tsv_path = BASE_DIR.parent / "docs" / "macroevolution" / "manuscripts" / "tables" / "TableS6_trio_branch_selection_polarization.tsv"
    if not tsv_path.exists():
        print(f"Warning: {tsv_path} not found, skipping Figure 6.")
        return
        
    df = pd.read_csv(tsv_path, sep="\t")
    pass_df = df[df["QC_Status"] == "PASS"].copy()
    
    # Clean numerical values
    for col in ["Omega_M0", "Omega_Vper", "Omega_Vtub", "Omega_Xvis", "LRT_Pval"]:
        pass_df[col] = pd.to_numeric(pass_df[col], errors="coerce")
        
    fig = plt.figure(figsize=(14.0, 7.2), dpi=300)
    
    # Custom axes placement with zero layout clipping
    ax1 = fig.add_axes([0.07, 0.11, 0.38, 0.78])
    ax2 = fig.add_axes([0.53, 0.11, 0.44, 0.78])
    inset_ax = fig.add_axes([0.23, 0.49, 0.20, 0.37])
    
    # Color palette
    C_VPER = "#D55E00"  # Terracotta
    C_VTUB = "#0072B2"  # Blue
    C_BOTH = "#6A3D9A"  # Purple
    C_CONS = "#94A3B8"  # Gray
    
    # ---------------- Panel A ----------------
    vper_om = pass_df["Omega_Vper"].dropna()
    vtub_om = pass_df["Omega_Vtub"].dropna()
    
    bins_main = np.linspace(0, 2.5, 51)
    ax1.hist(vtub_om[vtub_om <= 2.5], bins=bins_main, color=C_VTUB, alpha=0.45,
             label="V. tubiflora (resurrection)", edgecolor=C_VTUB, lw=0.8)
    ax1.hist(vper_om[vper_om <= 2.5], bins=bins_main, color=C_VPER, alpha=0.40,
             label="V. peripherica (avoidant)", edgecolor=C_VPER, lw=0.8)
    
    med_vt = vtub_om.median()
    med_vp = vper_om.median()
    ax1.axvline(med_vt, color=C_VTUB, linestyle=":", lw=1.6, label=f"Median Vtub (ω = {med_vt:.3f})")
    ax1.axvline(med_vp, color=C_VPER, linestyle=":", lw=1.6, label=f"Median Vper (ω = {med_vp:.3f})")
    ax1.axvline(1.0, color="#111111", linestyle="--", lw=1.3, label="Neutral Threshold (ω = 1.0)")
    
    ax1.set_xlabel("Lineage Divergence Ratio (ω = dN / dS)", weight="bold", fontsize=10)
    ax1.set_ylabel("Number of 1:1:1 Ortholog Trios", weight="bold", fontsize=10)
    ax1.set_xlim(0, 2.5)
    ax1.spines["right"].set_visible(False)
    ax1.spines["top"].set_visible(False)
    ax1.set_title("A   Genome-Wide Selective Constraint Across Trios", loc="left", weight="bold", fontsize=11)
    ax1.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="#CBD5E1", framealpha=0.92, fontsize=8.0)
    
    # Inset for accelerated tail (omega >= 1.0)
    bins_inset = np.linspace(1.0, 3.0, 16)
    inset_ax.hist(vtub_om[(vtub_om >= 1.0) & (vtub_om <= 3.0)], bins=bins_inset, color=C_VTUB, alpha=0.6,
                  label="V. tubiflora", edgecolor="white", lw=0.5)
    inset_ax.hist(vper_om[(vper_om >= 1.0) & (vper_om <= 3.0)], bins=bins_inset, color=C_VPER, alpha=0.5,
                  label="V. peripherica", edgecolor="white", lw=0.5)
    inset_ax.set_title("Accelerated Tail (ω ≥ 1.0)", weight="bold", fontsize=8.2, pad=3)
    inset_ax.set_xlabel("Lineage ω", weight="bold", fontsize=7.6)
    inset_ax.set_ylabel("Trios", weight="bold", fontsize=7.6)
    inset_ax.tick_params(axis="both", which="major", labelsize=7.2)
    inset_ax.spines["right"].set_visible(False)
    inset_ax.spines["top"].set_visible(False)
    inset_ax.legend(loc="upper right", frameon=False, fontsize=7.0)
    
    # Counts for categories
    m_vtub = pass_df["Polarization_Call"] == "ACCELERATED_VTUB"
    m_vper = pass_df["Polarization_Call"] == "ACCELERATED_VPER"
    m_both = pass_df["Polarization_Call"] == "ACCELERATED_BOTH"
    m_bg   = ~(m_vtub | m_vper | m_both)
    
    ax1.text(0.48, 0.08,
             f"Total evaluated: 10,966 trios\n"
             f"Passed QC: {len(pass_df):,} trios\n"
             f"• Background (p ≥ 0.05 or ω ≤ 1): {m_bg.sum():,} (97.9%)\n"
             f"• Lineage-accelerated Vtub: {m_vtub.sum()} (p < 0.05)\n"
             f"• Lineage-accelerated Vper: {m_vper.sum()} (p < 0.05)\n"
             f"• Accelerated in both: {m_both.sum()} trios\n"
             f"Outgroup: Xerophyta schlechteri",
             transform=ax1.transAxes, fontsize=8.0,
             bbox=dict(boxstyle="round,pad=0.4", facecolor="#F8FAFC", edgecolor="#CBD5E1", alpha=0.92))
    
    # ---------------- Panel B ----------------
    max_lim = 3.8
    # Quadrant tints
    ax2.axhspan(1.0, max_lim, 0, 1.0 / max_lim, facecolor="#EBF5FB", alpha=0.4, zorder=0)  # Vtub upper-left
    ax2.axvspan(1.0, max_lim, 0, 1.0 / max_lim, facecolor="#FDF2E9", alpha=0.4, zorder=0)  # Vper lower-right
    ax2.axhspan(1.0, max_lim, 1.0 / max_lim, 1.0, facecolor="#F4ECF7", alpha=0.4, zorder=0) # Both upper-right
    
    ax2.axvline(1.0, color="#666666", linestyle="--", lw=1.1, zorder=1)
    ax2.axhline(1.0, color="#666666", linestyle="--", lw=1.1, zorder=1)
    diag = np.linspace(0, max_lim, 100)
    ax2.plot(diag, diag, color="#AAAAAA", linestyle=":", lw=0.9, zorder=1)
    
    # Gray background for all non-significant / conserved trios (eliminates confusing green/peach dots)
    ax2.scatter(pass_df.loc[m_bg, "Omega_Vper"], pass_df.loc[m_bg, "Omega_Vtub"],
                color=C_CONS, alpha=0.22, s=12, rasterized=True, zorder=2,
                label=f"Background / unaccelerated (n={m_bg.sum():,})")
    
    # Significant accelerated points only
    ax2.scatter(pass_df.loc[m_both, "Omega_Vper"], pass_df.loc[m_both, "Omega_Vtub"],
                color=C_BOTH, alpha=0.9, s=40, edgecolor="#3B0764", lw=0.7, zorder=3,
                label=f"Accelerated in both lineages (n={m_both.sum()})")
    
    ax2.scatter(pass_df.loc[m_vtub, "Omega_Vper"], pass_df.loc[m_vtub, "Omega_Vtub"],
                color=C_VTUB, alpha=0.92, s=52, edgecolor="#0C4A6E", lw=0.8, zorder=4,
                label=f"V. tubiflora accelerated (n={m_vtub.sum()})")
    
    ax2.scatter(pass_df.loc[m_vper, "Omega_Vper"], pass_df.loc[m_vper, "Omega_Vtub"],
                color=C_VPER, alpha=0.92, s=52, edgecolor="#7C2D12", lw=0.8, zorder=4,
                label=f"V. peripherica accelerated (n={m_vper.sum()})")
    
    # Clean candidate callout annotations (no omega numbers, no OR/q text)
    annots = [
        # Vtub points (x < 1.0, y > 1.0)
        ("Cold shock protein (CSP)", 0.512, 2.427, 0.08, 2.65, C_VTUB),
        ("Tim17/22/23 translocase", 0.003, 2.934, 0.08, 3.15, C_VTUB),
        ("S1 RNA-binding domain", 0.079, 1.306, 0.08, 1.55, C_VTUB),
        ("Lipase class 3", 0.409, 1.138, 0.08, 1.15, C_VTUB),
        # Vper points (x > 1.0, y < 1.0)
        ("Lipid transfer protein (LTP)", 2.155, 0.944, 2.10, 0.65, C_VPER),
        ("Exostosin family", 1.240, 0.013, 1.30, 0.20, C_VPER),
        ("UPF0121 stress family", 1.264, 0.0001, 1.45, 0.42, C_VPER),
        ("Glycosyl hydrolase 1", 1.064, 0.681, 1.15, 0.82, C_VPER)
    ]
    for text, x_pt, y_pt, x_txt, y_txt, col in annots:
        ax2.annotate(
            text, xy=(x_pt, y_pt), xytext=(x_txt, y_txt),
            arrowprops=dict(arrowstyle="->", color=col, lw=0.8, shrinkA=2, shrinkB=2),
            fontsize=7.8, weight="bold", color=col,
            bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor=col, alpha=0.92, lw=0.6),
            zorder=6
        )
        
    ax2.set_xlabel("Substitution Rate in V. peripherica (ω_Vper)", weight="bold", fontsize=10)
    ax2.set_ylabel("Substitution Rate in V. tubiflora (ω_Vtub)", weight="bold", fontsize=10)
    ax2.set_xlim(-0.05, max_lim)
    ax2.set_ylim(-0.05, max_lim)
    ax2.spines["right"].set_visible(False)
    ax2.spines["top"].set_visible(False)
    
    # Solid white legend positioned in front of all scatter dots (zorder=100)
    leg = ax2.legend(loc="upper right", frameon=True, facecolor="white", edgecolor="#CBD5E1",
                     framealpha=0.96, fontsize=8.2)
    leg.set_zorder(100)
    
    ax2.set_title("B   Lineage Divergence Polarized by Outgroup (Xerophyta)", loc="left", weight="bold", fontsize=11, pad=14)
    
    # Supertitle
    fig.suptitle("Lineage-Polarized Coding Sequence Selection Across Contrasting Drought Syndromes",
                 fontsize=12.2, weight="bold", y=0.97)
    
    save_publication_figure(fig, "Figure6_coding_sequence_divergence")
    plt.close(fig)
    print("Figure 6 generated successfully.")

if __name__ == "__main__":
    plot_figure_1()
    plot_figure_2()
    plot_figure_3()
    plot_figure_4()
    plot_figure_6()
    print("=== ALL MANUSCRIPT FIGURES GENERATED SUCCESSFULLY ===")

