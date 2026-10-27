# LITERATURE REVIEW: GENOMIC AND REGULATORY BASES OF DROUGHT ADAPTATION IN VELLOZIACEAE

**Integrative Review, Theoretical Framework, and Scientific Propositions for the Doctoral Thesis**  
**Candidate:** Mariana Feitosa Cavalheiro  
**Advisor:** Isabel Rodrigues Gerhardt  
**Institution:** Universidade Estadual de Campinas (UNICAMP)  
**Date:** August 2026 (Final Converged Edition)  

---

## Abstract and Thesis Proposal Summary

This literature review establishes the theoretical framework, evolutionary context, and bioinformatic workflow to investigate the genomic and regulatory bases of contrasting drought adaptation strategies in Velloziaceae from the Neotropical *campos rupestres*. We focus on the structural, evolutionary, and functional characterization of the OSCA superfamily of mechanosensitive calcium channels as primary candidates for early osmotic stress perception. The doctoral thesis comprises two integrated chapters: Chapter 1 establishes the large-scale comparative genomic foundation of *Vellozia* species through high-contiguity chromosomal assemblies, synteny analysis, and gene family evolutionary dynamics; Chapter 2 examines the gene architecture, transcriptional expression profiles, cis-regulatory promoter composition, and protein-protein interaction networks of the OSCA family across contrasting drought regimes.

---

# 1. Ecological Context, Morphophysiological Diversity, and Evolutionary Trade-offs in Velloziaceae

The *campos rupestres* of central and eastern Brazil constitute an ancient, tropical montane ecosystem recognized biogeographically as an Old Climatically-Buffered Infertile Landscape (OCBIL) that harbors approximately 15% of the national vascular plant diversity within less than 1% of the Brazilian territory (SILVEIRA et al., 2015; FERNANDES et al., 2020; ALCANTARA et al., 2015). This extraordinary floristic richness and microhabitat-scale endemism reflect persistent diversification driven by severe, multidimensional edaphoclimatic filters (FERNANDES et al., 2018). In these landscapes, soils derived from quartzite and sandstone substrates are characteristically shallow, acidic, and exceptionally oligotrophic, exhibiting available phosphorus concentrations among the lowest recorded globally (TEODORO et al., 2019; LAMBERS et al., 2022; ABRAHÃO et al., 2018). Beyond severe nutrient scarcity, the skeletal substrate possesses minimal water retention capacity, exposing the endemic vegetation to acute seasonal water deficits, saturating solar irradiance, elevated vapor pressure deficits (VPD), pronounced daily thermal fluctuations, and abrasive winds. Regional bioclimatic models project that these selective pressures will intensify under global climate change, increasing the frequency and duration of severe drought events across tropical mountaintops (FERNANDES et al., 2020).

Under this stringent edaphoclimatic regime, the monocotyledonous family Velloziaceae (order Pandanales) represents the dominant floristic component, reaching its global center of taxonomic richness and morphological specialization in the Espinhaço Range (DE MELLO-SILVA, 2005; ALCANTARA et al., 2015; ALCANTARA; REE; MELLO-SILVA, 2018). These predominantly heliophytic monocots exhibit diverse vegetative architectures, ranging from arborescent woody shrubs supported by persistent adventitious roots to compact, cushion-forming graminoid rosettes attached to fibrous caudices (WANGA et al., 2021). To acquire essential nutrients from hyper-oligotrophic substrates, Velloziaceae evolved specialized "vellozioid" roots that exude high concentrations of carboxylates (primarily malate and citrate) to chemically weather quartzite rock surfaces and solubilize tightly bound inorganic phosphorus (TEODORO et al., 2019; LAMBERS et al., 2022; ABRAHÃO et al., 2018).

At the foliar level, specialized morphoanatomical structures coordinate to delay tissue dehydration and mitigate photo-oxidative damage during moisture deprivation. For example, *Barbacenia graminifolia* develops a single-layered adaxial epidermis covered by a thick cuticular layer, symmetrical mesophyll compaction, and reversible longitudinal leaf rolling upon turgor loss, which shields the photosynthetic apparatus from excessive radiative load (ALVES; SILVA, 2009; TEODORO et al., 2021). Within the mesophyll, palisade parenchyma cells accumulate vacuolar mucilage enriched in acidic polysaccharides, slowing the rate of foliar water loss and accelerating tissue rehydration upon water return (VIEIRA et al., 2022).

Co-occurring Velloziaceae species in the *campos rupestres* have evolved divergent water-use strategies to cope with extreme drought regimes (ALCANTARA et al., 2015; VIEIRA et al., 2022). Desiccation-tolerant (DT) species, commonly designated resurrection plants, survive the loss of more than 90% of their total protoplasmic water ($\Psi < -100\text{ MPa}$), entering a state of quiescent anhydrobiosis and restoring full metabolic competence within hours of rehydration (BONDI; MARKS; VANBUREN, 2023; TEODORO et al., 2021; MARKS et al., 2024). This vegetative anhydrobiosis represents an evolutionary specialization restricted to a small fraction of vascular plants. Prominent DT lineages in the *campos rupestres* include *Vellozia tubiflora* and *Vellozia caruncularis*. In contrast, sympatric desiccation-sensitive but drought-avoidant (evergreen) species, such as *Vellozia peripherica* and *Barbacenia gentianoides*, maintain functional foliar hydration through tight stomatal regulation, osmotic adjustment, and deep root foraging in rock crevices, sustaining baseline carbon assimilation throughout dry periods (DE MELLO-SILVA, 2005; VIEIRA et al., 2022; VIEIRA et al., 2025).

Yet exceeding the leaf turgor loss point ($\Psi_{TLP}$) carries diametrically opposed biological consequences between these lineages. In avoidant species, reaching $\Psi_{TLP}$ represents a lethal threshold triggering catastrophic xylem cavitation, hydraulic failure, and tissue mortality. In desiccation-tolerant species, reaching $\Psi_{TLP}$ acts as a physiological inductive cue that initiates cellular protection programs: cell walls fold harmoniously, the cytoplasm vitrifies, and metabolic activity arrests (BONDI; MARKS; VANBUREN, 2023; TEODORO et al., 2021). For an avoidant plant, turgor loss is fatal; for a resurrection plant, it is a developmental transition.

These contrasting physiological strategies drive fine-scale microhabitat segregation along substrate depth and moisture gradients across the landscape (ALCANTARA et al., 2015; SILVEIRA et al., 2015; ZAPPI et al., 2017). Specifically, desiccation-tolerant species such as *Vellozia caruncularis* and *Vellozia tubiflora* colonize exposed, shallow quartzite rock outcrops where water availability fluctuates rapidly between torrential saturation and severe dehydration, relying on vegetative anhydrobiosis for long-term persistence (VIEIRA et al., 2025; ALCANTARA et al., 2015). Conversely, avoidant species such as *Barbacenia gentianoides* and *Vellozia peripherica* occupy deeper soil pockets and shaded rock fissures that retain moisture and organic matter, sustaining seasonal carbon acquisition (VIEIRA et al., 2025).

This spatial and physiological segregation illustrates a fundamental evolutionary trade-off between productivity and survival in stressful environments (TEODORO et al., 2021; FERNANDES et al., 2020; FERNANDES et al., 2018; VOLAIRE et al., 2026). Desiccation tolerance guarantees survival through extreme, lethal droughts at the expense of negligible annual carbon gain and slow vegetative growth rates during dry periods (BONDI; MARKS; VANBUREN, 2023; TEODORO et al., 2021). Dehydration avoidance maximizes carbon assimilation under moderate water deficits, operating as Phase II "drought resistance," but exposes plants to catastrophic mortality if environmental stress exceeds their hydraulic safety margins, reflecting a universal trade-off between growth potential and drought survival (ALCANTARA et al., 2015; VIEIRA et al., 2022; VOLAIRE et al., 2026).

