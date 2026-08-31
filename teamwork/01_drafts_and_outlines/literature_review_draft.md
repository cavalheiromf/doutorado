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

This cellular shrinkage occurs not across an isolated lipid bilayer, but within the integrated cell wall–plasma membrane–cytoskeleton continuum (COLIN et al., 2023). As turgor pressure drops towards zero, the mechanical tethering between the plasma membrane and the primary cell wall pectin-cellulose network experiences severe shearing forces. In primary cell walls, homogalacturonan (HG) pectins cross-linked by calcium ions ($Ca^{2+}$) serve as both a mechanical support matrix and an extracellular calcium reservoir (COLIN et al., 2023). De-esterification of pectins by pectin methylesterases (PMEs) and wall loosening by expansins and xyloglucan endotransglucosylases/hydrolases (XTHs) modulate cell wall rheology, permitting harmonious cell wall folding while preventing cytorrhysis (the irreversible collapse of the wall inward) and avoiding membrane-wall delamination (COLIN et al., 2023; TEODORO et al., 2021). The local release of wall-bound calcium during matrix deformation directly interfaces with plasma membrane mechanosensors, establishing a coordinated continuum of early mechanoperception.

When protoplasmic water content falls below 10–20% of full turgor ($\Psi < -100\text{ MPa}$), terminal cellular desiccation occurs, causing severe macromolecular crowding and membrane phase transitions. In sensitive species, this induces irreversible membrane lysis and cell death; in resurrection plants, coordinated biochemical programs stabilize the desiccated protoplast in a vitrified, quiescent state (BONDI; MARKS; VANBUREN, 2023; TEODORO et al., 2021).

These divergent physiological trajectories rely on distinct cellular and metabolic adaptations (BONDI; MARKS; VANBUREN, 2023; VIEIRA et al., 2025). Avoidant species maintain high foliar water potentials during drought through tight abscisic acid (ABA)- and jasmonate-mediated stomatal closure, osmolyte accumulation (proline, glycine betaine), and extensive root foraging (TEODORO et al., 2019; ABRAHÃO et al., 2018). An evergreen habit sustains year-round carbon capture, but leaves these plants vulnerable to conduit cavitation if water potential drops below $\Psi_{TLP}$ (ALCANTARA et al., 2015; VIEIRA et al., 2022).

Resurrection plants, in contrast, poikilohydrically equilibrate with atmospheric water potential. During dehydration, they convert starch reserves into non-reducing sugars (sucrose, trehalose, and raffinose family oligosaccharides [RFOs]), which substitute for water hydrogen bonds on macromolecular surfaces and induce cytoplasmic vitrification to form an amorphous glassy matrix that prevents protein denaturation and membrane crystallization (VIEIRA et al., 2022; BONDI; MARKS; VANBUREN, 2023). Simultaneously, cell walls remodel with arabinose- and pectin-rich polymers, allowing the wall to fold in unison with the shrinking protoplast and preserve plasma membrane integrity (COLIN et al., 2023; TEODORO et al., 2021). Vacuoles fragment into multiple microvacuoles loaded with osmolytes to preserve subcellular compartmentalization. To minimize photo-oxidative damage, tolerant plants either degrade their chlorophylls or deploy high-capacity non-photochemical quenching (NPQ/qE), cyclic electron transport (CET), and enzymatic antioxidant cascades to scavenge Reactive Oxygen Species (ROS) (OUNG et al., 2021; THOR et al., 2020; HAN et al., 2022; BONDI; MARKS; VANBUREN, 2023).

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

> **Figure 1. Natural comparative model of drought persistence strategies in Velloziaceae.** Schematic representation of *Vellozia tubiflora* (desiccation-tolerant, DT) and *Vellozia peripherica* (dehydration-avoidant, evergreen) across microhabitat gradients in the *campos rupestres*, illustrating differential leaf rolling, turgor loss thresholds ($\Psi_{TLP}$), cellular anhydrobiosis, and hydraulic safety margins.

---

# 3. Comparative Genomics and Macroevolutionary Dynamics of Adaptation

