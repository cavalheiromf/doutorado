# She_2022 - Genome-Wide Identification, Evolution and Expressional Analy

**Source PDF:** 

---

              International Journal of
              Molecular Sciences


Article
Genome-Wide Identification, Evolution and Expressional
Analysis of OSCA Gene Family in Barley (Hordeum vulgare L.)
Kuijun She 1,2,† , Wenqiu Pan 1,† , Ying Yan 1 , Tingrui Shi 1 , Yingqi Chu 1 , Yue Cheng 1 , Bo Ma 1
and Weining Song 1, *

                                            1   State Key Laboratory of Crop Stress Biology in Arid Areas, College of Agronomy, Northwest A&F University,
                                                Yangling, Xianyang 712100, China
                                            2   Crop Research Institute, Ningxia Academy of Agriculture and Forestry Sciences, Yinchuan 750002, China
                                            *   Correspondence: sweining2002@yahoo.com
                                            †   These authors contributed equally to this work.


                                            Abstract: The hyperosmolality-gated calcium-permeable channel gene family (OSCA) is one kind
                                            of conserved osmosensors, playing a crucial role in maintaining ion and water homeostasis and
                                            protecting cellular stability from the damage of hypertonic stress. Although it has been systematically
                                            characterized in diverse plants, it is necessary to explore the role of the OSCA family in barley,
                                            especially its importance in regulating abiotic stress response. In this study, a total of 13 OSCA
                                            genes (HvOSCAs) were identified in barley through an in silico genome search method, which
                                            were clustered into 4 clades based on phylogenetic relationships with members in the same clade
                                            showing similar protein structures and conserved motif compositions. These HvOSCAs had many
                                            cis-regulatory elements related to various abiotic stress, such as MBS and ARE, indicating their
                                            potential roles in abiotic stress regulation. Furthermore, their expression patterns were systematically
                                            detected under diverse stresses using RNA-seq data and qRT-PCR methods. All of these 13 HvOSCAs
                                            were significantly induced by drought, cold, salt and ABA treatment, demonstrating their functions
Citation: She, K.; Pan, W.; Yan, Y.; Shi,   in osmotic regulation. Finally, the genetic variations of the HvOSCAs were investigated using the
T.; Chu, Y.; Cheng, Y.; Ma, B.; Song, W.
                                            re-sequencing data, and their nucleotide diversity in wild barley and landrace populations were
Genome-Wide Identification,
                                            0.4966 × 10−3 and 0.391 × 10−3 , respectively, indicating that a genetic bottleneck has occurred in the
Evolution and Expressional Analysis
                                            OSCA family during the barley evolution process. This study evaluated the genomic organization,
of OSCA Gene Family in Barley
                                            evolutionary relationship and genetic expression of the OSCA family in barley, which not only
(Hordeum vulgare L.). Int. J. Mol. Sci.
2022, 23, 13027. https://doi.org/
                                            provides potential candidates for further functional genomic study, but also contributes to genetically
10.3390/ijms232113027                       improving stress tolerance in barley and other crops.

Academic Editor: Frank M. You
                                            Keywords: barley; OSCA family; abiotic stress; genetic variation; expression pattern
Received: 23 September 2022
Accepted: 22 October 2022
Published: 27 October 2022
                                            1. Introduction
Publisher’s Note: MDPI stays neutral
with regard to jurisdictional claims in           As sessile organisms, plants usually have to suffer from the impact of adverse abiotic
published maps and institutional affil-     stresses, such as drought, salinity and extreme high or low temperature [1,2], which not
iations.                                    only determine the geographical adaptability of plants, but also seriously limits agricultural
                                            productivity worldwide [3]. To cope with these stresses, plants have evolved complicated
                                            and interconnected mechanisms to protect them from the impacts of harsh environments
                                            in a gradual manner [4]. Generally, plants can perceive and transduce extracellular stress
Copyright: © 2022 by the authors.           signals into intracellular second messengers, which are able to trigger a serial of signal
Licensee MDPI, Basel, Switzerland.          cascades to regulate the given metabolic and physiological processes through activating or
This article is an open access article      inhibiting the expression of some specific genes, resulting in cellular homeostasis and the
distributed under the terms and
                                            reprograming of growth to increase stress resistance or adapt to stressed conditions [5,6].
conditions of the Creative Commons
                                                  Calcium ions (Ca2+ ) mainly serve as crucial secondary messengers, playing a pivotal
Attribution (CC BY) license (https://
                                            role in signaling perception and transduction under biotic and abiotic stresses, especially
creativecommons.org/licenses/by/
                                            responding to osmotic change. Previous studies have revealed that calcium channels could
4.0/).




Int. J. Mol. Sci. 2022, 23, 13027. https://doi.org/10.3390/ijms232113027                                           https://www.mdpi.com/journal/ijms
Int. J. Mol. Sci. 2022, 23, 13027                                                                                             2 of 18




                                    act as osmosensors across unicellular prokaryotic bacteria to multicellular eukaryotic mam-
                                    mals [7–11]. In plants, several calcium channels have been characterized to find that they
                                    not only function to mediate the response to abiotic and biotic stresses, but are also involved
                                    in growth regulation and biosynthesis [12–17]. Among them, the hyperosmolality-gated
                                    calcium-permeable channel family (OSCA) is one of the most important and well-studied
                                    calcium channels participating in osmotic adjustment [18,19]. In light of its significance, the
                                    OSCA family has been identified in many plant species, including 15 OSCA members found
                                    in A. thaliana, 11 in rice [18], 42 in wheat [19], 12 in maize [20,21], 13 in mung bean [22], as
                                    well as 35 in cotton [23]. The expression profile of OSCA genes were also systematically in-
                                    vestigated under diverse abiotic stresses in different plant species, which demonstrated their
                                    differential roles in stress response and tolerance [18–23]. Some plant OSCA genes were
                                    also functionally validated. In A. thaliana, AtOSCA1.3 was phosphorylated by the immune
                                    receptor-associated cytosolic kinase BIK1 by treatment with pathogen-associated molecular
                                    patterns (PAMP) fg22, and showed an increase in channel activity, which functioned as a
                                    switch to control stomatal closure in the immune signaling pathway [24]. AtOSCA1 was
                                    found to act as an osmosensor through a calcium imaging-based genetic screen approach,
                                    which was a plasma-membrane located protein with a low hyperosmolality-induced Ca2+
                                    increase (OICI) [25]. In maize, ZmOSCA2.3 and ZmOSCA2.4 were up-regulated under ABA,
                                    PEG and NaCl treatments and over-expression of ZmOSCA2.4 could increase the expression
                                    of drought tolerance related genes while decreasing the expression of senescence-related
                                    genes in A. thaliana, respectively [21]. The expression profile analysis of ZmOSCAs in
                                    15 tissues found that ZmOSCA4.1 was shown to be up-regulated in all tissues and the
                                    genetic variations in ZmOSCA4.1 were significantly associated with drought tolerance at
                                    the seedling stage through association analysis [20]. Over-expression of OsOSCA1.4 in
                                    the A. thaliana osca1 mutant can be complementary with its function in hyperosmolality
                                    reactions under salt stress [26]. Over-expression of eight OsOSCAs in A. thaliana demon-
                                    strated that these OsOSCA members were mainly involved in osmotic perception and
                                    stress adaption, which could regulate stomatal closure, leaf water loss and root growth
                                    through mediating osmotic Ca2+ signaling [27]. Additionally, the function of GhOSCA1.1
                                    was validated by a virus-induced gene silenced (VIGS) approach, which controlled the
                                    activity of antioxidant enzymes to enhance salt and drought resistance [23].
                                         Barley (Hordeum vulgare L.) is the fourth largest cereal crop all over the world in
                                    terms of cultivation area and annual total yield, with great edible, forage and brewing
                                    value [28]. Furthermore, barley is also one of the most stress tolerant crops globally, such
                                    as salt, low temperature and soil infertility stress, providing the gene pool for genetic
                                    improvement against biotic/abiotic stress. However, it is necessary to explore the OSCA
                                    gene family further in order to mine the elite candidates regulating abiotic stress tolerance.
                                    The objective of the current study was to systematically identify the barley OSCA gene
                                    family (HvOSCAs) based on a genome-search approach and its genomic organization,
                                    exon-intron structures and phylogenetic relationship were investigated. Furthermore, the
                                    expression patterns of them were systematically detected during development stages and
                                    under diverse abiotic stresses, and a co-expression network of them was constructed based
                                    on RNA-seq data to obtain the stress-related modules. Finally, quantitative real-time PCR
                                    (qRT-PCR) analysis was used to validate their expressions under diverse stresses and the
                                    stress-related candidates were found. Additionally, the genetic variations of these HvOSCAs
                                    were investigated using population re-sequencing data.

                                    2. Results
                                    2.1. Identification of OSCA Gene in Barley
                                         Based on a genome-search method [18,19], a total of 13 putative OSCA genes were
                                    identified in the barley genome, which were nominated as HvOSCA1.1 to HvOSCA4.1
                                    according to the orthologs in A. thaliana and rice. As two orthologs of OSCA1.3 and OSCA2.1
                                    were found in barley, they were named HvOSCA1.3_1 and HvOSCA1.3_2, HvOSCA2.1_1
                                    and HvOSCA2.1_2, respectively, indicating that segmental duplication events of OSCA