---

# 2. Biophysical Bases of Drought Responses and the Comparative System in Velloziaceae

Analyzing plant responses to water deficits requires distinguishing between environmental water scarcity, cellular osmotic stress, and terminal desiccation (HARTMANN; FIEDLER, 2021; THOR et al., 2020; HAN et al., 2022), as well as standardizing terminology across functional adaptation strategies (VOLAIRE, 2017; VOLAIRE et al., 2026). A trait- and time-based framework separates Phase II "drought resistance" (traits focused on maintaining turgor, water potential, and growth potential under declining water availability, such as dehydration avoidance) from Phase III "drought survival" (mechanisms such as extreme dehydration tolerance or vegetative desiccation tolerance deployed when severe moisture limitations arrest vegetative growth entirely) (VOLAIRE et al., 2026).

While environmental water deficit denotes macroscopic moisture depletion across the soil-plant-atmosphere continuum, osmotic stress represents its immediate cellular biophysical manifestation: the decrease in extracellular water potential establishes a trans-membrane chemical potential gradient that drives rapid water efflux, increasing plasma membrane lateral tension and altering protoplast-cell wall biomechanics. This mechanical strain initiates signaling cascades within seconds: mechanosensitive channels open and drive an immediate cytosolic calcium wave ($OICI_{cyt}$) (ZHANG et al., 2018; LIU et al., 2022; ZHU et al., 2025; KAUR; MADHU; UPADHYAY, 2021). Calcium decoders subsequently activate downstream protein kinase cascades and transcriptional networks, coordinating stomatal closure, osmotic adjustment, and cytoprotective gene expression (THOR et al., 2020; HAN et al., 2022; KANG; ZHAO; LIU, 2023).

This cellular shrinkage occurs not across an isolated lipid bilayer, but within the integrated cell wall-plasma membrane-cytoskeleton continuum (COLIN et al., 2023). As turgor pressure drops towards zero, the mechanical tethering between the plasma membrane and the primary cell wall pectin-cellulose network experiences severe shearing forces. In primary cell walls, homogalacturonan (HG) pectins cross-linked by calcium ions ($Ca^{2+}$) serve as both a mechanical support matrix and an extracellular calcium reservoir (COLIN et al., 2023). De-esterification of pectins by pectin methylesterases (PMEs) and wall loosening by expansins and xyloglucan endotransglucosylases/hydrolases (XTHs) modulate cell wall rheology, permitting harmonious cell wall folding while preventing cytorrhysis (the irreversible collapse of the wall inward) and avoiding membrane-wall delamination (COLIN et al., 2023; TEODORO et al., 2021). The local release of wall-bound calcium during matrix deformation directly interfaces with plasma membrane mechanosensors, establishing a coordinated continuum of early mechanoperception.

When protoplasmic water content falls below 10-20% of full turgor ($\Psi < -100\text{ MPa}$), terminal cellular desiccation occurs, causing severe macromolecular crowding and membrane phase transitions. In sensitive species, this induces irreversible membrane lysis and cell death; in resurrection plants, coordinated biochemical programs stabilize the desiccated protoplast in a vitrified, quiescent state (BONDI; MARKS; VANBUREN, 2023; TEODORO et al., 2021).

## 2.1 Macroevolutionary Divergence in Angiosperm Desiccation Tolerance: Monocot Poikilochlorophylly vs. Eudicot Homoiochlorophylly and the Pan-Velloziaceae Paradigm

Vegetative desiccation tolerance (DT) evolved independently and convergently across multiple angiosperm lineages through the co-option and regulatory rewiring of ancestral seed maturation programs into vegetative tissues (COSTA et al., 2017; GAFF; OLIVER, 2013; OLIVER et al., 2020; MARKS et al., 2024). However, the macroevolutionary solutions deployed to withstand protoplasmic dehydration diverge sharply between monocotyledons and eudicotyledons, reflecting contrasting biophysical constraints, leaf anatomies, and organellar dynamics.

### 2.1.1 The Photosynthetic Divide: Poikilochlorophylly vs. Homoiochlorophylly

The most fundamental physiological dichotomy separating resurrection plants is the fate of the photosynthetic apparatus during vegetative dehydration. Homoiochlorophyllous species (predominantly eudicots exemplified by Gesneriaceae like *Boea hygrometrica*, *Haberlea rhodopensis*, and *Ramonda myconi*, Linderniaceae like *Craterostigma plantagineum*, and Scrophulariaceae like *Myrothamnus flabellifolia*) retain 80% to 100% of their foliar chlorophyll and preserve intact thylakoid membrane ultrastructures in the dry state (GAFF; OLIVER, 2013; XIAO et al., 2015; BLOMSTEDT et al., 2018). To prevent catastrophic singlet oxygen ($^1\text{O}_2$) and superoxide ($\text{O}_2^{\bullet-}$) generation under tropical solar irradiance, homoiochlorophyllous taxa rely on optical shielding (conspicuous abaxial pubescence, dense anthocyanin/polyphenol screens, and dramatic foliar curling) combined with high-capacity non-photochemical quenching (NPQ/qE) and Early Light-Induced Proteins (ELIPs). Consequently, homoiochlorophyllous plants restore net carbon assimilation within minutes to a few hours after re-watering.

In sharp contrast, desiccation-tolerant monocots (including African and South American Velloziaceae like *Xerophyta*, *Vellozia*, and *Barbacenia*, Boryaceae like *Borya*, and resurrection grasses like *Oropetium*, *Sporobolus*, and *Tripogon*) are overwhelmingly poikilochlorophyllous (SHERWIN; FARRANT, 1996; FARRANT et al., 2007; COSTA et al., 2017; OLIVER et al., 2020). During progressive dehydration, poikilochlorophyllous plants execute an active, highly regulated dismantling of chlorophyll pigments, thylakoid complexes (LHCII, PSII/PSI reaction centers), and stromal enzymes. This disassembly requires massive targeted protein degradation—often mediated by the ubiquitin-proteasome system—transforming functional chloroplasts into quiescent, rounded organellar structures termed *desmoplastos* or *sacoplasts* filled with lipidic plastoglobules (FARRANT et al., 2007; COSTA et al., 2017; SUN; JARVIS, 2023). While poikilochlorophylly provides absolute photoprotection in exposed, unshaded tropical rock outcrops by eliminating the primary photosensitizer, it imposes a severe physiological consequence: the **kinetic rehydration bottleneck** (WATSON; SOWDEN; JARVIS, 2018; SUN; JARVIS, 2023). Upon rehydration, poikilochlorophyllous leaves require 24 to 72 hours to synthesize chlorophyll *de novo*, transcribe and translate hundreds of nuclear-encoded plastid precursor polypeptides, and transport them across the chloroplast envelope via TOC/TIC translocons to rebuild functional thylakoid networks (COSTA et al., 2017; RADERMACHER et al., 2019).

### 2.1.2 Cell Wall Biomechanics, Foliar Architecture, and Vitrification Chemistry

