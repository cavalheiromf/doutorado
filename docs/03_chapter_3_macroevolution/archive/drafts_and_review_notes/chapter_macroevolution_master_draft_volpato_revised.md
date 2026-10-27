# Phylogenomic Context, Gene-Family Turnover and Coding-Sequence Divergence in Velloziaceae

**Mariana Feitosa Cavalheiro**$^{1,2,*}$, **Isabel Rodrigues Gerhardt**$^{1,2,3}$

$^{1}$ Institute of Biology, State University of Campinas (UNICAMP), Campinas, São Paulo, Brazil  
$^{2}$ Center for Molecular Biology and Genetic Engineering (CBMEG), State University of Campinas (UNICAMP), Campinas, São Paulo, Brazil  
$^{3}$ Brazilian Agricultural Research Corporation (Embrapa Digital Agriculture), Campinas, São Paulo, Brazil  
$^{*}$ Corresponding author: Mariana Feitosa Cavalheiro (marianacavalheiro@unicamp.br)

---

<!-- Working revision, 2026-09-15. Consolidated master; previous manuscript preserved in the review archive. Decisions and unresolved checks: ../../chapter_macroevolution/docs/reviews/volpato_master_review_2026-09-15.md -->

## Abstract

Contrasting responses to water loss in Velloziaceae motivate investigation of the genomic differences associated with these strategies. We compared seven annotated angiosperm genomes to characterize gene-family turnover, duplication architecture and coding-sequence divergence, while distinguishing these observations from hypotheses about the origin of desiccation tolerance. A phylogenomic supermatrix of 1,513 single-copy orthologs and 732,066 amino acid positions supported the relationships among the sampled taxa. Under the specified calibrations, the two-chain molecular-dating summary placed the sampled *Xerophyta–Vellozia* divergence at 33.77 Ma (95% equal-tailed credible interval: 22.41–48.11 Ma) and the *V. peripherica–V. tubiflora* divergence at 9.68 Ma (5.85–15.72 Ma). CAFE5 analyses identified 196 families with significant turnover in every retained run of the k=2, k=3 and k=4 rate models. Another 58 families were significant in every k=3 run but not in every retained k=2 run, providing an additional set whose support depends on the rate-model configuration. Local tandem and proximal duplicates accounted for 21.25% of annotated genes in *V. peripherica* and 15.96% in *V. tubiflora*, providing structural context for selected copy-number differences. Among 16,609 reciprocally unique ortholog pairs, 16,567 passed estimation filters and 233 had $\omega>1$; these ratios are a descriptive screen, not statistically confirmed positive selection. Together, the analyses prioritize genomic candidates for investigating contrasting water-loss responses. They do not establish the ancestral desiccation phenotype, a secondary loss of tolerance in *V. peripherica*, or adaptive causes of the observed genomic differences.

**Keywords:** Velloziaceae; desiccation tolerance; phylogenomics; molecular dating; CAFE5; orthology; coding-sequence divergence; *campos rupestres*.

---

# 1. Introduction

## 1.1 Environmental context and contrasting water-loss responses

The Brazilian *campos rupestres* contain diverse plant communities associated with rocky substrates, nutrient-poor soils and heterogeneous water availability (Silveira et al., 2016; Morellato & Silveira, 2018). These conditions provide a context for investigating how related plants differ in their responses to water loss. Velloziaceae is particularly relevant because it includes desiccation-tolerant and desiccation-sensitive species, allowing comparisons within a shared phylogenetic framework.

Vegetative desiccation tolerance permits recovery after extensive tissue dehydration, whereas avoidance mechanisms limit tissue water loss. Physiological work in Velloziaceae has identified a trade-off between productivity under mild drought and survival under extreme drought (Teodoro et al., 2021). Such findings motivate comparative genomic questions, but measurements from other species cannot be assigned directly to the focal species. In this study, *V. tubiflora* and *V. peripherica* are treated as the desiccation-tolerant and avoidant focal representatives, respectively. Their contrasting classifications define the biological comparison; detailed claims about their mortality thresholds, hydraulic mechanisms and year-round carbon balance require direct physiological evidence.

## 1.2 Genomic history and the origin of desiccation tolerance

The distribution of Velloziaceae across Africa, South America and Asia has motivated phylogenetic and biogeographic investigation (Mello-Silva et al., 2011; Alcantara et al., 2018). A dated phylogeny provides temporal context for these comparisons, but a divergence date does not independently reconstruct ancestral geographic ranges or the time and direction of dispersal. Likewise, the age of a clade cannot establish whether its ancestor was desiccation tolerant.

The genome of *Xerophyta viscosa* provides a comparative reference for investigating desiccation-related functions (Costa et al., 2017). Shared gene families may reflect an inherited repertoire, whereas copy-number differences may identify lineage-specific changes. However, the presence or expansion of a family does not demonstrate that it performed the same physiological role in an ancestor or in all descendant species. Ancestral retention, independent recruitment and changes in regulation remain alternative explanations unless phenotypic history and function are evaluated explicitly.

## 1.3 From genomic differences to functional hypotheses

Comparative analyses can distinguish several dimensions of genomic divergence. Gene-family models evaluate copy-number trajectories conditional on a species tree and model assumptions. Genomic position and collinearity describe the structural context of duplicated genes. Pairwise coding-sequence comparisons quantify divergence between aligned orthologs. These dimensions provide complementary evidence, but they answer different questions and should not be combined into an unsupported claim of adaptation.

For *V. peripherica* and *V. tubiflora*, the immediate question is which differences in gene repertoire and duplication architecture are supported by the available data. Connecting those differences to water-loss strategy requires additional evidence: intact gene models, reconciled functional annotations and a relevant role during dehydration or rehydration. Because only one focal avoidant species is sampled, the comparison does not isolate a general effect of the avoidant phenotype from lineage-specific history.

## 1.4 Objectives and scope of inference

This study aimed to characterize gene-family size variation and duplication architecture across the sampled Velloziaceae genomes within a phylogenomic and temporal framework. We assessed the stability of family-level turnover evidence across CAFE5 configurations, examined reconstructed changes on focal branches, and used duplication classifications and genomic positions to evaluate selected copy-number differences between the two *Vellozia* species. A complementary analysis screened coding-sequence divergence among reciprocally unique ortholog pairs for subsequent investigation of selective pressure.

These analyses prioritize candidates for investigating contrasting water-loss responses. They do not directly test whether desiccation tolerance was ancestral, whether *V. peripherica* lost it secondarily, or whether a particular dispersal route explains the modern distribution. Those hypotheses require broader phenotypic and taxonomic sampling, ancestral-state or biogeographic models, and independent functional evidence.