Int. J. Mol. Sci. 2022, 23, 13027                                                                                                       3 of 18




                                    genes had occurred in the barley genome. Sequence characteristics of these HvOSCAs
                                    showed that their gene length ranged from 2385 (HvOSCA4.1) to 26,794 (HvOSCA1.1) base-
                                    pair (bp), while their coding sequence length ranged from 2133 bp to 2400 bp, encoding
                                    711 to 800 amino acids. The isoelectric point (pI) varied from 6.7 to 9.24, and all of the
                                    HvOSCA proteins had a positive GRAVY score, indicating that HvOSCA proteins were
                                    hydrophobic proteins. In addition, the subcellular localization prediction found that all
                                    of the HvOSCAs were located in the inner-membrane (Table S1), which was consistent
                                    with previous studies [18,20,23]. Chromosome distribution analysis found that these
                                    13 HvOSCAs were unevenly distributed on 5 out of 7 barley chromosomes (Figure S1), of
                                    which chr1H, chr4H and chr5H contained 3 OSCA members, chr2H and chr3H harbored
                                    2 OSCA members, and chr6H and chr7H did not have any OSCA members (Table S2).

                                    2.2. Phylogenetic Relationship, Conserved Motifs and Gene Structure Analysis
                                         To explore the phylogenetic relationships of the OSCA family, a neighbor-joining (NJ)
                                    phylogenetic tree was constructed using the full-length protein sequences of 13 HvOSCAs,
                                    42 TaOSCAs, 15 AtOSCAs, 11 OsOSCAs and 11 ZmOSCAs (Table S3). Results showed
                                    that these OSCA proteins were classified into four clades based on phylogenetic rela-
                                    tionship (Figure 1), which was consistent with previous studies [18,19]. Further, thirteen
                                    HvOSCAs were distributed asymmetrically in each clade, with five, six, one and one mem-
                                    bers belonging to clade 1 to clade 4, respectively. In general, the HvOSCAs displayed closer
                                    phylogenetic relationships with those of wheat and rice compared to that of A. thaliana.

                                                                                       Clade1
                                                   HvOSCA1..2
                                                   OsOSC 1.2
                                                    ZmO CA19




                                                                                    Ta SCA .3 2
                                                                                          TaOSCA2
                                                     TaOSCA9




                                                                                      Hv CA1.7
                                                                                          TaOSCA5
                                                                                                 8
                                                                                        AtOS CA1
                                                      TaO CA22




                                                                                          TaOSCA


                                                                                     TaOOSCA1
                                                       TaO CA1 1a
                                                       Hv CA .1b
                                                       Zm OSC CA1 1.3




                                                                                   Ta OSC 13
                                                        SCA




                                                                                Os mOS CA1 5
                                                         Zm OS CA 1.




                                                          S
                                                          OS 1.




                                                                                  Z OS A1
                                                                                         TaOS
                                                          OS A1 .1




                                                                               Hv OS CA 7
                                                           A1
                                                           S




                                                                                 OS CA 1.3
                                                             Os tOS CA




                                                                                   CA 1.3
                                                              2




                                                                                          1
                                                               A tOS




                                                                                        3
                                                                                     1.
                                                  At                                                           11
                                                                 .1
                                                                 A




                                                At OSC                                                      CA A4
                                                  O
                                              At SC A1                                                    S
                                                                                                        O C 7
                                                O
                                             AtO SC A1. .1                                            Ta aOS CA 1.8
                                                                       4




                                                SC A1.5 2                                               T aOS CA .4
                                                   A1                                                     T tOS CA1
                                                      .6                                                    A OS A1.4
                                           TaO                                                               Zm OSC 6
                                               S                                                               Os SCA 4
                                          TaOS CA38                                                             TaO SCA1.
                                                C
                                         TaOSC A40                                                               HvO CA10
                                      HvOSCA A33                                                                  TaOS A3
                                                2.1 1                                                             TaOSC
                                      HvOSCA2.1 2                                                                  AtOSCA4.1
                                        TaOSCA37                                                                   ZmOSCA4.1
                                        TaOSCA34                                                                   OsOSCA4.1
                                                                                                                  HvOSCA4.
                                                                                                                               Clade4




                                        TaOSCA41                                                                  TaOSCA 1
                                                A2.1                                                                     36
                                        OsOSC 2.1                                                                TaOS
                                          m O SCA 26                                                            TaO CA32
                                        Z
                                               SCA                                                             AtO SCA29
                                           TaO CA27                                                           Zm SCA3
                                                 S    .2                                                    O OSC .1
                                            TaO CA2 30
                                              v OS CA 5                                                   Ta sOSC A3.1
                                            H OS A2                                                      H OS A3
                                               Ta SC A2.2 2                                            T vO CA .1
                                                   O      .
                                                 Ta SC A2 .1                                         Ta aOS SCA 12
                                                                                                       O C
                                                   m O SC A2                                            SC A1 3.1
                                                                               Ta aOS CA 2.5
                                                          Ta SC A24 2




                                                  Z sO SC                                                  A 6
                                                                     .




                                                                                 T OS CA
                                                            Ta OSC A2




                                                                                 OS CA 2.5




                                                                                                             14
                                                                                                                    Cl




                                                     O tO
                                                                                  At OS A2.5
                                                        Hv OSC A31
                                                              Ta SC




                                                                                    CA 21
                                                                                    Zm OSC 2.5
                                                      Zm SCA 28




                                                                                                                      ad




                                                      A
                                                                                     Os OSCA 3
                                                         OSC 2.3
                                                                  O




                                                                                                                        e3
                                                                                      Hv SCA2
                                                          SC 2.3
                                                                 A




                                                                                      18
                                                                                       TaO SCA20
                                                      TaOS A2.3
                                                               At




                                                                                        TaO A2.3
                                                     TaOSC A35




                                                                                        AtOSC 2.4
                                                     TaOSCA3 2


                                                                                         AtOSCA
                                                               9

                                                                                         ZmOSCA2.4
                                                    HvOSCA2.4
                                                                                         OsOSCA2.4
                                                              O


                                                              A


                                                            A4
                                                           C
                                                          O




                                                      e2
                                                      OsO




                                                    ad
                                                  Cl




                                    Figure 1. Phylogenetic analysis of the OSCA genes in Hordeum vulgare (Hv), Arabidopsis thaliana (At),
                                    Triticum aestivum (Ta), Oryza satival (Os) and Zea mays (Zm) by the neighbor-joining method. The
                                    OSCAs were clustered into four clades; each member of the OSCAs were annotated by (F for Hv),
                                    (• for At), ( for Ta), ( for Os) and ( for Zm), respectively.
Int. J. Mol. Sci. 2022, 23, 13027                                                                                                                                                                          4 of 18




                                                              Then, the conserved motifs and exon-introns of the HvOSCAs were analyzed (Figure 2).
                                                         It was indicated that all of the 13 HvOSCAs possessed three conserved function domains,
                                                         RSN1_TM (PF13967), 7TM (PF02714) and PHM7_cyt (PF14703) (Figure 2B), which were
                                                         the specific components of OSCA proteins [29,30], indicating the accuracy of the prediction
                                                         of HvOSCAs. Furthermore, a total of 10 conserved motifs were also found in HvOSCAs
                                                         (Figure 2C,E, Table S4). The majority of HvOSCAs displayed the relatively consistent
                                                         motif compositions with 8 to 10 conserved motifs, of which HvOSCA2.1_1, HvOSCA2.1_2,
                                                         HvOSCA2.2 and HvOSCA2.3 contained 9 motifs except motif-6, while HvOSCA1.1 and
                                                         HvOSCA3.1 contained 9 motifs except motif-1. Additionally, HvOSCA4.1 had only one
                                                         conserved motif. These different organizations of conserved motifs might correlate to the
                                                         different function of these HvOSCAs.
                                        motif-1    motif-2     motif-3   motif-4    motif-5
                                                                                                     PF02714         PF13967   PF14703
                                        motif-6    motif-7     motif-8   motif-9    motif-10
        (A)                         (B)                                                        (C)                                   (D)    (E)
                      HvOSCA2.1_2
                      HvOSCA2.1_1
                        OsOSCA2.1
                        OsOSCA2.2
                       HvOSCA2.2
                        AtOSCA2.2
                        AtOSCA2.1
                        OsOSCA2.3
                       HvOSCA2.3
                        AtOSCA2.3
                        AtOSCA2.4
                        OsOSCA2.4
                       HvOSCA2.4
                        OsOSCA2.5
                       HvOSCA2.5                                                                                                            motif                                seq
                        AtOSCA2.5                                                                                                          motif-1 MPAAFVSFKSRWGAAVCAQTQQTSNPTEWLTEWAPEPRDVYWSNLAIPYV
                        OsOSCA3.1
                       HvOSCA3.1
                                                                                                                                           motif-2          PLJLPFJLVYFALAYLVYRNQIJNVYNQKYESGGRFWPIVH
                        AtOSCA3.1                                                                                                          motif-3                 QSPKDIPRTJAVAIPMKATFFITYVMVD
                        OsOSCA4.1
                                                                                                                                           motif-4             YLLYKEYKHIATMRLAFLASEKRRPDQFTVLVRNI
                       HvOSCA4.1
                        AtOSCA4.1                                                                                                          motif-5                TVEHFFLVNHPDHYLSHQVVYNANKLAK
                        OsOSCA1.4
                                                                                                                                           motif-6    WAGVAGEILRLKPLIIFHLKNFFLVKTEKDREEAMDPGSJGFNTTEPRIQ
                       HvOSCA1.4
                        AtOSCA1.8                                                                                                          motif-7                    FAVLRKQPINDRVYFPKWYLK
                        OsOSCA1.3                                                                                                          motif-8              YLPFLNWMPAALKMPEPELJAHAGLDSVVYL
                      HvOSCA1.3_1
                      HvOSCA1.3_2
                                                                                                                                           motif-9                TJLFHKYCKNRFEPAFVKYPLQEAMDKDT
                        AtOSCA1.7                                                                                                          motif-10             KJFLILLPTILMLMSKFEGFISVSSLERRAASKY
                        OsOSCA1.2
                       HvOSCA1.2
                        OsOSCA1.1
                       HvOSCA1.1
                        AtOSCA1.4
                        AtOSCA1.3
                        AtOSCA1.2
                        AtOSCA1.1
                        AtOSCA1.6
                        AtOSCA1.5

                                    0             200             400         600             0       200      400     600
                                                                                                                                     0                10k                              20k




                                                             Figure 2. Motif composition, conserved domain and gene structure analysis of HvOSCAs. (A) Phylo-
                                                             genetic relationship of HvOSCAs, members of different clades were marked in different background
                                                             colors. (B) Functional motif compositions of these 13 HvOSCAs. Ten motifs were represented by
                                                             rectangle box in different colors. (C) The function conserved domain of PFAM02714, PFAM13967 and
                                                             PFAM14703 organization in HvOSCAs, represented by dark blue, dark turquoise boxes and purplish
                                                             blue, respectively. (D) Intron-exon organizations of HvOSCAs. The introns and exons are represented
                                                             by the broken line and gray boxes, respectively. (E) The protein sequence of the 10 identified motifs.

                                                               Exon-intron structure is an evolutionary force to decide the functional diversifica-
                                                         tion of the members in gene family [31]. It was found that the intron characteristics of
                                                         HvOSCAs were highly variable with the number ranging from 0 to 11. Similar to its ortholog
                                                         OsOSCA4.1 and AtOSCA4.1, HvOSCA4.1 had no introns reported, while HvOSCA1.1 had
                                                         11 introns. Additionally, HvOSCA1.1 also had the longest intron length, which might due
                                                         to a retro-transposon-like element insertion. Overall, the members in the same clade based
                                                         on phylogenetic relationship shared similar motif compositions and exon-intron structure,
                                                         suggesting that they might have more similar biological functions.

                                                             2.3. Cis-Element Analysis of HvOSCAs
                                                                  A total of 37 kinds of cis-elements were predicted in the upstream 2000 bp from the
                                                             transcription start sites of HvOSCAs (Figure 3, Table S5), which were widely involved
                                                             in growth biological process, hormone responsiveness, light responsiveness, metabolic
                                                             regulation, as well as stress response. Among them, the elements associated with response
