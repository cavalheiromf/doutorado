# Shan_2023 - Evolutionary analysis of the OSCA gene family in sunflower (

**Source PDF:** 

---

                                    Evolutionary analysis of the OSCA gene
                                    family in sunflower (Helianthus annuus
                                    L) and expression analysis under NaCl
                                    stress
                                    Feibiao Shan1 ,2 ,3 ,* , Yue Wu3 ,* , Ruixia Du3 , Qinfang Yang3 , Chunhui Liu3 ,
                                    Yongxing Wang3 , Chun Zhang1 and Yang Chen1 ,3
                                1
                                  Hetao College, Bayannur, China
                                2
                                  Inner Mongolia Traditional Chinese & Mongolian Medical Research Institute, Hohhot, China
                                3
                                  Bayannur Institute of Agricultural and Animal Sciences, Bayannur, China
                                *
                                  These authors contributed equally to this work.


                                        ABSTRACT
                                        Hyperosmolality-gated calcium-permeable channels (OSCA) are Ca2+ nonselective
                                        cation channels that contain the calcium-dependent DUF221 domain, which plays an
                                        important role in plant response to stress and growth. However, the OSCA gene has
                                        not been fully identified and analyzed in sunflowers. In this study, we comprehensively
                                        analyzed the number, structure, collinearity, and phylogeny of the OSCA gene family
                                        in the sunflower, six Compositae species (Arctium lappa, Chrysanthemum morifolium,
                                        Cichorium endivia, Cichorium intybus, Lactuca sativa var. Angustata, and Carthamus
                                        tinctorius), and six other plants (soybean, Arabidopsis thaliana, rice, grape, and maize).
                                        The expression of the sunflower OSCA gene in nine different tissues, six different
                                        hormones, and NaCl stress conditions were analyzed based on transcriptome data
                                        and qRT–PCR. A total of 15 OSCA proteins, distributed on 10 chromosomes, were
                                        identified in the sunflower, and all of them were located in the endoplasmic reticulum.
                                        Using the phylogenetic tree, collinearity, gene structure, and motif analysis of the six
Submitted 13 October 2022               Compositae species and six other plants, we found that the sunflower OSCA protein
Accepted 26 February 2023               had only three subfamilies and lacked the Group 4 subfamily, which is conserved in
Published 17 April 2023                 the evolution of Compositae and subject to purification selection. The OSCA gene
Corresponding authors                   structure and motif analysis of the sunflower and six Compositae showed that there
Yang Chen, chenyangrz@126.com           was a positive correlation between the number of motifs of most genes and the length
Chun Zhang,
zhangchun6625@163.com                   of the gene, different subfamilies had different motifs, and the Group 4 subfamily had
                                        the smallest number of genes and the simplest gene structure. RNA-seq and qRT–PCR
Academic editor
Ravindra Kumar                          analysis showed that the expression levels of most OSCA genes in the sunflower changed
                                        to varying degrees under salt stress, and HaOSCA2.6 and HaOSCA3.1 were the most
Additional Information and
Declarations can be found on            important in the sunflower’s response to salt stress. The coexpression network of the
page 20                                 sunflower genes under salt stress was constructed based on weighted gene co-expression
DOI 10.7717/peerj.15089                 network analysis (WGCNA). In conclusion, our findings suggest that the OSCA gene
                                        family is conserved during the sunflower’s evolution and plays an important role in salt
    Copyright                           tolerance. These results will deepen our understanding of the evolutionary relationship
2023 Shan et al.
                                        of the sunflower OSCA gene family and provide a basis for their functional studies
Distributed under                       under salt stress.
Creative Commons CC-BY 4.0

