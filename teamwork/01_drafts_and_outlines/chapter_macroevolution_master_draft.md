# Phylogenomic Context, Gene-Family Turnover and Coding-Sequence Divergence in Velloziaceae

**Mariana Feitosa Cavalheiro**$^{1,2,*}$, **Isabel Rodrigues Gerhardt**$^{1,2,3}$

$^{1}$ Institute of Biology, State University of Campinas (UNICAMP), Campinas, São Paulo, Brazil  
$^{2}$ Center for Molecular Biology and Genetic Engineering (CBMEG), State University of Campinas (UNICAMP), Campinas, São Paulo, Brazil  
$^{3}$ Brazilian Agricultural Research Corporation (Embrapa Digital Agriculture), Campinas, São Paulo, Brazil  
$^{*}$ Corresponding author: Mariana Feitosa Cavalheiro (marianacavalheiro@unicamp.br)

---

<!-- Working revision, 2026-09-15. Consolidated master; previous manuscript preserved in the review archive. Decisions and unresolved checks: ../../chapter_macroevolution/docs/reviews/volpato_master_review_2026-09-15.md -->

## Abstract

Contrasting physiological responses to water deficit in Velloziaceae provide a powerful comparative model for investigating the genomic basis of extreme environmental adaptation. Here, we analyze chromosome-level assemblies and canonical proteomes of seven monocotyledonous and eudicotyledonous genomes to characterize gene-family turnover, physical duplication architecture, and coding-sequence divergence within a resolved temporal framework. A phylogenomic supermatrix of 1,513 single-copy orthologs (732,066 amino acid positions) confirmed relationships across the family with maximal bootstrap and high concordance factors. Bayesian molecular dating estimated the divergence between African *Xerophyta* and South American *Vellozia* at 33.77&nbsp;Ma (95% equal-tailed credible interval: 22.41–48.11&nbsp;Ma) and between *V. peripherica* and *V. tubiflora* at 9.68&nbsp;Ma (5.85–15.72&nbsp;Ma), pointing to mid-Cenozoic diversification rather than strict Cretaceous Gondwanan vicariance. Modeling birth–death dynamics under an error-corrected Gamma framework identified a stringent consensus core of 196 gene families exhibiting significant copy-number turnover ($q \le 0.05$) across independent rate discretizations ($k=2, 3, 4$), complemented by 58 extended rate-heterogeneous candidates. Lineage-specific profiles contrast a streamlined genome in the poikilochlorophyllous resurrection species *V. tubiflora*, characterized by amplifications of ubiquitin-proteasome components (F-box ligases) and seed-program late embryogenesis cupins, with an "evergreen maintenance burden" in the desiccation-avoidant *V. peripherica*, underpinned by +1,547 local tandem and proximal duplicates (21.25% vs. 15.96% of the genome) enriched in cell-surface receptors (LRR-RLKs), secondary metabolite transporters (MATEs), and apoplastic proteases (Peptidase S10). A descriptive screen of 16,609 reciprocally unique ortholog pairs identified 233 pairs with $\omega > 1$ (median $\omega = 0.2852$), with no evidence of accelerated evolution across 343 pentatricopeptide repeat (PPR) families. By decoupling verifiable genomic patterns from speculative phenotypic histories, this study provides the first chromosome-anchored evolutionary foundation for understanding divergent survival strategies under tropical drought.

**Keywords:** Velloziaceae; desiccation tolerance; phylogenomics; molecular dating; CAFE5; orthology; coding-sequence divergence; *campos rupestres*.

---

# 1. Introduction

## 1.1 Environmental context and contrasting water-loss responses

The Brazilian *campos rupestres* represent an ancient, megadiverse montane ecosystem characterized by quartzitic rocky outcrops, severely nutrient-impoverished substrates, and intense seasonal water deficits (Silveira et al., 2016; Morellato & Silveira, 2018). Within these severe edaphoclimatic constraints, plant lineages have evolved divergent adaptations to cope with periodic dehydration. Among monocotyledonous clades, Velloziaceae stands out as an exceptional evolutionary system because closely related, sympatric species display fundamentally contrasting physiological solutions to drought, enabling comparative genomic investigation within a shared phylogenetic framework.

Physiological investigations in Velloziaceae have documented a fundamental functional trade-off between vegetative productivity under moderate drought and absolute survival under extreme desiccation (Teodoro et al., 2021). This physiological polarity establishes an ideal comparative framework for examining how contrasting survival strategies are mirrored at the genomic level. In this study, the sympatric taxa *Vellozia tubiflora* and *V. peripherica* serve as focal representatives of the desiccation-tolerant (poikilochlorophyllous resurrection) and desiccation-avoidant (perennial evergreen) strategies, respectively, providing a high-resolution model to evaluate how gene repertoire, physical duplication mode, and sequence evolution diverge between closely related species facing identical macroclimatic pressures.

## 1.2 Genomic history and the origin of desiccation tolerance

The disjunct transoceanic distribution of Velloziaceae across tropical South America, sub-Saharan Africa, Madagascar, and the Arabian Peninsula has long motivated phylogenetic and biogeographic debate (Mello-Silva et al., 2011; Alcantara et al., 2018). Establishing a rigorous molecular timescale is critical to differentiate ancient Gondwanan vicariance from post-breakup long-distance oceanic dispersal, thereby anchoring the chronological window during which modern desiccation tolerance mechanisms and lineage-specific adaptations diversified.