# 2. Materials and Methods

## 2.1 Taxon sampling and protein datasets

The comparative panel comprised *Vellozia peripherica*, *V. tubiflora*, *Xerophyta viscosa*, *Acanthochlamys bracteata*, *Pandanus tectorius*, *Dioscorea alata* and *Arabidopsis thaliana*. The first four provide the sampled Velloziaceae comparison; the remaining species provide outgroup context. This panel represents selected lineages rather than complete sampling of the family or of the higher clades represented by the outgroups.

The archived OrthoFinder input contained 191,075 protein sequences: 26,466 in *V. peripherica*, 25,551 in *V. tubiflora*, 26,969 in *X. viscosa*, 22,914 in *A. bracteata*, 28,399 in *P. tectorius*, 33,227 in *D. alata* and 27,549 in *A. thaliana*. These counts were checked against the run's per-species statistics. The supplied datasets were designated canonical proteomes. Canonical-transcript selection reduces isoform redundancy but does not itself validate gene-model completeness or remove all annotation artifacts.

<!-- Pending before submission: document assembly and annotation accessions, preprocessing scripts and species-specific physiological sources. The input counts above do not independently verify all preprocessing claims in the earlier draft. -->

## 2.2 Orthology inference and supermatrix assembly

Orthology was inferred with OrthoFinder v3.1.5 (Emms & Kelly, 2015, 2019). The archived log records DIAMOND for similarity searches, FAMSA for alignment and FastTree for gene-tree inference, with BLOSUM62, gap-opening and gap-extension scores of 11 and 1, and an MCL inflation value of 1.2. The run assigned 178,019 proteins (93.2%) to 17,750 orthogroups; 9,826 groups contained all seven species and 1,513 contained one sequence from each species.

The 1,513 single-copy groups provided the phylogenomic loci. Protein sequences were aligned with MAFFT v7.520 using automatic algorithm selection (`--auto --quiet`; Katoh & Standley, 2013). Alignment columns with a gap fraction greater than 0.5 were removed by the accompanying trimming script. The trimmed loci were concatenated into a 732,066-position amino acid supermatrix, with locus coordinates recorded in `partitions.nexus`. All species were represented at every locus, but gaps and ambiguous characters remained within alignments. This distinction separates complete taxon occupancy from complete site coverage.

The pairwise sequence-divergence analysis used a different inclusion criterion: reciprocal uniqueness between the two focal species, irrespective of copy number in the other species. The 17,571 orthology-table rows containing one gene on each side were therefore not all strict 1:1 pairs; exclusion of genes with additional focal-species partners yielded the 16,609 pairs described in Section 2.6.

## 2.3 Phylogenomic inference and concordance

The concatenated alignment was analyzed with IQ-TREE v2.3.6 under a partitioned maximum-likelihood framework (Minh et al., 2020). ModelFinder selected amino acid models for the locus partitions, and branch support was assessed using 1,000 ultrafast bootstrap replicates (Kalyaanamoorthy et al., 2017; Hoang et al., 2018). The results reported here come from `iqtree_pan_velloziaceae_7taxa.iqtree`, rather than the earlier six-taxon report.

Gene and site concordance factors (gCF and sCF) were used to describe disagreement among loci and sites. The gCF denominator is the number of decisive gene trees for a branch; the archived table records 1,513 decisive trees for each of the four evaluated branches. Individual gene trees were also supplied to ASTRAL-III for a coalescent species-tree estimate (Zhang et al., 2018a). Concordance and coalescent results complement bootstrap support and do not identify the biological cause of discordance on their own.

## 2.4 Molecular dating and separation of archived analysis versions

Divergence times were estimated using MCMCtree in PAML v4.10.8 (Yang, 2007), with the seven-species amino acid supermatrix and fixed species-tree topology. The archived configuration used an independent-rates clock (`clock = 2`), a Poisson amino acid model with five Gamma categories (`model = 0`, `alpha = 0.5`, `ncatG = 5`), `BDparas = 1 1 0.1`, `rgene_gamma = 2 20 1` and `sigma2_gamma = 1 10 1`. Approximate likelihood calculations supplied the branch-length information used in MCMC sampling (dos Reis & Yang, 2011).

Time was scaled in units of 100 Ma. The input specified intervals of 130–145 Ma for the sampled root, 115–128 Ma for *Dioscorea* versus the sampled Pandanales, 90–105 Ma for *Pandanus* versus the sampled Velloziaceae, 75–90 Ma for *Acanthochlamys* versus the sampled *Xerophyta–Vellozia* clade, and 2–25 Ma for the focal *Vellozia* split. These bounds document the archived configuration. Their individual fossil or secondary-calibration provenance and assignment to the sampled nodes require reconciliation with the cited dating literature before they can be described as independently validated fossil constraints.

The *Xerophyta–Vellozia* node had no direct calibration, but its age remained conditional on the calibrated ancestral and descendant nodes, the joint time prior and the substitution and clock models. A prior-only run was archived for comparison; lack of a direct calibration does not make the estimate independent of the surrounding temporal constraints.

The updated summary presented in Table 1 uses two chains with seeds 1234567 and 7654321. Each was configured with `burnin = 50000`, `sampfreq = 100` and `nsample = 30000`. The archived files contain 30,001 recorded states each, and the summary uses all rows. Intervals were calculated from the combined 2.5th and 97.5th percentiles and are therefore 95% equal-tailed credible intervals, despite the use of “HPD” in the source column names. The archived diagnostics include per-chain ESS, Gelman–Rubin R-hat and an ESS computed from the concatenated chains. That last statistic is not evidence that each chain attained ESS > 200.

The current Gamma CAFE5 analyses used the updated two-chain chronogram. Their reported tree has a root age of 138.431 Ma, a sampled *Xerophyta–Vellozia* divergence of 33.7699 Ma and a focal *Vellozia* divergence of 9.6839 Ma, consistent with the rounded estimates in Table 1. Turnover estimates remain conditional on this time tree and its calibrations.

## 2.5 Gene-family turnover and duplication architecture

Gene-family sizes were modeled with CAFE5 v5.1.0 (Mendes et al., 2020). Of the 17,750 orthogroups, 15 with at least 100 genes in a species were removed as a numerical safeguard, leaving 17,735 input families. The root-presence filter retained 12,276 families for model estimation and testing. The current Gamma analyses used the updated dated tree identified in Section 2.4.

A symmetric count-error model was estimated from replicated homogeneous-rate fits and then fixed in the Gamma analyses. Under the adopted parameterization, $\epsilon=0.00588995$ is the probability of each adjacent one-copy error away from the boundary, giving approximately $2\epsilon=0.0117799$ combined probability for a one-copy discrepancy. This models count uncertainty; it does not independently validate assemblies, annotations or orthogroup composition.

