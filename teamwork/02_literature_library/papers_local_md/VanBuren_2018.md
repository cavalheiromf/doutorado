# Extreme haplotype variation in the desiccation-tolerant clubmoss Selaginella lepidophylla

**Authors:** Robert VanBuren, Ching Man Wai, Shujun Ou, Jeremy Pardo, Doug Bryant, Ning Jiang, Todd C. Mockler, Patrick Edger, Todd P. Michael  
**Year:** 2018  
**Journal:** Nature Communications  
**Volume:** 9  
**Pages:** 13  
**DOI:** 10.1038/s41467-017-02546-5  

---

             ARTICLE
             DOI: 10.1038/s41467-017-02546-5                OPEN

             Extreme haplotype variation in the desiccation-
             tolerant clubmoss Selaginella lepidophylla
             Robert VanBuren            1,2,  Ching Man Wai1, Shujun Ou 1,3, Jeremy Pardo                             4,   Doug Bryant5, Ning Jiang1,3,
             Todd C. Mockler            5,   Patrick Edger1,3 & Todd P. Michael 6



             Plant genome size varies by four orders of magnitude, and most of this variation stems from
1234567890




             dynamic changes in repetitive DNA content. Here we report the small 109 Mb genome of
             Selaginella lepidophylla, a clubmoss with extreme desiccation tolerance. Single-molecule
             sequencing enables accurate haplotype assembly of a single heterozygous S. lepidophylla
             plant, revealing extensive structural variation. We observe numerous haplotype-speciﬁc
             deletions consisting of largely repetitive and heavily methylated sequences, with enrichment
             in young Gypsy LTR retrotransposons. Such elements are active but rapidly deleted, sug-
             gesting “bloat and purge” to maintain a small genome size. Unlike all other land plant
             lineages, Selaginella has no evidence of a whole-genome duplication event in its evolutionary
             history, but instead shows unique tandem gene duplication patterns reﬂecting adaptation to
             extreme drying. Gene expression changes during desiccation in S. lepidophylla mirror patterns
             observed across angiosperm resurrection plants.




             1 Department of Horticulture, Michigan State University, East Lansing, MI 48824, USA. 2 Plant Resilience Institute, Michigan State University, East Lansing,

             MI 48824, USA. 3 Ecology, Evolutionary Biology and Behavior, Michigan State University, East Lansing, MI 48824, USA. 4 Department of Plant Biology,
             Michigan State University, East Lansing, MI 48824, USA. 5 Donald Danforth Plant Science Center, St. Louis, MO 63132, USA. 6 J. Craig Venter Institute, La
             Jolla, CA 92037, USA. Correspondence and requests for materials should be addressed to R.V. (email: bobvanburen@gmail.com)
             or to T.P.M. (email: toddpmichael@gmail.com)

             NATURE COMMUNICATIONS | (2018)9:13                        | DOI: 10.1038/s41467-017-02546-5 | www.nature.com/naturecommunicationsnaturecommunications     1
ARTICLE                                                                            NATURE COMMUNICATIONS | DOI: 10.1038/s41467-017-02546-5




T
       he ability to survive periodic drying was essential for the           this variation enhances ﬁtness and serves as a reservoir for
       aquatic ancestors of terrestrial plants during their transi-          adaptive evolution. Heterozygosity is a major issue in plant
       tion from sea to land. These early protective mechanisms              genome assembly, and most heterozygous plant genomes are
are thought to be ancestral and conserved in most land plants1,              highly fragmented with collapsed haplotype regions11. S. lepido-
forming the basis of modern seed and pollen desiccation path-                phylla has an estimated genome size of 109 Mb based on kmer
ways2. A small group of plants have maintained this ancestral                frequency analyses, which is consistent with the small genomes
desiccation tolerance, surviving near complete anhydrobiosis                 observed across the genus9. Despite its compact size, the S. lepi-
(<10% relative water content) during prolonged drought events.               dophylla genome is highly heterozygous, with a bimodal dis-
Desiccation tolerance is widespread in non-seed plants such as               tribution of kmers corresponding to distinct heterozygous and
mosses, ferns, and lycophytes3, 4, but is uncommon in angios-                collapsed homozygous regions (Supplementary Fig. 1). Initial
perms. High-quality genomes for several angiosperm resurrection              sequencing attempts using an Illumina only approach yielded a
plants have shed light on the molecular basis of desiccation                 highly collapsed and fragmented assembly of 21,282 scaffolds,
tolerance2, 5, 6, but the sparse genomic resources for non-seed              totaling 54 Mb, with an N50 of 3 kb (Supplementary Table 1). To
plants has hindered progress toward understanding the origin of              overcome assembly issues related to heterozygosity, we generated
this trait.                                                                  175× coverage (19.3 Gb) of single-molecule real-time (SMRT)
   Here we report the small genome of Selaginella lepidophylla, a            sequences from PacBio with a ﬁltered subread N50 length of 18
lycophyte that can survive the loss of >95% cellular water for               kb (Supplementary Fig. 2). The long read lengths of PacBio
decades in a quiescent state. Selaginella are among the earliest             sequencing facilitate accurate separation and assembly of het-
diverging lineages of vascular plants, and extant species bear               erozygotic haplotypes12. Raw PacBio reads were error corrected
striking morphological similarities to fossils from the upper                and assembled using the Canu assembler13, which utilizes opti-
Carboniferous (333–350 Myr ago)7, 8. Genome size variation                   mized overlapping and assembly algorithms to avoid collapsing
within this ancient group is minimal and Selagienlla are the only            repetitive regions and haplotypes. The resulting contigs were
clade of land plants with no shared whole-genome duplication                 polished using the raw PacBio data with Quiver14, followed by a
event9. Detailed comparative genomics across angiosperms and                 second round of polishing with Pilon15 using the high-coverage
with the S. moellendorfﬁi genome10 shed light the origin of                  Illumina data.
desiccation tolerance and unique properties of Selaginella.                     The ﬁnal S. lepidophylla assembly spans 122 Mb across 1149
                                                                             contigs with an N50 length of 163 kb (Supplementary Table 2).
                                                                             These assembly metrics are similar to the S. moellendorfﬁi
Results                                                                      genome (contig N50 length = 120 kb), which was sequenced using
Haplotype-level genome assembly and annotation. Extensive                    a reiterative Sanger approach10. Our assembly includes 15 of the
within genome heterozygosity exists for most plant species, and              20 terminal telomere tracks (2n = 20) and 128 rRNA arrays,




                                                                      Heterozygous bubble




Fig. 1 Genome assembly graph of S. lepidophylla. Each line (node) represents a contig with connections (edges) representing ambiguities in the graph
structure. A subset of the graph showing heterozygous bubbles is enlarged. Contig color is randomly assigned

2       NATURE COMMUNICATIONS | (2018)9:13                       | DOI: 10.1038/s41467-017-02546-5 | www.nature.com/naturecommunicationsnaturecommunications
NATURE COMMUNICATIONS | DOI: 10.1038/s41467-017-02546-5                                                                                                         ARTICLE

                     a                                                                                b                                  Copia LTR
                                                                                                                   400
                                     Contig_37 69–157 kb                                                                                 Gypsy LTR

                                                                                                                   300




                                                                                                       LTR count
                                                                                                                   200


                                                                                                                   100
                                          Contig_87 0–86 kb
                                                                                                                    0
                                                                                                                         0      1           2          3 >3.5
                     c                                                           d
                                    1.0                                                                                         Insertion time (MYA)

                                                                                     Contig_117 45–211 kb
                                   0.75
                      Proportion




                                                                                                                             Gypsy LTR
                                    0.5


                                   0.25


                                     0                                                        Contig_142 21–130 kb
                                           Genes LTR Genes LTR
                                               Insertion      Collinear

