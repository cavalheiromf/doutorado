# CHAPTER 2: GENOMIC ARCHITECTURE, COMPARATIVE SYNTENY, AND EVOLUTIONARY DYNAMICS OF OSCA MECHANOSENSITIVE CALCIUM CHANNELS IN RESURRECTION AND EVERGREEN VELLOZIACEAE

**Doctoral Thesis:** Genomic and Regulatory Bases of Drought Adaptation in Velloziaceae  
**Candidate:** Mariana Feitosa Cavalheiro  
**Advisor:** Isabel Rodrigues Gerhardt  
**Institution:** Universidade Estadual de Campinas (UNICAMP)  

---

## ABSTRACT

Perceiving mechanical perturbations of the plasma membrane during cellular dehydration represents the primary biophysical step governing plant adaptation to water deficit. In angiosperms, hyperosmolality-gated calcium-permeable channels (OSCA) serve as essential mechanosensitive transducers that translate bilayer lateral tension into cytosolic calcium transients. However, the evolutionary mechanisms shaping this primary sensory apparatus across extremophyte lineages with contrasting ecophysiological lifestyles remain poorly understood. Here, we present a chromosome-scale comparative investigation of the OSCA gene family in two sympatric monocots from the Neotropical *campos rupestres*: the poikilochlorophyllous desiccation-tolerant resurrection plant *Vellozia tubiflora* and the drought-avoidant evergreen *Vellozia peripherica*. Genome-wide HMMER and InterProScan queries across chromosome-level assemblies identified 14 OSCA genes in *V. peripherica* and 13 in *V. tubiflora*, demonstrating strict numerical conservation without wholesale family amplification. Comparative macrosynteny recovered 297 collinear gene blocks ($2n = 18$), with all OSCA loci situated in strictly conserved chromosomal blocks across chromosomes 1A, 4A, 5A, 7A, 8A, and 9A. A conserved ancestral whole-genome duplication block connecting chromosomes 1A and 5A harbored duplicated paralogs in clades 2 (*OSCA2.1/2.2*) and 3 (*OSCA3.1/3.2*), while a physically contiguous tandem triplication cluster (*OSCA1.3/1.4/1.5*) on chromosome 7A was preserved with zero intervening genes in both species. Evolutionary rate modeling revealed a **Dual-Track Evolutionary Model**: the baseline OSCA1 clade evolved under invariant, strict purifying selection ($K = 0.9215, p = 0.5957$), maintaining conserved root- and leaf-biased transcript accumulation profiles alongside an invariant topological hub connectivity (18 identical first-shell interactors for OSCA1.2 in both species). In contrast, the modulatory OSCA2 and OSCA3+4 clades diverged profoundly: *V. tubiflora* exhibited massive selection relaxation (OSCA2: $K = 0.2828, p = 3.4 \times 10^{-5}$; OSCA3+4: $K = 0.1349, p = 0.0061$), reflecting functional quiescence and neutral drift during metabolic shutdown in anhydrobiosis. Conversely, *V. peripherica* displayed active channel diversification, characterized by 14 Contrast-FEL codon sites under selective acceleration in OSCA2 and a lineage-specific tandem duplication (*VpOSCA2.4a/b*, separated by 1,292 bp) accompanied by promoter *cis*-regulatory divergence and interactome partner division. Furthermore, a localized accelerated hotspot was identified at site 593 in *V. tubiflora* (OSCA3+4, $\beta_{Test} = 24.72, p = 0.0085$), highlighting a prime candidate for rapid channel gating during rehydration. These results demonstrate that the evolutionary transition to desiccation tolerance operates via selective relaxation of a modulatory sensory layer over an invariant baseline core, providing fundamental insights into extremophyte genome biology and establishing molecular targets for engineering drought resilience in crops.

---

## 1. INTRODUCTION

### 1.1 The Biophysical and Osmosensory Challenge in Dehydrating Plant Cells

Water availability represents the primary environmental constraint dictating terrestrial plant productivity, geographic distribution, and ecosystem structure globally (Lamers et al., 2020). While downstream transcriptional cascades, metabolic remodeling, and physiological adjustments to water deprivation have been characterized in extensive detail, the initial biophysical mechanisms through which plant cells perceive water scarcity and translate physical perturbations of the cellular boundary into biochemical signaling cascades remain fundamental open questions in plant biology (Gorgues et al., 2022). Upon the onset of dehydration, transpirational water loss induces immediate physical alterations within the cell, including protoplast shrinkage, progressive loss of hydrostatic turgor pressure, mechanical deformation of the cell wall, and elevated lateral tension across the lipid bilayer (Basu and Haswell, 2017). Because catastrophic plasmolysis and irreversible structural damage can occur rapidly under severe water deficit, plant cells must possess sensory systems capable of detecting mechanical disturbances at the plasma membrane interface within seconds of dehydration onset (Hartmann et al., 2021).

Primary osmosensing in vegetative plant tissues encompasses three major conceptual tiers: membrane-associated receptor histidine kinases, cell wall integrity sensors, and mechanosensitive ion channels (Gorgues et al., 2022). Membrane-bound histidine kinases, exemplified by Arabidopsis AtHK1, were initially proposed as putative osmosensors based on their structural resemblance to yeast SLN1 (Tran et al., 2007). However, genetic analyses demonstrated that *athk1* loss-of-function mutants retain normal hyperosmotically induced calcium transients and standard osmotic transcriptional induction, indicating that histidine kinases likely function as secondary modulators of stress signaling rather than primary mechanotransducers (Kumar et al., 2013). Conversely, cell wall integrity monitoring systems, predominantly composed of *Catharanthus roseus* RLK1-like (CrRLK1L) receptor kinases such as FERONIA (FER) and THESEUS1 (THE1), perceive pectin cross-linking status and wall deformation during cellular contraction (Bacete et al., 2022; Wolf et al., 2012). While FER is required for wall reinforcement and induces a delayed calcium influx under salinity, empirical evidence suggests that FER detects sodium ion displacement within pectin matrices rather than rapid fluctuations in hydrostatic pressure (Chen et al., 2016; Feng et al., 2018). Consequently, the earliest physiological response detectable upon hyperosmotic shock remains a rapid, biphasic elevation of cytosolic free calcium ($[\text{Ca}^{2+}]_{\text{cyt}}$), which functions as a universal secondary messenger directing downstream kinase cascades, stomatal closure, and global transcriptional reprogramming (White, 2003; Ketehouli et al., 2022).

### 1.2 The Mechanosensitive Ion Channel Landscape and the Discovery of OSCA Channels

Mechanosensitive ion channels represent the primary molecular transducers responsible for directly converting membrane mechanical tension into intracellular ionic fluxes (Basu and Haswell, 2017; Kurusu et al., 2013). Several distinct mechanosensitive channel families have been identified in angiosperms, including MscS-like (MSL) channels, Mid1-complementing activity (MCA) channels, and two-pore Piezo channels (Kaur et al., 2021; Maksaev and Haswell, 2012). While MSL10 acts as a bona fide stretch-activated channel in Arabidopsis, it displays a strong biophysical preference for anions over cations and functions predominantly in response to hypo-osmotic swelling rather than hyperosmotic dehydration (Maksaev and Haswell, 2012). Similarly, although MCA1 and MCA2 mediate calcium uptake in response to touch and gravity, *mca1/mca2* double mutants display unaltered hyperosmotic calcium influx, indicating that MCA channels do not operate as primary osmosensors during dehydration (Nakagawa et al., 2007; Yamanaka et al., 2010).

The identification of the hyperosmolality-gated calcium-permeable channel 1 (OSCA1) family in *Arabidopsis thaliana* resolved the search for the core molecular apparatus mediating dehydration-induced calcium transients (Yuan et al., 2014). OSCA proteins belong to the evolutionarily conserved TMEM63/Anoctamin-like superfamily (Pfam PF02714), structurally organized as symmetric homodimers where each monomer consists of ten transmembrane helices, an amino-terminal cytosolic domain (Pfam PF14703), and an essential calcium-conducting pore domain (Zhang et al., 2018; Liu et al., 2018). Functional reconstitution of Arabidopsis OSCA1.2 into artificial liposomes established that mechanical tension applied directly to the lipid bilayer gates channel opening in the complete absence of auxiliary proteins or soluble ligands, demonstrating that mechanosensitive calcium permeation is an intrinsic biophysical property of the channel complex (Zhang et al., 2018). Phylogenetic evaluations across angiosperms classify the OSCA family into four canonical subfamilies: Clade OSCA1, Clade OSCA2, Clade OSCA3, and Clade OSCA4 (Yuan et al., 2014; Li et al., 2015). Functional studies in model crops have revealed marked functional specialization among these clades. In *Zea mays*, ectopic overexpression of *ZmOSCA2.4* enhances vegetative drought survival and root hydraulic conductivity without causing growth penalties under well-watered conditions (Cao et al., 2020). In *Oryza sativa*, individual *OsOSCA* genes exhibit divergent transcriptional responses to dehydration, salinity, and abscisic acid (ABA), pointing to functional subfunctionalization among paralogs (Li et al., 2015). Despite these advances in standard agricultural and herbaceous models, the evolutionary trajectory and structural organization of the OSCA sensory machinery in extremophyte lineages adapted to recurring, catastrophic dehydration remain largely uncharacterized.

### 1.3 The Campos Rupestres as an Evolutionary Laboratory for Contrasting Water Regimes

The Neotropical *campos rupestres* (montane quartzitic rocky outcrops of Central and Eastern Brazil) constitute ancient, climatically buffered, infertile landscapes (OCBILs) characterized by extreme edaphic nutrient poverty, shallow quartzitic substrates, high solar irradiance, and severe seasonal drought (Silveira et al., 2016; Fernandes et al., 2020). Endemic to these harsh rupestrian environments, the monocot family Velloziaceae (order Pandanales) exhibits remarkable morphological and physiological radiations, harboring sympatric congeneric species that display diametrically opposed ecological strategies for managing severe water deficit (Alcantara et al., 2015, 2018; Mello-Silva et al., 2011). 

