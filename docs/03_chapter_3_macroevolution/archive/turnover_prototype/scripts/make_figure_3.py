#!/usr/bin/env python3
"""
Figure 3: Stochastic Gene Family Dynamics and Asymmetric Expansions ("The Genomic Burden of Being Evergreen")
Publication-ready 2-column figure for Chapter 2 (Macroevolution in Velloziaceae).

Author: Mariana Feitosa Cavalheiro
Date: September 2026
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyBboxPatch, Rectangle

# -------------------------------------------------------------------------
# Style & Publication Settings (Nature Standard)
# -------------------------------------------------------------------------
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['font.size'] = 7.5
plt.rcParams['axes.labelsize'] = 8
plt.rcParams['axes.titlesize'] = 8.5
plt.rcParams['xtick.labelsize'] = 7
plt.rcParams['ytick.labelsize'] = 7
plt.rcParams['legend.fontsize'] = 6.5
plt.rcParams['axes.linewidth'] = 0.6
plt.rcParams['lines.linewidth'] = 1.0
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

# -------------------------------------------------------------------------
# Color Palette (Colorblind-safe: Okabe-Ito / Tol)
# -------------------------------------------------------------------------
C_GAIN = '#009E73'      # Emerald Green (Expansion / Gain)
C_LOSS = '#D55E00'      # Vermilion Red (Contraction / Loss)
C_VTUB = '#E69F00'      # Golden Amber (Vellozia tubiflora - Resurrection)
C_VPER = '#0072B2'      # Deep Cobalt Blue (Vellozia peripherica - Evergreen)
C_ANCESTRAL = '#8E44AD' # Orchid Purple (Ancestral Node 9 MRCA)

def plot_panel_a_tree(ax):
    """Panel A: Time-calibrated phylogeny with CAFE5 Gamma gains/losses and divergence ages."""
    ax.set_title("Stochastic Birth-and-Death Dynamics (CAFE5 $\lambda=0.638$)", fontsize=8.2, fontweight='bold', pad=12, loc='left')
    
    # Range: 0.0 to 1.0 in X and Y
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(-0.25, 1.05)
    ax.axis('off')
    
    # Linear mapping: 140 Ma -> 0.04, 0 Ma -> 0.44 (tip line)
    def age_to_x(age):
        return 0.04 + 0.40 * (1.0 - (float(age) / 140.0))

    # Timescale Bar at bottom
    epochs = [
        (138.48, 66.0, "Cretaceous", "#BFE3C5"),
        (66.0, 56.0, "Pal", "#FDAE6B"),
        (56.0, 33.9, "Eocene", "#FDD0A2"),
        (33.9, 23.0, "Olig", "#FEE6CE"),
        (23.0, 5.3, "Miocene", "#FFF5EB"),
        (5.3, 0.0, "P/P", "#E0F3F8")
    ]
    
    y_bar = -0.19
    h_bar = 0.075
    for start, end, label, col in epochs:
        x_start = age_to_x(start)
        x_end = age_to_x(end)
        w = x_end - x_start
        rect = Rectangle((x_start, y_bar), w, h_bar, facecolor=col, edgecolor='white', linewidth=0.5, alpha=0.95)
        ax.add_patch(rect)
        if w > 0.035:
            ax.text(x_start + w/2, y_bar + h_bar/2, label, ha='center', va='center', fontsize=5.5, fontweight='bold', color='#2C3E50')
        else:
            ax.text(x_start + w/2, y_bar + h_bar/2, label, ha='center', va='center', fontsize=4.5, color='#2C3E50')

    # Y positions of tips
    y_tips = {
        'ath': 0.95,
        'ptec': 0.77,
        'abra': 0.59,
        'xvis': 0.41,
        'vper': 0.23,
        'vtub': 0.05
    }
    
    # Node X coordinates
    x_root = age_to_x(138.48)
    x_ptec_root = age_to_x(101.26)
    x_abra_root = age_to_x(78.21)
    x_node9 = age_to_x(31.92)
    x_node10 = age_to_x(9.74)
    x_tip = age_to_x(0.0)  # exactly 0.44
    
    y_node10 = (y_tips['vper'] + y_tips['vtub']) / 2.0
    y_node9 = (y_tips['xvis'] + y_node10) / 2.0
    y_abra_root = (y_tips['abra'] + y_node9) / 2.0
    y_ptec_root = (y_tips['ptec'] + y_abra_root) / 2.0

    kw_branch = dict(color='#2C3E50', linewidth=1.1)
    
    # 1. Root
    ax.plot([x_root, x_root], [y_tips['ath'], y_ptec_root], **kw_branch)
    ax.plot([x_root, x_tip], [y_tips['ath'], y_tips['ath']], **kw_branch)
    ax.plot([x_root, x_ptec_root], [y_ptec_root, y_ptec_root], **kw_branch)
    
    # 2. Pandanales
    ax.plot([x_ptec_root, x_ptec_root], [y_tips['ptec'], y_abra_root], **kw_branch)
    ax.plot([x_ptec_root, x_tip], [y_tips['ptec'], y_tips['ptec']], **kw_branch)
    ax.plot([x_ptec_root, x_abra_root], [y_abra_root, y_abra_root], **kw_branch)
    
    # 3. Crown Velloziaceae
    ax.plot([x_abra_root, x_abra_root], [y_tips['abra'], y_node9], **kw_branch)
    ax.plot([x_abra_root, x_tip], [y_tips['abra'], y_tips['abra']], **kw_branch)
    ax.plot([x_abra_root, x_node9], [y_node9, y_node9], **kw_branch)
    
    # 4. Core Velloziaceae (Node 9)
    ax.plot([x_node9, x_node9], [y_tips['xvis'], y_node10], **kw_branch)
    ax.plot([x_node9, x_tip], [y_tips['xvis'], y_tips['xvis']], **kw_branch)
    ax.plot([x_node9, x_node10], [y_node10, y_node10], **kw_branch)
    
    # 5. Vellozia MRCA (Node 10)
    ax.plot([x_node10, x_node10], [y_tips['vper'], y_tips['vtub']], **kw_branch)
    ax.plot([x_node10, x_tip], [y_tips['vper'], y_tips['vper']], **kw_branch)
    ax.plot([x_node10, x_tip], [y_tips['vtub'], y_tips['vtub']], **kw_branch)

    # Tip Labels (Placed neatly with right alignment or explicit X)
    tips_info = [
        ('ath', "A. thaliana (Ath)", "#7F8C8D", False),
        ('ptec', "P. tectorius (Ptec)", "#7F8C8D", False),
        ('abra', "A. bracteata (Abra)", "#7F8C8D", False),
        ('xvis', "X. viscosa (Xvis)", "#D35400", False),
        ('vper', "V. peripherica (Vper)", C_VPER, True),
        ('vtub', "V. tubiflora (Vtub)", C_VTUB, True),
    ]
    for key, name, col, is_bold in tips_info:
        y = y_tips[key]
        ax.text(x_tip + 0.015, y, name, ha='left', va='center', fontsize=6.1, 
                fontweight='bold' if is_bold else 'normal', color=col)

    # Badges on Branches
    def draw_badge(x, y, gain, loss, note=None, note_pos='top'):
        bbox_props = dict(boxstyle='round,pad=0.18', facecolor='white', edgecolor='#95A5A6', linewidth=0.5, alpha=0.95)
        text = f"+{gain} / -{loss}"
        ax.text(x, y, text, ha='center', va='center', fontsize=5.1, fontweight='bold', bbox=bbox_props,
                color='#196F3D' if gain > loss else '#943126', zorder=10)
        if note:
            y_offset = 0.042 if note_pos == 'top' else -0.042
            ax.text(x, y + y_offset, note, ha='center', va='center', fontsize=4.7, fontweight='bold', 
                    color=C_ANCESTRAL if 'Node' in note else '#2C3E50', zorder=10)

    draw_badge(0.20, y_tips['ptec'], 219, 34)
    draw_badge(0.25, y_tips['abra'], 56, 0)
    draw_badge(0.38, y_tips['xvis'], 196, 20)
    
    draw_badge(x_node9 - 0.015, y_node9, 218, 11, note="Node 9 (31.92 Ma)", note_pos='top')
    draw_badge(x_node10 + 0.01, y_node10, 66, 8, note="Node 10 (9.74 Ma)", note_pos='bottom')
    
    draw_badge(0.40, y_tips['vper'], 341, 140)
    draw_badge(0.40, y_tips['vtub'], 124, 148)

    # Core Velloziaceae Toolkit Banner
    rect_burst = FancyBboxPatch((x_node9 - 0.14, y_node9 + 0.055), 0.28, 0.075, boxstyle="round,pad=0.01", 
                                fc='#F4ECF7', ec=C_ANCESTRAL, lw=0.6, alpha=0.95)
    ax.add_patch(rect_burst)
    ax.text(x_node9, y_node9 + 0.092, "Ancestral Anhydrobiosis Toolkit (31.92 Ma)\n+218: LEA, sHSPs, RFO synthases, Sucrose",
            ha='center', va='center', fontsize=4.6, color='#5B2C6F', fontweight='bold')


def plot_panel_b_enrichment(ax):
    """Panel B: Divergent Functional Enrichment Barplots contrasting Vtub vs Vper."""
    ax.set_title("Top Lineage-Specific Functional Expansions (Net Genes)", fontsize=8.2, fontweight='bold', pad=12, loc='left')
    
    categories = [
        # Vper Evergreen Expansions
        ("LRR-RLK Turgor/Stress Kinases", 150, "Vper", C_VPER),
        ("Cytochrome P450 Monooxygenases", 88, "Vper", C_VPER),
        ("F-box & E3 Ubiquitin Ligases", 72, "Vper", C_VPER),
        ("WAKs & UDP-Glycosyltransferases", 41, "Vper", C_VPER),
        ("NLR (NBS-LRR) Immune Sentinels", 39, "Vper", C_VPER),
        # Vtub Resurrection Expansions
        ("Plastid Translocons (TOC/TIC)", 77, "Vtub", C_VTUB),
        ("Chloroplastic NDH Complex (CEF)", 71, "Vtub", C_VTUB),
        ("PSII Core Stabilizers (PsbO/P/Q)", 24, "Vtub", C_VTUB),
        ("FA & Wax Synthesis (ACC $\\beta$)", 23, "Vtub", C_VTUB),
        ("Group II RNA Maturases (matK)", 23, "Vtub", C_VTUB),
    ]
    
    y_pos = np.arange(len(categories))
    labels = [c[0] for c in categories]
    values = [c[1] for c in categories]
    colors = [c[3] for c in categories]
    
    bars = ax.barh(y_pos, values, color=colors, height=0.68, edgecolor='none', alpha=0.9)
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=6.6)
    ax.invert_yaxis()
    ax.set_xlabel("Net Expanded Gene Count ($\Delta$ Genes in Expanded OGs)", fontsize=7.2)
    ax.set_xlim(0, 195)
    ax.grid(axis='x', linestyle='--', alpha=0.4, color='#BDC3C7')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    for bar, val, cat in zip(bars, values, categories):
        w = bar.get_width()
        y = bar.get_y() + bar.get_height()/2
        ax.text(w + 3, y, f"+{val}", va='center', ha='left', fontsize=6.3, fontweight='bold', color=bar.get_facecolor())

    ax.text(190, 1.8, "V. peripherica (Evergreen)\nTotal Expansions: +723 Net", ha='right', va='center',
            fontsize=5.8, fontweight='bold', color=C_VPER, bbox=dict(boxstyle='square,pad=0.3', fc='#EBF5FB', ec=C_VPER, lw=0.6))
    ax.text(190, 7.5, "V. tubiflora (Resurrection)\nTotal Expansions: +194 Net", ha='right', va='center',
            fontsize=5.8, fontweight='bold', color=C_VTUB, bbox=dict(boxstyle='square,pad=0.3', fc='#FEF9E7', ec=C_VTUB, lw=0.6))


def plot_panel_c_trajectories(ax):
    """Panel C: Diagnostic Gene Family Trajectories (Slopechart Node 10 MRCA -> Vtub vs Vper)."""
    ax.set_title("Paralog Copy-Number Trajectories (MRCA $\\rightarrow$ Extant)", fontsize=8.2, fontweight='bold', pad=12, loc='left')
    
    fams = [
        ("OG16", "OG16 (TOC75/TIC110)", 12, 67, 14, C_VTUB, 0, 0),
        ("OG36", "OG36 (NDH Complex)", 8, 37, 10, C_VTUB, 0, 0),
        ("OG69", "OG69 (PSII Core Stabilizer)", 4, 18, 5, C_VTUB, 0, 0),
        ("OG12", "OG12 (LRR-RLK Kinases)", 14, 16, 71, C_VPER, 0, 0),
        ("OG26", "OG26 (F-box / SCF)", 9, 11, 60, C_VPER, 0, 0),
        ("OG50", "OG50 (TIR-NBS-LRR)", 4, 5, 26, C_VPER, 0, 0),
    ]
    
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["Node 10 MRCA\n(9.74 Ma)", "V. tubiflora\n(Resurrection)", "V. peripherica\n(Evergreen)"], fontsize=6.8)
    ax.set_ylabel("Gene Copy Number per Genome", fontsize=7.2)
    ax.set_xlim(-0.25, 2.5)
    ax.set_ylim(0, 85)
    ax.grid(axis='y', linestyle='--', alpha=0.3, color='#BDC3C7')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    for og, label, n10, vtub, vper, col, off_vtub, off_vper in fams:
        ax.plot([0, 1], [n10, vtub], color=col if col == C_VTUB else '#BDC3C7', lw=1.2, alpha=0.85)
        ax.plot([0, 2], [n10, vper], color=col if col == C_VPER else '#BDC3C7', lw=1.2, alpha=0.85, linestyle='--' if col == C_VPER else '-')
        ax.scatter([0, 1, 2], [n10, vtub, vper], color=col, s=20, zorder=5, edgecolor='white', lw=0.5)
        
        if col == C_VTUB:
            ax.text(1.05, vtub + off_vtub, f"{label}: {vtub}", ha='left', va='center', fontsize=5.6, fontweight='bold', color=C_VTUB)
        else:
            ax.text(2.05, vper + off_vper, f"{label}: {vper}", ha='left', va='center', fontsize=5.6, fontweight='bold', color=C_VPER)

    ax.text(0.95, 78, "Resurrection Focus:\nTOC/TIC & NDH Hubs", ha='center', va='top', fontsize=5.8, color=C_VTUB, fontweight='bold')
    ax.text(2.0, 78, "Evergreen Focus:\nLRR-RLK, F-box, NLRs", ha='center', va='top', fontsize=5.8, color=C_VPER, fontweight='bold')


def plot_panel_d_synthesis(ax):
    """Panel D: Synthesis Framework: The Genomic Burden of Being Evergreen."""
    ax.set_title("Evolutionary Paradigm: Anhydrobiosis vs. Evergreen Burden", fontsize=8.2, fontweight='bold', pad=12, loc='left')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    # Outer frame
    card = FancyBboxPatch((0.01, 0.01), 0.98, 0.98, boxstyle="round,pad=0.01", 
                          fc='#FBFCFC', ec='#BDC3C7', lw=0.7)
    ax.add_patch(card)
    
    # Box 1: Quiescent Desiccation Strategy (Top)
    box_vtub = FancyBboxPatch((0.03, 0.52), 0.94, 0.45, boxstyle="round,pad=0.015", 
                              fc='#FEF9E7', ec=C_VTUB, lw=0.85)
    ax.add_patch(box_vtub)
    ax.text(0.06, 0.92, "Vellozia tubiflora — Quiescent Protection Strategy", fontsize=7.0, fontweight='bold', color=C_VTUB)
    
    txt_vtub = (
        "• Habitat: Exposed bare rock inselbergs (Water potential $\Psi < -100\,$MPa)\n"
        "• Phenotype: Poikilochlorophylly, complete desiccoplast dismantling & vitrification\n"
        "• Genomic Footprint: Streamlined turnover (+194 net family balance)\n"
        "• Specialized Expansions: TOC/TIC plastid translocons (+77 genes) &\n"
        "  chloroplastic NDH complexes (+71 genes) for rapid post-drought re-greening\n"
        "• Outcome: Near-zero mortality under extreme desiccation; low carbon assimilation"
    )
    ax.text(0.06, 0.86, txt_vtub, fontsize=5.5, color='#2C3E50', va='top', linespacing=1.35)

    # Box 2: Continuous Foliar Maintenance Strategy (Bottom)
    box_vper = FancyBboxPatch((0.03, 0.03), 0.94, 0.45, boxstyle="round,pad=0.015", 
                              fc='#EBF5FB', ec=C_VPER, lw=0.85)
    ax.add_patch(box_vper)
    ax.text(0.06, 0.43, "Vellozia peripherica — 'The Genomic Burden of Being Evergreen'", fontsize=7.0, fontweight='bold', color=C_VPER)
    
    txt_vper = (
        "• Habitat: Shaded, soil-accumulating rock fissures ($\Psi \approx -1.5\,$MPa)\n"
        "• Phenotype: Homoiochlorophylly, active evergreen foliage year-round\n"
        "• Genomic Footprint: Massive ~3.7x expansion burst (+723 net balance)\n"
        "• Specialized Expansions: LRR-RLK turgor sentinels (+150 genes), F-box\n"
        "  proteostasis (+72), P450 detox (+88), and NLR immune defense (+39)\n"
        "• Outcome: Continuous carbon gain; chronic photo-oxidation and cavitation risk"
    )
    ax.text(0.06, 0.37, txt_vper, fontsize=5.5, color='#2C3E50', va='top', linespacing=1.35)


def main():
    print("[1/3] Initializing Figure 3 canvas (180 mm x 210 mm; Nature 2-column format)...")
    fig = plt.figure(figsize=(7.0866, 8.2677), dpi=300)
    
    # 2x2 GridSpec with balanced proportions
    gs = gridspec.GridSpec(2, 2, height_ratios=[1.15, 0.85], width_ratios=[1.0, 1.0],
                           hspace=0.28, wspace=0.30, left=0.04, right=0.98, top=0.95, bottom=0.05)
    
    ax_a = fig.add_subplot(gs[0, 0])
    ax_b = fig.add_subplot(gs[0, 1])
    ax_c = fig.add_subplot(gs[1, 0])
    ax_d = fig.add_subplot(gs[1, 1])
    
    # Bold Panel Tags
    ax_a.text(-0.02, 1.05, 'A', transform=ax_a.transAxes, fontsize=10, fontweight='bold', va='bottom', ha='right')
    ax_b.text(-0.08, 1.05, 'B', transform=ax_b.transAxes, fontsize=10, fontweight='bold', va='bottom', ha='right')
    ax_c.text(-0.02, 1.05, 'C', transform=ax_c.transAxes, fontsize=10, fontweight='bold', va='bottom', ha='right')
    ax_d.text(-0.08, 1.05, 'D', transform=ax_d.transAxes, fontsize=10, fontweight='bold', va='bottom', ha='right')
    
    print("[2/3] Rendering Panels A, B, C, and D...")
    plot_panel_a_tree(ax_a)
    plot_panel_b_enrichment(ax_b)
    plot_panel_c_trajectories(ax_c)
    plot_panel_d_synthesis(ax_d)
    
    out_dir = "teamwork/figures_chapter2/figures"
    os.makedirs(out_dir, exist_ok=True)
    
    pdf_path = os.path.join(out_dir, "figure_3_gene_families_turnover.pdf")
    png_path = os.path.join(out_dir, "figure_3_gene_families_turnover.png")
    
    print(f"[3/3] Exporting publication figures:")
    print(f"  -> Vector PDF: {pdf_path}")
    fig.savefig(pdf_path, format='pdf', dpi=300, bbox_inches='tight')
    
    print(f"  -> High-Res PNG (300 DPI): {png_path}")
    fig.savefig(png_path, format='png', dpi=300, bbox_inches='tight')
    
    plt.close(fig)
    print("SUCCESS: Figure 3 rendering and export completed cleanly!")

if __name__ == '__main__':
    main()
