# Functional Enrichment Notebook Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the outdated interpretation notebook with an executable, publication-oriented notebook aligned with enrichment pipeline v2.2.

**Architecture:** The notebook reads the complete and reportable TSV outputs as the statistical source of truth, uses RDS objects only for optional clusterProfiler plots, and separates confirmatory conclusions from descriptive or exploratory summaries. Reusable R helpers centralize validation, filtering, and forest plotting.

**Tech Stack:** Jupyter Notebook 4.5, R 4.5.1, clusterProfiler 4.18.4, enrichplot, dplyr, tidyr, readr, ggplot2.

## Global Constraints

- Primary criterion: `Reportable == TRUE` and `FDR_primary_global <= 0.05`.
- Direct lineage difference: `FDR_difference <= 0.05`.
- Do not interpret missing reportable rows as biological absence.
- Do not call co-detection convergence.
- Preserve the original results files.

---

### Task 1: Rebuild notebook narrative and setup

**Files:**
- Modify: `chapter_macroevolution/04_gene_families/functional_enrichment/interpretando_resultados_enriquecimento.ipynb`

**Interfaces:**
- Consumes: result TSV/RDS files under `results_5_objectives`.
- Produces: validated data frames, `primary_sig()`, `make_forest_plot()`, and notebook provenance output.

- [ ] **Step 1: Add validation expectations**

Validate file existence and required columns before any interpretation.

- [ ] **Step 2: Replace the setup and outdated method description**

Declare `PRIMARY_FDR <- "FDR_primary_global"`, `ALPHA <- 0.05`, and describe strict expansions versus directional contractions.

- [ ] **Step 3: Execute setup checks**

Run all code cells and expect no missing-file or missing-column errors.

### Task 2: Align Objectives 1-4 with final inference

**Files:**
- Modify: `chapter_macroevolution/04_gene_families/functional_enrichment/interpretando_resultados_enriquecimento.ipynb`

**Interfaces:**
- Consumes: helpers and validated tables from Task 1.
- Produces: globally corrected tables, forest plots, direct-comparison conclusion, and descriptive three-lineage matrix.

- [ ] **Step 1: Replace RDS-only significance filtering**

Filter TSV rows by `Reportable` and `FDR_primary_global`; build effect-size plots from OR and CI95%.

- [ ] **Step 2: Correct direct-comparison wording**

Print nominal rows as exploratory and state that zero terms survive BH when that assertion holds.

- [ ] **Step 3: Recover below-threshold lineage counts**

Join Objective 4 reportable patterns to the complete primary table so `NA` is not described as absence.

- [ ] **Step 4: Execute and inspect outputs**

Expect all plotted rows to satisfy the primary rule and `FDR_difference` to have zero values at or below 0.05.

### Task 3: Add Objective 5 and reproducibility

**Files:**
- Modify: `chapter_macroevolution/04_gene_families/functional_enrichment/interpretando_resultados_enriquecimento.ipynb`

**Interfaces:**
- Consumes: Objective 5 all-results table and session packages.
- Produces: reportable tier-stability summary and environment record.

- [ ] **Step 1: Recalculate the tier summary with `Reportable`**

Use only `Reportable == TRUE` and `FDR_local <= 0.05` when summarizing nested tiers.

- [ ] **Step 2: Add provenance**

Print input modification times, package versions, R version, and `sessionInfo()`.

- [ ] **Step 3: Validate notebook JSON and execute all cells**

Expected: valid notebook JSON, all code cells complete without errors, and stored outputs in the notebook.

