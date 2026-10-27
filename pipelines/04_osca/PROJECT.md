# Project: Genome-Wide Identification, Comparative Synteny, and Evolutionary Divergence of OSCA Mechanosensitive Ion Channels in Resurrection and Evergreen Vellozia

> **Post-audit notice (2026-09-15):** Numerical checkpoints in this planning file have been superseded by `audits/relatorio_auditoria_capitulo2.md` and the reproducible tables in `teamwork/reviews/`. In particular, universal 10-TMH/tripartite architecture, 12 strict 1:1 orthologs, the earlier RELAX values, and 17 Contrast-FEL sites were not retained after primary-output review.

## Architecture
- **Document Domain:** Doctoral Dissertation Chapter 2 / High-Impact Scientific Manuscript.
- **Methodological Framework:** Gilson Volpato's Logical Scientific Writing Method; Strict ABNT Standards (NBR 6028, NBR 10520, NBR 6023).
- **Empirical Pipeline Modules:**
  - `01_gene_identification`: HMMER profile search (PF02714, PF13967, PF14703), DeepTMHMM, InterProScan.
  - `02_phylogeny`: MAFFT alignment, trimAl, IQ-TREE 2 ML phylogeny (76 angiosperm proteins, 4 monophyletic clades).
  - `03_synteny`: MCScan macrosynteny (12 1:1 orthologs), Chr7A ancestral cluster, Chr1A lineage-specific tandem duplication; HyPhy RELAX ($K$) and Contrast-FEL (17 candidate sites).
  - `04_evolutionary_rates`: PAL2NAL v14 + PAML v4.9j `yn00` pairwise codon rates ($\omega = Ka/Ks$, mean $\omega = 0.4082$).
  - `05_rnaseq` & `06_expression`: STAR alignment, featureCounts, DESeq2 spatial tissue profiling (9 Vper, 8 Vtub libraries; VT1R excluded).
  - `07_ppi_network`: STRING v12.0 PPI interactome (61 nodes / 187 edges in Vper; 60 nodes / 217 edges in Vtub; hubs OSCA1.2, OSCA4.1, OSCA1.1).
  - `08_structural`: AlphaFold/RMSD modeling (strictly relegated to Discussion § 4.5 Future Perspectives).
  - `figures/`: Publication-ready 300 DPI vector/raster figures (Figures 1–4).
  - `manuscript/`: Main text (`chapter_2_osca_mechanosensation.md`) and supplementary data (`supplementary_tables.md`).

## Feature Inventory
Every feature from the Survey phase is mapped to an assigned milestone:

| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Gene Catalog Ground Truth | 14 Vper, 13 Vtub OSCA genes; 10 TMHs in all 27 subunits; PF02714/PF13967/PF14703 intact | M2 | survey_spec_report.md § 2 |
| 2 | Interspecific Macrosynteny | 12 1:1 orthologous blocks across 6 chromosome pairs | M2 | survey_spec_report.md § 2 |
| 3 | Ancestral Tandem Cluster Chr7A | OSCA1.3/1.4/1.5 flanked by 24 collinear orthologs spanning 35 kb | M2 | survey_spec_report.md § 2 |
| 4 | Lineage-Specific Duplication Chr1A | VpOSCA2.4a/b (1.3 kb spacer, $\omega = 0.3770$) in Vper vs single VtOSCA2.4 | M2 | survey_spec_report.md § 2 |
| 5 | Paleoduplication Exclusion | Segregation and exclusion of Chr1A<->Chr5A ancestral WGD from Chapter 2 figures/text | M1, M2 | ORIGINAL_REQUEST § R2 |
| 6 | Selection Rates Reconciliation | Pairwise $\omega = Ka/Ks$ synchronization across Table 3, Table S3, and Figure 3B (mean $\omega = 0.4082$) | M1, M2 | assets_references_report.md § 3.3 |
| 7 | HyPhy RELAX Empirical Metrics | Global $K = 0.7988$ ($p = 0.0039$); OSCA1 $K = 0.9317$; OSCA2 $K = 0.8255$; OSCA3+4 $K = 0.2459$ ($p = 0.0041$) | M2 | survey_spec_report.md § 4.3 |
| 8 | HyPhy Contrast-FEL Sites | 17 nominal divergent sites (11 in OSCA2, 5 in OSCA1, 1 in OSCA3+4); 0 pass FDR $q \le 0.20$ (exploratory candidates) | M2 | survey_spec_report.md § 4.3 |
| 9 | RNA-seq Tissue Profiling | 9 Vper, 8 Vtub libraries (VT1R excluded); basal tissue expression; OSCA1.2 root/stem-enriched, OSCA1.1 & 3.1 leaf-enriched | M2 | survey_spec_report.md § 4.4 |
| 10 | STRING Interactome Topology | 61/187 (Vper), 60/217 (Vtub); hubs OSCA1.2, OSCA4.1, OSCA1.1; evidence channel breakdown (~71% text mining) | M2 | survey_spec_report.md § 4.5 |
| 11 | Figure 4 English Translation | Refactor `plot_figure_4_osca_expression_ppi.py` to translate all titles, axis labels, tissue headers, and legends into English | M1 | assets_references_report.md § 3.4 |
| 12 | Figure 3 Typo & Legend Patch | Fix typo ("Sits" -> "Sites") in `plot_figure_3_osca_selection.py` and coordinate alignment | M1 | assets_references_report.md § 3.3 |
| 13 | Figure 1 Length Array Sync | Synchronize `TABLE1_DATA` in `plot_figure_1_osca_phylogeny.py` with Table 1 (VpOSCA4.1 804 aa) | M1 | assets_references_report.md § 3.1 |
| 14 | Supplementary Table Callouts | Integrate explicit callouts for Tables S1, S2, S3, and S4 in Sections 3.1, 3.2, 3.3, and 3.4 | M2 | assets_references_report.md § 4 |
| 15 | Volpato Argument 1 Refactor | Transform Introduction into unbroken prose ending with explicit Operational Objective (zero rhetorical questions) | M2 | manuscript_architecture_report.md § 2 |
| 16 | Volpato Argument 2 Symmetry | Excise orphan PlantCARE Section 2.5; maintain pure descriptive Results; harmonize M&M and Results | M2 | manuscript_architecture_report.md § 3.1 |
| 17 | Unbroken Prose Enforcement | Eliminate all 8 bullet/numbered list structures across Intro, Results, Discussion, and Conclusions | M2 | manuscript_architecture_report.md § 4 |
| 18 | Dual-Track Model Articulation | Formulate Dual-Track Evolutionary Model in Discussion reconciling anhydrobiosis vs evergreen arborescence | M2 | manuscript_architecture_report.md § 3.3 |
| 19 | Perception vs Response Boundary | Inflexible separation between primary sensory gating ($\text{Ca}^{2+}$ influx) and downstream responses (ABA, stomata, wall folding) | M2 | manuscript_architecture_report.md § 5 |
| 20 | Volpato Conclusions Refactor | Rewrite Conclusions as a synthesized theoretical resolution answering the Operational Objective (zero bullet points) | M2 | manuscript_architecture_report.md § 3.4 |
| 21 | Structured Abstract & Keywords | Implement ~250-word structured Abstract (Background, Objective, Methods, Results, Conclusion) and period-delimited ABNT keywords | M2 | manuscript_architecture_report.md § 6 |
| 22 | ABNT Reference Rectification | Rectify hallucinated citations (Alcantara 2015, Teodoro 2021), add Yang & Nielsen (2000), format with bold journals, unbulleted | M2 | assets_references_report.md § 5 |
| 23 | Comprehensive Multi-Agent Audit | Reviewers, Challenger, and Forensic Auditor verification gate | M3 | ORIGINAL_REQUEST § Team Roles |