Among these endemics, *Vellozia tubiflora* (Schult. & Schult.f.) Kunth represents a specialized poikilochlorophyllous desiccation-tolerant (DT) resurrection plant capable of surviving the loss of more than 95% of its total cellular water content (Alcantara et al., 2015; Vieira et al., 2022). Upon dehydration, *V. tubiflora* undergoes controlled degradation of its photosynthetic pigments and thylakoid membranes to mitigate photo-oxidative stress, enters a metabolic state of dormancy known as anhydrobiosis, and fully restores cellular integrity and photosynthetic competence within hours following rehydration (Vieira et al., 2022; Oliver et al., 2020). In sharp contrast, *Vellozia peripherica* Mello-Silva is a drought-sensitive, evergreen species that co-occurs in the same rocky microhabitats but adopts a dehydration-avoidant strategy (Alcantara et al., 2015, 2018). Rather than entering dormancy, *V. peripherica* sustains foliar water content, tight stomatal regulation, and basal photosynthetic metabolism throughout extended dry periods, relying on continuous water conservation and cellular maintenance (Alcantara et al., 2015). Because *V. tubiflora* and *V. peripherica* share a common phylogenetic origin, identical diploid chromosome numbers ($2n = 18$), and high macrosyntenic conservation, they provide an unmatched comparative framework to evaluate how contrasting adaptive regimes reshape the primary sensory machinery.

### 1.4 Research Questions and Conceptual Framework

The contrasting ecophysiological strategies of *V. tubiflora* and *V. peripherica* raise fundamental evolutionary questions regarding the architecture of primary osmosensing. Does the evolutionary acquisition of desiccation tolerance require large-scale genomic amplification or selective elimination of mechanosensitive ion channels, or does adaptation proceed through fine-scale regulatory divergence and selective rate modulation of ancestral channel clades? Furthermore, do baseline osmosensors that maintain cellular integrity differ in their evolutionary trajectories from modulatory channels involved in fine-tuning physiological responses?

To address these questions, we conducted a comprehensive, chromosome-scale comparative genomic investigation of the OSCA gene family in *Vellozia tubiflora* and *Vellozia peripherica*. By combining manual curation across chromosome-level assemblies, maximum-likelihood phylogenetics, macro- and microsynteny reconstruction, molecular evolutionary rate modeling ($Ka/Ks$), clade-specific selection intensity testing (HyPhy RELAX), codon-specific selective divergence scans (HyPhy Contrast-FEL), promoter *cis*-regulatory element profiling, tissue-level RNA-seq quantification, and protein-protein interaction (PPI) network topology, this study reveals the evolutionary mechanisms governing calcium-mediated osmotic perception in resurrection versus evergreen plants.

---

## 2. MATERIAL AND METHODS

### 2.1 Identification, Domain Validation, and Transmembrane Topology of OSCA Channels

To characterize the complete repertoire of OSCA genes in *Vellozia peripherica* and *Vellozia tubiflora*, we interrogated the predicted proteomes of both chromosome-level assemblies (hapA haplotype, $2n = 18$). Hidden Markov Model (HMM) profiles corresponding to the characteristic Pfam domains of the TMEM63/Anoctamin superfamily—PF02714 (RSN1_7TM), PF13967 (RSN1_TM), and PF14703 (PHM7_cyt)—were retrieved from the InterPro database (release 94.0). Profile searches were executed using the `hmmsearch` program within HMMER v3.4 with an inclusion $E\text{-value}$ threshold of $< 10^{-5}$. All retrieved candidate sequences were subsequently validated by scanning against the InterProScan v5.62-94.0 database across Pfam, PANTHER (PTHR13018 family), and SUPERFAMILY databases to confirm domain integrity and eliminate false-positive annotations.

Transmembrane topology and the number of transmembrane helices were assessed using DeepTMHMM v1.0.24 and Phobius v1.01. Protein physicochemical parameters, including deduced amino acid length, predicted molecular weight (kDa), and theoretical isoelectric point (pI), were calculated using the `ProtParam` utility within Biopython v1.83. For genomic loci encoding multiple alternatively spliced transcript isoforms, the longest canonical protein-coding sequence was selected for all downstream evolutionary and phylogenetic analyses.

### 2.2 Multiple Sequence Alignment and Maximum-Likelihood Phylogenetics

Full-length amino acid sequences of OSCA proteins from *V. peripherica* (14), *V. tubiflora* (13), *Arabidopsis thaliana* (15), *Oryza sativa* (11), *Sorghum bicolor* (11), and *Zea mays* (12) were compiled into a comprehensive monocot-eudicot comparative dataset. Sequences were aligned using MAFFT v7.526 under the L-INS-i iterative refinement algorithm (`--localpair --maxiterate 1000`), which optimizes alignment accuracy across multidomain transmembrane proteins. Non-homologous sequence extensions and poorly aligned regions were trimmed using trimAl v1.5 under the automated heuristic approach (`-automated1`).

Maximum-likelihood (ML) phylogenetic reconstruction was performed using IQ-TREE v2.4.0. ModelFinder was executed to determine the optimal amino acid substitution model according to the Bayesian Information Criterion (BIC), which selected the empirical plant-specific matrix Q.plant+F+R5. Branch support was evaluated using 1,000 ultrafast bootstrap replicates (UFBoot2) alongside 1,000 replicates of the SH-like approximate likelihood ratio test (SH-aLRT). Orthology and paralogy relationships across species were independently verified using OrthoFinder v2.5.5 executed in Diamond mode (`-S diamond`). Phylogenetic trees were rooted and visualized using the R package ggtree v3.10.1.

### 2.3 Chromosomal Localization, Macro- and Microsynteny, and Paleoduplication Profiling

Genomic coordinates and exon-intron architectures for all identified OSCA genes were parsed from the structural annotation GFF3 files of the hapA assemblies of *V. peripherica* and *V. tubiflora*. Interspecific macrosynteny and intraspecific self-synteny blocks were computed using MCScan (Python version, JCVI utility libraries v1.3.8). All-against-all protein sequence alignments were generated using Diamond v2.1.8 ($E\text{-value} < 10^{-10}$), and collinear syntenic chains were identified requiring a minimum block size of five collinear gene anchors (`--minspan=5`).

Microsynteny within local genomic windows flanking OSCA loci (spanning 10–20 adjacent gene models upstream and downstream) was visualized using custom Python scripts integrated with the JCVI graphics module. Intragenomic paleoduplications were evaluated by identifying self-synteny blocks linking non-homologous chromosomes within each genome, distinguishing ancestral whole-genome duplication (WGD) remnants from localized tandem duplication events. Tandem duplicates were formally defined as contiguous homologous genes separated by fewer than ten intervening non-homologous genes within a 100-kb window.

### 2.4 Molecular Evolutionary Rates, Selection Intensity (RELAX), and Codon-Specific Acceleration (Contrast-FEL)

To evaluate selective constraints operating on OSCA coding sequences, codon alignments were generated for all 14 orthologous and paralogous pairs using PAL2NAL v14 guided by the corresponding protein alignments. Pairwise nonsynonymous substitution rates ($Ka$), synonymous substitution rates ($Ks$), and the selective ratio ($Ka/Ks$, $\omega$) were estimated using the Yang and Nielsen (2000) method implemented in the `codeml` program of PAML v4.9.

To test whether the contrasting ecophysiological lifestyles of *V. tubiflora* (resurrection) and *V. peripherica* (evergreen) drove distinct selective pressures across gene subfamilies, the OSCA family was partitioned into three phylogenetic clades: Clade OSCA1, Clade OSCA2, and Clade OSCA3+4. Nucleotide sequences within each clade were aligned guided by local protein alignments, and corresponding subtrees were pruned from the global IQ-TREE topology. Clade-specific selection intensity was evaluated using the RELAX framework in HyPhy v2.5.52, designating *V. tubiflora* branches as the Test lineage and *V. peripherica* branches as the Reference lineage. The selection intensity parameter ($K$) was estimated, where $K < 1$ denotes significant selection relaxation toward neutrality ($p < 0.05$) and $K > 1$ indicates selection intensification.

Site-specific selective divergence between the two lineages was assessed using HyPhy Contrast-FEL v2.5.52, which compares nonsynonymous rates between Test and Reference lineages ($\beta_{Test}$ vs. $\beta_{Ref}$) at individual codon positions. To eliminate potential alignment artifacts, a gap sanitation filter was enforced, excluding positions with greater than 20% gap frequencies across the alignment. Significant sites were designated at a nominal threshold of $p \le 0.05$.

### 2.5 Upstream *cis*-Regulatory Element (CRE) Architecture

Strand-aware 2.0-kb promoter regions flanking the translation start site (ATG) of all OSCA genes were extracted from the genomic FASTA files using BEDTools v2.31.0. Putative *cis*-regulatory elements (CREs) were annotated by querying the PlantCARE database. Motif occurrences were processed using custom Python scripts to filter out general core promoter elements (TATA-box and CAAT-box) and harmonize nomenclature across case variants. Candidate CREs were classified into functional categories: phytohormone response (ABRE, CGTCA-motif, TGACG-motif, ERE), abiotic stress response (MBS, LTR, ARE, DRE, TC-rich repeats), and light regulation (G-box, Box 4, MRE, I-box). Motif distributions were visualized using ComplexHeatmap v2.18.0 in R.

### 2.6 Strand-Specific RNA-seq Profiling and Blocked Differential Expression

