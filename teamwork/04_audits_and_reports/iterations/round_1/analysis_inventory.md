# Analysis Inventory — Unified Chapter 1, Round 1

## Inspection scope and evidence policy

This inventory is a read-only inspection of:

- `analyses/chapter_1_genomics/`
- `chapter3/`
- `teamwork/chapter_1_comparative_genomics_abnt.md`
- `teamwork/chapter_macroevolution_velloziaceae_abnt.md`

No new biological analysis was run. Simple file enumeration and direct counting of rows already classified by the producing software were used only to verify the contents of existing outputs. Assembly, sequencing, and structural/functional annotation are treated as Appendix material. OSCA-specific content is excluded from Chapter 1 and reserved for Chapter 2.

Evidence labels used below:

- **OBSERVED**: directly present in an inspected output.
- **SUPPORTED INTERPRETATION**: conservative interpretation of an observed output.
- **UNTESTED INFERENCE**: biologically possible, but not demonstrated by the inspected outputs.
- **UNSUPPORTED/MISMATCHED**: contradicted by, or absent from, the inspected outputs.

## Executive evidence gate

The usable analytical backbone consists of two completed OrthoFinder runs and two sets of CAFE5 outputs. The pairwise three-proteome OrthoFinder run and seven-proteome OrthoFinder run are internally traceable. The CAFE5 runs are numerically inspectable but require strong qualifications. The three-species draft contains extensive numerical results not matching the current OrthoFinder outputs, and its enrichment table does not match the only enrichment output found. The macroevolutionary draft misidentifies CAFE5 node 13 and consequently makes an unsupported ancestral-state claim.

The following source-draft components must not be carried into the unified manuscript as empirical results:

1. synteny results (297 blocks, zero translocations, Chr1A–Chr5A paleoduplication), because the inspected synteny directory contains only four input symlinks and no result files;
2. all Ka/Ks values and functional-category summaries, because no selection-analysis outputs are present in either inspected analysis tree;
3. claims that node 13 represents the *Xerophyta* + *Vellozia* ancestor or demonstrates a Gondwanan origin of desiccation tolerance, because node 13 is explicitly the *V. peripherica* + *V. tubiflora* ancestor;
4. claims of absolute bootstrap support, formal molecular dating, ancestral-state reconstruction, secondary loss of desiccation tolerance, or adaptive mechanisms inferred solely from copy-number change;
5. the enrichment numbers in Tables 2–3 of the pairwise draft, because they do not occur in the available `functional_enrichment_results.tsv`.

## 1. File inventory

### 1.1 Source manuscripts (inputs, not analytical evidence)

| File | Contents | Inspection note |
|---|---|---|
| `teamwork/chapter_1_comparative_genomics_abnt.md` | Pairwise *V. tubiflora*–*V. peripherica* manuscript with assembly, orthology, synteny, CAFE5, enrichment, and Ka/Ks claims | Numerous numerical conflicts with current outputs; synteny and Ka/Ks result files absent. |
| `teamwork/chapter_macroevolution_velloziaceae_abnt.md` | Seven-taxon macroevolutionary manuscript | Orthogroup totals match, but CAFE5 node interpretation and ancestral-trait conclusions do not. |

### 1.2 `analyses/chapter_1_genomics/`

| Module | Available files | Status and use |
|---|---|---|
| `01_synteny/` | `data/Vper.bed`, `Vper.cds`, `Vtub.bed`, `Vtub.cds`, all symlinks | Inputs only. No BLAST, collinearity, anchor, block, plot, or summary outputs. No synteny result is admissible. |
| `02_orthofinder/` | Three canonical proteome FASTAs; OrthoFinder v3.1.5 log; complete result tree with orthogroups, orthologues, species tree, duplication events, alignments, and gene trees | Completed and usable with the exact values below. |
| `03_cafe5/` | Input preparation script and table; two-tip ultrametric tree; CAFE5 base-model reports, changes, counts, likelihoods, family and branch probabilities; descriptive annotation/enrichment scripts and outputs | Completed numerically, but the tree has arbitrary unit branch lengths and only two terminal taxa. Lambda is per unit branch, not per million years. |
| `annotation_db/` | master TSV (52,017 records plus header), SQLite database, database-building/query scripts | Useful for gene/orthogroup lookup. A bug makes `ancestral_count` unreliable in the database/TSV; use `Base_count.tab` directly. |

### 1.3 `chapter3/`