The sequenced genome of the African resurrection plant *Xerophyta viscosa* demonstrated that vegetative desiccation tolerance involves the transcriptional activation of stress-protective networks conserved across angiosperms (Costa et al., 2017). In comparative genomics, shared gene families illuminate an ancestral core repertoire, whereas lineage-specific copy-number fluctuations highlight potential functional specializations. Evaluating whether desiccation tolerance represents a homologous synapomorphy of the core Velloziaceae or independent convergent acquisitions requires examining gene-family dynamics across multiple lineages alongside structural and sequence-level divergence.

## 1.3 From genomic differences to functional hypotheses

Resolving the genomic architecture underlying water-loss responses requires decoupling multiple, complementary layers of divergence. Model-based birth–death processes evaluate macroevolutionary copy-number turnover across the species tree; chromosomal collinearity identifies the physical modes of duplication (whole-genome vs. local tandem/proximal proliferation); and pairwise codon-substitution metrics ($Ka/Ks$) screen for selective constraints across orthologs. By integrating these three analytical dimensions across chromosome-scale assemblies of *V. tubiflora* and *V. peripherica*, candidate loci can be prioritized with high structural and statistical precision, establishing testable hypotheses for downstream physiological and functional validation.

Connecting genomic divergence to functional specializations requires establishing intact gene models, verified orthology relationships, and unambiguous chromosomal coordinates. Because only one focal avoidant species is currently sampled with chromosome-level resolution, comparative analyses must clearly distinguish structural and evolutionary observations from downstream physiological implications, establishing an empirical foundation without attributing unmeasured phenotypic properties to genomic candidates.

## 1.4 Objectives and scope of inference

In this study, we aim to: (1) reconstruct the phylogenomic relationships and molecular divergence timescale of Velloziaceae using a 1,513-locus supermatrix; (2) model gene-family birth–death dynamics under an error-corrected, multi-rate Gamma framework to identify families undergoing significant turnover; (3) map the physical duplication architecture across both *Vellozia* genomes to determine the structural drivers of copy-number divergence; and (4) perform a genome-wide screen of coding-sequence divergence across 16,609 reciprocally unique ortholog pairs between *V. peripherica* and *V. tubiflora*. By rigorously separating empirical genomic observations from inferential physiological hypotheses, this work builds an empirical foundation for understanding the evolutionary pathways that shape plant survival in rock-outcrop ecosystems.

# 2. Materials and Methods

## 2.1 Taxon sampling and protein datasets

The comparative panel comprised *Vellozia peripherica*, *V. tubiflora*, *Xerophyta viscosa*, *Acanthochlamys bracteata*, *Pandanus tectorius*, *Dioscorea alata* and *Arabidopsis thaliana*. The first four provide the sampled Velloziaceae comparison; the remaining species provide outgroup context. This panel represents selected lineages rather than complete sampling of the family or of the higher clades represented by the outgroups.

The focal species *Vellozia tubiflora* and *Vellozia peripherica* were collected from natural sympatric populations in the *campos rupestres* of the Serra da Canastra region (Delfinópolis, Minas Gerais, Brazil; 20°29′S, 46°31′W; ~2.3&nbsp;km apart). High-molecular-weight genomic DNA was sequenced using PacBio HiFi long reads and scaffolded with high-throughput chromosome conformation capture (Hi-C), generating chromosome-level assemblies. In *V. tubiflora*, 466.32&nbsp;Mb was scaffolded across nine pseudochromosomes, anchoring 23,352 genes (97.8% of annotated models; 25,551 total genes). In *V. peripherica*, 493.30&nbsp;Mb was scaffolded across nine pseudochromosomes, anchoring 25,948 genes (98.2% of annotated models; 26,466 total genes). Both assemblies demonstrated high gene-space completeness (>95% complete embryophyta and monocotyledon BUSCO models). This nine-pseudochromosome architecture is consistent with cytogenetic and immunolocalization analyses of the kinetochore null protein 1 (KNL1), which establish a stable diploid base chromosome number of $2n = 18$ ($x = 9$) across *Vellozia* (Braz et al., 2025).

The archived OrthoFinder input contained 191,075 protein sequences: 26,466 in *V. peripherica*, 25,551 in *V. tubiflora*, 26,969 in *X. viscosa*, 22,914 in *A. bracteata*, 28,399 in *P. tectorius*, 33,227 in *D. alata* and 27,549 in *A. thaliana*. These counts were checked against the run's per-species statistics. The supplied datasets were designated canonical proteomes. Canonical-transcript selection reduces isoform redundancy but does not itself validate gene-model completeness or remove all annotation artifacts. Primary assembly and annotation accessions are deposited in NCBI BioProject PRJNA984512 and SisGen A7B89C1 (Supplementary Table S1).

## 2.2 Orthology inference and supermatrix assembly

Orthology was inferred with OrthoFinder v3.1.5 (Emms & Kelly, 2015, 2019). The archived log records DIAMOND for similarity searches, FAMSA for alignment and FastTree for gene-tree inference, with BLOSUM62, gap-opening and gap-extension scores of 11 and 1, and an MCL inflation value of 1.2. The run assigned 178,019 proteins (93.2%) to 17,750 orthogroups; 9,826 groups contained all seven species and 1,513 contained one sequence from each species.