Strand-specific paired-end RNA-seq libraries generated from three vegetative tissues (expanded leaves, stems, and roots) across biological replicates of *V. peripherica* ($n = 3$ per tissue) and *V. tubiflora* ($n = 3$ for leaf and stem, $n = 2$ for root) were evaluated. Raw sequencing reads were quality-trimmed and filtered using fastp v0.23.4 (`--detect_adapter_for_pe --qualified_quality_phred 30`). Clean paired reads were aligned to the respective hapA reference genomes using STAR v2.7.11a in two-pass mode with default parameters. Mapped fragments overlapping annotated gene models were quantified using featureCounts (Subread package v2.0.6) with strand specificity enforced (`-s 2 -p -B -C`).

Differential expression analysis was performed in R using DESeq2 v1.42.0. To account for inter-individual biological variation among wild-collected plants, a generalized linear model incorporating an individual-blocked design was implemented:
$$\text{design} = \sim \text{Individual} + \text{Tissue}$$
Pairwise tissue contrasts (Root vs. Leaf, Stem vs. Leaf, and Root vs. Stem) were evaluated independently for each species. Genes exhibiting an FDR-adjusted $p\text{-value}$ ($padj < 0.05$) and an absolute $\log_2\text{Fold Change} \ge 1.0$ were identified as significantly differentially expressed.

### 2.7 Protein-Protein Interaction (PPI) Network Topology

Functional protein-protein interaction networks were reconstructed using the STRING database (version 12.0) with an interaction confidence score threshold of $\ge 0.400$ (medium confidence). The 14 *V. peripherica* and 13 *V. tubiflora* OSCA proteins were used as primary seeds, and networks were expanded by incorporating the top 50 first-shell functional interactors. Topological properties, including node degree, betweenness centrality, and network edge density, were computed using NetworkX v3.2 in Python. Functional enrichment of interactors was evaluated against Gene Ontology (GO) and Kyoto Encyclopedia of Genes and Genomes (KEGG) databases using clusterProfiler v4.10.0, applying a Benjamini-Hochberg FDR threshold of $< 0.05$.

---

## 3. RESULTS

### 3.1 Genome-Wide Census and Tripartite Structural Architecture of OSCA Channels in *Vellozia*

Systematic profile hidden Markov model searches using HMMER v3.4 with the Pfam profiles PF02714, PF13967, and PF14703 identified 14 candidate OSCA genes in the chromosome-scale assembly of *Vellozia peripherica* and 13 genes in *Vellozia tubiflora* (Table 1). Full-sequence inclusion $E\text{-values}$ ranged from $3.7 \times 10^{-87}$ to $4.3 \times 10^{-26}$ in *V. peripherica* and from $3.1 \times 10^{-87}$ to $1.3 \times 10^{-25}$ in *V. tubiflora*, confirming high sequence homology to canonical plant osmosensors. The total number of OSCA loci in both *Vellozia* genomes is consistent with family sizes documented in other diploid angiosperms, such as *Arabidopsis thaliana* (15 loci) and *Oryza sativa* (11 loci), indicating that the macroevolutionary diversification of Velloziaceae occurred without massive global amplification of the mechanosensitive channel repertoire.

Deduced OSCA protein lengths ranged from 714 amino acids (*VtOSCA4.1*, 81.5 kDa) to 774 amino acids (*VpOSCA1.1*, 88.5 kDa), with predicted theoretical isoelectric points varying between 6.84 and 9.12 (Table 1). Transmembrane topology modeling using DeepTMHMM and Phobius confirmed that all 27 identified channels exhibit the structural signature of the TMEM63/Anoctamin superfamily, possessing 10 transmembrane helices, an intracellular amino-terminal cytosolic domain (Pfam PF14703), and a carboxy-terminal calcium-conducting pore domain (Pfam PF02714). Minor terminal rearrangements were observed in *VpOSCA2.2* and *VtOSCA1.2*, where the predicted cytosolic domain was truncated without compromising the core transmembrane gating helices. The numerical difference between the two species mapped exclusively to chromosome 1A, where *V. peripherica* harbored two tandemly arranged paralogs (*VpOSCA2.4a* and *VpOSCA2.4b*) compared to a single locus (*VtOSCA2.4*) in *V. tubiflora*.

#### Table 1: Genomic Characteristics of the OSCA Gene Family in *Vellozia*

| Species | Gene Name | Locus ID | Clade | Chromosome | Coordinates (bp) | Strand | Length (aa) | MW (kDa) | Pfam Domain Architecture |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| *V. peripherica* | *VpOSCA1.1* | `Vper.hapA.v1.chr4A.g118180.t1` | OSCA1 | chr4A | 11,237,808–11,254,982 | - | 774 | 88.5 | PF13967, PF14703, PF02714 |
| *V. peripherica* | *VpOSCA1.2* | `Vper.hapA.v1.chr9A.g255900.t1` | OSCA1 | chr9A | 17,564,347–17,578,689 | - | 768 | 87.9 | PF13967, PF14703, PF02714 |
| *V. peripherica* | *VpOSCA1.3* | `Vper.hapA.v1.chr7A.g179370.t1` | OSCA1 | chr7A | 1,154,964–1,162,617 | + | 761 | 86.8 | PF13967, PF14703, PF02714 |
| *V. peripherica* | *VpOSCA1.4* | `Vper.hapA.v1.chr7A.g179380.t1` | OSCA1 | chr7A | 1,165,818–1,173,766 | + | 759 | 86.4 | PF13967, PF14703, PF02714 |
| *V. peripherica* | *VpOSCA1.5* | `Vper.hapA.v1.chr7A.g179390.t1` | OSCA1 | chr7A | 1,190,163–1,199,238 | + | 763 | 87.1 | PF13967, PF14703, PF02714 |
| *V. peripherica* | *VpOSCA2.1* | `Vper.hapA.v1.chr5A.g140750.t1` | OSCA2 | chr5A | 1,645,547–1,653,691 | + | 739 | 84.6 | PF13967, PF14703, PF02714 |
| *V. peripherica* | *VpOSCA2.2* | `Vper.hapA.v1.chr1A.g021690.t1` | OSCA2 | chr1A | 21,367,423–21,371,278 | - | 742 | 85.1 | PF14703, PF02714 |
| *V. peripherica* | *VpOSCA2.3* | `Vper.hapA.v1.chr1A.g013600.t1` | OSCA2 | chr1A | 13,332,252–13,336,746 | + | 745 | 85.3 | PF13967, PF14703, PF02714 |
| *V. peripherica* | *VpOSCA2.4a* | `Vper.hapA.v1.chr1A.g023030.t1` | OSCA2 | chr1A | 22,689,052–22,697,439 | + | 738 | 84.2 | PF13967, PF14703, PF02714 |
| *V. peripherica* | *VpOSCA2.4b* | `Vper.hapA.v1.chr1A.g023020.t1` | OSCA2 | chr1A | 22,678,816–22,687,760 | + | 740 | 84.7 | PF13967, PF14703, PF02714 |
| *V. peripherica* | *VpOSCA2.5* | `Vper.hapA.v1.chr9A.g257040.t1` | OSCA2 | chr9A | 18,576,254–18,590,260 | - | 736 | 84.0 | PF13967, PF14703, PF02714 |
| *V. peripherica* | *VpOSCA3.1* | `Vper.hapA.v1.chr1A.g020450.t1` | OSCA3 | chr1A | 20,008,265–20,014,313 | + | 722 | 82.4 | PF13967, PF14703, PF02714 |
| *V. peripherica* | *VpOSCA3.2* | `Vper.hapA.v1.chr5A.g142080.t1` | OSCA3 | chr5A | 2,668,389–2,675,373 | - | 726 | 82.9 | PF13967, PF14703, PF02714 |
| *V. peripherica* | *VpOSCA4.1* | `Vper.hapA.v1.chr8A.g231320.t1` | OSCA4 | chr8A | 20,598,462–20,602,234 | - | 715 | 81.6 | PF13967, PF14703, PF02714 |
| *V. tubiflora* | *VtOSCA1.1* | `Vtub.hapA.v1.chr4A.g106800.t1` | OSCA1 | chr4A | 10,819,227–10,835,638 | - | 772 | 88.3 | PF13967, PF14703, PF02714 |
| *V. tubiflora* | *VtOSCA1.2* | `Vtub.hapA.v1.chr9A.g230740.t1` | OSCA1 | chr9A | 17,719,979–17,728,315 | - | 766 | 87.6 | PF14703, PF02714 |
| *V. tubiflora* | *VtOSCA1.3* | `Vtub.hapA.v1.chr7A.g166590.t1` | OSCA1 | chr7A | 1,018,480–1,027,560 | + | 760 | 86.7 | PF13967, PF14703, PF02714 |
| *V. tubiflora* | *VtOSCA1.4* | `Vtub.hapA.v1.chr7A.g166600.t1` | OSCA1 | chr7A | 1,029,792–1,039,945 | + | 758 | 86.3 | PF13967, PF14703, PF02714 |
| *V. tubiflora* | *VtOSCA1.5* | `Vtub.hapA.v1.chr7A.g166610.t1` | OSCA1 | chr7A | 1,049,541–1,057,767 | + | 762 | 87.0 | PF13967, PF14703, PF02714 |
| *V. tubiflora* | *VtOSCA2.1* | `Vtub.hapA.v1.chr5A.g127830.t1` | OSCA2 | chr5A | 1,496,336–1,503,868 | + | 738 | 84.5 | PF13967, PF14703, PF02714 |
| *V. tubiflora* | *VtOSCA2.2* | `Vtub.hapA.v1.chr1A.g019410.t1` | OSCA2 | chr1A | 20,232,004–20,238,727 | - | 741 | 85.0 | PF13967, PF14703, PF02714 |
| *V. tubiflora* | *VtOSCA2.3* | `Vtub.hapA.v1.chr1A.g012080.t1` | OSCA2 | chr1A | 12,783,202–12,787,679 | + | 744 | 85.2 | PF13967, PF14703, PF02714 |
| *V. tubiflora* | *VtOSCA2.4* | `Vtub.hapA.v1.chr1A.g020650.t1` | OSCA2 | chr1A | 21,645,212–21,654,612 | + | 739 | 84.4 | PF13967, PF14703, PF02714 |
| *V. tubiflora* | *VtOSCA2.5* | `Vtub.hapA.v1.chr9A.g231910.t1` | OSCA2 | chr9A | 18,668,636–18,684,281 | - | 735 | 83.9 | PF13967, PF14703, PF02714 |
| *V. tubiflora* | *VtOSCA3.1* | `Vtub.hapA.v1.chr1A.g018250.t1` | OSCA3 | chr1A | 18,922,458–18,928,500 | + | 721 | 82.3 | PF13967, PF14703, PF02714 |
| *V. tubiflora* | *VtOSCA3.2* | `Vtub.hapA.v1.chr5A.g129040.t1` | OSCA3 | chr5A | 2,457,574–2,466,320 | - | 725 | 82.8 | PF13967, PF14703, PF02714 |
| *V. tubiflora* | *VtOSCA4.1* | `Vtub.hapA.v1.chr8A.g207990.t1` | OSCA4 | chr8A | 24,477,668–24,481,020 | - | 714 | 81.5 | PF13967, PF14703, PF02714 |

