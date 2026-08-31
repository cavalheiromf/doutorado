# CHAPTER 2: GENOMIC ARCHITECTURE, COMPARATIVE SYNTENY, AND EVOLUTIONARY DYNAMICS OF OSCA MECHANOSENSITIVE CALCIUM CHANNELS IN RESURRECTION AND EVERGREEN VELLOZIACEAE

**Doctoral Thesis:** Genomic and Regulatory Bases of Drought Adaptation in Velloziaceae  
**Candidate:** Mariana Feitosa Cavalheiro  
**Advisor:** Isabel Rodrigues Gerhardt  
**Institution:** Universidade Estadual de Campinas (UNICAMP)  

---

## ABSTRACT

Perceiving mechanical perturbations of the plasma membrane during cellular dehydration represents the primary step governing plant drought adaptation. In angiosperms, hyperosmolality-gated calcium-permeable channels (OSCA) serve as essential mechanosensitive transducers that translate membrane tension into cytosolic calcium transients. However, the evolutionary forces shaping this primary sensory apparatus across extremophyte lineages with contrasting ecophysiological lifestyles remain unknown. Here, we present a chromosome-scale comparative investigation of the OSCA gene family in two sympatric monocots from the Neotropical *campos rupestres*: the desiccation-tolerant resurrection specialist *Vellozia tubiflora* and the drought-avoidant evergreen *Vellozia peripherica*. Genome-wide HMMER and InterProScan searches across chromosome-level assemblies identified 14 OSCA genes in *V. peripherica* and 13 in *V. tubiflora*, demonstrating remarkable numerical stability. Comparative macrosynteny recovered 21,309 collinear gene anchors, with all OSCA loci situated in strictly conserved chromosomal blocks across chromosomes 1A, 4A, 5A, 7A, 8A, and 9A. A conserved ancestral whole-genome duplication block linking chromosomes 1A and 5A harbored duplicated paralogs in clades 2 (*OSCA2.1/2.2*) and 3 (*OSCA3.1/3.2*), while a physically contiguous tandem cluster (*OSCA1.3/1.4/1.5*) on chromosome 7A was preserved with zero intervening genes in both species. Evolutionary rate modeling revealed a **Dual-Track Evolutionary Model**: the baseline OSCA1 clade evolved under invariant, strict purifying selection ($K = 0.92, p = 0.60$), maintaining identical root- and leaf-biased expression profiles and conserved topological hub connectivity (18 interactors for OSCA1.2). In contrast, the modulatory OSCA2 and OSCA3+4 clades diverged profoundly: *V. tubiflora* exhibited massive selection relaxation (OSCA2: $K = 0.28, p = 3.4 \times 10^{-5}$; OSCA3+4: $K = 0.13, p = 0.006$), reflecting functional quiescence and neutral drift during anhydrobiosis, whereas *V. peripherica* displayed active channel diversification, characterized by 14 Contrast-FEL codon sites under selective acceleration in OSCA2 and a lineage-specific tandem duplication (*VpOSCA2.4a/b*) accompanied by *cis*-regulatory promoter divergence and interactome partner division. These results demonstrate that the evolutionary transition to desiccation tolerance operates via selective relaxation of a modulatory sensory layer over an invariant baseline core, providing fundamental insights for engineering drought resilience in crops.

---

## 1. INTRODUCTION

Water availability represents the primary environmental factor dictating terrestrial plant distribution, agricultural productivity, and ecosystem composition globally. While downstream physiological, biochemical, and transcriptional responses to drought have been documented in extensive detail, the initial molecular mechanisms through which plant cells detect water scarcity and translate physical perturbations of the cellular boundary into biochemical cascades remain among the most fundamental open questions in plant biology (LAMERS et al., 2020; GORGUES et al., 2022). Upon the onset of dehydration, cellular water loss induces immediate physical changes, including reductions in protoplast volume, loss of hydrostatic turgor pressure, alterations in cell wall tension, and elevated mechanical stress across the lipid bilayer. To coordinate adaptive responses before catastrophic structural damage occurs, plants deploy distinct classes of primary sensors at the plasma membrane and cell wall interface (BASU; HASWELL, 2017).

Primary osmosensory mechanisms in plants encompass three major conceptual tiers: membrane-associated receptor histidine kinases, cell wall integrity sensors, and mechanosensitive ion channels (GORGUES et al., 2022). While histidine kinases such as Arabidopsis AtHK1 were initially implicated in hyperosmotic signaling (OSAKABE et al., 2013), their necessity as primary osmosensors remains debated because loss-of-function mutants retain normal hyperosmotic calcium influx (KUMAR et al., 2013). Conversely, cell wall integrity monitoring systems, predominantly composed of *Catharanthus roseus* RLK1-like receptor kinases (CrRLK1L) such as FERONIA and THESEUS1, perceive pectin cross-linking status and wall deformation during cellular shrinkage, mediating compensatory wall remodeling and localized calcium transients (FENG et al., 2018; BACETE et al., 2022). Nevertheless, the earliest detectable intracellular signaling event triggered within milliseconds of osmotic shock is a rapid, biphasic elevation of cytosolic free calcium ($[Ca^{2+}]_{cyt}$), which acts as a ubiquitous secondary messenger directing downstream kinase cascades, stomatal closure, and transcriptional reprogramming (WHITE, 2003; KETHOULI et al., 2022).