Fig. 2 Extensive haplotype-speciﬁc LTR retrotransposon accumulation and deletion. a Typical micro-collinearity between two S. lepidophylla haplotypes. b
Estimated insertions times of intact Copia and Gypsy LTR retrotransposons. c Composition of haplotype speciﬁc and paired collinear regions. The proportion
of genes and LTRs in the 105 manually curated insertions (left) and ﬂanking collinear regions (right) are plotted. d Micro-collinearity between two
haplotypes showing a large 57 kb deletion in contig 142. Green and blue bars delineate gene orientation. Predicted LTR elements are depicted in orange and
the three complete Gypsy LTRs are denoted by arrows. The three complete Gypsy LTRs have insertion times of <0.1 Ma

which are typically unassembled in most next-generation                                          retrotransposons (LTR-RTs), including 572 Gypsy and 17 Copia
sequencing (NGS) based genomes11. The S. lepidophylla assembly                                   elements (Supplementary Table 5). The majority of intact LTRs
graph is highly complex with numerous interconnected edges,                                      are relatively young, with average insertion times of 0.1 and 0.4
reﬂecting bubbles and ambiguities caused by heterozygous                                         MYA for Copia and Gypsy elements, respectively, and most intact
regions (Fig. 1). The long PacBio reads assembled 930 haplotype                                  LTR elements are younger than 0.5 Ma (Fig. 2b and Supple-
blocks spanning 33.7 Mb of separated haplotype sequences                                         mentary Fig. 5). The proportion of young LTR elements is higher
(Methods section; Fig. 2a; Supplementary Fig. 3). Other haplotype                                in S. lepidophylla than other high-quality plant genomes (Sup-
aware assemblers were tested but Canu provided the best                                          plementary Figure 5). The recent LTR ampliﬁcation suggests
separation of haplotype blocks as well as the best contiguity.                                   most elements have been active recently in Selaginella but they
   We annotated 27,204 genes across a deduced 89 Mb                                              are rapidly fragmented and deleted. S. lepidophylla has a much
haploid assembly, considerably more than S. moellendorfﬁi                                        higher ratio (4.06, Wilcoxon rank-sum, P < 0.05, same statistical
(22,285 genes)10. The majority (96%) of core eukaryotic                                          test hereafter unless speciﬁed) of solo-intact LTR elements
BUSCOs16 were identiﬁed in the gene set, supporting the                                          comparing to the genomes of rice and Arabidopsis (2.71 and 1.80,
completeness of the genome assembly and quality of the                                           respectively) (Supplementary Fig. 6), indicating more effective
annotation (Supplementary Table 3). Roughly 45% of genes                                         removal of LTR-RTs via unequal homologous recombination.
(11,847) are found in duplicated pairs across the full 122 Mb                                    Moreover, the average age of LTR families in S. lepidophylla is
assembly with an average protein homology of 99.1%. Gene                                         much younger (0.37 MY vs. 0.92 and 0.94 MY, respectively; P <
density in S. lepidophylla is 4.0 kb per gene, which is higher than                              0.05) under the mutation rate of μ = 1.3 × 10–8 (per bp per year),
S. moellendorfﬁ10 and Arabidopsis17, but lower than the smallest                                 suggesting rapid removal of LTR elements. The intensive and
sequenced plant genome (82 Mb) of Utricularia gibba18.                                           rapid removal of LTR-RTs is likely one of the causes of haplotype
                                                                                                 variation and enrichment of LTR-RTs (Fig. 2).
                                                                                                    Haplotype blocks within the S. lepidophylla genome are largely
Genome evolution and haplotype-speciﬁc structural variation.                                     collinear, with conserved gene content and 98.2% sequence
Genome size varies by four orders of magnitude across land                                       homology (Fig. 2a; Supplementary Fig. 3). However, since our
plants, ranging from 60 Mb in the carnivorous Genlisea to                                        analysis is based on both the number of contiguous protein and
152,000 Mb in Paris japonica. Lycophytes have a narrow variation                                 sequence homology, it is possible that we have missed large highly
in genome size compared to angiosperms19, and Selaginella sizes                                  diverged haplotype blocks. A detailed comparison uncovered 104
range from 90 to 182 Mb9. Rapid changes in genome size are                                       large-scale haplotype-speciﬁc insertions or deletions (indels)
driven by bursts of long terminal repeat (LTR) retrotransposon                                   across the genome. These high-conﬁdence indels collectively
proliferation followed by aggressive deletion through unequal                                    span 2.5 Mb among 13.5 Mb of collinear sequences (18.5%) with
homologous recombination and double-strand break repair20.                                       individual sizes ranging from 4.8 kb to 85 kb with an average size
LTR elements are distributed non-randomly across the genome                                      of 24 kb (Supplementary Table 6). This is likely an under-
with Gypsy-like elements predominantly found in gene poor and                                    estimation as separate haplotypes were assembled for 35% of the
repeat rich blocks while Copia-like elements are dispersed among                                 genome and only high-conﬁdence collinear regions spanning
genes (Supplementary Table 4). Most of the LTR elements are                                      >75 kb were surveyed. Haplotype-speciﬁc regions are largely
clustered in a relatively small number of LTR families (Supple-                                  repetitive with 58% of bases consisting of LTR retrotransposons
mentary Figure 4). We identiﬁed 744 full-length LTR                                              and only 9% genes (Fig. 2c). Flanking collinear regions show the

NATURE COMMUNICATIONS | (2018)9:13                                        | DOI: 10.1038/s41467-017-02546-5 | www.nature.com/naturecommunicationsnaturecommunications   3
ARTICLE                                                                                                 NATURE COMMUNICATIONS | DOI: 10.1038/s41467-017-02546-5



                        a                                                                  b
                                                8             Genes                        70                Intact LTR




                        Methylation level (%)
                                                6                                          50

                                                                                CHH
                                                4
                                                                                CHG        30
                                                                                                                                 CHH
                                                                                CpG
                                                2                                                                                CHG
                                                                                           10                                    CpG


                                                –1 kb   TSS             TTS   +1 kb          –1 kb     5′                 3′   +1 kb

                        c
                                 0                      0.2       0.4         0.6          0.8         1.0          1.2         1.4 Mb


                                                                                                                                                     Gypsy LTR

                                                                                                                                                     Copia LTR

                                                                                                                                                     Genes (exons)



                                                                                                                                        Genes (exons)
                                                                                                                                        LTR




                                                                                                                                       Methylation
                                                                                                                                                     CHG
                                                                                                                                                     CpG
                                                                                                                                                     CHH

