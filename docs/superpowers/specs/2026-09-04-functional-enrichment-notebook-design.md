# Functional enrichment interpretation notebook design

## Objective

Update `interpretando_resultados_enriquecimento.ipynb` so that every table,
figure, and biological statement follows the final enrichment pipeline rather
than the older local-FDR-only workflow.

## Analytical decisions

- Use `FDR_primary_global <= 0.05` and `Reportable == TRUE` as the primary
  confirmatory rule.
- Retain local and stratified FDR summaries as explicitly labeled sensitivity
  views.
- Use final TSV tables as the source of inferential decisions. RDS
  `enrichResult` objects are used only for plotting IDs already approved by the
  TSV criteria.
- Describe contractions as directional and expansions as strict.
- Treat lineage co-detection as descriptive. State explicitly that no Vtub vs
  Xvis term survives `FDR_difference <= 0.05`.
- Distinguish absence from non-significance or failure to meet `k >= 3`.
- Include Objective 5 only after applying `Reportable == TRUE` when constructing
  its summary inside the notebook.

## Notebook structure

1. Scope, analytical rules, and limitations.
2. Reproducible setup and input validation.
3. Global QC summary across primary contrasts.
4. Objective 1 tables and effect-size forest plot.
5. Objective 2 individual ORAs and direct Vtub-Xvis comparison.
6. Objective 3 tables and effect-size forest plot.
7. Objective 4 descriptive three-lineage patterns with below-threshold counts
   recovered from the complete primary table.
8. Objective 5 tier sensitivity filtered by `Reportable`.
9. Session and package provenance.

## Validation

- Parse and execute all code cells from a clean R environment.
- Assert required files and columns.
- Confirm that all primary plotted rows are reportable and globally
  significant.
- Confirm that the direct comparison reports zero FDR-significant differences.
- Validate notebook JSON and save executed outputs.