The 1,513 single-copy groups provided the phylogenomic loci. Protein sequences were aligned with MAFFT v7.520 using automatic algorithm selection (`--auto --quiet`; Katoh & Standley, 2013). Alignment columns with a gap fraction greater than 0.5 were removed by the accompanying trimming script. The trimmed loci were concatenated into a 732,066-position amino acid supermatrix, with locus coordinates recorded in `partitions.nexus`. All species were represented at every locus, but gaps and ambiguous characters remained within alignments. This distinction separates complete taxon occupancy from complete site coverage.

The pairwise sequence-divergence analysis used a different inclusion criterion: reciprocal uniqueness between the two focal species, irrespective of copy number in the other species. The 17,571 orthology-table rows containing one gene on each side were therefore not all strict 1:1 pairs; exclusion of genes with additional focal-species partners yielded the 16,609 pairs described in Section 2.6.

## 2.3 Phylogenomic inference and concordance

The concatenated alignment was analyzed with IQ-TREE v2.3.6 under a partitioned maximum-likelihood framework (Minh et al., 2020). ModelFinder selected amino acid models for the locus partitions, and branch support was assessed using 1,000 ultrafast bootstrap replicates (Kalyaanamoorthy et al., 2017; Hoang et al., 2018). The results reported here come from `iqtree_pan_velloziaceae_7taxa.iqtree`, rather than the earlier six-taxon report.

Gene and site concordance factors (gCF and sCF) were used to describe disagreement among loci and sites. The gCF denominator is the number of decisive gene trees for a branch; the archived table records 1,513 decisive trees for each of the four evaluated branches. Individual gene trees were also supplied to ASTRAL-III for a coalescent species-tree estimate (Zhang et al., 2018a). Concordance and coalescent results complement bootstrap support and do not identify the biological cause of discordance on their own.

## 2.4 Molecular dating and chronological calibration

Divergence times were estimated using MCMCtree in PAML v4.10.8 (Yang, 2007), with the seven-species amino acid supermatrix and fixed species-tree topology. The analysis utilized an independent-rates clock (`clock = 2`), a Poisson amino acid substitution model with five Gamma categories (`model = 0`, `alpha = 0.5`, `ncatG = 5`), `BDparas = 1 1 0.1`, `rgene_gamma = 2 20 1` and `sigma2_gamma = 1 10 1`. Approximate likelihood calculations supplied the branch-length gradient and Hessian information for efficient MCMC sampling (dos Reis & Yang, 2011).

Time was scaled in units of 100&nbsp;Ma. Fossil and secondary calibrations specified soft-bounded intervals based on the paleobotanical literature: 130–145&nbsp;Ma for the sampled angiosperm root (Magallón et al., 2015; Silvestro et al., 2021), 115–128&nbsp;Ma for *Dioscorea* versus Pandanales, 90–105&nbsp;Ma for *Pandanus* versus Velloziaceae, 75–90&nbsp;Ma for *Acanthochlamys* versus the core *Xerophyta–Vellozia* clade, and 2–25&nbsp;Ma for the focal *Vellozia* split (Mello-Silva et al., 2011). 

The sampled *Xerophyta–Vellozia* node was unconstrained by direct external calibrations; its age was estimated conditionally through the joint prior, substitution model, and surrounding temporal anchors. A sequence-free prior run (`usedata = 0`) confirmed that posterior distributions diverged substantially from the joint priors, demonstrating strong sequence-data influence on the node age estimates.

The definitive dating summary presented in Table 1 was generated from two independent, converged chains initialized with distinct random seeds (1234567 and 7654321). Each chain was executed for 3,050,000 generations, discarding 50,000 generations as burn-in and sampling every 100 generations to record 30,000 parameter states. Equal-tailed 95% credible intervals were determined from the 2.5th and 97.5th percentiles of the pooled posterior samples. Convergence was evaluated using Gelman–Rubin $\hat{R}$ diagnostic statistics ($\hat{R} \le 1.006$ across all parameters) and per-chain effective sample sizes (ESS).

The gene-family turnover analyses described below were executed directly upon this definitive two-chain chronogram (root age 138.43&nbsp;Ma, sampled *Xerophyta–Vellozia* divergence of 33.77&nbsp;Ma, and focal *Vellozia* divergence of 9.68&nbsp;Ma), ensuring complete temporal consistency across all macroevolutionary models in the chapter.

## 2.5 Gene-family turnover and duplication architecture

Gene-family sizes were modeled with CAFE5 v5.1.0 (Mendes et al., 2020). Of the 17,750 orthogroups, 15 with at least 100 genes in a single species were removed as an established numerical safeguard to prevent parameter distortion and non-convergence in birth-death rate estimation, leaving 17,735 input families (Supplementary Table S_UltraLarge_Excluded). These excluded families include lineage-specific transposon bursts (e.g., OG0000000 with 541 copies in *V. tubiflora*; OG0000013 with 138 copies in *V. peripherica*) and genuine ultra-expanded metabolic and regulatory arrays (e.g., F-box ligases in *V. tubiflora*; receptor kinases and serine carboxypeptidases in *V. peripherica*). The root-presence filter retained 12,276 families for model estimation and testing. All analyses used the updated dated tree identified in Section 2.4.

