# Zhu_2025 - Genome-wide identification and characterization of OSCA gene

**Source PDF:** 

---

                                                                  South African Journal of Botany 178 (2025) 1827



                                                                   Contents lists available at ScienceDirect


                                                          South African Journal of Botany
                                                            journal homepage: www.elsevier.com/locate/sajb




Genome-wide identiﬁcation and characterization of OSCA genes in white
clover revealing their function in response to abiotic stresses
Xiaoyue Zhu, Manman Li, Shuaixian Li, Xueqing Zhao, Tianxiang Zhang, Meiyan Guo,
Changhong Guo, Yongjun Shu*
Key Laboratory of Molecular Cytogenetics and Genetic Breeding of Heilongjiang Province, College of Life Science and Technology, Harbin Normal University, Harbin
150025, PR China




A R T I C L E          I N F O                             A B S T R A C T

Article History:                                           White clover (Trifolium repens L.) is a signiﬁcant forage crop and landscaping plant, playing a vital role in
Received 2 April 2024                                      enhancing the biodiversity and stability of grassland ecosystems. However, its yield and quality are affected
Revised 9 December 2024                                    by cold and drought stress. OSCA (Hyperosmolality-Gated Calcium-Permeable Channels) is a calcium-perme-
Accepted 3 January 2025
                                                           able cation channel proteins, with OSCA family members playing an important role in responding to
Available online 13 January 2025
                                                           osmotic-related abiotic stresses. This study identiﬁed the OSCA gene family of white clover and analyzed
Edited by K. Dolezal                                       OSCA gene family have stronger resistance to cold and drought stress. Phylogenetic analysis has classiﬁed
                                                           these members into four groups. The members of each clade have similar gene structures, conserved motifs,
Keywords:
                                                           and domains. Analysis of cis-acting elements revealed that the TrOSCA genes have many cis-regulatory ele-
White clover
                                                           ments that are responsive to abiotic stress and hormonal signals such as ABRE, ARE, MBS, etc. To investigate
OSCA
                                                           the functions of TrOSCA in growth, development, and response to abiotic stresses, RNA-seq data from various
Abiotic stresses
Genetic regulation network                                 tissues and stress were analyzed. The results suggested that TrOSCA shows signiﬁcant expression under abi-
qRT-PCR                                                    otic stress. Moreover, tissue expression pattern analysis demonstrated that the TrOSCA genes had different
                                                           expression patterns in various tissues. qRT-PCR results showed that a signiﬁcant majority of the TrOSCA
                                                           genes responded to cold stress. This study plays a pivotal role in exploring the molecular mechanisms under-
                                                           lying white clover’s response to abiotic stresses, thereby building the framework for investigating the biolog-
                                                           ical functions and evolutionary processes of this gene family.
                                                              © 2025 SAAB. Published by Elsevier B.V. All rights are reserved, including those for text and data mining, AI
                                                                                                                                         training, and similar technologies.




1. Introduction                                                                                 and development caused by non-biological factors such as tem-
                                                                                                perature, drought, salinity, soil infertility, and heavy metal pollu-
    White clover (Trifolium repens L.) is a perennial herbaceous                                tion. These stresses typically limit plant photosynthesis, root
plant and a member of the Fabaceae family, is well known for its                                growth, and nutrient absorption, and in severe cases, they can
signiﬁcance in agronomy (Manier, Deram et al. 2009). One of the                                 lead to plant death. Many plants, such as wheat (Triticum aesti-
notable features of white clover is its ability to ﬁx nitrogen in the                           vum) and maize (Zea mays), exhibit physiological changes when
soil through its symbiotic relationship with nitrogen-ﬁxing bacte-                              exposed to these stresses, such as leaf water loss, stomatal clo-
ria. This makes it a valuable component of pastures and crop                                    sure, reduced photosynthetic efﬁciency, and changes in antioxi-
rotations, as it can improve soil fertility and reduce the need for                             dant enzyme activity (Jafari, Wang et al. 2024). In addition, salt
synthetic fertilizers (Manier, Deram et al. 2009). White clover is                              stress can cause an imbalance in the ion concentration within the
subject to various abiotic stresses during growth, which can sig-                               plant, inhibiting growth and development. These studies demon-
niﬁcantly impact its production and spread (Santangelo, Battlay                                 strate that abiotic stress has a widespread and profound impact
et al. 2023). Abiotic stress refers to the impact on plant growth                               on plants. Therefore, investigating how white clover response to
                                                                                                abiotic stress has become a crucial area of scientiﬁc research.
                                                                                                    Calcium ions (Ca2+), as crucial secondary messengers in plants, are
  * Corresponding author at: College of Life Science and Technology, Harbin Normal              essential in regulating both plant growth, development, and
University, NO.1 Shida Road, Harbin 150025, Heilongjiang, PR China.                             responses to abiotic stress. In non-stimulated cells, the capacity typi-
    E-mail addresses: zhuxiaoyue2001@126.com (X. Zhu), limanman1208@stu.hrbnu.
                                                                                                cally ranges around (Ko  €ster, DeFalco et al. 2022). However, upon
edu.cn (M. Li), hsdlsx1201@stu.hrbnu.edu.cn (S. Li), zhaoxq1109@126.com (X. Zhao),
hsdztx@stu.hrbnu.edu.cn      (T.   Zhang),     Guomeiyan@163.com       (M.   Guo),
                                                                                                stimulation, it increases approximately 10 times to a low level -mM
kaku3008@hrbnu.edu.cn (C. Guo), shuyj@hrbnu.edu.cn (Y. Shu).                                    level. One proposed mechanism for this increase in [Ca2+]cyt is the

https://doi.org/10.1016/j.sajb.2025.01.005
0254-6299/© 2025 SAAB. Published by Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.
X. Zhu, M. Li, S. Li et al.                                                                                    South African Journal of Botany 178 (2025) 1827


