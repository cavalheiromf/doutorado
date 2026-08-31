# CHAPTER 3: MACROEVOLUTIONARY DYNAMICS AND THE PAN-GONDWANAN ORIGIN OF DESICCATION TOLERANCE IN VELLOZIACEAE

**Doctoral Thesis:** Genomic and Regulatory Bases of Drought Adaptation in Velloziaceae  
**Candidate:** Mariana Feitosa Cavalheiro  
**Advisor:** Isabel Rodrigues Gerhardt  
**Institution:** Universidade Estadual de Campinas (UNICAMP)  

---

## ABSTRACT

Vegetative desiccation tolerance represents one of the most extreme ecophysiological adaptations in vascular plants. Within the monocot family Velloziaceae, species endemic to African inselbergs (*Xerophyta*) and South American rock outcrops (*Vellozia*) exhibit profound desiccation tolerance, yet the evolutionary polarity of this trait remains highly debated. Specifically, it remains unclear whether tolerance evolved convergently or constitutes a homologous ancestral state, and whether the evergreen strategy of species such as *Vellozia peripherica* represents a basal condition or a derived adaptation. To resolve this macroevolutionary enigma, we performed a comprehensive phylogenomic and gene family dynamic analysis across seven canonical proteomes, utilizing 16,532 inferred orthogroups and 1,424 strictly conserved single-copy orthologs. Divergence calibration supported a Pan-Gondwanan separation of the African and South American lineages. Stochastic birth-and-death modeling using CAFE5 revealed a massive, significant expansion of 126 gene families at the Velloziaceae common ancestral node (Node 13) prior to continental vicariance, establishing that the core molecular machinery for desiccation tolerance is a homologous synapomorphy inherited from the Gondwanan ancestor. Consequently, the evergreen, drought-avoidant strategy of *V. peripherica* is identified as a highly specialized, secondary derived state. This derived evergreen lifestyle incurs a severe genomic cost, reflected in the asymmetric expansion of 209 gene families in *V. peripherica* compared to 106 in the resurrection species *Vellozia tubiflora*. Functional profiling of the *V. peripherica* terminal expansions revealed massive proliferation of F-box ubiquitin ligase complexes, receptor-like kinases (RLKs), NLR/ZAR1 immune receptors, pentatricopeptide repeat proteins (PPRs), and cytochrome P450 monooxygenases. Together, these results demonstrate that abandoning ancestral anhydrobiosis to remain metabolically active in harsh microclimates requires pervasive genomic rewiring to continuously monitor membrane integrity, recycle damaged proteins, and suppress oxidative and pathogenic stress.

---

## 1. INTRODUCTION

Vegetative desiccation tolerance, often referred to as the resurrection phenotype, is a rare and extreme ecophysiological trait that allows a select group of angiosperms to survive the loss of over 95% of their total cellular water content (FARRANT et al., 2007). Unlike orthodox seeds, which possess developmental programs to undergo programmed dehydration, vegetative tissues of resurrection plants must continuously suppress dehydration-induced senescence, preserve membrane integrity during severe physical shrinkage, and prevent irreversible photo-oxidative damage to the photosynthetic apparatus (COSTA et al., 2017). Within the monocot order Pandanales, the family Velloziaceae stands out as a unique evolutionary model for understanding the acquisition and diversification of this complex phenotype. The family displays a remarkable disjunct biogeographical distribution, with desiccation-tolerant species dominating both the ancient inselbergs of Africa, primarily within the genus *Xerophyta*, and the highly specialized quartzitic rock outcrops (*campos rupestres*) of South America, predominantly within the genus *Vellozia* (ALCANTARA et al., 2018).

The biogeographical disjunction of Velloziaceae raises a fundamental evolutionary enigma regarding the origin of vegetative desiccation tolerance. Historically, it has been debated whether the resurrection phenotype in African and South American lineages evolved independently through convergent evolution (homoplasy) driven by similar selective pressures in functionally analogous rock outcrop environments, or if the trait was already present in their common ancestor prior to the breakup of the supercontinent Gondwana (homology). Resolving this polarity requires high-resolution phylogenomic reconstructions integrated with molecular dating and stochastic modeling of gene family expansions and contractions across deep evolutionary time.

