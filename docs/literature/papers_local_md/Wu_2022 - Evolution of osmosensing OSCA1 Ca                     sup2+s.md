# Wu_2022 - Evolution of osmosensing OSCA1 Ca                     sup2+s

**Source PDF:** 

---

Received: 5 November 2021       Accepted: 27 January 2022

DOI: 10.1002/tpg2.20198

                                                                                                                                              The Plant Genome
ORIGINAL RESEARCH




Evolution of osmosensing OSCA1 Ca2+ channel family coincident
with plant transition from water to land

Xiaomei Wu1,2,#                      Fang Yuan1,2,#                     Xuewen Wang3                           Shan Zhu1                     Zhen-Ming Pei2

1 Collegeof Life and Environmental
Sciences, Hangzhou Normal Univ.,                        Abstract
Hangzhou 311121, China                                  Water is crucial to plant growth, development, and environmental adaptation. Water
2 Dep.
     of Biology, Duke Univ., Durham, NC                 stress triggers cytosolic Ca2+ ([Ca2+ ]i ) increases, and the osmosensor OSCA1
27708, USA
3 Center
                                                        (REDUCED-HYPEROSMOLALITY-INDUCED-[Ca2+ ]i -INCREASE 1), a mem-
        for Human Identification, Univ. of
North Texas Health Science Center, Fort                 ber of the OSCA family, perceives the initial water stress and governs its down-
Worth, TX 76107, USA                                    stream responses. OSCA homologs exist in eukaryotes and largely radiate in higher
                                                        plants. However, it is enigmatic whether the OSCA family is crucial for plant evolu-
Correspondence
Zhen-Ming Pei, Dep. of Biology, Duke                    tion from aqueous to terrestrial environments and for the subsequent adaptation on
Univ., Durham, NC, 27708, USA.                          land. Here, we carried out the first phylogenetic and molecular evolutionary analyses
Xiaomei Wu, College of Life and
Environmental Sciences, Hangzhou Normal
                                                        of the OSCA family. The family originated and diversified during the early evolution
Univ., Hangzhou, 311121, China.                         of protists, and three more lineages were established (a) in plants, (b) in fungi, and (c)
Email: zpei@duke.edu;                                   in a complex clade of several major eukaryotic lineages. The chlorophyte algal clus-
wuxm07@gmail.com
                                                        ter is directly basal to streptophyte-specific Clades 1–3, consistent with plant tran-
Assigned to Associate Editor Lin Li.                    sition from water to land. The Clades 1–3 present different gene expansion pattern
# Theseauthors contributed equally to this
                                                        and together with previous functional analysis of OSCAs reveal that they probably
work.
                                                        have evolved diverse functions in respond to various mechanical stresses during the
Funding information                                     independent evolution of land plant clades. Moreover, variable selection pressures on
Natural Science Foundation of Zhejiang
                                                        different land plant lineages were explored. OSCAs in early land plants (mosses and
Province, Grant/Award Numbers:
LY18C050005, LY19C020004,                               lycophytes) were under decelerated evolution, whereas OSCAs in seed plants showed
LZ16C020001; US National Science                        accelerated evolution. Together, we hypothesize OSCAs have evolved to sense water
Foundation, Grant/Award Number:
IOS-1457257; National Natural Science
                                                        stress in the ancestor of euphyllophytes, which occupies typical leaves, typical roots,
Foundation of China, Grant/Award Number:                and phloem tissues, all of which require osmosensors to maintain water balance and
31571461; Zhejiang Major Scientific and                 food conduction through plant bodies.
Technological Project of Agricultural
(Upland crop) Breeding, Grant/Award
Number: 2021C02064-6




Abbreviations: DEG/ENaC, degenerin/epithelial sodium channel; HMM, hidden Markov model; LRT, likelihood ratio tests; ML, maximum likelihood;
MscS, mechanosensitive channel of small conductance; MSL, MscS-like; TM, transmembrane; TMC, transmembrane channel-like; WGD, whole-genome
duplication.

This is an open access article under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs License, which permits use and distribution in any medium, provided
the original work is properly cited, the use is non-commercial and no modifications or adaptations are made.
© 2022 The Authors. The Plant Genome published by Wiley Periodicals LLC on behalf of Crop Science Society of America.

Plant Genome. 2022;15:e20198.                                                                                                wileyonlinelibrary.com/journal/tpg2      1 of 19
https://doi.org/10.1002/tpg2.20198
                                                                                                                                      19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
2 of 19    The Plant Genome                                                                                               WU ET AL.



1         INTRODUCTION
                                                                      Core Ideas
Water is vital to all known forms of life on earth. Water
                                                                      ∙ The evolution of OSCA1 family is coincident with
on the earth surface serves as a home for life, where most
life forms are considered to evolve initially from. During the          plant colonization on land.
                                                                      ∙ Variable selection pressures during the land plant
Paleozoic era, plants and animals took an important tran-
sition from the aquatic environments to land for the first              evolution were proposed.
                                                                      ∙ We hypothesized OSCAs may start sensing water
time (Kenrick & Crane, 1997; Little, 1990). This transition
allowed plants to benefit from plentiful carbon dioxide in the          stress in the ancestor of euphyllophytes.
                                                                      ∙ Living vertebrates keep most of the TMEM63
atmosphere and mineral nutrients in the soil. Animals could
escape predators and competition in the water and acquired              genes gained through the whole-genome duplica-
more oxygen on land. Water is also the most abundant con-               tions.
stituent of most organisms as both a solvent and a deliv-
ery mechanism, dissolving essential nutrients and metabolites
and transporting them to cells. To maintain water balance,        been reported to respond to changes in osmotic pressure so
cells undergo a process called osmosis, which is the diffu-       far in animals (Hamilton, et al., 2015b).
sion of water molecules from a place of higher water con-            Land plants evolved from green algae, which live in
centration (hypoosmotic side) to a place of lower water con-      water, during the middle Cambrian–Early Ordovician inter-
centration (hyperosmotic side) across a selectively permeable     val, approximately 515 to 475 million yr ago (Kenrick &
membrane. Thus, osmotic pressure is critical to proper devel-     Crane, 1997; Morris et al., 2018). In the colonization on land,
opment, environmental stress response, and overall cellular       plants experienced a series of body plan transitions linked
health in a wide variety of organisms (Hamilton et al., 2015b).   with major evolutionary innovations to deal with water on
   Mechanical signals include osmotic pressure, gravity,          the land. Such key morphological characters include epider-
and touch from the external and internal environments             mis, rooting and shooting systems, stomata, water-conducting
(Arnadottir & Chalfie, 2010; Kung, 2005; Monshausen &             cells, and food-conducting cells (Catarino et al., 2016; Doyle,
Gilroy, 2009). Bacterial and animal mechanosensitive ion          2013; Ohtani et al., 2017). Bryophytes, the earliest, nonva-
channels have been characterized to respond to osmotic pres-      scular land plants, show the stepwise origin of terrestrial
sure in their environment. Bacterial cells survive exposure       adaptations. The most striking was the origin of stomata for
to environmental extremes. A rapid decrease in the external       gas exchange and water loss in bryophytes (Edwards et al.,
osmolarity results in an acute and massive water influx into      1998). The developmental programs for water-conducting
the cell, which increases membrane tension. The Escherichia       cells and food-conducting cells have been also acquired within
coli mechanosensitive channel of small conductance (MscS)         bryophytes (Ohtani et al., 2017). The conductive efficiencies
opens in response to extreme turgor and serves as an emer-        of these conducting cells have improved during land plant evo-
gency safety valve to prevent cell lysis under conditions of      lution. The well-developed conduction system in extant plants
hypoosmotic shock (Booth & Blount, 2012; Levina et al.,           is the vascular bundle system, which is composed of xylem
1999). In animals, four classes of ion channels, namely           and phloem in vascular plants (Ohtani et al., 2017; Venturas
degenerin/epithelial sodium channel (DEG/ENaC), transient         et al., 2017). Xylem, consisting of dead cells, transports water
receptor potential (TRP), Piezo, and transmembrane channel-       and minerals from roots to the top of the plants as explained
like (TMC), belong to bona fide mechano-gated channels that       by the cohesion–tension theory (Schenk et al., 2017). Phloem
mediate multiple sensory pathways (Delmas & Coste, 2013;          transports carbohydrates from leaves to the rest of the plant,
Kefauver et al., 2020). At least one TRP channel, TRPV4,          and this process is mediated by constant water flow through
enables animal cells to detect hypoosmolality in their local      osmosis (Riedell & Schumacher, 2009). Roots, which absorb
environment and functions as an osmosensor (Servin-Vences         water and minerals from soil, and leaves, which store energy
et al., 2017) and the Drosophila melanogaster mechanosen-         from the sun through photosynthesis, evolved quite inde-
sor, NompC/TRPN, is a bona fide mechanosensitive                  pendently in two vascular plant lineages, namely lycophytes
channel (Walker et al., 2000; Yan et al., 2013). Piezo1           (early vascular plants) and euphyllophytes (ferns and seed
mediates osmotic control and membrane perturbation in             plants) (Doyle, 2013; Matsunaga & Tomescu, 2016). Typical
vertebrates (Servin-Vences et al., 2017; Syeda et al., 2016).     roots and typical leaves were formed in euphyllophytes dat-
Two TMC channels (TMC1 and TMC2) are candidate                    ing to approximately 420 million yr ago (Morris et al., 2018).
mechanically activated ion channels in hair cells (Jia et al.,    Osmosis is the fundamental driving force of the water uptake
2020), and DEG/ENaC mediates touch response but has not           in roots, the control of stomatal open and closure in leaves, and
                                                                                                                                        19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
WU ET AL.                                                                                         The Plant Genome            3 of 19


the conduction of carbohydrates in phloem tissues (Passioura,       roots, leaves, and phloem tissues with osmosensors installed
2001; Riedell & Schumacher, 2009). Through osmosis, plant           to maintain water balance and nutrition movement through
cells maintain their turgor.                                        bodies, but at what stage of the land plant evolution were
   However, how plant cells sense the osmotic stress is a long-     OSCA genes likely to have evolved to sense osmotic stress?
