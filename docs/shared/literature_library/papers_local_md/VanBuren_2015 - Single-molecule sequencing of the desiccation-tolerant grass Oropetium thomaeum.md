# VanBuren_2015 - Single-molecule sequencing of the desiccation-tolerant grass Oropetium thomaeum

**Source PDF:** 

---

Letter                                                                                                                                                                            OPEN
                                                                                                                                                                doi:10.1038/nature15714




Single-molecule sequencing of the desiccation-
tolerant grass Oropetium thomaeum
Robert VanBuren1*, Doug Bryant1*, Patrick P. Edger2,3, Haibao Tang4,5, Diane Burgess2, Dinakar Challabathula6†, Kristi Spittle7,
Richard Hall7, Jenny Gu7, Eric Lyons4, Michael Freeling2, Dorothea Bartels6, Boudewijn Ten Hallers8, Alex Hastie8,
Todd P. Michael9 & Todd C. Mockler1


Plant genomes, and eukaryotic genomes in general, are typically                                   and comparative genomics, although draft genomes are now avail-
repetitive, polyploid and heterozygous, which complicates genome                                  able for most agriculturally important grasses1. The largest genome
assembly1. The short read lengths of early Sanger and current                                     assemblies, such as maize (2,300 megabases (Mb))7, barley (5,100 Mb)8
next-generation sequencing platforms hinder assembly through                                      and wheat (hexaploid, 17,000 Mb)9 are highly fragmented as a result
complex repeat regions, and many draft and reference genomes                                      of the inability of current sequencing technologies to span complex
are fragmented, lacking skewed GC and repetitive intergenic                                       repeat regions. Near-finished reference genomes are available for rice4,
sequences, which are gaining importance due to projects like                                      Sorghum5 and Brachypodium10, but more high-quality grass genomes
the Encyclopedia of DNA Elements (ENCODE)2. Here we report                                        are needed for comparative genomics and gene discovery. Here we pres-
the whole-genome sequencing and assembly of the desiccation-                                      ent the ‘near-complete’ draft genome of the grass Oropetium thomaeum,
tolerant grass Oropetium thomaeum. Using only single-molecule                                     the first high-quality reference genome from the Chloridoideae sub-
real-time sequencing, which generates long (>16 kilobases)                                        family. The draft genome is near complete because we were able to
reads with random errors, we assembled 99% (244 megabases)                                        sequence through complex repeat regions that are unassembled in most
of the Oropetium genome into 625 contigs with an N50 length of                                    draft genomes. Oropetium has the smallest known grass genome at
2.4 megabases. Oropetium is an example of a ‘near-complete’ draft                                 245 Mb and is also a resurrection plant that can survive the extreme
genome which includes gapless coverage over gene space as well as                                 water stress such as loss of >95% of cellular water (Fig. 1)11.
intergenic sequences such as centromeres, telomeres, transposable                                    Single-molecule real-time (SMRT) sequencing (Pacific Biosciences)
elements and rRNA clusters that are typically unassembled in draft                                produces long and unbiased sequences, which enables assembly of
genomes. Oropetium has 28,466 protein-coding genes and 43%                                        complex repeat structures and GC- and AT-rich regions that are often
repeat sequences, yet with 30% more compact euchromatic regions                                   unassembled or highly fragmented in NGS-based draft genomes. We
it is the smallest known grass genome. The Oropetium genome                                       generated ~72× sequencing coverage of the Oropetium genome using
demonstrates the utility of single-molecule real-time sequencing for                              32 SMRT cells on the PacBio RS II platform (which is equivalent to <1
assembling high-quality plant and other eukaryotic genomes, and                                   week of sequencing time and <US$10,000 in reagents). The resulting
serves as a valuable resource for the plant comparative genomics                                  sequence had a read N50 length of over 16 kilobases (kb), and there was
community.                                                                                        10× coverage of reads over 20 kb in length (Extended Data Fig. 1a). The
   The genomes of Arabidopsis3, rice4, poplar, grape and Sorghum5                                 raw reads were error-corrected using the hierarchical genome assembly
were first sequenced using high-quality and reiterative Sanger-based                              process (HGAP), and the longest reads (>16 kb) were assembled using
approaches producing a series of ‘gold standard’ reference genomes.                               Celera assembler followed by two rounds of genome polishing using
The advent of next-generation sequencing (NGS) technologies reduced                               Quiver12. The assembly contains 650 contigs spanning 99% (244 Mb)
costs of sequencing substantially, which has enabled sequencing of over                           of the estimated 245 Mb genome size (Extended Data Fig. 1b) with a
100 plant genomes1. The quality of plant genome assemblies depends                                 contig N50 length of 2.4 Mb (Extended Data Fig. 1c). The final assem-
on genome size, ploidy, heterozygosity and sequence coverage, but most                            bly consists of 625 contigs after removal of the complete chloroplast
NGS-based genomes have on the order of tens of thousands of short                                 genome, mitochondria-derived contigs and contaminants. The 35
contigs distributed in thousands of scaffolds. The short read lengths of                          largest contigs span half the genome, and the largest 107 contigs contain
NGS, inherent biases and non-random sequencing errors have resulted                               90% of the sequence. The 135,324 base-pair (bp) chloroplast genome
in highly fragmented draft genome assemblies that are not complete,                               assembled into a single contig that includes both ~25 kb of inverted
which means they are missing biologically meaningful sequences                                    repeat regions which typically collapse into a single copy during
including entire genes, regulatory regions, transposable elements,                                assembly. The mitochondria genome was assembled into 20 ­partially
centromeres, telomeres and haplotype-specific structural variations.                              overlapping circular chromosomes, which are the product of
It is becoming clear from ENCODE projects that complete genomes                                   ­intramolecular recombination events that collectively span 1,100 kb.
are needed to better understand the importance of the non-coding                                     The Oropetium genome has high contiguity for an uncurated
regions of genomes2.                                                                               draft plant genome. The average contig N50 length for all published
   More than 40% of calories consumed by humans are derived from                                   plant genomes is 50 kb compared to 2.4 Mb for Oropetium (Extended
grasses, and the grass family (Poaceae) is arguably the most important                             Data Fig. 1d, e). After manual curation and data augmentation, only
plant family with regard to global food security6. The size and complex-                           the Arabidopsis (TAIR10)13, rice (V7) and Brachypodium (V 2.1)10
ity of most grass genomes has challenged progress in gene discovery                                genomes have longer contig N50 lengths. The accuracy rate is very

1
 Donald Danforth Plant Science Center, St Louis, Missouri 63132, USA. 2Department of Plant and Microbial Biology, University of California Berkeley, Berkeley, California 94720, USA. 3Department