---

### 3.2 Maximum-Likelihood Phylogeny and Topological Placement of the OSCA2.4 Locus

Maximum-likelihood phylogenetic inference incorporating 76 full-length OSCA sequences from *Vellozia peripherica* (14), *Vellozia tubiflora* (13), *Arabidopsis thaliana* (15), *Oryza sativa* (11), *Sorghum bicolor* (11), and *Zea mays* (12) resolved all *Vellozia* proteins into the four canonical angiosperm clades with robust statistical support (Figure 1). Under the best-fitting Q.plant+F+R5 model, Clade OSCA1 clustered 10 *Vellozia* sequences into five direct orthologous pairs. Clade OSCA2 emerged as the largest subfamily, containing 11 sequences (six in *V. peripherica* and five in *V. tubiflora*). Clade OSCA3 comprised four sequences forming two orthologous pairs (*OSCA3.1* and *OSCA3.2*), while Clade OSCA4 contained two sequences forming a basal sister pair (*VpOSCA4.1* and *VtOSCA4.1*). Major nodes separating the four subfamilies and 12 of the 13 interspecific gene pairs exhibited 100% Ultrafast Bootstrap (UFBoot2) and 100% SH-aLRT support, demonstrating that primary clade diversification predated the speciation of *Vellozia*.

The primary topological asymmetry was localized within the OSCA2.4 lineage on chromosome 1A (Figure 1). The OSCA2.4 subclade formed a strongly supported monophyletic group (100% bootstrap support) comprising *VpOSCA2.4a*, *VpOSCA2.4b*, and *VtOSCA2.4*. Within this cluster, *VpOSCA2.4b* was resolved as sister to *VtOSCA2.4* with 83% bootstrap support, whereas *VpOSCA2.4a* occupied an adjacent derived position. This branching pattern demonstrates that *VpOSCA2.4b* represents the ancestral ortholog shared across species, while *VpOSCA2.4a* arose via a lineage-specific gene duplication event in the evergreen *V. peripherica* lineage following its divergence from *V. tubiflora*.

---

### 3.3 Macrosyntenic Stability, Chromosomal Collinearity, and Ancient vs. Lineage-Specific Duplications

Comparative synteny analysis using MCScan recovered 21,309 gene anchors organized into 297 collinear syntenic blocks between the hapA genomes of *V. peripherica* and *V. tubiflora*. The genome-wide dot plot revealed an unbroken diagonal across all nine chromosome pairs ($2n = 18$), indicating that the two genomes maintain high chromosomal collinearity without large-scale interchromosomal translocations. All 27 OSCA loci mapped to strictly collinear syntenic blocks across chromosomes 1A, 4A, 5A, 7A, 8A, and 9A.

On chromosome 7A, the *OSCA1.3/1.4/1.5* tandem cluster exhibited complete conservation of gene order and transcriptional orientation in both species. The three loci were physically contiguous with zero intervening genes (gap = 0) and were flanked by 24 collinear orthologous anchors, confirming that this tandem sensory cluster expanded prior to the speciation of *Vellozia* and was preserved under strong purifying selection.

Intragenomic self-synteny profiling identified an ancient segmental paleoduplication block connecting chromosomes 1A and 5A in both species. This conserved collinear block harbored duplicated paralogs from two distinct subfamilies: Clade 2 (*OSCA2.1* on chr5A vs. *OSCA2.2* on chr1A) and Clade 3 (*OSCA3.1* on chr1A vs. *OSCA3.2* on chr5A). The reciprocal retention of this duplicated block across both species provides clear physical evidence of an ancestral whole-genome duplication (WGD) shared by Core Velloziaceae.

In contrast, localized divergence on chromosome 1A confirmed the species-specific architecture of the OSCA2.4 locus. In *V. peripherica*, *VpOSCA2.4a* and *VpOSCA2.4b* are located in direct head-to-tail orientation separated by an intergenic distance of only 1,292 bp with zero intervening genes. In *V. tubiflora*, this genomic interval contains exclusively *VtOSCA2.4*, which matches *VpOSCA2.4b* as the primary syntenic anchor. Thus, the chromosomal organization of the OSCA family in *Vellozia* reflects an evolutionary combination of stable ancestral WGD retention alongside a single, lineage-specific tandem duplication in the evergreen lineage.

---

### 3.4 Molecular Evolutionary Rates ($Ka/Ks$) and the Subfamily-Partitioned Dual-Track Model (RELAX)

Pairwise estimation of nonsynonymous ($Ka$) and synonymous ($Ks$) substitution rates across all 14 interspecific OSCA comparisons yielded $Ka/Ks$ ($\omega$) ratios ranging from 0.0536 to 0.8016, with an overall mean of 0.4082 and a median of 0.3403. All estimated pairwise ratios were strictly $< 1.0$, indicating that purifying selection has acted as the primary evolutionary force preserving OSCA protein coding sequences across both species. Among the orthologous pairs, *VpOSCA2.3/VtOSCA2.3* exhibited the lowest ratio ($Ka = 0.0046, Ks = 0.0859, Ka/Ks = 0.0536$), pointing to severe functional constraint. The basal pair *VpOSCA4.1/VtOSCA4.1* also showed strong purifying constraint ($Ka = 0.0124, Ks = 0.0775, Ka/Ks = 0.1600$). Conversely, *VpOSCA1.4/VtOSCA1.4* displayed the highest ratio ($Ka = 0.0877, Ks = 0.1094, Ka/Ks = 0.8016$), indicating accelerated nonsynonymous substitution within the chromosome 7A cluster. The tandem paralogous pair *VpOSCA2.4a/VpOSCA2.4b* yielded a $Ka/Ks$ ratio of 0.3771 ($Ka = 0.0442, Ks = 0.1172$).

Clade-partitioned selection intensity modeling using HyPhy RELAX revealed profound heterogeneity in selective constraints among subfamilies, establishing the **Dual-Track Evolutionary Model**. Under Track 1, Clade OSCA1 (comprising 10 genes) exhibited no significant difference in selection intensity between the resurrection specialist and the evergreen species ($K = 0.9215, p = 0.5957, \text{LRT} = 0.2816$). This indicates that baseline osmosensory channels, including the chromosome 7A tandem cluster, operate under identical, invariant purifying selection regardless of the drought survival strategy. In sharp contrast, Track 2 demonstrated that Clades OSCA2 and OSCA3+4 underwent massive, statistically significant selection relaxation in the resurrection specialist *V. tubiflora*. Specifically, in Clade OSCA2 (11 genes), *V. tubiflora* displayed a pronounced relaxation parameter of $K = 0.2828$ ($p = 3.4 \times 10^{-5}, \text{LRT} = 17.1612$), while in Clade OSCA3+4 (6 genes), selection was similarly relaxed in the resurrection specialist ($K = 0.1349, p = 0.0061$, $\text{LRT} = 7.5334$). Together, these results demonstrate that the global signal of evolutionary relaxation observed in *V. tubiflora* is entirely driven by the modulatory OSCA2 and OSCA3+4 subfamilies, whereas the primary OSCA1 sensory core remains canalized and unperturbed.

---

### 3.5 Site-Specific Selective Divergence and Gap-Sanitized Hotspots (Contrast-FEL)

Evaluation of site-specific selective divergence using HyPhy Contrast-FEL, combined with gap sanitation to eliminate five false-positive sites associated with high alignment gaps (sites 401, 797, 803, 821, and 842), identified individual codon positions evolving under significantly divergent nonsynonymous rates between species (Table 2; Figure 2).

#### Table 2: Statistically Significant Codon Sites under Selective Divergence (Contrast-FEL, $p \le 0.05$)

| Phylogenetic Clade | Local Site (Global Alignment Site) | $\beta_\text{Test}$ Rate (*Vtub*) | $\beta_\text{Ref}$ Rate (*Vper*) | $p\text{-value}$ | Predicted Evolutionary Divergence Pattern |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **OSCA1** | Local 181 (Global 484) | 8.20 | 0.03 | 0.0350 | Non-synonymous acceleration in resurrection specialist *V. tubiflora*. |
| **OSCA1** | Local 710 (Global 1232) | 7.66 | 0.00 | 0.0200 | Non-synonymous acceleration in resurrection specialist *V. tubiflora*. |
| **OSCA1** | Local 252 | 0.00 | 4.85 | 0.0412 | Non-synonymous acceleration in evergreen *V. peripherica*. |
| **OSCA1** | Local 430 | 0.00 | 5.12 | 0.0387 | Non-synonymous acceleration in evergreen *V. peripherica*. |
| **OSCA1** | Local 973 | 0.00 | 6.44 | 0.0195 | Non-synonymous acceleration in evergreen *V. peripherica*. |
| **OSCA2** | **14 Sites:** 8, 71, 76, 147, 191, 241, 270, 308, 394, 395, 432, 596, 720, 824 | $\approx 0.00$ | $\gg 0.00$ | $\le 0.05$ | **100% Unidirectional Acceleration in *V. peripherica*:** Active channel diversification in evergreen background. |
| **OSCA3+4** | Local 593 (Global 1094) | 24.72 | 0.018 | 0.0085 | **Accelerated Hotspot in *V. tubiflora*:** Localized relaxation or positive selection in resurrection specialist. |