Five optimization runs were evaluated for each Gamma discretization (k=2, k=3 and k=4), where k denotes the number of discrete rate categories used to represent variation in turnover rates among families. Four k=2 runs were retained; replicate 04 reached an inferior optimum and recorded a family failure. All five k=3 runs were retained. Four k=4 runs were retained; replicate 01 reached an inferior optimum and recorded a family failure. The primary reconstruction used k=2 replicate 01. Benjamini–Hochberg correction was applied across all 12,276 tested families within each run. 

Families were grouped by the repeatability of family-level significance across rate models. The cross-model consensus (196 families; designated Tier A in the supplementary tables) required q ≤ 0.05 in every retained k=2 and k=3 run. Every family in this consensus also met the threshold in every retained k=4 run. The additional k=3-supported set (58 families; designated Tier B in the supplementary tables) required q ≤ 0.05 in all five k=3 runs but failed that threshold in at least one retained k=2 run. The two sets are disjoint and together comprise the 254-family k=3 consensus. The runs are repeated optimizations of the same biological dataset. Family-level significance does not establish independently significant changes on individual branches; directional changes are Viterbi reconstructions.

Two distinct directional summaries were used. The sign of the reconstructed change describes all positive or negative changes within the cross-model consensus. The terminal-enrichment indicator additionally requires the focal species to have strictly more copies than the other sampled Velloziaceae. Thus, counts from the terminal-enrichment indicator are subsets of positive changes and should not be labeled as all expansions. Ancestral sign stability was assessed separately across retained k=3 runs.

Duplication architecture in the two *Vellozia* genomes was described using the archived MCScanX classifications (Wang et al., 2012) and JCVI collinearity analyses. MCScanX used the full intra-genomic homology input rather than the JCVI-filtered input, preserving local homologous hits. The documented parameters were `-k 50 -g -1 -s 5 -e 1e-5 -w 5 -m 25 -n 10`; classifications comprised WGD/segmental, tandem, proximal, dispersed and singleton categories. Category proportions use the complete annotated gene complement of each species as denominator. The combined WGD/segmental class describes collinearity and does not by itself date a whole-genome duplication. Genomic positions and inherited functional descriptions were used for candidate interpretation, not as independent tests of physiological function.

## 2.6 Pair-Specific Orthology and Coding-Sequence Divergence

The pairwise analysis used orthology relationships inferred by OrthoFinder v3.1.5 in the seven-species panel. All relationships in the directional *V. peripherica*–*V. tubiflora* orthologue tables were considered, including one-to-many and many-to-one entries. A pair was retained only when each focal gene had exactly one partner in the other focal species across the complete relationship tables. The two directional tables described the same relationships. Gene presence and copy number in the other five species did not restrict inclusion, and an orthogroup could contain several independent 1:1 focal pairs. Consequently, the pair identifier, rather than the orthogroup identifier alone, was used as the unique analysis unit.

Proteins and coding sequences (CDS) were retrieved using exact transcript identifiers from the Vper.hapA.v1 and Vtub.hapA.v1 annotations. Protein–CDS correspondence was validated by translation; CDS with incompatible translations, internal stops, or lengths not divisible by three were rejected, while terminal stops were permitted. Each protein pair was aligned globally with Biopython v1.87 PairwiseAligner (Cock et al., 2009), using BLOSUM62, a gap-opening score of −10 and a gap-extension score of −0.5, including terminal gaps. The first optimal alignment was retained when scores were tied. CDS were projected onto the complete protein alignment before columns containing a gap, a stop codon, or any nucleotide other than A/C/G/T in either sequence were removed. Retained codons were checked against their original CDS coordinates and protein translations. Alignments with fewer than 30 retained codons were excluded.

Pairwise nonsynonymous ($dN$, or $Ka$) and synonymous ($dS$, or $Ks$) substitution-rate estimates and their ratio ($\omega = dN/dS$) were obtained using the approximate Yang–Nielsen method in yn00/PAML v4.10.10 (Yang & Nielsen, 2000; Yang, 2007), with the standard genetic code and options `icode = 0`, `weighting = 0`, and `commonf3x4 = 0`. Only Yang–Nielsen estimates and their reported standard errors were extracted. Nonfinite or negative estimates, $dS \le 0$, $\omega \ge 99$, and $dS \ge 2$ were excluded from the descriptive screen. The upper $dS$ threshold was an operational filter, not a direct saturation test. Additional review flags identified $dS < 0.01$, $SE(dS) \ge dS$, $dN \ge 2$, protein identity below 70%, or retained-codon coverage below 70% of either protein. These flags were not significance tests or automatic exclusions. Values below one were summarized without dividing them into purportedly neutral and relaxed-selection classes.

Functional descriptions were inherited from the existing annotation tables; no new domain annotation or enrichment test was performed. PPR-related pairs were identified by the presence of PPR or pentatricopeptide in either focal description. Among pairs with $\omega > 1$, resolved OrthoFinder gene trees were inspected for the number and species composition of leaves descending from the focal most recent common ancestor (MRCA). This characterized local topology, without assessing node support or restricting possible outgroups to that MRCA.

Review priorities were assigned after examining the results and are therefore exploratory. Among the 202 sister pairs, those without flags and with $dS \ge 0.02$, protein identity $\ge 70\%$, and coverage $\ge 70\%$ formed a 152-pair review set. Requiring at least 100 retained codons, $SE(dS)/dS < 0.5$, and $\omega \ge 1.5$ further identified 17 pairs for descriptive inspection. Their analyzed codon alignments were examined for differing codons encoding the same or different amino acids. These endpoint counts do not reconstruct the number or direction of historical substitutions. No likelihood-ratio test, branch/site selection model, multiple-testing correction, or functional enrichment analysis was conducted in this stage. The ratios represent a descriptive screen and cannot assign selection to either focal lineage.

# 3. Results

## 3.1 Phylogenomic relationships and alignment coverage

The seven-taxon supermatrix comprised 1,513 single-copy loci and 732,066 amino acid positions. Counting gaps and the characters ? and X in the archived PHYLIP alignment yielded 3.56% missing/ambiguous positions in *Arabidopsis*, 3.99% in *Dioscorea*, 1.92% in *Pandanus*, 3.65% in *Acanthochlamys*, 15.33% in *Xerophyta*, 1.86% in *V. peripherica* and 1.95% in *V. tubiflora*. All taxa were present at each locus, but the matrix was not gap-free.

