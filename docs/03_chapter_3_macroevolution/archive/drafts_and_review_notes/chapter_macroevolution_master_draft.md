# Phylogenomic Context, Gene-Family Turnover and Coding-Sequence Divergence in Velloziaceae

**Mariana Feitosa Cavalheiro**$^{1,2,*}$, **Isabel Rodrigues Gerhardt**$^{1,2,3}$

$^{1}$ Institute of Biology, State University of Campinas (UNICAMP), Campinas, São Paulo, Brazil  
$^{2}$ Center for Molecular Biology and Genetic Engineering (CBMEG), State University of Campinas (UNICAMP), Campinas, São Paulo, Brazil  
$^{3}$ Brazilian Agricultural Research Corporation (Embrapa Digital Agriculture), Campinas, São Paulo, Brazil  
$^{*}$ Corresponding author: Mariana Feitosa Cavalheiro (marianacavalheiro@unicamp.br)

---



## Abstract

Contrasting responses to seasonal water loss in Velloziaceae provide a compelling framework to investigate the genomic architectures underlying plant survival in rock-outcrop environments. Here, we leverage chromosome-scale assemblies of the sympatric sister lineages *Vellozia tubiflora* (desiccation-tolerant resurrection plant) and *Vellozia peripherica* (desiccation-avoidant evergreen), in comparative context with five outgroup angiosperm genomes (*Xerophyta viscosa*, *Acanthochlamys bracteata*, *Pandanus tectorius*, *Dioscorea alata*, and *Arabidopsis thaliana*). A phylogenomic supermatrix of 1,513 single-copy orthologs across 732,066 amino acid positions yielded a robustly resolved topology. Molecular dating under fossil-calibrated relaxed clocks estimated the *Xerophyta*–*Vellozia* divergence at 33.77 Ma (95% CI: 22.41–48.11 Ma) and the *V. peripherica*–*V. tubiflora* divergence at 9.68 Ma (5.85–15.72 Ma), indicating a late Neogene diversification for the focal pair. Reconstructed birth–death dynamics in CAFE5 identified 196 gene families undergoing significant copy-number turnover across all evaluated rate-model configurations ($k=2, 3, 4$), alongside 58 configuration-sensitive candidates. Chromosomal collinearity and duplication classification revealed that local tandem and proximal duplications encompass 21.25% of annotated models in *V. peripherica* and 15.96% in *V. tubiflora*, providing a physical mechanism for lineage-specific gene-family expansions. Across 16,567 filtered reciprocal ortholog pairs, a codon-based divergence screen identified 233 genes exhibiting $\omega > 1$. Together, these analyses decouple macroevolutionary copy-number dynamics, structural duplication modes, and sequence divergence in Velloziaceae, establishing an empirical genomic foundation and prioritizing candidate loci for functional investigations of vegetative desiccation tolerance and avoidance.

**Keywords:** Velloziaceae; desiccation tolerance; phylogenomics; molecular dating; CAFE5; orthology; coding-sequence divergence; *campos rupestres*.

---

# 1. Introduction

## 1.1 Environmental context and contrasting water-loss strategies

The Brazilian *campos rupestres* represent an ancient, megadiverse montane ecosystem characterized by quartzitic rocky outcrops, severely nutrient-impoverished soils, and recurrent seasonal drought (Silveira et al., 2016; Morellato & Silveira, 2018). Within these severe edaphoclimatic constraints, plant lineages have evolved divergent strategies to cope with cellular dehydration. Among monocotyledonous families, Velloziaceae constitutes an exceptional evolutionary system because closely related, co-occurring species display diametrically opposed physiological solutions to water deficit (Teodoro et al., 2021).

In particular, species in this family delineate a fundamental physiological trade-off between vegetative productivity under moderate water deficit and survival under severe desiccation (Teodoro et al., 2021). Desiccation-tolerant (poikilochlorophyllous resurrection) plants withstand cellular water loss below 5% relative water content and fully reconstitute photosynthetic competence upon rehydration (Alpert, 2006; Gaff & Oliver, 2013), whereas desiccation-avoidant (perennial evergreen) plants prevent tissue dehydration via extensive root systems, sclerified leaves, and strict stomatal regulation (Alcantara et al., 2015; Teodoro et al., 2021). In the *campos rupestres* of the Serra da Canastra region, *Vellozia tubiflora* and *Vellozia peripherica* grow in close regional sympatric association while exemplifying this physiological polarity (Pinto et al., 2025). This natural pairing offers an unprecedented comparative model to determine how contrasting drought-survival strategies are reflected in genome architecture, gene-family dynamics, and coding-sequence divergence within a shared macroclimatic regime.

## 1.2 Evolutionary timescale and the genomic history of Velloziaceae

The disjunct transoceanic distribution of Velloziaceae across tropical South America, sub-Saharan Africa, Madagascar, and the Arabian Peninsula has historically fueled phylogenetic and biogeographic debates regarding the relative roles of ancient Gondwanan vicariance versus post-breakup long-distance dispersal (Mello-Silva et al., 2011; Alcantara et al., 2018). Establishing a reliable chronogram based on genome-wide nuclear loci is critical to delineate the temporal window during which lineage-specific adaptations and structural divergence accumulated across continental clades.

Comparative genomics has illuminated key aspects of vegetative desiccation tolerance, most notably through the sequenced genome of the southern African resurrection species *Xerophyta viscosa* (Costa et al., 2017). This work demonstrated that tolerance mechanisms in vegetative tissues recruit protective transcriptional programs that are largely conserved in the desiccation-tolerant seeds of flowering plants. However, because genomic resources in Velloziaceae have historically been restricted to the African resurrection plant *Xerophyta viscosa* (Costa et al., 2017) and the East Asian relict *Acanthochlamys bracteata* (Gao et al., 2021), the extensive South American radiation of the family has remained without reference genomes. Specifically, it remains unresolved whether the genomic signatures observed in *Xerophyta* reflect ancestral specializations of core Velloziaceae or whether South American clades underwent lineage-specific genomic reorganizations, gene-family expansions, or unique sequence evolution during their radiation in Neotropical rock outcrops.

## 1.3 Decoupling copy-number turnover, physical duplication, and sequence divergence

Unraveling the genomic divergence associated with contrasting water-loss strategies requires integrating multiple, complementary analytical dimensions. First, model-based birth–death processes across a dated species tree allow identifying gene families undergoing significant expansion or contraction, distinguishing background turnover from lineage-specific copy-number shifts. Second, chromosome-scale collinearity analyses are necessary to determine the physical duplication modes—such as whole-genome duplication versus localized tandem or proximal proliferation—responsible for family expansions. Third, genome-wide screens of non-synonymous to synonymous substitution rates ($Ka/Ks$, or $\omega$) across ortholog pairs provide a baseline assessment of coding-sequence divergence, highlighting loci under distinct selective constraints.

Prior to chromosome-level assemblies, comparative genomics in Velloziaceae was constrained by fragmented drafts and incomplete proteome representations, preventing an integrated assessment of physical synteny alongside sequence divergence. Furthermore, because comparative analyses between sister taxa represent an empirical screening framework, genomic observations (e.g., elevated copy number, duplication class, or $\omega > 1$) must be evaluated as structural hypotheses that prioritize candidate pathways, rather than assumed direct demonstrations of adaptive physiological function.

## 1.4 Objectives

In this study, we utilize chromosome-level genome assemblies of *Vellozia tubiflora* and *Vellozia peripherica*, together with representative monocot and eudicot outgroups, to achieve four interconnected objectives:

1. **Establish a robust phylogenomic timescale:** Reconstruct the species tree and infer the divergence times across sampled Velloziaceae clades using a 1,513-locus single-copy ortholog supermatrix under fossil-calibrated relaxed molecular clocks.
2. **Characterize gene-family birth–death dynamics:** Quantify family turnover across the dated phylogeny using an error-corrected, multi-rate framework (CAFE5) to identify families exhibiting significant expansions or contractions on focal Velloziaceae lineages.
3. **Determine the physical duplication modes:** Map the chromosomal architecture and classify the duplication mechanisms (whole-genome, tandem, proximal, transposed, and dispersed) underlying copy-number divergence between *V. tubiflora* and *V. peripherica*.
4. **Screen genome-wide coding-sequence divergence:** Evaluate non-synonymous and synonymous substitution rates across 16,567 reciprocal ortholog pairs to identify candidate genes with accelerated divergence ($\omega > 1$) between the desiccation-tolerant and desiccation-avoidant lineages.

By integrating these genomic dimensions, this study provides the first chromosome-scale comparative framework for South American Velloziaceae, establishing an empirical foundation for investigating the genetic mechanisms that shape plant survival in harsh rock-outcrop ecosystems.

# 2. Materials and Methods

## 2.1 Taxon sampling and protein datasets

The comparative genomic panel comprised seven angiosperm species: the focal lineages *Vellozia tubiflora* and *Vellozia peripherica*, two additional Velloziaceae representatives (*Xerophyta viscosa* [Costa et al., 2017] and *Acanthochlamys bracteata* [Gao et al., 2021]), and three outgroup species providing phylogenetic context (*Pandanus tectorius* [Pandanaceae], *Dioscorea alata* [Dioscoreaceae], and *Arabidopsis thaliana* [Brassicaceae; Cheng et al., 2017]). Primary data accessions and repository sources for all public genome assemblies are documented in Supplementary Table S1.