Int. J. Mol. Sci. 2022, 23, 13027                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     5 of 18




                                                                                                                   to biotic or abiotic stresses were identified in almost all HvOSCAs, such as the drought re-
                                                                                                                   sponsive element (MBS) found in eleven HvOSCAs, anaerobic induction elements (ARE) in
                                                                                                                   ten HvOSCAs, anoxic specific induction elements (GC-motif) in five HvOSCAs, as well as a
                                                                                                                   wound responsive element (WUN-motif) in one HvOSCA and a defense-responsive element
                                                                                                                   (AT-rich element) in one HvOSCA. Furthermore, nine types of hormone-responsive regu-
                                                                                                                   latory elements were also found, including auxin-responsive elements (AuxRR-core and
                                                                                                                   TGA-element) in four HvOSCAs, gibberellin-responsive elements (P-box and GARE-motif)
                                                                                                                   in eight HvOSCAs, salicylic acid-responsive elements (TCA-element) in four HvOSCAs,
                                                                                                                   MeJA-responsive elements (CGTCA-motif and TGACG-motif) in ten HvOSCAs and ABA-
                                                                                                                   responsive elements (ABRE) in eleven HvOSCAs. Additionally, there were meristem
                                                                                                                   expression-related elements (CAT-box) in five HvOSCAs, circadian control-related elements
                                                                                                                   (circadian) in two HvOSCAs and a cell cycle regulation-related element (SA-like) in one
                                                                                                                   HvOSCA. The results provided some clues about the putative roles that HvOSCAs play in
                                                                                                                   barley growth, development and stress response.
                                                                                                                                                                                                                                                                                                           metabolic responsive                                                stress responsive                                                                   3-AF3 binding site   4cl-CMA1b     ABRE         ACE             ARE              AT-rich element

                                                                                                                                                                                                                                                                                                                                                                                                                                                                   AT-rich sequence     ATCT-motif    AuxRR-core   Box 4           Box II           CAT-box
                                                                                                                                                             3-AF3 binding site




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   circadian




                                                                                                                                                                                                                                                                                                                                                                                             AT-rich sequence
                                                                                                                                                                                                                                                                                                                                                                                                                                                                   CGTCA-motif          chs-CMA1a     chs-CMA2a    chs-Unit 1 m1                    G-Box




                                                                                                                                                                                                                                                                                                                                                                                                                                 TC-rich repeats
                                                                                                                                                                                                                                                                                                                                                                           AT-rich element
                                                                                                                                               TGACG-motif
                                                                          CGTCA-motif




                                                                                                                                                                                                                                                          chs-Unit 1 m1




                                                                                                                                                                                                                                                                                                                                                                                                                                                                   GARE-motif           GATA-motif    GC-motif     GT1-motif       LTR              MBS
                                                                                                                                 TGA-element
                                                                                                                   TCA-element
                                                                                        GARE-motif
                                                             AuxRR-core




                                                                                                                                                                                                                                                                                                                                  TCCC-motif
                                                                                                                                                                                                                                                                                  GATA-motif
                                                                                                                                                                                                    ATCT-motif




                                                                                                                                                                                                                                                                                                                                                                                                                                                   WUN-motif
                                                                                                                                                                                                                                  chs-CMA1a
                                                                                                                                                                                                                                              chs-CMA2a
                                                                                                                                                                                  4cl-CMA1b




                                                                                                                                                                                                                                                                                                                 Pc-CMA2c




                                                                                                                                                                                                                                                                                                                                               TCT-motif
                                                                                                                                                                                                                                                                                               GT1-motif




                                                                                                                                                                                                                                                                                                                                                                                                                                                                   MRE                  MSA-like      O2-site      P-box           Pc-CMA2c         Sp1




                                                                                                                                                                                                                                                                                                                                                                                                                GC-motif
                               circadian
                                           MSA-like
                     CAT-box




                                                                                                                                                                                                                                                                                                                                                           O2-site
                                                                                                                                                                                                                                                                                                                                                                                                                                                                   TC-rich repeats      TCA-element   TCCC-motif   TCT-motif       TGA-element      TGACG-motif
                                                                                                                                                                                                                                                                          G-Box
                                                      ABRE




                                                                                                                                                                                                                         Box II
                                                                                                           P-box




                                                                                                                                                                                                                 Box 4




                                                                                                                                                                                                                                                                                                           MRE
                                                                                                                                                                                              ACE




                                                                                                                                                                                                                                                                                                                                                                     ARE




                                                                                                                                                                                                                                                                                                                                                                                                                           MBS
                                                                                                     LTR




                                                                                                                                                                                                                                                                                                                            Sp1


                                                                                                                                                                                                                                                                                                                                                                                                                                                                   WUN-motif


         HvOSCA4.1                                                              5             1       1                                              5                 1                                                                                                     1          1                                    2                                 1      2                                                     1
         HvOSCA3.1                                      6                       2                     1                                3             2                                         1                    1                                                        2          1                            1       1          1           1                                                               4
         HvOSCA2.5 1                           1        5                       1                     2                                              1                                                              1                                                        1          1           1       1                1          2                             2                                             5       1
         HvOSCA2.4 1                                    5                       4                                                                    4                                 1                            1                                                        1          1                                    3                      2          1      1                               1             1       1
         HvOSCA2.3                                      1                       2                     1       1                                      2                                                                                                                                                                       1         1           2                  2                                                                   1             1
         HvOSCA2.2 2                1                   1          1                                  1                  1                                                                     1                                       1                                                1                                                                             1             1                                       1
       HvOSCA2.1_2                                      1                                             1       1                                                                                           1                                        1                                    1                                    3                                 1      2                                             2       2
       HvOSCA2.1_1                                      6                       7                     1       1                                      7                                                                                                                       1                                               1          1           1          2      4                                             3       1
         HvOSCA1.4                  1                   3                       1             2       2                  1             1             1                                                              2       1                                                1                      1                        1                      1                 1                                                     2
       HvOSCA1.3_2                                      2          1            2                             1                        1             2                                                              2       1                                                                                                                       1                 2                                                     5
       HvOSCA1.3_1 2                                    2                       1                             1          1                           1                                                              1                                                                                                                               1          1      3                                                     1
         HvOSCA1.2 2                                    9                                             1                                                                                                                                                          1           2                                                          1                      1                                                            2
         HvOSCA1.1                                                              1             1              1           1                           1                                                              1                              1                                                2       1                1          1           1                                                 2                     1
                                                                                                                                                                                                                                                                                                                                                                                                                                                               0                           10                      20                          30



                                                                                                                    Figure 3. Cis-elements found in the promoter region of HvOSCAs. (Left): The number and function
                                                                                                                    classification of cis-acting element in each HvOSCA genes. (Right): Distribution of 37 identified
                                                                                                                    cis-acting elements in each HvOSCA; elements are represented by the boxes in different colors.

                                                                                                                   2.4. Expression Profiles of HvOSCAs in Tissues and under Stress Conditions Based on
                                                                                                                   RNA-Seq Data
                                                                                                                         To obtain some clues about the potential function of HvOSCAs, spatio-temporal expres-
                                                                                                                   sion profiles of them were investigated based on previous open access available RNA-seq
                                                                                                                   data of 16 different tissues at different growth stages (Figure 4A, Tables S6 and S7). Current
                                                                                                                   study results showed that HvOSCA1.1 and HvOSCA3.1 were highly expressed in almost
                                                                                                                   all tested tissues across diverse developmental stages, indicating that these OSCAs played
                                                                                                                   important roles in regulating the growth and development of barley. HvOSCA4.1 was
                                                                                                                   found to be expressed in all tissues/stages but with a relative lower level. At the same
                                                                                                                   time, six HvOSCAs displayed no expression in these tissues/stages, including HvOSCA1.2,
                                                                                                                   HvOSCA1.3_1, HvOSCA1.3_2, HvOSCA3.1, HvOSCA2.3 and HvOSCA2.5, suggesting that
                                                                                                                   they might not function on barley growth and development. HvOSCA1.4 showed high
                                                                                                                   expression in CAR5, RAC and LOO, but no expression in other stages/tissues. HvOSCA2.2
                                                                                                                   showed relatively higher expression in CAR15, LEM, NOD, RAC and ROC while lower
                                                                                                                   expression in other tissues/stages. Furthermore, some tissue-specific HvOSCAs were also
                                                                                                                   identified. It was interesting that the segmental duplication genes HvOSCA2.1_1 and
                                                                                                                   HvOSCA2.1_2 showed diverging expression patterns in these tissues: HvOSCA2.1_2 was
                                                                                                                   highly expressed in EPI, ETI, LEA and NOD, while HvOSCA2.1_1 only expressed in LEM
                                                                                                                   and LOD, despite having highly conserved sequence organization. This divergent expres-
                                                                                                                   sion pattern might be due to their different cis-element compositions, and further study on
                                                                                                                   their expression differentiation could provide helpful information reharding the evolution
                                                                                                                   and function of the duplicated genes.
Int. J. Mol. Sci. 2022, 23, 13027                                                                                                 6 of 18




                                                HvOSCA1.1

                                                HvOSCA1.2

                                               HvOSCA1.3_2

                                               HvOSCA1.3_1                                                        7.5
                                                HvOSCA1.4

                                                HvOSCA3.1
                                                                                                                  5.0
                                                HvOSCA4.1

                                               HvOSCA2.1_2

                                               HvOSCA2.1_1
                                                                                                                  2.5
                                                HvOSCA2.2

                                                HvOSCA2.3

                                                HvOSCA2.4                                                         0.0

                                                HvOSCA2.5
                                                       CA 15
                                                        EM 5
                                                            B




                                                        LE A
                                                        IN 1
                                                         LE 2

                                                           M



                                                        RA L



                                                        SE 2
                                                       N D
                                                          OD


                                                       RO C
                                                        IN I




                                                      RO O
                                                            I




                                                           N
                                                         ET
                                                           R

                                                         EP


                                                           F
                                                           F




                                                          O
                                                         PA
                                                        LO
                                                          R
                                                      CA




                                                HvOSCA1.1

                                                HvOSCA1.2

                                              HvOSCA1.3_2                                                           6
                                              HvOSCA1.3_1

                                                HvOSCA1.4

                                                HvOSCA3.1                                                           4
                                                HvOSCA4.1

                                              HvOSCA2.1_2

                                              HvOSCA2.1_1
                                                                                                                    2
                                                HvOSCA2.2

                                                HvOSCA2.3

                                                HvOSCA2.4
                                                                                                                    0
                                                HvOSCA2.5
                                                         CK ent




                                                           ea n
                                                            ea ld




                                                     Cd CK at




                                                                    t
                                                           ea d


                                                           ea u
                                                          CK elo




                                                     Zn K nt
                                                     Cu CK nt
                                                           CK er
                                                           aC o


                                                             L_ t
                                                          aC er




                                                                  en
                                                         aC a




                                                        _tr _Z
                                                        _tr _C


                                                        _tr _C
                                                         N el




                                                                 m




                                                                  e
                                                                  e
                                                        _tr Co




                                                       N _m
                                                                m
                                                       N _m
                                                               tm




                                                              tm
                                                               l_




                                                              tm
                                                              tm
                                                                _
                                                             l_
                                                      ld _




                                                           C
                                                    Co CK




                                    Figure 4. Expression profiles of HvOSCAs in different tissues and under diverse stresses. (A) The
                                    spatio-temporal expression profile of HvOSCAs in different tissues at different developmental stages.
                                    FPKM values were normalized by log2 (FPKM+1) transformation to display the heatmap color scores.
                                    CAR15: bracts removed grains at 15DAP; CAR5: bracts removed grains at 5DAP (CAR5); embryos
                                    dissected from 4-day-old germinating grains (EMB); epidermis at 4 weeks old (EPI); etiolated from
                                    10-day-old seedling (ETI); young inflorescences with 5 mm (INF1); young inflorescences with 1–1.5 cm
                                    (INF2); shoot with the size of 10 cm from the seedlings (LEA); lemma at 6 weeks after anthesis (LEM);
                                    lodicule at 6 weeks after anthesis (LOD); developing tillers at the six-leaf stage (PAL); 6-week-old
                                    palea (NOD); rachis at 5 weeks after anthesis (RAC); root from 4-week-old seedlings (ROO2); roots
                                    from the seedlings at the 10 cm shoot stage (ROO). (B) Expression profile of HvOSCAs under cold,
                                    NaCl and heavy metal ion (Cd, Cu and Zn) conditions. Cold stress treatment: CK of cold (CK_cold),
                                    cold (4 ◦ C) treatment (Cold_treatment), salt treatment of barley root (dissected and sampled the
                                    barley according to the organizational structure of root for meristem zone, elongation zone and
                                    mature zone). CK of meristem zone (CK_mer), meristem zone under salt treatment (NaCl_mer), CK
                                    of elongation zone (CK_elo), elongation zone under salt treatment (NaCl_elo), CK of maturation
                                    zone (CK_mat) and maturation zone under salt treatment (NaCl_mat). Heavy metal ion (Cd, Cu and
                                    Zn) stress. Control of cadmium ion stress (CK_Cd), cadmium ion treatment (Cd_treatment), control
                                    of copper ion treatment (CK_Cu), copper ion treatment (Cu_treatment), control of zinc ion stress
                                    (CK_Zn) and zipper ion treatment (Zn_treament).