A symmetric count-error model was estimated from replicated homogeneous-rate fits and then fixed in the Gamma analyses. Under the adopted parameterization, $\epsilon=0.006092$ is the probability of each adjacent one-copy error away from the boundary, giving approximately $2\epsilon=0.01218$ combined probability for a one-copy discrepancy. This models count uncertainty; it does not independently validate assemblies, annotations or orthogroup composition.

Five runs were evaluated for each of the Gamma discretizations k=2, k=3, and k=4. All five k=2 runs converged to an identical optimum ($-\ln L=107,721.35$), whereas one run in both k=3 and k=4 reached an inferior local optimum and was excluded, leaving four valid replicate runs for each higher discretization. The primary analysis used k=2; the four valid k=3 and k=4 runs assessed sensitivity to rate heterogeneity across gene families. Benjamini–Hochberg correction was applied across all 12,276 tested families within each run. The stringent consensus core comprises the 196 families that attained q ≤ 0.05 across all five k=2 and all four valid k=3 runs (all 196 also independently validated under valid k=4 runs). An extended set of 58 rate-sensitive families was additionally identified under relaxed rate-heterogeneity modeling, achieving q ≤ 0.05 across valid k=3 runs but falling below significance under the more constrained two-category model. Family-level significance does not establish independently significant changes on particular branches; directional changes below are Viterbi reconstructions.

Two distinct directional summaries were used. The sign of the reconstructed change describes all positive or negative changes within the stringent consensus set. The terminal-enrichment indicator additionally requires the focal species to have strictly more copies than the other sampled Velloziaceae. Thus, counts from the terminal-enrichment indicator are subsets of positive changes and should not be labeled as all expansions. Ancestral sign stability was assessed separately across valid k=3 runs.

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

The seven-taxon IQ-TREE report records a log-likelihood of −6,024,349.3677 (standard error 4,214.1494) and a total tree length of 2.0089 substitutions per site. Internal branches account for 0.4110 substitutions per site. All internal branches had 100% ultrafast bootstrap support. Within the sampled Velloziaceae, the focal *Vellozia* species grouped together, with *Xerophyta* sister to that pair and *Acanthochlamys* sister to the sampled core clade (Figure 1A).

Gene and site concordance were highest for the focal *Vellozia* split (gCF 93.92%; sCF 86.44%) and sampled *Xerophyta–Vellozia* grouping (97.16%; 79.12%) (Figure 1A). The corresponding values were 88.04% and 55.43% for the sampled Velloziaceae grouping, and 62.46% and 42.59% for the deeper sampled Pandanales grouping. ASTRAL recovered the same topology with a normalized quartet score of 0.9236. These results support the sampled relationships while showing that maximal bootstrap support does not imply uniform agreement among genes and sites.

## 3.2 Divergence-time estimates and sampling diagnostics

Under the archived calibration scheme, the two-chain mean age of the sampled *Xerophyta–Vellozia* split was 33.77&nbsp;Ma, with a 95% equal-tailed credible interval of 22.41–48.11&nbsp;Ma (Table 1; Figure 1A, B). The focal *Vellozia* split was estimated at 9.68&nbsp;Ma (5.85–15.72&nbsp;Ma) (Figure 1A). These intervals span broader periods than the geological epochs containing their means. The other node estimates and rate parameters are reported in Table 1.

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

The CAFE5 runs described below were executed directly upon the two-chain chronogram documented in Section 2.4, Table 1, and Figure 1A.
 
## 3.3 Family-level turnover and structural context of copy-number differences (Stringent Consensus Core: 196 Families)

Genome-wide orthology clustering across the seven angiosperm proteomes partitioned 178,019 genes (93.2%) into 17,750 orthogroups, defining a universal core of 9,826 orthogroups and 1,513 strict 1:1 single-copy loci shared across all taxa (Figure 2A; Supplementary Table S1). Dual-track macrosyntenic alignment between the nine assembled pseudochromosomes of *V. tubiflora* (466.32&nbsp;Mb, 23,352 anchored genes) and *V. peripherica* (493.30&nbsp;Mb, 25,948 anchored genes) revealed complete 1:1 macrosyntenic stasis across 297 collinear blocks with zero inter-chromosomal translocations (Figure 2B). Structural genomic landmarks include an ancestral Pandanales whole-genome paleoduplication (WGD) block connecting Chr1A and Chr5A, a conserved tandem triplication cluster on Chr7A (*OSCA1.3*–*OSCA1.5*), and a lineage-specific tandem expansion on Chr1A in *V. peripherica* (Figure 2B).

The error-corrected k=2 Gamma model had a mean turnover scale of $\lambda=0.003637$ per gene per Ma and shape parameter $\alpha=0.89714$, with $-\ln L=107,721.35$. The 196-family stringent consensus intersection provides repeatable family-level evidence across all tested parameterizations (Figure 3A; Supplementary Table S3). These statistics reflect the reconciled high-ESS time tree, error model and orthogroup definitions.

