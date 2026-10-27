# Vuruputoor_2023 - Welcome to the big leaves Best practices for improving genom

**Source PDF:** 

---

Received: 4 October 2022      |   Accepted: 10 February 2023

DOI: 10.1002/aps3.11533


APPLICATION ARTICLE




Welcome to the big leaves: Best practices for improving genome
annotation in non‐model plant genomes

Vidya S. Vuruputoor                            | Daniel Monyak | Karl C. Fetter                                     | Cynthia Webster                           |
Akriti Bhattarai | Bikash Shrestha   | Sumaira Zaman     | Jeremy Bennett                                                                          |
Susan L. McEvoy    | Madison Caballero   | Jill L. Wegrzyn

Department of Ecology and Evolutionary Biology,         Abstract
University of Connecticut, Storrs, Connecticut,
06269, USA                                              Premise: Robust standards to evaluate quality and completeness are lacking in
                                                        eukaryotic structural genome annotation, as genome annotation software is developed
Correspondence                                          using model organisms and typically lacks benchmarking to comprehensively evaluate
Jill L. Wegrzyn, Department of Ecology and              the quality and accuracy of the ﬁnal predictions. The annotation of plant genomes is
Evolutionary Biology, University of Connecticut,        particularly challenging due to their large sizes, abundant transposable elements, and
Storrs, Connecticut 06269, USA.
Email: jill.wegrzyn@uconn.edu                           variable ploidies. This study investigates the impact of genome quality, complexity,
                                                        sequence read input, and method on protein‐coding gene predictions.
This article is part of the special issue               Methods: The impact of repeat masking, long‐read and short‐read inputs, and de
“Bioinformatics for Plant Biology.”
                                                        novo and genome‐guided protein evidence was examined in the context of the
                                                        popular BRAKER and MAKER workﬂows for ﬁve plant genomes. The annotations
                                                        were benchmarked for structural traits and sequence similarity.
                                                        Results: Benchmarks that reﬂect gene structures, reciprocal similarity search
                                                        alignments, and mono‐exonic/multi‐exonic gene counts provide a more complete
                                                        view of annotation accuracy. Transcripts derived from RNA‐read alignments
                                                        alone are not suﬃcient for genome annotation. Gene prediction workﬂows that
                                                        combine evidence‐based and ab initio approaches are recommended, and a
                                                        combination of short and long reads can improve genome annotation. Adding
                                                        protein evidence from de novo assemblies, genome‐guided transcriptome assemblies,
                                                        or full‐length proteins from OrthoDB generates more putative false positives as
                                                        implemented in the current workﬂows. Post‐processing with functional and structural
                                                        ﬁlters is highly recommended.
                                                        Discussion: While the annotation of non‐model plant genomes remains complex, this
                                                        study provides recommendations for inputs and methodological approaches. We
                                                        discuss a set of best practices to generate an optimal plant genome annotation and
                                                        present a more robust set of metrics to evaluate the resulting predictions.

                                                        KEYWORDS
                                                        BRAKER, gene identiﬁcation, genome annotation, MAKER, plant genomes, StringTie2, TSEBRA




