# Li_2022 - Preliminary Expression Analysis of the OSCA Gene Family in M

**Source PDF:** 

---

              International Journal of
              Molecular Sciences


Article
Preliminary Expression Analysis of the OSCA Gene Family in
Maize and Their Involvement in Temperature Stress
Yuanyang Li † , Yubin Zhang † , Bin Li, Liyuan Hou, Jianing Yu, Chengguo Jia, Zhe Wang, Siqi Chen,
Mingzhe Zhang, Jianchun Qin , Ning Cao, Jinhu Cui and Wuliang Shi *


                                            Center for Emerging Agricultural Education & Advanced Interdisciplinary Science, College of Plant Science,
                                            Jilin University, Changchun 130062, China
                                            * Correspondence: wlshi@jlu.edu.cn; Fax: +86-431-86758762
                                            † These authors contributed equally to this work.


                                            Abstract: Hyperosmolality-gated calcium-permeable channels (OSCA) are characterized as an os-
                                            mosensor in plants; they are able to recognize and respond to exogenous and endogenous osmotic
                                            changes, and play a vital role in plant growth and adaptability to environmental stress. To explore the
                                            potential biological functions of OSCAs in maize, we performed a bioinformatics and expression anal-
                                            ysis of the ZmOSCA gene family. Using bioinformatics methods, we identified twelve OSCA genes
                                            from the genome database of maize. According to their sequence composition and phylogenetic rela-
                                            tionship, the maize OSCA family was classified into four groups (I, II, III, and IV). Multiple sequence
                                            alignment analysis revealed a conserved DUF221 domain in these members. We modeled the calcium
                                            binding sites of four OSCA families using the autodocking technique. The expression profiles of
                                            ZmOSCA genes were analyzed in different tissues and under diverse abiotic stresses such as drought,
                                            salt, high temperature, and chilling using quantitative real-time PCR (qRT-PCR). We found that the
                                            expression of twelve ZmOSCA genes is variant in different tissues of maize. Furthermore, abiotic
Citation: Li, Y.; Zhang, Y.; Li, B.; Hou,
                                            stresses such as drought, salt, high temperature, and chilling differentially induced the expression of
L.; Yu, J.; Jia, C.; Wang, Z.; Chen, S.;
                                            twelve ZmOSCA genes. We chose ZmOSCA2.2 and ZmOSCA2.3, which responded most strongly
Zhang, M.; Qin, J.; et al. Preliminary
                                            to temperature stress, for prediction of protein interactions. We modeled the calcium binding sites
Expression Analysis of the OSCA
                                            of four OSCA families using autodocking tools, obtaining a number of new results. These results
Gene Family in Maize and Their
Involvement in Temperature Stress.
                                            are helpful in understanding the function of the plant OSCA gene family for study of the molecular
Int. J. Mol. Sci. 2022, 23, 13658.          mechanism of plant osmotic stress and response, as well as exploration of the interaction between
https://doi.org/10.3390/                    osmotic stress, high-temperature stress, and low-temperature stress signal transduction mechanisms.
ijms232113658                               As such, they can provide a theoretical basis for crop breeding.

Academic Editor: Abir U. Igamberdiev
                                            Keywords: calcium signaling; OSCA; DUF221 domain; abiotic stress; maize (Zea mays L.)
Received: 29 September 2022
Accepted: 5 November 2022
Published: 7 November 2022

Publisher’s Note: MDPI stays neutral
                                            1. Introduction
with regard to jurisdictional claims in          As a major food crop, maize (Zea mays L.) plays a vital role in solving world hunger
published maps and institutional affil-     problems. However, the production process of maize is highly dependent on suitable
iations.                                    environmental factors [1]. With the reduction in the availability and quality of arable land
                                            and water resources, as well as frequent extreme weather [2], many different types of abiotic
                                            stresses have been highlighted, such as salinity, drought, heat, and chilling [3]. These major
                                            abiotic environmental stresses seriously affect crop development and constrain agronomic
Copyright: © 2022 by the authors.
                                            yields worldwide. Supposedly, abiotic stresses may be responsible for a yield reduction of
Licensee MDPI, Basel, Switzerland.
                                            over 50% in major crop plants globally [4]. Studies have shown that the decline in maize
This article is an open access article
                                            yield is very significant under conditions of undesirable stress. In the last 30 years, maize
distributed under the terms and
                                            yield losses due to heat stress were 1.13% per decade in China [5]. Based on reliable data,
conditions of the Creative Commons
                                            future high temperatures are predicted to increase the decline in corn production from 7%
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
                                            to 31% [6]. High temperatures are currently a major constraint on corn yields in Northeast
4.0/).
                                            China [7]. Cold stress limits food production, and is detrimental to normal plant growth




Int. J. Mol. Sci. 2022, 23, 13658. https://doi.org/10.3390/ijms232113658                                           https://www.mdpi.com/journal/ijms
Int. J. Mol. Sci. 2022, 23, 13658                                                                                           2 of 22




                                    and development [8]. Low temperatures disrupt photosynthetic metabolism, and may
                                    produce stress products such as reactive oxygen species, leading to a reduction in nutrients
                                    as well as inducing harmful structural changes in cells [9]. Maize growth in the field is
                                    influenced by various environmental factors, and it is particularly relevant to elucidate the
                                    signaling patterns associated with resistance to stress.
                                          Temperature, salt, and drought stresses are major environmental factors that affect
                                    growth and development of plants in world, restrict plant productivity, and threaten human
                                    food security. How plants sense these stress signals and adapt to adverse environments are
                                    fundamental biological questions [10]. Under osmotic stress, an increase in intracellular
                                    calcium levels is achieved through transport pathways such as calcium channels [11].
                                    Plants are subject to adversity stress, which triggers calcium oscillations in plants [12];
                                    at the physiological, cellular, and molecular levels, this takes the form of inducing the
                                    expression of many stress-related genes, regulating plant tolerance to stress, and generating
                                    specific calcium signals [13]. It has been reported that calcium-associated proteins are
                                    required for several environmental stress responses [14]. Ion channels are proteins located
                                    in the cell membrane that aid in ion transport and play an important role in maintaining
                                    cellular homeostasis [15]. Hyperosmolality-gated calcium-permeable channels (OSCA),
                                    as one of the more recently discovered calcium channels, play an essential role in calcium
                                    signaling. Following the discovery and identification of OSCA1.1 in Arabidopsis thaliana [16],
                                    the OSCA gene family has been increasingly valued by scientists worldwide. Yuan et al. [16]
                                    established that OSCA1 protein, localized in the plant cell membrane, is expressed in both
                                    leaves and roots of Arabidopsis. Currently, ZmOSCA is associated with osmolarity-related
                                    stresses [17] such as drought and ABA, which is consistent with studies on other species.
                                    Over time, researchers have discovered that OSCA is widely distributed in eukaryotic
                                    cells, whether plants or animals [18]. It has been discovered that OSCA carries a major
                                    conserved protein, DUF221, which contains six predicted TM helices [19]. The TM helices
                                    in the structures of such proteins may have disappeared during evolution, as OsOSCA2.2
                                    lacks three TM regions [20]. The same study found that OSCA proteins may have effects on
                                    other traits. TaOSCA1.4, which belongs to the same family as AtOSCA1.8 and OsOSCA1.4
                                    in the evolutionary tree analysis, is related to the grain number per ear [21]. The number of
                                    grains on the ear is one of the most important traits for maize yield. In addition, osmotic
                                    pressure affects the water balance in the plant, which in turn determines the crop yield.
                                    OSCA is a confirmed gene family associated with osmolality, and we found that it may
                                    have a key role in coping with the effects of temperature as well. This is an important
                                    means of improving the knowledge of abiotic stress resistance in maize. More importantly,
                                    determining the stress tolerance mechanism of maize can provide a theoretical basis for
                                    breeding drought-resistant varieties and improving cultivation techniques.
                                          In the present study, we performed a bioinformatics analysis of the entire maize
                                    genome and identified twelve OSCA genes. These twelve maize OSCAs were grouped
                                    based on their phylogenetic relationships and their expression profiles in various organs
                                    and under different abiotic stresses. We found that OSCAs play a role in osmolality, and may
                                    be important in temperature stress and related signaling pathways as well. Furthermore,
                                    we predicted the calcium binding sites in proteins and carried out a protein interaction
                                    analysis, verifying that our conjecture is possible. These results can be used for functional
                                    validation studies of ZmOSCA and increase our understanding of the roles of plant OSCAs.

                                    2. Results
                                    2.1. Phylogenetic Relationship and Gene Structure of Maize OSCAs
                                          We used the CDS (coding sequence of amino acids in protein) of 38 OSCAs from
                                    rice, Arabidopsis, and maize to construct a phylogenetic tree (Figure 1) to determine the
                                    evolutionary relationships of OSCA in maize, and collated the information related to the
                                    ZmOSCA gene in the maize genome database (http://ensembl.gramene.org/, revised 18
                                    January 2022) (Table 1). We found that members of the OSCA family were separated into
                                    four distinct clades, designated I, II, III, and IV (Figure 2). Most OSCA family members in
