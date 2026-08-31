# EMPIRICAL ANALYSIS INSPECTION: CHAPTER 1 COMPARATIVE GENOMICS

**Source Data Directory:** `/home/mfcaval/github/doutorado/analyses/chapter_1_genomics/` (supplemented by `/analyses/03_synteny/` and `/analyses/04_evolutionary_rates/`)  
**Target Chapter:** Chapter 1: *Large-Scale Comparative Genomics of Vellozia tubiflora and Vellozia peripherica*  
**Date of Extraction:** August 2026  

---

## 1. Upstream Genomic Datasets & Assembly Hand-Off Summary (Appendix A)

| Feature / Metric | *Vellozia tubiflora* (Resurrection / DT) | *Vellozia peripherica* (Evergreen / Avoidant) | Reference Model (*Arabidopsis thaliana*) |
|---|:---:|:---:|:---:|
| **Ecological Lifestyle** | Obligate Desiccation-Tolerant (DT) | Desiccation-Sensitive / Avoidant | Mesophyte Model |
| **Chromosomal Architecture** | 9 Pseudomolecules (Chr1A–Chr9A) | 9 Pseudomolecules (Chr1A–Chr9A) | 5 Chromosomes (Chr1–Chr5) |
| **Assembly Contiguity / BUSCO** | $> 95\%$ Complete Embryophyta | $> 95\%$ Complete Embryophyta | $> 99\%$ Complete |
| **Total Predicted Proteome** | **34,449** proteins | **34,705** proteins | **27,655** canonical proteins |
| **Proteins Assigned to Orthogroups** | **32,231 (93.6%)** | **30,551 (88.0%)** | **27,511 (99.5%)** |
| **Unassigned Specific Genes** | **2,218 (6.4%)** | **4,154 (12.0%)** | **144 (0.5%)** |
| **Methodological Reference** | Detailed in **Appendix A** | Detailed in **Appendix A** | TAIR10 / Araport11 |

---

## 2. OrthoFinder Comparative Proteome Clustering

**Input Proteomes:** 3 species (*Arabidopsis thaliana*, *Vellozia peripherica*, *Vellozia tubiflora*)  
**Total Analyzed Sequences:** 96,809 proteins (90,293 clustered into orthogroups = 93.3%; 6,516 unassigned = 6.7%)  

### 2.1 Global Orthogroup Statistics
- **Total Orthogroups (OGs):** 24,013
- **Mean Orthogroup Size:** 3.8 genes
- **Median Orthogroup Size:** 3.0 genes
- **Orthogroups with All 3 Species Present:** 11,048 (46.0%)
- **Single-Copy Universal Orthogroups (1:1:1):** 7,061 orthogroups
- **Gene Duplication Events (Species Tree Nodes):** 4,334 duplication events

### 2.2 Species-Specific Orthogroups & Gene Partitions
- **Vellozia tubiflora (Specific):** 655 orthogroups (2,019 genes)
- **Vellozia peripherica (Specific):** 1,189 orthogroups (3,526 genes)
- **Arabidopsis thaliana (Specific):** 511 orthogroups (1,349 genes)

### 2.3 Pairwise Ortholog Counts
- **V. peripherica vs. V. tubiflora:** 18,690 orthologous pairs (17,752 one-way / 18,690 mutual)
- **A. thaliana vs. V. peripherica:** 12,828 / 13,356 orthologous pairs
- **A. thaliana vs. V. tubiflora:** 12,740 / 13,104 orthologous pairs

---

## 3. Syntenic Collinearity & Structural Duplication Dynamics (MCScanX / JCVI)

### 3.1 Macrosynteny & Chromosomal Collinearity
- **Inter-genomic Syntenic Blocks:** **297 collinear syntenic blocks** preserved across all 9 homologous chromosome pairs (Chr1A–Chr9A).
- **Structural Integrity:** Zero major inter-chromosomal translocations; chromosome-to-chromosome collinearity is highly preserved between the two congeneric genomes.

### 3.2 Microsynteny of Candidate Signaling Loci
- **OSCA1.3 / OSCA1.4 / OSCA1.5 Cluster on Chr7A:** Perfect micro-collinear contiguity (gap of 0 intervening genes), flanked by a conserved block of 24 collinear orthologs, indicating pre-speciation tandem duplication maintained under purifying selection.

