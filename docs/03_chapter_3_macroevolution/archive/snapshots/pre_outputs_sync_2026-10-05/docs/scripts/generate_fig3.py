#!/usr/bin/env python3
"""
Publication-Grade Vector Figure 3 Generator
Chapter 1: Macroevolution and Genomic Divergence in Velloziaceae
Figure 3: Gene Family Dynamics & Asymmetric Lineage Turnover (CAFE5)

Author: Mariana Feitosa Cavalheiro
Advisor: Isabel Rodrigues Gerhardt
Institution: UNICAMP
Date: August 31, 2026

Description:
Generates publication-ready vector Figure 3 in pure SVG XML format.
Figure 3 integrates:
  - Panel A: Dated species chronogram annotated with branch-specific gene family
             expansions (+) and contractions (-) under CAFE5 Gamma model (lambda = 0.6383).
  - Panel B: Comparative functional category expansion barplots contrasting
             Vellozia tubiflora (resurrection) vs. Vellozia peripherica (evergreen).
  - Panel C: Diagnostic adaptive gene family trajectories (Ancestral -> Vtub vs Vper)
             and the conceptual synthesis of 'The Genomic Burden of Being Evergreen'.

Standards:
  - Accessible Okabe-Ito color palette.
  - Pure SVG vector output (viewBox="0 0 1200 900").
  - Hierarchical semantic XML groups (<g id="...">).
  - Standard sans-serif fonts (Arial/Helvetica/DejaVu Sans) with selectable text.
"""

import os
import sys
import xml.etree.ElementTree as ET

def escape_xml(text: str) -> str:
    """Escapes special XML characters."""
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&apos;"))