OPEN ACCESS



                                    How to cite this article Shan F, Wu Y, Du R, Yang Q, Liu C, Wang Y, Zhang C, Chen Y. 2023. Evolutionary analysis of the OSCA gene
                                    family in sunflower (Helianthus annuus L) and expression analysis under NaCl stress. PeerJ 11:e15089 http://doi.org/10.7717/peerj.15089
                                   Subjects Agricultural Science, Bioinformatics, Genomics, Plant Science, Soil Science
                                   Keywords Sunflowers, OSCA gene family, Evolutionary analysis, Expression analysis, Coexpres-
                                   sion network


                                   INTRODUCTION
                                   The sunflower (Helianthus annuus L.) belongs to the Compositae family of annual herbs,
                                   which are divided into edible the sunflower and oil sunflower (Keeley, Cantley & Gallaher,
                                   2021). Sunflower oil is one of the world’s four major oil crops (Rele & Mohile, 2003). The
                                   main uses of edible sunflower are ingestion and food addition (Cao et al., 2018). Because
                                   they have the advantages of simple cultivation and salt and drought tolerance, sunflowers
                                   are known as a pioneer crop in saline-alkali land (Keeley, Cantley & Gallaher, 2021; Rele &
                                   Mohile, 2003). Planting sunflowers on saline-alkali land has economic benefits as well as
                                   ecological benefits, such as the desalination of the soil (Keeley, Cantley & Gallaher, 2021;
                                   Rele & Mohile, 2003). Acting as a second messenger, calcium ions play an important role
                                   in the growth and development of plant cells (Klimecka & Muszyńska, 2007). When a plant
                                   is stimulated by the external environment, the Ca2+ concentration changes in the cell are
                                   regulated through transport systems such as Ca2+ channels. Corresponding signals are
                                   generated, including changes in ion transport, hormones, and protective enzyme systems,
                                   which then regulate the pore size, root hair development, and absorption of water and
                                   nutrients in plant guard cells (Shukla et al., 2014). Both abiotic and biotic stresses can
                                   induce plant stress resistance by activating the plant calcium ion pathway (Shukla et al.,
                                   2014; Ju et al., 2021). The calcium ion pathway is very important for the transduction of
                                   calcium signals, so the study of the calcium ion pathway has far-reaching significance when
                                   exploring the mechanism of plant resistance regulation (Liu & Zhu, 1998; Xu et al., 2006;
                                   Xue et al., 2019).
                                       Calcium ion channels are mainly divided into hypotonic and hypertonic calcium
                                   ion channels, OSCA belonging to the latter (Murthy et al., 2018). OSCA is a kind of
                                   hyperosmotic stress sensor (also called a sensor protein) in Arabidopsis thaliana, as
                                   well as a Ca2+ -selective cation channel (Zhang et al., 2018). Other common calcium
                                   channel proteins (such as depolarization-activated Ca2+ -permeable channels (DACCs),
                                   hyperpolarization-activated Ca2+ -permeable channels (HACCs), and inositol 1,4,5-
                                   trisphosphate receptor (IP3R)) have been systematically studied in plants, but there
                                   have been few studies on OSCA (Swarbreck, Colaço & Davies, 2013; Gao et al., 2021).
                                   Using protein-conserved domain analysis, it was found that OSCA gene family proteins
                                   contained three conserved functional domains: late exocytosis (pfam13967), cytosolic
                                   domain of 10TM putative phosphate transporter (pfam14703), and calcium-dependent
                                   channel (pfam02714) (Swarbreck, Colaço & Davies, 2013; Gao et al., 2021). In crops such
                                   as Arabidopsis thaliana and rice, the OSCA gene family was divided into four subfamilies,
                                   all of which contained the DUF221 domain (Yuan et al., 2014; Li et al., 2015). The DUF221
                                   domain is essential, representative, and decisive for both the OSCA gene family and
                                   represents the seven transmembrane domain regions of calcium-dependent channels
                                   that function as calcium channels in osmotic sensing (Kiyosue, Yamaguchi-Shinozaki &



Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                          2/26
                                   Shinozaki, 1994). Previous studies used forward genetics to screen AtOSCA1 as an unknown
                                   hyperosmotic calcium ion permeability channel (Yuan et al., 2014). The results of this
                                   study indicated that OSCA1 may be an osmotic sensor in Arabidopsis thaliana (Yuan et al.,
                                   2014; Zhang et al., 2020). In rice, osmotic-related abiotic stresses (ABA, NaCl, and PEG)
                                   differentially induced the expression of 10 OsOSCA genes, of which OsOSCA−3.1 was the
                                   identified OsERD4 (early drought response) gene (Li et al., 2015). A drought-tolerant gene
                                   (TaOSCA1.4) was cloned in wheat that belongs to the same gene family as AtOSCA1.8 and
                                   OsOSCA1.4 and is related to grain number per ear and yield (Zhai et al., 2020). Thirteen
                                   GmOSCA genes in soybean (Glycine max (Linn.) Merr) were associated with drought
                                   and alkali stress responses (Yin et al., 2021). A membrane-integral protein (AtOSCA1.2)
                                   was obtained in Arabidopsis thaliana (Liu, Wang & Sun, 2018). This gene can increase the
                                   concentration of intracellular calcium ions under hyperosmotic stress and increase the
                                   permeability of the cell membrane to K+ and Na+ . It has also been shown that AtOSCA1.2
                                   is an inherently mechanosensitive pore-forming ion channel that may be necessary for
                                   osmotic sensing, and AtOSCA1.1 and AtOSCA3.1 (also known as the ERD4 gene) are
                                   mechanosensitive channels (Liu, Wang & Sun, 2018; Zhang et al., 2018).
                                      OSCA family genes have been studied in a variety of plants and found to play potential
                                   roles in plant stress resistance (Li et al., 2015; Yin et al., 2021; Tong et al., 2021; Miao et al.,
                                   2022). Following the publication of the genomes of the sunflower and other Compositae
                                   plants, the evolution of this gene family in Compositae has not been systematically studied.
                                   In this study, the number, structure, collinearity, and phylogeny of the OSCA gene family
                                   were comprehensively analyzed using genomic data from the sunflower and six Compositae
                                   species. RNA-sequencing (RNA-seq) and qRT −PCR were used to analyze the expression of
                                   the sunflower OSCA gene in nine different tissues, six different hormones, and under NaCl
                                   stress conditions. The coexpression network of OSCA under salt stress was constructed
                                   using WGCNA. These results will further broaden our understanding of the evolutionary
                                   relationship of the sunflower OSCA gene family and provide a basis for its functional study
                                   under salt stress.

                                   MATERIAL AND METHODS
                                   Plant material
                                   The sunflower salt-tolerant inbred line 19S05 (bred by Bayannur Institute of Agricultural
                                   and Animal Sciences) was selected for this study. This material had a plant height of
                                   200 cm, number of leaves was approximately 30, leaves were green, without branches, and
                                   the inclination of the disc was 4. The diameter of the disc was 20 cm, yellow flowers were
                                   ligulated, and the weight of 100 seeds was 16 g. The grains were narrow oval, 2.00 cm long
                                   and 0.95 cm wide, with brown white edges, no streaks, and strong salt tolerance. Selected
                                   and full 19S05 seeds were washed with water, surface sterilized with 3% H2 O2 for 10 min,
                                   and then placed in plastic pots filled with sterilized soil. After culturing four true leaves, a
                                   200 mM NaCl stress treatment was performed. Root samples were taken at 0 h of treatment
                                   and then at 1 h, 3 h, 6 h, 12 h, and 24 h after treatment. Samples were then snap-frozen
                                   in liquid nitrogen (three biological replicates for each treatment) and stored in a −80 ◦ C
                                   refrigerator.



Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                                3/26
                                   Identification and cioinformatics analysis of OSCA genes
                                   Helianthus annuus, Lactuca sativa var. Angustata, Gossypium hirsutum, Glycine max
                                   (Linn.) Merr, Arabidopsis thaliana, Oryza sativa, Vitis vinifera, and Zea mays genomic
                                   and proteomic data were downloaded from the Ensembl Plants database (http:
                                   //plants.ensembl.org/index.html) (Bolser et al., 2016). Arctium lappa, Cichorium endivia,
                                   and Cichorium intybus genomic and proteomic data were downloaded from the
                                   NCBI database (https://www.ncbi.nlm.nih.gov/). Chrysanthemum morifolium genomic
                                   and proteomic data were downloaded from the Chrysanthemum genome database
                                   (http://www.amwayabrc.com/zh-cn/). Carthamus tinctorius L. genomic and proteomic
                                   data were downloaded from the NGINX database (http://118.24.202.236:11010/filedown/).
                                   Additionally, we used the OSCA gene domain Hidden Markov model (PF02714) and
                                   HMMER software (http://hmmer.org/) to identify protein sequences validated in the
                                   NCBI-CDD (https://www.ncbi.nlm.nih.gov/cdd/) database (Mistry et al., 2021). ExPASy
                                   software (http://cn.expasy.org/tools) was used on the physicochemical data to calculate the
                                   protein, and EuLoc software performed subcellular localization prediction (Wilkins et al.,
                                   1999; Chang et al., 2013).

                                   Phylogenetic and collinear analysis of the OSCA gene family
                                   The OSCA protein sequences from Helianthus annuus, Arctium lappa , Chrysanthe-
                                   mum morifolium, Cichorium endivia, Cichorium intybus, Lactuca sativa var. Angustata,
                                   Carthamus tinctorius, Gossypium hirsutum, Glycine max (Linn.) Merr, Arabidopsis thaliana,
                                   Oryza sativa, Vitis vinifera, and Zea mays were used for multiple sequence alignment. A
                                   phylogenetic tree was then constructed using the neighbor-joining method (the bootstrap
                                   method value was set to 1,000 and the remaining parameters were set to default values)
                                   (Hall, 2013). The nwk file was obtained using MEGA11 software, and a phylogenetic tree
                                   of the OSCA gene was made. The related collinearity map was constructed using the circle
                                   gene view function in TBtools (Chen et al., 2020; Wang et al., 2012).

                                   Chromosomal location, gene structure, and motif analysis
                                   The chromosomal location information for the members of the sunflower OSCA gene
                                   family was extracted using TBtools software, and the chromosomal location map was
                                   drawn using Mapchart software (Chen et al., 2020; Voorrips, 2002). A phylogenetic tree
                                   of Helianthus annuus, Arctium lappa L., Chrysanthemum morifolium, Cichorium endivia,
                                   Cichorium intybus, Lactuca sativa var. Angustata, and Carthamus tinctorius L. OSCA
                                   sequences was constructed using MEGA11 software (Wang et al., 2012). OSCA motif types
                                   were analyzed using Multiple Expectation maximizations for Motif Elicitation (MEME:
                                   http://meme-suite.org/) (Bailey et al., 2009). Based on the mRNA sequence of the OSCA
                                   gene, the intron-exon structure was analyzed. Graphs were made using TBtools software
                                   (Chen et al., 2020).

                                   Analysis of cis-acting elements of the sunflower OSCA gene
                                   The upstream 2,000 bp sequence of the sunflower OSCA gene was extracted, and
                                   the possible cis-acting elements were predicted using the PlantCARE database




Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                        4/26
                                   (http://bioinformatics.psb.ugent.be/webtools/plantcare/html/). After screening, the TBtools
                                   software was used to map (Chen et al., 2020).

                                   RNA-seq analysis
                                   Transcriptome sequencing of different tissues of sunflower under different hormone and
                                   salt stress conditions was downloaded from NCBI (SRP092742 and PRJNA866668). Fastp
                                   software was used for filtering, removing adapters, and quality control of the raw data.
                                   Hisat2 software aligned the filtered data to the sunflower reference gene, and StringTie
                                   software was used for expression quantification (Kim et al., 2019; Pertea et al., 2015). Gene
                                   expression was assessed using the FPKM method, and the expression data were normalized
                                   to log10 (FPKM+1). Then, the expression heatmap was drawn with TBtools software (Chen
                                   et al., 2018).

                                   qRT −PCR
                                   Primers were designed in specific regions of the sunflower OSCA gene sequence using
                                   Primer 6.0 software. The HaActin gene was chosen as the reference gene for qRT-PCR
                                   analysis (Table S1; Li & Brownley, 2010). Root tissue cDNA was used as the template to
                                   detect the expression of candidate genes by qRT −PCR, and each sample was repeated
                                   three times. The total reaction system was 20 µl, qRT −PCR program: 94 ◦ C for 30 s; 94 ◦ C
                                   for 5 s, 60 ◦ C for 15 s, 72 ◦ C for 10 s for 38 cycles; and 4 ◦ C for the end. Each group of
                                   data was replicated three times, and the 2−11Ct method was used for relative quantitative
                                   analysis (Tanino et al., 2017).

                                   WGCNA
                                   The DEseq2 software package was used to identify differential genes under salt stress for
                                   WGCNA analysis. We selected β = 6 to process the original relation matrix in order to
                                   get a non-proportional adjacency matrix. The adjacency matrix was further transformed
                                   into a topological overlap matrix (TOM). The minimum number of genes in a module
                                   was 30, the threshold for merging similar modules was 0.25 (cutHeight =0.25), and the
                                   network type was ‘‘signed’’ (type =‘‘signed’’ or networkType =‘‘signed’’). Cytoscape−3.8.2
                                   software was used for visualization (Shannon et al., 2003). We performed Gene Ontology
                                   (GO) and Kyoto Encyclopedia of Genes and Genomes (KEGG) analyses using the cluster
                                   Profiler software package in R language.

                                   RESULT
                                   Identification of the OSCA gene family
                                   We systematically studied the changes in the copy number of the OSCA gene
                                   family during the sunflower’s evolution. First, using HMMsearch the OSCA gene
                                   was comprehensively searched from seven Compositae species (Helianthus annuus,
                                   Arctium lappa, Chrysanthemum morifolium, Cichorium endivia, Cichorium intybus,
                                   Lactuca sativa, and Carthamus tinctorius). The search results were validated against the
                                   NCBI-CDD database. Helianthus annuus, Arctium lappa, Chrysanthemum morifolium,
                                   Cichorium endivia, Cichorium intybus, Lactuca sativa, and Carthamus tinctorius contained



Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                         5/26
                                   15, 17, 20, 19, 19, 21, and 14 OSCA sequences, respectively. We named them
                                   HaOSCA1.1∼HaOSCA3.1 according to the 15 sunflower sequences and the phylogenetic
                                   tree of 12 other plants. The protein encoded by sunflower OSCA family genes contained
                                   648-838 amino acid residues, the length of the open reading frame (ORF) was 1,947–2,517
                                   bp, the theoretical isoelectric point was 7.61−9.94, and the relative molecular weight was
                                   73.42–96.62 kDa. The protein subcellular localization showed that HaOSCA was localized
                                   to the endoplasmic reticulum, vacuole, chloroplast, golgi apparatus. and mitochondrion
                                   (Table 1).
                                      Fifteen HaOSCA genes were distributed on 10 sunflower chromosomes (Chr03, Chr04,
                                   Chr05, Chr06, Chr07, Chr09, Chr12, Chr15, Chr16, and Chr17) (Fig. 1). Among these,
                                   Chr07 and Chr16 staining contained the most (three) OSCA genes. Except for Chr10,
                                   which contained two OSCA genes, the other chromosomes contained only one OSCA
                                   gene.

                                   Evolutionary analysis of the OSCA gene family
                                   To better understand the evolutionary relationship of the sunflower OSCA family genes,
                                   we constructed a phylogenetic tree of the full-length OSCA protein sequences of Helianthus
                                   annuus, Gossypium hirsutum, Glycine max (Linn.) Merr, Arabidopsis thaliana, Oryza sativa,
                                   Vitis vinifera, and Zea mays (Fig. 2A). According to the results, the evolutionary tree was
                                   divided into four groups. Compared with Gossypium hirsutum, Glycine max (Linn.) Merr,
                                   Arabidopsis thaliana, Oryza sativa, Vitis vinifera, and Zea mays, there was no sunflower
                                   OSCA protein in Group 4 (Fig. 2), which may have been caused by the loss of genes in
                                   the sunflower during the evolution process. The number of OSCA proteins in Group 1
                                   and Group 2 subgroups was consistent both in the sunflower and in Gossypium hirsutum,
                                   Glycine max (Linn.) Merr, Arabidopsis thaliana, Oryza sativa, Vitis vinifera, and Zea mays
                                   (Fig. 2B). The number of OSCA genes in sunflower, Arabidopsis thaliana, and Glycine max
                                   (Linn.) Merr was basically the same, and the sunflower genes of the same branch were
                                   more closely related to those in Arabidopsis thaliana and Glycine max (Linn.) Merr. Except
                                   for soybean and cotton, the other crops in Group 3 all contained an OSCA sequence, which
                                   also indicated that the Group 3 subgroup of the OSCA gene family was more conserved
                                   during the plant’s evolution. Although Group 3 and Group 4 had relatively few members,
                                   they were retained in the evolution of plants, suggesting that they may play important roles
                                   in biological processes. However, the loss of members of sunflower Group 4 may have also
                                   been caused by functional redundancy of genes, which requires further study.
                                      To further explore the evolutionary relationship of the sunflower OSCA gene family, we
                                   selected the sunflower OSCA gene as the core and constructed a colinear relationship
                                   between sunflower and Gossypium hirsutum, Glycine max (Linn.) Merr, Arabidopsis
                                   thaliana, Oryza sativa, Vitis vinifera, and Zea mays OSCA genes (Fig. 3). We found that the
                                   sunflower OSCA had 18 collinear gene pairs with Arabidopsis thaliana, 36 with Gossypium
                                   hirsutum, 12 with Glycine max (Linn.) Merr, eight with Oryza sativa, and 10 with Vitis
                                   vinifera. There were 11 collinear gene pairs with Zea mays (Fig. 3). The greatest collinearity
                                   between sunflower OSCA and cotton may have been related to cotton having a larger
                                   genome and the largest number of OSCA genes. In addition to cotton, the sunflower OSCA



Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                          6/26
Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089




                                                     Table 1 Sunflower OSCA gene family member information.

                                                     Gene name       Gene ID                      Open reading   Protein     Relative    Theoretical   Subcellular
                                                                                                  frame/bp       length/aa   molecular   isoelectric   localization
                                                                                                                             weight      point (pI)
                                                                                                                             (r)/kDa
                                                     HaOSCA1.1       HannXRQ_Chr17g0558291        2,097          698         79.86       8.07          Vacuole, Endoplasmic reticulum
                                                     HaOSCA1.2       HannXRQ_Chr16g0516941        2,322          773         88.43       9.13          Endoplasmic reticulum
                                                     HaOSCA1.3       HannXRQ_Chr05g0129321        2,274          757         86.85       9.73          Endoplasmic reticulum
                                                     HaOSCA1.4       HannXRQ_Chr16g0506581        2,319          772         88.63       8.96          Endoplasmic reticulum
                                                     HaOSCA1.5       HannXRQ_Chr06g0164031        2,310          769         87.77       9.36          Vacuole, Endoplasmic reticulum
                                                     HaOSCA1.6       HannXRQ_Chr04g0118011        2,313          770         87.71       9.69          Vacuole, Endoplasmic reticulum
                                                     HaOSCA1.7       HannXRQ_Chr07g0194331        2,340          779         89.00       9.94          Vacuole, Endoplasmic reticulum
                                                     HaOSCA1.8       HannXRQ_Chr03g0081691        2,517          838         96.62       9.09          Chloroplast, Endoplasmic reticulum
                                                     HaOSCA2.1       HannXRQ_Chr17g0563981        1,947          648         73.42       8.54          Chloroplast, Endoplasmic reticulum
                                                     HaOSCA2.2       HannXRQ_Chr16g0525101        1,947          648         73.60       9.03          Chloroplast, Endoplasmic reticulum
                                                     HaOSCA2.3       HannXRQ_Chr07g0205641        2,172          723         82.82       8.75          Golgi apparatus, Vacuole, Endoplasmic reticulum
                                                     HaOSCA2.4       HannXRQ_Chr07g0188761        2,223          740         83.76       7.61          Chloroplast, Endoplasmic reticulum
                                                     HaOSCA2.5       HannXRQ_Chr09g0264291        2,133          710         80.64       9.1           Golgi apparatus, Vacuole, Endoplasmic reticulum
                                                     HaOSCA2.6       HannXRQ_Chr12g0379201        2,094          697         79.44       9.93          Mitochondrion, Vacuole, Endoplasmic reticulum
                                                     HaOSCA3.1       HannXRQ_Chr15g0481591        2,145          714         80.99       9.29          Vacuole, Endoplasmic reticulum
7/26
                                              Chr 03           Chr 04           Chr 05           Chr 06           Chr 07           Chr 09           Chr 12           Chr 15           Chr 16           Chr 17
                                     0 Mb                                            HaOSCA1.3        HaOSCA1.5

                                                                                                                       HaOSCA2.4
                                     22 Mb

                                     44 Mb                                                                                                                                                 HaOSCA1.4

                                                                                                                       HaOSCA1.7
                                     66 Mb                                                                                                                                HaOSCA3.1


                                     88 Mb
                                                                                                                       HaOSCA2.3
                                     110 Mb
                                                                                                                                                                                           HaOSCA1.2
                                                                                                                                                         HaOSCA2.6
                                     132 Mb        HaOSCA1.8                                                                                                                                                HaOSCA1.1

                                                                    HaOSCA1.6
                                     154 Mb
                                                                                                                                                                                           HaOSCA2.2
                                                                                                                                        HaOSCA2.5
                                     176 Mb                                                                                                                                                                 HaOSCA2.1

                                     198 Mb

                                     220 Mb




                                     Figure 1 Chromosomal location of the sunflower OSCA gene.
                                                                                            Full-size                                                           DOI: 10.7717/peerj.15089/fig-1


                                   had greater collinearity with Arabidopsis thaliana and Glycine max (Linn.) Merr, which was
                                   consistent with the results of the phylogenetic tree analysis.
                                      To further study the evolutionary relationship of the sunflower OSCA gene family, we
                                   constructed a phylogenetic tree based on the OSCA protein sequences of six Compositae
                                   species (Arctium lappa L., Chrysanthemum morifolium, Cichorium endivia, Cichorium
                                   intybus, Lactuca sativa var. Angustata, and Carthamus tinctorius L.) and Helianthus annuus
                                   (Fig. 4A). Except for Helianthus annuus and Carthamus tinctorius L., which lacked the
                                   Group 4 subgroup, all Asteraceae contained four subgroups (Fig. 4A). The Cichorium
                                   endivia and Lactuca sativa var. Angustata Group 4 subgroups contained three and four
                                   OSCA genes, respectively, while Arctium lappa L., Chrysanthemum morifolium, Cichorium
                                   endivia, and Carthamus tinctorius L all contained one, which was consistent with the results
                                   from Arabidopsis thaliana, Glycine max (Linn.) Merr, Oryza sativa, and Zea mays (Figs. 2B
                                   and 4B). Except for Chrysanthemum morifolium Group 3, which contained four sequences,
                                   there was no difference in the subgroups of Group 1, Group 2, and Group 3 based on
                                   Compositae.
                                      We also constructed the collinear relationships for the OSCA of seven species of
                                   Compositae and found that there were three pairs of HaOSCA (HaOSCA1.1 and
                                   HaOSCA2.1, HaOSCA1.2 and HaOSCA2.2, HaOSCA1.3 and HaOSCA1.5) with tandem
                                   repeats in sunflower genes (Fig. 5A), indicating that these three gene pairs may have been
                                   derived from tandem repeats. At the same time, five pairs of HaOSCA (HaOSCA1.5 and
                                   HaOSCA1.6, HaOSCA2.2 and HaOSCA2.1, HaOSCA1.2 and HaOSCA1.1, HaOSCA1.8 and
                                   HaOSCA1.7, HaOSCA1.3 and HaOSCA1.1) showed very high identities (over 84.77%),
                                   implying that they may have arisen from segments or whole genes (Fig. 5A). Additionally,
                                   the ratio of non-synonymous to synonymous (Ka/Ks) between duplicate gene pairs was
                                   calculated, and the Ka/Ks values of all gene pairs were less than 1, indicating that these
                                   gene pairs may have undergone purifying selection (Table S2). Helianthus annuus had 32
                                   collinear gene pairs with Arctium lappa L., 32 with Chrysanthemum morifolium, 29 with
                                   Cichorium endivia, 31 with Cichorium intybus, and 39 with Lactuca sativa var. Angustata,
                                   and 18 collinear gene pairs with Carthamus tinctorius L.. In addition to having lower



Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                                                                                                                8/26
                                     A                                    Grou
                                                                              p2




                                                                                                        ZmOSCA2.2
                                                              GhOSC A2.5




                                                                                                       GhOSCA2.2


                                                                                                      GmO CA2.1
                                                              ZmOSCA2.3
                                                              OsOSCA2.3



                                                                                                       GmOS 2.9
                                                              OsOSCA2. 3




                                                                                                      OsO SCA2.3
                                                               GhOS A2.1




                                                                                                     ZmO SCA2.5
                                                                                                  Zm OSCA 2.5
                                                                VvO




                                                                                                       GhOSCA
                                                                HaO SCA2. 6




                                                                                                 At OSC 2.2
                                                                  Gm OSC A2.3
                                                                  AtO




                                                                                               At OSC A2.4
                                                                                                    Os SCA
                                                                   Gm SC A2.




                                                                    SC

                                                                    A2.1
                                                                    C




                                                                                            Gh hOS CA2 1
                                                                    SCA 4
                                                                     OS A2.




                                                                                             G OS A2.
                                                                                          V O C .2
                                                                      AtO SC A2.4 .5




                                                                                         G vOS SC A2.1
                                                                       Ha OS CA 2.4



                                                                        C
                                                                        Gm O SC




                                                                        4




                                                                                            SC A2 .6
                                                                         2.6
                                                                          O C 2



                                                                          A2
                                                                           Gm vO




                                                                                          hO C A2
                                                                                              A 2 .2
                                                                             .
                                                                 G                                                           12




                                                                                                 .7
                                                                               V




                                                                                7
                                                             G hOS                                                         2. 4




                                                                                 S A
                                                                hO C                                                     A     .




                                                                                  5
                                                           Ha S A                                                      SC A2 .11
                                                         Ha OS CA 2.8                                                hO OSC A2 .1
                                                                  C 2                                               G h SC 4
                                                       Ha OSC A2 .3                                                  G hO CA 4.1
                                                                     .
                                                      Ha OSC A2. 4                                                     G sOS CA 1




                                                                                                                                      Gro
                                                        OS A2 3                                                         O OS A4.
                                                    Zm
                                                       OS CA2. .1                                                        Zm OSC 4.1




                                                                                                                                         up4
                                                  Os
                                                      O CA2
                                                                  2                                                        Vv SCA 4.1
                                                Gm SCA2 .1                                                                  AtO OSCA .2
                                                    OS        .
                                                 VvO CA2.8
                                                               1                                                              Gh SCA4
                                              GhO
                                                      SCA                                                                      GhO SCA4.1
                                                   SCA 2.3                                                                       GmO SCA4.2
                                                        2
                                                AtOSC .10                                                                        GmO
                                                        A
                                              GhOSC 2.5
                                                       A3.4
                                              GhOSCA3.2
                                              GhOSCA3.3
                                                                                                                                  GhOSCA1.1
                                              GhOSCA3.1
                                                                                                                                  GhOSCA1.9
                                              HaOSCA3.1
                                     Group3




                                                                                                                                 GhOSCA1.5
                                                          .1
                                               VvOSCA3                                                                           GhOSC
                                                      CA3.2                                                                            A
                                              GmOS                                                                               GmOS 1.13
                                                     SCA3
                                                           .1                                                                   GmO CA1.1
                                               GmO CA3.1                                                                        GmO SCA1.2
                                                      S
                                                 A tO       3.1                                                                Gm SCA1
                                                       SCA 1
                                                 ZmO SCA3. 6                                                                  AtO OSCA .3
                                                  OsO CA1 .8
                                                              .1                                                             AtO SCA 1.4
                                                      OS      A1                                                           At SC 1.2
                                                  Gh OSC 1.12                                                             At OSC A1.1
                                                      Gh SCA A1.4 3                                                     V OS A1
                                                         O      C 1.                                                  H vOS CA .3
                                                      Gh OS CA 1.9                                                   Ha aOS CA 1.4
                                                         Gh OS CA 1.8                                              H O C 1.4
                                                                                                                    aO S A1
                                                            Vv OS CA                                                  SC CA .3
                                                                      Zm OS CA 1.8




                                                                                        At O CA .6
                                                                    S
                                                             Gm O
                                                                     Os OS CA1 1.8




                                                                                                                         A1 1.2
                                                                        Ha OS CA




                                                                                          GmaOS CA1 .2
                                                                                          O S C 1.
                                                                  Gh OS CA1 .7




                                                                  m




                                                                                           SC A 4
                                                                                           H OS A1
                                                                                 S



                                                                     O CA .3




                                                                G                                                          .1
                                                                           Ha tO




                                                                                            At OSC A1.2
                                                                 Gh SCA 1.4




                                                                                             A1 1.5
                                                                       CA 1




                                                                                             Vv OSC 1.10
                                                                             A




                                                                     OS 1.1




                                                                                              Gh OSCA 1.7
                                                               GhO OSCA 1.3




                                                                                               .5
                                                                  SCA 1.7




                                                                                                Gh SCA 15
                                                                       1.14




                                                                                                  GhO SCA1.
                                                              GmO CA1.6




                                                                                                  GhO SCA1.3
                                                                       1.7




                                                                                                   OsO CA1.1
                                                              HaOSC 1.6




                                                                                                   OsOS A1.5
                                                                    A1.6
                                                             HaOSCA1.5




                                                                                                    ZmOSC
                                                             ZmOSCA1.4

                                                                                                    ZmOSCA1
                                                                                                    VvOSCA1.1
                                                                                                    OsOSCA1.2
                                                                  SCA
                                                                   CA
                                                                   S
                                                                 At



                                                             GmOS
                                                               GhO




                                                                                                             .1




                                     B                                                          Group
                                                                                                      1


                                         Gossypium hirsutum                   16.00         13.00         4.00          2.00
                                                    Zea mays                   5.00          5.00         1.00          1.00
                                                Oryza sativa                   4.00          5.00         1.00          1.00
                                                Vitis vinifera                 4.00          4.00         1.00          1.00
                                    Glycine max (Linn.) Merr                   9.00          8.00         2.00          2.00
                                         Arabidopsis thaliana                  8.00          5.00         1.00          1.00
                                           Helianthus annuus                   8.00          6.00         1.00          0.00
                                                                              1



                                                                                            2



                                                                                                          3



                                                                                                                       4
                                                                            up



                                                                                         up



                                                                                                       up



                                                                                                                     up
                                                                          ro



                                                                                       ro



                                                                                                     ro



                                                                                                                   ro
                                                                         G



                                                                                      G



                                                                                                    G



                                                                                                                 G




                                     Figure 2 (A) OSCA gene tree of sunflower, cotton, soybean, Arabidopsis thaliana, rice, grape, and
                                     maize. The different colors indicate different groups (1, 2, 3 and 4) of OSCA genes, different traits
                                     represent OSCA genes of different plants. (B) Sunflower, cotton, soybean, Arabidopsis thaliana, rice,
                                     grape, and maize OSCA gene evolutionary tree. The number of genes in each group.
                                                                                                     Full-size DOI: 10.7717/peerj.15089/fig-2




Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                                            9/26
                                                                                                                                                                                                          At1
                                                                                                                                                                    Zm7                                                          At4




                                                                                                                                                                                        300
                                                                                                                     275
                                                                                                                                                                                                                                             Gh




                                                                                                                     250




                                                                                                                                                                                              100
                                                                                                                      225




                                                                                                                                                                                               25
                                                                                                                                                                                               50
                                                                                                                      200




                                                                                                                                                                                              75
                                                                                                                                                                                                                                                    A07




                                                                                                                       175




                                                                                                                                                                                               0
                                                                                                                        150




                                                                                                                                                                                                                           25
                                                                                                                         125




                                                                                                                                                                                                                            0

                                                                                                                                                                                                                          50
                                                                                                                          100




                                                                                                                                                                                                                                        25
                                                                                                                                                                                                                                         0
                                                                                                                                                                                                                                                                       Gh




                                                                                                                            75




                                                                                                                                                                                                                                       50
                                                                                                                              50
                                                                                                                                                                                                                                                                         A1




                                                                                                                                                                                                                                                         75
                                                                                                                               25
                                                                                                                                                                                                                                                                           0




                                                                                                                                                                                              AtOSCA1.6
                                                                                                                                                                                              AtOSCA1.1
                                                                                                                                 22




                                                                                                                                 ZmOSCA1




                                                                                                                                                                                                           AtOSCA1.5
                                                                                                                                  0




                                                                                                                                                                                                                                                                   0
                                                                                                                                                                                                                          A1.8
                                                                                                                                   20




                                                                                                                                                                                                                                                                       25
                                                                                                                                    5
                                                                                                                    4




                                                                                                                                                                                                                                                                     50
                                                                                                                                      17
                                                                                                                                      0




                                                                                                                                                                                                                         AtOSC
                                                                                                              Zm




                                                                                                                                                                                                                                         1.10




                                                                                                                                                                                                                                                                   75
                                                                                                                                        .2
                                                                                                                                         15
                                                                                                                                                                                                                                                                                                     G




                                                                                                                                         5




                                                                                                                                                                                                                                                                                 0
                                                                                                                                                                                                                                        SCA



                                                                                                                                                                                                                                                   1.2




                                                                                                                                                                                                                                                                              10
                                                                                                                                                                                                                                                                                                         hA




                                                                                                                                           12
                                                                                                                                            0




                                                                                                                                                                                                                                                   SCA
                                                                                                                                                                                                                                       GhO




                                                                                                                                                                                                                                                               5
                                                                                                                                              5
                                                                                                              10




                                                                                                                                                                                                                                                           A1.
                                                                                                                                                                                                                                                                                                              11




                                                                                                                                                                                                                                                GhO




                                                                                                                                                                                                                                                                                    0
                                                                                                                                                                                                                                                            SC
                                                                                                                 0




                                                                                                                                                                                                                                                                                         25
                                                                                                                                                                                                                                                         GhO
                                                                                                              75




                                                                                                                                                                                                                                                                                            50
                                                                                                         50




                                                                                                                                                                                                                                                                                                     75
                                                                                                                                                                                                                                                                                                                   0




                                                                                                     25
                                                                                                     0                                                                                                                                                                                                        10




                                                                                                                                                                                                                                                                               5
                                                                                                                                                                                                                                                                              1.1
                                                                               40




                                                                                                                                                                                                                                                                           CA
                                                                                                                                                                                                                                                                         OS
                                                                             37 0




                                                                                                                                                                                                                                                                                                                                    Gh
                                                                                                                                                                                                                                                                                                                         0




                                                                                                                                                                                                                                                                         Gh
                                                                                                                    Zm
                                                                        35 5                                                                                                                                                                                                                                                  25




                                                                                                                      OS




                                                                                                                                                                                                                                                                                                                                           A1
                                                                                                                        CA
                                                                                                                            1.5
                                                                             0                                                                                                                                                                                                                                                         50
                                                                     32




                                                                                                                                                                                                                                                                                                                                                2
                                                                  30
                                                                        5                                                                                                                                                                                                                                                                75
                                                                     0                                                                                                                                                                                                                                                                        0
                                                                27                                                                                                                                                                                                                                                                         10
                                                                   5                                                                                                                                                                                                                                                                         0




                                                                                                                                                                                                                                                                                                                                                                Gh
                                                             25                                                                                                                                                                                                                                                        1.8
                                                                0                                                                                                                                                                                                                                              OS
                                                                                                                                                                                                                                                                                                                    CA
                                                                                                                                                                                                                                                                                                                                                        25
                                                           22




                                                                                                                                                                                                                                                                                                                                                                     D0
                                                                                                                                                                                                                                                                                                             Gh




                                                     1
                                                              5                                                                                                                                                                                                                                                                                          50

                                                   Zm
                                                                                                                                                                                                                                                                                                                                  .9
                                                          200                                                                                                                                                                                                                                                                A1




                                                                                                                                                                                                                                                                                                                                                                        5
                                                                                                                                                                                                                                                                                                                         SC
                                                                                                                                                                                                                                                                                                                                                           75
                                                                                                                                                                                                                                                                                                                       O
                                                                                                                                                                                                                                                                                                                    Gh
                                                        175
                                                                                                                                                                                                                                                                                                                                                                     100
                                                       150
                                                      125                                                                                                                                                                                                                                                                                                             0




                                                                                                                                                                                                                                                                                                                                                                           GhD
                                                    100                                                                                                                                                                                                                                                                                                                25
                                                                 ZmOS                                                                                                                                                                                                                                                                                                   50
                                                     75               CA1.




                                                                                                                                                                                                                                                                                                                                                                              08
                                                                                                                                                                                                                                                                                                                                                                         75
                                                                           3                                                                                                                                                                                                                                                                             2
                                                                                                                                                                                                                                                                                                                                                  CA1.1
                                                                                                                                                                                                                                                                                                                                           GhOS
                                                    50
                                                                                                                                                                                                                                                                                                                                                                          100
                                                   25
                                                                                                                                                                                                                                                                                                                                                                           125
                                                                                                                                                                                                                                                                                                                                                    CA    1.4
                                                                                                                                                                                                                                                                                                                                               GhOS

                                               0                   ZmOSC                                                                                                                                                                                                                                                                                                   0
                                              75




                                                                                                                                                                                                                                                                                                                                                                                 GhD10
                                                                         A1.1                                                                                                                                                                                                                                                                                 1.13
                                                                                                                                                                                                                                                                                                                                                GhOSCA
                                                                                                                                                                                                                                                                                                                                                                            25
                                             50
                                    Vv2




                                                                                                                                                                                                                                                                                                                                                                            50
                                             25                                                                                                                                                                                                                                                                                                                             75
                                                                  VvOSCA1.3
                                               0                                                                                                                                                                                                                                                                                                                             100
                                             75
                                                                                                                                                                                                                                                                                                                                                                            0
                                   Vv12




                                             50                                                                                                                                                                                                                                                                                                       GhOSCA1.7
                                                                                                                                                                                                                                                                                                                                                                            25




                                                                                                                                                                                                                                                                                                                                                                                 GhD11
                                             25                   VvOSCA1.2                                                                                                                                                                                                                                                                                                 50
                                               0                                                                                                                                                                                                                                                                                                                           75
                                    Vv10 O




                                              25                   VvOSCA
                                                                            1.4
                                                                                                                                                                                                                                                                                                                                                                           100
                                                0
                                                                           CA1.4
                                                                     OsOS                                                                                                                                                                                                                                                                                                 0
                                                     0                                                                                                                                                                                                                                                                                     GhOS
                                                                                                                                                                                                                                                                                                                                                                         25
                                           s10 O




                                                                                                                                                                                                                                                                                                                                                  CA1.1

                                                     25                    CA1.3                                                                                                                                                                                                                                                                          6
                                                                       OsOS
                                                                                                                                                                                                                                                                                                                                                                        50




                                                                                                                                                                                                                                                                                                                                                                              12
                                                         0                                                                                                                                                                                                                                                                                                             75




                                                                                                                                                                                                                                                                                                                                                                            GhD
                                                                                                                                                                                                                                                                                                                                    Gm
                                          s5




                                                                                      1.1                                                                                                                                                                                                                                                OSC
                                                                                   SCA                                                                                                                                                                                                                                                      A1.
                                                                                                                                                                                                                                                                                                                                                                      100
                                                         25                   OsO                                                                                                                                                                                                                                                                 1

                                                                                                                                                                                                                                                                                                                                                                 0
                                             Os1




                                                              0                             A2.1
                                                                                    HaO
                                                                                         SC
                                                                                                                                                                                                                                                                                                                                                               25
                                                             200                     A1
                                                                                        .1                                                                                                                                                                                                                         Gm
                                                                                                                                                                                                                                                                                                                     OS                                       50
                                                                 5                SC




                                                                                                                                                                                                                                                                                                                                                                       1
                                                                                                                                                                                                                                                                                                                       CA
                                                              17              HaO
                                                                                                                                                                                                                                                                                                                                                         75
                                                                                                                                                                                                                                                                                                                              1.9




                                                                                                                                                                                                                                                                                                                                                                     Gm
                                                                   0
                                                                15                                                                                                                                                                                                                                       Gm                                      0
                                                                     5                                                                                                                                                                                                                                     OS
                                                                   12                                                                                                                                                                                                                                         CA1
                                                                                                                                                                                                                                                                                                                  .2                           25
                                                                        0
                                                             Ha




                                                                     10                                                                                                                                                                                                                                                                    50
                                                                         75




                                                                                                                                                                                                                                                                                                                                                         3
                                                              17




                                                                                                                                                                                                                                                                                                                                       0




                                                                                                                                                                                                                                                                                                                                                  Gm
                                                                                                                                                                                                                                                                                         Gm

                                                                           50
                                                                                                                                                                                                                                                                                           OS
                                                                                                                    A
                                                                                                                      2.2                                                                                                                                                                       CA
                                                                                                                                                                                                                                                                                                  1.8                         25
                                                                              25
                                                                                                                 SC
                                                                                                              H
                                                                                                               aO
                                                                                                                                                                                                                                                                                                                         50
                                                                                    0
                                                                                                                             1.2




                                                                                                                                                                                                                                                                                                                                           4
                                                                                                                                                                                                                                                                              Gm
                                                                                                                                                                                                                                                                                                                   0
                                                                                                                            CA




                                                                                                                                                                                                                                                                                                                              Gm
                                                                                                                        OS




                                                                                                                                                                                                                                                                               OS
                                                                                                     5
                                                                                                                     Ha




                                                                                                                                                                                                                                                                                  CA
                                                                                                                                                                                                                                                                                                             25
                                                                                                   17




                                                                                                                                                                                                                                                                                     1
                                                                                                                                        1.4




                                                                                                                                                                                                                                                                                    .5
                                                                                                                                    CA
                                                                                                      12 0




                                                                                                                                   OS
                                                                                                        15




                                                                                                                                                                                                                                                                                                        50
                                                                                                                                   Ha




                                                                                                                                                                                                                                                                                                                    5
                                                                                                    10 5




                                                                                                                                                                                                                                                                                                              m
                                                                                                                                                                                                                                                                                                0
                                                                                                    Ha
                                                                                                                                                        1.7
                                                                                                      0




                                                                                                                                                                                                                                                                                                           G
                                                                                                                                                                                                                                                     HaO
                                                                                                                                                      A




                                                                                                                                                                                                                                                                                         25
                                                                                                         16
                                                                                                                                                   SC
                                                                                                   75




                                                                                                                                                                                                                                                                                                         7



                                                                                                                                                                                                                                                         SC
                                                                                                                                                  HaO
                                                                                                                      50




                                                                                                                                                                                                                                                          A1.




                                                                                                                                                                                                                                                                                    0
                                                                                                                                                                                                                                                                                                 Gm


                                                                                                                                                                                                                                                              8
                                                                                                                    25




                                                                                                                                                                                                                                                              25
                                                                                                                                   0




                                                                                                                                                                                                                                                                50
                                                                                                                                                                                                             HaOSCA1.3
                                                                                                                                    0




                                                                                                                                                                                                                                                                  75
                                                                                                                                   10
                                                                                                                                            75




                                                                                                                                                                                                                                                                   10
                                                                                                                                          50




                                                                                                                                                                                                                                                                           3

                                                                                                                                                                                                                                                                     125
                                                                                                                                                                                                                                                                         Ha


                                                                                                                                                                                                                                                                      0
                                                                                                                                        Ha
                                                                                                                                         25




                                                                                                                                                                                                                                                                       150
                                                                                                                                                           0




                                                                                                                                              7
                                                                                                                                                                                                    0
                                                                                                                                                        100




                                                                                                                                                                                                     25
                                                                                                                                                                75




                                                                                                                                                                                                      50
                                                                                                                                                               50




                                                                                                                                                                                                       75
                                                                                                                                                              25




                                                                                                                                                                                                        100
                                                                                                                                                                      0




                                                                                                                                                                                                         125




                                                                                                                                                              Ha6
                                                                                                                                                                          200




                                                                                                                                                                                                         150
                                                                                                                                                                          175




                                                                                                                                                                                                          175
                                                                                                                                                                            150




                                                                                                                                                                                                          0
                                                                                                                                                                                  125




                                                                                                                                                                                                          25
                                                                                                                                                                                        100

                                                                                                                                                                                                           50
                                                                                                                                                                                              75




                                                                                                                                                                                                                                   Ha4
                                                                                                                                                                                  Ha5



                                       Figure 3 Collinear relationship of OSCA genes in sunflower, cotton, soybean, Arabidopsis thaliana,
                                       rice, grape, and maize. The different colors represent a collinear relationship between different plants.
                                                                                                        Full-size DOI: 10.7717/peerj.15089/fig-3


                                   collinearity with Carthamus tinctorius, Helianthus annuus OSCA had more collinearity
                                   with other Compositae species, which indicates that the OSCA gene family was conserved
                                   in the evolution of Compositae. Moreover, Helianthus annuus and Lactuca sativa var.
                                   Angustata had the most collinear gene pairs and were also close to Lactuca sativa var.
                                   Angustata OSCA in the evolutionary tree, which indicates that the OSCA of Helianthus
                                   annuus and Lactuca sativa var. Angustata may have the same biological function.

                                   Gene structure and motif analysis of the OSCA gene of Compositae
                                   To further understand the composition of the sunflower OSCA gene, we compared the
                                   OSCA gene structure of seven Compositae species. All OSCA genes, except Group 4,
                                   contained introns (Fig. 6). Members of the same subfamily had similar conserved motifs,
                                   and Group 4 had the simplest gene structure and least number of motifs (Fig. 6). The Pfam
                                   website (http://pfam.xfam.org/family/pf02714#tabview=tab0) showed that the RSN1_7TM



Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                                                                                                                                                                                                                                                                            10/26
                                    A                                            Group
                                                                                      2




                                                                                                                CmOSCA2..   .3
                                                                                                                          .6
                                                                                                                AlOSCA2.3
                                                                  CtOSCA2.3
                                                                  CtOSCA2.2
                                                                  CeOSC




                                                                                                                       A2.6
                                                                  CiOSCA2




                                                                                                               HaOSCA2


                                                                                                              CeO A2.3
                                                                                                             CeO CA2.1
                                                                   LsOS
                                                                    HaO
                                                                    CmO CA2.1




                                                                                                                     A2.2

                                                                                                          Ha OSCA .5
                                                                                                         CtO OSC 2.6
                                                                                                           Cm SCA2
                                                                                                               LsOSC
                                                                      AlO CA2.4




                                                                                                                     C
                                                                       CtO CA2 .2




                                                                                                      AlO SC 2.5
                                                                        SCA .1




                                                                                                                   C
                                                                        CA2.2
                                                                         CtO SCA 2.3



                                                                         SC A




                                                                                                              CiOS
                                                                                                                   S
                                                                         Cm OSC A2. 3




                                                                         A2.6




                                                                                                                 S




                                                                                                     Ce SC A2.6
                                                                          S




                                                                                                                 A
                                                                           S
                                                                            Ha OSC A2. .1




                                                                                                               O
                                                                            .7




                                                                                                   Ci OS A2.5
                                                                             2.4
                                                                             O
                                                                             S




                                                                                               Ls OS CA 2.3
                                                                              2




                                                                                                            Cm
                                                                               Al SC A2 .5




                                                                                                 Ls OS CA
                                                                                                 O CA 2. 6
                                                                                 Ls OS CA2




                                                                                                     A2 .5
                                                                                   .5
                                                                                   O C



                                                                                   2
                                                                                    A 4
                                                                                    Ci OS




                                                                                                  SC 2
                                                                                                       .4
                                                                                      Ce
                                                                     C                                                             .4
                                                                  Ha iOS                                                        A2 .5
                                                               Ha OS CA                                                       SC A2 .1
                                                                  OS CA 2.2                                                 O C        4
                                                             Al                                                           Ce iOS CA .1
                                                                O C 2.                                                      C OS CA4 3
                                                          Ct SC A2. 1                                                          e
                                                       Cm OSC A2. 2                                                           C OS A4.




                                                                                                                                                  Gr
                                                          OS A2 2                                                               Ls OSC A4.2




                                                                                                                                                    o up
                                                      LsO CA .1                                                                   Ls SC 4.4
                                                                  2                                                                    O
                                                     LsO SCA2 .4                                                                    Ls SCA .3




                                                                                                                                                      4
                                                                                                                                               4
                                                         S        .7                                                                  LsO SCA .1
                                                    CiO CA2.                                                                             O
                                                        S        1                                                                     Ce SCA4
                                                  CeO CA2.4                                                                                O
                                                                                                                                        Cm CA4.1
                                                       S
                                                 CmO CA2.7                                                                                  S
                                                                                                                                         AlO CA4.2
                                                      SCA                                                                                     S
                                                CmO        3.3                                                                            CeO A4.1
                                                     SCA3                                                                                       C
                                               CmOS         .2                                                                            CiOS
                                                      CA3.1
                                               CmOSCA3
                                      Group3




                                                          .4
                                               HaOSCA3.1
                                               LsOSCA3.1
                                                                                                                                          CeOSCA1.1
                                                CiOSCA3.1                                                                                 CiOSCA1.1
                                               CeOSCA3.1                                                                                  LsOSCA1.9
                                                            1
                                                 AlOSCA3.                                                                                HaOSC
                                                                                                                                                   A1.1
                                                        A3.1
                                                 CtOSC                                                                                   CtOSC
                                                                                                                                                  A1.4
                                                         A1.8                                                                           AlOS
                                                  AlOSC 1.6                                                                                    C
                                                        CA                                                                              HaO A1.1
                                                  CtOS A1.7                                                                                  S
                                                                                                                                       HaO CA1.2
                                                       SC                                                                                   S
                                                  CmO CA1.6                                                                           Cm
                                                                                                                                         O
                                                                                                                                              C A1.
                                                                                                                                                    3
                                                      OS         .8                                                                  CtO SCA
                                                   Cm SCA1 5                                                                                     1.1
                                                        O        1.                                                                 AlO SCA
                                                    Cm SCA .8                                                                      Ls SCA 1.1
                                                                   1
                                                       CtO SCA .6                                                               Ce OSC 1.2
                                                            O        1
                                                         Ci
                                                                S CA 1.2                                                      Ci OS A1.1
                                                              O      A 4
                                                          Ce OSC A1. 0                                                       Ha OSC CA1
                                                                                                                           C O       A   .3
                                                             Ls SC A1.1 .7                                               Al tOS SCA 1.10
                                                                   O C    1                                                O C
                                                               Cm OS CA                                                     SC A 1.4
                                                                                   OS CA 1.5




                                                                   Al iOS                                                     A1 1.2




                                                                                            Ls mO CA .3
                                                                            Ha OSC A1 .6
                                                                                Ce iOS CA




                                                                                              C OS A1 7
                                                                                              O SC 1.8
                                                                                     C 1
                                                                                     A .4




                                                                      C                                                         .4




                                                                                               SC A
                                                                                   C OS




                                                                                               Ce OSC A1.
                                                                           AlO SCA 1.5




                                                                                                 Ci OSC 1.9




                                                                                                 A1 1.2
                                                                        Ha SCA 1.5
                                                                                       i
                                                                                     C




                                                                                                  Ce SCA 1.4
                                                                      Cm SCA 1.3




                                                                                                   .7
                                                                                                    CiO SCA .8
                                                                      LsO CA1 6




                                                                                                      LsO SCA1
                                                                                 1.
                                                                                 .5




                                                                                                       HaO CA1.3
                                                                     CiO CA1.6




                                                                                                        CtO CA1.9
                                                                        SCA .4
                                                                              Ls




                                                                                                         AlOS
                                                                             1.5
                                                                               O




                                                                         CA1.2




                                                                                                         CmO
                                                                              1


                                                                          A1.7




                                                                                                          AlOSC
                                                                           1.2




                                                                                                           AlOSCA
                                                                  CeOSCA1.2
                                                                  LsOSCA1.3


                                                                                                           AlOSCA1.7
                                                                         SCA




                                                                                                           HaOSCA1.7
                                                                                                           CmOSCA1.3




                                                                                                            S
                                                                         OS
                                                                           O

                                                                          S




                                                                   CiOSCA
                                                                   CtOSC




                                                                                                              SCA
                                                                    AlOS
                                                                    CeO




                                                                                                                A1.5
                                                                                                                  1.6

                                                                                                                  1.9




                                    B                                                            Group1

                                                   Cichorium endivia                      8.00            7.00         1.00                 3.00

                                        Lactuca sativa var. Angustata                     9.00            7.00         1.00                 4.00

                                             Carthamus tinctorius L.                      7.00            6.00         1.00                 0.00

                                                  Helianthus annuus                       8.00            6.00         1.00                 0.00

                                         Chrysanthemum morifolium                         9.00            6.00         4.00                 1.00

                                                    Arctium lappa L.                      10.00           5.00         1.00                 1.00

                                                  Cichorium intybus                       10.00           7.00         1.00                 1.00
                                                                                          1


                                                                                                          2


                                                                                                                      3


                                                                                                                                         4
                                                                                      up


                                                                                                      up


                                                                                                                   up


                                                                                                                                     up
                                                                                     ro


                                                                                                    ro


                                                                                                                 ro


                                                                                                                                  ro
                                                                                   G


                                                                                                  G


                                                                                                                 G


                                                                                                                               G




                                     Figure 4 (A) OSCA gene tree of sunflower, Arctium lappa, Chrysanthemum morifolium, Cichorium
                                     endivia, Cichorium intybus, Lactuca sativa, and Carthamus tinctorius. The different colors indicate dif-
                                     ferent groups (1, 2, 3 and 4) of OSCA genes, different traits represent OSCA genes of different plants.
                                     (B) Sunflowers, Arctium lappa, Chrysanthemum morifolium, Cichorium endivia, and Cichori.
                                                                                                     Full-size DOI: 10.7717/peerj.15089/fig-4




Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                                                        11/26
                                                                                                                                                                                                            Ls9                                 Al01                                  Al02
                                                                                                                                                                                         Ls8                                                                                                             Al03




                                                                                                                                                                                 125
                                                                                                                                                                                 100




                                                                                                                                                                                                                                    100
                                                                                                                                                                                                                                    125
                                                                                                                                                                                                                                    150
                                                                                                                                                                                                                                    175
                                                                                                                                                                                  150




                                                                                                                                                                                                                                     25
                                                                                                                                                                                                                                     50
                                                                                                                                                                                  125




                                                                                                                                                                                                                                    75
                                                                                                                                                                                  75
                                                                                                                                                                                  50
                                                                                                                                                                                  100


                                                                                                                                                                                  25
                                                                                                                                                                Ls7                                                                                                                                                        Al0




                                                                                                                                                                                                                                     0




                                                                                                                                                                                                                                                                                       25
                                                                                                                                                                                    0




                                                                                                                                                                                                                                                                                      50
                                                                                                                                                                                    75
                                                                                                                                                                                                                                                                                                                               6




                                                                                                                                                                                                                                                                                      75
                                                                                                                                                                                    50




                                                                                                                                                                                                                                                                                       0
                                                                                                                                                                                     25
                                                                                              1750
                                                                                                                                                                                                                                                                                                                                              Al0




                                                                                              15 5




                                                                                                                                                                                                                                                                                                      25
                                                                                               12 0




                                                                                                                                                                                                                                                                                                     50
                                                                                                                                                                                      0




                                                                                                                                                                                                                                                                                                      0
                                                                                               1075




                                                                                                                                                                                                                                                                                                     75
                                                                                                                                                                                                                                                                                                                                                      8 A




                                                                                                                                                                                                                                                                                                                      55
                                                                                                  50




                                                                                                                                                                                                                                                                                                                       0
                                                                                                                                                                                                                                                                                                                     750
                                                                                                                                                                                                                                                                                                                                                          l11




                                                                                                   250




                                                                                                                                                                                                                                                                                                                      2
                                                                                                                                                      6




                                                                                                    25205
                                                                                                                                                    Ls




                                                                                                     2 00
                                                                                                      2 5
                                                                                                                                                                                                                                                                                                                                                                           Al




                                                                                                                                                                                                                                                                                                                                       505
                                                                                                                                                                                                                                    AlOSCA1.4
                                                                                                                                                                                                                        LsOSCA2.3
                                                                                                       17 0




                                                                                                                                                                                                                                                                                                                                         0
                                                                                                                                                                                                           LsOSCA1.2




                                                                                                                                                                                                                                                                     3




                                                                                                                                                                                                                                                                                                                                        2
                                                                                                        1525
                                                                                                                                                                                                                                                                                                                                                                              13




                                                                                                                                                                                                                                                                  AlOSCA1.
                                                                                                                                                                                            LsOSCA
                                                                                                         1 00




                                                                                                                                                                                                                                                                                        A2.4
                                                                                                          1 75




                                                                                                                                                                                                                                                                                                                                                       505
                                                                                                                                                                                                                                                                                                                                                         0
                                                                                                                                                                                                                                                                                                                                                                                           Al




                                                                                                                                                                             LsOS




                                                                                                                                                                                                                                                                                                                                                        2
                                                                                                                                                                                                                                                                                      AlOSC
                                                                                                             50
                                                                                                                                                                                                                                                                                                                                                                                                14




                                                                                                                                                                                                   1.5




                                                                                                                                                                                                                                                                                                                            1.1
                                                                                                              LsO SCA1.
                                                                                                              250




                                                                                                                                                                                 CA1.7




                                                                                                                                                                                                                                                                                                                                                                    505
                                                                                                               LsO




                                                                                                                                                                                                                                                                                                                                                                      0
                                                                                                                                                                                                                                                                                                                          2.2
                                                                                                                                                                                                                                                                                                                       SCA




                                                                                                                                                                                                                                                                                                                                                                     2
                                                                                                                 SCA 1




                                                                                                                                                                                                                                                                                                                      SCA
                                                                                                                                                                                                                                                                                                                                                                                                           Al




                                                                                                                  35250
                                                                                                                   3 0 5




                                                                                                                                                                                                                                                                                                                                          8
                                                                                                                                                                                                                                                                                                                   AlO
                                                                                                                    LsO




                                                                                                                                                                                                                                                                                                                                      A1.
                                                                                                                    3.1
                                                                                                                                                                                                                                                                                                                                                                                                             15




                                                                                                                                                                                                                                                                                                                  AlO
                                                                                                                     0
                                                                                                                     3




                                                                                                                                                                                                                                                                                                                                                                                       0
                                                                                                                                                                                                                                                                                                                                                                                   5 5
                                                                                                                                                                                                                                                                                                                                                 .9
                                                                                                                        27 50 5
                                                                                                 5




                                                                                                                                                                                                                                                                                                                                     SC




                                                                                                                                                                                                                                                                                                                                                                                     2
                                                                                                                        LsO




                                                                                                                                                                                                                                                                                                                                                                                  75 0
                                                                                                                        SC




                                                                                                                                                                                                                                                                                                                                                A1
                                                                                              Ls




                                                                                                                          2 2 0




                                                                                                                                                                                                                                                                                                                                  AlO
                                                                                                                           A2.
                                                                                                                            SC




                                                                                                                                                                                                                                                                                                                                              SC
                                                                                                                             2 0 5




                                                                                                                                                                                                                                                                                                                                                            .2
                                                                                                                               2
                                                                                                                               A1




                                                                                                                                                                                                                                                                                                                                          AlO
                                                                                                                               LsO
                                                                                                                                2 7 0




                                                                                                                                                                                                                                                                                                                                                           A1
                                                                                                                                 .4




                                                                                                                                                                                                                                                                                                                                                                                                    0

                                                                                                                                                                                                                                                                                                                                                                                                                         Al
                                                                                                                                  1 5




                                                                                                                                                                                                                                                                                                                                                                                                 50 5
                                                                                             1




                                                                                                                                                                                                                                                                                                                                                       SC
                                                                                                                                   SC
                                                                                           10 25




                                                                                                                                                                                                                                                                                                                                                                                                  2
                                                                                                                                    1




                                                                                                                                                                                                                                                                                                                                                      AlO
                                                                                                                                      A1




                                                                                                                                                                                                                                                                                                                                                                                                                         16 C
                                                                                                                                                                                                                                                                                                                                                                                                                     0 5




                                                                                                                                         .3
                                                                                           7 0                                                                                                                                                                                                                                                                                                                        2 0




                                                                                                                                                                                                                                                                                                                                                                               .10
                                                                                                                                            Ls
                                                                                          5 5                                                                                                                                                                                                                                                                                                                          5 5




                                                                                                                                                                                                                                                                                                                                                                            A1
                                                                                                                                               OS
                                                                                        25 0




                                                                                                                                                                                                                                                                                                                                                                            SC
                                                                                                                                                                                                                                                                                                                                                                                                                         7




                                                                                                                                                  CA




                                                                                                                                                                                                                                                                                                                                                                                                                            Cen
                                                                                                                                                                                                                                                                                                                                                                         AlO




                                                                                                                                                                                                                                                                                                                                                                                          .1
                                                                                                                                                     2.1




                                                                                                                                                                                                                                                                                                                                                                                                                              e
                                                                                        0




                                                                                                                                                                                                                                                                                                                                                                                       A2
                                                                 4                                                                                                                                                                                                                                                                                                                                                         0




                                                                                                                                                                                                                                                                                                                                                                                                                               01
                                                                                                                                                                                                                                                                                                                                                                                    SC
                                                                3 00                                                                                                                                                                                                                                                                                                                                                                 0 5




                                                                                                                                                                                                                                                                                                                                                                                 AlO
                                                               3 75                                                                                                                                                                                                                                                                                                                                                                   2




                                                                                                                                                                                                                                                                                                                                                                                                                                  Ce
                                                                                                                                                                                                                                                                                                                                                                                                         .5
                                                              3 50                                                                                                                                                                                                                                                                                                                                SC
                                                                                                                                                                                                                                                                                                                                                                                                       A2

                                                             3 25                                                                                                                                                                                                                                                                                                                                               1.8
                                                                                                                                                                                                                                                                                                                                                                                                                                              0 5




                                                                                                                                                                                                                                                                                                                                                                                                                                     02
                                                                                                                                                                                                                                                                                                                                                                                               AlO
                                                            2700                                                                                                                                                                                                                                                                                                                                          OS
                                                                                                                                                                                                                                                                                                                                                                                                            CA
                                                                                                                                                                                                                                                                                                                                                                                                                  A1
                                                                                                                                                                                                                                                                                                                                                                                                                    .2
                                                                                                                                                                                                                                                                                                                                                                                                                                               2 0
                                                           2 5                                                                                                                                                                                                                                                                                                                                       Ce        SC                               5




                                                                                                                                                                                                                                                                                                                                                                                                                                        C
                                                          2 50
                                                                                                                                                                                                                                                                                                                                                                                                             O
                                                                                                                                                                                                                                                                                                                                                                                                          Ce
                                                         2 25
                                                                                             LsO




                                                                                                                                                                                                                                                                                                                                                                                                                                                             e0
                                                       4
                                                                                                   SC                                                                                                                                                                                                                                                                                                                                                 05
                                                        1 00




                                                    Ls
                                                                                                      A2
                                                                                                                                                                                                                                                                                                                                                                                                                                                      20




                                                                                                                                                                                                                                                                                                                                                                                                                                                                3C
                                                       1 75
                                                                                                         .5
                                                                                                                                                                                                                                                                                                                                                                                                                                                       5
                                                      1250




                                                                                                                                                                                                                                                                                                                                                                                                                                                                  e05
                                                     1005                                                                                                                                                                                                                                                                                                                                                                       A1
                                                                                                                                                                                                                                                                                                                                                                                                                                  .5                     05
                                                                                                                                                                                                                                                                                                                                                                                                                            SC                           20
                                                     7                                                                                                                                                                                                                                                                                                                                                                   CeO
                                                                                                                                                                                                                                                                                                                                                                                                                                                          5
                                                     55
                                                    250
                                                                                                                                                                                                                                                                                                                                                                                                                                          6
                                                                                                                                                                                                                                                                                                                                                                                                                                       A1.




                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Ce0
                                                                                                                                                                                                                                                                                                                                                                                                                                  SC
                                                                 LsO
                                                                    SC                                                                                                                                                                                                                                                                                                                                                         CeO                          05
                                                    0                  A               1.9                                                                                                                                                                                                                                                                                                                                                                  20
                                                 20
                                                                       LsO
                                                                             SCA                                                                                                                                                                                                                                                                                                                                                                             5




                                                                                                                                                                                                                                                                                                                                                                                                                                                                        6
                                                17 0                 LsO          2.7                                                                                                                                                                                                                                                                                                                                                           2.6
                                                                                                                                                                                                                                                                                                                                                                                                                                             SCA
                                               15 5
                                                                         SCA
                                                                                                                                                                                                                                                                                                                                                                                                                                     CeO                           0




                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Ce0
                                                                                 1.8

                                              12 0                                                                                                                                                                                                                                                                                                                                                                                                                 25
                                              1005
                                                                 LsO
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    50
                                      Ls3




                                                                       SCA                                                                                                                                                                                                                                                                                                                                                                       2.2
                                                                           4.1                                                                                                                                                                                                                                                                                                                                                               SCA 1
                                                                                                                                                                                                                                                                                                                                                                                                                                         CeOOSCA1.                   75 0




                                                                                                                                                                                                                                                                                                                                                                                                                                                                           8C
                                               75                                                                                                                                                                                                                                                                                                                                                                                        Ce
                                                                                                                                                                                                                                                                                                                                                                                                                                                CA2.3                10
                                              50                                                                                                                                                                                                                                                                                                                                                                                           CeOS
                                              25                                                                                                                                                                                                                                                                                                                                                                                                                     0




                                                                                                                                                                                                                                                                                                                                                                                                                                                                             e09
                                               0                                                                                                                                                                                                                                                                                                                                                                                                                     25
                                                                                                                                                                                                                                                                                                                                                                                                                                                   CeOS
                                                                                                                                                                                                                                                                                                                                                                                                                                                        CA1.3
                                                                                                                                                                                                                                                                                                                                                                                                                                                                      50
                                            150                                                                                                                                                                                                                                                                                                                                                                                                                       0
                                           125                                                                                                                                                                                                                                                                                                                                                                                                                         25
                                           100           LsOSCA
                                                                                                                                                                                                                                                                                                                                                                                                                                                                       50
                                    Ls2




                                                                 4.4




                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Ci01
                                            75                                                                                                                                                                                                                                                                                                                                                                                                                         75
                                            50                                                                                                                                                                                                                                                                                                                                                                                                                          100
                                            25                                                                                                                                                                                                                                                                                                                                                                                                                          125
                                             0                                                                                                                                                                                                                                                                                                                                                                                                                          150
                                                                                                                                                                                                                                                                                                                                                                                                                                                      CiOSCA1.2         175
                                          200                                                                                                                                                                                                                                                                                                                                                                                                                           200
                                          175          HaOSCA2.1
                                   Ha17




                                          150                                                                                                                                                                                                                                                                                                                                                                                                                       0
                                          125          HaOSCA1.1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    25
                                          100                                                                                                                                                                                                                                                                                                                                                                                                                       50
                                           75                                                                                                                                                                                                                                                                                                                                                                                                                       75
                                            50                                                                                                                                                                                                                                                                                                                                                                                                        CiOSCA2.1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    100




                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Ci02
                                            25                                                                                                                                                                                                                                                                                                                                                                                                                     125
                                             0                                                                                                                                                                                                                                                                                                                                                                                                CiOSCA1.4
                                                                                                                                                                                                                                                                                                                                                                                                                                                                   150
                                                                                                                                                                                                                                                                                                                                                                                                                                                                   175
                                           175
                                                               2.2
                                                        HaOSCA
                                                                                                                                                                                                                                                                                                                                                                                                                                                                   200
                                           150          HaOSCA
                                                              1.2                                                                                                                                                                                                                                                                                                                                                                            CiOSCA
                                                                                                                                                                                                                                                                                                                                                                                                                                                    2.3
                                    Ha16




                                           125                                                                                                                                                                                                                                                                                                                                                                                              CiOSCA
                                                                                                                                                                                                                                                                                                                                                                                                                                                    1.1           0
                                            100                                                                                                                                                                                                                                                                                                                                                                                                                   25
                                             75           HaOS
                                                               CA  1.4
                                                                                                                                                                                                                                                                                                                                                                                                                                                                 50
                                              50                                                                                                                                                                                                                                                                                                                                                                                                                 75
                                              25
                                                                                                                                                                                                                                                                                                                                                                                                                                         CiOS
                                                                                                                                                                                                                                                                                                                                                                                                                                                                10
                                                                                                                                                                                                                                                                                                                                                                                                                                                                1250




                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Ci03
                                                                                                                                                                                                                                                                                                                                                                                                                                              CA2.6
                                                0
                                                                                                                                                                                                                                                                                                                                                                                                                                                               1 5
                                                                                                                                                                                                                                                                                                                                                                                                                                                               1750
                                                                                                                                                                                                                                                                                                                                                                                                                                       CiOS
                                                                                                                                                                                                                                                                                                                                                                                                                                            CA1.8

                                              1505               SCA
                                                                           3.1
                                                                                                                                                                                                                                                                                                                                                                                                                                                              0
                                              12 0            HaO
                                                                                                                                                                                                                                                                                                                                                                                                                                                             25
                                               10 5
                                      Ha1




                                                 7
                                                                                                                                                                                                                                                                                                                                                                                                                                  CiO
                                                                                                                                                                                                                                                                                                                                                                                                                                                            5
                                                                                                                                                                                                                                                                                                                                                                                                                                                            750
                                                                                                                                                                                                                                                                                                                                                                                                                                      SCA
                                                 505
                                                                                                                                                                                                                                                                                                                                                                                                                                          1.3

                                                                                                                                                                                                                                                                                                                                                                                                                                                           1
                                                  20                                                                                                                                                                                                                                                                                                                                                                                                      1 00




                                                                                                                                                                                                                                                                                                                                                                                                                                                                        4
                                                                                         6
                                           5




                                                                                   A2.
                                                                                                                                                                                                                                                                                                                                                                                                                                                         15205
                                                                              SC




                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Ci0
                                                                         HaO

                                                    15205                                                                                                                                                                                                                                                                                                                                                                                               0
                                                                                                                                                                                                                                                                                                                                                                                                                                                       25
                                                     1 00                                                                                                                                                                                                                                                                                                                                                                                            5
                                                      1 75                                                                                                                                                                                                                                                                                                                                                                                         70
                                                         505                                                                                                                                                                                                                                                                                                                                                                                      105
                                               Ha




                                                                                                                                                                                                                                                                                                                                                                                                                                                                      6
                                                                               2.5                                                                                                                                                                                                                                                                                                                                C
                                                                             CA                                                                                                                                                                                                                                                                                                                                  CiOiOSC




                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Ci0
                                                          20            Ha
                                                                          OS
                                                                                                                                                                                                                                                                                                                                                                                                                     SC A3.1                          0
                                                                                                                                                                                                                                                                                                                                                                                                                                               0
                                                12




                                                                                                                                                                                                                                                                                                                                                                                                                       A1

                                                              0
                                                                                                                                                                                                                                                                                                                                                                                                            C
                                                                                                                                                                                                                                                                                                                                                                                                           CiOiOSC
                                                                                                                                                                                                                                                                                                                                                                                                                          .10
                                                                                                                                                                                                                                                                                                                                                                                                                                              2 5
                                                           2075                                                                                                                                                                                                                                                                                                                                                                            5
                                                                                                                                                                                                                                                                                                                                                                                                                                         70
                                                                                                                                                                                                                                                                                                                                                                                                               SC 2A
                                                                                                                                                                                                                                                                                                                                                                                                                 A1 .7
                                                             1 50                                                                                                                                                                                                                                                                                                                                                                       105
                                                                                                                                                                                                                                                                                                                                                                                                                    .9
                                                              1 25




                                                                                                                                                                                                                                                                                                                                                                                                                                                             07
                                                                                                                      2.3
                                                               1 00                                                 CA
                                                                                                                                                                                                                                                                                                                                                                                                                                    0 0
                                                                                                                                                                                                                                                                                                                                                                                               Cm
                                                                                                                OS          1.7                                                                                                                                                                                                                                                                   OS




                                                                                                                                                                                                                                                                                                                                                                                                                                                       Ci
                                                                1 75                                          Ha         CA                                                                                                                                                                                                                                                                          CA                           2
                                                                                                                                 2.4
                                                                                                                                                                                                                                                                                                                                                                                                                                5 5
                                                        Ha




                                                                   505
                                                                                                                     OS        A                                                                                                                                                                                                                                                                        3.4
                                                                                                                   Ha
                                                                     2 0
                                                                                                                            SC
                                                                                                                                                                                                                                                                                                                                                                                                                               7 0
                                                                                                                         aO
                                                                                                                                                                                                                                                                                                                                                                                                                              1 5
                                                           9




                                                                                                                      H
                                                                                                                                                                                                                                                                                                                                                                                                                           12 00




                                                                                                                                                                                                                                                                                                                                                                                 Cm
                                                                          0




                                                                                                                                                                                                                                                                                                                                                                                   OS
                                                                       10 75 0




                                                                                                                                                                                                                                                                                                                                                                                                                                              09
                                                                                                                                                                                                                                                                                                                                                                                                                       0 5




                                                                                                                                                                                                                                                                                                                                                                                       CA
                                                                                                                                               .5




                                                                                                                                                                                                                                                                                                                                                                                                                     2
                                                                                                                                            A1




                                                                                                                                                                                                                                                                                                                                                                                          1
                                                                                                                                                                                                                                                                                                                                                                    Cm




                                                                                                                                                                                                                                                                                                                                                                                         .8
                                                                            5 5                                                                                                                                                                                                                                                                                                                                   50 5




                                                                                                                                                                                                                                                                                                                                                                                                                                        Ci
                                                                                                                                          C
                                                                                                                                       OS




                                                                                                                                                                                                                                                                                                                                                                         OS
                                                                               2 0
                                                                                                                                       Ha




                                                                                                                                                                                                                                                                                                                                                                          CA
                                                                                                                                                                                                                                                                                                                                                            Cm
                                                                           Ha




                                                                                                                                                                                                                                                                                                                                                                            1.6




                                                                                                                                                                                                                                                                                                                                                                                                                 75
                                                                                                                                                                                                                                                                                                                                                             OS
                                                                                                 7 0




                                                                                                                                                                                                                                                                                                                                                                 CA
                                                                                  7




                                                                                                                                                                                                                                                                                                                                                 Cm




                                                                                                                                                                                                                                                                                                                                                                                                                               1
                                                                                                 10
                                                                                                5 5




                                                                                                                                                                                                                                                                                                                                                                                               0 5
                                                                                                                                                        .3




                                                                                             Ha




                                                                                                                                                                                                                                                                                                                                                                   1.9




                                                                                                                                                                                                                                                                                                                                                                                                                          m
                                                                                              25 0




                                                                                                                                                                                                                                                                                                                                                  OS
                                                                                                                                                     A1




                                                                                                                                                                                                                                                                                                                                                                                                2 0
                                                                                                                                                                                                                                                                                                                                      Cm




                                                                                                                                                                                                                                                                                                                                                      CA




                                                                                                                                                                                                                                                                                                                                                                                                 5
                                                                                                                                                    6
                                                                                                                                                 SC




                                                                                                                                                                                                                                                                                                                                                                                                                         C
                                                                                                6
                                                                                                                                                A1.
                                                                                              0




                                                                                                                                                                                                                                                                                                                                         O
                                                                                                                                             HaO




                                                                                                                                                                                                                                                                                                                                                      2.4
                                                                                                                                                                                                                                                                                                                                                                                                        2


                                                                                                                                                                                                                                                                                                                           Cm



                                                                                                                                                                                                                                                                                                                                       SC
                                                                                                                                             SC




                                                                                                                                                                                                                                                                                                                                                                     0
                                                                                                                                       1 00




                                                                                                                                                                                                                                                                                                                                                                                                       m




                                                                                                                                                                                                                                                                                                                                                                      250
                                                                                                                                                                                                                                                                                                                                         A2.
                                                                                                                                         HaO




                                                                                                                                                                                                                                                                                                                              O
                                                                                                                                      1 75




                                                                                                                                                                                                                                                                                                                             SC




                                                                                                                                                                                                                                                                                                                                                                       5
                                                                                                                                                                                                                                                                                                                                                                                                     3C
                                                                                                                                                                           8




                                                                                                                                                                                                                                                                                                                                             3
                                                                                                                                     1 50
                                                                                                                                        2




                                                                                                                                                                                                                                                                                                         CtOS
                                                                                                                                                                       CA1.




                                                                                                                                                                                                                                                                                                                               A2.




                                                                                                                                                                                                                                                                                                                                                                         0 5
                                                                                                                                    1025




                                                                                                                                                                                                                                                                                               CtOS




                                                                                                                                                                                                                                                                                                                                                                          20
                                                                                                                                    750




                                                                                                                                                                                                                                                                                                                                  6
                                                                                                                                                                                                                                                                                                                                                                               Cm
                                                                                                                                                                                                                                                                                      CtOSC




                                                                                                                                                                                                                                                                                                                                                                           5
                                                                                                                                                                                                                                                                                                          CA1.1
                                                                                                                                                                      HaOS




                                                                                                                                                                                                                                                                         CtOSCA1
                                                                                                                                  250




                                                                                                                                 Ha
                                                                                                                                                                                                                                                             CtOSCA2.1
                                                                                                                                                                                                            CtOSCA1.6
                                                                                                                                                                                                            CtOSCA2.6




                                                                                                                                                                                                                                                 CtOSCA2.4




                                                                                                                                                                                                                                                                                                    CA




                                                                                                                                                                                                                                                                                                                                  05
                                                                                                                                   5




                                                                                                                                                                                                                                                                                                                                                                            m4



                                                                                                                                                                                                                                                                                                                                  20
                                                                                                                              1 0




                                                                                                                                                                                                                                                                                                  1.2




                                                                                                                                       5
                                                                                                                                                                                                                                                                                       A1.3




                                                                                                                                                                                                                                                                                                                                   5
                                                                                                                             1 75




                                                                                                                                                                                                                                                                                                                                     05
                                                                                                                            12550




                                                                                                                                                                                                                                                                                                                                                                          5C

                                                                                                                                                                                                                                                                                                                                     20
                                                                                                                                                                                                                                                                                 .4




                                                                                                                                                                                                                                                                                                                                      5
                                                                                                                           100
                                                                                                                           505




                                                                                                                                                                                                                                                                                                                                       05
                                                                                                                                                                                                                                                                                                                                        2
                                                                                                                                                                                                                                                                                                                                                                 Cm
                                                                                                                            7
                                                                                                                          25
                                                                                                                          0




                                                                                                                                                                                                                                                                                                                                          m8
                                                                                                                                                                                                                                                                                                                05

                                                                                                                                                          Ha
                                                                                                                                                                                                                                                                                                                20
                                                                                                                                                                 12 0




                                                                                                                                                                                                                                                                                                                 5
                                                                                                                                                                1005




                                                                                                                                                                                                                                                                                                                 75 0




                                                                                                                                                            4                                                                                                                                                                           9C
                                                                                                                                                                 15




                                                                                                                                                                                                                                                                                                                  10
                                                                                                                                                                 75
                                                                                                                                                                50




                                                                                                                                                                                                                                                                  0
                                                                                                                                                                25




                                                                                                                                                                                                                                                                                                                                      Cm
                                                                                                                                                                                                                                                                  25
                                                                                                                                                                 0




                                                                                                                                                                                                                                                                   50
                                                                                                                                                                                                                                                                   75
                                                                                                                                                                                          100




                                                                                                                                                                                                                                                                    100
                                                                                                                                                                                           75
                                                                                                                                                                                          50




                                                                                                                                                                                                                                                                    0
                                                                                                                                                                                          25




                                                                                                                                                                                                                                                                     25




                                                                                                                                                                                                                                                                                                                      1
                                                                                                                                                                                           0




                                                                                                                                                                  Ha3
                                                                                                                                                                                                                                                                     50
                                                                                                                                                                                                                                                                     75
                                                                                                                                                                                         50




                                                                                                                                                                                                                                                                                                                  Ct0
                                                                                                                                                                                         25
                                                                                                                                                                                           0




                                                                                                                                                                                                                                      0
                                                                                                                                                                                                                                      25
                                                                                                                                                                                         50

                                                                                                                                                                                                                                      50
                                                                                                                                                                                         25
                                                                                                                                                                                                                                      75
                                                                                                                                                                                          0




                                                                                                                                                                                         Ct12
                                                                                                                                                                                                         Ct11 Ct10 Ct09                                           Ct04                         Ct03




                                     Figure 5 Collinearity of sunflowers, Arctium lappa, Chrysanthemum morifolium, Cichorium endivia,
                                     Cichorium intybus, Lactuca sativa, and Carthamus tinctorius OSCA genes. The different colors repre-
                                     sent a collinear relationship between different plants.
                                                                                                 Full-size DOI: 10.7717/peerj.15089/fig-5


                                   domain generally contained seven transmembrane domains. In this article, motif 2, motif
                                   3, motif 4, motif 6, motif 7, motif 8, and motif 9 showed that they may contain multiples
                                   of the seven transmembrane domains. Only a few OSCA genes (CtOSCA1.5, CiOSCA2.2,
                                   and LsOSCA4.1) contained a motif, although they were relatively long. CmOSCA2.2 was
                                   the longest and contained 10 exons, but it also contained eight motifs. The LsOSCA4.4
                                   gene had the shortest length and contained one exon but only one motif (Motif 3). This
                                   indicates that the distribution of OSCA gene motifs in Compositae was highly correlated
                                   with the length of the genes.




Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                                                                                                                                                                                                                                                                                                                                                                          12/26
                                         Phylogenetic tree       Conserved motif     Phylogenetic tree    Conserved motif                  Phylogenetic tree     Gene structural   Phylogenetic tree       Gene structural
                                                    CeOSCA1.1                                 CeOSCA2.7                                             CeOSCA1.1
                                                    CiOSCA1.1                                                               Motif 8                                                           CeOSCA2.7                      CDS
                                                                                              CiOSCA2.4                                             CiOSCA1.1
                                                                                                                            Motif 4                                                           CiOSCA2.4                      UTR
                                                    LsOSCA1.9                                 LsOSCA2.1                                             LsOSCA1.9
                                                                                                                            Motif 7                                                           LsOSCA2.1
                                                    HaOSCA1.1                                 LsOSCA2.7                                             HaOSCA1.1
                                                                                                                            Motif 9                                                           LsOSCA2.7
                                                    CtOSCA1.4                                 CmOSCA2.4                                             CtOSCA1.4                                 CmOSCA2.4
                                                    AlOSCA1.1                                 CtOSCA2.1                     Motif 2
                                                                                                                            Motif 3                 AlOSCA1.1                                 CtOSCA2.1
                                                    HaOSCA1.2                                 AlOSCA2.2
                                                                                                                            Motif 6                 HaOSCA1.2                                 AlOSCA2.2
                                                    HaOSCA1.3                                 HaOSCA2.2
                                                                                                                            Motif 10                HaOSCA1.3                                 HaOSCA2.2
                                                    CmOSCA1.1                                 HaOSCA2.1
                                                                                                                            Motif 5                 CmOSCA1.1                                 HaOSCA2.1
                                                    CtOSCA1.1                                 CiOSCA2.2
                                                                                                                            Motif 1                 CtOSCA1.1                                 CiOSCA2.2
                                                    AlOSCA1.12                                CeOSCA2.5
                                                                                                                                                    AlOSCA1.12                                CeOSCA2.5
                                                    LsOSCA1.1                                 CiOSCA2.1
                                                                                                                                                    LsOSCA1.1                                 CiOSCA2.1
                                                    CeOSCA1.3                                 LsOSCA2.3
                                                                                                                                                    CeOSCA1.3                                 LsOSCA2.3
                                                                                              AlOSCA2.4
                                                    CiOSCA1.10                                                                                      CiOSCA1.10                                AlOSCA2.4
                                                                                              HaOSCA2.3
                                                    HaOSCA1.4                                                                                       HaOSCA1.4                                 HaOSCA2.3
                                                                                              CmOSCA2.2
                                                    CtOSCA1.2                                                                                                                                 CmOSCA2.2
                                                                                              CtOSCA2.5                                             CtOSCA1.2
                                                    AlOSCA1.4                                                                                                                                 CtOSCA2.5
                                                                                              CtOSCA2.4                                             AlOSCA1.4                                 CtOSCA2.4
                                                    LsOSCA1.7                                 AlOSCA2.1                                             LsOSCA1.7
                                                    CmOSCA1.2                                                                                                                                 AlOSCA2.1




                                                                                   Group2
                                                                                              CmOSCA2.1                                             CmOSCA1.2




                                                                                                                                                                                   Group2
                                                    CeOSCA1.8                                                                                                                                 CmOSCA2.1
                                                                                              HaOSCA2.4                                             CeOSCA1.8
                                                    CiOSCA1.3                                                                                                                                 HaOSCA2.4
                                                                                              LsOSCA2.2                                             CiOSCA1.3
                                                    CeOSCA1.7                                                                                                                                 LsOSCA2.2
                                                                                              CeOSCA2.6                                             CeOSCA1.7                                 CeOSCA2.6
                                                    CiOSCA1.9                                 CiOSCA2.7                                             CiOSCA1.9                                 CiOSCA2.7
                                                    LsOSCA1.4                                 CtOSCA2.2                                             LsOSCA1.4                                 CtOSCA2.2
                                                    HaOSCA1.8                                 CtOSCA2.3                                             HaOSCA1.8                                 CtOSCA2.3
                                                    CtOSCA1.3                                 AlOSCA2.3
                                                                                                                                                    CtOSCA1.3                                 AlOSCA2.3
                                                    AlOSCA1.9                                 CmOSCA2.3
                                                                                                                                                    AlOSCA1.9                                 CmOSCA2.3
                                                    CmOSCA1.9                                 HaOSCA2.6
                                                                                                                                                    CmOSCA1.9                                 HaOSCA2.6
                                                    AlOSCA1.5                                 LsOSCA2.6
                                                                                                                                                    AlOSCA1.5                                 LsOSCA2.6
                                       Group1
                                                                                              CiOSCA2.3




                                                                                                                                       Group1
                                                    AlOSCA1.6                                                                                       AlOSCA1.6                                 CiOSCA2.3
                                                    AlOSCA1.7                                 CeOSCA2.1
                                                                                                                                                    AlOSCA1.7                                 CeOSCA2.1
                                                    HaOSCA1.7                                 CeOSCA2.2
                                                                                                                                                    HaOSCA1.7                                 CeOSCA2.2
                                                                                              CmOSCA2.5
                                                    CmOSCA1.3                                                                                       CmOSCA1.3                                 CmOSCA2.5
                                                                                              CmOSCA2.6
                                                    LsOSCA1.3                                                                                       LsOSCA1.3                                 CmOSCA2.6
                                                                                              HaOSCA2.5
                                                    CeOSCA1.2                                                                                       CeOSCA1.2                                 HaOSCA2.5
                                                                                              CtOSCA2.6
                                                    CiOSCA1.2                                                                                                                                 CtOSCA2.6
                                                                                              AlOSCA2.5                                             CiOSCA1.2
                                                    CtOSCA1.7                                                                                                                                 AlOSCA2.5
                                                                                              CeOSCA2.3                                             CtOSCA1.7                                 CeOSCA2.3
                                                    AlOSCA1.2                                 CiOSCA2.6                                             AlOSCA1.2
                                                    CeOSCA1.5                                                                                                                                 CiOSCA2.6
                                                                                              LsOSCA2.5                                             CeOSCA1.5
                                                    CiOSCA1.4                                                                                                                                 LsOSCA2.5
                                                                                              LsOSCA2.4                                             CiOSCA1.4
                                                    LsOSCA1.6                                                                                                                                 LsOSCA2.4
                                                                                              CeOSCA2.4                                             LsOSCA1.6
                                                    CmOSCA1.5                                                                                                                                 CeOSCA2.4
                                                                                              CiOSCA2.5                                             CmOSCA1.5                                 CiOSCA2.5
                                                    HaOSCA1.6                                                                                       HaOSCA1.6
                                                    AlOSCA1.3                                 CtOSCA3.1
                                                                                                                                                    AlOSCA1.3                                 CtOSCA3.1
                                                                                              AlOSCA3.1
                                                    HaOSCA1.5                                                                                       HaOSCA1.5                                 AlOSCA3.1
                                                                                              CeOSCA3.1




                                                                                   Group3
                                                    LsOSCA1.5                                                                                       LsOSCA1.5                                 CeOSCA3.1




                                                                                                                                                                                   Group3
                                                                                              CiOSCA3.1
                                                    CeOSCA1.4                                                                                                                                 CiOSCA3.1
                                                                                              LsOSCA3.1                                             CeOSCA1.4
                                                    CiOSCA1.6                                                                                                                                 LsOSCA3.1
                                                                                              HaOSCA3.1                                             CiOSCA1.6
                                                    CiOSCA1.5                                                                                                                                 HaOSCA3.1
                                                                                              CmOSCA3.4                                             CiOSCA1.5
                                                    CiOSCA1.7                                                                                                                                 CmOSCA3.4
                                                                                              CmOSCA3.1                                             CiOSCA1.7
                                                    AlOSCA1.10                                                                                                                                CmOSCA3.1
                                                                                              CmOSCA3.2                                             AlOSCA1.10
                                                    CmOSCA1.4                                                                                                                                 CmOSCA3.2
                                                                                              CmOSCA3.3                                             CmOSCA1.4
                                                    LsOSCA1.2                                                                                                                                 CmOSCA3.3
                                                                                              CeOSCA4.1                                             LsOSCA1.2
                                                    CeOSCA1.6                                                                                       CeOSCA1.6                                  CeOSCA4.1
                                                    CiOSCA1.8                                 LsOSCA4.1
                                                                                                                                                    CiOSCA1.8                                  LsOSCA4.1
                                                                                   Group4     LsOSCA4.3
                                                    CtOSCA1.5                                                                                                                                  LsOSCA4.3




                                                                                                                                                                                   Group4
                                                                                              LsOSCA4.2                                             CtOSCA1.5
                                                    CmOSCA1.8                                                                                       CmOSCA1.8                                  LsOSCA4.2
                                                                                              LsOSCA4.4
                                                    CmOSCA1.6                                                                                                                                  LsOSCA4.4
                                                                                              CeOSCA4.3                                             CmOSCA1.6
                                                    CmOSCA1.7                                                                                                                                  CeOSCA4.3
                                                                                              CmOSCA4.1                                             CmOSCA1.7                                  CmOSCA4.1
                                                    CtOSCA1.6                                 AlOSCA4.1                                             CtOSCA1.6
                                                    AlOSCA1.8                                                                                                                                  AlOSCA4.1
                                                                                              CeOSCA4.2                                             AlOSCA1.8                                  CeOSCA4.2
                                                                                              CiOSCA4.1
                                                                                                                                                                                               CiOSCA4.1




                                     Figure 6 Phylogenetic tree, gene structure, and conserved motif analysis of the OSCA gene family of
                                     Compositae. Different motifs are displayed in different colored boxes as indicated on the right side.
                                                                                                    Full-size DOI: 10.7717/peerj.15089/fig-6


                                   Analysis of cis-acting elements in the promoter of the sunflower OSCA
                                   gene
                                   Transcription factors (TFs) are proteins that can bind to the promoter regions of genes
                                   in a sequence-specific manner in order to regulate transcription, thereby regulating
                                   plant functions, including responses to environmental factors, growth, and development
                                   (Warren, 2002). Analysis of the 2,000 bp upstream sequence of the sunflower OSCA gene
                                   start codon showed that there were multiple stress and hormone response elements in
                                   the upstream sequence of the HaOSCA gene, with different types and numbers (Fig. 7).
                                   Three main categories of cis elements were found in the promoter sequences of HaOSCA
                                   genes. The first category was involved in phytohormones, such as abscisic acid (ABA),
                                   jasmonic acid (JA), auxin, gibberellins (GA), and salicylic acid (SA). The second category
                                   was associated with stresses, such as low-temperature responsiveness, defense, and stress
                                   responsiveness. The last category was mainly MYB binding sites. Importantly, all 14
                                   HaOSCA genes, except HaOSCA1.8, contained the JA-responsive element (TGACG-motif
                                   and CGTCA-motif), and the ABA responsive element (ABRE) was found in almost all gene
                                   promoters (Table S3). Interestingly, cis-acting elements were not found in the promoter
                                   region of HaOSCA1.8. These results showed that HaOSCA may affect hormone signal
                                   responsiveness and stress adaptation. No cytokinin-responsive elements were identified in
                                   the HaOSCA promoter regions.




Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                                                                                                                           13/26
                                                  HaOSCA1.5                                                                                                         ABA responsiveness cis-acting element
                                                  HaOSCA1.6                                                                                                         MeJA responsiveness cis-acting element
                                                  HaOSCA1.8                                                                                                         MYB binding site
                                                  HaOSCA1.7                                                                                                         SA responsiveness cis-acting element
                                        Group 1
                                                  HaOSCA1.4                                                                                                         auxin responsiveness cis-acting element
                                                  HaOSCA1.3                                                                                                         defense and stress responsiveness cis-acting element
                                                  HaOSCA1.2                                                                                                         GA responsiveness cis-acting element
                                                  HaOSCA1.1                                                                                                         low-temperature responsiveness cis-acting element
                                        Group 3   HaOSCA3.1
                                                  HaOSCA2.2
                                                  HaOSCA2.1
                                                  HaOSCA2.5
                                        Group 2   HaOSCA2.6
                                                  HaOSCA2.3
                                                  HaOSCA2.4
                                                          5'                                                                                                 3'
                                                           0    300                    600              900     1200   1500     1800                       2100




                                     Figure 7 Analysis of homeopathic elements in the promoters of the sunflower OSCA gene family.
                                                                                              Full-size DOI: 10.7717/peerj.15089/fig-7


                                    A                          HaOSCA1.3
                                                                                            3.00    B                                                               C
                                                                                                                              HaOSCA3.1                     3.00
                                                                                                                                                                                                  HaOSCA1.7                     1.20

                                                               HaOSCA1.5   log10 (FPKM+!)                                     HaOSCA2.3




                                                                                                                                          log10 (FPKM+!)
                                                                                                                                                                                                  HaOSCA1.1




                                                                                                                                                                                                              log10 (FPKM+!)
                                                               HaOSCA2.3                    0.00                              HaOSCA2.2                                                           HaOSCA1.5
                                                                                                                                                            0.00
                                                                                                                                                                                                                               0.00
                                                               HaOSCA2.4                                                      HaOSCA2.4                                                           HaOSCA2.5
                                                               HaOSCA2.1                                                      HaOSCA2.1                                                           HaOSCA2.1
                                                                                            -3.00
                                                               HaOSCA2.2                                                      HaOSCA2.5                     -3.00                                 HaOSCA2.3                    -1.20
                                                               HaOSCA1.8                                                      HaOSCA2.6                                                           HaOSCA2.4
                                                               HaOSCA2.5                                                      HaOSCA1.2                                                           HaOSCA1.3
                                                               HaOSCA1.4                                                      HaOSCA1.6                                                           HaOSCA1.8
                                                               HaOSCA1.7                                                      HaOSCA1.1                                                           HaOSCA1.2
                                                               HaOSCA1.6                                                      HaOSCA1.4                                                           HaOSCA3.1
                                                               HaOSCA3.1                                                      HaOSCA1.7                                                           HaOSCA2.2
                                                               HaOSCA1.2                                                      HaOSCA1.3                                                           HaOSCA2.6
                                                               HaOSCA1.1                                                      HaOSCA1.5                                                           HaOSCA1.4
                                                               HaOSCA2.6                                                      HaOSCA1.8                                                           HaOSCA1.6




                                                                                                                                                                                             h
                                          Br es




                                               en
                                         Po ry




                                                                                                                                                                               0h

                                                                                                                                                                                     3h
                                         Le em




                                        St le
                                        Co act
                                          O lla




                                                                                                           BA




                                                                                                                     A
                                          St t




                                                                                                                         SA
                                                                                                                     A
                                         Li en




                                                                                                           CK




                                                                                                                   JA
                                                                                                              BR




                                                                                                                                                                                           12
                                               o

                                            av




                                           gu
                                            va




                                                                                                                  IA
                                                                                                                   G
                                           Ro




                                          am
                                           ro


                                            ll




                                                                                                          A




                                     Figure 8 Expression analysis of the sunflower OSCA gene. (A) Heatmap of expression patterns in dif-
                                     ferent tissues. (B) Heatmap of expression patterns under different hormone treatments. (C) Heatmap of
                                     expression patterns under salt stress.
                                                                                                     Full-size DOI: 10.7717/peerj.15089/fig-8


                                   Expression analysis of the sunflower OSCA gene
                                   Gene expression patterns are usually closely related to gene functions. To gain insight
                                   into the expression patterns of sunflower OSCA genes, we first analyzed the expression
                                   patterns of 15 sunflower OSCA genes in nine tissues (Fig. 8A). The results showed that
                                   there were nine sunflower OSCAs (HaOSCA1.1, HaOSCA1.2, HaOSCA1.4, HaOSCA1.6,
                                   HaOSCA1.7, HaOSCA1.8, HaOSCA2.5, HaOSCA2.6, and HaOSCA3.1) in pollen and
                                   stamen. The expression was higher than in other tissues, and the remaining six had higher
                                   expression levels in root, stem, leaves, bract, corolla, ovary, and ligament, which indicated
                                   that sunflower OSCA had a wide range of tissue expression types.
                                      Plant hormones play an important role in the processes of growth, development, and
                                   stress. We analyzed the expression pattern of the sunflower OSCA gene induced by six
                                   hormones (ABA, BR, JA, GA, IAA, and SA) (Fig. 8B). Six genes (HaOSCA1.3, HaOSCA1.5,
                                   HaOSCA1.8, HaOSCA2.2, HaOSCA2.3, and HaOSCA2.4) were more strongly induced by
                                   ABA than other hormones, six genes (HaOSCA1.2, HaOSCA1.4, HaOSCA1.6, HaOSCA1.7,




Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                                                                                                                             14/26
                                                                          HaOSCA1.1                                                         HaOSCA1.2                                                            HaOSCA1.4                                                              HaOSCA1.5                                                                   HaOSCA1.6
                                                                                            **                                                           **                                                                                                                                                 **
                                                                                                                                                                                                                                                                                                                                          1.00
                                                                                                                              6                                                                 1.00
                                                         5                                                                                                                                                                                                           4
                                                                                                                                                                                                                                                                                                      **
                                                                                                                                                                                                                                                                                                                                                                                            **




                                                                                                                                                                                                                                                                                                                        Relative expression
                                                                                                                                                                                                                                                                                                                                          0.75




                                   Relative expression




                                                                                                        Relative expression




                                                                                                                                                                          Relative expression




                                                                                                                                                                                                                                               Relative expression
                                                         4                                                                                                                                      0.75
                                                                                                                                                                                                                                                                     3                                                                                                           **
                                                                                                                              4
                                                         3
                                                                                       **                                                                                                       0.50                                                                                                                                      0.50
                                                                                                                                                                                                                                                                     2
                                                                                                                                       **    *                                                                                                                                           *                                                                                            **
                                                         2                                        **
                                                                                                                              2
                                                                                                                                                                                                0.25                                                                                                                                      0.25
                                                                                                                                                                                                                                                                     1
                                                         1


                                                         0                                                                    0                                                                 0.00                                                                 0                                                                    0.00
                                                               0h    1h    3h          6h   12h   24h                             0h   1h    3h          6h   12h   24h                                0h   1h    3h          6h   12h   24h                                0h    1h     3h           6h    12h   24h                                     0h   1h    3h          6h   12h   24h
                                                                                Time                                                              Time                                                                 Time                                                                   Time                                                                        Time


                                                                          HaOSCA1.7                                                         HaOSCA2.2                                                            HaOSCA2.5                                                              HaOSCA2.6                                                                   HaOSCA3.1
                                                                                                                                                         **                                                                                                                                           **                                                                         **
                                                         1.5                                                                                                                                                                                                         12.5
                                                                                                                              4                                                                 1.25


                                                                                                                                                                                                                                                                     10.0                                                                            15
                                                                                                                                                                                                1.00




                                                                                                                                                                                                                                                                                                                               Relative expression
                                   Relative expression




                                                                                                        Relative expression




                                                                                                                                                                          Relative expression




                                                                                                                                                                                                                                               Relative expression
                                                                                                                              3                                                                                                                                                                                                                                                       **
                                                         1.0
                                                                                                                                                                                                                                                                      7.5
                                                                                                                                                                                                0.75
                                                                                                                                                                                                                                                                                         **                                                          10
                                                                                                                              2
                                                                                                                                             **
                                                                                                                                                                                                                                                                                                                                                                    **
                                                                                                                                                                                                0.50                                                                  5.0
                                                         0.5
                                                                                                                                                                                                                                                                                                                                                     5
                                                                                                                              1                                                                                                                                                                             **                                                 **
                                                                                                                                                                                                0.25                                                                  2.5
                                                                                                                                                                                                                                                                                  **                                                                                                         *

                                                         0.0                                                                  0                                                             0.00                                                                      0.0                                                                            0
                                                                0h   1h    3h          6h   12h   24h                             0h   1h    3h          6h   12h   24h                                0h   1h    3h          6h   12h   24h                                 0h    1h     3h           6h   12h   24h                                     0h   1h    3h          6h   12h   24h
                                                                                Time                                                              Time                                                                 Time                                                                    Time                                                                       Time




                                                         Figure 9 Expression analysis of the sunflower OSCA gene under NaCl stress. Error bars represent the
                                                         average of three replicates ± Sd. (* P < 0.05; ** P < 0.01). The housekeeping gene HaActin was used as the
                                                         internal reference gene.
                                                                                                                          Full-size DOI: 10.7717/peerj.15089/fig-9


                                   HaOSCA2.5, and HaOSCA2.6 ) were more strongly affected by IAA than other hormones,
                                   and HaOSCA1.1 was most strongly affected by JA.
                                      Next, we analyzed the expression pattern of the sunflower OSCA gene under salt
                                   stress. All sunflower OSCA gene expression levels changed after NaCl treatment (Fig. 8C).
                                   Seven OSCA genes (HaOSCA1.1, HaOSCA1.2, HaOSCA1.5, HaOSCA1.7, HaOSCA2.2,
                                   HaOSCA2.6, and HaOSCA3.1) were upregulated, three (HaOSCA1.4, HaOSCA1.6,
                                   and HaOSCA2.5) were significantly downregulated, and the expression levels of the
                                   remaining five (HaOSCA1.3, HaOSCA1.8, HaOSCA2.1, HaOSCA2.3, and HaOSCA2.4)
                                   also changed, but not significantly (Fig. 8C). These results indicated that the 10 OSCA
                                   genes (HaOSCA1.1, HaOSCA1.2, HaOSCA1.4, HaOSCA1.5, HaOSCA1.6, HaOSCA1.7,
                                   HaOSCA2.2, HaOSCA2.5, HaOSCA2.6, and HaOSCA3.1) may play a role in the sunflower’s
                                   response to salt stress.

                                   qRT−PCR of the sunflower OSCA gene under salt stress
                                   With the increase of soil salinization, salt stress has become the most important abiotic
                                   stress faced by the sunflowers. Based on the previous expression analysis, we found that
                                   10 genes (HaOSCA1.1, HaOSCA1.2, HaOSCA1.4, HaOSCA1.5, HaOSCA1.6, HaOSCA1.7,
                                   HaOSCA2.2, HaOSCA2.5, HaOSCA2.6, and HaOSCA3. 1) may be involved in the response
                                   of sunflower to salt stress. qRT −PCR was used to study the expression patterns of these 10
                                   genes under NaCl stress. Compared with levels before stress (0 h), the expression of seven
                                   genes (HaOSCA1.1, HaOSCA1.2, HaOSCA1.5, HaOSCA1.6, HaOSCA2.2, HaOSCA2.6,
                                   and HaOSCA3.1) was significantly changed at different points in time during treatment
                                   (Fig. 9). HaOSCA1.6 was significantly downregulated and the remaining six genes were
                                   significantly upregulated. The expression levels of HaOSCA2.6 and HaOSCA3.1 reached
                                   more than a 10-fold change at 6 h of NaCl stress. These results suggest that HaOSCA2.6
                                   and HaOSCA3.1 may play an important role in the response of sunflower to salt stress.




Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                                                                                                                                                                                                                                                                                          15/26
                                   Protein interaction of sunflower OSCA gene
                                   Genes typically perform their biological functions and signal transduction pathways
                                   through interacting networks, so studying the underlying interaction networks associated
                                   with gene families can provide a better understanding of their functions. To elucidate the
                                   role of OSCA genes in salt stress in the sunflower, we used WGCNA to analyze OSCA
                                   genes (HaOSCA1.1, HaOSCA1.2, HaOSCA1.5, HaOSCA1.6, HaOSCA2.2, HaOSCA2.6,
                                   and HaOSCA3.1) and the salt coexpression network of all differentially expressed genes
                                   under stress. Genes were clustered using dynamic shearing and divided into modules. By
                                   calculating the eigenvectors of each module and merging similar modules, a total of seven
                                   gene coexpression modules were obtained (Fig. 10A). In this study, OSCA genes in each
                                   module were selected as core genes, and gene interaction network diagrams were drawn
                                   using core genes and their interacting genes (Fig. 10B and Table S4). To further uncover
                                   the function of the network, we performed an enrichment analysis of all interacting genes
                                   (Figs. 10C and 10D). The GO enrichment results showed that the biological processes
                                   involved were mainly cellular component organization or biogenesis, biological regulation,
                                   multicellular organismal process, response to stimulus and cellular process, cellular
                                   components are extracellular regions, cells and extracellular regions, molecular functions
                                   are transporter activities, antioxidant activities, transcription regulator activities, and
                                   molecular carrier activity (Fig. 10C). The KEGG pathway was mainly alpha-linolenic acid
                                   metabolism, glycerolipid metabolism, peroxisome, and tryptophan metabolism (Fig. 10D).
                                   This network further demonstrated the complex functions and potential roles of the OSCA
                                   gene family in sunflower salt-stressed species. The results of this study lay a foundation
                                   for further research on the functions and molecular mechanisms of these genes in the
                                   sunflower under salt stress and provide a reference for further study of the sunflower
                                   OSCA gene family.

                                   DISCUSSION
                                   Over their long evolutionary history, all living plants are thought to have undergone at least
                                   one or more whole genome duplication (WGD) events, which provide opportunities for
                                   repeated genes to acquire functional diversification, leading to more complex organisms.
                                   In this process of differentiation, the gene family produces more members (Zhang et al.,
                                   2018; Swarbreck, Colaço & Davies, 2013). Plant biologists have always been fascinated by
                                   the structure, function, and evolution of genes, and the interactions and adaptations
                                   between the environment and plants have been well studied (Gao et al., 2021; Yuan et
                                   al., 2014). With the continuous publication of plant genomes, the structure, function,
                                   and evolution of various gene families have been extensively studied in plants, and these
                                   results can provide more insight into the origin, diversity, and biological function of these
                                   gene families (Kiyosue, Yamaguchi-Shinozaki & Shinozaki, 1994; Glasauer & Neuhauss,
                                   2014; Li et al., 2015; Tong et al., 2021; Miao et al., 2022). Asteraceae is made up of many
                                   different species, each with a rich morphological type that exhibits extreme characteristics
                                   (Badouin et al., 2017). The evolution of the cultivated sunflower progressed in two phases
                                   (domestication by native North Americans, followed by breeding according to traits related



Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                         16/26
                                    A                                                                                                                                             Cluster Dendrogram
                                                                                                                                                                                                                                                                                                                                                                          C                            transporter activity




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molecular function
                                                                                                                                                                                                                                                                                                                                                                                                       antioxidant activity




                                                                  0.8
                                                                                                                                                                                                                                                                                                                                                                                          transcription regulator activity


                                                                                                                                                                                                                                                                                                                                                                                                molecular carrier activity




                                                                  0.6
                                                    Height




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                cellular component
                                                                                                                                                                                                                                                                                                                                                                                                       extracellular region




                                                                                                                                                                                                                                                                                                                                                                       GO Terms
                                                                  0.4
                                                                                                                                                                                                                                                                                                                                                                                                                         cell


                                                                                                                                                                                                                                                                                                                                                                                             protein−containing complex




                                                                  0.2
                                                                                                                                                                                                                                                                                                                                                                                                           cellular process




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                biological process
                                                                                                                                                                                                                                                                                                                                                                                                      response to stimulus
                                              Module colors
                                                                                                                                                                                                                                                                                                                                                                                       multicellular organismal process


                                    B
                                                                                                         HannXRQ_Chr06g0181281
                                                                                                    HannXRQ_Chr07g0193771
                                                                                                              HannXRQ_Chr07g0202811
                                                                                              HannXRQ_Chr17g0534241 HannXRQ_Chr02g0051531


                                                                                                                                                                                                                                                                                                                                                                                                     biological regulation
                                                                                        HannXRQ_Chr03g0083361             HannXRQ_Chr05g0148381
                                                                                   HannXRQ_Chr07g0202951                       HannXRQ_Chr13g0419911
                                                                              HannXRQ_Chr13g0413121                                 HannXRQ_Chr17g0533311
                                                                         HannXRQ_Chr16g0511251                                           HannXRQ_Chr06g0172081
                                                                    HannXRQ_Chr08g0229171                                                     HannXRQ_Chr05g0146781
                                                                HannXRQ_Chr08g0225761                                                                  HannXRQ_Chr14g0447911
                                                         HannXRQ_Chr14g0445091                                                                             HannXRQ_Chr15g0479051                                                                                                  HannXRQ_Chr02g0043391
                                                                                                                                                                                                                                                                                       HannXRQ_Chr04g0124441
                                                                                                                                                                                                                                                                            HannXRQ_Chr04g0109581
                                                                                                                                                                                                                                                                      HannXRQ_Chr02g0031681 HannXRQ_Chr04g0109901
                                                                                                                                                                                                                                                                                                  HannXRQ_Chr03g0069531
                                                                                                                                                                                                                                                                 HannXRQ_Chr02g0035051
                                                     HannXRQ_Chr10g0278641                                                                                       HannXRQ_Chr04g0124761                                                                                                                  HannXRQ_Chr03g0070121

                                                                                                                                                                                                                                                                                                                                                                     cellular component organization or biogenesis
                                                                                                                                                                                                                                                            HannXRQ_Chr02g0059361
                                                 HannXRQ_Chr16g0499831                                                                                               HannXRQ_Chr17g0561461                                                             HannXRQ_Chr04g0113111

                                                                                                          HannXRQ_Chr04g0106651                                                                                                                   HannXRQ_Chr04g0100931
                                              HannXRQ_Chr16g0526021                              HannXRQ_Chr10g0309151
                                                                                                                 HannXRQ_Chr15g0478161                                   HannXRQ_Chr17g0567321
                                                                                          HannXRQ_Chr10g0297861           HannXRQ_Chr08g0226271                                                                                              HannXRQ_Chr03g0067611
                                          HannXRQ_Chr12g0373721                   HannXRQ_Chr15g0480661                                                                     HannXRQ_Chr04g0125911                                      HannXRQ_Chr03g0079641
                                                                                                                                      HannXRQ_Chr04g0106661


                                                                                                                                                                                                                                                                                                                                                                                                                                0             10           20      30
                                        HannXRQ_Chr16g0508761                                                                                                                   HannXRQ_Chr10g0291201                              HannXRQ_Chr04g0095361
                                                                           HannXRQ_Chr02g0047911                                              HannXRQ_Chr09g0261971
                                                                                                                                                                                                                                                                                                                                      HannXRQ_Chr02g0035461
                                                                                                                                                                                  HannXRQ_Chr16g0508701                        HannXRQ_Chr03g0061481


                                                                                                                                                                                                                                                                                                                                                                                                                                                     Count
                                                                      HannXRQ_Chr14g0428141                                                                                                                                                                                        HannXRQ_Chr04g0104381
                                                                                                                                                                                                                                                                            HannXRQ_Chr01g0028271
                                                                                                                                                                                                                                                                                            HannXRQ_Chr02g0033761                        HannXRQ_Chr03g0088531
                                                                                                                                                      HannXRQ_Chr09g0271221                                                 HannXRQ_Chr01g0006341
                                                                                                                                                                                      HannXRQ_Chr04g0115711
                                                                                                                                                                                                                                                                    HannXRQ_Chr03g0088911           HannXRQ_Chr03g0083791
                                                                HannXRQ_Chr16g0523701                                                                                                                                                                                                                                                        HannXRQ_Chr02g0038211
                                                                                                                                                                                                                          HannXRQ_Chr03g0088251
                                                                                                                                                                                        HannXRQ_Chr08g0222491                                               HannXRQ_Chr01g0027951                         HannXRQ_Chr01g0011251
                                                                                                                                                                                                                                                                                                                                               HannXRQ_Chr03g0083221
                                                                                                                                                          HannXRQ_Chr09g0267551                                         HannXRQ_Chr01g0002521
                                                           HannXRQ_Chr13g0417551                                                                                                         HannXRQ_Chr11g0325961
                                                                                                                                                                                                                                                       HannXRQ_Chr01g0022311                                   HannXRQ_Chr01g0014711            HannXRQ_Chr03g0071191
                                                                                                                                                                                                                      HannXRQ_Chr04g0121041
                                                                                                                                                                                          HannXRQ_Chr12g0362911
                                                         HannXRQ_Chr13g0393171                                                                                                                                                                                                                                                                   HannXRQ_Chr01g0005461
                                                                                                                                                                                                                     HannXRQ_Chr03g0063271         HannXRQ_Chr02g0056101                                            HannXRQ_Chr01g0011241
                                                                                                                                                              HannXRQ_Chr09g0250051        HannXRQ_Chr12g0354261
                                                                                                                                                                                                                                                                                                                                                  HannXRQ_Chr01g0000331
                                                        HannXRQ_Chr14g0437791
                                                                                     HaOSCA3.1                                        HaOSCA1.2                                            HannXRQ_Chr14g0442901
                                                                                                                                                                                                                    HannXRQ_Chr04g0094401
                                                                                                                                                                                                                                                                     HaOSCA2.6                   HaOSCA2.2
                                                                                                                                                                                                                                                                                                                                                  HannXRQ_Chr03g0077201
                                                                                                                                                                                                                    HannXRQ_Chr02g0032371
                                                                                                                                                              HannXRQ_Chr01g0009771        HannXRQ_Chr10g0285181
                                                         HannXRQ_Chr09g0274181                                                                                                                                                                                                                                                                    HannXRQ_Chr03g0075321
                                                                                                                                                                                                                   HannXRQ_Chr00c1257g0578881      HannXRQ_Chr03g0084051                                            HannXRQ_Chr03g0085251
                                                                                                                                                                                          HannXRQ_Chr10g0312771
                                                                                                                                                                                                                                                                                                                                                 HannXRQ_Chr01g0005051
                                                                                                                                                                                                                      HannXRQ_Chr03g0088661
                                                                                                                                                              HannXRQ_Chr10g0301571
                                                           HannXRQ_Chr03g0073471                                                                                                      HannXRQ_Chr00c0537g0575611                                       HannXRQ_Chr01g0016891                                   HannXRQ_Chr03g0071771
                                                                                                                                                                                                                                                                                                                                                HannXRQ_Chr02g0035071
                                                                                                                                                                                                                       HannXRQ_Chr04g0119381
                                                                                                                                                                                        HannXRQ_Chr14g0459241
                                                                HannXRQ_Chr01g0011101                                                                 HannXRQ_Chr12g0360571                                                                                 HannXRQ_Chr04g0094711                         HannXRQ_Chr01g0009091               HannXRQ_Chr01g0014541
                                                                                                                                                                                                                         HannXRQ_Chr03g0091801
                                                                                                                                                                                      HannXRQ_Chr02g0054171
                                                                                                                                                                                                                                                                HannXRQ_Chr00c0439g0574731          HannXRQ_Chr03g0086761                   HannXRQ_Chr02g0045481
                                                                                                                                                                                                                            HannXRQ_Chr04g0104511




                                                                                                                                                                                                                                                                                                                                                                          D
                                                                      HannXRQ_Chr16g0503511                                                      HannXRQ_Chr13g0411971
                                                                                                                                                                                  HannXRQ_Chr10g0278631                                                                     HannXRQ_Chr04g0094721
                                                                                                                                                                                                                                                                                            HannXRQ_Chr02g0052061
                                                                                                                                                                                                                                                                                   HannXRQ_Chr01g0000291                               HannXRQ_Chr04g0121761
                                                                                                                                                                                                                               HannXRQ_Chr02g0045141
                                                                           HannXRQ_Chr15g0464351                                           HannXRQ_Chr03g0090431                HannXRQ_Chr06g0171681
                                                                                                                                                                                                                                                                                                                                   HannXRQ_Chr04g0105641
                                                                                                                                                                                                                                  HannXRQ_Chr04g0109791
                                          HannXRQ_Chr17g0562251                   HannXRQ_Chr07g0189521                           HannXRQ_Chr13g0412901                     HannXRQ_Chr17g0533951
                                                                                                                                                                                                                                      HannXRQ_Chr03g0067571
                                                                                          HannXRQ_Chr07g0202021           HannXRQ_Chr15g0490541
                                              HannXRQ_Chr09g0276181                              HannXRQ_Chr17g0563461
                                                                                                                 HannXRQ_Chr10g0283891                                   HannXRQ_Chr03g0072171                                              HannXRQ_Chr04g0114331
                                                                                                          HannXRQ_Chr04g0099961
                                                 HannXRQ_Chr06g0176281                                                                                               HannXRQ_Chr16g0511421                                                      HannXRQ_Chr02g0053471
                                                                                                                                                                                                                                                     HannXRQ_Chr02g0045721
                                                     HannXRQ_Chr01g0029901                                                                                            XLOC_037753
                                                                                                                                                                                                                                                          HannXRQ_Chr02g0055151
                                                                                                                                                                                                                                                               HannXRQ_Chr01g0028681
                                                                                                                                                                                                                                                                                                                                                                                  30
                                                         HannXRQ_Chr08g0223221                                                                             HannXRQ_Chr10g0305371
                                                                                                                                                                                                                                                                                                HannXRQ_Chr01g0002691
                                                                                                                                                                                                                                                                    HannXRQ_Chr01g0017231 HannXRQ_Chr04g0095211
                                                                                                                                                                                                                                                                          HannXRQ_Chr02g0041301
                                                                                                                                                                                                                                                                                     HannXRQ_Chr04g0104881
                                                                                                                                                                                                                                                                                HannXRQ_Chr01g0026181
                                                                HannXRQ_Chr15g0489731                                                                  HannXRQ_Chr05g0134361
                                                                    HannXRQ_Chr11g0340291                                                     HannXRQ_Chr09g0271701
                                                                         HannXRQ_Chr13g0399131                                           HannXRQ_Chr15g0465581
                                                                              HannXRQ_Chr16g0523561                                 HannXRQ_Chr06g0175771
                                                                                   HannXRQ_Chr03g0089621                       HannXRQ_Chr13g0417671
                                                                                        HannXRQ_Chr17g0563151             HannXRQ_Chr08g0221861
                                                                                              HannXRQ_Chr05g0129481 HannXRQ_Chr02g0034981
                                                                                                    HannXRQ_Chr06g0183991
                                                                                                              HannXRQ_Chr10g0302761
                                                                                                         HannXRQ_Chr09g0256841




                                                                                                       HannXRQ_Chr01g0017041
                                                                                                 HannXRQ_Chr01g0000841
                                                                                                            HannXRQ_Chr01g0000431

                                                                                                                                                                                                                                                                                                                                                                                  20
                                                                                           HannXRQ_Chr01g0010081 HannXRQ_Chr01g0002531
                                                                                      HannXRQ_Chr01g0008131            HannXRQ_Chr01g0014191
                                                                                 HannXRQ_Chr01g0007561                       HannXRQ_Chr01g0001591




                                                                                                                                                                                                                                                                                                                                                                          Count
                                                                                                                                  HannXRQ_Chr01g0016471
                                                                                                                                        HannXRQ_Chr01g0021311

                                                                                                                                             HannXRQ_Chr01g0000201

                                                                                                     HannXRQ_Chr01g0020731
                                                                                                              HannXRQ_Chr01g0002161             HannXRQ_Chr01g0021831
                                                                                              HannXRQ_Chr01g0006381
                                                                                                                     HannXRQ_Chr01g0014221
                                                                                    HannXRQ_Chr01g0005821                                           HannXRQ_Chr01g0021351                                                                                                           HannXRQ_Chr17g0569031
                                                                                                                                                                                                                                                                               HannXRQ_Chr09g0257601
                                                                                                                                                                                                                                                                                           HannXRQ_Chr01g0001721
                                                                                                                                                                                                                                                                          HannXRQ_Chr12g0378831 HannXRQ_Chr09g0266631
                                                                                                                              HannXRQ_Chr01g0015111     HannXRQ_Chr01g0018011                                                                                        HannXRQ_Chr09g0276831           HannXRQ_Chr04g0111011
                                                                              HannXRQ_Chr01g0011481
                                                                                                                                                                                                                                                              HannXRQ_Chr06g0179231                      HannXRQ_Chr17g0558561
                                                                                                                                                         HannXRQ_Chr01g0005281
                                                                                                                                      HannXRQ_Chr01g0006591
                                                                         HannXRQ_Chr01g0005541
                                                                                                                                                              HannXRQ_Chr01g0014831
                                                                                                                                                                                                                                                          HannXRQ_Chr14g0437471                              HannXRQ_Chr03g0079661

                                                                                                                                                                                                                                                                                                                HannXRQ_Chr02g0045131
                                                                                                                                                                                                                                                                                                                                                                                  10
                                                                                                                                         HannXRQ_Chr01g0001311
                                                                    HannXRQ_Chr01g0007691
                                                                                                                                                            HannXRQ_Chr01g0018981                                                                                                                                   HannXRQ_Chr06g0165991


                                                                                                                                                                 HannXRQ_Chr01g0012131                                                                                                                                HannXRQ_Chr10g0281311

                                                                                          HaOSCA1.1
                                                                  HannXRQ_Chr01g0009211
                                                                                                                                            HannXRQ_Chr01g0021711
                                                                                                                         HaOSCA1.5                                                                                                                                                                                     HannXRQ_Chr17g0568051
                                                                                                                                                                                                                                                                                      HaOSCA1.6
                                                                                                                                                                 HannXRQ_Chr01g0005471

                                                                  HannXRQ_Chr01g0010261
                                                                                                                                                                 HannXRQ_Chr01g0006731                                                                                                                                 HannXRQ_Chr08g0225081
                                                                                                                                           HannXRQ_Chr01g0018901


                                                                                                                                                                                                                                                                                                                                                                                   0
                                                                                                                                                                HannXRQ_Chr01g0013241                                                                                                                                 HannXRQ_Chr02g0039561
                                                                    HannXRQ_Chr01g0016591                                                                                                                                                         HannXRQ_Chr03g0062641



                                                                      HannXRQ_Chr00c0011g0571061
                                                                                                                                                            HannXRQ_Chr01g0014871
                                                                                                                                        HannXRQ_Chr01g0008191
                                                                                                                                                                                                                                                    HannXRQ_Chr09g0276481
                                                                                                                                                                                                                                                                                                                     HannXRQ_Chr05g0153701
                                                                                                                                                                                                                                                                                                                                                                                       alpha-Linolenic acid metabolism   Glycerolipid metabolism      Peroxisome        Tryptophan metabolism
                                                                                                                                                                                                                                                                                                                                                                                                                                      KEGG Pathway Terms
                                                                                                                                                                                                                                                                                                                 HannXRQ_Chr09g0265751
                                                                                                                                                          HannXRQ_Chr01g0002451                                                                        HannXRQ_Chr09g0276471
                                                                           HannXRQ_Chr00c0028g0571141                                                                                                                                                                                                         HannXRQ_Chr12g0356701
                                                                                                                                HannXRQ_Chr01g0015921HannXRQ_Chr01g0003111                                                                                 HannXRQ_Chr01g0007581
                                                                                                                                                                                                                                                                                                          HannXRQ_Chr05g0137601
                                                                                    HannXRQ_Chr01g0002851                                                                                                                                                      HannXRQ_Chr15g0478871
                                                                                                                        HannXRQ_Chr01g0011581       HannXRQ_Chr01g0015931                                                                                                                            HannXRQ_Chr10g0282161
                                                                                                                                                                                                                                                                     HannXRQ_Chr16g0511181
                                                                                              HannXRQ_Chr01g0003941                                                                                                                                                                             HannXRQ_Chr10g0312831
                                                                                                              HannXRQ_Chr01g0003611
                                                                                                     HannXRQ_Chr01g0011401                      HannXRQ_Chr01g0000761                                                                                                     HannXRQ_Chr09g0252091
                                                                                                                                                                                                                                                                                           HannXRQ_Chr10g0300691
                                                                                                                                                                                                                                                                               HannXRQ_Chr13g0392811
                                                                                                                                                                                                                                                                                     HannXRQ_Chr15g0471451
                                                                  HannXRQ_Chr01g0021611                                                      HannXRQ_Chr01g0007021

                                                                       HannXRQ_Chr01g0015911                                            HannXRQ_Chr01g0017811
                                                                            HannXRQ_Chr01g0021361                                 HannXRQ_Chr01g0019621
                                                                                 HannXRQ_Chr01g0001231                       HannXRQ_Chr01g0005981
                                                                                      HannXRQ_Chr01g0005271            HannXRQ_Chr01g0003341
                                                                                           HannXRQ_Chr01g0003931 HannXRQ_Chr01g0006941
                                                                                                 HannXRQ_Chr01g0004301
                                                                                                            HannXRQ_Chr01g0003001
                                                                                                       HannXRQ_Chr01g0002881




                                     Figure 10 (A) Module partition of WGCNA clustering. (B) Sunflower OSCA coexpression network.
                                     (C) GO enrichment analysis results of coexpression genes. (D) KEGG pathway enrichment analysis re-
                                     sults of coexpression genes.
                                                                                                Full-size DOI: 10.7717/peerj.15089/fig-10


                                   to modern agricultural production) and have two complex WGD histories that provide
                                   an excellent opportunity to study the relationship between gene family isolation and plant
                                   morphological changes (Badouin et al., 2017). In a breakthrough study in 2014, the first
                                   hypertonic-induced Ca2+ conductive cation channel obtained from plants was discovered,
                                   which was designated to reduce hypertonic-induced [Ca2+ ] increase1 (OSCA1) (Yuan
                                   et al., 2014). OSCA1 mutants exhibited impaired osmotic Ca2+ signaling in guard cells
                                   and root cells, as well as weakened water transport regulation and root growth response
                                   under osmotic stress conditions (Yuan et al., 2014). This work advanced the study of OSCA
                                   genes, leading to the identification of more OSCA gene families (Yuan et al., 2014). The
                                   15 sunflower OSCA genes obtained in this study were close to the number of OSCA gene
                                   families in other crops, but much fewer than in soybeans and cotton, which may be related
                                   to the size of the soybean and cotton genomes and the large number of replications within
                                   their OSCA family members. The cell membrane (the dividing line between the internal
                                   and external environment of the cell) is the first to feel the stress stimulus, and OSCA is
                                   a calcium channel with multiple transmembrane domains, which is consistent with the
                                   subcellular structure predictions in this study (Table 1). This may be because when plants
                                   encounter adversity, genes in cells will regulate multiple organs to, through the synthesis




Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                                                                                                                                                                                                                                                                                                                                                                                                 17/26
                                   of organic matter, generate energy and jointly resist adversity and stress, which needs to be
                                   further explored (Yin et al., 2021; Miao et al., 2022).
                                      In Arabidopsis thaliana, two tandem repeat events occurred in the OSCA family (Kiyosue,
                                   Yamaguchi-Shinozaki & Shinozaki, 1994). Moreover, tandem duplications of the OSCA
                                   gene family have been detected in rice, litchi, wheat, and soybean species (Li et al., 2015;
                                   Tong et al., 2021; Yin et al., 2021; Miao et al., 2022). In this study, an in-depth evolutionary
                                   analysis of the sunflower OSCA gene family was performed using the OSCA genes of 13
                                   species (Figs. 2–6). The HaOSCA evolutionary tree was subdivided into three subfamilies,
                                   which was inconsistent with the OSCA family member evolutionary tree subfamily division
                                   of rice, soybean, corn, and other plants (Li et al., 2015; Tong et al., 2021; Ding et al., 2019;
                                   Wang et al., 2019). HaOSCA has the closest evolutionary tree clades and the largest number
                                   of collinear gene pairs to Arabidopsis thaliana and soybean, suggesting that the research basis
                                   of Arabidopsis thaliana and soybean OSCA genes can be used to expand our understanding
                                   of sunflower OSCA genes (Li et al., 2015; Tong et al., 2021; Ding et al., 2019; Wang et al.,
                                   2019). Three pairs of tandem duplication genes were found in the sunflower OSCA
                                   gene family, which indicated that the expansion and evolution of the sunflower OSCA
                                   gene family might be caused by tandem duplication. According to the Ka/Ks analysis,
                                   the strong purifying selection signal also indicated the functional importance of the
                                   sunflower OSCA gene. We also hypothesized that this may be because nonsynonymous
                                   substitutions generally bring harmful traits and rarely result in an evolutionary advantage
                                   (Swarbreck, Colaço & Davies, 2013; Miao et al., 2022). The six Asteraceae species contained
                                   four subgroups, and only three of these subgroups (1, 2, and 3) were included in the
                                   sunflower. Previous studies in tomatoes found that tomato OSCA family members were
                                   divided into five subfamilies, which indicates that the number of genetic family evolutionary
                                   subfamilies may be greatly related to crop growth habits (Wang et al., 2019). We found that
                                   sunflower OSCA had more collinearity with other Asteraceae plants and less collinearity
                                   with Carthamus tinctorius, indicating that the OSCA gene family was conserved during the
                                   evolution of Asteraceae. Sunflower and Lactuca sativa var. Angustata had the most colinear
                                   gene pairs, and the evolutionary tree was also closer to Lactuca sativa var. Angustata OSCA,
                                   suggesting that sunflower may have the same biological function as Lactuca sativa var.
                                   Angustata OSCA. Combined with the evolutionary tree, the number of CDS coding regions
                                   of family members from the same subfamily was similar, but the number of different
                                   subfamilies varied greatly, and it is speculated that the functions performed by subfamilies
                                   may be different.
                                      The functions of multiple OSCA genes involved in regulating plant growth, development,
                                   and various stress responses have been verified, and the roles played by different tissues
                                   and growth stages are different (Zhang et al., 2018; Swarbreck, Colaço & Davies, 2013; Gao
                                   et al., 2021; Kiyosue, Yamaguchi-Shinozaki & Shinozaki, 1994; Yin et al., 2021; Miao et al.,
                                   2022). In this study, cis-acting elements in the promoter region of the sunflower OSCA
                                   gene were analyzed, and we found that cis-acting elements in the binding sites of folic ABA
                                   and JA-bound cis-acting elements were the most abundant. Through expression analysis,
                                   we also found that more HaOSCA genes were induced by ABA and JA (Fig. 8B). A growing
                                   number of studies have found that ABA is the most important hormone for plant abiotic



Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                           18/26
                                   stress, and JA also plays an important role in this process (Wang et al., 2020; Baldoni, Genga
                                   & Cominelli, 2015). ABA has been found to activate the phosphorylation membrane of
                                   SnRKs bound to NADPH oxidase RBOHF, increasing the production of H2 O2 in apoplasts
                                   (Umezawa et al., 2009). Salt-induced ABA and Ca2+ signaling activates RBOHF activity
                                   through SnRK2.6 and CIPK11/26 signaling modules, while ABI1 is inhibitory. ABA, ROS,
                                   and Ca2+ exhibit complex signal crosstalk to control plant responses to salt stress (Quan et
                                   al., 2007). JA levels are elevated and JA signaling is activated under salt stress (Chen et al.,
                                   2016). The F-box protein COI1, also known as the JA receptor, forms complexes with SKP1
                                   and CULLIN1 to mediate JAZ degradation (Valenzuela et al., 2016). When JAZ is removed,
                                   inhibited transcription factors such as MYC activate the expression of JA response genes.
                                   Activation of JA signaling under salt stress eventually leads to inhibition of primary root
                                   growth. Exogenous JA can mitigate salt toxicity by maintaining ROS or ionic homeostasis
                                   (Valenzuela et al., 2016). These combined results hint at the complexity and importance of
                                   the sunflower OSCA gene in the coordination of growth and adversity.
                                       The yield and quality of the sunflower are susceptible to various biotic and abiotic stresses
                                   (Dar et al., 2021; Gogna & Bhatla, 2019). Abiotic stresses such as salinity and temperature
                                   often have a greater impact on plants (Gong et al., 2020; Verma, Ravindran & Kumar, 2016).
                                   Although sunflowers are not halophytes, they have a strong ability to tolerate salt and alkali
                                   (Keeley, Cantley & Gallaher, 2021; Rele & Mohile, 2003). This candidate gene for mining salt
                                   tolerance-related genes is a good research model. The soybean OSCA gene family generally
                                   responds to abiotic stress (saline-alkali), and nine OSCA genes were also upregulated
                                   or downregulated in rice abiotic stress treatments (Li et al., 2017). In the sunflower, we
                                   found that the expression levels of HaOSCA1.1, HaOSCA1.2, HaOSCA1.5, HaOSCA1.6,
                                   HaOSCA2.2, HaOSCA2.6, and HaOSCA3.1 all changed significantly at different time points
                                   during NaCl treatment. Of these, only HaOSCA1.6 was significantly downregulated (Fig.
                                   9). The expression levels of HaOSCA2.6 and HaOSCA3.1 reached more than a 10-fold
                                   change at 6 h of NaCl stress. These results suggest that HaOSCA2.6 and HaOSCA3.1 may
                                   be the most important in the sunflower’s response to salt stress.
                                       Studies on other plants have shown that most processes related to plant growth,
                                   development, and physiology are regulated by networks of protein−protein interactions
                                   (Yuan et al., 2014; Zhang et al., 2020; Liu, Wang & Sun, 2018). Building interaction
                                   networks between proteins is important for understanding how proteins work in
                                   biological systems. It is of great significance to understand the growth and development
                                   of plants, biological signals, and response mechanism of energy metabolism in some
                                   specific physiological states, as well as to understand the functional connections between
                                   proteins. We used WGCNA to analyze the coexpression network of sunflower OSCA genes
                                   and differentially expressed genes under salt stress (Fig. 10). Using the KEGG pathway
                                   enrichment analysis of the interacting genes, we found that the main enrichments were
                                   in the alpha-linolenic acid metabolism, glycerolipid metabolism, and peroxisome and
                                   tryptophan metabolism pathways (Fig. 10D). In Arabidopsis thaliana, alpha-linolenic acid
                                   metabolism has been found to be important in synthesizing JA (Valenzuela et al., 2016).
                                   AtLOX3 is involved in the process of Arabidopsis thaliana salt stress (Kilaru et al., 2011).
                                   Constitutive overexpression of AOC in wheat led to elevated JA levels and also confirmed JA



Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                            19/26
                                   involvement in salt stress response (Kilaru et al., 2011). The function of JAZ congeners in
                                   salt stress response has been demonstrated in many plant species (Valenzuela et al., 2016).
                                   In addition, the bHLH factor RICE SALT SENSITIVE3 (RSS3)/OsbHLH094 has been found
                                   to interact with JAZ to regulate salt tolerance (Toda et al., 2013). In addition, overexpression
                                   of OsbHLH148 in rice mutants induced high expression of OsDREB and OsJAZ under
                                   drought stress (Seo et al., 2011). Similarly, overexpression of OsJAZ9 significantly improved
                                   the salinity and drought tolerance of rice (Seo et al., 2011). However, whether OSCA relies
                                   on the JA pathway to improve the salinity tolerance of plants has not been reported, but
                                   provides a reference for our future research. In conclusion, the expression analysis of
                                   sunflower OSCA genes under salt stress and the construction of a coexpression network
                                   will provide clues to further study the salt tolerance of sunflower.

                                   CONCLUSION
                                   In this study, a systematic evolutionary analysis of sunflower OSCA genes was performed
                                   using 13 plant OSCA genes, and the sunflower OSCA gene family was found to be conserved
                                   in the evolution of Compositae. The analysis of the expression patterns of six hormones
                                   and salt stress in nine tissues showed that the OSCA gene played an important role in
                                   regulating the response of sunflower to salt stress, and HaOSCA2.6 and HaOSCA3.1 were
                                   the most important in the sunflower’s response to salt stress. The coexpression network
                                   of the sunflower OSCA gene under salt stress was also constructed based on WGCNA. In
                                   this study, the systematic evolution and expression analysis of the sunflower OSCA gene
                                   family was carried out for the first time, and provided clues for further research on the role
                                   of sunflower OSCA genes in salt-tolerant species.


                                    ADDITIONAL INFORMATION AND DECLARATIONS

                                   Funding
                                   This research was supported by grants from the Plant Variety Protection Foundation of
                                   the Ministry of Agriculture and Rural Affairs (2130135DUS202104). The funders had no
                                   role in study design, data collection and analysis, decision to publish, or preparation of the
                                   manuscript.

                                   Grant Disclosures
                                   The following grant information was disclosed by the authors:
                                   Plant Variety Protection Foundation of the Ministry of Agriculture and Rural Affairs:
                                   2130135DUS202104.

                                   Competing Interests
                                   The authors declare there are no competing interests.

                                   Author Contributions
                                   • Feibiao Shan conceived and designed the experiments, performed the experiments,
                                     analyzed the data, prepared figures and/or tables, authored or reviewed drafts of the
                                     article, and approved the final draft.



Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                           20/26
                                   • Yue Wu performed the experiments, analyzed the data, prepared figures and/or tables,
                                     and approved the final draft.
                                   • Ruixia Du performed the experiments, analyzed the data, prepared figures and/or tables,
                                     and approved the final draft.
                                   • Qinfang Yang performed the experiments, authored or reviewed drafts of the article,
                                     and approved the final draft.
                                   • Chunhui Liu performed the experiments, prepared figures and/or tables, and approved
                                     the final draft.
                                   • Yongxing Wang conceived and designed the experiments, performed the experiments,
                                     authored or reviewed drafts of the article, and approved the final draft.
                                   • Chun Zhang conceived and designed the experiments, authored or reviewed drafts of
                                     the article, and approved the final draft.
                                   • Yang Chen conceived and designed the experiments, performed the experiments,
                                     analyzed the data, prepared figures and/or tables, and approved the final draft.

                                   Data Availability
                                   The following information was supplied regarding data availability:
                                     The qRT-PCR raw data is available in the Supplemental File.

                                   Supplemental Information
                                   Supplemental information for this article can be found online at http://dx.doi.org/10.7717/
                                   peerj.15089#supplemental-information.


                                   REFERENCES
                                    Badouin H, Gouzy J, Grassa CJ, Murat F, Staton SE, Cottret L, Lelandais-Brière C,
                                        Owens GL, Carrère S, Mayjonade B, Legrand L, Gill N, Kane NC, Bowers JE,
                                        Hubner S, Bellec A, Bérard A, Bergès H, Blanchet N, Boniface MC, Brunel D,
                                        Catrice O, Chaidir N, Claudel C, Donnadieu C, Faraut T, Fievet G, Helmstetter
                                        N, King M, Knapp SJ, Lai Z, Le Paslier MC, Lippi Y, Lorenzon L, Mandel JR,
                                        Marage G, Marchand G, Marquand E, Bret-Mestries E, Morien E, Nambeesan
                                        S, Nguyen T, Pegot-Espagnet P, Pouilly N, Raftis F, Sallet E, Schiex T, Thomas
                                        J, Vandecasteele C, Varès D, Vear F, Vautrin S, Crespi M, Mangin B, Burke JM,
                                        Salse J, Muños S, Vincourt P, Rieseberg LH, Langlade NB. 2017. The sunflower
                                        genome provides insights into oil metabolism, flowering and Asterid evolution.
                                        Nature 546(7656):148–152 DOI 10.1038/nature22380.
                                    Bailey TL, Boden M, Buske FA, Frith M, Grant CE, Clementi L, Ren J, Li WW, Noble
                                        WS. 2009. MEME SUITE: tools for motif discovery and searching. Nucleic Acids
                                        Research 37:W202–W208 DOI 10.1093/nar/gkp335.
                                    Baldoni E, Genga A, Cominelli E. 2015. Plant MYB transcription factors: their role
                                        in drought response mechanisms. International Journal of Molecular Sciences
                                        16(7):15811–15851 DOI 10.3390/ijms160715811.




Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                      21/26
                                    Bolser D, Staines DM, Pritchard E, Kersey P. 2016. Ensemble plants: integrating tools
                                        for visualizing, mining, and analyzing plant genomics data. Methods in Molecular
                                        Biology 1374:115–140 DOI 10.1007/978-1-4939-3167-5_6.
                                    Cao L, Yang JX, Guo JJ, Guo JM, Zheng GD, Lu YF. 2018. Effect of fertilizers on cad-
                                        mium uptake and accumulation by sunflowers. Huan Jing Ke Xue 39(11):5189–5197.
                                    Chang TH, Wu LC, Lee TY, Chen SP, Huang HD, Horng JT. 2013. EuLoc: a web-
                                        server for accurately predict protein subcellular localization in eukaryotes by
                                        incorporating various features of sequence segments into the general form of
                                        Chou’s PseAAC. Journal of Computer-Aided Molecular Design 27(1):91–103
                                        DOI 10.1007/s10822-012-9628-0.
                                    Chen C, Chen H, Zhang Y, Thomas HR, Frank MH, He Y, Xia R. 2020. TBtools: an
                                        integrative toolkit developed for interactive analyses of big biological data. Molecular
                                        Plant 13(8):1194–1202 DOI 10.1016/j.molp.2020.06.009.
                                    Chen S, Zhou Y, Chen Y, Gu J. 2018. fastp: an ultra-fast all-in-one FASTQ preprocessor.
                                        Bioinformatics 34(17):i884–i890 DOI 10.1093/bioinformatics/bty560.
                                    Chen X, Zhang X, Jia A, Xu G, Hu H, Hu X, Hu L. 2016. Jasmonate mediates salt-
                                        induced nicotine biosynthesis in tobacco (Nicotiana tabacum L.). Plant Diversity
                                        38(2):118–123 DOI 10.1016/j.pld.2016.06.001.
                                    Dar JS, Cheema MA, Rehmani MIA, Khuhro S, Rajput S, Virk AL, Hussain S, Bashir
                                        MA, Alghanem SM, Al-Zuaibr FM, Ansari MJ, Hessini K. 2021. Potassium fertil-
                                        ization improves growth, yield and seed quality of sunflower (Helianthus annuus
                                        L.) under drought stress at different growth stages. PLOS ONE 16(9):e0256075
                                        DOI 10.1371/journal.pone.0256075.
                                    Ding S, Feng X, Du H, Wang H. 2019. Genome-wide analysis of maize OSCA
                                        family members and their involvement in drought stress. PeerJ 7:e6765
                                        DOI 10.7717/peerj.6765.
                                    Gao T, Yang P, Fu D, Liu M, Deng X, Shao M, Liao J, Jiang H, Li X. 2021. The protective
                                        effect of allicin on myocardial ischemia-reperfusion by inhibition of Ca2+ overload-
                                        induced cardiomyocyte apoptosis via the PI3K/GRK2/PLC- γ /IP3R signaling
                                        pathway. Aging 13(15):19643–19656 DOI 10.18632/aging.203375.
                                    Glasauer SM, Neuhauss SC. 2014. Whole-genome duplication in teleost fishes and its
                                        evolutionary consequences. Molecular Genetics and Genomics 289(6):1045–1060
                                        DOI 10.1007/s00438-014-0889-2.
                                    Gogna M, Bhatla SC. 2019. Biochemical mechanisms regulating salt tolerance in
                                        sunflower. Plant Signaling & Behavior 14(12):1670597
                                        DOI 10.1080/15592324.2019.1670597.
                                    Gong Z, Xiong L, Shi H, Yang S, Herrera-Estrella LR, Xu G, Chao DY, Li J, Wang PY,
                                        Qin F, Li J, Ding Y, Shi Y, Wang Y, Yang Y, Guo Y, Zhu JK. 2020. Plant abiotic
                                        stress response and nutrient use efficiency. Science China Life Sciences 63(5):635–674
                                        DOI 10.1007/s11427-020-1683-x.
                                    Hall BG. 2013. Building phylogenetic trees from molecular data with MEGA. Molecular
                                        Biology and Evolution 30(5):1229–1235 DOI 10.1093/molbev/mst012.



Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                         22/26
                                    Ju C, Zhang Z, Deng J, Miao C, Wang Z, Wallrad L, Javed L, Fu D, Zhang T, Kudla J,
                                          Gong Z, Wang C. 2021. Ca2+-dependent successive phosphorylation of vacuolar
                                          transporter MTP8 by CBL2/3-CIPK3/9/26 and CPK5 contributes to manganese
                                          homeostasis in Arabidopsis. Molecular Plant S1674-2052(21):00467–6.
                                    Keeley SC, Cantley JT, Gallaher TJ. 2021. The evil tribe spreads across the land: a dated
                                          molecular phylogeny provides insight into dispersal, expansion, and biogeographic
                                          relationships within one of the largest tribes of the sunflower family (Vernonieae:
                                          Compositae). American Journal of Botany 108(3):505–519
                                          DOI 10.1002/ajb2.1614.
                                    Kilaru A, Herrfurth C, Keereetaweep J, Hornung E, Venables BJ, Feussner I,
                                          Chapman KD. 2011. Lipoxygenase-mediated oxidation of polyunsaturated N-
                                          acylethanolamines in Arabidopsis. Journal of Biological Chemistry 286(17)
                                          15205–15214 DOI 10.1074/jbc.M110.217588.
                                    Kim D, Paggi JM, Park C, Bennett C, Salzberg SL. 2019. Graph-based genome align-
                                          ment and genotyping with HISAT2 and HISAT-genotype. Nature Biotechnology
                                          37(8):907–915 DOI 10.1038/s41587-019-0201-4.
                                    Kiyosue T, Yamaguchi-Shinozaki K, Shinozaki K. 1994. Cloning of cDNAs for genes
                                          that are early-responsive to dehydration stress (ERDs) in Arabidopsis thaliana
                                          L.: identification of three ERDs as HSP cognate genes. Plant Molecular Biology
                                          25(5):791–798 DOI 10.1007/BF00028874.
                                    Klimecka M, Muszyńska G. 2007. Structure and functions of plant calcium-dependent
                                          protein kinases. Acta Biochimica Polonica 54(2):219–233
                                          DOI 10.18388/abp.2007_3242.
                                    Li J, Yang J, Jia B, Sun M, Liu Y, Yin K, Sun X. 2017. Evolution and expression analysis of
                                          OSCA gene family in soybean genome. Chinese Journal of Oil Crops 39(5):589–599.
                                    Li K, Brownley A. 2010. Primer design for RT-PCR. Methods in Molecular Biology
                                          630:271–299 DOI 10.1007/978-1-60761-629-0_18.
                                    Li Y, Yuan F, Wen Z, Li Y, Wang F, Zhu T, Zhuo W, Jin X, Wang Y, Zhao H, Pei ZM,
                                          Han S. 2015. Genome-wide survey and expression analysis of the OSCA gene family
                                          in rice. BMC Plant Biology 15:261 DOI 10.1186/s12870-015-0653-8.
                                    Liu J, Zhu JK. 1998. A calcium sensor homolog required for plant salt tolerance. Science
                                          280(5371):1943–1945 DOI 10.1126/science.280.5371.1943.
                                    Liu X, Wang J, Sun L. 2018. Structure of the hyperosmolality-gated calcium-permeable
                                          channel OSCA1.2. Nature Communications 9(1):5060
                                          DOI 10.1038/s41467-018-07564-5.
                                    Miao S, Li F, Han Y, Yao Z, Xu Z, Chen X, Liu J, Zhang Y, Wang A. 2022. Identification
                                          of OSCA gene family in Solanum habrochaites and its function analysis under stress.
                                          BMC Genomics 23(1):547 DOI 10.1186/s12864-022-08675-6.
                                    Mistry J, Chuguransky S, Williams L, Qureshi M, Salazar GA, Sonnhammer ELL,
                                          Tosatto SCE, Paladin L, Raj S, Richardson LJ, Finn RD, Bateman A. 2021. Pfam:
                                          the protein families database in 2021. Nucleic Acids Research 49(D1):D412–D419
                                          DOI 10.1093/nar/gkaa913.



Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                       23/26
                                    Murthy SE, Dubin AE, Whitwam T, Jojoa-Cruz S, Cahalan SM, Mousavi SAR, Ward
                                        AB, Patapoutian A. 2018. OSCA/TMEM63 are an evolutionarily conserved family of
                                        mechanically activated ion channels. Elife 7:e41844
                                        DOI 10.7554/eLife.41844.
                                    Pertea M, Pertea GM, Antonescu CM, Chang TC, Mendell JT, Salzberg SL. 2015.
                                        StringTie enables improved reconstruction of a transcriptome from RNA-seq reads.
                                        Nature Biotechnology 33(3):290–295 DOI 10.1038/nbt.3122.
                                    Quan R, Lin H, Mendoza I, Zhang Y, Cao W, Yang Y, Shang M, Chen S, Pardo JM, Guo
                                        Y. 2007. SCABP8/CBL10, a putative calcium sensor, interacts with the protein kinase
                                        SOS2 to protect Arabidopsis shoots from salt stress. Plant Cell 19(4):1415–1431
                                        DOI 10.1105/tpc.106.042291.
                                    Rele AS, Mohile RB. 2003. Effect of mineral oil, sunflower oil, and coconut oil on
                                        prevention of hair damage. Journal of Cosmetic Science 54(2):175–192.
                                    Seo JS, Joo J, Kim MJ, Kim YK, Nahm BH, Song SI, Cheong JJ, Lee JS, Kim JK, Choi YD.
                                        2011. OsbHLH148, a basic helix-loop-helix protein, interacts with OsJAZ proteins in
                                        a jasmonate signaling pathway leading to drought tolerance in rice. The Plant Journal
                                        65(6):907–921 DOI 10.1111/j.1365-313X.2010.04477.x.
                                    Shannon P, Markiel A, Ozier O, Baliga NS, Wang JT, Ramage D, Amin N, Schwikowski
                                        B, Ideker T. 2003. Cytoscape: a software environment for integrated models
                                        of biomolecular interaction networks. Genome Research 13(11):2498–2504
                                        DOI 10.1101/gr.1239303.
                                    Shukla D, Huda KM, Banu MS, Gill SS, Tuteja R, Tuteja N. 2014. OsACA6, a P-type 2B
                                        Ca(2+) ATPase functions in cadmium stress tolerance in tobacco by reducing the
                                        oxidative stress load. Planta 240(4):809–824
                                        DOI 10.1007/s00425-014-2133-z.
                                    Swarbreck SM, Colaço R, Davies JM. 2013. Plant calcium-permeable channels. Plant
                                        Physiology 163(2):514–522 DOI 10.1104/pp.113.220855.
                                    Tanino Y, Kodama M, Daicho H, Miyauchi Y, Yasumoto T, Yamada Y. 2017. Selection
                                        of laboratory procedures to detect toxigenic by the 2-step method. Rinsho Biseibutshu
                                        Jinsoku Shindan Kenkyukai Shi 27(1):9–14.
                                    Toda Y, Yoshida M, Hattori T, Takeda S. 2013. RICE SALT SENSITIVE3 binding to
                                        bHLH and JAZ factors mediates control of cell wall plasticity in the root apex. Plant
                                        Signaling & Behavior 8(11):e26256 DOI 10.4161/psb.26256.
                                    Tong K, Wu X, He L, Qiu S, Liu S, Cai L, Rao S, Chen J. 2021. Genome-wide identifica-
                                        tion and expression profile of OSCA gene family members in triticum aestivum L.
                                        International Journal of Molecular Sciences 23(1):469
                                        DOI 10.3390/ijms23010469.
                                    Umezawa T, Sugiyama N, Mizoguchi M, Hayashi S, Myouga F, Yamaguchi-Shinozaki
                                        K, Ishihama Y, Hirayama T, Shinozaki K. 2009. Type 2C protein phosphatases
                                        directly regulate abscisic acid-activated protein kinases in Arabidopsis. Pro-
                                        ceedings of the National Academy of Sciences of the United States of America
                                        106(41):17588–17593 DOI 10.1073/pnas.0907095106.



Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                     24/26
                                    Valenzuela CE, Acevedo-Acevedo O, Miranda GS, Vergara-Barros P, Holuigue
                                        L, Figueroa CR, Figueroa PM. 2016. Salt stress response triggers activation of
                                        the jasmonate signaling pathway leading to inhibition of cell elongation in Ara-
                                        bidopsis primary root. The Journal of Experimental Botany 67(14):4209–4220
                                        DOI 10.1093/jxb/erw202.
                                    Verma V, Ravindran P, Kumar PP. 2016. Plant hormone-mediated regulation of stress
                                        responses. BMC Plant Biologyogy 16:86 DOI 10.1186/s12870-016-0771-y.
                                    Voorrips RE. 2002. MapChart: software for the graphical presentation of linkage maps
                                        and QTLs. Journal of Heredity 93(1):77–78 DOI 10.1093/jhered/93.1.77.
                                    Wang A, Zhang K, Zhang Y, Chen X, Liu J. 2019. Identification of tomato OSCA gene
                                        family and expression analysis under different stress conditions. Journal of Northeast
                                        Agricultural University 50(01):19–28.
                                    Wang J, Song L, Gong X, Xu J, Li M. 2020. Functions of jasmonic acid in plant regulation
                                        and response to abiotic stress. International Journal of Molecular Sciences 21(4):1446
                                        DOI 10.3390/ijms21041446.
                                    Wang Y, Tang H, Debarry JD, Tan X, Li J, Wang X, Lee TH, Jin H, Marler B, Guo H,
                                        Kissinger JC, Paterson AH. 2012. MCScanX: a toolkit for detection and evolu-
                                        tionary analysis of gene synteny and collinearity. Nucleic Acids Research 40(7):e49
                                        DOI 10.1093/nar/gkr1293.
                                    Warren AJ. 2002. Eukaryotic transcription factors. Current Opinion in Structural Biology
                                        12(1):107–114 DOI 10.1016/S0959-440X(02)00296-8.
                                    Wilkins MR, Gasteiger E, Bairoch A, Sanchez JC, Williams KL, Appel RD, Hochstrasser
                                        DF. 1999. Protein identification and analysis tools in the ExPASy server. Methods in
                                        Molecular Biology 112:531–552.
                                    Xu J, Li HD, Chen LQ, Wang Y, Liu LL, He L, Wu WH. 2006. A protein kinase, in-
                                        teracting with two calcineurin B-like proteins, regulates K+ Transporter AKT1 in
                                        Arabidopsis. Cell 125:1347–1360 DOI 10.1016/j.cell.2006.06.011.
                                    Xue Y, Zhao H, Wang HN, Crawford BM, Johnson DM, Hu C, Pei C, Zhou W,
                                        Swift GB, Zhang H, Vo-Dinh T, Hu Z, Siedow JN, Pei ZM. 2019. Plant cell–
                                        surface GIPC sphingolipids sense salt to trigger Ca2+ influx. Nature 572:341–346
                                        DOI 10.1038/s41586-019-1449-z.
                                    Yin L, Zhang M, Wu R, Chen X, Liu F, Xing B. 2021. Genome-wide analysis of OSCA
                                        gene family members in Vigna radiata and their involvement in the osmotic
                                        response. BMC Plant Biology 21(1):408 DOI 10.1186/s12870-021-03184-2.
                                    Yuan F, Yang H, Xue Y, Kong D, Ye R, Li C, Zhang J, Theprungsirikul L, Shrift T,
                                        Krichilsky B, Johnson DM, Swift GB, He Y, Siedow JN, Pei ZM. 2014. OSCA1
                                        mediates osmotic-stress-evoked Ca2+ increases vital for osmosensing in Arabidopsis.
                                        Nature 514(7522):367–371 DOI 10.1038/nature13593.
                                    Zhai Y, Wen Z, Han Y, Zhuo W, Wang F, Xi C, Liu J, Gao P, Zhao H, Wang Y, Wang Y,
                                        Han S. 2020. Heterogeneous expression of plasma-membrane-localised OsOSCA1.4
                                        complements osmotic sensing based on hyperosmolality and salt stress in Arabidop-
                                        sis osca1 mutant. Cell Calcium 91:102261 DOI 10.1016/j.ceca.2020.102261.



Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                       25/26
                                    Zhang M, Wang D, Kang Y, Wu JX, Yao F, Pan C, Yan Z, Song C, Chen L. 2018.
                                       Structure of the mechanosensitive OSCA channels. Nature Structural & Molecular
                                       Biology 25(9):850–858 DOI 10.1038/s41594-018-0117-6.
                                    Zhang S, Wu QR, Liu LL, Zhang HM, Gao JW, Pei ZM. 2020. Osmotic stress
                                       alters circadian cytosolic Ca2+ oscillations and OSCA1 is required in cir-
                                       cadian gated stress adaptation. Plant Signaling & Behavior 15(12):1836883
                                       DOI 10.1080/15592324.2020.1836883.




Shan et al. (2023), PeerJ, DOI 10.7717/peerj.15089                                                                 26/26