Complicating this macroevolutionary landscape is the striking intrageneric ecophysiological divergence observed within the South American genus *Vellozia*. While the majority of *Vellozia* species, such as *Vellozia tubiflora*, are poikilochlorophyllous resurrection plants that dismantle their photosynthetic apparatus and enter metabolic quiescence during the dry season, sympatric congeneric species have adopted diametrically opposed strategies (MELLO-SILVA, 2011). *Vellozia peripherica*, for instance, is an evergreen, drought-sensitive species that co-occurs in the exact same harsh *campos rupestres* microhabitats but actively avoids desiccation by maintaining hydrated leaf tissues, stomatal control, and continuous carbon assimilation throughout extended dry periods (ALCANTARA et al., 2015). The evolutionary directionality of these traits—whether the evergreen strategy represents a primitive basal condition that failed to acquire desiccation tolerance, or a highly derived, specialized innovation that secondarily lost the ancestral capacity for anhydrobiosis—remains a critical unanswered question in plant ecophysiology.

The continuous advancement of comparative genomics provides the computational framework necessary to decode the molecular footprints of these macroevolutionary transitions. Stochastic birth-and-death models, which estimate the rates of gene family expansion and contraction across phylogenetic trees, can pinpoint exact nodes where critical genetic toolkits were forged or discarded (MENDES et al., 2020). If desiccation tolerance is a convergent trait, distinct lineage-specific expansions in the African and South American terminal branches should dominate the genomic landscape. Conversely, if it is a homologous synapomorphy, massive gene family expansions should be localized to the deep ancestral nodes preceding continental vicariance. Furthermore, comparing the terminal branch dynamics of *V. tubiflora* and *V. peripherica* allows for the direct quantification of the genomic costs associated with diverging ecophysiological strategies.

Therefore, this study aims to reconstruct the macroevolutionary history and gene family dynamics of the Velloziaceae family. By integrating single-copy phylogenomics, ultrametric divergence calibration, and CAFE5 stochastic modeling across a rigorously curated panel of canonical proteomes, this research establishes the evolutionary polarity of desiccation tolerance and reveals the profound genomic remodeling required to sustain an evergreen lifestyle in extreme environments.

---

## 2. MATERIALS AND METHODS

### 2.1 Proteome Panel Assembly and Canonical Curation
A comprehensive comparative genomic panel was assembled comprising seven fully sequenced plant species designed to capture the deep evolutionary splits within Pandanales and the ecophysiological divergence within Velloziaceae. The dataset included three desiccation-tolerant species: *Xerophyta viscosa* (African Velloziaceae), *Vellozia tubiflora* (South American Velloziaceae), and the desiccation-sensitive evergreen *Vellozia peripherica*. To anchor the deep phylogenetic nodes, the basal Chinese Velloziaceae *Acanthochlamys bracteata*, the sister-group Pandanaceae representative *Pandanus tectorius*, the basal monocot *Dioscorea alata* (Dioscoreales), and the eudicot outgroup *Arabidopsis thaliana* were included. Raw predicted proteomes were parsed to extract exclusively the longest canonical isoform per locus, preventing alternative splicing artifacts from artificially inflating gene family counts. The final curated dataset comprised 168,596 high-quality protein sequences.

### 2.2 Pan-Velloziaceae Orthology Inference and Phylogenomics
Global orthology inference was conducted using OrthoFinder v3.1.5. All-versus-all sequence alignments were executed utilizing the DIAMOND high-speed search algorithm with an E-value threshold of 0.001. Orthogroup clustering was performed using the Markov Cluster Algorithm (MCL). To reconstruct the high-resolution species tree, strictly conserved single-copy orthogroups—defined as orthogroups containing exactly one gene from all seven analyzed species—were isolated. Multiple sequence alignments for these single-copy orthologs were generated using FAMSA, followed by concatenation and maximum-likelihood tree inference via FastTree.