def create_figure_3_svg(output_path: str):
    """Constructs and writes the complete Figure 3 SVG."""
    
    # -------------------------------------------------------------
    # 1. Colors and Theme Constants (Okabe-Ito & Publication Palette)
    # -------------------------------------------------------------
    c_bg = "#FFFFFF"
    c_card_bg = "#F8FAFC"
    c_card_border = "#E2E8F0"
    c_text_dark = "#0F172A"
    c_text_main = "#1E293B"
    c_text_muted = "#475569"
    c_text_sub = "#64748B"
    
    # Species colors
    c_vtub = "#E69F00"        # Warm Amber / Orange (Resurrection)
    c_vtub_dark = "#B45309"   # Dark Amber
    c_vtub_light = "#FEF3C7"  # Soft Amber Tint
    
    c_vper = "#009E73"        # Bluish Green / Emerald (Evergreen)
    c_vper_dark = "#065F46"   # Dark Emerald
    c_vper_light = "#D1FAE5"  # Soft Green Tint
    
    c_xvis = "#CC79A7"        # Reddish Purple / Orchid (African Outgroup)
    c_abra = "#4E79A7"        # Slate Blue (Basal Scree Alpine Sister)
    c_outgroup = "#64748B"    # Slate Grey (Ptec, Dala, Ath)
    
    # Evolutionary Dynamics
    c_gain = "#009E73"        # Expansion Green
    c_loss = "#D55E00"        # Contraction Vermilion
    c_sig_star = "#D97706"    # Gold Star for significance
    
    # Tree geometry
    tree_line_color = "#334155"
    tree_line_width = 2.5
    
    svg = []
    svg.append('<?xml version="1.0" encoding="UTF-8"?>')
    svg.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" width="1200" height="900" preserveAspectRatio="xMidYMid meet">')
    
    # -------------------------------------------------------------
    # 2. Defs: Gradients, Filters, Markers
    # -------------------------------------------------------------
    svg.append('  <defs>')
    svg.append('    <style type="text/css">')
    svg.append('      text { font-family: "Arial", "Helvetica", "DejaVu Sans", sans-serif; }')
    svg.append('      .subpanel-badge { font-size: 15px; font-weight: bold; fill: #FFFFFF; }')
    svg.append('      .panel-title { font-size: 14px; font-weight: bold; fill: #0F172A; }')
    svg.append('      .panel-subtitle { font-size: 10px; font-weight: normal; fill: #475569; }')
    svg.append('      .species-name { font-size: 11px; font-style: italic; font-weight: bold; fill: #1E293B; }')
    svg.append('      .species-desc { font-size: 9px; font-style: normal; font-weight: normal; fill: #64748B; }')
    svg.append('      .badge-text-gain { font-size: 9px; font-weight: bold; fill: #065F46; }')
    svg.append('      .badge-text-loss { font-size: 9px; font-weight: bold; fill: #991B1B; }')
    svg.append('      .axis-label { font-size: 9px; fill: #64748B; font-weight: 500; }')
    svg.append('      .bar-label { font-size: 9.5px; fill: #1E293B; font-weight: 600; }')
    svg.append('      .bar-sublabel { font-size: 8.5px; fill: #64748B; font-style: italic; }')
    svg.append('      .bar-val { font-size: 9px; font-weight: bold; fill: #0F172A; }')
    svg.append('      .table-header { font-size: 9.5px; font-weight: bold; fill: #334155; }')
    svg.append('      .table-cell { font-size: 9px; fill: #1E293B; }')
    svg.append('      .table-cell-bold { font-size: 9px; font-weight: bold; fill: #0F172A; }')
    svg.append('    </style>')
    
    # Drop shadow filter
    svg.append('    <filter id="card-shadow" x="-5%" y="-5%" width="110%" height="110%" filterUnits="userSpaceOnUse">')
    svg.append('      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.05"/>')
    svg.append('    </filter>')
    svg.append('    <filter id="pill-shadow" x="-10%" y="-10%" width="120%" height="120%">')
    svg.append('      <feDropShadow dx="0" dy="1" stdDeviation="1" flood-color="#000000" flood-opacity="0.08"/>')
    svg.append('    </filter>')
    
    # Gradients for functional bars
    svg.append(f'    <linearGradient id="grad-vtub" x1="0" y1="0" x2="1" y2="0">')
    svg.append(f'      <stop offset="0%" stop-color="{c_vtub}"/>')
    svg.append(f'      <stop offset="100%" stop-color="#F59E0B"/>')
    svg.append('    </linearGradient>')
    svg.append(f'    <linearGradient id="grad-vper" x1="0" y1="0" x2="1" y2="0">')
    svg.append(f'      <stop offset="0%" stop-color="{c_vper}"/>')
    svg.append(f'      <stop offset="100%" stop-color="#10B981"/>')
    svg.append('    </linearGradient>')
    svg.append(f'    <linearGradient id="grad-gold-card" x1="0" y1="0" x2="1" y2="1">')
    svg.append(f'      <stop offset="0%" stop-color="#FFFBEB"/>')
    svg.append(f'      <stop offset="100%" stop-color="#FEF3C7"/>')
    svg.append('    </linearGradient>')
    
    svg.append('  </defs>')
    
    # -------------------------------------------------------------
    # 3. Canvas Background Layer
    # -------------------------------------------------------------
    svg.append('  <!-- Global Background -->')
    svg.append(f'  <rect width="100%" height="100%" fill="{c_bg}"/>')
    
    # -------------------------------------------------------------
    # 4. Header: Figure Title and Metadata Banner
    # -------------------------------------------------------------
    svg.append('  <!-- Figure Header -->')
    svg.append('  <g id="figure_header" transform="translate(30, 20)">')
    svg.append(f'    <text x="0" y="16" font-size="16px" font-weight="bold" fill="{c_text_dark}">Figure 3 | Stochastic Gene Family Turnover &amp; Asymmetric Adaptive Expansions (CAFE5)</text>')
    svg.append(f'    <text x="0" y="32" font-size="10.5px" fill="{c_text_muted}">Evolutionary birth-and-death dynamics (λ = 0.0036, Gamma model) reveal massive surveillance/turnover burden in evergreen vs. streamlined plastid protection in resurrection lineage</text>')
    svg.append('  </g>')
    
    # -------------------------------------------------------------
    # 5. Panel A: Dated Chronogram with CAFE5 Branch Badges
    #    Bounds: X: 30 to 585, Y: 60 to 605
    # -------------------------------------------------------------
    svg.append('  <!-- Panel A: Phylogenetic Tree & Turnover Dynamics -->')
    svg.append('  <g id="panel_a" transform="translate(30, 60)">')
    
    # Panel A Card Frame
    svg.append(f'    <rect width="555" height="545" rx="8" fill="{c_card_bg}" stroke="{c_card_border}" stroke-width="1" filter="url(#card-shadow)"/>')
    
    # Subpanel A Badge & Title
    svg.append('    <g id="panel_a_header" transform="translate(14, 14)">')
    svg.append(f'      <circle cx="12" cy="12" r="12" fill="#0F172A"/>')
    svg.append('      <text x="12" y="12" class="subpanel-badge" text-anchor="middle" dominant-baseline="central">A</text>')
    svg.append('      <text x="32" y="10" class="panel-title">Dated Chronogram &amp; Branch-Specific Gene Family Turnover</text>')
    svg.append('      <text x="32" y="23" class="panel-subtitle">CAFE5 2-category Gamma model (λ = 0.0036 dup/loss/gene/Myr, -ln L = 107,721.35, 196 significant families)</text>')
    svg.append('    </g>')
    
    # Timescale formula: X(age) = 370 - (age * 2.2207)
    def age_to_x(age):
        return 370.0 - (age * 2.2207)
    
    x_root = age_to_x(138.48)  # 62.5
    x_n9   = age_to_x(121.90)  # 99.3
    x_n10  = age_to_x(101.26)  # 145.1
    x_n8   = age_to_x(78.21)   # 196.3 (Crown Velloziaceae / Node 8 in CAFE5)
    x_n9c  = age_to_x(31.92)   # 299.1 (Core Velloziaceae / Node 9 in CAFE5)
    x_n10c = age_to_x(9.74)    # 348.4 (Vellozia MRCA / Node 10 in CAFE5)
    x_tips = 370.0
    
    # Y coordinates for 7 tips
    y_ath  = 90
    y_dala = 148
    y_ptec = 206
    y_abra = 264
    y_xvis = 322
    y_vper = 380
    y_vtub = 438
    
    # Internal node Y coordinates
    y_node10 = (y_vper + y_vtub) / 2.0   # 409.0
    y_node9  = (y_xvis + y_node10) / 2.0  # 365.5
    y_node8  = (y_abra + y_node9) / 2.0   # 314.75
    y_t_n10  = (y_ptec + y_node8) / 2.0   # 260.375
    y_t_n9   = (y_dala + y_t_n10) / 2.0   # 204.1875
    y_root   = (y_ath + y_t_n9) / 2.0     # 147.09
    
    # --- Geological Timescale Grid at Bottom of Panel A ---
    svg.append('    <g id="panel_a_timescale" transform="translate(0, 485)">')
    
    x_k_start = age_to_x(145)
    x_pg_start = age_to_x(66)
    x_ng_start = age_to_x(23)
    x_q_start = age_to_x(2.6)
    x_pres = 370.0
    
    # Period boxes
    svg.append(f'      <rect x="{x_k_start:.1f}" y="0" width="{x_pg_start - x_k_start:.1f}" height="18" fill="#F1F8E9" stroke="#DCEDC8" stroke-width="0.8"/>')
    svg.append(f'      <text x="{(x_k_start + x_pg_start)/2:.1f}" y="12" font-size="8px" font-weight="bold" fill="#33691E" text-anchor="middle">Cretaceous (145–66 Ma)</text>')
    
    svg.append(f'      <rect x="{x_pg_start:.1f}" y="0" width="{x_ng_start - x_pg_start:.1f}" height="18" fill="#FFF8E1" stroke="#FFECB3" stroke-width="0.8"/>')
    svg.append(f'      <text x="{(x_pg_start + x_ng_start)/2:.1f}" y="12" font-size="8px" font-weight="bold" fill="#F57F17" text-anchor="middle">Paleogene</text>')
    
    svg.append(f'      <rect x="{x_ng_start:.1f}" y="0" width="{x_q_start - x_ng_start:.1f}" height="18" fill="#E0F2F1" stroke="#B2DFDB" stroke-width="0.8"/>')
    svg.append(f'      <text x="{(x_ng_start + x_q_start)/2:.1f}" y="12" font-size="7.5px" font-weight="bold" fill="#004D40" text-anchor="middle">Neog.</text>')
    
    svg.append(f'      <rect x="{x_q_start:.1f}" y="0" width="{x_pres - x_q_start:.1f}" height="18" fill="#EDE7F6" stroke="#D1C4E9" stroke-width="0.8"/>')
    
    # Timescale Axis Line & Ticks
    svg.append(f'      <line x1="{x_k_start:.1f}" y1="24" x2="{x_pres:.1f}" y2="24" stroke="#64748B" stroke-width="1.2"/>')
    for tick_age in [140, 120, 100, 80, 60, 40, 20, 0]:
        tx = age_to_x(tick_age)
        svg.append(f'      <line x1="{tx:.1f}" y1="24" x2="{tx:.1f}" y2="28" stroke="#64748B" stroke-width="1"/>')
        svg.append(f'      <text x="{tx:.1f}" y="38" class="axis-label" text-anchor="middle">{tick_age}</text>')
        # Vertical gridline up into tree area
        svg.append(f'      <line x1="{tx:.1f}" y1="-420" x2="{tx:.1f}" y2="0" stroke="#E2E8F0" stroke-width="0.8" stroke-dasharray="3,3"/>')
        
    svg.append(f'      <text x="{(x_k_start + x_pres)/2:.1f}" y="50" font-size="9px" font-weight="bold" fill="#475569" text-anchor="middle">Divergence Time (Million Years Ago, Ma)</text>')
    svg.append('    </g>')
    
    # --- Tree Branches Drawing ---
    svg.append('    <g id="tree_branches">')
    
    def draw_clade(x_parent, y_parent, x_child, y_child):
        return f'<path d="M {x_parent:.1f} {y_parent:.1f} V {y_child:.1f} H {x_child:.1f}" fill="none" stroke="{tree_line_color}" stroke-width="{tree_line_width}" stroke-linejoin="round" stroke-linecap="round"/>'
    
    # Root stem
    svg.append(f'      <line x1="{x_root - 18:.1f}" y1="{y_root:.1f}" x2="{x_root:.1f}" y2="{y_root:.1f}" stroke="{tree_line_color}" stroke-width="{tree_line_width}" stroke-linecap="round"/>')
    
    # Root splits to Ath and t_n9
    svg.append(f'      {draw_clade(x_root, y_root, x_tips, y_ath)}')
    svg.append(f'      {draw_clade(x_root, y_root, x_n9, y_t_n9)}')
    
    # t_n9 splits to Dala and t_n10
    svg.append(f'      {draw_clade(x_n9, y_t_n9, x_tips, y_dala)}')
    svg.append(f'      {draw_clade(x_n9, y_t_n9, x_n10, y_t_n10)}')
    
    # t_n10 splits to Ptec and Node 8 (Abra split)
    svg.append(f'      {draw_clade(x_n10, y_t_n10, x_tips, y_ptec)}')
    svg.append(f'      {draw_clade(x_n10, y_t_n10, x_n8, y_node8)}')
    
    # Node 8 splits to Abra and Node 9 (Xvis split)
    svg.append(f'      {draw_clade(x_n8, y_node8, x_tips, y_abra)}')
    svg.append(f'      {draw_clade(x_n8, y_node8, x_n9c, y_node9)}')
    
    # Node 9 splits to Xvis and Node 10 (Vper/Vtub split)
    svg.append(f'      {draw_clade(x_n9c, y_node9, x_tips, y_xvis)}')
    svg.append(f'      {draw_clade(x_n9c, y_node9, x_n10c, y_node10)}')
    
    # Node 10 splits to Vper and Vtub
    svg.append(f'      {draw_clade(x_n10c, y_node10, x_tips, y_vper)}')
    svg.append(f'      {draw_clade(x_n10c, y_node10, x_tips, y_vtub)}')
    
    svg.append('    </g>')
    
    # --- Branch Gain/Loss Pill Badges ---
    def draw_badge(x, y, gain, loss, is_sig=False):
        gain_str = f"+{gain}"
        loss_str = f"-{loss}"
        w_pill = 68
        h_pill = 16
        b_x = x - w_pill / 2
        b_y = y - h_pill / 2
        
        sig_border = f'stroke="{c_sig_star}" stroke-width="1.4"' if is_sig else 'stroke="#CBD5E1" stroke-width="0.8"'
        badge_svg = [
            f'      <g transform="translate({b_x:.1f}, {b_y:.1f})" filter="url(#pill-shadow)">',
            f'        <rect width="{w_pill}" height="{h_pill}" rx="8" fill="#FFFFFF" {sig_border}/>',
            f'        <line x1="{w_pill/2}" y1="2" x2="{w_pill/2}" y2="{h_pill-2}" stroke="#E2E8F0" stroke-width="0.8"/>',
            f'        <text x="{w_pill/4:.1f}" y="{h_pill/2:.1f}" class="badge-text-gain" text-anchor="middle" dominant-baseline="central">{gain_str}</text>',
            f'        <text x="{3*w_pill/4:.1f}" y="{h_pill/2:.1f}" class="badge-text-loss" text-anchor="middle" dominant-baseline="central">{loss_str}</text>'
        ]
        badge_svg.append('      </g>')
        return "\n".join(badge_svg)
    
    svg.append('    <g id="branch_badges">')
    svg.append(draw_badge(260, y_ath - 8, 1917, 2117))
    svg.append(draw_badge(280, y_ptec - 8, 2219, 346))
    svg.append(draw_badge(x_n8 + 36, y_node8 + 10, 386, 469))
    svg.append(draw_badge(285, y_abra - 8, 1750, 1578))
    svg.append(draw_badge(x_n9c + 18, y_node9 - 14, 117, 19, is_sig=True))
    svg.append(draw_badge(335, y_xvis - 8, 1201, 1084))
    svg.append(draw_badge(x_n10c - 4, y_node10 + 13, 293, 329))
    svg.append(draw_badge(x_n10c + 20, y_vper - 8, 86, 64, is_sig=True))
    svg.append(draw_badge(x_n10c + 20, y_vtub - 8, 56, 80, is_sig=True))
    svg.append('    </g>')
    
    # --- Node Callout Badges (Node 9 & Vellozia Sister Comparison) ---
    svg.append('    <g id="node_callout_annotations">')
    svg.append(f'      <g transform="translate(195, 328)">')
    svg.append(f'        <rect x="0" y="0" width="138" height="28" rx="4" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1"/>')
    svg.append(f'        <text x="6" y="10" font-size="8px" font-weight="bold" fill="#92400E">★ Node &lt;9&gt; (Core Velloziaceae)</text>')
    svg.append(f'        <text x="6" y="21" font-size="7.5px" fill="#B45309">117 sig. expansions (Stringent Core)</text>')
    svg.append('      </g>')
    svg.append(f'      <path d="M 300 328 L {x_n9c:.1f} {y_node9:.1f}" stroke="#F59E0B" stroke-width="1" stroke-dasharray="2,2"/>')
    svg.append('    </g>')
    
    # --- Species Tip Labels & Habit Badges ---
    svg.append('    <g id="species_tip_labels" transform="translate(378, 0)">')
    
    tips_info = [
        (y_ath, "Arabidopsis thaliana", "Eudicot Model Outgroup", c_outgroup, None),
        (y_dala, "Dioscorea alata", "Basal Monocot Outgroup", c_outgroup, None),
        (y_ptec, "Pandanus tectorius", "Pandanaceae Sister Family", c_outgroup, None),
        (y_abra, "Acanthochlamys bracteata", "Basal Scree Alpine Sister", c_abra, "Alpine Scree"),
        (y_xvis, "Xerophyta viscosa", "African Resurrection Outgroup", c_xvis, "Resurrection"),
        (y_vper, "Vellozia peripherica", "Montane Evergreen Specialist", c_vper, "Evergreen"),
        (y_vtub, "Vellozia tubiflora", "Poikilochlorophyllous Resurrection", c_vtub, "Resurrection")
    ]
    
    for y_pos, sp_name, sp_desc, sp_color, habit in tips_info:
        svg.append(f'      <circle cx="-8" cy="{y_pos}" r="3.5" fill="{sp_color}" stroke="#FFFFFF" stroke-width="1"/>')
        svg.append(f'      <text x="0" y="{y_pos - 2}" class="species-name" fill="{c_text_dark}">{sp_name}</text>')
        svg.append(f'      <text x="0" y="{y_pos + 10}" class="species-desc">{sp_desc}</text>')
        
        if habit == "Evergreen":
            svg.append(f'      <rect x="138" y="{y_pos - 8}" width="32" height="14" rx="3" fill="{c_vper_light}" stroke="{c_vper}" stroke-width="0.8"/>')
            svg.append(f'      <text x="154" y="{y_pos - 1}" font-size="7px" font-weight="bold" fill="{c_vper_dark}" text-anchor="middle" dominant-baseline="central">EVG</text>')
        elif habit == "Resurrection":
            svg.append(f'      <rect x="138" y="{y_pos - 8}" width="32" height="14" rx="3" fill="{c_vtub_light}" stroke="{c_vtub}" stroke-width="0.8"/>')
            svg.append(f'      <text x="154" y="{y_pos - 1}" font-size="7px" font-weight="bold" fill="{c_vtub_dark}" text-anchor="middle" dominant-baseline="central">RES</text>')
        elif habit == "Alpine Scree":
            svg.append(f'      <rect x="138" y="{y_pos - 8}" width="32" height="14" rx="3" fill="#EDE7F6" stroke="{c_abra}" stroke-width="0.8"/>')
            svg.append(f'      <text x="154" y="{y_pos - 1}" font-size="7px" font-weight="bold" fill="#4A148C" text-anchor="middle" dominant-baseline="central">ALP</text>')
            
    svg.append('    </g>')
    
    # --- Model Legend / Parameter Summary Card (Bottom-Left of Panel A) ---
    svg.append('    <g id="model_summary_card" transform="translate(14, 442)">')
    svg.append(f'      <rect width="185" height="34" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.8"/>')
    svg.append(f'      <text x="8" y="11" font-size="7.8px" font-weight="bold" fill="#1E293B">CAFE v5.1.0 Model Summary</text>')
    svg.append(f'      <text x="8" y="21" font-size="7.2px" fill="#475569">λ = 0.0036 dup/loss/gene/Myr (Gamma k=2)</text>')
    svg.append(f'      <text x="8" y="30" font-size="7.2px" fill="#475569">-ln L = 107,721.35 (Stringent Core)</text>')
    svg.append('    </g>')
    
    svg.append('  </g>')  # End Panel A
    
    # -------------------------------------------------------------
    # 6. Panel B: Comparative Functional Category Expansions
    #    Bounds: X: 615 to 1170, Y: 60 to 605
    # -------------------------------------------------------------
    svg.append('  <!-- Panel B: Comparative Functional Category Expansions -->')
    svg.append('  <g id="panel_b" transform="translate(615, 60)">')
    
    # Panel B Card Frame
    svg.append(f'    <rect width="555" height="545" rx="8" fill="{c_card_bg}" stroke="{c_card_border}" stroke-width="1" filter="url(#card-shadow)"/>')
    
    # Subpanel B Badge & Title
    svg.append('    <g id="panel_b_header" transform="translate(14, 14)">')
    svg.append(f'      <circle cx="12" cy="12" r="12" fill="#0F172A"/>')
    svg.append('      <text x="12" y="12" class="subpanel-badge" text-anchor="middle" dominant-baseline="central">B</text>')
    svg.append('      <text x="32" y="10" class="panel-title">Comparative Functional Category Expansions (Lineage-Specific)</text>')
    svg.append('      <text x="32" y="23" class="panel-subtitle">Contrasting adaptive investments: Plastid repair &amp; dormancy vs. Foliar surveillance &amp; proteasome turnover</text>')
    svg.append('    </g>')
    
    # Sub-section B1: Vellozia tubiflora Expansions (Resurrection Specialist)
    svg.append('    <g id="panel_b_vtub" transform="translate(14, 45)">')
    svg.append(f'      <rect width="527" height="235" rx="6" fill="#FFFFFF" stroke="#FDE68A" stroke-width="1"/>')
    
    # Subtitle Header Bar
    svg.append(f'      <rect width="527" height="24" rx="6" fill="{c_vtub_light}"/>')
    svg.append(f'      <circle cx="14" cy="12" r="5" fill="{c_vtub}"/>')
    svg.append(f'      <text x="26" y="15" font-size="11px" font-weight="bold" fill="{c_vtub_dark}">Vellozia tubiflora — Poikilochlorophyllous Resurrection Specialist (56 stringent expansions)</text>')
    
    vtub_categories = [
        ("TOC/TIC Plastid Protein Translocons", "OG0000016 (+55), OG0000087 (+22) [TOC75, TOC159, TIC110]", 77, "+77 genes"),
        ("Chloroplastic NDH Complex &amp; Redox Shuttles", "OG0000036 (+29), OG0000048 (+24), OG0000062 (+18)", 71, "+71 genes"),
        ("PSII Core Reaction Center &amp; Stabilizers", "OG0000069 (+18), OG0000010 (+43), OG0000019 (+20)", 43, "+43 genes"),
        ("Plastid Group II Intron Maturase &amp; Splicing", "OG0000044 (+23) [trnK maturase, organellar RNA processing]", 23, "+23 genes"),
        ("LEA Proteins &amp; Seed-Maturation Cascades", "Late Embryogenesis Abundant cascades &amp; cytoplasmic vitrification", 18, "+18 genes"),
        ("DnaJ / Hsp40 Chaperones &amp; Vitrification", "Co-chaperones stabilizing protein glasses during desiccation", 15, "+15 genes")
    ]
    
    y_bar = 35
    for title, subtitle, count, count_str in vtub_categories:
        bar_w = min(count * 2.5, 205)
        svg.append(f'      <g transform="translate(10, {y_bar})">')
        svg.append(f'        <text x="0" y="9" class="bar-label">{title}</text>')
        svg.append(f'        <text x="0" y="20" class="bar-sublabel">{subtitle}</text>')
        # Bar track & fill
        svg.append(f'        <rect x="260" y="2" width="205" height="15" rx="3" fill="#F1F5F9"/>')
        svg.append(f'        <rect x="260" y="2" width="{bar_w:.1f}" height="15" rx="3" fill="url(#grad-vtub)"/>')
        svg.append(f'        <text x="{260 + bar_w + 6:.1f}" y="13" class="bar-val" dominant-baseline="central">{count_str}</text>')
        svg.append('      </g>')
        y_bar += 32
        
    svg.append('    </g>')
    
    # Sub-section B2: Vellozia peripherica Expansions (Evergreen Specialist)
    svg.append('    <g id="panel_b_vper" transform="translate(14, 290)">')
    svg.append(f'      <rect width="527" height="240" rx="6" fill="#FFFFFF" stroke="#A7F3D0" stroke-width="1"/>')
    
    # Subtitle Header Bar
    svg.append(f'      <rect width="527" height="24" rx="6" fill="{c_vper_light}"/>')
    svg.append(f'      <circle cx="14" cy="12" r="5" fill="{c_vper}"/>')
    svg.append(f'      <text x="26" y="15" font-size="11px" font-weight="bold" fill="{c_vper_dark}">Vellozia peripherica — Montane Evergreen Specialist (86 stringent expansions)</text>')
    
    vper_categories = [
        ("LRR-RLK Receptor Kinases &amp; Turgor Monitoring", "OG0000012 (+57), OG0000021 (+29), OG0000025 (+25), OG0000060 (+22)", 150, "+150 genes"),
        ("F-box / E3 Ubiquitin Ligases (26S Proteasome)", "OG0000018/26 (+51), OG0000043 (+21) [turnover of photo-damaged proteins]", 72, "+72 genes"),
        ("NB-LRR / NLR Immune Receptors &amp; Defense", "OG0000050 (+22), OG0000049 (+17) [foliar pathogen surveillance]", 39, "+39 genes"),
        ("Cytochrome P450 Monooxygenases", "OG0000070 (+24), P450 arrays [cuticular wax &amp; UV-absorbing flavonoids]", 43, "+43 genes"),
        ("UDP-Glycosyltransferases (UGTs)", "Secondary metabolite conjugation &amp; cell wall maintenance", 25, "+25 genes"),
        ("Wall-Associated Receptor Kinases (WAKs)", "Cell wall stress sensing &amp; osmotic turgor maintenance", 16, "+16 genes")
    ]
    
    y_bar = 35
    for title, subtitle, count, count_str in vper_categories:
        bar_w = min(count * 1.35, 205)
        svg.append(f'      <g transform="translate(10, {y_bar})">')
        svg.append(f'        <text x="0" y="9" class="bar-label">{title}</text>')
        svg.append(f'        <text x="0" y="20" class="bar-sublabel">{subtitle}</text>')
        # Bar track & fill
        svg.append(f'        <rect x="260" y="2" width="205" height="15" rx="3" fill="#F1F5F9"/>')
        svg.append(f'        <rect x="260" y="2" width="{bar_w:.1f}" height="15" rx="3" fill="url(#grad-vper)"/>')
        svg.append(f'        <text x="{260 + bar_w + 6:.1f}" y="13" class="bar-val" dominant-baseline="central">{count_str}</text>')
        svg.append('      </g>')
        y_bar += 32
        
    svg.append('    </g>')
    
    svg.append('  </g>')  # End Panel B
    
    # -------------------------------------------------------------
    # 7. Panel C: Diagnostic Gene Family Trajectories & Conceptual Synthesis
    #    Bounds: X: 30 to 1170, Y: 620 to 880
    # -------------------------------------------------------------
    svg.append('  <!-- Panel C: Diagnostic Family Trajectories & The Evergreen Burden Synthesis -->')
    svg.append('  <g id="panel_c" transform="translate(30, 620)">')
    
    # Panel C Card Frame
    svg.append(f'    <rect width="1140" height="260" rx="8" fill="{c_card_bg}" stroke="{c_card_border}" stroke-width="1" filter="url(#card-shadow)"/>')
    
    # Subpanel C Badge & Title
    svg.append('    <g id="panel_c_header" transform="translate(14, 14)">')
    svg.append(f'      <circle cx="12" cy="12" r="12" fill="#0F172A"/>')
    svg.append('      <text x="12" y="12" class="subpanel-badge" text-anchor="middle" dominant-baseline="central">C</text>')
    svg.append('      <text x="32" y="10" class="panel-title">Diagnostic Adaptive Gene Family Trajectories &amp; The Macroevolutionary Synthesis</text>')
    svg.append('      <text x="32" y="23" class="panel-subtitle">Copy-number shifts from Ancestral Core Velloziaceae MRCA to extant sister species reveal contrasting evolutionary architectures</text>')
    svg.append('    </g>')
    
    # Left Sub-table: Top 6 Diagnostic Adaptive Gene Families
    # Bounds: X: 14 to 680, Y: 42 to 245
    svg.append('    <g id="diagnostic_trajectories_table" transform="translate(14, 42)">')
    svg.append(f'      <rect width="666" height="205" rx="6" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>')
    
    # Table Header
    svg.append(f'      <rect width="666" height="24" rx="6" fill="#F1F5F9"/>')
    svg.append('      <text x="12" y="16" class="table-header">Orthogroup &amp; Functional Description</text>')
    svg.append('      <text x="314" y="16" class="table-header" text-anchor="middle">Ancestral &lt;10&gt;</text>')
    svg.append(f'      <text x="427" y="16" class="table-header" fill="{c_vtub_dark}" text-anchor="middle">V. tubiflora (Resurrection)</text>')
    svg.append(f'      <text x="562" y="16" class="table-header" fill="{c_vper_dark}" text-anchor="middle">V. peripherica (Evergreen)</text>')
    
    # Trajectory Rows
    trajectories = [
        ("OG0000016", "Plastid Protein Import Translocon (TOC75/159)", 6, 61, "+55", 3, "-3", "Resurrection Specific"),
        ("OG0000036", "Chloroplastic NDH Plastoquinone Complex", 7, 36, "+29", 6, "-1", "Resurrection Specific"),
        ("OG0000069", "PSII Core Reaction Center &amp; Stabilizers", 6, 24, "+18", 5, "-1", "Resurrection Specific"),
        ("OG0000012", "LRR-RLK Receptor Kinase (Turgor Sensor)", 8, 13, "+5", 65, "+57", "Evergreen Specific"),
        ("OG0000018", "F-box Ubiquitin Ligase (26S Proteasome)", 5, 7, "+2", 56, "+51", "Evergreen Specific"),
        ("OG0000050", "NB-LRR Foliar Disease Resistance Sentinel", 7, 6, "-1", 29, "+22", "Evergreen Specific")
    ]
    
    y_row = 30
    for og, desc, anc_count, vtub_c, vtub_delta, vper_c, vper_delta, spec_type in trajectories:
        row_bg = "#FAFAFA" if (trajectories.index((og, desc, anc_count, vtub_c, vtub_delta, vper_c, vper_delta, spec_type)) % 2 == 1) else "#FFFFFF"
        svg.append(f'      <rect x="0" y="{y_row - 4}" width="666" height="28" fill="{row_bg}"/>')
        
        # OG & Description
        svg.append(f'      <text x="12" y="{y_row + 8}" class="table-cell-bold">{og}: <tspan font-weight="normal" fill="#475569">{desc}</tspan></text>')
        
        # Ancestral Copy
        svg.append(f'      <rect x="300" y="{y_row - 1}" width="28" height="18" rx="3" fill="#E2E8F0"/>')
        svg.append(f'      <text x="314" y="{y_row + 12}" font-size="9px" font-weight="bold" fill="#334155" text-anchor="middle">{anc_count}</text>')
        
        # Arrow 1
        svg.append(f'      <text x="350" y="{y_row + 11}" font-size="10px" fill="#94A3B8" text-anchor="middle">→</text>')
        
        # Vtub Copy & Delta Badge
        vtub_bg = c_vtub_light if "+" in vtub_delta else "#F1F5F9"
        vtub_fg = c_vtub_dark if "+" in vtub_delta else "#64748B"
        svg.append(f'      <rect x="390" y="{y_row - 1}" width="75" height="18" rx="3" fill="{vtub_bg}" stroke="{vtub_fg}" stroke-width="0.7"/>')
        svg.append(f'      <text x="427" y="{y_row + 12}" font-size="8.5px" font-weight="bold" fill="{vtub_fg}" text-anchor="middle">{vtub_c} ({vtub_delta})</text>')
        
        # Vper Copy & Delta Badge
        vper_bg = c_vper_light if "+" in vper_delta else "#F1F5F9"
        vper_fg = c_vper_dark if "+" in vper_delta else "#64748B"
        svg.append(f'      <rect x="525" y="{y_row - 1}" width="75" height="18" rx="3" fill="{vper_bg}" stroke="{vper_fg}" stroke-width="0.7"/>')
        svg.append(f'      <text x="562" y="{y_row + 12}" font-size="8.5px" font-weight="bold" fill="{vper_fg}" text-anchor="middle">{vper_c} ({vper_delta})</text>')
        
        y_row += 29
        
    svg.append('    </g>')
    
    # Right Synthesis Card: "The Genomic Burden of Being Evergreen"
    # Bounds: X: 695 to 1125, Y: 42 to 245
    svg.append('    <g id="synthesis_card" transform="translate(695, 42)">')
    svg.append(f'      <rect width="430" height="205" rx="6" fill="url(#grad-gold-card)" stroke="#F59E0B" stroke-width="1.2"/>')
    
    # Synthesis Title
    svg.append('      <g transform="translate(16, 16)">')
    svg.append(f'        <circle cx="10" cy="10" r="10" fill="#D97706"/>')
    svg.append('        <text x="10" y="10" font-size="12px" fill="#FFFFFF" text-anchor="middle" dominant-baseline="central">★</text>')
    svg.append(f'        <text x="28" y="11" font-size="12px" font-weight="bold" fill="#92400E" dominant-baseline="central">Macroevolutionary Synthesis &amp; Trade-offs</text>')
    svg.append('      </g>')
    
    # Synthesis Narrative Bullets
    bullets = [
        ("The Genomic Burden of Being Evergreen:", "V. peripherica underwent 86 stringent family expansions (plus 22 rate-sensitive expansions), demonstrating a substantially higher expansion profile than V. tubiflora (56 stringent, 11 rate-sensitive)."),
        ("Sustaining Hydrated Foliage in Extremes:", "Year-round photosynthesis under high UV and vapor pressure deficit demands continuous protein quality control (F-box ligases +51), cell wall turgor sensing (LRR-RLKs +57), and constant pathogen defense (NB-LRRs +22)."),
        ("Streamlined Poikilochlorophylly:", "V. tubiflora avoids foliar maintenance costs by dismantling thylakoids into dormant desiccoplasts, investing selectively in plastid import (TOC/TIC +55) and NDH redox buffering (+29) for rapid rehydration.")
    ]
    
    y_b = 48
    for b_title, b_text in bullets:
        svg.append(f'      <g transform="translate(16, {y_b})">')
        svg.append(f'        <circle cx="4" cy="5" r="2.5" fill="#D97706"/>')
        svg.append(f'        <text x="12" y="6" font-size="9px" font-weight="bold" fill="#78350F">{b_title}</text>')
        # Multi-line text for narrative
        words = b_text.split()
        lines = []
        cur_line = []
        for w in words:
            cur_line.append(w)
            if len(" ".join(cur_line)) > 60:
                lines.append(" ".join(cur_line))
                cur_line = []
        if cur_line:
            lines.append(" ".join(cur_line))
        
        for i, l in enumerate(lines):
            svg.append(f'        <text x="12" y="{17 + i*11}" font-size="8.3px" fill="#92400E">{l}</text>')
        svg.append('      </g>')
        y_b += 48
        
    svg.append('    </g>')
    
    svg.append('  </g>')  # End Panel C
    
    # -------------------------------------------------------------
    # 8. Closing Tag
    # -------------------------------------------------------------
    svg.append('</svg>')
    
    content = "\n".join(svg)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully generated Figure 3 SVG at: {output_path}")