"opening mechanism" (Miao, Li et al. 2022). Effectively using it as a           database, served as the query sequence to identify OSCA family
signaling system requires restoring it to its pre-stimulation level, a          members in white clover. BLAST searches were then conducted
process achieved through the "shutdown mechanism" (Yang, Zhu                    against the white clover protein database using the AtOSCA pro-
et al. 2022). In plants, there are several important calcium ion chan-          tein sequence, with a threshold set at an e-value 1 £ 105 (Alt-
nel proteins. For example, the CNGC (Cyclic Nucleotide-Gated Chan-              schul, Madden et al. 1997). The Hidden Markov Model ﬁle (version
nel) family, which is involved in the formation of calcium ion                  3.3) (PF02714) corresponding to DUF221 was downloaded from the
channels in the cell membrane, plays a crucial role in signal transduc-         Pfam database (Mistry, Chuguransky et al. 2021). HMMER3.1 was
tion and response to environmental stress (Breeze 2019). The GLR                applied to identify and validate candidate OSCA proteins within the
(Glutamate Receptor-Like) family is responsible for regulating the              white clover genome, thereby identifying members of the OSCA
concentration of calcium ions inside plant cells and is associated with         gene family (Finn, Clements et al. 2011). Annotation details for all
the opening and closing of calcium ion channels (Krzeszowiec, Lew-              candidate OSCA genes, such as genomic location, protein length,
andowska et al. 2023). ACA (AutoinhibitedCa2þ ATPase) is a calcium              and intron numbers, were derived from the white clover genome.
pump that participates in the transport and regulation of calcium               Then, white clover OSCA genes were classiﬁed into groups based on
ions within plant cells and the recently discovered high osmolarity-            their similarity to OSCA genes in Arabidopsis.
gated calcium-permeable channels (OSCAs).
    The OSCA gene family is a group of genes found in eukaryotic                2.2. Phylogenetic analysis of the TrOSCA genes