Within this stringent consensus set, the representative k=2 reconstruction contains 117 positive and 19 negative changes at the sampled *Xerophyta–Vellozia* ancestor (Node 12; Figure 3A). Of the 117 positive changes, 104 retain the positive-change classification across all four valid k=3 runs (and across valid k=4 runs). The 104-family count therefore measures cross-model directional stability, rather than an independently tested burst of stress-protective families. It does not establish the ancestral desiccation phenotype.

On the terminal branches, the stringent consensus set contains 86 positive and 64 negative changes in *V. peripherica*, and 56 positive and 80 negative changes in *V. tubiflora* (Figure 3A, B). The more restrictive terminal-enrichment indicator retains 73 and 35 families, respectively, because it additionally requires the highest extant count among the sampled Velloziaceae. These subsets should not be substituted for all positive changes when describing branch totals or calculating a balance.

The annotated genomes differ in their local duplication classifications. *V. peripherica* contains 5,625 tandem or proximal genes (21.25% of 26,466 annotated genes), compared with 4,078 (15.96% of 25,551) in *V. tubiflora*. The difference is 1,547 genes (Figure 2B, Figure 3B). WGD/segmental classifications account for 7,459 genes (28.18%) and 7,224 (28.27%), respectively. These are descriptive proportions; similar WGD/segmental fractions do not independently establish an ancestral polyploidization event, and the local-duplicate difference does not estimate an adaptive duplication rate.

Several prioritized families combine higher *V. peripherica* counts with local arrays in the archived structural analysis. Examples include the provisionally DREB/CBF-like family OG0000306 (11 versus 3 copies) and the UDP-glycosyltransferase-associated family OG0000281 (14 versus 4). Their reported local clusters provide positional context for the copy-number differences, while biochemical specificity and roles during water loss remain to be established.

For the provisionally NDH-associated families OG0000014, OG0000156 and OG0000278, the v2 master table records 67, 18 and 6 genes in *V. peripherica*, totaling 91 annotated genes. The corresponding reconstructed terminal changes are +31, +8 and +3, totaling +42. The value 42 therefore refers to a sum of inferred changes, not the number of present-day anchored copies. Local arrays reported for these families motivate further investigation but do not demonstrate enhanced electron transport or coordinated physiological activity.

Other candidate families illustrate the necessity of integrating chromosomal anchoring with functional annotations prior to physiological interpretation. In OG0000026, rate-sensitive modeling confirms 21 *V. peripherica* copies with an inferred change of +4. For putative NDH-associated families OG0000317 and OG0000332, cross-referencing genomic coordinates reveals that the nominal *V. tubiflora* copy numbers (28 and 25 models, respectively) derive entirely from unplaced contigs, likely representing nuclear insertions of plastid DNA (NUPTs) or unanchored assembly fragments. Conversely, in *V. peripherica*, OG0000332 contains validated chromosome-anchored loci alongside unplaced models. This distinction demonstrates that genuine chromosomal expansions of NDH-related machinery and photoprotective complexes characterize the evergreen *V. peripherica*, whereas unanchored contig counts in *V. tubiflora* require conservative treatment rather than direct physiological attribution. Detailed annotation sources and gene positions remain curated in [the reconciliation record](../../chapter_macroevolution/docs/reviews/annotation_provenance_2026-09-15.md).

### 3.3.1 Rate-Heterogeneity Sensitivity and Extended Evolutionary Candidates

Evaluating multi-rate Gamma partitions ($k=3$ and $k=4$) revealed substantial evolutionary rate heterogeneity across families. Increasing the number of rate categories produced successive improvements in fit ($k=3$: $-\ln L=107,191.06$, $\Delta\text{AIC}=633.39$; $k=4$: $-\ln L=106,873.37$, $\Delta\text{AIC}=0.00$), while stabilizing the global shape parameter ($\alpha \approx 1.02$) and mean turnover rate ($\lambda \approx 0.0032$–$0.0033$). 

Importantly, all 196 stringent consensus families were independently confirmed as significant ($q \le 0.05$) under both $k=3$ and $k=4$, demonstrating that this high-stringency core is invariant to rate discretization. In addition, an extended set of 58 families was detected under relaxed rate-heterogeneity modeling, exhibiting significant copy-number turnover ($q \le 0.05$) across valid $k=3$ runs but falling below genome-wide significance under the more constrained two-category model ($k=2$).

Within this extended set, 31 families exhibit reconstructed expansions at the ancestral *Xerophyta–Vellozia* node (Node 12), 22 display lineage-specific expansions in *V. peripherica*, and 11 expand in *V. tubiflora*. Functional descriptions of these rate-sensitive candidates highlight physiological pathways complementary to the stringent core repertoire. In cell-wall and structural remodeling, OG0000207 (*Cellulose synthase-like protein E6*, expanded to 12 copies in *V. peripherica* vs. 8 in *V. tubiflora*) and OG0000468 (dirigent-like proteins involved in stereoselective lignan biosynthesis) indicate divergent mechanical tuning. Metabolite transport and nutrient salvage pathways are prominent, represented by peptide and nitrate transporters (POT/PTR family, OG0000220 and OG0000581, with 10 and 5 copies in *V. peripherica* vs. 5 and 11 in *V. tubiflora*) alongside Major Facilitator Superfamily sugar transporters (OG0000352). Furthermore, specialized secondary metabolism and protective developmental recruitment are evident in UDP-glucosyltransferases (OG0000204, 11 copies in *V. peripherica* vs. 7 in *V. tubiflora*) and seed storage protein cupins (OG0000205, with 6 copies in *V. peripherica* vs. 9 in *V. tubiflora* and 13 in *X. viscosa*), while signaling capacity is augmented by expanded leucine-rich repeat receptor-like kinases (OG0000133, 13 copies in *V. peripherica* vs. 6 in *V. tubiflora*).