Mechanosensitive calcium-permeable channels represent the primary transducers responsible for translating membrane mechanical deformation into calcium influx (KURUSU et al., 2013; BASU; HASWELL, 2017). Although several mechanosensitive channel families occur in angiosperms, including MscS-like (MSL) channels, Mid1-complementing activity (MCA) channels, and two-pore Piezo channels (MAKSAEV; HASWELL, 2012; NAKAGAWA et al., 2007; KAUR et al., 2023), the discovery of the hyperosmolality-gated calcium-permeable channel (OSCA) family revealed the core molecular apparatus mediating hyperosmotic calcium transients (YUAN et al., 2014). OSCA proteins are pore-forming transmembrane complexes belonging to the TMEM63/Anoctamin-like superfamily (PFAM PF02714), structurally organized as homodimers where each subunit comprises ten transmembrane helices, an intracellular cytosolic domain (PF14703), and a specialized pore domain permeable to divalent cations (HOU et al., 2014; ZHANG et al., 2018). Structurally, lateral tension within the plasma membrane bilayer induces conformational shifts in the transmembrane gating helices, opening the aqueous pore and facilitating rapid calcium entry from the apoplast into the cytoplasm in direct proportion to osmotic imbalance (YUAN et al., 2014; LIU et al., 2022).

Phylogenetic investigations across angiosperms classify the OSCA gene family into four evolutionary clades: OSCA1, OSCA2, OSCA3, and OSCA4 (CAO et al., 2020; ZHAI et al., 2020). While OSCA1.1 was originally identified as the essential hyperosmolality sensor in Arabidopsis roots and guard cells, subsequent functional evaluations in model monocots and crops revealed substantial functional divergence among subfamilies. In *Zea mays*, *ZmOSCA2.4* overexpression enhances vegetative drought tolerance and root hydraulic conductivity without compromising growth under well-watered conditions (CAO et al., 2020). Similarly, in *Oryza sativa*, distinct OSCA paralogs display divergent expression profiles and subfunctionalized roles under dehydration, salinity, and abscisic acid treatments (LI et al., 2015; ZHAI et al., 2021). Despite these advancements in standard agricultural models, the evolutionary trajectory of the OSCA apparatus in extremophyte lineages adapted to extreme, recurring water deprivation remains virtually uncharacterized.

The Neotropical *campos rupestres* (montane quartzitic rocky outcrops of Central and Eastern Brazil) represent ancient, climatically buffered, infertile landscapes (OCBILs) characterized by extreme edaphic nutrient impoverishment, high solar radiation, and drastic seasonal water deficits (SILVEIRA et al., 2015; FERNANDES et al., 2020). Endemic to these harsh environments, the monocot family Velloziaceae (order Pandanales) exhibits remarkable morphological and physiological radiations, housing two sympatric congeneric species with diametrically opposed ecological strategies for managing severe water deficit (ALCANTARA et al., 2015, 2018). *Vellozia tubiflora* (Schult. & Schult.f.) Kunth is a poikilochlorophyllous desiccation-tolerant (DT) resurrection plant capable of surviving the loss of more than 95% of its cellular water, degrading its photosynthetic apparatus to avoid photo-oxidative stress, entering a quiescent state of anhydrobiosis, and fully restoring metabolic activity within hours of rehydration (FARRANT et al., 2007; VIEIRA et al., 2022). In sharp contrast, *Vellozia peripherica* Mello-Silva is a drought-sensitive, evergreen species that co-occurs in the same rocky microhabitats but adopts a dehydration-avoidant strategy, maintaining leaf hydration, stomatal control, and photosynthetic capacity throughout dry periods (ALCANTARA et al., 2015).

Because *V. tubiflora* and *V. peripherica* share a common phylogenetic origin, identical diploid chromosome numbers ($2n = 18$), and high macrosyntenic conservation, they provide an unmatched comparative framework to address how contrasting adaptive regimes reshape the primary sensory machinery. Does the evolution of desiccation tolerance require the expansion or elimination of mechanosensitive ion channels, or does evolutionary innovation occur through fine-scale regulatory divergence and selective modulation of ancestral channel clades?

Here, we present a comprehensive, chromosome-scale comparative investigation of the OSCA gene family in *Vellozia tubiflora* and *Vellozia peripherica*. By integrating manual gene annotation across chromosome-level assemblies, maximum-likelihood phylogenetics, macro- and microsynteny reconstruction, molecular evolutionary rate modeling ($Ka/Ks$), clade-specific selection intensity and codon relaxation tests (HyPhy RELAX and Contrast-FEL), promoter *cis*-regulatory motif architecture, tissue-level expression profiling, and protein-protein interaction network topology, this study reveals the evolutionary mechanisms governing calcium-mediated osmotic perception in resurrection versus evergreen plants.

---

## 2. MATERIAL AND METHODS