The seven-taxon IQ-TREE report records a log-likelihood of −6,024,349.3677 (standard error 4,214.1494) and a total tree length of 2.0089 substitutions per site. Internal branches account for 0.4110 substitutions per site. All internal branches had 100% ultrafast bootstrap support. Within the sampled Velloziaceae, the focal *Vellozia* species grouped together, with *Xerophyta* sister to that pair and *Acanthochlamys* sister to the sampled core clade.

Gene and site concordance were highest for the focal *Vellozia* split (gCF 93.92%; sCF 86.44%) and sampled *Xerophyta–Vellozia* grouping (97.16%; 79.12%). The corresponding values were 88.04% and 55.43% for the sampled Velloziaceae grouping, and 62.46% and 42.59% for the deeper sampled Pandanales grouping. ASTRAL recovered the same topology with a normalized quartet score of 0.9236. These results support the sampled relationships while showing that maximal bootstrap support does not imply uniform agreement among genes and sites.

## 3.2 Divergence-time estimates and sampling diagnostics

Under the archived calibration scheme, the two-chain mean age of the sampled *Xerophyta–Vellozia* split was 33.77 Ma, with a 95% equal-tailed credible interval of 22.41–48.11 Ma. The focal *Vellozia* split was estimated at 9.68 Ma (5.85–15.72 Ma). These intervals span broader periods than the geological epochs containing their means. The other node estimates and rate parameters are reported in Table 1.

Archived R-hat values were below 1.01 for all reported parameters. The *Xerophyta–Vellozia* node nevertheless had per-chain ESS values of 99.6 and 129.5, below the target of 200. Its concatenated-series ESS was 261.8. These diagnostics do not justify describing every node as having high effective sample size, and the combined ESS should not replace inspection of individual chains.

Table 1. Two-chain dating summary transcribed from `mcmctree_high_ess_convergence_summary.tsv`. Time values are in Ma; μ is in substitutions per site per 100 Myr. The intervals are percentiles, not HPD estimates. Diagnostics are those archived in the analysis and were not recalculated as a new multichain assessment.

| Parameter | Sampled split / parameter | Calibration interval (Ma) or prior | Mean | 95% equal-tailed interval | Chain 1 mean (ESS) | Chain 2 mean (ESS) | Concatenated ESS | R-hat |
|:--|:--|:--|--:|:--|:--|:--|--:|--:|
| t_n8 | Sampled root | 130–145 | 138.43 | [130.19, 145.11] | 138.45 (1760.7) | 138.41 (1691.1) | 3445.2 | 1.0000 |
| t_n9 | Dioscorea vs. sampled Pandanales | 115–128 | 122.68 | [115.48, 128.07] | 122.78 (1552.1) | 122.59 (1348.1) | 2866.0 | 1.0007 |
| t_n10 | Pandanus vs. sampled Velloziaceae | 90–105 | 100.39 | [92.69, 105.16] | 100.42 (988.8) | 100.36 (730.8) | 1729.3 | 1.0001 |
| t_n11 | Acanthochlamys vs. sampled core | 75–90 | 78.02 | [74.43, 85.45] | 77.88 (938.0) | 78.15 (601.8) | 1471.0 | 1.0021 |
| t_n12 | Sampled Xerophyta–Vellozia split | No direct calibration | 33.77 | [22.41, 48.11] | 33.26 (99.6) | 34.28 (129.5) | 261.8 | 1.0063 |
| t_n13 | V. peripherica–V. tubiflora split | 2–25 | 9.68 | [5.85, 15.72] | 9.49 (257.8) | 9.88 (265.5) | 516.3 | 1.0061 |
| mu | Mean substitution rate | G(2,20) | 0.2637 | [0.2105, 0.3286] | 0.2646 (869.0) | 0.2628 (1056.7) | 1870.3 | 1.0008 |
| sigma2 | Rate-variance parameter | G(1,10) | 0.1190 | [0.0455, 0.2669] | 0.1170 (1365.1) | 0.1211 (802.9) | 1987.3 | 1.0012 |

The CAFE5 runs described below use the earlier tree documented in Section 2.4. Differences between that tree and Table 1 are retained explicitly rather than attributing the same turnover results to a new temporal input.

## 3.3 Family-level turnover and structural context of copy-number differences

The representative error-corrected k=2 reconstruction (replicate 01) had $\lambda=0.00362378$ per gene per Ma and shape parameter $\alpha=0.899434$, with $-\ln L\approx107,704$ (the reported likelihood is rounded to an integer). The 196-family cross-model consensus provides repeatable family-level evidence under the retained configurations. These estimates are conditional on the dated tree, count-error model and orthogroup definitions.

Within the cross-model consensus, the representative k=2 reconstruction contains 117 positive and 19 negative changes at the sampled *Xerophyta–Vellozia* ancestor (Node 12). Of the 117 positive changes, 104 retain a positive sign in all five k=3 runs, whereas 106 retain a positive sign in all four retained k=4 runs. These counts describe directional stability under each sensitivity model; they do not establish independently significant branch changes or the ancestral desiccation phenotype.

On the terminal branches, the cross-model consensus contains 86 positive and 64 negative changes in *V. peripherica*, and 56 positive and 80 negative changes in *V. tubiflora*. The more restrictive terminal-enrichment indicator retains 73 and 35 families, respectively, because it additionally requires the highest extant count among the sampled Velloziaceae. These subsets should not be substituted for all positive changes when describing branch totals or calculating a balance.

The annotated genomes differ in their local duplication classifications. *V. peripherica* contains 5,625 tandem or proximal genes (21.25% of 26,466 annotated genes), compared with 4,078 (15.96% of 25,551) in *V. tubiflora*. The difference is 1,547 genes. WGD/segmental classifications account for 7,459 genes (28.18%) and 7,224 (28.27%), respectively. These are descriptive proportions; similar WGD/segmental fractions do not independently establish an ancestral polyploidization event, and the local-duplicate difference does not estimate an adaptive duplication rate.

Several prioritized families combine higher *V. peripherica* counts with local arrays in the archived structural analysis. Examples include the provisionally DREB/CBF-like family OG0000306 (11 versus 3 copies) and the UDP-glycosyltransferase-associated family OG0000281 (14 versus 4). Their reported local clusters provide positional context for the copy-number differences, while biochemical specificity and roles during water loss remain to be established.

For the provisionally NDH-associated families OG0000014, OG0000156 and OG0000278, the v2 master table records 67, 18 and 6 genes in *V. peripherica*, totaling 91 annotated genes. The corresponding reconstructed terminal changes are +31, +8 and +3, totaling +42. The value 42 therefore refers to a sum of inferred changes, not the number of present-day anchored copies. Local arrays reported for these families motivate further investigation but do not demonstrate enhanced electron transport or coordinated physiological activity.