Divergent mechanical and biochemical solutions coordinate with the contrasting leaf architectures of monocots and eudicots. Eudicot resurrection plants possess broad, reticulately veined leaves with plastic primary cell walls enriched in arabinogalactan-proteins (AGPs) and unesterified pectins (COLIN et al., 2023). Upon turgor loss, the cell wall undergoes reversible, multidirectional accordion-like folding (*concertina-like folding*), accommodating protoplast volume reduction without membrane-wall delamination or mechanical lysis (XIAO et al., 2015; BLOMSTEDT et al., 2018). Conversely, Velloziaceae and poikilochlorophyllous monocots develop rigid, linear, sclerenchymatous leaves reinforced by heavily lignified vascular bundle sheaths. Because their rigid cell walls cannot undergo concertina-style deformation, foliar shrinkage is strictly anisotropic (V-shaped longitudinal closure along the midrib), and cellular structural integrity is maintained by vacuolar fragmentation into tannin- and polyphenol-filled microvacuoles that act as internal hydraulic skeletons (ALCANTARA et al., 2015; SHERWIN; FARRANT, 1996; VIEIRA et al., 2022).

At the metabolic level, both lineages achieve cytoplasmic vitrification (amorphous glass formation), but deploy distinct carbohydrate precursors. In *Craterostigma plantagineum*, hydrated leaves accumulate massive concentrations of the rare 8-carbon monosaccharide **octulose**, converting it rapidly into **sucrose** during dehydration (BLOMSTEDT et al., 2018; OLIVER et al., 2020). In contrast, Velloziaceae utilize the canonical sucrose and Raffinose Family Oligosaccharide (RFO) cascade (raffinose, stachyose, verbascose) synthesized via galactinol synthase (*GolS*), accompanied by high accumulations of organonitrogenous osmoprotectants such as proline and GABA (WHITTAKER et al., 2001, 2007; SUGUIYAMA et al., 2014; VIEIRA et al., 2022).

### 2.1.3 Pan-Velloziaceae Validation Across African and South American Lineages

These conserved macroevolutionary patterns across Velloziaceae demonstrate that the genomic adaptations of *Vellozia* (encompassing translocon expansion, photosystem stabilization, and osmosensory signaling) represent the core molecular toolkit enabling poikilochlorophyllous survival on ancient, infertile Neotropical mountaintops.

### 2.1.4 The Ecological and Genomic Burden of the Evergreen Strategy

While resurrection lineages escape extreme drought and photo-oxidative stress by entering metabolic dormancy, sympatric evergreen avoidant species (such as *V. peripherica*) face a continuous physiological burden. By retaining functional, hydrated foliage year-round to maximize carbon assimilation, they are perpetually exposed to saturating UV irradiance, opportunistic pathogens, and high vapor pressure deficits (ALCANTARA et al., 2015). Avoidant species maintain high foliar water potentials during drought through tight abscisic acid (ABA)- and jasmonate-mediated stomatal closure, osmolyte accumulation, and extensive root foraging (TEODORO et al., 2019; ABRAHÃO et al., 2018; VIEIRA et al., 2022). 

However, sustaining an evergreen habit in the *campos rupestres* exacts a high ecological and energetic cost. The persistent green tissue requires continuous structural maintenance, robust secondary metabolism to shield against radiation, and uninterrupted immune surveillance to deter foliar pathogens in the warm, hydrated leaf environment. Consequently, while the physiological costs of the evergreen strategy are well-documented (GIVNISH, 2002; ALCANTARA et al., 2015), the underlying macroevolutionary genomic adaptations—specifically how the avoidance strategy drives lineage-specific amplification of constitutive defense and cellular remodeling pathways—remain a critical unknown.

Resurrection plants, in contrast, poikilohydrically equilibrate with atmospheric water potential. During dehydration, they convert starch reserves into non-reducing sugars (sucrose, trehalose, and raffinose family oligosaccharides [RFOs]), which substitute for water hydrogen bonds on macromolecular surfaces and induce cytoplasmic vitrification to form an amorphous glassy matrix that prevents protein denaturation and membrane crystallization (VIEIRA et al., 2022; BONDI; MARKS; VANBUREN, 2023). Simultaneously, cell walls remodel with arabinose- and pectin-rich polymers, allowing the wall to fold in unison with the shrinking protoplast and preserve plasma membrane integrity (COLIN et al., 2023; TEODORO et al., 2021). Vacuoles fragment into multiple microvacuoles loaded with osmolytes to preserve subcellular compartmentalization. To minimize photo-oxidative damage, tolerant plants either degrade their chlorophylls or deploy high-capacity non-photochemical quenching (NPQ/qE), cyclic electron transport (CET), and enzymatic antioxidant cascades to scavenge Reactive Oxygen Species (ROS) (OUNG et al., 2021; BONDI; MARKS; VANBUREN, 2023).

The sympatric congeneric pair *Vellozia tubiflora* and *Vellozia peripherica* provides a natural comparative model to investigate the genomic and regulatory foundations of drought adaptation (ALCANTARA et al., 2015; VIEIRA et al., 2022). As an obligate resurrection plant (DT), *V. tubiflora* responds to acute water deficit through programmed foliar rolling, metabolic shutdown, and entry into anabiosis (BONDI; MARKS; VANBUREN, 2023; TEODORO et al., 2021). In contrast, the evergreen *V. peripherica* enforces strict stomatal regulation and foliar water retention to remain photosynthetically active, but lacks macromolecular desiccation protection and suffers irreversible tissue mortality if cellular water drops below $\Psi_{TLP}$. This physiological dichotomy drives fine-scale microhabitat segregation: *V. tubiflora* occupies exposed rock crevices prone to rapid drying, whereas *V. peripherica* colonizes deeper soil pockets (BONDI; MARKS; VANBUREN, 2023; VIEIRA et al., 2025). These adaptive differences indicate fundamental divergences in early osmotic perception and transcriptional regulation, making mechanosensitive channels of the OSCA family prime candidates for comparative investigation (THOR et al., 2020; HAN et al., 2022).

Pairwise comparative models between phylogenetically paired desiccation-tolerant (DT) and desiccation-sensitive relatives isolate the mechanistic foundations of extreme drought adaptation while controlling for macroevolutionary phylogenetic noise (MARKS et al., 2024; BONDI; MARKS; VANBUREN, 2023). Velloziaceae has already enabled foundational breakthroughs in resurrection plant biology: the chromosome-level genome of the African monocot *Xerophyta viscosa* demonstrated that vegetative desiccation tolerance evolved through the co-option and promoter rewiring of ancestral seed maturation networks (COSTA et al., 2017). In South American *campos rupestres*, ecophysiological comparisons between co-occurring *Vellozia* and *Barbacenia* species delineated contrasting hydraulic safety margins and seasonal carbon remobilization (TEODORO et al., 2021; VIEIRA et al., 2022; VIEIRA et al., 2025; ALCANTARA et al., 2015).

These findings parallel comparative systems across the plant kingdom, including the resurrection grasses *Oropetium thomaeum* (VANBUREN et al., 2015) and *Sporobolus stapfianus* (OLIVER et al., 2011), the eudicot *Boea hygrometrica* (XIAO et al., 2015), and the lycophyte *Selaginella lepidophylla* (VANBUREN et al., 2018). However, previous literature has predominantly contrasted DT plants with standard, mesophytic relatives. This doctoral thesis pioneers a comparative genomics framework contrasting a DT resurrection plant directly against a highly specialized drought-avoidant relative from the same extreme environment. Extending this proven comparative paradigm to *Vellozia tubiflora* (DT) and *Vellozia peripherica* (avoidant) provides an unprecedented model to bridge whole-genome evolutionary dynamics with discrete mechanosensory signaling cascades.

### Table 1. Comparative summary of ecophysiological and adaptive traits between the focal species.