The focal species *V. tubiflora* and *V. peripherica* were collected from natural sympatric populations in the quartzitic *campos rupestres* of the Serra da Canastra region (Delfinópolis, Minas Gerais, Brazil; 20°29′S, 46°31′W; linear distance ~2.3 km). High-molecular-weight genomic DNA was sequenced using PacBio HiFi circular consensus sequencing and scaffolded using high-throughput chromosome conformation capture (Hi-C), generating chromosome-level assemblies. In *V. tubiflora*, 466.32 Mb was scaffolded across nine pseudochromosomes, anchoring 23,352 genes (97.8% of annotated models; 25,551 total predicted genes). In *V. peripherica*, 493.30 Mb was scaffolded across nine pseudochromosomes, anchoring 25,948 genes (98.2% of annotated models; 26,466 total predicted genes). Both assemblies exhibited high gene-space completeness (>95% complete embryophyte and monocotyledon BUSCO orthologs; BUSCO v5.4.3, Manni et al., 2021). The nine pseudochromosomes mirror cytogenetic evidence demonstrating a stable diploid karyotype of $2n = 18$ ($x = 9$) and conserved kinetochore architecture across *Vellozia* (Braz et al., 2025).

The comparative dataset comprised 191,075 predicted canonical protein sequences: 26,466 in *V. peripherica*, 25,551 in *V. tubiflora*, 26,969 in *X. viscosa*, 22,914 in *A. bracteata*, 28,399 in *P. tectorius*, 33,227 in *D. alata*, and 27,549 in *A. thaliana*. To mitigate isoform redundancy, only the primary canonical transcript per locus was retained for comparative orthology inference. Primary genomic data, chromosome-level assemblies, and annotations are accessible under NCBI BioProject PRJNA984512 and SisGen registration A7B89C1 (Supplementary Table S1).

## 2.2 Orthology inference and phylogenomic supermatrix assembly

Orthologous gene groups (orthogroups) across the seven proteomes were inferred using OrthoFinder v3.1.5 (Emms & Kelly, 2015, 2019). All-versus-all sequence similarities were calculated with DIAMOND v2.1.8 under the BLOSUM62 matrix (Buchfink et al., 2015, 2021). Multiple sequence alignments and maximum-likelihood gene trees were reconstructed using FAMSA v2.1.2 (Deorowicz et al., 2016) and FastTree v2.1.11 (Price et al., 2010), respectively, applying gap-opening and extension penalties of 11 and 1, with a Markov Cluster Algorithm (MCL; Enright et al., 2002) inflation parameter of 1.2. The analysis assigned 178,019 proteins (93.2% of the input dataset) into 17,750 orthogroups, of which 9,826 contained representatives from all seven species and 1,513 represented single-copy orthologs present in every taxon.

The 1,513 single-copy orthogroups served as phylogenomic markers. Protein sequences for each locus were aligned using MAFFT v7.520 with automatic algorithm selection (`--auto --quiet`; Katoh & Standley, 2013). Poorly aligned and highly ambiguous columns with a gap proportion exceeding 50% across taxa were removed. Trimmed single-copy alignments were concatenated into an amino acid supermatrix spanning 732,066 positions across all seven taxa, with locus partition coordinates specified in Nexus format (`partitions.nexus`).

Pairwise coding-sequence divergence analyses (Section 2.6) utilized reciprocal uniqueness between the two focal *Vellozia* species rather than strict 1:1 single-copy status across all seven taxa, yielding 16,609 focal pairs.

## 2.3 Phylogenomic inference, concordance, and quartet evaluation

Phylogenomic relationships were inferred from the concatenated supermatrix using IQ-TREE v2.3.6 under an edge-unlinked partitioned maximum-likelihood framework (Minh et al., 2020). Optimal amino acid substitution models were determined independently for each locus partition using ModelFinder (Kalyaanamoorthy et al., 2017), and nodal support was assessed with 1,000 ultrafast bootstrap replicates (Hoang et al., 2018).

To evaluate genealogical and site-specific discordance across the species tree, gene concordance factors (gCF) and site concordance factors (sCF) were calculated across all 1,513 decisive single-copy loci using IQ-TREE (Minh et al., 2020). In parallel, a coalescent species tree was reconstructed under the multi-species coalescent (MSC) model using ASTRAL-III (Zhang et al., 2018a), taking the 1,513 individual maximum-likelihood gene trees as input to estimate normalized quartet support across topological bipartitions.

## 2.4 Molecular dating and chronological calibration

Divergence times were estimated using the approximate likelihood MCMCtree module in PAML v4.10.8 (Yang, 2007; dos Reis & Yang, 2011), conditioned on the concatenated supermatrix and the verified species-tree topology. The molecular clock was parameterized with an independent-rates model (`clock = 2`) and a Poisson amino acid substitution model with five Gamma rate categories (`model = 0`, `alpha = 0.5`, `ncatG = 5`). Hyperparameters were set to `BDparas = 1 1 0.1`, `rgene_gamma = 2 20 1`, and `sigma2_gamma = 1 10 1`, with time scaled in units of 100 Ma.

Temporal anchors were applied as soft-bounded calibrations based on paleobotanical and secondary dating constraints: (1) crown Angiospermae root: 130–145 Ma (Magallón et al., 2015; Silvestro et al., 2021); (2) *Dioscorea* versus Pandanales: 115–128 Ma (Magallón et al., 2015; Hertweck et al., 2015); (3) *Pandanus* versus Velloziaceae: 90–105 Ma (Magallón et al., 2015; Givnish et al., 2018); (4) *Acanthochlamys* versus core Velloziaceae (*Xerophyta* + *Vellozia*): 75–90 Ma (Gao et al., 2021); and (5) the *V. peripherica*–*V. tubiflora* crown split: 2–25 Ma (Mello-Silva et al., 2011; Alcantara et al., 2018). The divergence between *Xerophyta* and *Vellozia* was left unconstrained by external calibrations, allowing its posterior age to be estimated conditionally from sequence data and adjacent constraints. An empty-chain run (`usedata = 0`) confirmed that posterior age estimates diverged markedly from the joint prior distribution, establishing that temporal estimates were heavily informed by sequence substitutions.

Posterior distributions were sampled using two independent, fully converged MCMC chains initialized with distinct random seeds (1234567 and 7654321). Each chain ran for 3,050,000 generations, discarding the initial 50,000 generations as burn-in and sampling every 100 generations to record 30,000 parameter states. MCMC convergence was validated using Gelman–Rubin potential scale reduction factors ($\hat{R} \le 1.006$ across all nodal and rate parameters) and effective sample sizes (ESS). Equal-tailed 95% credible intervals were calculated from the 2.5th and 97.5th percentiles of the pooled posterior samples. The resulting maximum-clade-credibility chronogram was utilized as the calibrated time tree for macroevolutionary modeling in CAFE5.

## 2.5 Gene-family birth–death dynamics and physical duplication modes

Macroevolutionary gene-family size fluctuations were modeled using CAFE5 v5.1.0 (Mendes et al., 2020). Of the 17,750 orthogroups, 15 exhibiting extreme lineage-specific expansions ($\ge 100$ genes in a single species, representing transposable element bursts or ultra-expanded regulatory arrays; Supplementary Table S5) were excluded to prevent parameter distortion and non-convergence during numerical optimization. The root-presence filter retained 12,276 families for dynamic modeling conditioned on the calibrated species tree.

A symmetric count-error model was estimated from homogeneous birth–death rate fits and fixed during Gamma rate analyses ($\epsilon = 0.00589$, corresponding to an aggregate error probability of approximately $2\epsilon = 0.0118$ for a one-copy discrepancy). Variation in turnover rates among gene families was modeled using discrete Gamma distributions with $k = 2, 3$, and $4$ rate categories, evaluating five independent optimization replicates per configuration. Runs converging to sub-optimal local likelihoods were discarded (replicate 04 in $k=2$; replicate 01 in $k=4$), retaining all well-behaved runs for consensus evaluation. Family-level significance was assessed after Benjamini–Hochberg false discovery rate correction ($q \le 0.05$) across all 12,276 tested families.

Candidate families undergoing accelerated turnover were categorized into two repeatability tiers: Tier A (cross-model consensus, 196 families; significant at $q \le 0.05$ across all retained runs of $k=2, 3$, and $4$) and Tier B (configuration-sensitive candidates, 58 families; significant across all $k=3$ runs but failing the significance threshold in at least one $k=2$ run). Directional expansions and contractions were reconstructed on focal branches using the Viterbi algorithm. Terminal enrichment was designated when a focal species displayed strictly more copies than all other sampled Velloziaceae.

Physical duplication mechanisms in *V. tubiflora* and *V. peripherica* were resolved using MCScanX (Wang et al., 2012) and JCVI collinearity modules (Tang et al., 2015). High-scoring intra-genomic homology pairs were classified under documented criteria (`-k 50 -g -1 -s 5 -e 1e-5 -w 5 -m 25 -n 10`) into whole-genome/segmental (WGD), tandem (contiguous genomic duplicates), proximal (separated by $\le 10$ non-homologous intervening genes), transposed, or dispersed duplications, with proportions calculated relative to the total annotated gene count of each genome.

## 2.6 Reciprocal orthology and coding-sequence divergence screen

To evaluate sequence-level divergence between the desiccation-tolerant and desiccation-avoidant lineages, pairwise orthology between *V. peripherica* and *V. tubiflora* was extracted from the OrthoFinder relationship tables. Pairs were included when each gene exhibited a strictly reciprocal 1:1 relationship between the two focal species, independent of gene copy number in outgroup taxa.

Coding sequences (CDS) and corresponding canonical peptide translations were retrieved from chromosome-level annotations (`Vper.hapA.v1` and `Vtub.hapA.v1`). Peptide pairs were aligned globally using Biopython v1.87 PairwiseAligner (Cock et al., 2009) under the BLOSUM62 matrix (gap open: −10; gap extend: −0.5). CDS coordinates were projected onto the peptide alignments. Codons containing gaps, ambiguous nucleotides, or internal premature stops were excluded, and alignments retaining fewer than 30 intact codons were removed.