Int. J. Mol. Sci. 2022, 23, 13027                                                                                        7 of 18




                                          As hyperosmotic stress sensors, OSCAs play a vital role in regulating abiotic stress
                                    signaling. Thus, the expression profiles of HvOSCAs were further investigated under
                                    cold, salinity and heavy metal ion abiotic stresses using the previous open access RNA-seq
                                    data (Figure 4B, Tables S6 and S8). Under cold stress treatment, HvOSCA1.2, HvOSCA1.3_1,
                                    HvOSCA2.3 and HvOSCA2.5 did not have any expression, while HvOSCA4.1 highlighted
                                    no differential expression between control and cold treatments. Compared to CK, only
                                    HvOSCA1.1, HvOSCA2.1_1, HvOSCA2.1_2, HvOSCA1.3_2 and HvOSCA2.4 showed up-
                                    regulated expression under cold stress treatment (Figure 4A), which could be considered
                                    as the cold-responsive candidates. Then, the expression patterns of HvOSCA genes were
                                    investigated in the meristem, elongation and mature zones of roots under salinity stress
                                    treatment, and most of them showed differential expressions (Figure 4B, Table S8). Com-
                                    pared with CK (mock), a total of eight, eight and four HvOSCA genes were significantly
                                    up-regulated in the meristem, elongation and maturation zones of roots, respectively.
                                    Especially, HvOSCA2.2 and HvOSCA2.4 exhibited an increasing expression in all three
                                    zones relative to the control. Under metal ion stresses, HvOSCA2.1_1, HvOSCA2.2 and
                                    HvOSCA2.4 were up-regulated under copper (Cu)- and cadmium (Cd)-stressed conditions,
                                    while down-regulated under zinc (Zn) treatment. By contrast, HvOSCA1.1, HvOSCA1.2,
                                    HvOSCA1.3_2 and HvOSCA4.1 were down-regulated under Cu and Cd treatments but
                                    up-regulated under zinc treatment. HvOSCA1.1 and HvOSCA1.2 were down-regulated in
                                    all of the three heavy metal ion treatments. The metal ion-responsive HvOSCAs provided
                                    potential targets for further functional genomics study to reveal their roles in regulating
                                    osmotic adjustment and ion toxicity.

                                    2.5. Co-Expression Network Analysis of HvOSCAs Involved in Abiotic Stress Response
                                         To get more information about the function and molecular modules of HvOSCAs that
                                    are involved in the response to abiotic stresses, the WGCNA method was employed to
                                    analyze the co-expression network based on the RNA-seq data under diverse stresses,
                                    and the HvOSCAs associated modules were identified. The present study results showed
                                    that a total of 27,987 genes displayed significant expressions, and these were used for
                                    constructing co-expression networks. A total of 47 co-expression modules with the gene
                                    number ranging from 34 to 7981 were obtained (Figures S2 and S3, Table S9). Then, the
                                    modules that 13 HvOSCAs were involved were further identified. Results found that
                                    12 out 13 HvOSCAs were inv olved in 7 co-expression modules, including cyan, brown,
                                    blue, turquoise, green, pink and red modules. It is interesting that these 12 HvOSCAs had
                                    the conserved RSN1_7TM functional domain that is the most prominent characteristic of
                                    calcium-permeable stress-gated channel proteins, while the remaining HvOSCA2.3 without
                                    the RSN1_7TM domain was not found in these constructed modules. Furthermore, a
                                    correlation analysis of these seven modules with the stress treatments was performed
                                    (Figure S4). Interestingly, one, one, four, one, two, one and one HvOSCAs were found in
                                    the cyan, brown, blue, turquoise, green, pink and red, respectively. The red module was
                                    significantly correlated with cadmium treatment and the turquoise module was correlated
                                    with cadmium treatment and copper treatment, respectively. The green module was
                                    correlated with NaCl treatment of the mature zone of the root, and also correlated with
                                    copper treatment. The brown module was significantly correlated with NaCl treatment of
                                    the elongation zone. The cyan and pink modules were both correlated with NaCl treatment
                                    of the mature zone. The results suggest the function of HvOSCAs in the heavy metal ion
                                    and salt response.
                                         Then, the current study predicted the miRNA that interacted with HvOSCAs and was
                                    involved in the stress response. Through prediction, eight HvOSCA genes were found to
                                    be targeted by thirteen miRNAs, including miR156, miR6195 and so on. Among them,
                                    HvOSCA1.3_1, HvOSCA1.1 and HvOSCA1.1 could be bound by three miRNAs, respectively.
                                    Meanwhile, Hvu-miR6206 could target both HvOSCA1.3_1 and HvOSCA1.2, and Hvu-
                                    miR6195 could target both HvOSCA1.2 and HvOSCA2.4. Furthermore, with integration
                                    of the miRNA–HvOSCA relationship and the co-regulation modules of HvOSCAs, the
Int. J. Mol. Sci. 2022, 23, 13027                                                                                                                                                            8 of 18




                                               sophisticated regulatory network that HvOSCAs use as the hub and is mediated by miRNAs
                                               was constructed, and a total of 16 miRNA-HvOSCA interactions were obtained (Figure 5,
                                               Table S10). The miRNA-mediated networks contributed to better understand the roles of
                                               HvOSCAs in regulating stress response and resistance in barley, which paved a way to
                                               modulate HvOSCAs expression to induce some physiological changes and then enhance
                                               stress resistance through a post-transcriptional approach.
                                                                                              HORVU.MOREX.r2.6HG0497230             HORVU.MOREX.r2.6HG0462450
                                               HORVU.MOREX.r2.3HG0223010                                            KCS11
                                                                                HORVU.MOREX.r2.4HG0303280
                                                   HORVU.MOREX.r2.7HG0611650                                                                                  ICS
                  HORVU.MOREX.r2.2HG0092530          HORVU.MOREX.r2.4HG0348370
                                                               CEST        HORVU.MOREX.r2.4HG0335940      HORVU.MOREX.r2.7HG0551930
                  HORVU.MOREX.r2.4HG0343430
                                                                                                                                                             IMB1
                                        HvOSCA1.4       HORVU.MOREX.r2.2HG0156970                                                      HvOSCA2.4
                 HORVU.MOREX.r2.4HG0277870                                HORVU.MOREX.r2.5HG0391750 HvOSCA2.2
                                                                                                                     WAXY
                                                         HORVU.MOREX.r2.4HG0281880
                 HORVU.MOREX.r2.6HG0509160 HvOSCA1.3_2                     HORVU.MOREX.r2.5HG0383520                                            HORVU.MOREX.r2.7HG0604200
                                                         HORVU.MOREX.r2.7HG0556520
                 HORVU.MOREX.r2.6HG0495140                                                               HORVU.MOREX.r2.6HG0505700 HORVU.MOREX.r2.7HG0579740
                                                        HORVU.MOREX.r2.4HG0339210     hvu-miR6205
                  HORVU.MOREX.r2.5HG0435880            HORVU.MOREX.r2.3HG0195250              HORVU.MOREX.r2.6HG0526850                                   hvu-miR5049f
                                               hvu-miR6206
                     HORVU.MOREX.r2.7HG0529240                       HORVU.MOREX.r2.3HG0233730                                        HORVU.MOREX.r2.7HG0540240
                         HORVU.MOREX.r2.3HG0214080                   NOP56         HORVU.MOREX.r2.3HG0237090             HORVU.MOREX.r2.6HG0488480
                                                                                                                                                     HORVU.MOREX.r2.5HG0427890
                                                           HORVU.MOREX.r2.6HG0488990    HORVU.MOREX.r2HG0019110          HORVU.MOREX.r2.3HG0230700
                                                                                                                hvu-miR6195                                  HORVU.MOREX.r2.5HG0397940
                                                                                HvOSCA1.2
                         HORVU.MOREX.r2.6HG0454170         HORVU.MOREX.r2.4HG0343460                                                rpl5
                                                                                      HORVU.MOREX.r2.6HG0523600                                    HvOSCA1.1
                                      HORVU.MOREX.r2.2HG0143250
                      hvu-miR156a                            HORVU.MOREX.r2.2HG0137270                                                                      HORVU.MOREX.r2.6HG0472000
                                                                                          RPL3 HORVU.MOREX.r2.4HG0335530
                                                                                                                                  hvu-miR6203
                                                 hvu-miR6190       HORVU.MOREX.r2.7HG0534530                                                                        hvu-miR6202
                                  HvOSCA1.3_1                                                         HORVU.MOREX.r2.3HG0211850 HORVU.MOREX.r2.7HG0542740
                                                                              HORVU.MOREX.r2.6HG0467930                                                 HORVU.MOREX.r2.7HG0618110
               HORVU.MOREX.r2.4HG0278560                                                                     HORVU.MOREX.r2.3HG0206960
                                          HORVU.MOREX.r2.3HG0235200                                                                       HORVU.MOREX.r2.4HG0335370
                HORVU.MOREX.r2.3HG0260540                HORVU.MOREX.r2.5HG0385560 hvu-miR6198                 HORVU.MOREX.r2.5HG0437420
                                                                                                                                                 HORVU.MOREX.r2.7HG0618800
                                       HORVU.MOREX.r2HG0074490                    FAD7                                    hvu-miR6184
                                hvu-miR156b                                                                                           HORVU.MOREX.r2.6HG0464740 HORVU.MOREX.r2.6HG0491320
                                            HORVU.MOREX.r2.7HG0592660     HORVU.MOREX.r2.5HG0416920                HORVU.MOREX.r2.4HG0339370
                                                                           HORVU.MOREX.r2.5HG0408010 HvOSCA3.1      HORVU.MOREX.r2.4HG0326830                    HORVU.MOREX.r2.5HG0427520
                                           HORVU.MOREX.r2.5HG0437670                                                                          ADR1
                                                                 HvOSCA2.1_2                                        HORVU.MOREX.r2.5HG0439100          HvOSCA2.1_1
                                                                                       FEY                                                                      HORVU.MOREX.r2.7HG0576290
                                                   hvu-miR6196                                                                P5CS HORVU.MOREX.r2.6HG0489660
                                                                            HORVU.MOREX.r2.7HG0572580             HORVU.MOREX.r2.4HG0297140                 HORVU.MOREX.r2.5HG0396640
                                                                                                                                         HORVU.MOREX.r2.7HG0576580
                                             HORVU.MOREX.r2.6HG0481310                                           HORVU.MOREX.r2.3HG0235650               HORVU.MOREX.r2.5HG0365770
                                                                       HORVU.MOREX.r2.5HG0421990hvu-miR6204    HORVU.MOREX.r2.4HG0318600
                                                  HORVU.MOREX.r2.6HG0464020                               HORVU.MOREX.r2.7HG0617130
                                                                HORVU.MOREX.r2.5HG0377220
                                                                                                    HORVU.MOREX.r2.5HG0414380



                                               Figure 5. miRNA¬–mRNA interaction network of HvOSCAs involving responses to abiotic stresses.
                                               The HvOSCAs are represented by the red diamonds, the predicted miRNAs by yellow ovals and the
                                               other interacting genes by blue dots.

                                               2.6. Validation of the Expression of HvOSCAs by qRT-PCR Assays
                                                     As OSCA genes function as hyperosmotic stress sensors, they play a vital part in
                                               abiotic stress response, hormone regulation and signaling transduction processes [25]. To
                                               identify the salt-responsive candidates, the expression profiles of all 13 HvOSCAs were
                                               systematically validated under drought, salt, cold and ABA treatments by qRT-PCR analysis
                                               (Table S11). Under 100 µM ABA treatment, HvOSCA2.1_1, HvOSCA2.1_2, HvOSCA2.4
                                               and HvOSCA3.1 showed up-regulated expression; in particular, the expression level of
                                               HvOSCA2.1_1 was significantly high. HvOSCA4.1 had gradually increased expression with
                                               the extension of treatment, and reached the peak at 24 h (h) after treatment. Moreover, the
                                               expressions of HvOSCA2.1_2, HvOSCA2.4 and HvOSCA3.1 were significantly up-regulated
                                               in the first 6 h, but decreased significantly as the treatment time continued, and finally
                                               were significantly lower compared to CK. Contrary to these results, the expressions of
                                               HvOSCA1.1, HvOSCA1.4 and HvOSCA2.2 displayed a continued decreasing trend, and
                                               reached the lowest levels at 24 h.
                                                     Under cold treatment, HvOSCA1.1, HvOSCA2.1_1, HvOSCA2.1_2, HvOSCA2.2, HvOSCA3.1
                                               and HvOSCA4.1 were found to exhibit a remarkably higher expression level in the first
                                               6 h and then decreased at 12 h after treatment. The expression level of HvOSCA1.3_2 was
                                               gradually increased with the duration of treatment, and reached the peak at 12 h, and then
                                               decreased at 24 h. The expression of HvOSCA1.4 showed no significant difference in the
                                               first 6 h of treatment, and then decreased significantly at 12 h, and finally increased sharply
                                               at 24 h. These results were consistent with the trends found by RNA-seq data and the
                                               differential expressed genes provided the candidates associated with the cold response.
                                                     Under 20% PEG-6000 treatment, these HvOSCAs showed completely diverse expres-
                                               sion patterns. The expressions of HvOSCA1.1 and HvOSCA1.4 showed consistence with
                                               that of CK at 6 h of drought treatment, and increased rapidly to reach the highest level
                                               at 12 h. Then, HvOSCA1.1 maintained a high expression at 24 h of treatment, while
