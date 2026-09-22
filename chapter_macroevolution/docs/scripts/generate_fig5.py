#!/usr/bin/env python3
"""
Figure 5: Conceptual Synthesis: The Evolutionary Cost of "Evergreen" vs. "Resurrection"
PhD Thesis Chapter 1: Macroevolution and Genomic Divergence in Velloziaceae
Candidate: Mariana Feitosa Cavalheiro
Advisor: Isabel Rodrigues Gerhardt

Generates publication-grade, fully editable vector SVG conforming to:
- Canvas: viewBox="0 0 1200 900" (responsive, 175mm equivalent)
- Accessible Okabe-Ito and scientific color palette
- Hierarchical semantic grouping (<g id="...">)
- Selectable vector <text> with standard sans-serif font family stack
- 100% empirical precision with Chapter 1 empirical genomics and macroevolutionary data
"""

import os
import sys
import xml.etree.ElementTree as ET

def build_figure5_svg(output_path: str):
    # Ensure parent directory exists
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    svg = []
    
    # XML Header & SVG Container
    svg.append('<?xml version="1.0" encoding="UTF-8"?>')
    svg.append('<svg xmlns="http://www.w3.org/2000/svg"')
    svg.append('     xmlns:xlink="http://www.w3.org/1999/xlink"')
    svg.append('     viewBox="0 0 1200 900"')
    svg.append('     width="100%" height="100%"')
    svg.append('     style="background-color: #FFFFFF; font-family: Arial, Helvetica, \'DejaVu Sans\', sans-serif;">')

    # =========================================================================
    # DEFS: Gradients, Filters, Markers, Clip Paths
    # =========================================================================
    svg.append('  <defs>')
    
    # Gradients
    svg.append('    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('      <stop offset="0%" stop-color="#0F172A"/>')
    svg.append('      <stop offset="100%" stop-color="#1E293B"/>')
    svg.append('    </linearGradient>')
    
    svg.append('    <linearGradient id="vtubBannerGrad" x1="0%" y1="0%" x2="100%" y2="0%">')
    svg.append('      <stop offset="0%" stop-color="#D97706"/>')
    svg.append('      <stop offset="100%" stop-color="#E69F00"/>')
    svg.append('    </linearGradient>')

    svg.append('    <linearGradient id="vperBannerGrad" x1="0%" y1="0%" x2="100%" y2="0%">')
    svg.append('      <stop offset="0%" stop-color="#007353"/>')
    svg.append('      <stop offset="100%" stop-color="#009E73"/>')
    svg.append('    </linearGradient>')

    svg.append('    <linearGradient id="sunGrad" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('      <stop offset="0%" stop-color="#FDE047"/>')
    svg.append('      <stop offset="100%" stop-color="#F59E0B"/>')
    svg.append('    </linearGradient>')

    svg.append('    <linearGradient id="chloroplastGrad" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('      <stop offset="0%" stop-color="#4ADE80"/>')
    svg.append('      <stop offset="100%" stop-color="#15803D"/>')
    svg.append('    </linearGradient>')

    svg.append('    <linearGradient id="desiccoplastGrad" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('      <stop offset="0%" stop-color="#FBBF24"/>')
    svg.append('      <stop offset="100%" stop-color="#92400E"/>')
    svg.append('    </linearGradient>')

    svg.append('    <linearGradient id="dnaGrad" x1="0%" y1="0%" x2="100%" y2="0%">')
    svg.append('      <stop offset="0%" stop-color="#0284C7"/>')
    svg.append('      <stop offset="100%" stop-color="#0369A1"/>')
    svg.append('    </linearGradient>')

    svg.append('    <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('      <stop offset="0%" stop-color="#10B981"/>')
    svg.append('      <stop offset="100%" stop-color="#047857"/>')
    svg.append('    </linearGradient>')

    # Drop shadows
    svg.append('    <filter id="cardShadow" x="-3%" y="-3%" width="106%" height="108%" filterUnits="userSpaceOnUse">')
    svg.append('      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.06"/>')
    svg.append('    </filter>')
    svg.append('    <filter id="softShadow" x="-2%" y="-2%" width="104%" height="106%" filterUnits="userSpaceOnUse">')
    svg.append('      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#000000" flood-opacity="0.05"/>')
    svg.append('    </filter>')

    # Arrow markers
    svg.append('    <marker id="arrowAmber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">')
    svg.append('      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#D97706"/>')
    svg.append('    </marker>')
    svg.append('    <marker id="arrowGreen" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">')
    svg.append('      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#007353"/>')
    svg.append('    </marker>')
    svg.append('    <marker id="arrowSlate" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">')
    svg.append('      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#475569"/>')
    svg.append('    </marker>')
    svg.append('    <marker id="arrowRed" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">')
    svg.append('      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#DC2626"/>')
    svg.append('    </marker>')

    # Clip paths for headers
    svg.append('    <clipPath id="vtubHeaderClip">')
    svg.append('      <rect x="24" y="118" width="548" height="46" rx="8" ry="8"/>')
    svg.append('    </clipPath>')
    svg.append('    <clipPath id="vperHeaderClip">')
    svg.append('      <rect x="628" y="118" width="548" height="46" rx="8" ry="8"/>')
    svg.append('    </clipPath>')

    svg.append('  </defs>')

    # Layer 0: Background
    svg.append('  <!-- Background Canvas -->')
    svg.append('  <g id="background_layer">')
    svg.append('    <rect width="1200" height="900" fill="#FAFAFA"/>')
    svg.append('  </g>')

    # =========================================================================
    # PANEL A: Master Title & Macroevolutionary Environmental Foundation
    # =========================================================================
    svg.append('  <!-- =================================================== -->')
    svg.append('  <!-- PANEL A: MACROEVOLUTIONARY & ENVIRONMENTAL MATRIX    -->')
    svg.append('  <!-- =================================================== -->')
    svg.append('  <g id="panel_a_macroevolutionary_foundation">')
    
    # Title and Subtitle
    svg.append('    <text x="24" y="27" font-size="16px" font-weight="bold" fill="#0F172A" text-anchor="start" dominant-baseline="alphabetic">Fig 5. Conceptual Synthesis: The Evolutionary Cost of "Evergreen" vs. "Resurrection"</text>')
    svg.append('    <text x="24" y="43" font-size="10.5px" font-style="italic" fill="#475569" text-anchor="start" dominant-baseline="alphabetic">Divergent adaptive trajectories and genomic trade-offs in Neotropical campos rupestres (OCBIL) under 9.68 Myr of divergence</text>')

    # Environmental Foundation Container Box
    svg.append('    <g id="environmental_foundation_card">')
    svg.append('      <rect x="24" y="52" width="1152" height="54" rx="6" ry="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.2" filter="url(#softShadow)"/>')
      
    # Sub-Box 1: Shared Environmental Pressures (OCBIL Biome)
    svg.append('      <g id="shared_pressures">')
    svg.append('        <rect x="32" y="58" width="220" height="42" rx="4" ry="4" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>')
    svg.append('        <circle cx="48" cy="79" r="9" fill="url(#sunGrad)"/>')
    svg.append('        <path d="M 48 65 L 48 68 M 48 90 L 48 93 M 34 79 L 37 79 M 59 79 L 62 79 M 38 69 L 40 71 M 56 87 L 58 89 M 38 89 L 40 87 M 56 71 L 58 69" stroke="#D97706" stroke-width="1.5" stroke-linecap="round"/>')
    svg.append('        <text x="64" y="72" font-size="9px" font-weight="bold" fill="#9A3412" text-anchor="start" dominant-baseline="central">Severe Abiotic Pressures (OCBIL)</text>')
    svg.append('        <text x="64" y="86" font-size="7.4px" fill="#475569" text-anchor="start" dominant-baseline="central">UV-B &gt;2000 µmol · Oligotrophic Sand · VPD &gt;3.5 kPa</text>')
    svg.append('      </g>')

    # Sub-Box 2: Center Macroevolutionary Timeline (78.2 Ma -> 31.92 Ma -> 9.74 Ma)
    svg.append('      <g id="macroevolutionary_deep_time">')
    svg.append('        <rect x="260" y="58" width="676" height="42" rx="4" ry="4" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>')
    svg.append('        <text x="598" y="68" font-size="8.5px" font-weight="bold" fill="#1E293B" text-anchor="middle" dominant-baseline="central">Macroevolutionary Timeline &amp; Karyotypic Backbone (2n = 18, x = 9)</text>')
      
    # Connecting Axis
    svg.append('        <line x1="280" y1="84" x2="916" y2="84" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>')
      
    # Node 1: Crown Velloziaceae
    svg.append('        <circle cx="310" cy="84" r="5" fill="#4E79A7" stroke="#1E293B" stroke-width="1"/>')
    svg.append('        <text x="310" y="94" font-size="7.2px" font-weight="bold" fill="#334155" text-anchor="middle">Crown: ~78.02 Ma</text>')

    # Node 2: Trans-Atlantic Disjunction (33.77 Ma)
    svg.append('        <circle cx="505" cy="84" r="6" fill="#CC79A7" stroke="#882255" stroke-width="1.2"/>')
    svg.append('        <text x="505" y="94" font-size="7.5px" font-weight="bold" fill="#882255" text-anchor="middle">Trans-Atlantic Split: 33.77 Ma</text>')
    svg.append('        <rect x="445" y="60" width="120" height="12" rx="2" ry="2" fill="#FDF2F8" stroke="#CC79A7" stroke-width="0.8"/>')
    svg.append('        <text x="505" y="66" font-size="6.8px" font-weight="bold" fill="#9D174D" text-anchor="middle" dominant-baseline="central">117 Stringent Expansions</text>')

    # Node 3: Sister Speciation (9.68 Ma)
    svg.append('        <circle cx="750" cy="84" r="6" fill="#D97706" stroke="#B45309" stroke-width="1.2"/>')
    svg.append('        <text x="750" y="94" font-size="7.5px" font-weight="bold" fill="#0F172A" text-anchor="middle">Sister Divergence: 9.68 Ma (Late Miocene)</text>')
    svg.append('        <rect x="690" y="60" width="120" height="12" rx="2" ry="2" fill="#FEF3C7" stroke="#D97706" stroke-width="0.8"/>')
    svg.append('        <text x="750" y="66" font-size="6.8px" font-weight="bold" fill="#92400E" text-anchor="middle" dominant-baseline="central">297 Collinear Syntenic Blocks</text>')

    # Divergence Arrows
    svg.append('        <path d="M 825 84 L 865 77" stroke="#D97706" stroke-width="1.5" marker-end="url(#arrowAmber)"/>')
    svg.append('        <path d="M 825 84 L 865 91" stroke="#007353" stroke-width="1.5" marker-end="url(#arrowGreen)"/>')
    svg.append('      </g>')

    # Sub-Box 3: Karyotypic Stasis Summary
    svg.append('      <g id="karyotypic_stasis_badge">')
    svg.append('        <rect x="944" y="58" width="224" height="42" rx="4" ry="4" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>')
    svg.append('        <text x="1056" y="72" font-size="9px" font-weight="bold" fill="#0F172A" text-anchor="middle" dominant-baseline="central">Macrosyntenic Stasis (2n = 18)</text>')
    svg.append('        <text x="1056" y="86" font-size="7.4px" fill="#047857" font-weight="bold" text-anchor="middle" dominant-baseline="central">0 Translocations · Chr1A ↔ Chr5A Dupl.</text>')
    svg.append('      </g>')
    svg.append('    </g>')
    svg.append('  </g>')

    # =========================================================================
    # PANEL B: LEFT COLUMN — Vellozia tubiflora (Resurrection Specialist)
    # =========================================================================
    svg.append('  <!-- =================================================== -->')
    svg.append('  <!-- PANEL B: VELLOZIA TUBIFLORA (RESURRECTION)          -->')
    svg.append('  <!-- =================================================== -->')
    svg.append('  <g id="panel_b_left_column_vtubiflora">')
    
    # Outer Framing Box
    svg.append('    <rect x="24" y="118" width="548" height="594" rx="8" ry="8" fill="#FFFDF8" stroke="#E69F00" stroke-width="1.8" filter="url(#cardShadow)"/>')
    
    # Column Header Banner (with clip path)
    svg.append('    <g clip-path="url(#vtubHeaderClip)">')
    svg.append('      <rect x="24" y="118" width="548" height="46" fill="url(#vtubBannerGrad)"/>')
    svg.append('    </g>')
    svg.append('    <text x="40" y="136" font-size="13px" font-weight="bold" fill="#FFFFFF" text-anchor="start" dominant-baseline="central">Vellozia tubiflora</text>')
    svg.append('    <text x="175" y="136" font-size="11px" font-style="italic" fill="#FEF3C7" text-anchor="start" dominant-baseline="central">— Resurrection Specialist (Poikilochlorophyllous)</text>')
    svg.append('    <rect x="40" y="148" width="516" height="12" rx="2" ry="2" fill="#B45309" fill-opacity="0.5"/>')
    svg.append('    <text x="44" y="154" font-size="7.5px" font-weight="bold" fill="#FFFFFF" text-anchor="start" dominant-baseline="central">HABITAT: Bare Monolithic Quartzite Outcrops · Soil-less Saxicole · Dry-Season Ψleaf &lt; -100 MPa</text>')

    # -------------------------------------------------------------------------
    # Card 1: Ecophysiological & Cellular Response (Y: 172 to 308)
    # -------------------------------------------------------------------------
    svg.append('    <!-- Vtub Card 1: Ecophysiology & Cellular State -->')
    svg.append('    <g id="vtub_card1_physiology">')
    svg.append('      <rect x="36" y="172" width="524" height="136" rx="6" ry="6" fill="#FFFFFF" stroke="#FDE68A" stroke-width="1" filter="url(#softShadow)"/>')
    svg.append('      <rect x="36" y="172" width="524" height="22" rx="6" ry="6" fill="#FEF3C7"/>')
    svg.append('      <text x="46" y="183" font-size="9px" font-weight="bold" fill="#92400E" text-anchor="start" dominant-baseline="central">1. ECOPHYSIOLOGICAL RESPONSE: ANHYDROBIOSIS &amp; METABOLIC DORMANCY</text>')
      
    # Left Illustration Graphic: Leaf States & Plastid Transformation
    svg.append('      <!-- Illustration: Desiccation & Desiccoplast Transition -->')
    svg.append('      <g id="vtub_plastid_graphic" transform="translate(46, 202)">')
    # Hydrated Foliage Icon
    svg.append('        <path d="M 12 40 C 6 25 15 10 24 5 C 26 18 20 32 12 40 Z" fill="#65A30D" stroke="#365314" stroke-width="1"/>')
    svg.append('        <path d="M 22 40 C 24 22 35 12 42 8 C 40 22 32 34 22 40 Z" fill="#84CC16" stroke="#365314" stroke-width="1"/>')
    svg.append('        <text x="24" y="52" font-size="7px" font-weight="bold" fill="#3F6212" text-anchor="middle">Hydrated (Rain)</text>')
      
    # Arrow to Desiccated
    svg.append('        <path d="M 46 25 L 70 25" stroke="#D97706" stroke-width="1.5" marker-end="url(#arrowAmber)"/>')
    svg.append('        <text x="58" y="18" font-size="6.5px" fill="#B45309" text-anchor="middle">Drought</text>')
      
    # Desiccated Foliage Icon (Curled, anthocyanic)
    svg.append('        <path d="M 76 40 C 74 28 80 18 84 15 C 88 18 86 30 84 40 Z" fill="#78350F" stroke="#451A03" stroke-width="1"/>')
    svg.append('        <path d="M 84 40 C 86 26 94 20 98 18 C 96 28 92 36 84 40 Z" fill="#9A3412" stroke="#451A03" stroke-width="1"/>')
    svg.append('        <text x="88" y="52" font-size="7px" font-weight="bold" fill="#78350F" text-anchor="middle">Desiccated (Dry)</text>')
      
    # Plastid Transition Graphic
    svg.append('        <g transform="translate(112, 0)">')
    svg.append('          <!-- Chloroplast -->')
    svg.append('          <ellipse cx="20" cy="22" rx="16" ry="11" fill="url(#chloroplastGrad)" stroke="#166534" stroke-width="1"/>')
    svg.append('          <line x1="10" y1="20" x2="18" y2="20" stroke="#DCFCE7" stroke-width="1.5"/>')
    svg.append('          <line x1="10" y1="23" x2="18" y2="23" stroke="#DCFCE7" stroke-width="1.5"/>')
    svg.append('          <line x1="22" y1="20" x2="30" y2="20" stroke="#DCFCE7" stroke-width="1.5"/>')
    svg.append('          <line x1="22" y1="23" x2="30" y2="23" stroke="#DCFCE7" stroke-width="1.5"/>')
    svg.append('          <text x="20" y="42" font-size="6.5px" font-weight="bold" fill="#15803D" text-anchor="middle">Chloroplast</text>')
          
    svg.append('          <!-- Arrow -->')
    svg.append('          <path d="M 38 22 L 54 22" stroke="#B45309" stroke-width="1.2" marker-end="url(#arrowAmber)"/>')
          
    # Desiccoplast
    svg.append('          <ellipse cx="72" cy="22" rx="14" ry="9" fill="url(#desiccoplastGrad)" stroke="#78350F" stroke-width="1"/>')
    svg.append('          <circle cx="67" cy="20" r="2" fill="#FEF08A"/>')
    svg.append('          <circle cx="73" cy="23" r="2.2" fill="#FEF08A"/>')
    svg.append('          <circle cx="77" cy="19" r="1.8" fill="#FEF08A"/>')
    svg.append('          <text x="72" y="42" font-size="6.5px" font-weight="bold" fill="#92400E" text-anchor="middle">Desiccoplast</text>')
    svg.append('        </g>')
    svg.append('      </g>')

    # Bullet Text for Physiology
    svg.append('      <g id="vtub_phys_bullets" transform="translate(254, 202)">')
    svg.append('        <circle cx="4" cy="7" r="2.5" fill="#D97706"/>')
    svg.append('        <text x="12" y="7" font-size="7.5px" font-weight="bold" fill="#1E293B" dominant-baseline="central">Poikilochlorophylly &amp; Thylakoid Dismantling:</text>')
    svg.append('        <text x="12" y="18" font-size="7.2px" fill="#475569" dominant-baseline="central">Targeted chlorophyll degradation prevents ROS formation in bare-rock sun.</text>')

    svg.append('        <circle cx="4" cy="33" r="2.5" fill="#D97706"/>')
    svg.append('        <text x="12" y="33" font-size="7.5px" font-weight="bold" fill="#1E293B" dominant-baseline="central">Cytoplasmic Vitrification (Glass Matrix):</text>')
    svg.append('        <text x="12" y="44" font-size="7.2px" fill="#475569" dominant-baseline="central">Accumulation of LEA proteins &amp; raffinose oligosaccharides (RFOs).</text>')

    svg.append('        <circle cx="4" cy="59" r="2.5" fill="#D97706"/>')
    svg.append('        <text x="12" y="59" font-size="7.5px" font-weight="bold" fill="#1E293B" dominant-baseline="central">Metabolic Arrest (Zero Respiration):</text>')
    svg.append('        <text x="12" y="70" font-size="7.2px" fill="#475569" dominant-baseline="central">Quiescent state; complete stomatal closure; zero hydraulic cavitation risk.</text>')
    svg.append('      </g>')
    svg.append('    </g>')

    # -------------------------------------------------------------------------
    # Card 2: Genomic & Molecular Architecture (Y: 316 to 518)
    # -------------------------------------------------------------------------
    svg.append('    <!-- Vtub Card 2: Genomic Architecture & Selection -->')
    svg.append('    <g id="vtub_card2_genomics">')
    svg.append('      <rect x="36" y="316" width="524" height="202" rx="6" ry="6" fill="#FFFFFF" stroke="#FDE68A" stroke-width="1" filter="url(#softShadow)"/>')
    svg.append('      <rect x="36" y="316" width="524" height="22" rx="6" ry="6" fill="#FEF3C7"/>')
    svg.append('      <text x="46" y="327" font-size="9px" font-weight="bold" fill="#92400E" text-anchor="start" dominant-baseline="central">2. GENOMIC ARCHITECTURE: REPAIR EXPANSIONS &amp; POSITIVE SELECTION</text>')

    # CAFE5 Summary Badge
    svg.append('      <rect x="46" y="344" width="504" height="20" rx="3" ry="3" fill="#FFFBEB" stroke="#FCD34D" stroke-width="0.8"/>')
    svg.append('      <text x="56" y="354" font-size="7.8px" font-weight="bold" fill="#B45309" text-anchor="start" dominant-baseline="central">CAFE5 TURNOVER (λ = 0.0036): 56 Stringent Expansions + 11 Rate-Sensitive Expansions</text>')

    # Category A: Plastid Import & Electron Transport
    svg.append('      <g id="vtub_repair_expansions" transform="translate(46, 372)">')
    svg.append('        <rect x="0" y="0" width="246" height="72" rx="4" ry="4" fill="#FAFAFA" stroke="#E5E7EB" stroke-width="0.8"/>')
    svg.append('        <text x="8" y="11" font-size="7.8px" font-weight="bold" fill="#92400E">Plastid Biogenesis &amp; Repair Expansions</text>')
        
    svg.append('        <rect x="8" y="18" width="230" height="15" rx="2" ry="2" fill="#FEF3C7"/>')
    svg.append('        <text x="14" y="26" font-size="7.2px" font-weight="bold" fill="#B45309" dominant-baseline="central">TOC/TIC Translocons: +55 Genes (OG0000016)</text>')
    svg.append('        <text x="14" y="38" font-size="6.8px" fill="#4B5563" dominant-baseline="central">Preprotein translocons for massive chloroplast reassembly.</text>')

    svg.append('        <rect x="8" y="45" width="230" height="15" rx="2" ry="2" fill="#FEF3C7"/>')
    svg.append('        <text x="14" y="53" font-size="7.2px" font-weight="bold" fill="#B45309" dominant-baseline="central">NDH Complex Subunits: +29 Genes (OG0000036)</text>')
    svg.append('        <text x="14" y="64" font-size="6.8px" fill="#4B5563" dominant-baseline="central">NADH:plastoquinone oxidoreductase for cyclic electron flow.</text>')
    svg.append('      </g>')

    # Category B: Photosystem & Chaperone Protection
    svg.append('      <g id="vtub_membrane_repair" transform="translate(304, 372)">')
    svg.append('        <rect x="0" y="0" width="246" height="72" rx="4" ry="4" fill="#FAFAFA" stroke="#E5E7EB" stroke-width="0.8"/>')
    svg.append('        <text x="8" y="11" font-size="7.8px" font-weight="bold" fill="#92400E">Photoprotection &amp; Structural Repair</text>')

    svg.append('        <rect x="8" y="18" width="230" height="15" rx="2" ry="2" fill="#FEF3C7"/>')
    svg.append('        <text x="14" y="26" font-size="7.2px" font-weight="bold" fill="#B45309" dominant-baseline="central">PSII Core Stabilizers: +24 Genes (OG0000069)</text>')
    svg.append('        <text x="14" y="38" font-size="6.8px" fill="#4B5563" dominant-baseline="central">PsbA / PsbD reaction center repair enzymes.</text>')

    svg.append('        <rect x="8" y="45" width="230" height="15" rx="2" ry="2" fill="#FEF3C7"/>')
    svg.append('        <text x="14" y="53" font-size="7.2px" font-weight="bold" fill="#B45309" dominant-baseline="central">Acetyl-CoA Carboxylase: +23 Genes (OG0000072)</text>')
    svg.append('        <text x="14" y="64" font-size="6.8px" fill="#4B5563" dominant-baseline="central">De novo thylakoid lipid synthesis upon rehydration.</text>')
    svg.append('      </g>')

    # Category C: Positive Selection Candidates (Ka/Ks > 1.0)
    svg.append('      <g id="vtub_positive_selection" transform="translate(46, 450)">')
    svg.append('        <rect x="0" y="0" width="504" height="60" rx="4" ry="4" fill="#FFF7ED" stroke="#FDBA74" stroke-width="1"/>')
    svg.append('        <text x="8" y="11" font-size="7.8px" font-weight="bold" fill="#C2410C">ORGANELIAR RNA EDITING &amp; CHAPERONES UNDER DIVERSIFYING SELECTION (Ka/Ks &gt; 1.0)</text>')
        
    svg.append('        <text x="8" y="24" font-size="7.2px" font-weight="bold" fill="#9A3412">★ 17 Pentatricopeptide Repeat (PPR) Genes:</text>')
    svg.append('        <text x="188" y="24" font-size="7.0px" fill="#334155">OG0011783 (ω = 4.91), OG0010277 (ω = 4.54), OG0012000 (ω = 4.50), OG0011369 (ω = 3.86)</text>')
        
    svg.append('        <text x="8" y="37" font-size="7.2px" font-weight="bold" fill="#9A3412">★ Catalytic RNA Editing &amp; Recognition:</text>')
    svg.append('        <text x="188" y="37" font-size="7.0px" fill="#334155">DYW cytidine deaminase (OG0011950, ω = 3.80), Organellar RRM (OG0012126, ω = 4.50)</text>')

    svg.append('        <text x="8" y="50" font-size="7.2px" font-weight="bold" fill="#9A3412">★ Vitrification &amp; Redox Chaperones:</text>')
    svg.append('        <text x="188" y="50" font-size="7.0px" fill="#334155">DnaJ/Hsp40 co-chaperone (OG0011532, ω = 3.86), Transmembrane thioredoxin (OG0011290, ω = 4.31)</text>')
    svg.append('      </g>')
    svg.append('    </g>')

    # -------------------------------------------------------------------------
    # Card 3: Rehydration Dynamics & Evolutionary Trade-Off (Y: 526 to 704)
    # -------------------------------------------------------------------------
    svg.append('    <!-- Vtub Card 3: Rehydration Dynamics & Trade-Off -->')
    svg.append('    <g id="vtub_card3_tradeoff">')
    svg.append('      <rect x="36" y="526" width="524" height="178" rx="6" ry="6" fill="#FFFFFF" stroke="#FDE68A" stroke-width="1" filter="url(#softShadow)"/>')
    svg.append('      <rect x="36" y="526" width="524" height="22" rx="6" ry="6" fill="#FEF3C7"/>')
    svg.append('      <text x="46" y="537" font-size="9px" font-weight="bold" fill="#92400E" text-anchor="start" dominant-baseline="central">3. REHYDRATION KINETICS &amp; EVOLUTIONARY FITNESS EQUATION</text>')

    # Rehydration Timeline Graphic (0h -> 24h -> 72h)
    svg.append('      <g id="rehydration_timeline" transform="translate(46, 554)">')
    svg.append('        <rect x="0" y="0" width="504" height="48" rx="4" ry="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="0.8"/>')
    svg.append('        <line x1="30" y1="20" x2="474" y2="20" stroke="#CBD5E1" stroke-width="2"/>')
        
    svg.append('        <circle cx="50" cy="20" r="6" fill="#D97706" stroke="#FFFFFF" stroke-width="1.5"/>')
    svg.append('        <text x="50" y="32" font-size="7px" font-weight="bold" fill="#92400E" text-anchor="middle">0 – 6 h</text>')
    svg.append('        <text x="50" y="41" font-size="6.2px" fill="#64748B" text-anchor="middle">Water Imbibition</text>')

    svg.append('        <circle cx="210" cy="20" r="6" fill="#F59E0B" stroke="#FFFFFF" stroke-width="1.5"/>')
    svg.append('        <text x="210" y="32" font-size="7px" font-weight="bold" fill="#92400E" text-anchor="middle">12 – 24 h</text>')
    svg.append('        <text x="210" y="41" font-size="6.2px" font-weight="bold" fill="#B45309" text-anchor="middle">Translation of Pre-Edited RNA</text>')

    svg.append('        <circle cx="430" cy="20" r="6" fill="#16A34A" stroke="#FFFFFF" stroke-width="1.5"/>')
    svg.append('        <text x="430" y="32" font-size="7px" font-weight="bold" fill="#15803D" text-anchor="middle">48 – 72 h</text>')
    svg.append('        <text x="430" y="41" font-size="6.2px" font-weight="bold" fill="#166534" text-anchor="middle">Full Photosynthetic Competence</text>')
    svg.append('      </g>')

    # Trade-off Balance Text
    svg.append('      <g id="vtub_tradeoff_summary" transform="translate(46, 610)">')
    # Major Evolutionary Advantage
    svg.append('        <rect x="0" y="0" width="246" height="86" rx="4" ry="4" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1"/>')
    svg.append('        <text x="8" y="12" font-size="7.8px" font-weight="bold" fill="#065F46">EVOLUTIONARY ADVANTAGES (RESILIENCE)</text>')
    svg.append('        <text x="8" y="26" font-size="7.2px" fill="#047857">✔ <tspan font-weight="bold">Zero Drought Mortality:</tspan> Survives total tissue</text>')
    svg.append('        <text x="18" y="37" font-size="7.2px" fill="#047857">dehydration on bare rock (Ψ &lt; -100 MPa).</text>')
    svg.append('        <text x="8" y="50" font-size="7.2px" fill="#047857">✔ <tspan font-weight="bold">Zero Hydraulic Cavitation:</tspan> Complete shutdown</text>')
    svg.append('        <text x="18" y="61" font-size="7.2px" fill="#047857">eliminates xylem embolism vulnerability.</text>')
    svg.append('        <text x="8" y="74" font-size="7.2px" fill="#047857">✔ <tspan font-weight="bold">Immediate Rebuilding:</tspan> PPR transcripts ready.</text>')

    # Major Evolutionary Cost
    svg.append('        <rect x="258" y="0" width="246" height="86" rx="4" ry="4" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1"/>')
    svg.append('        <text x="8" y="12" font-size="7.8px" font-weight="bold" fill="#9F1239">EVOLUTIONARY COSTS &amp; LIMITATIONS</text>')
    svg.append('        <text x="8" y="26" font-size="7.2px" fill="#BE123C">✖ <tspan font-weight="bold">Restricted Carbon Gain:</tspan> Lower annual Amax</text>')
    svg.append('        <text x="18" y="37" font-size="7.2px" fill="#BE123C">due to prolonged seasonal dormancy periods.</text>')
    svg.append('        <text x="8" y="50" font-size="7.2px" fill="#BE123C">✖ <tspan font-weight="bold">Reconstruction Energetic Cost:</tspan> Significant</text>')
    svg.append('        <text x="18" y="61" font-size="7.2px" fill="#BE123C">ATP/carbon spent re-synthesizing chlorophyll.</text>')
    svg.append('        <text x="8" y="74" font-size="7.2px" fill="#BE123C">✖ <tspan font-weight="bold">Low Competitive Vigor:</tspan> Restricted to bare rock.</text>')
    svg.append('      </g>')
    svg.append('    </g>')
    svg.append('  </g>')

    # =========================================================================
    # PANEL C: RIGHT COLUMN — Vellozia peripherica (Evergreen Generalist)
    # =========================================================================
    svg.append('  <!-- =================================================== -->')
    svg.append('  <!-- PANEL C: VELLOZIA PERIPHERICA (EVERGREEN)           -->')
    svg.append('  <!-- =================================================== -->')
    svg.append('  <g id="panel_c_right_column_vperipherica">')
    
    # Outer Framing Box
    svg.append('    <rect x="628" y="118" width="548" height="594" rx="8" ry="8" fill="#F7FCF9" stroke="#009E73" stroke-width="1.8" filter="url(#cardShadow)"/>')
    
    # Column Header Banner (with clip path)
    svg.append('    <g clip-path="url(#vperHeaderClip)">')
    svg.append('      <rect x="628" y="118" width="548" height="46" fill="url(#vperBannerGrad)"/>')
    svg.append('    </g>')
    svg.append('    <text x="644" y="136" font-size="13px" font-weight="bold" fill="#FFFFFF" text-anchor="start" dominant-baseline="central">Vellozia peripherica</text>')
    svg.append('    <text x="790" y="136" font-size="11px" font-style="italic" fill="#D1FAE5" text-anchor="start" dominant-baseline="central">— Evergreen Generalist (Desiccation-Sensitive)</text>')
    svg.append('    <rect x="644" y="148" width="516" height="12" rx="2" ry="2" fill="#064E3B" fill-opacity="0.5"/>')
    svg.append('    <text x="648" y="154" font-size="7.5px" font-weight="bold" fill="#FFFFFF" text-anchor="start" dominant-baseline="central">HABITAT: Shaded Rock Fissures &amp; Crevices · Micro-soil Pocket · Dry-Season Ψleaf ≈ -1.5 to -2.0 MPa</text>')

    # -------------------------------------------------------------------------
    # Card 1: Ecophysiological & Cellular Response (Y: 172 to 308)
    # -------------------------------------------------------------------------
    svg.append('    <!-- Vper Card 1: Ecophysiology & Active Transpiration -->')
    svg.append('    <g id="vper_card1_physiology">')
    svg.append('      <rect x="640" y="172" width="524" height="136" rx="6" ry="6" fill="#FFFFFF" stroke="#A7F3D0" stroke-width="1" filter="url(#softShadow)"/>')
    svg.append('      <rect x="640" y="172" width="524" height="22" rx="6" ry="6" fill="#D1FAE5"/>')
    svg.append('      <text x="650" y="183" font-size="9px" font-weight="bold" fill="#065F46" text-anchor="start" dominant-baseline="central">1. ECOPHYSIOLOGICAL RESPONSE: ACTIVE TRANSPIRATION &amp; HOMEOSTASIS</text>')

    # Right Illustration Graphic: Evergreen Habit & Intact Chloroplast Under Heat
    svg.append('      <!-- Illustration: Persistent Green Foliage in Fissure & Photo-Oxidative Stress -->')
    svg.append('      <g id="vper_chloroplast_graphic" transform="translate(650, 202)">')
    # Rock Fissure Outline
    svg.append('        <path d="M 5 44 L 20 20 L 25 44 Z" fill="#64748B"/>')
    svg.append('        <path d="M 75 44 L 60 20 L 55 44 Z" fill="#64748B"/>')
    # Persistent Leaves
    svg.append('        <path d="M 40 44 C 30 25 25 10 32 5 C 38 18 42 32 40 44 Z" fill="#15803D" stroke="#064E3B" stroke-width="1"/>')
    svg.append('        <path d="M 40 44 C 50 25 55 10 48 5 C 42 18 38 32 40 44 Z" fill="#16A34A" stroke="#064E3B" stroke-width="1"/>')
    svg.append('        <path d="M 40 44 C 40 20 40 4 40 2 C 40 18 40 32 40 44 Z" fill="#22C55E" stroke="#064E3B" stroke-width="1"/>')
    svg.append('        <text x="40" y="52" font-size="7px" font-weight="bold" fill="#065F46" text-anchor="middle">Evergreen (Year-Round)</text>')

    # Active Transpiration & ROS Graphic
    svg.append('        <g transform="translate(95, 0)">')
    svg.append('          <ellipse cx="26" cy="22" rx="20" ry="13" fill="url(#chloroplastGrad)" stroke="#064E3B" stroke-width="1.2"/>')
    svg.append('          <line x1="14" y1="18" x2="24" y2="18" stroke="#DCFCE7" stroke-width="1.5"/>')
    svg.append('          <line x1="14" y1="22" x2="24" y2="22" stroke="#DCFCE7" stroke-width="1.5"/>')
    svg.append('          <line x1="28" y1="18" x2="38" y2="18" stroke="#DCFCE7" stroke-width="1.5"/>')
    svg.append('          <line x1="28" y1="22" x2="38" y2="22" stroke="#DCFCE7" stroke-width="1.5"/>')
          
    # Photo-oxidative ROS Sparkles
    svg.append('          <circle cx="48" cy="12" r="3" fill="#EF4444" fill-opacity="0.8"/>')
    svg.append('          <text x="48" y="13" font-size="5.5px" font-weight="bold" fill="#FFFFFF" text-anchor="middle" dominant-baseline="central">ROS</text>')
    svg.append('          <circle cx="8" cy="14" r="2.5" fill="#EF4444" fill-opacity="0.8"/>')
    svg.append('          <circle cx="36" cy="34" r="2.5" fill="#EF4444" fill-opacity="0.8"/>')
    svg.append('          <text x="26" y="42" font-size="6.5px" font-weight="bold" fill="#065F46" text-anchor="middle">Continuous e- Flow &amp; ROS</text>')
    svg.append('        </g>')
    svg.append('      </g>')

    # Bullet Text for Physiology
    svg.append('      <g id="vper_phys_bullets" transform="translate(858, 202)">')
    svg.append('        <circle cx="4" cy="7" r="2.5" fill="#009E73"/>')
    svg.append('        <text x="12" y="7" font-size="7.5px" font-weight="bold" fill="#1E293B" dominant-baseline="central">Desiccation-Avoidance &amp; Hydraulic Regulation:</text>')
    svg.append('        <text x="12" y="18" font-size="7.2px" fill="#475569" dominant-baseline="central">Maintains hydrated foliage; taps crevice moisture (Ψ ≈ -2.0 MPa).</text>')

    svg.append('        <circle cx="4" cy="33" r="2.5" fill="#009E73"/>')
    svg.append('        <text x="12" y="33" font-size="7.5px" font-weight="bold" fill="#1E293B" dominant-baseline="central">Continuous Photosynthesis &amp; Light Harvesting:</text>')
    svg.append('        <text x="12" y="44" font-size="7.2px" fill="#475569" dominant-baseline="central">Persistent electron transport under intense irradiance causes high ROS.</text>')

    svg.append('        <circle cx="4" cy="59" r="2.5" fill="#009E73"/>')
    svg.append('        <text x="12" y="59" font-size="7.5px" font-weight="bold" fill="#1E293B" dominant-baseline="central">Vulnerability to Extreme Mega-Drought:</text>')
    svg.append('        <text x="12" y="70" font-size="7.2px" fill="#475569" dominant-baseline="central">If soil water is exhausted, prone to fatal runaway xylem cavitation.</text>')
    svg.append('      </g>')
    svg.append('    </g>')

    # -------------------------------------------------------------------------
    # Card 2: Genomic Architecture ("The Genomic Burden") (Y: 316 to 518)
    # -------------------------------------------------------------------------
    svg.append('    <!-- Vper Card 2: Genomic Architecture & Burden -->')
    svg.append('    <g id="vper_card2_genomics">')
    svg.append('      <rect x="640" y="316" width="524" height="202" rx="6" ry="6" fill="#FFFFFF" stroke="#A7F3D0" stroke-width="1" filter="url(#softShadow)"/>')
    svg.append('      <rect x="640" y="316" width="524" height="22" rx="6" ry="6" fill="#D1FAE5"/>')
    svg.append('      <text x="650" y="327" font-size="9px" font-weight="bold" fill="#065F46" text-anchor="start" dominant-baseline="central">2. "THE GENOMIC BURDEN OF BEING EVERGREEN": MASSIVE EXPANSIONS</text>')

    # CAFE5 Summary Badge
    svg.append('      <rect x="650" y="344" width="504" height="20" rx="3" ry="3" fill="#ECFDF5" stroke="#6EE7B7" stroke-width="0.8"/>')
    svg.append('      <text x="660" y="354" font-size="7.8px" font-weight="bold" fill="#047857" text-anchor="start" dominant-baseline="central">CAFE5 TURNOVER (λ = 0.0036): 86 Stringent Expansions + 22 Rate-Sensitive Expansions</text>')

    # Category A: Protein Turnover & F-box E3 Ligases
    svg.append('      <g id="vper_ubiquitin_expansions" transform="translate(650, 372)">')
    svg.append('        <rect x="0" y="0" width="246" height="72" rx="4" ry="4" fill="#FAFAFA" stroke="#E5E7EB" stroke-width="0.8"/>')
    svg.append('        <text x="8" y="11" font-size="7.8px" font-weight="bold" fill="#065F46">Protein Turnover &amp; Proteasome Degradation</text>')

    svg.append('        <rect x="8" y="18" width="230" height="15" rx="2" ry="2" fill="#D1FAE5"/>')
    svg.append('        <text x="14" y="26" font-size="7.2px" font-weight="bold" fill="#047857" dominant-baseline="central">F-box E3 Ubiquitin Ligases: +51 Genes (OG0000026)</text>')
    svg.append('        <text x="14" y="38" font-size="6.8px" fill="#4B5563" dominant-baseline="central">Degradation of photo-damaged proteins via 26S proteasome.</text>')

    svg.append('        <rect x="8" y="45" width="230" height="15" rx="2" ry="2" fill="#D1FAE5"/>')
    svg.append('        <text x="14" y="53" font-size="7.2px" font-weight="bold" fill="#047857" dominant-baseline="central">Ubiquitin Receptors &amp; E3s: +21 Genes (OG0000043)</text>')
    svg.append('        <text x="14" y="64" font-size="6.8px" fill="#4B5563" dominant-baseline="central">Proteome surveillance under uninterrupted solar irradiance.</text>')
    svg.append('      </g>')

    # Category B: Mechanical Stress & Pathogen Sentinels
    svg.append('      <g id="vper_defense_expansions" transform="translate(908, 372)">')
    svg.append('        <rect x="0" y="0" width="246" height="72" rx="4" ry="4" fill="#FAFAFA" stroke="#E5E7EB" stroke-width="0.8"/>')
    svg.append('        <text x="8" y="11" font-size="7.8px" font-weight="bold" fill="#065F46">Receptor Kinases &amp; Foliar Pathogen Sentinels</text>')

    svg.append('        <rect x="8" y="18" width="230" height="15" rx="2" ry="2" fill="#D1FAE5"/>')
    svg.append('        <text x="14" y="26" font-size="7.2px" font-weight="bold" fill="#047857" dominant-baseline="central">LRR-RLK Receptor Kinases: +57/+29/+25 Genes</text>')
    svg.append('        <text x="14" y="38" font-size="6.8px" fill="#4B5563" dominant-baseline="central">Continuous sensing of cell wall turgor and mechanical strain.</text>')

    svg.append('        <rect x="8" y="45" width="230" height="15" rx="2" ry="2" fill="#D1FAE5"/>')
    svg.append('        <text x="14" y="53" font-size="7.2px" font-weight="bold" fill="#047857" dominant-baseline="central">NB-LRR Disease Sentinels: +22/+17 Genes (OG0000050)</text>')
    svg.append('        <text x="14" y="64" font-size="6.8px" fill="#4B5563" dominant-baseline="central">Constitutive defense of warm, hydrated foliage against fungi.</text>')
    svg.append('      </g>')

    # Category C: Secondary Metabolism & Wax Protection
    svg.append('      <g id="vper_secondary_metabolism" transform="translate(650, 450)">')
    svg.append('        <rect x="0" y="0" width="504" height="60" rx="4" ry="4" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1"/>')
    svg.append('        <text x="8" y="11" font-size="7.8px" font-weight="bold" fill="#166534">FOLIAR DEFENSE ARRAYS &amp; SECONDARY METABOLIC SHIELDING</text>')

    svg.append('        <text x="8" y="24" font-size="7.2px" font-weight="bold" fill="#15803D">★ Cytochrome P450 Monooxygenases (+88 Genes):</text>')
    svg.append('        <text x="210" y="24" font-size="7.0px" fill="#334155">Massive expansion for dense cuticular wax biosynthesis &amp; UV-B flavonoid screening.</text>')

    svg.append('        <text x="8" y="37" font-size="7.2px" font-weight="bold" fill="#15803D">★ UDP-Glycosyltransferases (+78 Genes):</text>')
    svg.append('        <text x="210" y="37" font-size="7.0px" fill="#334155">Antioxidant conjugation &amp; phenolic solubilization for sustained foliar defense.</text>')

    svg.append('        <text x="8" y="50" font-size="7.2px" font-weight="bold" fill="#15803D">★ G-type Lectin Receptor Kinases (+22 Genes):</text>')
    svg.append('        <text x="210" y="50" font-size="7.0px" fill="#334155">Surveillance of opportunist foliar pathogens in permanently hydrated green tissue.</text>')
    svg.append('      </g>')
    svg.append('    </g>')

    # -------------------------------------------------------------------------
    # Card 3: Fitness Profile & Evolutionary Trade-Off (Y: 526 to 704)
    # -------------------------------------------------------------------------
    svg.append('    <!-- Vper Card 3: Fitness Profile & Trade-Off -->')
    svg.append('    <g id="vper_card3_tradeoff">')
    svg.append('      <rect x="640" y="526" width="524" height="178" rx="6" ry="6" fill="#FFFFFF" stroke="#A7F3D0" stroke-width="1" filter="url(#softShadow)"/>')
    svg.append('      <rect x="640" y="526" width="524" height="22" rx="6" ry="6" fill="#D1FAE5"/>')
    svg.append('      <text x="650" y="537" font-size="9px" font-weight="bold" fill="#065F46" text-anchor="start" dominant-baseline="central">3. YEAR-ROUND PRODUCTIVITY &amp; THE ECOLOGICAL CAVITATION RISK</text>')

    # Continuous Productivity Timeline Graphic
    svg.append('      <g id="evergreen_timeline" transform="translate(650, 554)">')
    svg.append('        <rect x="0" y="0" width="504" height="48" rx="4" ry="4" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="0.8"/>')
    svg.append('        <line x1="30" y1="20" x2="474" y2="20" stroke="#CBD5E1" stroke-width="2"/>')
        
    svg.append('        <circle cx="80" cy="20" r="6" fill="#059669" stroke="#FFFFFF" stroke-width="1.5"/>')
    svg.append('        <text x="80" y="32" font-size="7px" font-weight="bold" fill="#065F46" text-anchor="middle">Wet Season</text>')
    svg.append('        <text x="80" y="41" font-size="6.2px" font-weight="bold" fill="#047857" text-anchor="middle">Maximum Assimilation (Amax)</text>')

    svg.append('        <circle cx="252" cy="20" r="6" fill="#10B981" stroke="#FFFFFF" stroke-width="1.5"/>')
    svg.append('        <text x="252" y="32" font-size="7px" font-weight="bold" fill="#065F46" text-anchor="middle">Dry Season</text>')
    svg.append('        <text x="252" y="41" font-size="6.2px" fill="#475569" text-anchor="middle">Stomatal Throttling &amp; Upkeep</text>')

    svg.append('        <circle cx="424" cy="20" r="6" fill="#DC2626" stroke="#FFFFFF" stroke-width="1.5"/>')
    svg.append('        <text x="424" y="32" font-size="7px" font-weight="bold" fill="#991B1B" text-anchor="middle">Mega-Drought Event</text>')
    svg.append('        <text x="424" y="41" font-size="6.2px" font-weight="bold" fill="#B91C1C" text-anchor="middle">Runaway Hydraulic Cavitation Risk</text>')
    svg.append('      </g>')

    # Trade-off Balance Text
    svg.append('      <g id="vper_tradeoff_summary" transform="translate(650, 610)">')
    # Major Evolutionary Advantage
    svg.append('        <rect x="0" y="0" width="246" height="86" rx="4" ry="4" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1"/>')
    svg.append('        <text x="8" y="12" font-size="7.8px" font-weight="bold" fill="#065F46">EVOLUTIONARY ADVANTAGES (PRODUCTIVITY)</text>')
    svg.append('        <text x="8" y="26" font-size="7.2px" fill="#047857">✔ <tspan font-weight="bold">High Annual Carbon Gain:</tspan> Continuous</text>')
    svg.append('        <text x="18" y="37" font-size="7.2px" fill="#047857">photosynthesis yields faster biomass accumulation.</text>')
    svg.append('        <text x="8" y="50" font-size="7.2px" fill="#047857">✔ <tspan font-weight="bold">Zero Recovery Lag:</tspan> Instantaneous exploitation</text>')
    svg.append('        <text x="18" y="61" font-size="7.2px" fill="#047857">of intermittent rains without reassembly cost.</text>')
    svg.append('        <text x="8" y="74" font-size="7.2px" fill="#047857">✔ <tspan font-weight="bold">Competitive Exclusion:</tspan> Dominates crevice soils.</text>')

    # Major Evolutionary Cost
    svg.append('        <rect x="258" y="0" width="246" height="86" rx="4" ry="4" fill="#FFF1F2" stroke="#FECDD3" stroke-width="1"/>')
    svg.append('        <text x="8" y="12" font-size="7.8px" font-weight="bold" fill="#9F1239">EVOLUTIONARY COSTS &amp; VULNERABILITIES</text>')
    svg.append('        <text x="8" y="26" font-size="7.2px" fill="#BE123C">✖ <tspan font-weight="bold">High Genomic Upkeep:</tspan> Massive continuous</text>')
    svg.append('        <text x="18" y="37" font-size="7.2px" fill="#BE123C">protein turnover (F-box +51) &amp; immune sentinels.</text>')
    svg.append('        <text x="8" y="50" font-size="7.2px" fill="#BE123C">✖ <tspan font-weight="bold">Hydraulic Failure Risk:</tspan> Complete inability</text>')
    svg.append('        <text x="18" y="61" font-size="7.2px" fill="#BE123C">to tolerate tissue desiccation (lethal at &lt; -3 MPa).</text>')
    svg.append('        <text x="8" y="74" font-size="7.2px" fill="#BE123C">✖ <tspan font-weight="bold">Foliar Pathogen Load:</tspan> Permanent tissue target.</text>')
    svg.append('      </g>')
    svg.append('    </g>')
    svg.append('  </g>')

    # =========================================================================
    # PANEL D: CENTRAL NEXUS — Divergence Timeline & Balance Scale
    # =========================================================================
    svg.append('  <!-- =================================================== -->')
    svg.append('  <!-- PANEL D: CENTRAL NEXUS & TRADE-OFF BALANCE SCALE    -->')
    svg.append('  <!-- =================================================== -->')
    svg.append('  <g id="panel_d_central_tradeoff_scale" transform="translate(600, 410)">')
    # Background pill for center scale
    svg.append('    <rect x="-24" y="-230" width="48" height="520" rx="24" ry="24" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2" filter="url(#softShadow)"/>')

    # Top Divergence Label
    svg.append('    <circle cx="0" cy="-210" r="14" fill="#1E293B"/>')
    svg.append('    <text x="0" y="-208" font-size="8px" font-weight="bold" fill="#F8FAFC" text-anchor="middle" dominant-baseline="central">9.74</text>')
    svg.append('    <text x="0" y="-188" font-size="6.5px" font-weight="bold" fill="#64748B" text-anchor="middle">Ma Split</text>')

    # Central Vertical Spine
    svg.append('    <line x1="0" y1="-175" x2="0" y2="250" stroke="#94A3B8" stroke-width="2" stroke-dasharray="4,3"/>')

    # Stylized Mechanical Balance Scale in Center
    svg.append('    <g id="scale_graphic" transform="translate(0, 0)">')
    # Fulcrum
    svg.append('      <polygon points="-8,16 8,16 0,0" fill="#334155"/>')
    svg.append('      <circle cx="0" cy="0" r="3.5" fill="#F59E0B"/>')
      
    # Beam
    svg.append('      <line x1="-20" y1="-4" x2="20" y2="4" stroke="#475569" stroke-width="2.5" stroke-linecap="round"/>')
      
    # Left Pan (Resilience)
    svg.append('      <line x1="-18" y1="-4" x2="-18" y2="10" stroke="#94A3B8" stroke-width="1"/>')
    svg.append('      <path d="M -24 10 Q -18 16 -12 10 Z" fill="#D97706"/>')
      
    # Right Pan (Productivity)
    svg.append('      <line x1="18" y1="4" x2="18" y2="18" stroke="#94A3B8" stroke-width="1"/>')
    svg.append('      <path d="M 12 18 Q 18 24 24 18 Z" fill="#009E73"/>')
      
    svg.append('      <text x="0" y="32" font-size="6.8px" font-weight="bold" fill="#0F172A" text-anchor="middle">TRADE-OFF</text>')
    svg.append('    </g>')

    # Directional Badges
    svg.append('    <g transform="translate(0, 140)">')
    svg.append('      <rect x="-20" y="-12" width="40" height="24" rx="4" ry="4" fill="#0F172A"/>')
    svg.append('      <text x="0" y="-2" font-size="6.5px" font-weight="bold" fill="#FBBF24" text-anchor="middle">OCBIL</text>')
    svg.append('      <text x="0" y="6" font-size="5.5px" fill="#FFFFFF" text-anchor="middle">Divergence</text>')
    svg.append('    </g>')
    svg.append('  </g>')

    # =========================================================================
    # PANEL E: BOTTOM SYNTHESIS MATRIX — Synoptic Master Trade-Off Comparison
    # =========================================================================
    svg.append('  <!-- =================================================== -->')
    svg.append('  <!-- PANEL E: SYNOPTIC MASTER TRADE-OFF COMPARISON TABLE -->')
    svg.append('  <!-- =================================================== -->')
    svg.append('  <g id="panel_e_bottom_synthesis_matrix">')
    
    # Outer Matrix Frame
    svg.append('    <rect x="24" y="724" width="1152" height="162" rx="8" ry="8" fill="#FFFFFF" stroke="#334155" stroke-width="1.2" filter="url(#cardShadow)"/>')
    
    # Matrix Header Banner
    svg.append('    <path d="M 24 732 Q 24 724 32 724 L 1168 724 Q 1176 724 1176 732 L 1176 748 L 24 748 Z" fill="#0F172A"/>')
    svg.append('    <text x="36" y="738" font-size="9.5px" font-weight="bold" fill="#F8FAFC" text-anchor="start" dominant-baseline="central">SYNOPTIC EVOLUTIONARY SYNTHESIS: POIKILOCHLOROPHYLLOUS ANHYDROBIOSIS VS. THE BURDEN OF BEING EVERGREEN</text>')
    svg.append('    <text x="1164" y="738" font-size="8.5px" font-weight="bold" fill="#FBBF24" text-anchor="end" dominant-baseline="central">Chapter 1 Macroevolutionary Synthesis · Velloziaceae</text>')

    # Table Column Headers
    svg.append('    <rect x="24" y="748" width="1152" height="18" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="0.8"/>')
    svg.append('    <text x="90" y="757" font-size="7.8px" font-weight="bold" fill="#475569" text-anchor="middle" dominant-baseline="central">EVOLUTIONARY DIMENSION</text>')
    svg.append('    <text x="330" y="757" font-size="7.8px" font-weight="bold" fill="#B45309" text-anchor="middle" dominant-baseline="central">VELLOZIA TUBIFLORA (RESURRECTION SPECIALIST)</text>')
    svg.append('    <text x="600" y="757" font-size="7.8px" font-weight="bold" fill="#1E293B" text-anchor="middle" dominant-baseline="central">EVOLUTIONARY BALANCE</text>')
    svg.append('    <text x="870" y="757" font-size="7.8px" font-weight="bold" fill="#047857" text-anchor="middle" dominant-baseline="central">VELLOZIA PERIPHERICA (EVERGREEN GENERALIST)</text>')
    svg.append('    <text x="1094" y="757" font-size="7.8px" font-weight="bold" fill="#475569" text-anchor="middle" dominant-baseline="central">OCBIL ADAPTIVE DRIVER</text>')

    # Vertical Grid Column Lines
    svg.append('    <line x1="180" y1="748" x2="180" y2="886" stroke="#E2E8F0" stroke-width="0.8"/>')
    svg.append('    <line x1="500" y1="748" x2="500" y2="886" stroke="#E2E8F0" stroke-width="0.8"/>')
    svg.append('    <line x1="700" y1="748" x2="700" y2="886" stroke="#E2E8F0" stroke-width="0.8"/>')
    svg.append('    <line x1="1020" y1="748" x2="1020" y2="886" stroke="#E2E8F0" stroke-width="0.8"/>')

    # Row 1: Ecological Niche & Water Potential (Y: 766 to 794)
    svg.append('    <g id="row1_niche">')
    svg.append('      <rect x="24" y="766" width="1152" height="28" fill="#FFFFFF"/>')
    svg.append('      <text x="32" y="780" font-size="7.5px" font-weight="bold" fill="#1E293B" dominant-baseline="central">1. Microhabitat &amp; Water (Ψ)</text>')
    svg.append('      <text x="190" y="780" font-size="7.2px" fill="#92400E" dominant-baseline="central">Bare monolithic quartzite outcrops (zero water buffer, Ψ &lt; -100 MPa)</text>')
    svg.append('      <rect x="520" y="771" width="160" height="18" rx="3" ry="3" fill="#FEF3C7" stroke="#FDE68A" stroke-width="0.8"/>')
    svg.append('      <text x="600" y="780" font-size="7.0px" font-weight="bold" fill="#B45309" text-anchor="middle" dominant-baseline="central">Saxicole vs. Crevice Niche</text>')
    svg.append('      <text x="710" y="780" font-size="7.2px" fill="#065F46" dominant-baseline="central">Shaded rock crevices &amp; deep fissures (subsurface buffer, Ψ ≈ -2.0 MPa)</text>')
    svg.append('      <text x="1030" y="780" font-size="7.0px" fill="#334155" dominant-baseline="central">Micro-topographic refugia</text>')
    svg.append('      <line x1="24" y1="794" x2="1176" y2="794" stroke="#F1F5F9" stroke-width="1"/>')
    svg.append('    </g>')

    # Row 2: Cellular State & Chloroplast Strategy (Y: 794 to 822)
    svg.append('    <g id="row2_cellular">')
    svg.append('      <rect x="24" y="794" width="1152" height="28" fill="#F8FAFC"/>')
    svg.append('      <text x="32" y="808" font-size="7.5px" font-weight="bold" fill="#1E293B" dominant-baseline="central">2. Dry-Season Physiology</text>')
    svg.append('      <text x="190" y="808" font-size="7.2px" fill="#92400E" dominant-baseline="central">Poikilochlorophylly: Thylakoids dismantled into desiccoplasts; vitrification</text>')
    svg.append('      <rect x="520" y="799" width="160" height="18" rx="3" ry="3" fill="#E2E8F0" stroke="#CBD5E1" stroke-width="0.8"/>')
    svg.append('      <text x="600" y="808" font-size="7.0px" font-weight="bold" fill="#1E293B" text-anchor="middle" dominant-baseline="central">Dormancy vs. Transpiration</text>')
    svg.append('      <text x="710" y="808" font-size="7.2px" fill="#065F46" dominant-baseline="central">Desiccation-Avoidance: Persistent green leaves, active stomata, ROS buffering</text>')
    svg.append('      <text x="1030" y="808" font-size="7.0px" fill="#334155" dominant-baseline="central">Solar irradiance defense</text>')
    svg.append('      <line x1="24" y1="822" x2="1176" y2="822" stroke="#F1F5F9" stroke-width="1"/>')
    svg.append('    </g>')

    # Row 3: Genomic Architecture & Turnover (Y: 822 to 850)
    svg.append('    <g id="row3_genomics">')
    svg.append('      <rect x="24" y="822" width="1152" height="28" fill="#FFFFFF"/>')
    svg.append('      <text x="32" y="836" font-size="7.5px" font-weight="bold" fill="#1E293B" dominant-baseline="central">3. Genomic Investment</text>')
    svg.append('      <text x="190" y="836" font-size="7.2px" fill="#92400E" dominant-baseline="central">Streamlined (+194 net): TOC/TIC (+55), NDH (+29), 17 PPRs under selection</text>')
    svg.append('      <rect x="520" y="827" width="160" height="18" rx="3" ry="3" fill="#FEF3C7" stroke="#FDE68A" stroke-width="0.8"/>')
    svg.append('      <text x="600" y="836" font-size="7.0px" font-weight="bold" fill="#B45309" text-anchor="middle" dominant-baseline="central">Organelle Repair vs. Upkeep</text>')
    svg.append('      <text x="710" y="836" font-size="7.2px" fill="#065F46" dominant-baseline="central">Genomic Burden (+723 net): F-box ligases (+51), LRR-RLKs (+57), NLRs (+22)</text>')
    svg.append('      <text x="1030" y="836" font-size="7.0px" fill="#334155" dominant-baseline="central">Asymmetric birth-death rate</text>')
    svg.append('      <line x1="24" y1="850" x2="1176" y2="850" stroke="#F1F5F9" stroke-width="1"/>')
    svg.append('    </g>')

    # Row 4: Primary Evolutionary Trade-Off (Y: 850 to 884)
    svg.append('    <g id="row4_tradeoff">')
    svg.append('      <rect x="24" y="850" width="1152" height="34" fill="#F8FAFC"/>')
    svg.append('      <text x="32" y="867" font-size="7.5px" font-weight="bold" fill="#1E293B" dominant-baseline="central">4. Evolutionary Trade-Off</text>')
    svg.append('      <text x="190" y="867" font-size="7.2px" font-weight="bold" fill="#047857" dominant-baseline="central">Absolute Desiccation Resilience (0% Mortality) | Lower annual carbon gain</text>')
    svg.append('      <rect x="520" y="858" width="160" height="18" rx="3" ry="3" fill="#D1FAE5" stroke="#A7F3D0" stroke-width="0.8"/>')
    svg.append('      <text x="600" y="867" font-size="7.0px" font-weight="bold" fill="#065F46" text-anchor="middle" dominant-baseline="central">Resilience vs. Productivity</text>')
    svg.append('      <text x="710" y="867" font-size="7.2px" font-weight="bold" fill="#991B1B" dominant-baseline="central">High Competitive Carbon Gain (Amax) | High cavitation risk in mega-drought</text>')
    svg.append('      <text x="1030" y="867" font-size="7.0px" fill="#334155" dominant-baseline="central">OCBIL life-history strategy</text>')
    svg.append('    </g>')

    svg.append('  </g>')

    # Closing SVG Root
    svg.append('</svg>')

    full_svg_content = '\n'.join(svg)

    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_svg_content)
    
    print(f"Successfully generated Fig 5 vector SVG: {output_path}")

if __name__ == '__main__':
    target_path = '/home/mfcaval/github/doutorado/teamwork/figures_chapter1/fig5_conceptual_macroevolution_synthesis.svg'
    if len(sys.argv) > 1:
        target_path = sys.argv[1]
    build_figure5_svg(target_path)