In Clade OSCA2, 14 codon positions exhibited significant rate differences ($p \le 0.05$), with 100% of these sites displaying extreme selective acceleration in the evergreen *V. peripherica* ($\beta_{Ref} \gg 0$) while remaining strictly constrained in *V. tubiflora* ($\beta_{Test} \approx 0$; Table 2). This unidirectional pattern indicates that Clade 2 channels are actively diversifying in the evergreen lineage to fine-tune mechanosensation under continuous, diurnal osmotic fluctuations. Conversely, in Clade OSCA3+4, a single prominent codon position—Local Site 593 (Global Site 1094)—exhibited an exceptionally high nonsynonymous rate in *V. tubiflora* ($\beta_{Test} = 24.72$ vs. $\beta_{Ref} = 0.018, p = 0.0085$), defining a localized evolutionary hotspot in the resurrection plant. In Clade OSCA1, six sites showed selective divergence, including sites 181 and 710 accelerated in *V. tubiflora*, and sites 252, 430, and 973 accelerated in *V. peripherica*.

---

### 3.6 Promoter *cis*-Regulatory Element Landscaping and Tandem Paralog Divergence

Analysis of 2.0-kb upstream promoter sequences identified 672 non-core *cis*-regulatory element (CRE) occurrences across the 14 *V. peripherica* promoters and 653 across the 13 *V. tubiflora* promoters (Table 3). Stress-responsive ABRE motifs (ABA-responsive) occurred in 13 of 14 *V. peripherica* promoters and 10 of 13 *V. tubiflora* promoters. MYB-binding sites involved in drought signaling (MBS), low-temperature elements (LTR), and anaerobic/oxidative stress motifs (ARE) were broadly distributed in both species. Light-responsive G-box and Box 4 elements, along with methyl jasmonate-responsive CGTCA/TGACG motifs, were also widely detected, pointing to coordinated transcriptional regulation by light and hormonal signaling networks.

#### Table 3: Selected *cis*-Regulatory Elements in 2.0-kb Promoter Regions (PlantCARE)

| Gene | ABRE (ABA) | MBS (Drought/MYB) | LTR (Cold) | ARE (Oxidative) | G-box (Light/BZIP) | Box 4 (Light) | DRE (Dehydration) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| *VpOSCA1.1* | 3 | 0 | 0 | 1 | 3 | 14 | 1 |
| *VpOSCA1.2* | 3 | 1 | 4 | 2 | 3 | 2 | 0 |
| *VpOSCA2.1* | 13 | 2 | 0 | 0 | 7 | 4 | 0 |
| *VpOSCA2.4a* | 7 | 1 | 2 | 4 | 2 | 2 | 1 |
| *VpOSCA2.4b* | 8 | 0 | 1 | 1 | 6 | 6 | 0 |
| *VpOSCA3.2* | 14 | 1 | 0 | 0 | 11 | 2 | 2 |
| *VpOSCA4.1* | 5 | 2 | 1 | 3 | 3 | 3 | 0 |
| *VtOSCA1.1* | 11 | 1 | 0 | 1 | 10 | 11 | 1 |
| *VtOSCA1.2* | 0 | 1 | 0 | 2 | 0 | 0 | 1 |
| *VtOSCA2.1* | 15 | 3 | 1 | 2 | 14 | 5 | 4 |
| *VtOSCA2.4* | 12 | 0 | 2 | 2 | 8 | 4 | 0 |
| *VtOSCA3.2* | 6 | 1 | 2 | 0 | 5 | 1 | 0 |
| *VtOSCA4.1* | 0 | 2 | 1 | 3 | 0 | 1 | 0 |

Promoter comparison between the tandem duplicated paralogs on chromosome 1A revealed *cis*-regulatory divergence following duplication. Although *VpOSCA2.4a* and *VpOSCA2.4b* both contained 49 total CREs, their specific motif compositions diverged markedly. *VpOSCA2.4a* retained four ARE oxidative stress elements and two LTR motifs, but possessed only two G-box elements. Conversely, *VpOSCA2.4b* accumulated six G-box and six Box 4 light-responsive motifs while retaining only a single ARE motif (Table 3). This divergence supports regulatory subfunctionalization, wherein *VpOSCA2.4a* is preferentially configured for oxidative stress responses during drought, while *VpOSCA2.4b* is tuned to diurnal light and photoperiodic signaling.

---

### 3.7 Spatial Transcriptomic Profiling across Vegetative Tissues

Strand-specific RNA-seq quantification and generalized linear modeling with an individual-blocked design (`~ Individual + Tissue`) revealed conserved tissue-biased expression patterns for key OSCA orthologs (Table 4).

#### Table 4: Differentially Expressed OSCA Genes across Vegetative Tissues (DESeq2)

| Gene | Species | Tissue Contrast | $\text{baseMean}$ | $\log_2\text{Fold Change}$ | Standard Error (lfcSE) | $p\text{-adj}$ (FDR) | Tissue Specialization |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| *VpOSCA1.1* | *V. peripherica* | Root vs Leaf | 856.1 | -1.40 | 0.52 | 0.0269 | Leaf Enrichment |
| *VpOSCA1.1* | *V. peripherica* | Stem vs Leaf | 856.1 | -1.79 | 0.52 | 0.0029 | Leaf Enrichment |
| *VtOSCA1.1* | *V. tubiflora* | Root vs Leaf | 762.1 | -1.19 | 0.46 | 0.0357 | Leaf Enrichment |
| *VtOSCA1.1* | *V. tubiflora* | Stem vs Leaf | 762.1 | -2.07 | 0.39 | $1.2 \times 10^{-6}$ | Robust Leaf Enrichment |
| *VpOSCA1.2* | *V. peripherica* | Root vs Leaf | 33.8 | **+4.40** | 1.30 | **0.0041** | **Root Specialization** |
| *VtOSCA1.2* | *V. tubiflora* | Root vs Leaf | 39.0 | **+8.64** | 1.76 | $\mathbf{1.0 \times 10^{-5}}$ | **Extreme Root Specialization** |
| *VpOSCA1.2* | *V. peripherica* | Stem vs Leaf | 33.8 | **+5.46** | 1.30 | **0.0002** | Stem Specialization |
| *VtOSCA1.2* | *V. tubiflora* | Stem vs Leaf | 39.0 | **+5.52** | 1.60 | **0.0024** | Stem Specialization |
| *VpOSCA2.3* | *V. peripherica* | Stem vs Leaf | 19.2 | +3.84 | 1.53 | 0.0424 | Stem Induction |
| *VtOSCA2.4* | *V. tubiflora* | Root vs Leaf | 2082.4 | +0.79 | 0.28 | 0.0214 | Root Enrichment |
| *VtOSCA3.2* | *V. tubiflora* | Root vs Leaf | 96.2 | **+4.55** | 1.44 | 0.0075 | Root Enrichment |
| *VpOSCA3.1* | *V. peripherica* | Stem vs Leaf | 2985.4 | -1.69 | 0.44 | $9.5 \times 10^{-4}$ | Leaf Enrichment |
| *VtOSCA3.1* | *V. tubiflora* | Stem vs Leaf | 3222.3 | -2.92 | 0.66 | $5.8 \times 10^{-5}$ | Leaf Enrichment |
| *VtOSCA4.1* | *V. tubiflora* | Root vs Stem | 405.2 | +1.85 | 0.49 | 0.0018 | Subterranean Modulation |

The orthologous pair *OSCA1.2* exhibited striking subterranean and vascular specialization in both species. In *V. peripherica*, *VpOSCA1.2* was significantly enriched in roots ($\log_2\text{FC} = +4.40, padj = 0.0041$) and stems ($\log_2\text{FC} = +5.46, padj = 0.0002$) relative to leaves. This pattern was amplified in *V. tubiflora*, where *VtOSCA1.2* showed massive root enrichment ($\log_2\text{FC} = +8.64, padj = 1.0 \times 10^{-5}$) and stem enrichment ($\log_2\text{FC} = +5.52, padj = 0.0024$; Table 4). Conversely, *OSCA1.1* and *OSCA3.1* exhibited consistent foliar enrichment across both species. *VtOSCA1.1* was significantly downregulated in stems compared to leaves ($\log_2\text{FC} = -2.07, padj = 1.2 \times 10^{-6}$), mirroring *VpOSCA1.1* ($\log_2\text{FC} = -1.79, padj = 0.0029$). Similarly, *OSCA3.1* transcript abundance was significantly higher in leaves than stems in both *V. tubiflora* ($\log_2\text{FC} = -2.92, padj = 5.8 \times 10^{-5}$) and *V. peripherica* ($\log_2\text{FC} = -1.69, padj = 9.5 \times 10^{-4}$). The tandem duplicates *VpOSCA2.4a* and *VpOSCA2.4b* displayed basal expression across tissues without significant differential bias, whereas *VtOSCA2.4* was moderately enriched in roots ($\log_2\text{FC} = +0.79, padj = 0.0214$).

---

### 3.8 Comparative Interactome Topology and Hub Specialization

Reconstruction of functional protein-protein interaction networks using STRING (confidence $\ge 0.400$) revealed distinct network architectures between species. The *V. tubiflora* network comprised 60 nodes and 217 edges with a mean degree of 7.23, displaying a 16% higher edge density than the *V. peripherica* network (61 nodes, 187 edges, mean degree 6.13). Eleven *V. peripherica* and ten *V. tubiflora* OSCA queries were connected to the network, while *OSCA2.1*, *OSCA2.2*, and *OSCA2.3* lacked associations above the confidence threshold in both species, defining a "silent periphery".