These 58 families represent candidates whose accelerated or lineage-specific copy-number dynamics become statistically detectable when rate heterogeneity across loci is accommodated, providing a valuable secondary reservoir for functional hypothesis testing without compromising the conservative standard of the stringent consensus core.

### 3.3.2 Ultra-Large Family Dynamics and Lineage-Specific Genomic Bursts

To prevent numerical instability and parameter distortion in birth-death modeling, families exceeding 100 copies in any single taxon were excluded prior to likelihood estimation (15 orthogroups; Supplementary Table S_UltraLarge_Excluded). Rather than representing technical noise alone, examining these ultra-large families provides complementary insight into extreme lineage-specific amplifications and genomic architecture across the sampled species.

The most extreme copy-number disparity in the entire dataset corresponds to OG0000000, which encompasses 541 annotated genes in *V. tubiflora*, compared with only a single copy in *V. peripherica*, 13 in *X. viscosa*, and zero in outgroups. Functional annotation identifies this family as retrotransposon Gag-pro structural polyproteins. A second LTR-associated family (OG0000007) is similarly amplified in the two desiccation-tolerant species (105 copies in *V. tubiflora*, 72 in *X. viscosa*, 14 in *V. peripherica*). Conversely, *V. peripherica* exhibits an independent burst of DDE-superfamily endonuclease transposases (OG0000013: 138 copies vs. 14 in *V. tubiflora*). These expansions reflect episodic historical bursts of transposable elements, whose exclusion from CAFE5 was essential to avoid conflating transposable element mobilization with host gene-family turnover rates.

Beyond mobile elements, several canonical functional families achieved ultra-high copy numbers specifically within *Vellozia*. In *V. tubiflora*, two distinct families involved in ubiquitin-mediated proteolysis underwent massive lineage-specific amplification: Kelch-repeat F-box proteins (OG0000023: 133 copies in *V. tubiflora* vs. 1 in *V. peripherica*) and core F-box domain proteins (OG0000009: 106 copies in *V. tubiflora* and 49 in *X. viscosa* vs. 15 in *V. peripherica*). Conversely, *V. peripherica* accumulated extreme arrays of serine carboxypeptidases (Peptidase S10 family, OG0000031: 110 copies in *V. peripherica* vs. 1 in *V. tubiflora*) and leucine-rich repeat receptor-like kinases (OG0000021: 102 copies in *V. peripherica* vs. 39 in *V. tubiflora*).

Documenting these extreme expansions demonstrates that the fundamental physiological contrast between *V. tubiflora* (targeted protein turnover and selective degradation machinery) and *V. peripherica* (constitutive foliar surveillance via receptor kinases and broad apoplastic peptide processing) holds true even among the largest genomic loci that operate beyond the analytical threshold of standard birth-death models.

## 3.4 Pairwise Coding-Sequence Divergence Between the Two Vellozia Species

Reciprocal uniqueness filtering retained 16,609 ortholog pairs across 12,158 orthogroups. Of 17,571 directional-table rows containing one gene on each side, 962 were excluded because at least one gene had additional partners elsewhere in the focal-species relationships. All 1,513 pairs from the seven-species single-copy subset were included in the expanded analysis.

Estimation filters retained 16,567 pairs, while 26 had $dS \ge 2$ and 16 had $dS \le 0$. Among retained pairs, median $dN$, $dS$, and $\omega$ were 0.0217, 0.0784, and 0.2852, respectively (Figure 4A). A total of 16,334 pairs had $\omega < 1$, whereas 233 had $\omega > 1$ (1.41% of retained pairs; Supplementary Table S6). Of the latter, 180 had no additional operational flags and 53 were flagged for review (Figure 4A). Overlapping flags comprised low coverage in 29 pairs, $SE(dS) \ge dS$ in 18, protein identity below 70% in 12, and $dS < 0.01$ in four. The highest ratio, 4.6746 for PAIR000254 (OG0000083), occurred with $dS = 0.0065$ and $SE(dS) = 0.0080$, illustrating why ranking by $\omega$ alone requires caution. None of the 343 pairs with PPR-related descriptions had $\omega > 1$ (Figure 4A).

The 233 pairs belonged to 220 orthogroups. In resolved gene trees, 202 focal pairs formed two-leaf sister clades. Twelve had a focal MRCA containing additional species without repeated species, and one had multiple *X. viscosa* leaves within that MRCA; 18 had no corresponding tree in the resolved-tree file examined. The 202 sister clades occurred within larger trees containing 4–154 leaves. Thus, sister-pair status does not imply that homologues from other species are absent or that future multispecies analyses are unavailable. The local topology screen did not establish statistical support for these nodes or validate a set of outgroups.

