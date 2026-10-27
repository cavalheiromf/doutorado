# CAFE5 M5+Gamma Review Recalculation Implementation Plan

**Goal:** Make the reproduced M5+Gamma optimum the single source of truth for the macroevolution review, propagate it through gene-family, duplication, enrichment, table, figure, and manuscript outputs, and document sensitivity across equivalent runs.

**Architecture:** The CAFE5 evaluator will select the best completed M5+Gamma replicate and emit a convergence table. The master gene-family table will use that run for primary branch calls and the near-optimal runs for robustness flags. All publication outputs will read calculated tables rather than hard-coded values.

**Tech Stack:** Python 3 (pandas, numpy, matplotlib/seaborn), CAFE5 text outputs, Bash/SLURM, Markdown, unittest.

**Scope constraint:** Only files inside `chapter_macroevolution_review` plus this implementation plan are edited. No commits are created because the review tree is currently untracked amid unrelated user work.

---

### Task 1: Record convergence and select the primary M5+Gamma run

**Files:**
- Modify: `chapter_macroevolution_review/workflow/tests/test_cafe5_model_evaluation.py`
- Modify: `chapter_macroevolution_review/workflow/scripts/01_cafe5/05_evaluate_cafe5_models.py`
- Generate: `chapter_macroevolution_review/04_gene_families/cafe5/summary/M5_gamma_convergence_summary.tsv`

- [x] Add a failing synthetic test requiring the evaluator to calculate `delta_neg_lnL`, identify near-optimal M5 runs at a 0.1 threshold, parse four lambda values, and calculate `Vper_to_Vtub_ratio`.
- [x] Add pure evaluator functions for parsing lambda vectors and summarizing M5 replicates.
- [x] Export the convergence summary while preserving the existing model-comparison table.
- [x] Run `python -m unittest chapter_macroevolution_review/workflow/tests/test_cafe5_model_evaluation.py` and verify all tests pass.

### Task 2: Propagate primary and robust branch calls into the master table

**Files:**
- Create: `chapter_macroevolution_review/workflow/tests/test_cafe5_master_table.py`
- Modify: `chapter_macroevolution_review/workflow/scripts/03_functional_enrichment/00_build_master_table_6taxa.py`
- Regenerate: `chapter_macroevolution_review/04_gene_families/functional_enrichment/input/data/family_annotation_master_6taxa.tsv`

- [x] Add tests for resolving the selected M5 replicate from the comparison table and for computing intersection-based robust branch calls.
- [x] Resolve the lowest-likelihood M5 replicate dynamically and load its `Gamma_change` and branch-probability tables.
- [x] Add replicate-specific branch-significance columns for the near-optimal runs and `Robust` intersection columns; retain the selected run under the existing primary column names.
- [x] Record model, replicate, and sensitivity-run provenance in output columns and reports.
- [x] Rebuild the master table and validate expected primary counts (including Vper 217 expansions/66 contractions and Vtub 50/63).

### Task 3: Recalculate duplication and functional-enrichment outputs

**Files:**
- Modify: `chapter_macroevolution_review/04_gene_families/functional_enrichment/input/config/enrichment_config.yaml`
- Modify: `chapter_macroevolution_review/workflow/scripts/03_functional_enrichment/06_generate_summary_report.py`
- Modify: `chapter_macroevolution_review/workflow/scripts/03_functional_enrichment/09_run_enrichment_pipeline.sh`
- Regenerate outputs under: `chapter_macroevolution_review/04_gene_families/synteny/` and `chapter_macroevolution_review/04_gene_families/functional_enrichment/`

- [x] Remove stale sample sizes from contrast descriptions and derive displayed sizes from current data.
- [x] Remove the obsolete `teste` reservation and retain the `short` partition configuration.
- [x] Run duplication extraction against the selected M5+Gamma run.
- [x] Run the enrichment pipeline from the rebuilt master table and validate that provenance and reduced plotting tables are complete.

### Task 4: Replace hard-coded publication tables and figures

**Files:**
- Create: `chapter_macroevolution_review/workflow/tests/test_manuscript_exports.py`
- Modify: `chapter_macroevolution_review/workflow/scripts/04_manuscript/01_export_manuscript_tables.py`
- Modify: `chapter_macroevolution_review/workflow/scripts/04_manuscript/02_plot_manuscript_figures.py`
- Regenerate: `chapter_macroevolution_review/04_manuscript/tables/*.tsv`
- Regenerate: `chapter_macroevolution_review/04_manuscript/figures/*.{png,pdf}`

- [x] Add tests showing that branch-event rows and duplication-mode rows are derived from synthetic current inputs.
- [x] Build Table 2 from branch changes and selected-run significance calls.
- [x] Build Table 3 from the actual gene-level categories (`WGD/Segmental`, `Tandem`, `Proximal`, `Dispersed`, `Singleton`), eliminating the incorrect `Transposed` label.
- [x] Make Figures 1–3 consume current exported tables and enrichment results instead of embedded historical values.
- [x] Regenerate all tables/figures, inspect the PNGs visually, and verify PDF counterparts exist.

### Task 5: Revise manuscript and review documentation

**Files:**
- Modify: `chapter_macroevolution_review/docs/manuscripts/chapter_macroevolution_article.md`
- Modify: `chapter_macroevolution_review/README.md`

- [x] Update Methods with the M2–M5 Gamma model comparison, ten M5 starts, selected replicate, near-optimal sensitivity runs, and boundary treatment.
- [x] Update Abstract, Results, Discussion, and Conclusion using recalculated rates, counts, ranges, duplication modes, and enrichment results.
- [x] Distinguish inferential claims supported by the selected run from claims stable across near-optimal runs.
- [x] Update README summaries and paths so they match the regenerated artifacts.

### Task 6: End-to-end validation

**Files:**
- Inspect all modified and regenerated files above.

- [x] Run the complete review test suite.
- [x] Search active sources and manuscript outputs for stale key values (`5.6`, `0.00879`, `265`, and `Transposed`) and review every remaining occurrence.
- [x] Validate row counts, unique family IDs, numeric ranges, and agreement between manuscript statements, tables, and figures.
- [x] Render or preview the manuscript using the repository's available workflow and report any limitation that remains.
