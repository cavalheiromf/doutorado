#!/usr/bin/env python3
"""
Publication-grade Figure 2 Generator for Chapter 1:
"Macroevolution and Genomic Divergence in Velloziaceae: from Deep Time to Contrasting Survival Strategies"

Figure 2: Orthology Partition & Chromosomal Syntenic Architecture
Panel A: Comparative Orthology Distribution across 7 Monocot Proteomes (OrthoFinder v3)
Panel B: Whole-Genome Chromosome-Scale Macrosynteny & Collinearity Map (V. tubiflora vs V. peripherica, 2n = 18)

Author: Mariana Feitosa Cavalheiro
Repository: /home/mfcaval/github/doutorado
Output: teamwork/figures_chapter1/fig2_orthology_macrosynteny.svg
"""

import os
import sys
import xml.etree.ElementTree as ET
import math

def create_figure2_svg():
    width = 1200
    height = 900

    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background-color: #FFFFFF; font-family: Arial, Helvetica, DejaVu Sans, sans-serif;">')

    # Definitions: Gradients, Filters, Markers
    svg_lines.append('  <defs>')
    # Drop shadow filter for callouts
    svg_lines.append('    <filter id="card-shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">')
    svg_lines.append('      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.07"/>')
    svg_lines.append('    </filter>')
    svg_lines.append('    <filter id="badge-shadow" x="-8%" y="-8%" width="116%" height="120%" filterUnits="userSpaceOnUse">')
    svg_lines.append('      <feDropShadow dx="0" dy="1.5" stdDeviation="2" flood-color="#0F172A" flood-opacity="0.10"/>')
    svg_lines.append('    </filter>')
    
    # Arrow markers
    svg_lines.append('    <marker id="arrow-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">')
    svg_lines.append('      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#882255"/>')
    svg_lines.append('    </marker>')
    svg_lines.append('    <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">')
    svg_lines.append('      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0072B2"/>')
    svg_lines.append('    </marker>')
    svg_lines.append('    <marker id="arrow-amber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">')
    svg_lines.append('      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#E69F00"/>')
    svg_lines.append('    </marker>')
    svg_lines.append('  </defs>')

    # 1. Canvas Background
    svg_lines.append('  <!-- 1. Background Layer -->')
    svg_lines.append('  <g id="canvas_background">')
    svg_lines.append(f'    <rect width="{width}" height="{height}" fill="#FFFFFF"/>')
    svg_lines.append('  </g>')

    # =========================================================================
    # PANEL A: Comparative Orthology Distribution (OrthoFinder v3)
    # =========================================================================
    svg_lines.append('  <!-- ================================================================= -->')
    svg_lines.append('  <!-- PANEL A: Comparative Orthology Distribution (OrthoFinder v3)      -->')
    svg_lines.append('  <!-- ================================================================= -->')
    svg_lines.append('  <g id="panel_a">')
    
    # Panel A Header Badge & Title
    svg_lines.append('    <g id="panel_a_header">')
    svg_lines.append('      <rect x="35" y="18" width="28" height="28" rx="6" fill="#0F172A"/>')
    svg_lines.append('      <text x="49" y="37" font-size="16" font-weight="bold" fill="#FFFFFF" text-anchor="middle" dominant-baseline="central">A</text>')
    svg_lines.append('      <text x="72" y="32" font-size="14" font-weight="bold" fill="#0F172A" dominant-baseline="central">Comparative Orthology Partition across 7 Monocot Proteomes (OrthoFinder v3)</text>')
    svg_lines.append('      <text x="820" y="32" font-size="11" font-weight="medium" fill="#64748B" text-anchor="end" dominant-baseline="central">191,075 genes | 17,750 orthogroups (93.2% assigned)</text>')
    svg_lines.append('    </g>')

    # -------------------------------------------------------------------------
    # Panel A Left: Species Breakdown Stacked Bars (X: 35 to 675, Y: 55 to 430)
    # -------------------------------------------------------------------------
    svg_lines.append('    <g id="panel_a_species_breakdown">')
    svg_lines.append('      <rect x="35" y="55" width="635" height="375" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.2"/>')
    svg_lines.append('      <text x="50" y="77" font-size="12" font-weight="bold" fill="#1E293B" dominant-baseline="central">Species-Level Gene Assignment &amp; Orthology Partition</text>')
    svg_lines.append('      <text x="50" y="93" font-size="9.5" fill="#64748B" dominant-baseline="central">Partition of 191,075 total genes into core, shared, lineage-specific, and unassigned subsets</text>')

    species_data = [
        {
            "code": "Ath",
            "name": "Arabidopsis thaliana",
            "role": "Eudicot outgroup",
            "total": 27549,
            "sc": 1513,
            "multi_core": 6497,
            "clade": 12433,
            "specific": 3967,
            "unassigned": 3139,
            "pct_in_og": "88.6%",
            "color_tag": "#64748B"
        },
        {
            "code": "Dala",
            "name": "Dioscorea alata",
            "role": "Basal monocot outgroup",
            "total": 33227,
            "sc": 1513,
            "multi_core": 5250,
            "clade": 21502,
            "specific": 2721,
            "unassigned": 2241,
            "pct_in_og": "93.3%",
            "color_tag": "#56B4E9"
        },
        {
            "code": "Ptec",
            "name": "Pandanus tectorius",
            "role": "Pandanaceae sister family",
            "total": 28399,
            "sc": 1513,
            "multi_core": 5672,
            "clade": 18419,
            "specific": 1135,
            "unassigned": 1660,
            "pct_in_og": "94.2%",
            "color_tag": "#0072B2"
        },
        {
            "code": "Abra",
            "name": "Acanthochlamys bracteata",
            "role": "Basal Velloziaceae sister",
            "total": 22914,
            "sc": 1513,
            "multi_core": 5394,
            "clade": 13343,
            "specific": 535,
            "unassigned": 2129,
            "pct_in_og": "90.7%",
            "color_tag": "#CC79A7"
        },
        {
            "code": "Xvis",
            "name": "Xerophyta viscosa",
            "role": "African resurrection plant",
            "total": 26969,
            "sc": 1513,
            "multi_core": 6938,
            "clade": 15762,
            "specific": 1016,
            "unassigned": 1740,
            "pct_in_og": "93.5%",
            "color_tag": "#CC79A7"
        },
        {
            "code": "Vper",
            "name": "Vellozia peripherica",
            "role": "Evergreen generalist (2n=18)",
            "total": 26466,
            "sc": 1513,
            "multi_core": 7639,
            "clade": 15437,
            "specific": 552,
            "unassigned": 1325,
            "pct_in_og": "95.0%",
            "color_tag": "#009E73"
        },
        {
            "code": "Vtub",
            "name": "Vellozia tubiflora",
            "role": "Resurrection saxicole (2n=18)",
            "total": 25551,
            "sc": 1513,
            "multi_core": 8244,
            "clade": 14813,
            "specific": 159,
            "unassigned": 822,
            "pct_in_og": "96.8%",
            "color_tag": "#E69F00"
        }
    ]

    # Bar chart coordinate parameters
    y_bar_start = 115
    y_bar_step = 36
    bar_height = 20
    bar_x_start = 220
    max_bar_width = 330
    scale_max_genes = 35000

    for i, sp in enumerate(species_data):
        y = y_bar_start + i * y_bar_step
        
        # Species indicator dot
        svg_lines.append(f'      <circle cx="56" cy="{y + bar_height/2}" r="4" fill="{sp["color_tag"]}"/>')
        
        # Species label (Italic species name + code)
        svg_lines.append(f'      <text x="66" y="{y + bar_height/2 - 4}" font-size="10.5" font-weight="bold" fill="#0F172A" dominant-baseline="central">')
        svg_lines.append(f'        <tspan font-style="italic">{sp["name"]}</tspan> <tspan font-size="9" font-weight="normal" fill="#64748B">({sp["code"]})</tspan>')
        svg_lines.append('      </text>')
        svg_lines.append(f'      <text x="66" y="{y + bar_height/2 + 7}" font-size="8" fill="#64748B" dominant-baseline="central">{sp["role"]}</text>')

        # Calculate stacked bar segment widths
        w_sc = (sp["sc"] / scale_max_genes) * max_bar_width
        w_multi = (sp["multi_core"] / scale_max_genes) * max_bar_width
        w_clade = (sp["clade"] / scale_max_genes) * max_bar_width
        w_spec = (sp["specific"] / scale_max_genes) * max_bar_width
        w_unass = (sp["unassigned"] / scale_max_genes) * max_bar_width
        tot_w = w_sc + w_multi + w_clade + w_spec + w_unass

        # Background track
        svg_lines.append(f'      <rect x="{bar_x_start}" y="{y}" width="{max_bar_width}" height="{bar_height}" rx="3" fill="#E2E8F0" fill-opacity="0.4"/>')

        # Segments
        curr_x = bar_x_start
        # 1:1 single copy core (#0072B2)
        svg_lines.append(f'      <rect x="{curr_x}" y="{y}" width="{w_sc}" height="{bar_height}" rx="3" fill="#0072B2"/>')
        curr_x += w_sc
        # Multi-copy shared (#56B4E9)
        svg_lines.append(f'      <rect x="{curr_x}" y="{y}" width="{w_multi}" height="{bar_height}" fill="#56B4E9"/>')
        curr_x += w_multi
        # Clade-shared (#009E73 / #4E79A7)
        svg_lines.append(f'      <rect x="{curr_x}" y="{y}" width="{w_clade}" height="{bar_height}" fill="#71B280"/>')
        curr_x += w_clade
        # Species-specific (#E69F00)
        svg_lines.append(f'      <rect x="{curr_x}" y="{y}" width="{w_spec}" height="{bar_height}" fill="#E69F00"/>')
        curr_x += w_spec
        # Unassigned singletons (#CBD5E1)
        svg_lines.append(f'      <rect x="{curr_x}" y="{y}" width="{w_unass}" height="{bar_height}" rx="3" fill="#CBD5E1"/>')

        # Total and percentage label
        svg_lines.append(f'      <text x="{bar_x_start + max_bar_width + 8}" y="{y + bar_height/2}" font-size="9" font-weight="bold" fill="#1E293B" dominant-baseline="central">{sp["total"]:,} <tspan font-size="8" font-weight="normal" fill="#009E73">({sp["pct_in_og"]})</tspan></text>')

    # Legend for Panel A stacked bars
    leg_y = 385
    svg_lines.append('      <g id="panel_a_stacked_legend">')
    svg_lines.append('        <line x1="50" y1="373" x2="655" y2="373" stroke="#E2E8F0" stroke-width="1"/>')
    
    legs = [
        ("#0072B2", "1:1 Core (1,513)"),
        ("#56B4E9", "Multi-Copy Shared"),
        ("#71B280", "Clade-Shared"),
        ("#E69F00", "Species-Specific"),
        ("#CBD5E1", "Unassigned (Singletons)")
    ]
    leg_x = 50
    for col, text in legs:
        svg_lines.append(f'        <rect x="{leg_x}" y="{leg_y}" width="10" height="10" rx="2" fill="{col}"/>')
        svg_lines.append(f'        <text x="{leg_x + 14}" y="{leg_y + 6}" font-size="8" font-weight="medium" fill="#334155" dominant-baseline="central">{text}</text>')
        leg_x += len(text) * 5.2 + 26
    svg_lines.append('      </g>')
    svg_lines.append('    </g>')

    # -------------------------------------------------------------------------
    # Panel A Right: Global Metrics & UpSet Sharing Histogram (X: 685 to 1165)
    # -------------------------------------------------------------------------
    svg_lines.append('    <g id="panel_a_global_metrics">')
    svg_lines.append('      <rect x="685" y="55" width="480" height="375" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.2"/>')
    svg_lines.append('      <text x="700" y="77" font-size="12" font-weight="bold" fill="#1E293B" dominant-baseline="central">Global Orthogroup Partition &amp; Sharing Spectrum</text>')
    svg_lines.append('      <text x="700" y="93" font-size="9.5" fill="#64748B" dominant-baseline="central">17,750 Orthogroups across 7 species (OrthoFinder v3.1.5)</text>')

    # 4 KPI Summary Cards
    kpis = [
        {"title": "TOTAL GENES", "val": "191,075", "sub": "93.2% in OGs", "col": "#0F172A", "subcol": "#009E73"},
        {"title": "ORTHOGROUPS", "val": "17,750", "sub": "Median size: 8.0", "col": "#0F172A", "subcol": "#64748B"},
        {"title": "UNIVERSAL CORE", "val": "9,826", "sub": "All 7 species", "col": "#0072B2", "subcol": "#0072B2"},
        {"title": "1:1 SINGLE-COPY", "val": "1,513", "sub": "732,066 aa matrix", "col": "#D55E00", "subcol": "#D55E00"}
    ]
    kpi_x_start = 700
    kpi_w = 105
    kpi_gap = 10
    for k_idx, kpi in enumerate(kpis):
        kx = kpi_x_start + k_idx * (kpi_w + kpi_gap)
        ky = 108
        svg_lines.append(f'      <g id="kpi_{k_idx}">')
        svg_lines.append(f'        <rect x="{kx}" y="{ky}" width="{kpi_w}" height="52" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" filter="url(#badge-shadow)"/>')
        svg_lines.append(f'        <text x="{kx + kpi_w/2}" y="{ky + 12}" font-size="7.2" font-weight="bold" fill="#64748B" text-anchor="middle" dominant-baseline="central">{kpi["title"]}</text>')
        svg_lines.append(f'        <text x="{kx + kpi_w/2}" y="{ky + 28}" font-size="13.5" font-weight="bold" fill="{kpi["col"]}" text-anchor="middle" dominant-baseline="central">{kpi["val"]}</text>')
        svg_lines.append(f'        <text x="{kx + kpi_w/2}" y="{ky + 42}" font-size="7.5" font-weight="medium" fill="{kpi["subcol"]}" text-anchor="middle" dominant-baseline="central">{kpi["sub"]}</text>')
        svg_lines.append('      </g>')

    # Sharing Depth Histogram & UpSet Matrix
    svg_lines.append('      <g id="panel_a_sharing_histogram">')
    svg_lines.append('        <text x="700" y="180" font-size="10.5" font-weight="bold" fill="#1E293B" dominant-baseline="central">Orthogroup Frequency by Species Occupancy (1 to 7 Species)</text>')
    
    # Histogram Data
    hist_data = [
        {"species_n": 7, "ogs": 9826, "pct": "55.4%", "col": "#0072B2", "label": "Universal Core"},
        {"species_n": 6, "ogs": 2031, "pct": "11.4%", "col": "#56B4E9", "label": "6 Species"},
        {"species_n": 5, "ogs": 692, "pct": "3.9%", "col": "#56B4E9", "label": "5 Species"},
        {"species_n": 4, "ogs": 520, "pct": "2.9%", "col": "#71B280", "label": "4 Species"},
        {"species_n": 3, "ogs": 801, "pct": "4.5%", "col": "#71B280", "label": "3 Species"},
        {"species_n": 2, "ogs": 1582, "pct": "8.9%", "col": "#E69F00", "label": "2 Species"},
        {"species_n": 1, "ogs": 2298, "pct": "12.9%", "col": "#D55E00", "label": "Species-Specific"}
    ]

    h_x_start = 715
    h_w = 54
    h_gap = 11
    h_base_y = 330
    h_max_height = 120
    max_ogs = 10500

    # Gridlines
    for grid_val in [2500, 5000, 7500, 10000]:
        gy = h_base_y - (grid_val / max_ogs) * h_max_height
        svg_lines.append(f'        <line x1="705" y1="{gy}" x2="1150" y2="{gy}" stroke="#E2E8F0" stroke-width="0.8" stroke-dasharray="3,3"/>')
        svg_lines.append(f'        <text x="700" y="{gy}" font-size="7" fill="#94A3B8" text-anchor="end" dominant-baseline="central">{grid_val:,}</text>')

    for h_idx, hd in enumerate(hist_data):
        hx = h_x_start + h_idx * (h_w + h_gap)
        hbar_h = (hd["ogs"] / max_ogs) * h_max_height
        hy = h_base_y - hbar_h
        
        # Bar
        svg_lines.append(f'        <rect x="{hx}" y="{hy}" width="{h_w}" height="{hbar_h}" rx="3" fill="{hd["col"]}"/>')
        
        # Value label on top
        svg_lines.append(f'        <text x="{hx + h_w/2}" y="{hy - 11}" font-size="8.5" font-weight="bold" fill="#0F172A" text-anchor="middle" dominant-baseline="central">{hd["ogs"]:,}</text>')
        svg_lines.append(f'        <text x="{hx + h_w/2}" y="{hy - 3}" font-size="7" font-weight="normal" fill="#64748B" text-anchor="middle" dominant-baseline="central">({hd["pct"]})</text>')
        
        # Category label under bar
        svg_lines.append(f'        <text x="{hx + h_w/2}" y="{h_base_y + 12}" font-size="8" font-weight="bold" fill="#1E293B" text-anchor="middle" dominant-baseline="central">{hd["species_n"]} sp.</text>')
        
        # UpSet mini visual dots (depth indicator)
        for dot_i in range(7):
            dot_y = h_base_y + 24 + dot_i * 8.5
            dot_fill = hd["col"] if dot_i < hd["species_n"] else "#E2E8F0"
            svg_lines.append(f'        <circle cx="{hx + h_w/2}" cy="{dot_y}" r="3" fill="{dot_fill}"/>')
            if dot_i < hd["species_n"] - 1:
                svg_lines.append(f'        <line x1="{hx + h_w/2}" y1="{dot_y}" x2="{hx + h_w/2}" y2="{dot_y + 8.5}" stroke="{hd["col"]}" stroke-width="1.2"/>')

    # X-axis baseline
    svg_lines.append(f'        <line x1="705" y1="{h_base_y}" x2="1150" y2="{h_base_y}" stroke="#94A3B8" stroke-width="1"/>')
    svg_lines.append('      </g>')
    svg_lines.append('    </g>')
    svg_lines.append('  </g>')

    # =========================================================================
    # PANEL B: Chromosome-Scale Macrosynteny & Collinearity Map
    # =========================================================================
    svg_lines.append('  <!-- ================================================================= -->')
    svg_lines.append('  <!-- PANEL B: Chromosome-Scale Macrosynteny & Collinearity Map         -->')
    svg_lines.append('  <!-- ================================================================= -->')
    svg_lines.append('  <g id="panel_b">')
    
    # Panel B Header Badge & Title
    svg_lines.append('    <g id="panel_b_header">')
    svg_lines.append('      <rect x="35" y="445" width="28" height="28" rx="6" fill="#0F172A"/>')
    svg_lines.append('      <text x="49" y="464" font-size="16" font-weight="bold" fill="#FFFFFF" text-anchor="middle" dominant-baseline="central">B</text>')
    svg_lines.append('      <text x="72" y="459" font-size="14" font-weight="bold" fill="#0F172A" dominant-baseline="central">Chromosome-Scale Macrosynteny &amp; Collinearity Dual-Track Map (2n = 18, x = 9)</text>')
    svg_lines.append('      <text x="1165" y="459" font-size="11" font-weight="bold" fill="#0072B2" text-anchor="end" dominant-baseline="central">297 Collinear Syntenic Blocks | Complete Macrosyntenic Stasis (0 Translocations)</text>')
    svg_lines.append('    </g>')

    # Panel B Background Container
    svg_lines.append('    <rect x="35" y="480" width="1130" height="405" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.2"/>')

    # Chromosome physical lengths (Mb) and gene counts
    chrom_info = [
        {"chr": "Chr1A", "vtub_mb": 72.4, "vper_mb": 75.1, "vtub_genes": 3591, "vper_genes": 3994, "color": "#4E79A7"},
        {"chr": "Chr2A", "vtub_mb": 61.8, "vper_mb": 63.4, "vtub_genes": 2862, "vper_genes": 3122, "color": "#F28E2B"},
        {"chr": "Chr3A", "vtub_mb": 64.5, "vper_mb": 66.2, "vtub_genes": 3078, "vper_genes": 3366, "color": "#E15759"},
        {"chr": "Chr4A", "vtub_mb": 63.2, "vper_mb": 65.8, "vtub_genes": 3048, "vper_genes": 3379, "color": "#76B7B2"},
        {"chr": "Chr5A", "vtub_mb": 58.1, "vper_mb": 59.7, "vtub_genes": 1980, "vper_genes": 2377, "color": "#59A14F"},
        {"chr": "Chr6A", "vtub_mb": 52.4, "vper_mb": 54.1, "vtub_genes": 1970, "vper_genes": 2251, "color": "#EDC948"},
        {"chr": "Chr7A", "vtub_mb": 56.7, "vper_mb": 58.9, "vtub_genes": 2382, "vper_genes": 2639, "color": "#B07AA1"},
        {"chr": "Chr8A", "vtub_mb": 54.3, "vper_mb": 56.2, "vtub_genes": 2367, "vper_genes": 2541, "color": "#FF9DA7"},
        {"chr": "Chr9A", "vtub_mb": 49.6, "vper_mb": 51.3, "vtub_genes": 2074, "vper_genes": 2279, "color": "#9C755F"}
    ]

    vtub_tot_mb = sum(c["vtub_mb"] for c in chrom_info) # 533.0 Mb
    vper_tot_mb = sum(c["vper_mb"] for c in chrom_info) # 550.7 Mb

    track_x0 = 150
    track_w = 985
    gap_px = 11
    avail_w = track_w - gap_px * 8

    # Calculate X coordinates for each chromosome on Top (Vtub) and Bottom (Vper)
    vtub_coords = []
    curr_x = track_x0
    for c in chrom_info:
        w = (c["vtub_mb"] / vtub_tot_mb) * avail_w
        vtub_coords.append({"start": curr_x, "end": curr_x + w, "width": w})
        curr_x += w + gap_px

    vper_coords = []
    curr_x = track_x0
    for c in chrom_info:
        w = (c["vper_mb"] / vper_tot_mb) * avail_w
        vper_coords.append({"start": curr_x, "end": curr_x + w, "width": w})
        curr_x += w + gap_px

    y_top = 548
    y_bot = 785
    h_bar = 22
    y_top_bot = y_top + h_bar
    y_bot_top = y_bot

    # Species Track Labels on Left
    svg_lines.append('    <g id="synteny_track_labels">')
    # Vtub label
    svg_lines.append(f'      <text x="{track_x0 - 18}" y="{y_top + 3}" font-size="11" font-weight="bold" fill="#B37700" text-anchor="end" dominant-baseline="central">')
    svg_lines.append('        <tspan font-style="italic">Vellozia tubiflora</tspan>')
    svg_lines.append('      </text>')
    svg_lines.append(f'      <text x="{track_x0 - 18}" y="{y_top + 16}" font-size="8.5" font-weight="bold" fill="#E69F00" text-anchor="end" dominant-baseline="central">Resurrection Specialist (n=9)</text>')
    svg_lines.append(f'      <text x="{track_x0 - 18}" y="{y_top + 28}" font-size="7.5" fill="#64748B" text-anchor="end" dominant-baseline="central">533.0 Mb | 23,352 genes</text>')

    # Vper label
    svg_lines.append(f'      <text x="{track_x0 - 18}" y="{y_bot + 3}" font-size="11" font-weight="bold" fill="#007353" text-anchor="end" dominant-baseline="central">')
    svg_lines.append('        <tspan font-style="italic">Vellozia peripherica</tspan>')
    svg_lines.append('      </text>')
    svg_lines.append(f'      <text x="{track_x0 - 18}" y="{y_bot + 16}" font-size="8.5" font-weight="bold" fill="#009E73" text-anchor="end" dominant-baseline="central">Evergreen Generalist (n=9)</text>')
    svg_lines.append(f'      <text x="{track_x0 - 18}" y="{y_bot + 28}" font-size="7.5" fill="#64748B" text-anchor="end" dominant-baseline="central">550.7 Mb | 25,948 genes</text>')
    svg_lines.append('    </g>')

    # -------------------------------------------------------------------------
    # Syntenic Collinear Ribbons (297 collinear blocks linking 9 pairs)
    # -------------------------------------------------------------------------
    svg_lines.append('    <g id="synteny_collinear_ribbons">')
    
    # Sub-ribbons per chromosome to realistically depict 297 syntenic blocks
    blocks_per_chr = [48, 38, 42, 40, 28, 26, 32, 24, 19] # sum = 297
    
    for i, c in enumerate(chrom_info):
        s_t = vtub_coords[i]["start"]
        e_t = vtub_coords[i]["end"]
        s_p = vper_coords[i]["start"]
        e_p = vper_coords[i]["end"]
        col = c["color"]
        n_sub = blocks_per_chr[i]

        # Draw finely structured sub-ribbons
        for j in range(n_sub):
            # Proportional slices
            f0 = j / n_sub
            f1 = (j + 0.88) / n_sub
            sub_s_t = s_t + f0 * (e_t - s_t)
            sub_e_t = s_t + f1 * (e_t - s_t)
            sub_s_p = s_p + f0 * (e_p - s_p)
            sub_e_p = s_p + f1 * (e_p - s_p)

            mid_y = (y_top_bot + y_bot_top) / 2

            # Smooth cubic Bézier ribbon
            d_path = f"M {sub_s_t:.2f} {y_top_bot} C {sub_s_t:.2f} {mid_y}, {sub_s_p:.2f} {mid_y}, {sub_s_p:.2f} {y_bot_top} L {sub_e_p:.2f} {y_bot_top} C {sub_e_p:.2f} {mid_y}, {sub_e_t:.2f} {mid_y}, {sub_e_t:.2f} {y_top_bot} Z"
            svg_lines.append(f'      <path d="{d_path}" fill="{col}" fill-opacity="0.32" stroke="none"/>')

    svg_lines.append('    </g>')

    # -------------------------------------------------------------------------
    # Paleoduplication WGD Cross-Ribbon (Chr1A <-> Chr5A)
    # -------------------------------------------------------------------------
    svg_lines.append('    <g id="synteny_paleoduplication_wgd">')
    # Connect Chr1A (top) to Chr5A (bottom) with stylized translucent purple ribbon
    c1_s_t = vtub_coords[0]["start"] + 15
    c1_e_t = vtub_coords[0]["start"] + 65
    c5_s_p = vper_coords[4]["start"] + 10
    c5_e_p = vper_coords[4]["start"] + 55
    
    mid_y_wgd = (y_top_bot + y_bot_top) / 2
    d_wgd = f"M {c1_s_t:.2f} {y_top_bot} C {c1_s_t + 100:.2f} {mid_y_wgd - 30}, {c5_s_p - 100:.2f} {mid_y_wgd + 30}, {c5_s_p:.2f} {y_bot_top} L {c5_e_p:.2f} {y_bot_top} C {c5_e_p - 100:.2f} {mid_y_wgd + 30}, {c1_e_t + 100:.2f} {mid_y_wgd - 30}, {c1_e_t:.2f} {y_top_bot} Z"
    
    svg_lines.append(f'      <path d="{d_wgd}" fill="#CC79A7" fill-opacity="0.45" stroke="#882255" stroke-width="1.2" stroke-dasharray="4,3"/>')
    svg_lines.append('    </g>')

    # -------------------------------------------------------------------------
    # Top Chromosomes (V. tubiflora)
    # -------------------------------------------------------------------------
    svg_lines.append('    <g id="synteny_chromosomes_vtub">')
    for i, c in enumerate(chrom_info):
        x = vtub_coords[i]["start"]
        w = vtub_coords[i]["width"]
        mid_x = x + w / 2
        
        # Chromosome Pill
        svg_lines.append(f'      <rect x="{x:.2f}" y="{y_top}" width="{w:.2f}" height="{h_bar}" rx="5" fill="#E69F00" stroke="#B37700" stroke-width="1.5"/>')
        
        # Gene density stripes / bands
        svg_lines.append(f'      <rect x="{x + 4:.2f}" y="{y_top + 3}" width="{w - 8:.2f}" height="{h_bar - 6}" rx="3" fill="#D55E00" fill-opacity="0.25"/>')
        
        # Chromosome label above
        svg_lines.append(f'      <text x="{mid_x:.2f}" y="{y_top - 12}" font-size="9.5" font-weight="bold" fill="#0F172A" text-anchor="middle" dominant-baseline="central">{c["chr"]}</text>')
        svg_lines.append(f'      <text x="{mid_x:.2f}" y="{y_top - 3}" font-size="7.2" fill="#64748B" text-anchor="middle" dominant-baseline="central">{c["vtub_mb"]} Mb</text>')
        
        # Centromere notch marker
        cent_x = x + w * 0.42
        svg_lines.append(f'      <line x1="{cent_x:.2f}" y1="{y_top}" x2="{cent_x:.2f}" y2="{y_top + h_bar}" stroke="#B37700" stroke-width="1.5" stroke-dasharray="2,2"/>')
    svg_lines.append('    </g>')

    # -------------------------------------------------------------------------
    # Bottom Chromosomes (V. peripherica)
    # -------------------------------------------------------------------------
    svg_lines.append('    <g id="synteny_chromosomes_vper">')
    for i, c in enumerate(chrom_info):
        x = vper_coords[i]["start"]
        w = vper_coords[i]["width"]
        mid_x = x + w / 2
        
        # Chromosome Pill
        svg_lines.append(f'      <rect x="{x:.2f}" y="{y_bot}" width="{w:.2f}" height="{h_bar}" rx="5" fill="#009E73" stroke="#007353" stroke-width="1.5"/>')
        
        # Gene density stripes / bands
        svg_lines.append(f'      <rect x="{x + 4:.2f}" y="{y_bot + 3}" width="{w - 8:.2f}" height="{h_bar - 6}" rx="3" fill="#004D40" fill-opacity="0.25"/>')
        
        # Chromosome label below
        svg_lines.append(f'      <text x="{mid_x:.2f}" y="{y_bot + h_bar + 9}" font-size="9.5" font-weight="bold" fill="#0F172A" text-anchor="middle" dominant-baseline="central">{c["chr"]}</text>')
        svg_lines.append(f'      <text x="{mid_x:.2f}" y="{y_bot + h_bar + 18}" font-size="7.2" fill="#64748B" text-anchor="middle" dominant-baseline="central">{c["vper_mb"]} Mb</text>')
        
        # Centromere notch marker
        cent_x = x + w * 0.42
        svg_lines.append(f'      <line x1="{cent_x:.2f}" y1="{y_bot}" x2="{cent_x:.2f}" y2="{y_bot + h_bar}" stroke="#007353" stroke-width="1.5" stroke-dasharray="2,2"/>')
    svg_lines.append('    </g>')

    # -------------------------------------------------------------------------
    # Callout 1: Ancestral WGD Paleoduplication Callout (Chr1A <-> Chr5A)
    # -------------------------------------------------------------------------
    svg_lines.append('    <g id="callout_paleoduplication">')
    wgd_card_x = 350
    wgd_card_y = 612
    wgd_card_w = 265
    wgd_card_h = 58

    # Background card
    svg_lines.append(f'      <rect x="{wgd_card_x}" y="{wgd_card_y}" width="{wgd_card_w}" height="{wgd_card_h}" rx="6" fill="#FFFFFF" stroke="#882255" stroke-width="1.2" filter="url(#card-shadow)"/>')
    
    # Badge
    svg_lines.append(f'      <rect x="{wgd_card_x + 8}" y="{wgd_card_y + 8}" width="16" height="16" rx="4" fill="#882255"/>')
    svg_lines.append(f'      <text x="{wgd_card_x + 16}" y="{wgd_card_y + 16}" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle" dominant-baseline="central">&#x2605;</text>')
    
    # Title
    svg_lines.append(f'      <text x="{wgd_card_x + 30}" y="{wgd_card_y + 16}" font-size="9" font-weight="bold" fill="#882255" dominant-baseline="central">Ancestral WGD Paleoduplication (Chr1A &#x2194; Chr5A)</text>')
    
    # Subtext
    svg_lines.append(f'      <text x="{wgd_card_x + 10}" y="{wgd_card_y + 33}" font-size="7.8" fill="#334155" dominant-baseline="central">Conserved segmental duplication predating Vellozia split:</text>')
    svg_lines.append(f'      <text x="{wgd_card_x + 10}" y="{wgd_card_y + 46}" font-size="7.5" font-weight="bold" fill="#0F172A" dominant-baseline="central">&#x2022; <tspan font-style="italic">OSCA2.2</tspan> &#x2194; <tspan font-style="italic">OSCA2.1</tspan> &amp; <tspan font-style="italic">OSCA3.1</tspan> &#x2194; <tspan font-style="italic">OSCA3.2</tspan></text>')
    
    # Pointer lines to Chr1A and Chr5A
    svg_lines.append(f'      <path d="M {wgd_card_x} {wgd_card_y + 20} C 280 610, 240 580, {vtub_coords[0]["start"] + 50} {y_top_bot}" fill="none" stroke="#882255" stroke-width="1.2" stroke-dasharray="3,2"/>')
    svg_lines.append(f'      <path d="M {wgd_card_x + wgd_card_w} {wgd_card_y + 40} C 650 670, {vper_coords[4]["start"]} 720, {vper_coords[4]["start"] + 30} {y_bot_top}" fill="none" stroke="#882255" stroke-width="1.2" stroke-dasharray="3,2"/>')
    svg_lines.append('    </g>')

    # -------------------------------------------------------------------------
    # Callout 2: Chr7A Conserved Tandem Triplication Cluster (OSCA1.3/1.4/1.5)
    # -------------------------------------------------------------------------
    svg_lines.append('    <g id="callout_tandem_triplication">')
    trip_x = 835
    trip_y = 612
    trip_w = 285
    trip_h = 58

    # Background card
    svg_lines.append(f'      <rect x="{trip_x}" y="{trip_y}" width="{trip_w}" height="{trip_h}" rx="6" fill="#FFFFFF" stroke="#B07AA1" stroke-width="1.2" filter="url(#card-shadow)"/>')
    
    # Badge
    svg_lines.append(f'      <rect x="{trip_x + 8}" y="{trip_y + 8}" width="16" height="16" rx="4" fill="#B07AA1"/>')
    svg_lines.append(f'      <text x="{trip_x + 16}" y="{trip_y + 16}" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle" dominant-baseline="central">&#x2713;</text>')
    
    # Title
    svg_lines.append(f'      <text x="{trip_x + 30}" y="{trip_y + 16}" font-size="9" font-weight="bold" fill="#783F6D" dominant-baseline="central">Conserved Tandem Triplication Cluster (Chr7A)</text>')
    
    # Subtext
    svg_lines.append(f'      <text x="{trip_x + 10}" y="{trip_y + 33}" font-size="7.8" fill="#334155" dominant-baseline="central"><tspan font-style="italic">OSCA1.3 &#x2192; OSCA1.4 &#x2192; OSCA1.5</tspan> physically contiguous</text>')
    svg_lines.append(f'      <text x="{trip_x + 10}" y="{trip_y + 46}" font-size="7.5" fill="#64748B" dominant-baseline="central">0 intervening genes in both taxa | 24 flanking collinear orthologs</text>')
    
    # Pointers to Chr7A
    chr7_mid_top = vtub_coords[6]["start"] + vtub_coords[6]["width"] / 2
    chr7_mid_bot = vper_coords[6]["start"] + vper_coords[6]["width"] / 2
    svg_lines.append(f'      <path d="M {trip_x + 60} {trip_y} C {trip_x + 50} 580, {chr7_mid_top} 570, {chr7_mid_top} {y_top_bot}" fill="none" stroke="#B07AA1" stroke-width="1.2" stroke-dasharray="3,2"/>')
    svg_lines.append(f'      <path d="M {trip_x + 60} {trip_y + trip_h} C {trip_x + 50} 740, {chr7_mid_bot} 750, {chr7_mid_bot} {y_bot_top}" fill="none" stroke="#B07AA1" stroke-width="1.2" stroke-dasharray="3,2"/>')
    svg_lines.append('    </g>')

    # -------------------------------------------------------------------------
    # Callout 3: Lineage-Specific Chr1A Tandem Expansion (OSCA2.4a/b vs Single-Copy)
    # -------------------------------------------------------------------------
    svg_lines.append('    <g id="callout_tandem_expansion_chr1a">')
    exp_x = 150
    exp_y = 688
    exp_w = 265
    exp_h = 50

    svg_lines.append(f'      <rect x="{exp_x}" y="{exp_y}" width="{exp_w}" height="{exp_h}" rx="6" fill="#FFFFFF" stroke="#009E73" stroke-width="1.1" filter="url(#card-shadow)"/>')
    svg_lines.append(f'      <text x="{exp_x + 10}" y="{exp_y + 14}" font-size="8.5" font-weight="bold" fill="#007353" dominant-baseline="central">Lineage-Specific Tandem Duplication (Chr1A)</text>')
    svg_lines.append(f'      <text x="{exp_x + 10}" y="{exp_y + 27}" font-size="7.5" fill="#334155" dominant-baseline="central"><tspan font-style="italic">V. peripherica</tspan>: tandem <tspan font-style="italic">VpOSCA2.4a / 2.4b</tspan> (g023030/020)</text>')
    svg_lines.append(f'      <text x="{exp_x + 10}" y="{exp_y + 39}" font-size="7.5" fill="#B37700" dominant-baseline="central"><tspan font-style="italic">V. tubiflora</tspan>: single copy <tspan font-style="italic">VtOSCA2.4</tspan> (g020650)</text>')
    
    # Pointer to Chr1A
    svg_lines.append(f'      <path d="M {exp_x + 40} {exp_y + exp_h} C {exp_x + 30} 760, {vper_coords[0]["start"] + 30} 765, {vper_coords[0]["start"] + 30} {y_bot_top}" fill="none" stroke="#009E73" stroke-width="1.1" stroke-dasharray="3,2"/>')
    svg_lines.append('    </g>')

    # -------------------------------------------------------------------------
    # Central Macrosyntenic Stasis Banner
    # -------------------------------------------------------------------------
    svg_lines.append('    <g id="synteny_status_banner">')
    ban_x = 445
    ban_y = 690
    ban_w = 460
    ban_h = 32
    svg_lines.append(f'      <rect x="{ban_x}" y="{ban_y}" width="{ban_w}" height="{ban_h}" rx="16" fill="#0F172A" stroke="#334155" stroke-width="1.2" filter="url(#badge-shadow)"/>')
    svg_lines.append(f'      <circle cx="{ban_x + 18}" cy="{ban_y + ban_h/2}" r="6" fill="#009E73"/>')
    svg_lines.append(f'      <text x="{ban_x + 32}" y="{ban_y + ban_h/2}" font-size="9.5" font-weight="bold" fill="#FFFFFF" dominant-baseline="central">297 Collinear Blocks | Complete Macrosyntenic Stasis (0 Translocations)</text>')
    svg_lines.append('    </g>')

    # Assembly quality footnote on bottom right of Panel B
    svg_lines.append('    <g id="synteny_footnote">')
    svg_lines.append('      <text x="1150" y="870" font-size="8" fill="#64748B" text-anchor="end" dominant-baseline="central">BUSCO Completeness: &gt;95.0% Embryophyta in both taxa | Chromosome Anchoring: 97.8% (Vtub) vs 98.2% (Vper) | Braz et al. (2025)</text>')
    svg_lines.append('    </g>')

    svg_lines.append('  </g>')

    svg_lines.append('</svg>')
    
    return "\n".join(svg_lines)


def main():
    output_dir = "/home/mfcaval/github/doutorado/teamwork/figures_chapter1"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, "scripts"), exist_ok=True)
    
    svg_content = create_figure2_svg()
    
    svg_path = os.path.join(output_dir, "fig2_orthology_macrosynteny.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    
    print(f"Generated Figure 2 SVG successfully: {svg_path}")
    
    # XML Validation Check
    try:
        tree = ET.parse(svg_path)
        root = tree.getroot()
        print(f"XML Validation Passed: Root tag='{root.tag}', viewBox='{root.attrib.get('viewBox')}'")
    except Exception as e:
        print(f"XML Validation Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