Comparative genomics provides the computational framework to determine whether divergent ecological strategies correlate with broad chromosomal reorganizations, copy-number variations, or family-specific evolutionary rates (WU et al., 2022; LI et al., 2023). The foundation relies on high-contiguity chromosomal assemblies evaluated by metrics such as BUSCO, followed by structural annotation supported by multi-tissue RNA-seq data (VURUPUTOOR et al., 2023). Functional annotation incorporates Hidden Markov Models (HMM) to query conserved protein domain databases (Pfam, SMART, CDD). In the context of early osmotic signaling, the structural domain DUF221 (Pfam: PF02714) identifies members of the hyperosmolality-gated calcium-permeable OSCA family (ZHANG et al., 2018; LIU et al., 2022; YUAN et al., 2014). OSCA proteins display a modular tripartite architecture: an N-terminal RSN1_TM domain (PF13967) associated with membrane trafficking, a central PHM7_cyt cytosolic loop (PF14703) functioning as a mechanical scaffold, and the C-terminal DUF221 pore domain (PF02714) that conducts calcium fluxes under membrane lateral tension.

Homology relationships distinguish orthologs (genes diverged via speciation) from paralogs (genes generated via duplication) (WU et al., 2022; LI et al., 2023). Software packages such as OrthoFinder group translated proteomes into shared orthogroups to quantify lineage-specific expansions and contractions. Synteny and collinearity analyses (via MCScanX and Circos) elucidate the mechanistic origin of duplicated loci, categorizing them into Whole-Genome Duplications (WGD), segmental duplications, tandem expansions, proximal, or dispersed duplications (BONDI; MARKS; VANBUREN, 2023; MARKS et al., 2024; YANG et al., 2019; TONG et al., 2021).

Codon-based evolutionary models evaluate selective pressures on coding sequences through the ratio of non-synonymous ($Ka$) to synonymous ($Ks$) substitutions (WU et al., 2022; LI et al., 2023). Values of $Ka/Ks < 1$ indicate purifying (stabilizing) selection, $Ka/Ks = 1$ denotes neutral evolution, and $Ka/Ks > 1$ reveals positive (diversifying) selection (GU et al., 2018; SHE et al., 2022; SHAN et al., 2023; ZHU et al., 2025). In parallel, synonymous substitution distributions ($Ks$) estimate the relative timing of duplication and speciation events ($T = Ks / 2r$). Post-duplication functional divergence is evaluated using tools such as DIVERGE, which classify amino acid shifts into Type I (shifts in site-specific evolutionary rates) and Type II (radical changes in physicochemical properties). Establishing this macroevolutionary landscape provides the necessary genetic backdrop to dissect the discrete molecular sensors that initiate stress perception.

---

# 4. Primary Osmosensing and the OSCA Mechanosensitive Calcium Channel Family

## 4.1 The Search for Primary Osmosensors in Plants

Downstream drought signaling pathways are well mapped. Yet the primary biophysical mechanisms by which plant cells first sense water deficit remain one of the defining grand challenges in modern plant biology (VERSLUES et al., 2023; ZHANG et al., 2018; LIU et al., 2022; HARTMANN; FIEDLER, 2021). In a landmark international consensus on plant abiotic stress biology, Verslues et al. (2023) identified resolving the molecular identity and biophysical discrimination of primary osmosensors as a foundational unknown: plant cells must instantly distinguish purely mechanical changes in turgor pressure from chemical macromolecular crowding, ionic shifts, and localized cell wall deformations.

Osmotic stress rapidly alters membrane-cell wall biomechanics through three interconnected pathways: plasma membrane sensors, cell wall integrity sentinels, and mechanosensitive ion channels (COLIN et al., 2023; VERSLUES et al., 2023). Early paradigms proposed the *Arabidopsis* histidine kinase AtHK1 as the primary osmosensor (THOR et al., 2020; HAN et al., 2022); however, *athk1-null* mutants display normal cytosolic calcium signaling under hyperosmotic shock, indicating the presence of independent mechanosensory channels. As cell volume contracts under dehydration, tensile stress develops at the cell wall-membrane interface, where Receptor-Like Kinases (RLKs, such as FERONIA and THE1) monitor this biomechanical strain, modulating ABA accumulation and evoking late calcium transients to induce cell wall remodeling (COLIN et al., 2023).