Centrality analysis identified *OSCA1.2* as an invariant vascular hub possessing exactly 18 identical first-shell functional interactors in both species. These conserved partners included vacuolar proton pumps (V-type $\text{H}^+$-ATPases), cation/calcium exchangers (CAX family), and calcium-dependent protein kinases (CDPKs). Conversely, *OSCA4.1* functioned as the primary hub in *V. peripherica* with 19 connections (compared to 13 in *V. tubiflora*), interacting with molecular chaperones (HSP70 and HSP90) and voltage-dependent calcium channels. *OSCA1.1* served as a foliar hub (11 connections in *V. peripherica*, 13 in *V. tubiflora*), connecting to inward-rectifying potassium channels and plasma membrane $\text{H}^+$-ATPases. 

Topological analysis also provided evidence of interactome partner partitioning between the tandem duplicates on chromosome 1A. In *V. tubiflora*, the single-copy *VtOSCA2.4* possessed five distinct functional connections. In *V. peripherica*, *VpOSCA2.4a* and *VpOSCA2.4b* each possessed only two connections, dividing the ancestral interactome partners between the duplicated copies.

---

## 4. DISCUSSION

### 4.1 Numerical Invariance and Evolutionary Canalization of Primary Osmosensors

The chromosome-scale identification of 14 OSCA genes in *Vellozia peripherica* and 13 in *Vellozia tubiflora* demonstrates that the macroevolutionary transition to poikilochlorophyllous desiccation tolerance did not require large-scale gene family expansion (Table 1). This numerical stability—closely mirroring the 15 loci in *Arabidopsis thaliana* and 11 in *Oryza sativa*—stands in stark contrast to the massive lineage-specific expansions observed in downstream protective gene families in resurrection plants, such as late embryogenesis abundant (LEA) proteins, small heat shock proteins, and dirigent-like proteins (Costa et al., 2017; Vieira et al., 2022). In extremophyte genomes, whole-genome duplication remnants are frequently retained selectively in gene families directly involved in scavenging reactive oxygen species, repairing macromolecular damage, or vitrifying the cytoplasm (Farrant et al., 2007; Oliver et al., 2020). However, the mechanosensitive calcium channel apparatus appears subject to strict gene dosage constraints and functional canalization. Because OSCA proteins assemble into homodimeric complexes that gate calcium entry directly in response to bilayer tension (Zhang et al., 2018), unconstrained proliferation of pore-forming channel subunits could risk unregulated calcium influx, membrane depolarization, or spontaneous cytotoxicity (Basu and Haswell, 2017). Consequently, natural selection in Velloziaceae preserved the ancestral angiosperm channel inventory, directing evolutionary innovation toward fine-scale regulatory divergence, localized tandem duplication, and subfamily-specific modulation of selective constraints rather than global gene dosage amplification.

### 4.2 The Dual-Track Evolutionary Model: Preserving the Perceptive Base While Relaxing the Modulatory Layer

The central finding of this investigation is the empirical establishment of the **Dual-Track Evolutionary Model**, which resolves how conflicting selective pressures govern primary osmosensing in extremophytes with contrasting ecological strategies. In **Track 1**, Clade OSCA1 evolved under invariant, strict purifying selection across both the resurrection specialist and the evergreen species ($K = 0.9215, p = 0.5957$). This evolutionary stability indicates that Clade 1 channels fulfill an essential, non-negotiable physiological requirement: detecting baseline osmotic fluctuations and maintaining hydraulic communication between roots, vascular conduits, and leaves (Yuan et al., 2014; Liu et al., 2022). Regardless of whether a plant adopts anhydrobiosis or drought avoidance, it must accurately monitor initial soil water depletion and trigger baseline stomatal closure before cellular water potential drops to critical thresholds (Gorgues et al., 2022).

In contrast, **Track 2** revealed massive, statistically significant selection relaxation in *V. tubiflora* across Clades OSCA2 ($K = 0.2828, p = 3.4 \times 10^{-5}$) and OSCA3+4 ($K = 0.1349, p = 0.0061$). This evolutionary release is functionally congruent with the ecophysiological phenotype of resurrection plants. Upon losing more than 90% of its cellular water, *V. tubiflora* ceases transpiration, dismantles its photosynthetic apparatus, vitrifies its cytoplasm with non-reducing sugars, and enters a state of complete metabolic dormancy (Alcantara et al., 2015; Vieira et al., 2022). During this anhydrobiotic quiescence, the plasma membrane undergoes severe folding and physical compaction, and dynamic transmembrane ion transport is arrested (Oliver et al., 2020). Because mechanosensitive ion channels cannot operate within a vitrified, glass-like cytoplasm, functional selective constraints on modulatory OSCA2 and OSCA3+4 channels are suspended during extended periods of seasonal desiccation. Under this temporary cessation of functional screening, neutral mutations accumulate across modulatory channel loci, generating the pronounced signatures of selection relaxation detected by HyPhy RELAX. Conversely, the evergreen *V. peripherica* remains metabolically active year-round in the same rocky outcrops, experiencing continuous diurnal cycles of evaporative demand, solar radiation, and fluctuating leaf turgor (Alcantara et al., 2015). To survive under these relentless environmental oscillations without entering dormancy, *V. peripherica* requires continuous sensory surveillance and fine-tuned channel gating, driving the active diversification of its modulatory channel repertoire.

### 4.3 Physical Contiguity, Purifying Selection, and Concerted Evolution of the Chromosome 7A Tandem Cluster

The structural preservation of the *OSCA1.3/1.4/1.5* tandem cluster on chromosome 7A represents a striking example of chromosomal conservation across speciation. In both *V. peripherica* and *V. tubiflora*, these three genes are arranged in identical transcriptional orientation with zero intervening genes (gap = 0) and are flanked by 24 collinear orthologs. Tandem gene clusters in plants frequently serve as evolutionary cradles for environmental sensing, facilitating coregulated chromatin opening, coordinated transcriptional induction, and sequence homogenization via unequal crossing-over or gene conversion (Hanada et al., 2008). The fact that this physical cluster was maintained intact despite the ecological divergence of the two species points to strong purifying selection acting on its architectural configuration.

Interestingly, evolutionary rate modeling revealed that *OSCA1.4* exhibited the highest $Ka/Ks$ ratio among all evaluated orthologous pairs ($Ka/Ks = 0.8016, Ka = 0.0877, Ks = 0.1094$), despite being embedded within this conserved cluster. While this elevated ratio remains below 1.0 and does not provide formal proof of positive selection, it suggests that *OSCA1.4* experienced relaxed constraint or accelerated nonsynonymous substitution following speciation. In Arabidopsis, OSCA1.3 and OSCA1.4 have been implicated in stomatal immunity and specialized calcium influx during pathogen perception and environmental stress (Thor et al., 2020; Zhai et al., 2020). It is therefore plausible that while *OSCA1.3* and *OSCA1.5* maintain core mechanosensory functions within the cluster, *OSCA1.4* underwent localized subfunctionalization, potentially adapting its channel kinetics to lineage-specific signaling requirements.

### 4.4 Lineage-Specific Tandem Duplication of *OSCA2.4* and *cis*-Regulatory Subfunctionalization

The discovery of a lineage-specific tandem duplication at the OSCA2.4 locus in *V. peripherica* provides direct empirical evidence of sensory diversification in the evergreen lineage. Genomic coordinates confirmed that *VpOSCA2.4a* and *VpOSCA2.4b* are separated by only 1,292 bp on chromosome 1A, while phylogenetic analysis placed *VpOSCA2.4b* as the direct cross-species sister to *VtOSCA2.4* (83% bootstrap support) and *VpOSCA2.4a* in an adjacent derived branch (Figure 1). This chromosomal architecture demonstrates that the duplication occurred post-speciation in the evergreen lineage, providing an additional paralogous unit in the exact subfamily (OSCA2) that is undergoing active diversification.

Promoter profiling revealed clear evidence of *cis*-regulatory subfunctionalization between the duplicated paralogs (Table 3). *VpOSCA2.4a* retained four ARE oxidative stress motifs and two LTR motifs, configuring its promoter for transcriptional activation under photo-oxidative and thermal stress. In contrast, *VpOSCA2.4b* accumulated six G-box and six Box 4 light-responsive motifs while retaining only a single ARE motif. In montane *campos rupestres*, evergreen plants must cope simultaneously with extreme midday solar irradiance and rapid transpiration surges (Silveira et al., 2016; Fernandes et al., 2020). The regulatory partitioning between *VpOSCA2.4a* and *VpOSCA2.4b* suggests that gene duplication allowed the evergreen lineage to decouple mechanosensory channel induction during oxidative crisis from diurnal, light-dependent stomatal regulation, providing greater physiological plasticity during seasonal water deficit.

### 4.5 Conserved Spatial Deployment and the Immutable Vascular Core Hub (*OSCA1.2*)

Transcriptomic profiling across vegetative tissues demonstrated that spatial division of labor among OSCA channels remained remarkably conserved across speciation (Table 4). In both *V. peripherica* and *V. tubiflora*, *OSCA1.2* displayed pronounced, preferential transcript accumulation in roots ($\log_2\text{FC} = +4.40$ and $+8.64$, respectively) and stems ($\log_2\text{FC} = +5.46$ and $+5.52$, respectively) compared to leaves. Conversely, *OSCA1.1* and *OSCA3.1* showed consistent foliar enrichment across both genomes. This shared spatial partitioning indicates that the anatomical mapping of osmosensation—deploying *OSCA1.2* for subterranean and vascular water perception and *OSCA1.1/3.1* for foliar turgor and stomatal regulation—was fully established in the common ancestor of *Vellozia* and remained refractory to ecophysiological divergence.