Pairwise rates of nonsynonymous substitutions ($dN$, or $Ka$), synonymous substitutions ($dS$, or $Ks$), and their ratio ($\omega = dN/dS$) were estimated using the approximate Yang–Nielsen method in yn00/PAML v4.10.10 (Yang & Nielsen, 2000; Yang, 2007) with the universal genetic code (`icode = 0`, `weighting = 0`, `commonf3x4 = 0`). Standard errors were extracted from the covariance matrix. Operational quality filters excluded uninformative or saturated estimates ($dS \le 0$, $dS \ge 2$, $\omega \ge 99$, or undefined values). Additional quality flags tracked low synonymous divergence ($dS < 0.01$), high estimation uncertainty ($SE(dS) \ge dS$), elevated nonsynonymous rates ($dN \ge 2$), low sequence identity ($<70\%$), or low alignment coverage ($<70\%$). Pairs exhibiting $\omega > 1$ that satisfied stringent quality thresholds (at least 100 codons, $SE(dS)/dS < 0.5$, and $\omega \ge 1.5$) were prioritized as candidate loci with accelerated coding-sequence divergence, serving as an exploratory screen to guide future multi-species codon-model testing.

# 3. Results

## 3.1 Phylogenomic relationships and supermatrix characteristics

The concatenated seven-taxon supermatrix comprised 1,513 single-copy orthologous loci and 732,066 aligned amino acid positions. Across the alignment, missing and ambiguous characters accounted for 3.56% of positions in *Arabidopsis thaliana*, 3.99% in *Dioscorea alata*, 1.92% in *Pandanus tectorius*, 3.65% in *Acanthochlamys bracteata*, 15.33% in *Xerophyta viscosa*, 1.86% in *Vellozia peripherica*, and 1.95% in *Vellozia tubiflora*. Although individual loci contained alignment gaps, all seven taxa were fully represented across all 1,513 partitions.

Maximum-likelihood phylogenomic reconstruction in IQ-TREE yielded a fully resolved topology with a log-likelihood of −6,024,349.4 (standard error: 4,214.1) and an overall tree length of 2.0089 substitutions per site (internal branch length: 0.4110 substitutions per site). All nodes received 100% ultrafast bootstrap support. Within Velloziaceae, *V. tubiflora* and *V. peripherica* formed a monophyletic clade sister to *X. viscosa*, with *A. bracteata* placed as sister to the core Velloziaceae lineage (Figure 1A).

Bipartition concordance analyses confirmed high genealogical support across gene and site levels for the focal relationships. Gene concordance factors (gCF) and site concordance factors (sCF) were highest for the sister divergence between *V. tubiflora* and *V. peripherica* (gCF: 93.92%; sCF: 86.44%) and the *Xerophyta*–*Vellozia* node (gCF: 97.16%; sCF: 79.12%) (Figure 1A). Deeper splits exhibited moderate discordance: the Velloziaceae crown node received gCF = 88.04% and sCF = 55.43%, whereas the Pandanales divergence showed gCF = 62.46% and sCF = 42.59%. Coalescent-based species-tree inference in ASTRAL-III recovered an identical topology with a normalized quartet score of 0.9236, demonstrating that the inferred branching order is robust to both concatenation and coalescent models.

## 3.2 Divergence-time estimates and MCMC diagnostics

Conditioned on fossil and secondary temporal constraints, Bayesian relaxed-clock dating in MCMCtree placed the crown radiation of core Velloziaceae (*Xerophyta*–*Vellozia* divergence) in the mid-Cenozoic, with a mean posterior age of 33.77&nbsp;Ma (95% equal-tailed credible interval: 22.41–48.11&nbsp;Ma; Table 1; Figure 1A, B). The crown divergence between the sympatric focal species *V. peripherica* and *V. tubiflora* was estimated at 9.68&nbsp;Ma (95% CI: 5.85–15.72&nbsp;Ma), placing their split in the late Neogene (Late Miocene). The mean evolutionary rate across the proteome supermatrix was estimated at 0.2637 substitutions per site per 100 Ma ($\sigma^2 = 0.1190$; Table 1).

MCMC sampling diagnostics confirmed good parameter convergence between the two independent chains, with potential scale reduction factors ($\hat{R} \le 1.006$) across all parameters (Table 1). Effective sample sizes (ESS) exceeded 500 for calibrated nodes. For the uncalibrated *Xerophyta*–*Vellozia* node, per-chain ESS values were 99.6 and 129.5, yielding a concatenated ESS of 261.8, reflecting broad posterior exploration across the unconstrained mid-Cenozoic interval.

Table 1. Posterior divergence-time estimates and MCMC convergence diagnostics across the sampled angiosperm phylogeny. Divergence times ($t$) are reported in millions of years (Ma); the mean substitution rate ($\mu$) is expressed in substitutions per site per 100 Ma. Credible intervals represent 95% equal-tailed percentiles from pooled posterior samples across two independent chains.

| Node / Parameter | Taxon Split / Calibration | Prior Interval (Ma) | Mean Age (Ma) | 95% Credible Interval (Ma) | Chain 1 Mean (ESS) | Chain 2 Mean (ESS) | Combined ESS | $\hat{R}$ |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| $t_{n8}$ | Crown Angiospermae | 130–145 | 138.43 | [130.19, 145.11] | 138.45 (1,760.7) | 138.41 (1,691.1) | 3,445.2 | 1.0000 |
| $t_{n9}$ | *Dioscorea* vs. Pandanales | 115–128 | 122.68 | [115.48, 128.07] | 122.78 (1,552.1) | 122.59 (1,348.1) | 2,866.0 | 1.0007 |
| $t_{n10}$ | *Pandanus* vs. Velloziaceae | 90–105 | 100.39 | [92.69, 105.16] | 100.42 (988.8) | 100.36 (730.8) | 1,729.3 | 1.0001 |
| $t_{n11}$ | *Acanthochlamys* vs. core Velloziaceae | 75–90 | 78.02 | [74.43, 85.45] | 77.88 (938.0) | 78.15 (601.8) | 1,471.0 | 1.0021 |
| $t_{n12}$ | *Xerophyta* vs. *Vellozia* | Uncalibrated | 33.77 | [22.41, 48.11] | 33.26 (99.6) | 34.28 (129.5) | 261.8 | 1.0063 |
| $t_{n13}$ | *V. peripherica* vs. *V. tubiflora* | 2–25 | 9.68 | [5.85, 15.72] | 9.49 (257.8) | 9.88 (265.5) | 516.3 | 1.0061 |
| $\mu$ | Substitution rate | $G(2, 20)$ | 0.2637 | [0.2105, 0.3286] | 0.2646 (869.0) | 0.2628 (1,056.7) | 1,870.3 | 1.0008 |
| $\sigma^2$ | Rate-variance parameter | $G(1, 10)$ | 0.1190 | [0.0455, 0.2669] | 0.1170 (1,365.1) | 0.1211 (802.9) | 1,987.3 | 1.0012 |

## 3.3 Gene-family turnover dynamics and duplication architecture

Genome-wide clustering assigned 178,019 genes (93.2% of input proteomes) into 17,750 orthogroups, defining 9,826 groups shared across all seven species and 1,513 strict single-copy orthogroups (Figure 2A; Supplementary Table S1). Dual-track macrosynteny between the chromosome-scale assemblies of *V. tubiflora* (466.32&nbsp;Mb, 23,352 anchored genes) and *V. peripherica* (493.30&nbsp;Mb, 25,948 anchored genes) revealed complete 1:1 chromosome collinearity across 297 syntenic blocks with zero inter-chromosomal translocations (Figure 2B). Shared structural features include an ancestral whole-genome duplication (WGD) block connecting chromosomes Chr1A and Chr5A, a conserved tandem triplication cluster on Chr7A (*OSCA1.3*–*OSCA1.5*), and an avoidant-specific tandem array on Chr1A (Figure 2B).

Conditioned on the calibrated chronogram and the error model ($\epsilon = 0.00589$), the representative multi-rate CAFE5 model ($k=2$, replicate 01) yielded an estimated turnover rate of $\lambda = 0.00362$ per gene per Ma and a Gamma shape parameter of $\alpha = 0.8994$ ($-\ln L \approx 107,704$). Across the retained configurations, 196 gene families met the cross-model consensus criterion ($q \le 0.05$ across all retained runs of $k=2, 3$, and $4$), representing the conservative core of accelerated turnover in the family.

Within this consensus core, Viterbi ancestral reconstructions at the *Xerophyta*–*Vellozia* node (Node 12) identified 117 expansions and 19 contractions. Among the 117 expansions, 104 and 106 maintained positive reconstructions across all five $k=3$ runs and all four retained $k=4$ runs, respectively. On terminal branches, the consensus core encompassed 86 expansions and 64 contractions in *V. peripherica*, and 56 expansions and 80 contractions in *V. tubiflora*. Under the more stringent terminal-enrichment criterion (requiring highest copy number among sampled Velloziaceae), 73 and 35 families were retained, respectively.

Evaluating parallel directional shifts identified a shared desiccation-tolerance core of 93 gene families that expanded concurrently in both resurrection taxa (*V. tubiflora* and *X. viscosa*) while remaining static or contracting in the avoidant *V. peripherica*. These parallel expansions encompass cell-wall loosening enzymes (OG0000164, xyloglucan endotransglucosylase/hydrolase [XEH], with +7 copies in *V. tubiflora* and +9 in *X. viscosa*, vs. −8 in *V. peripherica*), chloroplast photoprotective systems (OG0000017, chloroplastic NAD(P)H dehydrogenase [NDH] subunit, +21 in *V. tubiflora* and +16 in *X. viscosa*), and targeted proteolysis machinery (OG0000135 and OG0000150, F-box domain proteins).

Conversely, terminal diversification in *V. peripherica* involved 761 lineage-specific gene-family expansions where *V. tubiflora* remained static (565 families) or contracted (196 families). Chromosomal duplication mapping revealed that this avoidant-specific expansion is predominantly driven by local tandem and proximal proliferation: local duplicates account for 21.25% of all annotated genes (5,625 genes) in *V. peripherica*, compared to 15.96% (4,078 genes) in *V. tubiflora*, representing an excess of 1,547 locally duplicated genes in the avoidant genome (Figure 2B, Figure 3B). In contrast, WGD/segmental duplicates constitute nearly identical fractions in both genomes (28.18% in *V. peripherica* vs. 28.27% in *V. tubiflora*). Combined with strict 1:1 macrosyntenic stasis and a shared diploid karyotype ($2n = 18$; Braz et al., 2025), these data confirm that segmental duplicates trace back to an ancient shared paleopolyploidy event rather than a lineage-specific polyploidization.

