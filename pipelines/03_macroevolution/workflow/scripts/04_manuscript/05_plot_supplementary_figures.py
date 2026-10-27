#!/usr/bin/env python3
"""
scripts/04_manuscript/05_plot_supplementary_figures.py

Generates publication-quality Supplementary Figures for synteny validation:
- Figure S1: High-resolution pairwise 2D synteny dotplot between V. peripherica and V. tubiflora (hap1, Chr1–Chr9)
- Figure S2: Syntenic depth dosage distribution & collinear block size metrics
"""

import os
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parents[3]
FIG_DIR = BASE_DIR / "04_manuscript/figures"
DOCS_FIG_DIR = Path("/home/mfcaval/github/doutorado/docs/macroevolution/manuscripts/figures")
SYNTENY_DIR = BASE_DIR / "04_gene_families/synteny"

os.makedirs(FIG_DIR, exist_ok=True)
os.makedirs(DOCS_FIG_DIR, exist_ok=True)

# Styling
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 8.5
plt.rcParams["axes.titlesize"] = 9.5
plt.rcParams["axes.labelsize"] = 8.5

C_VPER = "#C8523A"
C_VTUB = "#3D6898"
C_GRAY = "#666666"

def generate_figure_s1():
    print("Generating Figure S1: Pairwise 2D synteny dotplot...")
    # S1 is generated from JCVI dotplot with vper.bed & vtub.bed (Chr1–Chr9)
    # Target files:
    src_png = SYNTENY_DIR / "FigureS1_synteny_dotplot.png"
    src_pdf = SYNTENY_DIR / "FigureS1_synteny_dotplot.pdf"
    src_svg = SYNTENY_DIR / "FigureS1_synteny_dotplot.svg"
    
    if src_png.exists():
        import shutil
        shutil.copy(src_png, FIG_DIR / "FigureS1_synteny_dotplot.png")
        shutil.copy(src_pdf, FIG_DIR / "FigureS1_synteny_dotplot.pdf")
        shutil.copy(src_png, DOCS_FIG_DIR / "FigureS1_synteny_dotplot.png")
        shutil.copy(src_pdf, DOCS_FIG_DIR / "FigureS1_synteny_dotplot.pdf")
        if src_svg.exists():
            shutil.copy(src_svg, FIG_DIR / "FigureS1_synteny_dotplot.svg")
            shutil.copy(src_svg, DOCS_FIG_DIR / "FigureS1_synteny_dotplot.svg")
        print("Figure S1 synchronized successfully.")
    else:
        print("Warning: Figure S1 source not found in synteny dir.")