Mechanosensitive (MS) ion channels are the fastest sensors capable of converting lipid bilayer physical deformation directly into intracellular chemical signals (ZHANG et al., 2018; LIU et al., 2022; KAUR; MADHU; UPADHYAY, 2021). Tension changes directly gate the channel pore, driving rapid $Ca^{2+}$ influx from the apoplast within seconds ($OICI_{cyt}$) (THOR et al., 2020; HAN et al., 2022). Alternative plant mechanosensitive families fulfill specialized functions: MSL channels are predominantly anion-selective and operate in hypoosmotic relief; MCA channels are calcium-permeable, but *mca1/mca2* mutants maintain normal hyperosmotic calcium spikes; and plant Piezo channels participate primarily in root penetration mechanotransduction (HARTMANN; FIEDLER, 2021; KAUR; MADHU; UPADHYAY, 2021). Consequently, the OSCA (*hyperosmolality-gated calcium-permeable channels*) family stands out as the only plant mechanosensor class whose direct gating by membrane lateral tension and rapid $Ca^{2+}$ conductance under hyperosmotic shock have been unequivocally demonstrated (ZHANG et al., 2018; LIU et al., 2022; YUAN et al., 2014). This leaves OSCA at the apex of osmotic mechanoperception. Thus, comparative analysis of OSCA channels between *V. tubiflora* and *V. peripherica* provides an ideal platform to uncover the molecular foundations of early water sensing.

## 4.2 Molecular Architecture, Phylogeny, and Biophysical Gating of OSCA Channels

The founder locus OSCA1 (*AtOSCA1.1*) was isolated in *Arabidopsis thaliana* as the essential channel mediating hyperosmolality-induced $Ca^{2+}$ increase (YUAN et al., 2014; HAN et al., 2022). Knockout *osca1* plants exhibit abolished root $OICI_{cyt}$ waves and defective stomatal closure, leading to accelerated dehydration (ZHANG et al., 2018). *AtOSCA1.2* was subsequently validated as an active paralog sharing 85% sequence identity (LIU; WANG; SUN, 2018; LIU et al., 2022). OSCA homologs possess an exclusive 180-amino-acid cytosolic gating loop. Plant genomes underwent substantial lineage-specific expansions of this family, ranging from 15 in *Arabidopsis* (YUAN et al., 2014) to 42 in bread wheat (TONG et al., 2021; KAUR et al., 2022).

Phylogenetically, the family comprises four monophyletic clades (WU et al., 2022; LI et al., 2023): Clade I mediates hyperosmotic perception at the plasma membrane; Clade II regulates developmental osmotic control; Clade III features low copy-number retention and early drought responsiveness; and Clade IV represents the basal single-exon lineage. Evolutionary genomics indicates that OSCA diversified during the land plant transition, expanding via whole-genome duplications to equip stomata, roots, and vascular tissues with precise osmosensors (WU et al., 2022; KE et al., 2022; YUAN et al., 2014).

Single-particle cryo-EM structures reveal that OSCA channels assemble as symmetrical homodimers perpendicular to the plasma membrane (ZHANG et al., 2018; LIU; WANG; SUN, 2018; LIU et al., 2022). The transmembrane domains of each subunit remain physically separated by a central hydrophobic cavity, with dimerization stabilized exclusively by cytosolic hydrogen bonding networks. Each monomer comprises 11 transmembrane helices (M0–M10) organized into three functional domains: an N-terminal domain (RSN1_TM, PF13967) stabilizing membrane insertion, a central cytosolic domain (PHM7_cyt, PF14703) acting as a biomechanical scaffold, and a C-terminal DUF221 domain (RSN1_7TM, PF02714) forming the ion-conducting pore.