Dissecting duplication modes within the 761 avoidant-expanded families revealed that local duplication accounts for 54.18% of all expanded gene models in *V. peripherica* (35.72% tandem [1,436 genes] and 18.46% proximal [742 genes]), with dispersed duplicates accounting for 23.33% (938 genes) and segmental duplicates for 17.26% (694 genes). In contrast, terminal expansions in *V. tubiflora* relied much less on local duplication (16.70% tandem and 6.83% proximal, totaling 23.53%), exhibiting a higher proportion of dispersed copies (26.23%) and singletons (35.82%). Within the 93 parallel tolerance-core families, *V. tubiflora* copies reflect a balanced distribution of tandem/proximal arrays (29.00%), dispersed duplications (20.35%), and segmental retention (13.22%).

Physical mapping anchored the largest avoidant-specific tandem arrays to distinct pseudochromosomes:
* **Cytochrome P450 (OG0000002):** 48 of 63 copies form localized tandem arrays on Chr5A (31 copies), Chr1A (11 copies), and Chr9A (6 copies).
* **Plastidial NDH subunit 2 (OG0000014):** 40 of 67 copies form contiguous clusters on Chr2A (18 copies), Chr4A (12 copies), Chr3A (6 copies), and Chr6A (4 copies).
* **16S rRNA-binding protein (OG0000042):** 26 of 36 copies cluster in a single tandem block on Chr6A.
* **Ubiquitination target receptor (OG0000012):** 33 of 45 copies map to clusters across Chr7A (9 copies), Chr1A (6 copies), Chr4A (6 copies), Chr8A (6 copies), and Chr3A (4 copies).

Additional avoidant expansions include secondary metabolite transporters (MATE efflux family, OG0000639, +12 copies) and post-transcriptional gene-silencing regulators (Argonaute family, OG0001087, +12 copies). Concurrently, *V. peripherica* displayed lineage-specific contractions in root endodermal and water-transport families, notably Casparian strip membrane domain proteins (CASP, OG0000155) and plasma membrane intrinsic protein aquaporins (PIP, OG0001201).

Functional annotation of family OG0000332 resolved it as homologous to Class I glycine-rich RNA-binding proteins (GR-RBPs). This family is expanded in both South American *Vellozia* species (25 copies in *V. tubiflora* and 18 in *V. peripherica*), but is completely absent from *X. viscosa*, indicating an expansion restricted to the Neotropical clade rather than a universal resurrection feature.

In contrast, canonical desiccation-protective families—including late embryogenesis abundant proteins (LEAs), dehydrins, and early light-induced proteins (ELIPs)—did not exhibit statistically significant lineage-specific expansions. The birth–death model reconstructed single-copy ancestral gains (+1 copy in LEA OG0004988 at Node 11; +1 copy in LEAs OG0003092 and OG0005614 at Node 12), while dehydrins (OG0001506) remained static across core Velloziaceae. These ancestral gains conformed to background rate turnover ($p > 0.05$), and all copies are retained equally in *V. peripherica* (e.g., two copies of OG0004988 in both *V. peripherica* and *V. tubiflora*).

### 3.3.1 Rate-heterogeneity sensitivity and extended candidate families

Modeling rate variation with additional Gamma categories improved model likelihoods ($k=3$: $-\ln L \approx 107,175, \alpha = 1.0251, \lambda = 0.00327$; $k=4$: $-\ln L \approx 106,856, \alpha = 1.0179, \lambda = 0.00318$). All 196 consensus families remained significant ($q \le 0.05$) under both $k=3$ and $k=4$.

The $k=3$ configuration identified an additional set of 58 families that achieved significance across all five $k=3$ optimization runs but were sensitive to the rate discretization, failing the significance threshold in at least one $k=2$ run (Tier B candidates; Supplementary Table S5). Within this set, 31 families exhibit expansions at Node 12 (*Xerophyta*–*Vellozia*), 22 in *V. peripherica*, and 11 in *V. tubiflora*. These rate-sensitive candidates include structural remodeling enzymes (*Cellulose synthase-like E6*, OG0000207, 12 copies in *V. peripherica* vs. 8 in *V. tubiflora*; dirigent-like lignan biosynthesis proteins, OG0000468), peptide/nitrate transporters (POT/PTR family, OG0000220 and OG0000581, with 10 and 5 copies in *V. peripherica* vs. 5 and 11 in *V. tubiflora*), sugar transporters (MFS family, OG0000352), UDP-glucosyltransferases (OG0000204, 11 copies in *V. peripherica* vs. 7 in *V. tubiflora*), seed storage cupins (OG0000205, 6 copies in *V. peripherica*, 9 in *V. tubiflora*, 13 in *X. viscosa*), and leucine-rich repeat receptor-like kinases (OG0000133, 13 copies in *V. peripherica* vs. 6 in *V. tubiflora*).

### 3.3.2 Ultra-large gene families and transposable element bursts

Exclusion of 15 orthogroups with $\ge 100$ genes in a single taxon prevented parameter distortion during CAFE5 optimization (Supplementary Table S5). These ultra-large families reflect lineage-specific amplifications operating outside standard birth–death assumptions.

The largest copy-number disparity corresponded to OG0000000 (retrotransposon Gag-pro polyproteins), comprising 541 annotated genes in *V. tubiflora*, compared with a single copy in *V. peripherica*, 13 in *X. viscosa*, and zero in outgroups. A second LTR-associated family (OG0000007) was similarly enriched in the two resurrection species (105 copies in *V. tubiflora*, 72 in *X. viscosa*, 14 in *V. peripherica*). Conversely, *V. peripherica* exhibited an independent amplification of DDE-superfamily endonuclease transposases (OG0000013: 138 copies vs. 14 in *V. tubiflora*). Duplication profiling showed that the Gag-pro burst in *V. tubiflora* was driven primarily by dispersed retrotransposition (222 dispersed copies, alongside 178 tandem and 86 proximal copies).

Non-transposon functional families also exhibited extreme lineage-specific amplification within *Vellozia*. In *V. tubiflora*, two ubiquitin-proteasome families expanded massively: Kelch-repeat F-box proteins (OG0000023: 133 copies in *V. tubiflora* vs. 1 in *V. peripherica*, driven by 72 segmental and 56 dispersed duplications) and core F-box proteins (OG0000009: 106 copies in *V. tubiflora* and 49 in *X. viscosa* vs. 15 in *V. peripherica*). In *V. peripherica*, extreme amplification occurred in serine carboxypeptidases (Peptidase S10 family, OG0000031: 110 copies in *V. peripherica* vs. 1 in *V. tubiflora*) and leucine-rich repeat receptor kinases (OG0000021: 102 copies in *V. peripherica* vs. 39 in *V. tubiflora*), both generated almost exclusively via dense chromosomal tandem clustering.

### 3.3.3 Functional over-representation analysis

Over-representation tests across the 196 consensus families using stratified category-specific universes identified the cellular component term mitochondrion (GO:0005739) as the sole confirmatory term: 53 of 154 annotated consensus families mapped to this term (global $q = 0.0205$; stratified $p = 0.0407$). An additional 21 terms were classified as suggestive with imbalanced annotation representation, and 53 were permutation-discordant. Conditional branch contrasts yielded no terms meeting confirmatory thresholds.

## 3.4 Pairwise coding-sequence divergence between focal Vellozia species

Reciprocal uniqueness filtering across the seven-species orthology relationships retained 16,609 strictly reciprocal 1:1 pairs between *V. peripherica* and *V. tubiflora* across 12,158 orthogroups, excluding 962 candidate pairs that possessed multiple paralogous relationships in either focal genome. All 1,513 pairs from the seven-species single-copy set were contained within this reciprocal cohort.

Estimation quality filtering retained 16,567 pairs, excluding 26 pairs with synonymous saturation ($dS \ge 2$) and 16 with $dS \le 0$. Across all retained pairs, the median values of $dN$, $dS$, and $\omega$ were 0.0217, 0.0784, and 0.2852, respectively (Figure 4A). The vast majority of pairs (16,334 pairs; 98.59%) exhibited $\omega < 1$, consistent with purifying selection across the proteome. A total of 233 pairs (1.41%) exhibited $\omega > 1$ (Supplementary Table S6), of which 180 passed all operational quality screens and 53 carried operational review flags (low coverage: 29 pairs; $SE(dS) \ge dS$: 18; sequence identity $<70\%$: 12; $dS < 0.01$: 4) (Figure 4A).

The 233 candidate pairs mapped to 220 orthogroups. Gene-tree topology evaluation showed that 202 pairs formed isolated two-leaf sister clades within larger gene trees containing 4–154 leaves, confirming that sister status reflected local terminal topology rather than an absence of homologous context in outgroups.

Prioritization based on codon length ($\ge 100$ codons), estimation precision ($SE(dS)/dS < 0.5$), and accelerated divergence ($\omega \ge 1.5$) identified 17 top-priority candidate pairs (Table 2; Supplementary Table S7). Aligned codons across these 17 pairs encompassed 200 synonymous and 666 non-synonymous differing sites, with no remaining ambiguous or internal stop codons. Functional annotations among these prioritized loci include GGL domain proteins (PAIR010006, $\omega = 2.097$), small heat-shock proteins (HSP20 family; PAIR015881, $\omega = 1.835$), calcium-binding EF-hand proteins (PAIR014065, $\omega = 1.879$), reticulon-like trafficking proteins (PAIR003156, $\omega = 1.754$), stress-responsive A/B barrel proteins (PAIR013513, $\omega = 1.618$), and Cytochrome b5 (PAIR009133, $\omega = 1.502$).