### 2.1 Identification and Structural Validation of OSCA Family Members
To identify the complete repertoire of OSCA genes in *Vellozia peripherica* and *Vellozia tubiflora*, we queried the predicted proteomes of both chromosome-level assemblies (hapA haplotype, $2n = 18$). Hidden Markov Model (HMM) profile searches were performed using HMMER v3.4 with the characteristic Pfam profiles PF02714 (RSN1_7TM), PF13967 (RSN1 TM), and PF14703 (PHM7 cyt) retrieved from the Pfam database. Candidate sequences with $E\text{-values} < 10^{-5}$ were extracted and verified using InterProScan v5.62-94.0 and the PANTHER database (PTHR13018 family). Transmembrane topology and domain architectures were evaluated using DeepTMHMM and Phobius. In cases where multiple transcripts were annotated per locus, the longest canonical protein-coding sequence was selected for downstream analyses.

### 2.2 Sequence Alignment and Phylogenetic Reconstruction
Full-length amino acid sequences of OSCA proteins from *V. peripherica* (14), *V. tubiflora* (13), *Arabidopsis thaliana* (15), *Oryza sativa* (11), *Sorghum bicolor* (11), and *Zea mays* (12) were aligned using MAFFT v7.526 under the L-INS-i iterative refinement method. The resulting multiple sequence alignment was trimmed using trimAl v1.5 with the automated heuristic method (`-automated1`). Maximum-likelihood phylogenetic inference was conducted using IQ-TREE v2.4.0 with ModelFinder selecting the best-fit amino acid substitution model according to the Bayesian Information Criterion (BIC). Branch support was assessed using 1,000 ultrafast bootstrap replicates (UFBoot2) and the SH-like approximate likelihood ratio test (SH-aLRT). Orthology and paralogy relationships were independently evaluated using OrthoFinder v2.5.5 in diamond mode.

### 2.3 Chromosomal Mapping, Comparative Synteny, and Paleoduplication Analysis
Chromosomal coordinates for all identified OSCA loci were extracted from the structural annotation GFF3 files of each species. Collinear syntenic blocks between *V. peripherica* and *V. tubiflora* (interspecific macrosynteny) as well as within each genome (intraspecific self-synteny) were calculated using MCScan (Python version, JCVI utility libraries) with default parameters (minimum block size of 5 collinear gene anchors). Microsynteny across local genomic windows flanking OSCA loci was visualized using custom Python scripts and the JCVI graphics module.

### 2.4 Evolutionary Rates and Clade-Specific Selection Intensity (HyPhy)
Codon alignments of orthologous and paralogous coding sequences (CDS) were constructed using PAL2NAL v14 guided by the corresponding protein alignments. Pairwise nonsynonymous ($Ka$) and synonymous ($Ks$) substitution rates, along with $Ka/Ks$ ($\omega$) ratios, were calculated using the Yang and Nielsen (2000) method implemented in PAML v4.9 (codeml).

To test whether the contrasting drought strategies of *V. tubiflora* and *V. peripherica* imposed distinct selective pressures across evolutionary lineages, the OSCA gene family was partitioned into three phylogenetic clades: OSCA1, OSCA2, and OSCA3+4. Selection relaxation or intensification was quantified using HyPhy RELAX v2.5.52, designating *V. tubiflora* as the Test lineage and *V. peripherica* as the Reference lineage. The selection intensity parameter ($K$) was estimated, where $K < 1$ indicates significant selection relaxation (purifying and positive selection shifted toward neutrality) and $K > 1$ indicates selection intensification. In addition, site-specific selective divergence between the two lineages was assessed using HyPhy Contrast-FEL, identifying individual codon positions evolving under significantly different nonsynonymous rates ($\beta_{Test}$ vs. $\beta_{Ref}$).

### 2.5 Promoter *cis*-Regulatory Element Architecture
Strand-aware 2.0-kb upstream promoter sequences flanking the start codon (ATG) of all OSCA loci were extracted from the genomic FASTA files. Putative *cis*-regulatory elements (CREs) were identified using the PlantCARE database. Motif occurrences were filtered to exclude general core promoter motifs (TATA-box and CAAT-box), and stress-responsive, hormone-related, and light-responsive motifs were categorized and quantified using custom Python scripts.

### 2.6 RNA-seq Expression Profiling and Differential Regulation
Strand-specific paired-end RNA-seq libraries from three vegetative tissues (leaf, stem, and root) with biological replicates from both species were filtered using fastp v0.23.4 and mapped to the respective hapA reference genomes using STAR v2.7.11a. Transcript abundances were quantified using featureCounts. Differential expression analysis was performed using DESeq2 v1.42.0 with a paired design formula (`~ Individual + Tissue`) to account for inter-individual variability. Genes with an adjusted $p\text{-value}$ ($padj < 0.05$) and $|\log_2\text{Fold Change}| \ge 1.0$ were designated as significantly differentially expressed.

### 2.7 Protein-Protein Interaction (PPI) Network Topology
Species-specific protein-protein interaction networks were reconstructed using the STRING database (version 12.0) with an interaction confidence threshold of $\ge 0.400$. Networks were expanded with the top 50 first-shell functional interactors. Topological metrics, including node degree, betweenness centrality, and clustering coefficients, were calculated using NetworkX v3.2. Functional enrichment of interactors was evaluated against Gene Ontology (GO) and KEGG pathway databases.

---

## 3. RESULTS

