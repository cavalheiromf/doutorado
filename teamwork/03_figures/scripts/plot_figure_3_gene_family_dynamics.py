#!/usr/bin/env python3
"""
Figure 3: Macroevolutionary Gene Family Dynamics (CAFE5) and Functional Enrichment
Panel A: Species Tree with Expansion/Contraction Badges
Panel B: Functional Enrichment Bubble Plot (Fold vs -log10 q-value)
Panel C: Adaptive Gene Family Expansion/Contraction Dynamics Matrix
Enforces anti-clipping padding and zero text overlap.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import sqlite3
import pandas as pd

# Global typography
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 8
plt.rcParams['axes.labelsize'] = 8.5
plt.rcParams['axes.titlesize'] = 9.5
plt.rcParams['xtick.labelsize'] = 7.5
plt.rcParams['ytick.labelsize'] = 7.5
plt.rcParams['legend.fontsize'] = 7.5

out_dir = '/home/mfcaval/github/doutorado/teamwork/figures'
os.makedirs(out_dir, exist_ok=True)
os.makedirs(os.path.join(out_dir, 'scripts'), exist_ok=True)

# 175mm x 150mm figure (6.89 x 5.91 inches)
fig = plt.figure(figsize=(6.89, 5.91), dpi=300)

gs = fig.add_gridspec(2, 2, height_ratios=[1.0, 1.15], width_ratios=[0.85, 1.15], hspace=0.38, wspace=0.32,
                       left=0.08, right=0.96, top=0.94, bottom=0.08)

# -------------------------------------------------------------
# Panel A: Species Tree with Expansion/Contraction Node Badges
# -------------------------------------------------------------
ax_a = fig.add_subplot(gs[0, 0])
ax_a.set_xlim(-15, 160)
ax_a.set_ylim(-0.5, 3.5)
ax_a.axis('off')

y_ath = 2.8
y_vper = 1.6
y_vtub = 0.4
y_node_vel = 1.0
y_root = 1.9

x_root = 145
x_vel_node = 25
x_tips = 0

# Draw branches
ax_a.plot([x_root, x_root, x_tips], [y_root, y_ath, y_ath], color='#444444', lw=2.0)
ax_a.plot([x_root, x_root, x_vel_node], [y_root, y_node_vel, y_node_vel], color='#444444', lw=2.0)
ax_a.plot([x_vel_node, x_vel_node, x_tips], [y_node_vel, y_vper, y_vper], color='#444444', lw=2.0)
ax_a.plot([x_vel_node, x_vel_node, x_tips], [y_node_vel, y_vtub, y_vtub], color='#444444', lw=2.0)

# Time axis
ax_a.plot([145, 0], [-0.3, -0.3], color='#888888', lw=1.0)
for t in [145, 100, 50, 25, 0]:
    ax_a.plot([t, t], [-0.3, -0.22], color='#888888', lw=1.0)
    ax_a.text(t, -0.42, f'{t}', ha='center', va='top', fontsize=6.5, color='#555555')
ax_a.text(72.5, -0.70, 'Divergence Time (Mya)', ha='center', va='top', fontsize=7, color='#333333')

# Tip labels
ax_a.text(x_tips - 3, y_ath, 'Arabidopsis thaliana\n(Outgroup)', ha='right', va='center', fontsize=7.2, fontweight='bold', color='#0072B2')
ax_a.text(x_tips - 3, y_vper, 'Vellozia peripherica\n(Evergreen)', ha='right', va='center', fontsize=7.2, fontweight='bold', color='#009E73')
ax_a.text(x_tips - 3, y_vtub, 'Vellozia tubiflora\n(Resurrection)', ha='right', va='center', fontsize=7.2, fontweight='bold', color='#E69F00')

# CAFE Node Badges
def draw_badge(ax, x, y, exp, cont):
    txt = f"+{exp} / -{cont}"
    ax.text(x, y, txt, ha='center', va='center', fontsize=6.8, fontweight='bold', color='#111111',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#F0F0F0', edgecolor='#888888', alpha=0.9))

draw_badge(ax_a, 12, y_vtub + 0.30, 924, 147)
draw_badge(ax_a, 12, y_vper + 0.30, 1549, 84)
draw_badge(ax_a, 50, y_ath + 0.30, 812, 320)
draw_badge(ax_a, 85, y_node_vel + 0.30, 642, 210)

ax_a.text(75, 3.2, 'CAFE5 Model (λ = 0.07456)\n412 Significant Families (p ≤ 0.05)', ha='center', va='center',
          fontsize=7.0, fontweight='bold', color='#333333', bbox=dict(boxstyle='square,pad=0.3', facecolor='#FFF8E7', edgecolor='#E69F00', alpha=0.8))

ax_a.text(-0.15, 1.08, 'A', transform=ax_a.transAxes, fontsize=12, fontweight='bold', va='top')

# -------------------------------------------------------------
# Panel B: Functional Enrichment Bubble Plot
# -------------------------------------------------------------
ax_b = fig.add_subplot(gs[0, 1])

enrichment_data = [
    # Vtub
    ('Plastid Translocon (TOC/TIC)', 13.60, 113.2, 103, 'Vtub'),
    ('NDH Electron Transport', 11.25, 100.6, 112, 'Vtub'),
    ('Organonitrogen Metabolism', 13.06, 84.3, 81, 'Vtub'),
    ('Plastid Ribosome (16S rRNA)', 9.45, 35.5, 47, 'Vtub'),
    ('Acetyl-CoA Carboxylase (ACC)', 13.87, 25.1, 23, 'Vtub'),
    ('PSII Core / Reaction Center', 9.25, 17.8, 24, 'Vtub'),
    ('Plant Mobile Transposases', 6.70, 23.9, 43, 'Vtub'),
    # Vper
    ('LRR Receptor Kinases', 5.57, 54.7, 110, 'Vper'),
    ('U-box E3 Ubiquitin Ligases', 6.41, 36.1, 63, 'Vper'),
    ('UDP-Glycosyltransferases', 4.97, 34.1, 78, 'Vper'),
    ('Cytochrome P450s', 3.26, 22.4, 88, 'Vper'),
    ('NB-ARC Disease Sentinels', 10.07, 23.6, 25, 'Vper'),
    ('Ubiquitination Receptors', 7.49, 21.5, 32, 'Vper'),
]

for term, fold, logq, cnt, sp in enrichment_data:
    col = '#E69F00' if sp == 'Vtub' else '#009E73'
    sz = np.sqrt(cnt) * 18
    ax_b.scatter(fold, logq, s=sz, color=col, alpha=0.75, edgecolors='black', linewidth=0.7)
    
    ha = 'left' if fold < 12 else 'right'
    offset_x = 0.35 if fold < 12 else -0.35
    offset_y = 1.5 if 'ACC' in term or 'P450' in term else 0.0
    ax_b.text(fold + offset_x, logq + offset_y, term, fontsize=6.0, ha=ha, va='center', color='#222222', fontweight='medium')

# Bubble size legends
ax_b.scatter([], [], s=np.sqrt(25)*18, c='#888888', alpha=0.6, edgecolors='black', label='25 genes')
ax_b.scatter([], [], s=np.sqrt(75)*18, c='#888888', alpha=0.6, edgecolors='black', label='75 genes')
ax_b.scatter([], [], s=np.sqrt(120)*18, c='#888888', alpha=0.6, edgecolors='black', label='120 genes')

ax_b.set_xlabel('Fold Enrichment (Expanding vs Background)', fontweight='medium')
ax_b.set_ylabel(r'$-\log_{10}(\mathrm{FDR}\ q\mathrm{-value})$', fontweight='medium')
ax_b.set_xlim(2, 16.5)
ax_b.set_ylim(10, 125)
ax_b.grid(True, linestyle='--', alpha=0.5, color='#CCCCCC')
ax_b.spines['top'].set_visible(False)
ax_b.spines['right'].set_visible(False)

legend1 = ax_b.legend(loc='upper right', frameon=True, facecolor='#FFFFFF', edgecolor='#CCCCCC', fontsize=6.5)
ax_b.text(-0.15, 1.08, 'B', transform=ax_b.transAxes, fontsize=12, fontweight='bold', va='top')

# -------------------------------------------------------------
# Panel C: Top 10 Adaptive Gene Families Dynamics Matrix
# -------------------------------------------------------------
ax_c = fig.add_subplot(gs[1, :])

families = [
    'Chloroplast Translocon (OG0000016)',
    'Chloroplast Intermediate (OG0000087)',
    'NDH Electron Transport (OG0000036)',
    'PSII Core Reaction Center (OG0000069)',
    '16S rRNA Biogenesis (OG0000104)',
    'Acetyl-CoA Carboxylase (OG0000072)',
    'LRR Receptor Kinase (OG0000012)',
    'Receptor-Like Kinase (OG0000021)',
    'NB-LRR Immune Sentinel (OG0000050)',
    'U-box E3 Ligase (OG0000094)'
]

anc_counts = [6, 4, 7, 6, 4, 7, 8, 8, 7, 6]
vtub_counts = [61, 26, 36, 24, 22, 24, 13, 16, 6, 5]
vper_counts = [3, 2, 6, 5, 3, 6, 65, 37, 29, 22]

y_c = np.arange(len(families))
height_c = 0.25

ax_c.barh(y_c + height_c, vtub_counts, height_c, label='V. tubiflora (Extant Count)', color='#E69F00', edgecolor='none')
ax_c.barh(y_c, vper_counts, height_c, label='V. peripherica (Extant Count)', color='#009E73', edgecolor='none')
ax_c.barh(y_c - height_c, anc_counts, height_c, label='Ancestral Node Count', color='#888888', alpha=0.7, edgecolor='none')

ax_c.set_yticks(y_c)
ax_c.set_yticklabels(families, fontsize=7.2, fontweight='medium')
ax_c.set_xlabel('Gene Copy Number in Family', fontweight='medium')
ax_c.set_xlim(0, 78)
ax_c.xaxis.grid(True, linestyle='--', alpha=0.5, color='#CCCCCC')
ax_c.set_axisbelow(True)
ax_c.spines['top'].set_visible(False)
ax_c.spines['right'].set_visible(False)

for i in range(len(families)):
    vt_delta = vtub_counts[i] - anc_counts[i]
    sign_vt = f"+{vt_delta}" if vt_delta > 0 else f"{vt_delta}"
    ax_c.text(vtub_counts[i] + 1.2, i + height_c, sign_vt, va='center', fontsize=6.5, color='#B37700', fontweight='bold')
    
    vp_delta = vper_counts[i] - anc_counts[i]
    sign_vp = f"+{vp_delta}" if vp_delta > 0 else f"{vp_delta}"
    ax_c.text(vper_counts[i] + 1.2, i, sign_vp, va='center', fontsize=6.5, color='#007353', fontweight='bold')

ax_c.legend(loc='lower right', ncol=3, frameon=True, facecolor='#FFFFFF', edgecolor='#CCCCCC', fontsize=7.0)
ax_c.text(-0.28, 1.06, 'C', transform=ax_c.transAxes, fontsize=12, fontweight='bold', va='top')

# Save with anti-clipping parameters
png_path = os.path.join(out_dir, 'Figure_3_Gene_Family_Dynamics.png')
pdf_path = os.path.join(out_dir, 'Figure_3_Gene_Family_Dynamics.pdf')
plt.savefig(png_path, dpi=300, bbox_inches='tight', pad_inches=0.15)
plt.savefig(pdf_path, bbox_inches='tight', pad_inches=0.15)
plt.close()
print(f"Generated Figure 3:\n- {png_path}\n- {pdf_path}")