of Horticulture, Michigan State University, East Lansing, Michigan 48823, USA. 4iPlant Collaborative, School of Plant Sciences, University of Arizona, Tucson, Arizona 85721, USA. 5Center for
Genomics and Biotechnology, Haixia Institute of Science and Technology (HIST), Fujian Agriculture and Forestry University, Fuzhou 350002, China. 6IMBIO, University of Bonn, Kirschallee 1,
D-53115 Bonn, Germany. 7Pacific Biosciences, Menlo Park, California 94025, USA. 8BioNano Genomics, San Diego, California 92121, USA. 9Ibis Biosciences, Carlsbad, California 92008, USA.
†Present address: Department of Life Sciences, School of Basic and Applied Sciences, Central University of Tamil Nadu, Thiruvarur 610101, India.
*These authors contributed equally to this work.


5 0 8 | N A T U R E | V O L 5 2 7 | 2 6 nove m b er 2 0 1 5
                                                                 © 2015 Macmillan Publishers Limited. All rights reserved
                                                                                                                                      Letter RESEARCH

                            a                                 b                                     c




                                                  1 cm

Figure 1 | Desiccation tolerance in the resurrection grass Oropetium thomaeum. a, Well watered. b, Desiccated (relative water content <5%) after
9 days of drought stress. c, Condition 24 h post-hydration (relative water content >70%).
high at 99.99995%, which is similar to Sanger-based approaches and              grasses17 at 90%, 60%, 50%, 30% and 10% the size of Brachypodium10,
higher than most NGS-based assemblies (Extended Data Fig. 1h).                  rice4, Setaria18, Sorghum5 and maize7, respectively. We found that
We ­plotted repeat density and GC content along the length of the               Oropetium has a solo:intact LTR ratio >1, which is similar to small
contigs to identify factors causing contig breaks (Extended Data                grass genomes like rice and Brachypodium, where proliferating LTRs are
Fig. 1f, g). There is no correlation between repeat density and GC              removed by illegitimate recombination, whereas large grass genomes
content at contig break points. This suggests that contig break points          like Sorghum and maize have solo:intact LTR ratios <1 (ref. 15). Despite
occur at the start of repeats or that most assembly breaks are caused           its compact size, the Oropetium genome has a typical number of pre-
by other factors, such as within-genome heterozygosity or haplo-                dicted protein coding genes at 28,446. A pan-cereal whole-genome
type-specific structural variation. To test this, we also tried ‘dip-           duplication (WGD) event, called rho, occurred before the diversi-
loid-aware’ assemblers Falcon (https://github.com/PacificBiosciences/           fication of grasses5,19. There appear to have been no further WGDs
falcon) and MinHash Alignment Process (MHAP)14. These assem-                    in the selected grass genomes, including Oropetium, since the shared
blies had similar metrics but were less contiguous overall (Extended            rho event4,5.
Data Fig. 1i).                                                                     Genome alignments between Oropetium and selected grass genomes
   The completeness of the Oropetium genome allowed us to accu-                 are mostly one-to-one after exclusion of the alignments derived from
rately survey its highly repetitive features that are often unassembled in      the shared genome duplication events (Extended Data Fig. 3a–e).
most plant genomes. The Oropetium assembly captures all 18 telomeric            Overall, 75% of the Oropetium genome, or 89% of its gene space, is
arrays (Extended Data Table 1) with repeat number ranging from 40 to            contained in conserved syntenic blocks when compared to other
900, suggesting that at least some are full length. Three of the nine cen-      grasses. Genomic colinearity across grass genomes is extensive, with a
tromeric satellites are completely assembled into large inverted repeats        high density of orthologous genes spanning much of the euchromatin
spanning 400 kb with a base monomer length of 155 bp, and higher                (Fig. 3). Insertions of retrotransposons and non-collinear genes that
order structures of dimers (310 bp), trimers (465 bp) and tetramers             originated elsewhere in the genome contribute greatly to the differences
(620 bp; Fig. 2, Extended Data Fig. 2 and Supplementary Table 1). The           in the intergenic sequences in grasses20.
remaining 40 centromeric sequences are incomplete centromere repeat                The relative sizes of syntenic blocks in the grass genomes track
fragments broken during assembly or solo repeats not associated with            closely with the overall genome size difference (Extended Data Fig. 3f).
a larger centromere satellite. Nucleolus organizer regions contain tan-
dem arrays of the 18S, 5.8S and 25S ribosomal RNA (rRNA) genes and                a 0                         1                  2                Mb
typically span several megabase pairs with hundreds of nearly identi-                         Contig 24                                             CDS
cal 10-kb arrays. Twenty-two full-length rRNA tandem arrays in six
                                                                                                                                                    DNA-TE
contigs are found in the Oropetium assembly (Extended Data Table 2).                                                                                LTR
The largest tandem array contains five identical and one partial 9-kb                                                                               CenOt
repeats collectively spanning 51 kb; this is approaching the theoretical
limit given the read-length distributions of our data. The remaining                                                                              CenOt
rRNA tandem repeats probably collapsed during read correction or                                                                                  LTR
                                                                                                                                                  DNA-TE
genome assembly given their high sequence conservation.                                                                                           CDS
   Most repeats are incomplete, unassembled or highly collapsed in                b 0                2             4              6              8 Mb
Illumina/454 NGS-based genomes, which has led to an underestima-                               Contig 1
tion and misclassification of repeat content in most plant genomes.                                                                                 CDS
                                                                                                                                                    DNA-TE
Repetitive elements account for a surprisingly high proportion of the
                                                                                                                                                    LTR
Oropetium genome (43%) compared to 21% in Brachypodium10, 35%                                                                                       CenOt
in rice4, 54% in Sorghum5 and over 90% in wheat9 (Extended Data
Table 3). Similar to these other genomes, the long terminal repeat (LTR)                                                                          CenOt
retrotransposons are the most abundant class and account for 35.6% of                                                                             LTR
                                                                                                                                                  DNA-TE
the Oropetium genome. We identified 3,247 intact LTRs in 358 families,                                                                            CDS
which is similar to rice (3,663) and Brachypodium (2,162), but far less
                                                                                Figure 2 | SMRT sequencing enables contiguous sequencing over
than Sorghum (17,022)15. Only ~2% of the repeats are unclassified,              complex regions. The distributions of centromere-specific satellite DNA
which reflects the completeness of individual repeat elements due to            (CenOt), long terminal repeat retrotransposons (LTRs), DNA transposable
the long reads.                                                                 elements (DNA-TE) and coding DNA sequences (CDS) are plotted.
   Genome size in the grasses varies by several orders of magnitude as a        a, The gap-free assembly of a full-length centromeric array and the
