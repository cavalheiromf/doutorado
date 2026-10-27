# Genome-Wide Identification, Comparative Synteny, and Evolutionary Divergence of OSCA Mechanosensitive Ion Channels in Resurrection and Evergreen *Vellozia*

**Mariana Feitosa Cavalheiro**$^{1,2}$, **Isabel Rodrigues Gerhardt**$^{2,3,*}$

$^{1}$ Graduate Program in Genetics and Molecular Biology, Institute of Biology, University of Campinas (UNICAMP), Campinas, SP, Brazil  
$^{2}$ Brazilian Biosciences National Laboratory (LNBio), Brazilian Center for Research in Energy and Materials (CNPEM), Campinas, SP, Brazil  
$^{3}$ Center for Molecular Biology and Genetic Engineering (CBMEG), University of Campinas (UNICAMP), Campinas, SP, Brazil  

$^*$**Corresponding author:** Isabel Rodrigues Gerhardt (isabel.gerhardt@unicamp.br / isabel.gerhardt@embrapa.br)

---

## Abstract

**Background:** OSCA/TMEM63 ion channels mediate primary osmotic and mechanical perception in plants. Their evolution in congeneric lineages with contrasting water-deficit adaptations remains unexplored. **Objective:** We tested whether OSCA channel repertoires diverged between desiccation-tolerant *Vellozia tubiflora* and evergreen *Vellozia peripherica*. **Methods:** Genomic comparisons evaluated gene duplications, macrosynteny, pairwise evolutionary rates, ortholog-set selection intensity, basal tissue transcript abundance, functional networks, and promoter architectures. We used HMMER/InterProScan searches, maximum-likelihood phylogenetics (IQ-TREE), syntenic collinearity (MCScan), and pairwise substitution rates (PAML YN00). We evaluated selection intensity across the analyzed OSCA ortholog set (HyPhy RELAX), tissue RNA-seq profiles (DESeq2), functional networks (STRING v12), and upstream *cis*-element annotation (PlantCARE). **Results:** Fourteen loci were identified in *V. peripherica* and 13 in *V. tubiflora* across four canonical clades (OSCA1-4). Twenty-five of the 27 *Vellozia* proteins displayed the tripartite Pfam domain architecture, whereas *VpOSCA2.2* and *VtOSCA1.2* were short predicted models lacking PF13967. Macrosynteny revealed high collinearity, with two adjacent *OSCA2.4* loci in *V. peripherica* and one in *V. tubiflora*. HyPhy RELAX estimated a selection intensity parameter *K* = 0.7064 (*p* = 0.0003), indicative of relaxed selection constraint along *V. tubiflora* test branches relative to *V. peripherica* reference branches under the tested codon model. *OSCA1.2* transcripts were consistently more abundant in roots and stems than in leaves in both species. They also had high connectivity in STRING functional-association networks, including predicted links to carbohydrate-metabolism proteins. **Conclusion:** Broad conservation of the OSCA repertoire coexists with differences in copy number, selection intensity, and basal transcript abundance. These patterns provide a framework for testing whether such divergence contributes to contrasting drought adaptations in *Vellozia*.

**Keywords:** Velloziaceae, mechanosensation, OSCA channels, desiccation tolerance, comparative synteny, purifying selection, tandem duplication, *campos rupestres*.

## 1. INTRODUCTION

Because water availability varies across spatial and temporal scales, plants continuously adjust cellular growth and tissue turgor to fluctuating hydration states (FENG et al., 2016). During dehydration, transpirational water loss diminishes cell volume and hydrostatic pressure, altering the physical interface between the plasma membrane and the cell wall while generating mechanical tension across the lipid bilayer (FRACHISSE et al., 2014). Early mechanical perturbations of membrane tension develop within seconds of water loss, preceding downstream transcriptional cascades and metabolic adjustments that unfold over minutes to hours (HASWELL; VERSLUES, 2015). At the cellular level, the rapid perception of bilayer deformation directly triggers immediate biophysical responses, predominantly cytosolic calcium transients and ionic fluxes (BASU; HASWELL, 2017). These early ionic signals operate upstream of, and integrate with, broader physiological adaptations to water deficit, including phytohormone signaling, stomatal regulation, and osmotic adjustment (ZHU, 2016). In land plants, this primary sensory layer is mediated in part by mechanosensitive and osmosensitive ion channels that convert physical membrane tension into rapid ion conductances.

Among plant mechanotransducers, the hyperosmolality-gated calcium-permeable channel (OSCA) family represents a principal sensory conduit. In *Arabidopsis thaliana*, *OSCA1.1* mediates hyperosmolality-induced cytosolic calcium increases (YUAN et al., 2014), and broader electrophysiological surveys have established that multiple OSCA/TMEM63 homologs operate as bona fide stretch-activated ion channels across eukaryotic lineages (MURTHY et al., 2018). Structural determinations of *Arabidopsis* *OSCA1.1* and *OSCA1.2* demonstrate that functional channels assemble as homodimers, with each subunit containing eleven transmembrane helices including an uncoupled peripheral helix (TM0). Based on these architectural features, structural models propose that interactions between cytosolic domains and lipid-interfacing elements couple bilayer deformation to conformational rearrangements at the ion-permeation pore (LIU; WANG; SUN, 2018; ZHANG et al., 2018). At the sequence level, this conserved channel architecture is defined by three canonical Pfam domain signatures (PF02714, PF13967, and PF14703), while phylogenetic surveys across angiosperms partition the family into four ancient clades (OSCA1-4) characterized by distinct activation thresholds, ion selectivities, and spatial expression profiles (YUAN et al., 2014; DING et al., 2019; YIN et al., 2021; KE et al., 2022).

Like other plant multigene families, the evolutionary dynamics of these channel clades reflect a balance between functional constraint on essential cellular roles and lineage-specific copy-number turnover (FLAGEL; WENDEL, 2009). Under this framework, core mechanosensory channel orthologs mediating baseline cellular perception are expected to evolve under purifying selection, whereas gene duplication provides raw material for potential evolutionary diversification (PANCHY; LEHTI-SHIU; SHIU, 2016). Retained paralogs may subsequently undergo selective relaxation, organ-specific expression divergence, or *cis*-regulatory subfunctionalization (LYNCH; FORCE, 2000), thereby modulating channel density, tissue allocation, or responsiveness to environmental stimuli. Investigating how channel repertoires evolve across syntenic genomic contexts, selective regimes, and regulatory architectures provides an empirical framework to test whether extreme ecological divergence, such as vegetative desiccation tolerance, reshapes primary sensory systems or preserves deeply conserved mechanosensory constraints.

The monocot family Velloziaceae provides a compelling system to evaluate sensory-channel evolution under contrasting hydrological regimes. Prominent across the *campos rupestres*, nutrient-poor rocky outcrops of eastern Brazil where shallow soils, intense solar radiation, and a pronounced dry season impose recurrent water limitation (ALCANTARA et al., 2015; VIEIRA et al., 2025), Velloziaceae species have diversified across two primary dry-season strategies: dehydration avoidance, which limits water loss while maintaining physiological activity, and vegetative desiccation tolerance, which enables survival of extensive tissue dehydration and metabolic recovery after rehydration (ALCANTARA et al., 2015; DE FREITAS LAROCCA et al., 2022). Physiological comparisons further show that desiccation tolerance permits survival under extreme water loss but entails distinct costs and seasonal adjustments in carbon assimilation, growth, and metabolism (TEODORO et al., 2021; VIEIRA et al., 2025). Within *Vellozia*, *Vellozia tubiflora* is a desiccation-tolerant resurrection species, whereas *Vellozia peripherica* is an evergreen, non-desiccation-tolerant species that relies on dehydration avoidance. Previously established as a congeneric model of contrasting drought-adaptation strategies in seasonal microbiome analyses (PINTO et al., 2025), this species pair provides a well-defined comparative system to test whether mechanosensory channel repertoires vary with water-deficit strategy.

This ecological divergence raises a central question about primary cellular perception: how does mechanosensory machinery evolve in closely related plants with opposing strategies for managing severe water deficit? On one hand, because both resurrection and evergreen plants must monitor cellular turgor and osmotic fluctuations during vegetative growth, we hypothesize that baseline sensory demands could maintain the core OSCA repertoire under purifying selection across both lineages. On the other hand, vegetative desiccation tolerance imposes severe cellular shrinkage and profound mechanical strain on the protoplast during drying and rehydration, stresses that resurrection plants mitigate through diverse, species-specific cellular mechanisms such as wall folding, vacuolar fragmentation, or chemical vitrification (FARRANT et al., 2015; LYALL; GECHEV, 2020; VIEIRA et al., 2022). These distinct biomechanical demands could favor lineage-specific copy retention, shifts in selective constraint, or specialized transcriptional regulation in particular OSCA clades.

To evaluate these hypotheses, we tested whether the divergence between dehydration avoidance and desiccation tolerance coincides with structural or regulatory differences in the primary mechanosensory machinery by comparing the genome-wide OSCA gene-family repertoires of *V. tubiflora* and *V. peripherica*. Across chromosome-scale assemblies, we assessed six complementary features: gene-copy history, macrosyntenic collinearity, clade-specific selective constraints, basal tissue transcript abundance, predicted functional-association networks, and upstream *cis*-regulatory motif repertoires. By integrating these genomic and evolutionary layers, we characterized patterns of conservation and divergence in the OSCA family between resurrection and evergreen *Vellozia*.

## 2. MATERIAL AND METHODS

### 2.1 Genome resources, candidate identification, and sequence validation