Int. J. Mol. Sci. 2022, 23, 13027                                                                                                                                                                                                                          9 of 18




                                                                              HvOSCA1.4 decreased remarkably at 24 h. HvOSCA1.3_2 displayed the highest expression
                                                                              level at 6 h, and then decreased gradually during the drought treatment. At the same
                                                                              time, HvOSCA2.1_1, HvOSCA2.2 and HvOSCA4.1 showed similar expression patterns that
                                                                              were significantly down-regulated at 6 h and 12 h of treatment, and then up-regulated at
                                                                              24 h. HvOSCA2.1_2 seemed to function as a negative regulator of the drought response
                                                                              and displayed significantly down-regulated expression at 12 h. Finally, the expression
                                                                              levels of HvOSCA2.4 and HvOSCA3.1 increased at 6 h, then decreased sharply at 12 h, but
                                                                              increased significantly to the highest level at 24 h. The different expression patterns of these
                                                                              HvOSCAs suggest their divergent regulatory roles in drought response and tolerance.
                                                                                    Under salt stress treatment, these HvOSCAs also showed obviously different expres-
                                                                              sion patterns. HvOSCA2.1_2 displayed the up-regulated expression all the time with a
                                                                              high expression level, while HvOSCA2.2 and HvOSCA4.1 showed down-regulated expres-
                                                                              sions at all time courses, suggesting that these might function in differential stages of
                                                                              salt stress. HvOSCA3.1 and HvOSCA2.4 were up-regulated at both 6 h and 12 h, while
                                                                              down-regulated at 24 h. The expression levels of HvOSCA1.1 and HvOSCA1.4 was the
                                                                              highest at 6 h, then decreased sharply at 12 h, but increased a little at 24 h. HvOSCA1.3_2
                                                                              showed no differential expression with CK at 6 h, but was up-regulated at 12 h and then
                                                                              down-regulated at 24 h. The expression of HvOSCA2.1_1 decreased rapidly after salt
                                                                              treatment, and reached the lowest expression at 6 h, then increased steadily to the highest
                                                                              level at 24 h. The results provided some clues on their divergent function on salt response
                                                                              and tolerance. Interestingly, the expressions of HvOSCA1.2, HvOSCA1.3_1, HvOSCA2.3
                                                                              and HvOSCA3.1 had extremely low or seldom expression under all stress conditions, which
                                                                              was also demonstrated by RNA-seq analysis, indicating they might not function in the
                                                                              stress response (Figure 6, Table S12).
                                                                      HvOSCA1.1                                                              HvOSCA1.3_2                                                           HvOSCA1.4
                                                                                          a                                                              a                   a        4                                            a
                                                                                      a                       2.5                                                                                                                  a
                                                Moc                                       a                                                  a           a                   a
                                                                  a                   a
                                                06h                                                                                          a
                 Relative abundance




                                                12h
                                                                  a                               a                                                                                                                                            a
                                                                                                              2.0                                            b                        3                                                        a
                                                24h                                               a
                                        2                                                                                                                    b
                                                                                                                                         b       b
                                                                                                                                 a
                                                                                                              1.5      ab                b       b               c
                                                                                                                                 a                                       b
                                                                                                          b
                                                 a                                                                  bc ab            c               c           c   b           b    2
                                            a                 b               b               b           b               c                                              b
                                                 a                    b                                             bc               c               c               b           b             a
                                            a                 b               b   b           b                           c                                                                a                               b               b           b
                                                                      b                                       1.0                                                                              a           a   a                                       b
                                        1             b                           b                                                                                                        a               a   a           b               b
                                                          b                                                                                                                                                                            b
                                                      b                                                                                                                                                                b       b
                                                          b                                           c                                                                               1                                b               b           c
                                                                          c                                   0.5                                                                                                              b                   c
                                                                                                      c                                                                                                            c
                                                                          c                                                                                                                            b           c
                                                                                                                                                                                                   b
                                                                                                                                                                                                   b   b
                                        0                                                                     0.0                                                                     0
                                                 ABA              Cold            PEG             Salt                  ABA              Cold            PEG             Salt                  ABA             Cold            PEG             Salt

                                                                      HvOSCA2.1_1                                                            HvOSCA2.1_2                                                           HvOSCA2.2
                                                                  a                                           2.0                        a                                                                     a
                                                      a           a   a                                                                                                      a   a   2.0
                                                                                                                        a
                                                                      a                                                                  a                                                                     a
                                        3             a
                                                                                                                        a                                                a   a   a
                                                 b
                   Relative abundance




                                                 b        b                                                                                                              a
                                                                                                          a   1.5                                                                    1.5
                                                          b
                                                                                                          a         b                b       b   b   a   a       a   b
                                                                                                                                                                                           a   a           b               a               a
                                                                          b                                                 bc
                                        2                                 b                                         b            c   b       b   b   a   a       a   b                         a
                                                                                                                                                             b                             a               b               a               a
                                                                                                                            bc
                                                                                                              1.0                c                                                   1.0               b                               b
                                                                                                      b                                                                                            b               c
                                                                                                                                                             b
                                            c                 c               a               b       b                                                                                                b                               b
                                                                                          a                                                                                                        b               c           c   c
                                            c                 c               a               b                                                                                                                                                        b
                                        1                                                 a                                                                                                                                                    c
                                                                                  b               c                                                                                                                            c                   c
                                                                                      b                       0.5                                                                    0.5                               d           c                   b
                                                                                  b               c                                                                                                                                            c
                                                                                      b                                                                                                                                                            c
                                                                                                                                                                                                                       d


                                        0                                                                     0.0                                                                    0.0
                                                 ABA              Cold            PEG             Salt                  ABA              Cold            PEG             Salt                  ABA             Cold            PEG             Salt

                                                                      HvOSCA2.4                                                              HvOSCA3.1                                                             HvOSCA4.1
                                                                                                      a                                                                      a                                 a
                                                                                                      a                                                                      a        4                        a
                                                                                                               5
                                        3

                                                                                                               4                                                                      3
                  Relative abundance




                                                                                          a
                                                 a                                b                                                      a
                                        2                                             c   a       b                                      a                                       b
                                                 a                                b                            3                                                                 b
                                                                                      c           b
                                                                                                          c             a                                                             2                a
                                                                                                                        a                                                                              a                               a
                                            b                 a   a           d               c           c                                      b
                                                                          a                                    2                                 b                                           bc b                  b                   a            a
                                            b         c bc    a   a   b   a   d               c                                                          a       a       c                 c bc b          b       b       ab              a
                                                                                                                                                                                                                                                 ab a
                                        1             c bc            b                                                                      c           a       a       c                 c               b               ab b    b       a
                                                                                                                    b                c       c       b               d                1                                       b    b           b ab
                                                                                                                    b            c   c               b       c       d                                                                         b
                                                                                                               1            d    c                           c                                                         c
                                                                                                                            d                                                                                          c


                                        0                                                                      0                                                                      0
                                                 ABA              Cold            PEG             Salt                  ABA              Cold            PEG             Salt                  ABA             Cold            PEG             Salt



                                                                              Figure 6. Validation of the expression signature of nine HvOSCA genes under ABA (100 µM ABA),
                                                                              cold (4 ◦ C), drought (20% PEG-6000) and salt (NaCl) treatment through the qRT-PCR method. The
                                                                              treatments were conducted with 100 µM ABA solution for ABA, 4 ◦ C for cold, 20% PEG 6000 solution
                                                                              for drought, and 150 mM NaCl solution for salt stresses, respectively. Data represent the average of
                                                                              three technical replications and the error bar represents the standard error of mean (SEM).
Int. J. Mol. Sci. 2022, 23, 13027                                                                                             10 of 18




                                    2.7. Genetic Variations and Haplotype Analysis of HvOSCA
                                         The genetic variations of these HvOSCA genes were investigated based on the rese-
                                    quencing data of wild barley and cultivated barley populations, including 85 wild and
                                    135 landrace accessions. A total of 2077 SNP loci were found in the 13 HvOSCAs and
                                    then were used to calculate the population divergence (Fst) and nucleotide diversity (π)
                                    values. The current study results found that the Fst value of them ranged from 0 to 0.808825.
                                    According to a previous study, the Fst value of a gene exceeds the threshold line (Fst = 0.456)
                                    was considered as an artificially selected gene. Among these 13 HvOSCAs, HvOSCA1.3_1,
                                    HvOSCA2.2 and HvOSCA1.1, as well as HvOSCA2.2, were under artificial selection during
                                    barley domestication (Figure 7A, Table S13).




                                    Figure 7. Genetic variations and haplotype analysis of HvOSCAs based on resequencing data. (A) Ge-
                                    netic divergence and artificial selection analysis of HvOSCAs; (B) nucleotide diversity of HvOSCA
                                    genes in landrace and wild barley populations; (C) haplotype frequency analysis of HvOSCAs in
                                    landrace and wild barley populations.

                                         Furthermore, the genetic diversity of HvOSCAs in the wild barley population was
                                    0.4966 × 10−3 , while that of landrace population was 0.391 × 10−3 (Figure 7B, Table S14).
                                    Compared to wild barley, the cultivated barley had relatively lower genetic diversity,
                                    suggesting that genetic bottleneck had occurred on the barley OSCA family during the
                                    barley evolution process. Further, the current study observed that the haplotype frequencies
                                    of the HvOSCAs were investigated based on the SNP variations. Results found only four
                                    genes showed different haplotype frequencies between wild and cultivated barley, and all
                                    of them displayed more haplotypes in wild barley than that of cultivated barley, which
                                    also demonstrated the genetic bottleneck effect on the OSCA family when wild barley
                                    domesticated to a landrace (Figure 7C, Table S15).
Int. J. Mol. Sci. 2022, 23, 13027                                                                                           11 of 18




                                    2.8. Subcellular Localization of HvOSCA1.1, HvOSCA 2.4, HvOSCA3.1 and HvOSCA 4.1
                                         In order to validate the subcellular localization of HvOSCA proteins, four HvOSCAs
                                    genes, including HvOSCA1.1, HvOSCA2.4, HvOSCA3.1 and HvOSCA4.1 were cloned from
                                    the barley cv. Morex to construct their corresponding transient vectors, and then separately
                                    injected into tobacco leaf cells to track the localization of the HvOSCA proteins through laser
                                    confocal microscopy. As shown in Figure 8, all four proteins were expressed as HvOSCA-
                                    GFP fusion protein in transformed tobacco leaf cells, and they were mainly localized in
                                    the inner-membrane.
                                                         GFP                  Bright Field              Merged




                                    HvOSCA1.1




                                    HvOSCA2.4




                                    HvOSCA3.1




                                    HvOSCA4.1




                                    Figure 8. Subcellular localization of four recombinant CaMV35S: HvOSCA-GFP HvOSCA protein
                                    fusions transiently expressed in tobacco leaf cells.

                                    3. Discussion
                                         Plants inevitably undergo changing environments including adverse abiotic environ-
                                    ments, such as a drought, soil salinity and extreme temperatures, throughout their life cycle,
                                    and they have evolved interconnected regulatory pathways in response to the exogenous
                                    and endogenous osmotic changes [3]. Barley ranked as the fourth most important cereal
                                    crop worldwide [32], which is widely distributed from the vicinity of Dead Sea in the
                                    Middle East where H. vulgare originated, to the high altitude areas of the Qinghai-Tibet
                                    plateau [33]. Barley has a wide range of adaptability and can withstand harsh environ-
                                    ments [34]. Extensive studies have demonstrated that barely is one of the most stress