Gating operates via a "force-from-lipid" mechanism: membrane stretching pulls a hydrophobic anchor (consensus motif `LGFLGLWG`), levering the gating helix M6 to straighten around a conserved glycine hinge (G528 in AtOSCA1.1) (ZHANG et al., 2018; LIU et al., 2022). This movement rotates bulky aromatic residues away from the pore axis, opening a conductive pathway ($>5.5\text{ Å}$) for hydrated $Ca^{2+}$ influx. Isoforms lacking this cytosolic anchor fail to rescue osmotic $Ca^{2+}$ deficiency, demonstrating the sensory centrality of the cytosolic arm.

> **Figure 2. Structural architecture and "force-from-lipid" gating mechanism of the OSCA mechanosensitive calcium channel.** (A) Symmetrical homodimeric architecture with $C_2$ rotational axis, highlighting the transmembrane DUF221 pore (PF02714), the cytosolic scaffold (PHM7_cyt / RRM, PF14703), and the N-terminal anchor (RSN1_TM, PF13967). (B) Detailed biophysical mechanotransduction model showing membrane lateral tension pulling the cytosolic `LGFLGLWG` hydrophobic anchor, straightening the gating helix M6 around the conserved glycine hinge (G528), and opening the central pore ($>5.5\text{ Å}$) for rapid $Ca^{2+}$ influx.

## 4.3 Cis-Regulatory Architecture, Expression Dynamics, and Interaction Networks

Promoter regions of OSCA genes harbor diverse cis-regulatory elements mediating environmental responsiveness (LI et al., 2015; DING et al., 2019; GU et al., 2018; ZHANG et al., 2023; MIAO et al., 2022): ABRE governing bZIP-driven transcription under drought; DRE/CRT regulating rapid ABA-independent activation; MBS and LTR driving responses to physical desiccation and cold stress; and CGTCA/TGACG motifs mediating jasmonate signaling (LI et al., 2023). Spatiotemporal expression profiles show high transcript abundance in roots, vascular bundles, and pollen (JIE et al., 2022; LI et al., 2022), alongside marked post-duplication subfunctionalization in paralogous pairs (YANG et al., 2026; WU et al., 2022; LI et al., 2023).

Downstream of the lipid bilayer, protein-protein interaction (PPI) networks couple OSCA channels to transcriptional regulators and signaling kinases (ZHANG et al., 2018; LIU et al., 2022). In *Arabidopsis*, AtOSCA1.3 is phosphorylated at Ser54 by the immune kinase BIK1 upon flg22 perception, rapidly gating calcium influx to execute stomatal closure during pathogen attack (THOR et al., 2020; HAN et al., 2022). In maize, ZmOSCA2.3 and ZmOSCA2.4 physically interact with transcription factor ZmEREB198 to modulate proline accumulation (CAO et al., 2020). In wheat, TaOSCA1.4 functions as a QTL regulator coupling turgor signaling to vegetative shoot elongation (LV et al., 2024; SU et al., 2025).

---

# 5. Scientific Propositions: Gaps, Hypotheses, and Research Objectives

## 5.1 Specific Gap and Integrating Hypotheses

While late-stage drought adaptations in *campos rupestres* plants are widely documented, the early molecular mechanisms through which cells perceive water deficit and trigger divergent physiological trajectories remain largely unknown, directly intersecting with the grand challenges of plant abiotic stress research (VERSLUES et al., 2023). The congeneric pair *Vellozia tubiflora* (desiccation-tolerant) and *Vellozia peripherica* (evergreen, desiccation-sensitive) represents an ideal comparative model: sharing the same evolutionary history and macroclimate, they display diametrically opposed strategies under acute drought (ALCANTARA et al., 2015; VIEIRA et al., 2022).

**General Hypothesis:** The contrasting ecophysiological responses to water deficit in *V. tubiflora* and *V. peripherica* are driven by multilevel molecular divergence, spanning broad genomic architecture, gene family dynamics, structural features, and transcriptional regulation of primary mechanosensory components.

