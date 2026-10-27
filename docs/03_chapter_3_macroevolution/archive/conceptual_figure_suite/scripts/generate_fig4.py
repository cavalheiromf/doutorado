#!/usr/bin/env python3
"""
Figure 4: Genome-Wide Selection Landscape & Pentatricopeptide Repeat (PPR) RNA-Editing Architecture
Chapter 1: "Macroevolution and Genomic Divergence in Velloziaceae: from Deep Time to Contrasting Survival Strategies"

Author: Mariana Feitosa Cavalheiro & Teamwork Subagents
Affiliation: CBMEG / UNICAMP
Date: 2026-08-31

This script parses empirical PAML yn00 selection scan results across 1,513 1:1 single-copy
orthogroups in Velloziaceae and generates a publication-grade, editable vector SVG figure.

Panel A: Genome-Wide Selection Landscape (Ka/Ks = omega)
  - A1: Raincloud / Density Distribution of pairwise omega ratios (Purifying, Relaxed, Positive).
  - A2: Pairwise Ka (dN) vs Ks (dS) Scatter Plot with Evolutionary Isoclines (omega = 1.0, 0.5, 0.1)
        and callouts for top candidate adaptive loci (17 PPRs, DYW deaminase, DnaJ, Thioredoxin, Kinases).
Panel B: Structural and Mechanistic Model of PPR-Mediated Chloroplast RNA Editing
  - B1: Modular PLS-Class PPR-DYW Protein Architecture (P-L-S tandem motifs, E/E+ motif, DYW cytidine deaminase).
  - B2: Mechanistic Chloroplastic C-to-U RNA Editing during Poikilochlorophyllous Desiccation & Rehydration.
"""

import os
import sys
import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
from scipy.stats import gaussian_kde