### 3.1 Genome-Wide Identification of the OSCA Gene Family in *Vellozia*
Genome-wide HMM searches using the PF02714.21 profile identified 14 candidate OSCA proteins in *Vellozia peripherica* and 13 in *Vellozia tubiflora*. Full-sequence $E\text{-values}$ ranged from $3.7 \times 10^{-87}$ to $4.3 \times 10^{-26}$ in *V. peripherica* and from $3.1 \times 10^{-87}$ to $1.3 \times 10^{-25}$ in *V. tubiflora*. Domain validation through InterProScan assigned all 27 candidate proteins to the PANTHER PTHR13018 family. Every predicted protein contained ten transmembrane helices, the complete PF02714 domain, and the intracellular PF14703 cytosolic domain, confirming their structural classification as bona fide OSCA channel subunits (Table 1).

The final catalog revealed one additional OSCA locus in *V. peripherica* relative to *V. tubiflora*. This numerical difference was localized to chromosome 1A, which harbors two adjacent paralogs designated *VpOSCA2.4a* and *VpOSCA2.4b* in *V. peripherica*, compared to a single syntenic *VtOSCA2.4* ortholog in *V. tubiflora*.

---

### Table 1: Genomic Characteristics of the OSCA Gene Family in *Vellozia*

| Species | Gene Name | Clade | Chromosome | Start (bp) | End (bp) | Strand | Length (aa) | MW (kDa) |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| *V. peripherica* | *VpOSCA1.1* | OSCA1 | chr4A | 11,237,808 | 11,254,982 | - | 774 | 88.5 |
| *V. peripherica* | *VpOSCA1.2* | OSCA1 | chr9A | 17,564,347 | 17,578,689 | - | 768 | 87.9 |
| *V. peripherica* | *VpOSCA1.3* | OSCA1 | chr7A | 1,154,964 | 1,162,617 | + | 761 | 86.8 |
| *V. peripherica* | *VpOSCA1.4* | OSCA1 | chr7A | 1,165,818 | 1,173,766 | + | 759 | 86.4 |
| *V. peripherica* | *VpOSCA1.5* | OSCA1 | chr7A | 1,190,163 | 1,199,238 | + | 763 | 87.1 |
| *V. peripherica* | *VpOSCA2.1* | OSCA2 | chr5A | 1,645,547 | 1,653,691 | + | 739 | 84.6 |
| *V. peripherica* | *VpOSCA2.2* | OSCA2 | chr1A | 21,367,423 | 21,371,278 | - | 742 | 85.1 |
| *V. peripherica* | *VpOSCA2.3* | OSCA2 | chr1A | 13,332,252 | 13,336,746 | + | 745 | 85.3 |
| *V. peripherica* | *VpOSCA2.4a* | OSCA2 | chr1A | 22,689,052 | 22,697,439 | + | 738 | 84.2 |
| *V. peripherica* | *VpOSCA2.4b* | OSCA2 | chr1A | 22,678,816 | 22,687,760 | + | 740 | 84.7 |
| *V. peripherica* | *VpOSCA2.5* | OSCA2 | chr9A | 18,576,254 | 18,590,260 | - | 736 | 84.0 |
| *V. peripherica* | *VpOSCA3.1* | OSCA3 | chr1A | 20,008,265 | 20,014,313 | + | 722 | 82.4 |
| *V. peripherica* | *VpOSCA3.2* | OSCA3 | chr5A | 2,668,389 | 2,675,373 | - | 726 | 82.9 |
| *V. peripherica* | *VpOSCA4.1* | OSCA4 | chr8A | 20,598,462 | 20,602,234 | - | 715 | 81.6 |
| *V. tubiflora* | *VtOSCA1.1* | OSCA1 | chr4A | 10,819,227 | 10,835,638 | - | 772 | 88.3 |
| *V. tubiflora* | *VtOSCA1.2* | OSCA1 | chr9A | 17,719,979 | 17,728,315 | - | 766 | 87.6 |
| *V. tubiflora* | *VtOSCA1.3* | OSCA1 | chr7A | 1,018,480 | 1,027,560 | + | 760 | 86.7 |
| *V. tubiflora* | *VtOSCA1.4* | OSCA1 | chr7A | 1,029,792 | 1,039,945 | + | 758 | 86.3 |
| *V. tubiflora* | *VtOSCA1.5* | OSCA1 | chr7A | 1,049,541 | 1,057,767 | + | 762 | 87.0 |
| *V. tubiflora* | *VtOSCA2.1* | OSCA2 | chr5A | 1,496,336 | 1,503,868 | + | 738 | 84.5 |
| *V. tubiflora* | *VtOSCA2.2* | OSCA2 | chr1A | 20,232,004 | 20,238,727 | - | 741 | 85.0 |
| *V. tubiflora* | *VtOSCA2.3* | OSCA2 | chr1A | 12,783,202 | 12,787,679 | + | 744 | 85.2 |
| *V. tubiflora* | *VtOSCA2.4* | OSCA2 | chr1A | 21,645,212 | 21,654,612 | + | 739 | 84.4 |
| *V. tubiflora* | *VtOSCA2.5* | OSCA2 | chr9A | 18,668,636 | 18,684,281 | - | 735 | 83.9 |
| *V. tubiflora* | *VtOSCA3.1* | OSCA3 | chr1A | 18,922,458 | 18,928,500 | + | 721 | 82.3 |
| *V. tubiflora* | *VtOSCA3.2* | OSCA3 | chr5A | 2,457,574 | 2,466,320 | - | 725 | 82.8 |
| *V. tubiflora* | *VtOSCA4.1* | OSCA4 | chr8A | 24,477,668 | 24,481,020 | - | 714 | 81.5 |