**Specific Hypotheses:**
1. **Broad Genomic Divergence Hypothesis:** Chromosomal organization, syntenic collinearity, and family expansion/contraction dynamics reflect the evolutionary signatures of their respective ecological strategies.
2. **OSCA Channel Structural Conservation Hypothesis:** Core OSCA domain topology and pore-lining residues remain highly conserved in both species due to purifying selection on basic ion conduction.
3. **OSCA Regulatory and Transcriptional Divergence Hypothesis:** Temporal kinetics and stress responsiveness diverge significantly in promoter cis-element composition, producing early, coordinated activation in *V. tubiflora* versus conservative expression in *V. peripherica*.
4. **Interaction Network Specialization Hypothesis:** OSCA protein-protein interaction networks exhibit differential wiring, preferentially integrating with cell wall integrity and ABA cascades in *V. tubiflora*, and with osmotic homeostasis in *V. peripherica*.

---

## 5.2 Objectives and Thesis Structure

**General Objective:** To investigate the comparative genomics of *Vellozia tubiflora* and *Vellozia peripherica*, delineating global evolutionary signatures associated with their contrasting drought adaptations, and systematically characterizing the molecular, evolutionary, and regulatory determinants of the OSCA mechanosensitive calcium channel family.

**Specific Objectives:**

**Chapter 1 (Large-Scale Comparative Genomics):**
1. Quantify the completeness, contiguity, and quality of chromosomal assemblies and annotations of *V. tubiflora* and *V. peripherica* using metrics such as BUSCO and RNA-seq alignments.
2. Group the predicted proteomes into orthogroups using OrthoFinder to establish high-confidence orthology and paralogy relationships.
3. Map syntenic collinearity blocks via MCScanX/Circos and categorize duplication mechanisms.
4. Model gene family expansion and contraction dynamics (CAFE) and estimate selection regimes ($Ka/Ks$) and functional divergence (DIVERGE).

**Chapter 2 (Characterization of the OSCA Family):**
1. Identify all OSCA family members in both genomes using Hidden Markov Model profiles for the DUF221 domain (PF02714).
2. Reconstruct phylogenetic relationships with monocot/dicot models, classifying genes into the four conserved clades.
3. Model exon-intron architectures, and membrane domain topologies.
4. Map and compare cis-regulatory promoter elements (-2000 bp) via PlantCARE to assess hormone and stress sensitivity.
5. Predict protein-protein interaction (PPI) networks to identify functional partners in early stress signal transduction.

The thesis progresses logically from the whole-genome macroevolutionary framework (Chapter 1) to the high-resolution characterization of the candidate mechanosensory gene family (Chapter 2), establishing predictive molecular hypotheses for future functional validation.

> **Figure 3. Integrated bioinformatic and evolutionary workflow of the doctoral thesis.** Methodological roadmap bridging whole-genome comparative genomics (Chapter 1) with fine-scale target characterization of the OSCA mechanosensory channel family (Chapter 2).

---

# References

ABRAHÃO, Anna; et al. Soil types select for plants with matching nutrient‐acquisition and ‐use traits in hyperdiverse and severely nutrient‐impoverished campos rupestres and cerrado in central Brazil. **Journal of Ecology**, v. 107, n. 3, p. 1302–1316, 2018. DOI: https://doi.org/10.1111/1365-2745.13111.

ALCANTARA, Suzana; et al. Carbon assimilation and habitat segregation in resurrection plants: a comparison between desiccation‐ and non‐desiccation‐tolerant species of Neotropical Velloziaceae (Pandanales). **Functional Ecology**, v. 29, n. 12, p. 1499–1512, 2015. DOI: https://doi.org/10.1111/1365-2435.12462.

ALCANTARA, Suzana; REE, Richard H; MELLO-SILVA, Renato. Accelerated diversification and functional trait evolution in Velloziaceae reveal new insights into the origins of the campos rupestres’ exceptional floristic richness. **Annals of Botany**, v. 122, n. 1, p. 165–180, 2018. DOI: https://doi.org/10.1093/aob/mcy063.

ALVES, Ruy José Válka; SILVA, Nélida Gomes da. Flora vascular de canga e quartzito da Serra de São José, Minas Gerais, Brasil. **Rodriguésia**, v. 60, n. 4, p. 817–835, 2009. DOI: https://doi.org/10.1590/2175-7860200960408.