Int. J. Mol. Sci. 2022, 23, 13658                                                                                                   3 of 22




                                     Arabidopsis, rice, and maize were mainly distributed in groups I and II as compared with
                                     groups III and IV. By further analyzing the results, we found that the OSCA genes in maize
                                     and rice were more closely related. We grouped all the OSCAs genes as shown in Table 2.




                                     Figure 1. Phylogenetic analysis of OSCA proteins. Arabidopsis, rice, and maize are denoted by circle,
                                     diamond, and triangle respectively, and the tree is divided into four groups.

                                     Table 1. Information of OSCA family members in maize.

                                                                 Number of          Number of
         Gene                         Position                                                       Length (AA)           Strand
                                                                 Transcripts          Exons
                                 Contig B73V4_ctg31
    ZmOSCA1.1                                                         9                 11                768          forward strand
                                   243,552–267,664
    ZmOSCA1.2                Chr3 231,673,936–231,685,374             15                13                785          forward strand
    ZmOSCA1.3                 Chr8 80,433,878–80,440,706               6                12                790          forward strand
    ZmOSCA1.4                Chr6 152,198,261–152,212,313             14                12                748           reverse strand
    ZmOSCA1.5                Chr1 108,282,883–108,288,994              5                11                810           reverse strand
    ZmOSCA2.1                Chr3 106,709,675–106,715,943              6                12                767          forward strand
    ZmOSCA2.2                Chr1 261,919,725–261,930,103              2                12                765          forward strand
    ZmOSCA2.3                  Chr5 9,735,399–9,740,575                8                11                749          forward strand
    ZmOSCA2.4                Chr1 164,016,950–164,031,018              5                10                699          forward strand
    ZmOSCA2.5                Chr8 163,438,578–163,443,056              3                10                703           reverse strand
    ZmOSCA3.1                Chr2 241,256,310–241,261,093              1                 6                732           reverse strand
    ZmOSCA4.1                Chr9 155,107,951–155,110,341              1                 1                796          forward strand