consequence of polyploidy and genome bloating due to repetitive DNA             flanking highly repetitive pericentromeric region. b, The largest contig
accumulation16. Oropetium has the smallest known genome among the               (7.8 Mb), which has a more typical distribution of elements.

                                                                                                    2 6 nove m b er 2 0 1 5 | V O L 5 2 7 | N A T U R E | 5 0 9
                                                   © 2015 Macmillan Publishers Limited. All rights reserved
 RESEARCH Letter

                                                                   Gene (+)     Repeat Gene (–)




                                     PACMAD
                                                                                                  Oropetium scaffold 3
                                                                                                  2.7–3.0 Mb

                                                                                                                   Setaria chr 3
                                                                                                                   20.7–21.4 Mb

                                                                                                                           Sorghum chr 9
                                                                                                                           49.4–48.5 Mb
                           Poaceae

                                                                                                            Oryza chr 5
                                                                                                            20.1–19.6 Mb

                                                                                                                 Brachypodium chr 2
                                     BOP




                                                                                                                 23.4–24.1 Mb

Figure 3 | Compact genome structure of Oropetium. Oropetium, part                   regions from Oropetium, Setaria, Sorghum, Oryza and Brachypodium
of the PACMAD clade, provides the first high-quality reference genome               are shown. Rectangles show predicted gene models, and colours
from the Chloridoideae subfamily—a large and diverse group of ~1,600                indicate relative orientations. Matching gene pairs are displayed as grey
species that contains the orphan crops tef (Eragrostis tef) and finger millet       connections. chr, chromosome.
(Eleusine coracana). Typical micro-colinearity patterns among genomic

In contrast, the genomic span of coding sequences is similar across                 grasses, but a similar proportion (24% of genes). Tandem duplicated
genes that are retained in orthologous locations, although coding fea-              genes are enriched for gene ontology terms involved in response to abi-
tures are slightly smaller in Oropetium (Extended Data Table 4). The                otic stresses, gene regulation and cellular metabolism (Supplementary
relatively constant sizes of coding sequences among grass genomes                   Table 2). In addition, Oropetium has 4,209 homeologous gene pairs
confirm that genome size differences are indeed due to variations in                retained from the rho WGD event, which are enriched for gene ontology
the intergenic contents. It was thought that plants have a ‘one-way                 terms related to gene regulation and stress responses such as transcrip-
ticket to genome obesity’ due to the retention of proliferating trans-              tion factor activity, nitrogen metabolism, response to abiotic stimulus, to
posable elements21. However, analysis of carnivorous plants Utricularia             salt stress and to oxygen-containing compounds (Supplementary Tables
gibba (bladderwort, 82 Mb)22 and Genlisea aurea (corkscrew, 63.6 Mb)23              3 and 4). Understanding the genomic mechanisms of extreme desicca-
provided evidence that almost all intergenic space can be purged. Small             tion tolerance in resurrection plants such as Oropetium may provide
genomes also arise from a reduction in gene number as seen in the                   targets for engineering drought and stress tolerance in crop plants.
aquatic monocotyledon Spirodela polyrhiza, which has the fewest pre-                   Pacific Biosciences (PacBio) SMRT sequencing has been used
dicted protein coding genes at 19,623 (ref. 24). Oropetium seems to have            to close gaps in the human genome27, assemble complete bacterial
reduced both its intergenic and intragenic sequence.                                genomes12 and identify novel gene isoforms28. Here we present a several
   As the intergenic sequence in Oropetium is specifically reduced com-             hundred megabase plant genome, sequenced and assembled entirely by
pared with other grasses (Extended Data Fig. 3f), we determined which               SMRT sequencing. The long SMRT reads produced a near-complete
sequence accounted for its smaller genome size by comparing highly                  draft genome that captured three of nine complete centromeres, all
syntenic regions of the larger 730 Mb Sorghum genome. To identify                   of the telomeres and biologically relevant features of the Oropetium
highly orthologous regions we looked for Sorghum genes (promoter,                   genome. The total time from extracted DNA to a complete assembly
5′ UTR, exons, introns and 3′ UTR) with an increased number of con-                 was less than one month, and costs for PacBio were comparable to
served noncoding sequences25. We then analysed the top 48 Sorghum                   an Illumina-based genome assembly. Our study demonstrates that
genes against their orthologous sequences in Oropetium and found                    SMRT sequencing enables a new level of genome assembly required
that they were 38% (± 0.27, 1 s.d.) larger in Sorghum (Extended Data                for full ENCODE-type analysis of intergenic sequence, which is not
Fig. 4a). The primary driver of gene-space expansion was highly unique              currently possible with other NGS-based methods. The compactness
~1-kb intragenic sequences evenly spaced within the Sorghum genes.                  of the Oropetium genome results from purging of both inter- and intra-
One explanation is that these evenly spaced highly unique sequences                 genic sequences, probably through small deletions during illegitimate
are degenerate remnants of transposons that have been partly purged                 recombination, as has been shown in other grasses. One hypothesis is
from the Sorghum genome. Oropetium has a >1 solo:intact LTR ratio,                  that genome size is a function of cell size29, and consistent with this, all
consistent with active purging of transposons and complete loss of                  small plant genomes sequenced to date including Arabidopsis (125 Mb),
these regions. These results lend support to an emerging theory about               Brachypodium (272 Mb), Selaginella (100 Mb) Spirodela (158 Mb) and
the C-value paradox called the Genome Balance Hypothesis26, which                   Utricularia (82 Mb) are plants of very small stature (Fig. 1). However,
suggests that selection on gene networks and pericentromeric growth                 we provide evidence for the Genome Balance Hypothesis, which sug-
(centromere movement) is balanced by transposon proliferation and                   gests that there is selective pressure on Oropetium to purge proliferat-
retention. Therefore, these evenly spaced highly unique sequences                   ing transposons in order to maintain expression balance of networked
balance the 6:1 expansion of pericentromeric sequence in Sorghum as                 genes and spacing in centromeres. The complete assembly of complex
compared to Oropetium (Extended Data Fig. 4b).                                      and highly similar repeat sequences demonstrated here suggests that
   Desiccation tolerance was a key adaptation that permitted the                    SMRT sequencing can be used to assemble large and polyploid plant
most recent common ancestor of terrestrial plants to survive on land.               and other eukaryotic genomes, assuming ample sequence coverage and
Desiccation tolerance is widespread in bryophytes and lichens but rare in           computational resources. SMRT-sequencing-based assemblies provide
flowering plants, although similar mechanisms have evolved in vascular              an opportunity to determine how these regions play a role in genome
plants for seed and pollen desiccation. Desiccation tolerance to survive            architecture and dynamics.
prolonged drought evolved independently in diverse monocotyledon
and eudicotyledon lineages, and is found in at least 300 s­ pecies. Gene            Online Content Methods, along with any additional Extended Data display items and
                                                                                    Source Data, are available in the online version of the paper; references unique to
duplications have provided the raw material for evolutionary innova-                these sections appear only in the online paper.
tion across plants. Tandem duplicated genes are often involved in stress
responses and are probably important for adaptive evolution in dynam-               received 28 April; accepted 10 September 2015.
ically changing environments. Oropetium has 6,668 tandem duplicated                 Published online 11 November 2015; corrected online 25 November 2015
genes in 2,326 clusters, which is a slightly higher number than in other            (see full-text HTML version for details).