BONDI, Luiz; MARKS, Russell A; VANBUREN, Robert. Demystifying the convergent ecological specialization of desiccation-tolerant vascular plants for water deficit. **Annals of Botany**, v. 131, n. 3, p. 521–531, 2023. DOI: https://doi.org/10.1093/aob/mcad005.

CAO, Yu; et al. Systematic Analysis of the Maize OSCA Genes Revealing ZmOSCA Involved in Osmotic Stress. **International Journal of Molecular Sciences**, v. 21, n. 11, p. 3844, 2020. DOI: https://doi.org/10.3390/ijms21113844.

CHAKRABORTY, Sudip; et al. Genome-wide characterization and comparative analysis of the OSCA gene family in Camelina sativa. **Scientific Reports**, v. 13, n. 1, p. 5914, 2023. DOI: https://doi.org/10.1038/s41598-023-33226-8.

COLIN, Léia; et al. The cell biology of primary cell walls during salt stress. **The Plant Cell**, v. 35, n. 1, p. 201–217, 2023. DOI: https://doi.org/10.1093/plcell/koac292.

COSTA, Maria-Cecilia D.; et al. A footprint of desiccation tolerance in the genome of the resurrection plant Xerophyta viscosa. **Nature Plants**, v. 3, n. 4, p. 17038, 2017. DOI: https://doi.org/10.1038/nplants.2017.38.

DE MELLO-SILVA, Renato. Morphological analysis, phylogenies and classification in Velloziaceae. **Botanical Journal of the Linnean Society**, v. 148, n. 2, p. 157–173, 2005. DOI: https://doi.org/10.1111/j.1095-8339.2005.00399.x.

DING, Shouren; et al. Genome-wide analysis of maize OSCA family members and their involvement in drought stress. **Plant Science**, v. 286, p. 11–21, 2019. DOI: https://doi.org/10.1016/j.plantsci.2019.05.019.

FERNANDES, Geraldo Wilson; et al. Plant functional types in the campos rupestres: a framework for ecology and conservation. **Biodiversity and Conservation**, v. 27, n. 12, p. 3087–3107, 2018. DOI: https://doi.org/10.1007/s10531-018-1556-4.

FERNANDES, Geraldo Wilson; et al. Biodiversity and ecosystem services in the Campo Rupestre: A neglected conservation hotspot. **Perspectives in Ecology and Conservation**, v. 18, n. 4, p. 213–222, 2020. DOI: https://doi.org/10.1016/j.pecon.2020.09.006.

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

MIAO, Shan; et al. Identification of OSCA gene family in Solanum habrochaites and its function analysis under stress. **BMC Genomics**, v. 23, n. 1, p. 547, 2022. DOI: https://doi.org/10.1186/s12864-022-08675-6.

OLIVER, Melvin J.; et al. Desiccation tolerance in the resurrection grass Sporobolus stapfianus: a biochemical and transcriptomic analysis. **Plant and Cell Physiology**, v. 52, n. 12, p. 2100–2118, 2011. DOI: https://doi.org/10.1093/pcp/pcr145.

OUNG, Hsin-Mei O.; et al. Differential response of the photosynthetic machinery to dehydration in older and younger resurrection plants. **Journal of Experimental Botany**, v. 73, n. 5, p. 1566–1580, 2021. DOI: https://doi.org/10.1093/jxb/erab485.

SHAN, Fang; et al. Evolutionary analysis of the OSCA gene family in sunflower (Helianthus annuus L.) and expression analysis under NaCl stress. **PeerJ**, v. 11, p. e15089, 2023. DOI: https://doi.org/10.7717/peerj.15089.

SHE, Kui; et al. Genome-Wide Identification, Evolution and Expressional Analysis of OSCA Gene Family in Barley (Hordeum vulgare L.). **International Journal of Molecular Sciences**, v. 23, n. 21, p. 13027, 2022. DOI: https://doi.org/10.3390/ijms232113027.

SILVEIRA, Fernando A. O.; et al. Ecology and evolution of plant diversity in the endangered campo rupestre: a neglected conservation priority. **Plant and Soil**, v. 403, n. 1-2, p. 129–152, 2015. DOI: https://doi.org/10.1007/s11104-015-2637-8.

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