Fig. 3 Global methylation patterns in the S. lepidophylla genome. a S. lepidophylla lacks gene body methylation. Levels of CHH (green), CHG (blue) and CpG
(red) methylation are plotted in the upstream (transcriptional start site; TSS), downstream (transcriptional termination site (TTS), and body of genes. b
Intact LTR retrotransposons are highly methylated with decreasing levels at the 5′- and 3′-ﬂanking regions. c Methylation levels are highly variable across
the genome with strong correlation of LTR retrotransposon density. Top, genome landscape of genomic features across Contig 1. Bottom, heatmap of
genomic features and methylation levels, where blue indicates low abundance and red signiﬁes high abundance

opposite trend, with 86% genic and only 11% LTR retro-                                            experienced a recent whole-genome duplication event, contrast-
transposon sequences. We annotated 335 protein-coding genes in                                    ing patterns observed in all other land plants10, 25. S. lepidophylla
the gene poor, haplotype-speciﬁc regions, but most (74%; 248                                      and S. moellendorfﬁi have maintained a surprising degree of
genes) have little to no detectable expression (TPM <0.5). Young                                  collinearity with 36% (7849) of S. moellendorfﬁ genes showing
LTR retrotransposons (insertion times <0.1 Ma) are over-                                          conserved order in S. lepidophylla. Genic regions are generally
represented in haplotype-speciﬁc regions, supporting a recent                                     more compact in S. lepidophylla, correlating with the higher TE
origin of these indels (Fig. 2d; P < 0.01).                                                       content (37.5%) in S. moellendorfﬁi (Supplementary Fig. 7). By
   DNA methylation is associated with suppressing repetitive                                      contrast, only ~ 15% of rice and core eudicot genes are colli-
element proliferation and larger, repeat-dense plant genomes                                      near26, reﬂecting the role of WGD events in shaping gene order
tend to have higher levels of methylation21. We surveyed                                          and genome architecture. In the absence of WGD, any new traits
genome-wide DNA methylation in S. lepidophylla for patterns                                       and adaptations associated with duplicate genes in Selaginella
related to repetitive element silencing. Similar to other non-seed                                must arise through local or segmental gene duplications27. S.
vascular plants22, 23, S. lepidophylla lacks evidence of any gene                                 moellendorfﬁi has signiﬁcantly more tandem gene duplications
body methylation (Fig. 3a). In contrast, intact LTR retro-                                        (TD) than S. lepidophylla with 6693 compared to 4170, but both
transposons have high levels of CpG and CHG methylation with                                      share similar enrichment pattern (Supplementary Tables 7–10).
comparatively little CHH methylation (Fig. 3b). Methylation is                                    TDs in Selaginella are enriched in molecular function GO terms
highest in the body of LTR retrotransposons with levels dropping                                  related to kinase activity, ion and other small molecule binding
at the 5′- and 3′-ﬂanking regions. Gene rich regions of the S.                                    among others (Supplementary Tables 7 and 9). Few TDs were
lepidophylla genome are highly compact with an average of 1.1 kb                                  annotated as transcription factors or highly connected metabolic
intergenic sequences with interspersed, repeat-dense blocks                                       genes, which is consistent with expectations under the gene bal-
(Fig. 3c). This creates large tracks in the genome that are                                       ance hypothesis28, 29. Both Selaginella species have overlapping
essentially devoid of methylation ﬂanked by densely methylated,                                   KEGG pathway enrichments across TDs including phenylpro-
likely heterochromatic regions.                                                                   panoid, cutin, and secondary metabolite metabolism (Supple-
                                                                                                  mentary Tables 8 and 10). S. lepidophylla has TDs enriched in
                                                                                                  phagosome pathways, which may be related to controlled
Comparative genomics across Selaginella and angiosperms.                                          autophagy during desiccation30.
Selaginella arose in the early Carboniferous period 333–350                                          Lycophytes are sister to all other vascular plants including
MYA8, and the ancestors of S. lepidophylla and S. moellendorfﬁi                                   angiosperms, the most diverse extant plant group on the planet.
diverged about 250 MYA9, well before the radiance of modern                                       We surveyed changes in orthogroup composition across angios-
angiosperms24. Despite this separation, both lineages have                                        perms and the two Selaginella species to identify patterns
maintained a similar genome size (~ 100 Mb) and neither has                                       associated with WGD and life history traits. We identiﬁed 5891

4        NATURE COMMUNICATIONS | (2018)9:13                                           | DOI: 10.1038/s41467-017-02546-5 | www.nature.com/naturecommunicationsnaturecommunications
NATURE COMMUNICATIONS | DOI: 10.1038/s41467-017-02546-5                                                                                                                   ARTICLE

                      a




                               5 cm


                                                  0h                 1h                      6h                                     24 h              24 h (dehydrated)




                                                                                                                                                     120
                      b                                                                                             c




                                                                                                                                                     24

                                                                                                                                                     24
                                                                                                                                                     0
                                                                                                                                                     1
                                                                                                                                                     6
                                                                          Cluster 14




                                                                                                                S. moellendorffii
                                                        Cluster 10                           Cluster 16                                Sle_014211

                                                                                                                                       Sle_014207

                                                  5
                      Median centered Log2 TPM




                                                                                                                                       Sle_014212

                                                                                                                                       Sle_014210

                                                                                                                                       Sle_014209
                                                  0                                                                                    Sle_014206

                                                                                                                                       Sle_014203


                                                 –5                                                                                    Sle_014204

                                                                                                                                       Sle_002382
                                                                                                                                                              Log2 TPM
                                                                                                                                       Sle_015016
                                                         Cluster 5        Cluster 30         Cluster 34
                                                                                                                                       Sle_015015                   12
                                                  5                                                                                    Sle_02367.1                  10
                                                                                                                                       Sle_02367.3                  8
                                                                                                                                       Sle_02367.2                  6
                                                  0                                                                                    Sle_015009                   4
                                                                                                                                       Sle_007899

                                                                                                                                       Sle_010758
                                                 –5                                                                                    Sle_014588
                                                         0h
                                                         1h
                                                         6h
                                                        24 h
                                                       120 h
                                                      de24 h
                                                                        0h
                                                                        1h
                                                                        6h
                                                                       24 h
                                                                      120 h
                                                                     de24 h
                                                                                          0h
                                                                                          1h
                                                                                          6h
                                                                                         24 h
                                                                                        120 h
                                                                                       de24 h
                                                                                                                                       Sle_007329

                                                                                                                                       Sle_005932

                                                                                                                                       Sle_007889

                                                                                                                                       Sle_003987

                                                                                                                                       Sle_009563
                                                                      Timepoint                                                        Sle_001027




Fig. 4 Genomic features of the rehydration and desiccation processes. a Overview of sampling for the rehydration and desiccation time course. Samples
were taken from plants that were desiccated for 3 years (0), 1, 6, and 24 h post rehydration (recovery), 120 h post rehydration (fully recovered), and after a
24 h dehydration (de24 h). b Scaled transcript expression proﬁles (in transcripts per million, TPM) of representative gene co-expression clusters with
decreased (10, 16, 34) and increased expression (5, 14, 34) during rehydration. c Heatmap of log2 transformed early light-induced protein (ELIP)
expression with the two arrays of tandem duplicated genes in S. lepidophylla orthologous to the only ELIP in to S. moellendorfﬁi highlighted on the left


orthogroups with representatives from every species and 69                                                expression in desiccated leaf tissue, implicating strong protective
orthogroups with expansion in angiosperms (Supplementary                                                  mechanisms to preserve the mRNA pool.
Table 11). Angiosperm-dominated orthogroups have diverse GO                                                  We performed gene-co-expression analysis across the rehydra-
terms and enriched KEGG pathways for alkaloid biosynthesis,                                               tion and subsequent dehydration RNAseq timecourse data. The
proteolysis, and plant-pathogen interactions (Supplementary                                               38 co-expression clusters fall under the following three general
Tables 12 and 13). The angiosperm biased orthogroups are more                                             patterns with (1) high expression in desiccated tissues followed by
highly connected than expected by chance (~ 2.7 edges per gene;                                           decreases during rehydration, (2) increased expression during
P ≤ 10−20, Fisher’s exact test), ﬁtting expectations for gene                                             rehydration, and (3) steady expression across all samples (Fig. 4b,
duplicates retained from WGD28. The 55 Selaginella-biased                                                 Supplementary Fig. 8). Transcript levels are relatively consistent
orthogroups have GO enrichment in vesicle related processes                                               across the 0, 1, and 6 h post-rehydration time-points, with only
and KEGG pathway enrichment in phenylpropanoid biosynthesis                                               123 and 567 differentially expressed genes, respectively (0 h vs. 1
(Supplementary Tables 14 and 15). Most Selaginella-biased                                                 h and 1 h vs. 6 h). Clusters with increased expression during
orthogroups are unique and completely uncharacterized, reﬂect-                                            rehydration are enriched with functions related to DNA repair,
ing the need for more functional studies in other major plant                                             oxidative and water stress response among others. Clusters with
lineages.                                                                                                 high expression in desiccated tissues and low expression during
                                                                                                          rehydration have functions related to cell protection and
                                                                                                          osmoprotectant accumulation as described in more detail below.
Origins and evolution of desiccation tolerance. The transition                                               Gene duplications drive evolutionary innovation and tandem
from sea to land posed unique challenges for the ancestors of                                             gene duplications (TDs) are important for adaptive evolution in
terrestrial plants. Early land plants needed to evolve protective                                         dynamic environments31. Several clusters with peak expression
mechanisms to survive periodic drying and low atmospheric                                                 during desiccation are enriched in TDs, including many with
water potential. Desiccation tolerance in angiosperms likely                                              previously characterized roles in desiccation tolerance (Cluster 5,
evolved from rewiring seed desiccation pathways2, but the origins                                         fdr = 1.26 e−16; Supplementary Fig. 9). Early light-induced
of this trait in non-seed plants is unknown. We surveyed gene                                             proteins (ELIPs) protect photosynthetic apparatus against
expression changes during the desiccation and rehydration pro-                                            photo-oxidative damage under high light and other abiotic
cess in S. lepidophylla and compared patterns to angiosperm                                               stresses32. Land plants typically have 1–2 ELIPs but S.
resurrection plants. S. lepidophylla can survive for years or even                                        lepidophylla has undergone a major expansion to 23 ELIPs. Most
decades in a desiccated state without loss in viability. Samples                                          ELIPs are located in three tandem arrays with 8, 7, and 2
were taken from S. lepidophylla plants that were desiccated (0 h),                                        members, and the largest array is syntenic to the single ELIP
1, 6, and 24 h post rehydration (recovery), 120 h post rehydration                                        found in S. moellendorfﬁi (Fig. 4c). ELIPs are universally highly
(fully recovered), and after a 24 h dehydration (Fig. 4a). Despite                                        expressed during desiccation and show co-expression with other
prolonged quiescence, 77% of genes (21,062) have detectable                                               desiccation-related genes including heat-shock proteins, DNA

NATURE COMMUNICATIONS | (2018)9:13                                              | DOI: 10.1038/s41467-017-02546-5 | www.nature.com/naturecommunicationsnaturecommunications     5
ARTICLE                                                                                       NATURE COMMUNICATIONS | DOI: 10.1038/s41467-017-02546-5


repair enzymes, oleosins, LEAs, and others (enriched in cluster                         rehydration experiments. Sampling at the 0 h (desiccated), 24 and 120 h post
10, fdr = 6.70 e−23, Fig. 3c; Supplementary Table 16). A similar                        rehydration and 24 h post dehydration were taken at T = 0 to avoid any variance
                                                                                        associated with natural circadian oscillation. Sampling was done in triplicate with
expansion of ELIPs was identiﬁed in the resurrection plant Boea                         three biological replicates sequenced for each timepoint. The relative water content
hygrometrica6, suggesting these proteins are likely involved in the                     (RWC) for the S. lepidophylla rehydration time-course was calculated using the
convergent evolution of desiccation tolerance.                                          following equation: RWC = [(FW − DW)/(SW − DW)], where FW, DW, and SW
   LEA proteins function in membrane stability and macro-                               indicate fresh weight, dry weight, and saturated weight, respectively. DW was
molecular protection with roles in seed development, response to                        obtained after drying plant leaf tissue at 103 °C for 24 h and SW was obtained after
                                                                                        submerging the leaf tissue in water for 36 h. RWC for each sample can be found in
abiotic stresses, and desiccation tolerance in angiosperm                               Supplementary Table 18. Total RNA was extracted from 100 mg of ground S.
resurrection plants2, 33, 34. S. lepidophylla has an expansion in                       lepidophylla leaf tissues using Omega-biotek E.Z.N.A. Plant RNA Kit (Omega-
LEA proteins compared to S. moellendorfﬁi with 65 vs 36 across                          biotek), according to the manufacturer’s instructions. Two micrograms of total
six LEA subfamilies (Supplementary Table 17). The LEA2 and                              RNA was used for construction Illumina TruSeq stranded mRNA libraries fol-
                                                                                        lowing the manufactures protocol (Illumina). Multiplexed pooled libraries were
seed maturation protein (SMP) subfamilies show the most                                 sequenced on the Illumina HiSeq4000 under paired-end 150 nt mode.
dramatic expansion with 31 and 11 members, respectively. LEAs
are dispersed across the genome and few are found in tandem                             DNA extraction and methylation sequencing. Genomic DNA for methylation
arrays. LEAs are among the most highly expressed transcripts in                         proﬁling was extracted from 500 mg of ground tissues using the CTAB method,
the S. lepidophylla desiccation/rehydration timecourse with                             followed by RNase digestion and column puriﬁcation using Zymo Research
48 showing signiﬁcant expression changes (Supplementary                                 genomic DNA clean & concentrator™ (Zymo Research). In total, 500 ng of
Fig. 10). Interestingly, LEAs are also highly expressed in well-                        genomic DNA was ﬁrst sheared to an average size of 400–800 bp using Covaris
                                                                                        M200. Libraries were constructed using KAPA Hyper Prep Kits (KapaBiosystem,
hydrated tissues, suggesting they may be involved in constitutive                       #KK8504) according to the manufacturer’s protocol. The sheared DNA fragments
protective mechanisms, similar to several osmoprotectants.                              were end-repaired and A-tailed followed by adapter ligation. Adapter-ligated
   Desiccation-related genes are found in large tandem arrays in                        fragments were subjected to bisulﬁte conversion using EZ DNA Methylation-
the S. lepidophylla genome with individual genes having similar                         Lightning™ Kit (Zymo Research). Bisulﬁte-converted DNA was ampliﬁed using
                                                                                        KAPA HiFi HotStart Uracil + Ready Mix (KapaBiosystem) with 8 PCR cycles. PCR
expression patterns. This reﬂects the importance of TD in the                           products were then size-selected by gel electrophoresis for the range of 300–600 bp
evolution of novel traits and the advantages of gene proximity for                      and recovered by Zymoclean® Gel DNA Recovery Kit (Zymo Research). Multi-
coordinated expression. Patterns of gene expression during                              plexed pooled libraries were sequenced on the Illumina HiSeq4000 platform under
desiccation in S. lepidophylla mirror the pathways activated in                         paired-end 150 nt mode.
angiosperm resurrection plants. These pathways were either
independently co-opted through convergent evolution in both                             Genome assembly. S. lepidophylla PacBio reads collectively span 19.3 Gb repre-
                                                                                        senting 175× genome coverage with a ﬁltered subread N50 length of 18 kb. Raw
lineages or present in the common ancestor of early land plants.                        reads were error corrected and assembled using the Canu (V1.4)13 assembler with
The latter explanation is more likely as dehydration tolerance was                      the following parameters: minReadLength = 3000, GenomeSize = 110 Mb, and
acquired during the colonization of land. This hypothesis can be                        minOverlapLength = 2000. Other Canu parameters were left as default. The Falcon
further reﬁned with additional non-seed resurrection plant                              assembler (V0.3.0) was also tested but the overall contiguity was much lower
genomes.                                                                                (N50–110 kb) and a higher proportion of haplotypes were collapsed. Contigs were
                                                                                        polished using a reiterative approach with two rounds of Quiver (V2.3.0)14 with a
   The extreme haplotype-speciﬁc variation in Selaginella has not                       minimum subread length = 5000 bp, minimum polymerase read quality = 0.8,
been observed in other sequenced plant genomes. This dynamic                            maximum divergence percentage = 30 and minimum anchor size = 15. The
ﬂux of accumulating and purging sequences likely serves two                             polished contigs underwent a ﬁnal round of error correction using high-coverage
purposes. Strong selective pressures for removal of excess LTR                          300 bp PE Illumina data using Pilon (V1.21)15. Quality trimmed Illumina reads
                                                                                        were aligned to the Quiver polished contigs using bowtie2 (V2.3.0)36 with default
retrotransposons act to preserve proper gene and cis-element                            parameters. Reads were locally re-aligned around insertions/deletions (indels)
spacing, which in turn maintains the small genome size. Unequal                         using the IndelRealigner from the genome analysis tool kit (GATK; V3.7)37. Pilon
crossing over between divergent haplotypes and LTR-mediated                             parameters were as follows: --ﬂank 7, --K 51, and --mindepth 30. Illumina reads
gene duplications create a reservoir of new genes to facilitate                         were re-aligned to the ﬁnal polished genome to verify no residual errors remained
                                                                                        using GATK.
adaptive evolution. In this context, haplotype-speciﬁc gene
content may supplement the diversity lost in the absence of
WGD.                                                                                    Identiﬁcation of haplotype-speciﬁc regions. Assembled haplotypes were iden-
                                                                                        tiﬁed using a two-step approach based on gene level microsynteny followed by
                                                                                        whole-genome alignment. Gene synteny avoided spurious hits and misclassiﬁcation
Methods                                                                                 around repetitive elements with whole-genome alignment facilitating base-pair
DNA extraction and sequencing. The Selaginella lepidophylla plants used in this         resolution of overlapping haplotype regions. Syntenic gene pairs were identiﬁed
study were collected in the Chihuahuan Desert in the Southwestern US. These             with BLAST followed by ﬁltering for only collinear pairs using the MCSCAN
plants were conﬁrmed to be S. lepidophylla based on sequence homology to pub-           toolkit (V1.1)38. This approach ﬂagged 11,847 duplicated gene pairs collectively
lished vouchered specimens with the following nucleotide identities based on            representing ~45% of genes across 28 Mb of the genome. The exact boundaries of
BLAST: rbcL (99.6%; GenBank: AF419051.1) ITS2 (99.8%; GenBank: AF419002.1)              haplotype overlaps and haplotype-speciﬁc structural variants were identiﬁed by
28S (99.8%; GenBank: AJ507594.1). Desiccated plants were stored at 20 °C in dark        whole-genome alignment using MUMmer (V3.0)39. The unmasked genome was
conditions for roughly 3 years prior to this experiment. Rehydrated plants were         aligned against itself using NUCmer with default parameters and a minimum
maintained in growth chambers under 24 °C day, 20 °C night, 12-h photoperiod,           overlap size of 2 kb. Only hits in contigs with collinear gene pairs were considered
and 200 μmol m−2 s−1 light. High-molecular-weight genomic DNA was extracted             and overlaps in these regions were manually ﬁltered removing misalignments in
from young leaf tissue of a single S. lepidophylla plant using a modiﬁed nuclei         repetitive regions. In total, 33.7 Mb of assembled haplotype sequences were iden-
preparation35 followed by phenol chloroform puriﬁcation to remove residual              tiﬁed including 105 high-conﬁdence haplotype-speciﬁc insertions/deletions (indel).
contaminants. DNA quality was veriﬁed on a low-concentration agarose gel (0.5%          The boundaries of each indel were manually reﬁned using the GEvo module in
W/V) prior to library construction. gDNA was sheared to a 30 kb target size             CoGe (https://genomevolution.org)40. Haplotype-speciﬁc indels were veriﬁed
followed by end repair and adapter ligation. The ﬁnal library was size selected using   through alignment of raw PacBio reads spanning the boundary regions in both
a BluePippen size selection system (Sage Science) followed by puriﬁcation using         haplotypes.
AMPure XP beads (Beckman Coulter). High-molecular-weight libraries were
sequenced using the PacBio RsII instrument with P6C4 chemistry. A total of 21
                                                                                        Transposable element identiﬁcation. Non-autonomous DNA transposons in S.
SMRT cells were sequenced. A PCR-free Illumina DNAseq library was constructed
                                                                                        lepidophylla were identiﬁed by MITE-Hunter41 and were classiﬁed according to the
using the same high-molecular weight DNA following the manufactories instruc-
                                                                                        sequence of termini and length of target site duplication (TSD) provided in the
tions. Paired end 300 bp reads were sequenced on an Illumina MiSeq platform
                                                                                        output from MITE-Hunter based on the guide of Zhao et al.42. Candidate long
yielding a total of 80× Illumina sequence coverage for error correction.
                                                                                        terminal repeat retrotransposons (LTR-RTs) in S. lepidophylla were identiﬁed using
                                                                                        LTR_Finder (V1.02)43 and LTRharvest44. LTR_retriever45 was used to ﬁlter out
RNA extraction and sequencing. S. lepidophylla plants were maintained in                false LTR retrotransposons using structural and sequence features of target site
growth chambers under 16-h-light/8-h-night regime at 22 ± 2 °C for desiccation/         duplications, terminal motifs, and LTR-RT Pfam domains. Whole-genome

6         NATURE COMMUNICATIONS | (2018)9:13                               | DOI: 10.1038/s41467-017-02546-5 | www.nature.com/naturecommunicationsnaturecommunications
NATURE COMMUNICATIONS | DOI: 10.1038/s41467-017-02546-5                                                                                                    ARTICLE

annotation of LTR retrotransposons was done by RepeatMasker (http://www.               0.15. The co-expression network resulted in 38 clusters, with 13 genes not placed in
repeatmasker.org/)46 using the non-redundant LTR-RT library constructed by             any cluster.
LTR_retriever. DNA transposons that were nest-inserted in LTR retrotransposons
were identiﬁed and removed in the LTR library using a Perl scrip “Purger.pl” from      MethylC-seq analysis. Quality ﬁltered MethylC-seq reads were ﬁltered as
the LTR_retriever package. Non-LTR retrotransposons and other interspersed
                                                                                       described above. Three replicates for 0 h, 24 h, and 120 h post rehydration and
repeats were identiﬁed using RepeatModeler (V1.0.8) (http://www.repeatmasker.
                                                                                       unconverted control DNA were sequenced. The average genome coverage of each
org). While RepeatModeler also reports LTR retrotransposons, their sequences
                                                                                       library is 12.3×. Reads were mapped to the in silico converted, unmasked S. lepi-
were examined using TE-speciﬁc Pfam domains by HMMER (V3.1b2)47. Among
                                                                                       dophylla genome for the forward and reverse strands using Bismark (v0.12.0)64.
34 RepeatModeler-predicted LTR retrotransposons, none of them were exclusively
                                                                                       Genome-wide cytosine methylation was obtained using the following parameters in
matched with LTR-speciﬁc Pfam domains, thus all these sequences were labeled as
                                                                                       the Bismark methylation extractor step: –comprehensive –CX_context --cytosi-
unknown repeats instead of LTR retrotransposons. Candidate tandem repeats were
                                                                                       ne_report. The methylation level of each CHH, CHG, and CpG position was
identiﬁed by Tandem Repeat Finder (trf409.linux64)48 and were masked by the            calculated as the number of methylated count/total of methylated and unmethy-
TEs identiﬁed in previous steps. Unmasked candidates were labeled as tandem
                                                                                       lated count. Any position with coverage of less than three reads was removed. For
repeats, and the sequence redundancy were reduced using Cd-hit (V4.6.6)49 with
                                                                                       each cytosine position, the average methylation level was calculated from the mean
parameters -c 0.8, -G 0.8, -s 0.9, -aL 0.9, -aS 0.9, -M 0, and -T 5. The Perl script
                                                                                       methylation level among biological replicates.
“Purger.pl” from LTR_retriever and the plant protein database “alluniR-
                                                                                           Methylation level of the upstream (1 kb), downstream (1 kb) and body (from
efprexp082813” from MAKER (V2)50 were used to remove any protein-coding
                                                                                       transcription start site to transcription stop site) of all genic regions and intact LTR
sequences that were accidentally identiﬁed in these TEs. The top 10 most abundant
                                                                                       retrotransposons were calculated using BEDTools (v2.24.0)65 and in-house scripts.
repeat families (based on genome mass) were manually curated through alignment
                                                                                       To study differential methylated regions between 0 h, 24 h, and 120 h post
of multiple family members so to determine their boundary, termini, and TSD,
                                                                                       rehydration samples, the whole-genome methylated count of each library was
which were used to classify the relevant repeat.
                                                                                       obtained from the Bismark output. Differential methylated regions were analyzed
    Solo LTRs were identiﬁed from the whole-genome annotation of LTR-RT using
                                                                                       using the R package methylKit (v1.2.0)66 in 100 bp window and minimum coverage
the Perl script “solo_ﬁnder.pl” in the LTR_retriever package. In brief, independent    of 10 reads per site.
LTR sequences (no other LTR-related sequence presented in 300 bp distance) that
cover at least 80% of the library LTR entry with alignment score >300 and at least
100 bp in length were identiﬁed as solo LTR. The solo-intact LTR ratio was             Data availability. The genome assembly, raw PacBio, Illumina DNAseq, and
calculated based on the number of solo LTR over the number of intact LTR-RT for        RNAseq data are available from the National Center for Biotechnology Informa-
each family, which was estimated using the Perl script “solo_intact_ratio.pl” in the   tion (NCBI) Short Read Archive (SRA). The RNAseq reads were deposited to
LTR_retriever package. Since LTR length is positively correlated with the formation    NCBI SRA under BioProject PRJNA420971 (BioSample
of solo LTRs, we only compared the S/I ratio using elements with comparable LTR        SAMN08128719–08128734) and MethylCseq data were deposited under BioProject
length. This was achieved by using the 95 percentile of LTR length in S.               PRJNA421023 (BioSample SAMN08132846-08132853). The genome assembly has
lepidophylla (90–1540 bp) to screen for LTR-RT families within into this range in      been deposited under BioSample SAMN07071123 and BioProject ID
the rice and Arabidopsis genomes.                                                      PRJNA386571.
    Estimation of insertion time for each intact LTR element was provided by
LTR_retriever using the formula of T = K/2μ, where K is the divergence rate
approximated by percent identity and adjusted using the Jukes-Cantor model for
                                                                                       Received: 21 September 2017 Accepted: 8 December 2017
non-coding sequences. The neutral mutation rate of μ = 1.3 × 10–8 mutations per
bp per year was used51.

Genome annotation. The S. lepidophylla genome was annotated using MAKER (V
2.31.8)52. A set of high-quality transcripts for gene prediction were assembled with   References
StringTie (V1.3.1)53 using the stranded, paired end Illumina RNAseq data               1. Oliver, M. J., Tuba, Z. & Mishler, B. D. The evolution of vegetative desiccation
described above. Quality ﬁltered RNAseq reads were aligned to the unmasked S.              tolerance in land plants. Plant Ecol. 151, 85–100 (2000).
lepidophylla genome using TopHat (V2.1.0)54 and the accepted_hits.bam ﬁle was          2. Costa, M. et al. A footprint of desiccation tolerance in the genome of Xerophyta
used as input for StringTie. Default parameters were used for StringTie with the           viscosa. Nat. Plants 3, 17038 (2017).
--merge ﬂag to produce a set of non-redundant transcripts to feed into MAKER.          3. Proctor, M. The physiological basis of bryophyte production. Bot. J. Linn. Soc.
These transcripts were treated as expressed sequence tag evidence and protein              104, 61–77 (1990).
sequences from Arabidopsis17, Selaginella moellendorfﬁi10, and UniprotKB plant         4. Lüttge, U., Beck, E. & Bartels, D. Plant desiccation tolerance. Vol. 215 (Springer,
databases55 were used as protein homology evidence. Intact S. lepidophylla LTR             2011).
retrotransposons were input as a custom repeat database along with default repeat      5. VanBuren, R. et al. Single-molecule sequencing of the desiccation-tolerant grass
libraries in MAKER. Ab initio gene prediction was done using the gene predictors           Oropetium thomaeum. Nature 527, 508–511 (2015).
SNAP and Augustus with reiterative training in S. lepidophylla. The initial MAKER      6. Xiao, L. et al. The resurrection genome of Boea hygrometrica: A blueprint for
Max gene set was ﬁltered for gene models with Pfam domain evidence and                     survival of dehydration. Proc. Natl Acad. Sci. 112, 5833–5837 (2015).
annotation edit distance <1.0. Putative transposon-derived models were removed.        7. Banks, J. A. Selaginella and 400 million years of separation. Annu. Rev. Plant.
This produced a set of 39,051 ﬁltered gene models. A further 11,847 duplicated             Biol. 60, 223–238 (2009).
gene models corresponding to separate haplotypes were removed to produce a ﬁnal        8. Thomas, B. A. Paleozoic herbaceous lycopsids and the beginnings of extant
set of 27,204 non-redundant genes.                                                         lycopodium sens lat. And Selaginella Sens. Lat. Ann. Mo. Bot. Gard. 79,
                                                                                           623–631 (1992).
Orthogroup annotation. Orthogroups were identiﬁed using Orthoﬁnder                     9. Baniaga, A. E., Arrigo, N. & Barker, M. S. The small nuclear genomes of
(V1.0.6)56 with protein-coding genes from the Arabidopsis17, rice57, poplar58,             Selaginella are associated with a low rate of genome size evolution. Genome
grape59, Oropetium thomaeum60, S. moellendorfﬁi10, and S. lepidophylla genomes             Biol. Evol. 8, 1516–1525 (2016).
using default settings (Supplementary Table 11). We set a stringent cutoff of a 5      10. Banks, J. A. et al. The Selaginella genome identiﬁes genetic changes associated
fold difference in orthogroup composition and at least a minimum of 10 genes               with the evolution of vascular plants. science 332, 960–963 (2011).
(average) across either Angiosperms or Selaginella groups to identify expanded         11. Michael, T. P. & VanBuren, R. Progress, challenges and the future of crop
orthogroups. On average, angiosperm enriched orthogroups had 20-fold enrich-               genomes. Curr. Opin. Plant. Biol. 24, 71–81 (2015).
ment and Selaginella had 40 fold enrichment.                                           12. Chin, C.-S. et al. Phased diploid genome assembly with single-molecule real-
                                                                                           time sequencing. Nat. Methods 13, 1050–1054 (2016).
Gene expression analysis. Adapter sequences and low-quality bases were ﬁltered         13. Koren, S. et al. Canu: scalable and accurate long-read assembly via adaptive k-
from the raw, paired end Illumina RNAseq reads using TRIMMOMATIC (v0.33)61                 mer weighting and repeat separation. Genome Res. 27, 722–736 (2017).
and reads shorter than 36 bp were discarded. Expression levels (in Transcript Per      14. Chin, C.-S. et al. Nonhybrid, ﬁnished microbial genome assemblies from long-
Million, TPM) were quantiﬁed using Kallisto62 with the 27,204 monoploid S.                 read SMRT sequencing data. Nat. Methods 10, 563–569 (2013).
lepidophylla gene models provided as input. An average TPM for each time-point         15. Walker, B. J. et al. Pilon: an integrated tool for comprehensive microbial variant
was calculated from the mean TPM of the three biological replicates. We pre-               detection and genome assembly improvement. PLoS ONE 9, e112963 (2014).
formed weighted gene co-expression analysis of the dehydration and subsequent          16. Simão, F. A., Waterhouse, R. M., Ioannidis, P., Kriventseva, E. V. & Zdobnov, E.
rehydration time course RNA-seq data with the R package WGCNA63. The                       M. BUSCO: assessing genome assembly and annotation completeness with
expression data were pre-ﬁltered to remove genes with excessive missing values or          single-copy orthologs. Bioinformatics 31, 3210–3212 (2015).
invariant expression using the built-in quality control function. A signed co-         17. Initiative, A. G. Analysis of the genome sequence of the ﬂowering plant
expression network was constructed using a soft-thresholding power of 10 and               Arabidopsis thaliana. Nature 408, 796 (2000).
default parameters. The only exception was the mergeCutHeight parameter, con-          18. Ibarra-Laclette, E. et al. Architecture and evolution of a minute plant genome.
trolling the minimum distance between co-expression clusters, which was set to             Nature 498, 94–98 (2013).

NATURE COMMUNICATIONS | (2018)9:13                              | DOI: 10.1038/s41467-017-02546-5 | www.nature.com/naturecommunicationsnaturecommunications                  7
ARTICLE                                                                                       NATURE COMMUNICATIONS | DOI: 10.1038/s41467-017-02546-5


19. Leitch, I., Soltis, D., Soltis, P. & Bennett, M. Evolution of DNA amounts across    51 Ma, J. & Bennetzen, J. L. Rapid recent growth and divergence of rice nuclear
    land plants (Embryophyta). Ann. Bot. 95, 207–217 (2005).                               genomes. Proc. Natl Acad. Sci. USA 101, 12404–12410 (2004).
20. Michael, T. P. Plant genome size variation: bloating and purgingDNA. Brief.         52 Cantarel, B. L. et al. MAKER: an easy-to-use annotation pipeline designed for
    Funct. Genomics 13, 308–317 (2014).                                                    emerging model organism genomes. Genome Res. 18, 188–196 (2008).
21. Niederhuth, C. E. et al. Widespread natural variation of DNA methylation            53 Pertea, M. et al. StringTie enables improved reconstruction of a transcriptome
    within angiosperms. Genome Biol. 17, 194 (2016).                                       from RNA-seq reads. Nat. Biotechnol. 33, 290–295 (2015).
22. Zemach, A., McDaniel, I. E., Silva, P. & Zilberman, D. Genome-wide evolutionary     54 Trapnell, C., Pachter, L. & Salzberg, S. L. TopHat: discovering splice junctions
    analysis of eukaryotic DNA methylation. Science 328, 916–919 (2010).                   with RNA-Seq. Bioinformatics 25, 1105–1111 (2009).
23. Takuno, S., Ran, J.-H. & Gaut, B. S. Evolutionary patterns of genic DNA             55 Boutet, E., Lieberherr, D., Tognolli, M., Schneider, M. & Bairoch, A. UniProtKB/
    methylation vary across land plants. Nat. Plants 2, 15222 (2016).                      Swiss-Prot: the manually annotated section of the UniProt KnowledgeBase.
24. Magallón, S., Gómez‐Acevedo, S., Sánchez‐Reyes, L. L. & Hernández‐                     Methods Mol. Biol, 406, 89–112 (2007).
    Hernández, T. A metacalibrated time‐tree documents the early rise of ﬂowering       56 Emms, D. M. & Kelly, S. OrthoFinder: solving fundamental biases in whole
    plant phylogenetic diversity. New Phytol. 207, 437–453 (2015).                         genome comparisons dramatically improves orthogroup inference accuracy.
25. Jiao, Y. et al. Ancestral polyploidy in seed plants and angiosperms. Nature 473,       Genome Biol. 16, 157 (2015).
    97–100 (2011).                                                                      57 Goff, S. A. et al. A draft sequence of the rice genome (Oryza sativa L. ssp.
26. Tang, H. et al. Synteny and collinearity in plant genomes. Science 320, 486–488        japonica). Science 296, 92–100 (2002).
    (2008).                                                                             58 Tuskan, G. A. et al. The genome of black cottonwood, Populus trichocarpa
27. Ohno, S. Evolution by Gene Duplication. (Springer-Verlag, 1970).                       (Torr. & Gray). science 313, 1596–1604 (2006).
28. Birchler, J. A. & Veitia, R. A. The gene balance hypothesis: From classical         59 Jaillon, O. et al. The grapevine genome sequence suggests ancestral
    genetics to modern genomics. Plant. Cell 19, 395–402, https://doi.org/10.1105/         hexaploidization in major angiosperm phyla. Nature 449, 463–467 (2007).
    tpc.106.049338 (2007).                                                              60 VanBuren, R. et al. Single-molecule sequencing of the desiccation-tolerant grass
29. Bekaert, M., Edger, P. P., Pires, J. C. & Conant, G. C. Two-phase resolution of        Oropetium thomaeum. Nature 527, 508–511 (2015).
    polyploidy in the Arabidopsis metabolic network gives rise to relative and          61 Bolger, A. M., Lohse, M. & Usadel, B. Trimmomatic: a ﬂexible trimmer for
    absolute dosage constraints. Plant. Cell 23, 1719–1728 (2011).                         Illumina sequence data. Bioinformatics 30, 2117–2120(2014).
30. Williams, B. et al. Trehalose accumulation triggers autophagy during plant          62 Bray, N. L., Pimentel, H., Melsted, P. & Pachter, L. Near-optimal probabilistic
    desiccation. PLoS Genet. 11, e1005705 (2015).                                          RNA-seq quantiﬁcation. Nat. Biotechnol. 34, 525–527 (2016).
31. Panchy, N., Lehti-Shiu, M. & Shiu, S.-H. Evolution of gene duplication in           63 Langfelder, P. & Horvath, S. WGCNA: an R package for weighted correlation
    plants. Plant Physiol. 171, 2294–2316 (2016).                                          network analysis. BMC Bioinformatics 9, 1 (2008).
32. Hutin, C. et al. Early light-induced proteins protect Arabidopsis from              64 Krueger, F. & Andrews, S. R. Bismark: a ﬂexible aligner and methylation caller
    photooxidative stress. Proc. Natl Acad. Sci. 100, 4921–4926 (2003).                    for Bisulﬁte-Seq applications. Bioinformatics 27, 1571–1572 (2011).
33. Gechev, T. S. et al. Molecular mechanisms of desiccation tolerance in the           65 Quinlan, A. R. & Hall, I. M. BEDTools: a ﬂexible suite of utilities for comparing
    resurrection glacial relic Haberlea rhodopensis. Cell. Mol. Life Sci. 70, 689–709      genomic features. Bioinformatics 26, 841–842 (2010).
    (2013).                                                                             66 Akalin, A. et al. methylKit: a comprehensive R package for the analysis of
34. Challabathula, D. & Bartels, D. Desiccation tolerance in resurrection plants:          genome-wide DNA methylation proﬁles. Genome Biol. 13, R87 (2012).
    new insights from transcriptome, proteome and metabolome analysis. Front.
    Plant Sci. 4, 482 (2013).
35. Zhang, H. B., Zhao, X., Ding, X., Paterson, A. H. & Wing, R. A. Preparation of
                                                                                        Acknowledgements
                                                                                        R.V. was supported by Hatch (Award 1013240) and startup funds from MSU. S.O and N.
    megabase‐size DNA from plant nuclei. Plant J. 7, 175–184 (1995).
                                                                                        J. were supported by the National Science Foundation (MCB-1121650 to N.J.)
36. Langmead, B. & Salzberg, S. L. Fast gapped-read alignment with Bowtie 2. Nat.
    Methods 9, 357–359 (2012).
37. McKenna, A. et al. The genome analysis toolkit: a MapReduce framework for           Author contributions
    analyzing next-generation DNA sequencing data. Genome Res. 20, 1297–1303            R.V. designed and conceived research; T.P.M. performed Illumina and PacBio sequen-
    (2010).                                                                             cing; R.V., J.W., S.O. and N.J. annotated genome features; J.W. and R.V. performed
38. Wang, Y. et al. MCScanX: a toolkit for detection and evolutionary analysis of       desiccation experiments, RNAseq, and MethylCseq experiments; R.V., J.W., S.O., J. P., D.
    gene synteny and collinearity. Nucleic Acids Res. 40, e49–e49 (2012).               B., T.C.M., P.E. and T.P.M analyzed data; R.V. wrote the paper. All authors read and
39. Kurtz, S. et al. Versatile and open software for comparing large genomes.           approved the ﬁnal manuscript.
    Genome Biol. 5, R12 (2004).
40. Lyons, E. & Freeling, M. How to usefully compare homologous plant genes and
    chromosomes as DNA sequences. Plant J. 53, 661–673 (2008).                          Additional information
41. Han, Y. & Wessler, S. R. MITE-Hunter: a program for discovering miniature           Supplementary Information accompanies this paper at https://doi.org/10.1038/s41467-
    inverted-repeat transposable elements from genomic sequences. Nucleic Acids         017-02546-5.
    Res. 38, e199 (2010).
42. Zhao, D., Ferguson, A. A. & Jiang, N. What makes up plant genomes: The              Competing interests: The authors declare no competing ﬁnancial interests.
    vanishing line between transposable elements and genes. Biochim. Biophys.
    Acta 1859, 366–380 (2015).                                                          Reprints and permission information is available online at http://npg.nature.com/
43. Xu, Z. & Wang, H. LTR_FINDER: an efﬁcient tool for the prediction of full-          reprintsandpermissions/
    length LTR retrotransposons. Nucleic Acids Res. 35, W265–W268 (2007).
44. Ellinghaus, D., Kurtz, S. & Willhoeft, U. LTRharvest, an efﬁcient and ﬂexible       Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in
    software for de novo detection of LTR retrotransposons. BMC Bioinformatics 9,       published maps and institutional afﬁliations.
    18 (2008).
45. Ou, S. & Jiang, N. LTR_retriever: a highly accurate and sensitive program for
    identiﬁcation of long terminal-repeat retrotransposons. Plant Physiol. DOI:                           Open Access This article is licensed under a Creative Commons
    https://doi.org/10.1104/pp.17.01310 (2017).                                                           Attribution 4.0 International License, which permits use, sharing,
46. Tarailo‐Graovac, M. & Chen, N. Using RepeatMasker to identify repetitive            adaptation, distribution and reproduction in any medium or format, as long as you give
    elements in genomic sequences. Curr. Protoc. Bioinformatics 4.10. 11-14.10. 14      appropriate credit to the original author(s) and the source, provide a link to the Creative
    (2009).                                                                             Commons license, and indicate if changes were made. The images or other third party
47 Eddy, S. R. Accelerated proﬁle HMM searches. PLoS Comput. Biol. 7, e1002195          material in this article are included in the article’s Creative Commons license, unless
   (2011).                                                                              indicated otherwise in a credit line to the material. If material is not included in the
48 Benson, G. Tandem repeats ﬁnder: a program to analyze DNA sequences.                 article’s Creative Commons license and your intended use is not permitted by statutory
   Nucleic Acids Res. 27, 573–580 (1999).                                               regulation or exceeds the permitted use, you will need to obtain permission directly from
49 Li, W. & Godzik, A. Cd-hit: a fast program for clustering and comparing large        the copyright holder. To view a copy of this license, visit http://creativecommons.org/
   sets of protein or nucleotide sequences. Bioinformatics 22, 1658–1659 (2006).
                                                                                        licenses/by/4.0/.
50 Holt, C. & Yandell, M. MAKER2: an annotation pipeline and genome-database
   management tool for second-generation genome projects. BMC Bioinformatics
   12, 1–14 (2011).                                                                     © The Author(s) 2017




8         NATURE COMMUNICATIONS | (2018)9:13                               | DOI: 10.1038/s41467-017-02546-5 | www.nature.com/naturecommunicationsnaturecommunications