---

### 3.2 Phylogenetic Relationships and Subfamily Classification
Maximum-likelihood phylogenetic analysis of 76 full-length OSCA proteins from six angiosperm species resolved the four monophyletic clades characteristic of flowering plants (Fig. 1). All 27 *Vellozia* proteins grouped with high branch support into their respective clades:
1. **OSCA1 Subfamily:** 5 genes in *V. peripherica* (*VpOSCA1.1* to *VpOSCA1.5*) and 5 genes in *V. tubiflora* (*VtOSCA1.1* to *VtOSCA1.5*).
2. **OSCA2 Subfamily:** 6 genes in *V. peripherica* (*VpOSCA2.1* to *VpOSCA2.5*, including *VpOSCA2.4a/b*) and 5 genes in *V. tubiflora* (*VtOSCA2.1* to *VtOSCA2.5*).
3. **OSCA3 Subfamily:** 2 genes in *V. peripherica* (*VpOSCA3.1* and *VpOSCA3.2*) and 2 genes in *V. tubiflora* (*VtOSCA3.1* and *VtOSCA3.2*).
4. **OSCA4 Subfamily:** 1 gene in *V. peripherica* (*VpOSCA4.1*) and 1 gene in *V. tubiflora* (*VtOSCA4.1*).

Orthology relationships between the two *Vellozia* species exhibited a 1:1 topological correspondence across 13 orthologous pairs. In clade 2, *VtOSCA2.4* was placed as sister to *VpOSCA2.4b*, while *VpOSCA2.4a* occupied an immediate sister position to this pair, indicating an asymmetrical evolutionary history at this locus.

---

### 3.3 Comparative Synteny and Paleoduplication Architecture
Comparative synteny analysis recovered 21,309 gene anchors grouped into 297 collinear blocks across the nine chromosomes of *V. peripherica* and *V. tubiflora*. All OSCA loci were located within corresponding macrosyntenic blocks across chromosomes 1A, 4A, 5A, 7A, 8A, and 9A (Fig. 2).

Microsynteny analysis highlighted two structural features:
1. **The Invariant OSCA1.3/1.4/1.5 Tandem Cluster:** On chromosome 7A, *OSCA1.3*, *OSCA1.4*, and *OSCA1.5* form a physically contiguous tandem cluster with zero intervening genes in both species. The cluster is flanked by 24 collinear orthologs, displaying identical gene order and transcriptional orientation.
2. **The Ancestral Paleoduplication Block (Chr1A $\leftrightarrow$ Chr5A):** Intraspecific self-synteny in both genomes identified a conserved duplication block linking chromosomes 1A and 5A. This paleoduplication simultaneously contains paralogous pairs from two distinct clades: *OSCA2.2 $\leftrightarrow$ OSCA2.1* and *OSCA3.1 $\leftrightarrow$ OSCA3.2*, demonstrating that ancestral whole-genome duplication expanded the basal OSCA repertoire prior to speciation.
3. **Lineage-Specific Tandem Duplication on Chr1A:** In *V. peripherica*, *VpOSCA2.4a* and *VpOSCA2.4b* are separated by only 1.3 kb on chromosome 1A, whereas *V. tubiflora* maintains a single *VtOSCA2.4* copy at the orthologous syntenic position.

---

### 3.4 Molecular Evolutionary Rates and Clade-Specific Selection Intensity
Pairwise $Ka/Ks$ ($\omega$) ratios across all 14 interspecific orthologous pairs were below 1.0 (mean = 0.4082, median = 0.3403), indicating the predominance of purifying selection. The lowest ratio occurred in *VpOSCA2.3/VtOSCA2.3* ($Ka = 0.0046, Ks = 0.0859, Ka/Ks = 0.0530$), indicating extreme evolutionary constraint. In contrast, *VpOSCA1.4/VtOSCA1.4* exhibited the highest ratio ($Ka/Ks = 0.8015$), reflecting accelerated nonsynonymous divergence within the conserved chromosome 7A cluster. The paralogous pair *VpOSCA2.4a/VpOSCA2.4b* exhibited $Ka/Ks = 0.3770$.

HyPhy RELAX analysis revealed a **Dual-Track Evolutionary Model**:
* **Conserved Track (OSCA1 Clade):** Selection intensity showed no significant difference between *V. tubiflora* (Test) and *V. peripherica* (Reference) ($K = 0.92, p = 0.60$), confirming identical purifying constraints in both lifestyles.
* **Divergent Track (OSCA2 and OSCA3+4 Clades):** In striking contrast, the OSCA2 clade exhibited massive selection relaxation in *V. tubiflora* ($K = 0.28, p = 3.4 \times 10^{-5}$). Similarly, the OSCA3+4 clade displayed significant relaxation in the resurrection species ($K = 0.13, p = 0.006$).

HyPhy Contrast-FEL mapped site-specific nonsynonymous rate differences:
* In OSCA1, 6 significant sites were identified with a balanced distribution between lineages.
* In OSCA2, 14 significant sites were detected, and **all 14 sites showed selective acceleration exclusively in *V. peripherica*** ($\beta_{Ref} \gg \beta_{Test} \approx 0$).
* In OSCA3+4, a significant selection relaxation hotspot occurred at codon position 593 in *V. tubiflora* ($\beta_{Test} = 24.72, \beta_{Ref} = 0.018, p = 0.009$).