| Module | Available files | Status and use |
|---|---|---|
| `01_species_data/` | Seven protein FASTAs: `Abra`, `Ath`, `Dala`, `Ptec`, `Vper`, `Vtub`, `Xvis` | Used by the completed OrthoFinder run. No provenance/checksum manifest validates all taxon identities or releases. |
| `02_orthofinder/` | OrthoFinder v3.1.5 logs and complete results for seven taxa | Completed and usable with qualifications below. |
| `03_phylogenomics/` | empty directory | No IQ-TREE, gene-tree concordance, ASTRAL/coalescent, bootstrap, or MCMCtree outputs. |
| `04_cafe5/` | full and filtered family tables; manually specified ultrametric tree; Base and Gamma model outputs | Completed, but calibration ages are assumptions encoded in the tree, not estimates generated by a dating analysis. Base/Gamma results are mixed by the existing summary script. |
| `05_selection_rates/` | empty directory | No HyPhy, RELAX, BUSTED, or PAML evidence. |
| `results/` | `Table_1_Pan_Velloziaceae_CAFE5_Summary.tsv` | This summary reports the Base model, not the Gamma model. |
| visual files | none | No chapter 3 figures are available. |

## 2. Evidence ledger: pairwise *Vellozia* analysis

### A-001 — Pairwise OrthoFinder configuration

- **OBSERVED:** OrthoFinder v3.1.5 ran on `Ath.canonical.pep.fa`, `Vper.pep.fa`, and `Vtub.pep.fa`, using DIAMOND, FAMSA, FastTree, BLOSUM62, gap extension 1, and gap opening 11.
- **Provenance:** `analyses/chapter_1_genomics/02_orthofinder/data/OrthoFinder/Results_Aug27_2/Log.txt`, lines 1–16.
- **Important draft conflict:** the source draft states OrthoFinder v2.5.5, DIAMOND v2.0.15, MCL inflation 1.5, DendroBLAST/STAG, and 96,809 input proteins. Those values are not the configuration/current input shown in the inspected log and statistics.

### A-002 — Pairwise orthogroup totals

- **OBSERVED:** 3 species; 69,772 genes; 64,380 genes in orthogroups (92.3%); 5,392 unassigned genes (7.7%); 16,953 orthogroups; 787 species-specific orthogroups containing 3,673 genes; 8,541 orthogroups containing all three species; 4,445 single-copy orthogroups; mean and median orthogroup sizes 3.8 and 3.0.
- **Provenance:** `analyses/chapter_1_genomics/02_orthofinder/data/OrthoFinder/Results_Aug27_2/Comparative_Genomics_Statistics/Statistics_Overall.tsv`, lines 1–18.
- **Draft conflict:** 96,809 genes, 90,293 assigned genes, 24,013 orthogroups, 11,048 universal orthogroups, 7,061 single-copy orthogroups, and 6,516 unassigned genes in the draft are not supported by the current output.

### A-003 — Pairwise per-species counts

- **OBSERVED:**

| Taxon/file | Input genes | Genes in orthogroups | Assigned (%) | Unassigned | Species-specific orthogroups | Genes in species-specific orthogroups |
|---|---:|---:|---:|---:|---:|---:|
| `Ath.canonical.pep` | 17,755 | 15,412 | 86.8 | 2,343 | 557 | 2,523 |
| `Vper.pep` | 26,466 | 25,015 | 94.5 | 1,451 | 123 | 641 |
| `Vtub.pep` | 25,551 | 23,953 | 93.7 | 1,598 | 107 | 509 |

- **Provenance:** `analyses/chapter_1_genomics/02_orthofinder/data/OrthoFinder/Results_Aug27_2/Comparative_Genomics_Statistics/Statistics_PerSpecies.tsv`, lines 1–11.
- **Draft conflict:** the predicted protein and assigned-gene counts in the draft (e.g., 34,449/34,705 proteins in Methods and 29,889/24,560 genes in Table 1) do not match the current OrthoFinder inputs.

### A-004 — Pairwise orthologue totals and species topology

- **OBSERVED:** the directional totals table contains 18,690 *V. peripherica*→*V. tubiflora* relationships and 17,752 *V. tubiflora*→*V. peripherica* relationships. These are directional gene counts reported by OrthoFinder, not necessarily 18,690 unique one-to-one pairs.
- **Provenance:** `analyses/chapter_1_genomics/02_orthofinder/data/OrthoFinder/Results_Aug27_2/Comparative_Genomics_Statistics/OrthologuesStats_Totals.tsv`, lines 1–4.
- **OBSERVED:** rooted topology is `(Arabidopsis, (Vtub, Vper))`.
- **Provenance:** `analyses/chapter_1_genomics/02_orthofinder/data/OrthoFinder/Results_Aug27_2/Species_Tree/SpeciesTree_rooted_node_labels.txt`, line 1.
- **SUPPORTED INTERPRETATION:** the sampled *Vellozia* proteomes form a sister pair relative to the sampled *Arabidopsis* outgroup.
- **Caution:** do not call the directional totals “unique orthologous pairs” without resolving OrthoFinder’s relationship definition and multiplicity.