Chromosome-scale haplotype-A assemblies and predicted proteomes of *V. peripherica* and *V. tubiflora* were used, alongside the predicted proteome of the sister taxon *Xerophyta schlechteri* (COSTA et al., 2017). OSCA candidates were identified across all three proteomes with HMMER v3.4 hmmsearch using the PF02714 (RSN1_7TM) profile (EDDY, 2011). For loci with alternative isoforms, the protein encoded by the longest transcript was retained. Candidate sequences were subsequently evaluated for domain composition using the PF13967 and PF14703 profiles and annotated with InterProScan to verify assignment to the PANTHER PTHR13018 family. Transmembrane segments were predicted using TMHMM Server v.2.0 (KROGH et al., 2001; https://services.healthtech.dtu.dk/services/TMHMM-2.0/). Molecular mass and theoretical isoelectric point were calculated with Biopython (COCK et al., 2009).

### 2.2 Phylogenetic reconstruction and clade assignment

To reconstruct evolutionary relationships and establish clade designations, a phylogenetic dataset was assembled comprising 84 OSCA protein sequences, including the 27 identified *Vellozia* candidates, eight *X. schlechteri* loci, and canonical reference models from *Arabidopsis thaliana*, *Oryza sativa*, *Sorghum bicolor*, and *Zea mays*. Sequences were aligned with MAFFT v7 under default settings (KATOH; ROZEWICKI; YAMADA, 2019). Maximum-likelihood inference was conducted in IQ-TREE v3.0.1 (MINH et al., 2020) under the Q.PLANT+R5 substitution model selected by ModelFinder according to the Bayesian information criterion. Branch support was evaluated with 1,000 ultrafast bootstrap replicates (HOANG et al., 2018). The resulting circular cladogram topology was formatted and visualized using Interactive Tree Of Life (iTOL) v5 (LETUNIC; BORK, 2021).

### 2.3 Chromosomal location and interspecific synteny

OSCA gene coordinates were obtained from the GFF3 annotation of each haplotype-A assembly. Interspecific collinearity between *V. peripherica* and *V. tubiflora* was inferred from coding-sequence and GFF3-derived BED files using the Python implementation of MCScan in JCVI v1.6.5 with LAST-backed default parameters (TANG et al., 2008). The resulting anchor table was filtered to identify pairs in which both endpoints belonged to the curated OSCA gene set. Chromosome correspondence and gene identity were retained to distinguish interspecific anchors from matches involving tandem paralogs. Local gene order, intergenic distances, and flanking collinear genes were then examined for the OSCA1 cluster on chromosome 7A and the *OSCA2.4* region on chromosome 1A. Macrosynteny and local collinearity were visualized using JCVI synteny scripts.

### 2.4 Pairwise evolutionary rates and ortholog-set selection intensity

To quantify baseline selective pressures for each interspecific OSCA pair, protein alignments and their corresponding coding sequences were converted into codon alignments using PAL2NAL v14 (SUYAMA; TORRENTS; BORK, 2006), and nonsynonymous (*K*~a~) and synonymous (*K*~s~) substitution rates were estimated with the Yang-Nielsen method in PAML YN00 (YANG; NIELSEN, 2000; YANG, 2007) (Supplementary Table S3).

Lineage-specific shifts in selection intensity across the analyzed *Vellozia* OSCA ortholog set were evaluated using RELAX in HyPhy v2.5.99 (KOSAKOVSKY POND et al., 2020) under the MG94xREV codon substitution model (WERTHEIM et al., 2015). The analysis incorporated all 27 identified OSCA coding sequences across both species, comprising 14 loci from *V. peripherica* and 13 from *V. tubiflora*, which encompass 12 single-copy ortholog pairs alongside the tandemly duplicated *VpOSCA2.4a/b* paralogs paired with *VtOSCA2.4*. Protein sequences of all 27 loci were aligned and converted into a multiple codon alignment using PAL2NAL v14, excluding alignment columns with gaps in >20% of sequences (Supplementary Table S4). The analysis was conditioned on the 27-tip maximum-likelihood gene-tree topology connecting these loci, where all 13 terminal branches of the desiccation-tolerant specialist (*V. tubiflora*) were designated as the Test set, and all 14 terminal branches of the evergreen congener (*V. peripherica*) were designated as the Reference set (WIBERG; BRAND; SCHÄRER, 2021). Under this formulation, RELAX tests whether the distribution of nonsynonymous-to-synonymous rate ratios (ω) on Test branches is systematically contracted toward neutrality (ω = 1; *K* < 1, indicating relaxed selection) or expanded away from neutrality (*K* > 1, indicating intensified selection) relative to Reference branches using a likelihood ratio test (2Δln *L* ~ χ^{2}_{1}).

### 2.5 Plant sampling, RNA sequencing, and basal tissue transcript abundance

One population of each focal species was sampled from *campos rupestres* on private property adjacent to Serra da Canastra National Park, Delfinópolis, Minas Gerais, Brazil: *V. peripherica* at 20°29′07.2″S, 46°30′49.8″W (1,002 m elevation) and *V. tubiflora* at 20°29′15.8″S, 46°32′05.3″W (950 m elevation), located approximately 2.3 km apart. All individuals analyzed in this study originated from these two populations.

To establish baseline expression profiles, unstressed leaf, stem, and root tissues were sampled from three biological individuals per species, immediately flash-frozen in liquid nitrogen, and stored at −80 °C. Following total RNA extraction via a CTAB protocol (CHANG; PURYEAR; CAIRNEY, 1993), poly(A)-selected, paired-end Illumina libraries were sequenced at a target depth of approximately 30 million reads per library. Transcript abundance was quantified by aligning reads to the respective haplotype-A genome assemblies using STAR v2.7.11b (DOBIN et al., 2013). The final dataset comprised nine libraries for *V. peripherica* and eight for *V. tubiflora* (owing to the exclusion of one failed root library).

To characterize spatial expression profiles, transcript abundance was compared among roots, stems, and leaves using DESeq2 (LOVE; HUBER; ANDERS, 2014). Each species was analyzed independently using a statistical design that included biological individual as a blocking factor to account for intraspecific variation. After filtering low-expressed genes and applying median-of-ratios normalization, pairwise tissue contrasts were assessed via Wald tests, with significant differential abundance defined by a Benjamini-Hochberg adjusted *p*-value < 0.05.

### 2.6 STRING functional-association networks and enrichment analysis

To infer the functional contexts of the OSCA channels, the deduced protein sequences of *Vellozia* OSCA channels were analyzed using the STRING v12 REST API (SZKLARCZYK et al., 2023). Predicted proteomes of *V. peripherica* and *V. tubiflora* were mapped into STRING v12 under custom organism identifiers (STRG0A77QVI and STRG0A11TDW, respectively), which transfer functional associations from reference plant networks (principally *Arabidopsis thaliana*, NCBI taxon ID 3702, and *Oryza sativa*, NCBI taxon ID 4530) via STRING's automated orthology pipeline based on eggNOG orthologous groups and all-against-all sequence alignments. Queries were executed separately for each species using the canonical transcript identifiers of the identified OSCA loci (14 in *V. peripherica* and 13 in *V. tubiflora*). Networks were generated using the functional network mode (network_type = "functional"), where edges represent integrated functional associations (including co-expression, shared genomic context, automated text-mining, and homology transfer) rather than strictly physical protein-protein interactions. We retrieved edges meeting a medium-confidence threshold (combined score ≥ 0.400) and allowed the addition of up to 50 interactor nodes per species network (add_nodes = 50) to capture the extended regulatory environment connecting queried channels. The resulting species-specific interactomes were modeled as undirected graphs to extract key topological metrics, including node degree, connected components, and unweighted clustering coefficients, in NetworkX (HAGBERG; SCHULT; SWART, 2008). Finally, to identify biological pathways and Gene Ontology terms overrepresented across all connected network nodes, interacting proteins were analyzed via the STRING functional annotation and enrichment endpoints, retaining terms with a false discovery rate below 0.05.

### 2.7 Upstream *cis*-element annotation

To characterize the *cis*-regulatory architecture of the OSCA family, transcript coordinates were retrieved from the genomic annotations of both *Vellozia* species. A 2,000-bp promoter region immediately upstream of each annotated transcript boundary was extracted in a strand-specific manner using BEDTools v2.30.0 (QUINLAN; HALL, 2010). Putative *cis*-regulatory elements within these regions were then identified by querying the PlantCARE database (LESCOT et al., 2002). To resolve database redundancies, orthographic variants of identical motif families (e.g., G-box, MYC, and MYB) were normalized, and overlapping coordinates for the same motif class were merged into single non-redundant occurrences. Curated motifs were classified into five functional categories (Supplementary Table S7) following the framework of QU et al. (2019): core promoter elements (TATA-box and CAAT-box), light responsiveness, growth and development, phytohormone signaling (abscisic acid, methyl jasmonate, and salicylic acid), and abiotic stress response (drought, low temperature, anaerobic induction, and defense/wounding).

## 3. RESULTS

### 3.1 OSCA gene set, predicted architecture, and phylogenetic placement

Profile searches and domain curation identified 27 OSCA loci across the two focal genomes, comprising 14 in *V. peripherica* and 13 in *V. tubiflora*, alongside eight loci identified in the sister outgroup *X. schlechteri* (Figure 1; Supplementary Table S1). Both *Vellozia* species contained five OSCA1 loci, two OSCA3 loci, and one OSCA4 locus. The difference in total family size occurred within OSCA2, which included six loci in *V. peripherica* and five in *V. tubiflora*. Each candidate retained the PANTHER PTHR13018 assignment and the PF02714 and PF14703 domains.

Among the 27 *Vellozia* OSCA proteins, 25 also contained PF13967 and therefore showed the complete three-domain combination recovered for most of the family. The exceptions were *VpOSCA2.2* and *VtOSCA1.2*. These sequences were 478 and 485 amino acids long, respectively, whereas most identified OSCA proteins ranged from 634 to 869 amino acids, and both lacked a saved PF13967 hit. Their reduced length was accompanied by fewer predicted transmembrane segments, with TMHMM returning six for *VpOSCA2.2* and five for *VtOSCA1.2* (Figure 1B,C; Supplementary Table S1). Across the complete OSCA gene set, TMHMM counts ranged from five to 12, indicating that baseline predictions do not support a uniform count of eleven helices across all 27 gene models. Although consistent RNA-seq read coverage across annotated exons confirms that both loci are actively expressed, short-read mappings alone cannot verify full-length transcript continuity or formally exclude misannotated splice junctions and assembly artifacts. Consequently, targeted full-length cDNA sequencing remains necessary to determine whether these shortened models reflect genuine biologically truncated channels or bioinformatic annotation errors. Domain validation in the sister outgroup *X. schlechteri* confirmed that all eight identified loci retained all three canonical Pfam domain signatures (PF13967, PF14703, and PF02714; Supplementary Table S1).

Molecular masses ranged from 54.42 to 100.53 kDa, largely tracking predicted sequence length. Theoretical isoelectric points were generally basic, although *OSCA4.1* in both species showed lower values of 6.55 and 6.52.

The maximum-likelihood tree placed the *Vellozia* sequences within the four established OSCA clades alongside the *X. schlechteri* outgroup and angiosperm references (Figure 1A). Across the 27 *Vellozia* proteins, 12 interspecific ortholog pairs resolved as reciprocally monophyletic one-to-one pairs (*OSCA1.1*, *OSCA1.2*, *OSCA1.3*, *OSCA1.4*, *OSCA1.5*, *OSCA2.1*, *OSCA2.2*, *OSCA2.3*, *OSCA2.5*, *OSCA3.1*, *OSCA3.2*, and *OSCA4.1*), with 11 pairs supported by ultrafast bootstrap values ≥ 99% and *OSCA1.4* nested within the chromosome 7A *OSCA1.3*/1.4/1.5 cluster (UFBoot = 100%). Within the remaining orthologous group (*OSCA2.4*), the two *V. peripherica* sequences and the single *V. tubiflora* sequence formed a monophyletic clade (UFBoot = 100%) sister to *XsOSCA2.4*. The topology resolved the canonical four-clade architecture rooted between Clade OSCA1 and Clades OSCA2-4.

Taken together, OSCA gene-set size and phylogenetic placement established a conserved family framework across both genomes: the two species differed by a single locus, retained representatives of all four canonical clades, and resolved 12 one-to-one orthologous pairs alongside the 2:1 *OSCA2.4* orthogroup. The two shortened gene models (*VpOSCA2.2* and *VtOSCA1.2*) represented locus-specific architectural variations rather than clade loss.

### 3.2 Conserved collinearity and localized copy-number differences

Interspecific MCScan collinearity analysis identified 12 anchor rows in which both endpoints belonged to the OSCA gene set (Figure 2A; Supplementary Table S2). Eleven anchors connected genes located on corresponding chromosomes in the two assemblies. These included OSCA representatives on chromosomes 1A, 4A, 5A, 7A, 8A, and 9A. One additional anchor connected *VpOSCA2.1* on chromosome 5A to *VtOSCA2.2* on chromosome 1A. Because this cross-chromosome relationship reflects an ancient paralogous duplication (paleoduplication) rather than 1:1 species orthology, it was not counted as focal one-to-one orthology.

Conserved microsynteny was particularly evident in the chromosome 7A tandem cluster comprising *OSCA1.3*, *OSCA1.4*, and *OSCA1.5* in both genomes. Although high sequence similarity among adjacent paralogs can cause pairwise collinearity heuristics to produce degenerate anchor matches within tandem arrays (such as the raw anchor pairing *VpOSCA1.5* with *VtOSCA1.4*; Supplementary Table S2), the recovered phylogenetic topology and conserved local gene order supported the corresponding one-to-one relationships. The local genomic block surrounding this cluster contained 24 collinear anchor pairs, 23 of which involved non-OSCA flanking genes. The microsyntenic intervals spanned 213.6 kb in *V. peripherica* and 188.6 kb in *V. tubiflora* (Figure 2B), showing strong positional conservation of the tandem architecture in both species.

The chromosome 1A comparison revealed the principal family-size difference between the two assemblies (Figure 2C). *Vellozia peripherica* contained two adjacent loci, *VpOSCA2.4b* and *VpOSCA2.4a*, ordered from lower to higher genomic coordinates and separated by 1,292 bp, whereas the homologous *V. tubiflora* interval contained a single *VtOSCA2.4* locus. Conserved flanking collinearity placed these loci within orthologous chromosomal segments; integrated with the single-copy outgroup ortholog *XsOSCA2.4* (Figure 1A), this local arrangement supports a lineage-specific tandem duplication on chromosome 1A of *V. peripherica*.

### 3.3 Pairwise divergence and ortholog-set selection intensity

All 14 interspecific pairwise coding-sequence comparisons had ω < 1.00 (Figure 3B; Supplementary Table S3). Values ranged from 0.0530 for *OSCA2.3* to 0.8015 for *OSCA1.4*, with a mean of 0.4082 and a median of 0.3368, confirming that purifying selection predominates across the repertoire. Notably, although *OSCA1.4* maintains ω < 1.00, its ratio of 0.8015 lies substantially closer to neutrality than any other ortholog pair in the family (where eight pairs exhibit strong constraint with ω < 0.40, reaching 0.0530 in *OSCA2.3* and 0.1601 in *OSCA4.1*), representing the highest relative rate of nonsynonymous substitution among the analyzed pairs. The *VpOSCA2.4a*-*VpOSCA2.4b* tandem paralog comparison produced *K*~a~ = 0.0442, *K*~s~ = 0.1172, and ω = 0.3770. Interspecific comparisons at this locus showed contrasting synonymous divergence: *VpOSCA2.4b* and *VtOSCA2.4* shared low synonymous divergence (*K*~s~ = 0.0343, ω = 0.5155), whereas *VpOSCA2.4a* showed substantially higher divergence from both *VtOSCA2.4* (*K*~s~ = 0.1215, ω = 0.2985) and *VpOSCA2.4b*.

Evaluating selection intensity across the analyzed OSCA ortholog set with HyPhy RELAX detected a significant branch-level difference (Figure 3A; Supplementary Table S4). Selection intensity was lower on *V. tubiflora* Test branches than on *V. peripherica* Reference branches (*K* = 0.7064, LRT = 12.8509, *p* = 0.000337). This pattern across the analyzed ortholog set indicates that while baseline purifying constraint is preserved across the core mechanosensory repertoire, the distribution of substitution rates along *V. tubiflora* lineages is shifted toward neutrality relative to *V. peripherica*, consistent with a hypothesis of relaxed selection under the tested codon model.

### 3.4 Basal tissue transcript abundance

Baseline RNA-seq libraries clustered by vegetative organ in principal component analysis (Supplementary Figure S1) and revealed distinct tissue-level expression profiles across the OSCA family (Figure 4; Supplementary Table S5). Within OSCA1, *OSCA1.2* showed the clearest shared pattern. Its abundance was higher in roots than leaves in *V. peripherica* (log~2~FC = 4.3568, *p*~adj~ = 0.0115) and *V. tubiflora* (log~2~FC = 8.2653, *p*~adj~ = 0.000168). Stem abundance was also higher than leaf abundance in both species (log~2~FC = 5.3005, *p*~adj~ = 0.00141; and log~2~FC = 5.3692, *p*~adj~ = 0.00882, respectively). *OSCA1.1* showed the reciprocal pattern: abundance was lower in roots than leaves in *V. peripherica* (log~2~FC = −1.3977, *p*~adj~ = 0.0252) and *V. tubiflora* (log~2~FC = −1.1758, *p*~adj~ = 0.0474). Stem abundance was also lower than leaf abundance in both species (log~2~FC = −1.7833, *p*~adj~ = 0.00302; and log~2~FC = −2.0638, *p*~adj~ = 2.69×10^{−6}, respectively). Among the remaining Clade 1 loci, only *VtOSCA1.4* showed a significant tissue contrast, with higher abundance in stems than in leaves (log~2~FC = 3.7440, *p*~adj~ = 0.0220).

Within OSCA2, *VpOSCA2.3* was more abundant in roots and stems than in leaves (root-leaf: log~2~FC = 4.2153, *p*~adj~ = 0.0402; stem-leaf: log~2~FC = 4.1253, *p*~adj~ = 0.0461), whereas neither contrast was significant for *VtOSCA2.3*. The single *VtOSCA2.4* locus showed higher abundance in roots than in leaves (log~2~FC = 0.8016, *p*~adj~ = 0.0255) and stems (log~2~FC = 1.0112, *p*~adj~ = 0.00623). By contrast, neither *VpOSCA2.4a* nor *VpOSCA2.4b* showed a significant within-gene tissue contrast at the adopted threshold. These separate within-gene tests did not directly evaluate a paralog-by-tissue interaction and therefore do not establish equivalent regulation of the duplicated copies. In addition, *V. tubiflora* showed species-specific contrasts in *VtOSCA2.2*, which was less abundant in stems than in leaves (log~2~FC = −0.7879, *p*~adj~ = 0.0331), and in *VtOSCA2.5*, which was more abundant in roots than in stems (log~2~FC = 1.0999, *p*~adj~ = 0.0290) and less abundant in stems than in leaves (log~2~FC = −1.5526, *p*~adj~ = 1.10×10^{−5}).

Within OSCA3, *OSCA3.1* abundance was lower in stems than in leaves in both *V. peripherica* (log~2~FC = −1.6826, *p*~adj~ = 0.000757) and *V. tubiflora* (log~2~FC = −2.9118, *p*~adj~ = 5.31 × 10^{−5}). Although the root-leaf contrast followed the same direction in both species, it reached statistical significance only in *V. peripherica* (log~2~FC = −1.5623, *p*~adj~ = 0.00200) and not in *V. tubiflora* (log~2~FC = −1.3779, *p*~adj~ = 0.1733). Conversely, *VtOSCA3.2* showed higher abundance in roots than in leaves (log~2~FC = 4.4166, *p*~adj~ = 0.0103), whereas the corresponding *VpOSCA3.2* contrast was not significant.

OSCA4 also exhibited a species-specific tissue pattern: *VtOSCA4.1* abundance was higher in roots than in stems (log~2~FC = 1.8408, *p*~adj~ = 0.00338) and lower in stems than in leaves (log~2~FC = −1.4430, *p*~adj~ = 0.00341), whereas no tissue contrast was significant for *VpOSCA4.1*. Overall, the conserved organ-level polarities observed for *OSCA1.1*, *OSCA1.2*, and the stem-leaf contrast of *OSCA3.1* coexisted with species-specific patterns in OSCA2, *OSCA3.2*, and OSCA4. Because read counts were normalized independently within each species, log~2~FC magnitudes were not compared directly between assemblies.

### 3.5 Predicted functional-association networks and pathway enrichment

The reconstructed STRING functional-association network for *V. peripherica* comprised 61 nodes and 187 edges, whereas the *V. tubiflora* network comprised 60 nodes and 217 edges (Figure 5; Supplementary Table S5; pathway enrichment in Supplementary Table S8). Thus, despite nearly identical node counts, the *V. tubiflora* network contained 16.0% more edges and exhibited a higher mean node degree than the *V. peripherica* network (7.23 vs. 6.13). Mean unweighted clustering coefficients were similar between species (0.4718 in *V. tubiflora* and 0.4937 in *V. peripherica*), and both networks partitioned into two connected components: a major component containing 54 nodes in *V. tubiflora* and 55 in *V. peripherica*, alongside a separate six-node component.

Functional enrichment of the network proteins revealed a similar overall profile in the two species. Starch and sucrose metabolism (KEGG map00500) was the most significantly enriched pathway, comprising 23 genes in *V. tubiflora* (FDR = 3.57 × 10^{−28}) and 22 in *V. peripherica* (FDR = 2.60 × 10^{−26}). Enriched molecular functions included amylase activity (GO:0016160; FDR = 3.74 × 10^{−16} and 3.22 × 10^{−16}, respectively), amylopectin maltohydrolase activity (GO:0102229; FDR = 3.61 × 10^{−15} and 4.14 × 10^{−13}, respectively), β-amylase activity (GO:0016161; FDR ≤ 2.14 × 10^{−10}), α-amylase activity (GO:0004556; FDR ≤ 6.93 × 10^{−5}), and calcium-activated cation channel activity (GO:0005227; FDR = 8.80 × 10^{−18} and 5.64 × 10^{−20}, respectively). Plasma membrane (GO:0005886) and plasmodesmata (GO:0009506) were also enriched cellular-component categories in both networks (FDR < 0.009).

The connectivity of individual OSCA proteins further revealed shared and species-specific patterns. Restricting the calculation specifically to the connected OSCA channels (10 of 13 in *V. tubiflora* and 11 of 14 in *V. peripherica*, excluding the three loci lacking interactions in each species), the mean degree of the focal channels was 7.30 in *V. tubiflora* (5.62 across all 13 queried loci) and 6.09 in *V. peripherica* (4.79 across all 14 queried loci), closely tracking the whole-network mean node degrees of 7.23 and 6.13 across all interactors. Within OSCA1, *OSCA1.2* occupied an identical conserved topological position in both species, with a degree of 18 (comprising 16 predicted functional associations with carbohydrate-catabolizing enzymes alongside two adjacent channel interactors in each network). *OSCA1.1* had degree 13 in *V. tubiflora* and 11 in *V. peripherica*. The remaining OSCA1 proteins were more peripheral: *OSCA1.3*, *OSCA1.4*, and *OSCA1.5* each had degree 3 in *V. tubiflora* and degree 1 in *V. peripherica*.

Differences were also observed among OSCA2 proteins. *OSCA2.5* had degree 7 in *V. tubiflora* and 4 in *V. peripherica*. At the chromosome 1A locus, the single-copy *VtOSCA2.4* had degree 5, whereas each of the tandem paralogs *VpOSCA2.4a* and *VpOSCA2.4b* had degree 2. By contrast, *OSCA2.1*, *OSCA2.2*, and *OSCA2.3* returned no associations in either species at the adopted confidence threshold.

The OSCA3 proteins displayed a distinct but conserved organization. In both species, *OSCA3.1* and *OSCA3.2* occurred in the separate six-node component and each had degree 4. Their predicted partners were organellar proteins annotated with plant-type vacuole and photosystem I components.

OSCA4 also showed high connectivity in both networks, although its degree differed between species. *VpOSCA4.1* was the most connected OSCA query in *V. peripherica*, with 19 associations, whereas *VtOSCA4.1* had 13 in *V. tubiflora*. Both values exceeded the corresponding mean degree of the connected OSCA queries, and the predicted partners of *VpOSCA4.1* included HSP70 chaperones.

Text mining supported most network edges: 157 of 217 (72.35%) in *V. tubiflora* and 132 of 187 (70.59%) in *V. peripherica*. Curated-database evidence supported 119 and 109 edges, respectively, whereas five edges in each network had experimental support. Coexpression, co-occurrence, genomic neighbourhood, and gene fusion contributed smaller subsets.

### 3.6 Promoter *cis*-regulatory element repertoire

PlantCARE annotation of the 2-kb upstream promoter regions across all 27 *Vellozia* OSCA loci identified non-overlapping *cis*-regulatory motifs across core promoter, growth and development, light responsiveness, phytohormone signaling, and abiotic stress categories, with similar overall category distributions between the two species (Figure 6; Supplementary Tables S6 and S7).

Excluding basal core promoter elements (TATA-box and CAAT-box; 1,380 total occurrences across all 27 promoters), growth- and development-associated transcription factor sites (MYB and MYC, alongside a single RY-element; 204 occurrences) and light-responsive elements (Box 4, G-box, and GT1-motif; 187 occurrences) were the most abundant categories, followed by phytohormone signaling (161 occurrences) and abiotic stress response (116 occurrences). Phytohormone-related elements included the ABA-responsive element (ABRE), MeJA-responsive elements (CGTCA-motif and TGACG-motif), and the salicylic acid-responsive TCA-element. Stress-related motifs included the drought-responsive MBS (MYB binding site involved in drought inducibility), the low-temperature-responsive LTR, the anaerobic induction element ARE, TC-rich repeats, and the WRKY-binding W box involved in defense and wounding responses.

Despite these similarities at the gene-family level, individual promoter regions differed in motif composition. This contrast was evident at the *OSCA2.4* locus: *VpOSCA2.4a* contained two non-overlapping ABRE matches, *VpOSCA2.4b* contained four, and *VtOSCA2.4* contained six. The highest ABRE counts in *V. peripherica* occurred in *VpOSCA2.1* and *VpOSCA3.2* (six matches each), whereas *VtOSCA2.1* had the highest count in *V. tubiflora* (seven), followed by *VtOSCA2.4* (six). Hormone-, stress-, and development-associated elements also varied across individual paralogs (Figure 6).

## 4. DISCUSSION

### 4.1 Conservation and structural variation in OSCA channels

The two *Vellozia* species retained closely similar OSCA repertoires across all four clades, with most loci occupying conserved chromosomal contexts. Shared family composition, extensive macrosyntenic collinearity, and pairwise ω < 1.00 demonstrate a predominantly conserved evolutionary framework, with divergence restricted to localized copy-number variation, basal transcript abundance, and promoter motif composition. However, OSCA family membership establishes sequence homology rather than demonstrated channel biophysics in *Vellozia*: although osmotic calcium signaling and mechanically activated currents have been characterized in model angiosperms (YUAN et al., 2014; MURTHY et al., 2018), direct electrophysiological recordings are required to determine whether *Vellozia* homologs share these conductance, ion-selectivity, and tension-gating properties.

The shortened architectures of *VpOSCA2.2* and *VtOSCA1.2* further show that family conservation does not imply uniform channel structure across all loci. Both proteins retained PF02714, PF14703, and PTHR13018 but lacked a detectable PF13967 domain. Truncations of OSCA channels have also been documented in other monocots; for instance, in maize (*Zea mays*), *ZmOSCA1.1a* and *ZmOSCA3.1* harbor independent deletions that reduce the number of predicted transmembrane segments relative to canonical full-length paralogs (DING et al., 2019). In *Vellozia*, this reduction in predicted transmembrane passes (five to six helices compared to 7 to 12 predicted by TMHMM in full-length models) coincides with the absence of PF13967. Because structurally resolved OSCA channels form functional homodimers with eleven transmembrane helices per subunit, including the membrane-deforming TM0 (LIU; WANG; SUN, 2018; ZHANG et al., 2018), such structural deletions are expected to directly impact channel topology, oligomerization, or mechanosensory gating. Transcript-supported re-annotation and *in vivo* functional assays remain necessary to confirm whether these shortened models represent functional specialized variants or bioinformatic annotation artifacts. Overall, the species share a strongly conserved core repertoire interspersed with localized structural divergence.

In terms of gene copy number and family architecture, the primary mechanosensory repertoire exhibits high compositional stability in the resurrection specialist, showing no lineage-specific expansions. However, this stability does not imply uniform selective pressure: modeling across the analyzed OSCA ortholog set detected significant relaxation of selective constraint along the *V. tubiflora* lineage (*K* = 0.7064, *p* = 0.0003), while purifying selection (*K*~a~/*K*~s~ < 1) remained the broad baseline. Because electrophysiological and structural investigations have demonstrated that OSCA channels operate as intrinsically mechanosensitive conduits gated by membrane tension (MURTHY et al., 2018; YUAN et al., 2014; ZHANG et al., 2018), this evolutionary pattern does not imply a substitution of the biophysical tension-gating mechanism itself. Rather, we hypothesize that macroevolutionary divergence between vegetative desiccation tolerance and dehydration avoidance involves differential upstream regulation and downstream signaling integration. In resurrection Velloziaceae, vegetative tissues survive extreme water loss exceeding 90% of cellular water content (ALCANTARA et al., 2015; FARRANT et al., 2015). During severe dehydration, extensive cell-wall folding and protoplast shrinkage occur alongside specialized cellular mitigation mechanisms (FARRANT et al., 2015). Whether constitutive stretch-activated ion influx would interfere with anhydrobiotic quiescence, and whether dampening mechanosensory channel activity or uncoupling downstream calcium cascades prevents potentially detrimental signaling during severe drying, remains a hypothesis to be evaluated through functional assays across dehydration time courses.

### 4.2 Syntenic conservation and localized copy-number variation

Syntenic analysis confirmed chromosome-scale structural conservation between the two congeners. On chromosome 7A, the *OSCA1.3/1.4/1.5* tandem array occurred in conserved gene order within a collinear block containing 23 non-OSCA anchor pairs spanning more than 188 kb. Although high sequence similarity among adjacent paralogs can generate degenerate pairwise anchor matches, the concordance between phylogenetic topology, local gene order, and flanking collinearity indicates that this three-gene array predates the divergence of the focal *Vellozia* lineages.

The principal departure from this conserved organization occurred at *OSCA2.4* on chromosome 1A, where *V. peripherica* contained two adjacent copies (*VpOSCA2.4a* and *VpOSCA2.4b*) and *V. tubiflora* contained one (*VtOSCA2.4*). Their chromosomal contiguity is consistent with a local tandem duplication event. Orthology mapping and domain annotation against the sister outgroup *Xerophyta schlechteri* identified a single ancestral *OSCA2.4* copy (*XsOSCA2.4* / MP002250 in orthogroup OG0006102). Because both the outgroup *X. schlechteri* and the congener *V. tubiflora* carry a single locus, maximum parsimony polarizes this locus as a derived, lineage-specific tandem duplication in *V. peripherica* rather than an ancestral loss in *V. tubiflora*. Interspecific synonymous divergence estimates provide complementary relative timing: *VpOSCA2.4b* and *VtOSCA2.4* share a markedly lower synonymous divergence (*K*~s~ = 0.0343) than either does with *VpOSCA2.4a* (*K*~s~ ≈ 0.12; Supplementary Table S3), designating *VpOSCA2.4b* as the primary syntenic ortholog to *VtOSCA2.4*. Independently, pairwise nonsynonymous-to-synonymous rate ratios remain well below unity (ω = 0.3770 between *2.4a* and *2.4b*, and ω = 0.2985 relative to *VtOSCA2.4*; Supplementary Table S3), indicating that both coding sequences evolve under purifying selection. While low ω values alone cannot rule out recent pseudogenization, the preservation of an uninterrupted open reading frame, an intact tripartite Pfam domain architecture, and consistent basal transcript abundance across vegetative tissues (Supplementary Tables S1 and S5) collectively support the retention of *VpOSCA2.4a* as a functional coding channel rather than a pseudogene. Synteny thus establishes a conserved chromosomal framework while pinpointing the *OSCA2.4* locus as a localized site of copy-number divergence, providing a clear focal candidate for broader evolutionary sampling across Velloziaceae.

### 4.3 Selection intensity and the limits of the two-species comparison

All pairwise *K*~a~/*K*~s~ (ω) estimates were below unity across the 14 ortholog pairs (ω < 1.00, median = 0.3368; Supplementary Table S3), indicating that purifying selection predominates across the OSCA gene set. Notably, while eight pairs exhibited strong purifying constraint (ω < 0.40), *OSCA1.4* displayed a markedly higher ratio (ω = 0.8015), pointing to weaker constraint and substantial selective relaxation at this locus compared to the remainder of the family. Similar predominantly purifying regimes have been reported for duplicated OSCA pairs in *Vigna radiata* (YIN et al., 2021) and *Liriodendron chinense* (KE et al., 2022). This overall evolutionary constraint is consistent with the maintenance of the complex transmembrane architecture of OSCA proteins, which typically contain 6 to 11 transmembrane helices (CHAKRABORTY et al., 2023).

Despite this baseline structural constraint, RELAX detected a significant reduction in selection intensity across the analyzed OSCA ortholog set along the *V. tubiflora* lineage (*K* = 0.7064, *p* = 0.0003). While this parameter estimate is compatible with relaxed functional constraint accompanying anhydrobiotic quiescence, such estimates under phenomenological codon models may also absorb unmodeled mutational dynamics, substitution-model saturation, or lineage-specific demographic fluctuations (JONES et al., 2018). Furthermore, because pairwise comparisons between two species cannot definitively separate physiological adaptation from demographic history or effective population size (*N*~e~; LYNCH; CONERY, 2003; STRASBURG et al., 2011), this relaxation across the analyzed ortholog set should be interpreted as a comparative hypothesis warranting expanded sampling across the *Vellozia* eco-physiological spectrum.

### 4.4 Conserved and divergent tissue-expression patterns

Parallel to sequence-level selective constraints, the physiological deployment of mechanosensory channels is influenced by their spatial regulation across plant organs (HARTMANN et al., 2021). The baseline transcriptomes revealed repeated spatial patterns in both species. *OSCA1.2* was more abundant in roots and stems than in leaves, whereas *OSCA1.1* showed the opposite tendency in the principal contrasts. These shared directions suggest that some tissue partitioning predates the divergence of the focal species or has been maintained in both lineages. By contrast, *OSCA3.1* was more abundant in leaves than stems in both species, but its root-leaf difference was supported only in *V. peripherica*. Likewise, the absence of significant tissue contrasts for the two *VpOSCA2.4* copies does not establish regulatory redundancy, which would require a direct paralog-by-tissue test. Moreover, because one field population per species was sampled, these tissue expression profiles should be interpreted alongside potential intraspecific variation and local microenvironmental effects.

While resolving cell-type specificity and dehydration-induced transcriptional dynamics will require single-cell profiling and progressive drying time courses, these whole-organ transcriptomes establish an organ-level physiological baseline for the *Vellozia* OSCA family. Specifically, the concordant spatial partitioning of key paralogs such as *OSCA1.2* and *OSCA1.1* across both species supports conserved basal tissue regulation alongside structural conservation, providing a reference baseline for evaluating stress-responsive expression across contrasting drought strategies.

### 4.5 Predicted functional associations of OSCA proteins

The STRING networks positioned *OSCA1.2*, *OSCA4.1*, and *OSCA1.1* among the most connected queried channels. Because these edges map functional associations derived predominantly from text-mining and homology transfer from model systems (Figure 5B; SZKLARCZYK et al., 2023), they provide a predictive framework for identifying candidate cellular contexts and metabolic pathways for these proteins in *Vellozia*.

Among the primary hubs, *OSCA1.2* had the same degree in both species and was associated with 16 carbohydrate-metabolism proteins, principally α- and β-amylases. Together with its higher basal transcript abundance in roots and stems, this pattern suggests a testable connection between mechanosensory signaling and osmotic-metabolic adjustment. Phylogenetically, the *Vellozia* *OSCA1.2* lineage is sister to a grass clade containing rice *OsOSCA1.3* and maize *ZmOSCA1.3*; in rice, clade 1 channels such as *OsOSCA1.1* rescue osmotic Ca^{2+} signaling in *Arabidopsis* *osca1* mutants (ZHAI et al., 2021), whereas maize *ZmOSCA1.3* is downregulated under stress (LI et al., 2022). This evolutionary proximity generates the testable prediction that *Vellozia* *OSCA1.2* functions as a mechanosensory channel, potentially contributing to basal turgor maintenance rather than stress-inducible responses. However, phylogenetic homology to grass models and elevated basal transcript abundance do not directly demonstrate protein-level channel activity, membrane localization, or transport function in *Vellozia*. This interpretation therefore represents a predictive hypothesis requiring electrophysiological validation, and its network centrality must be evaluated with particular caution for *V. tubiflora*: because the *VtOSCA1.2* gene model lacks the principal transmembrane domain (PF13967), its predicted hub status derives from full-length orthologs and reflects the ancestral role of the lineage rather than the confirmed capacity of this specific protein. If this truncation is biologically real rather than an annotation artifact, *VtOSCA1.2* may lack ion channel activity entirely. Whether dampening constitutive mechanosensory sensitivity could prevent maladaptive calcium signaling during the massive cellular shrinkage of anhydrobiosis is a speculative hypothesis. Because this scenario lacks direct functional or selective evidence, experimental validation of the gene model through cDNA sequencing and transport assays is necessary before attributing any adaptive significance to this locus. In parallel, *OSCA4.1* emerged as a prominent connected node in the predicted networks. In maize, natural genetic variation at *ZmOSCA4.1* is associated with seedling dehydration survival and drought-tolerance traits (DING et al., 2019), supporting the relevance of this channel family to water-deficit responses. However, genetic association with drought traits in a crop model does not demonstrate network centrality, nor does it establish that *OSCA4.1* occupies a central physiological role in *Vellozia*.

Unlike the candidate plasma-membrane hubs, *OSCA3.1* and *OSCA3.2* formed a separate network component associated with vacuolar and photosystem proteins. Because STRING networks aggregate predicted functional associations from heterogeneous data types, including co-expression and automated text-mining, they do not establish physical protein interactions or shared subcellular localization (SZKLARCZYK et al., 2023). This topological separation therefore does not demonstrate organellar compartmentation in *Vellozia*, but rather generates the hypothesis that clade 3 channels could participate in specialized intracellular processes. This hypothesis is compatible with comparative findings where OSCA3 orthologs, historically identified as early responsive to dehydration 4 (ERD4) genes (KIYOSUE; YAMAGUCHI-SHINOZAKI; SHINOZAKI, 1994), have been associated with intracellular stress responses in model plants. Nevertheless, predicted network associations cannot substitute for experimental evidence of localization, and determining whether *Vellozia* OSCA3 channels reside in the tonoplast, plastidial membranes, or the plasma membrane requires direct empirical validation.

Conversely, lower connectivity in other family members often reflects database bias and evolutionary history rather than biological isolation. For example, the peripheral network positions of *OSCA1.3*, *OSCA1.4*, and *OSCA1.5* likely reflect their origin via tandem expansion in Velloziaceae and the resulting absence of direct one-to-one functional equivalents in the model organisms represented in STRING. Similarly, although connectivity is lower for the two *V. peripherica* *OSCA2.4* paralogs than for the single *V. tubiflora* copy, which could speculatively reflect a division of ancestral interaction partners, transferred edge counts cannot establish subfunctionalization (LYNCH; FORCE, 2000). Testing whether these tandem duplicates have undergone genuine subfunctionalization will require direct experimental comparisons of paralog expression and transport physiology. More broadly, absent edges for *OSCA2.1*, *OSCA2.2*, and *OSCA2.3* highlight the coverage limits of homology-based annotation transfer.

Collectively, these computational predictions require *in vivo* validation to establish true pathway membership in *Vellozia*. Nevertheless, the network topologies highlight *OSCA1.2*, *OSCA4.1*, and the *OSCA2.4* copies as priority candidates for functional characterization.

### 4.6 Regulatory variation and functional priorities

Within each *Vellozia* species, OSCA promoters exhibited pronounced locus-level heterogeneity in motif composition. This internal variation mirrors patterns reported in *Liriodendron chinense*, sunflower, and alfalfa (KE et al., 2022; SHAN et al., 2023; LI et al., 2023), as well as in *Vigna radiata*, where promoter differences within OSCA clades may indicate functional diversity in ABA and osmotic stress responses (YIN et al., 2021). Despite this intra-species variation, the two *Vellozia* species shared a broadly similar overall distribution of ABRE, MBS, G-box, ARE, and LTR motifs. The OSCA family thus exhibits a broadly similar predicted *cis*-regulatory motif composition across species, while locus-specific differences provide candidate hypotheses of distinct regulatory sensitivities.

This promoter heterogeneity is most evident at the *OSCA2.4* locus. The two *V. peripherica* paralogs differed in ABRE abundance, and both contained fewer ABRE matches than the single *VtOSCA2.4* copy. Combined with the localized copy-number variation, this pattern suggests that duplication was accompanied by regulatory divergence. However, because basal transcriptomes do not capture induced stress dynamics, it remains to be tested whether the elevated ABRE counts in *VtOSCA2.4*, *VtOSCA2.1*, *VpOSCA2.1*, and *VpOSCA3.2* directly translate into enhanced ABA-dependent transcription *in vivo*. Validating this regulatory divergence and determining the precise stress responsiveness of individual paralogs will require RNA-seq assays under varying water availability.

## 5. CONCLUSIONS

Comparative genomic analysis of *Vellozia peripherica* and *Vellozia tubiflora* reveals a predominantly conserved OSCA mechanosensory repertoire characterized by similar family sizes (14 vs. 13 loci), retention of all four canonical clades, and conserved chromosomal collinearity. Pairwise coding-sequence divergence remained below unity (ω < 1.00) across all analyzed ortholog pairs, confirming pervasive purifying selection, while branch-level modeling in RELAX detected relative relaxation of selection intensity across the analyzed OSCA ortholog set along *V. tubiflora* branches (*K* = 0.7064, *p* = 0.0003). Against this conserved structural background, chromosome 1A harbors a localized copy-number divergence resulting from a lineage-specific *VpOSCA2.4a/b* tandem duplication in *V. peripherica*. Together, these findings demonstrate that broad family conservation coexists with circumscribed structural and evolutionary divergence between the two congeners.

Integrating basal organ transcriptomes, functional-association networks, and promoter architectures identifies priority candidates for functional validation. *OSCA1.2* exhibits conserved root and stem transcript enrichment and high connectivity in STRING functional networks, including predicted associations with starch and sucrose catabolic enzymes, whereas the *OSCA2.4* locus provides a defined comparative system for testing paralog subfunctionalization and ABA-responsive transcriptional regulation. While comparisons between a single species pair cannot disentangle strategy-specific adaptation from demographic history, these results establish that vegetative desiccation tolerance in *V. tubiflora* does not require wholesale restructuring of the primary OSCA mechanosensory repertoire, operating instead within a conserved channel framework modified by localized evolutionary and regulatory divergence.

## ACKNOWLEDGMENTS

The authors thank the staff and facilities of the Center for Molecular Biology and Genetic Engineering (CBMEG/UNICAMP) for infrastructural and computational support. We thank the administration of Serra da Canastra National Park and the private landowners in Delfinópolis, MG, Brazil, for logistical assistance and permission to conduct field sampling.

## FUNDING

This study was financed in part by the Coordenação de Aperfeiçoamento de Pessoal de Nível Superior - Brasil (CAPES) - Finance Code 001 (doctoral fellowship to M.F.C.), the Fundação de Amparo à Pesquisa do Estado de São Paulo (FAPESP; grant 2020/02084-0 to M.F.C.), and the Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq).

## AUTHOR CONTRIBUTIONS

M.F.C.: Conceptualization, Methodology, Software, Formal analysis, Investigation, Data curation, Writing - original draft, Writing - review & editing, Visualization. I.R.G.: Conceptualization, Supervision, Project administration, Resources, Funding acquisition, Writing - review & editing.

## DATA AVAILABILITY STATEMENT

All genome assemblies and structural annotation files used in this study are available through institutional data repositories and NCBI BioProject (PRJNA1019079 for *V. tubiflora* and PRJNA1019080 for *V. peripherica*; accession details in Supplementary Table S1). Derived data, including custom scripts, multiple sequence alignments, phylogenetic tree files, and supplementary tables, are available in the project GitHub repository (https://github.com/cavalheiromf/doutorado).

## CONFLICT OF INTEREST STATEMENT

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## FIGURE LEGENDS

**Figure 1. OSCA phylogeny and predicted domain architecture.** (A) Circular maximum-likelihood tree of 84 OSCA protein sequences, inferred with the Q.PLANT+R5 model in IQ-TREE. Branch lengths were equalized to optimize tip-label resolution. Following established deep-paralogy rooting in angiosperm OSCA gene families (KE et al., 2022; YUAN et al., 2014), the tree is rooted between Clade OSCA1 and the remaining clades (OSCA2, OSCA3, and OSCA4). The tree incorporates *Vellozia peripherica* (14 loci, purple circles), *Vellozia tubiflora* (13 loci, orange circles), the sister outgroup *Xerophyta schlechteri* (8 loci, teal triangles), and angiosperm reference channels from *Arabidopsis thaliana*, *Oryza sativa*, *Zea mays*, and *Sorghum bicolor*. Canonical clades are color-coded: Clade OSCA1 (pastel blue), Clade OSCA2 (pastel green), Clade OSCA3 (pastel purple), and Clade OSCA4 (pastel red). Numbers at internal nodes indicate ultrafast bootstrap support values (≥ 70%). Across the tree, individual *X. schlechteri* loci branch as immediate sister outgroups to the corresponding *Vellozia* orthologs rather than forming a single genus-level cluster; specifically, *XsOSCA2.4* resolves sister to the *OSCA2.4* clade, supporting an ancestral single-copy state and polarizing the *VpOSCA2.4a/b* tandem duplication in *V. peripherica* under maximum parsimony. (B-C) Curated Pfam domain architectures and transmembrane topology of OSCA channels in *Vellozia peripherica* (B) and *Vellozia tubiflora* (C). Colored boxes indicate canonical Pfam domains: RSN1_7TM (PF02714, pink), Cytoplasmic domain (PF13967, green), and Calcium-dependent channel domain (PF14703, yellow). Scales indicate amino acid coordinates from N- to C-terminus. Detailed protein lengths, theoretical isoelectric points, and transmembrane helix counts predicted by TMHMM are provided in Supplementary Table S1.

**Figure 2. Comparative OSCA synteny.** (A) Whole-genome macrosynteny and collinear anchors across homologous chromosomes (Chr1A-Chr9A). (B) Microsyntenic conservation of the *OSCA1.3*, *OSCA1.4*, and *OSCA1.5* cluster on chromosome 7A with flanking collinear genes. (C) Microsynteny of the two adjacent *VpOSCA2.4* loci on chromosome 1A. Raw anchor rows are in Supplementary Table S2. Secondary alignments derived from cross-chromosome paleoduplications were excluded from focal 1:1 orthology. Phylogenetic comparison with the outgroup *Xerophyta schlechteri* polarizes the *OSCA2.4* copy-number difference as a lineage-specific tandem duplication in *V. peripherica*.

**Figure 3. Selection dynamics and pairwise evolutionary rates.** (A) RELAX estimate of selection intensity parameter *K* across reference (*V. peripherica*) and test (*V. tubiflora*) branches for the analyzed OSCA ortholog set (*K* = 0.7064, *p* = 0.0003); *K* < 1 denotes relaxed selection in *V. tubiflora* relative to *V. peripherica* under the tested codon framework. (B) Pairwise whole-gene coding-sequence divergence ratios (ω = *K*~a~/*K*~s~) for 14 ortholog pairs and the *VpOSCA2.4a*-*VpOSCA2.4b* tandem paralogs calculated via YN00, demonstrating pervasive purifying selection across the family (all ω < 1.00; median = 0.3368; range = 0.0530 to 0.8015, with *OSCA1.4* displaying the highest ratio approaching neutrality).

**Figure 4. Basal tissue transcript abundance of OSCA genes in *****Vellozia*****.** Per-library log~2~(normalized counts + 1) across leaf (F), stem (C), and root (R) tissues, with *V. peripherica* (A) and *V. tubiflora* (B); asterisks denote root-leaf contrasts and daggers stem-leaf contrasts with transcriptome-wide Benjamini-Hochberg-adjusted *p* < 0.05. Transcriptome-wide PCA ordinations validating sample clustering by tissue are shown in Supplementary Figure S1.

**Figure 5. Predicted functional interactome and network modules of OSCA channels in *****Vellozia*****.** (A) Degree centrality of OSCA channels in reconstructed STRING functional-association networks. (B) Proportions of network edges supported by distinct STRING evidence channels across all retained interactions. (C1-C2) Reconstructed functional-association networks for *V. peripherica* (C1) and *V. tubiflora* (C2), reflecting integrated functional associations rather than strictly physical interactions. Functional modules were identified by greedy modularity optimization on confidence-weighted interaction matrices, and biological identities were assigned from significant STRING Gene Ontology and KEGG pathway enrichment (FDR < 0.05). Categories were: starch and sucrose metabolism / carbohydrate catabolism (blue); stress response and secondary metabolism (orange); nuclear and macromolecular complexes (purple); membrane transport and ion channel activity (green); and photosystem and organellar homeostasis (gold). Larger numbered circles with dark borders denote focal OSCA mechanosensitive channels. Smaller nodes denote associated functional interactors retrieved via the STRING API (combined score ≥ 0.400). Edge thickness represents interaction confidence score.

**Figure 6. PlantCARE motif occurrences in 2-kb upstream regions.** Selected non-overlapping annotations upstream of transcript boundaries, merged across identical motif classes. Counts are computational predictions and do not imply demonstrated transcription-factor binding or physiological response.

**Figure S1. Principal component analysis (PCA) of RNA-seq transcriptomes across tissues and individuals.** Two-dimensional projection of variance-stabilizing transformed (VST) gene expression data across leaf, stem, and root tissues for *V. peripherica* (A) and *V. tubiflora* (B). Individual biological replicates cluster by tissue along PC1 and PC2.

## SUPPLEMENTARY MATERIAL

All supplementary tables are provided in Supplementary_Tables_OSCA.xlsx:

**• Table S1:** Audited OSCA gene catalog and predicted protein features across *Vellozia peripherica*, *Vellozia tubiflora*, and the sister outgroup *Xerophyta schlechteri* (lengths, molecular weights, theoretical pI, transmembrane helix predictions, and Pfam domains).

**• Table S2:** OSCA pairs present in the raw MCScan anchor file.

**• Table S3:** PAL2NAL and PAML YN00 pairwise evolutionary rate estimates (Ka, Ks, omega).

**• Table S4:** HyPhy RELAX selection intensity parameter (*K*) across the analyzed OSCA ortholog set and likelihood ratio test.

**• Table S5:** Basal vegetative tissue transcript abundance (DESeq2 normalized counts and pairwise contrasts) and STRING network topological properties.

**• Table S6:** Selected PlantCARE *cis*-regulatory motif occurrence counts across 2.0-kb upstream promoters.

**• Table S7:** Functional classification and consensus sequences of annotated *cis*-regulatory elements.

**• Table S8:** Gene Ontology (GO) and KEGG pathway functional enrichment of OSCA STRING interactomes.

## References

ALCANTARA, S. et al. Carbon assimilation and habitat segregation in resurrection plants: a comparison between desiccation- and non-desiccation-tolerant species of Neotropical Velloziaceae (Pandanales). Functional Ecology, v. 29, n. 12, p. 1499–1512, 2015. DOI: https://doi.org/10.1111/1365-2435.12462.

BASU, D.; HASWELL, E. S. Plant mechanosensitive ion channels: an ocean of possibilities. Current Opinion in Plant Biology, v. 40, p. 43–48, 2017. DOI: https://doi.org/10.1016/j.pbi.2017.07.002.

CHAKRABORTY, S. et al. Genome-wide characterization and comparative analysis of the OSCA gene family and identification of its potential stress-responsive members in legumes. Scientific Reports, v. 13, art. 5914, 2023. DOI: https://doi.org/10.1038/s41598-023-33226-8.

CHANG, S.; PURYEAR, J.; CAIRNEY, J. A simple and efficient method for isolating RNA from pine trees. Plant Molecular Biology Reporter, v. 11, p. 113–116, 1993. DOI: https://doi.org/10.1007/BF02670468.

COCK, P. J. A. et al. Biopython: freely available Python tools for computational molecular biology and bioinformatics. Bioinformatics, v. 25, n. 11, p. 1422–1423, 2009. DOI: https://doi.org/10.1093/bioinformatics/btp163.

COSTA, M.-C. D. et al. A footprint of desiccation tolerance in the genome of *Xerophyta viscosa*. Nature Plants, v. 3, n. 4, art. 17038, 2017. DOI: https://doi.org/10.1038/nplants.2017.38.

DE FREITAS LAROCCA, P. et al. Recent divergence in functional traits affects rates of speciation in the Neotropical Velloziaceae (Pandanales). Botanical Journal of the Linnean Society, v. 199, n. 1, p. 144–172, 2022. DOI: https://doi.org/10.1093/botlinnean/boab102.

DING, S. et al. Genome-wide analysis of maize OSCA family members and their involvement in drought stress. PeerJ, v. 7, p. e6765, 2019. DOI: https://doi.org/10.7717/peerj.6765.

DOBIN, A. et al. STAR: ultrafast universal RNA-seq aligner. Bioinformatics, v. 29, n. 1, p. 15–21, 2013. DOI: https://doi.org/10.1093/bioinformatics/bts635.

EDDY, S. R. Accelerated profile HMM searches. PLoS Computational Biology, v. 7, n. 10, p. e1002195, 2011. DOI: https://doi.org/10.1371/journal.pcbi.1002195.

FARRANT, J. M. et al. A molecular physiological review of vegetative desiccation tolerance in the resurrection plant *Xerophyta viscosa* (Baker) with reference to biotechnological application for the production of drought tolerant cereals. Planta, v. 242, n. 2, p. 407–426, 2015. DOI: https://doi.org/10.1007/s00425-015-2325-6.

FENG, W.; LINDNER, H.; ROBBINS, N. E.; DINNENY, J. R. Growing Out of Stress: The Role of Cell- and Organ-Scale Growth Control in Plant Water-Stress Responses. The Plant Cell, v. 28, n. 8, p. 1769–1782, 2016. DOI: https://doi.org/10.1105/tpc.16.00182.

FLAGEL, L. E.; WENDEL, J. F. Gene duplication and evolutionary novelty in plants. New Phytologist, v. 183, n. 3, p. 557–564, 2009. DOI: https://doi.org/10.1111/j.1469-8137.2009.02923.x.

FRACHISSE, J. M. et al. Mechanosensitive channels: feeling tension in a world under pressure. Frontiers in Plant Science, v. 5, p. 551, 2014. DOI: https://doi.org/10.3389/fpls.2014.00551.

HAGBERG, A. A.; SCHULT, D. A.; SWART, P. J. Exploring network structure, dynamics, and function using NetworkX. In: PYTHON IN SCIENCE CONFERENCE, 7., 2008, Pasadena. Proceedings [...]. Pasadena: [s. n.], 2008. p. 11–15. Disponível em: https://aric.hagberg.org/papers/hagberg-2008-exploring.pdf. Acesso em: 15 set. 2026.

HARTMANN, F. P. et al. Between Stress and Response: Function and Localization of Mechanosensitive Ca2+ Channels in Herbaceous and Perennial Plants. International Journal of Molecular Sciences, v. 22, n. 20, art. 11043, 2021. DOI: https://doi.org/10.3390/ijms222011043.

HASWELL, E. S.; VERSLUES, P. E. The ongoing search for the molecular basis of plant osmosensing. Journal of General Physiology, v. 145, n. 5, p. 389–394, 2015. DOI: https://doi.org/10.1085/jgp.201411295.

HOANG, D. T. et al. UFBoot2: improving the ultrafast bootstrap approximation. Molecular Biology and Evolution, v. 35, n. 2, p. 518–522, 2018. DOI: https://doi.org/10.1093/molbev/msx281.

JONES, C. T. et al. Phenomenological load on model parameters can lead to false biological conclusions. Molecular Biology and Evolution, v. 35, n. 6, p. 1473–1488, 2018. DOI: https://doi.org/10.1093/molbev/msy049.

KATOH, K.; ROZEWICKI, J.; YAMADA, K. D. MAFFT online service: multiple sequence alignment, interactive sequence choice and visualization. Briefings in Bioinformatics, v. 20, n. 4, p. 1160–1166, 2019. DOI: https://doi.org/10.1093/bib/bbx108.

KE, Y. et al. OSCA genes in *Liriodendron chinense*: characterization, evolution and response to abiotic stress. Forests, v. 13, n. 11, art. 1835, 2022. DOI: https://doi.org/10.3390/f13111835.

KIYOSUE, T.; YAMAGUCHI-SHINOZAKI, K.; SHINOZAKI, K. Cloning of cDNAs for genes that are early-responsive to dehydration stress (ERDs) in Arabidopsis thaliana L.: identification of three ERDs as HSP cognate genes. Plant Molecular Biology, v. 25, n. 5, p. 791–798, 1994. DOI: https://doi.org/10.1007/BF00028884.

KOSAKOVSKY POND, S. L. et al. HyPhy 2.5—a customizable platform for evolutionary hypothesis testing using phylogenies. Molecular Biology and Evolution, v. 37, n. 1, p. 295–299, 2020. DOI: https://doi.org/10.1093/molbev/msz197.

KROGH, A. et al. Predicting transmembrane protein topology with a hidden Markov model: application to complete genomes. Journal of Molecular Biology, v. 305, n. 3, p. 567–580, 2001. DOI: https://doi.org/10.1006/jmbi.2000.4315.

LESCOT, M. et al. PlantCARE, a database of plant cis-acting regulatory elements and a portal to tools for in silico analysis of promoter sequences. Nucleic Acids Research, v. 30, n. 1, p. 325–327, 2002. DOI: https://doi.org/10.1093/nar/30.1.325.

LETUNIC, I.; BORK, P. Interactive Tree Of Life (iTOL) v5: an online tool for phylogenetic tree display and annotation. Nucleic Acids Research, v. 49, n. W1, p. W293–W296, 2021. DOI: https://doi.org/10.1093/nar/gkab301.

LI, S. et al. Preliminary Expression Analysis of the OSCA Gene Family in Maize. International Journal of Molecular Sciences, v. 23, n. 14, art. 7606, 2022. DOI: https://doi.org/10.3390/ijms23147606.

LI, X. et al. Genome-wide investigation and expression analysis of OSCA gene family in response to abiotic stress in alfalfa. Frontiers in Plant Science, v. 14, art. 1285488, 2023. DOI: https://doi.org/10.3389/fpls.2023.1285488.

LIU, X.; WANG, J.; SUN, L. Structure of the hyperosmolality-gated calcium-permeable channel OSCA1.2. Nature Communications, v. 9, art. 5060, 2018. DOI: https://doi.org/10.1038/s41467-018-07564-5.

LOVE, M. I.; HUBER, W.; ANDERS, S. Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. Genome Biology, v. 15, n. 12, p. 550, 2014. DOI: https://doi.org/10.1186/s13059-014-0550-8.

LYALL, R.; GECHEV, T. S. Multi-omics insights into the evolution of angiosperm resurrection plants. Annual Plant Reviews online, v. 3, n. 4, p. 77–110, 2020. DOI: https://doi.org/10.1002/9781119312994.apr0730.

LYNCH, M.; CONERY, J. S. The origins of genome complexity. Science, v. 302, n. 5647, p. 1401–1404, 2003. DOI: https://doi.org/10.1126/science.1089370.

LYNCH, M.; FORCE, A. The probability of duplicate gene preservation by subfunctionalization. Genetics, v. 154, n. 1, p. 459–473, 2000. DOI: https://doi.org/10.1093/genetics/154.1.459.

MINH, B. Q. et al. IQ-TREE 2: new models and efficient methods for phylogenetic inference in the genomic era. Molecular Biology and Evolution, v. 37, n. 5, p. 1530–1534, 2020. DOI: https://doi.org/10.1093/molbev/msaa015.

MURTHY, S. E. et al. OSCA/TMEM63 are an evolutionarily conserved family of mechanically activated ion channels. eLife, v. 7, e41844, 2018. DOI: https://doi.org/10.7554/eLife.41844.

PANCHY, N.; LEHTI-SHIU, M.; SHIU, S. H. Evolution of gene duplication in plants. Plant Physiology, v. 171, n. 4, p. 2294–2316, 2016. DOI: https://doi.org/10.1104/pp.16.00523.

PINTO, O. H. B. et al. Seasonal bacterial profiles of *Vellozia* with distinct drought adaptations in the megadiverse campos rupestres. Scientific Data, v. 12, art. 636, 2025. DOI: https://doi.org/10.1038/s41597-025-04984-z.

QU, J. et al. Comparative transcriptomics reveals the difference in early endosperm development between maize with different amylose contents. PeerJ, v. 7, e7528, 2019. DOI: https://doi.org/10.7717/peerj.7528.

QUINLAN, A. R.; HALL, I. M. BEDTools: a flexible suite of utilities for comparing genomic features. Bioinformatics, v. 26, n. 6, p. 841–842, 2010. DOI: https://doi.org/10.1093/bioinformatics/btq033.

SHAN, F. et al. Evolutionary analysis of the OSCA gene family in sunflower (*Helianthus annuus* L.) and expression analysis under NaCl stress. PeerJ, v. 11, e15089, 2023. DOI: https://doi.org/10.7717/peerj.15089.

STRASBURG, J. L. et al. Effective population size is positively correlated with levels of adaptive divergence among annual sunflowers. Molecular Biology and Evolution, v. 28, n. 4, p. 1569–1580, 2011. DOI: https://doi.org/10.1093/molbev/msq342.

SUYAMA, M.; TORRENTS, D.; BORK, P. PAL2NAL: robust conversion of protein sequence alignments into the corresponding codon alignments. Nucleic Acids Research, v. 34, supl. 2, p. W609–W612, 2006. DOI: https://doi.org/10.1093/nar/gkl315.

SZKLARCZYK, D. et al. The STRING database in 2023: protein–protein association networks and functional enrichment analyses for any sequenced genome of interest. Nucleic Acids Research, v. 51, n. D1, p. D638–D646, 2023. DOI: https://doi.org/10.1093/nar/gkac1000.

TANG, H. et al. Synteny and collinearity in plant genomes. Science, v. 320, n. 5875, p. 486–488, 2008. DOI: https://doi.org/10.1126/science.1153917.

TEODORO, G. S. et al. Desiccation tolerance implies costs to productivity but allows survival under extreme drought conditions in Velloziaceae species in campos rupestres. Environmental and Experimental Botany, v. 189, art. 104556, 2021. DOI: https://doi.org/10.1016/envexpbot.2021.104556.

VIEIRA, E. A. et al. Water retention and metabolic changes improve desiccation tolerance in *Barbacenia graminifolia* (Velloziaceae). Physiologia Plantarum, v. 174, n. 5, e13783, 2022. DOI: https://doi.org/10.1111/ppl.13783.

VIEIRA, E. A. et al. Surviving water scarcity: seasonal contrasts in drought and desiccation tolerance of co-occurring *Barbacenia gentianoides* and *Vellozia* caruncularis. Frontiers in Plant Science, v. 16, art. 1642013, 2025. DOI: https://doi.org/10.3389/fpls.2025.1642013.

WERTHEIM, J. O. et al. RELAX: detecting relaxed selection in a phylogenetic framework. Molecular Biology and Evolution, v. 32, n. 3, p. 820–832, 2015. DOI: https://doi.org/10.1093/molbev/msu400.

WIBERG, R. A. W.; BRAND, J. N.; SCHÄRER, L. Faster Rates of Molecular Sequence Evolution in Reproduction-Related Genes and in Species with Hypodermic Sperm Morphologies. Molecular Biology and Evolution, v. 38, n. 12, p. 5685–5703, 2021. DOI: https://doi.org/10.1093/molbev/msab247.

YANG, Z. PAML 4: phylogenetic analysis by maximum likelihood. Molecular Biology and Evolution, v. 24, n. 8, p. 1586–1591, 2007. DOI: https://doi.org/10.1093/molbev/msm088.

YANG, Z.; NIELSEN, R. Estimating synonymous and nonsynonymous substitution rates under realistic evolutionary models. Molecular Biology and Evolution, v. 17, n. 1, p. 32–43, 2000. DOI: https://doi.org/10.1093/oxfordjournals.molbev.a026236.

YIN, L. et al. Genome-wide analysis of OSCA gene family members in *Vigna radiata* and their involvement in the osmotic response. BMC Plant Biology, v. 21, art. 408, 2021. DOI: https://doi.org/10.1186/s12870-021-03184-2.

YUAN, F. et al. OSCA1 mediates osmotic-stress-evoked Ca2+ increases vital for osmosensing in Arabidopsis. Nature, v. 514, n. 7522, p. 367–371, 2014. DOI: https://doi.org/10.1038/nature13593.

ZHAI, Y. et al. Functional analysis of rice OSCA genes overexpressed in the Arabidopsis osca1 mutant. Plant Cell Reports, v. 40, p. 1073–1087, 2021. DOI: https://doi.org/10.1007/s00299-021-02662-y.

ZHANG, M. et al. Structure of the mechanosensitive OSCA channels. Nature Structural & Molecular Biology, v. 25, p. 850–858, 2018. DOI: https://doi.org/10.1038/s41594-018-0117-6.

ZHU, J. K. Abiotic Stress Signaling and Responses in Plants. Cell, v. 167, n. 2, p. 313–324, 2016. DOI: https://doi.org/10.1016/j.cell.2016.08.029.

---

# SUPPLEMENTARY MATERIAL

## Table S1. Audited OSCA gene catalog and predicted protein features

Coordinates were obtained from `03_synteny/data/{Vper,Vtub}.bed`, sequences from the OSCA FASTA files, molecular properties were recalculated with Biopython, and topology/domain counts were parsed from the raw InterProScan output. TMHMM and Phobius are independent predictions and are therefore reported separately.

| Gene | Transcript | Chr | Start (1-based) | End (1-based) | Strand | Length (aa) | MW (kDa) | pI | TMHMM TMHs | Phobius TMHs | Pfam domains | PANTHER |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VpOSCA1.1 | Vper.hapA.v1.chr4A.g117080.t1 | chr4A | 11237809 | 11254982 | - | 824 | 94.61 | 9.293 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA1.2 | Vper.hapA.v1.chr9A.g255760.t1 | chr9A | 17564348 | 17578689 | - | 796 | 90.59 | 8.747 | 8 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA1.3 | Vper.hapA.v1.chr7A.g186390.t1 | chr7A | 1154965 | 1162617 | + | 784 | 90.92 | 9.168 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA1.4 | Vper.hapA.v1.chr7A.g186400.t1 | chr7A | 1165819 | 1173766 | + | 737 | 84.85 | 8.941 | 7 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA1.5 | Vper.hapA.v1.chr7A.g186410.t1 | chr7A | 1190164 | 1199238 | + | 777 | 89.06 | 9.332 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA2.1 | Vper.hapA.v1.chr5A.g140750.t1 | chr5A | 1645548 | 1653691 | + | 740 | 84.05 | 8.873 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA2.2 | Vper.hapA.v1.chr1A.g021690.t1 | chr1A | 21367424 | 21371278 | - | 478 | 54.42 | 9.464 | 6 | 7 | PF02714;PF14703 | PTHR13018 |
| VpOSCA2.3 | Vper.hapA.v1.chr1A.g013600.t1 | chr1A | 13332253 | 13336746 | + | 718 | 81.89 | 9.067 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA2.4a | Vper.hapA.v1.chr1A.g023030.t1 | chr1A | 22689053 | 22697439 | + | 639 | 72.62 | 8.823 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA2.4b | Vper.hapA.v1.chr1A.g023020.t1 | chr1A | 22678817 | 22687760 | + | 662 | 75.23 | 8.233 | 11 | 11 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA2.5 | Vper.hapA.v1.chr9A.g257040.t1 | chr9A | 18576255 | 18590260 | - | 636 | 72.22 | 8.664 | 10 | 11 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA3.1 | Vper.hapA.v1.chr1A.g020450.t1 | chr1A | 20008266 | 20014313 | + | 734 | 83.15 | 9.335 | 9 | 10 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA3.2 | Vper.hapA.v1.chr5A.g142080.t1 | chr5A | 2668390 | 2675373 | - | 733 | 83.16 | 9.444 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA4.1 | Vper.hapA.v1.chr8A.g231320.t1 | chr8A | 20598463 | 20602234 | - | 802 | 89.81 | 6.553 | 10 | 10 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA1.1 | Vtub.hapA.v1.chr4A.g106800.t1 | chr4A | 10819228 | 10835638 | - | 766 | 87.63 | 9.117 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA1.2 | Vtub.hapA.v1.chr9A.g230740.t1 | chr9A | 17719980 | 17728315 | - | 485 | 55.12 | 8.951 | 5 | 6 | PF02714;PF14703 | PTHR13018 |
| VtOSCA1.3 | Vtub.hapA.v1.chr7A.g166590.t1 | chr7A | 1018481 | 1027560 | + | 869 | 100.53 | 8.848 | 12 | 11 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA1.4 | Vtub.hapA.v1.chr7A.g166600.t1 | chr7A | 1029793 | 1039945 | + | 833 | 96.53 | 9.366 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA1.5 | Vtub.hapA.v1.chr7A.g166610.t1 | chr7A | 1049542 | 1057767 | + | 760 | 87.54 | 9.482 | 10 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA2.1 | Vtub.hapA.v1.chr5A.g127830.t1 | chr5A | 1496337 | 1503868 | + | 676 | 76.69 | 8.584 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA2.2 | Vtub.hapA.v1.chr1A.g019410.t1 | chr1A | 20232005 | 20238727 | - | 745 | 84.87 | 9.31 | 9 | 8 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA2.3 | Vtub.hapA.v1.chr1A.g012080.t1 | chr1A | 12783203 | 12787679 | + | 718 | 81.88 | 9.023 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA2.4 | Vtub.hapA.v1.chr1A.g020650.t1 | chr1A | 21645213 | 21654612 | + | 750 | 85.49 | 8.905 | 11 | 11 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA2.5 | Vtub.hapA.v1.chr9A.g231910.t1 | chr9A | 18668637 | 18684281 | - | 634 | 71.83 | 8.669 | 10 | 11 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA3.1 | Vtub.hapA.v1.chr1A.g018250.t1 | chr1A | 18922459 | 18928500 | + | 734 | 83.29 | 9.451 | 9 | 10 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA3.2 | Vtub.hapA.v1.chr5A.g129040.t1 | chr5A | 2457575 | 2466320 | - | 772 | 87.49 | 9.462 | 9 | 10 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA4.1 | Vtub.hapA.v1.chr8A.g207990.t1 | chr8A | 24477669 | 24481020 | - | 802 | 89.96 | 6.523 | 10 | 11 | PF02714;PF13967;PF14703 | PTHR13018 |
| XsOSCA1.1 | MP011677 | - | - | - | - | 766 | 87.94 | 9.237 | - | - | PF02714;PF13967;PF14703 | PTHR13018 |
| XsOSCA2.1 | MP002111 | - | - | - | - | 744 | 84.54 | 9.110 | - | - | PF02714;PF13967;PF14703 | PTHR13018 |
| XsOSCA2.2 | MP013956 | - | - | - | - | 681 | 77.01 | 8.893 | - | - | PF02714;PF13967;PF14703 | PTHR13018 |
| XsOSCA2.3 | MP001327 | - | - | - | - | 718 | 81.83 | 9.000 | - | - | PF02714;PF13967;PF14703 | PTHR13018 |
| XsOSCA2.4 | MP002250 | - | - | - | - | 337 | 38.55 | 8.855 | - | - | PF02714;PF13967;PF14703 | PTHR13018 |
| XsOSCA3.1 | MP001991 | - | - | - | - | 734 | 83.13 | 9.368 | - | - | PF02714;PF13967;PF14703 | PTHR13018 |
| XsOSCA3.2 | MP014080 | - | - | - | - | 750 | 85.37 | 9.417 | - | - | PF02714;PF13967;PF14703 | PTHR13018 |
| XsOSCA4.1 | MP022802 | - | - | - | - | 804 | 90.05 | 6.901 | - | - | PF02714;PF13967;PF14703 | PTHR13018 |

## Table S2. OSCA pairs present in the raw MCScan anchor file

These 12 rows are OSCA-OSCA anchors in `03_synteny/intergenomic/intermediates/Vper.Vtub.anchors`. They must not be read as 12 strict one-to-one orthologs: one row crosses chromosomes and corresponds to the excluded paleoduplication, and one row links differently named members of the chromosome 7A cluster. Eleven anchors connect the same chromosome in both assemblies.

| V. peripherica transcript | V. tubiflora transcript | V. peripherica gene | V. tubiflora gene |
|---|---|---|---|
| Vper.hapA.v1.chr1A.g013600.t1 | Vtub.hapA.v1.chr1A.g012080.t1 | VpOSCA2.3 | VtOSCA2.3 |
| Vper.hapA.v1.chr1A.g020450.t1 | Vtub.hapA.v1.chr1A.g018250.t1 | VpOSCA3.1 | VtOSCA3.1 |
| Vper.hapA.v1.chr1A.g021690.t1 | Vtub.hapA.v1.chr1A.g019410.t1 | VpOSCA2.2 | VtOSCA2.2 |
| Vper.hapA.v1.chr1A.g023020.t1 | Vtub.hapA.v1.chr1A.g020650.t1 | VpOSCA2.4b | VtOSCA2.4 |
| Vper.hapA.v1.chr4A.g117080.t1 | Vtub.hapA.v1.chr4A.g106800.t1 | VpOSCA1.1 | VtOSCA1.1 |
| Vper.hapA.v1.chr5A.g140750.t1 | Vtub.hapA.v1.chr1A.g019410.t1 | VpOSCA2.1 | VtOSCA2.2 |
| Vper.hapA.v1.chr5A.g140750.t1 | Vtub.hapA.v1.chr5A.g127830.t1 | VpOSCA2.1 | VtOSCA2.1 |
| Vper.hapA.v1.chr5A.g142080.t1 | Vtub.hapA.v1.chr5A.g129040.t1 | VpOSCA3.2 | VtOSCA3.2 |
| Vper.hapA.v1.chr7A.g186410.t1 | Vtub.hapA.v1.chr7A.g166600.t1 | VpOSCA1.5 | VtOSCA1.4 |
| Vper.hapA.v1.chr8A.g231320.t1 | Vtub.hapA.v1.chr8A.g207990.t1 | VpOSCA4.1 | VtOSCA4.1 |
| Vper.hapA.v1.chr9A.g255760.t1 | Vtub.hapA.v1.chr9A.g230740.t1 | VpOSCA1.2 | VtOSCA1.2 |
| Vper.hapA.v1.chr9A.g257040.t1 | Vtub.hapA.v1.chr9A.g231910.t1 | VpOSCA2.5 | VtOSCA2.5 |

## Table S3. PAL2NAL/PAML YN00 pairwise evolutionary rate estimates

| Pair | Ks | Ka | omega |
|---|---|---|---|
| VpOSCA1.1_VtOSCA1.1 | 0.0371 | 0.0124 | 0.3332 |
| VpOSCA1.2_VtOSCA1.2 | 0.0987 | 0.0416 | 0.4211 |
| VpOSCA1.3_VtOSCA1.3 | 0.0761 | 0.023 | 0.3015 |
| VpOSCA1.4_VtOSCA1.4 | 0.1094 | 0.0877 | 0.8015 |
| VpOSCA1.5_VtOSCA1.5 | 0.098 | 0.0684 | 0.6979 |
| VpOSCA2.1_VtOSCA2.1 | 0.0757 | 0.0227 | 0.2993 |
| VpOSCA2.2_VtOSCA2.2 | 0.0912 | 0.0634 | 0.6947 |
| VpOSCA2.3_VtOSCA2.3 | 0.0859 | 0.0046 | 0.053 |
| VpOSCA2.4a_VpOSCA2.4b | 0.1172 | 0.0442 | 0.377 |
| VpOSCA2.4a_VtOSCA2.4 | 0.1215 | 0.0363 | 0.2985 |
| VpOSCA2.4b_VtOSCA2.4 | 0.0343 | 0.0177 | 0.5155 |
| VpOSCA2.5_VtOSCA2.5 | 0.0589 | 0.0177 | 0.3011 |
| VpOSCA3.1_VtOSCA3.1 | 0.0471 | 0.0234 | 0.4971 |
| VpOSCA3.2_VtOSCA3.2 | 0.0634 | 0.0216 | 0.3403 |
| VpOSCA4.1_VtOSCA4.1 | 0.0775 | 0.0124 | 0.1601 |

## Table S4. HyPhy RELAX selection intensity across the analyzed OSCA ortholog set

The analysis used the `gap20` codon alignment of the full OSCA family (27 sequences, 639 filtered codons). *V. peripherica* branches were designated as Reference and *V. tubiflora* branches as Test.

| Dataset | Codons | K | LRT | p-value | Reference branches | Test branches | Unclassified branches |
|---|---|---|---|---|---|---|---|
| Analyzed OSCA Ortholog Set | 639 | 0.7064 | 12.8509 | 0.000337 | 14 | 13 | 24 |

## Table S5. Tissue transcript abundance, DESeq2 contrasts, and STRING topology

Means are DESeq2-normalized counts within each species. Adjusted p values are transcriptome-wide Benjamini-Hochberg values for each contrast. Network metrics were recalculated from the saved undirected STRING edge tables. A zero degree for a query with no returned edge does not mean that it contributed to the reported endpoint-based node count.

| Gene | Returned in network | Degree | Clustering | Leaf mean | Stem mean | Root mean | Root vs leaf log~2~FC | Root vs leaf padj | Root vs stem log~2~FC | Root vs stem padj | Stem vs leaf log~2~FC | Stem vs leaf padj |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VpOSCA1.1 | True | 11 | 0.436364 | 782.493 | 215.606 | 283.503 | -1.39775 | 0.0252138 | 0.385571 | 1 | -1.78332 | 0.00301629 |
| VpOSCA1.2 | True | 18 | 0.575163 | 0.865729 | 31.2788 | 18.7347 | 4.35684 | 0.0115214 | -0.94365 | 1 | 5.30049 | 0.00141018 |
| VpOSCA1.3 | True | 1 | 0 | 102.105 | 266.265 | 282.887 | 1.37418 | 0.0928902 | 0.0639585 | 1 | 1.31022 | 0.11503 |
| VpOSCA1.4 | True | 1 | 0 | 9.6305 | 10.6598 | 9.68648 | 0.519403 | 0.817586 | 0.706704 | 1 | -0.187301 | 0.941141 |
| VpOSCA1.5 | True | 1 | 0 | 22.1649 | 0.26282 | 12.6331 | -1.03394 | 0.740306 | 2.57367 | 1 | -3.60762 | 0.18595 |
| VpOSCA2.1 | False | 0 | 0 | 135.416 | 93.1436 | 123.917 | -0.158416 | 0.823551 | 0.319853 | 1 | -0.47827 | 0.451303 |
| VpOSCA2.2 | False | 0 | 0 | 525.562 | 352.933 | 394.074 | -0.451889 | 0.440597 | 0.144816 | 1 | -0.596705 | 0.293544 |
| VpOSCA2.3 | False | 0 | 0 | 0.739602 | 15.6739 | 12.2076 | 4.21532 | 0.0401675 | 0.090009 | 1 | 4.12531 | 0.0460652 |
| VpOSCA2.4a | True | 2 | 1 | 280.762 | 543.219 | 399.869 | 0.541817 | 0.429422 | -0.591014 | 1 | 1.13283 | 0.0595769 |
| VpOSCA2.4b | True | 2 | 1 | 576.126 | 695.656 | 711.961 | 0.346628 | 0.566521 | 0.01681 | 1 | 0.329818 | 0.601002 |
| VpOSCA2.5 | True | 4 | 0 | 379.124 | 305.621 | 197.65 | -0.832986 | 0.237169 | -0.580895 | 1 | -0.252091 | 0.774947 |
| VpOSCA3.1 | True | 4 | 0 | 2696.46 | 769.969 | 1007.29 | -1.5623 | 0.00199878 | 0.120329 | 1 | -1.68263 | 0.00075662 |
| VpOSCA3.2 | True | 4 | 0 | 82.9973 | 116.959 | 111.328 | 0.635932 | 0.640002 | -0.304857 | 1 | 0.940789 | 0.477818 |
| VpOSCA4.1 | True | 19 | 0.0409357 | 242.219 | 227.43 | 147.6 | -0.819373 | 0.245954 | -0.763611 | 0.994926 | -0.0557619 | 0.954541 |
| VtOSCA1.1 | True | 13 | 0.5 | 658.212 | 153.82 | 302.037 | -1.17583 | 0.0473601 | 0.888008 | 0.187653 | -2.06383 | 2.69388e-06 |
| VtOSCA1.2 | True | 18 | 0.640523 | 0 | 5.80042 | 67.6767 | 8.26527 | 0.000167521 | 2.89609 | 0.192866 | 5.36918 | 0.0088198 |
| VtOSCA1.3 | True | 3 | 0 | 97.0986 | 226.286 | 410.114 | 2.30381 | 0.0662839 | 1.0189 | 0.517513 | 1.28491 | 0.242416 |
| VtOSCA1.4 | True | 3 | 0 | 3.27811 | 34.3111 | 4.34668 | 2.70776 | 0.275657 | -1.03625 | 0.712201 | 3.74401 | 0.0220064 |
| VtOSCA1.5 | True | 3 | 0 | 8.12599 | 4.02131 | 6.52002 | -0.390364 | 0.911289 | 0.421535 | 0.914285 | -0.811899 | 0.739772 |
| VtOSCA2.1 | False | 0 | 0 | 132.194 | 120.286 | 135.586 | -0.0159172 | 0.985008 | 0.132161 | 0.876313 | -0.148078 | 0.796684 |
| VtOSCA2.2 | False | 0 | 0 | 542.43 | 302.931 | 483.779 | -0.219651 | 0.714538 | 0.56822 | 0.288809 | -0.787871 | 0.0330851 |
| VtOSCA2.3 | False | 0 | 0 | 1.35782 | 1.89484 | 11.3014 | 1.76325 | 0.579418 | 1.8416 | 0.585927 | -0.0783476 | 0.98419 |
| VtOSCA2.4 | True | 5 | 0.1 | 930.427 | 805.862 | 1566.78 | 0.801609 | 0.0255357 | 1.0112 | 0.00622962 | -0.209587 | 0.555531 |
| VtOSCA2.5 | True | 7 | 0.047619 | 380.649 | 126.675 | 249.018 | -0.452692 | 0.411536 | 1.09995 | 0.0289874 | -1.55264 | 1.10012e-05 |
| VtOSCA3.1 | True | 4 | 0 | 3221.71 | 392.071 | 1030.8 | -1.37785 | 0.173284 | 1.53396 | 0.147245 | -2.91181 | 5.31353e-05 |
| VtOSCA3.2 | True | 4 | 0 | 19.3689 | 14.0032 | 138.743 | 4.4166 | 0.0103181 | 3.5682 | 0.0608347 | 0.848401 | 0.648987 |
| VtOSCA4.1 | True | 13 | 0.0384615 | 244.619 | 83.6536 | 322.668 | 0.397784 | 0.608887 | 1.84076 | 0.00338089 | -1.44298 | 0.00340788 |

## Table S6. Selected PlantCARE motif occurrence counts in 2-kb upstream regions

Counts were generated after normalizing case variants of identical motif families (e.g., `G-box`/`G-Box`, `MYC`/`Myc`, and `MYB`/`Myb`) and merging overlapping occurrences of the same motif kind across 2-kb regions immediately upstream of annotated transcript boundaries. Motif presence is a computational annotation and does not establish binding or regulation.

| Species | Gene | ABRE | CGTCA-motif | TGACG-motif | TCA-element | MBS | LTR | ARE | TC-rich repeats | W box | G-box | Box 4 | GT1-motif | MYC | MYB | RY-element | TATA-box | CAAT-box |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vper | VpOSCA1.1 | 2 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 9 | 1 | 3 | 3 | 0 | 18 | 32 |
| Vper | VpOSCA1.2 | 1 | 1 | 1 | 0 | 1 | 4 | 2 | 0 | 0 | 3 | 2 | 1 | 3 | 3 | 0 | 14 | 28 |
| Vper | VpOSCA1.3 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 3 | 1 | 1 | 1 | 0 | 17 | 28 |
| Vper | VpOSCA1.4 | 1 | 0 | 0 | 1 | 2 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 5 | 0 | 31 | 32 |
| Vper | VpOSCA1.5 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 3 | 2 | 0 | 19 | 24 |
| Vper | VpOSCA2.1 | 6 | 1 | 1 | 0 | 2 | 0 | 0 | 1 | 0 | 6 | 4 | 1 | 4 | 8 | 0 | 22 | 24 |
| Vper | VpOSCA2.2 | 2 | 0 | 0 | 1 | 1 | 1 | 3 | 0 | 0 | 3 | 3 | 0 | 8 | 9 | 1 | 17 | 33 |
| Vper | VpOSCA2.3 | 1 | 2 | 2 | 0 | 0 | 0 | 1 | 1 | 1 | 3 | 10 | 0 | 1 | 2 | 0 | 42 | 28 |
| Vper | VpOSCA2.4a | 2 | 2 | 2 | 0 | 1 | 2 | 4 | 0 | 1 | 2 | 2 | 0 | 4 | 3 | 0 | 18 | 34 |
| Vper | VpOSCA2.4b | 4 | 2 | 2 | 0 | 0 | 1 | 1 | 0 | 3 | 4 | 5 | 0 | 4 | 2 | 0 | 26 | 30 |
| Vper | VpOSCA2.5 | 2 | 4 | 4 | 1 | 1 | 6 | 1 | 0 | 1 | 2 | 4 | 2 | 6 | 4 | 0 | 26 | 30 |
| Vper | VpOSCA3.1 | 3 | 2 | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 3 | 1 | 1 | 2 | 7 | 0 | 20 | 29 |
| Vper | VpOSCA3.2 | 6 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 2 | 7 | 2 | 0 | 1 | 4 | 0 | 13 | 29 |
| Vper | VpOSCA4.1 | 2 | 1 | 1 | 0 | 2 | 1 | 3 | 1 | 0 | 2 | 3 | 1 | 10 | 5 | 0 | 19 | 35 |
| Vtub | VtOSCA1.1 | 5 | 2 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 5 | 9 | 0 | 7 | 2 | 0 | 31 | 35 |
| Vtub | VtOSCA1.2 | 0 | 0 | 0 | 2 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 3 | 5 | 5 | 0 | 13 | 33 |
| Vtub | VtOSCA1.3 | 3 | 3 | 3 | 0 | 1 | 0 | 1 | 0 | 0 | 3 | 1 | 1 | 3 | 3 | 0 | 26 | 32 |
| Vtub | VtOSCA1.4 | 3 | 2 | 2 | 0 | 1 | 1 | 1 | 1 | 1 | 2 | 0 | 1 | 0 | 4 | 0 | 26 | 20 |
| Vtub | VtOSCA1.5 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 6 | 1 | 1 | 2 | 0 | 28 | 30 |
| Vtub | VtOSCA2.1 | 7 | 3 | 3 | 0 | 2 | 1 | 2 | 1 | 1 | 10 | 5 | 4 | 0 | 5 | 0 | 23 | 30 |
| Vtub | VtOSCA2.2 | 3 | 4 | 4 | 0 | 0 | 3 | 1 | 0 | 1 | 3 | 1 | 0 | 6 | 2 | 0 | 20 | 24 |
| Vtub | VtOSCA2.3 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 3 | 0 | 1 | 6 | 0 | 20 | 26 |
| Vtub | VtOSCA2.4 | 6 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 1 | 6 | 3 | 0 | 2 | 4 | 0 | 27 | 25 |
| Vtub | VtOSCA2.5 | 3 | 1 | 1 | 1 | 1 | 2 | 0 | 1 | 0 | 4 | 4 | 1 | 9 | 6 | 0 | 30 | 25 |
| Vtub | VtOSCA3.1 | 2 | 1 | 1 | 0 | 1 | 1 | 5 | 0 | 0 | 2 | 1 | 0 | 2 | 5 | 0 | 12 | 37 |
| Vtub | VtOSCA3.2 | 2 | 2 | 2 | 1 | 1 | 2 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 4 | 0 | 15 | 30 |
| Vtub | VtOSCA4.1 | 0 | 1 | 1 | 1 | 2 | 1 | 3 | 1 | 1 | 0 | 1 | 2 | 6 | 4 | 0 | 11 | 33 |

## Table S7. Functional classification and consensus sequences of annotated cis-regulatory elements

Classification framework adapted from Qu et al. (2019) and PlantCARE functional annotation standards. Motifs correspond to the curated categories analyzed across the 2-kb promoter regions of *OSCA* genes in *V. peripherica* and *V. tubiflora*.

| Functional Category | Motif Name | Consensus / Representative Sequence | Predicted Biological Function / Responsiveness | References |
|---|---|---|---|---|
| Phytohormone Signaling | ABRE | ACGTG / TACGTG / CCGTG | Abscisic acid (ABA) responsiveness; dehydration and osmotic stress | Lescot et al. (2002); Qu et al. (2019) |
| Phytohormone Signaling | CGTCA-motif | CGTCA | Methyl jasmonate (MeJA) responsiveness | Lescot et al. (2002) |
| Phytohormone Signaling | TGACG-motif | TGACG | Methyl jasmonate (MeJA) responsiveness | Lescot et al. (2002) |
| Phytohormone Signaling | TCA-element | CCATCTTTTT / CAGAAAAGGA | Salicylic acid (SA) responsiveness; defense and stress signaling | Lescot et al. (2002) |
| Abiotic Stress Response | MBS | TAACTG / CAACTG | MYB binding site involved in drought inducibility and osmotic regulation | Lescot et al. (2002) |
| Abiotic Stress Response | LTR | CCGAAA | Low-temperature and cold responsiveness | Lescot et al. (2002) |
| Abiotic Stress Response | ARE | TGGTTT / AAACCA | Anaerobic induction essential for hypoxia-induced expression | Lescot et al. (2002) |
| Abiotic Stress Response | TC-rich repeats | ATTTTCTTCA / GTTTTCTTAC | Defense and stress responsiveness | Lescot et al. (2002) |
| Abiotic Stress Response | W box | TTGACC | WRKY transcription factor binding site; pathogen defense and wounding | Lescot et al. (2002) |
| Growth & Development | MYC | CANNTG (e.g., CACATG, CATGTG) | bHLH transcription factor binding site; drought, ABA, and cold response | Lescot et al. (2002) |
| Growth & Development | MYB | CAACCA / WAACCA / YAACKG | MYB transcription factor binding site; development and stress response | Lescot et al. (2002) |
| Growth & Development | RY-element | CATGCA | Seed-specific and embryo-development regulation | Lescot et al. (2002) |
| Light Responsiveness | G-box | CACGTG / CACGTC | Light responsiveness and multi-factor stress signaling hub | Lescot et al. (2002) |
| Light Responsiveness | Box 4 | ATTAAT | Conserved DNA module involved in light responsiveness | Lescot et al. (2002) |
| Light Responsiveness | GT1-motif | GGTTAA | Light-responsive element; GT-1 factor binding | Lescot et al. (2002) |
| Core Promoter Elements | TATA-box | TATA(A/T)A(A/T) | Core promoter element initiating transcription | Lescot et al. (2002) |
| Core Promoter Elements | CAAT-box | CAAT / CAAAT / CCAAT | Common cis-acting element in promoter and enhancer regions | Lescot et al. (2002) |


## Table S8. Gene Ontology and KEGG pathway functional enrichment of STRING networks

Functional enrichment results retrieved via the STRING v12 API for the reconstructed OSCA interactomes of *V. peripherica* and *V. tubiflora*. Only terms with a false discovery rate (FDR) < 0.05 in at least one species are shown. Genes/Background indicates observed query proteins vs total annotated background proteins in the genome assembly.

| Category | Term ID | Description | *V. peripherica* Genes | *V. peripherica* Background | *V. peripherica* FDR | *V. tubiflora* Genes | *V. tubiflora* Background | *V. tubiflora* FDR |
|---|---|---|---|---|---|---|---|---|
| Biological Process (GO) | GO:0016052 | Carbohydrate catabolic process | 15 | 239 | 3.48e-14 | 16 | 245 | 1.81e-15 |
| Biological Process (GO) | GO:0005975 | Carbohydrate metabolic process | 16 | 1029 | 8.12e-07 | - | - | - |
| Biological Process (GO) | GO:0009056 | Catabolic process | 19 | 1779 | 3.76e-06 | 19 | 1619 | 1.20e-06 |
| Biological Process (GO) | GO:0008219 | Cell death | 4 | 88 | 8.10e-03 | - | - | - |
| Biological Process (GO) | GO:0044275 | Cellular carbohydrate catabolic process | 7 | 65 | 3.31e-07 | 7 | 62 | 2.20e-07 |
| Biological Process (GO) | GO:0044262 | Cellular carbohydrate metabolic process | 8 | 448 | 1.40e-03 | - | - | - |
| Biological Process (GO) | GO:0044248 | Cellular catabolic process | 11 | 1300 | 1.92e-02 | 10 | 1142 | 3.82e-02 |
| Biological Process (GO) | GO:0006073 | Cellular glucan metabolic process | 6 | 184 | 8.50e-04 | 6 | 181 | 1.00e-03 |
| Biological Process (GO) | GO:0044247 | Cellular polysaccharide catabolic process | 6 | 39 | 7.40e-07 | 6 | 37 | 5.13e-07 |
| Biological Process (GO) | GO:0009987 | Cellular process | 50 | 15523 | 1.18e-02 | - | - | - |
| Biological Process (GO) | GO:0051085 | Chaperone cofactor-dependent protein refolding | 3 | 53 | 2.97e-02 | - | - | - |
| Biological Process (GO) | GO:0046352 | Disaccharide catabolic process | 4 | 15 | 2.70e-05 | 4 | 15 | 2.89e-05 |
| Biological Process (GO) | GO:0009251 | Glucan catabolic process | 6 | 44 | 1.02e-06 | 6 | 41 | 6.02e-07 |
| Biological Process (GO) | GO:0005980 | Glycogen catabolic process | 2 | 2 | 4.40e-03 | 2 | 2 | 5.10e-03 |
| Biological Process (GO) | GO:0005977 | Glycogen metabolic process | 3 | 10 | 6.30e-04 | 3 | 10 | 8.10e-04 |
| Biological Process (GO) | GO:0006559 | L-phenylalanine catabolic process | 2 | 13 | 4.83e-02 | - | - | - |
| Biological Process (GO) | GO:0051179 | Localization | - | - | - | 19 | 3175 | 1.11e-02 |
| Biological Process (GO) | GO:0009057 | Macromolecule catabolic process | 15 | 911 | 1.04e-06 | 16 | 810 | 4.98e-08 |
| Biological Process (GO) | GO:0034051 | Negative regulation of plant-type hypersensitive response | 2 | 6 | 1.74e-02 | 2 | 7 | 2.39e-02 |
| Biological Process (GO) | GO:1901575 | Organic substance catabolic process | 18 | 1566 | 3.64e-06 | 18 | 1432 | 1.20e-06 |
| Biological Process (GO) | GO:0000272 | Polysaccharide catabolic process | 14 | 137 | 1.54e-15 | 15 | 132 | 2.10e-17 |
| Biological Process (GO) | GO:0042026 | Protein refolding | 3 | 41 | 1.74e-02 | - | - | - |
| Biological Process (GO) | GO:0005983 | Starch catabolic process | 4 | 13 | 1.78e-05 | 4 | 13 | 1.91e-05 |
| Biological Process (GO) | GO:0005987 | Sucrose catabolic process | 3 | 11 | 7.30e-04 | 3 | 11 | 9.20e-04 |
| Biological Process (GO) | GO:0006810 | Transport | 22 | 2899 | 5.54e-05 | 18 | 3001 | 1.67e-02 |
| Biological Process (GO) | GO:0006572 | Tyrosine catabolic process | 2 | 9 | 2.92e-02 | - | - | - |
| Biological Process (GO) | GO:1990961 | Xenobiotic detoxification by transmembrane export across the plasma membrane | 3 | 41 | 1.74e-02 | - | - | - |
| Molecular Function (GO) | GO:0004556 | Alpha-amylase activity | 3 | 5 | 6.93e-05 | 3 | 4 | 5.09e-05 |
| Molecular Function (GO) | GO:0016160 | Amylase activity | 9 | 13 | 3.22e-16 | 9 | 13 | 3.74e-16 |
| Molecular Function (GO) | GO:0102229 | Amylopectin maltohydrolase activity | 7 | 7 | 4.14e-13 | 8 | 8 | 3.61e-15 |
| Molecular Function (GO) | GO:0016161 | Beta-amylase activity | 6 | 8 | 9.95e-11 | 6 | 9 | 2.14e-10 |
| Molecular Function (GO) | GO:0005227 | Calcium activated cation channel activity | 11 | 15 | 5.64e-20 | 10 | 14 | 8.80e-18 |
| Molecular Function (GO) | GO:0008324 | Cation transmembrane transporter activity | - | - | - | 12 | 453 | 1.11e-07 |
| Molecular Function (GO) | GO:0008184 | Glycogen phosphorylase activity | 2 | 2 | 3.00e-03 | 2 | 2 | 3.00e-03 |
| Molecular Function (GO) | GO:0031072 | Heat shock protein binding | 3 | 68 | 4.66e-02 | - | - | - |
| Molecular Function (GO) | GO:0016787 | Hydrolase activity | 20 | 3299 | 3.00e-03 | 20 | 3013 | 1.00e-03 |
| Molecular Function (GO) | GO:0004553 | Hydrolase activity, hydrolyzing O-glycosyl compounds | 12 | 367 | 1.05e-08 | 13 | 353 | 6.88e-10 |
| Molecular Function (GO) | GO:0022890 | Inorganic cation transmembrane transporter activity | - | - | - | 11 | 415 | 5.69e-07 |
| Molecular Function (GO) | GO:0102250 | Linear malto-oligosaccharide phosphorylase activity | 2 | 2 | 3.00e-03 | 2 | 2 | 3.00e-03 |
| Molecular Function (GO) | GO:0008381 | Mechanosensitive ion channel activity | 3 | 13 | 6.50e-04 | 3 | 11 | 4.90e-04 |
| Molecular Function (GO) | GO:0102499 | SHG alpha-glucan phosphorylase activity | 2 | 2 | 3.00e-03 | 2 | 2 | 3.00e-03 |
| Molecular Function (GO) | GO:0022857 | Transmembrane transporter activity | 18 | 1496 | 6.84e-07 | 15 | 1642 | 4.90e-04 |
| Cellular Component (GO) | GO:0098588 | Bounding membrane of organelle | 9 | 970 | 2.35e-02 | - | - | - |
| Cellular Component (GO) | GO:0110165 | Cellular anatomical entity | 61 | 22201 | 7.60e-03 | 60 | 21115 | 8.80e-03 |
| Cellular Component (GO) | GO:0009507 | Chloroplast | 17 | 2378 | 7.60e-03 | - | - | - |
| Cellular Component (GO) | GO:0000793 | Condensed chromosome | - | - | - | 3 | 54 | 2.41e-02 |
| Cellular Component (GO) | GO:0000796 | Condensin complex | 2 | 7 | 1.25e-02 | 2 | 6 | 1.21e-02 |
| Cellular Component (GO) | GO:0005737 | Cytoplasm | 45 | 11248 | 6.10e-04 | 42 | 11428 | 8.80e-03 |
| Cellular Component (GO) | GO:0005886 | Plasma membrane | 17 | 2512 | 7.60e-03 | 16 | 2155 | 8.80e-03 |
| Cellular Component (GO) | GO:0009506 | Plasmodesma | 7 | 363 | 7.60e-03 | 7 | 343 | 8.80e-03 |
| Cellular Component (GO) | GO:0009536 | Plastid | 18 | 2652 | 7.60e-03 | - | - | - |
| KEGG Pathway | map01110 | Biosynthesis of secondary metabolites | 29 | 2417 | 7.10e-13 | 31 | 2196 | 7.61e-16 |
| KEGG Pathway | map01100 | Metabolic pathways | 30 | 5617 | 6.49e-05 | 32 | 5722 | 9.53e-06 |
| KEGG Pathway | map00500 | Starch and sucrose metabolism | 22 | 255 | 2.60e-26 | 23 | 248 | 3.57e-28 |
| KEGG Pathway | map00350 | Tyrosine metabolism | 3 | 66 | 2.07e-02 | - | - | - |