### 2.3 Ultrametric Calibration and Divergence Time Estimation
To prepare the phylogenetic tree for stochastic gene family modeling, the maximum-likelihood topology was converted into a time-calibrated ultrametric tree. Divergence times were calibrated based on established paleobotanical and biogeographical vicariance events. Specifically, the root divergence (Angiosperm split) was constrained to approximately 135 million years ago (Ma). Subsequent nodes were calibrated corresponding to the monocot ordinal split between Dioscoreales and Pandanales (~115 Ma), the familial divergence between Pandanaceae and Velloziaceae (~95 Ma), the basal split of *Acanthochlamys* (~85 Ma), and the critical Gondwanan vicariance event separating the African *Xerophyta* and South American *Vellozia* lineages (~75 Ma). The terminal speciation event between *V. tubiflora* and *V. peripherica* was estimated at ~12 Ma.

### 2.4 CAFE5 Stochastic Gene Family Dynamics Modeling
The evolutionary dynamics of gene family expansions and contractions were modeled using Computational Analysis of gene Family Evolution (CAFE5). The global orthogroup count matrix generated by OrthoFinder was filtered to remove excessively large families (greater than 100 copies in a single species) to ensure model stability. CAFE5 was executed utilizing both a Base model (single global birth/death rate, $\lambda$) and a Gamma distributed rate model (estimating $\lambda$ alongside a rate variation parameter $\alpha$ across four discrete categories). Significant family size variations at specific branches and ancestral nodes were identified applying a stringent statistical threshold (Viterbi $p$-value < 0.05). Function annotations for significantly expanded orthogroups were mapped using cross-reference queries against the *Arabidopsis thaliana* UniProtKB database to extract biological pathway insights.

---

## 3. RESULTS

### 3.1 The Orthologous Core and Pan-Velloziaceae Topology
The comprehensive orthology inference effectively classified 168,596 total genes into 16,532 distinct orthogroups. The clustering algorithm demonstrated exceptional assignment efficiency, capturing 95.2% of all input sequences into homologous clusters. A robust core of 8,011 orthogroups contained representatives from all seven species, defining the foundational genomic architecture of the studied lineages. Crucially, the pipeline identified 1,424 strictly conserved single-copy orthologs, which provided an unparalleled, recombination-free genomic dataset for phylogenetic reconstruction.

The resulting species tree topology resolved the evolutionary relationships with absolute bootstrap support. The basal monocot *Dioscorea alata* accurately positioned outside the Pandanales clade, which subsequently split into Pandanaceae (*Pandanus tectorius*) and Velloziaceae. Within Velloziaceae, the Chinese species *Acanthochlamys bracteata* emerged as the basal-most lineage. The tree unequivocally confirmed the monophyletic divergence between the African clade, represented by *Xerophyta viscosa*, and the South American clade, housing the recently diverged sister species *Vellozia peripherica* and *Vellozia tubiflora*.

### 3.2 The Great Gondwanan Expansion at Node 13
Stochastic modeling of gene family sizes utilizing the CAFE5 Gamma error-corrected model ($\lambda = 0.00289$, $\alpha = 1.058$) revealed distinct macroevolutionary pulses across the phylogeny. The most profound molecular innovation occurred at Node 13, representing the common ancestral population of *Xerophyta* and *Vellozia* immediately prior to the Gondwanan continental breakup. At this critical ancestral node, 893 gene families exhibited numerical expansions, with 126 families expanding at statistically significant rates ($p < 0.05$). This massive ancestral accumulation contrasts sharply with the minimal significant expansions (35 families) observed at the deeper Pandanales root, demonstrating a sudden, massive recruitment of genetic material precisely at the evolutionary dawn of the core Velloziaceae. 

### 3.3 Asymmetric Terminal Diversification in Vellozia
While the African lineage (*Xerophyta viscosa*) experienced a moderate recent terminal expansion involving 39 significantly expanding families, the South American sister species displayed a highly asymmetric pattern of genomic diversification following their recent speciation.

