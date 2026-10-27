# Comparative Gene Family Dynamics v2 (Calibrated CAFE5 Pipeline - Final Revised)

**Primary Data Table:** [`comparative_families_master_table_v2.tsv`](./comparative_families_master_table_v2.tsv)  
**Total Gene Families Evaluated:** 12,276 (families with <100 copies filtered for CAFE5 numerical stability and present at the root)  
**Total Physical Columns:** 73 (`FamilyID` index + 72 variables)  
**Phylogenetic Calibration:** Ultrametric MCMCtree chronogram (Fossil-calibrated, Root = 138.48 Ma)  
**Primary Model:** CAFE5 Gamma $k=2$ (Empirical count error matrix fixed)  
**Sensitivity Model:** CAFE5 Gamma $k=3$ (Consensus across all 4 valid replicates: rep01, rep03, rep04, rep05; rep02 discarded as suboptimal local minimum)  

---

## 1. Technical Notes & Methodological Clarifications

1. **Count Error Model Parameterization ($\epsilon$ vs $2\epsilon$)**:
   - The estimated single-step error parameter is $\epsilon \approx 0.00609$ (~0.61%).
   - In the CAFE5 Markovian transition matrix, $\epsilon$ represents the transition probability for each adjacent error state ($c \rightarrow c-1$ or $c \rightarrow c+1$).
   - Consequently, for any positive gene count ($c \ge 1$), the total modeled probability of observation error within $\pm 1$ copy is $2\epsilon \approx 1.22\%$ (approximately 98.78% diagonal retention probability).
2. **Branch Probabilities and Expected Missingness**:
   - CAFE5 computes and outputs branch-specific probabilities (`Gamma_branch_probabilities.tab`) exclusively for gene families meeting the initial strict nominal reporting threshold ($p < 0.05$).
   - While 508 families exhibit $p \le 0.05$, the 3 families with exactly $p = 0.05$ were excluded by CAFE5 from the branch probabilities file, resulting in the 505 reported families.
   - Of these 505 families, 201 are subsequently classified as non-significant after global false discovery rate (FDR) control ($q > 0.05$).
   - Therefore, the 11,771 missing values are absent by design because they did not meet the initial nominal report threshold, rather than simply being "non-significant" post-hoc.
   - Crucially, **100% of the 188 Tier A families** have complete, valid branch-specific probabilities. These probabilities represent CAFE5 branch-specific test probabilities (branch $p$-values) and are not posterior probabilities.
3. **Replicate $q$-values**:
   - The columns `k2_mean_qval` and `k3_mean_qval` represent descriptive summaries of stochastic stability across runs, **not a combined hypothesis test**.
   - Classification into Tier A strictly requires independent significance ($q \le 0.05$) in 5/5 replicates of $k=2$ and 4/4 valid replicates of $k=3$.