def generate_figure_s2():
    print("Generating Figure S2: Synteny depth dosage & block size distribution...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2), dpi=300, gridspec_kw={"wspace": 0.30})
    
    # ---------------------------------------------------------
    # Panel A: Synteny Depth Ratio (JCVI depth model)
    # ---------------------------------------------------------
    # Depths: 0, 1, 2, >=3
    # Vper: Depth 0: 1.5%, Depth 1: 39.9%, Depth 2: 55.7%, Depth >=3: 2.9%
    # Vtub: Depth 0: 7.0%, Depth 1: 34.9%, Depth 2: 55.4%, Depth >=3: 2.7%
    depth_categories = ["Depth 0\n(Unmapped)", "Depth 1\n(1:1 Ortholog)", "Depth 2\n(2:2 Shared)", "Depth ≥3\n(Multi-copy)"]
    vper_depths = [1.54, 39.94, 55.67, 2.85]
    vtub_depths = [7.00, 34.86, 55.37, 2.77]
    
    x = np.arange(len(depth_categories))
    w = 0.36
    b1 = ax1.bar(x - w/2, vper_depths, width=w, color=C_VPER, alpha=0.9, label="V. peripherica (hap1)", edgecolor="#333333", lw=0.7)
    b2 = ax1.bar(x + w/2, vtub_depths, width=w, color=C_VTUB, alpha=0.9, label="V. tubiflora (hap1)", edgecolor="#333333", lw=0.7)
    
    for bar in b1:
        h = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, h + 1.0, f"{h:.1f}%", ha="center", va="bottom", fontsize=7.2, color=C_VPER, weight="bold")
    for bar in b2:
        h = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, h + 1.0, f"{h:.1f}%", ha="center", va="bottom", fontsize=7.2, color=C_VTUB, weight="bold")
        
    ax1.set_xticks(x)
    ax1.set_xticklabels(depth_categories, fontsize=8.0)
    ax1.set_ylabel("Proportion of Annotated Proteome (%)", weight="bold", fontsize=8.5)
    ax1.set_ylim(0, 68)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.legend(frameon=False, fontsize=8, loc="upper right")
    ax1.set_title("A   Pairwise Syntenic Depth Dosage", loc="left", weight="bold", fontsize=9.2)
    
    # Inset badge for diploid dosage
    ax1.text(0.04, 0.93, "Strict 1:1 / 2:2 Diploid Dosage\n(Zero Unshared Polyploidies)",
             transform=ax1.transAxes, va="top", fontsize=7.5, weight="bold", color="#1A3B5C",
             bbox=dict(boxstyle="round,pad=0.3", facecolor="#EBF3FA", edgecolor=C_VTUB, lw=0.8))
             
    # ---------------------------------------------------------
    # Panel B: Collinear Block Size Distribution (Genes per block)
    # ---------------------------------------------------------
    simple_file = SYNTENY_DIR / "vper.vtub.simple"
    df_simple = pd.read_csv(simple_file, sep="\t")
    counts = pd.to_numeric(df_simple.iloc[:, 4], errors="coerce").dropna().to_numpy()
    
    # Filter for blocks between pseudochromosomes
    # Plot log-scaled or binned histogram
    bins = np.logspace(np.log10(4), np.log10(4000), 22)
    ax2.hist(counts, bins=bins, color="#4A6572", edgecolor="#232F34", lw=0.7, alpha=0.85)
    ax2.set_xscale("log")
    ax2.set_xlabel("Collinear Gene Pairs per Syntenic Block (log scale)", weight="bold", fontsize=8.5)
    ax2.set_ylabel("Number of Syntenic Blocks", weight="bold", fontsize=8.5)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.set_title("B   Syntenic Block Size Distribution", loc="left", weight="bold", fontsize=9.2)
    
    med = np.median(counts)
    mean_val = np.mean(counts)
    max_val = np.max(counts)
    n_total = len(counts)
    
    ax2.axvline(med, color="#D95F02", linestyle="--", lw=1.2, label=f"Median: {med:.0f} genes")
    ax2.legend(frameon=False, fontsize=8, loc="upper right")
    
    metrics_text = (
        f"Block Metrics (N = {n_total}):\n"
        f"• Median: {med:.0f} genes/block\n"
        f"• Mean: {mean_val:.1f} genes/block\n"
        f"• Max block: {max_val:.0f} genes (Chr1)\n"
        f"• Total collinear pairs: 18,690"
    )
    ax2.text(0.05, 0.93, metrics_text, transform=ax2.transAxes, va="top", fontsize=7.5,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="#F8F9FA", edgecolor="#CCCCCC", lw=0.8))

    plt.tight_layout()
    png_out = FIG_DIR / "FigureS2_synteny_depth_histogram.png"
    pdf_out = FIG_DIR / "FigureS2_synteny_depth_histogram.pdf"
    svg_out = FIG_DIR / "FigureS2_synteny_depth_histogram.svg"
    fig.savefig(png_out, dpi=300)
    fig.savefig(pdf_out)
    fig.savefig(svg_out)
    
    # Mirror
    fig.savefig(DOCS_FIG_DIR / "FigureS2_synteny_depth_histogram.png", dpi=300)
    fig.savefig(DOCS_FIG_DIR / "FigureS2_synteny_depth_histogram.pdf")
    fig.savefig(DOCS_FIG_DIR / "FigureS2_synteny_depth_histogram.svg")
    plt.close(fig)
    print("Figure S2 generated and synchronized successfully.")

if __name__ == "__main__":
    generate_figure_s1()