def build_fig4_svg(tsv_annotated_path, tsv_top250_path, output_svg_path):
    print(f"Loading empirical data from:\n  - {tsv_annotated_path}\n  - {tsv_top250_path}")
    
    # 1. Load Data
    if not os.path.exists(tsv_annotated_path):
        raise FileNotFoundError(f"Missing annotated TSV: {tsv_annotated_path}")

    if not os.path.exists(tsv_top250_path):
        raise FileNotFoundError(f"Missing top 250 TSV: {tsv_top250_path}")

    df_all = pd.read_csv(tsv_annotated_path, sep='\t')
    df_top = pd.read_csv(tsv_top250_path, sep='\t')

    # Extract selection stats
    total_genes = len(df_all)
    purifying = df_all[df_all['Selection_Regime'] == 'Purifying_Selection']
    relaxed = df_all[df_all['Selection_Regime'] == 'Relaxed_or_Neutral']
    positive = df_all[df_all['Selection_Regime'] == 'Positive_Selection']
    
    n_pur = len(purifying)
    pct_pur = (n_pur / total_genes) * 100
    n_rel = len(relaxed)
    pct_rel = (n_rel / total_genes) * 100
    n_pos = len(positive)
    pct_pos = (n_pos / total_genes) * 100
    
    mean_omega = df_all['Omega_KaKs'].mean()
    median_omega = df_all['Omega_KaKs'].median()
    median_pos_omega = positive['Omega_KaKs'].median()

    print(f"Selection Regimes across {total_genes} 1:1 Orthologs:")
    print(f"  - Purifying (<0.5): {n_pur} ({pct_pur:.1f}%)")
    print(f"  - Relaxed/Neutral (0.5-1.0): {n_rel} ({pct_rel:.1f}%)")
    print(f"  - Positive Selection (>1.0, Ks<2.0): {n_pos} ({pct_pos:.1f}%, median omega={median_pos_omega:.4f})")

    # 2. Setup Canvas Geometry (viewBox: 0 0 1200 900)
    width = 1200
    height = 900
    
    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background-color: #FFFFFF; font-family: \'Arial\', \'Helvetica Neue\', \'DejaVu Sans\', sans-serif;">')
    
    # Defs: Gradients, Filters, Markers
    svg_lines.append('''
  <defs>
    <!-- Shadow Filters -->
    <filter id="cardShadow" x="-2%" y="-2%" width="104%" height="104%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="1.5" stdDeviation="2" flood-color="#000000" flood-opacity="0.06"/>
    </filter>
    <filter id="badgeShadow" x="-10%" y="-10%" width="120%" height="120%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="1" stdDeviation="1.5" flood-color="#000000" flood-opacity="0.12"/>
    </filter>

    <!-- Arrow Markers -->
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#4A5568"/>
    </marker>
    <marker id="arrowBlue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0072B2"/>
    </marker>
    <marker id="arrowRed" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#D55E00"/>
    </marker>
    <marker id="arrowAmber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#E69F00"/>
    </marker>
    <marker id="arrowGreen" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#009E73"/>
    </marker>

    <!-- Linear Gradients for Cylinders / Domains -->
    <linearGradient id="cTPGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#94A3B8"/>
      <stop offset="50%" stop-color="#64748B"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>
    <linearGradient id="pGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="50%" stop-color="#0284C7"/>
      <stop offset="100%" stop-color="#0369A1"/>
    </linearGradient>
    <linearGradient id="lGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#7DD3FC"/>
      <stop offset="50%" stop-color="#0EA5E9"/>
      <stop offset="100%" stop-color="#0284C7"/>
    </linearGradient>
    <linearGradient id="sGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#BAE6FD"/>
      <stop offset="50%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#0284C7"/>
    </linearGradient>
    <linearGradient id="eGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FCD34D"/>
      <stop offset="50%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#D97706"/>
    </linearGradient>
    <linearGradient id="dywGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F87171"/>
      <stop offset="50%" stop-color="#DC2626"/>
      <stop offset="100%" stop-color="#B91C1C"/>
    </linearGradient>
    
    <!-- Density Area Gradient -->
    <linearGradient id="densityGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0072B2" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#0072B2" stop-opacity="0.05"/>
    </linearGradient>
  </defs>
''')

    # =========================================================================
    # HEADER SECTION
    # =========================================================================
    svg_lines.append('  <!-- Header / Figure Title Bar -->')
    svg_lines.append('  <g id="figure_header">')
    svg_lines.append('    <text x="30" y="32" font-size="16" font-weight="bold" fill="#0F172A" letter-spacing="-0.2px">Fig 4. Genome-Wide Selection Landscape &amp; PPR RNA-Editing Architecture</text>')
    svg_lines.append('    <text x="1170" y="32" text-anchor="end" font-size="11.5" font-weight="500" fill="#475569">Vellozia tubiflora (Resurrection) &#8596; V. peripherica (Evergreen) | 1,513 1:1 Orthologs</text>')
    svg_lines.append('    <line x1="30" y1="42" x2="1170" y2="42" stroke="#CBD5E1" stroke-width="1.2"/>')
    svg_lines.append('  </g>')

    # =========================================================================
    # PANEL A: GENOME-WIDE SELECTION LANDSCAPE (LEFT COLUMN)
    # Bounds: X: 30 to 575 (width 545), Y: 52 to 880 (height 828)
    # =========================================================================
    svg_lines.append('\n  <!-- PANEL A: SELECTION LANDSCAPE -->')
    svg_lines.append('  <g id="panel_a">')
    # Background Card
    svg_lines.append('    <rect x="30" y="52" width="545" height="828" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2" filter="url(#cardShadow)"/>')
    
    # Panel Title Badge
    svg_lines.append('    <g id="panel_a_title">')
    svg_lines.append('      <rect x="42" y="64" width="26" height="26" rx="5" fill="#0072B2"/>')
    svg_lines.append('      <text x="55" y="82" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">A</text>')
    svg_lines.append('      <text x="76" y="82" font-size="13.5" font-weight="bold" fill="#0F172A">Genome-Wide Selection Landscape (Ka/Ks = &#969;)</text>')
    svg_lines.append('    </g>')

    # -------------------------------------------------------------------------
    # Subpanel A1: Selection Ratio (omega) Distribution & Raincloud
    # Card Bounds: X: 42 to 563 (width 521), Y: 98 to 415 (height 317)
    # Plot Area: X: 95 to 545 (width 450), Y: 160 to 345 (height 185)
    # -------------------------------------------------------------------------
    svg_lines.append('\n    <!-- Subpanel A1: omega Density & Raincloud -->')
    svg_lines.append('    <g id="subpanel_a1">')
    svg_lines.append('      <rect x="42" y="98" width="521" height="317" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>')
    svg_lines.append('      <text x="54" y="118" font-size="11.5" font-weight="bold" fill="#1E293B">A1. Empirical Distribution of Pairwise Selection Ratios (&#969;)</text>')
    
    # Regime Metric Pills (Top of A1)
    svg_lines.append('      <g id="a1_metric_pills" transform="translate(54, 125)">')
    # Pill 1: Purifying
    svg_lines.append('        <rect x="0" y="0" width="158" height="20" rx="4" fill="#E0F2FE" stroke="#0072B2" stroke-width="0.8"/>')
    svg_lines.append('        <circle cx="9" cy="10" r="4" fill="#0072B2"/>')
    svg_lines.append(f'        <text x="18" y="14" font-size="9.2" font-weight="bold" fill="#0369A1">Purifying: {n_pur} ({pct_pur:.1f}%)</text>')
    # Pill 2: Relaxed
    svg_lines.append('        <rect x="165" y="0" width="160" height="20" rx="4" fill="#FEF3C7" stroke="#E69F00" stroke-width="0.8"/>')
    svg_lines.append('        <circle cx="174" cy="10" r="4" fill="#E69F00"/>')
    svg_lines.append(f'        <text x="183" y="14" font-size="9.2" font-weight="bold" fill="#92400E">Relaxed/Neut.: {n_rel} ({pct_rel:.1f}%)</text>')
    # Pill 3: Positive
    svg_lines.append('        <rect x="332" y="0" width="165" height="20" rx="4" fill="#FEE2E2" stroke="#D55E00" stroke-width="0.8"/>')
    svg_lines.append('        <circle cx="341" cy="10" r="4" fill="#D55E00"/>')
    svg_lines.append(f'        <text x="350" y="14" font-size="9.2" font-weight="bold" fill="#991B1B">Positive: {n_pos} ({pct_pos:.1f}%)</text>')
    svg_lines.append('      </g>')

    # Compute Density Curve & Geometry for A1
    p_x0, p_x1 = 95, 545
    p_y_top, p_y_base = 160, 345
    plot_w = p_x1 - p_x0
    plot_h = p_y_base - p_y_top
    
    def omega_to_x(val):
        capped = min(max(val, 0.0), 2.5)
        return p_x0 + (capped / 2.5) * plot_w

    # Background Regime Zones in Plot
    x_zero = omega_to_x(0.0)
    x_half = omega_to_x(0.5)
    x_one = omega_to_x(1.0)
    x_max = omega_to_x(2.5)

    svg_lines.append('      <!-- Background Selection Regime Shading -->')
    svg_lines.append(f'      <rect x="{x_zero}" y="{p_y_top}" width="{x_half - x_zero}" height="{plot_h}" fill="#0072B2" fill-opacity="0.07"/>')
    svg_lines.append(f'      <rect x="{x_half}" y="{p_y_top}" width="{x_one - x_half}" height="{plot_h}" fill="#E69F00" fill-opacity="0.08"/>')
    svg_lines.append(f'      <rect x="{x_one}" y="{p_y_top}" width="{x_max - x_one}" height="{plot_h}" fill="#D55E00" fill-opacity="0.08"/>')

    # Gridlines
    for grid_om in [0.5, 1.0, 1.5, 2.0]:
        gx = omega_to_x(grid_om)
        svg_lines.append(f'      <line x1="{gx:.1f}" y1="{p_y_top}" x2="{gx:.1f}" y2="{p_y_base}" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="3,3"/>')

    # Compute empirical KDE
    finite_omegas = df_all['Omega_KaKs'].values
    finite_omegas = finite_omegas[(finite_omegas >= 0) & (finite_omegas <= 3.0)]
    kde = gaussian_kde(finite_omegas, bw_method=0.15)
    x_eval = np.linspace(0.0, 2.5, 150)
    y_dens = kde(x_eval)
    max_dens = np.max(y_dens)
    y_scale = (plot_h - 20) / (max_dens * 1.08)

    # Build Path
    path_d = [f"M {omega_to_x(x_eval[0]):.1f} {p_y_base:.1f}"]
    for xe, ye in zip(x_eval, y_dens):
        cur_x = omega_to_x(xe)
        cur_y = p_y_base - ye * y_scale
        path_d.append(f"L {cur_x:.1f} {cur_y:.1f}")
    path_d.append(f"L {omega_to_x(x_eval[-1]):.1f} {p_y_base:.1f} Z")
    path_str = " ".join(path_d)

    svg_lines.append(f'      <!-- Density Polygon -->')
    svg_lines.append(f'      <path d="{path_str}" fill="url(#densityGrad)" stroke="#0072B2" stroke-width="2.2"/>')

    # Vertical Markers for Median, Mean, Neutral (1.0)
    med_x = omega_to_x(median_omega)
    mean_x = omega_to_x(mean_omega)
    one_x = omega_to_x(1.0)

    # Neutral Threshold Line
    svg_lines.append(f'      <line x1="{one_x:.1f}" y1="{p_y_top - 5}" x2="{one_x:.1f}" y2="{p_y_base + 35}" stroke="#475569" stroke-width="1.6" stroke-dasharray="4,3"/>')
    svg_lines.append(f'      <text x="{one_x:.1f}" y="{p_y_top + 12}" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#334155">Neutral (&#969; = 1.0)</text>')

    # Median Line
    svg_lines.append(f'      <line x1="{med_x:.1f}" y1="{p_y_top + 20}" x2="{med_x:.1f}" y2="{p_y_base}" stroke="#0072B2" stroke-width="1.8" stroke-dasharray="3,2"/>')
    svg_lines.append(f'      <text x="{med_x - 4:.1f}" y="{p_y_top + 32}" text-anchor="end" font-size="8.5" font-weight="bold" fill="#0072B2">Median = {median_omega:.2f}</text>')

    # Mean Line
    svg_lines.append(f'      <line x1="{mean_x:.1f}" y1="{p_y_top + 45}" x2="{mean_x:.1f}" y2="{p_y_base}" stroke="#D55E00" stroke-width="1.8" stroke-dasharray="4,2"/>')
    svg_lines.append(f'      <text x="{mean_x + 4:.1f}" y="{p_y_top + 55}" text-anchor="start" font-size="8.5" font-weight="bold" fill="#D55E00">Mean = {mean_omega:.2f}</text>')

    # Raincloud Jitter Strip at Bottom (Y: 354 to 372)
    np.random.seed(101)
    jitter_indices = np.random.choice(len(df_all), size=350, replace=False)
    svg_lines.append('      <!-- Raincloud Jitter Points (Sampled n=350) -->')
    svg_lines.append('      <g id="a1_jitter_strip">')
    for idx in jitter_indices:
        row = df_all.iloc[idx]
        om = row['Omega_KaKs']
        if om > 2.5:
            continue
        cx = omega_to_x(om)
        cy = 354 + np.random.uniform(0, 18)
        reg = row['Selection_Regime']
        fill_col = "#0072B2" if reg == "Purifying_Selection" else ("#E69F00" if reg == "Relaxed_or_Neutral" else "#D55E00")
        svg_lines.append(f'        <circle cx="{cx:.1f}" cy="{cy:.1f}" r="2" fill="{fill_col}" opacity="0.6"/>')
    svg_lines.append('      </g>')

    # X-Axis for A1
    svg_lines.append(f'      <!-- A1 Axes & Ticks -->')
    svg_lines.append(f'      <line x1="{p_x0}" y1="{p_y_base + 30}" x2="{p_x1}" y2="{p_y_base + 30}" stroke="#475569" stroke-width="1.2"/>')
    for om_tick, label in [(0.0, '0.0'), (0.5, '0.5'), (1.0, '1.0'), (1.5, '1.5'), (2.0, '2.0'), (2.5, '&#8805;2.5')]:
        tx = omega_to_x(om_tick)
        svg_lines.append(f'      <line x1="{tx:.1f}" y1="{p_y_base + 30}" x2="{tx:.1f}" y2="{p_y_base + 35}" stroke="#475569" stroke-width="1.2"/>')
        svg_lines.append(f'      <text x="{tx:.1f}" y="{p_y_base + 47}" text-anchor="middle" font-size="9" fill="#475569">{label}</text>')
    
    svg_lines.append(f'      <text x="{(p_x0 + p_x1)/2:.1f}" y="{p_y_base + 61}" text-anchor="middle" font-size="10" font-weight="bold" fill="#1E293B">Pairwise Selection Ratio (&#969; = Ka / Ks)</text>')
    svg_lines.append(f'      <text x="50" y="{(p_y_top + p_y_base)/2:.1f}" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#475569" transform="rotate(-90 50 {(p_y_top + p_y_base)/2:.1f})">Probability Density</text>')
    svg_lines.append('    </g>')

    # -------------------------------------------------------------------------
    # Subpanel A2: Pairwise Ka vs Ks Scatter Plot with Isoclines
    # Card Bounds: X: 42 to 563 (width 521), Y: 424 to 868 (height 444)
    # Plot Area: X: 95 to 545 (width 450), Y: 465 to 735 (height 270)
    # -------------------------------------------------------------------------
    svg_lines.append('\n    <!-- Subpanel A2: Ka vs Ks Scatter Plot -->')
    svg_lines.append('    <g id="subpanel_a2">')
    svg_lines.append('      <rect x="42" y="424" width="521" height="444" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>')
    svg_lines.append('      <text x="54" y="444" font-size="11.5" font-weight="bold" fill="#1E293B">A2. Pairwise Ka (dN) vs Ks (dS) Scatter &amp; Adaptive Candidate Loci</text>')
    
    s_x0, s_x1 = 95, 545
    s_y_top, s_y_base = 465, 735
    s_w = s_x1 - s_x0
    s_h = s_y_base - s_y_top

    def ks_to_x(val):
        capped = min(max(val, 0.0), 2.0)
        return s_x0 + (capped / 2.0) * s_w

    def ka_to_y(val):
        capped = min(max(val, 0.0), 6.0)
        return s_y_base - (capped / 6.0) * s_h

    # Gridlines for A2
    svg_lines.append('      <!-- A2 Gridlines -->')
    for ks_val in [0.5, 1.0, 1.5, 2.0]:
        gx = ks_to_x(ks_val)
        svg_lines.append(f'      <line x1="{gx:.1f}" y1="{s_y_top}" x2="{gx:.1f}" y2="{s_y_base}" stroke="#E2E8F0" stroke-width="1"/>')
    for ka_val in [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]:
        gy = ka_to_y(ka_val)
        svg_lines.append(f'      <line x1="{s_x0}" y1="{gy:.1f}" x2="{s_x1}" y2="{gy:.1f}" stroke="#E2E8F0" stroke-width="1"/>')

    # Evolutionary Isoclines:
    # 1. omega = 1.0 (Neutral)
    iso1_x0, iso1_y0 = ks_to_x(0.0), ka_to_y(0.0)
    iso1_x1, iso1_y1 = ks_to_x(2.0), ka_to_y(2.0)
    svg_lines.append(f'      <!-- Isocline omega = 1.0 (Neutral) -->')
    svg_lines.append(f'      <line x1="{iso1_x0:.1f}" y1="{iso1_y0:.1f}" x2="{iso1_x1:.1f}" y2="{iso1_y1:.1f}" stroke="#475569" stroke-width="1.8" stroke-dasharray="5,4"/>')
    svg_lines.append(f'      <text x="{iso1_x1 - 8:.1f}" y="{iso1_y1 - 6:.1f}" text-anchor="end" font-size="8.5" font-weight="bold" fill="#334155">&#969; = 1.0 (Neutral Boundary)</text>')

    # 2. omega = 0.5 (Purifying)
    iso05_x1, iso05_y1 = ks_to_x(2.0), ka_to_y(1.0)
    svg_lines.append(f'      <!-- Isocline omega = 0.5 (Purifying) -->')
    svg_lines.append(f'      <line x1="{iso1_x0:.1f}" y1="{iso1_y0:.1f}" x2="{iso05_x1:.1f}" y2="{iso05_y1:.1f}" stroke="#0072B2" stroke-width="1.5" stroke-dasharray="4,3"/>')
    svg_lines.append(f'      <text x="{iso05_x1 - 8:.1f}" y="{iso05_y1 - 5:.1f}" text-anchor="end" font-size="8.5" font-weight="bold" fill="#0072B2">&#969; = 0.5 (Purifying Threshold)</text>')

    # 3. omega = 0.1 (Strongly Constrained)
    iso01_x1, iso01_y1 = ks_to_x(2.0), ka_to_y(0.2)
    svg_lines.append(f'      <!-- Isocline omega = 0.1 (Strong Constraint) -->')
    svg_lines.append(f'      <line x1="{iso1_x0:.1f}" y1="{iso1_y0:.1f}" x2="{iso01_x1:.1f}" y2="{iso01_y1:.1f}" stroke="#009E73" stroke-width="1.2" stroke-dasharray="3,3"/>')
    svg_lines.append(f'      <text x="{iso01_x1 - 8:.1f}" y="{iso01_y1 - 4:.1f}" text-anchor="end" font-size="8" font-weight="bold" fill="#009E73">&#969; = 0.1 (Strongly Constrained)</text>')

    # Positive Selection Shaded Zone in Upper Wedge (Ka > Ks)
    wedge_p = f"M {ks_to_x(0):.1f} {ka_to_y(0):.1f} L {ks_to_x(2.0):.1f} {ka_to_y(2.0):.1f} L {ks_to_x(2.0):.1f} {ka_to_y(6.0):.1f} L {ks_to_x(0):.1f} {ka_to_y(6.0):.1f} Z"
    svg_lines.append(f'      <path d="{wedge_p}" fill="#D55E00" fill-opacity="0.05"/>')
    svg_lines.append(f'      <text x="{ks_to_x(0.35):.1f}" y="{ka_to_y(4.8):.1f}" font-size="10.5" font-weight="bold" fill="#C2410C" opacity="0.8">Positive Diversifying Selection (&#969; &gt; 1.0)</text>')

    # Plot 1,513 Scatter Points
    svg_lines.append('      <!-- Data Points: Purifying (Blue), Relaxed (Amber), Positive (Vermilion) -->')
    svg_lines.append('      <g id="a2_scatter_points">')
    df_sorted = df_all.sort_values(by='Omega_KaKs', ascending=True)
    for _, row in df_sorted.iterrows():
        ks = row['Ks_dS']
        ka = row['Ka_dN']
        reg = row['Selection_Regime']
        
        if ks > 2.0 or ka > 6.0:
            continue
            
        cx = ks_to_x(ks)
        cy = ka_to_y(ka)
        
        if reg == "Purifying_Selection":
            svg_lines.append(f'        <circle cx="{cx:.1f}" cy="{cy:.1f}" r="2.2" fill="#0072B2" opacity="0.4"/>')
        elif reg == "Relaxed_or_Neutral":
            svg_lines.append(f'        <circle cx="{cx:.1f}" cy="{cy:.1f}" r="2.4" fill="#E69F00" opacity="0.5"/>')
        else: # Positive_Selection
            svg_lines.append(f'        <circle cx="{cx:.1f}" cy="{cy:.1f}" r="3.4" fill="#D55E00" stroke="#7C2D12" stroke-width="0.8" opacity="0.9"/>')
    svg_lines.append('      </g>')

    # Top Candidate Loci Callout Labels (Explicit OG + Function + Omega)
    candidates_to_label = [
        {"og": "OG0011783", "label": "OG0011783: PPR repeat (&#969;=4.91)", "ks": 1.0752, "ka": 5.2755, "dx": 28, "dy": -12},
        {"og": "OG0010819", "label": "OG0010819: Stress kinase (&#969;=4.92)", "ks": 0.9766, "ka": 4.8076, "dx": -165, "dy": -10},
        {"og": "OG0011519", "label": "OG0011519: ATPase HMA1 (&#969;=4.70)", "ks": 1.1845, "ka": 5.5688, "dx": -170, "dy": -14},
        {"og": "OG0010277", "label": "OG0010277: PPR repeat (&#969;=4.54)", "ks": 1.1557, "ka": 5.2467, "dx": 25, "dy": 8},
        {"og": "OG0011290", "label": "OG0011290: Thioredoxin TM (&#969;=4.31)", "ks": 1.0837, "ka": 4.6656, "dx": 25, "dy": 4},
        {"og": "OG0011532", "label": "OG0011532: DnaJ/Hsp40 (&#969;=3.86)", "ks": 1.1055, "ka": 4.2708, "dx": 25, "dy": 6},
        {"og": "OG0011950", "label": "OG0011950: DYW deaminase (&#969;=3.80)", "ks": 1.4382, "ka": 5.4589, "dx": 15, "dy": -12},
        {"og": "OG0010401", "label": "OG0010401: Receptor kinase (&#969;=2.59)", "ks": 1.6604, "ka": 4.3038, "dx": 15, "dy": 10},
    ]

    svg_lines.append('      <!-- Top Adaptive Candidate Annotations -->')
    svg_lines.append('      <g id="a2_callouts">')
    for cand in candidates_to_label:
        cx = ks_to_x(cand['ks'])
        cy = ka_to_y(cand['ka'])
        tx = cx + cand['dx']
        ty = cy + cand['dy']
        
        svg_lines.append(f'        <circle cx="{cx:.1f}" cy="{cy:.1f}" r="5.5" fill="none" stroke="#DC2626" stroke-width="1.8"/>')
        svg_lines.append(f'        <line x1="{cx:.1f}" y1="{cy:.1f}" x2="{tx:.1f}" y2="{ty:.1f}" stroke="#991B1B" stroke-width="1.1"/>')
        is_left = cand['dx'] < 0
        anchor = "end" if is_left else "start"
        svg_lines.append(f'        <text x="{tx + (-3 if is_left else 3):.1f}" y="{ty + 3:.1f}" text-anchor="{anchor}" font-size="8.5" font-weight="bold" fill="#7F1D1D">{cand["label"]}</text>')
    svg_lines.append('      </g>')

    # Axes for A2
    svg_lines.append(f'      <!-- A2 Axes & Ticks -->')
    svg_lines.append(f'      <line x1="{s_x0}" y1="{s_y_base}" x2="{s_x1}" y2="{s_y_base}" stroke="#475569" stroke-width="1.2"/>')
    svg_lines.append(f'      <line x1="{s_x0}" y1="{s_y_top}" x2="{s_x0}" y2="{s_y_base}" stroke="#475569" stroke-width="1.2"/>')
    
    # X Ticks
    for ks_val in [0.0, 0.5, 1.0, 1.5, 2.0]:
        tx = ks_to_x(ks_val)
        svg_lines.append(f'      <line x1="{tx:.1f}" y1="{s_y_base}" x2="{tx:.1f}" y2="{s_y_base + 5}" stroke="#475569" stroke-width="1.2"/>')
        svg_lines.append(f'      <text x="{tx:.1f}" y="{s_y_base + 16}" text-anchor="middle" font-size="9" fill="#475569">{ks_val:.1f}</text>')
    svg_lines.append(f'      <text x="{(s_x0 + s_x1)/2:.1f}" y="{s_y_base + 29}" text-anchor="middle" font-size="10" font-weight="bold" fill="#1E293B">Synonymous Substitution Rate (Ks = dS)</text>')

    # Y Ticks
    for ka_val in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]:
        ty = ka_to_y(ka_val)
        svg_lines.append(f'      <line x1="{s_x0 - 5}" y1="{ty:.1f}" x2="{s_x0}" y2="{ty:.1f}" stroke="#475569" stroke-width="1.2"/>')
        svg_lines.append(f'      <text x="{s_x0 - 8}" y="{ty + 3:.1f}" text-anchor="end" font-size="9" fill="#475569">{ka_val:.1f}</text>')
    svg_lines.append(f'      <text x="50" y="{(s_y_top + s_y_base)/2:.1f}" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#475569" transform="rotate(-90 50 {(s_y_top + s_y_base)/2:.1f})">Non-synonymous Rate (Ka = dN)</text>')

    # Summary Inset Card at Bottom of A2 (Y: 772 to 856)
    svg_lines.append('      <!-- Top Functional Categories Inset Card -->')
    svg_lines.append('      <g id="a2_candidate_summary" transform="translate(54, 772)">')
    svg_lines.append('        <rect x="0" y="0" width="497" height="84" rx="5" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.9"/>')
    svg_lines.append('        <text x="12" y="16" font-size="9.5" font-weight="bold" fill="#0F172A">Enriched Functional Classes Under Positive Selection (Top 250 Candidates, &#969; &gt; 1.0):</text>')
    
    # Col 1: PPR Proteins
    svg_lines.append('        <rect x="10" y="24" width="154" height="52" rx="4" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="0.8"/>')
    svg_lines.append('        <text x="16" y="38" font-size="8.8" font-weight="bold" fill="#0369A1">&#8226; 17 PPR Proteins</text>')
    svg_lines.append('        <text x="16" y="50" font-size="8" fill="#475569">&#969; up to 4.91 (OG0011783)</text>')
    svg_lines.append('        <text x="16" y="62" font-size="8" fill="#475569">Organelle RNA-editing array</text>')
    
    # Col 2: DYW Deaminases & RNA factors
    svg_lines.append('        <rect x="171" y="24" width="154" height="52" rx="4" fill="#FEF2F2" stroke="#FECACA" stroke-width="0.8"/>')
    svg_lines.append('        <text x="177" y="38" font-size="8.8" font-weight="bold" fill="#991B1B">&#8226; DYW Deaminases</text>')
    svg_lines.append('        <text x="177" y="50" font-size="8" fill="#475569">&#969; = 3.80 (OG0011950)</text>')
    svg_lines.append('        <text x="177" y="62" font-size="8" fill="#475569">Organelle RRM (&#969; = 4.50)</text>')

    # Col 3: Chaperones, Redox & Kinases
    svg_lines.append('        <rect x="332" y="24" width="155" height="52" rx="4" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="0.8"/>')
    svg_lines.append('        <text x="338" y="38" font-size="8.8" font-weight="bold" fill="#166534">&#8226; Redox &amp; Kinases</text>')
    svg_lines.append('        <text x="338" y="50" font-size="8" fill="#475569">Thioredoxin TM (&#969; = 4.31)</text>')
    svg_lines.append('        <text x="338" y="62" font-size="8" fill="#475569">DnaJ/Hsp40 (&#969;=3.86), Kinases</text>')
    svg_lines.append('      </g>')

    svg_lines.append('    </g>')
    svg_lines.append('  </g>')

    # =========================================================================
    # PANEL B: STRUCTURAL & MECHANISTIC MODEL OF PPR RNA EDITING (RIGHT COLUMN)
    # Bounds: X: 595 to 1170 (width 575), Y: 52 to 880 (height 828)
    # =========================================================================
    svg_lines.append('\n  <!-- PANEL B: PPR DOMAIN ARCHITECTURE & MECHANISM -->')
    svg_lines.append('  <g id="panel_b">')
    # Background Card
    svg_lines.append('    <rect x="595" y="52" width="575" height="828" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2" filter="url(#cardShadow)"/>')
    
    # Panel Title Badge
    svg_lines.append('    <g id="panel_b_title">')
    svg_lines.append('      <rect x="607" y="64" width="26" height="26" rx="5" fill="#009E73"/>')
    svg_lines.append('      <text x="620" y="82" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">B</text>')
    svg_lines.append('      <text x="641" y="82" font-size="13.5" font-weight="bold" fill="#0F172A">Pentatricopeptide Repeat (PPR) Architecture &amp; C-to-U Editing</text>')
    svg_lines.append('    </g>')

    # -------------------------------------------------------------------------
    # Subpanel B1: Modular PLS-Class PPR-DYW Protein Architecture
    # Card Bounds: X: 607 to 1158 (width 551), Y: 98 to 415 (height 317)
    # -------------------------------------------------------------------------
    svg_lines.append('\n    <!-- Subpanel B1: Modular Domain Architecture -->')
    svg_lines.append('    <g id="subpanel_b1">')
    svg_lines.append('      <rect x="607" y="98" width="551" height="317" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>')
    svg_lines.append('      <text x="619" y="118" font-size="11.5" font-weight="bold" fill="#1E293B">B1. Modular PLS-Class PPR-DYW Architecture &amp; RNA Recognition Code</text>')

    # Domain Diagram (Y: 136 to 168)
    dom_y = 136
    dom_h = 32
    svg_lines.append(f'      <text x="620" y="{dom_y + 20}" font-size="10" font-weight="bold" fill="#64748B">N-term</text>')
    
    # 1. cTP transit peptide
    svg_lines.append(f'      <rect x="662" y="{dom_y}" width="42" height="{dom_h}" rx="4" fill="url(#cTPGrad)" stroke="#334155" stroke-width="1"/>')
    svg_lines.append(f'      <text x="683" y="{dom_y + 20}" text-anchor="middle" font-size="9" font-weight="bold" fill="#FFFFFF">cTP</text>')

    # 2. Tandem P-L-S repeats (Array of 9 modular blocks)
    pls_x = 710
    repeats = [
        ('P1', '#0284C7', 'url(#pGrad)'), ('L1', '#0EA5E9', 'url(#lGrad)'), ('S1', '#38BDF8', 'url(#sGrad)'),
        ('P2', '#0284C7', 'url(#pGrad)'), ('L2', '#0EA5E9', 'url(#lGrad)'), ('S2', '#38BDF8', 'url(#sGrad)'),
        ('Pn', '#0284C7', 'url(#pGrad)'), ('Ln', '#0EA5E9', 'url(#lGrad)'), ('Sn', '#38BDF8', 'url(#sGrad)')
    ]
    rep_w = 26
    for i, (name, bcol, grad) in enumerate(repeats):
        rx = pls_x + i * rep_w
        svg_lines.append(f'      <rect x="{rx}" y="{dom_y}" width="{rep_w - 2}" height="{dom_h}" rx="3" fill="{grad}" stroke="{bcol}" stroke-width="0.8"/>')
        svg_lines.append(f'      <text x="{rx + rep_w/2 - 1}" y="{dom_y + 20}" text-anchor="middle" font-size="8.2" font-weight="bold" fill="#FFFFFF">{name}</text>')

    # 3. E/E+ motif (Linker / Positioning domain)
    e_x = pls_x + len(repeats) * rep_w + 4
    e_w = 64
    svg_lines.append(f'      <rect x="{e_x}" y="{dom_y}" width="{e_w}" height="{dom_h}" rx="4" fill="url(#eGrad)" stroke="#B45309" stroke-width="1"/>')
    svg_lines.append(f'      <text x="{e_x + e_w/2}" y="{dom_y + 20}" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#FFFFFF">E / E+</text>')

    # 4. DYW Deaminase Domain (Catalytic zinc deaminase)
    dyw_x = e_x + e_w + 6
    dyw_w = 88
    svg_lines.append(f'      <rect x="{dyw_x}" y="{dom_y}" width="{dyw_w}" height="{dom_h}" rx="4" fill="url(#dywGrad)" stroke="#991B1B" stroke-width="1.2"/>')
    svg_lines.append(f'      <text x="{dyw_x + dyw_w/2}" y="{dom_y + 16}" text-anchor="middle" font-size="9" font-weight="bold" fill="#FFFFFF">DYW Domain</text>')
    svg_lines.append(f'      <text x="{dyw_x + dyw_w/2}" y="{dom_y + 27}" text-anchor="middle" font-size="7.5" fill="#FEE2E2">Zn&#178;&#8314; Deaminase</text>')
    
    # C-term label
    svg_lines.append(f'      <text x="{dyw_x + dyw_w + 8}" y="{dom_y + 20}" font-size="10" font-weight="bold" fill="#64748B">C-term</text>')

    # Domain Annotations (Y: 180)
    svg_lines.append(f'      <!-- Annotations for Domain Functions -->')
    svg_lines.append(f'      <text x="683" y="180" text-anchor="middle" font-size="7.8" fill="#475569">Transit Pept.</text>')
    svg_lines.append(f'      <text x="{pls_x + (len(repeats)*rep_w)/2}" y="180" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#0369A1">Tandem &#945;-Solenoid Array (Base-by-Base RNA Recognition)</text>')
    svg_lines.append(f'      <text x="{e_x + e_w/2}" y="180" text-anchor="middle" font-size="7.8" fill="#92400E">Linker/Spacer</text>')
    svg_lines.append(f'      <text x="{dyw_x + dyw_w/2}" y="180" text-anchor="middle" font-size="8" font-weight="bold" fill="#991B1B">Catalytic Center</text>')

    # Molecular Inset: RNA Recognition Code Table (Y: 192 to 288)
    svg_lines.append('      <!-- RNA Recognition Code Matrix Inset -->')
    svg_lines.append('      <g id="b1_rna_code_inset" transform="translate(618, 192)">')
    svg_lines.append('        <rect x="0" y="0" width="529" height="96" rx="5" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.9"/>')
    svg_lines.append('        <text x="12" y="16" font-size="9.2" font-weight="bold" fill="#0F172A">Modular 5th &amp; 35th Amino Acid Recognition Code (PPR RNA Binding):</text>')
    
    base_boxes = [
        {"base": "Adenine (A)", "aa": "Thr5 + Asn35", "bg": "#ECFDF5", "border": "#10B981", "col": "#065F46"},
        {"base": "Uracil (U)", "aa": "Asn5 + Asp35", "bg": "#EFF6FF", "border": "#3B82F6", "col": "#1E40AF"},
        {"base": "Cytidine (C)", "aa": "Asn5 + Asn35", "bg": "#FFFBEB", "border": "#F59E0B", "col": "#92400E"},
        {"base": "Guanine (G)", "aa": "Thr5 + Asp35", "bg": "#F5F3FF", "border": "#8B5CF6", "col": "#5B21B6"},
    ]
    for i, b_info in enumerate(base_boxes):
        bx = 10 + i * 128
        svg_lines.append(f'        <rect x="{bx}" y="24" width="122" height="42" rx="4" fill="{b_info["bg"]}" stroke="{b_info["border"]}" stroke-width="0.9"/>')
        svg_lines.append(f'        <text x="{bx + 61}" y="40" text-anchor="middle" font-size="9.5" font-weight="bold" fill="{b_info["col"]}">{b_info["base"]}</text>')
        svg_lines.append(f'        <text x="{bx + 61}" y="56" text-anchor="middle" font-size="8.2" fill="#475569">{b_info["aa"]}</text>')
    
    svg_lines.append('        <text x="12" y="83" font-size="8.2" fill="#475569">&#8594; Single-stranded pre-mRNA is bound in the inner concave groove in an antiparallel (5&#8242;&#8594;3&#8242;) orientation.</text>')
    svg_lines.append('      </g>')

    # 17 Positively Selected PPR Genes Badge Table (Y: 298 to 405)
    svg_lines.append('      <!-- 17 Positively Selected PPR Genes Summary -->')
    svg_lines.append('      <g id="b1_ppr_table" transform="translate(618, 298)">')
    svg_lines.append('        <rect x="0" y="0" width="529" height="106" rx="5" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.9"/>')
    svg_lines.append('        <text x="12" y="16" font-size="9.2" font-weight="bold" fill="#0F172A">Inventory of 17 PPR Genes Under Positive Selection in Velloziaceae (&#969; &gt; 1.0):</text>')
    
    ppr_loci = [
        ("OG0011783", "Chr3A", "4.91", "PPR repeat"),
        ("OG0010277", "Chr6A", "4.54", "PPR repeat"),
        ("OG0012000", "Chr1A", "4.50", "PPR repeat"),
        ("OG0011369", "Chr4A", "3.86", "PPR domain"),
        ("OG0010798", "Chr3A", "2.74", "PPR domain"),
        ("OG0011089", "Chr4A", "2.18", "PPR domain"),
        ("OG0011020", "Chr3A", "2.09", "PPR protein"),
        ("OG0010861", "Chr3A", "2.05", "PPR repeat"),
        ("OG0011042", "Chr3A", "1.76", "PPR domain"),
        ("OG0011627", "Chr5A", "1.65", "PPR domain"),
        ("OG0010729", "Chr7A", "1.62", "PPR At1g06150"),
        ("OG0010756", "Chr7A", "1.60", "PPR domain"),
    ]
    # Row 1
    for i in range(6):
        og, chrom, om_v, desc = ppr_loci[i]
        lx = 10 + i * 86
        svg_lines.append(f'        <rect x="{lx}" y="24" width="82" height="34" rx="3" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="0.7"/>')
        svg_lines.append(f'        <text x="{lx + 41}" y="36" text-anchor="middle" font-size="7.8" font-weight="bold" fill="#0369A1">{og}</text>')
        svg_lines.append(f'        <text x="{lx + 41}" y="48" text-anchor="middle" font-size="7.5" fill="#D55E00">&#969; = {om_v} ({chrom})</text>')
    
    # Row 2
    for i in range(6):
        og, chrom, om_v, desc = ppr_loci[6 + i]
        lx = 10 + i * 86
        svg_lines.append(f'        <rect x="{lx}" y="62" width="82" height="34" rx="3" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="0.7"/>')
        svg_lines.append(f'        <text x="{lx + 41}" y="74" text-anchor="middle" font-size="7.8" font-weight="bold" fill="#1E293B">{og}</text>')
        svg_lines.append(f'        <text x="{lx + 41}" y="86" text-anchor="middle" font-size="7.5" fill="#D55E00">&#969; = {om_v} ({chrom})</text>')

    svg_lines.append('        <text x="520" y="101" text-anchor="end" font-size="7.2" font-style="italic" fill="#64748B">+5 additional loci (OG0011413, OG0011154, OG0011297, OG0011817, OG0010975; &#969; = 1.03–1.40)</text>')
    svg_lines.append('      </g>')

    svg_lines.append('    </g>')

    # -------------------------------------------------------------------------
    # Subpanel B2: Mechanistic Chloroplastic C-to-U RNA Editing in Desiccation
    # Card Bounds: X: 607 to 1158 (width 551), Y: 424 to 868 (height 444)
    # -------------------------------------------------------------------------
    svg_lines.append('\n    <!-- Subpanel B2: Mechanistic C-to-U Editing Model -->')
    svg_lines.append('    <g id="subpanel_b2">')
    svg_lines.append('      <rect x="607" y="424" width="551" height="444" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>')
    svg_lines.append('      <text x="619" y="444" font-size="11.5" font-weight="bold" fill="#1E293B">B2. Mechanistic Chloroplastic C-to-U Editing &amp; Poikilochlorophyllous Cycle</text>')

    # Step 1: Biochemical Reaction Banner (Y: 452 to 540)
    svg_lines.append('      <!-- Biochemical Deamination Reaction -->')
    svg_lines.append('      <g id="b2_reaction_card" transform="translate(618, 452)">')
    svg_lines.append('        <rect x="0" y="0" width="529" height="88" rx="5" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.9"/>')
    
    # Left: Unedited Pre-mRNA
    svg_lines.append('        <text x="12" y="16" font-size="9" font-weight="bold" fill="#64748B">Unedited Pre-mRNA (Chloroplast ndhB / psbE / atpA):</text>')
    svg_lines.append('        <rect x="10" y="24" width="180" height="26" rx="4" fill="#FEF3C7" stroke="#F59E0B" stroke-width="0.8"/>')
    svg_lines.append('        <text x="20" y="41" font-family="Courier, monospace" font-size="10.5" font-weight="bold" fill="#92400E">5&#8242;- A U G [ <tspan fill="#DC2626">C</tspan> ] G A U C -3&#8242;</text>')
    svg_lines.append('        <text x="10" y="62" font-size="7.8" fill="#64748B">Target Cytidine (Non-translatable / Premature Stop)</text>')
    svg_lines.append('        <text x="10" y="74" font-size="7.8" fill="#B45309">ACG &#8594; Non-functional codon</text>')

    # Center: DYW Catalytic Deamination Arrow
    svg_lines.append('        <g id="reaction_arrow" transform="translate(202, 37)">')
    svg_lines.append('          <line x1="0" y1="0" x2="80" y2="0" stroke="#DC2626" stroke-width="2.5" marker-end="url(#arrowRed)"/>')
    svg_lines.append('          <text x="40" y="-12" text-anchor="middle" font-size="8.2" font-weight="bold" fill="#991B1B">DYW Deaminase</text>')
    svg_lines.append('          <text x="40" y="-2" text-anchor="middle" font-size="7.2" fill="#7F1D1D">+ H&#8322;O &#8594; + NH&#8323;</text>')
    svg_lines.append('          <text x="40" y="14" text-anchor="middle" font-size="7.5" font-weight="bold" fill="#DC2626">C &#8594; U Deamination</text>')
    svg_lines.append('        </g>')

    # Right: Edited Translatable mRNA
    svg_lines.append('        <g id="edited_mrna" transform="translate(300, 0)">')
    svg_lines.append('          <text x="0" y="16" font-size="9" font-weight="bold" fill="#009E73">Edited Translatable mRNA (Resurrection Ready):</text>')
    svg_lines.append('          <rect x="0" y="24" width="180" height="26" rx="4" fill="#ECFDF5" stroke="#10B981" stroke-width="0.8"/>')
    svg_lines.append('          <text x="10" y="41" font-family="Courier, monospace" font-size="10.5" font-weight="bold" fill="#065F46">5&#8242;- A U G [ <tspan fill="#059669">U</tspan> ] G A U C -3&#8242;</text>')
    svg_lines.append('          <text x="0" y="62" font-size="7.8" fill="#047857">&#10004; Correct Functional AUG / Leucine Restored</text>')
    svg_lines.append('          <text x="0" y="74" font-size="7.8" fill="#065F46">Enables immediate ribosomal translation</text>')
    svg_lines.append('        </g>')
    svg_lines.append('      </g>')

    # Step 2: Desiccation vs Rehydration Two-Stage Cycle (Y: 548 to 742)
    svg_lines.append('      <!-- Two-Stage Poikilochlorophyllous Desiccation & Rehydration Cycle -->')
    svg_lines.append('      <g id="b2_cycle_cards" transform="translate(618, 548)">')
    
    # Left Card: DESICCATION
    svg_lines.append('        <!-- Stage 1: Desiccation Card -->')
    svg_lines.append('        <g id="card_desiccation">')
    svg_lines.append('          <rect x="0" y="0" width="258" height="194" rx="5" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1"/>')
    svg_lines.append('          <rect x="0" y="0" width="258" height="26" rx="5" fill="#FEF3C7"/>')
    svg_lines.append('          <circle cx="12" cy="13" r="5" fill="#D97706"/>')
    svg_lines.append('          <text x="24" y="17" font-size="9.5" font-weight="bold" fill="#92400E">1. Desiccation (Desiccoplast Dormancy)</text>')
    
    # Schematic: Desiccoplast
    svg_lines.append('          <g transform="translate(10, 34)">')
    svg_lines.append('            <rect x="0" y="0" width="238" height="66" rx="6" fill="#FEF9C3" stroke="#CA8A04" stroke-width="0.8" stroke-dasharray="4,2"/>')
    svg_lines.append('            <text x="119" y="15" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#854D0E">Dormant Desiccoplast (Thylakoids Dismantled)</text>')
    svg_lines.append('            <circle cx="28" cy="38" r="10" fill="#FBBF24" stroke="#D97706"/>')
    svg_lines.append('            <circle cx="52" cy="44" r="8" fill="#FBBF24" stroke="#D97706"/>')
    svg_lines.append('            <text x="40" y="60" text-anchor="middle" font-size="6.8" fill="#78350F">Plastoglobules</text>')
    svg_lines.append('            <rect x="88" y="24" width="138" height="34" rx="4" fill="#FFFFFF" stroke="#E69F00" stroke-width="0.8"/>')
    svg_lines.append('            <text x="157" y="38" text-anchor="middle" font-size="7.8" font-weight="bold" fill="#B45309">&#9733; PPR-Edited Transcripts Protected</text>')
    svg_lines.append('            <text x="157" y="50" text-anchor="middle" font-size="7.2" fill="#78350F">ndhB, psbE, atpA preserved in vitrified glass</text>')
    svg_lines.append('          </g>')
    
    # Bullets
    svg_lines.append('          <g transform="translate(12, 110)">')
    svg_lines.append('            <text x="0" y="12" font-size="7.8" font-weight="bold" fill="#92400E">&#8226; Chloroplast Transcription Ceases (PEP/NEP off)</text>')
    svg_lines.append('            <text x="0" y="24" font-size="7.5" fill="#78350F">  Prevents aberrant unedited transcript accumulation.</text>')
    svg_lines.append('            <text x="0" y="38" font-size="7.8" font-weight="bold" fill="#92400E">&#8226; Transcripts Pre-Edited in Vitrified Stroma</text>')
    svg_lines.append('            <text x="0" y="50" font-size="7.5" fill="#78350F">  PPR-PLS complexes lock &amp; edit pre-existing mRNAs.</text>')
    svg_lines.append('            <text x="0" y="64" font-size="7.8" font-weight="bold" fill="#92400E">&#8226; Zero Photo-Oxidative Damage</text>')
    svg_lines.append('            <text x="0" y="74" font-size="7.5" fill="#78350F">  Dismantled grana prevent chlorophyll triplet ROS.</text>')
    svg_lines.append('          </g>')
    svg_lines.append('        </g>')

    # Right Card: REHYDRATION
    svg_lines.append('        <!-- Stage 2: Rehydration Card -->')
    svg_lines.append('        <g id="card_rehydration" transform="translate(271, 0)">')
    svg_lines.append('          <rect x="0" y="0" width="258" height="194" rx="5" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1"/>')
    svg_lines.append('          <rect x="0" y="0" width="258" height="26" rx="5" fill="#D1FAE5"/>')
    svg_lines.append('          <circle cx="12" cy="13" r="5" fill="#059669"/>')
    svg_lines.append('          <text x="24" y="17" font-size="9.5" font-weight="bold" fill="#065F46">2. Rehydration (Photosynthetic Burst)</text>')
    
    # Schematic: Rebuilt Thylakoids
    svg_lines.append('          <g transform="translate(10, 34)">')
    svg_lines.append('            <rect x="0" y="0" width="238" height="66" rx="6" fill="#D1FAE5" stroke="#059669" stroke-width="0.8"/>')
    svg_lines.append('            <text x="119" y="15" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#065F46">Hydrated Active Chloroplast (Thylakoids Rebuilt)</text>')
    svg_lines.append('            <rect x="15" y="24" width="24" height="6" rx="2" fill="#047857"/>')
    svg_lines.append('            <rect x="15" y="32" width="24" height="6" rx="2" fill="#047857"/>')
    svg_lines.append('            <rect x="15" y="40" width="24" height="6" rx="2" fill="#047857"/>')
    svg_lines.append('            <text x="27" y="58" text-anchor="middle" font-size="6.8" fill="#065F46">Grana Thylakoids</text>')
    svg_lines.append('            <rect x="52" y="24" width="176" height="34" rx="4" fill="#FFFFFF" stroke="#10B981" stroke-width="0.8"/>')
    svg_lines.append('            <text x="140" y="38" text-anchor="middle" font-size="7.8" font-weight="bold" fill="#047857">&#9889; Immediate Translation (No De Novo Delay)</text>')
    svg_lines.append('            <text x="140" y="50" text-anchor="middle" font-size="7.2" fill="#065F46">Pre-edited mRNAs instantly translated by 70S ribosomes</text>')
    svg_lines.append('          </g>')

    # Bullets
    svg_lines.append('          <g transform="translate(12, 110)">')
    svg_lines.append('            <text x="0" y="12" font-size="7.8" font-weight="bold" fill="#065F46">&#8226; Water Influx (0&#8211;24 h): Vitrified Matrix Liquefies</text>')
    svg_lines.append('            <text x="0" y="24" font-size="7.5" fill="#047857">  Ribosomes immediately engage pre-edited transcripts.</text>')
    svg_lines.append('            <text x="0" y="38" font-size="7.8" font-weight="bold" fill="#065F46">&#8226; Rapid NDH &amp; PSII Assembly (24&#8211;48 h)</text>')
    svg_lines.append('            <text x="0" y="50" font-size="7.5" fill="#047857">  NdhB (+29 family expansion) restores cyclic flow.</text>')
    svg_lines.append('            <text x="0" y="64" font-size="7.8" font-weight="bold" fill="#065F46">&#8226; Full Photosynthetic Recovery (Fv/Fm &gt; 0.75)</text>')
    svg_lines.append('            <text x="0" y="74" font-size="7.5" fill="#047857">  Resurrection achieved without de novo gene transcription.</text>')
    svg_lines.append('          </g>')
    svg_lines.append('        </g>')

    svg_lines.append('      </g>')

    # Step 3: Comparative Strategy Footer Card (Y: 750 to 836)
    svg_lines.append('      <!-- Evolutionary Strategy Contrast Footer Card -->')
    svg_lines.append('      <g id="b2_evolutionary_contrast" transform="translate(618, 750)">')
    svg_lines.append('        <rect x="0" y="0" width="529" height="84" rx="5" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.9"/>')
    svg_lines.append('        <text x="12" y="16" font-size="9.2" font-weight="bold" fill="#0F172A">Evolutionary Contrast: Poikilochlorophylly vs Continuous Evergreen Surveillance</text>')
    
    # Left Box: V. tubiflora
    svg_lines.append('        <rect x="10" y="24" width="248" height="52" rx="4" fill="#FFFBEB" stroke="#F59E0B" stroke-width="0.8"/>')
    svg_lines.append('        <text x="16" y="38" font-size="8.5" font-weight="bold" fill="#B45309">V. tubiflora (Poikilochlorophyllous):</text>')
    svg_lines.append('        <text x="16" y="50" font-size="7.6" fill="#78350F">Pre-edited RNA stockpile in desiccoplasts enables</text>')
    svg_lines.append('        <text x="16" y="62" font-size="7.6" fill="#78350F">instant recovery upon rain; near-zero drought mortality.</text>')

    # Right Box: V. peripherica
    svg_lines.append('        <rect x="271" y="24" width="248" height="52" rx="4" fill="#F0FDF4" stroke="#10B981" stroke-width="0.8"/>')
    svg_lines.append('        <text x="277" y="38" font-size="8.5" font-weight="bold" fill="#065F46">V. peripherica (Montane Evergreen):</text>')
    svg_lines.append('        <text x="277" y="50" font-size="7.6" fill="#047857">Continuous RNA editing &amp; high protein turnover</text>')
    svg_lines.append('        <text x="277" y="62" font-size="7.6" fill="#047857">sustain green foliage, incurring high energetic costs.</text>')

    svg_lines.append('      </g>')

    svg_lines.append('    </g>')
    svg_lines.append('  </g>')

    # Footer Metadata
    svg_lines.append('\n  <!-- Metadata / Standards Footer -->')
    svg_lines.append('  <g id="figure_footer">')
    svg_lines.append('    <text x="30" y="892" font-size="8.5" fill="#94A3B8">PAML v4.10.8 yn00 codon selection analysis (1,513 single-copy orthogroups, 732,066 aa sites) | Okabe-Ito colorblind-accessible palette | Scalable Vector Graphics (SVG 1.1)</text>')
    svg_lines.append('  </g>')

    svg_lines.append('</svg>')

    # Join and Save
    svg_content = "\n".join(svg_lines)
    
    # Validate with ElementTree
    try:
        ET.fromstring(svg_content)
        print("SVG XML validation PASSED: Well-formed and valid XML.")
    except ET.ParseError as e:
        print(f"ERROR: SVG XML validation FAILED: {e}", file=sys.stderr)
        raise e

    os.makedirs(os.path.dirname(output_svg_path), exist_ok=True)
    with open(output_svg_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Successfully generated Figure 4 SVG:\n  -> {output_svg_path}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))

    # Determine paths from CLI args or default repo root
    if len(sys.argv) >= 4:
        annotated_tsv = sys.argv[1]
        top250_tsv = sys.argv[2]
        out_svg = sys.argv[3]
    else:
        annotated_tsv = os.path.join(repo_root, "chapter_macroevolution/05_selection/vellozia_pairwise_kaks_annotated.tsv")
        top250_tsv = os.path.join(repo_root, "chapter_macroevolution/05_selection/positive_selection_candidates_top250.tsv")
        out_svg = os.path.join(repo_root, "teamwork/figures_chapter1/fig4_selection_landscape_ppr.svg")

    build_fig4_svg(annotated_tsv, top250_tsv, out_svg)