4. **Enrichment Background Universe**:
   - The eligible background universe for all subsequent functional enrichment analyses (e.g., Fisher's exact tests or hypergeometric overrepresentation) consists of the **complete set of 12,276 families analyzed by CAFE5**.
5. **Species Nomenclature**:
   - The basal Velloziaceae taxon is ***Acanthochlamys bracteata*** (`Abra`), endemic to the Hengduan Mountains (China).

---

## 2. Classification by Evidence Tiers

| Evidence Tier | Inclusion Criteria | Number of Families | Analytical Purpose |
| :--- | :--- | :---: | :--- |
| **Tier A (High-Confidence Core)** | $q \le 0.05$ across all 5 reps of $k=2$ **AND** all 4 valid reps of $k=3$ | **188** | Core analytical dataset for thesis figures, biological discussion, and gene tree reconstructions. |
| **Tier B (Rate Heterogeneity)** | $q \le 0.05$ across all 4 valid reps of $k=3$, but not all 5 reps of $k=2$ | **43** | Sensitivity dataset; evidence conditioned on 3-category gamma rate modeling. |
| **Tier C (Exploratory)** | $q \le 0.05$ in $\ge 1$ replicate of $k=2$ or $k=3$ | **73** | Secondary candidates for exploratory review only. |
| **Non-Significant** | $q > 0.05$ across all tested models | **11,972** | Families without statistically detectable deviation from the neutral birth-death turnover process (eligible background universe). |

---

## 3. Independent Binary Indicators for Evolutionary Events & Consensus ($k=2$ vs ALL 4 Valid $k=3$ Replicates)

Rather than forcing gene families into mutually exclusive categories, `comparative_families_master_table_v2.tsv` provides **independent boolean indicator columns**. 

### Biological Context of Lineages:
- **Desiccation-Tolerant (DT) Lineages**: *Vellozia tubiflora* (`Vtub`), *Xerophyta viscosa* (`Xvis`), and *Acanthochlamys bracteata* (`Abra`).
- **Desiccation-Avoidance Lineage**: *Vellozia peripherica* (`Vper`).
- **Outgroups**: *Pandanus tectorius* (`Ptec`), *Dioscorea alata* (`Dala`), *Arabidopsis thaliana* (`Ath`).

### Indicator Preservation Requiring Consensus Across ALL 4 Valid $k=3$ Replicates in Tier A ($N = 188$):

| Evolutionary Indicator Column | Definition / Condition in $k=2$ | Count in $k=2$ | Consensus Across ALL 4 $k=3$ Reps | Robustness Interpretation |
| :--- | :--- | :---: | :---: | :--- |
| **`Ind_Exp_Terminal_Vper`** | `Change_Vper > 0` & strictly highest count among Velloziaceae | **72** | **72 / 72 (100%)** | Robust to the tested Gamma rate partition. |
| **`Ind_Exp_Terminal_Vtub`** | `Change_Vtub > 0` & strictly highest count among Velloziaceae | **31** | **31 / 31 (100%)** | Robust to the tested Gamma rate partition. |
| **`Ind_Exp_Terminal_Xvis`** | `Change_Xvis > 0` & strictly highest count among Velloziaceae | **34** | **34 / 34 (100%)** | Robust to the tested Gamma rate partition. |
| **`Ind_Exp_Terminal_Abra`** | `Change_Abra > 0` & strictly highest count among Velloziaceae | **7** | **7 / 7 (100%)** | Robust to the tested Gamma rate partition. |
| **`Ind_Exp_Terminal_Ptec`** | `Change_Ptec > 0` & strictly highest count among all 7 species | **17** | **17 / 17 (100%)** | Robust outgroup expansion in *P. tectorius*. |
| **`Ind_Parallel_Exp_DT_2plus`** | Positive change (`Change > 0`) in $\ge 2$ tolerant species (*Vtub*, *Xvis*, *Abra*) | **28** | **28 / 28 (100%)** | Robust candidates associated with the desiccation phenotype. |
| **`Ind_Parallel_Contraction_DT_2plus`** | Negative change (`Change < 0`) in $\ge 2$ tolerant species (*Vtub*, *Xvis*, *Abra*) | **94** | **79 / 94 (84.0%)** | Moderately dependent on rate heterogeneity modeling. |
| **`Ind_Exp_Ancestral_Node13_Vellozia`** | `Change_Node13 > 0` (crown ancestor of *Vellozia*, ~10 Ma) | **79** | **68 / 79 (86.1%)** | Moderately dependent on rate heterogeneity modeling. |
| **`Ind_Exp_Ancestral_Node12_CoreVelloziaceae`** | `Change_Node12 > 0` (ancestor of *Vper*+*Vtub*+*Xvis*, ~32 Ma) | **112** | **100 / 112 (89.3%)** | Moderately dependent on rate heterogeneity modeling. |
| **`Ind_Exp_Ancestral_Node11_Velloziaceae_Crown`** | `Change_Node11 > 0` (ancestor of *Abra*+Core Velloziaceae, ~78 Ma) | **35** | **22 / 35 (62.9%)** | Highly sensitive to rate heterogeneity modeling at deep nodes. |
| **`Concordant_Exact_Sign_All_Key_Branches`** | Exact sign equality across all 6 key branches (`Vper`, `Vtub`, `Xvis`, `Abra`, Node 13, Node 12) matching across all 4 valid $k=3$ reps | — | **132 / 188 (70.2%)** | Strict multi-replicate sign equality across all branches simultaneously. |

*Takeaway:* Terminal expansions and parallel expansions across desiccation-tolerant lineages are 100% invariant across all valid parameter searches. Conversely, parallel gene contractions and deep ancestral nodes (especially Node 11) display greater sensitivity to gamma rate partition modeling.

---

## 4. Priority Hierarchy in `Evolutionary_Dynamic_Summary`

While the independent binary indicator columns constitute the primary analytical result, a derived categorical summary column (`Evolutionary_Dynamic_Summary`) is provided for high-level visualization according to the following explicit priority hierarchy:
1. **`Outgroup_Expansion_Ptec`**: Expansions driven by outgroup *Pandanus tectorius* are isolated first to prevent confounding with ingroup dynamics.
2. **`Parallel_Expansion_DT`**: Prioritizes candidates with parallel expansions across multiple tolerant lineages (*Vtub*, *Xvis*, *Abra*).
3. **`Ancestral_Exp_Node12_CoreVelloziaceae`**: Captures shared expansions at the radiation of *Core Velloziaceae* (~32 Ma).
4. **`Ancestral_Exp_Node11_Velloziaceae_Crown`**: Captures ancient crown Velloziaceae expansions (~78 Ma).
5. **`Ancestral_Exp_Node13_Vellozia_Crown`**: Captures expansions at the divergence of genus *Vellozia* (~10 Ma).
6. **Terminal Expansions (`Terminal_Exp_Vper`, `Terminal_Exp_Vtub`, `Terminal_Exp_Xvis`, `Terminal_Exp_Abra`)**: Lineage-specific terminal proliferations.
7. **`Parallel_Contraction_DT`**: Coordinated reductions in gene family size across tolerant taxa.
8. **`Other_Dynamic`**: Complex turnover patterns.

---

## 5. Refined Quality Control & Biological Flags

1. **`Flag_Transposon` (4 families in Tier A)**:
   - Evaluated with strict word-boundary regex (`\b(transposon|retrotransposon|gag|reverse transcriptase|integrase|gypsy|copia|helitron)\b`).
   - Families identified: `OG0000005`, `OG0000037`, `OG0000111`, `OG0000188`.
2. **`Flag_Organellar` (13 families in Tier A)**:
   - Evaluated with comprehensive plastidial/photosynthetic regex (`\b(chloroplasts?|plastids?|mitochondri(on|a|al)?|ycf\d*|matk|rbcl|psa[a-z]?|psb[a-z]?|cox\d*|ndh[a-z]?|nadh dehydrogenase|photosystem(\s+[i|v|x]+)?|psii|psi)\b`).
   - Confirms true organellar components (e.g., plastidial NDH subunits `OG0000014`, `OG0000017`, `OG0000036`, `OG0000062`, `OG0000098`, `OG0000156`, `OG0000278`; Photosystem II components `OG0000069`, `OG0000091`, `OG0000912`; chloroplast envelope/import `OG0000075`, `OG0000229`, `OG0000785`).
3. **`Flag_High_Copy_Asymmetry` (15 families in Tier A)**:
   - Identifies families where a single taxon contains $\ge 85\%$ of all gene copies (minimum total count $\ge 20$), prioritizing them for tandem assembly vs. genuine duplication validation without presuming an artifact.
4. **Annotation Labeling**:
   - Orthogroups lacking explicit EggNOG description in *Vper* or *Vtub* annotations are designated as `"Sem anotacao EggNOG recuperada"`.

---

## 6. Physical Table Structure (73 Columns)

1. **Identifiers (1 col)**: `FamilyID` (index).
2. **Counts (8 cols)**: `Count_Abra`, `Count_Ath`, `Count_Dala`, `Count_Ptec`, `Count_Vper`, `Count_Vtub`, `Count_Xvis`, `Total_Count`.
3. **Branch Changes ($k=2$, 13 cols)**: `Change_Vper`, `Change_Vtub`, `Change_Xvis`, `Change_Abra`, `Change_Ptec`, `Change_Dala`, `Change_Ath`, `Change_Node13_Vellozia_Crown`, `Change_Node12_Core_Velloziaceae`, `Change_Node11_Velloziaceae_Crown`, `Change_Node10_Pandanales`, `Change_Node9_Monocots`, `Change_Node8_Root`.
4. **Branch Probabilities (10 cols)**: `BranchProb_Vper`, `BranchProb_Vtub`, `BranchProb_Xvis`, `BranchProb_Abra`, `BranchProb_Ptec`, `BranchProb_Dala`, `BranchProb_Ath`, `BranchProb_Node11_Velloziaceae_Crown`, `BranchProb_Node12_CoreVelloziaceae`, `BranchProb_Node13_Vellozia_Crown`.
5. **Replicate FDR $q$-values (13 cols)**: `qval_k2_rep01` to `rep05`, `qval_k3_rep01`, `rep03`, `rep04`, `rep05`, `k2_mean_qval`, `k3_mean_qval`, `k2_sig_reps_count`, `k3_sig_reps_count`.
6. **Classification & Independent Indicators (23 cols)**:
   - `Evidence_Tier`
   - `Ind_Exp_Terminal_Vper`, `Ind_Exp_Terminal_Vtub`, `Ind_Exp_Terminal_Xvis`, `Ind_Exp_Terminal_Abra`, `Ind_Exp_Terminal_Ptec`
   - `Ind_Parallel_Exp_DT_2plus`
   - `Ind_Exp_Ancestral_Node13_Vellozia`, `Ind_Exp_Ancestral_Node12_CoreVelloziaceae`, `Ind_Exp_Ancestral_Node11_Velloziaceae_Crown`
   - `Ind_Parallel_Contraction_DT_2plus`
   - `Concordant_Exact_Sign_All_Key_Branches`
   - `Preserved_k3_Exp_Terminal_Vper`, `Preserved_k3_Exp_Terminal_Vtub`, `Preserved_k3_Exp_Terminal_Xvis`, `Preserved_k3_Exp_Terminal_Abra`, `Preserved_k3_Exp_Terminal_Ptec`
   - `Preserved_k3_Parallel_Exp_DT`, `Preserved_k3_Parallel_Cont_DT`
   - `Preserved_k3_Exp_Node13`, `Preserved_k3_Exp_Node12`, `Preserved_k3_Exp_Node11`
   - `Evolutionary_Dynamic_Summary`
7. **Annotations & Quality Flags (5 cols)**:
   - `EggNOG_Description`, `Arabidopsis_Orthologs`
   - `Flag_Organellar`, `Flag_Transposon`, `Flag_High_Copy_Asymmetry`