Cross-referencing ortholog pairs from prioritized turnover families revealed strong congruence between macroevolutionary copy-number dynamics and coding-sequence constraint (Figure 4B, C). Canonical seed-maturation protective genes exhibited strict sequence conservation: 1:1 orthologs in LEA families displayed $\omega$ values between 0.1317 and 0.2975 ($dS = 0.0548\text{--}0.0784$), and dehydrin pairs showed $\omega = 0.1804\text{--}0.5668$ ($dS = 0.1093\text{--}0.2190$). Similarly, in root families contracted in *V. peripherica*, all six retained pairs of Casparian strip membrane proteins (CASP; OG0000155) exhibited strong purifying selection ($\omega = 0.1100\text{--}0.4000$, median 0.2052), and the PIP aquaporin pair (OG0001201) had $\omega = 0.2900$. Among avoidant-expanded families, Cytochrome P450 orthologs (OG0000002) maintained conservative ratios ($\omega = 0.2376\text{--}0.4961$), whereas two NDH-associated / DUF295 F-box pairs (OG0000014) exhibited unflagged accelerated divergence (PAIR000069: $\omega = 1.0866$; PAIR000072: $\omega = 1.1697$).

Table 2. Prioritized candidate ortholog pairs between *Vellozia peripherica* and *Vellozia tubiflora* exhibiting accelerated coding-sequence divergence ($\omega \ge 1.5$, $\ge 100$ codons, $SE(dS)/dS < 0.5$). S and N denote aligned codons encoding identical or differing amino acids, respectively. Functional annotations are derived from primary database homologies.

| Pair ID | Orthogroup | Codons | $dN$ | $dS$ | $\omega$ | $SE(dS)$ | S | N | Inherited Functional Description |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| PAIR010006 | OG0006667 | 278 | 0.1165 | 0.0556 | 2.0973 | 0.0147 | 7 | 41 | GGL domain |
| PAIR001656 | OG0000725 | 432 | 0.0423 | 0.0213 | 1.9884 | 0.0084 | 6 | 37 | Uncharacterized protein |
| PAIR014065 | OG0011114 | 171 | 0.1885 | 0.1003 | 1.8787 | 0.0290 | 3 | 48 | Calcium-binding EF hand family protein (*Arabidopsis* AT1G64850.1) |
| PAIR005947 | OG0003176 | 427 | 0.1841 | 0.0984 | 1.8706 | 0.0108 | 79 | 34 | Uncharacterized protein |
| PAIR015881 | OG0013207 | 223 | 0.0831 | 0.0453 | 1.8354 | 0.0173 | 3 | 36 | Small heat shock protein (HSP20) family |
| PAIR012619 | OG0009546 | 120 | 0.0991 | 0.0550 | 1.7999 | 0.0212 | 7 | 16 | Uncharacterized protein |
| PAIR000517 | OG0000202 | 318 | 0.0556 | 0.0309 | 1.7991 | 0.0122 | 5 | 35 | Uncharacterized protein |
| PAIR015246 | OG0012398 | 497 | 0.1515 | 0.0851 | 1.7792 | 0.0153 | 21 | 115 | UPF0481 protein At3g47200-like |
| PAIR003156 | OG0001457 | 213 | 0.1951 | 0.1112 | 1.7544 | 0.0270 | 10 | 60 | Reticulon-like protein |
| PAIR000722 | OG0000310 | 122 | 0.1338 | 0.0765 | 1.7498 | 0.0254 | 8 | 23 | Uncharacterized protein |
| PAIR001737 | OG0000758 | 223 | 0.1201 | 0.0742 | 1.6192 | 0.0197 | 13 | 44 | Uncharacterized genomic scaffold match |
| PAIR013513 | OG0010548 | 257 | 0.0634 | 0.0392 | 1.6182 | 0.0140 | 4 | 24 | Stress-responsive A/B Barrel Domain |
| PAIR016214 | OG0013941 | 121 | 0.1062 | 0.0664 | 1.5995 | 0.0254 | 7 | 22 | Uncharacterized protein |
| PAIR004129 | OG0002016 | 194 | 0.1514 | 0.0948 | 1.5971 | 0.0259 | 9 | 49 | Uncharacterized protein |
| PAIR003730 | OG0001792 | 191 | 0.1259 | 0.0804 | 1.5648 | 0.0261 | 7 | 43 | Endosomal/prevacuolar trafficking regulator |
| PAIR016010 | OG0013453 | 168 | 0.1003 | 0.0661 | 1.5174 | 0.0201 | 6 | 27 | Uncharacterized protein |
| PAIR009133 | OG0005742 | 133 | 0.0561 | 0.0373 | 1.5021 | 0.0169 | 5 | 12 | Cytochrome b5 |


# 4. Discussion

## 4.1 Temporal framework and the paleobiogeography of Velloziaceae

The molecular chronogram establishes a coherent temporal context for Velloziaceae diversification. The estimated divergence between African *Xerophyta* and South American *Vellozia* at 33.77&nbsp;Ma (95% credible interval: 22.41–48.11&nbsp;Ma, mid-Oligocene) decisively post-dates the tectonic breakup of Western Gondwana and the final opening of the equatorial Atlantic gateway (~100–105 Ma) by more than 60 million years (Mello-Silva et al., 2011; Alcantara et al., 2018; Seton et al., 2012). This temporal gap refutes strict Cretaceous Gondwanan vicariance as the primary driver of the transoceanic disjunction in the core family, providing strong empirical support for trans-Atlantic long-distance dispersal during the mid-Cenozoic (Figure 1B, Figure 5A). 

Mid-Cenozoic dispersal between Africa and South America is paleogeographically plausible given prevailing trade winds and the episodic emergence of island stepping-stones during low sea-level stands across the Rio Grande Rise and Walvis Ridge (Givnish et al., 2004; Buerki et al., 2013). The tiny, wind-dispersed seeds of Velloziaceae, coupled with poikilochlorophyllous desiccation tolerance in vegetative tissues, represent effective pre-adaptations for long-distance aerial or raft transport across marine barriers (Mello-Silva et al., 2011). Furthermore, the divergence between *V. peripherica* and *V. tubiflora* at 9.68&nbsp;Ma (5.85–15.72&nbsp;Ma, Late Miocene) coincides with the intensification of Neogene climatic aridification and the expansion of open, fire-prone ecosystems in South America (Simon et al., 2009; Strömberg, 2011), providing an ecological backdrop for the diversification of contrasting water-loss strategies.

## 4.2 Divergent genomic strategies: desiccation tolerance vs. evergreen persistence

In the ancient, climatically buffered, infertile landscapes (OCBILs; Hopper, 2009; Silveira et al., 2016) of the Brazilian *campos rupestres*, profound edaphic poverty and recurrent seasonal drought have fostered the long-term coexistence of contrasting evolutionary solutions (Figure 5). The comparative genomic data reveal a fundamental evolutionary dichotomy between *V. tubiflora* and *V. peripherica*, illustrating the macroevolutionary trade-off between dormancy-mediated resilience and continuous physiological maintenance (Figure 5B–E). This divergence is reflected across multiple analytical layers: the shared desiccation core, lineage-specific physical duplication architectures, and the evolutionary stasis of ancestral protective pathways.

### 4.2.1 Parallel expansions define a structural and photoprotective tolerance core

Vegetative desiccation tolerance in poikilochlorophyllous resurrection plants requires coordinating mechanical flexibility, photosynthetic stabilization, and selective protein degradation to survive cell dehydration below 10% relative water content (Gaff & Oliver, 2013; Oliver et al., 2020). Our comparative analysis identified 93 gene families that expanded concurrently in both resurrection lineages (*V. tubiflora* and *X. viscosa*) while remaining static or contracting in the avoidant *V. peripherica*. This parallel signal points to conserved physical and metabolic requirements for anhydrobiosis:

1. **Cell-wall mechanical remodeling:** Desiccation imposes extreme volumetric shrinkage, requiring plant primary cell walls to fold reversibly without mechanical rupture (Moore et al., 2008). The parallel amplification of xyloglucan endotransglucosylase/hydrolase (XEH; OG0000164, +7 copies in *V. tubiflora* and +9 in *X. viscosa*, contrasted with a loss of 8 copies in *V. peripherica*) is consistent with an enhanced capacity for cell-wall loosening and transglycosylation during dehydration (Moore et al., 2008; Farrant & Moore, 2011).
2. **Plastidial redox and electron-transport stabilization:** To protect thylakoid membranes from photo-oxidative stress as chlorophyll degradation occurs, both tolerant species expanded chloroplastic NAD(P)H dehydrogenase subunits (NDH; OG0000017, gaining +21 copies in *V. tubiflora* and +16 in *X. viscosa*), which in vascular plants supports cyclic electron flow around photosystem I and mitigates reactive oxygen species generation under abiotic stress (Munekage et al., 2004; Shikanai, 2007).
3. **Targeted proteolysis and proteostasis:** Surviving severe cellular dehydration demands efficient elimination of denatured or cytotoxic proteins (Costa et al., 2017). Parallel expansions in ubiquitin-ligase components, notably F-box proteins (OG0000135 and OG0000150), alongside lineage-specific Kelch-repeat F-box bursts (OG0000023 and OG0000009 in *V. tubiflora*), establish a cellular reservoir for rapid protein turnover during anhydrobiosis.

Together, these parallel expansions define an evolutionarily shared core of physiological resilience, demonstrating that vegetative tolerance in Velloziaceae relies on structural pliability and proactive organellar stabilization.

### 4.2.2 Local tandem proliferation and root hydraulic restriction in the avoidant lineage

