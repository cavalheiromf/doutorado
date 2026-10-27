# Zhang_2023 - Genome-wide analysis of hyperosmolality-gated calcium-permea

**Source PDF:** 

---

                                                                               Gene 856 (2023) 147137


                                                                    Contents lists available at ScienceDirect


                                                                                        Gene
                                                            journal homepage: www.elsevier.com/locate/gene




Genome-wide analysis of hyperosmolality-gated calcium-permeable
channel (OSCA) family members and their involvement in various osmotic
stresses in Brassica napus
Xiaojuan Zhang a, c, d, e, 1, Xiaohui Cheng b, 1, Chenlu Zhang a, Xiuqi Ma a, Yu Zhang a,
Jianmin Song c, Meili Xie b, *
a
  School of Biological Science and Engineering, Shaanxi University of Technology, Hanzhong 723001, Shaanxi, China
b
  The Key Laboratory of Biology and Genetic Improvement of Oil Crops, Oil Crops Research Institute of the Chinese Academy of Agricultural Sciences, Wuhan 430000,
China
c
  Shaanxi Province Key Laboratory of Bio-resources, Hanzhong 723001, Shaanxi, China
d
  Qinba Mountain Area Collaborative Innovation Center of Bioresources Comprehensive Development, Hanzhong 723001, Shaanxi, China
e
  Qinba State Key Laboratory of Biological Resources and Ecological Environment (Incubation), Hanzhong 723001, Shaanxi, China




A R T I C L E I N F O                                      A B S T R A C T

Edited by Tengbo Huang                                     Plant hyperosmolality-gated calcium-permeable channel (OSCA) is a calcium permeable cation channel that
                                                           responds to hyperosmotic stress and plays a pivotal role in plant growth, development and stress response.
Keywords:                                                  Through a genome-wide survey, 41 OSCA genes were identified from the genome of Brassica napus. The OSCA
Brassica napus                                             family genes were unevenly distributed over 14 chromosomes of B. napus and phylogenetic analysis separated
OSCA gene family
                                                           the OSCA family into four clades. Motif analyses indicated that OSCA proteins in the same clade were highly
Tissue expression
                                                           conserved and the protein conserved motifs shared similar composition patterns. The OSCA promoter regions
Osmotic stress
Cold stress                                                contained many hormone-related elements and stress response elements. Gene duplication analysis elucidated
                                                           that WGD/segmental duplication was the main driving force for the expansion of OSCA genes during evolution
                                                           and these genes mainly underwent purifying selection. RNA-seq and qRT-PCR analysis of different tissues showed
                                                           that OSCA genes are expressed and function mainly in the root. Among these genes, BnOSCA3.1a and BnO­
                                                           SCA3.1c had relatively high expression levels under osmotic stresses and cold stress and were highly expressed in
                                                           different tissues. Protein interaction network analysis showed that a total of 5802 proteins might interact with
                                                           OSCAs in B. napus, while KEGG/GO enrichment analysis indicated that OSCAs and their interacting proteins were
                                                           mainly involved in plant response to abiotic stress. This systematic analysis of the OSCAs in B. napus identified
                                                           gene structures, evolutionary features, expression patterns and related biological processes. These findings will
                                                           facilitate further functional and evolutionary analysis of OSCAs in B. napus for breeding of osmotic-stress-
                                                           resistant plants.




1. Introduction                                                                                  affect plant growth, leading to a decrease in yield, quality and may even
                                                                                                 result in the plant dying (Stanley and Isabelle, 2015). Plants have
    Drought and salt stress are the two main types of abiotic stresses that                      evolved complex mechanisms to respond to these stresses as a means of



    Abbreviations: TRPV4, Transient Receptor Potential Vanilloid 4; ERE, Ethylene-Responsive Element; ARE, Antioxidant Response Element; TGA-box, Auxin-
Responsive Element; GARE-motif, Gibberellin-Responsive Element; ABRE, Abscisic Acid Responsive Element; MBS, MYB Binding Site; WUN-motif, Wound-
Responsive Element; O2-site, Cis-acting regulatory element involved in the metabolism regulation of maize gliadin; MBSI, MYB binding site involved in flavonoid
biosynthetic genes regulation; HD-Zip1, Homeodomain leucine zipper I; CAT-box, Cis-acting regulatory elements involved in the expression of meristems;
GCN4_motif, Cis-regulating elements involving endosperm expression; LTR, Cis-acting element involved in low-temperature responsiveness; TC-rich repeats, Cis-
acting element involved in defense and stress responsiveness.
 * Corresponding author.
    E-mail addresses: yuzhang20160315@outlook.com (Y. Zhang), 412532011@qq.com (J. Song), xiemeili@caas.cn (M. Xie).
  1
    Xiaojuan Zhang and Xiaohui Cheng contributed equally to this work.

https://doi.org/10.1016/j.gene.2022.147137
Received 15 July 2022; Received in revised form 12 December 2022; Accepted 21 December 2022
Available online 24 December 2022
0378-1119/© 2022 Elsevier B.V. All rights reserved.
X. Zhang et al.                                                                                                                             Gene 856 (2023) 147137


avoiding or reducing damage to their body (Ingram and Bartels, 1996;                 response to hypertonic stress. Previous studies on several plant species
Zhu, 2002; Bartels and Sunkar, 2005). The first common phase of                      identified and analyzed OSCA gene families at the genome-wide level
drought and salt stress is osmotic stress (Shavrukov, 2013). Plants sense            and found 15, 11, 10, 21 and 13 OSCA genes in Arabidopsis (Yuan et al.,
external stress stimuli through receptors or sensory proteins. The plants            2014), rice (Li et al., 2015), maize (Ding et al., 2019), soybean (Li et al.,
then transmit signals through various channels and regulate the                      2017) and Vigna radiata (Yin et al., 2021), respectively. Brassica napus is
expression of stress response genes, leading to modifications in plant               an allopolyploid originating from a spontaneous hybridization between
physiology and morphology (Li et al., 2015). The genes involved in the               Brassica rapa (AA genome) and Brassica oleracea (CC genome) (Chalhoub
regulation of the plant’s early response to stress factors have been re­             et al., 2014) and is an important oil crop worldwide. It is the main source
ported in previous studies, including early-responsive to dehydration                of edible rapeseed oil but can also be used as a vegetable, feed or
stress protein gene ERD4 (Camargo et al., 2007; Liu et al., 2009; Rai                ornamental crop, which has important economic, social and ecological
et al., 2012), Na+/H+ antiporter gene NHX (Reguera et al., 2014),                    benefits. So far, characterization of B. napus OSCA genes and their
StNAC2 gene (Xu et al., 2014) and dehydration-responsive element-                    expression pattern in tissues and under various stresses is limited. Based
binding protein gene DREB (Shinozaki and Yamaguchi-Shinozaki,                        on the published genome (Chalhoub et al., 2014) and transcriptome
2000). Genes such as RD22, RD29A, KIN1, KIN2 and RASD1 that                          datasets (Li et al., 2019; Zhang et al., 2019), B. napus OSCA family genes
participate in the Abscisic acid (ABA) signaling pathway are also related            were identified in this study. In addition, the phylogenetic relationship,
to osmotic stress in plants (Fujita et al., 2011; Podia et al., 2017).               conserved motifs, duplication events, cis-regulatory elements in pro­
    Calcium plays a crucial role in sensing external osmotic stress, acti­           moter regions and protein interaction networks were also systematically