| Feature / Trait | *Vellozia tubiflora* (Resurrection / DT) | *Vellozia peripherica* (Evergreen / Avoidant) |
|---|---|---|
| **Ecophysiological Strategy** | Desiccation Tolerance (Poikilohydry) | Dehydration Avoidance (Homoiohydry) |
| **Microhabitat Preference** | Exposed quartzite outcrops, skeletal shallow crevices | Deeper soil depressions with organic matter accumulation |
| **Foliar Response to Drought** | Reversible rolling, chlorophyll degradation / NPQ protection | Maintained vertical architecture, strict stomatal closure |
| **Turgor Loss Point ($\Psi_{TLP}$)** | Functional cue triggering vitrification & cellular dormancy | Critical hydraulic threshold; risk of irreversible xylem cavitation |
| **Metabolic State under Severe Drought** | Quiescent anabiosis; shutdown of $CO_2$ assimilation | Baseline carbon assimilation sustained via water conservation |
| **Primary Evolutionary Trade-off** | Guaranteed survival under acute drought; low annual growth | High annual biomass gain; elevated mortality under extreme drought |

> **Figure 1. Natural comparative model of drought persistence strategies in Velloziaceae.** Schematic representation of *Vellozia tubiflora* (desiccation-tolerant, DT) and *Vellozia peripherica* (dehydration-avoidant, evergreen) across microhabitat gradients in the *campos rupestres*, illustrating differential leaf rolling, turgor loss thresholds ($\Psi_{TLP}$), cellular anhydrobiosis, and hydraulic safety margins. Vector source: [fig1_ecophysiological_model.svg](file:///home/mfcaval/github/doutorado/teamwork/figures_review/fig1_ecophysiological_model.svg).

---

# 3. Comparative Genomics and Macroevolutionary Dynamics of Adaptation

Comparative genomics provides the conceptual framework to determine whether divergent ecological strategies—such as vegetative desiccation tolerance versus continuous evergreen hydration—are driven by broad chromosomal reorganizations, widespread gene duplication events, or shifts in family-specific evolutionary rates (WU et al., 2022; LI et al., 2023). Historically, genomic studies of extremophyte plants have demonstrated that ecophysiological innovations frequently emerge from the segmental or tandem expansion of gene families linked to stress perception, secondary metabolism, and cellular repair (BONDI; MARKS; VANBUREN, 2023; MARKS et al., 2024). 

Beyond numerical copy-number variations, divergent selective pressures rapidly sculpt the functional proteome. While core metabolic structural genes typically remain under strong purifying selection to preserve essential mechanics, signatures of positive (diversifying) selection often highlight the recruitment and subfunctionalization of ancestral pathways into novel roles critical for survival in extreme niches (GU et al., 2018; SHAN et al., 2023; ZHU et al., 2025). Establishing this macroevolutionary landscape between *Vellozia tubiflora* and *Vellozia peripherica* provides the necessary genetic backdrop to dissect how discrete molecular sensors, which initiate early osmotic perception, evolved to underpin such diametrically opposed survival strategies in hyper-arid environments.

---

# 4. Primary Osmosensing and the OSCA Mechanosensitive Calcium Channel Family

## 4.1 The Search for Primary Osmosensors in Plants

Downstream drought signaling pathways are well mapped. Yet the primary biophysical mechanisms by which plant cells first sense water deficit remain one of the defining grand challenges in modern plant biology (VERSLUES et al., 2023; ZHANG et al., 2018; LIU et al., 2022; HARTMANN; FIEDLER, 2021). In a landmark international consensus on plant abiotic stress biology, Verslues et al. (2023) identified resolving the molecular identity and biophysical discrimination of primary osmosensors as a foundational unknown: plant cells must instantly distinguish purely mechanical changes in turgor pressure from chemical macromolecular crowding, ionic shifts, and localized cell wall deformations.

Osmotic stress rapidly alters membrane-cell wall biomechanics through three interconnected pathways: plasma membrane sensors, cell wall integrity sentinels, and mechanosensitive ion channels (COLIN et al., 2023; VERSLUES et al., 2023). Early paradigms proposed the *Arabidopsis* histidine kinase AtHK1 as the primary osmosensor (THOR et al., 2020; HAN et al., 2022); however, *athk1-null* mutants display normal cytosolic calcium signaling under hyperosmotic shock, indicating the presence of independent mechanosensory channels. As cell volume contracts under dehydration, tensile stress develops at the cell wall-membrane interface, where Receptor-Like Kinases (RLKs, such as FERONIA and THE1) monitor this biomechanical strain, modulating ABA accumulation and evoking late calcium transients to induce cell wall remodeling (COLIN et al., 2023).

Mechanosensitive (MS) ion channels are the fastest sensors capable of converting lipid bilayer physical deformation directly into intracellular chemical signals (ZHANG et al., 2018; LIU et al., 2022; KAUR; MADHU; UPADHYAY, 2021). Tension changes directly gate the channel pore, driving rapid $Ca^{2+}$ influx from the apoplast within seconds ($OICI_{cyt}$) (THOR et al., 2020; HAN et al., 2022). Alternative plant mechanosensitive families fulfill specialized functions: MSL channels are predominantly anion-selective and operate in hypoosmotic relief; MCA channels are calcium-permeable, but *mca1/mca2* mutants maintain normal hyperosmotic calcium spikes; and plant Piezo channels participate primarily in root penetration mechanotransduction (HARTMANN; FIEDLER, 2021; KAUR; MADHU; UPADHYAY, 2021). Consequently, the OSCA (*hyperosmolality-gated calcium-permeable channels*) family stands out as the only plant mechanosensor class whose direct gating by membrane lateral tension and rapid $Ca^{2+}$ conductance under hyperosmotic shock have been unequivocally demonstrated (ZHANG et al., 2018; LIU et al., 2022; YUAN et al., 2014). This leaves OSCA at the apex of osmotic mechanoperception. Thus, comparative analysis of OSCA channels between *V. tubiflora* and *V. peripherica* provides an ideal platform to uncover the molecular foundations of early water sensing.

## 4.2 Molecular Architecture, Phylogeny, and Biophysical Gating of OSCA Channels

The founder locus OSCA1 (*AtOSCA1.1*) was isolated in *Arabidopsis thaliana* as the essential channel mediating hyperosmolality-induced $Ca^{2+}$ increase (YUAN et al., 2014; HAN et al., 2022). Knockout *osca1* plants exhibit abolished root $OICI_{cyt}$ waves and defective stomatal closure, leading to accelerated dehydration (ZHANG et al., 2018). *AtOSCA1.2* was subsequently validated as an active paralog sharing 85% sequence identity (LIU; WANG; SUN, 2018; LIU et al., 2022). OSCA homologs possess an exclusive 180-amino-acid cytosolic gating loop. Plant genomes underwent substantial lineage-specific expansions of this family, ranging from 15 in *Arabidopsis* (YUAN et al., 2014) to 42 in bread wheat (TONG et al., 2021; KAUR et al., 2022).

Phylogenetically, the family comprises four monophyletic clades (WU et al., 2022; LI et al., 2023): Clade I mediates hyperosmotic perception at the plasma membrane; Clade II regulates developmental osmotic control; Clade III features low copy-number retention and early drought responsiveness; and Clade IV represents the basal single-exon lineage. Evolutionary genomics indicates that OSCA diversified during the land plant transition, expanding via whole-genome duplications to equip stomata, roots, and vascular tissues with precise osmosensors (WU et al., 2022; KE et al., 2022; YUAN et al., 2014).

Single-particle cryo-EM structures reveal that OSCA channels assemble as symmetrical homodimers perpendicular to the plasma membrane (ZHANG et al., 2018; LIU; WANG; SUN, 2018; LIU et al., 2022). The transmembrane domains of each subunit remain physically separated by a central hydrophobic cavity, with dimerization stabilized exclusively by cytosolic hydrogen bonding networks. Each monomer comprises 11 transmembrane helices (M0-M10) organized into three functional domains: an N-terminal domain (RSN1_TM, PF13967) stabilizing membrane insertion, a central cytosolic domain (PHM7_cyt, PF14703) acting as a biomechanical scaffold, and a C-terminal DUF221 domain (RSN1_7TM, PF02714) forming the ion-conducting pore.

Gating operates via a "force-from-lipid" mechanism: membrane stretching pulls a hydrophobic anchor (consensus motif `LGFLGLWG`), levering the gating helix M6 to straighten around a conserved glycine hinge (G528 in AtOSCA1.1) (ZHANG et al., 2018; LIU et al., 2022). This movement rotates bulky aromatic residues away from the pore axis, opening a conductive pathway ($>5.5\text{ Å}$) for hydrated $Ca^{2+}$ influx. Isoforms lacking this cytosolic anchor fail to rescue osmotic $Ca^{2+}$ deficiency, demonstrating the sensory centrality of the cytosolic arm.

> **Figure 2. Structural architecture and "force-from-lipid" gating mechanism of the OSCA mechanosensitive calcium channel.** (A) Symmetrical homodimeric architecture with $C_2$ rotational axis, highlighting the transmembrane DUF221 pore (PF02714), the cytosolic scaffold (PHM7_cyt / RRM, PF14703), and the N-terminal anchor (RSN1_TM, PF13967). (B) Detailed biophysical mechanotransduction model showing membrane lateral tension pulling the cytosolic `LGFLGLWG` hydrophobic anchor, straightening the gating helix M6 around the conserved glycine hinge (G528), and opening the central pore ($>5.5\text{ Å}$) for rapid $Ca^{2+}$ influx. Vector source: [fig2_osca_biophysics.svg](file:///home/mfcaval/github/doutorado/teamwork/figures_review/fig2_osca_biophysics.svg).

## 4.3 Cis-Regulatory Architecture, Expression Dynamics, and Interaction Networks

Promoter regions of OSCA genes harbor diverse cis-regulatory elements mediating environmental responsiveness (LI et al., 2015; DING et al., 2019; GU et al., 2018; ZHANG et al., 2023; MIAO et al., 2022): ABRE governing bZIP-driven transcription under drought; DRE/CRT regulating rapid ABA-independent activation; MBS and LTR driving responses to physical desiccation and cold stress; and CGTCA/TGACG motifs mediating jasmonate signaling (LI et al., 2023). Spatiotemporal expression profiles show high transcript abundance in roots, vascular bundles, and pollen (JIE et al., 2022; LI et al., 2022), alongside marked post-duplication subfunctionalization in paralogous pairs (YANG et al., 2026; WU et al., 2022; LI et al., 2023).

Downstream of the lipid bilayer, protein-protein interaction (PPI) networks couple OSCA channels to transcriptional regulators and signaling kinases (ZHANG et al., 2018; LIU et al., 2022). In *Arabidopsis*, AtOSCA1.3 is phosphorylated at Ser54 by the immune kinase BIK1 upon flg22 perception, rapidly gating calcium influx to execute stomatal closure during pathogen attack (THOR et al., 2020; HAN et al., 2022). In maize, ZmOSCA2.3 and ZmOSCA2.4 physically interact with transcription factor ZmEREB198 to modulate proline accumulation (CAO et al., 2020). In wheat, TaOSCA1.4 functions as a QTL regulator coupling turgor signaling to vegetative shoot elongation (LV et al., 2024; SU et al., 2025).

---

# 5. Scientific Propositions: Gaps, Hypotheses, and Research Objectives

## 5.1 Knowledge Gap and Central Working Hypotheses

While late-stage physiological and biochemical adaptations to water deficit in *campos rupestres* plants are increasingly documented, the early molecular mechanisms through which extremophyte cells perceive acute moisture deprivation and trigger divergent downstream trajectories remain poorly understood (VERSLUES et al., 2023). The sympatric congeneric pair *Vellozia tubiflora* (desiccation-tolerant) and *Vellozia peripherica* (evergreen, desiccation-sensitive) provides an ideal natural comparative system to address this gap: sharing identical macroclimatic selective regimes and close phylogenetic ancestry, they display diametrically opposed life-history solutions to water scarcity (ALCANTARA et al., 2015; VIEIRA et al., 2022).

We hypothesize that the contrasting ecophysiological adaptations of *V. tubiflora* and *V. peripherica* stem from coordinated, multilevel molecular divergence across their genomes, spanning macrosyntenic architecture, gene family copy-number dynamics, and the transcriptional and structural regulation of primary mechanosensory calcium channels. Specifically, we propose four interconnected working hypotheses:
- **Broad Genomic Divergence:** Lineage-specific gene family expansions and contractions reflect the evolutionary footprints of quiescent anhydrobiosis versus continuous foliar hydration within a conserved chromosomal scaffold.
- **Structural Channel Conservation:** Core OSCA transmembrane topology, gating hinges, and pore-lining residues remain under strong purifying selection in both genomes to maintain essential ion-conduction mechanics.
- **Regulatory and Transcriptional Divergence:** Promoter cis-regulatory element architecture and expression kinetics diverge substantially, directing rapid, coordinated stress induction in *V. tubiflora* versus constitutive or buffered expression in *V. peripherica*.
- **Protein Interaction Specialization:** OSCA signaling complexes exhibit distinct functional wiring, preferentially coupling to cell wall remodeling and ABA cascades in the resurrection specialist, while associating with osmotic homeostasis and turgor maintenance in the evergreen avoidant.

---

## 5.2 Objectives and Thesis Organization

The overarching objective of this doctoral thesis is to establish the comparative genomic landscape of *Vellozia tubiflora* and *Vellozia peripherica*, identifying global evolutionary signatures associated with contrasting drought persistence strategies, and to elucidate the structural, evolutionary, and regulatory determinants of the OSCA mechanosensitive calcium channel superfamily.

To achieve this goal, the research is organized into two integrated chapters:

**Chapter 1: Large-Scale Comparative Genomics.** This chapter evaluates the completeness, contiguity, and structural annotation of the chromosome-scale assemblies ($2n = 18$) using BUSCO and transcriptomic mappings; delineates orthologous and paralogous relationships across 24,013 orthogroups using OrthoFinder; reconstructs chromosomal collinearity and paleoduplication blocks via MCScanX; and models gene family evolutionary trajectories (CAFE5), selection pressures ($Ka/Ks$), and functional divergence across the proteomes.

**Chapter 2: Evolutionary and Structural Characterization of the OSCA Channel Superfamily.** Building on the macroevolutionary foundation of Chapter 1, this chapter identifies all OSCA family members in both genomes using DUF221 domain profiles; reconstructs phylogenetic relationships within angiosperm clades; models exon-intron architectures and transmembrane topologies; characterizes promoter cis-regulatory elements (-2000 bp) to evaluate hormonal and stress responsiveness; and reconstructs protein-protein interaction networks to identify functional partners in early osmotic mechanotransduction.

Together, these investigations progress from whole-genome macroevolutionary patterns to high-resolution structural and regulatory dissection of candidate mechanosensors, establishing predictive molecular foundations for functional plant biology in Neotropical montane ecosystems.

> **Figure 3. Integrated bioinformatic and evolutionary workflow of the doctoral thesis.** Methodological roadmap bridging whole-genome comparative genomics (Chapter 1) with fine-scale target characterization of the OSCA mechanosensory channel family (Chapter 2).

---

# References

ABRAHÃO, Anna; et al. Soil types select for plants with matching nutrient‐acquisition and ‐use traits in hyperdiverse and severely nutrient‐impoverished campos rupestres and cerrado in central Brazil. **Journal of Ecology**, v. 107, n. 3, p. 1302–1316, 2018. DOI: https://doi.org/10.1111/1365-2745.13111.

AIDAR, Saulo T.; et al. Desiccation tolerance and recovery of photosynthesis in Barbacenia purpurea (Velloziaceae). **Brazilian Journal of Plant Physiology**, v. 22, n. 3, p. 195–204, 2010. DOI: https://doi.org/10.1590/S1677-04202010000300007.

ALCANTARA, Suzana; et al. Carbon assimilation and habitat segregation in resurrection plants: a comparison between desiccation‐ and non‐desiccation‐tolerant species of Neotropical Velloziaceae (Pandanales). **Functional Ecology**, v. 29, n. 12, p. 1499–1512, 2015. DOI: https://doi.org/10.1111/1365-2435.12462.

ALCANTARA, Suzana; REE, Richard H; MELLO-SILVA, Renato. Accelerated diversification and functional trait evolution in Velloziaceae reveal new insights into the origins of the campos rupestres’ exceptional floristic richness. **Annals of Botany**, v. 122, n. 1, p. 165–180, 2018. DOI: https://doi.org/10.1093/aob/mcy063.

ALVES, Ruy José Válka; SILVA, Nélida Gomes da. Flora vascular de canga e quartzito da Serra de São José, Minas Gerais, Brasil. **Rodriguésia**, v. 60, n. 4, p. 817–835, 2009. DOI: https://doi.org/10.1590/2175-7860200960408.

BLOMSTEDT, Cecilia K.; et al. Mechanisms of desiccation tolerance in the resurrection plant Craterostigma plantagineum: modern insights. **Plant, Cell & Environment**, v. 41, n. 11, p. 2520–2534, 2018. DOI: https://doi.org/10.1111/pce.13324.

BONDI, Luiz; MARKS, Russell A; VANBUREN, Robert. Demystifying the convergent ecological specialization of desiccation-tolerant vascular plants for water deficit. **Annals of Botany**, v. 131, n. 3, p. 521–531, 2023. DOI: https://doi.org/10.1093/aob/mcad005.

CAO, Yu; et al. Systematic Analysis of the Maize OSCA Genes Revealing ZmOSCA Involved in Osmotic Stress. **International Journal of Molecular Sciences**, v. 21, n. 11, p. 3844, 2020. DOI: https://doi.org/10.3390/ijms21113844.

CHAKRABORTY, Sudip; et al. Genome-wide characterization and comparative analysis of the OSCA gene family in Camelina sativa. **Scientific Reports**, v. 13, n. 1, p. 5914, 2023. DOI: https://doi.org/10.1038/s41598-023-33226-8.

COLIN, Léia; et al. The cell biology of primary cell walls during salt stress. **The Plant Cell**, v. 35, n. 1, p. 201–217, 2023. DOI: https://doi.org/10.1093/plcell/koac292.

COSTA, Maria-Cecilia D.; et al. A footprint of desiccation tolerance in the genome of the resurrection plant Xerophyta viscosa. **Nature Plants**, v. 3, n. 4, p. 17038, 2017. DOI: https://doi.org/10.1038/nplants.2017.38.

DE MELLO-SILVA, Renato. Morphological analysis, phylogenies and classification in Velloziaceae. **Botanical Journal of the Linnean Society**, v. 148, n. 2, p. 157–173, 2005. DOI: https://doi.org/10.1111/j.1095-8339.2005.00399.x.

DING, Shouren; et al. Genome-wide analysis of maize OSCA family members and their involvement in drought stress. **Plant Science**, v. 286, p. 11–21, 2019. DOI: https://doi.org/10.1016/j.plantsci.2019.05.019.

FARRANT, Jill M.; et al. Desiccation tolerance in the resurrection plant Xerophyta elegans: physiological and ultrastructural aspects of shade adaptation. **Plant Growth Regulation**, v. 28, n. 3, p. 177–185, 1999. DOI: https://doi.org/10.1023/A:1006283626248.

FARRANT, Jill M.; et al. Subcellular and biochemical changes during dehydration and rehydration in the poikilochlorophyllous resurrection plant Xerophyta viscosa. **Journal of Experimental Botany**, v. 58, n. 8, p. 1973–1984, 2007. DOI: https://doi.org/10.1093/jxb/erm055.

FERNANDES, Geraldo Wilson; et al. Plant functional types in the campos rupestres: a framework for ecology and conservation. **Biodiversity and Conservation**, v. 27, n. 12, p. 3087–3107, 2018. DOI: https://doi.org/10.1007/s10531-018-1556-4.

FERNANDES, Geraldo Wilson; et al. Biodiversity and ecosystem services in the Campo Rupestre: A neglected conservation hotspot. **Perspectives in Ecology and Conservation**, v. 18, n. 4, p. 213–222, 2020. DOI: https://doi.org/10.1016/j.pecon.2020.09.006.

GAFF, Donald F.; OLIVER, Melvin J. The evolution of desiccation tolerance in angiosperm plants: a review. **Annals of Botany**, v. 111, n. 4, p. 651–693, 2013. DOI: https://doi.org/10.1093/aob/mct049.

GIVNISH, Thomas J. Adaptive significance of evergreen vs. deciduous leaves: solving the triple paradox. **Silva Fennica**, v. 36, n. 3, p. 703–743, 2002. DOI: https://doi.org/10.14214/sf.535.

GU, Xiao; et al. Genome-wide identification and expression analysis of the OSCA gene family in Pyrus bretschneideri. **International Journal of Biological Macromolecules**, v. 114, p. 831–838, 2018. DOI: https://doi.org/10.1016/j.ijbiomac.2018.03.176.

HAN, Yong; et al. OsOSCA1.1 Mediates Hyperosmolality and Salt Stress Sensing in Rice. **International Journal of Molecular Sciences**, v. 23, n. 24, p. 15993, 2022. DOI: https://doi.org/10.3390/ijms232415993.

HARTMANN, Frank; FIEDLER, Marco. Between Stress and Response: Function and Localization of Mechanosensitive Ca2+ Channels in Herbaceous and Woody Plants. **International Journal of Molecular Sciences**, v. 22, n. 18, p. 9857, 2021. DOI: https://doi.org/10.3390/ijms22189857.

JIE, Li; et al. Identification of Populus tomentosa OSCA Genes and Their Expressional Characteristics in Response to Osmotic Stress. **Plant Gene and Trait**, v. 13, n. 1, p. 1–10, 2022. DOI: https://doi.org/10.5376/pgt.2022.13.0001.

KANG, Xiaoli; ZHAO, Lin; LIU, Xiaojing. Calcium Signaling and the Response to Heat Shock in Crop Plants. **International Journal of Molecular Sciences**, v. 25, n. 1, p. 324, 2023. DOI: https://doi.org/10.3390/ijms25010324.

KAUR, Amandeep; MADHU; UPADHYAY, Santosh Kumar. Mechanosensitive ion channels in plants. In: **Sensory Biology of Plants**. Singapore: Springer, 2021. p. 375–387. DOI: https://doi.org/10.1007/978-981-16-0421-8_16.

KAUR, Amandeep; et al. OSCA Genes in Bread Wheat: Molecular Characterization, Expression Profiling, and Evolutionary Analysis. **International Journal of Molecular Sciences**, v. 23, n. 17, p. 9687, 2022. DOI: https://doi.org/10.3390/ijms23179687.

KE, Ying; et al. OSCA Genes in Liriodendron chinense: Characterization, Evolution and Abiotic Stress Responses. **Frontiers in Plant Science**, v. 13, p. 893630, 2022. DOI: https://doi.org/10.3389/fpls.2022.893630.

LAMBERS, Hans; et al. The phosphorus nutrition of plants in ancient, nutrient‐impoverished landscapes (OCBILs) of Western Australia and south‐eastern Brazil. **Plant and Soil**, v. 476, n. 1-2, p. 69–95, 2022. DOI: https://doi.org/10.1007/s11104-022-05464-8.

LI, Xing; et al. Genome-wide investigation and expression analysis of OSCA gene family in response to abiotic stress in alfalfa (Medicago sativa L.). **BMC Genomics**, v. 24, n. 1, p. 765, 2023. DOI: https://doi.org/10.1186/s12864-023-09857-8.

LI, Yang; et al. Genome-wide survey and expression analysis of the OSCA gene family in rice. **BMC Plant Biology**, v. 15, n. 1, p. 261, 2015. DOI: https://doi.org/10.1186/s12870-015-0653-8.

LI, Yong; et al. Preliminary Expression Analysis of the OSCA Gene Family in Medicago sativa. **International Journal of Molecular Sciences**, v. 23, n. 19, p. 11467, 2022. DOI: https://doi.org/10.3390/ijms231911467.

LIU, Chao; et al. Systematic Characterization of the OSCA Family Members in Soybean and Validation of GmOSCA1.2 and GmOSCA1.4. **International Journal of Molecular Sciences**, v. 23, n. 17, p. 9673, 2022. DOI: https://doi.org/10.3390/ijms23179673.

LIU, Xiaojing; WANG, Jian; SUN, Linfeng. Structure of the hyperosmolality-gated calcium-permeable channel OSCA1.2. **Nature Structural & Molecular Biology**, v. 25, n. 9, p. 845–849, 2018. DOI: https://doi.org/10.1038/s41594-018-0118-5.

LV, Guangyao; et al. Cloning a novel reduced-height (Rht) gene TaOSCA1.4 from a QTL in wheat. **Theoretical and Applied Genetics**, v. 137, n. 3, p. 60, 2024. DOI: https://doi.org/10.1007/s00122-024-04566-5.

MARKS, Russell A.; et al. Convergent evolution of desiccation tolerance in grasses. **Nature Plants**, v. 10, n. 7, p. 1112–1125, 2024. DOI: https://doi.org/10.1038/s41477-024-01729-5.

MARQUES, Danielle M.; et al. Physiological and biochemical mechanisms of desiccation tolerance in Barbacenia purpurea (Velloziaceae). **Functional Plant Biology**, v. 46, n. 4, p. 331–342, 2019. DOI: https://doi.org/10.1071/FP18182.

MIAO, Shan; et al. Identification of OSCA gene family in Solanum habrochaites and its function analysis under stress. **BMC Genomics**, v. 23, n. 1, p. 547, 2022. DOI: https://doi.org/10.1186/s12864-022-08675-6.

MUNDREE, Sagadevan G.; et al. Physiological and molecular insights into drought tolerance. **African Journal of Biotechnology**, v. 1, n. 2, p. 28–38, 2002. DOI: https://doi.org/10.5897/AJB2002.000-006.

OLIVER, Melvin J.; et al. Desiccation tolerance in the resurrection grass Sporobolus stapfianus: a biochemical and transcriptomic analysis. **Plant and Cell Physiology**, v. 52, n. 12, p. 2100–2118, 2011. DOI: https://doi.org/10.1093/pcp/pcr145.

OLIVER, Melvin J.; et al. Desiccation tolerance: from genomics to the field. **Plant Science**, v. 298, p. 110592, 2020. DOI: https://doi.org/10.1016/j.plantsci.2020.110592.

OUNG, Hsin-Mei O.; et al. Differential response of the photosynthetic machinery to dehydration in older and younger resurrection plants. **Journal of Experimental Botany**, v. 73, n. 5, p. 1566–1580, 2021. DOI: https://doi.org/10.1093/jxb/erab485.

RADERMACHER, Alicia M.; et al. Organelle proteostasis during desiccation in Xerophyta schlechteri. **Frontiers in Plant Science**, v. 10, p. 1385, 2019. DOI: https://doi.org/10.3389/fpls.2019.01385.

SHAN, Fang; et al. Evolutionary analysis of the OSCA gene family in sunflower (Helianthus annuus L.) and expression analysis under NaCl stress. **PeerJ**, v. 11, p. e15089, 2023. DOI: https://doi.org/10.7717/peerj.15089.

SHE, Kui; et al. Genome-Wide Identification, Evolution and Expressional Analysis of OSCA Gene Family in Barley (Hordeum vulgare L.). **International Journal of Molecular Sciences**, v. 23, n. 21, p. 13027, 2022. DOI: https://doi.org/10.3390/ijms232113027.

SHERWIN, H. W.; FARRANT, Jill M. Differences in physiological responses to desiccation in resurrection plants. **Plant, Cell & Environment**, v. 19, n. 2, p. 181–191, 1996. DOI: https://doi.org/10.1111/j.1365-3040.1996.tb00239.x.

SILVEIRA, Fernando A. O.; et al. Ecology and evolution of plant diversity in the endangered campo rupestre: a neglected conservation priority. **Plant and Soil**, v. 403, n. 1-2, p. 129–152, 2015. DOI: https://doi.org/10.1111/1365-2637.12462.

SUGUIYAMA, Viviane F.; et al. Desiccation tolerance in the resurrection plant Barbacenia purpurea involves the accumulation of sucrose and raffinose family oligosaccharides. **Plant Biology**, v. 16, n. 3, p. 556–564, 2014. DOI: https://doi.org/10.1111/plb.12088.

SUN, Yi; JARVIS, Paul. Chloroplast Proteostasis: Import, Sorting, Ubiquitination, and Proteolysis. **Annual Review of Plant Biology**, v. 74, p. 259–285, 2023. DOI: https://doi.org/10.1146/annurev-arplant-070122-032532.

SU, Ruolan; et al. Isolation of OSCAs in wheat and over-expression of TaOSCA14D increased salt stress tolerance. **Journal of Plant Physiology**, v. 306, p. 154449, 2025. DOI: https://doi.org/10.1016/j.jplph.2025.154449.

TEODORO, Grazielle Sales; et al. Specialized roots of Velloziaceae weather quartzite rock while mobilizing phosphorus using carboxylates. **Functional Ecology**, v. 33, n. 5, p. 762–773, 2019. DOI: https://doi.org/10.1111/1365-2435.13324.

TEODORO, Grazielle Sales; et al. Desiccation tolerance implies costs to productivity but allows survival under extreme drought conditions in Velloziaceae species in campos rupestres. **Environmental and Experimental Botany**, v. 189, p. 104556, 2021. DOI: https://doi.org/10.1016/j.envexpbot.2021.104556.

THOR, Kathrin; et al. The calcium-permeable channel OSCA1.3 regulates plant stomatal immunity. **Nature**, v. 585, n. 7826, p. 569–573, 2020. DOI: https://doi.org/10.1038/s41586-020-2702-1.

TONG, Kai; et al. Genome-Wide Identification and Expression Profile of OSCA Gene Family Members in Triticum aestivum L. **International Journal of Molecular Sciences**, v. 23, n. 1, p. 469, 2021. DOI: https://doi.org/10.3390/ijms23010469.

VANBUREN, Robert; et al. Single-molecule sequencing of the desiccation-tolerant grass Oropetium thomaeum. **Nature**, v. 527, n. 7579, p. 498–502, 2015. DOI: https://doi.org/10.1038/nature15714.

VANBUREN, Robert; et al. The resurrection plant Selaginella lepidophylla has a compact genome with duplicate gene retention. **Proceedings of the National Academy of Sciences**, v. 115, n. 7, p. E1591–E1599, 2018. DOI: https://doi.org/10.1073/pnas.1717659115.

VERSLUES, Paul E.; et al. Burning questions for a warming and changing world: 15 unknowns in plant abiotic stress. **The Plant Cell**, v. 35, n. 1, p. 67–108, 2023. DOI: https://doi.org/10.1093/plcell/koac263.

VIEIRA, Evandro Alves; et al. Water retention and metabolic changes improve desiccation tolerance in Barbacenia graminifolia (Velloziaceae). **Functional Plant Biology**, v. 49, n. 10, p. 875–887, 2022. DOI: https://doi.org/10.1071/FP21307.

VIEIRA, Evandro Alves; et al. Surviving water scarcity: seasonal contrasts in drought and desiccation tolerance of co-occurring Barbacenia gentianoides and Vellozia caruncularis. **Plant Biology**, v. 27, n. 2, p. 180–194, 2025. DOI: https://doi.org/10.1111/plb.13745.

VOLAIRE, Florence. A unified framework of plant adaptive strategies to drought: Crossing scales and disciplines. **Global Change Biology**, v. 24, n. 7, p. 2929–2938, 2017. DOI: https://doi.org/10.1111/gcb.14062.

VOLAIRE, Florence; et al. From growth potential to drought survival: a trait- and time-based framework for plant water economics across vascular species. **New Phytologist**, v. 249, n. 3, p. 1120–1135, 2026. DOI: https://doi.org/10.1111/nph.20450.

VURUPUTOOR, Vidya S.; et al. Welcome to the big leaves: Best practices for improving genome annotation in non-model plant genomes. **Applications in Plant Sciences**, v. 11, n. 2, p. e11533, 2023. DOI: https://doi.org/10.1002/aps3.11533.

WANGA, Vincent Okelo; et al. Complete Chloroplast Genomes of Acanthochlamys bracteata (China) and Xerophyta (Africa) (Velloziaceae): Comparative Genomics and Phylogenomic Placement. **Frontiers in Plant Science**, v. 12, p. 691833, 2021. DOI: https://doi.org/10.3389/fpls.2021.691833.

WATSON, Samuel J.; SOWDEN, Robert G.; JARVIS, Paul. Abiotic stress-induced chloroplast proteome remodelling: a mechanistic overview. **Journal of Experimental Botany**, v. 69, n. 11, p. 2773–2781, 2018. DOI: https://doi.org/10.1093/jxb/ery053.

WHITTAKER, Allison; et al. Characterization of sucrose and oligosaccharide synthesis during desiccation in Xerophyta viscosa. **Journal of Experimental Botany**, v. 52, n. 358, p. 961–970, 2001. DOI: https://doi.org/10.1093/jexbot/52.358.961.

WHITTAKER, Allison; et al. Galactinol synthase gene expression and RFO accumulation in Xerophyta viscosa. **Physiologia Plantarum**, v. 130, n. 4, p. 556–564, 2007. DOI: https://doi.org/10.1111/j.1399-3054.2007.00936.x.

WU, Xiaoming; et al. Evolution of osmosensing OSCA1 Ca2+ channel family coincident with plant transition from water to land. **The Plant Genome**, v. 15, n. 2, p. e20198, 2022. DOI: https://doi.org/10.1002/tpg2.20198.

XIAO, Lin; et al. Genome sequencing of the resurrection plant Boea hygrometrica provides the first insight into the desiccation tolerance of the eudicot. **Proceedings of the National Academy of Sciences**, v. 112, n. 18, p. 5838–5843, 2015. DOI: https://doi.org/10.1073/pnas.1505399112.

YANG, Lihua; et al. Genome-wide identification of castor bean OSCA genes and analysis of their function under drought and salt stress. **BMC Plant Biology**, v. 26, n. 1, p. 661, 2026. DOI: https://doi.org/10.1186/s12870-026-06610-w.

YANG, Shuning; et al. Identification and Expression Profile Analysis of the OSCA Gene Family Related to Abiotic and Biotic Stress Response in Cucumber. **Biology**, v. 11, n. 8, p. 1134, 2022. DOI: https://doi.org/10.3390/biology11081134.

YANG, Xiaoyan; et al. Genome-wide identification of OSCA gene family and their potential function in dehydration and salt stress in Gossypium hirsutum. **BMC Genomics**, v. 20, n. 1, p. 831, 2019. DOI: https://doi.org/10.1186/s12864-019-6184-7.

YIN, Lin; et al. Genome-wide analysis of OSCA gene family members in Vigna radiata. **BMC Plant Biology**, v. 21, n. 1, p. 574, 2021. DOI: https://doi.org/10.1186/s12870-021-03362-z.

YUAN, Feng; et al. OSCA1 mediates osmotic-stress-evoked Ca2+ increases vital for osmosensing in Arabidopsis. **Nature**, v. 514, n. 7522, p. 367–371, 2014. DOI: https://doi.org/10.1038/nature13593.

ZAPPI, Daniela C.; et al. Flora das cangas da Serra dos Carajás, Pará, Brasil: Velloziaceae. **Rodriguésia**, v. 68, n. 3, p. 1109–1114, 2017. DOI: https://doi.org/10.1590/2175-7860201768349.

ZHAI, Yujie; et al. Heterogeneous expression of plasma-membrane-localised OsOSCA1.4 complements osmotic sensing. **Cell Calcium**, v. 91, p. 102264, 2020. DOI: https://doi.org/10.1016/j.ceca.2020.102264.

ZHAI, Yujie; et al. Functional analysis of rice OSCA genes overexpressed in the arabidopsis osca1 mutant. **Plant Cell Reports**, v. 40, n. 10, p. 1935–1946, 2021. DOI: https://doi.org/10.1007/s00299-021-02758-6.

ZHANG, Min; et al. Structure of the mechanosensitive OSCA channels. **Nature Structural & Molecular Biology**, v. 25, n. 9, p. 850–858, 2018. DOI: https://doi.org/10.1038/s41594-018-0117-6.

ZHANG, Qian-Yi; et al. Genome-Wide Identification, Phylogeny, and Abiotic Stress Response Analysis of OSCA Family Genes in Notopterygium franchetii. **International Journal of Molecular Sciences**, v. 26, n. 11, p. 5043, 2025. DOI: https://doi.org/10.3390/ijms26115043.

ZHANG, Xiao; et al. Genome-wide analysis of hyperosmolality-gated calcium-permeable channel (OSCA) family members in Brassica napus. **Gene**, v. 856, p. 147137, 2023. DOI: https://doi.org/10.1016/j.gene.2022.147137.

ZHU, Xiao; et al. Genome-wide identification and characterization of OSCA genes in white clover revealing their function in response to abiotic stresses. **BMC Plant Biology**, v. 25, n. 1, p. 45, 2025. DOI: https://doi.org/10.1186/s12870-025-06045-3.