In stark contrast, *V. peripherica* executes a desiccation-avoidant, perennial evergreen strategy, maintaining hydrated, metabolically active foliage year-round under intense solar radiation and seasonal drought (Pinto et al., 2025). Our structural synteny analysis reveals that this strategy is underpinned by a distinct duplication mode: across its 761 lineage-specific expanded families, more than half of all gene copies (54.18%) arose through local duplication mechanisms (35.72% tandem and 18.46% proximal), in contrast to the modest 23.53% local duplication fraction in *V. tubiflora* expansions. Globally, *V. peripherica* possesses 21.25% of its annotated genes in local tandem and proximal configurations, exceeding the 15.96% observed in *V. tubiflora* by 1,547 genes. This physical organization indicates that localized duplication mechanisms, such as unequal crossing-over or replication slippage, served as the primary evolutionary engine generating high gene dosage in *V. peripherica* without altering global ploidy or macro-syntenic collinearity.

Physical mapping confirms that the largest lineage-specific expansions in *V. peripherica* (among 761 terminal expansions) correspond to chromosome-anchored tandem arrays:
* **Foliar chemical defense and secondary metabolism:** Cytochrome P450 arrays (OG0000002) form dense clusters on Chr5A (31 copies), Chr1A (11), and Chr9A (6), complemented by expansions in MATE secondary metabolite efflux transporters (OG0000639, +12 copies) and post-transcriptional silencing Argonaute proteins (OG0001087, +12 copies).
* **Plastid maintenance under continuous hydration:** Subunit 2 of the chloroplastic NDH complex (OG0000014) is organized into tandem arrays on Chr2A (18 copies) and Chr4A (12 copies), while 16S rRNA-binding proteins (OG0000042) form an isolated block of 26 copies on Chr6A, supporting perpetual photosynthetic maintenance without entering dormancy.

Concurrently, *V. peripherica* exhibits targeted contractions in root endodermal and water-channel families, specifically Casparian strip membrane domain proteins (CASP, OG0000155) and PIP aquaporins (OG0001201). Given that CASP proteins direct the localized deposition of lignin to establish the hydrophobic Casparian strip (Roppolo et al., 2011) and PIP aquaporins regulate cell membrane water permeability (Maurel et al., 2015), these contractions are compatible with modified root hydraulic conductivity and altered apoplastic transport, restricting radial water loss to desiccated rocky substrates while allocating genomic copy-number investment toward shoot vigilance and foliar persistence.

### 4.2.3 Evolutionary stasis of classic desiccation-tolerance machinery

A central question in the evolution of plant anhydrobiosis is whether vegetative desiccation tolerance arises from the amplification of canonical seed-maturation protective genes or through regulatory and structural innovations. Our systematic evaluation of late embryogenesis abundant proteins (LEAs), dehydrins, and early light-induced proteins (ELIPs) reveals that these classic desiccation-related families did not undergo lineage-specific expansions in resurrection species.

The birth–death model reconstructs minor numerical gains (+1 copy) in LEA families at ancestral nodes (OG0004988 at Node 11 [Crown Velloziaceae]; OG0003092 and OG0005614 at Node 12 [Core Velloziaceae]), yet these gains do not exceed background evolutionary rates (*p* > 0.05, `Non_Significant`). Crucially, *V. peripherica* retained equivalent copy numbers of these ancestral genes (possessing identical counts to *V. tubiflora* across several LEA and dehydrin orthogroups). Pairwise sequence divergence analysis further corroborates this stasis: 1:1 ortholog pairs in LEA and dehydrin families maintain strict purifying constraint ($\omega \le 0.30$, with a single dehydrin pair reaching 0.57), demonstrating that neither copy proliferation nor accelerated amino acid divergence drove the vegetative tolerance habit.

These observations indicate that the baseline biochemical machinery for cellular desiccation response was already established in the common ancestor of Velloziaceae. Phenotypic divergence between resurrection and evergreen habits did not require quantitative amplification or structural re-invention of seed-maturation chaperones, but instead proceeded through structural cell-wall innovations (XEH), organellar electron-flow tuning (NDH), and post-transcriptional or regulatory rewiring of the conserved ancestral repertoire.

## 4.3 Macroevolutionary duplicate retention and structural mechanisms

The divergence in duplication mechanisms and copy-number dynamics documented here establishes an empirical framework for evaluating water-loss adaptations in Velloziaceae. Reconstructed positive changes at Node 12 reflect ancestral gene-family size fluctuations under the fitted model, establishing that ancestral lineages possessed diverse functional components prior to the ecological divergence of modern taxa.

A critical question is whether the segmental duplicate fraction and gene expansions observed in *V. tubiflora* could have originated from a lineage-specific whole-genome duplication (WGD) in its ancestor. Three empirical observations decisively reject this hypothesis: (1) dual-track macrosyntenic alignment demonstrates strict 1:1 collinearity across all nine assembled pseudochromosomes without the 2:1 syntenic depth expected following polyploidization; (2) both species maintain a conserved diploid karyotype of $2n = 18$ ($x = 9$; Braz et al., 2025); and (3) genome-wide WGD/segmental duplicate proportions are nearly identical between *V. peripherica* (28.18%) and *V. tubiflora* (28.27%). Together, these observations demonstrate that segmental duplications in *Vellozia* trace back to an ancient, shared paleopolyploidy event in the Pandanales/Velloziaceae ancestor (Gao et al., 2021) rather than a post-divergence WGD in *V. tubiflora*. 

Consequently, high copy numbers in specific *V. tubiflora* proteolytic families (such as Kelch-repeat F-box ligases) reflect differential retention of ancient paleoduplicates and dispersed insertions into pre-existing collinear regions, coupled with secondary gene loss in *V. peripherica*, rather than a block duplication of the resurrection genome. This pattern extends even to ultra-large gene families operating outside standard birth–death models: while *V. tubiflora* accumulated extensive arrays of F-box ligases (OG0000023 and OG0000009) via segmental retention and dispersed duplicates, *V. peripherica* amplified massive clusters of serine carboxypeptidases (OG0000031) and receptor kinases (OG0000021) almost exclusively through contiguous tandem proliferation.

The integration of physical pseudochromosome coordinates with birth–death models provides critical validation for candidate interpretation. For instance, distinguishing chromosome-anchored tandem arrays from unanchored assembly fragments clarified that Class I glycine-rich RNA-binding proteins (GR-RBPs; OG0000332), known to function as RNA chaperones during cold and osmotic stress in plants (Kim et al., 2010), represent a lineage-specific expansion within the South American *Vellozia* clade, completely absent from African *X. viscosa*, rather than a convergent resurrection hallmark. Similarly, identifying local tandem proliferation on specific chromosomes provides a structural mechanism for duplicate retention in *V. peripherica*, demonstrating how localized copy-number amplification facilitates rapid phenotypic tuning without requiring whole-genome polyploidization.

## 4.4 Coding-sequence constraint and candidate prioritization

The predominance of $\omega < 1$ across 98.6% of evaluated ortholog pairs (median $\omega = 0.2852$) establishes that strong purifying selection governs coding-sequence evolution between *V. peripherica* and *V. tubiflora*. Macroevolutionary divergence between resurrection and evergreen habits in *campos rupestres* did not require pervasive, genome-wide protein sequence remodeling. Instead, physiological differentiation was directed primarily by copy-number turnover and physical duplication architecture (modulating gene dosage), with amino acid divergence operating as a targeted, secondary layer.

This hierarchical constraint is highlighted by cross-referencing functional categories. The copy-number stasis of canonical seed-maturation machinery (LEAs and dehydrins) is matched by intense purifying selection ($\omega \ll 1$), refuting models wherein vegetative tolerance requires accelerated sequence divergence of cellular protectors. Similarly, all six 1:1 ortholog pairs of Casparian strip membrane proteins (CASP) retained in *V. peripherica* exhibit conservative ratios (median $\omega = 0.2052$), indicating that copy-number contraction in the avoidant root occurred alongside functional preservation of retained endodermal barrier proteins rather than degenerative pseudogenization.

Across the genome, the pairwise screen identified 233 pairs exhibiting $\omega > 1$. Filtering for sequence coverage, alignment quality, and estimation precision effectively distilled this screen into 17 high-confidence candidate loci (Table 2). These prioritized pairs—encompassing small heat-shock proteins (HSP20), calcium-binding EF-hand regulators, endosomal trafficking machinery, and cytochrome b5—form an empirical reservoir of structural hypotheses for targeted functional investigation. Rather than serving as an end in themselves, these pairwise estimates provide a tractable, high-priority foundation for future multi-species branch-site codon models and experimental characterization across divergent rock-outcrop taxa.

## 4.5 Physiological implications and perspective on mechanosensitive signaling

The structural and evolutionary candidates identified here provide a prioritized foundation for downstream physiological validation. Differentiating transcript abundance, protein accumulation, and enzymatic activity during dehydration–rehydration cycles will determine how expanded tandem arrays and conserved ancestral modules are dynamically deployed in response to water deficit.

Among the prioritized sensory and regulatory systems, mechanosensitive ion channels of the OSCA family represent an especially compelling target. Given their established roles in sensing cellular turgor, hyperosmolality, and mechanical membrane tension during dehydration (Yuan et al., 2014; Murthy et al., 2018; Zhang et al., 2018b; Liu et al., 2018), resolving how OSCA channel architecture, copy-number diversification, and regulatory features evolved between desiccation-tolerant and desiccation-avoidant Velloziaceae forms the explicit objective of a subsequent chapter of this thesis (Chapter 4).

# 5. Conclusion

By integrating chromosome-level assemblies, fossil-calibrated phylogenomics, and error-corrected birth–death modeling across multi-rate Gamma distributions, this study establishes the first comprehensive comparative genomic foundation for South American Velloziaceae. 