vating various signal transduction pathways and expression of stress                 analyzed. Moreover, expression profiles of the OSCA family genes in
induced genes. Upon receipt of a signal, which activates the plants’                 different tissues and in response to various stresses (drought, ABA, NaCl
response to external osmotic stress or other stress stimuli, the concen­             and cold) were also examined. This investigation provided important
tration of cytoplasm/intracellular free calcium increases due to changes             new findings for the subsequent in-depth analysis of the biological
in osmotic pressure (Knight et al., 1997; McAinsh and Pittman, 2009).                functions and molecular mechanisms of B. napus OSCA genes in response
Studies have shown that hypertonic-induced increases in calcium ion                  to drought and other abiotic stresses. Identification and analysis of the
concentration (OICI) can be detected in five seconds after plants un­                B. napus OSCA gene family will enable the screening of resistance genes
dergo stress and this is the earliest detected event in plants (Knight et al.,       which may be potential molecular genetic targets for future breeding of
1997). The calcium ion channel and other transport systems on the                    drought and osmotic stress-resistant rapeseed.
plasma membrane are responsible for regulating the concentration of
free calcium ions in the cytoplasm when plants are stimulated by                     2. Materials and methods
external stresses (Batistic and Kudla, 2012; Hou et al., 2014). In bacteria
and animals, Ca2+ permeable channels stimulated by osmotic/me­                       2.1. Genome wide identification of OSCA gene family members in B.
chanical stress have been identified as osmosensors (Arnadóttir and                 Napus
Chalfie, 2003; Booth et al., 2007). The hyperosmolality-gated calcium-
permeable channel (OSCA) is a calcium ion non-selective cation chan­                     The conserved OSCA DUF221 protein domain (pfam accession
nel, which has been characterized as an osmosensor in Arabidopsis                    number: 02714) from the Pfam website was used to build the Hidden
thaliana (Batistic and Kudla, 2012; Hou et al., 2014). OSCA is an                    Markov Model profiles (https://hmmer.janelia.org/) to search against
important calcium permeable cation channel located on the plasma                     the whole-genome protein database of B. napus cultivar ‘Darmor-bzh’
membrane and is induced in the presence of osmotic stress (Batistic and              (the Brassicaceae Database: Brassica napus v4.1) (Chalhoub et al., 2014).
Kudla, 2012; Hou et al., 2014; Yuan et al., 2014). The OSCA family                   The OSCA gene sequences of Arabidopsis were also used to search against
proteins have three conserved functional domains, namely, cytosolic                  the B. napus genome to obtain the homologous sequences in B. napus.
domain of 10 TM putative phosphate transporter (pfam 14703,                          The proteins obtained by both methods were further verified through
DUF4463), late exocytosis (pfam13967) and calcium-dependent chan­                    submissions       to      NCBI-CDD          (https://www.ncbi.nlm.nih.
nel (pfam02714, DUF221) (Li et al., 2015; Yuan et al., 2014). In Ara­                gov/Structure/cdd/wrpsb.cgi), Smart (https://smart.embl-heidelberg.
bidopsis, a plasma membrane protein (OSCA1) (Yuan et al., 2014) forms                de/) and Pfam (https://pfam.xfam.org/) for domain prediction. Pro­
hyperosmolality-gated calcium-permeable channels that mediate the                    teins without the intact pfam 02,714 domain were removed and the
increase in Ca2+ concentrations. OSCA1 can be activated by hyper­                    OSCA genes for B. napus were obtained. Based on the information of
osmolality and function similar to the osmosensor TRPV4 (Liedtke et al.,             genome annotation, the location of OSCA genes on chromosomes were
2000), which suggests that OSCA1 is also an osmosensor. Yuan et al.                  displayed by MG2C v2 (Chao et al., 2021). The isoelectric point and
(2014) also established that OSCA1 functions upstream of the ABA                     molecular weight of OSCA proteins were analyzed using ExPASY (https
signaling pathway and may affect calcium-regulating osmotic signals in               ://web.expasy.org/compute_pi/) while the subcellular localizations
guard cells by regulating the closure of stomata to reduce water evap­               were predicted by CELLO (Yu et al., 2006).
oration. OSCA1 also contains the DUF221 domain and genes containing
this domain encode for proteins involved in hyperosmotic stress (Ganie               2.2. Construction of the B. Napus OSCA protein family phylogenetic tree
et al., 2017). In Arabidopsis, OSCA1.2 (also referred to as AtCSC1) was
identified as a membrane integral protein cation channel that regulates                 The OSCA protein sequences of B. napus and Arabidopsis were aligned
Ca2+ permeability. It was predicted that there are three transmembrane               together using ClustalW (Larkin et al., 2007). The phylogenetic tree was
(TM) helices in the N-terminal region and six TM helices in the C-ter­               constructed using MEGA7 with the neighbor-joining method and 1000
minal region, which together form the DUF221 domain (Hou et al.,                     replicate iterations (Kumar et al., 2016). Evolview was used to visualize
2014; Liu et al., 2018). In rice, OsOSCA3. 1 was identified as the early             the evolutionary tree (He et al., 2016).
drought response gene OsERD4 (Li et al., 2015). The over-expression of
maize ZmOSCA2.4 in Arabidopsis improved drought resistance of trans­                 2.3. OSCA gene structure, motif and promoter element analysis
genic plants (Cao et al., 2020). The wheat drought resistance gene
TaOSCA1.4, which is similar to OsOSCA1. 4 and AtOSCA1. 8, also                           OSCA genes sequence information was extracted from the B. napus
affected the number of sterile spikelets, the number of grains per spike             reference genome (the Brassicaceae Database: Brassica napus v4.1). The
and the total yield (Lv, 2015). However, the plant molecular mechanism               MEME software (Bailey et al., 2015) was used for conserved motif
(s) of early response to osmotic stress have yet to be fully established.            analysis with an e-value of 10.0, minimum length of 6 and maximum
    Members of the OSCA gene family play an important role in plant                  length of 50, and the results were displayed through Tbtools (Chen et al.,

                                                                                 2
                                                                                                                                                                                                        X. Zhang et al.
    Table 1
    Hyperosmolality-gated calcium-permeable channel (OSCA) gene family members in B. napus.
     Gene              Name           Ath           Ath_name      Chr            Start        End          pI     MW (kDa)    Amino acids   Exon number   Duplication type   Subcellular Localization

     BnaA03g25360D     BnOSCA1.1a     AT4G04340     AtOSCA1.1     A03            12,252,116   12,256,795   8.67    87.00201   769           12            WGD or Segmental   Plasma Membrane
     BnaC03g29810D     BnOSCA1.1b     AT4G04340     AtOSCA1.1     C03            17,939,650   17,944,049   8.43    87.06001   769           12            WGD or Segmental   Plasma Membrane
     BnaA01g11920D     BnOSCA1.2a     AT4G22120     AtOSCA1.2     A01            5,970,386    5,973,641    9.24    79.23721   696           9             WGD or Segmental   Plasma Membrane
     BnaA08g10140D     BnOSCA1.2b     AT4G22120     AtOSCA1.2     A08            9,491,843    9,495,017    8.89    79.71964   700           9             WGD or Segmental   Plasma Membrane
     BnaC01g13570D     BnOSCA1.2c     AT4G22120     AtOSCA1.2     C01            8,876,853    8,880,156    8.96    87.79263   769           7             WGD or Segmental   Plasma Membrane
     BnaC03g64830D     BnOSCA1.2d     AT4G22120     AtOSCA1.2     C03            54,238,412   54,241,847   8.06    88.35515   776           9             WGD or Segmental   Plasma Membrane
     BnaA06g08400D     BnOSCA1.3a     AT1G11960     AtOSCA1.3     A06            4,569,709    4,573,293    8.83    87.9275    769           10            WGD or Segmental   Plasma Membrane
     BnaC05g09770D     BnOSCA1.3b     AT1G11960     AtOSCA1.3     C05            5,460,338    5,464,705    8.83    87.83921   769           11            WGD or Segmental   Plasma Membrane
     BnaA03g60360D     BnOSCA1.4a     AT1G62320     AtOSCA1.4     A03_random     4,896,830    4,901,368    8.68    91.59287   797           11            WGD or Segmental   Plasma Membrane
     BnaA09g13330D     BnOSCA1.4b     AT1G62320     AtOSCA1.4     A09            7,440,887    7,444,705    6.94    89.15059   780           11            WGD or Segmental   Plasma Membrane
     BnaC09g13620D     BnOSCA1.4c     AT1G62320     AtOSCA1.4     C09            10,278,146   10,282,008   7.62    89.10944   780           11            WGD or Segmental   Plasma Membrane
     BnaA03g36370D     BnOSCA1.5a     AT3G21620     AtOSCA1.5     A03            17,797,453   17,801,197   9.22    86.77362   757           11            WGD or Segmental   Plasma Membrane
     BnaC03g42220D     BnOSCA1.5b     AT3G21620     AtOSCA1.5     C03            27,006,537   27,010,407   9.32    86.75679   757           11            WGD or Segmental   Plasma Membrane
     BnaA01g18580D     BnOSCA1.6a     AT4G15430     AtOSCA1.6     A01            10,073,176   10,076,844   9.35    86.69542   757           13            WGD or Segmental   Plasma Membrane
     BnaA08g05680D     BnOSCA1.6b     AT4G15430     AtOSCA1.6     A08            5,594,017    5,597,361    9.24    86.42824   756           11            WGD or Segmental   Plasma Membrane
     BnaC01g22480D     BnOSCA1.6c     AT4G15430     AtOSCA1.6     C01            15,904,044   15,907,694   9.32    86.65126   757           13            WGD or Segmental   Plasma Membrane
     BnaC08g10180D     BnOSCA1.6d     AT4G15430     AtOSCA1.6     C08            15,182,212   15,185,622   9.2     87.10297   762           11            WGD or Segmental   Plasma Membrane
     BnaA03g25940D     BnOSCA1.7a     AT4G02900     AtOSCA1.7     A03            12,658,525   12,662,327   8.86    88.08077   770           11            WGD or Segmental   Plasma Membrane
     BnaC03g30530D     BnOSCA1.7b     AT4G02900     AtOSCA1.7     C03            18,580,901   18,584,827   8.86    88.0187    770           11            WGD or Segmental   Plasma Membrane
3




     BnaA05g16450D     BnOSCA1.8a     AT1G32090     AtOSCA1.8     A05            11,157,355   11,161,661   8.74    92.95295   806           11            WGD or Segmental   Plasma Membrane
     BnaC05g29030D     BnOSCA1.8b     AT1G32090     AtOSCA1.8     C05            27,746,174   27,750,524   8.81    93.01001   806           11            WGD or Segmental   Plasma Membrane
     BnaA01g21850D     BnOSCA2.1a     AT1G58520     AtOSCA2.1     A01            14,142,369   14,146,362   7.84    82.22777   724           12            WGD or Segmental   Plasma Membrane
     BnaA03g59260D     BnOSCA2.1b     AT1G58520     AtOSCA2.1     A03_random     2,561,158    2,566,145    8.42    87.05853   766           11            Dispersed          Plasma Membrane
     BnaC01g28160D     BnOSCA2.1c     AT1G58520     AtOSCA2.1     C01            25,835,002   25,839,822   8.06    81.49697   717           12            WGD or Segmental   Plasma Membrane
     BnaC04g18540D     BnOSCA2.1d     AT1G58520     AtOSCA2.1     C04            18,255,409   18,259,690   8.06    82.1658    724           12            WGD or Segmental   Plasma Membrane
     BnaA08g25990D     BnOSCA2.2a     AT1G10090     AtOSCA2.2     A08            17,725,866   17,729,944   8.95    86.12898   762           9             WGD or Segmental   Plasma Membrane
     BnaC08g13980D     BnOSCA2.2b     AT1G10090     AtOSCA2.2     C08            18,962,420   18,965,784   9.01    86.10487   762           9             WGD or Segmental   Plasma Membrane
     BnaA03g27630D     BnOSCA2.3a     AT3G01100     AtOSCA2.3     A03            13,578,326   13,581,523   8.66    79.50809   703           11            WGD or Segmental   Plasma Membrane
     BnaA05g34090D     BnOSCA2.3b     AT3G01100     AtOSCA2.3     A05            23,022,737   23,028,210   9.52    89.91786   793           12            WGD or Segmental   Plasma Membrane
     BnaC03g32650D     BnOSCA2.3c     AT3G01100     AtOSCA2.3     C03            20,012,136   20,018,463   8.95   140.62979   1241          21            WGD or Segmental   Plasma Membrane
     BnaC05g48610D     BnOSCA2.3d     AT3G01100     AtOSCA2.3     C05            43,024,423   43,027,955   8.75    80.96981   714           10            WGD or Segmental   Plasma Membrane
     BnaA07g27960D     BnOSCA2.4a     AT1G69450     AtOSCA2.4     A07            20,245,451   20,248,495   9.41    82.33867   716           9             WGD or Segmental   Plasma Membrane
     BnaC06g30620D     BnOSCA2.4b     AT1G69450     AtOSCA2.4     C06            31,317,242   31,320,857   9.37    82.48683   716           10            WGD or Segmental   Plasma Membrane
     BnaA09g34360D     BnOSCA2.5a     AT3G54510     AtOSCA2.5     A09            25,191,186   25,194,383   7.91    80.25888   705           10            WGD or Segmental   Plasma Membrane
     BnaC08g25280D     BnOSCA2.5b     AT3G54510     AtOSCA2.5     C08            27,053,137   27,056,275   7.63    80.2578    706           10            WGD or Segmental   Plasma Membrane
     BnaA08g17380D     BnOSCA3.1a     AT1G30360     AtOSCA3.1     A08            13,821,919   13,825,861   9.27    81.96712   724           6             WGD or Segmental   Plasma Membrane
     BnaA09g26160D     BnOSCA3.1b     AT1G30360     AtOSCA3.1     A09            19,282,008   19,286,964   9.52    82.19357   723           6             WGD or Segmental   Plasma Membrane
     BnaC03g59660D     BnOSCA3.1c     AT1G30360     AtOSCA3.1     C03            48,939,496   48,943,164   9.25    81.92407   724           6             WGD or Segmental   Plasma Membrane
     BnaCnng57110D     BnOSCA3.1d     AT1G30360     AtOSCA3.1     Cnn_random     56,902,948   56,904,569   9.49    55.3965    488           3             Dispersed          PlasmaMembrane
     BnaA08g14860D     BnOSCA4.1a     AT4G35870     AtOSCA4.1     A08            12,456,975   12,459,413   7.09    91.78679   813           1             Dispersed          PlasmaMembrane
     BnaC03g76890D     BnOSCA4.1b     AT4G35870     AtOSCA4.1     C03_random     5,417,434    5,420,044    7.5     91.49058   809           1             Dispersed          PlasmaMembrane




                                                                                                                                                                                                        Gene 856 (2023) 147137
X. Zhang et al.                                                                                                                        Gene 856 (2023) 147137




                                                Fig. 1. Location of the B. napus OSCA genes on chromosomes.


2020). For analysis of cis-elements, the 2 kb sequences upstream of the            transcription was performed using the PrimeScript RT Reagent Kit with
OSCA CDS were extracted and analyzed with the PlantCARE software                   gDNA Eraser (Takara, Japan). The relative expression of BnOSCAs was
(Lescot et al., 2002). The results were sorted and displayed by TBtools.           quantified using quantitative real time-PCR (qRT-PCR) with gene-
The heatmap representing the number of cis-elements was drawn with                 specific primers (Supplementary Table 3). qRT-PCR was run on the
the R package pheatmap.                                                            CFX96 Real-time PCR System (Bio-Rad) using the SYBR Green Real-time
                                                                                   PCR Master Mix (Bio-Rad, USA). The internal standard was the B. napus
2.4. Gene duplication analysis                                                     actin gene (BnaA01g27090D). All assays were conducted over three
                                                                                   biological repeats, each with three technical repeats. The quantification
    BLASTP and MCScanX (Wang et al., 2012) were adopted to analyze                 method used for expression of BnOSCAs in different tissues and under
the duplicated genes in the OSCA family of B. napus. Circos software               different stresses were 2 -△CT (Livak and Schmittgen, 2001) and 2 -△△CT
(Krzywinski et al., 2009) was used to show the position and relationship           (Livak and Schmittgen, 2001), respectively.
of the duplicated genes. The protein sequences of the duplicated gene
pair were aligned by Muscle (Edgar, 2004), and the Ka/Ks values were               2.7. Protein interaction analysis
calculated with the KaKs_Calculator (Wang et al., 2010) to evaluate the
selection pressure.                                                                    The protein interaction information for OSCAs in Arabidopsis was
                                                                                   obtained with STRING (https://www.string-db.org/). That resource was
2.5. Gene expression analysis                                                      used to search the corresponding interaction network of B. napus OSCA
                                                                                   proteins based on the homology between Arabidopsis and B. napus
    The RNA-seq data of different tissues (root, leaf, bud, silique, stamen,       OSCAs. Cytoscape (Shannon et al., 2003) was used to display the
pistil, blossomy petal, wilting petal, stem, sepal, ovule and pericarp) and        interaction relationship. KEGG and GO enrichment analysis were per­
various stresses (dehydrate, cold, ABA and NaCl) were downloaded to                formed for the genes encoding proteins that interacted with OSCA
investigate the expression patterns of OSCA genes in B. napus (Li et al.,          proteins using the R package clusterProfiler (Yu et al., 2012).
2019; Zhang et al., 2019). Hisat2 was used to map the RNA-seq reads to
the B. napus genome and Stringtie was used to calculate the expression             3. Results
levels. The expression data of OSCAs were extracted and displayed with
the R package pheatmap.                                                            3.1. Identification of the OSCA gene family members in B. Napus

2.6. Quantitative reverse transcription polymerase chain reaction                      We used the Hidden Markov Model to search for the DUF221 domain
                                                                                   within the B. napus cultivar ‘Darmor-bzh’ as a systematic screen of OSCA
    Brassica napus ZS11 seedlings were grown in a growth room at 24 ◦ C            genes at the whole genome level. A total of 41 genes were identified as
with a 16/8h light/dark photoperiod. The leaves, stems and roots were              OSCAs in the B. napus genome. The BnOSCA genes were named based on
collected from 20-day-old seedlings, buds were collected from 70-day-              their homologs in Arabidopsis. Thirty-seven OSCA genes were unevenly
old seedlings, and siliques were harvested 90 days after germination.              distributed over 14 chromosomes, and the other four OSCA genes were
For cold and osmotic stresses treatment research, leaf samples from                located on random chromosomes of B. napus (Table 1, Fig. 1). In
three weeks old plants of Brassica napus ZS11 were collected at 1 h and 8          particular, no OSCAs were located on the A02, A04, A10, C02, and C07
h after dehydration while 4 h and 24 h of ABA (25 μM), salt (200 mM),              chromosomes. The C03 chromosome contained the largest number of
and low temperature (4 ◦ C) treatment, as described in (Zhang et al.,              OSCA genes (7) while only one OSCA gene is present on chromosomes
2019). Samples were stored in liquid nitrogen immediately after                    A06, A07, C04, and C06. Subcellular localization prediction showed that
collection. Total RNA was extracted using the TRIzol reagent (Invi­                all the BnOSCAs were located on the plasma membrane. The number of
trogen, 15596026, USA) according to the product manual. Reverse                    exons contained in the OSCA genes ranged from one (BnOSCA4.1a and

                                                                               4
X. Zhang et al.                                                                                                                            Gene 856 (2023) 147137




Fig. 2. Phylogenetic tree of the B. napus and Arabidopsis OSCA gene families. The neighbor-joining tree was generated using the amino acid sequences of the OSCA
proteins through the MEGA7 program and neighbor-joining (NJ) method, with 1000 bootstrap replicates. The four major phylogenetic clades (I to IV) are labeled and
the OSCAs from B. napus and Arabidopsis are marked with asterisks and triangles, respectively.


BnOSCA4.1b) to 21 (BnOSCA2.3c). Many OSCA genes (33.33%) con­                       had been preserved during evolution, indicating that they may have
tained 11 exons while only four genes had three exons or less. The length           important biological functions. Clade I could be further subdivided into
of most of the B. napus OSCA proteins coding regions varied between                 eight small branches with each branch containing an AtOSCA protein
700 and 800 amino acids (AA). BnOSCA3.1d with 488 AA was the                        and two to five BnOSCA proteins. Meanwhile, Clade II consisted of five
smallest OSCA protein, while BnOSCA2.3c was the largest protein at                  branches. Clades I and II contained a larger number of branches and
1241 AA. The isoelectric points of the OSCA proteins ranged from 6.94               OSCAs, suggesting that there may be functional differentiation of OSCA
to 9.52 and the molecular weights varied from 55.40 to 140.63 kDa.                  genes in these two clades. Phylogenetic analysis showed that the OSCAs
                                                                                    in B. napus and Arabidopsis had a relatively conserved evolutionary
                                                                                    relationship.
3.2. Phylogenetic relationship analysis of the OSCA gene family

    To elucidate the phylogenetic relationship among OSCAs in B. napus,             3.3. Analysis of the B. Napus OSCA gene structure and OSCAs motifs
a phylogenetic tree was built based on the full-length sequence of 41
BnOSCA proteins and 15 AtOSCA proteins. The evolutionary tree                           We analyzed and compared the distribution of exons and introns
showed that these OSCA proteins were clearly divided into four main                 within the B. napus OSCA gene family members. The number of introns
clades (Fig. 2), consistent with previous studies (Yuan et al., 2014).              in OSCA genes within the same clade was close (Fig. 3C). For example,
Clade I was the largest branch, consisting of 21 BnOSCA proteins and                with the exception of BnOSCA3.1d, all OSCA genes in clade III contained
eight AtOSCA proteins. Clade II consisting of 14 BnOSCA proteins and                five introns, and the intron composition pattern of the OSCA genes in
five AtOSCA proteins was the second largest branch. Clade III comprised             Clade I was also similar. Interestingly, none of the two OSCA genes in
of four BnOSCA proteins and one AtOSCA protein while the smallest                   Clade IV contained introns, meaning that the OSCA protein in this
branch, Clade IV, contained two BnOSCA proteins and one AtOSCA                      branch had different gene structures. In addition, the composition
protein. Although the number of OSCAs in this group was small, they                 pattern of OSCA gene introns in Clade II was variable. To further explore

                                                                                5
X. Zhang et al.                                                                                                                               Gene 856 (2023) 147137




Fig. 3. B. napus OSCA proteins conserved motifs and OSCA family gene structures. A. Phylogenetic tree of OSCAs in B. napus. B. Analysis of conserved motifs of OSCA
proteins in B. napus. C. Gene architecture of OSCA genes in B. napus. The purple box, the green box and the horizontal line represent UTRs, exons and introns,
respectively. The length of the purple box, the green box and the horizontal line represents the relative lengths of the corresponding UTRs, exons and introns. (For
interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)


the conservation and evolutionary relationship of the OSCAs in B. napus,             have similar biological functions. Different motif compositions within
conservative motifs were identified using the MEME software. Fifteen                 the same clade were also noted. For example, the conserved motif
conserved motifs were identified in the B. napus OSCA protein family                 composition of BnOSCA3.1d in clade III, BnOSCA2.3a, BnOSCA2.3b,
(Fig. 3B). All OSCA family numbers contained motif 1 and most OSCA                   BnOSCA2.3c and BnOSCA2.3d in clade II were different from other
proteins contained motifs 5, 8 and 9, indicating that the OSCA genes may             OSCA proteins in the same clade, indicating OSCAs in the same clade
encode for proteins with common functions. Notably, motifs 13 and 14                 also underwent variation during evolution. The two OSCA proteins in
were only identified in clade I implied that the OSCAs in clade I may                clade IV contained only four conserved motifs, which is significantly
have different functions from those in other clades. Generally, the OSCA             different from the other branches in both the number and pattern of
proteins in the same clade were highly conserved and the composition                 conserved motifs.
patterns of protein-conserved motifs were very similar. The conserva­
tion of OSCA protein motifs in the same clade was consistent with their              3.4. Analysis of cis-acting elements within the promoters of OSCA genes in
close evolutionary relationship (Fig. 3A and 3B). In clade I, all OSCA               B. Napus
proteins contained 14 to 15 conserved motifs and had very similar
conserved motif composition. OSCAs in clades II and III had similar                     To further analyze the functions of B. napus OSCA family members in
protein conserved motif composition suggesting that the OSCAs may                    plant growth, development and response to stress, analysis of cis-acting

                                                                                 6
X. Zhang et al.                                                                                                                              Gene 856 (2023) 147137




Fig. 4. Distribution of the cis-regulatory elements in the promoters of B. napus OSCA genes. The OSCA genes are shown on the left. The hormone responsive elements,
the plant development-related elements and the stress responsive elements are represented by rectangles, upright triangles and inverted triangles, respectively.
Different colors represent different components.


element(s) within the promoter regions of B. napus OSCAs was under­                  drought stress, this implies that OSCA gene products assist plants with
taken. PlantCARE was able to predict multiple types of cis-regulatory                adaptation to drought stress. The stress-related element ARE was also
elements controlling hormones, developmental and stress processes                    more abundant in the BnOSCA1.8a (4), BnOSCA1.8b (5), BnOSCA1.5a
(Fig. 4). Among them, hormone response elements including ERE, TGA-                  (4), BnOSCA1.6a (4), BnOSCA2.2a (4) and BnOSCA2.3c (4) gene pro­
box, GARE-motif, ABRE, TATC-box and CGTCA-motif, developmental                       moters. The BnOSCA1.8a gene promoter contained five stress-related
response elements including O2-site, MBSI, CAT-box, CAT-box, circa­                  elements LTR, and the stress-related element MBS was more pro­
dian, HD-Zip1 and GCN4_motif as well as stress response elements                     nounced in the BnOSCA1.1b (4) and BnOSCA1.4a (4) gene promoters
including ARE, TC-rich repeats, MBS, WUN-motif and LTR were iden­                    (Table S1).
tified. Among all the OSCAs in B. napus, the promoter regions of BnO­
SCA2.3c contained the most cis-regulatory elements (23), while
                                                                                     3.5. Gene duplication of OSCAs
BnOSCA2.4a contained only five elements. In general, hormone
response elements ABRE, ERE, CGTCA-motif and stress response ele­
                                                                                         To elucidate the expansion patterns of the OSCA genes in rapeseed,
ments ARE and MBS were highly abundant in OSCA gene promoters
                                                                                     gene duplication events were analyzed. We identified 42 syntenic OSCA
(Fig. 5) with ABRE being the most abundant. The promoter regions of
                                                                                     gene pairs by using the MCScanX program; six pairs were found in the A
the clade II genes BnOSCA2.1d, BnOSCA2.2a, BnOSCA2.2b, BnOSCA2.1b
                                                                                     subgenome, five pairs occurred in the C subgenome, and the other 31
and BnOSCA2.1a contained numerous ABRE elements, which were 8, 7,
                                                                                     pairs were detected between the A and C subgenomes (Fig. 6). Most of
6, 5 and 6, respectively. In clade I, the promoters of BnOSCA1.3a (6),
                                                                                     the OSCA genes (37/41) were derived from whole-genome duplication
BnOSCA1.3b (5), BnOSCA1.2d (2), BnOSCA1.1a (6) and BnOSCA1.1b (4)
                                                                                     (WGD) or segmental duplication events, and only four genes were ob­
also contained ABRE elements. ABRE, which is the ABA response
                                                                                     tained by dispersed duplication. Thus, it can be concluded that WGD/
element, regulates the expression of genes activated by ABA and the ABA
                                                                                     segmental duplication was the main driving force for the expansion of
signaling pathway. As ABRE is associated with the plant response to
                                                                                     OSCA genes in the B. napus genome. To explore the evolutionary forces

                                                                                 7
X. Zhang et al.                                                                                                                                     Gene 856 (2023) 147137




Fig. 5. Heatmap of the cis-regulatory elements for 41 OSCA genes in B. napus normalized to log2 transformation. The color scale represents the number of transcripts
from low (blue color) to high (red color). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)


of the OSCAs in B. napus, the non-synonymous/synonymous substitution                     composed of 27 genes that exhibited very low or no expression in
ratio (Ka/Ks) for each duplicated gene pair was calculated. The Ka/Ks                    various tissues. Among them, BnOSCA1.4a and BnOSCA1.5b were not
ratio of the duplicated OSCAs in B. napus varied from 0.0093 to 0.2014                   expressed in all tissues, while expression of BnOSCA1.2a and BnO­
with an average of 0.0971 (Table S2). All the Ka/Ks values of the                        SCA1.2c in the ovule was relatively high, suggesting that the encoded
duplicated OSCAs gene pairs were less than 1 indicating that the                         proteins may be required for the development of the ovule. Group III
duplicated B. napus OSCAs had undergone purifying selection pressure                     included five moderately expressed genes with expression levels inter­
during their evolution.                                                                  mediate to that of Groups I and II genes. The total number of OSCA genes
                                                                                         expressed in buds was the largest, followed by roots and blossomy pistil
3.6. Expression of OSCAs in different tissues of B. Napus                                (Fig. 7B). A total of 13 genes including most of the genes in Group I were
                                                                                         expressed in all tissues. Only one gene was specifically expressed in
    To further understand the expression patterns of the B. napus OSCA                   ovule (BnOSCA1.5a), sepal (BnOSCA2.1a) and bud (BnOSCA1.7b).
gene family, we analyzed the expression of OSCA genes in 12 different                        As the gene expression analysis was performed on previously pub­
tissues (pistil, ovule, silique, stem, leaf, wilting pistil, pericarp, sepal,            lished RNA-seq data, we verified the expression patterns of nine OSCA
stamen, blossomy pistil, root and bud) using previous published data (Li                 genes representing the four clades of the B. napus OSCA gene family.
et al. 2019) (Fig. 7). The results show that members of the OSCA gene                    Expression of these genes in root, stem, leaf, silique and bud of B. napus
family had different tissue expression patterns, indicating that OSCA                    cultivar ZS11 was analyzed by quantitative Real Time-PCR (qRT-PCR).
genes may have evolved towards tissue specificity for growth and                         The expression profiles of the selected OSCA genes were highly consis­
development. Based on the expression patterns, the BnOSCAs could be                      tent with the analysis using previous published RNA-seq data (Fig. 8).
divided into three groups (I–III) (Fig. 7A). Group I consists of nine genes              Expression of these genes in the root was generally higher than in other
which were highly expressed in multiple tissues. For example, BnO­                       tissues while expression in siliques was relatively low. It can be
SCA3.1a and BnOSCA3.1c, which had the highest expression in roots,                       concluded that the BnOSCA genes may play a role primarily in the root.
followed by petals, sepals and stems, showed similar expression patterns
indicating that these two genes may have similar functions and may be
important for the development of these tissues in B. napus. Group II was

                                                                                     8
X. Zhang et al.                                                                                                                                  Gene 856 (2023) 147137




Fig. 6. The synteny analysis of OSCA genes in B. napus. Red lines indicate duplicated OSCA gene pairs. Chromosome numbers are shown in the blue box. The name
and location of the OSCA gene is marked on the respective chromosome. The four colors represent the four clades of the OSCA genes, with brown, purple, green, and
red represent cladeI-IV, respectively. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)


3.7. Expression profiles of the OSCAs under cold and osmotic stresses                  stresses (more than 5-fold compared to control), indicating that they
                                                                                       may be common key genes in different stress-specific regulatory net­
    We used the published RNA-seq data (Zhang et al., 2019) to perform                 works. Meanwhile, BnOSCA1.1a and BnOSCA1.1b in Clade I had rela­
an initial screen of B. napus OSCA genes in response to stress to under­               tively high expression levels under different stresses, and their
stand the possible functions of OSCA proteins. The expression profiles of              expression patterns were very similar. After dehydration for 1 h, genes
BnOSCA genes under cold and osmotic stresses (dehydration, ABA and                     with higher expression levels were BnOSCA3.1c, BnOSCA3.1a, BnO­
NaCl) from the published data were analyzed. The OSCA gene family in                   SCA2.2b, BnOSCA1.1a and BnOSCA1.1b. These genes may be involved in
rapeseed was differentially expressed under different stresses, which                  the early rapeseed response to drought stress. The BnOSCA1.1a and
indicted a functional divergence of BnOSCAs in B. napus (Fig. 9). In                   BnOSCA1.1b in Clade I along with BnOSCA3.1c had relatively higher
general, OSCA genes in the same clade often showed similar expression                  expression levels at 4 h after ABA treatment. This is not surprising as
patterns. For example, the expression patterns of BnOSCA2.1a, BnO­                     both BnOSCA1.1a and BnOSCA1.1b promoters contained a higher
SCA2.1c, and BnOSCA2.1d in clade II were similar under different                       number of ABREs. Following NaCl treatment for 4 h, BnOSCA3.1a and
stresses, indicating that genes with close evolutionary relationships                  BnOSCA3.1c in clade III and BnOSCA1.1a and BnOSCA1.1b in clade I
frequently retained some similar functions. However, genes in the same                 exhibited higher expression levels, indicating that these genes may be
clade also had functional diversity (Yoshida et al., 2014), for example, in            the required to respond to the early stages of salt stress. Many induced
clade I, BnOSCA1.1a and BnOSCA1.1b responded to different stresses                     genes were expressed at a higher level in the early stage of stress, rather
and BnOSCA1.6d responded to early cold stress; however, the majority                   than in the later stage. For example, the expression levels of BnO­
of OSCA genes in clade I were not expressed or expressed at very low                   SCA1.1a and BnOSCA1.1b after 1 h of dehydration were higher than that
levels under these stresses. More than half (26/41) of OSCA genes were                 at 8 h, and the expression levels at 4 h of cold stress, ABA treatment and
up regulated in response to one or more treatments. Notably, BnO­                      NaCl stress were also higher than that at 24 h. Taken together, this
SCA3.1a and BnOSCA3.1c in Clade III, which were highly expressed in                    implies that proteins encoded by OSCA genes may play a crucial role in
different tissues, also showed highest expression levels under different               the early response of plants to abiotic stress. The expression level of


                                                                                   9
X. Zhang et al.                                                                                                                                     Gene 856 (2023) 147137




Fig. 7. Expression profiles of B. napus OSCA genes in different tissues. (A) Heatmap representation and hierarchical clustering of OSCA genes in different tissues. The
three groups (I, II, III) are labeled at the outermost circle. Expression data were processed with log2 normalization. The color scale represents relative expression
levels from low (blue color) to high (red color). (B) Number of OSCA genes that were expressed in different tissues. (For interpretation of the references to color in this
figure legend, the reader is referred to the web version of this article.)



                                                                                    10
X. Zhang et al.                                                                                                                             Gene 856 (2023) 147137




Fig. 8. qRT-PCR analysis of BnOSCA genes expression patterns in roots, stems, leaves, siliques, and buds. The error bars represent standard deviations. The y-axis
represents relative expression levels and x-axis represents the different tissues of ZS11.


BnOSCA1.6b was higher after 4 h of cold stress, but lower when exposed              proteins were mainly involved in oligopeptide transport, transporter
to other stress conditions and time points, suggesting that the gene                activity, positive regulation of catalytic activity, peroxidase activity and
product may be involved in the early rapeseed response to cold stress.              other functions (Fig. 11C). It was worth noting that the response-to-
    We further analyzed the expression of nine representative OSCA                  desiccation function was mainly enriched, further verifying that OSCA
genes under cold, dehydration, ABA and NaCl stresses in B. napus                    played important roles in the process of plant response to drought (Yuan
cultivar ZS11 by quantitative Real Time-PCR (qRT-PCR). The results                  et al., 2014).
showed that the expression profiles of the selected OSCA genes were
consistent with the analysis using previous published RNA-seq data                  4. Discussion
(Fig. 10), and it can be speculated that BnOSCA genes may be involved in
the early response to cold and osmotic stresses.                                        B. napus, an important oil crop planted worldwide, is often affected
                                                                                    by drought and other abiotic stresses during its growth and develop­
                                                                                    ment. Changes in osmotic pressure caused by drought stress and salt
3.8. Protein interaction network analysis of B. Napus OSCA family                   stress affect the osmotic balance of plants, leading to damage to the cell
members                                                                             membrane system and ultimately affect plant growth and yield (Ahanger
                                                                                    et al., 2018; Huang et al., 2015). OSCA is a calcium permeable cation
    To comprehensively and systematically analyze the function of OSCA              channel that induced by hypertonic stress. It regulates the concentration
gene-encoded proteins and the pathways involved at the molecular                    of calcium ions in cells under osmotic stress, subsequently causes the
level, we performed protein interaction network analysis for BnOSCA                 expression of stress-related genes in plant, and therefore participates in
genes in combination with GO and KEGG pathway enrichment analysis.                  the resistance of plants to osmotic stress such as drought stress (Stein­
The protein interaction network analysis showed that a total of 5802                horst and Kudla, 2013; Yuan et al., 2014).
proteins might interact with OSCAs in B. napus (Fig. 11A). Besides                      Members of the OSCA gene family play a very important role in the
interacting with other proteins, BnOSCAs could also interact with each              resistance of plants to osmotic stress (Yin et al., 2021). At present, there
other. According to the KEGG annotations of the interacting proteins,               is no systematic analysis of the OSCA gene family in B. napus. Further­
the first three enriched pathways were glycolysis/gluconeogenesis,                  more, the expression patterns of rapeseed OSCA genes under various
arginine and proline metabolism, proteasome and glycerolipid meta­                  osmotic-related stresses and the identity of the genes involved in plant
bolism (Fig. 11B). Previous studies had shown that proline played a                 tolerance to osmotic stress, remain unclear. To answer these questions,
pivotal role in plant osmotic adjustment where it was noted that proline-           this study identified and analyzed the OSCA genes in B. napus. In total,
related genes were highly expressed and a higher content of proline was             41 OSCA genes were identified in the B. napus genome, far more than the
evident in drought and high-salt environments (Furlan et al., 2020; Wu              number of OSCA gene family members in Arabidopsis (15), rice (11),
et al., 2018). GO enrichment analysis showed that OSCA interacting

                                                                               11
X. Zhang et al.                                                                                                                                Gene 856 (2023) 147137




Fig. 9. Heatmap of the expression of 41 OSCA genes under dehydration, cold, ABA and NaCl treatment at 4 h and 24 h. Expression data were processed with log2
normalization. The color scale represents relative expression levels from low (blue color) to high (red color). (For interpretation of the references to color in this
figure legend, the reader is referred to the web version of this article.)


soybean (21) and Vigna radiata (13). This suggested that the OSCA                     clade may have functional differentiation.
family had undergone a significant expansion in rapeseed, which was                       The expression profile analysis of OSCAs provided vital clues to
mainly caused by whole genome duplication during evolution. Phylo­                    determine their function and facilitated the understanding of their
genetic relationship analysis divided BnOSCAs into four clades, which                 possible role(s) during osmotic stress. In this study, OSCA gene expres­
was consistent with previous studies (Ganie et al., 2017; Li et al., 2017;            sion was induced by various osmotic stresses triggered by ABA, NaCl and
Yin et al., 2021; Yuan et al., 2014). Each clade/subclade contained OSCA              dehydration. Previous studies had also reported that the AtOSCA and
members of B. napus as well as Arabidopsis homologs indicating that the               OsOSCA families responded to osmotic stress (drought) (Hou et al.,
OSCA family was conserved between Arabidopsis and B. napus. However,                  2014; Li et al., 2015). Furthermore, we showed that OSCAs in B. napus
in B. napus, the homologous gene numbers for each AtOSCA were less                    were also induced by cold stress, implying the BnOSCAs may be involved
than six, which implied that gene loss also happened during the                       in the response to cold stress. Overall, this family of proteins was very
evolution.                                                                            important for regulating plant stress, which was also reflected in the
    Analysis of the conserved motifs highlighted that the motif compo­                GO/KEGG enrichment results for OSCA interacting proteins. Members of
sition of OSCAs in the same clade were highly conserved, consistent with              the OSCA family in B. napus showed different expression patterns in
their close evolutionary relationship. The two OSCAs (BnOSCA4.1a and                  different stress treatments and different tissues, suggesting that different
BnOSCA4.1b) in clade IV contained only four conserved motifs, and their               OSCAs might have diverse functions. BnOSCA3.1a and BnOSCA3.1c
pattern of conserved motifs was also significantly different from the                 responded strongly to several different osmotic stresses (NaCl, ABA and
OSCA proteins in the other branches. Both genes were expressed at                     dehydration), implying that the signal regulation pathways of plants
lower levels in different tissues and when exposed to various stresses,               corresponding to different osmotic stresses may be interrelated (Wang
suggesting that the OSCA genes in Clade IV may encode for proteins that               et al., 2003) and that the two genes may be the key mediators in the
have lost their function over the process of evolution. In particular, there          complex signaling network of osmotic stress in B. napus. Interestingly,
were also differences in the conservative motifs contained in OSCA                    these two genes not only responded to different stresses, but also had
proteins in the same clade. For example, four genes (BnOSCA2.3a,                      higher expression levels in different tissues, indicating that the two
BnOSCA2.3b, BnOSCA2.3c, BnOSCA2.3d) in clade II contained motif 12                    OSCA genes may play an indispensable role in plant growth and
which was not existed on other genes in the same clade. In particular, the            development along with responses to stress. Further functional studies
motif composition of BnOSCA2.3b was different form other genes in the                 on these two genes are needed to provide a detailed understanding of
BnOSCA2.3 gene cluster, which indicated that OSCA genes in the same                   OSCA protein function(s). The expression of OSCA genes was generally


                                                                                 12
X. Zhang et al.                                                                                                                          Gene 856 (2023) 147137




Fig. 10. qRT-PCR analysis of BnOSCA genes expression under cold and osmotic stresses (dehydration, ABA and NaCl). The error bars represent standard deviations.
The y-axis represents relative expression levels and x-axis represents different stresses of ZS11.


higher in roots, suggesting that the root may be an important organ for                A total of 42 duplicated OSCA gene pairs were identified in the
OSCA gene to sense osmotic stress. Previous research also indicated that           B. napus genome, signifying that there was much duplication in the
roots are the important organs which sense osmotic stress and it can               OSCAs gene family. All Ka/Ks values of the duplicated BnOSCA genes
response to abiotic stresses such as water deficit, salinity, or hypoxia           were less than 1 indicating that the OSCA family genes in B. napus were
(Kreszies et al., 2018, 2019). Many protective genes in response to os­            subject to purification selection pressure during evolution. Since puri­
motic stress were expressed highly in root by osmotic stress such as               fication selection limited gene differentiation, it can be inferred that the
proline dehydrogenase (ProDH) gene, trehalose phosphate synthases                  duplicated OSCA genes in B. napus were relatively conserved in evolu­
(TPS) genes and trehalose phosphate phosphatases (TPP) genes (Yang                 tion and may have similar functions (Liu et al., 2014). For example,
et al., 2016). Analysis of cis-acting elements in the promoters of OSCAs           BnOSCA3.1a and BnOSCA3.1c had similar expression patterns under
combined with gene expression analysis suggested that OSCA genes                   various stresses and in different tissues. The expression patterns of the
containing stress response elements often responded to stress. For                 duplicated gene pairs BnOSCA1.1a/BnOSCA1.1b and BnOSCA2.2a/
example, BnOSCA3.1a (containing the hormone response element ABRE                  BnOSCA2.2b under different stresses were also similar verifying that the
in its promoter) was expressed significantly higher after 24 h of ABA              duplicated OSCA gene retained some similar functions. However, there
treatment when compared to the other OSCA genes. Similarly, the                    were also different gene expression patterns in duplicated gene pairs.
expression level of BnOSCA1.1a (also containing the ABRE element) was              For example, BnOSCA2.3d did not express under various stresses, while
also higher after 4 h of ABA treatment. BnOSCA1.1b, which contained a              BnOSCA2.3b expressed at 8 h under dehydration stress, indicating that
large number of the MBS stress response elements, responded to various             duplicated genes of OSCA may have functionally differentiated after
osmotic stresses (NaCl, ABA, and dehydration) and cold stress. This                duplication to improve the plant’s response to stress (Adams, 2007).
indicated that the stress-induced genes might respond to abiotic stress
by the cis-acting regulatory elements found within the promoters.                  5. Conclusions
Interestingly, the expression levels of BnOSCA3.1c (without ABRE ele­
ments) at 4 h and 24 h after ABA treatment were much higher than that                 In this study, genome-wide identification and characterization of
of BnOSCA2.1d, which was driven by a promoter that contained the                   OSCA genes were performed for B. napus. A total of 41 OSCA genes were
greatest number of ABRE response elements. This high expression of                 identified in the genome of B. napus, which were then divided into four
BnOSCA3.1c may have been due to the presence of four CGTCA-motif                   clades with gene structures and motifs relatively conserved within the
hormone-related elements in the promoter. Therefore, we speculate                  same clade. Protein interaction analysis showed that OSCA proteins
that different hormone response elements have cooperative effects.                 were indeed involved in the plant response to abiotic stresses. Infor­
Interestingly, BnOSCA1.4a, which contains four MBS stress response                 mation on cis-elements within the OSCA gene promoters together with
elements, did not express when faced with various stresses, indicating             the expression patterns of BnOSCA in different tissues and towards
that this OSCA gene’s response to stress did not entirely depend on the            various abiotic stresses revealed that several candidate OSCA proteins
elements contained in the gene promoter.                                           were responsible for the response to various stresses. Overall, these


                                                                              13
X. Zhang et al.                                                                                                                            Gene 856 (2023) 147137




Fig. 11. Protein interaction network of OSCA family members and enrichment analysis in B. napus. A. Protein interaction network of OSCA family members in
B. napus. Red dots indicate OSCAs in B. napus, blue dots indicate other proteins, green lines indicate the relationship between OSCAs and gray lines indicate the
relationship between OSCAs and other proteins. B. KEGG pathway enrichment of proteins interacting with B. napus OSCAs. C. GO enrichment of proteins interacting
with B. napus OSCAs. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)


findings have provided an important basis for further revealing the                 and Technology Project (2020NY-068), Shaanxi University of Technol­
biological functions and molecular mechanisms of OSCA genes of                      ogy talent startup project (SLGRCQD2115) and Scientific Research
B. napus important for plant growth, development and in response to a               Program Funded by Shaanxi Provincial Education Department (grant
variety of abiotic stresses. Collectively, the knowledge would assist in            number 11JS034).
the cultivation of new B. napus varieties that are resistant to osmotic
stress.                                                                             Ethical approval

Funding information                                                                    This article does not contain any studies with human participants or
                                                                                    animals performed by any of the authors.
    This study was funded by Shaanxi Provincial Department of Science

                                                                               14
X. Zhang et al.                                                                                                                                                       Gene 856 (2023) 147137


CRediT authorship contribution statement                                                            Huang, Z.N., Tang, J., Duan, W.K., et al., 2015. Molecular evolution, characterization,
                                                                                                         and expression analysis of SnRK2 gene family in Pak-choi (Brassica rapa ssp.
                                                                                                         chinensis). Front. Plant Sci. 6, 1–13.
   Xiaojuan Zhang: Conceptualization, Writing – original draft,                                     Ingram, J., Bartels, D., 1996. The molecular basia of dehydration tolerance in plants.
Funding acquisition. Xiaohui Cheng: Writing – original draft, Software.                                  Ann. Rev. Plant. Physiol. Mol. Bio. 47, 377.
Chenlu Zhang: Writing – review & editing. Xiuqi Ma: Methodology,                                    Knight, H., Trewavas, A.J., Knight, M.R., 1997. Calcium signalling in Arabidopsis thaliana
                                                                                                         responding to drought and salinity. Plant J. 12, 1067–1078.
Software. Yu Zhang: Methodology. Jianmin Song: Writing – review &                                   Kreszies, T., Shellakkutti, N., Osthoff, A., et al., 2018. Osmotic stress enhances
editing. Meili Xie: Conceptualization, Writing – review & editing,                                       suberization of apoplastic barriers in barley seminal roots: analysis of chemical,
Methodology.                                                                                             transcriptomic and physiological responses. New Phytol. 221, 180–194.
                                                                                                    Kreszies, T., Eggels, S., Kreszies, V.i., et al., 2019. Seminal roots of wild and cultivated
                                                                                                         barley differentially respond to osmotic stress in gene expression, suberization, and
                                                                                                         hydraulic conductivity. Plant Cell Environ. 43, 344–357.
Declaration of Competing Interest                                                                   Krzywinski, M., Schein, J., Birol, I., et al., 2009. Circos: an information aesthetic for
                                                                                                         comparative genomics. Genome Res. 19, 1639–1645.
    The authors declare that they have no known competing financial                                 Kumar, S., Stecher, G., Tamura, K., 2016. MEGA7: Molecular evolutionary genetics
                                                                                                         analysis version 7.0 for bigger datasets. Mol. Biol. Evol. 33, 1870–1874.
interests or personal relationships that could have appeared to influence                           Larkin, M.A., Blackshields, G., Brown, N.P., et al., 2007. Clustal W and clustal X ver. 2.0.
the work reported in this paper.                                                                         Bioinformatics 23, 2947–2948.
                                                                                                    Lescot, M., Déhais, P., Thijs, G., et al., 2002. PlantCARE, a database of plant cis-acting
                                                                                                         regulatory elements and a portal to tools for in silico analysis of promoter sequences.
Acknowledgements                                                                                         Nucleic Acids Res. 30, 325–327.
                                                                                                    Li, Y., Dong, C.H., Hu, M., et al., 2019. Identification of flower-specific promoters
                                                                                                         through comparative transcriptome analysis in Brassica napus. Int. J. Mol. Sci. 20,
    We thank Dr. Zhixian Qiao of the Analysis and Testing Centre of
                                                                                                         5949.
Institute of Hydrobiology, Chinese Academy of Sciences for technical                                Li, Y., Yuan, F., Wen, Z., et al., 2015. Genome-wide survey and expression analysis of the
supports in RNA-seq analysis. The authors would like to express their                                    OSCA gene family in rice. BMC Plant Biol. 15, 261.
gratitude to EditSprings (https://www.editsprings.cn) for the expert                                Li, J.W., Yang, J.K., Jia, B.W., et al., 2017. Evolution and expression analysis of OSCA
                                                                                                         gene family in soybean. Oil Crop Science. 39, 589–599.
linguistic services provided.                                                                       Liedtke, W.F., Choe, Y., Martí-Renom, M.A., et al., 2000. Vanilloid receptor-related
                                                                                                         osmotically activated channel (VR-OAC), a candidate vertebrate osmoreceptor. Cell.
                                                                                                         103, 525–535.
Appendix A. Supplementary material
                                                                                                    Livak, K.J., Schmittgen, T.D., 2001a. Analysis of relative gene expression data using real-
                                                                                                         time quantitative PCR and the 2–DDCT method. Methods 25, 402–408.
   Supplementary data to this article can be found online at https://doi.                           Liu, W., Li, W., He, Q.L., et al., 2014. Genome-wide survey and expression analysis of
                                                                                                         calcium-dependent protein kinase in Gossypium raimondii. Plos One 9, e98189.
org/10.1016/j.gene.2022.147137.
                                                                                                    Liu, X., Wang, J., Sun, L., 2018. Structure of the hyperosmolality-gated calcium-
                                                                                                         permeable channel OSCA1.2. Nat. Commun. 9, 5060.
References                                                                                          Liu, Y.H., Li, H.Y., Shi, Y.S., et al., 2009. A maize early responsive to dehydration gene,
                                                                                                         ZmERD4, provides enhanced drought and salt tolerance in Arabidopsis. Plant Mol.
                                                                                                         Biol. Rep. 27, 542–548.
Ahanger, M.A., Alyemeni, M.N., Wijaya, L., et al., 2018. Potential of exogenously sourced
                                                                                                    Livak, K.J., Schmittgen, T.J.M., 2001. Analysis of relative gene expression data using
     kinetin in protecting solanum lycopersicum from nacl-induced oxidative stress
                                                                                                         real-time quantitative PCR and the 2-DDCt method. 25, 402–408.
     through up-regulation of the antioxidant system, ascorbate-glutathione cycle and
                                                                                                    Lv, G.D., 2015. Cloning, molecular markers and function of the gene TaOSCA1.4 in
     glyoxalase system. PLoS One 13, e0202175.
                                                                                                         common wheat. Thesis for M.S., Shandong Agricultural University, ShanDong,
Adams, K.L., 2007. Evolution of duplicate gene expression in polyploid and hybrid
                                                                                                         China.
     plants. J. Hered. 98, 136–141.
                                                                                                    McAinsh, M.R., Pittman, J.K., 2009. Shaping the calcium signature. New phytol. 181,
Arnadóttir, J., Chalfie, M., 2003. Eukaryotic mechanosensitive channels. Adv. Protein
                                                                                                         275–294.
     Chem. 63, 177.
                                                                                                    Podia, V., Milioni, D., Martzikou, M., et al., 2017. The role of Arabidopsis thaliana RASD1
Bailey, T.L., Johnson, J., Grant, C.E., et al., 2015. The MEME Suite. Nucleic Acids Res.
                                                                                                         gene in ABA-dependent abiotic stress response. Plant Biol. 20, 235–249.
     43, W39–W49.
                                                                                                    Rai, A., Suprasanna, P., D ’Souza, S.F., et al., 2012. Membrane topology and predicted
Bartels, D., Sunkar, R., 2005. Drought and salt tolerance in plants. Crit. Rev. Plant Scic.
                                                                                                         RNA-binding function of the ’early responsive to dehydration (ERD4)’ plant protein.
     24, 23–58.
                                                                                                         Plos One 7, e32658.
Batistic, O., Kudla, J., 2012. Analysis of calcium signaling pathways in plants. BBA-GEN
                                                                                                    Reguera, M., Bassil, E., Blumwald, E., 2014. Intracellular NHX-type cation/H+
     Subjects 1820, 1283–1293.
                                                                                                         antiporters in plants. Mol Plant. 7, 261–263.
Booth, I.R., Edwards, M.D., Black, S., et al., 2007. Mechanosensitive channels in bacteria:
                                                                                                    Shannon, P., Markiel, A., Ozier, O., et al., 2003. Cytoscape: a software environment for
     signs of closure? Nat. Rev. Microbiol. 5, 431–440.
                                                                                                         integrated models of biomolecular interaction networks. Genome Res. 13,
Cao, L.R., Zhang, P.Y., Lu, X.M., et al., 2020. Systematic analysis of the maize OSCA
                                                                                                         2498–2504.
     genes revealing ZmOSCA family members involved in osmotic stress and
                                                                                                    Shavrukov, Y., 2013. Salt stress or salt shock: which genes are we studying? J. Exp. Bot.
     ZmOSCA2.4 confers enhanced drought tolerance in transgenic Arabidopsis. Int. J.
                                                                                                         64, 119–127.
     Mol. Sci. 21, 351.
                                                                                                    Shinozaki, K., Yamaguchi-Shinozaki, K., 2000. Molecular responses to dehydration and
Camargo, S.R., Cançado, G.M., Ulian, E.C., et al., 2007. Identification of genes responsive
                                                                                                         low temperature: differences and cross-talk between two stress signaling pathways.
     to the application of ethanol on sugarcane leaves. Plant Cell Rep. 26, 2119–2128.
                                                                                                         Curr. Opin. Plant Biol. 3, 217–223.
Chalhoub, B., Denoeud, F., Liu, S., et al., 2014. Early allopolyploid evolution in the post-
                                                                                                    Stanley, L., Isabelle, L., 2015. How can we take advantage of halophyte properties to
     neolithic Brassica napus oilseed genome. Science 345, 950–953.
                                                                                                         cope with heavy metal toxicity in salt-affected areas? Ann. Bot. 3, 509.
Chao, J.T., Li, Z.Y., Sun, Y.H., et al., 2021. MG2C: a user-friendly online tool for drawing
                                                                                                    Steinhorst, L., Kudla, J., 2013. Calcium - a central regulator of pollen germination and
     genetic maps. Mol Hortic. 1–16.
                                                                                                         tube growth. BBA-Mol. Cell Res. 1833, 1573–1581.
Chen, C.J., Chen, H., Zhang, Y., et al., 2020. TBtools: An integrative toolkit developed for
                                                                                                    Wang, D.P., Zhang, Y.B., Zhang, Z., et al., 2010. KaKs_Calculator 2.0: a toolkit
     interactive analyses of big biological data. Mol. Plant. 13, 1194–1202.
                                                                                                         incorporating gamma-series methods and sliding window strategies. Genom.
Ding, S.C., Feng, X., Du, H.W., et al., 2019. Genome-wide analysis of maize OSCA family
                                                                                                         Proteom. Bioinf. 8, 77–80.
     members and their involvement in drought stress. Peer J. 7, e6765.
                                                                                                    Wang, W.X., Vinocur, B., Altman, A., 2003. Plant responses to drought, salinity and
Edgar, R.C., 2004. MUSCLE: multiple sequence alignment with high accuracy and high
                                                                                                         extreme temperatures: towards genetic engineering for stress tolerance. Planta. 218,
     throughput. Nucleic Acids Res. 32, 1792–1797.
                                                                                                         1–14.
Fujita, Y., Fujita, M., Shinozaki, K., et al., 2011. ABA-mediated transcriptional regulation
                                                                                                    Wang, Y.P., Tang, H.B., Debarry, J.D., et al., 2012. MCScanX: a toolkit for detection and
     in response to osmotic stress in plants. J Plant Res. 124, 509–525.
                                                                                                         evolutionary analysis of gene synteny and collinearity. Nucleic Acids Res. 40, e49.
Furlan, A.L., Bianucci, E., Giordano, W., et al., 2020. Proline metabolic dynamics and
                                                                                                    Wu, Z., Liang, J.H., Wang, C.P., et al., 2018. Overexpression of lily HsfA3s in Arabidopsis
     implications in drought tolerance of peanut plants. Plant Physiol. Bioch. 151,
                                                                                                         confers increased thermotolerance and salt sensitivity via alterations in proline
     566–578.
                                                                                                         catabolism. J. Exp. Bot. 69, 2005–2021.
Ganie, S.A., Pani, D.R., Mondal, T.K., 2017. Genome-wide analysis of DUF221 domain-
                                                                                                    Xu, Q.F., He, Q., Li, S., et al., 2014. Molecular characterization of StNAC2 in potato and
     containing gene family in Oryza species and identification of its salinity stress-
                                                                                                         its overexpression confers drought and salt tolerance. Acta Physiol. Plant. 36,
     responsive members in rice. Plos One 12, e0182469.
                                                                                                         1841–1851.
He, Z.L., Zhang, H.K., Gao, S.H., et al., 2016. Evolview v2: an online visualization and
                                                                                                    Yang, Y.C., Mo, Y.L., Yang, X.Z., et al., 2016. Transcriptome profiling of watermelon root
     management tool for customized and annotated phylogenetic trees. Nucleic Acids
                                                                                                         in response to short-term osmotic stress. PLoS One 11, e0166314.
     Res. 44, W236–W241.
                                                                                                    Yin, L.L., Zhang, M.L., Wu, R.G., et al., 2021. Genome-wide analysis of OSCA gene family
Hou, C.C., Wang, T., Kleist, T., et al., 2014. DUF221 proteins are a family of
                                                                                                         members in Vigna radiata and their involvement in the osmotic response. BMC Plant
     osmosensitive calcium-permeable cation channels conserved across eukaryotes. Cell
                                                                                                         Biol. 21, 408.
     Res. 24, 632–635.


                                                                                               15
X. Zhang et al.                                                                                                                                                      Gene 856 (2023) 147137

Yoshida, T., Mogami, J., Yamaguchi-Shinozaki, K., 2014. ABA-dependent and ABA-                       Yuan, F., Yang, H., Xue, Y., et al., 2014. OSCA1 mediates osmotic-stress-evoked Ca2+
    independent signaling in response to osmotic stress in plants. Curr. Opin. Plant Biol.               increases vital for osmosensing in Arabidopsis. Nature 514, 367–371.
    21, 133–139.                                                                                     Zhang, Y.T., Ali, U., Zhang, G.F., et al., 2019. Transcriptome analysis reveals genes
Yu, C.S., Chen, Y.C., Lu, C.H., et al., 2006. Prediction of protein subcellular localization.            commonly responding to multiple abiotic stresses in rapeseed. Mol. Breeding 39,
    Proteins 64, 643–651.                                                                                158.
Yu, G., Wang, L.G., Han, Y., et al., 2012. ClusterProfiler: an R package for comparing               Zhu, J.K., 2002. Salt and drought stress signal transduction in plants. Annu. Rev. Plant.
    biological themes among gene clusters. Omics 16, 284–287.                                            Biol. 53, 247–273.




                                                                                                16