Other examples require reconciliation before functional interpretation. OG0000026 belongs to the cross-model consensus and contains 21 *V. peripherica* copies and a reconstructed change of +4, rather than the previously stated F-box expansion of +51. For OG0000317 and OG0000332, the annotation discrepancy involves two sources: the Vellozia descriptions are pre-mRNA-splicing factor and glycine-rich RNA-binding protein, whereas the actual Arabidopsis members used in the enrichment mapping are the plastid reference sequences NP_051114.1 (ArthCp079/ndhA) and NP_051113.1 (ArthCp078/ndhI). The archived KEGG mapping assigns both to ath00190. This establishes the provenance of their NDH-associated pathway labels, not the function or integrity of every Vellozia model. In V. tubiflora, all 28 and 25 models, respectively, occur on unplaced contigs; in V. peripherica, all five OG0000317 models are unplaced, whereas OG0000332 has two chromosome-anchored and five unplaced models. These positions warrant checks for redundancy, fragmentation and organellar sequence representation but do not demonstrate artifacts. Neither contig placement nor chromosomal anchoring alone establishes copy authenticity or functionality. The annotation sources and gene positions are documented in [the reconciliation record](../../chapter_macroevolution/docs/reviews/annotation_provenance_2026-09-15.md).

### 3.3.1 Rate-heterogeneity sensitivity

The k=3 consensus contains 254 families: 196 in the cross-model consensus and 58 in the additional k=3-supported set. In the representative k=2 reconstruction, these 58 candidates include 31 positive changes at Node 12, 22 in *V. peripherica* and 11 in *V. tubiflora*. These overlapping subsets describe reconstructed directions rather than separately significant branch events. The representative k=3 and k=4 fits had reported −lnL values of approximately 107,175 and 106,856, with turnover scales of 0.00327108 and 0.00318130 per gene per Ma and shape parameters of 1.02510 and 1.01791, respectively.

### 3.3.2 Functional enrichment in the current consensus

Functional over-representation was recalculated from the current family table using category-specific annotation universes. Among 7,269 primary inferential tests, the mitochondrion term (GO:0005739) in the general cross-model consensus contrast was the only term classified as confirmatory: 53 of 154 GO cellular-component-annotated consensus families were associated with this term (global q = 0.02045; stratified p = 0.04070). Another 21 terms were classified as suggestive with imbalanced annotation opportunity, and 53 as permutation-discordant. Conditional contrasts contained no terms meeting the balanced confirmatory or suggestive criteria. The mitochondrial annotation signal does not establish mitochondrial function in each focal gene or a lineage-specific physiological mechanism.

## 3.4 Pairwise Coding-Sequence Divergence Between the Two Vellozia Species

Reciprocal uniqueness filtering retained 16,609 ortholog pairs across 12,158 orthogroups. Of 17,571 directional-table rows containing one gene on each side, 962 were excluded because at least one gene had additional partners elsewhere in the focal-species relationships. All 1,513 pairs from the seven-species single-copy subset were included in the expanded analysis.

Estimation filters retained 16,567 pairs, while 26 had $dS \ge 2$ and 16 had $dS \le 0$. Among retained pairs, median $dN$, $dS$, and $\omega$ were 0.0217, 0.0784, and 0.2852, respectively. A total of 16,334 pairs had $\omega < 1$, whereas 233 had $\omega > 1$ (1.41% of retained pairs). Of the latter, 180 had no additional operational flags and 53 were flagged for review. Overlapping flags comprised low coverage in 29 pairs, $SE(dS) \ge dS$ in 18, protein identity below 70% in 12, and $dS < 0.01$ in four. The highest ratio, 4.6746 for PAIR000254 (OG0000083), occurred with $dS = 0.0065$ and $SE(dS) = 0.0080$, illustrating why ranking by $\omega$ alone requires caution. None of the 343 pairs with PPR-related descriptions had $\omega > 1$.

The 233 pairs belonged to 220 orthogroups. In resolved gene trees, 202 focal pairs formed two-leaf sister clades. Twelve had a focal MRCA containing additional species without repeated species, and one had multiple *X. viscosa* leaves within that MRCA; 18 had no corresponding tree in the resolved-tree file examined. The 202 sister clades occurred within larger trees containing 4–154 leaves. Thus, sister-pair status does not imply that homologues from other species are absent or that future multispecies analyses are unavailable. The local topology screen did not establish statistical support for these nodes or validate a set of outgroups.

The operational review criteria yielded 152 sister pairs, of which 17 met the additional length, precision, and ratio thresholds (Table 2). Direct inspection of their retained codon alignments counted 200 differing codons encoding the same amino acid and 666 encoding different amino acids, with no ambiguous or stop codons retained. Each pair contained 17–136 differing codons. These descriptive counts are unnormalized for mutational opportunities and do not demonstrate selection. Inherited descriptions among the 17 pairs included GGL domain, HSP20, reticulon-like protein, stress-responsive A/B barrel domain, and cytochrome b5; several descriptions were uncharacterized or nonspecific.

The current pairwise alignments retained ten pairs with $\omega > 1$ within the original 1,513-pair subset; nine overlapped the ten candidates from the corrected seven-species alignment analysis. This comparison reflects changes in alignment context and retained columns as well as the broader gene set. The current analysis supersedes the earlier, uncorrected 250-candidate screen, whose protein–CDS coordinate mismatch invalidated its numerical estimates and PPR selection claims.

The complete estimates are available in [the pairwise results table](../../chapter_macroevolution/05_selection/pair_specific_2026-09-11/pairwise_kaks_all.tsv), with [the 233-pair screen](../../chapter_macroevolution/05_selection/pair_specific_2026-09-11/omega_gt1_screen.tsv), [gene-tree context](../../chapter_macroevolution/05_selection/pair_specific_2026-09-11/candidate_gene_tree_qc.tsv), and [the 17-pair alignment review](../../chapter_macroevolution/05_selection/pair_specific_2026-09-11/pair_only_alignment_review.tsv). An independent verification recorded concordance for all 16,609 pair relationships, codon alignments, and parsed yn00 outputs.


Table 2. The 17 pairs selected for descriptive alignment review after the operational prioritization in Section 2.6, ordered by estimated $\omega$. S and N count differing aligned codons encoding the same and different amino acids, respectively; they are endpoint observations, not estimates of synonymous and nonsynonymous substitution rates. Functional descriptions are inherited annotations and do not establish adaptive roles. Exact transcript identifiers and the full 233-pair screen are retained in the linked analysis files.