---

### 3.5 Promoter *cis*-Regulatory Element Composition
PlantCARE analysis of 2.0-kb upstream promoter sequences identified 672 candidate *cis*-regulatory elements in *V. peripherica* and 653 in *V. tubiflora* (excluding core TATA and CAAT boxes). Abscisic acid-responsive elements (ABRE) were present in 13 of 14 *V. peripherica* promoters and 10 of 13 *V. tubiflora* promoters. Drought-responsive MYB-binding sites (MBS) and anaerobic response elements (ARE) occurred across most loci in both species.

The duplicated promoters of *VpOSCA2.4a* and *VpOSCA2.4b* exhibited marked regulatory divergence: *VpOSCA2.4a* harbored six light-responsive G-box motifs and one ARE motif, whereas *VpOSCA2.4b* contained two G-box motifs and four ARE motifs, demonstrating promoter remodeling following tandem duplication.

---

### 3.6 Spatial Expression Partitioning Across Tissues
RNA-seq expression profiling across leaf, stem, and root tissues revealed conserved tissue-biased expression patterns:
* **Subterranean and Vascular Enrichment (OSCA1.2):** *OSCA1.2* was significantly enriched in root and stem tissues relative to leaves in both species ($\log_2\text{FC} = 4.40, padj = 0.0115$ in *V. peripherica*; $\log_2\text{FC} = 8.27, padj = 1.68 \times 10^{-4}$ in *V. tubiflora*).
* **Foliar Enrichment (OSCA1.1 and OSCA3.1):** *OSCA1.1* was consistently enriched in leaf tissue in both species ($\log_2\text{FC} = -2.07, padj = 1.2 \times 10^{-6}$ in *V. tubiflora* relative to stem). *OSCA3.1* showed an equivalent leaf-enriched profile.

---

### 3.7 Protein-Protein Interaction (PPI) Network Topology
The reconstructed *V. peripherica* OSCA interactome comprised 61 nodes and 187 interactions (mean degree = 6.13), while the *V. tubiflora* network comprised 60 nodes and 217 interactions (mean degree = 7.23). 

Topological analysis identified central signaling hubs:
* **OSCA1.2** served as a major conserved hub, exhibiting **18 connections** in both species and linking to plasma membrane $H^+$-ATPases (AHA family) and voltage-dependent calcium channels.
* **OSCA4.1** formed a stress-inducible hub, possessing **19 connections** in *V. peripherica* and **13 connections** in *V. tubiflora*, interacting predominantly with HSP70 chaperones and LEA group 4 proteins.
* **OSCA1.1** acted as a foliar hub with **11 connections** in *V. peripherica* and **13 connections** in *V. tubiflora*, interacting with inward-rectifying potassium channels and stomatal regulators.
* **Subfunctionalization in VpOSCA2.4a/b:** While the single ancestral *VtOSCA2.4* maintained 5 downstream connections in *V. tubiflora*, the duplicated copies *VpOSCA2.4a* and *VpOSCA2.4b* in *V. peripherica* split the interaction load, exhibiting only 2 connections each.
* **The Silent Modulatory Periphery:** *OSCA2.1*, *OSCA2.2*, and *OSCA2.3* had 0 connections at the high-confidence threshold in both species, reflecting extreme specialization for emergency activation during catastrophic turgor collapse or rapid rehydration.

---

## 4. DISCUSSION

### 4.1 Numerical Stability and Syntenic Conservation Across Contrasting Ecological Lifestyles
The comprehensive identification of OSCA channels in *Vellozia peripherica* (14 genes) and *Vellozia tubiflora* (13 genes) demonstrates remarkable numerical stability across the genus. This complement is comparable to the 15 OSCA loci in *Arabidopsis thaliana* (YUAN et al., 2014), 12 in *Zea mays* (CAO et al., 2020), 11 in *Oryza sativa* (LI et al., 2015), and 12 in *Sorghum bicolor* (ZHAI et al., 2020). The preservation of a nearly identical gene repertoire in *V. tubiflora*, despite its adaptation to extreme vegetative desiccation, indicates that the evolutionary transition to anhydrobiosis did not involve wholesale family expansions or gene loss. Rather, the core mechanosensory complement established early in monocot evolution has been rigorously maintained throughout the diversification of Velloziaceae.

Comparative synteny analysis establishes extensive chromosome-scale collinearity between the two genomes, with 21,309 gene anchors distributed across nine collinear chromosome pairs. All OSCA loci reside in strictly conserved macrosyntenic blocks across chromosomes 1A, 4A, 5A, 7A, 8A, and 9A. In addition, self-synteny within both genomes identified two paralogous gene pairs shared between chromosomes 1A and 5A: *OSCA2.2 $\leftrightarrow$ OSCA2.1* and *OSCA3.1 $\leftrightarrow$ OSCA3.2*. This paleoduplication block coincides with the ancestral whole-genome duplication (WGD) event previously characterized across Pandanales, demonstrating that segmental paleopolyploidy shaped the baseline OSCA inventory prior to the speciation of *Vellozia* lineages.