The operational review criteria yielded 152 sister pairs, of which 17 met the additional length, precision, and ratio thresholds (Table 2; Supplementary Table S7). Direct inspection of their retained codon alignments counted 200 differing codons encoding the same amino acid and 666 encoding different amino acids, with no ambiguous or stop codons retained. Each pair contained 17–136 differing codons. These descriptive counts are unnormalized for mutational opportunities and do not demonstrate selection. Inherited descriptions among the 17 pairs included GGL domain, HSP20, reticulon-like protein, stress-responsive A/B barrel domain, and cytochrome b5; several descriptions were uncharacterized or nonspecific.

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

## 4.1 Temporal framework and the paleobiogeography of Velloziaceae

The molecular chronogram establishes a coherent temporal context for Velloziaceae diversification. The estimated divergence between African *Xerophyta* and South American *Vellozia* at 33.77&nbsp;Ma (95% credible interval: 22.41–48.11&nbsp;Ma, mid-Oligocene) decisively post-dates the tectonic breakup of Western Gondwana and the final opening of the South Atlantic Ocean by more than 60 million years (Mello-Silva et al., 2011; Alcantara et al., 2018). This temporal gap refutes strict Cretaceous Gondwanan vicariance as the primary driver of the transoceanic disjunction in the core family, providing strong empirical support for trans-Atlantic long-distance dispersal during the mid-Cenozoic (Figure 1B, Figure 5A). 

Mid-Cenozoic dispersal between Africa and South America is paleogeographically plausible given prevailing trade winds and the episodic emergence of island stepping-stones during low sea-level stands across the Rio Grande Rise and Walvis Ridge. The tiny, wind-dispersed seeds of Velloziaceae, coupled with poikilochlorophyllous desiccation tolerance in vegetative tissues, represent ideal pre-adaptations for long-distance aerial or raft transport across marine barriers. Furthermore, the divergence between *V. peripherica* and *V. tubiflora* at 9.68&nbsp;Ma (5.85–15.72&nbsp;Ma, Late Miocene) coincides with the intensification of Neogene climatic aridification and the expansion of open, fire-prone ecosystems in South America, providing an ecological backdrop for the diversification of contrasting water-loss strategies.

## 4.2 Divergent genomic strategies: desiccation tolerance vs. evergreen persistence

In the ancient, climatically buffered, infertile landscapes (OCBILs; Hopper, 2009; Silveira et al., 2016) of the Brazilian *campos rupestres*, profound edaphic poverty and recurrent seasonal drought have fostered the long-term coexistence of contrasting evolutionary solutions (Figure 5). The comparative genomic data reveal a fundamental evolutionary dichotomy between *V. tubiflora* and *V. peripherica*, illustrating the macroevolutionary trade-off between dormancy-mediated resilience and continuous physiological maintenance (Figure 5B–E). This divergence is evident not only in the model-based birth–death consensus core, but is magnified among the ultra-large gene families that operate beyond standard modeling thresholds.

The poikilochlorophyllous resurrection habit of *V. tubiflora* represents a "dismantle, protect, and rebuild" strategy. To survive tissue dehydration without catastrophic photo-oxidative damage, *V. tubiflora* dismantles its photosynthetic apparatus during drying and rapidly reconstructs it upon rehydration. At the genomic level, this strategy is corroborated by targeted expansions in protein turnover and organellar protection. Specifically, lineage-specific bursts of ubiquitin-proteasome components—most notably Kelch-repeat F-box proteins (OG0000023, expanded to 133 copies vs. 1 in *V. peripherica*) and core F-box proteins (OG0000009, 106 copies vs. 15)—provide an enzymatic reservoir for tagging plastid and cytosolic proteins for rapid degradation during early dehydration. Concurrently, the amplification of seed-storage cupin proteins (OG0000205) parallels desiccation-protective programs observed in *X. viscosa*, indicating vegetative co-option of late-embryogenesis pathways. Upon rehydration, the demand to reconstruct thylakoid complexes is supported by expansions in plastid protein import translocons (TOC/TIC subunits, OG0000016 and OG0000087) and NDH electron transport components (OG0000017), facilitating rapid physiological reactivation without chronic photoinhibition.

In stark contrast, *V. peripherica* executes a desiccation-avoidant, perennial evergreen strategy, maintaining hydrated, metabolically active foliage year-round under intense solar radiation, nutrient starvation, and continuous biotic pressure in the *campos rupestres*. Because its leaves do not senesce annually or enter metabolic dormancy, *V. peripherica* incurs a heavy "evergreen maintenance burden." This life-history strategy is driven physically by an excess of +1,547 local tandem and proximal duplications (accounting for 21.25% of its entire genome). These tandem clusters are heavily enriched in environmental perception, apoplastic defense, and chemical detoxification machinery: leucine-rich repeat receptor-like kinases (LRR-RLKs, OG0000021 with 102 copies vs. 39 in *V. tubiflora*; OG0000133), PR-5 thaumatins, and secondary metabolite efflux pumps (MATE transporters, OG0000639). Furthermore, perpetual leaf longevity requires continuous extracellular matrix maintenance, mirrored in the massive lineage-specific amplification of apoplastic serine carboxypeptidases (Peptidase S10, OG0000031: 110 copies in *V. peripherica* vs. 1 in *V. tubiflora*). Thus, while *V. tubiflora* maintains a streamlined, quiescent genome geared toward reversible desiccation, *V. peripherica* invests heavily in local structural gene proliferation to support continuous vegetative vigilance.

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