| Pair ID | Orthogroup | Codons | $dN$ | $dS$ | $\omega$ | $SE(dS)$ | S | N | Inherited description |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| PAIR010006 | OG0006667 | 278 | 0.1165 | 0.0556 | 2.0973 | 0.0147 | 7 | 41 | GGL domain |
| PAIR001656 | OG0000725 | 432 | 0.0423 | 0.0213 | 1.9884 | 0.0084 | 6 | 37 | Uncharacterized protein |
| PAIR014065 | OG0011114 | 171 | 0.1885 | 0.1003 | 1.8787 | 0.0290 | 3 | 48 | BEST Arabidopsis thaliana protein match is Calcium-binding EF hand family protein (TAIR AT1G64850.1) |
| PAIR005947 | OG0003176 | 427 | 0.1841 | 0.0984 | 1.8706 | 0.0108 | 79 | 34 | Uncharacterized protein |
| PAIR015881 | OG0013207 | 223 | 0.0831 | 0.0453 | 1.8354 | 0.0173 | 3 | 36 | Belongs to the small heat shock protein (HSP20) family |
| PAIR012619 | OG0009546 | 120 | 0.0991 | 0.0550 | 1.7999 | 0.0212 | 7 | 16 | Uncharacterized protein |
| PAIR000517 | OG0000202 | 318 | 0.0556 | 0.0309 | 1.7991 | 0.0122 | 5 | 35 | Uncharacterized protein |
| PAIR015246 | OG0012398 | 497 | 0.1515 | 0.0851 | 1.7792 | 0.0153 | 21 | 115 | UPF0481 protein At3g47200-like |
| PAIR003156 | OG0001457 | 213 | 0.1951 | 0.1112 | 1.7544 | 0.0270 | 10 | 60 | Reticulon-like protein |
| PAIR000722 | OG0000310 | 122 | 0.1338 | 0.0765 | 1.7498 | 0.0254 | 8 | 23 | Uncharacterized protein |
| PAIR001737 | OG0000758 | 223 | 0.1201 | 0.0742 | 1.6192 | 0.0197 | 13 | 44 | Whole genome shotgun sequence of line PN40024, scaffold_28.assembly12x (Fragment) |
| PAIR013513 | OG0010548 | 257 | 0.0634 | 0.0392 | 1.6182 | 0.0140 | 4 | 24 | Stress responsive A/B Barrel Domain |
| PAIR016214 | OG0013941 | 121 | 0.1062 | 0.0664 | 1.5995 | 0.0254 | 7 | 22 | Uncharacterized protein |
| PAIR004129 | OG0002016 | 194 | 0.1514 | 0.0948 | 1.5971 | 0.0259 | 9 | 49 | Uncharacterized protein |
| PAIR003730 | OG0001792 | 191 | 0.1259 | 0.0804 | 1.5648 | 0.0261 | 7 | 43 | May be involved in both secretory and endocytic intracellular trafficking in the endosomal prevacuolar compartments |
| PAIR016010 | OG0013453 | 168 | 0.1003 | 0.0661 | 1.5174 | 0.0201 | 6 | 27 | Uncharacterized protein |
| PAIR009133 | OG0005742 | 133 | 0.0561 | 0.0373 | 1.5021 | 0.0169 | 5 | 12 | Cytochrome b5 |


# 4. Discussion

## 4.1 What the temporal framework can establish

The dated phylogeny provides a conditional temporal context for the sampled relationships. Its estimated *Xerophyta–Vellozia* divergence is younger than the continental-separation interval invoked in discussions of strict Gondwanan vicariance (Mello-Silva et al., 2011; Alcantara et al., 2018). However, the focal age depends on surrounding temporal constraints whose justification needs to be established individually. Lack of a direct calibration at this node does not make the estimate an independent test of every competing geological scenario.

Post-breakup dispersal is compatible with a younger divergence estimate, but the current analysis does not reconstruct ancestral ranges, distinguish dispersal routes or infer its direction. Similarly, the divergence time is not a direct estimate of the arrival of a lineage in South America. Testing these scenarios requires broader taxon sampling, explicit biogeographic models and assessment of sensitivity to the calibrations. The earlier tree used for CAFE5 and the updated two-chain summary also need to remain distinct until turnover sensitivity is evaluated.

## 4.2 Genomic differences in the context of water-loss strategies

The two focal species differ in copy-number profiles and in the observed proportions of local duplicate classifications. These differences provide a basis for candidate prioritization, but they do not identify the ecological cause of divergence. A dated split that overlaps a period of climatic change does not demonstrate that aridification caused speciation or habitat partitioning. With one focal representative of avoidance, effects of phenotype and lineage history remain confounded.

The physiological trade-off documented in other Velloziaceae provides a useful hypothesis-generating context (Teodoro et al., 2021). It does not establish the mortality thresholds, hydraulic mechanisms or maintenance costs of the focal genotypes. Relating their genomic differences to performance will require direct measurements under comparable dehydration and rehydration conditions. This distinction allows a biological interpretation of the genomic comparison without assigning unmeasured physiological effects to its candidates.

## 4.3 Ancestral copy numbers and competing explanations for duplicate retention

Positive reconstructed changes at Node 12 describe the history of gene-family size under the fitted model. They do not reconstruct the ancestral state of desiccation tolerance or demonstrate that every affected family formed a stress-protective system. Shared gene families can support different functions in different lineages, and desiccation tolerance may involve regulatory recruitment of an inherited repertoire. Ancestral tolerance with secondary loss and independent recruitment remain alternatives to be tested rather than conclusions resolved by these counts.

The higher proportion of tandem and proximal classifications in *V. peripherica* provides structural context for selected local copy-number increases. Similar WGD/segmental proportions in the two genomes do not independently date a shared WGD or exclude other duplication and loss histories. Establishing the history of particular families requires gene trees, positional correspondence and validation of the annotated copies.

The proposal that maintaining an evergreen habit favors investment in repair, defense or environmental perception remains a functional hypothesis. The current analyses do not measure those maintenance costs and do not exclude demographic processes, relaxed constraint, dosage effects or other explanations for duplicate retention. Functional annotation does not demonstrate a specific biochemical role, and local arrays do not by themselves establish intact open reading frames or canonical read coverage. The provisional NDH-associated candidates therefore require validation before being linked to photosynthetic maintenance, while the source-dependent annotations of OG0000317 and OG0000332 require gene-level validation before their Vellozia members can support an energy-related mechanism. Their Arabidopsis-based KEGG assignments are traceable, but do not resolve that functional question.

## 4.4 Coding-Sequence Divergence and the Limits of Functional Interpretation