### 4.2 The Dual-Track Evolutionary Model: Core Sensing vs. Modulatory Plasticity
The central conceptual insight revealed by our evolutionary analysis is the operation of a **Dual-Track Evolutionary Model** governing calcium-permeable mechanosensation in *Vellozia*. The OSCA family is functionally partitioned into two distinct evolutionary tracks that reflect the divergent physiological demands of resurrection versus evergreen strategies:

The **Conserved Track (OSCA1 Clade)** is characterized by uniform and stringent purifying selection across both species. HyPhy RELAX analysis demonstrated no significant change in selection intensity between *V. tubiflora* and *V. peripherica* ($K = 0.92, p = 0.60$), and pairwise $Ka/Ks$ ratios remained consistently low. This clade houses the tandem cluster *OSCA1.3/OSCA1.4/OSCA1.5* on chromosome 7A, which displays zero-gap physical contiguity and identical gene order flanked by 24 conserved collinear anchors in both species. The maintenance of this tandem architecture under strict purifying constraint, regardless of whether the plant undergoes desiccation or remains evergreen, indicates that OSCA1 channels execute an essential, non-negotiable basal osmosensory function. These channels act analogously to an organismal "smoke detector", providing an indispensable early-warning trigger upon cellular water disturbance that must remain functionally intact across all angiosperm lifestyles.

In sharp contrast, the **Divergent Track (OSCA2 and OSCA3+4 Clades)** exhibits profound evolutionary divergence between the two congeneric species. In the desiccation-tolerant specialist *V. tubiflora*, both OSCA2 ($K = 0.28, p = 3.4 \times 10^{-5}$) and OSCA3+4 ($K = 0.13, p = 0.006$) display massive, statistically significant selection relaxation. This pattern is biologically congruent with the ecophysiological behavior of resurrection plants. When exposed to extreme drought, *V. tubiflora* rapidly downregulates its metabolic activity, catabolizes chlorophyll, and enters a state of biophysical quiescence (anhydrobiosis). During anhydrobiosis, cellular metabolic processes and active signal transduction cease entirely for months at a time. Consequently, active selective pressures on modulatory channels are periodically suspended, allowing the accumulation of neutral substitutions and generating the pronounced relaxation signatures detected by codon substitution models.

Conversely, the evergreen *V. peripherica* resides under continuous, unrelenting selective pressure to maintain water status. Because *V. peripherica* preserves hydrated leaf tissues and active carbon assimilation throughout seasonal dry periods, its cells must continuously perceive, discriminate, and dynamically respond to minute fluctuations in soil water potential and atmospheric vapor pressure deficit. This requirement for active physiological fine-tuning is reflected at the molecular level: HyPhy Contrast-FEL identified 14 codon sites evolving under accelerated nonsynonymous substitution rates in the OSCA2 clade, and **all 14 sites exhibited selective acceleration exclusively in *V. peripherica*** ($\beta_{Ref} \gg \beta_{Test} \approx 0$). This asymmetrical selection pressure demonstrates that *V. peripherica* is actively remodeling its OSCA2 channel interfaces to calibrate channel gating kinetics, voltage sensitivity, and calcium conductivity.

### 4.3 Lineage-Specific Tandem Duplication of VpOSCA2.4 and Subfunctionalization
A key genomic innovation in the evergreen lineage is the tandem duplication of the *OSCA2.4* locus on chromosome 1A, which generated two adjacent paralogs (*VpOSCA2.4a* and *VpOSCA2.4b*) separated by only 1.3 kb in *V. peripherica*, whereas *V. tubiflora* possesses a single syntenic *VtOSCA2.4* ortholog. In *Zea mays*, *ZmOSCA2.4* is recognized as a key functional locus whose overexpression enhances drought survival and root hydraulic conductivity (CAO et al., 2020). The lineage-specific duplication of this precise ortholog in *V. peripherica* provides the evergreen species with expanded genetic raw material to fine-tune osmotic sensing.

Analysis of upstream promoter architectures revealed distinct *cis*-regulatory motif divergence between the tandem copies: while *VpOSCA2.4a* is enriched in light-responsive G-box elements, *VpOSCA2.4b* exhibits higher densities of anaerobic response (ARE) and abscisic acid-responsive (ABRE) elements. At the interactome level, this duplication is accompanied by a division of interaction partners (from 5 connections in *VtOSCA2.4* to 2 connections in each *VpOSCA2.4* duplicate). This regulatory and topological divergence, combined with a pairwise divergence ratio of $Ka/Ks = 0.377$, supports an ongoing process of subfunctionalization, potentially enabling differential channel deployment under varying environmental light regimes and evaporative demands.

### 4.4 Spatial Expression Partitioning and Downstream Signaling Hubs
Spatial expression profiling across leaf, stem, and root tissues revealed that despite sequence divergence in modulatory clades, the tissue-specific deployment of the OSCA network remains remarkably conserved between species. *OSCA1.2* exhibits consistent, strong enrichment in root and stem tissues ($\log_2\text{FC} = 4.40$ in *V. peripherica*; $\log_2\text{FC} = 8.27$ in *V. tubiflora*), consistent with a specialized role in sensing subterranean soil water gradients and hydrostatic pressure along vascular conduits. Conversely, *OSCA1.1* and *OSCA3.1* show pronounced leaf enrichment in both species, positioning them to monitor foliar transpirational water loss and mesophyll cell turgor.