### 3.3 Intragenomic Paleoduplications (Self-Synteny)
- **Ancestral Whole-Genome Paleoduplication Block (Chr1A $\leftrightarrow$ Chr5A):** Conserved collinear duplication block connecting Chromosome 1A and Chromosome 5A in both genomes, harboring simultaneously duplicated OSCA subfamilies:
  - OSCA2 subfamily: *OSCA2.1* (Chr1A) $\leftrightarrow$ *OSCA2.2* (Chr5A)
  - OSCA3 subfamily: *OSCA3.1* (Chr1A) $\leftrightarrow$ *OSCA3.2* (Chr5A)
- **Lineage-Specific Tandem Duplication on Chr1A:** *Vellozia peripherica* exhibits an adjacent tandem duplication of the OSCA2.4 locus (*VpOSCA2.4a* and *VpOSCA2.4b*, physical gap = 0 genes), whereas *Vellozia tubiflora* possesses a single copy (*VtOSCA2.4*).

---

## 4. Gene Family Expansion & Contraction Dynamics (CAFE5)

**Model:** Base Birth-Death ($\lambda$) Model  
**Final Negative Log-Likelihood (-lnL):** 31,073  
**Estimated Global Birth-Death Rate ($\lambda$):** **0.07456** gains/losses per gene per million years  

### 4.1 Clade-Level Family Variations
- **Vellozia tubiflora Lineage:** **924 expanding families**, **147 contracting families**
- **Vellozia peripherica Lineage:** **1,549 expanding families**, **84 contracting families**

### 4.2 Top Functionally Annotated Expansions

#### A. Expansions in *Vellozia tubiflora* (Desiccation Tolerance Specialization)
1. **Chloroplast Inner Envelope Translocation Complex (TOC/TIC translocon, OG0000016):** $+55$ genes in *V. tubiflora* vs. $-3$ in *V. peripherica*. Mediates protein precursor import and inner envelope remodeling during rehydration.
2. **Photosynthetic NDH Complex / Cyclic Electron Transport (OG0000036):** $+29$ genes in *V. tubiflora* vs. $-1$ in *V. peripherica*. Shuttles electrons from NAD(P)H to plastoquinone to power photoprotective Cyclic Electron Transport (CET) during dehydration.
3. **Organonitrogen Compound Metabolic Processes (OG0000014, OG0000017):** $+51$ and $+42$ genes in *V. tubiflora*.
4. **Plant Transposases & Mobile Domains (OG0000010, OG0000020, OG0000013):** $+43$, $+33$, $+30$ genes in *V. tubiflora*.

#### B. Expansions in *Vellozia peripherica* (Evergreen Drought Avoidance Specialization)
1. **Leucine-Rich Repeat (LRR) Receptor-Like Kinases (RLKs, OG0000012, OG0000021, OG0000025, OG0000060, OG0000029):** $+57$, $+29$, $+25$, $+22$, $+17$ genes in *V. peripherica*. Monitor cell wall integrity, osmotic changes, and extracellular ligands during sustained vegetative hydration.
2. **NB-LRR Disease Resistance Gene Families (OG0000050, OG0000049):** $+22$, $+17$ genes in *V. peripherica*. Protects active green foliar tissue against pathogen attacks in year-round vegetative states.
3. **DUF295 Domain Proteins of Unknown Function (OG0000009):** $+55$ genes in *V. peripherica* vs. $+16$ in *V. tubiflora*.
4. **ADP-Binding Proteins (OG0000015):** $+40$ genes in *V. peripherica* vs. $+10$ in *V. tubiflora*.
5. **Peptidase A1 Family (OG0000052):** $+19$ genes in *V. peripherica* vs. $0$ in *V. tubiflora*.

---

## 5. Selection Pressure Estimation & Functional Divergence (Ka/Ks & HyPhy)

### 5.1 Pairwise Codeml Selection Rates across Homologous Pairs