The resurrection species *Vellozia tubiflora* exhibited targeted genomic fine-tuning, characterized by 106 significantly expanded gene families ($p < 0.05$). These expansions were numerically restrained and biologically focused on pathways associated with controlled metabolic shutdown, late embryogenesis abundant (LEA) chaperones, and orderly desiccation responses.

In striking contrast, the evergreen, desiccation-sensitive *Vellozia peripherica* underwent a massive genomic overhaul. CAFE5 identified 209 significantly expanded gene families in the *V. peripherica* terminal branch, generating a net gain of 1,134 genes. This represents nearly double the evolutionary innovation rate of its desiccation-tolerant sister. Functional interrogation of the top 15 most expanded families in *V. peripherica* (e.g., OG0000026 gaining 51 copies; OG0000007 gaining 37 copies) revealed a massive proliferation of five distinct molecular classes:
1. **F-box Ubiquitin Ligase Complexes:** Massive parallel expansions of F-box/LRR-repeat proteins, governing rapid, targeted protein degradation.
2. **Receptor-Like Kinases (RLKs):** Extensive proliferation of G-type lectin S-receptor-like kinases and serine/threonine kinases localized to the plasma membrane.
3. **NLR/ZAR1 Immune Receptors:** Significant multiplication of disease resistance arrays, including RPP13-like and RFL1 proteins.
4. **Pentatricopeptide Repeat (PPR) Proteins:** Expansion of organellar RNA-editing complexes required for continuous plastid and mitochondrial maintenance.
5. **Cytochrome P450 Monooxygenases:** Proliferation of enzymes dictating secondary metabolite biosynthesis, cuticular wax deposition, and xenobiotic detoxification.

---

## 4. DISCUSSION

### 4.1 The Pan-Gondwanan Homology of Desiccation Tolerance
The evolutionary timing and magnitude of gene family expansions provide a definitive answer to the historical enigma surrounding the origin of desiccation tolerance in Velloziaceae. The CAFE5 analysis identified a massive burst of significant gene family expansions (126 families) at Node 13, the common ancestor of the African *Xerophyta* and South American *Vellozia* clades. Because this node predates the geological breakup of the Gondwana supercontinent (~75 Ma), it proves that the core genetic toolkit required for vegetative anhydrobiosis was established long before the lineages were geographically separated. 

Consequently, desiccation tolerance in Velloziaceae is not a product of convergent evolution (homoplasy) driven independently by isolated rock outcrops in Brazil and Africa. Instead, it is a homologous ancestral state (synapomorphy) that defines the core of the family. The African and South American clades share the exact same basal architecture for surviving extreme dehydration, which likely originated from the ancestral rewiring of seed maturation programs (e.g., ABI3/ABI5 regulons, LEA protein deposition, and sucrose accumulation networks) into vegetative tissues (COSTA et al., 2017).

### 4.2 The Genomic Cost of Remaining Evergreen
Establishing desiccation tolerance as the basal condition of the genus fundamentally reverses the traditional interpretation of *Vellozia peripherica*. Rather than representing a primitive lineage that failed to acquire the resurrection phenotype, the evergreen strategy of *V. peripherica* is a highly derived, specialized ecological innovation. To exploit the *campos rupestres* microhabitats by maintaining continuous carbon assimilation during severe dry periods, *V. peripherica* had to secondarily suppress or abandon its ancestral anhydrobiosis capability (ALCANTARA et al., 2015).

However, abandoning the "safe mode" of anhydrobiosis incurs a severe biological cost, which is perfectly captured by the asymmetric expansion of 209 gene families in *V. peripherica*. Because this species retains hydrated, green leaves under intense solar radiation and severe soil water deficit, it suffers continuous photo-oxidative stress and sustained mechanical tension. The massive expansion of F-box ubiquitin ligases indicates a desperate requirement for high-turnover cellular cleanup, constantly degrading proteins damaged by oxidative stress. Simultaneously, because the leaves never dry out into impenetrable tissue, they remain highly susceptible to fungal and bacterial pathogens year-round, necessitating the massive observed expansion of NLR/ZAR1 immune receptors. Finally, the proliferation of RLKs and Cytochrome P450s reflects the need for continuous environmental surveillance and the synthesis of thick, protective cuticular waxes. Ultimately, being evergreen in an extreme environment requires a hyper-vigilant, high-maintenance genome.