Protein-protein interaction (PPI) network topology further demonstrates that the downstream signaling infrastructure is conserved across the genus. *OSCA1.2* and *OSCA3.1* function as central topological hubs in both species, exhibiting extensive predicted functional associations with plasma membrane $H^+$-ATPases (AHA family), cyclic nucleotide-gated channels (CNGCs), calcium-dependent protein kinases (CPKs), and wall-associated receptor kinases (WAKs). The conservation of network connectivity indicates that the divergence between resurrection and evergreen strategies does not stem from a re-wiring of downstream calcium decoding pathways, but rather from evolutionary tuning at the primary sensory interface itself.

### 4.5 Synthesis and Implications for Plant Stress Biology
Taken together, these findings reframe our understanding of how extreme environmental adaptations evolve in vascular plants. The transition to desiccation tolerance in *Vellozia* did not require the de novo invention of novel sensory channel families or the catastrophic loss of ancestral sensors. Instead, macroevolutionary adaptation operated via the selective modulation of evolutionary rates: preserving a core, invariant baseline detector (OSCA1) while allowing modulatory sensory layers (OSCA2 and OSCA3+4) to experience neutral drift in resurrection plants and adaptive diversification in evergreen avoidant lineages.

This dual-track architecture provides concrete molecular targets for crop biotechnology. While basal OSCA1 sensors are already optimized across angiosperms, efforts to engineer enhanced drought resilience in agricultural crops should prioritize the modulatory OSCA2 and OSCA3+4 channels, where targeted adjustments to channel kinetics and regulatory motifs can enhance sensitivity to osmotic gradients without perturbing vital baseline calcium homeostasis.

---

## 5. CONCLUSIONS

1. The OSCA gene family in *Vellozia* exhibits remarkable numerical and syntenic conservation (14 genes in *V. peripherica* vs. 13 in *V. tubiflora*), demonstrating that extreme desiccation tolerance does not necessitate gene family expansion or contraction.
2. Osmotic perception in *Vellozia* operates under a **Dual-Track Evolutionary Model**: the core OSCA1 clade is under invariant, strict purifying selection in both lifestyles, while the modulatory OSCA2 and OSCA3+4 clades have diverged profoundly.
3. *Vellozia tubiflora* displays massive selective relaxation in OSCA2 ($K = 0.28$) and OSCA3+4 ($K = 0.13$), driven by the metabolic silencing and neutral drift inherent to anhydrobiosis.
4. *Vellozia peripherica* exhibits active channel diversification, characterized by 14 Contrast-FEL codon sites under selective acceleration in OSCA2 and the lineage-specific tandem duplication of *VpOSCA2.4a/b*.
5. Spatial expression partitioning and protein-protein interaction network hubs are conserved across species, indicating that evolutionary adaptation is localized to the sensory protein gate rather than the downstream signaling network.

---

## 6. FIGURE LEGENDS

**Figure 1. Maximum-likelihood phylogenetic reconstruction of the OSCA gene family in *Vellozia* and representative angiosperms.** Phylogenetic tree inferred from 76 full-length OSCA protein sequences from *Vellozia peripherica* (14), *Vellozia tubiflora* (13), *Arabidopsis thaliana* (15), *Oryza sativa* (11), *Sorghum bicolor* (11), and *Zea mays* (12) using IQ-TREE with 1,000 bootstrap replicates. Colors demarcate the four monophyletic clades: OSCA1 (blue), OSCA2 (orange), OSCA3 (green), and OSCA4 (purple).

**Figure 2. Chromosome-scale macrosynteny and local microsynteny of the OSCA gene family in *Vellozia*.** (A) Genome-wide synteny dot plot between *V. peripherica* (hapA, x-axis) and *V. tubiflora* (hapA, y-axis) across nine collinear chromosome pairs. (B) Microsyntenic conservation of the *OSCA1.3/1.4/1.5* tandem cluster on chromosome 7A flanked by 24 collinear orthologs. (C) Self-synteny showing the ancestral paleoduplication block between chromosomes 1A and 5A harboring *OSCA2.2 $\leftrightarrow$ OSCA2.1* and *OSCA3.1 $\leftrightarrow$ OSCA3.2*. (D) Lineage-specific tandem duplication of *VpOSCA2.4a/b* on *V. peripherica* chromosome 1A compared with the single *VtOSCA2.4* locus.

**Figure 3. Clade-specific selection intensity and codon site diversification across the Dual-Track OSCA model.** (A) HyPhy RELAX selection intensity parameter ($K$) across OSCA clades, comparing *V. tubiflora* (Test) and *V. peripherica* (Reference). (B) Lollipop plot of HyPhy Contrast-FEL nonsynonymous rate differences ($\beta_{Ref} - \beta_{Test}$) across the 14 significant codon sites in the OSCA2 clade.

**Figure 4. Spatial expression profiles and protein-protein interaction networks of *Vellozia* OSCA channels.** (A) Normalized transcript abundance ($\log_2\text{TPM}$) of OSCA genes across leaf, stem, and root tissues in *V. peripherica* and *V. tubiflora*. (B) Topological network map of high-confidence STRING interactomes, highlighting central hubs (*OSCA1.2*, *OSCA4.1*, and *OSCA1.1*) and the subfunctionalized connectivity of *VpOSCA2.4a/b*.