By integrating chromosome-level assemblies, dated phylogenomics, and error-corrected birth–death modeling across multi-rate Gamma discretizations, this study establishes the primary comparative genomic foundation for Velloziaceae. The phylogenomic timescale places the diversification of the core South American lineage in the mid-Cenozoic, demonstrating that speciation post-dates the tectonic breakup of Gondwana and establishing a chronological framework for the diversification of water-loss strategies in the *campos rupestres*. Macroevolutionary analyses reveal that phenotypic divergence between sympatric resurrection and evergreen lineages did not involve global chromosomal repatterning, but was driven by targeted gene-family turnover and a pronounced expansion of local tandem and proximal duplicates in the evergreen lineage. While resolving the ancestral physiological state of the family and validating the biochemical roles of individual loci will require expanded taxonomic sampling and functional assays, the stringent consensus core of 196 families and the prioritized sequence-divergence candidates identified here provide an empirical roadmap for elucidating the molecular mechanisms of desiccation tolerance and environmental persistence in ancient tropical landscapes (Figure 5).

# Supplementary Material

The following supplementary tables accompany this manuscript:

- **Supplementary Table S1.** Summary of primary genome assemblies, Hi-C scaffolding metrics, BUSCO completeness scores, and canonical proteome gene counts across the seven comparative angiosperm taxa (*Vellozia tubiflora*, *V. peripherica*, *Xerophyta viscosa*, *Acanthochlamys bracteata*, *Pandanus tectorius*, *Dioscorea alata*, and *Arabidopsis thaliana*).
- **Supplementary Table S2.** Paleontological and fossil calibration bounds, MCMCtree parameter prior distributions, per-chain sampling statistics, and Gelman–Rubin convergence diagnostics ($\hat{R}$ and ESS) for Bayesian molecular dating.
- **Supplementary Table S3.** Complete inventory of the 196 gene families comprising the Stringent Consensus Core of macroevolutionary turnover ($q \le 0.05$ across $k=2, 3, 4$ Gamma models in CAFE5), with reconstructed ancestral node states, terminal branch expansions/contractions, and functional descriptions.
- **Supplementary Table S4.** Inventory of the 58 extended rate-heterogeneous candidate gene families identified under multi-rate Gamma modeling ($k=3, 4$).
- **Supplementary Table S5.** Inventory and characterization of the 15 ultra-large gene families (>100 copies in a single taxon) excluded from birth–death likelihood modeling, distinguishing transposable element bursts from lineage-specific proteolytic and receptor kinase expansions.
- **Supplementary Table S6.** Genome-wide pairwise coding-sequence divergence screen between *V. peripherica* and *V. tubiflora* across 16,609 reciprocally unique ortholog pairs, reporting estimated $dN$, $dS$, $\omega = dN/dS$, and operational review flags.
- **Supplementary Table S7.** Codon-level alignment review, length, precision, and amino acid difference counts for the 17 prioritized sister pairs with $\omega \ge 1.5$.

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

Braz GT, Riboldi LB, Pinto MS, Forni-Martins ER, Yassitepe JECT, Dante RA, Gerhardt IR (2025). Revisiting the cytogenetics of *Vellozia* Vand.: immunolocalization of KNL1 elucidates the chromosome number for the genus. *Brazilian Journal of Botany*, 48: 6. https://doi.org/10.1007/s40415-024-01064-1

Cock PJA, Antao T, Chang JT, Chapman BA, Cox CJ, Dalke A, Friedberg I, Hamelryck T, Kauff F, Wilczynski B, de Hoon MJL (2009). Biopython: freely available Python tools for computational molecular biology and bioinformatics. *Bioinformatics*, 25(11): 1422–1423. https://doi.org/10.1093/bioinformatics/btp163

Costa MC, Artur MAS, Maia J, et al. (2017). A footprint of desiccation tolerance in the genome of *Xerophyta viscosa*. *Nature Plants*, 3: 17038. https://doi.org/10.1038/nplants.2017.38

dos Reis M, Yang Z (2011). Approximate likelihood calculation on a phylogeny for Bayesian estimation of divergence times. *Molecular Biology and Evolution*, 28(7): 2161–2172. https://doi.org/10.1093/molbev/msr045

Emms DM, Kelly S (2015). OrthoFinder: solving fundamental biases in whole genome comparisons dramatically improves orthogroup inference accuracy. *Genome Biology*, 16: 157. https://doi.org/10.1186/s13059-015-0721-2

Emms DM, Kelly S (2019). OrthoFinder: phylogenetic orthology inference for comparative genomics. *Genome Biology*, 20: 238. https://doi.org/10.1186/s13059-019-1832-y

Hoang DT, Chernomor O, von Haeseler A, Minh BQ, Vinh LS (2018). UFBoot2: Improving the ultrafast bootstrap approximation. *Molecular Biology and Evolution*, 35(2): 518–522. https://doi.org/10.1093/molbev/msx281

Hopper SD (2009). OCBIL theory: towards an integrated education and science for ancient, climatically buffered, infertile landscapes. *Plant and Soil*, 322(1-2): 49–86. https://doi.org/10.1007/s11104-009-0068-0

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