The biological significance of *OSCA1.2* is further underscored by protein-protein interaction network topology, where it emerged as an invariant vascular hub possessing exactly 18 identical first-shell interactors in both species. In angiosperm vascular bundles, xylem parenchyma cells experience intense mechanical tension during transpirational pull and drought-induced embolism (Lamers et al., 2020). The conserved physical interaction between OSCA1.2, vacuolar $\text{H}^+$-ATPases, and cation/calcium exchangers suggests that OSCA1.2 functions as an essential tension sensor that detects cavitation risk or xylem sap hyperosmolality, triggering localized calcium influx to activate downstream proton pumps and maintain ionic homeostasis. The immutable conservation of both transcript localization and interactome connectivity confirms that *OSCA1.2* constitutes the primary biophysical anchor of osmosensory perception in Velloziaceae.

### 4.6 The "Silent Periphery" and the OSCA3+4 Residue 593 Hotspot

Protein-protein interaction analysis revealed that *OSCA2.1*, *OSCA2.2*, and *OSCA2.3* lacked functional associations above the confidence threshold in both species, defining a "silent periphery". Rather than indicating pseudogenization or functional irrelevance, this topological isolation is functionally coherent with channel biophysics. Notably, *OSCA2.3* exhibited the most extreme purifying selection of the entire family ($Ka/Ks = 0.0536, Ka = 0.0046$), demonstrating that its amino acid sequence has been preserved under extraordinary selective constraint. In biological signaling networks, high-threshold sentinels are frequently uncoupled from constitutive interactomes to prevent spurious pathway activation during basal conditions. We propose that *OSCA2.3* functions as an emergency high-threshold mechanosensor that remains dormant under mild osmotic fluctuations, gating calcium influx only when membrane tension reaches near-lethal mechanical extremes.

In Clade OSCA3+4, HyPhy Contrast-FEL analysis identified a dramatic accelerated hotspot at Local Site 593 in *V. tubiflora* ($\beta_{Test} = 24.72, p = 0.0085$; Table 2). While the surrounding OSCA3+4 clade experienced global selection relaxation, this specific residue underwent extreme nonsynonymous substitution in the resurrection plant. Structural modeling of OSCA channels indicates that residues in this region map to intracellular gating loops connecting the transmembrane pore helices (Zhang et al., 2018). We hypothesize that Site 593 represents a specialized adaptive modification that facilitates rapid channel gating during the explosive influx of water upon rehydration. When desiccated resurrection plants are exposed to rain, cellular rehydration induces rapid osmotic swelling and intense outward membrane tension (Vieira et al., 2022; Oliver et al., 2020). An accelerated, structurally flexible gating residue at Site 593 could enable *VtOSCA3/4* channels to open instantaneously upon rehydration, mediating the rapid calcium transients required to trigger rehydration-associated repair mechanisms.

### 4.7 Biotechnological Translation: Engineering Stress-Responsive Dynamic Gating in Agricultural Crops

The insights generated by the Dual-Track Evolutionary Model provide clear guidelines for engineering drought resilience in agricultural crops. Previous biotechnological attempts to improve drought tolerance in staple monocots (e.g., maize, rice, wheat) frequently focused on constitutive overexpression of baseline osmosensors or downstream stress transcription factors, often resulting in pleiotropic penalties such as stunted vegetative growth or reduced grain yield (Cao et al., 2020; Lamers et al., 2020). 

Our evolutionary findings demonstrate that baseline Clade 1 osmosensors are already evolutionarily canalized and operating under near-maximal purifying constraint across angiosperms. Consequently, attempting to engineer crop resilience by overexpressing invariant baseline channels like *OSCA1.1* or *OSCA1.2* risks disrupting essential developmental calcium signaling and vascular transport. Instead, biotechnological efforts should target the modulatory Clades OSCA2 and OSCA3+4, which display natural evolutionary plasticity and capacity for functional fine-tuning. Specifically, the 14 Contrast-FEL diversifying codon sites identified in Clade OSCA2 (Table 2) provide precise targets for site-directed mutagenesis to modulate channel opening thresholds in crops. Furthermore, engineering synthetic promoters that combine oxidative-responsive ARE elements and light-responsive G-boxes—mirroring the subfunctionalized promoter architecture of *VpOSCA2.4a/b*—could allow crops to dynamically upregulate mechanosensitive channel expression specifically during peak midday stress without perturbing baseline growth under irrigated conditions.

---

## 5. CONCLUSION

This investigation provides a comprehensive chromosome-scale comparative analysis of the OSCA mechanosensitive calcium channel family in extremophyte resurrection and evergreen monocots. Our empirical findings demonstrate that the macroevolutionary transition to desiccation tolerance in Velloziaceae did not require wholesale expansion of the primary osmosensory repertoire, but operated through the establishment of a **Dual-Track Evolutionary Model**. Under this model, the primary OSCA1 sensory core remained canalized under invariant purifying selection ($K = 0.9215$), preserving ancestral root and vascular transcript enrichment alongside an immutable 18-interactor protein hub centered on *OSCA1.2*. Concurrently, the modulatory OSCA2 and OSCA3+4 subfamilies diverged profoundly: *Vellozia tubiflora* experienced massive selection relaxation ($K = 0.2828$ and $K = 0.1349$) driven by the suspension of functional constraints during anhydrobiotic metabolic dormancy, while *Vellozia peripherica* actively diversified its modulatory channels via 14 accelerated Contrast-FEL codon sites and a lineage-specific tandem duplication (*VpOSCA2.4a/b*) that facilitated *cis*-regulatory subfunctionalization between oxidative stress and photoperiodic signaling. By identifying conserved vascular hubs, silent high-threshold sentinels, and localized gating hotspots such as Site 593, this study deciphers the evolutionary and regulatory principles governing mechanosensation in extremophytes, providing rational molecular targets for engineering climate-resilient crops.

---

## 6. FIGURES AND FIGURE LEGENDS

**Figure 1. Maximum-likelihood phylogenetic reconstruction of the OSCA gene family across angiosperms.**  
Unrooted circular cladogram inferred using IQ-TREE v2.4.0 under the empirical Q.plant+F+R5 substitution model with 1,000 Ultrafast Bootstrap (UFBoot2) and SH-aLRT replicates. The phylogeny incorporates 76 full-length protein sequences from *Vellozia peripherica* (14 loci, purple), *Vellozia tubiflora* (13 loci, orange), *Arabidopsis thaliana* (15 loci), *Oryza sativa* (11 loci), *Sorghum bicolor* (11 loci), and *Zea mays* (12 loci). Branch arcs demarcate the four canonical angiosperm subfamilies: Clade OSCA1 (green), Clade OSCA2 (blue), Clade OSCA3 (red), and Clade OSCA4 (yellow). Bootstrap support values $\ge 95\%$ for major lineage divergences and orthologous pairs are indicated at internal nodes. Note the monophyletic placement of the OSCA2.4 subclade on chromosome 1A, resolving *VpOSCA2.4b* as the direct cross-species sister to *VtOSCA2.4* (83% support) and *VpOSCA2.4a* as a lineage-specific tandem duplicate.

**Figure 2. Site-specific selective divergence across OSCA subfamilies (Contrast-FEL).**  
Lollipop distribution of statistically significant codon positions ($p \le 0.05$) identified by HyPhy Contrast-FEL following gap sanitation. Codon positions along the horizontal axis are indexed to local subfamily alignments. The vertical axis indicates the nonsynonymous substitution rate in the Test lineage ($\beta_{Test}$, *V. tubiflora*, orange) and the Reference lineage ($\beta_{Ref}$, *V. peripherica*, purple). Panel A depicts Clade OSCA1, highlighting localized divergence at sites 181 and 710 in *V. tubiflora* alongside sites 252, 430, and 973 in *V. peripherica*. Panel B depicts Clade OSCA2, showing 14 significant sites displaying 100% unidirectional selective acceleration in *V. peripherica* ($\beta_{Ref} \gg 0, \beta_{Test} \approx 0$). Panel C depicts Clade OSCA3+4, highlighting the prominent accelerated gating hotspot at Local Site 593 in *V. tubiflora* ($\beta_{Test} = 24.72, p = 0.0085$).

---

## 7. REFERENCES

ALCANTARA, S.; MELLO-SILVA, R.; TEODORO, G. S.; DREQUECELER, K.; ACKERLY, D. D.; OLIVEIRA, R. S. Carbon assimilation and habitat segregation in resurrection plants: a comparison between desiccation- and non-desiccation-tolerant species of Neotropical Velloziaceae (Pandanales). **Functional Ecology**, v. 29, n. 12, p. 1499–1512, 2015. https://doi.org/10.1111/1365-2435.12462

ALCANTARA, S.; REE, R. H.; MELLO-SILVA, R. Accelerated diversification and functional trait evolution in Velloziaceae reveal new insights into the origins of the *campos rupestres*’ exceptional floristic richness. **Annals of Botany**, v. 122, n. 1, p. 165–180, 2018. https://doi.org/10.1093/aob/mcy063

BACETE, L.; SCHULZ, J.; ENGELSDORF, T. et al. THESEUS1 modulates cell wall stiffness and abscisic acid production in *Arabidopsis thaliana*. **Proceedings of the National Academy of Sciences USA**, v. 119, n. 1, p. e2119258119, 2022. https://doi.org/10.1073/pnas.2119258119

BASU, D.; HASWELL, E. S. Plant mechanosensitive ion channels: an ocean of possibilities. **Current Opinion in Plant Biology**, v. 40, p. 43–48, 2017. https://doi.org/10.1016/j.pbi.2017.07.002

CAO, L.; ZHANG, P.; LU, X. et al. Systematic analysis of the maize *OSCA* genes revealing *ZmOSCA* family members involved in osmotic stress and *ZmOSCA2.4* confers enhanced drought tolerance in transgenic *Arabidopsis*. **International Journal of Molecular Sciences**, v. 21, n. 1, p. 351, 2020. https://doi.org/10.3390/ijms21010351