### A-005 — Pairwise inferred duplication events

- **OBSERVED:** OrthoFinder reports 3,106 duplications on the *V. tubiflora* terminal, 4,422 on the *V. peripherica* terminal, 3,864 on their ancestral node N1, 5,620 on *Arabidopsis*, and 2 at N0 (1 at 50% support).
- **Provenance:** `analyses/chapter_1_genomics/02_orthofinder/data/OrthoFinder/Results_Aug27_2/Comparative_Genomics_Statistics/Duplications_per_Species_Tree_Node.tsv`, lines 1–6.
- **Draft conflict:** the draft’s total of 4,334 mapped duplication events is not present in the current output.

### A-006 — Pairwise CAFE5 input and scale

- **OBSERVED:** the preparation retained only `Vper.pep` and `Vtub.pep`, initially retained 16,391 families after a >100-copy filter, and CAFE5 removed root-absent families, leaving 16,032 modeled families.
- **Provenance:** `analyses/chapter_1_genomics/03_cafe5/cafe5_818154.log`, lines 4–16; filter logic in `analyses/chapter_1_genomics/03_cafe5/prep_cafe_input.py`, lines 14–36.
- **OBSERVED:** both terminal branches were manually assigned length 1.0, described in the script itself as an arbitrary distance for structural analysis.
- **Provenance:** `analyses/chapter_1_genomics/03_cafe5/prep_cafe_input.py`, lines 39–54; `analyses/chapter_1_genomics/03_cafe5/ultrametric_vellozia.tre`, line 1.
- **UNSUPPORTED:** interpreting lambda as “gains/losses per gene per million years.” The branch scale is arbitrary and not time-calibrated.
- **Important method conflict:** the actual command is `cafe5 -i ... -t ... -p -o ... -c 4`; no error model (`-e`) is shown, contrary to the source draft.
- **Provenance:** `analyses/chapter_1_genomics/03_cafe5/cafe5_818154.log`, line 14.

### A-007 — Pairwise CAFE5 global and clade summaries

- **OBSERVED:** Base-model final negative log likelihood = 31,073; lambda = 0.074560175552628; 56 values attempted.
- **Provenance:** `analyses/chapter_1_genomics/03_cafe5/cafe5_results/Base_results.txt`, lines 1–4.
- **OBSERVED:** 924 families increased and 147 decreased on the *V. tubiflora* terminal; 1,549 increased and 84 decreased on the *V. peripherica* terminal. These are all inferred changes, not counts restricted to significant families.
- **Provenance:** `analyses/chapter_1_genomics/03_cafe5/cafe5_results/Base_clade_results.txt`, lines 1–3.
- **OBSERVED:** 412 of the 16,032 modeled families have family-wide `p <= 0.05` (the existing `Base_family_results.txt` explicitly flags them `y`).
- **Provenance:** `analyses/chapter_1_genomics/03_cafe5/cafe5_results/Base_family_results.txt`, header line 1 and the file’s 16,032 family rows; direct inspection of the `Significant at 0.05` field.
- **Caution:** the two-tip design cannot localize deeper ancestral changes or support macroevolutionary claims across Velloziaceae.

### A-008 — Selected pairwise family counts and changes

All values below are direct CAFE5 inferred counts. `Root` is node `<3>`; Δ is the corresponding tip change. A p-value printed as `0` is reported exactly as present and must not be rewritten as mathematically equal to zero; use `p < output precision` or “reported as 0 by CAFE5.”