| Homologous Gene Pair | Non-Synonymous Rate ($Ka$) | Synonymous Rate ($Ks$) | Selection Ratio ($Ka/Ks$) | Selection Regime |
|---|:---:|:---:|:---:|:---:|
| **VpOSCA1.1 / VtOSCA1.1** | 0.0120 | 0.0429 | **0.2794** | Strong Purifying Selection |
| **VpOSCA1.2 / VtOSCA1.2** | 0.0397 | 0.1114 | **0.3560** | Strong Purifying Selection |
| **VpOSCA1.3 / VtOSCA1.3** | 0.0230 | 0.0795 | **0.2889** | Strong Purifying Selection |
| **VpOSCA1.4 / VtOSCA1.4** | 0.0867 | 0.1209 | **0.7172** | Relaxed Purifying Selection |
| **VpOSCA1.5 / VtOSCA1.5** | 0.0687 | 0.1035 | **0.6638** | Relaxed Purifying Selection |
| **VpOSCA2.1 / VtOSCA2.1** | 0.0225 | 0.0784 | **0.2870** | Strong Purifying Selection |
| **VpOSCA2.2 / VtOSCA2.2** | 0.0626 | 0.0992 | **0.6317** | Relaxed Purifying Selection |
| **VpOSCA2.3 / VtOSCA2.3** | 0.0046 | 0.0886 | **0.0518** | Ultra-Conserved Purifying Selection |
| **VpOSCA2.4a / VpOSCA2.4b (Paralogs)** | 0.0443 | 0.1228 | **0.3606** | Purifying Selection |
| **VpOSCA2.4a / VtOSCA2.4** | 0.0367 | 0.1230 | **0.2987** | Strong Purifying Selection |
| **VpOSCA2.4b / VtOSCA2.4** | 0.0177 | 0.0361 | **0.4909** | Moderate Purifying Selection |
| **VpOSCA2.5 / VtOSCA2.5** | 0.0170 | 0.0636 | **0.2681** | Strong Purifying Selection |
| **VpOSCA3.1 / VtOSCA3.1** | 0.0231 | 0.0520 | **0.4436** | Moderate Purifying Selection |
| **VpOSCA3.2 / VtOSCA3.2** | 0.0216 | 0.0663 | **0.3260** | Strong Purifying Selection |
| **VpOSCA4.1 / VtOSCA4.1** | 0.0123 | 0.0824 | **0.1498** | Strong Purifying Selection |
| **Mean Genomic Pairwise Values** | **0.0339** | **0.0838** | **0.3542** | **Global Purifying Selection ($Ka/Ks < 1$)** |

### 5.2 Clade-Specific Selection Intensity (HyPhy RELAX)
- **OSCA1 Subfamily (10 genes):** Selection intensity parameter $K = 0.9215$ ($p = 0.5957$). **No significant relaxation/intensification.** Both lineages maintain identical, stringent purifying selection to preserve core baseline osmosensing.
- **OSCA2 Subfamily (11 genes):** Selection intensity parameter $K = 0.2828$ ($p = 3.4 \times 10^{-5}$). **Highly significant selection relaxation in *V. tubiflora*.**
- **OSCA3+4 Subfamily (6 genes):** Selection intensity parameter $K = 0.1349$ ($p = 0.0061$). **Extremely significant selection relaxation in *V. tubiflora*.**
- **Ecological Mechanism:** Quiescent anhydrobiosis in *V. tubiflora* suspends daily functional metabolic demands on OSCA2 and OSCA3+4 channels during prolonged desiccation, relaxing selective constraints and facilitating neutral sequence drift, while the evergreen *V. peripherica* actively deploys and constrains these channels daily.

### 5.3 Site-Specific Selection Acceleration (HyPhy Contrast-FEL)
- **OSCA1 Clade:** 6 significant sites ($p \le 0.05$). Local Site 181 (Global 484, $p = 0.035, \beta_\text{Test} = 8.20, \beta_\text{Ref} = 0.03$) and Local Site 710 (Global 1232, $p = 0.020, \beta_\text{Test} = 7.66, \beta_\text{Ref} = 0.00$) show positive acceleration in *V. tubiflora*.
- **OSCA2 Clade:** 14 significant sites (8, 71, 76, 147, 191, 241, 270, 308, 394, 395, 432, 596, 720, 824) displaying extreme positive acceleration in *V. peripherica* ($\beta_\text{Ref} \gg 0$) and strict constraint in *V. tubiflora* ($\beta_\text{Test} \approx 0$).
- **OSCA3+4 Clade:** Local Site 593 (Global 1094, $p = 0.0085, \beta_\text{Test} = 24.72, \beta_\text{Ref} = 0.018$) represents a strong diversification hotspot in *V. tubiflora*.