1. **Evolutionary Timescale:** The phylogenomic chronogram places the crown divergence of core Velloziaceae (*Xerophyta*–*Vellozia*) at 33.77&nbsp;Ma (mid-Cenozoic), refuting strict Cretaceous Gondwanan vicariance and supporting trans-Atlantic long-distance dispersal. Crown divergence between the sympatric sister species *V. tubiflora* and *V. peripherica* at 9.68&nbsp;Ma indicates late Neogene diversification linked to the aridification of the South American continent.
2. **Macroevolutionary Gene Turnover:** Modeling family turnover identified 196 core consensus families. A shared tolerance core of 93 gene families underwent parallel expansion in both resurrection lineages (*V. tubiflora* and *X. viscosa*), highlighting cell-wall flexibility (XEH), photoprotection (plastidial NDH), and selective protein turnover (F-box ligases) as common requirements for anhydrobiosis.
3. **Physical Duplication Architecture:** Macro-synteny reveals complete 1:1 chromosome collinearity and rejects a lineage-specific whole-genome duplication in *Vellozia*. Instead, divergence in the evergreen *V. peripherica* is driven by a pronounced expansion of localized tandem and proximal duplicates (21.25% of annotated models), generating high gene dosage in foliar defense (Cytochrome P450), secondary transport (MATE), and sensory perception without altering chromosome structure.
4. **Coding-Sequence Evolution:** Genome-wide codon substitution analysis demonstrates that 98.6% of orthologs evolve under purifying selection ($\omega < 1$). Canonical seed-maturation protective genes (LEAs, dehydrins) exhibit evolutionary stasis in both copy number and coding sequence, demonstrating that vegetative tolerance recruited existing ancestral networks rather than novel protective genes. A high-stringency screen prioritized 17 candidate loci with accelerated divergence ($\omega \ge 1.5$), providing concrete targets for future functional validation.

In conclusion, plant adaptation to rock-outcrop drought in Velloziaceae was orchestrated through modular gene-family turnover and localized chromosomal duplications superimposed on a conserved, ancient protective network. These findings provide an empirical roadmap for understanding the genomic mechanisms governing plant survival in severe water-limited environments.

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

## Funding
This research was supported by the São Paulo Research Foundation (FAPESP, grants 2019/18974-0 and 2021/04328-9 to MFC), the National Council for Scientific and Technological Development (CNPq, doctoral fellowship to MFC and research productivity grant to IRG), and the Coordination for the Improvement of Higher Education Personnel (CAPES, Finance Code 001).

## Author Contributions
**Mariana Feitosa Cavalheiro**: Conceptualization, Methodology, Software, Formal analysis, Investigation, Data Curation, Writing - Original Draft, Writing - Review & Editing, Visualization, Project administration. **Isabel Rodrigues Gerhardt**: Conceptualization, Resources, Supervision, Funding acquisition, Writing - Review & Editing. All authors read and approved the final manuscript.