5 1 0 | N A T U R E | V O L 5 2 7 | 2 6 nove m b er 2 0 1 5
                                                      © 2015 Macmillan Publishers Limited. All rights reserved
                                                                                                                                                    Letter RESEARCH

1.    Michael, T. P. & VanBuren, R. Progress, challenges and the future of crop          25. Lyons, E. & Freeling, M. How to usefully compare homologous plant
      genomes. Curr. Opin. Plant Biol. 24, 71–81 (2015).                                     genes and chromosomes as DNA sequences. Plant J. 53, 661–673
2.    Kellis, M. et al. Defining functional DNA elements in the human genome.                (2008).
      Proc. Natl Acad. Sci. USA 111, 6131–6138 (2014).                                   26. Freeling, M., Xu, J., Woodhouse, M. & Lisch, D. A solution to the C-value paradox
3.    The Arabidopsis Genome Initiative. Analysis of the genome sequence of the              and the function of junk DNA: the Genome Balance Hypothesis. Mol. Plant 8,
      flowering plant Arabidopsis thaliana. Nature 408, 796–815 (2000).                      899–910 (2015).
4.    International Rice Genome Sequencing Project. The map-based sequence of            27. Chaisson, M. J. P. et al. Resolving the complexity of the human genome using
      the rice genome. Nature 436, 793–800 (2005).                                           single-molecule sequencing. Nature 517, 608–611 (2015).
5.    Paterson, A. H. et al. The Sorghum bicolor genome and the diversification of       28. Au, K. F. et al. Characterization of the human ESC transcriptome by hybrid
      grasses. Nature 457, 551–556 (2009).                                                   sequencing. Proc. Natl Acad. Sci. USA 110, E4821–E4830 (2013).
6.    Elert, E. Rice by the numbers: A good grain. Nature 514, S50–S51 (2014).           29. Beaulieu, J. M., Leitch, I. J., Patel, S., Pendharkar, A. & Knight, C. A. Genome size
7.    Schnable, P. S. et al. The B73 maize genome: complexity, diversity, and                is a strong predictor of cell size and stomatal density in angiosperms. New
      dynamics. Science 326, 1112–1115 (2009).                                               Phytol. 179, 975–986 (2008).
8.    International Barley Genome Sequencing Consortium. A physical, genetic and
      functional sequence assembly of the barley genome. Nature 491, 711–716             Supplementary Information is available in the online version of the paper.
      (2012).
9.    International Wheat Genome Sequencing Consortium (IWGSC). A                        Acknowledgements This work is supported in part by funding from the National
      chromosome-based draft sequence of the hexaploid bread wheat (Triticum             Science foundation (DBI-1401572 to R.V.; DBI-120793 to P.P.E.), USDA NIFA
      aestivum) genome. Science 345, 1251788 (2014).                                     (CO471A-B to M.F.), the Department of Energy (DE-SC0012639 to T.C.M. and
10.   The International Brachypodium Initiative. Genome sequencing and analysis of       T.P.M.; DE-SC-0008769 to T.C.M.), the Donald Danforth Plant Science Center
      the model grass Brachypodium distachyon. Nature 463, 763–768 (2010).               to T.C.M. and the Enterprise Rent-A-Car Institute for Renewable Fuels to T.C.M.
11.   Bartels, D. & Mattar, M. Oropetium thomaeum: A resurrection grass with a           Sequencing was provided by Pacific Biosciences under the ‘Most Interesting
      diploid genome. Maydica 47, 185–192 (2002).                                        Genome in the World’ 2014 SMRT grant program.
12.   Chin, C.-S. et al. Nonhybrid, finished microbial genome assemblies from
      long-read SMRT sequencing data. Nature Methods 10, 563–569 (2013).                 Author Contributions R.V., D.Br., T.P.M. and T.C.M. designed and conceived
13.   Lamesch, P. et al. The Arabidopsis Information Resource (TAIR): improved gene      research; D.Ba. and D.C. identified biological material, performed desiccation
      annotation and new tools. Nucleic Acids Res. 40, D1202–D1210 (2012).               experiments and extracted DNA and RNA; R.V. prepared DNA for PacBio
14.   Berlin, K. et al. Assembling large genomes with single-molecule sequencing         sequencing; T.P.M., R.V. and T.C.M. performed Illumina sequencing; K.S.,
      and locality-sensitive hashing. Nature Biotechnol. 33, 623–630 (2015).             R.H. and J.G. performed PacBio sequencing and assembly; B.T.H. and A.H.
15.   El Baidouri, M. & Panaud, O. Comparative genomic paleontology across plant         conducted the BioNano analysis. D.Br., R.V., T.P.M. and T.C.M. annotated genome
      kingdom reveals the dynamics of TE-driven genome evolution. Genome Biol.           features; E.L., M.F., D.Bu., R.V., D.Br., H.T., T.P.M., T.C.M. and P.P.E. analysed data;
      Evol. 5, 954–965 (2013).                                                           R.V., T.P.M. and T.C.M. wrote the paper. All authors read and approved the final
16.   Michael, T. P. Plant genome size variation: bloating and purging DNA. Brief.       manuscript.
      Funct. Genomic. 13, 308–317 (2014).
17.   Jones, N. & Pašakinskienė, I. Genome conflict in the gramineae. New Phytol.        Author Information The genome assembly and annotation have been
      165, 391–410 (2005).                                                               deposited in CoGe under the accession code 25799 (https://genomevolution.
18.   Bennetzen, J. L. et al. Reference genome sequence of the model plant Setaria.      org/CoGe/GenomeInfo.pl?gid= 25799), in the NCBI BioProject under
      Nature Biotechnol. 30, 555–561 (2012).                                             PRJNA286116, and in GenBank under accession number LFJQ00000000.
19.   Tang, H., Bowers, J. E., Wang, X. & Paterson, A. H. Angiosperm genome              Raw PacBio and Illumina reads are available at the Short Read Archive at
      comparisons reveal early polyploidy in the monocot lineage. Proc. Natl Acad.       NCBI under the aforementioned NCBI BioProject. Genome assembly and
      Sci. USA 107, 472–477 (2010).                                                      annotation are also available at http://www.oropetium.org/. Reprints and
20.   Wicker, T., Buchmann, J. P. & Keller, B. Patching gaps in plant genomes results    permissions information is available at www.nature.com/reprints. The
      in gene movement and erosion of colinearity. Genome Res. 20, 1229–1237             authors declare no competing financial interests. Readers are welcome to
      (2010).                                                                            comment on the online version of the paper. Correspondence and requests for
21.   Bennetzen, J. L. & Kellogg, E. A. Do plants have a one-way ticket to genomic       materials should be addressed to T.P.M. (toddpmichael@gmail.com) or T.C.M.
      obesity? Plant Cell 9, 1509 (1997).                                                (tmockler@danforthcenter.org).