def validate_svg(svg_path: str):
    """Validates the well-formedness and structural features of the SVG."""
    print(f"Validating SVG file: {svg_path}")
    tree = ET.parse(svg_path)
    root = tree.getroot()
    
    # Check root attributes
    assert root.tag.endswith("svg"), "Root element must be <svg>"
    assert root.attrib.get("viewBox") == "0 0 1200 900", f"Unexpected viewBox: {root.attrib.get('viewBox')}"
    
    # Check semantic panels
    panel_ids = ["panel_a", "panel_b", "panel_c", "figure_header"]
    found_ids = set()
    for elem in root.iter():
        elem_id = elem.attrib.get("id")
        if elem_id:
            found_ids.add(elem_id)
            
    for pid in panel_ids:
        assert pid in found_ids, f"Missing required semantic group id: {pid}"
        
    # Check text element count and selectability
    texts = list(root.iter("{http://www.w3.org/2000/svg}text")) + list(root.iter("text"))
    print(f"Total text nodes found: {len(texts)}")
    assert len(texts) > 50, "Insufficient text annotations in SVG"
    
    print("SVG Validation PASSED successfully!")

if __name__ == "__main__":
    out_file = "/home/mfcaval/github/doutorado/teamwork/figures_chapter1/fig3_gene_family_cafe5_turnover.svg"
    if len(sys.argv) > 1:
        out_file = sys.argv[1]
    create_figure_3_svg(out_file)
    validate_svg(out_file)