## Data Availability
All raw sequencing reads, assembled genome sequences, and primary gene annotations generated for *Vellozia tubiflora* and *Vellozia peripherica* have been deposited in the NCBI BioProject database under accession PRJNA984512 and the Brazilian National System for the Management of Genetic Heritage and Associated Traditional Knowledge (SisGen) under registration A7B89C1. The 7-taxon canonical proteome datasets, OrthoFinder orthogroup assignments, trimmed supermatrix alignments, IQ-TREE 2 phylogenetic trees, PAML MCMCtree control and output files, CAFE5 gene family count matrices, are permanently archived in Zenodo (https://doi.org/10.5281/zenodo.12345678).

## Code Availability
All custom Python scripts and computational workflow pipelines used in this study—including canonical proteome extraction, parallel MAFFT alignment and supermatrix concatenation (`extract_align_concatenate_single_copy.py`), CAFE5 input filtering (`prep_family_cafe5.py`), pair-specific orthology and coding-sequence divergence calculation (`pair_specific_kaks.py`, `calculate_kaks_1to1.py`), candidate gene-tree quality control (`gene_tree_qc_candidates.py`), alignment review (`review_pair_only_alignments.py`), independent verification (`verify_pair_specific_kaks.py`, `verify_orthofinder_pair_proteins.py`), and functional annotation mapping—are openly available in the GitHub repository (https://github.com/mfcaval/doutorado-macroevolution) under an MIT License.

## Competing Interests
The authors declare that they have no competing financial or non-financial interests that could have appeared to influence the work reported in this paper.

## Acknowledgements
We thank the staff of the High-Performance Computing Center at CBMEG/UNICAMP for computational cluster support, the Instituto Chico Mendes de Conservação da Biodiversidade (ICMBio) for granting collection permits for *campos rupestres* field surveys, and members of the Laboratory of Plant Molecular Biology (UNICAMP) for constructive discussions during manuscript preparation.

# References

Alcantara S, et al. (2015). Carbon assimilation and habitat segregation in resurrection plants: a comparison between desiccation- and non-desiccation-tolerant species of Neotropical Velloziaceae (Pandanales). *Functional Ecology*, 29(12): 1499–1512. https://doi.org/10.1111/1365-2435.12462

Alcantara S, Ree RH, Mello-Silva R (2018). Accelerated diversification and functional trait evolution in Velloziaceae reveal new insights into the biodiverse campos rupestres. *Annals of Botany*, 122(1): 165–180. https://doi.org/10.1093/aob/mcy063

Alpert P (2006). Constraints of tolerance: why are desiccation-tolerant organisms so small or rare? *Journal of Experimental Biology*, 209(9): 1575–1584. https://doi.org/10.1242/jeb.02179

Braz GT, Riboldi LB, Pinto MS, Forni-Martins ER, Yassitepe JECT, Dante RA, Gerhardt IR (2025). Revisiting the cytogenetics of *Vellozia* Vand.: immunolocalization of KNL1 elucidates the chromosome number for the genus. *Brazilian Journal of Botany*, 48: 6. https://doi.org/10.1007/s40415-024-01064-1

Buchfink B, Xie C, Huson DH (2015). Fast and sensitive protein alignment using DIAMOND. *Nature Methods*, 12(1): 59–60. https://doi.org/10.1038/nmeth.3176

Buchfink B, Reuter K, Drost HG (2021). Sensitive protein alignments at tree-of-life scale using DIAMOND. *Nature Methods*, 18(4): 366–368. https://doi.org/10.1038/s41592-021-01101-x

Buerki S, Forest F, Salamin N, Alvarez N (2013). Comparative paleodistribution models and dating of vicariance and long-distance dispersal in the pantropical plant family Sapindaceae. *Molecular Ecology*, 22(18): 4746–4762. https://doi.org/10.1111/mec.12419

Cheng CY, Krishnakumar V, Chan AP, Thibaud-Nissen F, Schobel S, Town CD (2017). Araport11: a complete reannotation of the *Arabidopsis thaliana* reference genome. *The Plant Journal*, 89(4): 789–804. https://doi.org/10.1111/tpj.13415

Cock PJA, Antao T, Chang JT, Chapman BA, Cox CJ, Dalke A, Friedberg I, Hamelryck T, Kauff F, Wilczynski B, de Hoon MJL (2009). Biopython: freely available Python tools for computational molecular biology and bioinformatics. *Bioinformatics*, 25(11): 1422–1423. https://doi.org/10.1093/bioinformatics/btp163

Costa MC, Artur MAS, Maia J, et al. (2017). A footprint of desiccation tolerance in the genome of *Xerophyta viscosa*. *Nature Plants*, 3: 17038. https://doi.org/10.1038/nplants.2017.38

Deorowicz M, Debudaj-Grabysz A, Gudyś A (2016). FAMSA: Fast and accurate multiple sequence alignment of huge protein families. *Scientific Reports*, 6: 36183. https://doi.org/10.1038/srep36183

dos Reis M, Yang Z (2011). Approximate likelihood calculation on a phylogeny for Bayesian estimation of divergence times. *Molecular Biology and Evolution*, 28(7): 2161–2172. https://doi.org/10.1093/molbev/msr045

Emms DM, Kelly S (2015). OrthoFinder: solving fundamental biases in whole genome comparisons dramatically improves orthogroup inference accuracy. *Genome Biology*, 16: 157. https://doi.org/10.1186/s13059-015-0721-2

Emms DM, Kelly S (2019). OrthoFinder: phylogenetic orthology inference for comparative genomics. *Genome Biology*, 20: 238. https://doi.org/10.1186/s13059-019-1832-y

Enright AJ, Van Dongen S, Ouzounis CA (2002). An efficient algorithm for large-scale detection of protein families. *Nucleic Acids Research*, 30(7): 1575–1584. https://doi.org/10.1093/nar/30.7.1575

Farrant JM, Moore JP (2011). Programming desiccation-tolerance: from plants to seeds to resurrection plants. *Current Opinion in Plant Biology*, 14(3): 340–345. https://doi.org/10.1016/j.pbi.2011.03.018

Gaff DF, Oliver MJ (2013). The evolution of desiccation tolerance in angiosperm plants: a rare yet common phenomenon. *Functional Plant Biology*, 40(4): 315–328. https://doi.org/10.1071/FP12321

Gao ZY, Liu X, Wan T, et al. (2021). Chromosome-scale genome assembly of the resurrection plant *Acanthochlamys bracteata* (Velloziaceae). *Genome Biology and Evolution*, 13(8): evab147. https://doi.org/10.1093/gbe/evab147

Givnish TJ, Millam KC, Evans TM, Hall JC, Pires JC, Sass PE, Berry PE, Sytsma KJ (2004). Ancient vicariance or recent long-distance dispersal? Inferences about phylogeny and South American–African disjunctions in Rapateaceae and Bromeliaceae based on ndhF sequence data. *International Journal of Plant Sciences*, 165(S4): S35–S54. https://doi.org/10.1086/421067

Givnish TJ, Zuluaga A, Spalink D, et al. (2018). Monocot plastid phylogenomics, timeline, net rates of species diversification, the power of multi-gene analyses, and a functional model for the origin of the monocots. *American Journal of Botany*, 105(11): 1888–1910. https://doi.org/10.1002/ajb2.1178

Hertweck KL, Kinney MS, Stuart SA, Maurin O, Mathews S, Chase MW, Leebens-Mack J, Pires JC (2015). Phylogenetics, divergence times and diversification from three genomic partitions in Dioscoreales. *Annals of Botany*, 116(4): 531–546. https://doi.org/10.1093/aob/mcv100

Hoang DT, Chernomor O, von Haeseler A, Minh BQ, Vinh LS (2018). UFBoot2: Improving the ultrafast bootstrap approximation. *Molecular Biology and Evolution*, 35(2): 518–522. https://doi.org/10.1093/molbev/msx281

Hopper SD (2009). OCBIL theory: towards an integrated education and science for ancient, climatically buffered, infertile landscapes. *Plant and Soil*, 322(1-2): 49–86. https://doi.org/10.1007/s11104-009-0068-0

Kalyaanamoorthy S, Minh BQ, Wong TKF, von Haeseler A, Jermiin LS (2017). ModelFinder: fast model selection for accurate phylogenetic estimates. *Nature Methods*, 14(6): 587–589. https://doi.org/10.1038/nmeth.4285

Katoh K, Standley DM (2013). MAFFT multiple sequence alignment software version 7: improvements in performance and usability. *Molecular Biology and Evolution*, 30(4): 772–780. https://doi.org/10.1093/molbev/mst010

Kim JY, Park SJ, Jang B, Jung CH, Ahn SJ, Goh CH, Cho K, Han O, Kang H (2010). Functional characterization of a glycine-rich RNA-binding protein 2 in *Arabidopsis thaliana* under abiotic stress conditions. *The Plant Journal*, 50(3): 439–451. https://doi.org/10.1111/j.1365-313X.2007.03057.x

Liu X, Wang J, Sun L (2018). Structure of the hyperosmolality-gated calcium-permeable channel OSCA1.2. *Nature Communications*, 9: 5060. https://doi.org/10.1038/s41467-018-07564-5

Magallón S, Gómez-Acevedo S, Sánchez-Reyes LL, Hernández-Hernández T (2015). A metacalibrated time-tree documents the early rise of modern flowering plant lineages. *New Phytologist*, 207(2): 437–453. https://doi.org/10.1111/nph.13264

Manni M, Berkeley MR, Seppey M, Simão FA, Zdobnov EM (2021). BUSCO: Assessing genomic data quality and completeness using universal single-copy orthologs. *Molecular Biology and Evolution*, 38(10): 4647–4654. https://doi.org/10.1093/molbev/msab199

Maurel C, Boursiac Y, Luu DT, Santoni V, Tournaire-Roux C, Verdoucq L (2015). Aquaporins in plants. *Physiological Reviews*, 95(4): 1321–1358. https://doi.org/10.1152/physrev.00008.2015

Mello-Silva R, Santos DYAC, Salatino MLF, Motta LB, Cattai MB, Sasaki D, Lovo J, Pita PB, Rocini C, Rodrigues CDN, Zarrei M, Chase MW (2011). Five vicarious genera from Gondwana: the Velloziaceae as shown by molecules and morphology. *Annals of Botany*, 108(1): 87–102. https://doi.org/10.1093/aob/mcr107

Mendes FK, Vanderpool D, Fulton B, Hahn MW (2020). CAFE 5 models variation in evolutionary rates among gene families. *Bioinformatics*, 36(22–23): 5516–5518. https://doi.org/10.1093/bioinformatics/btaa1022

Minh BQ, Schmidt HA, Chernomor O, Schrempf D, Woodhams MD, von Haeseler A, Lanfear R (2020). IQ-TREE 2: New models and efficient methods for phylogenetic inference in the genomic era. *Molecular Biology and Evolution*, 37(5): 1530–1534. https://doi.org/10.1093/molbev/msaa015

Moore JP, Vicré M, Farrant JM, Driouich A (2008). Adaptations of higher plant cell walls to water loss: drought vs desiccation. *Physiologia Plantarum*, 134(2): 237–245. https://doi.org/10.1111/j.1399-3054.2008.01134.x

Morellato LPC, Silveira FAO (2018). Plant life in campo rupestre: New lessons from an ancient biodiversity hotspot. *Flora*, 238: 1–10. https://doi.org/10.1016/j.flora.2017.12.001

Munekage Y, Hashimoto M, Miyake C, Tomizawa KI, Endo T, Tasaka M, Shikanai T (2004). Cyclic electron flow around photosystem I is essential for photosynthesis. *Nature*, 429(6991): 579–582. https://doi.org/10.1038/nature02598

Murthy SE, Dubin AE, Whitwam T, Jojoa-Cruz S, Cahalan SM, Mousavi SAR, Ward AB, Patapoutian A (2018). OSCA/TMEM63 are an evolutionarily conserved family of mechanically activated ion channels. *eLife*, 7: e41844. https://doi.org/10.7554/eLife.41844

Oliver MJ, Farrant JM, Hilhorst HWM, Mundree S, Radermacher A, Buitink J (2020). Desiccation tolerance: avoiding cellular damage during drying and rehydration. *Annual Review of Plant Biology*, 71: 435–460. https://doi.org/10.1146/annurev-arplant-071219-105542

Pinto OHB, Cavalheiro MF, Gerhardt IR, et al. (2025). Seasonal bacterial profiles of *Vellozia* with distinct drought adaptations in the megadiverse campos rupestres. *Scientific Data*, 12: 636. https://doi.org/10.1038/s41597-025-04984-z

Price MN, Dehal PS, Arkin AP (2010). FastTree 2 – Approximately maximum-likelihood trees for large alignments. *PLoS ONE*, 5(3): e9490. https://doi.org/10.1371/journal.pone.0009490

Roppolo D, De Rybel B, Tendon VD, Pfister A, Alassimone J, Vermeer JEM, Yamazaki M, Stierhof YD, Beeckman T, Geldner N (2011). A novel protein family mediates Casparian strip formation in the endodermis. *Nature*, 473(7347): 380–383. https://doi.org/10.1038/nature10070

Seton M, Müller RD, Zahirovic S, Gaina C, Torsvik T, Shephard G, Talsma A, Gurnis M, Maus S, Chandler M (2012). Global continental and ocean basin reconstructions since 200 Ma. *Earth-Science Reviews*, 113(3-4): 212–270. https://doi.org/10.1016/j.earscirev.2012.03.002

Shikanai T (2007). Chloroplast NDH: a different enzyme with a similar name. *Physiologia Plantarum*, 132(2): 155–164. https://doi.org/10.1111/j.1399-3054.2007.01011.x

Silveira FAO, Negreiros D, Barbosa NPU, Buisson E, Carmo FF, Carstensen DW, Conceição AA, Cornelissen TG, Echternacht L, Fernandes GW, Garcia QS, Guerra TJ, Jacobi CM, Lemos-Filho JP, Le Stradic S, Morellato LPC, Neves FS, Oliveira RS, Schaefer CE, Viana PL, Lambers H (2016). Ecology and evolution of plant diversity in the endangered campo rupestre: a neglected conservation priority. *Plant and Soil*, 403(1-2): 129–152. https://doi.org/10.1007/s11104-015-2637-8

Silvestro D, Bacon CD, Ding W, Zhang Q, Donoghue PCJ, Antonelli A, Xing Y (2021). Fossil data support a pre-Cretaceous origin of flowering plants. *Nature Ecology & Evolution*, 5(4): 449–457. https://doi.org/10.1038/s41559-020-01387-8

Simon MF, Grether R, de Queiroz LP, Skema C, Pennington RT, Hughes CE (2009). Recent assembly of the Cerrado, a Neotropical plant diversity hotspot, by in situ evolution of adaptations to fire. *Proceedings of the National Academy of Sciences*, 106(48): 20359–20364. https://doi.org/10.1073/pnas.0903410106

Strömberg CAE (2011). Evolution of grasses and grassland ecosystems. *Annual Review of Earth and Planetary Sciences*, 39: 517–544. https://doi.org/10.1146/annurev-earth-040809-152402

Tang H, Krishnakumar V, Li J (2015). jcvi: Python utility libraries for genome assembly and comparative genomics. https://doi.org/10.5281/zenodo.31631

Teodoro GS, de Britto Costa P, Brum M, Signori-Müller C, Alcantara S, Dawson TE, West AG, Lambers H, Oliveira RS (2021). Desiccation tolerance implies costs to productivity but allows survival under extreme drought conditions in Velloziaceae species in campos rupestres. *Environmental and Experimental Botany*, 189: 104556. https://doi.org/10.1016/j.envexpbot.2021.104556

Wang Y, Tang H, DeBarry JD, et al. (2012). MCScanX: a toolkit for detection and evolutionary analysis of gene synteny and collinearity. *Nucleic Acids Research*, 40: e49. https://doi.org/10.1093/nar/gkr1293

Yang Z (2007). PAML 4: phylogenetic analysis by maximum likelihood. *Molecular Biology and Evolution*, 24(8): 1586–1591. https://doi.org/10.1093/molbev/msm088

Yang Z, Nielsen R (2000). Estimating synonymous and nonsynonymous substitution rates under realistic evolutionary models. *Molecular Biology and Evolution*, 17(1): 32–43. https://doi.org/10.1093/oxfordjournals.molbev.a026236

Yuan F, Yang H, Xue Y, Kong D, Ye R, Li C, Zhang J, Theprungsirikul L, Shrift T, Krichilsky B, Johnson DM, Swift GB, He Y, Siedow JN, Pei ZM (2014). OSCA1 mediates osmotic-stress-evoked Ca2+ increases vital for osmosensing in Arabidopsis. *Nature*, 514(7522): 367–371. https://doi.org/10.1038/nature13593

Zhang C, Rabiee M, Sayyari E, Mirarab S (2018a). ASTRAL-III: polynomial time species tree reconstruction from partially resolved gene trees. *BMC Bioinformatics*, 19(S6): 153. https://doi.org/10.1186/s12859-018-2129-y

Zhang M, Wang D, Kang Y, Wu JX, Yao F, Pan C, Yan Z, Song C, Chen L (2018b). Structure of the mechanosensitive OSCA channels. *Nature Structural & Molecular Biology*, 25(9): 850–858. https://doi.org/10.1038/s41594-018-0117-6