22.   Ibarra-Laclette, E. et al. Architecture and evolution of a minute plant genome.
      Nature 498, 94–98 (2013).                                                                          This work is licensed under a Creative Commons Attribution-
23.   Leushkin, E. V. et al. The miniature genome of a carnivorous plant Genlisea                        NonCommercial-ShareAlike 3.0 Unported licence. The images or
      aurea contains a low number of genes and short non-coding sequences. BMC           other third party material in this article are included in the article’s Creative
      Genomics 14, 476 (2013).                                                           Commons license, unless indicated otherwise in the credit line; if the material
24.   Wang, W. et al. The Spirodela polyrhiza genome reveals insights into its           is not included under the Creative Commons license, users will need to obtain
      neotenous reduction fast growth and aquatic lifestyle. Nature Commun. 5,           permission from the license holder to reproduce the material. To view a copy
      3311 (2014).                                                                       of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/




                                                                                                              2 6 nove m b er 2 0 1 5 | V O L 5 2 7 | N A T U R E | 5 1 1
                                                            © 2015 Macmillan Publishers Limited. All rights reserved
 RESEARCH Letter

Methods                                                                                from three different libraries of 570-bp insert, 1-kb insert and 3-kb insert sizes
No statistical methods were used to predetermine sample size.                          were trimmed for quality using Trimmomatic (v.0.32; ref. 33). Illumina sequence
Plant material. Oropetium thomaeum is a compact resurrection plant that has            adaptors were removed, leading low quality (below quality 3) and N base pairs
the smallest known genome among the grasses, at 245 Mb and 9 chromosomes               were trimmed, and reads were scanned using a 4-bp sliding window and trimmed
(2n =  2x =  18; 1C =  0.25 pg)17. We estimated the genome size to be 250 Mb by        when the average quality per base dropped below 30. Read pairs where both reads
flow cytometry and 245 Mb by k-mer analysis (Extended Data Fig. 1b). Oropetium         were ultimately of at least 36 bp in length following this quality control process
thomaeum plants were originally collected in Jodhpur, Rajasthan, India and prop-       were retained and used for subsequent analyses.
agated as previously described11. Oropetium is a member of the Chloridoideae              Quality trimmed data were aligned to our assembly using BWA mem (v.
subfamily, a large and diverse group of roughly 1,600 species that contains the        0.7.12-r1039)34. Duplicate alignments were marked using Picard tools v.1.104
orphan crops tef (Eragrostis tef) and finger millet (Eleusine coracana) as well as     MarkDuplicates (http://broadinstitute.github.io/picard/). Genome Analysis Toolkit
some turf grasses (such as Bermuda grass, Cynodon dactylon and Zoysia japonica).       (v.3.3.0)35 IndelRealigner was used to perform local realignment around indels,
SMRT PacBio sequencing. Fifty micrograms of high-molecular-weight Oropetium            followed by application of GATK HaplotypeCaller to call variants. Identified single
gDNA was extracted using a modified nuclei preparation method30 followed by            nucleotide polymorphisms were filtered by depth, strand bias, mapping quality and
an additional high-salt phenol–chloroform purification to minimize contamina-          read position. Identified indels were filtered by depth, strand bias and read position.
tion. A 20-kb insert SMRTbell library was generated using a 15 kb lower-end size          The native error rate of raw PacBio reads is in the range of 15–20%, raising
selection protocol on the BluePippin (Sage Science). Initial titration runs were       the possibility that residual sequencing errors may be introduced into the final
performed to optimize loading on the SMRT Cell for maximum performance. The            assembly of the Oropetium genome. Homozygous mismatches are classified as
Oropetium genome was sequenced using 32 SMRT Cells with 4-h collections and            sequencing errors, and heterozygous mismatches indicate sites of heterozygosity.
P6-C4 chemistry on the PacBio RS II platform (Pacific Biosciences).                    The accuracy rate is very high at 99.99995%, and a relatively high proportion of the
HGAP genome assembly. The Oropetium genome was assembled using the                     errors (two-thirds) are small insertions or deletions (indels). The accuracy rate is
RS_HGAP_Assembly.3 protocol for assembly and Quiver for genome polish-                 similar to those obtained with WGS Sanger approaches5,36 and is higher than those
ing in SMRT Analysis v2.3.012. This consisted of a three-step process involving        reported for most NGS-based assemblies. The estimated residual within-genome
(1) generation of preassembled reads with improved consensus accuracy;                 heterozygosity for the Oropetium genome is very low at 0.087%, which probably
(2) assembly of the genome through overlap consensus accuracy using Celera; and        contributed to the high contiguity of the assembly. This suggests that provided
(3) one round of genome polishing with Quiver. For HGAP, the following param-          sufficient coverage, a PacBio SMRT-only approach can produce a high-quality
eters were used: PreAssembler Filter v1 (minimum sub-read length =  3,000 bp,          complete plant genome.
minimum polymerase read quality =  0 .80, minimum polymerase read                      Repeat annotation. To structurally annotate repeat sequences in the Oropetium
length =  3,000 bp); PreAssembler v2 (minimum seed length = 16,000 bp, number          genome, we began by discovering repetitive elements through application of the
of seed read chunks =  6, alignment candidates per chunk = 10, total alignment         REPET v.2.2 packages TEdenovo and TEannot37. The TEdenovo pipeline ­compares
candidates =  24, min coverage for correction =  6); AssembleUnitig v1 (target         the genome with itself to identify and classify repeated genomic elements.
genome coverage =  30, overlap error rate =  0.06, minimum overlap =  40 bp and        All-by-all alignments were conducted with NCBI-BLAST+ using default
overlap k-mer =  14); and BLASR v1 mapping of reads for genome polishing with          TEdenovo p    ­ arameters. LTRharvest38 was used for structural detection. During
Quiver (max divergence percentage =  30, minimum anchor size =  12). A second          clustering, Grouper, Recon and Plier steps were invoked both with and without
round of genome polishing was performed using Quiver (SMRT Analysis v2.3.0) to         structural detection. Consensus building was performed using default parameters.
further improve the site-specific consensus accuracy of the assembly. The following    During consensus detect features, repeat scout39 was invoked, and Pfam26.0 HMM
Quiver parameters were used for genome polishing: filtering (minimum sub-read          profiles40 and Repbase (v18.08) nucleotide and amino acid databanks were used.
length =  3,000 bp, minimum polymerase read quality =  0.80, minimum polymer-          Finally, consensus classification, filtering and clustering were performed using
ase read length =  3,000 bp); mapping (maximum divergence percentage =  30,            default parameters.
minimum anchor size =  12). Default parameters were otherwise employed for both           Output from the TEdenovo pipeline was used as input to the TEannot pipeline.
HGAP assembly and Quiver protocols.                                                    This pipeline mines the genome sequence using repeated sequences identified in the
Falcon and MHAP assemblies. We also tested other assemblers to compare the             previous TEdenovo pipeline to produce classified non-redundant consensus repeat
PacBio HGAP assembly results (Extended Data Fig. 1i). Raw PacBio reads were            sequences along with short simple repeats, which are exported to GFF3 format.
error-corrected and assembled using Falcon and MHAP under default parame-              First, a set of perfectly matching sequences from the TEdenovo-output transposable
ters. The Falcon and MHAP assemblies have lower contiguity than the HGAP               elements (TE) library was selected by running a subset of the TEannot pipeline, pro-
assembly and have fewer assembled centromere and telomere sequences with a             ducing a working reference TE library. This TE library was used in a full run of the
lower average length.                                                                  TEannot pipeline. For alignment of the reference TE library, NCBI-BLAST+ was
Construction of a genome map using the Irys system for contig anchoring                used, and blaster, repeat masker and censor steps were run both on the reference TE
and scaffolding. Genome mapping from BioNano Genomics31 was used to                    library and on randomized chunks. Filtering was applied using default parameters.
improve the assembly quality of the Oropetium genome with the eventual goal            Short simple repeats were identified using the crossmatch engine. Merging was
of producing a chromosome-scale assembly. High molecular weight genomic                performed using default parameters. For comparisons, Repbase (v18.08) nucleotide
DNA was isolated from fresh Oropetium tissue using the following protocol              and amino acids databanks were used. Finally, filtering was applied using default
outline. Three grams of leaves were collected from live Oropetium thomaeum             parameters, and annotations were exported to GFF3 format.
plants and fixed with formaldehyde. After blending with a tissue homogenizer              To classify identified repeats, non-redundant consensus repeat sequences
in isolation buffer, a filtration step and Triton-X washing treatment were per-        as output by TEanno were annotated via PASTEClassifier v1.0 https://urgi.
formed. The nuclei were purified on percoll cushions. The nuclei were washed           versailles.inra.fr/Tools/PASTEClassifier/README). To classify these sequences,
extensively and embedded in low melting agarose at different dilutions. Finally,       Repbase (v18.08)41 nucleotide and amino acid sequences were used, as were
the DNA plugs were treated with a lysis buffer containing detergent, protein-          Pfam v26.0 (http://pfam.xfam.org/) HMM repeat profiles. Finally, identified
ase K and β -mercaptoethanol (BME). In total, 53 Gb of data (>100 kb) were             LTRs were classified as Gypsy if homology or motif evidence existed for Gypsy
collected representing ~200× genome coverage with a molecule N50 length of             and not for Copia, classified as Copia if the opposite were true, and otherwise
169 kb (Extended Data Fig. 5a). The size distribution was lower than expected          classified as unknown.
and is probably a result of impurities during high-molecular-weight gDNA               Centromere and telomere identification. Centromeric repeats were identified
isolation that would cause shearing and inhibition of enzymes. Molecules were          using an approach outlined in ref. 42. Tandem repeat finder (TRF, Version 4.07b)43
de novo assembled as previously described32. Two genome maps were assembled            was used to find tandem repeats using the parameters ‘1 1 2 80 5 200 2000-d
at different stringencies, map set 1 has 402 maps with an N50 length of 725 kb and     –h’ in order to find high order repeats. The resulting ‘.dat file’ was transformed
spans 216 Mb (Extended Data Fig. 5b); the second genome map has 214 maps and           into a GFF3 file, which was used to identify telomeric and centromeric repeats.
an N50 of 1.674 Mb. Combining the genome maps with the PacBio assembly to              To identify the centromeric repeats, the largest repeat arrays (period length X
produce a hybrid scaffold was performed sequentially with the two genome maps.         copy number) were identified and clustered. Clustered centromeric repeat regions
The scaffolding merged 90 contigs producing an assembly of 46 primary scaffolds        were transformed into FASTA files and aligned using clustalX to identify array
covering 94% of the sequence assembly with an N50 of 7.8 Mb; in total there are        sequence composition and orientation. The base centromere repeat was 155 bp
535 scaffolds with an N50 of 7.1 Mb and total assembled size of 244 Mb.                dimers (310 bp), trimers (465 bp) and tetramers (620 bp) (Extended Data Fig. 2
Variant calling using Illumina data. WGS Illumina sequences from Oropetium             and Supplementary Table 1). The three largest centromeric arrays (contigs 003,
gDNA were used to assess the error rate of the PacBio assembly and residual            028 and 064) were >400 kb and resolved into large inverted repeats, consistent
­within-genome heterozygosity (Supplementary Table 5). Raw Illumina HiSeq data         with them being full length. The telomeric repeats were identified by searching


                                                         © 2015 Macmillan Publishers Limited. All rights reserved
                                                                                                                                                     Letter RESEARCH

the ends of contigs for short (~7 bp) high copy number repeats; 18 telomeric repeat       to identify clusters of co-expressed and interacting duplicate genes, respectively
sequences with the monomer ‘AAACCCT’ were identified (Extended Data Table 1).             (Extended Data Fig. 6). Various network statistics were calculated using
Transcriptome assembly. Total RNA was extracted from fresh, desiccated and                NetworkAnalyzer55, including average number of neighbours (that is, protein inter-
24-h post rehydration Oropetium leaf tissues with 2 biological replicates collected       actions) and total number of isolated nodes (that is, without known interactors).
for each tissue. RNA-seq libraries were prepared from the total RNA and bar-coded         Constructing a gene interaction network. We constructed a gene interaction
using TruSeq RNA Sample Prep Kits (Illumina) according to the manufacturer’s              network for Oropetium on the basis of orthologous relationships with Arabidopsis
protocol. Raw Illumina RNA-seq data from the six libraries were trimmed for qual-         genes with validated interactions and expression data yielding a network with 4,421
ity using Trimmomatic (v.0.32; ref. 33). Illumina sequence adaptors were removed,         nodes (gene products) with 36,918 edges (interactions). This network encompasses
then leading low-quality (below quality 3) and N base pairs were trimmed and,             most metabolic pathways including photosynthesis, core anabolic and catabolic
finally, resulting trimmed reads were scanned using a 4-bp sliding window and cut         processes and stress response pathways (Extended Data Fig. 6).
when the average quality per base dropped below 30. Read pairs where both reads
were ultimately of at least 36 base pairs in length following this quality control pro-   30. Zhang, H.-B., Zhao, X., Ding, X., Paterson, A. H. & Wing, R. A. Preparation of
cess were retained and used for subsequent analyses. Trinity (v.r20140717)44 was              megabase-size DNA from plant nuclei. Plant J. 7, 175–184 (1995).
                                                                                          31. Lam, E. T. et al. Genome mapping on nanochannel arrays for structural
used to assemble quality filtered data. Assembled transcripts were aligned to our             variation analysis and sequence assembly. Nature Biotechnol. 30, 771–776
genome sequence using NCBI blastn v.2.2.30+ with an e-value cut-off of 1 ×  10−5.             (2012).
Successfully aligned transcripts were clustered at 90% identity using CD-HIT              32. Cao, H. et al. Rapid detection of structural variation in a human genome
(v. 4.5.4)45, with representative sequences from each cluster retained and used to            using nanochannel-based genome mapping technology. GigaScience 3,
help parameterize gene calling. Eighty-seven per cent of the trimmed RNA-seq                  34 (2014).
                                                                                          33. Bolger, A. M., Lohse, M. & Usadel, B. Trimmomatic: a flexible trimmer for
reads aligned to the Oropetium genome, suggesting that the genome is largely                  Illumina sequence data. Bioinformatics 30, 2114–2120 (2014).
complete (Supplementary Table 5). Reads that failed to align may have been                34. Li, H. & Durbin, R. Fast and accurate short read alignment with Burrows–
contaminants from other organisms.                                                            Wheeler transform. Bioinformatics 25, 1754–1760 (2009).
Gene annotation. Maker v2.31.846 (http://www.yandell-lab.org/software/maker.              35. McKenna, A. et al. The Genome Analysis Toolkit: a MapReduce framework for
html) was used to identify putative genes. Aligned and representative sequences               analyzing next-generation DNA sequencing data. Genome Res. 20, 1297–1303
                                                                                              (2010).
from our transcriptome assembly were input to Maker as expressed sequence tag
                                                                                          36. Ming, R. et al. The draft genome of the transgenic tropical fruit tree papaya
evidence. Rice and Brachypodium proteome sequences clustered at 90% iden-                     (Carica papaya Linnaeus). Nature 452, 991–996 (2008).
tity using CD-HIT (v. 4.5.4)45 with representative sequences from each cluster            37. Flutre, T., Duprat, E., Feuillet, C. & Quesneville, H. Considering transposable
retained and input to Maker as multi-organismal protein homology evidence.                    element diversification in de novo annotation approaches. PLoS ONE 6,
The Oropetium repeat database was input to Maker as a custom repeat library.                  e16526 (2011).
SNAPhmm, Augustus, and GeneMarkHMM were invoked by Maker and were                         38. Ellinghaus, D., Kurtz, S. & Willhoeft, U. LTRharvest, an efficient and flexible
                                                                                              software for de novo detection of LTR retrotransposons. BMC Bioinformatics 9,
initially trained using rice and maize. Only genes for which the encoded protein              18 (2008).
was predicted to contain a complete open reading frame were retained.                     39. Price, A. L., Jones, N. C. & Pevzner, P. A. De novo identification of repeat families
    On the basis of the gene annotations provided by Maker, cufflinks (v2.2.1)47 was          in large genomes. Bioinformatics 21, i351–i358 (2005).
used to identify predicted genes without empirical expression evidence. Quality-          40. Finn, R. D. et al. Pfam: the protein families database. Nucleic Acids Res. 42,
trimmed data from all six RNA-seq libraries were input simultaneously to cufflinks,           D222–D230 (2014).
                                                                                          41. Jurka, J. et al. Repbase Update, a database of eukaryotic repetitive elements.
with results used to identify genes with and without expression.                              Cytogenet. Genome Res. 110, 462–467 (2005).
    Protein sequences from genes predicted by Maker were functionally annotated           42. Melters, D. P. et al. Comparative analysis of tandem repeats from hundreds of
using NCBI blastp v.2.2.30+ versus the NCBI non-redundant refseq protein data-                species reveals unique insights into centromere evolution. Genome Biol. 14,
base (http://www.ncbi.nlm.nih.gov/refseq/), versus the UniProt database48, and                R10 (2013).
using InterProScan (v. 5.6-48.0)49.                                                       43. Benson, G. Tandem repeats finder: a program to analyze DNA sequences.
                                                                                              Nucleic Acids Res. 27, 573 (1999).
    Finally, Maker-predicted genes were pruned based on a Maker-defined anno-
                                                                                          44. Grabherr, M. G. et al. Full-length transcriptome assembly from
tation edit distanced (AED) score that measures distance between the predicted                RNA-Seq data without a reference genome. Nature Biotechnol. 29, 644–652
gene and the evidence input to Maker, non-redundant (NR) annotation, Uniprot                  (2011).
annotation, InterProScan annotation and expression level as output by cufflinks.          45. Huang, Y., Niu, B., Gao, Y., Fu, L. & Li, W. CD-HIT Suite: a web server for
Genes were removed that had no alignment evidence (AED =  1), no sequence                     clustering and comparing biological sequences. Bioinformatics 26, 680–682
match to either the NR or Uniprot databases, no InterProScan predicted domains                (2010).
                                                                                          46. Cantarel, B. L. et al. MAKER: an easy-to-use annotation pipeline designed for
and no expression evidence in our RNA-seq data.                                               emerging model organism genomes. Genome Res. 18, 188–196 (2008).
Synteny and comparative genomics. Genome data sets from Setaria, Sorghum,                 47. Trapnell, C. et al. Differential gene and transcript expression analysis of
rice and Brachypodium were downloaded from Phytozome (version 9.1) and                        RNA-seq experiments with TopHat and Cufflinks. Nature Protocols 7, 562–578
subject to pairwise genome alignments against the Oropetium genome. For each                  (2012).
pairwise alignment, the coding sequences of predicted gene models are compared            48. Wu, C. H. et al. The Universal Protein Resource (UniProt): an expanding
                                                                                              universe of protein information. Nucleic Acids Res. 34, D187–D191 (2006).
to each other using adaptive seeds50. Our synteny search pipeline defines syntenic        49. Quevillon, E. et al. InterProScan: protein domains identifier. Nucleic Acids Res.
blocks by chaining the large-scale alignment tool (LAST) hits with a distance cut-            33, W116–W120 (2005).
off of 20 genes apart, also requiring at least four gene pairs per syntenic block.        50. Kiełbasa, S. M., Wan, R., Sato, K., Horton, P. & Frith, M. C. Adaptive seeds tame
The syntenic blocks were further screened using QUOTA-ALIGN51 to retain one-                  genomic sequence comparison. Genome Res. 21, 487–493 (2011).
to-one blocks and to exclude weak blocks derived from shared ancient duplications.        51. Tang, H. et al. Screening synteny blocks in pairwise genome comparisons
                                                                                              through integer programming. BMC Bioinformatics 12, 102 (2011).
The resulting dot plots were visually inspected to confirm the structural similarity
                                                                                          52. Li, L., Stoeckert, C. J. & Roos, D. S. OrthoMCL: identification of ortholog groups
of the Oropetium genome in relation to other genomes (Extended Data Fig. 3a–e).               for eukaryotic genomes. Genome Res. 13, 2178–2189 (2003).
    Pairwise genomic alignments, described above, combined with OrthoMCL52                53. Franceschini, A. et al. STRING v9. 1: protein-protein interaction networks, with
analyses filtered to one-to-one hits were used to identify orthologous gene ­clusters         increased coverage and integration. Nucleic Acids Res. 41, D808–D815
between Oropetium and Sorghum, rice, Vitis and Arabidopsis. The c­ omplete                    (2013).
Oropetium–Arabidopsis orthologue list was then filtered to focus on genes with            54. Saito, R. et al. A travel guide to Cytoscape plugins. Nature Methods 9,
                                                                                              1069–1076 (2012).
functional data in the STRING v9.1 global Arabidopsis protein interaction                 55. Doncheva, N. T., Assenov, Y., Domingues, F. S. & Albrecht, M. Topological
network53. Gene expression patterns and duplicated genes (tandem and whole-­                  analysis and interactive visualization of biological networks and protein
genome duplicates) were mapped onto this network using Cytoscape v3.1.154                     structures. Nature Protocols 7, 670–685 (2012).




                                                            © 2015 Macmillan Publishers Limited. All rights reserved
 RESEARCH Letter




Extended Data Figure 1 | Summary of the Oropetium genome assembly                   N50 length (e) of all published plant genomes is plotted. The average
statistics. a, Histogram of length distribution of raw P6C4 chemistry               contig N50 length for published plant genomes is ~50 kb compared to
PacBio reads. The mean read length of the raw reads is 12,872 bp, and the           2.4 Mb for Oropetium. f, g, Repeat density (as a function of percentage
N50 is 16,485 bp. b, Genome size estimation using k-mer distribution.               repeats) (f) and GC content (g) are plotted at a scaled position along each
K-mer distribution of unassembled Oropetium Illumina WGS reads.                     contig. Each contig was divided into 5,000 sliding windows with each
K-mer frequency displays a unimodal curve indicating a low rate of                  window representing 0.02% of the contig length and the averages of each
heterozygosity in the Oropetium genome. Frequency distribution suggests             scaled sliding window are plotted. Repeat content and GC content do
a genome size of ~245 Mb, consistent with flow-cytometry-based                      not vary at the ends of contigs. h, Estimated accuracy of SMRT PacBio
estimations. c, SMRT sequencing raw read, preassembly and assembly                  assembly and within-genome heterozygosity. i, Comparison of HGAP
statistics. d, e, The distribution of the contig N50 length (d) and scaffold        Falcon and MHAP PacBio assemblers.



                                                      © 2015 Macmillan Publishers Limited. All rights reserved
                                                                                                                                  Letter RESEARCH




Extended Data Figure 2 | PacBio sequencing and assembly completely               identity between monomers in the repeat decreases. c, The inverted repeat
resolves the Oropetium centromeres. a, The Oropetium centromere                  structure of the entire centromere on contig028 with a 60 kb spacer (blue
repeat base is 155 bp (red arrow), whereas they are also found in dimer          box); arrows are as in a. d, Consensus 155 bp centromere monomer.
(310 bp, grey arrow), trimer (465 bp, black arrow) and tetramer (620 bp,         e, Integrated genome browser view of centromere repeat, LTRs and
white arrow) form. b, As the copy number of a repeat increases, the match        predicted genes on contig028.




                                                   © 2015 Macmillan Publishers Limited. All rights reserved
 RESEARCH Letter




Extended Data Figure 3 | Macrosynteny patterns and comparative                    Syntenic block span is based on regions that show conserved synteny
genomics between the grasses. a–e, Macrosynteny of Oropetium versus               across all five genomes. Syntenic gene and coding DNA sequences span is
Oropetium (a); Oropetium versus Brachypodium (b); Oropetium versus                based on 13,683 genes that are retained as genes in orthologous locations
rice (c); Oropetium versus Setaria (d); and Oropetium versus Sorghum (e).         across all five genomes. The ratio compared to Oropetium is given in
f, Genome compaction in Oropetium compared to related grass genomes.              brackets.




                                                    © 2015 Macmillan Publishers Limited. All rights reserved
                                                                                                                                 Letter RESEARCH




Extended Data Figure 4 | Expansion of intragenic and pericentric                 annotated at the bottom in black. b, Pericentric region expansion in
regions in Sorghum compared to Oropetium. a, A GEvo sequence                     Sorghum compared to Oropetium. A syntenic dot plot of the Sorghum
similarity graphic of an Oropetium gene (upper) and its orthologous              and Oropetium genomes is plotted. Oropetium contigs are ordered based
Sorghum gene (lower). Blast hits (high-scoring segment pairs) are denoted        on synteny with Sorghum. Hits are coloured based on Ks divergence,
by red rectangles, and syntenic hits are connected by a red line. The            with purple blocks corresponding to 1:1 orthologous regions and other
green rectangles on the model line of Sorghum are conserved noncoding            colours corresponding to retained genes from the rho and sigma WGDs.
sequences (CNS) computed between Sorghum and rice; the expanse of                Pericentric regions in Sorghum have few syntenic matches to Oropetium,
CNS coverage defines ‘gene space’. Within the oval are three CNS that            suggesting that much of the expansion occurred in pericentric regions.
may be spatially constrained. The expanded interspersed sequences are




                                                   © 2015 Macmillan Publishers Limited. All rights reserved
 RESEARCH Letter




Extended Data Figure 5 | Assembly improvement using a Bionano-                  the genome assembly. Overlap between the PacBio-based contigs and the
based genome map from the Irys system. a, Distribution of molecule size         genome map. Each line shows a single PacBio contig in green; genome
for raw single-molecule genome mapping data. Size of single molecules           maps are shown in light blue.
in nanochannel arrays is plotted. b, Integration of the genome map with




                                                  © 2015 Macmillan Publishers Limited. All rights reserved
                                                                                                                           Letter RESEARCH




Extended Data Figure 6 | Network statistics for tandem duplicated genes. a, Tandem duplicated genes in the metabolic network are shown in pink.
b, Distribution of shared neighbours. c, The average number of neighbours.




                                                  © 2015 Macmillan Publishers Limited. All rights reserved
 RESEARCH Letter

Extended Data Table 1 | Telomere repeat (AAACCCT) locations and organization in the Oropetium genome




                                            © 2015 Macmillan Publishers Limited. All rights reserved
                                                                                                       Letter RESEARCH

Extended Data Table 2 | rRNA tandem array locations and organization in the Oropetium genome




                                            © 2015 Macmillan Publishers Limited. All rights reserved
 RESEARCH Letter

Extended Data Table 3 | Repeat annotation of the Oropetium genome




                                            © 2015 Macmillan Publishers Limited. All rights reserved
                                                                                                        Letter RESEARCH

Extended Data Table 4 | Comparisons of repeats and coding features in the monocotyledons




                                             © 2015 Macmillan Publishers Limited. All rights reserved