Int. J. Mol. Sci. 2022, 23, 13027                                                                                         12 of 18




                                    tolerant staple crops all over the world with the excellent salt tolerance, drought and low
                                    temperature resistance, as well as adaptation to soil infertility, providing a gene pool for
                                    genetic improvement and breeding of stress tolerant crops. Therefore, mining elite genes
                                    underlying stress tolerance in barley will provide a useful gene resource for stress-oriented
                                    genetic improvement and breeding. The OSCA family acts as an osmosensor, playing
                                    a crucial role in the sensing of osmotic stresses and regulating osmotic adjustment in
                                    plants [25,30]. In view of its importance, the OSCA family has been systematically iden-
                                    tified in several species, including A. thaliana, rice, maize and wheat, but not so far in
                                    barely. In this study, 13 HvOSCA genes were identified at genome level in barley. Based on
                                    phylogenetic analysis, these HvOSCAs could be clustered into four clades, and the members
                                    clustered in the same clade possessed the detected similar conserved motif composition,
                                    exon-intron structures and cis-element organizations, suggesting that they had similar
                                    function, which is consistent with previous studies [20]. Domains of the late exocytosis
                                    TM putative phosphate transporter and calcium-dependent channel of OSCA genes were
                                    found to be extremely conserved in higher plants [25]. All HvOSCA genes identified herein
                                    contained these three functional domains, further supporting the high conservation of the
                                    OSCA family and also demonstrating the accuracy of our prediction.
                                          The expression pattern is the external embodiment of gene function, and gene expres-
                                    sion is largely regulated by the cis-elements in the promoter region [35]. Cis-regulatory
                                    elements play an essential role in a gene’s spatio-temporal expression, and then in reg-
                                    ulating plant growth, development, morphogenesis, senescence, apoptosis, as well as
                                    in coordination and adaptation to the environment [36]. The current study found that
                                    HvOSCAs harbored various cis-elements related to growth, hormone responsiveness and
                                    also stress responsiveness. Combined with the expression profiles of HvOSCAs from RNA-
                                    seq and qRT-PCR analysis, the current study found that the cis-elements could regulate
                                    the expressional specificity of some HvOSCAs. For example, HvOSCA1.3_2, harboring five
                                    MBS cis-elements that are regulatory elements serving as a MYB binding site involved
                                    in drought inducibility, showed a quick response under PEG-induced drought treatment.
                                    HvOSCA1.2_2 showed rapid up-regulation expression under ABA treatment and main-
                                    tained at a high expression level, which contained seven CGTCA-motif elements that
                                    involved in the MeJA responsiveness. The current study further reconstructed the co-
                                    expression network by the WGCNA method based on public RNA-seq data, and further
                                    investigated the correlations between seven modules and simulated abiotic stress treat-
                                    ment including cold, NaCl and heavy metal ion (cadmium, copper and zipper) treatment.
                                    Results showed that seven modules were significantly associated with stress treatment. All
                                    modules harbored the HvOSCA genes as the hub factors. Furthermore, prediction results
                                    of miRNA regulating OSCA genes in seven modules showed that thirteen microRNAs
                                    were found to target eight HvOSCA genes involved in the stress-related modules, including
                                    Hvu-miR5049f, Hvu-miR6195, Hvu-miR6196 and Hvu-miR156a. Previous studies have been
                                    reported that Hvu-miR5049f could respond to drought stress in Tibetan wild barley [37],
                                    Hvu-miR6195 and Hvu-miR6196 were detected in rice root under salt treatment [38], and the
                                    expression of Hvu-miR156a was modulated by barley leaf stripe (BLS) in Tibetan barley [39].
                                    We postulated that these four miRNAs might play a regulatory role in the response to stress
                                    by controlling the expression of OSCA genes in barley.
                                          In previous studies, different OSCA members mainly functioned as stress responsive
                                    proteins in dehydration stress or acted as hyperosmolality sensors, and also played the
                                    role of a switch to control the influx of Ca2+ in the pathway of immune signal transduc-
                                    tion [20,25–27,40]. The present study found that HvOSCA2.1_1 was significantly induced
                                    by ABA and cold, but was inhibited by drought and salt treatment during the initial 12 h,
                                    while there was little change in expression of HvOSCA4.1 under ABA, PEG, salt and cold
                                    (except 6 h) treatment compared with control. HvOSCA2.2 was significantly inhibited
                                    by drought, salt and ABA, but markedly induced by cold in the initial 6 h. Among the
                                    cis-elements of HvOSCA genes, the number of hormone-responsive and stress-responsive