The ﬁrst published plant genome, Arabidopsis thaliana                                  National Center for Biotechnology Information (NCBI;
(L.) Heynh., was released in 2000 (Arabidopsis Genome                                  https://www.ncbi.nlm.nih.gov/) genome repository contains
Initiative, 2000). Its small size (135 Mbp) and minimal                                the genomes of over 900 land plant species, and roughly half
repeat content stand in stark contrast to the plant genomes                            of these are assembled to chromosome scale. The total
sequenced and assembled today (Kress et al., 2022). The                                number of complete reference plant genomes has more than

This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the
original work is properly cited.
© 2023 The Authors. Applications in Plant Sciences published by Wiley Periodicals LLC on behalf of Botanical Society of America.

Appl. Plant Sci. 2023;11:e11533.                                                                              wileyonlinelibrary.com/journal/AppsPlantSci   |       1 of 17
https://doi.org/10.1002/aps3.11533
2 of 17   |                                                                    IMPROVING NON‐MODEL PLANT GENOME ANNOTATION



doubled in the past ﬁve years (Marks et al., 2021). Initiatives   When extrinsic evidence from RNA‐Seq and protein
like the Open Green Genomes (https://phytozome-next.jgi.          alignments are available, workﬂow packages such as
doe.gov/ogg/), 10KP (Cheng et al., 2018), and the Earth           MAKER (Cantarel et al., 2008; Holt and Yandell, 2011;
BioGenome Project (Lewin et al., 2022) are improving the          Campbell et al., 2014a) and BRAKER (Hoﬀ et al., 2016, 2019;
phylogenetic representation of plant genomes by sampling          Brůna et al., 2021) can assist in training prediction tools ab
underrepresented clades. The plant genomes published              initio. These packages can leverage sequence data from the
today are more likely to be polyploids and/or larger              target species, as well as external evidence from closely
genomes with substantial transposable element (TE) con-           related species. While these workﬂows can simplify the
tents (Sun et al., 2022). Recent high‐throughput sequencing       integration across external evidence, downstream packages
advancements, particularly long reads and chromosome              are still required to select or modify the resulting
conformation capture approaches, have enabled the com-            predictions (Haas et al., 2008; Banerjee et al., 2021; Gabriel
pletion of these more challenging assemblies (Pucker              et al., 2021).
et al., 2022).                                                        Here, we provide a comprehensive evaluation of plant
    While genome assembly has seen substantial improve-           genome annotation workﬂows, intentionally selecting
ments in accuracy and contiguity, structural annotation           beyond the typical model species to represent some of the
remains challenging. This process delineates the physical         more complex genomes under investigation today. In doing
positions of genomic features, including protein‐coding           so, we evaluate the impact of repeat masking using two
genes, promoters, and regulatory elements. It can be              diﬀerent implementations of the RepeatModeler2 frame-
followed by functional annotation, which assigns biological       work (Flynn et al., 2020). This is followed by exploring the
descriptors to the identiﬁed features. The accurate classiﬁ-      role of read length and accuracy, and the impact of short‐
cation of these features provides the basis for questions         read and long‐read data. Finally, we examine the contribu-
focused on species evolution, population dynamics, and            tion of protein evidence, generated from the de novo
functional genomics. Errors in genome annotation are              assembly of the RNA inputs and a genome‐guided
frequent, even among well‐studied models, and are                 assembly. These variations are examined in the MAKER
propagated through downstream analyses (Deutekom                  and BRAKER frameworks to emphasize the importance of
et al., 2019; Salzberg, 2019; Meyer et al., 2020). In most        deﬁning benchmarks to guide downstream ﬁltering ap-
eukaryotes, genome annotation is made more challenging            proaches. Finally, the largest and most repetitive genome
by the partial conservation of sequence patterns, variable        assessed in this study, Liriodendron chinense (Hemsl.) Sarg.,
intron lengths, variable distances between genes, alternative     was used to demonstrate best practices to reﬁne the
splicing, and higher densities of TEs and pseudogenes             predictions.
(Kersey, 2019; Salzberg, 2019). As a result of these
complexities, the structural annotation process requires
more advanced informatic tools and skills that support the        METHODS
integration and manipulation of large data sets (Mudge and
Harrow, 2016).                                                    Gathering plant genome data sets
    Structural and functional genome annotation proceeds
in three stages: identifying and masking noncoding regions        Five plant genomes were chosen for this study, including
(repeats), predicting the physical positions of gene struc-       the Chinese tulip tree (Liriodendron chinense) (Chen
tures, and assigning biological information to the predic-        et al., 2019), black cottonwood (Populus trichocarpa Torr.
tions (Jung et al., 2020). Repeat regions are soft‐masked         & A. Gray ex Hook. version 3) (Tuskan et al., 2006),
(e.g., RepeatMasker [Smit et al., 2013–2015] and Repeat-          Chinese rose (Rosa chinensis Jacq.) (Raymond et al., 2018),
Modeler2 [Flynn et al., 2020]), which means these regions         thale cress (Arabidopsis thaliana TAIR 10) (Cheng
are indicated but not obscured to annotation software. This       et al., 2017), and a bryophyte, the common cord‐moss
is followed by gene prediction, which may be ab initio            (Funaria hygrometrica Hedw.) (Kirbis et al., 2022) (Appen-
(evidence‐free) or evidenced‐based. Evidence‐based ap-            dix S1). The genomes were selected to represent two model
proaches use RNA sequencing (RNA‐Seq) and protein                 systems (Populus L. and Arabidopsis Heynh.) with well‐
sequence similarity search alignments. Evidence‐based             curated structural annotations and three non‐model sys-
approaches are often used in combination with ab initio           tems, for which computational techniques were exclusively
approaches (e.g., AUGUSTUS [Stanke and Waack, 2003]) to           used to produce the annotations. Two of these non‐model
generate models trained on patterns associated with true          systems were also more divergent examples, representing
genes. Given the advanced state of high‐throughput                the only sequenced member of their genus (Funaria Hedw.
transcriptome sequencing, it is common to resolve tran-           and Liriodendron L.). The publicly available assembly and
scripts from RNA reads through genome‐guided ap-                  annotations for each species were accessed from NCBI, and
proaches, such as using StringTie2 (Kovaka et al., 2019).         genome completeness was estimated by searching the
Long‐read cDNA sequencing through Paciﬁc Biosciences              genome and annotation for the conserved single‐copy
(PacBio) and Oxford Nanopore can provide additional               orthologs in the Embryophyta odb10 BUSCO version
resolution and improve the identiﬁcation of splice variants.      5.0.0 (Simão et al., 2015). The contiguity of the reference
IMPROVING NON‐MODEL PLANT GENOME ANNOTATION                                                                             |   3 of 17



genomes was assessed using Quast version 5.0.2 (Gurevich        available and performs in a comparable manner but is not
et al., 2013). The published annotation ﬁles were summa-        always superior in all metrics (Bolger et al., 2018). For this
rized using gFACs (Caballero and Wegrzyn, 2019).                study, it was selected as the most widely used package for
    Read sets available through NCBI's Sequence Read            this purpose. Redundancy in the predicted coding regions
Archive (SRA) were accessed to provide transcriptomic           was reduced after clustering at 98% identity using UCLUST,
evidence for each species and included a variety of tissue      a clustering algorithm of USEARCH version 9.0.2132
types. The Illumina short‐read libraries were sequenced         (Edgar, 2010). Frame‐selected transcripts shorter than
(100‐bp paired‐end) with a HiSeq 2500 (Illumina, San            300 bp were removed. The remaining transcripts were
Diego, California, USA). The read sets included at least four   aligned to the genome using GMAP version 2019‐06‐10
libraries, 20–82 million reads before the quality control       (Wu and Watanabe, 2005). The predicted proteins (from the
(QC), and a minimum of 16 million reads after QC. Iso‐Seq       same Transdecoder run) were aligned to the reference genome
(PacBio, Menlo Park, California, USA) long reads were           using GenomeThreader version 1.7.1 (Gremme et al., 2005).
accessed for Populus and Liriodendron, and PromethION               To provide protein evidence from genome‐guided
(Oxford Nanopore Technologies [ONT], Oxford, United             sources, the previously aligned Illumina short reads (via
Kingdom) reads were available for Rosa and Arabidopsis.         HISAT2) were constructed into transcripts with StringTie2
The read sets for long‐read data ranged from 161,000 to 41      version 2.2.0 (Pertea et al., 2015; Kovaka et al., 2019). Long
million total reads per species (Appendix S2).                  reads were treated similarly, along with a combination of
                                                                short and long reads. The predicted transcripts were
                                                                extracted using gﬀRead (Pertea and Pertea, 2020) and
Repeat masking and read alignment                               frame‐selected with TransDecoder. The transcriptome
                                                                alignment annotation ﬁle (gﬀ3) was passed to gFACs for
RepeatModeler2 (Flynn et al., 2020) was used to construct       the evaluation of the gene model statistics. The complete-
repeat libraries with default settings, and the repeats were    ness of the aligned transcripts and protein sequences was
soft masked with the libraries constructed via RepeatMasker     estimated using BUSCO. Finally, to provide evidence from
version 4.0.6 (Smit et al., 2013–2015). The genomes of          external sources (not derived from any transcriptomic
Arabidopsis, Funaria, Populus, and Liriodendron were            inputs), full‐length protein evidence from OrthoDB
additionally masked using RepeatModeler2 with additional        (odb10_plants; Kriventseva et al., 2019) was provided for
long terminal repeat (LTR) identiﬁcation (‐LTRStruct ﬂag).      BRAKER/TSEBRA runs.
A quality assessment of the Illumina short reads was
performed using FastQC version 0.11.7 (Andrews, 2010)
before and after trimming the low‐quality bases. Sickle         Genome annotations
version 1.33 (Joshi and Fass, 2011) was used to trim low‐
quality bases, with 50 bp as the minimum read length            Each genome was tested in four primary open‐source
threshold. Single‐end reads generated post‐trimming were        annotation softwares to predict the gene models (Table 1).
excluded from the RNA alignments and assembly. The              Several diﬀerent runs of BRAKER version 2.1.5 (Hoﬀ
trimmed short reads were aligned against their reference        et al., 2019) and BRAKER/TSEBRA (Gabriel et al., 2021) were
genomes using HISAT2 version 2.2.0 (Kim et al., 2019).          used with various combinations of RNA‐Seq (long‐ and short‐
HISAT2 was selected for its performance in recent               read inputs) and protein evidence. MAKER version 3.1.3
benchmarking studies and as the aligner of choice for input     (Cantarel et al., 2008) was run once with the transcript and
to StringTie2 (Corchete et al., 2020; Musich et al., 2021).     protein evidence. Finally, StringTie2 (Kovaka et al., 2019), with
Long‐read RNA data were obtained for four species:              TransDecoder, was used to generate genome‐guided predic-
Arabidopsis and Rosa were sequenced with ONT's Pro-             tions from RNA evidence alone (Appendix S3).
methION, and Populus and Liriodendron were sequenced
with PacBio Sequel. The long‐read data sets were aligned
against their respective genomes using Minimap2 version         MAKER annotation
2.1.7 (Li, 2018, 2021).
                                                                MAKER (MK) was run on the soft‐masked reference
                                                                genomes of Arabidopsis, Populus, and Funaria, with repeats
Generation of protein evidence                                  estimated using the additional LTR detection method in
                                                                RepeatModeler2 (LTRStruct ﬂag; RM2+). This was intended
To generate protein evidence, Illumina short reads were         to emulate the MAKER‐P (Campbell et al., 2014b) method
assembled de novo using Trinity version 2.8.5 (Grabherr         because the original repeat and pseudogene identiﬁcation
et al., 2011), with a minimum contig length of 300 bp. The      protocols are deprecated. MK (RM2+) was executed (i.e.,
assembled transcriptomes for the multiple libraries were        trained) twice. The annotations derived from MK (RM2+)
combined, and putative coding regions were predicted using      used protein evidence generated from de novo–assembled
TransDecoder version 5.3.0 (http://transdecoder.github.io).     RNA reads from Trinity. These models were used to train
TransDecoder is one of several frame‐selection methods          the ab initio gene prediction software AUGUSTUS version
4 of 17   |                                                                                             IMPROVING NON‐MODEL PLANT GENOME ANNOTATION



TABLE 1        Notations for the diﬀerent runs performed for benchmarking.
 Run                                                                                                Arabidopsis      Funaria      Populus   Liriodendron   Rosa
 StringTie2

 ST2 (SR)                      Short reads                                                          X                X            X         X              X

 ST2 (LR)                      Long reads                                                           X                             X         X              X

 ST2 (SR/LR)                   Short and long reads                                                 X                             X         X              X

 BRAKER

 BR (SR)                       Short reads                                                          X                X            X         X              X

 BR (LR)                       Long reads                                                           X                             X         X              X

 BR (SR/LR)                    Short and long reads                                                 X                             X         X              X

 BR (SR/RM2+)                  Short reads with additional masking for LTRs                         X                X            X         X

 TSEBRA

 TSB (SR/TRINITY)              Short reads and de novo proteins                                     X                X            X         X              X

 TSB (SR/ST2)                  Short reads and genome‐guided proteins                               X                X            X         X              X

 TSB (LR/ST2)                  Long reads and genome‐guided proteins                                X                             X         X              X

 TSB (SR/LR/ST2)               Short and long reads and genome‐guided proteins                      X                             X         X              X

 TSB (SR/ST2/RM2+)             Short reads and genome‐guided proteins with additional               X                X            X         X
                                  masking for LTRs

 TSB (SR/OrthoDB)              Short reads and OrthoDB proteins                                     X                X            X         X              X

 MAKER

 MK (RM2+)                     Short reads with additional masking for LTRs                         X                X            X

Note: LR = long reads; LTR = long terminal repeats; RM2+ = RepeatModeler2 with the additional repeat masking; SR = short reads.




3.3.3 (Stanke and Waack, 2003) and SNAP version 2006‐07‐                              model plant genomes (Appendix S4) (Jain et al., 2008). The
28 (Korf, 2004). The hidden Markov models (HMMs)                                      gene prediction assessment was recorded as a percentage
trained using AUGUSTUS and SNAP were used, along with                                 of sequence similarity hits to the total number of genes. The
initial aligned evidence (est2genome and protein2genome                               value of the reciprocal BLAST search will be dependent
parameters) for the second MK (RM2+) run to generate the                              on the phylogenetic relationships of the target species.
ﬁnal gene models.                                                                     While higher annotation rates indicate better gene predic-
                                                                                      tion abilities, species‐speciﬁc genes will always be missed
                                                                                      (Armisén et al., 2008); therefore, a minimum annotation
Assessment of gene predictions                                                        rate of 80% is a reasonable threshold to expect when dealing
                                                                                      with most non‐models. Similarly, a higher BUSCO score
The quality of genome annotations among the diﬀerent                                  indicates a better annotation, as BUSCO utilizes OrthoDB
gene prediction methods was evaluated using three primary                             to form its conserved sets; the recommended target score is
metrics: (1) the mono‐exonic (single‐exon) and multi‐                                 >95% for land plants (Simão et al., 2015; Manni et al., 2021).
exonic (multiple‐exon) ratio, (2) conserved single‐copy                                   The sensitivity and precision of the runs for Arabidopsis
orthologs queried from the predicted gene models using                                and Populus were assessed using Mikado version 2.3.2
BUSCO (embryophyta database version 10), and (3) gene                                 (Venturini et al., 2018), by comparing the predicted gene
prediction assessment with EnTAP version 0.10.8 (Hart                                 models to the current reference annotations.
et al., 2020) using a 70% reciprocal functional annotation
approach with NCBI's RefSeq Plant and UniProt databases.
The mono:multi ratio was calculated from the gFACs                                    Post‐processing ﬁltering
summary report run with default parameters (Caballero and
Wegrzyn, 2019). We regard a mono:multi ratio near 0.2 to                              The predicted gene models for Liriodendron were taken a
be ideal and have further validated this with a larger set of                         step further to reﬁne the genome annotation. Post‐process
IMPROVING NON‐MODEL PLANT GENOME ANNOTATION                                                                                               |   5 of 17



ﬁltering was performed using gFACs and assessed for                         downloaded, contigs <500 bp were removed. The published
improvement using BUSCO completeness scores and                             genome assemblies and annotations were compared in terms
annotation rates. The mono‐exonic and multi‐exonic genes                    of completeness using BUSCO (Figure 1, Table 2). When
predicted for Liriodendron were ﬁltered for unique genes.                   BUSCO is run in genome mode, it searches the genome for a
The mono‐exonic genes were further ﬁltered for the                          set of 1614 single‐copy orthologs in the embryophyte
presence of protein domains using InterProScan version                      database. Aside from Funaria, which had the lowest
5.35‐74.0 and Pfam (Quevillon et al., 2005; Jones et al., 2014).            completeness score of 82.4%, the remaining plant genomes
Multi‐exonic genes that did not have an EggNOG (Huerta‐                     ranged from 94% to 99% complete. When we evaluated the
Cepas et al., 2019) or a sequence similarity hit were                       published annotations for the same species and ran BUSCO
removed, and the ﬁnal annotation was assessed using                         in protein mode, a slightly lower level of completeness was
gFACs and EnTAP.                                                            observed in every species except Funaria and Arabidopsis
                                                                            (Figure 1B). The largest reduction in BUSCO score was
                                                                            observed in Liriodendron (98.6% vs. 75.1%). The discrepancy
RESULTS                                                                     between the estimated completeness at the genome‐level and
                                                                            most of the published annotations speaks to the challenges of
Genome sizes, repeats, and published                                        achieving an accurate structural annotation.
annotations                                                                     RepeatModeler2 with and without the LTRStruct package
                                                                            (the additional LTR masking module) (Flynn et al., 2020) was
The genome sizes of the ﬁve species assessed represented a                  used to soft‐mask the repeats in four of the genomes. The
10‐fold diﬀerence between the smallest (Arabidopsis ~119                    increase in repeat content was marginal in all species, ranging
Mbp) and the largest (Liriodendron ~1.7 Gbp) (Figure 1A,                    from 1% in Funaria to 5% in Populus. Comparisons using the
Table 2). Liriodendron and Rosa have higher levels of repeat                LTRStruct ﬂag were denoted as RM2+ (Appendix S5).
content (73.18% and 60.58%, respectively), and Arabidopsis
has the lowest (23.9%). Arabidopsis is the most complete
chromosome‐scale genome, with seven contigs reﬂecting its                   Transcriptome evidence
ﬁve chromosomes and two organellar chromosomes. The
other genomes are assembled into pseudochromosomes                          For the subsequent genome annotation analysis, the
(except for Liriodendron). Once the genomes were                            Illumina RNA short reads were ﬁrst aligned to the genome.




F I G U R E 1 Genome size, repeat content, and BUSCO completeness for the ﬁve plant genomes: Arabidopsis thaliana, Populus trichocarpa, Funaria
hygrometrica, Rosa chinensis, and Liriodendron chinense. Each pie represents the BUSCO completeness. Green denotes the completeness score, orange
indicates the fragmented score, and blue indicates the missing score from BUSCO. (A) BUSCO scores estimated from the published assemblies. (B) BUSCO
scores estimated from protein‐coding gene predictions from the published annotations.
6 of 17    |                                                                                  IMPROVING NON‐MODEL PLANT GENOME ANNOTATION



TABLE 2        Genome assembly and annotation statistics for the ﬁve published plant genomes.
                                                                                                                      BUSCO completeness
 Species                   Genome size (Mbp)       Total scaﬀolds (chromosomes)       N50 (Mbp)      Repeat content   Genome    Annotation
 Arabidopsis thaliana       119                       7 (5)                           23.46          23.6%            99.30%    99.60%

 Funaria hygrometrica       327                     687 (26)                           1.48          42.35%           85.60%    86.60%

 Liriodendron chinense     1742                    3711 (21)                           3.53          73.18%           98.60%    75.10%

 Populus trichocarpa        434                    1446 (19)                          19.47          35.90%           98.80%    98.30%

 Rosa chinensis             515                      55 (7)                           69.64          60.53%           98.80%    97.30%



All libraries, ranging from four to 20 per species, aligned at               published annotations (Figure 2B, Appendix S8). Overall,
over 97%, apart from Rosa (92%) (Table 3, Appendix S6).                      the StringTie2 predictions had higher sensitivity and
Long‐read RNA libraries were aligned with Minimap2 for                       precision rates than the Trinity runs. From this point,
four species: Arabidopsis (ONT PromethION reads, 97.1%                       Trinity was excluded, and StringTie2 runs were compared
aligned), Populus (PacBio Iso‐Seq reads, 92.01% aligned),                    against the BRAKER and TSEBRA predictions (Figure 2B).
Liriodendron (PacBio Iso‐Seq reads, 95.5% aligned), and                          The mono:multi ratios produced by StringTie2 ranged
Rosa (ONT PromethION reads, 99% aligned). The N50s for                       from 0.15 in Populus (ST2 (LR)) to 0.53 in Liriodendron (ST2
the long reads range from 976 bp in Rosa to 4.6 kbp in                       (LR)), which were an improvement over the mono:multi
Liriodendron (Appendix S7).                                                  ratios produced from the BRAKER annotations that ranged
                                                                             from 0.37 in Arabidopsis (BR (LR)) to 1.27 in Funaria (BR
                                                                             (SR/RM2+)). The BUSCO scores of the proteins predicted
Transcript‐derived annotations                                               from BRAKER were generally higher than the BUSCO scores
                                                                             from StringTie2; for example, Arabidopsis StringTie2 runs
The reads were assembled using StringTie2 (ST2) and                          ranged from 85% (ST2 (LR)) to 95.5% in ST2 (SR), while
Trinity. The Trinity de novo assemblies of the Illumina                      BRAKER runs ranged from 94% (BR (LR)) to 95.9% (BR
short reads generated longer transcripts, with N50s ranging                  (SR)). Some runs are comparable, however; the ST2 (SR) run,
from 1.2 kbp (151,265 transcripts in total) in Funaria to 3.06               BR (SR) run, and the BR (SR/RM2+) run in Arabidopsis all
kbp (2,839,867 transcripts) in Liriodendron. Among the                       had a BUSCO score of 95%. StringTie2‐predicted models had
genome‐guided assemblies with StringTie2 (ST2 (SR)), the                     a higher annotation rate, in general, than BRAKER; for
range was much smaller, with N50s ranging from 369 bp                        example, the EnTAP annotation rate in Funaria was just over
(59,741 transcripts in total) in Funaria to 2.54 kbp (37,747                 40% post‐BRAKER but was near 60% from the StringTie2
transcripts) in Arabidopsis (Appendix S7). The StringTie2                    runs (Figure 3).
(ST2 (LR) and ST2 (SR/LR)) range was longer, with N50s
ranging from 1.07 kbp (20,633 transcripts in total) in Rosa
ST2 (LR) to 2.36 kbp (45,785 transcripts) in Liriodendron                    Genome annotation with MAKER
ST2 (SR/LR) (Table 3, Appendix S7). The StringTie2 and
Trinity transcripts were aligned back to the genome using                    To replicate the repeat pipeline of MAKER‐P, the RM2+
GMAP after the frame selection. The BUSCO scores for the                     genome was used for the MAKER runs for Arabidopsis,
aligned transcriptomes derived from short‐read data, run in                  Populus, and Funaria. BUSCO completeness was low
transcriptome mode, ranged from 73% in Funaria to 83% in                     compared with the BRAKER runs, ranging from 19.6% in
Rosa for Trinity, and 73% in Liriodendron to 97% in Rosa                     Populus to 90.4% in Arabidopsis (Figure 4A). The mono:
using StringTie2 (Table 3). The BUSCO scores were the                        multi ratio of MAKER(RM2+) for Arabidopsis was compa-
lowest for the ST2 (LR) runs across all species, as compared                 rable to the BRAKER runs for the same species (0.22 for BR
to the other StringTie2‐only runs. For ST2 (SR/LR), the                      (SR) and BR (SR/RM2+), 0.24 for BR (LR), and 0.23 for BR
BUSCO scores were lower than for ST2 (SR), except for                        (SR/LR)). The MK (RM2+) predictions for the total number
Rosa, where the ST2 (SR/LR) was 97.2% as opposed to                          of genes in Arabidopsis (22,000) and Funaria (44,000) were
97.0% in ST2 (SR). In all species, ST2 (SR/LR) had higher                    in the expected range for these species, whereas only 7000
BUSCO scores than ST2 (LR). Despite Trinity producing                        genes were predicted for Populus. The average gene lengths
more than double the total transcripts than StringTie2, the                  ranged from 1.8 kbp in Funaria to 2.3 kbp in Arabidopsis
BUSCO completeness scores of most StringTie2 runs were                       (Appendix S9). The best MK (RM2+) run was for
much higher than that of Trinity. Liriodendron remained                      Arabidopsis, with a mono:multi ratio of 0.22 and a BUSCO
the only exception, with a slightly higher BUSCO score                       score of 90.4%. On the other hand, the mono:multi ratio for
from Trinity.                                                                Populus was 0.07, and the BUSCO score was 19.6%.
    Arabidopsis and Populus were further evaluated with                          The model systems, Arabidopsis and Populus, were
Mikado to compare the sensitivity and speciﬁcity of the                      further evaluated with Mikado to compare the sensitivity
IMPROVING NON‐MODEL PLANT GENOME ANNOTATION                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |   7 of 17



                                                                                                                                                                                                                                                                                                                                                                                                                                                            and speciﬁcity of the published annotations (Figure 2B,




                                                                                                                                                                                                                                    Note: LR = long reads; RM = RepeatModeler2; RM2+= RepeatModeler2 with the LTRStruct ﬂag; RM% = repeat content masked with RepeatModeler2; RM2 + % = repeat content masked with RepeatModeler2 with the LTRStruct ﬂag;
                                                                                                                                                                                                                                                                                                                                                                                                                                                            Appendix S8). The sensitivity and precision scores for


                                                                                                              (SR/


                                                                                                                                       93.6



                                                                                                                                                                           77.3

                                                                                                                                                                                                65.3

                                                                                                                                                                                                                  97.2
                                                                                                              ST2

                                                                                                              LR)
                                                                                                                                                                                                                                                                                                                                                                                                                                                            gene predictions were lowest from MAKER, followed by
                                                                                                                                                                                                                                                                                                                                                                                                                                                            Trinity, and were highest from TSEBRA. StringTie2 and
                                                                                           BUSCO transcript



                                                                                                                                                                                                                                                                                                                                                                                                                                                            BRAKER yielded similar sensitivity and speciﬁcity scores for
                                                                                                                   (SR)
                                                                                                                                       95.5

                                                                                                                                                         84.5

                                                                                                                                                                           87.1

                                                                                                                                                                                                73.3
                                                                                                                   ST2




                                                                                                                                                                                                                  97
                                                                                           alignments (%)



                                                                                                                                                                                                                                                                                                                                                                                                                                                            Arabidopsis, whereas for Populus the sensitivity score was
                                                                                                                                                                                                                                                                                                                                                                                                                                                            lower than those from the BRAKER runs. Given its overall
                                                                                                                                                                                                                                                                                                                                                                                                                                                            low scores, MAKER was excluded from the subsequent
                                                                                                                   Trinity
                                                                                                                   (SR)




                                                                                                                                                                                                                                                                                                                                                                                                                                                            comparisons. It should be noted, however, that some
                                                                                                                                       82.7

                                                                                                                                                         72.9

                                                                                                                                                                           92.5

                                                                                                                                                                                                71.3

                                                                                                                                                                                                                  88.8
                                                                                                                                                                                                                                                                                                                                                                                                                                                            protocols recommend using GeneMark in MAKER (Brůna
                                                                                                                                                                                                                                                                                                                                                                                                                                                            et al., 2021). With this addition to the training protocol,
                                                                                                                                                                                                                                                                                                                                                                                                                                                            MAKER was shown to have a higher accuracy in prediction.
                                                                                                              transcripts (SR/


                                                                                                                                       42,265 (1363)



                                                                                                                                                                           45,785 (2361)

                                                                                                                                                                                                37,222 (1869)

                                                                                                                                                                                                                  105,639 (1605)
                                                                                                              LR) (N50)
                                                                                                              Total ST2




                                                                                                                                                                                                                                                                                                                                                                                                                                                            Genome annotation with BRAKER

                                                                                                                                                                                                                                                                                                                                                                                                                                                            In general, the BUSCO scores were improved in the
                                                                                                                                                                                                                                                                                                                                                                                                                                                            BRAKER and TSEBRA runs, with the TSB (SR/OrthoDB)
                                                                                                                                       36,241 (1599)



                                                                                                                                                                           33,895 (1815)

                                                                                                                                                                                                20,633 (1074)




                                                                                                                                                                                                                                                                                                                                                                                                                                                            predictions scoring the highest. The best BUSCO scores
                                                                                                                                                                                                                  74397 (1866)
                                                                                                              (LR) (N50)
                                                                                                              transcripts
                                                                                                              Total ST2




                                                                                                                                                                                                                                                                                                                                                                                                                                                            were from TSB (SR/OrthoDB), ranging from 98.9% (TSB;
                                                                                                                                                                                                                                                                                                                                                                                                                                                            SR/OrthoDB) in Arabidopsis to 82.2% in Funaria. Overall,
                                                                                                                                                                                                                                                                                                                                                                                                                                                            the TSEBRA runs fared better, with the annotation
                                                                                                                                                                                                                                                                                                                                                                                                                                                            completeness rates ranging from 99% in Arabidopsis (TSB;
                                                                                                                                                                                                                                                                                                                                                                                                                                                            SR/OrthoDB) to 53% in Funaria. On the other hand, the
                                                                                                                                                                                                                                                                                                                                                                                                                                                            TSEBRA runs had the worst mono:multi ratios; for
                                                                                                                                       37,747 (2538)



                                                                                                                                                                           62,341 (1041)
                                                                                                                                                         59,741 (369)



                                                                                                                                                                                                56,468 (402)

                                                                                                                                                                                                                  53,708 (672)
                                                                                                              (SR) (N50)
                                                                                                              transcripts
                                                                                                              Total ST2




                                                                                                                                                                                                                                                                                                                                                                                                                                                            example, the highest TSB (SR/ST2/RM2+) ratio was 1.27
                                                                                                                                                                                                                                                                                                                                                                                                                                                            for Funaria (Figure 4).
 Comparison between genome‐guided (StringTie2) and de novo (Trinity) genome annotations.




                                                                                                                                                                                                                                                                                                                                                                                                                                                                Overall, the gene models generated for Arabidopsis by
                                                                                                                                                                                                                                                                                                                                                                                                                                                            BRAKER performed similarly across runs when evaluated
                                                                                                                   transcripts (N50)




                                                                                                                                                                                                                                                                                                                                                                                                                                                            using BUSCO scores. The mono:multi ratios across
                                                                                                                                       319,434 (2726)

                                                                                                                                                         151,265 (1198)

                                                                                                                                                                           2,839,867 (3055)

                                                                                                                                                                                                283,572 (1837)

                                                                                                                                                                                                                  812,407 (2187)
                                                                                                                   Total Trinity




                                                                                                                                                                                                                                                                                                                                                                                                                                                            BRAKER runs ranged from 0.23 to 0.39, and the annotation
                                                                                                                                                                                                                                                                                                                                                                                                                                                            rates were consistently above 95%.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                The annotation rates for Funaria were lower than
                                                                                                                                                                                                                                                                                                                                                                                                                                                            expected: 43% for BR (SR) and 53% for nearly all methods
                                                                                                                                                                                                                                                                                                                                                                                                                                                            that included protein evidence (TSB (SR/TRINITY) and
                                                                                                                   Total long reads




                                                                                                                                                                                                                                                                                                                                                                                                                                                            TSB (SR/OrthoDB)). The BUSCO completeness scores of
                                                                                                                   (total libraries)
                                                                                                                                       23,134,068 (4)



                                                                                                                                                                           10,437,029 (1)

                                                                                                                                                                                                161,334 (1)

                                                                                                                                                                                                                  41,929,383 (6)




                                                                                                                                                                                                                                                                                                                                                                                                                                                            about 85% post‐BRAKER are comparable to those from
                                                                                                                                                                                                                                                                                                                                                                                                                                                            StringTie2.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                In the case of the Liriodendron BRAKER and TSEBRA
                                                                                                                                                                                                                                                                                                                                                                                                                                                            runs, the mono:multi ratios were more variable when
                                                                                                                                                                                                                                                                                                                                                                                                                                                            compared to the StringTie2 runs, which ranged from 0.34
                                                                                                                                                                                                                                                                                                                                                                                                                                                            BR (SR) to 1.04 with BR (SR/RM2+). The annotation rates
                                                                                                                                                                           1,408,831,670 (20)
                                                                                                                   Total short reads


                                                                                                                                       511,277,126 (9)

                                                                                                                                                         549,205,030 (9)



                                                                                                                                                                                                267,403,772 (5)

                                                                                                                                                                                                                  134,461,068 (4)




                                                                                                                                                                                                                                                                                                                                                                                                                                                            for each run were around 75%, with BUSCO scores from
                                                                                                                   (total libraries)




                                                                                                                                                                                                                                                                                                                                                                                                                                                            83% with TSB (SR/LR/ST2) to 90.8% for BR (SR). Populus
                                                                                                                                                                                                                                                                                                                                                                                                                                                            gene models post‐BRAKER without protein evidence had
                                                                                                                                                                                                                                                                                                                                                                                                                                                            mono:multi scores around 0.24, and with TSEBRA, the ratio
                                                                                                                                                                                                                                                                                                                                                                                                                                                            ranged from 0.4 to 0.5. The annotation rates also diﬀered
                                                                                                                                                                                                                                                                                                                                                                                                                                                            between BR (SR) (75%) and TSB (SR/ST2) (88%). Rosa had
                                                                                                                            RM2 + %




                                                                                                                                                                                                                                                                                                                                                                                                                                                            overall consistent scores (around 96%) for BUSCO post‐
                                                                                                                                                                                                                                    SR = short reads; ST2 = StringTie2.
                                                                                                                                       16.5

                                                                                                                                                         43.1

                                                                                                                                                                           72.7

                                                                                                                                                                                                45.1




                                                                                                                                                                                                                                                                                                                                                                                                                                                            BRAKER. TSEBRA runs had higher mono:multi ratios (0.75)
                                                                                                                                                                                                                                                                                                                                                                                                                                                            compared with the BRAKER runs (0.37) (Appendix S9).
                                                                                                                            RM%
                                                                                                                                       15.2

                                                                                                                                                         42.3

                                                                                                                                                                           73.2

                                                                                                                                                                                                35.9

                                                                                                                                                                                                                  60.5
                                                                                                                                                                           Liriodendron




                                                                                                                                                                                                                                                                                                                                                                                                                                                            Annotation with long reads
                                                                                                                                       Arabidopsis
 TABLE 3




                                                                                                                                                         Funaria



                                                                                                                                                                                                Populus
                                                                                                                            Species




                                                                                                                                                                                                                  Rosa




                                                                                                                                                                                                                                                                                                                                                                                                                                                            For BRAKER runs, the predicted gene lengths from the long
                                                                                                                                                                                                                                                                                                                                                                                                                                                            reads were comparable with those based on short reads,
8 of 17   |                                                                                 IMPROVING NON‐MODEL PLANT GENOME ANNOTATION




F I G U R E 2 Comparison of BUSCO, sensitivity, and false positive rates between the Arabidopsis and Populus annotations (Appendix S8). (A) BUSCO
completeness scores for the MK (SR/RM2+) and BR (SR/RM2+) runs of Arabidopsis and Populus. Green denotes the completeness score, orange indicates
the fragmented score, and blue indicates the missing score from BUSCO. (B) False positive rates and sensitivity scores from Mikado against published
annotations for Arabidopsis (red) and Populus (gold) for the MAKER, BRAKER, TSEBRA, Trinity, and StringTie2 runs. The scores were assessed using
Mikado. Multiple points per run reﬂect diﬀerences in input read type and repeat masking.


except for some runs with long reads within Populus. The                    ST2) is comparable to the BR (SR) reads in terms of BUSCO
average gene length for BRAKER with long reads for                          completeness. Exceptions to this case are Arabidopsis and
Populus ranged from 2.7 kbp to 3.4 kbp, although some                       Rosa, which had marginally higher BUSCO completeness
transcripts exceed 6 kbp. The longest average gene lengths                  scores. BR (SR/LR) runs produced more genes (in total) for
were observed in Liriodendron (9.3 kbp; BR (SR/LR)). The                    Arabidopsis, Populus, and Rosa than BR (SR); however,
inclusion of long reads (exclusively) did not improve                       fewer genes were identiﬁed in the TSB (SR/LR/ST2) runs
BUSCO completeness for any species, apart from Arabi-                       than for BR (SR), apart from in Rosa. The annotation rate in
dopsis, where the BR (LR) BUSCO completeness was 1%                         the BR (SR/LR) of Liriodendron was higher than its BR (SR).
higher than for the BR (SR) run. The increase in BUSCO                      The combination of proteins with SR and LR (TSB (SR/LR/
completeness in Arabidopsis could be due to the large                       ST2)) resulted in higher annotation rates across all species.
number of long reads included (23 million across four                       The combination of SR and LR increased the mono:multi
libraries); however, the quality of genome annotation does                  ratios, which were therefore worse across all species.
not seem correlated with the depth of long‐read sequencing.
For example, Rosa had more reads (41 million across six
libraries), and the BR (LR) run had a similar BUSCO score                   Reﬁning the genome annotation for
to BR (SR) (96%). It should be noted that the long reads for                Liriodendron
Arabidopsis and Rosa were sequenced with ONT Pro-
methION. The PromethION reads had higher mapping                            The BRAKER runs for Liriodendron were ﬁltered with
rates, compared with Iso‐Seq, to their respective genomes:                  gFACs and InterProScan to remove unlikely gene models
97.1% in Arabidopsis and 99% in Rosa (Appendix S6). The                     (Table 4). The number of mono‐exonic genes was
long‐read inputs, regardless of depth or type, lowered the                  drastically reduced post‐ﬁlter with InterProScan. Across
BUSCO completeness (up to 10%) across all ST2 (LR) runs                     all runs, the mono‐exonic genes numbered 11,000 to 25,000.
(Appendix S10). Finally, we note that the combination of                    After removing mono‐exonics without a protein domain
short reads and long reads (BR; SR/LR and TSB; SR/LR/                       annotation from the Pfam database, they decreased from
IMPROVING NON‐MODEL PLANT GENOME ANNOTATION                                                                                        |   9 of 17




F I G U R E 3 Comparing metrics between BRAKER (blue) and StringTie2 (red) predictions. (A) Mono:multi ratios, (B) BUSCO comparisons, and
(C) EnTAP annotation rates of the gene models. The yellow region indicates the ideal value for each of the metrics.



13,000 to 5000. The decrease in false positive mono‐exonics              high‐throughput transcriptomics, in the form of both short‐ and
resulted in an improved mono:multi ratio that ranged from                long‐read evidence, become more accessible, rapid approaches
0.16 for BR (SR) and BR (SR/RM2+), 0.16 and 0.23 for the                 such as StringTie2 (cited 451 times [Kovaka et al., 2019]) are
StringTie2 runs, to 0.43 for the TSEBRA runs. The BUSCO                  occasionally used as the exclusive approach, although they are
scores decreased slightly post‐ﬁltering (1–2%). EnTAP                    more often used in combination with the options listed above.
annotation rates ranged from 66% to 86%, with the TSB                         Regardless of the methods selected, recently published
(SR/OrthoDB), which is an improvement from 59% to 68%                    benchmarks demonstrate the challenge of achieving high
pre‐ﬁltering.                                                            values for gene sensitivity in larger genomes (Brůna et al., 2021).
    In terms of BUSCO completeness and mono:multi                        Within smaller and less complex model systems such as
ratios, the two best‐performing runs (BR (SR) and BR                     Caenorhabditis elegans and Drosophila melanogaster, the ab
(SR/LR)) were further ﬁltered (Table 4). In this step, multi‐            initio prediction results in gene sensitivities of 49.8% and
exonic genes without an EggNOG alignment or a sequence                   59.5%, respectively (Brůna et al., 2021). In well‐studied
similarity alignment through EnTAP were removed. These                   complex organisms, such as humans, the gene‐level sensitivity
ﬁltered models were re‐assessed for their mono:multi ratio,              and speciﬁcity hovers at 48% and 43%, respectively (Banerjee
BUSCO completeness, and EnTAP annotations. The                           et al., 2021). While generating benchmarks with model systems
BUSCO completeness remained the same for BR (SR), but                    (A. thaliana, C. elegans, and D. melanogaster) provides more
not for BR (SR/LR). The EnTAP annotation increased from                  reliable metrics for comparison, they do not fully represent the
66% to 81% in BR (SR), and 67% to 87% in BR (SR/LR).                     diversity of their respective clades (Chang et al., 2016).
                                                                              This study focused on four gene prediction workﬂows,
                                                                         StringTie2, MAKER, BRAKER, and BRAKER/TSEBRA, and
DISCUSSION                                                               examined the process across a variety of evidence inputs.
                                                                         Both model and non‐model plant genomes were considered
BRAKER (Hoﬀ et al., 2019; Brůna et al., 2021) and MAKER                  to highlight the challenges and reinforce the need for
(Cantarel et al., 2008) are currently the most popular eukaryotic        downstream ﬁltering.
structural annotation tools, cited 475 and 1010 times,
respectively, since 2021, as referenced in Google Scholar
(https://scholar.google.com/). Processes that select from multiple       Genome annotation benchmarks for both
ab initio or aligned forms of evidence are gaining popularity as         models and non‐models
well, although they add both time and complexity to the
analyses (FINDER cited 22 times [Banerjee et al., 2021];                 Among plant genomes, the total number of genes is
EVidenceModeler cited 381 times [Haas et al., 2008]). Finally, as        relatively conserved and ranges from 20,000 to just over
10 of 17   |                                                                              IMPROVING NON‐MODEL PLANT GENOME ANNOTATION




F I G U R E 4 Comparison of scores across all species between the runs of diﬀerent input types and software. (A) BUSCO completeness scores.
(B) Mono:multi ratios. (C) EnTAP annotation rates. MAKER is shown in green, BRAKER is light blue, TSEBRA is dark blue, and StringTie2 is red. The
yellow rectangle represents the target scores for each benchmark. RM2+, RepeatModeler2 with LTRStruct.



40,000. As such, the total gene number provides an                         high‐quality reference annotation. Poor BUSCO scores are
accessible preliminary benchmark; however, the number                      immediately indicative of a larger issue; however, a high
of genes in the reference annotation cannot be used to assess              BUSCO score is not suﬃcient to estimate the quality of an
the overall quality of the annotation. To measure this, we                 annotation (Figure 4B). Six of the 18 BRAKER runs and
should consider additional metrics. Here, we describe the                  four of the 17 StringTie2 runs exceeded 95% completeness,
utility of the BUSCO score, mono:multi‐exonic ratio, and                   but their total gene number, gene length, and structure
sequence similarity assessment.                                            varied considerably.
     BUSCO allows us to identify complete, duplicated,                         Repeat content, especially in the form of LTRs, and
fragmented, and missing single‐copy orthologs shared by                    pseudogenes can lead to inﬂated gene model estimates,
most seed plants (Simão et al., 2015; Seppey et al., 2019).                especially for mono‐exonic genes (Scott et al., 2020;
This provides a reliable benchmark in the absence of a                     Trouern‐Trend et al., 2020). We expect that eukaryotes
IMPROVING NON‐MODEL PLANT GENOME ANNOTATION                                                                                       |   11 of 17



T A B L E 4 Gene model statistics for Liriodendron after two rounds of       of the tree of life, this might be a less reliable metric. Some
structural and functional ﬁlters.                                            species may fare poorly in database comparisons, so
    Liriodendron          Total       Mono:multi                             searches for protein domains could provide some level of
    annotationa           genes       ratio          BUSCO %   EnTAP %       conﬁdence. We demonstrate this as a ﬁlter to reduce the
    Published             35,261      0.7            75.1      63            mono‐exonics in Liriodendron (Table 4).
       annotation

    Mono‐exonic ﬁlters                                                       Repeat masking is important but may not
    BR (LR)               39,031      0.21           87.4      69
                                                                             require additional LTR resolution to improve
                                                                             performance
    BR (SR) *             41,065      0.16           90.2      66

    BR (SR/LR) *          40,420      0.16           90.3      67            Plant genomes typically contain many repeats, mostly in the
                                                                             form of TEs, averaging around 46% of the genome (Luo
    BR (SR/RM2+)          40,740      0.17           88.2      67
                                                                             et al., 2022). Given the abundance of TEs in genomes, it is
    ST2 (SR)              51,804      0.16           86.5      80            important to mask these in advance of gene prediction. Soft
    ST2 (LR)              27,012      0.23           65        84            masking involves changing nucleotides identiﬁed as repeats
                                                                             to lowercase letters (Yandell and Ence, 2012), signaling
    ST2 (SR/LR)           36,345      0.24           70.6      82
                                                                             downstream programs to ignore these sequences. Of the ﬁve
    TSB (LR/ST2)          33,132      0.43           82.3      84            genomes included in this study, Liriodendron had the largest
    TSB (SR/              33,964      0.43           82.4      84
                                                                             genome size and highest repeat content. Running down-
       LR/ST2)                                                               stream analyses on an unmasked genome of Liriodendron
                                                                             resulted in a four‐fold increase in gene predictions
    TSB (SR/ST)           32,898      0.41           83.4      84
                                                                             (Figure 5A, Appendix S11). Many repeats were identiﬁed
    TSB (SR/              33,637      0.45           82.8      84            as putative gene models, resulting in a large increase in the
       ST2/                                                                  total number of genes (Figure 5B, Appendix S11).
       RM2+)
                                                                                 RepeatModeler2 is a widely used tool for TE discovery
    TSB (SR/              34,646      0.42           84        83            (Flynn et al., 2020). The recent release of RepeatModeler2
       TRINITY)                                                              includes an optional module for more robust LTR structural
    TSB (SR/              33,667      0.43           86.5      86            detection (LTRStruct module) that includes the LTRharvest
       OrthoDB)                                                              (Ellinghaus et al., 2008), LTRDetector (Valencia and
                                                                             Girgis, 2019), and LTR_retriever packages (Ou and
    +Multi‐exonic ﬁlters                                                     Jiang, 2018). This is particularly useful in identifying more
    BR (SR)               30,219      0.24           90.3      81            divergent LTRs in the genome that may exist in fewer copies
                                                                             (Ou and Jiang, 2018; Valencia and Girgis, 2019). Among the
    BR (SR/LR)            30,035      0.23           86.9      87            default packages included, RepeatScout serves as a fast
Note: BR = BRAKER; BUSCO % = completeness percentage; EnTAP % = annotation   method for detecting young and abundant repeat families in
rates after reciprocal BLAST; LR = long reads; RM2+ = RepeatModeler2 with    the genome. RECON, on the other hand, is more
LTRStruct; SR = short reads; ST2 = StringTie2; TSB = TSEBRA.
a                                                                            computationally intensive and is sensitive enough to detect
    Asterisks denote the two best annotation sets.
                                                                             older TE families. The LTRStruct module is run on the
                                                                             unmasked genome to identify LTR families that may be
                                                                             redundant with the families identiﬁed by the default
maintain 20% or less of their gene space as mono‐exonics                     package; this creates redundancy that is resolved through
(Jain et al., 2008; Appendix S4). Although the BUSCO                         clustering with CD‐HIT (Flynn et al., 2020).
scores were consistent, we note tremendous variation in the                      In the four species compared, additional repeat masking
mono‐ to multi‐gene model ratios post‐BRAKER. In                             did not signiﬁcantly improve gene predictions (Figure 4,
practice, having a worse mono:multi ratio is preferable to                   Appendix S10). The mono:multi ratios across species were
having a lower BUSCO score, as missing genes, especially                     consistent before and after additional LTR masking
those thought to be conserved, cannot be easily rectiﬁed,                    (Figure 5A). The BUSCO completeness scores remained
while putative false positives may be ﬁltered out through                    relatively the same, with BR (SR/RM2+) being 1% higher
other means.                                                                 than BR (SR) in Arabidopsis, Funaria, and Populus. The
    Sequence similarity search metrics are more complex to                   marginal improvement observed in these genomes could be
interpret, but can provide a benchmark when used with                        related to the structure and type of LTRs, such as the better
high‐quality and curated databases that contain full‐length                  identiﬁcation of divergent Ty1‐copia elements described in
proteins (e.g., NCBI RefSeq). Speciﬁcally, a reciprocal                      the Funaria genome (Kirbis et al., 2022). Although we did
BLAST search requires that both the query and target in                      not include genomes with excessive repeat estimates
the search retain a minimum level of coverage in the                         (>70%), our results indicated that the optional LTRStruct
alignment. For new plant genomes in the darkest branches                     module was not beneﬁcial.
12 of 17   |                                                                                 IMPROVING NON‐MODEL PLANT GENOME ANNOTATION




F I G U R E 5 The eﬀect of soft masking on gene prediction in Liriodendron (Appendix S11). (A) Performing structural annotation on the unmasked
Liriodendron genome results in the identiﬁcation of more mono‐exonic genes as opposed to multi‐exonic genes. Blue denotes the BRAKER (BR) runs for
both genomes, SR denotes short reads, and LR denotes long reads. The lighter shade represents mono‐exonics, and the darker shade represents the multi‐
exonics. (B) More genes predicted using the unmasked genome (blue), as compared with only one gene predicted in this region with the masked genome
(red). The green track shows the long terminal repeat elements in the genome as identiﬁed by RepeatModeler2. The RNA alignment reads show a read
pile‐up at the predicted gene (masked track).



Transcripts derived directly from alignments                                 much more challenging, computationally intensive, and
are not suﬃcient to annotate reference                                       prone to error.
genomes                                                                          We compared the accuracy of annotations produced by
                                                                             StringTie2, the accuracy of de novo–assembled transcripts
Transcriptome assemblers are designed to work with                           with Trinity, and the accuracy of annotations produced by
primarily short RNA‐Seq reads to construct full‐length                       BRAKER. The selected packages are top performers when
transcripts. In the presence of a high‐quality reference                     compared in their respective categories of genome‐guided
genome, genome‐guided approaches are preferred, as the                       and de novo transcriptome assembly (Sahraeian et al., 2017;
reads are aligned directly to the target genome in advance.                  Venturini et al., 2018). As expected, Trinity produced a
Aligned RNA evidence provides resolution on exon                             higher number of transcripts than StringTie2, and BUSCO
boundaries, and aids in the identiﬁcation of splice variants.                completeness was consistently lower (Table 3), except for
De novo approaches build graph models directly from the                      Liriodendron. The gene models generated by StringTie2
short (or long) reads to generate transcripts. The latter is                 were more numerous than the BRAKER gene models,
IMPROVING NON‐MODEL PLANT GENOME ANNOTATION                                                                          |   13 of 17



resulting in more than was expected for each species. It           addition of OrthoDB, given the phylogenetic placement of
should be noted, however, that StringTie2 identiﬁes splice         Rosa in comparison to Arabidopsis. On the other hand, the
variants by generating a splice graph and resolving conﬂict        annotation rate of TSB (SR/OrthoDB) was similar to that of
between multiple potential splice sites (Kovaka et al., 2019),     the other runs in Rosa. The higher quality of the Rosa
whereas BRAKER trains an internal algorithm, GeneMark‐ET,          genome assembly, compared with the other two non‐
to ﬁnd speciﬁc genes with complete support among all introns       models, could also inﬂuence the utility of the protein
to be further used in training AUGUSTUS (Hoﬀ et al., 2019).        evidence; however, the mono:multi ratios remained high,
    The StringTie2 runs resulted in lower BUSCO com-               and annotation rates were similar to those of the runs
pleteness than the BRAKER and/or TSEBRA runs                       without OrthoDB proteins.
(Figure 4A, Appendix S12). This outcome is supported by                TSEBRA runs with proteins sourced from genome‐
the lack of ab initio prediction with genome‐guided                guided predictions performed similarly, but had lower
approaches. Inﬂated mono‐exonic predictions (and lower             BUSCO scores, higher mono:multi ratios, and lower total
BUSCO scores) were also observed in the StringTie2                 gene numbers when compared with the short read–only
genome annotation of the water strider (Microvelia longipes)       runs (Figure 4A, Appendix S10). Among the TSEBRA runs,
(Toubiana et al., 2021). In our study, the Rosa ST2 (SR/LR)        Trinity fares better only for Liriodendron, which could
run was closest to the BRAKER runs, with a BUSCO score             indicate that genome‐guided proteins are not a suitable
of 97.2%, BR (SR/LR) of 96.9%, and TSB (SR/ST2) of 98%             choice for a more repetitive genome. This is consistent with
(Appendices S10, S12).                                             the independent assessments between the de novo tran-
                                                                   scriptome assemblers and genome‐guided assemblers with
                                                                   complex genomes with fragmented genome assemblies (e.g.,
Genome annotations are improved when                               in Aedes albopictus [Huang et al., 2016]). TSEBRA with full‐
combining published full‐length protein                            length proteins sourced from OrthoDB had lower BUSCO
sequences and read data                                            scores when compared to BR (SR) for the non‐model
                                                                   species Liriodendron and Funaria.
The performance of StringTie2 and the Trinity‐derived                  The total number of genes predicted by the TSEBRA
protein evidence was assessed on the predicted gene models         and BRAKER runs remained largely the same across all
using BRAKER and TSEBRA. In this context, the genome‐              species (Appendix S10). However, it should be noted that
guided or de novo–assembled transcripts were translated            the number of mono‐exonic genes increased, whereas the
into proteins and provided as evidence to train the ab initio      multi‐exonic genes decreased, across all TSEBRA runs
component of the pipelines. Adding protein evidence to             relative to the BRAKER runs without proteins across all
genome annotations can target protein‐coding genes,                species. The average gene lengths also decreased, while the
leading to more accurate predictions than RNA‐Seq                  average lengths of mono‐exonics remained the same, and
evidence alone (Bruna, 2022). This study speciﬁcally               the lengths of multi‐exonics were higher.
focused on using protein evidence derived in some fashion              Our initial examination of the EnTAP reciprocal BLAST
from the transcriptomic inputs, but also evaluated the             assessment revealed high annotation rates for the non‐
recommendation to include clade‐speciﬁc OrthoDB protein            model species when protein evidence was included,
inputs to the BRAKER/TSEBRA approach.                              particularly the multi‐exonics (whereas the mono‐exonic
    The TSEBRA runs of the model species Arabidopsis and           percentage remained the same) (Appendix S10). However,
Populus were compared with the reference annotations. These        this increase in multi‐exonic annotation proved to be an
runs were the best for the model species in terms of sensitivity   artifact resulting from the reduced numbers of these genes
and speciﬁcity as compared to the MAKER, StringTie2,               using this approach. Direct comparisons of the predictions
Trinity, and BRAKER runs (Figure 4B). The model genomes            revealed that 40–52% of the multi‐exonics were split into
also had very similar BUSCO completeness scores, but               mono‐exonic predictions when comparing the BR (SR) to
diﬀerent mono:multi ratios with the addition of protein            the TSB (SR/ST2) and TSB (SR/OrthoDB) gene models
evidence. As expected, the model genomes beneﬁted the most         predicted using Liriodendron (Appendices S13, S14).
from the inclusion of the external OrthoDB proteins in terms
of annotation rate and BUSCO score (both Arabidopsis and
Populus reference proteins are contained within this resource);    Long reads can be paired with short reads to
however, mono:multi ratio challenges remained consistent           improve model quality
across the TSEBRA runs with varying inputs.
    In the case of non‐model plant genomes, TSEBRA                 Long reads generated from platforms such as ONT or
contributed to higher mono:multi ratios, which was very            PacBio have the potential to resolve splice variants and
evident in Liriodendron; however, the BUSCO scores of the          assemble transcripts more accurately than traditional
non‐protein runs were lower across all runs of Liriodendron        Illumina RNA‐Seq (Amarasinghe et al., 2020). While long
than for all runs using protein evidence. The Rosa TSB (SR/        reads can independently generate transcriptomes, it is
OrthoDB) had the highest BUSCO score across all runs,              recommended to have a combination of short and long
which we believe may have been greatly inﬂuenced by the            reads to achieve greater depth, improved error proﬁles, and
14 of 17   |                                                                   IMPROVING NON‐MODEL PLANT GENOME ANNOTATION



more evidence for splice site resolution (Gonzalez‐Ibeas          substantial ﬁltering to remove false positives. Among the
et al., 2016; Watson and Warr, 2019; Amarasinghe et al., 2020).   less contiguous and more evolutionary distant species
     In this study, we utilized both ONT PromethION and           (Funaria and Liriodendron), the BR (SR) runs performed
PacBio Iso‐Seq long reads. In the latter, we relied on raw        best in terms of BUSCO completeness and mono:multi
reads (not the error‐corrected circular consensus sequenc-        ratios. The overall EnTAP annotation rates were greatly
ing reads) in our comparisons for genome annotations.             improved in runs where OrthoDB proteins were included as
In all cases, long reads (alone) did not outperform short         evidence; however, when considering BUSCO scores and
reads for the BRAKER runs; however, in some cases, the            mono:multi ratios, especially for non‐model species, the BR
combination of short‐read and long‐read inputs was                (SR) runs performed best. For more divergent species (as
beneﬁcial. The Iso‐Seq reads from Populus and Liriodendron        deﬁned by current public databases), BRAKER runs with
had a higher error rate and produced comparable, but              short reads, or short reads and long reads, are advised.
lower, BUSCO scores than the BR (SR) runs. By contrast,                Regardless of approach, the existing pipelines do not
the ONT PromethION long reads used for Arabidopsis and            provide appropriate summary statistics or robust methods
Rosa in the combined runs (BR (SR/LR)) had slightly better        for ﬁltering unlikely gene models. All methods produce
BUSCO completeness than the BR (SR) runs, and similar             more putative false positives than desired. We recommend
mono:multi ratios. Overall, the lower error proﬁle of using       utilizing reciprocal BLAST searches with well‐curated
ONT PromethION reads, supplemented with short‐read                databases containing targets with full‐length proteins (such
data, as well as the use of high‐quality reference genomes,       as NCBI's RefSeq) to identify fragmented models. We also
support the higher BUSCO completeness scores.                     recommend ﬁltering and removing mono‐exonics that do
                                                                  not have a protein domain. Finally, we recommend
                                                                  structural ﬁlters to remove unlikely gene structures (e.g.,
Best practices for plant genome annotation                        splice sites, start sites, incompletes).
                                                                       In this study, we demonstrated the impact of post‐
From the existing tools, we recommend that investigators          ﬁltering on the most complex genome assessed in this study,
utilize RepeatModeler2 to mask their genome of interest           Liriodendron. We improved the published annotation across
with the default settings (Flynn et al., 2020). Following soft    all benchmarks evaluated in this study following a new BR
masking, RNA‐Seq short reads (between 4–10 libraries,             (SR) run (Table 4) (Chen et al., 2019). The ﬁlters reduced
minimum 15 million paired‐end reads per library) are              the overall number of putative false positives and increased
generally suﬃcient for annotation. While we did not               the overall rate of annotation, with minimal reduction to
comprehensively investigate the impact of tissue type, it is      BUSCO completeness.
recommended to sample from multiple tissues when
possible (Kress et al., 2022). In our study, we did not           AUTHOR CONTRIBUTIONS
observe a diﬀerence in the annotation completeness among          The genome annotation software was executed for bench-
species with a higher number of short‐read libraries,             marking purposes with contributions from V.S.V., D.M.,
although we did not comprehensively evaluate the eﬀect            J.B., and B.S. Troubleshooting and statistical evaluation of
of using fewer libraries within a single species.                 the genome annotations were undertaken by C.W., A.B.,
     Sequencing long‐read libraries remains more expensive        K.C.F., S.Z., S.L.M., M.C., and J.L.W. J.L.W. was responsible
than generating deep Illumina short‐read RNA‐Seq cover-           for acquiring the funding. Data analysis and manuscript
age. In most cases, the short reads were a suﬃcient input.        preparation were carried out by V.S.V., with assistance from
The notable exceptions include the BR (SR/LR), as they            C.W., K.C.F., S.Z., and J.L.W. All authors approved the ﬁnal
were comparable, and in some cases slightly better than, the      version of the manuscript.
BR (SR) runs across all species. The PromethION reads had
a lower error proﬁle and were more beneﬁcial when                 ACKNOWLEDGMENTS
combined with short reads; however, current long‐read             The authors would like to thank the Institute for Systems
technologies available from both platforms may provide            Genomics (ISG) and Computational Biology Core at the
diﬀerent results.                                                 University of Connecticut for high‐performance computing
     BRAKER and TSEBRA outperformed runs of MAKER,                services. Thanks go to Dr. Bernard Goﬃnet (University of
StringTie2, and Trinity with default settings. It should be       Connecticut) for his careful review of this manuscript. This
noted that we did not comprehensively benchmark MAKER             work was supported by the National Science Foundation
with more than two training runs of AUGUSTUS (Appen-              (awards DEB‐1753811 and DBI‐1943371).
dix 15), as is recommended, which could have further
improved results; however, previous benchmarking studies          OPE N RE SE ARCH BADGE S
also reported a lower performance for MAKER (Banerjee
et al., 2021; Brůna et al., 2021). Among the BRAKER runs
executed in the model plants Arabidopsis and Populus, the         This article has earned Open Data and Open Materials badges.
TSEBRA runs were best. TSEBRA, especially TSB (SR/                Data and materials are available at https://dx.doi.org/10.17504/
OrthoDB), performed best for Rosa but would require               protocols.io.yxmvmkp95g3p/v1.
IMPROVING NON‐MODEL PLANT GENOME ANNOTATION                                                                                                         |   15 of 17



DATA AVAILABILITY STATE MENT                                                     Cheng, C. Y., V. Krishnakumar, A. P. Chan, F. Thibaud‐Nissen,
All scripts and data used are available through https://dx.                            S. Schobel, and C. D. Town. 2017. Araport11: A complete
doi.org/10.17504/protocols.io.yxmvmkp95g3p/v1. The pub-                                reannotation of the Arabidopsis thaliana reference genome. Plant
                                                                                       Journal 89(4): 789–804.
lic data (NCBI SRA and genome assembly accessions) for                           Cheng, S., M. Melkonian, S. A. Smith, S. Brockington, J. M. Archibald,
the reference genomes, short reads, and long reads are listed                          P.‐M. Delaux, F.‐W. Li, et al. 2018. 10KP: A phylodiverse genome
in Appendix S2.                                                                        sequencing plan. GigaScience 7(3): giy013.
                                                                                 Corchete, L. A., E. A. Rojas, D. Alonso‐López, J. De Las Rivas,
                                                                                       N. C. Gutiérrez, and F. J. Burguillo. 2020. Systematic comparison
ORCID
                                                                                       and assessment of RNA‐seq procedures for gene expression
Vidya S. Vuruputoor     http://orcid.org/0000-0002-                                    quantitative analysis. Scientiﬁc Reports 10(1): 19737.
5836-7054                                                                        Deutekom, E. S., J. Vosseberg, T. J. P. van Dam, and B. Snel. 2019.
Karl C. Fetter  http://orcid.org/0000-0002-9234-9300                                   Measuring the impact of gene prediction on gene loss estimates in
Cynthia Webster    http://orcid.org/0000-0002-8646-1398                                Eukaryotes by quantifying falsely inferred absences. PLoS
Bikash Shrestha   http://orcid.org/0000-0001-6349-3007                                 Computational Biology 15(8): e1007301.
                                                                                 Edgar, R. 2010. Breaking through the BLAST barrier to high‐throughput
Sumaira Zaman      http://orcid.org/0000-0002-1126-1906                                sequence analysis. Abstract presented at the Sequencing, Finishing,
Susan L. McEvoy     http://orcid.org/0000-0002-0028-4299                               Analysis in the Future meeting in Santa Fe, New Mexico, USA.
Madison Caballero http://orcid.org/0000-0002-4499-5105                                 Available at Usearch: https://www.osti.gov/biblio/1137186 [accessed
Jill L. Wegrzyn  http://orcid.org/0000-0001-5923-0888                                  24 May 2023].
                                                                                 Ellinghaus, D., S. Kurtz, and U. Willhoeft. 2008. LTRharvest, an eﬃcient
                                                                                       and ﬂexible software for de novo detection of LTR retrotransposons.
REFERENCES                                                                             BMC Bioinformatics 9: 18.
Amarasinghe, S. L., S. Su, X. Dong, L. Zappia, M. E. Ritchie, and Q. Gouil.      Flynn, J. M., R. Hubley, C. Goubert, J. Rosen, A. G. Clark, C. Feschotte, and
     2020. Opportunities and challenges in long‐read sequencing data                   A. F. Smit. 2020. RepeatModeler2 for automated genomic discovery
     analysis. Genome Biology 21(1): 30.                                               of transposable element families. Proceedings of the National Academy
Andrews, S. 2010. FastQC: A quality control tool for high throughput                   of Sciences, USA 117(17): 9451–9457.
     sequence data. Available online. Website: https://www.bioinformatics.       Gabriel, L., K. J. Hoﬀ, T. Brůna, M. Borodovsky, and M. Stanke. 2021.
     babraham.ac.uk/projects/fastqc/ [accessed 17 May 2018].                           TSEBRA: Transcript selector for BRAKER. BMC Bioinformatics
Arabidopsis Genome Initiative. 2000. Analysis of the genome sequence                   22(1): 566.
     of the ﬂowering plant Arabidopsis thaliana. Nature 408(6814):               Gonzalez‐Ibeas, D., P. J. Martinez‐Garcia, R. A. Famula, A. Delﬁno‐Mix,
     796–815.                                                                          K. A. Stevens, C. A. Loopstra, C. H. Langley, et al. 2016. Assessing the
Armisén, D., A. Lecharny, and S. Aubourg. 2008. Unique genes in plants:                gene content of the megagenome: Sugar pine (Pinus lambertiana).
     Speciﬁcities and conserved features throughout evolution. BMC                     G3: Genes, Genomes, Genetics 6(12): 3787–3802.
     Evolutionary Biology 8: 280.                                                Grabherr, M. G., B. J. Haas, M. Yassour, J. Z. Levin, D. A. Thompson,
Banerjee, S., P. Bhandary, M. Woodhouse, T. Z. Sen, R. P. Wise, and                    I. Amit, X. Adiconis, et al. 2011. Full‐length transcriptome assembly
     C. M. Andorf. 2021. FINDER: An automated software package to                      from RNA‐Seq data without a reference genome. Nature
     annotate eukaryotic genes from RNA‐Seq data and associated protein                Biotechnology 29(7): 644–652.
     sequences. BMC Bioinformatics 22(1): 205.                                   Gremme, G., V. Brendel, M. E. Sparks, and S. Kurtz. 2005. Engineering a
Bolger, M. E., B. Arsova, and B. Usadel. 2018. Plant genome and                        software tool for gene structure prediction in higher organisms.
     transcriptome annotations: From misconceptions to simple solutions.               Information and Software Technology 47(15): 965–978.
     Brieﬁngs in Bioinformatics 19(3): 437–449.                                  Gurevich, A., V. Saveliev, N. Vyahhi, and G. Tesler. 2013. QUAST:
Bruna, T. 2022. Unsupervised algorithms for automated gene prediction in               Quality assessment tool for genome assemblies. Bioinformatics 29(8):
     novel eukaryotic genomes. Website: http://hdl.handle.net/1853/67297               1072–1075.
     [accessed 12 May 2023].                                                     Haas, B. J., S. L. Salzberg, W. Zhu, M. Pertea, J. E. Allen, J. Orvis, O. White,
Brůna, T., K. J. Hoﬀ, A. Lomsadze, M. Stanke, and M. Borodovsky. 2021.                 et al. 2008. Automated eukaryotic gene structure annotation using
     BRAKER2: Automatic eukaryotic genome annotation with GeneMark‐                    EVidenceModeler and the program to assemble spliced alignments.
     EP+ and AUGUSTUS supported by a protein database. NAR Genomics                    Genome Biology 9(1): R7.
     and Bioinformatics 3(1): lqaa108.                                           Hart, A. J., S. Ginzburg, M. S. Xu, C. R. Fisher, N. Rahmatpour,
Caballero, M., and J. Wegrzyn. 2019. gFACs: Gene ﬁltering, analysis, and               J. B. Mitton, R. Paul, and J. L. Wegrzyn. 2020. EnTAP: Bringing
     conversion to unify genome annotations across alignment and gene                  faster and smarter functional annotation to non‐model eukar-
     prediction frameworks. Genomics, Proteomics & Bioinformatics 17(3):               yotic transcriptomes. Molecular Ecology Resources 20(2):
     305–310.                                                                          591–604.
Campbell, M. S., C. Holt, B. Moore, and M. Yandell. 2014a. Genome                Hoﬀ, K. J., S. Lange, A. Lomsadze, M. Borodovsky, and M. Stanke.
     annotation and curation using MAKER and MAKER‐P. Current                          2016. BRAKER1: Unsupervised RNA‐Seq‐based genome annota-
     Protocols in Bioinformatics 48: 4.11.1–4.11.39.                                   tion with GeneMark‐ET and AUGUSTUS. Bioinformatics 32(5):
Campbell, M. S., M. Law, C. Holt, J. C. Stein, G. D. Moghe, D. E. Hufnagel,            767–769.
     J. Lei, et al. 2014b. MAKER‐P: A tool kit for the rapid creation,           Hoﬀ, K. J., A. Lomsadze, M. Borodovsky, and M. Stanke. 2019. Whole‐
     management, and quality control of plant genome annotations. Plant                genome annotation with BRAKER. Methods in Molecular Biology
     Physiology 164(2): 513–524.                                                       1962: 65–95.
Cantarel, B. L., I. Korf, S. M. C. Robb, G. Parra, E. Ross, B. Moore, C. Holt,   Holt, C., and M. Yandell. 2011. MAKER2: An annotation pipeline and
     et al. 2008. MAKER: An easy‐to‐use annotation pipeline designed for               genome‐database management tool for second‐generation genome
     emerging model organism genomes. Genome Research 18(1): 188–196.                  projects. BMC Bioinformatics 12: 491.
Chang, C., J. L. Bowman, and E. M. Meyerowitz. 2016. Field guide to plant        Huang, X., X.‐G. Chen, and P. A. Armbruster. 2016. Comparative
     model systems. Cell 167(2): 325–339.                                              performance of transcriptome assembly methods for non‐model
Chen, J., Z. Hao, X. Guang, C. Zhao, P. Wang, L. Xue, Q. Zhu, et al. 2019.             organisms. BMC Genomics 17: 523.
     Liriodendron genome sheds light on angiosperm phylogeny and                 Huerta‐Cepas, J., D. Szklarczyk, D. Heller, A. Hernández‐Plaza,
     species‐pair diﬀerentiation. Nature Plants 5(1): 18–25.                           S. K. Forslund, H. Cook, D. R. Mende, et al. 2019. eggNOG 5.0:
16 of 17   |                                                                                     IMPROVING NON‐MODEL PLANT GENOME ANNOTATION



      A hierarchical, functionally and phylogenetically annotated orthology      Ou, S., and N. Jiang. 2018. LTR_retriever: A highly accurate and sensitive
      resource based on 5090 organisms and 2502 viruses. Nucleic Acids                 program for identiﬁcation of long terminal repeat retrotransposons.
      Research 47(Database issue): D309–D314.                                          Plant Physiology 176(2): 1410–1422.
Jain, M., P. Khurana, A. K. Tyagi, and J. P. Khurana. 2008. Genome‐wide          Pertea, G., and M. Pertea. 2020. GFF Utilities: GﬀRead and GﬀCompare.
      analysis of intronless genes in rice and Arabidopsis. Functional &               F1000Research 9: 304.
      Integrative Genomics 8(1): 69–78.                                          Pertea, M., G. M. Pertea, C. M. Antonescu, T.‐C. Chang, J. T. Mendell, and
Jones, P., D. Binns, H.‐Y. Chang, M. Fraser, W. Li, C. McAnulla,                       S. L. Salzberg. 2015. StringTie enables improved reconstruction of a
      H. McWilliam, et al. 2014. InterProScan 5: Genome‐scale protein                  transcriptome from RNA‐seq reads. Nature Biotechnology 33(3):
      function classiﬁcation. Bioinformatics 30(9): 1236–1240.                         290–295.
Joshi, N. A., and J. N. Fass. 2011. Sickle: A sliding‐window, adaptive,          Pucker, B., I. Irisarri, J. de Vries, and B. Xu. 2022. Plant genome sequence
      quality‐based trimming tool for FastQ ﬁles (Version 1.33). Website:              assembly in the era of long reads: Progress, challenges and future
      https://github.com/najoshi/sickle [accessed 23 May 2023].                        directions. Quantitative Plant Biology 3: e5.
Jung, H., T. Ventura, J. S. Chung, W.‐J. Kim, B.‐H. Nam, H. J. Kong, Y.‐O.       Quevillon, E., V. Silventoinen, S. Pillai, N. Harte, N. Mulder, R. Apweiler,
      Kim, et al. 2020. Twelve quick steps for genome assembly and                     and R. Lopez. 2005. InterProScan: Protein domains identiﬁer. Nucleic
      annotation in the classroom. PLoS Computational Biology 16(11):                  Acids Research 33(Web Server issue): W116–W120.
      e1008325.                                                                  Raymond, O., J. Gouzy, J. Just, H. Badouin, M. Verdenaud,
Kersey, P. J. 2019. Plant genome sequences: Past, present, future. Current             A. Lemainque, P. Vergne, et al. 2018. The Rosa genome provides
      Opinion in Plant Biology 48: 1–8.                                                new insights into the domestication of modern roses. Nature
Kim, D., J. M. Paggi, C. Park, C. Bennett, and S. L. Salzberg. 2019. Graph‐            Genetics 50(6): 772–777.
      based genome alignment and genotyping with HISAT2 and HISAT‐               Sahraeian, S. M. E., M. Mohiyuddin, R. Sebra, H. Tilgner, P. T. Afshar,
      genotype. Nature Biotechnology 37(8): 907–915.                                   K. F. Au, N. Bani Asadi, et al. 2017. Gaining comprehensive biological
Kirbis, A., N. Rahmatpour, S. Dong, J. Yu, N. van Gessel, M. Waller,                   insight into the transcriptome by performing a broad‐spectrum RNA‐
      R. Reski, et al. 2022. Genome dynamics in mosses: Extensive synteny              seq analysis. Nature Communications 8(1): 59.
      coexists with a highly dynamic gene space. bioRxiv 492078 [Preprint]       Salzberg, S. L. 2019. Next‐generation genome annotation: We still struggle
      [posted 18 May 2022]. Available at: https://doi.org/10.1101/2022.05.             to get it right. Genome Biology 20(1): 92.
      17.492078 [accessed 12 May 2023].                                          Scott, A. D., A. V. Zimin, D. Puiu, R. Workman, M. Britton, S. Zaman,
Korf, I. 2004. Gene ﬁnding in novel genomes. BMC Bioinformatics 5(1): 59.              M. Caballero, et al. 2020. A reference genome sequence for giant
Kovaka, S., A. V. Zimin, G. M. Pertea, R. Razaghi, S. L. Salzberg, and                 sequoia. G3: Genes, Genomes, Genetics 10(11): 3907–3919.
      M. Pertea. 2019. Transcriptome assembly from long‐read RNA‐seq             Seppey, M., M. Manni, and E. M. Zdobnov. 2019. BUSCO: Assessing
      alignments with StringTie2. Genome Biology 20(1): 278.                           genome assembly and annotation completeness. In M. Kollmar [ed.],
Kress, W. J., D. E. Soltis, P. J. Kersey, J. L. Wegrzyn, J. H. Leebens‐Mack,           Gene prediction, 227–245. Humana Press, New York, New
      M. R. Gostel, X. Liu, and P. S. Soltis. 2022. Green plant genomes:               York, USA.
      What we know in an era of rapidly expanding opportunities.                 Simão, F. A., R. M. Waterhouse, P. Ioannidis, E. V. Kriventseva, and
      Proceedings of the National Academy of Sciences, USA 119(4):                     E. M. Zdobnov. 2015. BUSCO: Assessing genome assembly and
      e2115640118.                                                                     annotation completeness with single‐copy orthologs. Bioinformatics
Kriventseva, E. V., D. Kuznetsov, F. Tegenfeldt, M. Manni, R. Dias,                    31(19): 3210–3212.
      F. A. Simão, and E. M. Zdobnov. 2019. OrthoDB v10: Sampling the            Smit, A. F. A., R. Hubley, and P. Green. 2013–2015. RepeatMasker
      diversity of animal, plant, fungal, protist, bacterial and viral genomes         Open‐4.0. Website: http://www.repeatmasker.org [accessed 12
      for evolutionary and functional annotations of orthologs. Nucleic                May 2023].
      Acids Research 47(D1): D807–D811.                                          Stanke, M., and S. Waack. 2003. Gene prediction with a hidden Markov
Lewin, H. A., S. Richards, E. Lieberman Aiden, M. L. Allende,                          model and a new intron submodel. Bioinformatics 19(Suppl 2):
      J. M. Archibald, M. Bálint, K. B. Barker, et al. 2022. The Earth                 ii215–ii225.
      BioGenome Project 2020: Starting the clock. Proceedings of the             Sun, Y., L. Shang, Q.‐H. Zhu, L. Fan, and L. Guo. 2022. Twenty years of
      National Academy of Sciences, USA 119(4): e2115635118.                           plant genome sequencing: Achievements and challenges. Trends in
Li, H. 2018. Minimap2: Pairwise alignment for nucleotide sequences.                    Plant Science 27(4): 391–401.
      Bioinformatics 34(18): 3094–3100.                                          Tuskan, G. A., S. Difazio, S. Jansson, J. Bohlmann, I. Grigoriev, U. Hellsten,
Li, H. 2021. New strategies to improve minimap2 alignment accuracy.                    N. Putnam, et al. 2006. The genome of black cottonwood, Populus
      Bioinformatics 37: 4572–4574.                                                    trichocarpa (Torr. & Gray). Science 313(5793): 1596–1604.
Luo, X., S. Chen, and Y. Zhang. 2022. PlantRep: A database of plant              Toubiana, W., D. Armisén, C. Dechaud, R. Arbore, and A. Khila. 2021.
      repetitive elements. Plant Cell Reports 41(4): 1163–1166.                        Impact of male trait exaggeration on sex‐biased gene expression and
Manni, M., M. R. Berkeley, M. Seppey, F. A. Simão, and E. M. Zdobnov.                  genome architecture in a water strider. BMC Biology 19(1): 89.
      2021. BUSCO Update: Novel and streamlined workﬂows along with              Trouern‐Trend, A. J., T. Falk, S. Zaman, M. Caballero, D. B. Neale,
      broader and deeper phylogenetic coverage for scoring of eukaryotic,              C. H. Langley, A. M. Dandekar, et al. 2020. Comparative genomics of
      prokaryotic, and viral genomes. Molecular Biology and Evolution                  six Juglans species reveals disease‐associated gene family contractions.
      38(10): 4647–4654.                                                               Plant Journal 102(2): 410–423.
Marks, R. A., S. Hotaling, P. B. Frandsen, and R. VanBuren. 2021.                Valencia, J. D., and H. Z. Girgis. 2019. LtrDetector: A tool‐suite for
      Representation and participation across 20 years of plant genome                 detecting long terminal repeat retrotransposons de‐novo. BMC
      sequencing. Nature Plants 7(12): 1571–1578.                                      Genomics 20(1): 450.
Meyer, C., N. Scalzitti, A. Jeannin‐Girardon, P. Collet, O. Poch, and            Venturini, L., S. Caim, G. G. Kaithakottil, D. L. Mapleson, and
      J. D. Thompson. 2020. Understanding the causes of errors in                      D. Swarbreck. 2018. Leveraging multiple transcriptome assembly
      eukaryotic protein‐coding gene prediction: A case study of primate               methods for improved gene structure annotation. GigaScience 7(8):
      proteomes. BMC Bioinformatics 21(1): 513.                                        giy093.
Mudge, J. M., and J. Harrow. 2016. The state of play in higher eukaryote         Watson, M., and A. Warr. 2019. Errors in long‐read assemblies can critically
      gene annotation. Nature Reviews. Genetics 17(12): 758–772.                       aﬀect protein prediction. Nature Biotechnology 37(2): 124–126.
Musich, R., L. Cadle‐Davidson, and M. V. Osier. 2021. Comparison of              Wu, T. D., and C. K. Watanabe. 2005. GMAP: A genomic mapping and
      short‐read sequence aligners indicates strengths and weaknesses for              alignment program for mRNA and EST sequences. Bioinformatics
      biologists to consider. Frontiers in Plant Science 12: 657240.                   21(9): 1859–1875.
IMPROVING NON‐MODEL PLANT GENOME ANNOTATION                                                                              |   17 of 17



Yandell, M., and D. Ence. 2012. A beginner's guide to eukaryotic genome   Appendix S10. Comparisons among StringTie2, BRAKER,
    annotation. Nature Reviews. Genetics 13(5): 329–342.                  and TSEBRA runs.
                                                                          Appendix S11. Liriodendron masked and unmasked.
S U P P OR T I N G I N F OR M A TI O N
Additional supporting information can be found online in                  Appendix S12. Comparison between StringTie2 and
the Supporting Information section at the end of this article.            BRAKER runs.
Appendix S1. Genomes for this study, with versions and                    Appendix S13. Overlaps between BR (SR) and BR (SR/ST2)
links to the genome.                                                      in Liriodendron.
Appendix S2. Public transcriptomic evidence (short and                    Appendix S14. Genes predicted as mono‐exonic from the
long read).                                                               BR (SR/ST2) run overlapping with multis from the BR (SR)
                                                                          run in Liriodendron.
Appendix S3. StringTie proteins before and after frame‐
selection.                                                                Appendix S15. Comparison between MAKER and
                                                                          BRAKER.
Appendix S4. Mono:multi ratios in published model plant
genomes.
Appendix S5. Initial genome statistics.                                     How to cite this article: Vuruputoor, V. S.,
                                                                            D. Monyak, K. C. Fetter, C. Webster, A. Bhattarai,
Appendix S6. RNA alignments for short and long reads.                       B. Shrestha, S. Zaman, et al. 2023. Welcome to the
Appendix S7. N50s for the short and long reads.                             big leaves: Best practices for improving genome
                                                                            annotation in non‐model plant genomes.
Appendix S8. Sensitivity and precision scores for Arabi-                    Applications in Plant Sciences 11(4): e11533.
dopsis and Populus.                                                         https://doi.org/10.1002/aps3.11533
Appendix S9. Gene characteristics in BRAKER runs.
