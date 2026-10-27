# Project: Chapter 1 Scientific Figures Suite, Scripts & Bilingual Legends
**Thesis:** Macroevolution and Genomic Divergence in Velloziaceae: from Deep Time to Contrasting Survival Strategies  
**Target Directory:** `teamwork/figures_chapter1/`  
**Scripts Directory:** `teamwork/figures_chapter1/scripts/`  
**Legends File:** `teamwork/figures_chapter1/figure_legends.md`  

---

## Architecture

The figure suite consists of 5 publication-grade vector figures (pure editable SVG), standalone Python generation scripts (`matplotlib`/`drawsvg`/`svgwrite`/`pure svg builder`), and a complete bilingual figure legend document (English publication style + Portuguese ABNT style).

```
teamwork/figures_chapter1/
├── fig1_dating_chronogram_biogeography.svg
├── fig2_orthology_macrosynteny.svg
├── fig3_gene_family_cafe5_turnover.svg
├── fig4_selection_landscape_ppr.svg
├── fig5_conceptual_macroevolution_synthesis.svg
├── figure_legends.md
└── scripts/
    ├── generate_fig1.py
    ├── generate_fig2.py
    ├── generate_fig3.py
    ├── generate_fig4.py
    ├── generate_fig5.py
    ├── generate_figure_legends.py
    └── test_figures_e2e.py
```

### Visual and Technical Standards:
1. **Format:** Pure, valid, editable vector SVG (no raster embedding, no outline-converted fonts).
2. **Semantic Grouping:** Deep hierarchical `<g id="...">` tagging (e.g. `<g id="panel_a_chronogram">`, `<g id="error_bars">`, `<g id="labels">`, etc.).
3. **Typography:** Standard sans-serif fonts (`Arial, Helvetica, DejaVu Sans, sans-serif`), explicit `font-size`, `text-anchor`, and `dominant-baseline`.
4. **Color Palettes:** Calibrated Okabe-Ito and Viridis/Mako palettes (accessible, colorblind-safe, distinct fills and strokes).
5. **Dimensions:** Full-page / 1.5-column width (175mm / ~700–1200px viewBox), crisp scaling at 300+ DPI.
6. **Empirical Precision:** 100% empirical precision with `chapter_macroevolution/` data tables.

---

## Feature Inventory

| # | Feature | Description | Milestone | Source | Status |
|---|---------|-------------|-----------|--------|--------|
| 1 | Fig 1A: Chronogram Tree | 7-species MCMCtree chronogram, 95% HPD bars, 5 fossil anchors, node ages (138.48, 121.90, 101.26, 78.21, 31.92, 9.74 Ma) | M1 | `03_dating/mcmctree_node_ages_summary.tsv` | DONE |
| 2 | Fig 1B: Paleogeography Map | Mid-Cenozoic trans-Atlantic LDD (31.92 Ma) vs. Cretaceous Gondwana vicariance refutation map | M1 | `03_dating/`, survey report | DONE |
| 3 | Fig 2A: Orthology Partition | OrthoFinder v3 7-species breakdown: 17,750 orthogroups, 1,513 single-copy core, shared vs species-specific | M2 | `01_orthology/` | DONE |
| 4 | Fig 2B: Macrosynteny Ribbons | 9-chromosome macrosynteny ribbon / dual-track map (297 collinear blocks, 2n=18, 0 translocations, OSCA callouts) | M2 | `01_orthology/`, survey report | DONE |
| 5 | Fig 3A: CAFE5 Species Tree | Dated tree with branch net gains/losses (+/-) under Gamma model (lambda = 0.638) | M3 | `04_gene_families/cafe5_results/` | DONE |
| 6 | Fig 3B: Expansion Barplots | Lineage expansions: Vtub (+55 TOC/TIC, +29 NDH, LEA) vs Vper (+57/+29/+25 LRR-RLK, +22/+17 NB-LRR) | M3 | `04_gene_families/` | DONE |
| 7 | Fig 4A: Ka/Ks Omega Distribution | Genome-wide Ka/Ks on 1,513 orthologs (722 purifying, 541 neutral, 250 positive candidates omega > 1.0) | M4 | `05_selection/positive_selection_candidates_top250.tsv` | DONE |
| 8 | Fig 4B: PPR RNA-Editing Diagram | Structural PPR domain + DYW deaminase C-to-U editing mechanism during desiccoplast disassembly/reassembly | M4 | `05_selection/`, master draft | DONE |
| 9 | Fig 5: Conceptual Synthesis | Multi-tier macroevolutionary model contrasting Resurrection (Vtub) vs Evergreen (Vper) in campos rupestres | M5 | Master draft, survey report | DONE |
| 10| Python Generation Scripts | Modular reproducible scripts (`generate_fig1.py` - `generate_fig5.py`, `generate_figure_legends.py`) | M6 | Survey specs | DONE |
| 11| Bilingual Figure Legends | Exhaustive, publication-grade bilingual legends (English publication + Portuguese ABNT) in `figure_legends.md` | M6 | Master draft, survey specs | DONE |
| 12| E2E Verification & Test Suite | Automated test harness checking XML validity, viewBox, text objects, color palettes, empirical consistency | E2E | Quality Verification | DONE |

---

## Milestones

| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Fig 1: Molecular Dating & Biogeography | `fig1_dating_chronogram_biogeography.svg` (Panels A & B) | none | DONE |
| M2 | Fig 2: Orthology & Macrosynteny | `fig2_orthology_macrosynteny.svg` (Panels A & B) | none | DONE |
| M3 | Fig 3: CAFE5 Gene Family Dynamics | `fig3_gene_family_cafe5_turnover.svg` (Panels A & B) | none | DONE |
| M4 | Fig 4: Selection & PPR RNA Editing | `fig4_selection_landscape_ppr.svg` (Panels A & B) | none | DONE |
| M5 | Fig 5: Conceptual Macroevolution Synthesis | `fig5_conceptual_macroevolution_synthesis.svg` | none | DONE |
| M6 | Python Scripts & Bilingual Legends | `scripts/generate_fig1.py`..`generate_fig5.py` & `figure_legends.md` | M1, M2, M3, M4, M5 | DONE |
| E2E | E2E Testing & Adversarial Audit | `TEST_INFRA.md`, `test_figures_e2e.py`, XML/Data validation | M1..M6 | DONE |