| Orthogroup | Root | Vtub count (Δ) | Vper count (Δ) | Family p | Predominant annotation available in local descriptive file |
|---|---:|---:|---:|---:|---|
| OG0000016 | 6 | 61 (+55) | 3 (-3) | 0 | chloroplast precursor import/intermediate translocation channel |
| OG0000087 | 4 | 26 (+22) | 2 (-2) | 0 | chloroplast precursor import/intermediate translocation complex |
| OG0000036 | 6 | 35 (+29) | 5 (-1) | 0 | chloroplastic NDH-related annotation |
| OG0000062 | 7 | 25 (+18) | 6 (-1) | 0 | chloroplastic NDH-related annotation |
| OG0000069 | 6 | 24 (+18) | 5 (-1) | 0 | Photosystem II core annotation |
| OG0000076 | 6 | 22 (+16) | 6 (0) | 0 | annotation not shown in the top-family table |
| OG0000104 | 4 | 22 (+18) | 3 (-1) | 0 | annotation not shown in the top-family table |
| OG0000119 | 4 | 19 (+15) | 3 (-1) | 0 | annotation not shown in the top-family table |
| OG0000014 | 8 | 59 (+51) | 15 (+7) | 0 | organonitrogen compound metabolic process |
| OG0000017 | 8 | 50 (+42) | 15 (+7) | 0 | organonitrogen compound metabolic process |
| OG0000012 | 8 | 13 (+5) | 65 (+57) | 0 | LRR-repeat protein |
| OG0000021 | 8 | 16 (+8) | 37 (+29) | 0 | receptor-like protein kinase |
| OG0000025 | 8 | 20 (+12) | 33 (+25) | 0 | LRR receptor-like serine/threonine kinase |
| OG0000060 | 6 | 5 (-1) | 28 (+22) | 0 | LRR receptor-like serine/threonine kinase |
| OG0000050 | 7 | 6 (-1) | 29 (+22) | 0 | disease-resistance annotation |
| OG0000049 | 8 | 10 (+2) | 25 (+17) | 0 | NB-LRR family annotation |
| OG0000052 | 8 | 8 (0) | 27 (+19) | 0 | peptidase A1 family |
| OG0000043 | 8 | 7 (-1) | 29 (+21) | 0 | receptor for ubiquitination targets |
| OG0000094 | 6 | 5 (-1) | 22 (+16) | 0 | U-box E3 ubiquitin ligase |
| OG0000131 | 4 | 2 (-2) | 20 (+16) | 0 | PPR-related annotation in draft; not among locally tabulated top annotations |

- **Count/change provenance:** `analyses/chapter_1_genomics/03_cafe5/cafe5_results/Base_count.tab` and `Base_change.tab`, matching orthogroup rows; significance in `Base_family_results.txt`.
- **Annotation provenance:** `analyses/chapter_1_genomics/03_cafe5/descriptive_analysis/top_families_annotated.md`, lines 1–37. The annotation is the most frequent free-text EggNOG description among family members, not experimental functional validation.
- **Draft corrections required:** OG0000036 is 35/5/root 6, not 36/6/root 7; OG0000014 is 59/15/root 8, not 58/14/root 7; OG0000017 is 50/15/root 8, not 49/14/root 7.

### A-009 — Available functional enrichment output

- **OBSERVED:** enrichment was computed over annotated orthogroups, not genes. The tested background is 14,210 annotated orthogroups; target totals are 819 expanding *V. tubiflora* orthogroups and 1,347 expanding *V. peripherica* orthogroups.
- **Provenance:** `analyses/chapter_1_genomics/03_cafe5/descriptive_analysis/functional_enrichment_results.tsv`, header and lines 2–104 for *V. tubiflora*, lines 105 onward for *V. peripherica*; implementation in `run_enrichment_analysis.py`, lines 36–55 and 104–149.
- **OBSERVED, selected FDR-significant curated categories (`q <= 0.05`):**

| Species | Category | Target/background hits | Fold | p | q | Source line |
|---|---|---:|---:|---:|---:|---:|
| *V. tubiflora* | Transposases & mobile elements | 15/42 | 6.20 | 5.1686e-09 | 5.3237e-07 | 2 |
| *V. tubiflora* | LRR receptor-like kinases & cell-wall signaling | 24/161 | 2.59 | 1.6783e-05 | 8.6434e-04 | 3 |
| *V. tubiflora* | Plastid ribosome biogenesis & translation | 30/236 | 2.21 | 3.8161e-05 | 1.3102e-03 | 4 |
| *V. tubiflora* | Photosynthetic electron transport & NDH | 5/9 | 9.64 | 6.5162e-05 | 1.6779e-03 | 5 |
| *V. tubiflora* | Chloroplast protein translocation (TOC/TIC) | 3/8 | 6.51 | 8.5846e-03 | 4.6951e-02 | 18 |
| *V. peripherica* | Cytochrome P450 monooxygenases | 43/128 | 3.54 | 4.0612e-14 | 7.0258e-12 | 105 |
| *V. peripherica* | UDP-glycosyltransferases | 25/53 | 4.98 | 1.4031e-12 | 1.2137e-10 | 106 |
| *V. peripherica* | Wall-associated receptor kinases | 12/27 | 4.69 | 2.2539e-06 | 7.7985e-05 | 109 |
| *V. peripherica* | LRR receptor-like kinases & cell-wall signaling | 31/161 | 2.03 | 1.0012e-04 | 2.1652e-03 | 112 |
| *V. peripherica* | NB-LRR immune receptors | 21/102 | 2.17 | 5.0263e-04 | 7.2462e-03 | 116 |