The predominance of $\omega < 1$ and the median ratio of 0.2852 are consistent with widespread constraint on coding-sequence divergence between the two focal species. The 233 ratios above one identify loci for further investigation, but they do not establish positive selection in either lineage. Pairwise estimates combine divergence along both lineages, and uncertainties in annotation, alignment, and synonymous divergence remain relevant even when operational quality flags are absent. In particular, the 53 flagged pairs warrant cautious interpretation, while the 17-pair review set represents a post hoc prioritization rather than a statistically supported subset.

The corrected analysis does not support the earlier claim of PPR enrichment among positively selected genes: none of the 343 pairs identified through PPR-related descriptions exceeded $\omega = 1$. This result does not exclude site-specific or lineage-specific evolution within PPR genes, nor does it negate possible roles of these proteins in organellar biology. It does mean that adaptive remodeling of organellar RNA editing cannot be inferred from the pairwise results presented here. Likewise, the presence of HSP20, reticulon-like, stress-responsive, and cytochrome b5 descriptions in the review set provides functional hypotheses, without demonstrating enrichment, physiological effects, or associations with the evergreen or resurrection phenotype.

The observed codon differences add a transparent account of the sequence comparisons but should not be interpreted as a ratio of evolutionary rates. Codons encoding different amino acids and those encoding the same amino acid have different mutational opportunities, and endpoint comparisons do not reconstruct intervening changes. The current stage therefore ends with a reproducible descriptive screen. Future selection tests would require validated multispecies codon alignments, appropriate gene-tree context, and an explicitly defined testing universe; the thresholds used to prioritize 17 pairs should not be treated as independent confirmation of the signal used to select them.

## 4.5 Functional priorities and connection to the following chapter

The next stage is to validate the gene models and functional assignments of prioritized families and test their behavior during dehydration and rehydration. Transcript abundance, protein abundance and physiological activity represent different levels of evidence and should be measured and interpreted accordingly. Comparisons that include additional tolerant and avoidant species would help distinguish lineage-specific features from associations with water-loss strategy.

Mechanosensitive OSCA channels provide a complementary focus for the following chapter because of their characterized roles in osmotic and mechanical signaling in model systems (Yuan et al., 2014; Zhang et al., 2018b; Liu et al., 2018; Thor et al., 2020). This rationale does not depend on claiming that the present pairwise screen demonstrates selection on mechanosensory pathways. Comparative analysis of these channels can instead ask whether their repertoire, structure or regulation differs between the focal species, with functional consequences treated as a separate question.

# 5. Conclusion

The sampled Velloziaceae genomes differ in gene-family size, local duplication architecture and coding-sequence divergence. The phylogenomic analysis supports the sampled relationships, while the dating estimates provide temporal context conditional on their calibrations. The 196-family turnover consensus, complemented by 58 model-sensitive families, and the structural information for selected candidates offer complementary criteria for prioritization. The pairwise screen adds 233 ratios above one for further investigation, without statistically confirmed positive selection or assignment of changes to either lineage.

These results support investigation of the genomic basis of contrasting water-loss responses. They do not establish ancestral desiccation tolerance, its secondary loss in *V. peripherica*, a particular route of intercontinental dispersal, or adaptive causes of duplicate retention. Resolving those hypotheses requires validated annotations, broader comparative sampling and evidence linking genomic differences to physiological responses.

# Statements & Declarations

> **Working-draft note:** The declarations below are retained from the supplied manuscript. Funding identifiers, deposition accessions, repository DOI and URL, license, author approval and institutional details have not been verified in this revision and require confirmation before publication.

## Funding
This research was supported by the São Paulo Research Foundation (FAPESP, grants 2019/18974-0 and 2021/04328-9 to MFC), the National Council for Scientific and Technological Development (CNPq, doctoral fellowship to MFC and research productivity grant to IRG), and the Coordination for the Improvement of Higher Education Personnel (CAPES, Finance Code 001).

## Author Contributions
**Mariana Feitosa Cavalheiro**: Conceptualization, Methodology, Software, Formal analysis, Investigation, Data Curation, Writing - Original Draft, Writing - Review & Editing, Visualization, Project administration. **Isabel Rodrigues Gerhardt**: Conceptualization, Resources, Supervision, Funding acquisition, Writing - Review & Editing. All authors read and approved the final manuscript.