### 4.3 Vicariance as an Engine of Divergent Specialization
While the foundational toolkit for desiccation tolerance is universally shared among core Velloziaceae, the terminal branch dynamics illustrate how post-Gondwanan geographic isolation (vicariance) acts as an engine for fine-scale speciation. The African *Xerophyta viscosa* and the South American *Vellozia tubiflora* both inherited the Node 13 toolkit, but their subsequent, independent terminal expansions (39 and 106 families, respectively) demonstrate that millions of years of isolation drove distinct, localized fine-tuning of the resurrection response to match the specific edaphic and climatic constraints of African inselbergs versus Brazilian quartzitic outcrops.

### 4.4 Synthesis and Future Horizons
The integration of whole-genome orthology and CAFE5 stochastic modeling confirms that the macroevolutionary trajectory of Velloziaceae is driven by the dynamic repurposing and expansion of ancestral gene families rather than the de novo invention of unique genes at the terminal tips. Recognizing the evergreen strategy as a derived, high-maintenance phenotype provides a crucial evolutionary context for investigating specific sensory channels. Future research must now transition from global macroevolutionary family counts to the structural and functional analysis of specific candidate genes—such as the mechanosensitive calcium channels (OSCA)—to determine precisely how these expanded environmental surveillance networks operate at the biophysical level to support continuous hydration in the *campos rupestres*.

---

## 5. CONCLUSIONS

1. **Robust Phylogenomic Resolution:** The Velloziaceae family exhibits strict monophyly, with *Acanthochlamys* forming the basal lineage, followed by a clear, robust divergence between the African (*Xerophyta*) and South American (*Vellozia*) clades.
2. **Pan-Gondwanan Origin of Desiccation Tolerance:** The massive expansion of 126 gene families at the common ancestor preceding continental separation confirms that vegetative desiccation tolerance is a homologous basal synapomorphy, not a product of convergent evolution.
3. **Derived Evergreen Specialization:** The drought-avoidant, evergreen lifestyle of *Vellozia peripherica* is a secondary, highly derived innovation rather than a primitive trait, evolved through the loss or suppression of ancestral anhydrobiosis.
4. **The High Cost of Avoidance:** Maintaining active evergreen tissues in extreme environments requires intense genomic remodeling, evidenced by the asymmetric expansion of 209 gene families in *V. peripherica* dedicated to protein recycling (F-box), membrane surveillance (RLKs), and continuous pathogen defense (NLRs).
5. **Macroevolutionary Dynamics:** Speciation within Velloziaceae is characterized by the localized fine-tuning of an ancient, universally shared survival toolkit, fundamentally shaped by geographical vicariance and extreme microclimatic selection pressures.

---

## REFERENCES

ALCANTARA, S. et al. The spectacular radiation of the Velloziaceae in the Neotropical *campos rupestres* vegetation. **Botanical Journal of the Linnean Society**, v. 187, n. 3, p. 384-400, 2018.

ALCANTARA, S. et al. Transcriptomic response to dehydration in *Vellozia* species. **Plant Cell & Environment**, v. 38, n. 5, p. 885-896, 2015.

COSTA, M. C. D. et al. A footprint of desiccation tolerance in the genome of *Xerophyta viscosa*. **Nature Plants**, v. 3, n. 4, p. 17038, 2017.

FARRANT, J. M. et al. Desiccation tolerance in resurrection plants: establishing the principles for engineering drought tolerance in crops. **Plant Physiology**, v. 143, n. 2, p. 876-884, 2007.

MELLO-SILVA, R. Velloziaceae: taxonomy, biogeography, and evolution. **Flora**, v. 206, n. 1, p. 11-20, 2011.

MENDES, F. K. et al. CAFE 5 models variation in evolutionary rates among gene families. **Bioinformatics**, v. 36, n. 22, p. 5516-5518, 2020.