Int. J. Mol. Sci. 2022, 23, 13658                                                                                                      4 of 22




                                    Figure 2. Exon–intron gene structures of ZmOSCAs. The horizontal black lines, green boxes, thick
                                    blue lines, and numbers in the top right corner of the green boxes indicate the positions of introns, the
                                    positions of exons, the positions of UTRs (untranslated regions), and the intron phase, respectively.

                                    Table 2. The distribution of plant OSCA genes in groups I, II, III, and IV.

                                            Species               Total         Group I        Group II       Group III       Group IV
                                      Arabidopsis thaliana         15              8               5               1               1
                                         Oryza sativa              11              4               5               1               1
                                           Zea mays                12              5               5               1               1


                                         Then, we used Gene Structure Display Server (http://gsds.cbi.pku.edu.cn/index.php,
                                    revised 30 January 2022) to generate the intron and exon structure information maps of each
                                    gene in the ZmOSCA family (Figure 2). It was recognized that the gene structures of OSCA
                                    genes belonging to the same subfamily were often very similar, with the number and size
                                    of introns and exons being nearly identical. Except for ZmOSCA3.1, which contained six
                                    exons and for which the fourth exon was significantly longer, all members of the ZmOSCA
                                    I subfamily contained eleven exons and ten introns; however, the lengths of exons 1, 2, 5,
                                    and 6 of ZmOSCA3.1 are noteworthy. The lengths of exons 1, 2, 5, and 6 of ZmOSCA3.1
                                    are the same as the lengths of the exons at both ends of the other members. All OSCA
                                    II subfamily members contain ten exons and nine introns. ZmOSCA4.1 is more distantly
                                    related to the other members, and may be more primitive and conserved.

                                    2.2. Analysis of Structural Domains of the ZmOSCA Family
                                         DUF221 is a characterized structural domain of the OSCA gene family [16]. Mul-
                                    tiple sequence alignments of OSCAs were performed using DNAMAN software (http:
                                    //www.lynnon.com/dnaman.html, revised 20 February 2022), and the transmembrane
                                    (TM) region of the DUF221 conserved region was predicted using TMHMM. We found
                                    that different OSCA members contain different TMs; most of the OSCA have six TMs with
                                    two exceptions. ZmOSCA4.1 had fewer TM4, and ZmOSCA1.5 had more TM5 disappear
                                    than their orthologues, which suggested that a deletion event occurred in the genomes of
Int. J. Mol. Sci. 2022, 23, 13658                                                                                               5 of 22




                                    ZmOSCA4.1 and ZmOSCA1.5 (Figure 3). TMs from the same family are similar, while there
                                    are large differences between families.




                                    Figure 3. Multiple sequence alignment and transmembrane region of the DUF221 conserved region
                                    in ZmOSCAs. The region between two vertical red lines represents the DUF221 conserved region.
                                    Identical (100%), conserved (75–99%), and blocks (50–74%) of similar amino acid residues are shaded
                                    in dark navy, pink, and cyan, respectively. The transmembrane regions are marked by black lines and
                                    called TM1-TM6.
Int. J. Mol. Sci. 2022, 23, 13658                                                                                             6 of 22




                                    2.3. Predicted Secondary Structure Analysis of ZmOSCA Gene Family Proteins
                                         The secondary structure of each member of the ZmOSCA protein family was predicted
                                    by SOPMA based on the Protein Data Bank, and the results were counted. The results
                                    showed that the twelve OSCA protein family members of maize mainly contained four
                                    structures, Alpha helix (Hh), Extended strand (Ee), Beta turn (Tt), and Random coil (Cc),
                                    among which Alpha helix (Hh) accounted for the largest number and proportion of the
                                    secondary structures (Figure 4: Table 3). The protein secondary structures of ZmOSCA1.1,
                                    ZmOSCA1.2, and ZmOSCA1.3 are identical to each other. ZmOSCA2.1, ZmOSCA2.2, and
                                    ZmOSCA2.3 are very close to each other as well. In addition, we discovered a large
                                    difference in the secondary structure of proteins from different families.

                                    Table 3. Predicted secondary structure of maize OSCA proteins.

     Gene                Alpha Helix (Hh)         Extended Strand (Ee)            Beta Ture (Tt)            Random Coil (Cc)
 ZmOSCA1.1               317        41.28%          178         23.18%           44          5.73%          229          29.82%
 ZmOSCA1.2               331        42.17%          175         22.29%           46          5.86%          233          29.68%
 ZmOSCA1.3               338        42.78%          170         21.52%           51          6.46%          231          29.24%
 ZmOSCA1.4               302        40.37%          167         22.33%           60          8.02%          219          29.28%
 ZmOSCA1.5               380        46.91%          151         18.64%           50          6.17%          229          28.27%
 ZmOSCA2.1               322        41.98%          173         22.56%           50          6.52%          222          28.94%
 ZmOSCA2.2               292        28.17%          166         21.70%           53          6.93%          254          33.20%
 ZmOSCA2.3               337        44.99%          165         22.03%           63          8.41%          184          24.57%
 ZmOSCA2.4               315        45.06%          147         21.03%           42          6.01%          195          27.90%
 ZmOSCA2.5               332        47.23%          128         18.21%           56          7.97%          187          26.60%
 ZmOSCA3.1               329        44.95%          154         21.04%           52          7.10%          197          26.91%
 ZmOSCA4.1               400        50.25%          122         15.33%           50          6.28%          224          28.14%




                                    Figure 4. Predicted secondary structure of maize OSCA proteins. The blue, red, green, and yellow
                                    stripes represent the α helices, the β bridges, the β turns, and the random coils, respectively.

                                    2.4. Characterization of the ZmOSCA Gene Family for Tissue-Based Expression
                                         To unveil the potential function of ZmOSCAs in maize, the expression profiles of
                                    ZmOSCA genes in various tissues and organs were first determined using RT-PCR (real-time
                                    reverse transcription-PCR), and are represented in greyscale to facilitate visualization. The
Int. J. Mol. Sci. 2022, 23, 13658                                                                                               7 of 22




                                    twelve ZmOSCA genes showed tissue-specific expression patterns. ZmOSCA genes were
                                    highly expressed in all tissues tested with two exceptions (Figure 5), which is indicative of
                                    a universal role of OSCAs in osmotic-sensing processes throughout the plant. ZmOSCA2.3
                                    and ZmOSCA2.5 were detected only in the leaf, indicative of a specific function therein.
                                    ZmOSCA1.3, ZmOSCA1.4, ZmOSCA1.5, ZmOSCA2.3, and ZmOSCA2.4 showed medium
                                    transcript abundances in all tissues tested. ZmOSCA1.2, ZmOSCA2.1, and ZmOSCA3.1 had
                                    high transcript abundance in the root and relatively high transcript abundance in the stem,
                                    suggesting that they are likely related to root uptake. These results indicate that ZmOSCAs
                                    are involved in various physiological and developmental processes in maize.




                                    Figure 5. Schematic representation of the organ-specific expression of the ZmOSCA genes. The colors
                                    white, 25% grey, 35% grey, 50% grey, 75% grey, and black represent the multiple ranges of ZmOSCA
                                    mRNA expression levels, which were <0.01, 0.01–0.1, 0.1–1, 1.0–10, 10–50, and >50, respectively,
                                    compared with 0.002 GAPDH.
Int. J. Mol. Sci. 2022, 23, 13658                                                                                                8 of 22




                                    2.5. Expression Profiles of ZmOSCAs under Osmotic-Related Abiotic Stresses
                                          To determine whether the expression of ZmOSCAs is responsive to osmotic-related
                                    abiotic stress, qRT-PCR analysis of the ZmOSCAs at the 10-day stage in maize was per-
                                    formed under PEG 6000 (10%) and NaCl (250 mM). We found that twelve ZmOSCA genes
                                    were down- or upregulated in the stress conditions examined as compared with the con-
                                    trol (Figures 6 and 7). Majority of the ZmOSCAs were substantially altered within 6 h.
                                    ZmOSCA1.1 was upregulated by 10% PEG and salt stress treatment, and ZmOSCA1.5 was
                                    specifically downregulated. ZmOSCA1.3 and ZmOSCA2.1 were downregulated at 1 h and
                                    then slowly recovered. Among the genes expressed after treatment, ZmOSCA1.1 was the
                                    most altered. These results indicate that ZmOSCAs might be involved in osmotic-related
                                    signaling pathways.




                                    Figure 6. Expression profiles of ZmOSCA genes under 10% PEG-6000. The relative expression
                                    levels of ZmOSCAs were determined in the roots of three-true-leaf-stage seedlings treated with 10 %
                                    PEG-6000 for 0 h, 1 h, and 6 h and compared with the control.
Int. J. Mol. Sci. 2022, 23, 13658                                                                                               9 of 22




                                    Figure 7. Expression profiles of ZmOSCA genes under NaCl stress. The relative expression levels of
                                    ZmOSCAs were determined in the roots of three-true-leaf-stage seedlings treated with 200 mM NaCl.

                                    2.6. Expression Profile of ZmOSCAs under Environment-Related Abiotic Stresses
                                          To further investigate whether ZmOSCAs affect other environmentally relevant abiotic
                                    stresses, we used qRT-PCR analysis at the 10-day stage in maize, performed at 4 ◦ C and
                                    40 ◦ C. The test results showed that twelve ZmOSCA genes were changed in the conditions
                                    examined as compared with the control (Figures 8 and 9).




                                    Figure 8. The expression levels of ZmOSCA genes under 40 ◦ C treatment conditions were monitored
                                    using qRT-PCR. Samples were collected after 0, 1, 6, 12, and 24 h of heat treatment.
Int. J. Mol. Sci. 2022, 23, 13658                                                                                           10 of 22




                                    Figure 9. The expression levels of ZmOSCA genes under 4 ◦ C treatment conditions were monitored
                                    with qRT-PCR. Samples were collected after 0, 1, 6, 12, and 24 h of cold treatment.

                                          When the plants were under 40 ◦ C stress, we found that the expression of OSCA
                                    genes could be divided into two groups. The expression trends of six genes, ZmOSCA1.4,
                                    ZmOSCA2.1, ZmOSCA2.2, ZmOSCA2.5, ZmOSCA3.1, and ZmOSCA4.1, were relatively
                                    similar; all of them showed a significant increase in gene expression level after 1 h of
                                    high-temperature stress, reached a peak, and then were rapidly downregulated, followed
                                    by a slow increase. The expression trend of ZmOSCA2.1 was similar to that of ZmOSCA2.3,
                                    except that the expression level continued to be downregulated until 24 h of treatment, and
                                    did not increase. The expression trend of ZmOSCA1.2 was similar, with the difference that
                                    expression was slightly downregulated at 1 h of high-temperature stress and then increased
                                    continuously.
                                          The expression patterns of ZmOSCA1.3, ZmOSCA1.5, and ZmOSCA2.4 were opposite
                                    to the other members of the maize OSCA family. The expression of ZmOSCA1.3 continued
                                    to be downregulated after high-temperature stress in maize, and started to show an up-
                                    regulation trend after reaching a minimum value at 6–12 h. By 24 h, it exceeded its level
                                    in the absence of stress. ZmOSCA1.5 expression dropped to a very low level within 1 h of
                                    heat stress, then increased slowly during the next 23 h. The initial expression level was
                                    restored after 24 h of stress. The expression image of ZmOSCA2.4 showed that after the
                                    rapid upregulation of expression level induced by high temperature, the transcript level of
                                    this gene continued to be stable at the level above and below three times the level of the
                                    initial expression.
                                          From the data obtained from seedlings under low-temperature stress at 4 ◦ C, we
                                    know that for the vast majority of ZmOSCA genes (ZmOSCA1.2, ZmOSCA1.3, ZmOSCA1.5,
                                    ZmOSCA2.4, ZmOSCA3.1, and ZmOSCA4.1), expression decreases first, then rises to a
                                    relatively large value, then gradually decreases again. ZmOSCA1.4 is very similar to this
                                    trend, except that it rises to a value and then does not fall. Similarly, ZmOSCA2.1 is not
                                    obvious at the beginning of the decline. Their function in plant resistance to low temper-
Int. J. Mol. Sci. 2022, 23, 13658                                                                                            11 of 22




                                    atures is similar as well. More special are ZmOSCA1.1, ZmOSCA2.2, and ZmOSCA2.3.
                                    ZmOSCA1.1 showed a cliff-like decrease and only slowly recovered after 12 h. The expres-
                                    sions of ZmOSCA2.2 and ZmOSCA2.3, in general, increased steadily. The expression level
                                    of ZmOSCA3.1 at 6 h reached 1.5-fold that in the absence of stress, and we speculate that the
                                    transcription of this gene may be regulated by the feedback mechanism of low-temperature
                                    stress and involved in a specific function in the low-temperature stress response.

                                    2.7. Prediction of Binding Sites for Ca2+ in OSCA Proteins
                                         As the crystal structure of ZmOSCAs has not been reported, we used the OSCA1.1
                                    of Arabidopsis. We acquired the projected structure of this protein by SWISS-MODEL
                                    Repository (OSCA1.1, ID: 6JPF) and modeled the likely binding mode of calcium ions to
                                    the OSCA proteins using molecular docking. There are different potential binding sites
                                    between calcium ions and OSCAs through polar contacts, as shown in Figure 10. According
                                    to the results of the images, we conclude that OSCA is often combined with ASN and
                                    ILE. Such a phenomenon may be associated with the charge distribution of protein amino
                                    acid residues. Perhaps a deeper study of OSCA, a calcium-permeable protein, could be
                                    performed through calcium-binding sites.




                                    Figure 10. The possible binding mode of Ca2+ and OSCAs was simulated by Auto Dock 4.0 software.
                                    (a) Ca2+ binds to residues GLN-609, ILE-610, and TRY-614 by a covalent bond in OSCA1.1 (b) Ca2+
                                    binds to residues SER-342 and ASN-343 by a covalent bond in OSCA2.1 (c) Ca2+ binds to residues
                                    ASN-463 and VAL-461 by a covalent bond in OSCA3.1 (d) Ca2+ bind to residues ILE-662 by a covalent
                                    bond in OSCA4.1.
Int. J. Mol. Sci. 2022, 23, 13658                                                                                                12 of 22




                                    2.8. ZmOSCA2.2 and ZmOSCA2.3 Protein Prediction Analysis Results
                                         Based on the OSCA genes affected by temperature stress, we selected ZmOSCA2.2
                                    and ZmOSCA2.3, for which the expression was significantly altered at both 40 ◦ C and
                                    4 ◦ C. These were further analyzed in order to predict protein interactions (Figure 11;
                                    Tables 4 and 5). From the predictive analysis, we know that the PPI enrichment p-value is
                                    9.36 × 10-5 for ZmOSCA2.2, while for ZmOSCA2.3 PPI it is 6.58 × 10-8 . The mean clustering
                                    coefficients of ZmOSCA2.2 and ZmOSCA2.3 are 0.793 and 0.855, respectively.




                                    Figure 11. Predicted protein interaction results for ZmOSCA2.2 and ZmOSCA2.3. (a) Predictive
                                    analysis results of ZmOSCA2.2 and (b) Predictive analysis results of ZmOSCA2.3. The length of the
                                    line segment indicates the distance between the target protein and the predicted protein in terms of
                                    the action relationship. No second shell is set to interact with the protein.

                                         Looking at the predicted results, our analysis perceives that both ZmOSCA2.2 and
                                    ZmOSCA2.3 have interactions with GRMZM2G029546, GRMZM2G045854, GRMZM2G033926,
                                    GRMZM2G175423, GRMZM2G702253, GRMZM2G060296, and GRMZM2G319454. Anal-
                                    ysis of its protein annotation and family revealed that GRMZM2G029546 is a Dnaj heat
                                    shock n-terminal domain-containing and Electron transporter/heat shock protein binding
                                    protein with important roles in plant stress responses and signaling. GRMZM2G045854 is a
                                    Gbf-interacting protein, which has a DUF1296 domain, which can enhance the transcrip-
                                    tional activity of plant growth-related transcription factors [22]. GRMZM2G033926 belongs
                                    to the 1-acyl-sn-glycerol-3-phosphate acyltransferases, which can catalyze the acylation
                                    of lysophosphatidic acid and are responsible for the de novo production of phosphatidic
                                    acid [23]. GRMZM2G175423 belongs to the class of Sorbitol dehydrogenases. For enzymes,
                                    including many proteins that are irreplaceable in biological reactions, the differences they
                                    show with changes in temperature are extremely significant. OSCA has several interactions
                                    with a wide range of enzymes in maize.
                                         Moreover, OSCA2.2 interacts closely with the NAD(P)-dependent dehydrogenase,
                                    short-chain alcohol dehydrogenase family and allantoin: proton symporter activity. As
                                    such, we speculate that OSCA2.2 is related to energy metabolism. In the prediction results
                                    of OSCA2.3, two protein families, pectinesterase inhibitor activity and ethylene-activated
                                    signaling pathway, were prominent. We speculate that OSCA2.3 is involved in the hormone
                                    pathway in plants and may play a specific role. Furthermore, OSCA2.3 was found to be
                                    associated with ABC transporter protein. In Gram-Positive Pathogens, the ABC protein is
                                    governed by the treatment temperature [24].
Int. J. Mol. Sci. 2022, 23, 13658                                                                                                                                                                13 of 22




                                       Table 4. Prediction of proteins interacting with OSCA2.2 and their family information.

                                    Identifier                    Protein Annotations                    Length (AA)            Protein Families (COGs):          Protein Families Function
                                                                                                                                                                Ca2+ -binding protein, EF-hand
        P2.2-1             GRMZM2G072052_P01            Putative calcium-binding protein CML15                234                      COG5126
                                                                                                                                                                         superfamily
                                                            NAD(P)-binding Rossmann-fold
                                                                   superfamily protein;
                                                                Retinol dehydrogenase 12;                                                                     NAD(P)-dependent dehydrogenase,
        P2.2-2             GRMZM2G121034_P01                                                                  367                      COG1028
                                                                 Uncharacterized protein;                                                                  short-chain alcohol dehydrogenase family
                                                                Belongs to the short-chain
                                                        dehydrogenases/reductases (SDR) family
        P2.2-3             GRMZM2G450125_P01                           Beta-amylase                           573                     NOG256053              Amylopectin maltohydrolase activity
        P2.2-4             GRMZM2G177570_P01                    Annotation not available                      707                      COG4886                Leucine-rich repeat (LRR) protein
                                                         Plant invertase/pectin Methylesterase
        P2.2-5             GRMZM2G046111_P01                                                                  243                     NOG10079                    Enzyme inhibitor activity
                                                              inhibitor superfamily protein
                                                           Gbf-interacting protein 1 isoform x1;
        P2.2-6             GRMZM2G045854_P01              Putative DUF1296 domain-containing                  540                     NOG236453            Protein of unknown function (DUF1296)
                                                                      family protein
                                                            WAPL (Wings apart-like protein                                                                     1-acyl-sn-glycerol-3-phosphate
        P2.2-7             GRMZM2G033926_P01                                                                  334                      COG0204
                                                         Regulation of heterochromatin) protein                                                                        acyltransferase
                                                                                                                                                               Ca2+ -binding protein, EF-hand
        P2.2-8             GRMZM2G180054_P01            Putative calcium-binding protein CML15                109                      COG5126
                                                                                                                                                                         superfamily
        P2.2-9             GRMZM2G025833_P01                           Beta-amylase                           544                     NOG256053              Amylopectin maltohydrolase activity
                                                              Calcium-binding protein CML;                                                                     Ca2+ -binding protein, EF-hand
       P2.2-10             GRMZM5G847466_P01                                                                  172                      COG5126
                                                                       Calmodulin                                                                                        superfamily
                                                                    Dehydrin COR410;
       P2.2-11             GRMZM2G147014_P01                                                                  290                     NOG17228                        Response to water
                                                           Belongs to the plant dehydrin family
                                                        Tyrosine-sulfated glycopeptide receptor 1;
                                                          Putative phytosulfokine receptor (LRR
       P2.2-12             GRMZM2G474777_P01                                                                  665                      COG4886                 Leucine-rich repeat (LRR) protein
                                                         repeat-containing protein kinase) family
                                                                          protein
       P2.2-13             GRMZM2G154114_P01                     Annotation not available                     381                      COG0515                 Serine/threonine-protein kinase
                                                                        Dehydrin3;
                                                                        Dehydrin;
       P2.2-14             GRMZM2G373522_P01                                                                  289                     NOG17228                        Response to water
                                                                 Uncharacterized protein;
                                                           Belongs to the plant dehydrin family
                                                                                                                                                             Negative regulation of transcription,
       P2.2-15             GRMZM2G095452_P01                 Transcription repressor OFP12                    269                     NOG269813
                                                                                                                                                                      DNA-templated
Int. J. Mol. Sci. 2022, 23, 13658                                                                                                                                                   14 of 22




                                       Table 4. Cont.

                                    Identifier                    Protein Annotations                 Length (AA)   Protein Families (COGs):          Protein Families Function
                                                          Uncharacterized protein loc100192507;
                                                                                                                                                  NAD(P)-dependent dehydrogenase,
       P2.2-16             GRMZM2G464885_P01               Short-chain dehydrogenase TIC 32               314              COG1028
                                                                                                                                               short-chain alcohol dehydrogenase family
                                                                       chloroplastic
                                                          Uncharacterized protein loc100279724;
       P2.2-17             GRMZM2G043191_P01                 Type IV inositol polyphosphate               347              COG5411             Phosphatidylinositol dephosphorylation
                                                                    5-phosphatase 11
                                                           Sorbitol dehydrogenase homolog 1;                                                     Threonine dehydrogenase or related
       P2.2-18             GRMZM2G175423_P01                                                              366              COG1063
                                                                 Sorbitol dehydrogenase                                                            Zn-dependent dehydrogenase
                                                           Short-chain dehydrogenase TIC 32
                                                                       chloroplastic;
                                                                Retinol dehydrogenase 14;                                                         NAD(P)-dependent dehydrogenase,
       P2.2-19             GRMZM2G009940_P02                                                              316              COG1028
                                                                 Uncharacterized protein;                                                      short-chain alcohol dehydrogenase family
                                                                Belongs to the short-chain
                                                        dehydrogenases/reductases (SDR) family
                                                           Short-chain dehydrogenase TIC 32
                                                                       chloroplastic;                                                             NAD(P)-dependent dehydrogenase,
       P2.2-20             GRMZM2G128577_P02                                                              315              COG1028
                                                                Belongs to the short-chain                                                     short-chain alcohol dehydrogenase family
                                                        dehydrogenases/reductases (SDR) family
       P2.2-21             GRMZM2G702253_P02                     Annotation not available                 304              COG0345                Pyrroline-5-carboxylate reductase
                                                        Dual-specificity protein-like phosphatase
                                                                             1;
       P2.2-22             GRMZM2G119079_P01                                                              347              KOG1719                   Dual specificity phosphatase
                                                              Protein-tyrosine phosphatase
                                                                     mitochondrial 1
                                                                Dnaj heat shock n-terminal
                                                                domain-containing protein;
                                                                                                                                                 DnaJ-class molecular chaperone with
       P2.2-23             GRMZM2G029546_P03                 Electron transporter/heat shock              343              COG0484
                                                                                                                                                    C-terminal Zn finger domain
                                                                 protein-binding protein;
                                                                 Uncharacterized protein
                                                              Uncharacterized loc100272659;
       P2.2-24             GRMZM2G055238_P01                                                              403             NOG06404               Allantoin: proton symporter activity
                                                                 Uncharacterized protein
                                                                 Uncharacterized protein;
       P2.2-25             GRMZM2G135746_P01                                                              403             NOG06404               Allantoin: proton symporter activity
                                                                    Ureide permease 5
                                                           Signal recognition particle receptor
                                                                      subunit alpha;
       P2.2-26             GRMZM2G060296_P01                                                              625              COG0552                Signal recognition particle GTPase
                                                        Signal recognition particle protein subunit
                                                                             9
Int. J. Mol. Sci. 2022, 23, 13658                                                                                                                                                                  15 of 22




                                       Table 4. Cont.

                                    Identifier                    Protein Annotations                    Length (AA)            Protein Families (COGs):          Protein Families Function
                                                         Uncharacterized protein;
       P2.2-27             GRMZM2G025528_P05                                                                  242                     NOG06404               Allantoin: proton symporter activity
                                                           Ureide permease 5
                                                      Uncharacterized loc100502471;
       P2.2-28             GRMZM2G091891_P02                                                                  411                     NOG06404               Allantoin: proton symporter activity
                                                           Ureide permease 5
                                                   Menaquinone-specific isochorismate
                                                                                                                                                              Anthranilate/para-aminobenzoate
       P2.2-29             GRMZM2G022837_P01                    synthase;                                     562                      COG0147
                                                                                                                                                                   synthases component I
                                                  Isochorismate synthase 2 chloroplastic
                                                  Uncharacterized protein loc100278112;
       P2.2-30            GRMZM2G319454_P01IDP592                                                             170                      KOG4831                        Unnamed protein
                                                       Transmembrane-like protein


                                       Table 5. Prediction of proteins interacting with OSCA2.3 and their family information.

                                    Identifier                    Protein Annotations                    Length (AA)            Protein Families (COGs):          Protein Families Function
        P2.3-1             GRMZM6G732597_P01                    Annotation not available                      732                      COG5594             Calcium-activated cation channel activity
                                                               Pectinesterase inhibitor 28;
        P2.3-2               AC186577.3_FGP006               Cell wall/vacuolar inhibitor of                   -                      NOG14257                 Pectinesterase inhibitor activity
                                                                     fructosidase 2
                                                             Cell wall/vacuolar inhibitor of
                                                                     fructosidase 2;
        P2.3-3             GRMZM2G368698_P02                                                                  214                     NOG14257                 Pectinesterase inhibitor activity
                                                                        C/VIF2;
                                                                Uncharacterized protein
                                                             Cell wall/vacuolar inhibitor of
        P2.3-4             GRMZM2G300141_P01                         fructosidase 2;                          222                     NOG14257                 Pectinesterase inhibitor activity
                                                                Uncharacterized protein
                                                               Pectinesterase inhibitor 28;
        P2.3-5             GRMZM2G101945_P01                 Cell wall/vacuolar inhibitor of                  233                     NOG14257                 Pectinesterase inhibitor activity
                                                                     fructosidase 2
                                                                Uncharacterized protein;
        P2.3-6             GRMZM5G891247_P01                 Cell wall/vacuolar inhibitor of                  222                     NOG14257                 Pectinesterase inhibitor activity
                                                                     fructosidase 2
        P2.3-7             GRMZM2G055180_P01            Ethylene-responsive transcription factor 2            279                     NOG243370             Ethylene-activated signaling pathway
        P2.3-8             GRMZM2G466044_P01                    Annotation not available                      282                     NOG243370             Ethylene-activated signaling pathway
Int. J. Mol. Sci. 2022, 23, 13658                                                                                                                                               16 of 22




                                       Table 5. Cont.

                                    Identifier                    Protein Annotations                 Length (AA)   Protein Families (COGs):        Protein Families Function
                                                            WAPL (Wings apart-like protein                                                       1-acyl-sn-glycerol-3-phosphate
        P2.3-9             GRMZM2G033926_P01                                                              334              COG0204
                                                         regulation of heterochromatin) protein                                                           acyltransferase
                                                                                                                                                S-adenosylmethionine-dependent
       P2.3-10             GRMZM2G358139_P01                    Annotation not available                  282             NOG01264
                                                                                                                                                    methyltransferase activity
                                                                                                                                               DnaJ-class molecular chaperone with
       P2.3-11             GRMZM2G059801_P01                    Annotation not available                  325              COG0484
                                                                                                                                                  C-terminal Zn finger domain
                                                             AP2-EREBP transcription factor;
                                                        Putative AP2/EREBP transcription factor
       P2.3-12             GRMZM2G080516_P01                                                              270             NOG243370            Ethylene-activated signaling pathway
                                                                    superfamily protein;
                                                                 Uncharacterized protein
                                                                Dnaj heat shock n-terminal
                                                                domain-containing protein;
                                                                                                                                               DnaJ-class molecular chaperone with
       P2.3-13             GRMZM2G029546_P03                 Electron transporter/heat shock              343              COG0484
                                                                                                                                                  C-terminal Zn finger domain
                                                        protein-binding protein; Uncharacterized
                                                                          protein
                                                               DNAJ heat shock N-terminal
                                                                domain-containing protein;                                                     DnaJ-class molecular chaperone with
       P2.3-14             GRMZM2G343149_P01                                                              473              COG0484
                                                             DnaJ domain-containing protein;                                                      C-terminal Zn finger domain
                                                                 Uncharacterized protein
                                                              Uncharacterized loc100383917;                                                     S-adenosylmethionine-dependent
       P2.3-15               AC204277.3_FGP006                                                             -              NOG01264
                                                            Putative methyltransferase PMT23                                                        methyltransferase activity
                                                        Probable methyltransferase pmt23 isoform
                                                                                                                                                S-adenosylmethionine-dependent
       P2.3-16             GRMZM2G045249_P01                                x1;                           508             NOG01264
                                                                                                                                                    methyltransferase activity
                                                            Putative methyltransferase PMT23
                                                                 Uncharacterized protein                                                       Late embryogenesis abundant (LEA)
       P2.3-17             GRMZM2G473960_P01                                                              112             NOG44451
                                                          loc100286326;Seed maturation protein                                                             group 1
                                                            Signal recognition particle receptor
                                                                       subunit alpha;
       P2.3-18             GRMZM2G060296_P01                                                              625              COG0552              Signal recognition particle GTPase
                                                        Signal recognition particle protein subunit
                                                                             9
                                                          Uncharacterized protein loc109623449;
       P2.3-19             GRMZM2G054465_P01                                                              409              COG0133               Tryptophan synthase beta chain
                                                             Tryptophan synthase beta type 2
                                                          Chaperone DnaJ-domain superfamily
                                                                          protein;                                                             DnaJ-class molecular chaperone with
       P2.3-20             GRMZM2G087758_P01                                                              258              COG0484
                                                             DnaJ domain-containing protein;                                                      C-terminal Zn finger domain
                                                                 Uncharacterized protein
Int. J. Mol. Sci. 2022, 23, 13658                                                                                                                                                17 of 22




                                       Table 5. Cont.

                                    Identifier                    Protein Annotations                Length (AA)   Protein Families (COGs):          Protein Families Function
                                                                                                                                                  Negative regulation of ceramide
       P2.3-21             GRMZM2G064898_P01                     ORMDL family protein                    162              COG5081
                                                                                                                                                       biosynthetic process
                                                          Uncharacterized protein loc100278112;
       P2.3-22             GRMZM2G319454_P01                                                             170              KOG4831                        Unnamed protein
                                                               Transmembrane-like protein
                                                              Uncharacterized loc100273730;                                                       Negative regulation of ceramide
       P2.3-23             GRMZM2G044720_P01                                                             162              COG5081
                                                                 ORMDL family protein                                                                  biosynthetic process
                                                               DNAJ heat shock N-terminal
                                                                domain-containing protein;                                                      DnaJ-class molecular chaperone with
       P2.3-24             GRMZM2G125072_P01                                                             304              COG0484
                                                                    3Fe-4S ferredoxin;                                                             C-terminal Zn finger domain
                                                                 Uncharacterized protein
                                                           Gbf-interacting protein 1 isoform x1;
       P2.3-25             GRMZM2G045854_P01              Putative DUF1296 domain-containing             540             NOG236453            Protein of unknown function (DUF1296)
                                                                      family protein
       P2.3-26             GRMZM2G478664_P01                     Annotation not available               1058              COG0060                   Isoleucyl-tRNA synthetase
                                                           Sorbitol dehydrogenase homolog 1;                                                    Threonine dehydrogenase or related
       P2.3-27             GRMZM2G175423_P01                                                             366              COG1063
                                                                 Sorbitol dehydrogenase                                                           Zn-dependent dehydrogenase
       P2.3-28             GRMZM2G702253_P02                     Annotation not available                304              COG0345                Pyrroline-5-carboxylate reductase
                                                        Pathogenesis-related genes transcriptional
       P2.3-29             GRMZM2G474326_P01                          activator pti5;                    229             NOG243370             Ethylene-activated signaling pathway
                                                        Ethylene-responsive transcription factor 2
                                                        Abc transporter c family mrp4 precursor;
                                                                                                                                              The ABC-type multidrug transport system,
       P2.3-30             GRMZM5G820122_P01             ABC transporter that may affect phytic         1510              COG1132
                                                                                                                                                  ATPase and permease component
                                                        acid transport and compartmentalization.
Int. J. Mol. Sci. 2022, 23, 13658                                                                                           18 of 22




                                         In addition, botanists have shown that the protein expression of ABC transporter
                                    protein changes in plant leaves with the impact of temperature [25]. These findings offer
                                    additional proof that OSCA is involved in many physiological activities in plants.
                                         Finally, OSCA might be temperature-related in a way that we do not yet know. Our
                                    work demonstrates the dependence between OSCA and temperature, and provides evi-
                                    dence to further investigate the temperature mechanism of plants.

                                    3. Discussion
                                          Ion channels are essential for cell survival, and cells use them for nutrient uptake,
                                    sensing environmental stimuli, and signaling [26]. Many different stimulus-sensing pro-
                                    teins exist in plants to sense different stress signals; the functional proteins of the early
                                    signaling phase of plant stress signal transduction are unknown. However, it has been
                                    demonstrated that low temperature, drought, and high salt stress can induce transient
                                    calcium inward flow in the cytoplasm. Thus, it can be inferred that the ion channels causing
                                    inward calcium flow are likely to act as a class of receptors for stress signals [27]. The
                                    Sodium Proton Antiporter (NHX) temperature of Arabidopsis has previously been found
                                    to affect the translation of its gene family, while predictive analysis found that SbNHX is
                                    closely linked to the calcineurin B-like proteins (CBL)-interacting protein kinases (CIPK)
                                    pathway [28]. This further suggests that calcium proteins may be temperature-dependent.
                                    Calcium transporter protein ANN1 was found to be involved in plant cold-induced re-
                                    sponses in Arabidopsis [29], suggesting that calcium transporter proteins can be directly
                                    involved in plant stress responses due to temperature changes. We found differences in the
                                    expression levels of the twelve ZmOSCA genes under high and low temperature conditions,
                                    something that has never previously been suggested.
                                          In addition to the above, there are many transcription factors associated with osmoreg-
                                    ulation in plants, such as DREB, MYC/MYB, and WRKY [30]. As osmoregulation-related
                                    transcription factors, they have been found to play a role in osmosis and to be inextri-
                                    cably linked to other metabolic pathways in plants. DREB2A regulates plant heat stress
                                    response by regulating the cascade response of the heat stress transcription factor HsfA [31].
                                    MYB/MYC, the largest family of transcription factors in plants [32], can alter the regulation
                                    of stomatal movement and is involved in physiological regulation related to plant sensi-
                                    bility [33]. WRKY has been shown to have an important relationship with the response
                                    to high-temperature stress. WRKY factors can bind to the W-box cis-acting elements of
                                    target gene promoters, thereby regulating the expression of multiple target genes and
                                    participating in multiple signaling pathways in plants [34]. While OSCAs are found to be
                                    associated with osmosis, they should not act only in osmoregulation, as with the factors
                                    mentioned above. Three OsOSCAs are associated with circadian regulation, and are related
                                    to transpiration regulation [20]. The SlOSCA gene regulates light responses and contains
                                    elements involved in the light pathway [35]. Based on these results, the role of OSCAs
                                    stretches far beyond what has been found to date. OSCAs encode genes that may play a
                                    decisive role in other processes of plant growth and development, and these questions
                                    require further investigation. In the case of heat stress, changes in other factors provide us
                                    with a new viewpoint about OSCAs; based on existing knowledge of OSCAs, we assume
                                    that they have a high probability of reacting to thermal stress.
                                          The evolutionary tree we constructed based on the proteins tells us that OSCAs can
                                    be classified into four categories, which is consistent with the evolutionary analysis of
                                    Arabidopsis, rice, poplar, and grapevine [16]. The OSCA gene family of the typical monocot
                                    plant rice and the dicotyledonous plant Arabidopsis is present in each category, showing
                                    that the OSCA gene family has the potential to diversify before plant differentiation. We
                                    found that the second subfamily of ZmOSCA was expressed in a similar trend in cold
                                    stress, which is similar to the results of the promoter analysis in [17]. Thus, we believe that
                                    OSCA subfamily II may be a group with less alteration in the biological evolution of the
Int. J. Mol. Sci. 2022, 23, 13658                                                                                        19 of 22




                                    OSCA gene family in terms of their protein reaction to temperature stress. This may play a
                                    decisive role in the investigation of species genesis.
                                          Through predictive analysis of ZmOSCA protein interactions, we found that
                                    ZmOSCA2.3 is closely associated with catabolic processes such as amino acids, cellular ni-
                                    trogen compounds, and organic cyclic compounds, suggesting that ZmOSCA2.3 is involved
                                    in many metabolic activities. This echoes the OSCA2.3 related study of Thor. et al. [36].
                                    These data strengthen the credibility of our protein interactions prediction analysis. At
                                    the same time, we discovered that ZmOSCA involves enzymatic reactions in a variety of
                                    organisms. The temperature–enzyme relationship gives us more confidence that ZmOSCA
                                    is a protein involved in temperature regulation. In fact, several in vivo transporters have
                                    a co-operative relationship with ZmOSCA2.2, and many of these are transmembrane-
                                    associated protein transporters. The effect of temperature on the association between plant
                                    plasma membrane transport and protein transporters has been well documented in plant
                                    physiology. In addition, the properties of protein denaturation at high temperatures allows
                                    us to be more certain that ZmOSCA is highly temperature modulation-related.
                                          At present, we have not explored the specific targets of the OSCA signaling pathway
                                    under temperature stress via other experiments, and this is the direction we are considering
                                    following in continuing our in-depth study in the future. In our protein interactions
                                    prediction, we found that OSCA is closely linked to other metabolic pathways, and in the
                                    future we will consider validating the role of OSCA within other metabolic pathways in
                                    order to explore and discuss more functions that OSCA may have. This protein could be
                                    interchangeable with yield-related influences in experiments to help solve the problem of
                                    world hunger.

                                    4. Materials and Methods
                                    4.1. Bioinformatics Analysis
                                    4.1.1. Gene Screening and Identification Analysis
                                         Identified Arabidopsis OSCA gene family gene IDs were downloaded from the National
                                    Center for Biotechnology Information (https://www.ncbi.nlm.nih.gov/, revised 17 January
                                    2022), and candidate genes were identified by tBlast N searches in their maize genome
                                    library. The ZmOSCA gene family members were identified using the Pfam and SMART
                                    databases and validated by the DUF221 structural domain. When multiple transcripts
                                    existed at the same gene locus, the deduced amino acid sequence of the longest transcript
                                    was selected for comparison. Prediction of genomic exons and introns was carried out using
                                    Gene Structure Display Server (GSDS, http://gsds.cbi.pku.edu.cn/, revised 26 January
                                    2022).

                                    4.1.2. Construction of Evolutionary Tree and Analysis of Gene Structure
                                         The full-length proteins were analyzed using MEGA5.0 software, and phylogenetic
                                    trees were constructed by the Neighbor Joining (NJ) method [37]. A total of 5000 bootstrap
                                    replicates were performed in each analysis to obtain confidential support. Gene structures
                                    of OSCAs were identified using the Gene Structure Display Server. Multiple sequence
                                    alignments of OSCAs were performed using DNAMAN, and the transmembrane region of
                                    the DUF221 conserved region was predicted using TMHMM.

                                    4.1.3. Analysis of Protein Secondary Structure Prediction in Maize OSCA Family
                                         Based on the principle of homology prediction, the protein secondary structure predic-
                                    tion website SOPMA (https://npsa-prabi.ibcp.fr/cgi-bin/npsa_automat.pl?page=/NPSA/
                                    npsa_sopma.html, revised 2 March 2022) was used to predict the secondary structure
                                    of OSCA in maize based on the relevant protein database. The secondary structure of
                                    each member of the OSCA protein family was predicted based on the relevant protein
                                    database, and the results were checked statistically. The TM domains in OSCAs were anno-
                                    tated according to TMHMM Server v. 2.0 predictions (http://www.cbs.dtu.dk/services/
                                    TMHMM/, revised 8 March 2022).
Int. J. Mol. Sci. 2022, 23, 13658                                                                                                    20 of 22




                                    4.1.4. Predictive Analysis of Protein Interactions
                                         Using the STRING website (https://string-db.org/, revised 18 March 2022), the mini-
                                    mum required interaction score was manually set to 0.4 and the first interacting protein
                                    shell parameter was set to 30 to construct the protein interaction prediction analysis data,
                                    then edited with Cytoscape software and checked with protein information from the Na-
                                    tional Center for Biotechnology Information (https://www.ncbi.nlm.nih.gov/, revised 18
                                    March 2022).

                                    4.1.5. Prediction of Recognition Sites for Calcium Ions
                                         The OSCA protein structure was located and downloaded from the PDB database
                                    (https://www.rcsb.org/, accessed on 22 March 2022); using the SWISS-MODEL website
                                    (https://swissmodel.expasy.org/, accessed 24 March 2022), the remaining several OSCA
                                    structures that were not yet measured were constructed homologously using AtOSCA1.1
                                    (ID: 6JPF) as a template [38]. The proteins were then processed using Auto Dock 4.0 [39]
                                    for mapping and analysis based on the system-defined highly probable docking sites.

                                    4.2. Plant Materials and Growth Conditions
                                          Maize plants (B73) were planted in a growth chamber at Jilin University (Changchun,
                                    China). Plants were surface sterilized in a 10% (v/v) H2 O2 solution for 20 min and ger-
                                    minated on sand for 3 days in a growth chamber at 4 ◦ C with a 10 h/14 h light/dark
                                    cycle and 70–80% relative humidity. The seeds were transferred into improved Hoagland
                                    solution at 28/25 ◦ C (day/night) with a photoperiod of 16/8 h (day/night) and relative
                                    humidity of 50–70%; the nutrient solution was replaced regularly with a new one every day.
                                    When10 days old, maize seedlings were placed in a nutrient solution containing 10% PEG
                                    for drought stress treatment; seedlings were treated with a low temperature of 4 ◦ C and
                                    a high temperature of 40 ◦ C for 24 h in the light incubator and taken at 0 h, 1 h, 6 h, 12 h,
                                    and 24 h after treatment. Maize seedlings were treated with 250 mmol/L NaCl solution for
                                    salt stress, and the seedlings were taken at 0 h, 1 h, and 6 h, after treatment. The nutrient
                                    solution was renewed daily.

                                    4.3. RNA Extraction and Quantitative qRT-PCR Analysis
                                          Extraction of maize RNA was carried out by the TRIzol method. Reverse transcription
                                    kits from Invitrogen were then used to synthesize the first strand cDNA. cDNA template
                                    was diluted and used and real-time fluorescence quantitative PCR was performed using
                                    the SYBR GREEN method as provided by the company’s QRT kit. Finally, the relative
                                    amount of gene expression was calculated using the 2−∆∆Ct method [40]. For detailed
                                    primer sequences, see Table S1

                                    5. Conclusions
                                         We found evidence for the involvement of ZmOSCAs in temperature correlation, along
                                    with an exhaustive analysis of the ZmOSCA family. We found that the OSCA gene family
                                    of maize is characterized by tissue-specific expression, which is highly consistent with
                                    studies of OSCA in rice [20]. This is the first discovery in maize, and represents a further
                                    exploration of the molecular mechanisms underlying the interactions of ZmOSCA under
                                    adversity stresses. Further investigation of the regulatory mechanism of ZmOSCA2.2
                                    and ZmOSCA2.3 in the cold/heat stress response can contribute to the engineering of
                                    cold/heat-tolerant crops via element-specific genome editing.

                                    Supplementary Materials: The following supporting information can be downloaded at: https:
                                    //www.mdpi.com/article/10.3390/ijms232113658/s1.
                                    Author Contributions: Writing the manuscript, Draft Preparation, J.C., Y.Z. and W.S.; Writing—
                                    Review and Editing, Supervision, N.C.; Supervision, B.L. and Z.W.; Methodology, C.J. and M.Z.;
                                    Software, Y.L. and J.Y.; Validation, J.Q. and J.C.; Formal Analysis, Y.L.; Investigation Y.L., S.C., L.H.
Int. J. Mol. Sci. 2022, 23, 13658                                                                                                    21 of 22




                                    and B.L.; Resources, N.C. All authors contributed to the manuscript preparation. All authors have
                                    read and agreed to the published version of the manuscript.
                                    Funding: This work is supported by Jilin Provincial Science and Technology Department Program
                                    (2020201124JC and 20220404006NC) via the project of technological guidance from the college stu-
                                    dents’ innovative entrepreneurial training plan (202110183343).
                                    Institutional Review Board Statement: Not applicable.
                                    Informed Consent Statement: Not applicable.
                                    Data Availability Statement: The original contributions presented in this study are included in the
                                    article.
                                    Acknowledgments: Thanks to Qing Li and Yijie Wang for helping with the experiment.
                                    Conflicts of Interest: No conflict of interest is reported by the authors.

References
1.    Gong, F.P.; Yang, L.; Tai, F.J.; Hu, X.L.; Wang, W. “Omics” of Maize Stress Response for Sustainable Food Production: Opportunities
      and Challenges. Omics A J. Integr. Biol. 2014, 18, 714–732. [CrossRef] [PubMed]
2.    He, Y.; Hu, X.K.; Xu, W.; Fang, J.Y.; Shi, P.J. Increased probability and severity of compound dry and hot growing seasons over
      world’s major croplands. Sci. Total Environ. 2022, 824, 153885. [CrossRef] [PubMed]
3.    Krasensky, J.; Jonak, C. Drought, salt, and temperature stress-induced metabolic rearrangements and regulatory networks. J. Exp.
      Bot. 2012, 63, 1593–1608. [CrossRef] [PubMed]
4.    de Zelicourt, A.; Colcombet, J.; Hirt, H. The Role of MAPK Modules and ABA during Abiotic Stress Signaling. Trends Plant Sci.
      2016, 21, 677–685. [CrossRef]
5.    Zhang, L.L.; Zhang, Z.; Chen, Y.; Wei, X.; Song, X. Exposure, vulnerability, and adaptation of major maize-growing areas to
      extreme temperature. Nat. Hazards 2018, 91, 1257–1272. [CrossRef]
6.    Feng, S.F.; Hao, Z.C.; Zhang, X.; Hao, F.H. Probabilistic evaluation of the impact of compound dry-hot events on global maize
      yields. Sci. Total Environ. 2019, 689, 1228–1234. [CrossRef]
7.    Li, E.; Zhao, J.; Pullens, J.W.M.; Yang, X.G. The compound effects of drought and high temperature stresses will be the main
      constraints on maize yield in Northeast China. Sci. Total Environ. 2022, 812, 152461. [CrossRef]
8.    Lobell, D.B.; Gourdji, S.M. The Influence of Climate Change on Global Crop Productivity. Plant Physiol. 2012, 160, 1686–1697.
      [CrossRef]
9.    Mao, J.H.; Yu, Y.T.; Yang, J.; Li, G.K.; Li, C.Y.; Qi, X.T.; Wen, T.X.; Hu, J.G. Comparative transcriptome analysis of sweet corn
      seedlings under low-temperature stress. Crop J. 2017, 5, 396–406. [CrossRef]
10.   Zhu, J.K. Abiotic Stress Signaling and Responses in Plants. Cell 2016, 167, 313–324. [CrossRef]
11.   Steinhorst, L.; Kudla, J. Calcium—A central regulator of pollen germination and tube growth. Biochim. Biophys. Acta 2013, 1833,
      1573–1581. [CrossRef] [PubMed]
12.   Waters, M.T.; Langdale, J.A. The making of a chloroplast. EMBO J. 2009, 28, 2861–2873. [CrossRef] [PubMed]
13.   Hubbard, K.E.; Siegel, R.S.; Valerio, G.; Brandt, B.; Schroeder, J.I. Abscisic acid and CO2 signalling via calcium sensitivity priming
      in guard cells, new CDPK mutant phenotypes and a method for improved resolution of stomatal stimulus-response analyses.
      Ann. Bot. 2012, 109, 5–17. [CrossRef] [PubMed]
14.   Luan, S.; Kudla, J.; Rodriguez-Concepcion, M.; Yalovsky, S.; Gruissem, W. Calmodulins and calcineurin B-like proteins: Calcium
      sensors for specific signal response coupling in plants. Plant Cell 2002, 14, S389–S400. [CrossRef]
15.   Hepler, P.K. Calcium: A central regulator of plant growth and development. Plant Cell 2005, 17, 2142–2155. [CrossRef]
16.   Yuan, F.; Yang, H.M.; Xue, Y.; Kong, D.D.; Ye, R.; Li, C.J.; Zhang, J.Y.; Theprungsirikul, L.; Shrift, T.; Krichilsky, B.; et al. OSCA1
      mediates osmotic-stress-evoked Ca2+ increases vital for osmosensing in Arabidopsis. Nature 2014, 514, 367–378. [CrossRef]
17.   Cao, L.R.; Zhang, P.Y.; Lu, X.M.; Wang, G.R.; Wang, Z.H.; Zhang, Q.J.; Zhang, X.; Wei, X.; Mei, F.J.; Wei, L.; et al. Systematic
      Analysis of the Maize OSCA Genes Revealing ZmOSCA Family Members Involved in Osmotic Stress and ZmOSCA2.4 Confers
      Enhanced Drought Tolerance in Transgenic Arabidopsis. Int. J. Mol. Sci. 2020, 21, 351. [CrossRef]
18.   Wu, J.X.; Chen, L. Recent Progress on The Studies of OSCA/TMEM63 Family Ion Channels. Prog. Biochem. Biophys. 2020, 47,
      123–130.
19.   Hou, C.C.; Tian, W.; Kleist, T.; He, K.; Garcia, V.; Bai, F.L.; Hao, Y.L.; Luan, S.; Li, L.G. DUF221 proteins are a family of
      osmosensitive calcium-permeable cation channels conserved across eukaryotes. Cell Res. 2014, 24, 632–635. [CrossRef]
20.   Li, Y.S.; Yuan, F.; Wen, Z.H.; Li, Y.H.; Wang, F.; Zhu, T.; Zhuo, W.Q.; Jin, X.; Wang, Y.D.; Zhao, H.P.; et al. Genome-wide survey
      and expression analysis of the OSCA gene family in rice. Bmc Plant Biol. 2015, 15, 261. [CrossRef]
21.   Lv, G.D. Cloning, Marker Development and Functional Analysis of the Wheat TaOSCA1.4 Gene. Master’s Thesis, Shandong
      Agricultural University, Taian, China, 2015.
22.   Lee, H.W.; Park, J.H.; Park, M.Y.; Kim, J. GIP1 may act as a coactivator that enhances transcriptional activity of LBD18 in
      Arabidopsis. J. Plant Physiol. 2014, 171, 14–18. [CrossRef] [PubMed]
Int. J. Mol. Sci. 2022, 23, 13658                                                                                                      22 of 22




23.   Ogawa, T.; Tanaka, A.; Kawamoto, J.; Kurihara, T. Purification and characterization of 1-acyl-sn-glycerol-3-phosphate acyltrans-
      ferase with a substrate preference for polyunsaturated fatty acyl donors from the eicosapentaenoic acid-producing bacterium
      Shewanella livingstonensis Ac10. J. Biochem. 2018, 164, 33–39. [CrossRef] [PubMed]
24.   Fernandez, P.; Diaz, A.R.; Re, M.F.; Porrini, L.; de Mendoza, D.; Albanesi, D.; Mansilla, M.C. Identification of Novel Thermosensors
      in Gram-Positive Pathogens. Front. Mol. Biosci. 2020, 7, 592747. [CrossRef] [PubMed]
25.   Sang-Hoon, L.; Jun, C.; KimKi, Y.; Chung, J.; Soo, P.H.; Dong-Gi, L.; Ki-Won, L. Identification of temperature stress-induced
      differentially expressed genes of tall fescue leaves. Res. J. Biotechnol. 2015, 10, 99–101.
26.   Hou, C.C. Isolation, Identification and Preliminary Functional Analysis of Calcium Permeable Cation Channels Gated by
      Hyperosmotic Stress. Ph.D. Thesis, Capital Normal University, Beijing, China, 2014.
27.   Xiong, L.; Schumaker, K.S.; Zhu, J.-K. Cell Signaling during Cold, Drought, and Salt Stress. Plant Cell 2002, 14, S165–S183.
      [CrossRef]
28.   Kumari, P.H.; Kumar, S.A.; Ramesh, K.; Reddy, P.S.; Nagaraju, M.; Prakash, A.B.; Shah, T.; Henderson, A.; Srivastava, R.K.;
      Rajasheker, G.; et al. Genome-Wide Identification and Analysis of Arabidopsis Sodium Proton Antiporter (NHX) and Human
      Sodium Proton Exchanger (NHE) Homologs in Sorghum bicolor. Genes 2018, 9, 236. [CrossRef]
29.   Liu, Q.B.; Ding, Y.L.; Shi, Y.T.; Ma, L.; Wang, Y.; Song, C.P.; Wilkins, K.A.; Davies, J.M.; Knight, H.; Knight, M.R.; et al. The calcium
      transporter ANNEXIN1 mediates cold-induced calcium signaling and freezing tolerance in plants. EMBO J. 2021, 40, e104559.
      [CrossRef]
30.   Tang, Y.M.; Zhao, C.P.; Gao, S.Q.; Tian, I.Q.; Shan, F.H.; Wu, J.X. Advances in the study of drought-related genes in plants. J.
      Triticeae Crops 2009, 29, 166–173.
31.   Schramm, F.; Larkindale, J.; Kiehlmann, E.; Ganguli, A.; Englich, G.; Vierling, E.; von Koskull-Doering, P. A cascade of transcription
      factor DREB2A and heat stress transcription factor HsfA3 regulates the heat stress response of Arabidopsis. Plant J. 2008, 53,
      264–274. [CrossRef]
32.   Yang, Y.T.; Yu, Y.; Gao, X.R.; Pi, E.X. Progress in the study of MYB-like transcription factors regulating the mechanism of plant
      stress tolerance. J. Hangzhou Norm. Univ. 2021, 20, 621–627.
33.   Jung, C.; Seo, J.S.; Han, S.W.; Koo, Y.J.; Kim, C.H.; Song, S.I.; Nahm, B.H.; Do Choi, Y.; Cheong, J.-J. Overexpression of AtMYB44
      enhances stomatal closure to confer abiotic stress tolerance in transgenic Arabidopsis. Plant Physiol. 2008, 146, 623–635. [CrossRef]
      [PubMed]
34.   Cheng, Z.; Luan, Y.; Meng, J.; Sun, J.; Tao, J.; Zhao, D. WRKY Transcription Factor Response to High-Temperature Stress. Plants
      2021, 10, 2211. [CrossRef] [PubMed]
35.   Zhang, K.W. Identification and Stress Response Analysis of the OSCA Gene Family of Calcium Channels in Tomato. Master’s
      Thesis, Shandong Agricultural University, Taian, China, 2019.
36.   Thor, K.; Jiang, S.S.; Michard, E.; George, J.; Scherzer, S.; Huang, S.G.; Dindas, J.; Derbyshire, P.; Leitao, N.; DeFalco, T.A.; et al.
      The calcium-permeable channel OSCA1.3 regulates plant stomatal immunity. Nature 2020, 585, 569–573. [CrossRef] [PubMed]
37.   Wu, Y.X.; Fang, C.M.; He, Y.Q. Distribution and clustering analysis of hydrophobic proteins in the genome of rice blast fungus.
      Mol. Plant Breed. 2009, 7, 978–984.
38.   Kiefer, F.; Arnold, K.; Kunzli, M.; Bordoli, L.; Schwede, T. The SWISS-MODEL Repository and associated resources. Nucleic Acids
      Res. 2009, 37, D387–D392. [CrossRef]
39.   Li, B.; Hou, L.; Song, C.; Wang, Z.; Xue, Q.; Li, Y.; Qin, J.; Cao, N.; Jia, C.; Zhang, Y.; et al. Biological function of calcium-sensing
      receptor (CAS) and its coupling calcium signaling in plants. Plant Physiol. Biochem. 2022, 180, 74–80. [CrossRef]
40.   Wang, Z.B.; Li, H.; Wei, Z.P.; Sun, H.R.; He, Y.; Gao, J.; Yang, Z.M.; You, J.F. Overexpression of UDP-glycosyltransferase genes
      enhanced aluminum tolerance through disrupting cell wall polysaccharide components in soybean. Plant Soil 2021, 469, 135–147.
      [CrossRef]