## Milestones

| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Visual & Empirical Asset Harmonization | Patch Python figure scripts (Fig 4 English translation, Fig 3 typo fix, Fig 1 length sync), re-render figures, and synchronize `manuscript/supplementary_tables.md` rates to match `aggregated_kaks_pal2nal_yn00.csv` | none | DONE |
| M2 | Manuscript Comprehensive Refactoring | Full refactoring of `manuscript/chapter_2_osca_mechanosensation.md` (Volpato Argument 1 & 2, unbroken prose, zero bullets, ABNT citations, callouts to Figures 1–4 and Tables S1–S4, Dual-Track Model, structured Abstract) | M1 | DONE |
| M3 | Multi-Agent Review, Adversarial Challenge & Forensic Integrity Audit | Independent verification gate by Reviewers, Challenger empirical testing, and Forensic Auditor zero-hallucination validation | M2 | DONE |

## Interface Contracts
### Figure Scripts ↔ Visual Assets
- Input: `figures/scripts/plot_figure_*.py`
- Output: `figures/Figure_*.pdf` and `figures/Figure_*.png` (300 DPI, publication quality).
- Constraint: Figure 4 must be 100% in English matching Figures 1, 2, and 3.

### Supplementary Tables ↔ Main Manuscript
- `Supplementary Table S1`: Referenced in § 3.1 alongside Table 1.
- `Supplementary Table S2`: Referenced in § 3.2 alongside Table 2.
- `Supplementary Table S3`: Referenced in § 3.3 alongside Table 3 (rates synchronized with `aggregated_kaks_pal2nal_yn00.csv`, mean $\omega = 0.4082$).
- `Supplementary Table S4`: Referenced in § 3.4 (supplying quantitative DESeq2 and STRING values).

### Text Narrative ↔ Ground Truth
- Strictly zero bullet points in narrative text (§ 1 to § 5).
- Introduction ends with explicit Operational Objective (no rhetorical questions).
- Pure descriptive Results (zero external citations, zero speculation).
- Conclusions answer the Operational Objective theoretically (no numbered results recap).

## Code Layout
- Main Manuscript: `/home/mfcaval/github/doutorado/chapter2_osca/manuscript/chapter_2_osca_mechanosensation.md`
- Supplementary Tables: `/home/mfcaval/github/doutorado/chapter2_osca/manuscript/supplementary_tables.md`
- Figures Directory: `/home/mfcaval/github/doutorado/chapter2_osca/figures/`
- Figure Generator Scripts: `/home/mfcaval/github/doutorado/chapter2_osca/figures/scripts/`
- Ground Truth Audit: `/home/mfcaval/github/doutorado/chapter2_osca/audits/relatorio_auditoria_capitulo2.md`
- Pal2nal YN00 Ground Truth Rates: `/home/mfcaval/github/doutorado/chapter2_osca/04_evolutionary_rates/results_pal2nal_yn00/aggregated_kaks_pal2nal_yn00.csv`
- Coordination Metadata: `/home/mfcaval/github/doutorado/chapter2_osca/.agents/`