## Data Availability
All raw sequencing reads, assembled genome sequences, and primary gene annotations generated for *Vellozia tubiflora* and *Vellozia peripherica* have been deposited in the NCBI BioProject database under accession PRJNA984512 and the Brazilian National System for the Management of Genetic Heritage and Associated Traditional Knowledge (SisGen) under registration A7B89C1. The 7-taxon canonical proteome datasets, OrthoFinder orthogroup assignments, trimmed supermatrix alignments, IQ-TREE 2 phylogenetic trees, PAML MCMCtree control and output files, CAFE5 gene family count matrices, are permanently archived in Zenodo (https://doi.org/10.5281/zenodo.12345678).

The current pairwise $Ka/Ks$ estimates, alignment-review tables, raw per-pair outputs, and provenance records are available locally in `chapter_macroevolution/05_selection/pair_specific_2026-09-11/`. These current files are the source for Section 3.4 and Table 2.

## Code Availability
All custom Python scripts and computational workflow pipelines used in this study—including canonical proteome extraction, parallel MAFFT alignment and supermatrix concatenation (`extract_align_concatenate_single_copy.py`), CAFE5 input filtering (`prep_family_cafe5.py`), pair-specific orthology and coding-sequence divergence calculation (`pair_specific_kaks.py`, `calculate_kaks_1to1.py`), candidate gene-tree quality control (`gene_tree_qc_candidates.py`), alignment review (`review_pair_only_alignments.py`), independent verification (`verify_pair_specific_kaks.py`, `verify_orthofinder_pair_proteins.py`), and functional annotation mapping—are openly available in the GitHub repository (https://github.com/mfcaval/doutorado-macroevolution) under an MIT License.

## Competing Interests
The authors declare that they have no competing financial or non-financial interests that could have appeared to influence the work reported in this paper.

## Acknowledgements
We thank the staff of the High-Performance Computing Center at CBMEG/UNICAMP for computational cluster support, the Instituto Chico Mendes de Conservação da Biodiversidade (ICMBio) for granting collection permits for *campos rupestres* field surveys, and members of the Laboratory of Plant Molecular Biology (UNICAMP) for constructive discussions during manuscript preparation.

# References

<!-- Bibliography restricted to cited entries. Metadata and claim support have not all been independently audited. -->

Alcantara S, Ree RH, Mello-Silva R (2018). Accelerated diversification and functional trait evolution in Velloziaceae reveal new insights into the biodiverse campos rupestres. *Annals of Botany*, 122(1): 165–180. https://doi.org/10.1093/aob/mcy063

Cock PJA, Antao T, Chang JT, Chapman BA, Cox CJ, Dalke A, Friedberg I, Hamelryck T, Kauff F, Wilczynski B, de Hoon MJL (2009). Biopython: freely available Python tools for computational molecular biology and bioinformatics. *Bioinformatics*, 25(11): 1422–1423. https://doi.org/10.1093/bioinformatics/btp163

Costa MC, Artur MAS, Maia J, et al. (2017). A footprint of desiccation tolerance in the genome of *Xerophyta viscosa*. *Nature Plants*, 3: 17038. https://doi.org/10.1038/nplants.2017.38

dos Reis M, Yang Z (2011). Approximate likelihood calculation on a phylogeny for Bayesian estimation of divergence times. *Molecular Biology and Evolution*, 28(7): 2161–2172. https://doi.org/10.1093/molbev/msr045

Emms DM, Kelly S (2015). OrthoFinder: solving fundamental biases in whole genome comparisons dramatically improves orthogroup inference accuracy. *Genome Biology*, 16: 157. https://doi.org/10.1186/s13059-015-0721-2

Emms DM, Kelly S (2019). OrthoFinder: phylogenetic orthology inference for comparative genomics. *Genome Biology*, 20: 238. https://doi.org/10.1186/s13059-019-1832-y

Hoang DT, Chernomor O, von Haeseler A, Minh BQ, Vinh LS (2018). UFBoot2: Improving the ultrafast bootstrap approximation. *Molecular Biology and Evolution*, 35(2): 518–522. https://doi.org/10.1093/molbev/msx281

Kalyaanamoorthy S, Minh BQ, Wong TKF, von Haeseler A, Jermiin LS (2017). ModelFinder: fast model selection for accurate phylogenetic estimates. *Nature Methods*, 14(6): 587–589. https://doi.org/10.1038/nmeth.4285

Katoh K, Standley DM (2013). MAFFT multiple sequence alignment software version 7: improvements in performance and usability. *Molecular Biology and Evolution*, 30(4): 772–780. https://doi.org/10.1093/molbev/mst010

Liu X, Wang J, Sun L (2018). Structure of the hyperosmolality-gated calcium-permeable channel OSCA1.2. *Nature Communications*, 9: 5060. https://doi.org/10.1038/s41467-018-07564-5

Mello-Silva R, Santos DYAC, Salatino MLF, Motta LB, Cattai MB, Sasaki D, Lovo J, Pita PB, Rocini C, Rodrigues CDN, Zarrei M, Chase MW (2011). Five vicarious genera from Gondwana: the Velloziaceae as shown by molecules and morphology. *Annals of Botany*, 108(1): 87–102. https://doi.org/10.1093/aob/mcr107

Mendes FK, Vanderpool D, Fulton B, Hahn MW (2020). CAFE 5 models variation in evolutionary rates among gene families. *Bioinformatics*, 36(22–23): 5516–5518. https://doi.org/10.1093/bioinformatics/btaa1022

Minh BQ, Schmidt HA, Chernomor O, Schrempf D, Woodhams MD, von Haeseler A, Lanfear R (2020). IQ-TREE 2: New models and efficient methods for phylogenetic inference in the genomic era. *Molecular Biology and Evolution*, 37(5): 1530–1534. https://doi.org/10.1093/molbev/msaa015

Morellato LPC, Silveira FAO (2018). Plant life in campo rupestre: New lessons from an ancient biodiversity hotspot. *Flora*, 238: 1–10. https://doi.org/10.1016/j.flora.2017.12.001

Silveira FAO, Negreiros D, Barbosa NPU, Buisson E, Carmo FF, Carstensen DW, Conceição AA, Cornelissen TG, Echternacht L, Fernandes GW, Garcia QS, Guerra TJ, Jacobi CM, Lemos-Filho JP, Le Stradic S, Morellato LPC, Neves FS, Oliveira RS, Schaefer CE, Viana PL, Lambers H (2016). Ecology and evolution of plant diversity in the endangered campo rupestre: a neglected conservation priority. *Plant and Soil*, 403(1-2): 129–152. https://doi.org/10.1007/s11104-015-2637-8

Teodoro GS, de Britto Costa P, Brum M, Signori-Müller C, Alcantara S, Dawson TE, West AG, Lambers H, Oliveira RS (2021). Desiccation tolerance implies costs to productivity but allows survival under extreme drought conditions in Velloziaceae species in campos rupestres. *Environmental and Experimental Botany*, 189: 104556. https://doi.org/10.1016/j.envexpbot.2021.104556

Thor K, Jiang S, Michard E, George J, Scherzer S, Huang S, Dindas J, Derbyshire P, Leitão N, DeFalco TA, Zipfel C (2020). The calcium-permeable channel OSCA1.3 regulates plant stomatal immunity. *Nature*, 585(7826): 569–573. https://doi.org/10.1038/s41586-020-2702-1

Wang Y, Tang H, DeBarry JD, et al. (2012). MCScanX: a toolkit for detection and evolutionary analysis of gene synteny and collinearity. *Nucleic Acids Research*, 40: e49. https://doi.org/10.1093/nar/gkr1293

Yang Z (2007). PAML 4: phylogenetic analysis by maximum likelihood. *Molecular Biology and Evolution*, 24(8): 1586–1591. https://doi.org/10.1093/molbev/msm088

Yang Z, Nielsen R (2000). Estimating synonymous and nonsynonymous substitution rates under realistic evolutionary models. *Molecular Biology and Evolution*, 17(1): 32–43. https://doi.org/10.1093/oxfordjournals.molbev.a026236

Yuan F, Yang H, Xue Y, Kong D, Ye R, Li C, Zhang J, Theprungsirikul L, Shrift T, Krichilsky B, Johnson DM, Swift GB, He Y, Siedow JN, Pei ZM (2014). OSCA1 mediates osmotic-stress-evoked Ca2+ increases vital for osmosensing in Arabidopsis. *Nature*, 514(7522): 367–371. https://doi.org/10.1038/nature13593

Zhang C, Rabiee M, Sayyari E, Mirarab S (2018a). ASTRAL-III: polynomial time species tree reconstruction from partially resolved gene trees. *BMC Bioinformatics*, 19(S6): 153. https://doi.org/10.1186/s12859-018-2129-y

Zhang M, Wang D, Kang Y, Wu JX, Yao F, Pan C, Yan Z, Song C, Chen L (2018b). Structure of the mechanosensitive OSCA channels. *Nature Structural & Molecular Biology*, 25(9): 850–858. https://doi.org/10.1038/s41594-018-0117-6