- **Draft conflict:** the draft reports target totals 1,533 and 2,219, species-specific backgrounds 21,259 and 22,341, and much larger hit counts and significance values. None matches the available output. The unified manuscript must use the table above/current TSV or omit enrichment pending regeneration.
- **Method limitation:** categories are generated by substring rules applied to the predominant free-text annotation per orthogroup (`run_enrichment_analysis.py`, lines 57–102). They are exploratory and partly ad hoc. Biological mechanism claims must be phrased cautiously.

### A-010 — Annotation database status

- **OBSERVED:** `vellozia_comparative_master_annotation.tsv` has 52,017 data rows and columns for coordinates, annotation, orthogroup, single-copy status, sister/*Arabidopsis* orthologues, CAFE significance, delta, and expansion status.
- **Provenance:** `analyses/chapter_1_genomics/annotation_db/vellozia_comparative_master_annotation.tsv`, line 1 and full row count.
- **DATA DEFECT:** `build_annotation_databases.py` defines ancestral columns as every column containing `<` and takes the first match. In `Base_count.tab`, the first such column is `Vtub.pep<1>`, not root `<3>`. Therefore, the exported `ancestral_count` field contains the *V. tubiflora* tip count rather than the ancestral root count.
- **Provenance:** `build_annotation_databases.py`, lines 58–67; `Base_count.tab`, line 1.
- **Decision:** do not use `ancestral_count` from the database/TSV. Read root counts directly from `Base_count.tab`.

## 3. Evidence ledger: seven-taxon analysis

### A-011 — Seven-taxon OrthoFinder configuration and sampling

- **OBSERVED:** OrthoFinder v3.1.5 ran with DIAMOND, FAMSA, and FastTree over seven files: `Abra`, `Ath`, `Dala`, `Ptec`, `Vper`, `Vtub`, and `Xvis`.
- **Provenance:** `chapter3/02_orthofinder/results/Results_Aug29/Log.txt`, lines 1–20.
- **OBSERVED:** OrthoFinder used 1,339 orthogroups in which 100% of species had single-copy genes for the species-tree alignment; 1,424 all-species single-copy orthogroups exist overall.
- **Provenance:** `chapter3/02_orthofinder/orthofinder_ch3_818680.log`, lines 54–67 and 95–100; `Species_Tree/Orthogroups_for_concatenated_alignment.txt` contains 1,339 entries.
- **Caution:** the local files do not include a taxon-source manifest with accession, version, canonical-filter audit, or checksum. Taxon identities and comparability require validation before publication.

### A-012 — Seven-taxon orthogroup totals

- **OBSERVED:** 168,596 genes; 160,585 assigned to 16,532 orthogroups (95.2%); 8,011 unassigned (4.8%); 1,540 species-specific orthogroups containing 6,203 genes; 8,011 orthogroups present in all seven species; 1,424 single-copy orthogroups; mean/median sizes 9.7/8.0.
- **Provenance:** `chapter3/02_orthofinder/results/Results_Aug29/Comparative_Genomics_Statistics/Statistics_Overall.tsv`, lines 1–18.
- **Status:** these values agree with the macroevolutionary source draft.

### A-013 — Seven-taxon per-species counts

| File label | Input genes | Assigned | Assigned (%) | Unassigned | Species-specific orthogroups (genes) |
|---|---:|---:|---:|---:|---:|
| Abra | 18,085 | 17,939 | 99.2 | 146 | 12 (44) |
| Ath | 17,755 | 15,679 | 88.3 | 2,076 | 446 (2,026) |
| Dala | 38,603 | 35,646 | 92.3 | 2,957 | 887 (3,385) |
| Ptec | 20,039 | 19,782 | 98.7 | 257 | 12 (31) |
| Vper | 26,466 | 25,238 | 95.4 | 1,228 | 109 (396) |
| Vtub | 25,551 | 24,324 | 95.2 | 1,227 | 61 (264) |
| Xvis | 22,097 | 21,977 | 99.5 | 120 | 13 (57) |

- **Provenance:** `chapter3/02_orthofinder/results/Results_Aug29/Comparative_Genomics_Statistics/Statistics_PerSpecies.tsv`, lines 1–11.

### A-014 — Seven-taxon species tree

- **OBSERVED topology:** `(Ath,(Dala,(Ptec,(Abra,(Xvis,(Vper,Vtub))))))`.
- **Provenance:** `chapter3/02_orthofinder/results/Results_Aug29/Species_Tree/SpeciesTree_rooted_node_labels.txt`, line 1.
- **SUPPORTED INTERPRETATION within this sample:** *V. peripherica* and *V. tubiflora* form a sister pair; *X. viscosa* is sister to that pair; *A. bracteata* is the next sampled branch; *Ptec* is outside the sampled Velloziaceae group.
- **UNSUPPORTED wording:** “absolute bootstrap support.” The tree file has internal labels of `1`, but no bootstrap replicate output or explicit support-method report is present. The OrthoFinder log documents FAMSA/FastTree and 1,339 genes, not a dedicated IQ-TREE bootstrap analysis.

### A-015 — Seven-taxon CAFE5 input and calibration assumptions

- **OBSERVED:** full table contains 16,532 families; filtered input contains 16,524 families (8 excluded because at least one taxon had >=100 copies); CAFE5 family-results files contain 9,209 modeled families after root-presence filtering.
- **Provenance:** `chapter3/04_cafe5/cafe_family_input_full.tsv` and `cafe_family_input.tsv` row counts; filter implementation in `chapter3/scripts/prep_family_cafe5.py`, lines 66–80; `Base_family_results.txt` and `Gamma_family_results.txt` row counts.
- **OBSERVED:** the tree encodes tip ages/branch lengths corresponding to 12, 75, 85, 95, 115, and 135 units/Ma assumptions.
- **Provenance:** `chapter3/04_cafe5/velloziaceae_ultrametric.tre`, line 1.
- **UNTESTED/UNSUPPORTED:** calling these “estimated divergence times.” `chapter3/03_phylogenomics/` is empty, `make_ultrametric_tree.py` is empty, and there are no fossil-calibration or MCMCtree outputs. The ages are manually specified assumptions.

### A-016 — Seven-taxon Base and Gamma model results

- **OBSERVED Base:** negative log likelihood 83,483.1; lambda 0.0022109590091792; 62 values attempted.
- **Provenance:** `chapter3/04_cafe5/cafe5_results/base_model/Base_results.txt`, lines 1–4.
- **OBSERVED Gamma:** negative log likelihood 79,951.4; lambda 0.0028896458243847; alpha 1.05816; 100 values attempted.
- **Provenance:** `chapter3/04_cafe5/cafe5_results/gamma_model/Gamma_results.txt`, lines 1–5.
- **OBSERVED:** 661 Base families and 460 Gamma families are flagged family-wide significant at 0.05 in their respective `*_family_results.txt` files.
- **Caution:** lower negative log likelihood for Gamma alone is not a complete documented model-selection test. The chapter must identify which model supplies every downstream number.

### A-017 — Existing CAFE5 branch summary is Base-model output

- **OBSERVED:** `Table_1_Pan_Velloziaceae_CAFE5_Summary.tsv` reports:

| Branch/node | Expanded | Contracted | Significant expanded | Significant contracted | Net gene gain |
|---|---:|---:|---:|---:|---:|
| Vper<1> | 664 | 225 | 209 | 39 | 1,134 |
| Vtub<2> | 415 | 333 | 106 | 57 | 547 |
| Xvis<3> | 1,818 | 708 | 39 | 26 | 1,475 |
| Abra<4> | 801 | 1,491 | 22 | 81 | -805 |
| Ptec<5> | 1,315 | 1,138 | 41 | 21 | 531 |
| Dala<6> | 3,969 | 850 | 360 | 23 | 9,520 |
| Ath<7> | 1,295 | 1,949 | 70 | 14 | 340 |
| node 9 | 363 | 4 | 74 | 2 | 435 |
| node 10 | 186 | 191 | 35 | 5 | 21 |
| node 11 | 146 | 156 | 33 | 7 | -1 |
| node 12 | 105 | 44 | 40 | 4 | 92 |
| node 13 | 893 | 542 | 126 | 5 | 1,070 |

- **Provenance:** `chapter3/results/Table_1_Pan_Velloziaceae_CAFE5_Summary.tsv`, lines 1–14; matching Base-model counts in `base_model/Base_clade_results.txt`, lines 1–13, and `Base_report.cafe`, lines 1–9.
- **PIPELINE DEFECT:** `analyze_cafe5_family_results.py` first selects the Gamma directory but checks for filenames beginning `Base_`; because Gamma files begin `Gamma_`, it falls back to the Base directory. Thus the table is Base-derived while the macroevolutionary draft labels the analysis Gamma-derived.
- **Provenance:** `chapter3/scripts/analyze_cafe5_family_results.py`, lines 37–45.

### A-018 — Correct CAFE5 node identities

- **OBSERVED node map:**

| Node | Descendant clade |
|---|---|
| 13 | *V. peripherica* + *V. tubiflora* |
| 12 | (*V. peripherica* + *V. tubiflora*) + *X. viscosa* |
| 11 | node 12 + *A. bracteata* |
| 10 | node 11 + `Ptec` |
| 9 | node 10 + *D. alata* |
| 8 | node 9 + *A. thaliana* (root; no modeled change) |

- **Provenance:** `chapter3/04_cafe5/cafe5_results/base_model/Base_report.cafe`, line 4; same mapping in `gamma_model/Gamma_report.cafe`, line 4.
- **CRITICAL DRAFT ERROR:** node 13 is not the common ancestor of *Xerophyta* and *Vellozia*. The source draft attributes 893 expansions and 126 significant expansions at node 13 to a pre-Gondwanan *Xerophyta* + *Vellozia* ancestor. Those values actually belong to the *V. peripherica* + *V. tubiflora* ancestor. Under the Base summary, the sampled *Xerophyta* + *Vellozia* ancestor is node 12, with 105 expanded families and 40 significant expansions.
- **Consequence:** the current outputs do not demonstrate that desiccation tolerance is a pan-Gondwanan homologous synapomorphy, do not reject convergence, and do not establish the evergreen condition as a secondary loss. Those require a character-coded ancestral-state model and properly interpreted, functionally annotated branch results.

### A-019 — Seven-taxon functional claims are not traceable

- **OBSERVED:** the macroevolutionary draft lists functional classes for terminal expansions and invokes LEA, F-box, RLK, NLR/ZAR1, PPR, and P450 mechanisms.
- **MISSING:** no chapter 3 orthogroup-to-function table, enrichment output, gene list, annotation database, or script output supporting these functional summaries is present under `chapter3/`.
- **Decision:** numerical branch counts from A-017 may be used with clear Base-model labeling. Functional interpretation of specific expanded families must be omitted or explicitly presented as unvalidated pending a traceable annotation artifact.

## 4. Available figures and tables

### Existing visual artifact

- `analyses/chapter_1_genomics/03_cafe5/descriptive_analysis/expansion_contraction_summary.png`
  - Displays total Base-model expansion/contraction counts for the two-tip analysis, generated by `analyze_cafe_functional.py`, lines 22–44.
  - It does not distinguish significant families and should be labeled accordingly.

### Existing machine-readable tables suitable for manuscript-table generation

- Pairwise OrthoFinder:
  - `Statistics_Overall.tsv`
  - `Statistics_PerSpecies.tsv`
  - `OrthologuesStats_Totals.tsv`
  - `Duplications_per_Species_Tree_Node.tsv`
  - `Orthogroups.GeneCount.tsv`
- Pairwise CAFE5:
  - `Base_results.txt`
  - `Base_clade_results.txt`
  - `Base_count.tab`
  - `Base_change.tab`
  - `Base_family_results.txt`
  - `functional_enrichment_results.tsv`
  - `top_families_annotated.md`
- Seven-taxon OrthoFinder:
  - `Statistics_Overall.tsv`
  - `Statistics_PerSpecies.tsv`
  - species-tree Newick files
  - duplication statistics
- Seven-taxon CAFE5:
  - Base and Gamma model result/count/change/probability files
  - `chapter3/results/Table_1_Pan_Velloziaceae_CAFE5_Summary.tsv` (Base only)

### Draft-only figure/table placeholders with no inspected figure file

- Pairwise draft Figures 1–4: orthogroup Venn, synteny plots, gene-family dynamics, and Ka/Ks distributions.
- Pairwise draft Table 1 assembly/BUSCO values: no local output in scope.
- Pairwise draft Tables 2–3: values must be replaced/reconciled against A-008 and A-009.
- Macroevolutionary species tree/CAFE plots: no visual file exists.

## 5. Missing or incomplete expected analyses

These items are reported as limitations only. No new analysis was run.

| Priority | Missing/incomplete item | Why it matters for Chapter 1 | Required disposition now |
|---|---|---|---|
| Critical | Reconcile the pairwise manuscript against the current OrthoFinder run | Core orthogroup, single-copy, input-gene, species-specific, and duplication numbers are inconsistent | Replace draft numbers with A-002–A-005 or explicitly identify and restore the older run that generated the draft values. |
| Critical | Correct node identities and model labeling in macroevolutionary section | Present draft’s central evolutionary conclusion is based on a wrong node and mixed Base/Gamma outputs | Restrict to observed topology and model-specific family-count patterns; remove “proved pan-Gondwanan origin,” ancestral synapomorphy, and secondary-loss claims. |
| Critical | Synteny result outputs | No evidence for 297 blocks, zero translocations, or Chr1A–Chr5A duplication exists in scope | Remove empirical synteny results. Mention synteny only as pending or as analysis described elsewhere with a verifiable source. |
| Critical | Ka/Ks/selection outputs | No evidence for 7,061 tested pairs, mean omega 0.3542, or functional selection gradients exists | Remove the Results and mechanistic Discussion based on Ka/Ks. Do not infer positive selection from elevated omega below 1. |
| Critical | Trait ancestral-state reconstruction | Gene-family expansions cannot determine whether desiccation tolerance is homologous or convergent | Phrase origin as an unresolved hypothesis. |
| Critical | Validate seven-taxon proteome provenance and species identity | Taxon labels/accessions and canonicalization are not auditable | Add a source/version/checksum manifest before publication; until then, refer to file labels conservatively. |
| Useful | Traceable chapter 3 functional annotation and enrichment | Functional classes in the macro draft cannot be audited | Omit functional claims or register exact family/gene evidence in a future artifact. |
| Useful | Dedicated phylogenomic support and discordance analysis | FastTree topology lacks documented bootstrap/concordance; ILS/gene-tree conflict not assessed | Call it the OrthoFinder species tree, not a fully supported dated phylogeny. |
| Useful | Independent time calibration | Current ages are hard-coded assumptions; no dating outputs exist | Describe the CAFE tree as using assumed calibration values, not estimated divergence times. |
| Useful | CAFE5 error model/model-selection audit | Commands do not document an error model; Base/Gamma outputs are mixed | Keep models separate and avoid “error-corrected” unless an error model output is supplied. |
| Useful | Regenerate enrichment with predefined ontologies and transparent universe | Current categories are substring-defined over predominant free-text orthogroup annotations | Treat A-009 as exploratory, not definitive pathway evidence. |
| Appendix | Assembly/BUSCO/annotation QC outputs | Draft reports chromosome count and >95% BUSCO without inspected evidence | Move methods to Appendix and omit exact QC results unless Appendix outputs are registered. |
| Optional | Ks-based WGD dating and syntenic-depth analysis | Needed to time a proposed paleoduplication | Record as future dry-lab analysis; do not anticipate its result. |

## 6. Claim-by-claim decision matrix for the Scientific Writer

| Proposed claim | Decision | Evidence/constraint |
|---|---|---|
| Current pairwise run clustered 69,772 proteins into 16,953 orthogroups, with 4,445 single-copy orthogroups | Use | A-002. |
| *V. peripherica* has more terminal OrthoFinder duplications than *V. tubiflora* | Use cautiously | A-005; these are inferred duplication events and are annotation-quality-sensitive. |
| Two-tip CAFE5 inferred more increased families in *V. peripherica* than *V. tubiflora* | Use cautiously | A-007; all-family counts, arbitrary branch scale, two taxa. |
| Lambda = 0.07456 gains/losses per gene per million years | Do not use | A-006; branches are arbitrary unit lengths. |
| Current enrichment supports plastid-related categories in *V. tubiflora* and P450/UGT/receptor categories in *V. peripherica* | Use as exploratory | A-009; use exact current values and describe substring-based annotation limitations. |
| Gene-family expansion enables rapid chloroplast rebuilding or causes evergreen hypervigilance | Interpretive only | Copy number/enrichment does not establish physiological function or causality. Use “is consistent with” and cite literature evidence separately. |
| Seven-taxon topology places *Xerophyta* sister to sampled *Vellozia* | Use | A-014, limited to sampled taxa. |
| Node 13 is the *Xerophyta*–*Vellozia* ancestor | Do not use | A-018; it is the two-*Vellozia* ancestor. |
| 126 significant expansions prove ancestral desiccation tolerance before Gondwanan breakup | Do not use | Wrong node plus no trait reconstruction; A-018. |
| *V. peripherica* secondarily lost ancestral desiccation tolerance | Do not use | No ancestral-state or loss/silencing analysis. |
| 297 syntenic blocks, zero translocations, and Chr1A–Chr5A WGD | Do not use | No result files. |
| Mean Ka/Ks = 0.3542 and functional-category omega gradients | Do not use | No result files. |
| OSCA motivates targeted Chapter 2 work | At most one scope-transition sentence | No OSCA-specific results or detailed discussion in Chapter 1. |

## 7. Recommended evidence-safe Chapter 1 analytical narrative

The evidence currently supports a unified chapter centered on: (i) a pairwise comparison of current *V. tubiflora* and *V. peripherica* proteomes; (ii) conservative description of orthogroup partitioning, duplication inference, and exploratory two-tip CAFE5/enrichment patterns; and (iii) a broader seven-taxon OrthoFinder topology and model-specific CAFE5 family-count context. It does not support chromosomal-synteny, Ka/Ks, formal molecular-dating, adaptive ancestral-state, or causal mechanistic conclusions. The central biological conclusion should therefore be framed as differential gene-family turnover consistent with contrasting genomic repertoires, not as proof of drought-strategy causation or of a single Gondwanan origin of desiccation tolerance.

## Inspection status

`EVIDENCE_STATUS: COMPLETE_FIRST_PASS`

The available analytical outputs were sufficient to establish a safe core and identify blocking mismatches. Remaining issues require source/result recovery or future dry-lab work and must not be silently inferred.