standing question in biology. It is known that cytosolic free          To better understand the evolutionary scenarios and func-
Ca2+ elevation is one of the earliest responses of plant cells      tions of OSCA, in this study, we aimed to present the
to hyperosmolality and various other stimuli (Dodd et al.,          first comprehensive phylogenetic and molecular evolution-
2010; Knight et al., 1997). Stress-activated Ca2+ channels are      ary analyses of this family. First, a systematic homology
candidates that may link osmotic stress to Ca2+ –dependent          search on all bacterial and eukaryotic genomes that have been
downstream events (Hamilton, et al., 2015b). A novel                fully sequenced was applied. We did not find any clue of
osmotic stress-triggered Ca2+ channel, OSCA1 (REDUCED-              OSCA homologs in bacteria. Then, we constructed phyloge-
HYPEROSMOLALITY-INDUCED-[Ca2+ ]i -INCREASE 1),                      netic trees rooted on the anoctamin family—the closest rel-
was first reported in Arabidopsis thaliana (L.) Heynh., high-       ative of OSCA. The rooted trees displayed the presence of
lighting an advance in the understanding of sensory Ca2+            OSCA in all major eukaryotic branches, which falls into nine
channels in plants (Yuan et al., 2014). OSCA1 is a plasma           major clusters. The evolutionary relationships among the dif-
membrane protein and functions in the initial perception and        ferent clusters were then investigated. The gene expansions
short-term responses to hyperosmotic stress. Under hyper-           and phylogenetic divergence on major lineages of land plants
osmotic stress, root and leaf growth was stunted in mutant          were evaluated. Furthermore, we investigated the functional
OSCA1 plants. The determination of OSCA1 as osmotic                 divergence of OSCAs after gene duplications and tried to
stress-induced fast signalling is most likely of general impor-     understand how natural selection shapes functional diversi-
tance since OSCA1 represents a member of a large Ara-               fication of the OSCA family at the level of coding regions.
bidopsis gene family, OSCA. Phylogenetic inference of OSCA          Finally, variable selection pressures during the land plant evo-
have been carried out in three studies (Edel & Kudla, 2015;         lution were explored. Together, we speculate when OSCA
Hou et al., 2014; Yuan et al., 2014). By creating unrooted          genes could have evolved to sense water stress from dry envi-
trees of OSCA in selected eukaryotic genomes, these studies         ronment during land plant evolution. This study may provide
revealed that OSCA proteins are distributed throughout the          valuable insights into the further experimental research aimed
eukaryotic kingdom (Edel & Kudla, 2015; Hou et al., 2014;           at characterizing the molecular mechanisms and functions of
Yuan et al., 2014) and expanded to extensive gene families          the OSCA family and into crop improvement against water
during the evolution of plants (Edel & Kudla, 2015). Cryo-          stress.
genic electron microscopy structures of three OSCA fam-
ily members in Arabidopsis or rice (Oryza sativa L) have
been reported by a series of studies (Jojoa-Cruz et al., 2018;      2       MATERIALS AND METHODS
Liu et al., 2018; Maity et al., 2019; Zhang et al., 2018).
The overall structures for these members are quite simi-            2.1       Data sources
lar, containing 11 transmembrane (TM) helices as well as
a cytosolic soluble domain and forming a homodimer. The             A list of fully sequenced eukaryotic and prokaryotic organ-
TM domains have similar structure to the anoctamin (also            isms was derived from the database of KEGG Organisms
known as TMEM16) family, which are Ca2+ –activated ion              (https://www.genome.jp/kegg/catalog/org_list.html). Chro-
channels and lipid scramblases (Malvezzi et al., 2013; Yang         mosome, protein, and mRNA sequences of these eukaryotic
et al., 2012). Furthermore, electrophysiological studies of the     species were downloaded from National Center for Biotech-
OSCA members in Arabidopsis and animals revealed that               nology Information (https://ncbi.nih.gov/refseq/release/).
the OSCA family are bona-fide, pore-forming mechanosen-             Genome data of three fully sequenced gymnosperms,
sitive ion channels (Murthy et al., 2018). Thus, OSCA pro-          Norway spruce [Picea abies (L.) H. Karst.] (https:
teins potentially represent the largest family of mechanosen-       //plantgenie.org/Data/ConGenIE/), loblolly pine (Pinus
sitive ion channels that are conserved from plants to               taeda L.) (https://treegenesdb.org/Drupal/FTP), and clus-
humans.                                                             ter pine (Pinus pinaster Aiton) (https://www.scbi.uma.es/
   In spite of these studies, the origin of OSCA and its diversi-   sustainpinedb/assemblies/) (SustainPine version 3.0) were
fication history during the evolution of eukaryotes, especially     downloaded separately. Genome data of liverwort Marchantia
green plants, are elusive. For example, has this osmosens-          polymorpha was from MarpolBase (https://marchantia.info/).
ing OSCA family evolved in the plants transition from an            Charophyte algal data of Klebsormidium flaccidum was
aquatic environment to land? Has this family experienced phy-       from the Klebsormidium nitens NIES-2285 genome
logenetic and even functional diversification in land plants?       project        (https://www.plantmorphogenesis.bio.titech.ac.
The adaptation of plants on land requires the evolution of          jp/∼algae_genome_project/klebsormidium/index.html).
                                                                                                                                      19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
4 of 19    The Plant Genome                                                                                               WU ET AL.


Maize (Zea mays L.) data was from Phytozome v9.0. With             2.3       Phylogenetic analysis
the similar method as described in Chanderbali et al. (2015),
a large number of partial sequences in green algae (chloro-        Trees were constructed based on the full-length protein
phytes and charophytes) and nonseed plants (i.e., hornworts,       sequences and the RSN1_7TM domain regions. Sequences of
liverworts, mosses, lycophytes, and ferns) were derived from       the eukaryotic OSCA full dataset and subdataset were aligned
the 1KP transcriptomes (https://db.cngb.org/onekp/) (One           using MAFFT (v7.05) (Katoh & Standley, 2013) employing
Thousand Plant Transcriptomes Initiative, 2019) through            the speed-oriented FFT-NS-i (two cycles) method. For all
BLASTP (Altschul et al., 1997) searches at E value ≤ 1             the other protein sequences, multiple protein alignments were
using Arabidopsis OSCA proteins to query the 1KP protein           conducted using MAFFT employing the accuracy-oriented E-
database.                                                          INS-i method. Amino acid Bayesian and maximum likelihood
                                                                   (ML) trees were estimated using MrBayes (v3.2.3) (Ronquist
                                                                   et al., 2012) and PhyML (v3.1) (Guindon et al., 2010), respec-
2.2       Identification of orthologs                              tively. For each alignment, the appropriate model of evolu-
                                                                   tion was determined using the Akaike Information Criterion
Three steps were applied to detect putative OSCA homologs          implemented in ProtTest (v3.4) (Darriba et al., 2011). The
that harbor RSN1_7TM domain in fully sequenced eukaryotic          best-fit models are LG+I+G for the full-length alignment of
genomes as well as green algae and nonseed plants from the         OSCA Clades 1–3, LG+G for the RSN1_7TM domain align-
1KP transcriptomes.                                                ment of OSCA Clades 1–3, LG+I+G+F for the full-length
                                                                   and the RSN1_7TM domain alignments of the fungal group,
  (1) We ran the hmmsearch command of the HMMER                    and LG+G+F for the other alignments. The ML trees were
      package (v3.1b2) by querying the Pfam-A PF02714              estimated with 100 bootstrap replicates. Bayesian analyses
      (RSN1_7TM) hidden Markov model (HMM) against                 were performed on two parallel runs with distribution poste-
      the eukaryotic protein databases. An E value ≤ 1 × 10−2      rior probability of the generated trees estimated using Markov
      for sequences and a conditional E value ≤ 1×10−2 for         chain Monte Carlo with four chains (one cold, three heated)
      individual domains were adopted to identify significant      each. Convergence between the two parallel runs was ascer-
      protein matches containing the RSN1_7TM domain.              tained by examining the average standard deviation of their
  (2) To confirm the presence of RSN1_7TM domain in the            split frequencies as <0.01 in all analyses. Consensus topology
      obtained protein sequences, we further compared the          and posterior probability values were computed from saved
      results from hmmsearch against the library of Pfam-          trees after discarding 25% of generations as burn-in. Gen-
      A HMMs (v27.0) (https://ftp.ebi.ac.uk/pub/databases/         erations and subsampling frequencies were set for different
      Pfam/) using the Pfam_scan.pl script (parameters set as      trees, 3,000,000 generations and 500 subsampling frequencies
      -e_seq 1e-3 -e_dom 1e-3). Protein sequences that cov-        for the eukaryotic subdataset and the full-length sequences
      ered ≥50% of the RSN1_7TM domain were kept.                  of OSCA Clades 1–3, and 1,000,000 generations and 500
  (3) Since the eukaryotic protein database contains multiple      subsampling frequencies for the other datasets. Some trees
      splice isoforms of a gene, redundant protein sequences       were constructed using FastTree (v2.1.7) (Price et al., 2009)
      need to be discarded from the Pfam scan results for each     with default parameters. FastTree implements an ultrafast and
      species. CD-HIT (v4.6) (Fu et al., 2012) was used for        fairly accurate approximate ML method. The RSN1_7TM
      this purpose (parameters set as -c 0.95, -n 5, -g 1, -G 0,   domain-based Bayesian tree in the eukaryotic subdataset is
      -aS 0.6, -d 0, -p 1).                                        available in Supplemental Data S1.

   We also identified sequences that harbor RSN1_TM
domain using a similar method by querying Pfam-A PF13967           2.4       Molecular evolutionary analysis
HMM against the eukaryotic protein sequences. Interestingly,
all the sequences queried by RSN1_TM belong to the dataset         The MAFFT sequence alignment of the land plant OSCA pro-
by RSN1_7TM. Thus, the result queried by RSN1_7TM                  teins is available in Supplemental Data S2. Tail regions that
was finally adopted. The 1KP transcriptomes data were not          contained large gaps were trimmed. A phylogenetic tree was
included in the molecular evolutionary analysis. Detailed pro-     constructed using FastTree. The analysis of functional diver-
tein information and FASTA sequences of the full OSCA              gence of a gene family after gene duplication was estimated
dataset and the 1KP sequences are available in Supplemen-          by Type I and Type II analysis using DIVERGE (v3.0) (Gu
tal Table S1. We also searched OSCAs in fully sequenced            et al., 2013) with 500 bootstrap replications. Type I represents
prokaryotic genomes but did not find any bacterial sequence        heterogeneous evolutionary rates between duplicated genes
harboring RSN1_TM and RSN1_7TM.                                    (Gu, 1999), while Type II represents amino acid patterns that
                                                                                                                                        19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
WU ET AL.                                                                                         The Plant Genome            5 of 19


are highly conserved within both subfamilies but have radical          To detect whether positive selection had acted at some
shifts of physiochemical properties between duplicates (Gu,         amino acid sites within the foreground lineage, branch-site
2006). Coefficients of functional divergence and posterior          Test 1 (Zhang et al., 2005) was used. Branch-site Model A,
probabilities of amino acid sites to be responsible for func-       featuring an extra subset of sites under positive selection with
tional divergence were estimated. A P value was calculated          ω > 1 in the foreground lineages, was compared with site
by comparing the coefficient (theta value from likelihood ratio     model M1a (nearly neutral) as the null hypothesis. Signifi-
test [LRT]) of functional divergence with a chi-square distri-      cance of the test can be caused either by relaxed selective con-
bution (one degree of freedom). Amino acid residues likely          straint (e.g., presence of sites with ω2 = 1 in the foreground
to reflect functional divergence were identified with poste-        and ω2 < 1 in the background) or by positive selection along
rior probabilities ≥0.95. No significant functional divergence      the foreground. Relaxed purifying selection was concluded in
Type II was found in our dataset (P value > .05).                   all branch-site 1 tests in this study. We performed the clade-
   Estimation of the relative rate of nonsynonymous (dN) and        model and branch-site model analyses multiple times using
synonymous (dS) substitutions (ω = dN/dS) during the evo-           different initial values of ω to find the globally optimum log-
lution of OSCA Clades 1–3 was performed by means of the             likelihood value.
CODEML program in the PAML package (v4.7) (Z. Yang,                    To estimate variable selective pressures in the main species
1997), where dN means the number of nonsynonymous sub-              lineages during the evolution of land plants, two- and three-
stitutions per nonsynonymous site, and dS means the number          ratio models were adopted. The comparison between the two-
of synonymous substitutions per synonymous site. The ω ratio        ratio model and one-ratio model examines whether the ω ratio
is a measure of natural selection acting on a protein. Values of    for the branches of interest is different from the background
ω < 1, ω = 1, and ω > 1 indicate negative or purifying selection    ratio. The comparison of three-ratio model with two-ratio
(acting against change), neutral (i.e., no) selection, and posi-    model tests whether the significance of ω ratio in one lin-
tive Darwinian selection (driving change), respectively. If an      eage still holds while allowing the ω in the other lineage to
amino acid change is deleterious, purifying selection reduces       vary freely. Benjamini–Hochberg multiple correction (Ben-
its fixation rate so that ω < 1. When the substitution has no       jamini & Hochberg, 1995) was used to adjust the significance
effect on fitness, nonsynonymous substitutions occur at the         level.
same rate as synonymous ones and ω = 1, indicating neu-
tral evolution; ω > 1 indicates positive Darwinian selection
when amino acid changes offer a selective advantage and non-        2.5       Structural analysis
synonymous changes fixed at a higher rate than synonymous
changes. Codon multiple alignment of mRNA sequences was             Multiple sequence alignments of representative sequences of
created from the protein alignment using PAL2NAL (v14)              OSCA, anoctamin, and TMC were generated using MAFFT
(Suyama et al., 2006). Subsequently, the codon alignment            and MUSCLE (Edgar, 2004). Secondary structure elements
and tree topology were input to CODEML. Three different             of these protein sequences were predicted using Jpred 3
classes of codon substitution-based evolutionary models—            (Cole et al., 2008). The TM domains were predicted using
branch model (Yang, 1998), clade model, and branch-site             TMHMM server (v2.0) (Krogh et al., 2001) and Phobius (Kall
model (Yang & Nielsen, 2002)—were adopted. These mod-               et al., 2007). The computational results were then validated
els perform ML estimates of ω ratios and produce a log-             using the known three-dimentional structures of OSCA1.1
likelihood value to each examined alignment and phylogeny.          and OSCA3.1 in Arabidopsis (Zhang et al., 2018) and the
   To assess whether one clade (termed as ‘foreground’ lin-         anoctamin structure in fungus Nectria haematococca (Brun-
eage) evolved under a different selection relative to the rest of   ner et al., 2014).
the phylogeny (termed as ‘background’ lineage), branch mod-
els were used. A two-ratio branch model, which assumes one
ω ratio for the foreground lineage and another for the back-        3       RESULTS
ground lineage, was compared with a one-ratio null model,
which constrains all branches in the phylogeny to the same ω.       3.1     Phylogenetic classification of OSCA
An LRT was used to evaluate the better fitting model from the       family into different clades
comparison if the P value for fitting the examined dataset to
the alternative model was ≤.05.                                     The yeast RSN1 (Sce_OSCA1 in our data) was the funding
   To test for divergent selection pressures acting on a signifi-   member of OSCA, which harbors conserved RSN1 domains
cant number of sites in the three land-plant-specific clades,       (RSN1_TM and RSN1_7TM) (Wadskog et al., 2006; Yuan
clade Model C was used. The significance of clade Model             et al., 2014) as illustrated for Arabidopsis osmosensor OSCA1
C was tested using LRT against the site-specific null model         Ca2+ channel (Figure 1a; Supplemental Note S1). To iden-
M2a_ref (Weadick & Chang, 2012).                                    tify the OSCA family systematically, we searched all OSCA
                                                                                                                                                      19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
6 of 19         The Plant Genome                                                                                                         WU ET AL.



          (a)




          (b)




F I G U R E 1 Domain organization of the OSCA family. (a) A diagram of predicted topology of Arabidopsis thaliana OSCA1.1 (Yuan et al.,
2014). Topologies include 11 transmembrane (TM) helices and a cytosolic domain between TM2 and TM3. ‘Loop’ indicates a region between two
TM domains. Two regions highlighted in green represent RSN1_TM and RSN1_7TM domains. Intracellular (‘In’) and extracellular (‘Out’) regions
are labeled. (b) Secondary structural elements of the representative sequences of OSCA (also indicated with triangles in Figure 2), anoctamin (also
known as TMEM16), and TMC (Supplemental Note S1). The three gene families belong to the Pfam clan Anoctamin-like (CL0416). Anoctamin
contains an anoctamin domain that is structurally similar to RSN1_TM and RSN1_7TM domains but shows no sequence similarity to OSCA. A large
intracellular region (Yuan et al., 2014) with roughly 180 amino acids between TM2 and TM3 is present in all OSCA sequences but is absent from
TMEM16 and TMC. RSN1_TM and RSN1_7TM domains are labeled according to the A. thaliana OSCA1.1 sequence. Anoctamin domain is
labeled according to the fungus Nectria haematococca anoctamin sequence and TMC domain is labeled based on the Homo sapiens TMC1
sequence. The C-termini of these sequences were not displayed. The accession numbers of A. thaliana OSCA1.1 is NP_192343, A. thaliana
OSCA4.1 is NP_195312, human TMEM63A is NP_055513, S. cerevisiae OSCA1 (known as RSN1) is NP_013993, and Phytophthora infestans
OSCA6 is XP_002905819. The accession numbers of N. haematococca anoctamin (ANO) is XP_003046028, H. sapiens anoctamin1 (ANO1) is
NP_060513, H. sapiens TMC1 is NP_619636 and Selaginella moellendorffii (spikemoss) TMC is EFJ05970



homologs using RSN1_TM and RSN1_7TM Pfam profile in                         domain region using FastTree (Supplemental Figure S1).
available full-sequenced genomes. We did not identify any                   For a better phylogenetic and molecular evolutionary anal-
sequence containing RSN1_TM or RSN1_7TM in prokary-                         yses thereafter, we built a subdataset containing 314 OSCA
otic species. Thus, we focused on the evolution of OSCA in                  sequences by sampling 51 fully sequenced genomes to rep-
eukaryotic species.                                                         resent a wide variety of eukaryotic lineages. Based on the
   We generated a full OSCA dataset containing 983                          sub-OSCA dataset, Bayesian and ML trees of the RSN1_7TM
sequences from 220 fully sequenced eukaryotic genomes.                      domain region (Figure 2, the tree in newick format in Supple-
We obtained an additional dataset containing 1KP partial                    mental Data S1) and the full-length sequences (Supplemental
sequences from green algae (chlorophytes and charophytes)                   Figure S2) were generated. Different from the three previous
and nonseed land plants (i.e., bryophytes, lycophytes, and                  unrooted trees (Edel & Kudla, 2015; Hou et al., 2014; Yuan
ferns). Proteins and their sequences in the two datasets are                et al., 2014), our trees were rooted on the anoctamin family
available in Supplemental Table S1. A gene tree of the full                 (Figure 1b; Supplemental Figure S3, Supplemental Note S1),
OSCA dataset was constructed based on the RSN1_7TM                          which provided new insights.
                                                                                                                                                      19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
WU ET AL.                                                                                                   The Plant Genome                7 of 19




F I G U R E 2 Bayesian phylogeny of the RSN1_7TM domains in eukaryotic subdataset. Approximately 50 species representing a wide variety of
eukaryotic lineages were sampled. Anoctamin1 (ANO1) to anoctamin10 (ANO10) from human (hsa) were selected as the outgroup to root the gene
tree. Bayesian posterior probability and maximum likelihood (ML) bootstrap are shown beside selected major nodes. The symbol of ‘-‘ indicates no
support for a branching. Branch lengths are scaled with the number of amino acids substitution per site. Each protein is depicted as a three- or
four-letter abbreviation for species name (some plant species listed in Table 1) followed by gene ID. The full tree could be divided by nine major
clades: one chlorophyte algal group, OSCA Clades 1–3 that only harbor land plant homologs, OSCA Clade 4, one fungal group, and three protozoan
groups. Colored protein names and major clades indicate different species lineages. The nodes defining independent duplications leading to OSCA
Clades 1, 2, and 3 are marked with green asterisks, while the nodes indicating duplications producing three subfamilies of TMEM63 in vertebrates
are marked with red asterisks. The fungal sublineage containing an additional DUF3779 domain on the C-terminus is labeled. The five sequences
indicated with triangles were selected in Figure 1b. The tree in newick format is in Supplemental Data S1. The OSCA protein information and
sequences can be obtained from Supplemental Table S1. Accession numbers of the human anoctamin proteins ANO2 to ANO10 are NP_001265525,
NP_113606, NP_001273544, XP_005252877, NP_001191732, NP_001357623, NP_066010, NP_001012302, and NP_060545, respectively. Animal
and plant phylogenies are displayed in Supplemental Figure S5
                                                                                                                                        19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
8 of 19     The Plant Genome                                                                                                WU ET AL.


   Our trees showed that the OSCA family is present in all           to the gene duplications via the two rounds of whole-genome
major lineages of eukaryotes and can be clearly classified           duplication (WGD) occurred in early vertebrates followed by
into nine major groups (Figure 2; Supplemental Figures S1            an independent WGD that is shared by all teleosts (Supple-
and S2). Among these groups, a chlorophyte algal group and           mental Note S1; Supplemental Figures S5a, S6, and S7; Sup-
three protozoan groups 1–3 were newly classified as distinct         plemental Table S2).
clusters, while the remaining groups were consistent with pre-          Interestingly, the chlorophyte algal cluster is directly
vious studies including the OSCA Clades 1–3, the extended            basal to streptophyte-specific OSCA Clades 1–3 (Figure 2;
OSCA Clade 4, and the fungal group (Edel & Kudla, 2015;              Supplemental Figure S2) consistent with the evolution of
Hou et al., 2014; Yuan et al., 2014). Of which, OSCA Clades          green plants from chlorophytes, which mostly live in the
1–3 are specific for streptophytes (including charophyte algae       ocean (Kenrick & Crane, 1997). The phylogeny of OSCAs in
and land plants), whereas OSCA Clade 4 is a complex group,           plants from both fully sequenced genomes and 1KP transcrip-
comprising homologs from streptophytes, protists, and ani-           tomes also confirmed this transition (Supplemental Figure
mals (annotated as TMEM63 in National Center for Biotech-            S8). Furthermore, charophyte algal genes are placed basally
nology Information). Interestingly, OSCA Clade 4 is evolu-           with respect to land plants in OSCA Clades 1–4 (Figure 2;
tionarily distant from Clades 1–3. Clade 4 is the closest to         Supplemental Figures S2 and S8), indicating that Clades 1–
the basal group, that is, protozoa 3, but Clades 1–3 are the         3 and the plant subgroup in Clade 4 originated before the
farthest.                                                            diversification of the streptophytes. Accordingly, after diverg-
   Protists are a diverse group of the simplest eukaryotes, and      ing from marine green algae (chlorophytes), the plant OSCAs
some protists are closely related to fungi, animals, and plants      established three major Clades 1–3 prior to the transition of
(Adl et al., 2012). There are on average 3.1 homologs per            plants from freshwater (charophytes) to terrestrial habitats.
protozoan organism estimated from 99 sequences from 32
species (Supplemental Table S1). These protozoan homologs
are divided into three major groups and a sublineage in OSCA         3.2       Evolution of OSCA in land plants
Clade 4 (Figure 2). Protozoan Group 3, which is closest to the
outgroups, forms a sister group to the rest of OSCA homologs         Animals, fungi, chlorophytes, and streptophytes harbor on
with a strong support value of 100. Protozoan Group 2 is basal       average 2.4 (184 sequences in 76 fully sequenced species),
to the fungal group (Supplemental Figure S4, Supplemental            4.4 (306 sequences in 70 fully sequenced species), five
Note S1), while protozoan Group 1 is basal to plant-specific         (40 sequences in 8 fully sequenced species), and 10.5 (356
clusters including chlorophyte algae and streptophyte OSCA           sequences in 34 fully sequenced species) OSCA genes per
Clades 1-3. Within OSCA Clade 4, protozoan homologs are              genome, respectively. An approximately two- to 4.5-fold high
also in a basic position. Basic positions of these protozoan lin-    of the OSCA copies in streptophytes over marine green algae,
eages imply that the plant groups, OSCA Clade 4, and the fun-        fungi, protists, and animals suggest that the OSCA family in
gal group may have distinct protozoan origins. Furthermore,          streptophytes has expanded substantially after diverging from
the six protozoan genomes containing multiple OSCAs scat-            the marine green algae. To trace the evolutionary trajectory of
ter into more than one group. For example, OSCAs of Amoe-            the OSCA family after the colonization on land, we evaluated
bozoa Acanthamoeba castellanii or red algae Galdieria sul-           OSCA gene expansions on major land plant lineages and dated
phuraria belong to protozoa Group 2 and OSCA Clade 4,                the duplication events. We chose charophyte K. flaccidum and
while OSCAs of oomycete Phytophthora infestans belong to             13 representative land plant species (Table 1; Supplemen-
protozoa Groups 1 and 3 and OSCA Clade 4 (Supplemen-                 tal Figure S5b). Then, we built the Bayesian and ML phy-
tal Note S1). This scattering suggests that the OSCA family          logenetic trees specific for the OSCA Clades 1–3 (Figure 3;
have already evolutionarily diverged in protists, and this initial   Supplemental Figure S9) and the Clade 4 (Supplemental
diversification formed three main lineages of OSCAs, namely          Figure S10).
plants, fungi, and OSCA Clade 4.                                        Plant Clades 1–4 cover OSCA homologs from all strep-
   The OSCA family is present in nearly all animal genomes;          tophytes except that moss and hornworts are absent from
however, they have been lost from nematodes (Supplemen-              the Clade 4 (Figure 4; Supplemental Figure S8). Two inde-
tal Table S1). A comparison between the TMEM63 genes in              pendent duplication events occurred at the base of land
invertebrates and vertebrates shows the emergence of three           plant lineage (marked with green asterisks beside the nodes
paralogs, namely TMEM63A, TMEM63B, and TMEM63C,                      defining the duplications in Figure 2). OSCA Clade 3, split
in vertebrates. All fully sequenced teleost genomes [for exam-       from the first round of duplication, is basal to all others,
ple, zebrafish (Danio rerio) and medaka (Oryzias latipes)]           and OSCA Clade 2 and Clade 1 were then split after the
harbor four paralogs with an additional copy of TMEM63B.             second round of duplication. Furthermore, the seed plant
Syntenic cluster analysis showed that the most likely dynamic        lineage of OSCA Clade 1 is divided into three subclades
phases for the evolution of TMEM63 genes in animals traces           with strong statistical support—OSCA1.1-1.6, OSCA1.7, and
                                                                                                                                                        19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
WU ET AL.                                                                                                             The Plant Genome        9 of 19


TA B L E 1       Representative plant species used in phylogenetic analysis

                                                Representative species                                         Phylogenetic
  Plant lineagea                                (abbreviation)                                                 cladeb                    OSCAc
  Eudicots                                      Arabidopsis thaliana (L.) Heynh.                               Clades 1–4                15
                                                  (Ath)
  Monocots                                      Oryza sativa L. (Osa)                                          Clades 1–4                11
  Basal magnoliophyta                           Amborella trichopoda Baill. (Atr)                              Clades 1–4                9
  Gymnosperms                                   Picea abies (L.) H. Karst. (Pabi)                              Clades 1–4                10
  Spikemosses                                   Selaginella moellendorffii Hieron.                             Clades 1–4                6
                                                  (Smo)
  Mosses                                        Physcomitrella patens (Hedw.) Bruch                            Clades 1–3                14
                                                  & Schimp. (Ppp)
  Liverworts                                    Marchantia polymorpha L. (Mpo)                                 Clades 1–3                4
  Charophyte algae                              Klebsormidium flaccidum (Kfl)                                  Clades 1–3                6
  Chlorophyte algae                             Chlamydomonas reinhardtii                                      Green algae               8
                                                  P.A.Dang. (Cre)
a Phylogeniesof plants are displayed in Supplemental Figure S5b.
b Thephylogenetic OSCA clade to which each species belongs refers to Figures 2 and 3 and Supplemental Figure S10.
c
  Number of OSCA homologs in a species.



OSCA1.8—following the name classification of Arabidop-                              species only have single OSCA in Clades 3 and 4 compared
sis homologs (Figure 3a; Supplemental Figure S9a). The                              with 5.4 and 4.8 genes per species in Clades 1 and 2. However,
split into the three subclades probably resulted from two                           the gymnosperm OSCA genes expanded extensively in Clade
independent duplications (OSCA1.8 and then OSCA1.1-1.6                              3, with six homologs per species (Figure 4). The gymnosperm
and OSCA1.7, sequentially). Similarly, the seed plant lin-                          and angiosperm OSCA genes in different clades remain to
eage of OSCA Clade 2 is also split into three subclades:                            be functionally characterized. Therefore, it remains unclear
OSCA2.5 as a basal subclade and then OSCA2.1-2.2 and                                why angiosperm OSCA genes expanded in Clades 1 and 2
OSCA2.3-2.4 (Figure 3b, Supplemental Figure S9b). Gym-                              but only keep single gene in Clades 3 and 4, whereas there are
nosperms (branches in red) showed consistent branching                              more gymnosperm OSCA genes in Clade 3 compared with
of subclades (OSCA1.8, OSCA2.1-2.2, and OSCA2.3-2.4)                                those in the other clades. Taken together, the four major lin-
with angiosperm but are absent in the other three sub-                              eages of land plants, that is, nonvascular plants bryophytes
clades (OSCA1.1-1.6, OSCA1.7, and OSCA2.5). We further                              (liverworts, moss, and hornworts), the earliest vascular plants
aligned the Amborella trichopoda OSCA sequences against                             lycophytes, ferns, and seed plants, underwent lineage-specific
the whole-genome sequences of three gymnosperms using                               OSCA gene expansions (Supplemental Figure S8). Members
TBLASTN and confirmed that no other genome sequences                                in OSCA Clades 1 and 2 expanded most extensively in the
harbor the missed OSCAs (Supplemental Note S1). We could                            seed plants via splitting into three subclades followed by inde-
not exclude the possibility that incomplete genome assem-                           pendent gene expansions in the lineages of monocots and
bly of the gymnosperms might result in the missing of gym-                          eudicots during the evolution of individual subclades.
nosperm genes in several land plant subclades. Alternatively,
the OSCA gene loss events (nonfunctionalization) might have
happened during the evolution of gymnosperms after diverg-                          3.3     Phylogeny-based functional divergence
ing from the angiosperms via nonfunctionalization of dupli-                         analysis of OSCAs after gene duplication
cated gene copies (Lynch & Conery, 2000). Therefore, the
gene duplications could yield the subclades within OSCA                             Gene duplication has generally been viewed as a necessary
Clades 1 and 2 after the divergence of all living seed plants                       source of material for the origin of novel biological functions
(gymnosperms and angiosperms) from lycophytes (including                            (Ohno, 1970). Changes in protein function may then yield dif-
spikemoss) but before the split between gymnosperms and                             ferent evolutionary constraints on gene copies after duplica-
angiosperms.                                                                        tions (Taylor & Raes, 2004). To gain evolutionary statistics
   Interestingly, the similar division of seed plant lineage                        on diverged functions of the OSCA Clades 1–3, we performed
into multiple subclades is found in neither OSCA Clade 3                            pair-wise analysis between different clades using DIVERGE
(Figure 3c; Supplemental Figure S9c) nor the plant lineage                          (Gu et al., 2013). For the dataset of Clades 1–3, all com-
of OSCA Clade 4 (Supplemental Figure S10). Angiosperm                               parisons showed the coefficients (ThetaML, θ) of functional
                                                                                                                                                     19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
10 of 19     The Plant Genome                                                                                                           WU ET AL.




F I G U R E 3 Bayesian phylogeny of full-length sequences in OSCA Clades (a) 1, (b) 2, and (c) 3. Alignment was based on the full-length protein
sequences from one charophyte algae and 13 species representing distinct land plant lineages (phylogeny in Supplemental Figure S5b). Statistical
supports corresponding to Bayesian posterior probability and maximum likelihood (ML) bootstrap value, respectively, are shown beside selected
major nodes. Branch lengths are scaled with the number of amino acids substitution per site. Each protein is depicted as a three- or four-letter
abbreviation for species name followed by gene ID. Subclades in Clades 1 and 2 are enclosed with square brackets. The nodes defining gene
duplications producing subclades in Clades 1 and 2 are denoted with black circles. The branches in brown denote charophyte algae Klebsormidium
flaccidum (Kfl), cyan bryophytes (Ppp, Mpo), blue spikemoss (Smo), and red gymnosperms (Ppin, Ptae, and Pabi). Other branches in black denote
basal angiosperm (Atr), monocots (Osa and Sbi), and eudicots (Ath, Gmx, Vvi, and Sly). Ppin, Pinus pinaster; Ptae, P. taeda; Sbi, Sorghum bicolor;
Gmx, Glycine max (soybean); Vvi, Vitis vinifera (grapevine); Sly, Solanum lycopersicum (tomato). Full names of other species are listed in Table 1



divergence Type I >0.4 and a significant functional diver-                 divergent sites are within the RSN1_7TM domain region. At
gence between any two clades (P value ≤ 3.9 × 10−25 in                     these sites, amino acid residues are highly conserved within
Supplemental Table S3). It implies that the three OSCA clades              a clade but variable in the other one, likely representing a
underwent distinct functional constraints during their inde-               shift in their evolutionary constraints between the two clades,
pendent evolution after gene duplications. Furthermore, 10                 which might lead to a change of their functional roles. Two
(Clades 1 and 2), eight (Clades 1 and 3), and 17 (Clades 2                 sites, whose positions in the multiple sequence alignment are
and 3) amino acid residues reflecting functional divergence                533 and 674, were predicted to be functional divergent sites
Type I were identified with posterior probabilities ≥0.95                  between Clade 1 and Clade 2. The prior site is conserved
(Supplemental Table S4). Interestingly, all of the functional              with residue lysine in OSCA Clade 1, and the corresponding
                                                                                                                                                            19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
WU ET AL.                                                                                                       The Plant Genome                 11 of 19




F I G U R E 4 Prediction of the earliest time point at which OSCAs might have evolved to sense water stress. (a) Phylogeny showing divergence
of major plant lineages (Morris et al., 2018; Puttick et al., 2018). Approximate timings of divergence (million years ago) are displayed according to
the latest study (Morris et al., 2018). The red asterisk (*) marks the predicted time point at which land plant OSCAs have evovled to sense water
stress. Major body plan transitions including stomata, vascular tissue, true leaves, and true roots are labeled along the branches. Ancient deviation of
stomatal behavior types is labeled along the tree leaves. (b) Average number of OSCA homologs from individual species lineages falling in the plant
OSCA Clades. Gene numbers are indicated as bars. Species numbers are labeled on the right side. OSCAs in charophyte algae and land plants,
including the partial 1KP OSCA sequences and the complete OSCA sequences in eukaryotic subdataset, were used for the calculation of gene
numbers (Supplemental Table S1, Supplemental Figure S8). Classification of 1KP OSCA homologs into different plant clades was derived from the
phylogeny in Supplemental Figure S8. Angiosperms have, on average, 5.4, 4.8, one, and one gene in Clades 1–4, respectively; Gymnosperms 1.7,
1.3, six, and two genes; Ferns 1.3, 1.3, 1.4, and one gene; Lycophyte S. moellendorffii 1.6, 1.1, 1.4, and 1.1 genes; Liverworts 1.3, 1, 1.1, and four
genes; charophytes 1.8, 1, 2.8, and one genes. Hornworts have 3.5, one, and one gene in Clades 1–3, respectively, and mosses have two, 1.8, and 2.6
genes. Tree branches in (a) and bars in (b) are colored: euphyllophytes (angiosperms, gymnosperms, and ferns) in green, lycophyte in yellow,
bryophytes (hornworts, moss, and liverworts) in cyan, and charophyte algae in brown


residue in Clade 2 is lysine, asparagine, or glutamine, all of                 3.4    Selective pressure analysis of OSCA
which are hydrophilic amino acids. The latter site is with a                   Clades 1–3 at the coding region level
hydrophilic residue (asparagine or aspartic acid) or a special
residue proline in Clade 1, whereas the corresponding residue                  The significant functional divergence of OSCA between any
is histidine (hydrophilic) or tyrosine (hydrophobic) in Clade                  two clades in land plants implies different evolutionary rates
2. Consistent with previous structural studies of Arabidopsis                  at certain amino acid residues. To understand to what extent
OSCA1.2, the two sites are important residues within the con-                  the natural selection has exerted on the OSCA genes in land
duction pore of OSCA1.2 (Jojoa-Cruz et al., 2018; Liu et al.,                  plants and how the selective pressure is different in OSCA
2018). K435 (multiple sequence alignment position as 533)                      Clades 1–3, different codon substitution-based evolutionary
is on TM4 of OSCA1.2, which binds with TM6 to form a                           models were applied (Yang, 1998; Yang & Nielsen, 2002).
cytoplasmic cavity of the conduction pore. There are inter-                    First, the one-ratio model, which assumes all lineages to have
actions of three phospholipids in the cytoplasmic cavity with                  the same evolutionary rate, showed the most likely estimate
the sidechains of K435 and two other residues (K536 and                        of ω, a measure of the selection pressure (see Materials and
K544) (Jojoa-Cruz et al., 2018). As described in the other                     Methods), was 0.13, which indicated that OSCAs in the whole
study of OSCA1.2, the inner part of the conduction pore con-                   dataset of Clades 1–3 has spent a majority of time under neg-
tains several negatively charged or polar residues, like E461                  ative selection to act against mutations during land plant evo-
on TM5, N567 (multiple sequence alignment position as 674),                    lution. The two-ratio branch model assigned the ratio ω1 for
and T568 on TM7 (Liu et al., 2018). Whether the two sites in                   each individual clade and the ratio ω0 for the other clades.
OSCA Clade 2 are functionally divergent from those in the                      The LRTs for the comparisons of the two-ratio branch mod-
Clade 1 needs to be investigated in the future. This suggested                 els with the one-ratio models indicated that three individual
that our prediction result of the functional divergent analy-                  clades underwent asymmetrical evolution after gene dupli-
sis of OSCAs may assistant the functional verification of this                 cation (three P value ≤ 3.4 × 10−7 in Supplemental Table
family.                                                                        S5). Moreover, significant divergent selection pressures were
                                                                                                                                                                                  19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
12 of 19        The Plant Genome                                                                                                                                    WU ET AL.


TA B L E 2         Likelihood ratio tests for selective pressure divergence among OSCA Clades 1–3 by using clade Model C

  2×ΔLn L (M2a_rel
  vs. clade Model C)a                  P valuea                Site class              pb                       ωClade 1 c              ωClade 2 c              ωClade 3 c
  56.052                               6.7 ×   10−13           0                       0.38                     0.056                   0.056                   0.056
                                                               1                       0.05                     1                       1                       1
                                                               2                       0.57                     0.176                   0.25                    0.226
a ΔLn L = ln L1 – ln L0 while ln L1 (−102932.320) was the likelihood value of clade Model C and ln L0 (−102960.346) was the likelihood value of null model M2a_rel.
Degrees of freedom (df) = 1.
b
  Proportion of sites evolving under different site classes.
c
  Measure of natural selection acting on each of the Clades 1–3.



TA B L E 3         Likelihood ratio tests to estimate variable selective pressures among the main species lineages in land plants

                                                                                                                                               Estimates of
  Model                             Foreground lineage                          2×ΔLn La                       P valuea                        parametersb
  A. Two ratios                     Klebsormidium                               22.566c                        2.0 × 10−6                      ωB = 0.13; ωF = 0.22
  B. Two ratios                     Bryophytes                                  68.931  c
                                                                                                               –                               ωB = 0.14; ωF = 0.03
  C. Two ratios                     Spikemoss                                   36.221c                        –                               ωB = 0.14; ωF = 0.02
  D. Two ratios                     Seed plants                                 37.914c                        7.4 × 10−10                     ωB = 0.09; ωF = 0.14
  E. Two ratios                     Gymnosperms (Gym)                           385.485c                       8.0 × 10−86                     ωB = 0.11; ωF = 0.41
  F. Two ratios                     Angiosperms (Ang)                           81.672  c
                                                                                                               –                               ωB = 0.17; ωF = 0.12
  G.                                Gym,                                        314.414d                       2.4 × 10−70                     ωB = 0.09; ωGym = 0.42;
  Three                             Ang                                         10.601e                        1.1 ×   10−3                    ωAng = 0.11
  ratios
a ΔLn  L = ln L1 – ln L0 and df = 1. A likelihood ratio test was carried out to test whether the foreground ratio ω is significantly greater than the background ratio (P value
≤ .05 and 2×ΔLn L > 3.8).
b
  ωB means the ω ratio for the background and ωF is the ω ratio for the foreground.
c ln L1 was the likelihood value for two-ratio model (A–F) and ln L0 was the likelihood value for one-ratio model.
d
  Models G and F were compared to test whether the ω ratio for the gymnosperm lineage is different (that is, larger than) from the background ratio ωB when the angiosperm
lineage ratio is allowed to vary freely. ln L1 was the likelihood value for three-ratio model (G) and ln L0 for the two-ratio model in the foreground lineage of Ang (F).
e Models G and E were compared to test whether the ω ratio for the angiosperm lineage is greater than ω when the gymnosperm lineage ratio is allowed to vary freely. ln
                                                                                                           B
L1 was the likelihood value for three-ratio model (G) and ln L0 for the two-ratio model in the foreground lineage of Gym (E).


indicated at the sequence level in each paralogous clade (P                                 OSCA Clade 1 (Model A in Supplemental Table S6) and
value = 6.7 × 10−13 in Table 2). Fifty-seven percent of the                                 in the whole dataset of Clades 1–3 (Model A in Table 3).
sequence sites evolved under divergent selective pressures.                                 The ω ratios in bryophytes (0.03) and spikemoss (0.02) are
The ω values in Clade 2 (ωClade 2 = 0.25) and Clade 3 (ωClade 3                             significantly lower than the background ωB (0.14) (2×ΔLn
= 0.226) are larger than the ω value in Clade 1 (ωClade 1                                   L > 3.8 in Models B and C in Table 3), whereas the ω ratio
= 0.176), indicating weaker (or relaxed) purifying selective                                in seed plants (0.14) is significantly greater than ωB (0.09)
pressure on OSCA genes in Clades 2 and 3. Genes that are                                    (P value = 7.4 × 10−10 in Model D). To find out which of
under relaxed selective pressure will accumulate substitutions                              the branches in gymnosperms and angiosperms may have
at a higher rate than the genes under strong purifying selection                            caused the significant higher ω ratio in seed plants, ω ratios
(Liman & Innan, 2003). Thus, OSCA genes in Clades 2 and                                     in gymnosperms and angiosperms are allowed to differ. Only
3 might accumulate more substitutions somewhere along the                                   one of the two lineages was compared with the background
sequences.                                                                                  ratio ωB , while the other was either allowed to vary freely
   Were there variable selection pressures on OSCA                                          (three-ratio Model G compared with two-ratio Models F
sequences along the main lineages during land plant evolu-                                  and E) or constrained to be equal to ωB (two-ratio Models E
tion? The charophyte algae K. flaccidum, the earliest land                                  and F, compared with the one-ratio model) (Table 3). These
plant bryophytes, the earliest vascular plant spikemoss,                                    tests showed that the ω ratio in gymnosperms is significantly
gymnosperms, angiosperms, and seed plants were indi-                                        greater than the background ωB whether (P value = 8.0 ×
vidually assigned as foreground branches in the two-ratio                                   10−86 ) or not (P value = 2.4 × 10−70 ) angiosperms ω ratio is
model. We found that the ω ratio in charophyte K. flaccidum                                 constrained to be equal to ωB . Angiosperms ω ratio is signifi-
is only greater than the background ωB in the dataset of                                    cantly greater than ωB when gymnosperms ω ratio is allowed
                                                                                                                                                         19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
WU ET AL.                                                                                                     The Plant Genome                13 of 19




F I G U R E 5 Numbers of four mechanosensitive ion channels and two ion channels related to OSCA in representative species. Four
mechanosensitive ion channels are MscS-like (MSL), degenerin/epithelial sodium channel (DEG/ENaC), transient receptor potential (TRP), and
Piezo. Anoctamin, TMC, and OSCA are in the same Pfam clan. MSL, DEG/ENaC, anoctamin, and TMC were respectively identified using a hidden
Markov model (HMM)-based search for the MS (PF00924), ASC (PF00858), Anoctamin (PF04547), and TMC (PF07810) domains, respectively.
Both TRP and Piezo were identified using a modified bidirectional BLASTP method and the putative candidates were verified with Pfam
(Supplemental Note S1). The presence of a homolog of a gene family in a particular species is filled with different colors according to the numbers.
The lack of an apparent homolog is in white. A consensus cladogram showing the topology (branch lengths are not intended to be to scale) of the
phylogenetic relationships between the species is on the left. Colored branches and nodes indicate membership in different major lineages of the tree


to vary freely (P value = 1.1 × 10−3 ). Therefore, OSCAs in                  first reported the novel hyperosmolality-induced Ca2+ chan-
the foreground lineages of bryophytes and spikemoss were                     nel OSCA1 (Yuan et al., 2014). Then, one MSL channel in
under significantly decelerated evolution, whereas OSCAs in                  plants, MSL8, was characterized to be required for pollen to
seed plants showed significantly accelerated evolution. The                  survive the hypoosmotic shock of rehydration and full male
higher estimate of ω ratio in seed plants could be explained                 fertility. MSL8 forms a membrane tension-gated ion channel
by relaxed selective pressure along the OSCA sequences in                    but with a preference for anions (Hamilton, et al., 2015a).
seed plants. The same conclusion could be obtained from                         The OSCA, anotamin, and TMC families belong to the
the LRTs based on the three individual trees of Clades 1–3                   Pfam clan anoctamin-like (CL0416) (Medrano-Soto et al.,
(Supplemental Table S6).                                                     2018). Although anoctamin and TMC are the closest known
                                                                             relatives of OSCA (Figure 1b; Supplemental Figure S3), their
                                                                             evolutionary profile across eukaryotic genomes is different
4       DISCUSSION                                                           from that of OSCA (Figure 5). The anoctamin family is
                                                                             present in nearly all eukaryotes but not found in most green
4.1    Evolution of mechanosensitive ion                                     algae and several protist lineages (Acanthamoeba and apicom-
channels and two closest relatives of OSCA                                   plexans). The TMC family is present in all animals and a few
                                                                             lower plants [Spikemoss (Selaginella moellendorffii Hieron.)
The MscS-like (MSL) family is widely distributed in all                      and green algae (Coccomyxa subellipsoidea)] and one proto-
three kingdoms of life but is absent from animals (Figure 5).                zoan species (Naegleria gruberi). Both anoctamin and TMC
Both DEG/EnaC and TRP channels have extensive members                        families have more members in animals than plants. In con-
in animals, but no DEG/EnaC or TRP exist in land plants                      trast, the size of the OSCA family in green plants (average
(Hedrich, 2012; Mano & Driscoll, 1999). The Piezo chan-                      size as 9.6) increases fourfold over animals. Living verte-
nel can be found in animals, plants, and some protists and is                brates keep most of the TMEM63 genes gained through the
made up of one or two members in most organisms. However,                    WGDs. It has been reported that gene duplicates from the two
evidence that Piezo proteins are mechanosensitive in plants                  rounds of vertebrate WGDs that have been retained in mod-
is still lacking (Hedrich, 2012; Murthy et al., 2018). How                   ern vertebrate genomes are enriched for diversified develop-
plant cells sense the osmotic stress was unknown until we                    mental regulation, which are correlated with the evolution of
                                                                                                                                       19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
14 of 19    The Plant Genome                                                                                               WU ET AL.


vertebrate novelties (Putnam et al., 2008). Expression profiles    by BIK1 are critical for stomatal closure during immune sig-
of TMEM63A and TMEM63B in human and mouse (Mus                     nalling and suggested specificity in Ca2+ influx mechanisms
musculus) indeed show that they are ubiquitously expressed         in response to different stresses (Thor et al., 2020). In sum-
(https://BioGPS.org). Furthermore, in humans, mutations in         mary, mechanical stresses in plants result from the pressure
TMEM63A result in a myelination defect in infants, suggest-        exerted by wind, drought, flood, frost, cold, and hot. OSCA
ing a previously unappreciated role for mechanosensitive ion       members may respond to different mechanical stresses, and
channels in myelin development (Yan et al., 2019). Thus,           alternatively, different OSCA members may perform redun-
TMEM63 in extant vertebrate genomes could be recruited for         dant functions in hyperosmotic sensing but with specificity
roles in some fundamental functions.                               in permeation and gating properties, reminiscent of the broad
                                                                   functions of TRP ion channels.
                                                                      Transient receptor potential ion channels all share a canoni-
4.2     Enormous expansion and appreciable                         cal tetrameric architecture, with cytosolic asparagine and cys-
diversification of OSCA genes in land plants                       teine termini and six TM domains (Startek et al., 2019) and
                                                                   the 27 members in human are grouped into six subfamilies
Enormous expansion and appreciable diversification of              based on sequence homology. They are involved in a variety
OSCA genes in land plants were discovered in this study.           of sensory processes including chemosensation, thermosensa-
Lineage-specific OSCA gene expansions can be found in              tion, mechanosensation, and osmosensation (Kefauver et al.,
bryophytes, lycophytes, ferns, and seed plants, but the            2020). Several TRP channels from different subfamilies show
OSCA family has expanded most appreciably in seed plants           temperature-dependent activation but with different thermal
accompanied by the origin of new subfamilies (Figure 3;            sensitivity. TRPV1 (VR-1) was originally cloned as the ‘cap-
Supplemental Figures S8 and S9). Besides, the OSCA family          saicin receptor’ (Caterina et al., 1997) and has been discov-
in streptophyte Clades 1–3 underwent appreciable functional        ered to be activated by other stimuli such as toxins, pro-
diversification during their independent evolution after gene      tons, and temperature in the noxious range (>42 ˚C). TRPV2
duplications (Supplemental Table S3). Furthermore, Clades          (VRL-1) is also activated by heat but with a higher thresh-
2 and 3 have experienced relaxed selective pressure, which         old (>50 ˚C). TRPV3 and TRPV4 are activated by innocu-
represents the accumulation of more substitutions relative to      ous heat with temperature threshold ranges of 30–40 ˚C (Peier
Clade 1 (Table 2). Although eukaryotic OSCA proteins share         et al., 2002; Xu et al., 2002) and 25–34 ˚C (Guler et al., 2002),
quite similar overall structures (Figure 1b) (Jojoa-Cruz et al.,   respectively. TRPM8 (CMR1) is best known for its cold sens-
2018; Liu et al., 2018; Maity et al., 2019; Zhang et al., 2018),   ing ability (<25 ˚C). In addition to thermosensation, TRPM8
previous experimental studies have provided clues that the         is also involved in pain sensation, thermoregulation, bladder
OSCA family probably has diverse functional properties, in         function, and cancer (Samanta et al., 2018).
agreement with our phylogenetic and molecular evolutionary            In summary, our results, together with the previous exper-
analysis.                                                          imental evidence, reveal that the OSCA family probably
   Electrophysiological experiments revealed that stretch-         have evolved diverse functions and specified mechanisms in
activated single-channel currents of multiple OSCA channels        respond to different mechanical stresses during the indepen-
(OSCA1.1, OSCA1.2, OSCA1.8, OSCA2.3, and OSCA3.1)                  dent evolution of land plant clades after gene duplication and
and TMEM63 channels recorded quite distinct single-channel         phylogenetic diversification events. In a similar manner, the
conductance, providing evidence that OSCAs are a fam-              TRP family shows diverse functions and the anoctamin family
ily of mechanosensitive ion channels with unique biophys-          members act as ion channels and phospholipid scramblers in
ical properties (Murthy et al., 2018). The cytosolic domain        animals (Malvezzi et al., 2013; Yang et al., 2012). The absence
(depicted in Figure 1a) may partly contribute to the dif-          of the TRP family from land plants and only single anoctamin
ferent channel properties (Liu et al., 2018). Zhai et al.          member in plants (Figure 5) indicates that the two families
(2020, 2021) found that multiple members (OsOSCA1.1,               cannot fulfill their diverse functions in plants.
OsOSCA1.2, OsOSCA1.3, OsOSCA2.1, and OsOSCA2.2)
of the rice OsOSCA family complement hyperosmolality-
induced cytosolic Ca2+ increases, salt stress-induced cytoso-      4.3    How are OSCAs able to sense
lic Ca2+ increases, and the associated growth phenotype in         hyperosmotic stress?
Arabidopsis mutant osca1. Moreover, osca1 overexpressing
these OsOSCAs exhibited various abiotic stress-associated          In plants, the intrinsic cause of mechanical stress comes
growth phenotypes, indicating redundant functions in osmotic       down to the membrane tension within the cell wall aris-
sensing and diverse roles in stress adaptation (Zhai et al.,       ing from turgor pressure acting on it (Codjoe et al., 2021;
2021; Zhai et al., 2020). A recent study demonstrated that         Hamant & Haswell, 2017). As a subtype of mechanical
Ca2+ –permeable channel OSCA1.3 and its phosphorylation            forces, osmotic stress generates membrane tension, which
                                                                                                                                          19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
WU ET AL.                                                                                          The Plant Genome            15 of 19


applies forces to the embedded channels. Electrophysiological          accelerated evolution, bryophytes and lycophytes were under
experiments revealed that multiple OSCA and TMEM63                     significantly decelerated evolution (Table 3; Supplemental
channels are activated by negative pressure in inside-out              Table S6). These findings, based on phylogenetic and molec-
patches (Jojoa-Cruz et al., 2018; Murthy et al., 2018; Zhang           ular evolutionary analyses, relate nicely to the development
et al., 2018) and by positive pressure in outside-out patches          of major morphological characters that are crucial for plant
(Murthy et al., 2018; Yuan et al., 2014). These studies showed         colonization and subsequent radiation on land.
that OSCAs are directly sensitive to and intrinsically gated              To thrive in a terrestrial habitat, plants must coordinate
by membrane tension. However, the molecular mechanism                  the uptake of water and minerals by roots with the tran-
of OSCA channel gating remains unclear. To address the                 spiration and photosynthesis in leaves through the osmo-
structural aspects of the gating mechanism, four groups have           sis process. The ancestor of euphyllophytes occupies typi-
published the high-resolution crystal structures of Arabidop-          cal leaves, typical roots, and phloem tissues, all of which
sis OSCA1.1, OSCA1.2, and OSCA3.1 and rice OSCA1.2                     require osmosensors to maintain water balance and food con-
(Jojoa-Cruz et al., 2018; Liu et al., 2018; Murthy et al., 2018;       duction through plant bodies (Figure 4a). The nonvascular
Zhang et al., 2018). The OSCA structures proposed that an              land plants, bryophytes, lack the morphological adaptations
extended helical arm in the cytosolic soluble domain (Jojoa-           that commonly exist in the dominant land plants. It means
Cruz et al., 2018; Maity et al., 2019) makes hydrophobic con-          that their primary response to water stress is at the cellu-
tacts with the loop connecting the gating helix TM6 (Jojoa-            lar level (Wang et al., 2012). Bryophytes might rely on dif-
Cruz et al., 2018; Maity et al., 2019; Zhang et al., 2018). It sug-    ferent mechanisms to perceive and respond to water stress
gests a possible role for the helical arm in sensing the lateral       and to facilitate lineage-specific adaptation to environmental
tension on the inner leaflet side of the lipid bilayer and, in turn,   changes. Water stress has been examined in the model moss
transmitting these conformational and mechanical changes to            species Physcomitrella patens (Hedw.) Bruch & Schimp.
the gating helix TM6 opening of the transport pathway. This            (Wang et al., 2012). It can adjust the cellular structure to
feature is missing in TMEM16 chloride channels possibly as             avoid the severe damage from the dehydration. Transcriptome
Ca2+ ions control gating (Maity et al., 2019).                         and proteomic analyses also found actinoporin-like proteins
   Thus, we speculate that OSCA channels might directly                and late-embryogenesis-abundant proteins were induced upon
sense mechanical force from lipid, analogous to proposed               the dehydration stress. The early vascular plants, lycophytes,
mechanistic models for the bacterial MscL and MscS chan-               developed both roots and leaves, but they are not homologous
nels and the metazoan K2P channel TRAAK (Ranade et al.,                with their counterparts in euphyllophytes. In spite of these
2015). TRAAK is also activated by either negative or positive          studies, how the earliest land plants sense water stress needs
pressure using electrophysiological studies. High-resolution           to be discovered. The lack of major morphological charac-
crystal structures of TRAAK revealed that activating mutants           ters in the earliest land plants may support our evolutionary
induce conformational changes within the TM domains,                   result that bryophytes and lycophytes were under significantly
which opens up a wide-pathway toward the inner leaflet of the          decelerated evolution, whereas seed plants were under accel-
bilayer and allows channel gating upon changes to membrane             erated evolution. Therefore, we initially proposed that OSCA
tension (Ranade et al., 2015).                                         genes have evolved to sense water stress in the ancestor of
                                                                       euphyllophytes at the earliest.
                                                                          Stomata were the solution for early land plants to main-
4.4     When were OSCAs likely to have                                 tain water and carbon dioxide balance between leaves and the
evolved to sense osmotic stress?                                       dry atmosphere. Osmosis process is required for the control
                                                                       of stomatal open and closure in leaves. Although extant land
Water plays a crucial role in the life of land plant. OSCA1 in         plants possess key genetic components that are known to con-
Arabidopsis is involved in the initial perception and response         trol stomatal movement actively in angiosperms (Sussmilch
of cells to water stress (Yuan et al., 2014). The streptophyte-        et al., 2019a,2019b), the mechanisms required for osmotically
specific OSCA clades emerged from a group of OSCA                      driven stomatal movement have been gradually acquired dur-
homologs in marine green algae. One question arose natu-               ing land plant evolution (Figure 4a). The genetic components
rally: At what stage of the land plant evolution did OSCA              are specifically expressed in angiosperm guard cells, but none
genes acquire the ability to perceive and respond to envi-             appear specifically expressed in stomata-bearing moss tis-
ronmental water stress? Besides the expansion patterns of              sues (Sussmilch, Roelfsema, 2019a). The early diverging vas-
the OSCA family based on the phylogenetic trees, the ear-              cular plant lineages (lycophytes and ferns) have constrained
lier land plants (bryophytes and lycophytes) are differenti-           stomatal responses to soil and atmospheric water deficit as a
ated from the higher land plants (i.e., seed plants here) in           consequence of a predominantly passive hydraulic regulation
the aspect of variable selection pressures that were exerted           (Brodribb & McAdam, 2011; McAdam & Brodribb, 2013).
on the OSCA sequences. Whereas higher land plants showed               A gymnosperm species (Metasequoia glyptostroboides) also
                                                                                                                                                         19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
16 of 19      The Plant Genome                                                                                                              WU ET AL.


behaves as passive hydraulic valves in response to changes                  Arnadottir, J., & Chalfie, M. (2010). Eukaryotic mechanosensitive chan-
in humidity and soil water content unless exposed to severe                   nels. Annual Review of Biophysics, 39, 111–137. https://doi.org/10.
water stress. Thus, M. glyptostroboides, and perhaps other                    1146/annurev.biophys.37.032807.125836
                                                                            Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery
gymnosperm lineages, occupy a stomatal behavior type inter-
                                                                              rate: A practical and powerful approach to multiple testing. Journal
mediate between the passive and active stomatal control
                                                                              of the Royal Statistical Society: Series B (Statistical Methodology),
(McAdam & Brodribb, 2014). Since the active stomatal con-                     57, 289–300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x
trol is found in seed plants (Sussmilch et al., 2017), we can               Booth, I. R., & Blount, P. (2012). The MscS and MscL families of
make the hypothesis of sensing water stress in seed plants with               mechanosensitive channels act as microbial emergency release valves.
more certainty.                                                               Journal of Bacteriology, 194, 4802–4809. https://doi.org/10.1128/JB.
                                                                              00576-12
AC K N OW L E D G M E N T S                                                 Brodribb, T. J., & McAdam, S. A. (2011). Passive origins of stomatal
We thank the two anonymous reviewers and the editor for                       control in vascular plants. Science, 331, 582–585. https://doi.org/10.
                                                                              1126/science.1197985
their valuable comments as well as Guoning Qi, Yuantao
                                                                            Brunner, J. D., Lim, N. K., Schenck, S., Duerst, A., & Dutzler, R. (2014).
Liu, Lulu Liu, Fei-Hua Wu, and Yibo Teng for illuminat-
                                                                              X-ray structure of a calcium-activated TMEM16 lipid scramblase.
ing discussions. This work was supported by Natural Sci-                      Nature, 516, 207–212. https://doi.org/10.1038/nature13984
ence Foundation of Zhejiang Province [LY18C050005 to                        Catarino, B., Hetherington, A. J., Emms, D. M., Kelly, S., & Dolan, L.
XiaomeiW, LY19C020004 to Shan Zhu, and LZ16C020001                            (2016). The stepwise increase in the number of transcription factor
to Zhen-Ming Pei], Zhejiang Major Scientific and Tech-                        families in the precambrian predated the diversification of plants on
nological Project of Agricultural (Upland crop) Breeding                      land. Molecular Biology and Evolution, 33, 2815–2819. https://doi.
(2021C02064-6), US National Science Foundation [IOS-                          org/10.1093/molbev/msw155
                                                                            Caterina, M. J., Schumacher, M. A., Tominaga, M., Rosen, T. A., Levine,
1457257 to Zhen-Ming Pei], National Natural Science Foun-
                                                                              J. D., & Julius, D. (1997). The capsaicin receptor: A heat-activated ion
dation of China [31571461 to Fang Yuan].                                      channel in the pain pathway. Nature, 389, 816–824. https://doi.org/10.
                                                                              1038/39807
AU T H O R C O N T R I B U T I O N S                                        Chanderbali, A. S., He, F., Soltis, P. S., & Soltis, D. E. (2015). Out of
Xiaomei Wu: Data curation; Formal analysis; Funding acqui-                    the water: Origin and diversification of the LBD gene family. Molec-
sition; Methodology; Project administration; Writing – orig-                  ular Biology and Evolution, 32, 1996–2000. https://doi.org/10.1093/
inal draft; Writing – review & editing. Fang Yuan: Data                       molbev/msv080
curation; Formal analysis; Funding acquisition; Methodol-                   Codjoe, J. M., Miller, K., & Haswell, E. S. (2021). Plant cell mechanobi-
ogy; Validation; Writing – original draft; Writing – review                   ology: Greater than the sum of its parts. Plant Cell, 34, 129–145.
                                                                              https://doi.org/10.1093/plcell/koab230
& editing. Xuewen Wang: Validation; Visualization; Writ-
                                                                            Cole, C., Barber, J. D., & Barton, G. J. (2008). The Jpred 3 secondary
ing – review & editing. Shan Zhu: Funding acquisition;                        structure prediction server. Nucleic Acids Research, 36, W197–W201.
Investigation; Writing – review & editing. Zhen-Ming Pei:                     https://doi.org/10.1093/nar/gkn238
Conceptualization; Funding acquisition; Project administra-                 Darriba, D., Taboada, G. L., Doallo, R., & Posada, D. (2011). ProtTest 3:
tion; Supervision; Validation; Writing – review & editing.                    Fast selection of best-fit models of protein evolution. Bioinformatics,
                                                                              27, 1164–1165. https://doi.org/10.1093/bioinformatics/btr088
CONFLICT OF INTEREST                                                        Delmas, P., & Coste, B. (2013). Mechano-gated ion channels in sensory
The authors declare no conflict of interest.                                  systems. Cell, 155, 278–284. https://doi.org/10.1016/j.cell.2013.09.
                                                                              026
ORCID                                                                       Dodd, A. N., Kudla, J., & Sanders, D. (2010). The language of calcium
                                                                              signaling. Annual Review of Plant Biology, 61, 593–620. https://doi.
Xuewen Wang         https://orcid.org/0000-0003-2820-9255
                                                                              org/10.1146/annurev-arplant-070109-104628
                                                                            Doyle, J. A. (2013). Phylogenetic analyses and morphological innova-
REFERENCES                                                                    tions in land plants. In B. A. Ambrose & M. Purugganan (Eds.),
Adl, S. M., Simpson, A. G., Lane, C. E., Lukes, J., Bass, D., Bowser,         Annual plant reviews volume 45: The evolution of plant form (pp. 1–
   S. S., Brown, M. W., Burki, F., Dunthorn, M., Hample, V., Heiss,           50). John Wiley & Sons, Ltd.
   A., Hoppenrath, M., Lara, E., le Gall, L., Lynn, D. H., McManus,         Edel, K. H., & Kudla, J. (2015). Increasing complexity and versatility:
   H., Mitchell, E. A. D., Mozley-Stanridge, S. E., Parfrey, L. W.,           How the calcium signaling toolkit was shaped during plant land col-
   . . . Spiegel, F. W. (2012). The revised classification of eukaryotes.     onization. Cell Calcium, 57, 231–246. https://doi.org/10.1016/j.ceca.
   Journal of Eukaryotic Microbiology, 59, 429–493. https://doi.org/10.       2014.10.013
   1111/j.1550-7408.2012.00644.x                                            Edgar, R. C. (2004). MUSCLE: Multiple sequence alignment with high
Altschul, S. F., Madden, T. L., Schaffer, A. A., Zhang, J., Zhang, Z.,        accuracy and high throughput. Nucleic Acids Research, 32, 1792–
   Miller, W., & Lipman, D. J. (1997). Gapped BLAST and PSI-BLAST:            1797. https://doi.org/10.1093/nar/gkh340
   A new generation of protein database search programs. Nucleic Acids      Edwards, D., Kerp, H., & Hass, H. (1998). Stomata in early land
   Research, 25, 3389–3402. https://doi.org/10.1093/nar/25.17.3389            plants: An anatomical and ecophysiological approach. Journal of
                                                                                                                                                           19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
WU ET AL.                                                                                                      The Plant Genome                 17 of 19


   Experimental Botany, 49, 255–278. https://doi.org/10.1093/jxb/49.          Kefauver, J. M., Ward, A. B., & Patapoutian, A. (2020). Discoveries
   Special_Issue.255                                                             in structure and physiology of mechanically activated ion channels.
Fu, L., Niu, B., Zhu, Z., Wu, S., & Li, W. (2012). CD-HIT: Acceler-              Nature, 587, 567–576. https://doi.org/10.1038/s41586-020-2933-1
   ated for clustering the next-generation sequencing data. Bioinformat-      Kenrick, P., & Crane, P. R. (1997). The origin and early evolution of
   ics, 28, 3150–3152. https://doi.org/10.1093/bioinformatics/bts565             plants on land. Nature, 389, 33–39. https://doi.org/10.1038/37918
Gu, X. (1999). Statistical methods for testing functional divergence after    Knight, H., Trewavas, A. J., & Knight, M. R. (1997). Calcium signalling
   gene duplication. Molecular Biology and Evolution, 16, 1664–1674.             in Arabidopsis thaliana responding to drought and salinity. The Plant
   https://doi.org/10.1002/9780470619902.ch8                                     Journal, 12, 1067–1078. https://doi.org/10.1046/j.1365-313X.1997.
Gu, X. (2006). A simple statistical method for estimating type-II (cluster-      12051067.x
   specific) functional divergence of protein sequences. Molecular Biol-      Krogh, A., Larsson, B., von Heijne, G., & Sonnhammer, E. L. (2001).
   ogy and Evolution, 23, 1937–1945. https://doi.org/10.1093/molbev/             Predicting transmembrane protein topology with a hidden Markov
   msl056                                                                        model: Application to complete genomes. Journal of Molecular Biol-
Gu, X., Zou, Y., Su, Z., Huang, W., Zhou, Z., Arendsee, Z., & Zeng,              ogy, 305, 567–580. https://doi.org/10.1006/jmbi.2000.4315
   Y. (2013). An update of DIVERGE software for functional diver-             Kung, C. (2005). A possible unifying principle for mechanosensation.
   gence analysis of protein family. Molecular Biology and Evolution,            Nature, 436, 647–654. https://doi.org/10.1038/nature03896
   30, 1713–1719. https://doi.org/10.1093/molbev/mst069                       Levina, N., Totemeyer, S., Stokes, N. R., Louis, P., Jones, M. A.,
Guindon, S., Dufayard, J. F., Lefort, V., Anisimova, M., Hordijk,                & Booth, I. R. (1999). Protection of Escherichia coli cells against
   W., & Gascuel, O. (2010). New algorithms and methods to esti-                 extreme turgor by activation of MscS and MscL mechanosensitive
   mate maximum-likelihood phylogenies: Assessing the performance                channels: Identification of genes required for MscS activity. The
   of PhyML 3.0. Systematic Biology, 59, 307–321. https://doi.org/10.            EMBO Journal, 18, 1730–1737. https://doi.org/10.1093/emboj/18.7.
   1093/sysbio/syq010                                                            1730
Guler, A. D., Lee, H., Iida, T., Shimizu, I., Tominaga, M., & Caterina, M.    Liman, E. R., & Innan, H. (2003). Relaxed selective pressure on an
   (2002). Heat-evoked activation of the ion channel, TRPV4. Journal of          essential component of pheromone transduction in primate evolution.
   Neuroscience, 22, 6408–6414. https://doi.org/10.1523/JNEUROSCI.               Proceedings of the National Academy of Sciences, 100, 3328–3332.
   22-15-06408.2002                                                              https://doi.org/10.1073/pnas.0636123100
Hamant, O., & Haswell, E. S. (2017). Life behind the wall: Sensing            Little, C. (Ed.) (1990). The terrestrial invasion: An ecophysiological
   mechanical cues in plants. BMC Biology, 15, 59. https://doi.org/10.           approach to the origins of land animals. Cambridge University Press.
   1186/s12915-017-0403-5                                                     Liu, X., Wang, J., & Sun, L. (2018). Structure of the hyperosmolality-
Hamilton, E. S., Jensen, G. S., Maksaev, G., Katims, A., Sherp, A. M.,           gated calcium-permeable channel OSCA1.2. Nature Communica-
   & Haswell, E. S. (2015a). Mechanosensitive channel MSL8 regulates             tions, 9, 5060. https://doi.org/10.1038/s41467-018-07564-5
   osmotic forces during pollen hydration and germination. Science, 350,      Lynch, M., & Conery, J. S. (2000). The evolutionary fate and conse-
   438–441. https://doi.org/10.1126/science.aac6014                              quences of duplicate genes. Science, 290, 1151–1155. https://doi.org/
Hamilton, E. S., Schlegel, A. M., & Haswell, E. S. (2015b). United in            10.1126/science.290.5494.1151
   diversity: Mechanosensitive ion channels in plants. Annual Review of       Maity, K., Heumann, J. M., McGrath, A. P., Kopcho, N. J., Hsu, P.
   Plant Biology, 66, 113–137. https://doi.org/10.1146/annurev-arplant-          K., Lee, C. W., Mapes, J. H., Garza, D., Krishnan, S., Morgan,
   043014-114700                                                                 G. P., Hendargo, K. J., Klose, T., Rees, S. D., Medrano-Soto, A.,
Hedrich, R. (2012). Ion channels in plants. Physiological Reviews, 92,           Saier, M. H., Jr., Piñeros, M., Komives, E. A., Schroeder, J. I., . . .
   1777–1811. https://doi.org/10.1152/physrev.00038.2011                         Stowell, M. H. B. (2019). Cryo-EM structure of OSCA1.2 from
Hou, C., Tian, W., Kleist, T., He, K., Garcia, V., Bai, F., Hao, Y., Luan,       Oryza sativa elucidates the mechanical basis of potential membrane
   S., & Li, L. (2014). DUF221 proteins are a family of osmosensitive            hyperosmolality gating. Proceedings of the National Academy of
   calcium-permeable cation channels conserved across eukaryotes. Cell           Sciences, 116, 14309–14318. https://doi.org/10.1073/pnas.19007741
   Research, 24, 632–635. https://doi.org/10.1038/cr.2014.14                     16
Jia, Y., Zhao, Y., Kusakizako, T., Wang, Y., Pan, C., Zhang, Y., Nureki,      Malvezzi, M., Chalat, M., Janjusevic, R., Picollo, A., Terashima, H.,
   O., Hattori, M., & Yan, Z. (2020). TMC1 and TMC2 proteins are pore-           Menon, A. K., & Accardi, A. (2013). Ca2+ –dependent phospholipid
   forming subunits of mechanosensitive ion channels. Neuron, 105,               scrambling by a reconstituted TMEM16 ion channel. Nature Commu-
   310–321 e313. https://doi.org/10.1016/j.neuron.2019.10.017                    nications, 4, 2367. https://doi.org/10.1038/ncomms3367
Jojoa-Cruz, S., Saotome, K., Murthy, S. E., Tsui, C. C. A., Sansom, M.        Mano, I., & Driscoll, M. (1999). DEG/ENaC channels: A touchy
   S., Patapoutian, A., & Ward, A. B. (2018). Cryo-EM structure of the           superfamily that watches its salt. BioEssays, 21, 568–578.
   mechanically activated ion channel OSCA1.2. eLife, 7. https://doi.org/        https://doi.org/10.1002/(SICI)1521-1878(199907)21:7⟨568::AID-
   10.7554/eLife.41845                                                           BIES5⟩3.0.CO;2-L
Kall, L., Krogh, A., & Sonnhammer, E. L. (2007). Advantages of com-           Matsunaga, K. K., & Tomescu, A. M. (2016). Root evolution at the
   bined transmembrane topology and signal peptide prediction—The                base of the lycophyte clade: Insights from an early Devonian lyco-
   Phobius web server. Nucleic Acids Research, 35, W429–W432. https:             phyte. Annals of Botany, 117, 585–598. https://doi.org/10.1093/aob/
   //doi.org/10.1093/nar/gkm256                                                  mcw006
Katoh, K., & Standley, D. M. (2013). MAFFT multiple sequence align-           McAdam, S. A., & Brodribb, T. J. (2013). Ancestral stomatal con-
   ment software version 7: Improvements in performance and usabil-              trol results in a canalization of fern and lycophyte adaptation to
   ity. Molecular Biology and Evolution, 30, 772–780. https://doi.org/           drought. The New phytologist, 198, 429–441. https://doi.org/10.1111/
   10.1093/molbev/mst010                                                         nph.12190
                                                                                                                                                            19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
18 of 19      The Plant Genome                                                                                                                 WU ET AL.


McAdam, S. A., & Brodribb, T. J. (2014). Separating active and passive         Ronquist, F., Teslenko, M., van der Mark, P., Ayres, D. L., Darling, A.,
   influences on stomatal control of transpiration. Plant Physiology, 164,        Höhna, S., Larget, B., Liu, L., Suchard, M. A., & Huelsenbeck, J.
   1578–1586. https://doi.org/10.1104/pp.113.231944                               P. (2012). MrBayes 3.2: Efficient Bayesian phylogenetic inference
Medrano-Soto, A., Moreno-Hagelsieb, G., McLaughlin, D., Ye, Z. S.,                and model choice across a large model space. Systematic Biology, 61,
   Hendargo, K. J., & Saier, M. H. Jr. (2018). Bioinformatic character-           539–542. https://doi.org/10.1093/sysbio/sys029
   ization of the Anoctamin Superfamily of Ca2+ –activated ion chan-           Samanta, A., Hughes, T. E. T., & Moiseenkova-Bell, V. Y. (2018).
   nels and lipid scramblases. Plos One, 13, e0192851. https://doi.org/           Transient receptor potential (TRP) channels. In J. R. Harris & E. J.
   10.1371/journal.pone.0192851                                                   Boekema (Eds.), Membrane protein complexes: Structure and func-
Monshausen, G. B., & Gilroy, S. (2009). Feeling green: Mechanosens-               tion (pp. 141–165). Springer Singapore.
   ing in plants. Trends in Cell Biology, 19, 228–235. https://doi.org/10.     Schenk, H. J., Espino, S., Romo, D. M., Nima, N., Do, A. Y., Michaud,
   1016/j.tcb.2009.02.005                                                         J. M., Papahadjopoulos-Sternberg, B., Yang, J., Zuo, Y. Y., Steppe,
Morris, J. L., Puttick, M. N., Clark, J. W., Edwards, D., Kenrick, P.,            K., & Jansen, S. (2017). Xylem surfactants introduce a new element
   Pressel, S., Wellman, C. H., Yang, Z., Schneider, H., & Donoghue,              to the cohesion-tension theory. Plant Physiology, 173, 1177–1196.
   P. C. J. (2018). The timescale of early land plant evolution. Pro-             https://doi.org/10.1104/pp.16.01039
   ceedings of the National Academy of Sciences, 115, E2274–E2283.             Servin-Vences, M. R., Moroni, M., Lewin, G. R., & Poole, K. (2017).
   https://doi.org/10.1073/pnas.1719588115                                        Direct measurement of TRPV4 and PIEZO1 activity reveals multiple
Murthy, S. E., Dubin, A. E., Whitwam, T., Jojoa-Cruz, S., Cahalan,                mechanotransduction pathways in chondrocytes. eLife, 6. https://doi.
   S. M., Mousavi, S. A. R., Ward, A. B., & Patapoutian, A. (2018).               org/10.7554/eLife.21074
   OSCA/TMEM63 are an evolutionarily conserved family of mechan-               Startek, J. B., Boonen, B., Talavera, K., & Meseguer, V. (2019). TRP
   ically activated ion channels. eLife, 7. https://doi.org/10.7554/eLife.        channels as sensors of chemically-induced changes in cell membrane
   41844                                                                          mechanical properties. International Journal of Molecular Sciences,
Ohno, S. (1970). Evolution by gene duplication. Springer-Verlag.                  20, 371. https://doi.org/10.3390/ijms20020371
Ohtani, M., Akiyoshi, N., Takenaka, Y., Sano, R., & Demura, T. (2017).         Sussmilch, F. C., Brodribb, T. J., & McAdam, S. A. (2017). What are
   Evolution of plant conducting cells: Perspectives from key regulators          the evolutionary origins of stomatal responses to abscisic acid in land
   of vascular cell differentiation. Journal of Experimental Botany, 68,          plants? Journal of Integrative Plant Biology, 59, 240–260. https://doi.
   17–26. https://doi.org/10.1093/jxb/erw473                                      org/10.1111/jipb.12523
One Thousand Plant Transcriptomes Initiative. (2019). One thousand             Sussmilch, F. C., Roelfsema, M. R. G., & Hedrich, R. (2019a). On the
   plant transcriptomes and the phylogenomics of green plants. Nature,            origins of osmotically driven stomatal movements. The New Phytol-
   574, 679–685. https://doi.org/10.1038/s41586-019-1693-2                        ogist, 222, 84–90. https://doi.org/10.1111/nph.15593
Passioura, J. B. (2001). Plant–water relations. In Encyclopedia of life sci-   Sussmilch, F. C., Schultz, J., Hedrich, R., & Roelfsema, M. R. G.
   ences (pp. 1–7). John Wiley & Sons, Ltd.                                       (2019b). Acquiring control: The evolution of stomatal signalling path-
Peier, A. M., Reeve, A. J., Andersson, D. A., Moqrich, A., Earley, T.             ways. Trends in Plant Science, 24, 342–351. https://doi.org/10.1016/
   J., Hergarden, A. C., Storys, G. M., Colley, I., Hogenesch, J. B.,             j.tplants.2019.01.002
   McIntyre, P., Hergarden, A. C., Bevan, S., & Patapoutian, A. (2002).        Suyama, M., Torrents, D., & Bork, P. (2006). PAL2NAL: Robust con-
   A heat-sensitive TRP channel expressed in keratinocytes. Science,              version of protein sequence alignments into the corresponding codon
   296, 2046–2049. https://doi.org/10.1126/science.1073140                        alignments. Nucleic Acids Research, 34, W609–W612. https://doi.
Price, M. N., Dehal, P. S., & Arkin, A. P. (2009). FastTree: Comput-              org/10.1093/nar/gkl315
   ing large minimum evolution trees with profiles instead of a dis-           Syeda, R., Florendo, M. N., Cox, C. D., Kefauver, J. M., Santos, J. S.,
   tance matrix. Molecular Biology and Evolution, 26, 1641–1650. https:           Martinac, B., & Patapoutian, A. (2016). Piezo1 channels are inher-
   //doi.org/10.1093/molbev/msp077                                                ently mechanosensitive. Cell Reports, 17, 1739–1746. https://doi.org/
Putnam, N. H., Butts, T., Ferrier, D. E., Furlong, R. F., Hellsten,               10.1016/j.celrep.2016.10.033
   U., Kawashima, T., Robinson-Rechavi, M., Shoguchi, E., Terry, A.,           Taylor, J. S., & Raes, J. (2004). Duplication and divergence: The evo-
   Yu, J.-K., Benito-Gutiérrez, E., Dubchak, I., Garcia-Fernàndez, J.,            lution of new genes and old ideas. Annual Review of Genetics, 38,
   Gibson-Brown, J. J., Grigoriev, I. V., Horton, A. C., de Jong, P. J.,          615–643. https://doi.org/10.1146/annurev.genet.38.072902.092831
   Jurka, J., Kapitonov, V. V., . . . Rokhsar, D. S. (2008). The amphioxus     Thor, K., Jiang, S., Michard, E., George, J., Scherzer, S., Huang, S.,
   genome and the evolution of the chordate karyotype. Nature, 453,               Dindas, J., Derbyshire, P., Leitão, N., DeFalco, T. A., Köster, P.,
   1064–1071. https://doi.org/10.1038/nature06967                                 Hunter, K., Kimura, S., Gronnier, J., Stransfeld, L., Kadota, Y.,
Puttick, M. N., Morris, J. L., Williams, T. A., Cox, C. J., Edwards, D.,          Bücherl, C. A., Charpentier, M., Wrzaczek, M., . . . Zipfel, C. (2020).
   Kenrick, P., Pressel, S., Wellman, C. H., Schneider, H., Pisani, D., &         The calcium-permeable channel OSCA1.3 regulates plant stomatal
   Donoghue, P. C. J. (2018). The interrelationships of land plants and           immunity. Nature, 585, 569–573. https://doi.org/10.1038/s41586-
   the nature of the ancestral embryophyte. Current Biology, 28, 733–             020-2702-1
   745. https://doi.org/10.1016/j.cub.2018.01.063                              Venturas, M. D., Sperry, J. S., & Hacke, U. G. (2017). Plant xylem
Ranade, S. S., Syeda, R., & Patapoutian, A. (2015). Mechanically acti-            hydraulics: What we understand, current research, and future chal-
   vated ion channels. Neuron, 87, 1162–1179. https://doi.org/10.1016/            lenges. Journal of Integrative Plant Biology, 59, 356–389. https://doi.
   j.neuron.2015.08.032                                                           org/10.1111/jipb.12534
Riedell, W. E., & Schumacher, T. E. (2009). Transport of water and nutri-      Wadskog, I., Forsmark, A., Rossi, G., Konopka, C., Öyen, M., Goksör,
   ents in plants. In L. Rattan (Ed.), Agricultural sciences (Vol. 1, pp.         M., Ronne, H., Brennwald, P., & Adler, L. (2006). The yeast tumor
   372–378). Eolss Publishers.                                                    suppressor homologue Sro7p is required for targeting of the sodium
                                                                                                                                                         19403372, 2022, 2, Downloaded from https://acsess.onlinelibrary.wiley.com/doi/10.1002/tpg2.20198 by University Of Sao Paulo - Brazil, Wiley Online Library on [04/08/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
WU ET AL.                                                                                                    The Plant Genome                 19 of 19


  pumping ATPase to the cell surface. Molecular Biology of the Cell,          Molecular Biology and Evolution, 19, 908–917. https://doi.org/10.
  17, 4988–5003. https://doi.org/10.1091/mbc.e05-08-0798                      1093/oxfordjournals.molbev.a004148
Walker, R. G., Willingham, A. T., & Zuker, C. S. (2000). A Drosophila       Yuan, F., Yang, H., Xue, Y., Kong, D., Ye, R., Li, C., Zhang, J.,
  mechanosensory transduction channel. Science, 287, 2229–2234.               Theprungsirikul, L., Shrift, T., Krichilsky, B., Johnson, K. M., Swift,
  https://doi.org/10.1126/science.287.5461.2229                               G. B., He, Y., Siedow, J. N., & Pei, Z.-M. (2014). OSCA1 medi-
Wang, X., Liu, Y., & Yang, P. (2012). Proteomic studies of the abiotic        ates osmotic-stress-evoked Ca2+ increases vital for osmosensing in
  stresses response in model moss: Physcomitrella patens. Frontiers in        Arabidopsis. Nature, 514, 367–371. https://doi.org/10.1038/nature1
  Plant Science, 3, 258. https://doi.org/10.3389/fpls.2012.00258              3593
Weadick, C. J., & Chang, B. S. (2012). An improved likelihood ratio         Zhai, Y., Wen, Z., Fang, W., Wang, Y., Xi, C., Liu, J., Zhao, H., Wang,
  test for detecting site-specific functional divergence among clades of      Y., & Han, S. (2021). Functional analysis of rice OSCA genes over-
  protein-coding genes. Molecular Biology and Evolution, 29, 1297–            expressed in the arabidopsis osca1 mutant due to drought and salt
  1300. https://doi.org/10.1093/molbev/msr311                                 stresses. Transgenic Research, 30, 811–820. https://doi.org/10.1007/
Xu, H., Ramsey, I. S., Kotecha, S. A., Moran, M. M., Chong, J. A.,            s11248-021-00270-x
  Lawson, D., Ge, P., Lilly, J., Silos-Santiago, I., Xie, Y., DiStefano,    Zhai, Y., Wen, Z., Han, Y., Zhuo, W., Wang, F., Xi, C., Liu, J., Gao,
  P. S., Curtis, R., & Clapham, D. E. (2002). TRPV3 is a calcium-             P., Zhao, H., Wang, Y., Wang, Y., & Han, S. (2020). Heterogeneous
  permeable temperature-sensitive cation channel. Nature, 418, 181–           expression of plasma-membrane-localised OsOSCA1.4 complements
  186. https://doi.org/10.1038/nature00882                                    osmotic sensing based on hyperosmolality and salt stress in Arabidop-
Yan, H., Helman, G., Murthy, S. E., Ji, H., Crawford, J., Kubisiak,           sis osca1 mutant. Cell Calcium, 91, 102261. https://doi.org/10.1016/
  T., Bent, S. J., Xiao, J., Taft, R. J., Coombs, A., Wu, Y., Pop, A.,        j.ceca.2020.102261
  Li, D., de Vries, L. S., Jiang, Y., Salomons, G. S., van der Knapp,       Zhang, J., Nielsen, R., & Yang, Z. (2005). Evaluation of an improved
  M. S., Patapoutian, A., Simons, C., . . . Wolf, N. I. (2019). Het-          branch-site likelihood method for detecting positive selection at the
  erozygous variants in the mechanosensitive ion channel TMEM63A              molecular level. Molecular Biology and Evolution, 22, 2472–2479.
  result in transient hypomyelination during infancy. American Journal        https://doi.org/10.1093/molbev/msi237
  of Human Genetics, 105, 996–1004. https://doi.org/10.1016/j.ajhg.         Zhang, M. F., Wang, D. L., Kang, Y. L., Wu, J. X., Yao, F. Q., Pan, C.
  2019.09.011                                                                 F., Pan, C. F., Pan, C. F., et al., & Chen, L. (2018). Structure of the
Yan, Z., Zhang, W., He, Y., Gorczyca, D., Xiang, Y., Cheng, L. E.,            mechanosensitive OSCA channels. Nature Structural & Molecular
  Meltzer, S., Jan, L. Y., & Jan, Y. N. (2013). Drosophila NOMPC              Biology, 25, 850–858. https://doi.org/10.1038/s41594-018-0117-6
  is a mechanotransduction channel subunit for gentle-touch sensation.
  Nature, 493, 221–225. https://doi.org/10.1038/nature11685
Yang, H., Kim, A., David, T., Palmer, D., Jin, T., Tien, J., Huang, F.,
                                                                            S U P P O RT I N G I N F O R M AT I O N
  Cheng, T., Coughlin, S. R., Jan, Y. N., & Jan, L. Y. (2012). TMEM16F
                                                                            Additional supporting information may be found in the online
  forms a Ca2+-activated cation channel required for lipid scrambling
  in platelets during blood coagulation. Cell, 151, 111–122. https://doi.   version of the article at the publisher’s website.
  org/10.1016/j.cell.2012.07.036
Yang, Z. (1997). PAML: A program package for phylogenetic analysis
  by maximum likelihood. Computer Applications in the Biosciences,
  13, 555–556. https://doi.org/10.1093/bioinformatics/13.5.555                 How to cite this article: Wu, X., Yuan, F., Wang, X.,
Yang, Z. (1998). Likelihood ratio tests for detecting positive selection       Zhu, S., & Pei, Z.-M. (2022). Evolution of
  and application to primate lysozyme evolution. Molecular Biology             osmosensing OSCA1 Ca channel family coincident
  and Evolution, 15, 568–573. https://doi.org/10.1093/oxfordjournals.          with plant transition from water to land. Plant
  molbev.a025957                                                               Genome, 15, e20198.
Yang, Z., & Nielsen, R. (2002). Codon-substitution models for detect-
                                                                               https://doi.org/10.1002/tpg2.20198
  ing molecular adaptation at individual sites along specific lineages.