organisms, characterized by the presence of a conserved domain
known as DUF221 (Domain of Unknown Function 221) (Chakraborty,                      White clover OSCA protein sequences were aligned through MUS-
Gangwar et al. 2023). They can induce an increase in Ca2+concentra-             CLE (version 5.1.0), using its default parameters (Edgar 2004).
tion by sensing changes in extracellular osmotic potential, thereby             MEGA11 was used to construct phylogenetic trees, through the
regulating osmotic potential. OSCA proteins are considered to be                Neighbor-Joining (NJ) method, and supported by 1000 bootstrap rep-
osmosensors in both plants and animals, playing a crucial role in per-          licates (Tamura, Stecher et al. 2021). This analysis informed the sys-
ceiving changes in osmotic conditions from both external and inter-             tematic classiﬁcation of the TrOSCA genes into distinct groups,
nal sources, and in regulating plant growth, development, and                   reﬂecting the phylogenetic relationships identiﬁed between the
reproduction (Ding, Feng et al. 2019). The gene family was ﬁrst dis-            AtOSCA and TrOSCA sequences.
covered in Arabidopsis thaliana (L.), containing 15 family members
with highly conserved amino acid sequences, all have the DUF221                 2.3. Conserved motif analysis of TrOSCA proteins
domain associated with plant stress responses (Zhai, Wen et al.
2021). In Arabidopsis, a membrane-integrated protein gene                           Using MEME (https://meme-suite.org/meme/tools/meme) to
                                                        2+
(AtOSCA1.2) identiﬁed can increase intracellular Ca concentration               identify conserved motifs in TrOSCA protein sequences, a MEME
under hyperosmotic stress and shows some permeability to K+ and                 search was performed on speciﬁed TrOSCA protein sequences, with
Na+(Zhang, Wang et al. 2018). In tomato (Solanum lycopersicum Mill.),           the maximum number of different motifs set to 10 (Bailey, Boden
there are 12 OSCA family members, among which SlOSCA9 and                       et al. 2009). Gene structure analysis was conducted using the white
SlOSCA10 can respond to drought, salt and ABA (Miao, Li et al. 2022).           clover genome annotation ﬁle, and the results were visualized using
In soybean (Glycine max Merrill), 21 family members have been iden-             TBtools (Chen, Chen et al. 2020).
tiﬁed, with GmOSCA3.2 showing the highest expression in ﬂowers,
leaves, and roots under drought stress; while GmOSCA3.1 is most                 2.4. Analysis of promoter Cis-acting element of TrOSCA gene family
notably upregulated under alkaline stress (Zhou, Guo et al. 2016). In           members
rice (Oryza sativa L.), ABA, NaCl, and PEG treatments can induce dif-
ferential expression of 10 OsOSCA genes, among which OsOSCA3.1 has                  Using TBtools, the upstream 2000 bp gene sequences of the
been identiﬁed as the OsERD4 gene (Li, Yuan et al. 2015). In Barley             TrOSCA gene family were extracted and their corresponding CDS
(Hordeum vulgare L.), a total of 13 HvOSCAs have been identiﬁed, all            ﬁles were retained (Chen, Chen et al. 2020). These CDS ﬁles were
of which are signiﬁcantly induced by drought, cold, salt, and ABA               then submitted to the PlantCare online tool (http://bioinformat
treatments, indicating their role in osmotic regulation (She, Pan et al.        ics.psb.ugent.be/webtools/plantcare/html/) to identify cis-acting
2022). In summary, OSCA genes play crucial roles in plant adaptation            elements within the promoter regions, followed by visualization
to environments with high osmotic stress. Nonetheless, the response             using TBtools.
of OSCA gene family members to abiotic stress in white clover
remains largely unexplored.                                                     2.5. Chromosomal location and gene duplication of TrOSCA genes
    In this study, we systematically identiﬁed members of the OSCA
gene family and analyzed their phylogenetic relationships, promoter                Each protein from white clover was subjected to a BLASTP
regions, cis-acting elements, and tissue expression patterns. In addi-          (version 2.9.0+) analysis for comparison, with gene duplications
tion, the impact of cold stress on the OSCA gene family and the                 being identiﬁed and characterized through the MCSanX software
expression of the OSCA gene family in different tissues were analyzed           using default parameters (Lynch and Conery 2000; Wang, Tang
using qRT-PCR and publicly available transcriptomic data. Some OSCA             et al. 2012). The genomic localization and duplication events of
genes in white clover showed differential expression under various              OSCA genes within the white clover genome were visually repre-
abiotic stresses, laying the groundwork for further research into the           sented using CIRCOS (version 0.698), demonstrating the geno-
biological functions and evolutionary processes of the white clover             mic distribution of the OSCA gene family in white clover
OSCA gene family.                                                               (Krzywinski, Schein et al. 2009).

2. Materials and methods                                                        2.6. Analysis of gene regulatory network of TrOSCA gene family

2.1. Identiﬁcation and classiﬁcation of OSCA gene family in white clover            The information regarding the Arabidopsis gene regulatory net-
                                                                                work (GRN) was obtained from the AraNet database (V2), which
   The genome resources were kindly provided by Stig Uggerhøj                   encompasses Arabidopsis genes and their interactions (Lee, Yang
Andersen, Aarhus University (Grifﬁths, Moraga et al. 2019). The                 et al. 2015). The proteins of white clover were analyzed using BLAST
Arabidopsis OSCA protein sequence, obtained from the TAIR                       against the Arabidopsis collection, with an e-value cutoff of 1e-05
                                                                           19
X. Zhu, M. Li, S. Li et al.                                                                                          South African Journal of Botany 178 (2025) 1827


applied to identify highly similar gene pairs in white clover. Similarly,        was used for this analysis. The quality of the generated models was
Arabidopsis proteins were subjected to a BLAST search against the                assessed via the SAVES server (https://saves.mbi.ucla.edu/).
white clover proteins. The highest scoring matches were identiﬁed as
Arabidopsis homologs, and these mutually identiﬁed matches were                  3. Results and analysis
acknowledged as homologous pairs (Li, Zhang et al. 2023). Using
these pairs, a white clover GRN was constructed, reﬂecting the struc-            3.1. Identiﬁcation of OSCA gene in white clover
ture found in Arabidopsis. Cytoscape (version 3.10.1) was used to
identify and analyze sub-networks containing TrOSCA genes in white                   To identify white clover OSCA genes, HMMER and Pfam acces-
clover (Shannon, Markiel et al. 2003). In order to analyze the GO                sion (PF02714) were used to search for OSCA protein sequences
enrichment of these functional genes involved in GRN, topGO soft-                in the white clover genome database. Following the removal of
ware was used to assign GO annotations to these functional genes                 identical and incomplete gene sequences, a total of 26 OSCA
(Alexa and Rahnenfuhrer 2010).                                                   genes containing the conserved RSN1_7TM (PF02714) functional
                                                                                 domain were identiﬁed and named TrOSCA01-TrOSCA26. The
2.7. Expression analysis of TrOSCA gene in response to cold stress               detailed information of these genes is presented in Table 1,
                                                                                 including their names, gene loci, chromosomal positions, intron
    To analyze the expression patterns of white clover OSCA genes                numbers, and protein lengths (amino acid). Among the 26 TrOSCA
under cold and drought stress, as well as in various tissues, RNA-seq            genes, protein lengths ranged from 181aa to 1055aa, with
datasets were sourced from the NCBI SRA database, can be accessed                TrOSCA06 having the longest amino acid and TrOSCA19 the short-
using the accession numbers as follows: PRJNA781064,                             est. In addition, there is a wide range of intron distribution
PRJNA953427, and PRJNA523044 (Zoabi and Shomron 2021). The                       within TrOSCA genes, with TrOSCA13 having the most introns
RNA-seq reads were mapped to white clover transcript sequences                   (14), while TrOSCA25 does not contain any introns.
using the Salmon software (version 0.12.0), which also facilitated the
calculation of gene expression levels (FPKM values). Additionally, the           3.2. Classiﬁcation and phylogenetic analysis of white clover
R programming language was used to visualize the data (Patro, Dug-
gal et al. 2017).                                                                    A neighbour-joining (NJ) method was used to construct a phylo-
                                                                                 genetic tree to investigate the evolutionary relationships among
2.8. Plant materials and stress treatments                                       OSCA proteins. As shown in Fig. 1, the 26 OSCA proteins were
                                                                                 grouped into four clades, named I, II, III and IV. Notably, the number
   White clover (Haifa) seeds were sown in pots prepared with a                  of clade II proteins was the highest with a total of 14 proteins, fol-
nurturing blend of perlite and vermiculite, adhering to a 3:1 ratio              lowed by clade I with 8 proteins. Conversely, clades III and IV con-
to ensure optimal aeration and moisture retention conducive to                   sisted of only two members each.
seed germination and root development (Li, Zhang et al. 2023).
The plants were grown for four weeks under a 14-hour light cycle                 3.3. Analysis of motif composition distribution of TrOSCA protein
at 24 °C and a 10-hour dark cycle at 18 °C. This cycle was com-
plemented by twice-daily irrigations, carefully timed to promote                    To conduct a comprehensive analysis of the conserved structure of
consistent soil moisture without the risk of over-saturation,                    TrOSCA proteins, ten conserved motifs in the white clover OSCA gene
thereby encouraging healthy plant growth. At the end of this                     family were identiﬁed using the MEME tool. This analysis helps to
period, the plants were randomly divided into seven groups for                   explore their functional characteristics, as shown in Fig. 2. The phylo-
cold stress trials. These groups were exposed to cold stress (4 °C)              genetic tree shows that TrOSCA can be broadly divided into four
for varying durations: 0, 0.5, 1, 3, 6, 12, and 24 h. Sampling took
place at each of these seven intervals, after which the samples
                                                                                 Table 1
were immediately frozen in liquid nitrogen and preserved at                      Summary of TrOSCA genes identiﬁed in the white clover.
80 °C for further analysis (Kaur, Sharma et al. 2022).
                                                                                   Name        Locus          Chromosomal locations       Group Intron Length(aa)

2.9. qRT-PCR analysis                                                              TrOSCA01    chr13.jg2801   Tr5P:19093032-19097797      1     10     756
                                                                                   TrOSCA02    chr5.jg1156    Tr5O:8144734-8150286        1     10     805
    At each time point, total RNA was isolated using the Total Plant               TrOSCA03    chr5.jg1399    Tr5O:9926116-9930999        1     10     787
                                                                                   TrOSCA04    chr5.jg5808    Tr5O:39043821-39048294      1     10     764
RNA Extraction Kit from Tiangen (Beijing, China), followed by the
                                                                                   TrOSCA05    chr7.jg3102    Tr7O:19543649-19549361      1     10     770
synthesis of cDNAs with the Prime Script RT kit by Toyobo (Shanghai,               TrOSCA06    chr7.jg5967    Tr7O:36850988-36856168      1     10     755
China). Primers for the TrOSCA genes were designed using Primer3                   TrOSCA07    chr7.jg6471    Tr7O:40140117-40144753      1     10     755
software and produced by Sangon Ltd (Shanghai, China), showed in                   TrOSCA08    chr8.jg8887    Tr8O:62557150-62562952      1     10     770
                                                                                   TrOSCA09    chr1.jg1030    Tr1O:7968455-7978276        2     13     852
Table S1 (Untergasser, Cutcutache et al. 2012). The qRT-PCR assays
                                                                                   TrOSCA10    chr1.jg7913    Tr1O:55189591-55194799      2     11     676
were conducted using the Light CyclerÒ 96 system by Roche (Rotk-                   TrOSCA11    chr12.jg3090   Tr4P:20549264-20553079      2     9      708
reuz, Switzerland), with the thermal cycling conditions set to: an ini-            TrOSCA12    chr13.jg1024   Tr5P:6682203-6687147        2     9      685
tial denaturation at 95 °C for 2 min, followed by 40 cycles of 95 °C for           TrOSCA13    chr13.jg4093   Tr5P:26778581-26787995      2     14     1055
30 s, 55 °C for 30 s, and 72 °C for 1 min (Espitia, Zhao et al. 2010).             TrOSCA14    chr14.jg228    Tr6P:1752827-1757683        2     9      710
                                                                                   TrOSCA15    chr14.jg249    Tr6P:1958925-1963785        2     9      710
Each sample underwent triplet tests, and the 2ΔΔCt method was uti-
                                                                                   TrOSCA16    chr14.jg3156   Tr6P:21323158-21328132      2     10     699
lized to assess the relative expression levels of the TrOSCA genes (Ma,            TrOSCA17    chr3.jg169     Tr3O:1078583-1082780        2     9      715
Bell et al. 2021).                                                                 TrOSCA18    chr4.jg3976    Tr4O:29062771-29066213      2     7      520
                                                                                   TrOSCA19    chr4.jg8665    Tr4O:61443482-61444408      2     2      181
                                                                                   TrOSCA20    chr6.jg1676    Tr6O:11470346-11476973      2     9      673
2.10. Homologous modeling of TrOSCA
                                                                                   TrOSCA21    chr6.jg1694    Tr6O:11620993-11627868      2     9      708
                                                                                   TrOSCA22    chr9.jg1174    Tr1P:8210439-8222141        2     13     775
    The 3D structures of the TrOSCA gene family members were pre-                  TrOSCA23    chr1.jg916     Tr1O:7110886-7114778        3     5      721
dicted through homology modeling, using the SWISS-MODEL server                     TrOSCA24    chr10.jg825    Tr2P:5631992-5637523        3     7      889
for homology-based protein structure prediction (https://www.                      TrOSCA25    chr1.jg3399    Tr1O:24590607-24593021      4     0      804
                                                                                   TrOSCA26    chr8.jg3810    Tr8O:27795077-27799479      4     1      643
string-db.org/) (Waterhouse, Bertoni et al. 2018). Intensive modelling
                                                                            20
X. Zhu, M. Li, S. Li et al.                                                                                                            South African Journal of Botany 178 (2025) 1827




Fig. 1. Phylogenetic analysis of white clover OSCA proteins.Note: The NJ tree was constructed from the amino acid sequences of TrOSCA using MEGA11 with 1000 bootstrap repli-
cates. The white clover OSCA proteins were grouped into four groups (Group I labeled as red solid circles, Group II labeled as green solid squares, Group III labeled as blue solid trian-
gles, and Group IV labeled as pink solid diamonds).




clades, as mentioned above. The results suggest that within the same                            response, is also widely present across the OSCA genes. In addition,
clade, TrOSCA members display similar patterns of gene structure dis-                           the drought response element MBS is found in all other OSCA genes
tribution. For example, all OSCA protein members within Clade I                                 except TrOSCA02, suggesting that the TrOSCA genes may play an
share the same number and arrangement of conserved motifs.                                      active role in regulating various stresses and plant hormone
                                                                                                responses.
3.4. Analysis of cis-acting elements in the TrOSCA gene promoters
                                                                                                3.5. Chromosomal mapping and gene duplication analysis of TrOSCA
   PlantCare was employed to analyze the cis-acting elements in the                             gene
promoters of TrOSCA genes. Fig. 3 shows that a variety of cis-acting
elements, totaling 19 different types, were predicted in the TrOSCA                                To investigate the evolutionary progress and spread of OSCAs in
genes. These elements have been found to play a role in several bio-                            white clover, MCScanX (Python version) and CIRCOS (version 0.69)
logical processes, including growth, hormone response and stress                                were used to map the chromosomal distribution of these genes. As
response. As shown in Fig. 3, all OSCA genes in white clover contain                            shown in Fig. 4, the 26 OSCA genes are unevenly distributed across 16
the cis-acting element ARE, associated with abiotic stress responses.                           chromosomes in white clover, with several TrOSCA genes located on
TrOSCA13 has the most number of ARE motifs, comparable to the                                   chromosomes 1O, 1P, 2P, 3O, 4O, 4P, 7O, and 8O. Based on the results
number in TrOSCA10. This observation might be related to the phylo-                             from BLAST, we identiﬁed 17 gene duplication events, which include
genetic tree, where members of the same group are likely to show                                3 tandem duplications and 14 segmental duplications. These results
more similarity in the distribution patterns of their cis-acting ele-                           suggest that chromosome duplication has been a factor in the expan-
ments. Furthermore, the ABRE element, linked to plant hormone                                   sion of the OSCA gene family in white clover.
                                                                                           21
X. Zhu, M. Li, S. Li et al.                                                                                                    South African Journal of Botany 178 (2025) 1827




Fig. 2. Distribution of conserved motifs in TrOSCA genes.Note: The conserved motifs in TrOSCA genes were identiﬁed and characterized using MEME software. Each colored box rep-
resents the putative motifs detected in the protein sequence.




3.6. Genetic regulatory network analysis of OSCA gene in white clover                      visualized through violin plots, as displayed in Figure S3. The
                                                                                           analysis revealed a pronounced response of TrOSCA to cold stress,
    Gene regulatory networks (GRNs) are increasingly vital for explor-                     subsequently conﬁrmed by hierarchical clustering and heatmap
ing the systemic functions of genes. Using a publicly available inter-                     visualization (Fig. 6a), aligning with the violin plot outcomes and
action database, we constructed GRNs for the TrOSCA gene family                            underlining the TrOSCA genes’ signiﬁcant role in adapting to cold
and its associated genes. The networks consist of three genes, namely                      environments. Notably, most genes peaked in expression at
TrOSCA10, TrOSCA23, and TrOSCA25, which exhibit interactions with                          30 min. Next, to delve into the TrOSCA genes’ expression pattern
15, 10, and 8 genes respectively, totaling 33 interactions. This                           under drought, we subjected three different white clover varieties
detailed mapping is depicted in Fig. 5. Gene ontology (GO) annota-                         to drought stress. As shown in Fig. 6b, compared to the control
tions for these interacting genes were obtained, and GO enrichment                         group, the OSCA gene expression levels were signiﬁcantly upregu-
analysis was conducted using the topGO package in the R platform.                          lated under drought conditions. Lastly, to explore the expression
The results, shown in Figure S2, highlight their predominant distribu-                     pattern of TrOSCA genes across tissues, we analyzed their expres-
tion in molecular function, indicating that these genes are primarily                      sion in eight different tissues (Fig. 6c), revealing that TrOSCA
associated with the organelle membrane.                                                    genes are relatively highly expressed in leaves. These ﬁndings
                                                                                           indicate tissue-speciﬁc expression of TrOSCA genes and their
3.7. Abiotic stress and expression analysis of TrOSCA gene in different                    important role in responding to abiotic stress.
tissues
                                                                                           3.8. qRT-PCR validation of TrOSCA genes in response to cold stress
   To further investigate the role of TrOSCA in growth and its
function under abiotic stress, we gathered RNA-seq data from                                   To conﬁrm their expression patterns during cold stress, we per-
various tissues and stress conditions. Since then, to explore the                          formed qRT-PCR analysis on nine TrOSCA genes at seven different
expression pattern of TrOSCA genes in response to cold, we                                 time points: 0, 0.5, 1, 3, 6, 12 and 24 h, with the results shown in
exposed white clover to cold stress at 4 °C and carried out RNA-                           Fig. 7. The qRT-PCR data conﬁrmed a signiﬁcant increase in the
seq analysis at eight distinct time points: 0 h, 30 min, 1 hour, 3                         expression of these TrOSCA genes when exposed to cold stress. The
h, 6 h, 12 h, 24 h, and 72 h. Their expression levels were                                 concordance between qRT-PCR results and transcriptome sequencing
                                                                                      22
X. Zhu, M. Li, S. Li et al.                                                                                                         South African Journal of Botany 178 (2025) 1827




            Fig. 3. Three types of cis-acting elements were identiﬁed in the promoter regions of TrOSCAs Note:Darker colors indicate higher numbers of cis-acting elements.




data supported the consistent up-regulation of TrOSCA genes follow-                            family in the white clover genome, showing a signiﬁcant
ing cold stress. This evidence suggests that TrOSCAs are actively                              response to stress. The phylogenetic analysis indicates that the
involved in the cold stress response and play an essential role in the                         TrOSCA family can be classiﬁed into four groups, consistent with
regulation of gene expression.                                                                 previous studies on Arabidopsis, maize, etc. (Li, Yuan et al. 2015;
                                                                                               Ding, Feng et al. 2019; Zhai, Wen et al. 2021). Further analysis
3.9. Homologous modeling of TrOSCA                                                             revealed that members of the clade III and clade IV groups of the
                                                                                               OSCA family are relatively few in number, but they have been
   Through the prediction of the tertiary structures of TrOSCA                                 conserved throughout the evolutionary process, suggesting that
proteins, we have acquired structural models for several mem-                                  they may play crucial roles in biological evolution.
bers including TrOSCA04, TrOSCA05, TrOSCA08, TrOSCA09,                                             The OSCA family possesses a highly conserved DUF221 domain
TrOSCA20, TrOSCA21, TrOSCA22, TrOSCA23, and TrOSCA24 (see                                      (Yin, Zhang et al. 2021). The DUF221 domain (Pfam accession num-
Fig. 8). The observed structural features reveal that these pro-                               ber: PF02714) is a presumed 7-transmembrane domain region of a
teins are rich in a-helices and b-turn structures, which are                                   putative phosphate transporter, potentially associated with plant
closely associated with their function as osmotic stress recep-                                responses to abiotic stresses such as cold (Bartels and Sunkar 2005).
tors. For instance, TrOSCA09 and TrOSCA20 exhibit complex                                      In this study, all 26 members of the OSCA family in white clover pos-
transmembrane regions that may be involved in transmembrane                                    sess the RSN1_7TM domain, consistent with studies on Arabidopsis
signal transmission. Additionally, TrOSCA04 and TrOSCA21 show                                  (Hill, Vance et al. 2023). Conservation motif analysis revealed that,
extended extracellular loops that could participate in protein-                                except for TrOSCA19, 25, and 26, the motif composition patterns and
protein interactions or ligand binding.                                                        sequence arrangements of the remaining white clover OSCA family
                                                                                               members are largely consistent. It is possible that the common ances-
4. Discussion                                                                                  tral gene already possessed this intron/exon structure. Although
                                                                                               introns do not contribute to the protein sequence, their relative posi-
   Genome-wide analyses of the OSCA gene families have been                                    tions provide clues for predicting the evolution of genes and their
carried out in many model plants, and research has shown that                                  corresponding proteins, further promoting the diversiﬁcation of gene
Arabidopsis thaliana has 15 members of the OSCA gene family,                                   families (Cao, Guo et al. 2019).
while tomatoes and tobacco contain 12 and 23 members, respec-                                      The transcriptional regulation of genes is controlled by the inter-
tively (Ashraﬁ-Dehkordi, Alemzadeh et al. 2018; Zhai, Wen et al.                               action between cis-acting elements and relevant transcription factors
2021). The OSCA gene families are widespread in diverse plants,                                in their upstream promoter sequences (Xiao, Zhang et al. 2023). Com-
and phylogenetic analysis suggests that the plant OSCA family                                  bining analysis of promoter cis-acting elements is helpful in predict-
proteins classiﬁed into four major clades in evolution (Yin, Zhang                             ing the functions of associated genes (Yamaguchi-Shinozaki and
et al. 2021). This study identiﬁed 26 members of the OSCA gene                                 Shinozaki 2005). In this study, it was found that anaerobic-induced
                                                                                          23
X. Zhu, M. Li, S. Li et al.                                                                                                    South African Journal of Botany 178 (2025) 1827




Fig. 4. Chromosomal distribution and gene duplication analysis of the TrOSCA genes in white clover.Note: All genes duplications were identiﬁed using MCSanX software, and they
were displayed using CIRCOS software. Red lines show duplications between members of the GroupⅠ;Green lines show duplications between members of the GroupⅣ;Blue lines
show duplications between members of the GroupⅡ;Purple lines show duplications between members of the GroupⅢ;Green lines show duplications between members of the
GroupⅣ.



cis-acting elements (ARE) are distributed in the upstream promoter                            Through intraspeciﬁc collinearity analysis of the white clover
regions of all OSCA genes, and are the most abundant (Tong, Wu et al.                      genes, the results indicate a total of 17, suggesting that some
2021). This is an indication that TrOSCA is responsive to environmen-                      OSCA genes may have originated through gene duplication. Subse-
tal stress, particularly anaerobic induction.                                              quently, a gene regulatory network was constructed, comprising
                                                                                           three genes in interaction. The interaction between TrOSCA10 and
                                                                                           TrOSCA23 was observed to be more abundant in the gene regula-
                                                                                           tory network. Previous research has shown that the AtOSCA,
                                                                                           OsOSCA, and ZmOSCA gene families response to osmotic stress,
                                                                                           indicating their potential role in stress regulation (Cao, Zhang
                                                                                           et al. 2020). In rice, the expression of OsOSCA1.2, OsOSCA2.1, and
                                                                                           OsOSCA2.2 is regulated by circadian rhythms, playing a role in
                                                                                           sensing and responding to extracellular osmotic changes induced
                                                                                           by the day-night cycle (Zhai, Wen et al. 2021). Rice can response
                                                                                           to drought, salinity, and ABA treatment by inducing the expres-
                                                                                           sion of multiple OsOSCA genes, with at least 8 genes being up-
                                                                                           regulated in response to one or more osmotic stresses(Li, Yuan
                                                                                           et al. 2015). Among these, under PEG stress, the expression of
                                                                                           OsOSCA1.1 and OsOSCA3.1 can be up-regulated up to 40-fold,
                                                                                           while after 6 h of ABA treatment, the expression of OsOSCA2.1
                                                                                           can increase up to 60-fold, and under NaCl stress, OsOSCA3.1
                                                                                           expression can be up-regulated up to 20-fold (Shan, Wu et al.
                                                                                           2023). Furthermore, in maize, it was observed that ZmOSCA2.3
Fig. 5. Gene regulatory network analysis of TrOSCA genes in white clover.Note: Gene
regulatory network of white clover was reconstructed using Arabidopsis gene regula-        and ZmOSCA2.4 are signiﬁcantly up regulated, over 200-fold,
tory network (GRN) in from AraNet database. The pink nodes were TrOSCAs genes, and         under PEG, NaCl, and ABA treatments, and they are positively cor-
the blue nodes were function genes interacting with TrOSCAs genes in white clover.         related with proline content (Li, Zhang et al. 2022).
                                                                                      24
X. Zhu, M. Li, S. Li et al.                                                                                                          South African Journal of Botany 178 (2025) 1827




Fig. 6. The expressional proﬁles of TrOSCAs under various tissues and stresses.Note: The expressional proﬁles of TrOSCAs under various tissues and stresses.The details of the experi-
ments are as follows: (a) Cold stress: RNA-seq database accession numbers of PRJNA781064. Eight time points were examined under cold stress as follows: 0 h, 30 min, 1 h, 3 h, 6 h,
12 h, 24 h, and 72 h, with three biological replications at each time point. (b) Drought stress: RNA-seq database accession numbers of PRJNA953427. Three white clover varieties—
Minnesota, Florida, and Missouri—were studied under drought stress, with three biological replications for each variety. (c) Tissue-speciﬁc expression: RNA-seq database accession
numbers of PRJNA523044. Eight tissues of white clover were analyzed, including emerging leaf, internode, leaf, mature leaf, nodal root, open ﬂorets, root,and stolon. Each tissue
type was replicated three times.Mean expression levels (FPKM values) were measured using Salmon software (version 0.12.0) and they were displayed using the ggplots package of
the R platform.




    Furthermore, studies on the OSCA gene family have revealed its                            Methodology, Investigation, Data curation. Xueqing Zhao: Software,
multifaceted roles in plant abiotic stress response. These roles may                          Resources, Methodology, Investigation. Tianxiang Zhang: Visualiza-
include regulating cell membrane conductivity, maintaining cell                               tion, Validation, Software, Resources, Methodology. Meiyan Guo:
osmotic balance, and participating in cell signal transduction, among                         Software, Methodology, Investigation. Changhong Guo: Project
other functions. Overall, the OSCA gene family plays a critical role in                       administration, Funding acquisition, Conceptualization. Yongjun
abiotic stress adaptation by modulating ion ﬂow inside and outside                            Shu: Writing  review & editing, Writing  original draft, Supervi-
cells, highlighting its importance in the plant’s response to abiotic                         sion, Funding acquisition, Data curation, Conceptualization.
stress.

CRediT authorship contribution statement                                                      Declaration of competing interest

   Xiaoyue Zhu: Writing  original draft, Visualization, Validation,                             The authors declare that there is no conﬂict of interest that could
Methodology, Investigation, Data curation. Manman Li: Visualization,                          be perceived as prejudicial to the impartiality of the reported
Validation, Methodology, Investigation, Data curation. Shuaixian Li:                          research.




Fig. 7. qRT-PCR analysis of TrOSCA genes in white clover under cold stress.Note: The X-axis represent time points in response to cold stress, and Y-axis represent relative expression
level of TrOSCA genes.

                                                                                         25
X. Zhu, M. Li, S. Li et al.                                                                                                              South African Journal of Botany 178 (2025) 1827




Fig. 8. Tertiary structure of nine TrOSCA proteins.Note: The 3D structure of TrOSCA gene family members was predicted through homology modeling. The SWISS-MODEL homology
modeling server (https://www.string-db.org/) was utilized for constructing protein tertiary structures.




CRediT authorship contribution statement                                                         Cao, L., et al., 2020. Systematic analysis of the maize OSCA genes revealing ZmOSCA
                                                                                                      family members involved in osmotic stress and ZmOSCA2.4 confers enhanced
                                                                                                      drought tolerance in transgenic arabidopsis. Int. J. Mol. Sci. 21 (1).
   Xiaoyue Zhu: Writing  original draft, Visualization, Validation,                             Cao, S., et al., 2019. Genome-wide characterization of aspartic protease (AP) gene fam-
Methodology, Investigation, Data curation. Manman Li: Visualization,                                  ily in Populus trichocarpa and identiﬁcation of the potential PtAPs involved in
Validation, Methodology, Investigation, Data curation. Shuaixian Li:                                  wood formation. BMC Plant Biol. 19 (1), 276.
                                                                                                 Chakraborty, S., et al., 2023. Genome-wide characterization and comparative analysis
Methodology, Investigation, Data curation. Xueqing Zhao: Software,                                    of the OSCA gene family and identiﬁcation of its potential stress-responsive mem-
Resources, Methodology, Investigation. Tianxiang Zhang: Visualiza-                                    bers in legumes. Sci. Rep. 13 (1), 5914.
tion, Validation, Software, Resources, Methodology. Meiyan Guo:                                  Chen, C., et al., 2020. TBtools: an integrative toolkit developed for interactive analyses
                                                                                                      of big biological data. Mol. Plant 13 (8), 1194–1202.
Software, Methodology, Investigation. Changhong Guo: Project                                     Chen, C., et al., 2020. TBtools: an integrative toolkit developed for interactive analyses
administration, Funding acquisition, Conceptualization. Yongjun                                       of big biological data. Mol. Plant 13 (8), 1194–1202.
Shu: Writing  review & editing, Writing  original draft, Supervi-                              Ding, S., et al., 2019. Genome-wide analysis of maize OSCA family members and their
                                                                                                      involvement in drought stress. PeerJ. 7, e6765.
sion, Funding acquisition, Data curation, Conceptualization.
                                                                                                 Edgar, R.C., 2004. MUSCLE: multiple sequence alignment with high accuracy and high
                                                                                                      throughput. Nucleic Acids. Res. 32 (5), 1792–1797.
                                                                                                 Espitia, C.M., et al., 2010. Duplex real-time reverse transcriptase PCR to determine
Acknowledgements
                                                                                                      cytokine mRNA expression in a hamster model of New World cutaneous leishman-
                                                                                                      iasis. BMC Immunol. 11, 31.
    This research was funded by the Natural Science Foundation of                                Finn, R.D., et al., 2011. HMMER web server: interactive sequence similarity searching.
Heilongjiang Province (grant number LH2022C050), and Natural and                                      Nucleic Acids. Res. 39 (Web Server issue), W29–W37.
                                                                                                 Grifﬁths, A.G., et al., 2019. Breaking free: the genomics of allopolyploidy-facilitated
Science Foundation of China (grant number U21A20182). The data                                        niche expansion in white clover. Plant Cell 31 (7), 1466–1487.
analysis work was supported by high performance computing center                                 Hill, T.W., et al., 2023. A member of the OSCA/TMEM63 family of mechanosensitive cal-
of Harbin Normal University.                                                                          cium channels participates in cell wall integrity maintenance in Aspergillus nidu-
                                                                                                      lans. Fungal. Genet. Biol. 169, 103842.
                                                                                                 Jafari, F., et al., 2024. Breeding maize of ideal plant architecture for high-density plant-
Supplementary materials                                                                               ing tolerance through modulating shade avoidance response and beyond. J. Integr.
                                                                                                      Plant Biol. 66 (5), 849–864.
                                                                                                 Kaur, A., et al., 2022. OSCA genes in bread wheat: molecular characterization, expres-
    Supplementary material associated with this article can be found,                                 sion proﬁling, and interaction analyses indicated their diverse roles during devel-
in the online version, at doi:10.1016/j.sajb.2025.01.005.                                             opment and stress response. Int. J. Mol. Sci. 23 (23).
                                                                                                   €
                                                                                                 Koster, P., et al., 2022. Ca(2+) signals in plant immunity. EMBO J. 41 (12), e110741.
                                                                                                 Krzeszowiec, W., et al., 2023. Two types of GLR channels cooperate differently in light
References                                                                                            and dark growth of Arabidopsis seedlings. BMC Plant Biol. 23 (1), 358.
                                                                                                 Krzywinski, M., et al., 2009. Circos: an information aesthetic for comparative genomics.
                                                                                                      Genome Res. 19 (9), 1639–1645.
Alexa, A., Rahnenfuhrer, J, 2010. topGO: enrichment analysis for gene ontology. R pack-
                                                                                                 Lee, T., et al., 2015. AraNet v2: an improved database of co-functional gene networks
    age version 2 (0), 2010.
                                                                                                      for the study of Arabidopsis thaliana and 27 other nonmodel plant species. Nucleic
Altschul, S.F., et al., 1997. Gapped BLAST and PSI-BLAST: a new generation of protein
                                                                                                      Acids Res. 43 (Database issue), D996–1002.
    database search programs. Nucleic Acids. Res. 25 (17), 3389–3402.
                                                                                                 Li, M., et al., 2023. Genome-wide analysis of the WRKY genes and their important roles
Ashraﬁ-Dehkordi, E., et al., 2018. Meta-analysis of transcriptomic responses to biotic
                                                                                                      during cold stress in white clover. PeerJ. 11, e15610.
    and abiotic stress in tomato. PeerJ. 6, e4631.
                                                                                                 Li, Y., et al., 2015. Genome-wide survey and expression analysis of the OSCA gene fam-
Bailey, T.L., et al., 2009. MEME SUITE: tools for motif discovery and searching. Nucleic
                                                                                                      ily in rice. BMC Plant Biol. 15 (1), 1–13.
    Acids. Res. 37 (Web Server issue), W202–W208.
                                                                                                 Li, Y., et al., 2022. Preliminary expression analysis of the OSCA gene family in maize and
Bartels, D., Sunkar, R., 2005. Drought and salt tolerance in plants. CRC Crit. Rev. Plant
                                                                                                      their involvement in temperature stress. Int. J. Mol. Sci. 23 (21).
    Sci. 24 (1), 23–58.
                                                                                                 Lynch, M., Conery, J.S., 2000. The evolutionary fate and consequences of duplicate
Breeze, E., 2019. State of (In)ﬂux: action of a CNGC Ca(2+) channel in defense against
                                                                                                      genes. Science 290 (5494), 1151–1155.
    herbivory. Plant Cell 31 (7), 1423–1424.

                                                                                            26
X. Zhu, M. Li, S. Li et al.                                                                                                                South African Journal of Botany 178 (2025) 1827


Ma, H., et al., 2021. qPCR and qRT-PCR analysis: regulatory points to consider when                 Wang, Y., et al., 2012. MCScanX: a toolkit for detection and evolutionary analysis of
    conducting biodistribution and vector shedding studies. Mol. Ther. Methods Clin.                    gene synteny and collinearity. Nucleic Acids Res. 40 (7), e49.
    Dev. 20, 152–168.                                                                               Waterhouse, A., et al., 2018. SWISS-MODEL: homology modelling of protein structures
Manier, N., et al., 2009. White clover nodulation index in heavy metal contaminated                     and complexes. Nucleic Acids Res. 46 (W1), W296–w303.
    soils- a potential bioindicator. J. Environ. Qual. 38 (2), 685–692.                             Xiao, J., et al., 2023. Identiﬁcation of cis-acting elements upstream of regR gene in
Miao, S., et al., 2022. Identiﬁcation of OSCA gene family in Solanum habrochaites and                   streptococcus pneumoniae. Microb. Pathog. 182, 106263.
    its function analysis under stress. BMC Genomics 23 (1), 547.                                   Yamaguchi-Shinozaki, K., Shinozaki, K., 2005. Organization of cis-acting regulatory ele-
Mistry, J., et al., 2021. Pfam: the protein families database in 2021. Nucleic Acids Res. 49            ments in osmotic- and cold-stress-responsive promoters. Trends. Plant Sci. 10 (2),
    (D1), D412–d419.                                                                                    88–94.
Patro, R., et al., 2017. Salmon provides fast and bias-aware quantiﬁcation of transcript            Yang, S., et al., 2022. Identiﬁcation and expression proﬁle analysis of the OSCA gene
    expression. Nat. Methods 14 (4), 417–419.                                                           family related to abiotic and biotic stress response in cucumber. Biology (Basel) 11
Santangelo, J.S., et al., 2023. Haplotype-Resolved, chromosome-level assembly of white                  (8).
    clover (Trifolium repens L., Fabaceae). Genome Biol. Evol. 15 (8).                              Yin, L., et al., 2021. Genome-wide analysis of OSCA gene family members in Vigna
Shan, F., et al., 2023. Evolutionary analysis of the OSCA gene family in sunﬂower (Heli-                radiata and their involvement in the osmotic response. BMC Plant Biol. 21 (1),
    anthus annuus L) and expression analysis under NaCl stress. PeerJ. 11, e15089.                      408.
Shannon, P., et al., 2003. Cytoscape: a software environment for integrated models of               Zhai, Y., et al., 2021. Functional analysis of rice OSCA genes overexpressed in the arabi-
    biomolecular interaction networks. Genome Res. 13 (11), 2498–2504.                                  dopsis osca1 mutant due to drought and salt stresses. Transgenic Res. 30 (6), 811–
She, K., et al., 2022. Genome-Wide identiﬁcation, evolution and expressional analysis                   820.
    of OSCA gene family in barley (Hordeum vulgare L.). Int. J. Mol. Sci. 23 (21).                  Zhang, M., et al., 2018. Structure of the mechanosensitive OSCA channels. Nat. Struct.
Tamura, K., et al., 2021. MEGA11: molecular evolutionary genetics analysis version 11.                  Mol. Biol. 25 (9), 850–858.
    Mol. Biol. Evol. 38 (7), 3022–3027.                                                             Zhou, F., et al., 2016. Genome-wide identiﬁcation and evolutionary analysis of
Tong, K., et al., 2021. Genome-Wide identiﬁcation and expression proﬁle of OSCA gene                    leucine-rich repeat receptor-like protein kinase genes in soybean. BMC Plant
    family members in Triticum aestivum L. Int. J. Mol. Sci. 23 (1).                                    Biol. 16, 1–13.
Untergasser, A., et al., 2012. Primer3new capabilities and interfaces. Nucleic Acids               Zoabi, Y., Shomron, N., 2021. Processing and analysis of RNA-seq data from public
    Res. 40 (15), e115.                                                                                 resources. Methods Mol. Biol. 2243, 81–94.




                                                                                               27