Int. J. Mol. Sci. 2022, 23, 13027                                                                                           13 of 18




                                    elements were more than that of growth and metabolic-responsive elements, signifying
                                    that HvOSCAs mainly functioned in stress response and signal transduction.
                                         Population genomic research has provided a crucial approach for the investigation of
                                    genetic divergence, domestication and evolution, as well as the genetic basis for the trait in
                                    plant populations [41–44].
                                         The current study evaluated the genetic variations of the HvOSCA family in wild barley
                                    and landrace populations. Fst values among different populations indicated that artificial
                                    selection had occurred in barley OSCA genes at different degrees between members of four
                                    identified HvOSCAs . The results showed that wild barley possessed higher nucleotide
                                    diversity and alternative haplotypes compared to landrace populations, which suggested
                                    that genetic bottleneck had occurred within this family during barley domestication. These
                                    results suggested that barley domestication occurred from the perspectives of the OSCA
                                    family, and are promising enrich the genetic diversity for barley breeding against abiotic
                                    stress resistance.
                                         Generally, the subcellular localization helps to decipher its cellular function. Previ-
                                    ous studies have reported that OSCA proteins were localized in the cell membrane in
                                    other plants [18,45]. In the current study, both the in silico prediction and the subcellular
                                    localization results indicated that the HvOSCA family members are localized in the inner-
                                    membrane. The results in the current study testified the previous conclusions and provided
                                    useful information for further functional studies of HvOSCAs.

                                    4. Materials and Methods
                                    4.1. Identification of OSCA Genes in Barley
                                         For the identification of the OSCA gene family in barley, the protein sequences of the
                                    barley genome were retrieved from the Ensembl plant database (http://plants.ensembl.org/
                                    Hordeum_vulgare/Info/Index, accessed on 10 January 2022). The Hidden Markov Model
                                    (HMM) profile of homeodomain (HD) (DUF221) (renamed from DUF221 to RSN1_7TM
                                    (PF02714) was used as a query to search against the local protein database using the
                                    HMM3.0 tool with the E-value ≤ 1 × 10−10 as the threshold. Furthermore, 15 AtOSCAs
                                    and 11 OsOSCAs protein sequences were used to perform a BLASTP search against the
                                    local protein database with the threshold of E-value < 1 × 10−5 . Subsequently, the results
                                    of the HMMER and BLASTP searches were integrated together, and the redundants were
                                    manually removed to obtain the putative barley OSCA proteins. These data were submitted
                                    to the Conserved Domain Database (CDD) (https://www.ncbi.nlm.nih.gov/cdd, accessed
                                    on 10 January 2022), the Simple Modular Architecture Research Tool (SMART) (http:
                                    //smart.embl-heidelberg.de/, accessed on 5 February 2022) and PFAM (https://pfam.
                                    xfam.org, accessed on 1 March 2022) to further confirm their OSCA conserved domain;
                                    those with a complete OSCA domain remained as candidates. Finally, the candidates
                                    were submitted to the ExPASy (http://web.expasy.org/protparam/, accessed on 1 March
                                    2022) database to investigate the physicochemical properties such as molecular weight
                                    (Mw), isoelectric point (pI), instability index (II), aliphatic index (AI) and grand average of
                                    hydrophobicity (GRAVY). The subcellular localization of them was predicted by the online
                                    CELLO tool (v2.5) (http://cello.life.nctu.edu.tw/, accessed on 1 March 2022).

                                    4.2. Phylogenetic Relationships, Genic Structure, Conserved Motif and Cis-Element Analysis
                                         The protein sequences of the identified barley and previously reported AtOSCAs,
                                    ZmOSCAs, OsOSCAs and TaOSCAs were employed to construct the phylogenetic tree.
                                    Multiple sequence alignment was performed using Phylip software [46] and the MEGA-X
                                    tool was used for a phylogenetic tree constructed by the neighbor-joining (NJ) method with
                                    the bootstrap of 1000 replications. The chromosome location and exon-intron structures
                                    of these HvOSCA genes were retrieved according to the genome annotation files (http:
                                    //plants. ensembl.org/Hordeum_vulgare/Info/Index, accessed on 10 January 2022) and
                                    then were visualized using MapGene2Chromosome v2.0 (http://mg2c.iask.in/mg2c_v2.0/,
                                    accessed on 1 March 2022) and Gene Structure Display Server (GSDS2.0) (http://gsds.cbi.
Int. J. Mol. Sci. 2022, 23, 13027                                                                                            14 of 18




                                    pku.edu.cn/, accessed on 1 March 2022), respectively. The conserved protein motifs were
                                    predicted based on online MEME tools (http://alternate.meme-suite.org/, accessed on 1
                                    March 2022) with the following parameters: the maximum number of motifs was set to 10,
                                    any number of repetitions was allowed, and the optimum width ranged from 6 to 250.

                                    4.3. Cis-Element Analysis
                                         The 2.0 kb genomic sequences upstream of the transcription start site of HvOSCAs were
                                    extracted from the barley reference sequence by in-home Perl script and submitted to the Plant-
                                    CARE database (http://bioinformatics.psb.ugent.be/webtools/plantcare/html/, accessed on
                                    12 March 2022) to predict the supposed cis-acting transcriptional regulatory elements.

                                    4.4. Expression Profile Analysis of HvOSCAs Based on RNA-seq Data
                                         A total of 142 RNA-seq data from the samples of different tissues at different de-
                                    velopment stages (including embryos, bracts, epidermis, young inflorescences, lemma,
                                    lodicule, shoot, rachis, developing tillers, palea, roots and leaves) and under diverse biotic
                                    and abiotic stresses (including drought, salinity, cold and ABA treatment) were down-
                                    loaded from the NCBI Sequence Reading Archive (SRA) database (Table S6). The HISAT2
                                    (v2.1.0) [47] and StringTie (v1.3.5) pipeline [48] were used to calculate the value of frag-
                                    ments per kilobase per million (FPKM). The expression profiles of HvOSCAs were retrieved
                                    and visualized with heat maps by using the pheatmap package in R software.

                                    4.5. Co-Expression Network Analysis of HvOSCAs under Stressed Conditions
                                          The R package WGCNA (V1.71, R 4.2) [49] was employed to conduct co-expression
                                    analysis based on the FPKM values matrix from various stresses with the default parameters
                                    except soft power = 8, min_module_size = 30, ME_miss_thread = 0.2. The FPKM values
                                    matrix of cold, NaCl and heavy metal ion (cadmium, copper and zipper) treatment were
                                    used for correlation analysis, and visualization was done by the ggcor package (V0.9.8.1).
                                    Thirteen HvOSCAs protein sequences were used as queries to predict the miRNA binding
                                    sites by using published miRNAs of barley in the psRNATarget database (https://www.
                                    zhaolab.org/psRNATarget/analysis?function=2, accessed on 18 May 2022) with the default
                                    parameters. The software Cytoscape v3.9.1 [50] was employed to visualize the regulatory
                                    network with miRNA of HvOSCAs.

                                    4.6. Plant Materials Preparation, Stress Treatment and qRT-PCR Analysis
                                          The seeds of barley cv. Morex, which is stored by the Wheat Genomics Lab in
                                    Northwest A&F University (Central Shaanxi Province, China; 34 260 N latitude, 108 070
                                    E longitude, altitude: 458 m), were sterilized by 5% (w/v) sodium hypochlorite (NaClO)
                                    (Xinyicheng, Shaanxi, China) for 5 min, and then rinsed using distilled water for 3 min, and
                                    finally incubated on wet filter paper in a petri dish at 25 ◦ C for 5 days [51]. This experiment
                                    was conducted from 10 to 30 March 2022 in NWSUAF. When the seedlings had grown
                                    to 4–5 cm, they were transplanted to hydroponic colonization plates, and put in culture
                                    medium (aqueous solution with 1/2 Hogeland nutrient) to reach the trifoliate leaf stage
                                    in a growth chamber under 20 ◦ C /15 ◦ C day/night, 16 h light/8 h dark cycle, and 50%
                                    relative humidity. Hydraulically cultured trifoliate leaf stage seedlings were exposed to
                                    culture medium, adding 150 mM NaCl, 20% PEG, 4 ◦ C, or 100 µM ABA, and the roots and
                                    leaves were sampled at 0, 6 h, 12 h and 24 h as the stressed treatments [51,52]. The seedlings
                                    grown in the culture medium without any treatment were sampled simultaneously at
                                    the corresponding time point as the control. All the samples were collected from at least
                                    three replicates, frozen by liquid nitrogen immediately and then stored at −80 ◦ C. Total
                                    RNA was extracted by Plant RNA Kit reagent (Omega BioTek, Norcross, GA, USA), then
                                    synthesis cDNA by 5× All-in-one RT MasterMix (ABM,Vancouver, Canada) following the
                                    manufacturer’s protocols. The HvACTIN (HORVU.MOREX.r2.5HG0378970) was used as
                                    the reference gene. The relative expression of HvOSCAs was quantified using the TB-Green
                                    ® Premix Ex Taq™ II kit (Takara, Dalian, China) and ABI7500 Real-Time PCR Systems
Int. J. Mol. Sci. 2022, 23, 13027                                                                                                15 of 18




                                    (Applied Biosystems, Foster City, CA, USA). The qRT-PCR thermal cycling condition as
                                    follows: 95 ◦ C for 30 s, followed by 40 cycles of 15 s at 95 ◦ C, and 30 s at 60 ◦ C. The 2−∆∆CT
                                    quantification method was used for calculating the relative expression level [52,53]. Three
                                    parallel technical replicates were set for each sample. The primers used in the current study
                                    are listed in Table S11.

                                    4.7. Genetic Variations and Haplotype Analysis of HvOSCAs
                                         The resequencing data of 220 genotypes of barley (including 135 landraces and 85 wild
                                    barley) were obtained by an exome-captured approach from the NCBI SRA database
                                    (PRJEB8044/ERP009079), producing a visual component framework (VCF) file [43,52]. The
                                    SNPs of OSCA genes subsets were retrieved from the VCF file. The fixation index (Fst) was
                                    analyzed by vcftools v0.1.16 with the parameters as window = 100, step = 1, and visualized
                                    by R package CMplot. The nucleotide diversity (π) was also calculated by using vcftools
                                    v0.1.16, and visualized by R package ggsci. The variant of all HvOSCAs were annotated by
                                    snpEff software, the intro-variants were filtered, and the protein-coding variants were used
                                    for haplotype analysis by in-home python scripts [54], and visualized by R packages ggsci
                                    and scales.

                                    4.8. Subcellular Localization of HvOSCA-GFP Fusion Proteins
                                          One HvOSCA member from each clade based on phylogenetic relationships (HvOSCA1.1,
                                    HvOSCA 2.4, HvOSCA3.1 and HvOSCA4.1) was randomly selected for amplification using
                                    the primers listed in Table S11. The PCR products were separately recovered and cloned
                                    into the multiple cloning sites of NdeI and SacI in the pBI121-GFP vector. Each recombinant
                                    vector was separately transformed into Agrobacterium tumefaciens strain GV3101 prepared
                                    for agro-infiltration. For transient expression of HvOSCAs in tobacco, the Agrobacterium
                                    strains harboring the recombined vector were injected into 4-week-old tobacco leaves. Then,
                                    the images of the leaves were captured after 48 h of agro-infiltration by a laser confocal
                                    microscope (Olympus, Tokyo, Japan).

                                    5. Conclusions
                                          The current study identified and characterized a new OSCA gene family in barley with
                                    13 HvOSCAs belonging to 4 clades. The exon-intron structures analysis found that they
                                    displayed highly variable intron numbers ranging from 0 to 11. Expression profiles and
                                    qRT-PCR validation found that these HvOSCAs were significantly induced by drought, cold,
                                    salt and phytohormone ABA treatment, demonstrating their function in stress response.
                                    Finally, genetic variations and haplotype analysis indicated that artificial selection was
                                    conserved on the OSCA family during wild barley domestication to the barley landrace.
                                    This study not only paves the way for further elucidating the function of HvOSCAs on
                                    stress response and tolerance but also provides a potential gene resource for breeding
                                    studies on stress tolerance in barely and other crops.

                                    Supplementary Materials: The following supporting information can be downloaded at: https:
                                    //www.mdpi.com/article/10.3390/ijms232113027/s1.
                                    Author Contributions: Conceptualization, K.S. and W.S.; formal analysis, K.S.; funding acquisition,
                                    W.S.; investigation, K.S., W.P., T.S. and Y.C. (Yue Cheng); project administration, W.S.; resources,
                                    W.S.; validation, K.S., T.S., W.P., Y.C. (Yingqi Chu) and Y.Y.; visualization, K.S and W.P. and B.M.;
                                    writing—original draft, K.S.; writing-review and editing, K.S and W.S. All authors have read and
                                    agreed to the published version of the manuscript.
                                    Funding: This research was funded by the Programmer of Introduction Talents of Innovative Disci-
                                    pline to Universities (Project 111) from the State Administration of Foreign Experts Affairs, China
                                    (Grant No. #B18042), and partially supported by the Key Research and Development Program of
                                    Shaanxi Province, China (Grant Nos. CSBAA202202 and CSBAA202203).
                                    Institutional Review Board Statement: Not applicable.
Int. J. Mol. Sci. 2022, 23, 13027                                                                                                         16 of 18




                                    Informed Consent Statement: Not applicable.
                                    Data Availability Statement: All of the datasets supporting the results of this article are included
                                    within the article and its additional files.
                                    Acknowledgments: We appreciate Jun’an Yan and Guang Yang for their help in chart drawing and
                                    reading through the earlier manuscript and giving constructive advices, and we are grateful to the High-
                                    Performance Computing Center of Northwest A&F University for providing computational resources.
                                    Conflicts of Interest: All authors declare no conflict of interest.

References
1.    Braam, J. In touch: Plant responses to mechanical stimuli. New Phytol. 2005, 165, 373–389. [CrossRef]
2.    Scheres, B.; van der Putten, W.H. The plant perceptron connects environment to development. Nature 2017, 543, 337–345.
      [CrossRef]
3.    Zhu, J.K. Abiotic Stress Signaling and Responses in Plants. Cell 2016, 167, 313–324. [CrossRef] [PubMed]
4.    Zhang, H.; Zhu, J.; Gong, Z.; Zhu, J.K. Abiotic stress responses in plants. Nat. Rev. Genet. 2022, 23, 104–119. [CrossRef] [PubMed]
5.    Feijó, J.A.; Wudick, M.M. ‘Calcium is life’. J. Exp. Bot. 2018, 69, 4147–4150. [CrossRef]
6.    Zhang, Y.; Lv, Y.; Jahan, N.; Chen, G.; Ren, D.; Guo, L. Sensing of Abiotic Stress and Ionic Stress Responses in Plants. Int. J. Mol.
      Sci. 2018, 19, 3298. [CrossRef] [PubMed]
7.    Sukharev, S.I.; Blount, P.; Martinac, B.; Kung, C. Mechanosensitive channels of Escherichia coli: The MscL gene, protein, and
      activities. Annu. Rev. Physiol. 1997, 59, 633–657. [CrossRef]
8.    Sachs, F. Mechanical transduction by ion channels: A cautionary tale. World J. Neurol. 2015, 5, 74. [CrossRef]
9.    Maingret, F.; Fosset, M.; Lesage, F.; Lazdunski, M.; Honoré, E. TRAAK Is a Mammalian Neuronal Mechano-gated K+Channel*. J.
      Biol. Chem. 1999, 274, 1381–1387. [CrossRef] [PubMed]
10.   Patel, A.; Sharif-Naeini, R.; Folgering, J.R.; Bichet, D.; Duprat, F.; Honoré, E. Canonical TRP channels and mechanotransduction:
      From physiology to disease states. Pflug. Arch. Eur. J. Physiol. 2010, 460, 571–581. [CrossRef]
11.   Coste, B.; Mathur, J.; Schmidt, M.; Earley, T.J.; Ranade, S.; Petrus, M.J.; Dubin, A.E.; Patapoutian, A. Piezo1 and Piezo2 are essential
      components of distinct mechanically activated cation channels. Science 2010, 330, 55–60. [CrossRef]
12.   Frietsch, S.; Wang, Y.-F.; Sladek, C.; Poulsen, L.R.; Romanowsky, S.M.; Schroeder, J.I.; Harper, J.F. A cyclic nucleotide-gated
      channel is essential for polarized tip growth of pollen. Proc. Natl. Acad. Sci. USA 2007, 104, 14531–14536. [CrossRef] [PubMed]
13.   Gao, Q.-F.; Fei, C.-F.; Dong, J.-Y.; Gu, L.-L.; Wang, Y.-F. Arabidopsis CNGC18 is a Ca2+ -permeable channel. Mol. Plant 2014, 7,
      739–743. [CrossRef] [PubMed]
14.   Gao, Q.-F.; Gu, L.-L.; Wang, H.-Q.; Fei, C.-F.; Fang, X.; Hussain, J.; Sun, S.-J.; Dong, J.-Y.; Liu, H.; Wang, Y.-F. Cyclic nucleotide-gated
      channel 18 is an essential Ca2+ channel in pollen tube tips for pollen tube guidance to ovules in Arabidopsis. Proc. Natl. Acad. Sci.
      USA 2016, 113, 3096–3101. [CrossRef] [PubMed]
15.   Chen, J.; Yin, H.; Gu, J.; Li, L.; Liu, Z.; Jiang, X.; Zhou, H.; Wei, S.; Zhang, S.; Wu, J. Genomic characterization, phylogenetic
      comparison and differential expression of the cyclic nucleotide-gated channels gene family in pear (Pyrus bretchneideri Rehd.).
      Genomics 2015, 105, 39–52. [CrossRef] [PubMed]
16.   Weiland, M.; Mancuso, S.; Baluska, F. Signalling via glutamate and GLRs in Arabidopsis thaliana. Funct. Plant Biol. 2015, 43, 1–25.
      [CrossRef] [PubMed]
17.   Michard, E.; Lima, P.T.; Borges, F.; Silva, A.C.; Portes, M.T.; Carvalho, J.E.; Gilliham, M.; Liu, L.-H.; Obermeyer, G.; Feijó, J.A.
      Glutamate receptor-like genes form Ca2+ channels in pollen tubes and are regulated by pistil D-serine. Science 2011, 332, 434–437.
      [CrossRef] [PubMed]
18.   Li, Y.; Yuan, F.; Wen, Z.; Li, Y.; Wang, F.; Zhu, T.; Zhuo, W.; Jin, X.; Wang, Y.; Zhao, H.; et al. Genome-wide survey and expression
      analysis of the OSCA gene family in rice. BMC Plant Biol 2015, 15, 261. [CrossRef] [PubMed]
19.   Tong, K.; Wu, X.; He, L.; Qiu, S.; Liu, S.; Cai, L.; Rao, S.; Chen, J. Genome-Wide Identification and Expression Profile of OSCA
      Gene Family Members in Triticum aestivum L. Int. J. Mol. Sci. 2022, 23, 469. [CrossRef] [PubMed]
20.   Ding, S.; Feng, X.; Du, H.; Wang, H. Genome-wide analysis of maize OSCA family members and their involvement in drought
      stress. PeerJ 2019, 7, e6765. [CrossRef] [PubMed]
21.   Cao, L.; Zhang, P.; Lu, X.; Wang, G.; Wang, Z.; Zhang, Q.; Zhang, X.; Wei, X.; Mei, F.; Wei, L.; et al. Systematic Analysis of
      the Maize OSCA Genes Revealing ZmOSCA Family Members Involved in Osmotic Stress and ZmOSCA2.4 Confers Enhanced
      Drought Tolerance in Transgenic Arabidopsis. Int. J. Mol. Sci. 2020, 21, 351. [CrossRef] [PubMed]
22.   Yin, L.; Zhang, M.; Wu, R.; Chen, X.; Liu, F.; Xing, B. Genome-wide analysis of OSCA gene family members in Vigna radiata and
      their involvement in the osmotic response. BMC Plant Biol 2021, 21, 408. [CrossRef] [PubMed]
23.   Yang, X.; Xu, Y.; Yang, F.; Magwanga, R.O.; Cai, X.; Wang, X.; Wang, Y.; Hou, Y.; Wang, K.; Liu, F.; et al. Genome-wide identification
      of OSCA gene family and their potential function in the regulation of dehydration and salt stress in Gossypium hirsutum. J.
      Cotton Res. 2019, 2, 1–18. [CrossRef]
24.   Thor, K.; Jiang, S.; Michard, E.; George, J.; Scherzer, S.; Huang, S.; Dindas, J.; Derbyshire, P.; Leitao, N.; DeFalco, T.A.; et al. The
      calcium-permeable channel OSCA1.3 regulates plant stomatal immunity. Nature 2020, 585, 569–573. [CrossRef]
Int. J. Mol. Sci. 2022, 23, 13027                                                                                                       17 of 18




25.   Yuan, F.; Yang, H.; Xue, Y.; Kong, D.; Ye, R.; Li, C.; Zhang, J.; Theprungsirikul, L.; Shrift, T.; Krichilsky, B.; et al. OSCA1 mediates
      osmotic-stress-evoked Ca2+ increases vital for osmosensing in Arabidopsis. Nature 2014, 514, 367–371. [CrossRef]
26.   Zhai, Y.; Wen, Z.; Han, Y.; Zhuo, W.; Wang, F.; Xi, C.; Liu, J.; Gao, P.; Zhao, H.; Wang, Y.; et al. Heterogeneous expression of
      plasma-membrane-localised OsOSCA1.4 complements osmotic sensing based on hyperosmolality and salt stress in Arabidopsis
      osca1 mutant. Cell Calcium 2020, 91, 102261. [CrossRef]
27.   Zhai, Y.; Wen, Z.; Fang, W.; Wang, Y.; Xi, C.; Liu, J.; Zhao, H.; Wang, Y.; Han, S. Functional analysis of rice OSCA genes
      overexpressed in the arabidopsis osca1 mutant due to drought and salt stresses. Transgenic Res. 2021, 30, 811–820. [CrossRef]
28.   Kirschner, G.K.; Rosignoli, S.; Guo, L.; Vardanega, I.; Imani, J.; Altmüller, J.; Milner, S.G.; Balzano, R.; Nagel, K.A.; Pflugfelder, D.;
      et al. ENHANCED GRAVITROPISM 2 encodes a STERILE ALPHA MOTIF—containing protein that controls root growth angle
      in barley and wheat. Proc. Natl. Acad. Sci. USA 2021, 118, e2101526118. [CrossRef]
29.   Zhu, J.; Zhang, B.; Smith, E.N.; Drees, B.; Brem, R.B.; Kruglyak, L.; Bumgarner, R.E.; Schadt, E.E. Integrating large-scale functional
      genomic data to dissect the complexity of yeast regulatory networks. Nat. Genet. 2008, 40, 854–861. [CrossRef]
30.   Hou, C.; Tian, W.; Kleist, T.; He, K.; Garcia, V.; Bai, F.; Hao, Y.; Luan, S.; Li, L. DUF221 proteins are a family of osmosensitive
      calcium-permeable cation channels conserved across eukaryotes. Cell Res. 2014, 24, 632–635. [CrossRef]
31.   Xu, G.; Guo, C.; Shan, H.; Kong, H. Divergence of duplicate genes in exon-intron structure. Proc. Natl. Acad. Sci. USA 2012, 109,
      1187–1192. [CrossRef] [PubMed]
32.   Newton, A.C.; Flavell, A.J.; George, T.S.; Leat, P.; Mullholland, B.; Ramsay, L.; Revoredo-Giha, C.; Russell, J.; Steffenson, B.J.;
      Swanston, J.S.; et al. Crops that feed the world 4. Barley: A resilient crop? Strengths and weaknesses in the context of food
      security. Food Secur. 2011, 3, 141–178. [CrossRef]
33.   Aldughpassi, A.; Wolever, T.M.S.; Abdel-Aal, E.S.M. Barley Food and Product. In Encyclopedia of Food and Health; Elsevier Ltd.:
      Alpharetta, GA, USA, 2016; pp. 328–331.
34.   Kumar, A.; Verma, R.P.S.; Singh, A.; Kumar Sharma, H.; Devi, G. “Barley landraces: Ecological heritage for edaphic stress
      adaptations and sustainable production”. Environ. Sustain. Indic. 2020, 6, 100035. [CrossRef]
35.   Biłas, R.; Szafran, K.; Hnatuszko-Konka, K.; Kononowicz, A.K. Cis-regulatory elements used to control gene expression in plants.
      Plant Cell Tissue Organ Cult. 2016, 127, 269–287. [CrossRef]
36.   Priest, H.D.; Filichkin, S.A.; Mockler, T.C. cis-Regulatory elements in plant cell signaling. Curr. Opin. Plant Biol. 2009, 12, 643–649.
      [CrossRef] [PubMed]
37.   Qiu, C.-W.; Zhao, J.; Chen, Q.; Wu, F. Genome-wide characterization of drought stress responsive long non-coding RNAs in
      Tibetan wild barley. Environ. Exp. Bot. 2019, 164, 124–134. [CrossRef]
38.   Huang, X.; Jiejie, F.; Wang, R.; Zhang, H.; Huang, J. Comparative analysis of microRNAs and their targets in the roots of two
      cultivars with contrasting salt tolerance in rice (Oryza sativa L.). Plant Growth Regul. 2019, 87, 139–148. [CrossRef]
39.   Yao, X.; Wang, Y.; Yao, Y.; Bai, Y.; Wu, K.; Qiao, Y. Identification microRNAs and target genes in Tibetan hulless barley to BLS
      infection. Agron. J. 2021, 113, 2273–2292. [CrossRef]
40.   Maity, K.; Heumann, J.M.; McGrath, A.P.; Kopcho, N.J.; Hsu, P.K.; Lee, C.W.; Mapes, J.H.; Garza, D.; Krishnan, S.; Morgan, G.P.;
      et al. Cryo-EM structure of OSCA1.2 from Oryza sativa elucidates the mechanical basis of potential membrane hyperosmolality
      gating. Proc. Natl. Acad. Sci. USA 2019, 116, 14309–14318. [CrossRef]
41.   Mascher, M.; Richmond, T.A.; Gerhardt, D.J.; Himmelbach, A.; Clissold, L.; Sampath, D.; Ayling, S.; Steuernagel, B.; Pfeifer, M.;
      D’Ascenzo, M.; et al. Barley whole exome capture: A tool for genomic research in the genus Hordeum and beyond. Plant J. Cell
      Mol. Biol. 2013, 76, 494–505. [CrossRef]
42.   Pankin, A.; Altmüller, J.; Becker, C.; von Korff, M. Targeted resequencing reveals genomic signatures of barley domestication.
      New Phytol. 2018, 218, 1247–1259. [CrossRef] [PubMed]
43.   Russell, J.; Mascher, M.; Dawson, I.K.; Kyriakidis, S.; Calixto, C.; Freund, F.; Bayer, M.; Milne, I.; Marshall-Griffiths, T.; Heinen,
      S.; et al. Exome sequencing of geographically diverse barley landraces and wild relatives gives insights into environmental
      adaptation. Nat. Genet. 2016, 48, 1024–1030. [CrossRef] [PubMed]
44.   Zeng, X.; Guo, Y.; Xu, Q.; Mascher, M.; Guo, G.; Li, S.; Mao, L.; Liu, Q.; Xia, Z.; Zhou, J.; et al. Origin and evolution of qingke
      barley in Tibet. Nat. Commun. 2018, 9, 5433. [CrossRef] [PubMed]
45.   Miao, S.; Li, F.; Han, Y.; Yao, Z.; Xu, Z.; Chen, X.; Liu, J.; Zhang, Y.; Wang, A. Identification of OSCA gene family in Solanum
      habrochaites and its function analysis under stress. BMC Genom. 2022, 23, 547. [CrossRef] [PubMed]
46.   Retief, J.D. Phylogenetic Analysis Using PHYLIP. In Bioinformatics Methods and Protocols; Misener, S., Krawetz, S.A., Eds.; Humana
      Press: Totowa, NJ, USA, 1999; pp. 243–258.
47.   Kim, D.; Paggi, J.M.; Park, C.; Bennett, C.; Salzberg, S.L. Graph-based genome alignment and genotyping with HISAT2 and
      HISAT-genotype. Nat. Biotechnol. 2019, 37, 907–915. [CrossRef]
48.   Pertea, M.; Pertea, G.M.; Antonescu, C.M.; Chang, T.C.; Mendell, J.T.; Salzberg, S.L. StringTie enables improved reconstruction of
      a transcriptome from RNA-seq reads. Nat. Biotechnol. 2015, 33, 290–295. [CrossRef]
49.   Langfelder, P.; Horvath, S. WGCNA: An R package for weighted correlation network analysis. BMC Bioinform. 2008, 9, 559.
      [CrossRef]
50.   Smoot, M.E.; Ono, K.; Ruscheinski, J.; Wang, P.L.; Ideker, T. Cytoscape 2.8: New features for data integration and network
      visualization. Bioinformatics 2011, 27, 431–432. [CrossRef]
Int. J. Mol. Sci. 2022, 23, 13027                                                                                                       18 of 18




51.   Li, T.; Pan, W.; Yuan, Y.; Liu, Y.; Li, Y.; Wu, X.; Wang, F.; Cui, L. Identification, Characterization, and Expression Profile Analysis of
      the mTERF Gene Family and Its Role in the Response to Abiotic Stress in Barley (Hordeum vulgare L.). Front. Plant Sci. 2021,
      12, 684619. [CrossRef]
52.   Ai, Q.; Pan, W.; Zeng, Y.; Li, Y.; Cui, L. CCCH Zinc finger genes in Barley: Genome-wide identification, evolution, expression and
      haplotype analysis. BMC Plant Biol. 2022, 22, 117.
53.   Livak, K.J.; Schmittgen, T.D. Analysis of relative gene expression data using real-time quantitative PCR and the 2(-Delta Delta
      C(T)) Method. Methods 2001, 25, 402–408. [CrossRef] [PubMed]
54.   Yang, G.; Zhang, Y.; Wei, X.; Cui, L.; Nie, X. Genetic Diversity of Transcription Factor Genes in Triticum and Mining for Promising
      Haplotypes for Beneficial Agronomic Traits. Front. Plant Sci. 2022, 13, 899292. [CrossRef] [PubMed]