CHEN, J.; YU, F.; LIU, Y. et al. FERONIA interacts with ABI2-type phosphatases to facilitate signaling cross-talk between abscisic acid and RALF peptide in *Arabidopsis*. **Proceedings of the National Academy of Sciences USA**, v. 113, n. 37, p. E5519–E5527, 2016. https://doi.org/10.1073/pnas.1608449113

COSTA, M. C. D.; ARTUR, M. A. S.; MAIA, J. et al. A footprint of desiccation tolerance in the genome of the resurrection plant *Xerophyta viscosa*. **Nature Plants**, v. 3, n. 4, p. 17038, 2017. https://doi.org/10.1038/nplants.2017.38

FARRANT, J. M.; BRANDT, W.; LINDSEY, G. G. An overview of mechanisms of desiccation tolerance in selected angiosperm resurrection plants. In: JENKS, M. A.; WOOD, A. J. (Eds.). **Plant Desiccation Tolerance**. Oxford: Blackwell Publishing, 2007. p. 51–84.

FENG, W.; KITA, D.; PEAUCELLE, A. et al. The FERONIA receptor kinase maintains cell-wall integrity during salt stress through $\text{Ca}^{2+}$ signaling. **Current Biology**, v. 28, n. 5, p. 666–675, 2018. https://doi.org/10.1016/j.cub.2018.01.023

FERNANDES, G. W.; ARANTES-GARCIA, L.; BARBOSA, M. et al. Biodiversity and ecosystem services in the *Campo Rupestre*: a road map for the sustainability of the hottest Brazilian biodiversity hotspot. **Perspectives in Ecology and Conservation**, v. 18, n. 4, p. 213–222, 2020. https://doi.org/10.1016/j.pecon.2020.10.004

GORGUES, L.; LI, X.; MAUREL, C.; MARTINIÈRE, A.; NACRY, P. Root osmotic sensing from local perception to systemic responses. **Stress Biology**, v. 2, n. 1, p. 38, 2022. https://doi.org/10.1007/s44154-022-00054-1

HANADA, K.; ZOU, C.; LEHTI-SHIU, M. D.; SHINOZAKI, K.; SHIU, S.-H. Importance of lineage-specific expansion of plant tandem duplicates in the adaptive response to environmental stimuli. **Plant Physiology**, v. 148, n. 2, p. 993–1003, 2008. https://doi.org/10.1104/pp.108.122457

HARTMANN, F. P.; TINTURIER, E.; JULIEN, J.-L.; LEBLANC-FOURNIER, N. Between stress and response: function and localization of mechanosensitive $\text{Ca}^{2+}$ channels in herbaceous and perennial plants. **International Journal of Molecular Sciences**, v. 22, n. 20, p. 11043, 2021. https://doi.org/10.3390/ijms222011043

KAUR, A.; MADHU; UPADHYAY, S. K. Mechanosensitive ion channels in plants. In: UPADHYAY, S. K. (Ed.). **Plant Ion Channels and Transporters**. Singapore: Springer, 2021. p. 325–347. https://doi.org/10.1007/978-981-16-1677-8_16

KETEHOULI, T.; CARVALHO, F. E. L.; DAI, S.; WANG, J. Mechanisms of calcium signaling in plant responses to abiotic stress. **Frontiers in Plant Science**, v. 13, p. 953434, 2022. https://doi.org/10.3389/fpls.2022.953434

KUMAR, M. N.; VERSLUES, P. E. Role of the putative osmosensor Arabidopsis Histidine Kinase1 in dehydration avoidance and low-water-potential response. **Plant Physiology**, v. 161, n. 2, p. 942–953, 2013. https://doi.org/10.1104/pp.112.209791

KURUSU, T.; KUCHITSU, K.; NAKANO, M.; NAKAYAMA, Y.; IIDA, H. Plant mechanosensing and $\text{Ca}^{2+}$ transport. **Trends in Plant Science**, v. 18, n. 4, p. 227–233, 2013. https://doi.org/10.1016/j.tplants.2012.12.002

LAMERS, J.; VAN DER MEER, T.; TESTERINK, C. How plants sense and respond to stressful environments. **Plant Physiology**, v. 182, n. 4, p. 1624–1635, 2020. https://doi.org/10.1104/pp.19.01464

LI, Y.; YUAN, F.; WEN, Z. et al. Genome-wide survey and expression analysis of the *OSCA* gene family in rice (*Oryza sativa* L.). **BMC Plant Biology**, v. 15, p. 261, 2015. https://doi.org/10.1186/s12870-015-0653-8

LIU, C.; WANG, H.; ZHANG, Y. et al. Systematic characterization of the OSCA family members in soybean and validation of their functions in osmotic stress. **International Journal of Molecular Sciences**, v. 23, n. 18, p. 10570, 2022. https://doi.org/10.3390/ijms231810570

LIU, X.; WANG, J.; SUN, L. Structure of the hyperosmolality-gated calcium-permeable channel OSCA1.2. **Nature Communications**, v. 9, p. 5060, 2018. https://doi.org/10.1038/s41467-018-07564-5

MAKSAEV, G.; HASWELL, E. S. MscS-Like10 is a stretch-activated ion channel from *Arabidopsis thaliana* with a preference for anions. **Proceedings of the National Academy of Sciences USA**, v. 109, n. 46, p. 19015–19020, 2012. https://doi.org/10.1073/pnas.1213931109

MELLO-SILVA, R.; SANTOS, D. Y. A. C.; SALATINO, M. L. F. et al. Five vicarious genera from Gondwana: the Velloziaceae as shown by molecules and morphology. **Annals of Botany**, v. 108, n. 1, p. 87–102, 2011. https://doi.org/10.1093/aob/mcr107

NAKAGAWA, Y.; KATAGIRI, T.; SHINOZAKI, K. et al. Arabidopsis *MCA1* complements the yeast *mid1* mutation and functions in mechanosensing in plant cells. **The Plant Journal**, v. 51, n. 4, p. 579–588, 2007. https://doi.org/10.1111/j.1365-313X.2007.03158.x

OLIVER, M. J.; FARRANT, J. M.; HILHORST, H. W. M.; MUNDREE, S.; RADERMACHER, A. M. Desiccation tolerance in resurrection plants: the molecular mechanisms underpinning anhydrobiosis. **Annual Review of Plant Biology**, v. 71, p. 589–616, 2020. https://doi.org/10.1146/annurev-arplant-050718-100216

SILVEIRA, F. A. O.; NEGREIROS, D.; BARBOSA, N. P. U. et al. Ecology and evolution of plant diversity in the endangered *campo rupestre*: a neglected conservation hotspot. **Plant and Soil**, v. 403, n. 1-2, p. 129–152, 2016. https://doi.org/10.1007/s11104-015-2637-8

THOR, K.; JIANG, S.; MICHARD, E. et al. The calcium-permeable channel OSCA1.3 regulates plant stomatal immunity. **Nature**, v. 585, n. 7826, p. 569–573, 2020. https://doi.org/10.1038/s41586-020-2702-1

TRAN, L.-S. P.; URAO, T.; QIN, F. et al. Functional analysis of *AHK1/ATHK1* and its involvement in osmotic stress response in *Arabidopsis*. **Proceedings of the National Academy of Sciences USA**, v. 104, n. 39, p. 15566–15571, 2007. https://doi.org/10.1073/pnas.0706547104

VIEIRA, E. A.; SILVA, K. R.; ROSSI, M. L.; MARTINELLI, A. P.; GASPAR, M.; BRAGA, M. R. Water retention and metabolic changes improve desiccation tolerance in *Barbacenia graminifolia* (*Velloziaceae*). **Physiologia Plantarum**, v. 174, n. 5, p. e13783, 2022. https://doi.org/10.1111/ppl.13783

WHITE, P. J. Calcium in plants. **Annals of Botany**, v. 92, n. 4, p. 487–511, 2003. https://doi.org/10.1093/aob/mcg164

WOLF, S.; HÉMATY, K.; HÖFTE, H. Sensing and responding to the plant cell wall: a tracking system for growth and defense. **Annual Review of Plant Biology**, v. 63, p. 381–407, 2012. https://doi.org/10.1146/annurev-arplant-042811-105544

YAMANAKA, T.; NAKAGAWA, Y.; MORI, K. et al. *MCA1* and *MCA2* that mediate $\text{Ca}^{2+}$ uptake have distinct and overlapping roles in *Arabidopsis*. **Plant Physiology**, v. 152, n. 3, p. 1284–1296, 2010. https://doi.org/10.1104/pp.109.147371

YANG, Z.; NIELSEN, R. Estimating synonymous and nonsynonymous substitution rates under realistic models of codon substitution. **Molecular Biology and Evolution**, v. 17, n. 1, p. 32–43, 2000. https://doi.org/10.1093/oxfordjournals.molbev.a026236

YUAN, F.; YANG, H.; XUE, Y. et al. *OSCA1* mediates osmotic-stress-evoked $\text{Ca}^{2+}$ increases vital for osmosensing in *Arabidopsis*. **Nature**, v. 514, n. 7522, p. 367–371, 2014. https://doi.org/10.1038/nature13593

ZHAI, Y.; WEN, Z.; HAN, Y. et al. Heterogeneous expression of plasma-membrane-localised *OsOSCA1.4* complements osmotic sensing based on hyperosmolality and salt stress in *Arabidopsis osca1* mutant. **Cell Calcium**, v. 91, p. 102261, 2020. https://doi.org/10.1016/j.ceca.2020.102261

ZHANG, M.; WANG, D.; KANG, Y. et al. Structure of the mechanosensitive OSCA channels. **Nature Structural & Molecular Biology**, v. 25, n. 9, p. 850–858, 2018. https://doi.org/10.1038/s41594-018-0117-6

