# Mendes 2020

**Source PDF:** 

---

                                                                                                  Bioinformatics, 36(22-23), 2020, 5516–5518
                                                                                                         doi: 10.1093/bioinformatics/btaa1022
                                                                                     Advance Access Publication Date: 16 December 2020
                                                                                                                      Applications Note




Genome analysis
CAFE 5 models variation in evolutionary rates among
gene families
Fábio K. Mendes1,2,†, Dan Vanderpool                                           1, ,†
                                                                                  * , Ben Fulton1,3,† and Matthew W. Hahn1,4




                                                                                                                                                                   Downloaded from academic.oup.com/bioinformatics/article/36/22-23/5516/6039105 by guest on 30 August 2026
1
 Department of Biology, Indiana University, Bloomington, IN 47405, USA, 2Department of Computer Science, The University of
Auckland, 1010 Auckland, New Zealand, 3Department of Computer Science, University Information Technology Services, Indiana
University, Bloomington, IN 47405, USA and 4Department of Computer Science, Indiana University, Bloomington, IN 47405, USA
*To whom correspondence should be addressed.
†
 The authors wish it to be known that, in their opinion, the first three authors should be regarded as Joint First Authors.
Associate Editor: Peter Robinson
Received on June 2, 2020; revised on November 12, 2020; editorial decision on November 25, 2020; accepted on November 30, 2020


Abstract
Motivation: Genome sequencing projects have revealed frequent gains and losses of genes between species.
Previous versions of our software, Computational Analysis of gene Family Evolution (CAFE), have allowed research-
ers to estimate parameters of gene gain and loss across a phylogenetic tree. However, the underlying model
assumed that all gene families had the same rate of evolution, despite evidence suggesting a large amount of vari-
ation in rates among families.
Results: Here, we present CAFE 5, a completely re-written software package with numerous performance and user-
interface enhancements over previous versions. These include improved support for multithreading, the explicit
modeling of rate variation among families using gamma-distributed rate categories, and command-line arguments
that preclude the use of accessory scripts.
Availability and implementation: CAFE 5 source code, documentation, test data and a detailed manual with exam-
ples are freely available at https://github.com/hahnlab/CAFE5/releases.
Contact: danvand@indiana.edu
Supplementary information: Supplementary data are available at Bioinformatics online.



1 Introduction                                                                              CAFE models rates of change among gene families with a birth-
                                                                                        death distribution having a mean rate (k) of gain and loss common
The earliest eukaryotic genome sequencing projects revealed large                       to all families. In reality, individual families can evolve at very dif-
and frequent changes between species in the size of gene families                       ferent rates, with the most rapidly evolving families in terms of gain
(Gibbs et al., 2007; Rubin et al., 2000; Waterston et al., 2002).                       and loss (e.g. sex and reproduction-related, immunity) being the
Variation in family size results from the gain or loss of genes, either                 same as those observed to be evolving most rapidly at the sequence
of which may be advantageous, deleterious or neutral. To enable the                     level (Demuth et al., 2006; Hahn et al., 2007). Furthermore, there
rigorous study of changes in gene family size, we previously pro-                       appears to be a class of genes that are extremely resistant to duplica-
posed a statistical framework that would allow for inferences                           tion or loss, a trait that can be used to assess genome assembly qual-
regarding gene family evolution among species along a phylogenetic                      ity (Waterhouse et al., 2013). Recent studies have confirmed
tree (Hahn et al., 2005). We showed that this model can be used for                     variation in rates among families to be true in many different taxa
hypothesis testing, inference of ancestral states and estimation of                     (Casola and Lawing, 2019). Both DupliPHY (Ames et al., 2012) and
gene duplication and loss rates. Since its release, the software imple-                 Badirate (Librado et al., 2012), older programs designed for gene
menting this model, Computational Analysis of gene Family                               family analysis, employ measures to account for rate variation
Evolution (CAFE), has been steadily improved to accommodate                             among families in some way.
growing genomic resources (De Bie et al., 2006; Han et al., 2013).                          Here, we present CAFE 5, an upgrade that explicitly models
CAFE continues to be widely used in comparative genomics.                               rate-variation among families in a manner directly analogous
However, in order to fully exploit the benefits of the rapidly grow-                    to similar models used for nucleotides and amino acids. Below
ing number of sequenced genomic datasets, improvements such as                          we describe the implementation and testing of this model, as
multi-core parallelization and more sophisticated models of gene                        well as the other new features and improvements included in
family evolution must be implemented.                                                   CAFE 5.



C The Author(s) 2020. Published by Oxford University Press. All rights reserved. For permissions, please e-mail: journals.permissions@oup.com
V                                                                                                                                                         5516
CAFE 5 models variation in evolutionary rates among gene families                                                                                                         5517




                                                                                                                                                                                    Downloaded from academic.oup.com/bioinformatics/article/36/22-23/5516/6039105 by guest on 30 August 2026
Fig. 1. Evolutionary rate (k) estimated for empirical and simulated data under an increasing number of discrete rate categories (K). (A) k estimated for three empirical datasets
under increasing values of K. (B) Data simulated using the maximum likelihood values estimated for each dataset in A. The simulated values of k are indicated by the dashed
lines. The * indicates the value of k for which the highest likelihood was estimated, in both panels


2 Materials and methods                                                                    overestimate k. This latter effect is likely due to the bifurcation of
                                                                                           the data into one rate category for families that undergo little or no
2.1 Improved performance, stability and usability of                                       change and the other category accounting for all other families that
CAFE                                                                                       change across the tree.
CAFE 5 introduces a more modular style of programming with a re-                               To assess the accuracy of the software and these results, we
write from C into Cþþ. The current version employs powerful com-                           simulated three datasets (see Supplementary Material for simulation
pilers and matrix multiplication libraries and is able to take                             conditions) intended to match the distributions inferred from the
advantage of multiple cores, with noticeable performance increases                         empirical data. In all cases, CAFE 5 accurately estimated the max-
up to at least 64 cores (Supplementary Fig. S1). To provide a simpler                      imum likelihood value of k and of K (Fig. 1b). As in the empirical
experience for the user, the script-based paradigm of earlier versions                     datasets, we also see that k is consistently underestimated with K¼1,
has been discarded in favor of a strictly command-line interface.                          and slightly overestimated for K ¼ 2–3.
Output files have been reconfigured to minimize post-processing,
with trees written to a Nexus file for easy viewing.
                                                                                           4 Summary
2.2 New features in CAFE 5
A common approach used in molecular phylogenetics to model vari-                           •   CAFE 5 is now written in Cþþ, a modular style of programming
ation in rates among nucleotide or amino acid sites is to use a dis-                           facilitating future development.
crete approximation of the gamma (C) distribution (Yang, 1994).                            •   Support for powerful compilers, parallelization and matrix
CAFE 5 uses this same approach (as does DupliPHY, Ames et al.,                                 multiplication allow CAFE 5 to take advantage of high-
2012), with the number of discrete rate categories, K, specified a pri-                        performance computing clusters.
ori and each category assumed equi-probable (1/K). The C distribu-                         •   Accurate and fast joint ancestral state reconstruction is now
tion is scaled such that the mean rate across categories is 1, with
shape parameter a (¼b) estimated from the data. The shape of the C                             available.
distribution determines a unique rate for each category, under which                       •   Variation in the evolutionary rate among gene families is accounted
a gene family has its probability (given a set of parameter values)                            for using a discrete approximation of the gamma distribution.
calculated. CAFE 5 then uses an empirical Bayes approach to esti-
mate the posterior probability of a family belonging to a rate cat-
egory, which in turn enables down-stream analyses of ‘slow’ or ‘fast’                      Accounting for rate variation among families using a discrete
families.                                                                                  gamma approximation results in a better model fit and more accur-
    In addition, ancestral state reconstruction is now performed                           ate rate estimates. While this can be accomplished with as few as
using the algorithm of Pupko et al. (2000), resulting in run times                         K¼2 rate categories, we recommend testing K¼3–4 categories with
that scale linearly with the number of taxa in the tree.                                   real data.


3 Results                                                                                  Acknowledgements
We used CAFE 5 to analyze three published datasets consisting of                           The authors thank Simon Whelan, Robert Henschel and Gregg Thomas for
gene families from primates (Thomas et al., 2020b), birds of para-                         help throughout this project.
dise (Prost et al., 2019) and Hymenoptera (Thomas et al., 2020a).
For each dataset rates were estimated using increasing values for K
(Fig. 1a).For primates, the highest likelihood was found using K¼4                         Funding
rate categories, with k¼0.00453 and a¼0.62. The birds of paradise                          This work was supported by National Science Foundation [DBI-1564611 to
dataset had the highest likelihood using K¼10 rate categories, with                        M.W.H.].
k¼0.00226 and a¼0.98. The Hymenoptera had the highest likeli-
                                                                                           Conflict of Interest: none declared.
hood using K¼6 rate categories, with k¼0.00375 and a¼0.373. As
expected (Gillespie, 1986; Golding, 1984; Yang, 1996) single-rate
models consistently underestimate k (Fig. 1a), highlighting the need
to model rate variation. Although K > 1 always results in higher                           References
likelihoods, the maximum likelihood value does not always have the                         Ames,R.M. et al. (2012) Determining the evolutionary history of gene fami-
largest value of K considered; indeed, models with K ¼ 2–3 often                            lies. Bioinformatics, 28, 48–55.
5518                                                                                                                                         F.K.Mendes et al.


Casola,C. and Lawing,A.M. (2019) The nonrandom evolution of gene fami-            Prost,S. et al. (2019) Comparative analyses identify genomic features poten-
  lies. Am. J. Bot., 106, 14–17.                                                    tially involved in the evolution of birds-of-paradise. GigaScience, 8, giz003.
De Bie,T. et al. (2006) CAFE: a computational tool for the study of gene family   Pupko,T. et al. (2000) A fast algorithm for joint reconstruction of ancestral
  evolution. Bioinformatics, 22, 1269–1271.                                         amino acid sequences. Mol. Biol. Evol., 17, 890–896. https://doi.org/10.
Demuth,J.P. et al. (2006) The evolution of mammalian gene families. PLoS            1093/oxfordjournals.molbev.a026369
  One, 1, e85.                                                                    Rubin,G.M. et al. (2000) Comparative genomics of the eukaryotes. Science,
Gibbs,R.A. et al.; Rhesus Macaque Genome Sequencing and Analysis                    287, 2204–2215.
  Consortium. (2007) Evolutionary and biomedical insights from the Rhesus         Thomas,G.W.C. et al. (2020a) Gene content evolution in the arthropods.
  Macaque Genome. Science, 316, 222–234.                                            Genome Biol., 21, 15.
Gillespie,J.H. (1986) Variability of evolutionary rates of DNA. Genetics, 113,    Thomas,G.W.C. et al. (2020b) Origins and long-term patterns of copy-number
  1077–1091.                                                                        variation in rhesus macaques. Mol. Biol. and Evol., msaa303. https://doi.org/10.
Golding,G.B. (1984) Estimates of DNA and protein sequence divergence: an            1093/molbev/msaa303
  examination of some assumptions. Mol. Biol. Evol., 1, 125–142.                  Waterhouse,R.M. et al. (2013) OrthoDB: a hierarchical catalog of animal,
Hahn,M.W. et al. (2005) Estimating the tempo and mode of gene family                fungal and bacterial orthologs. Nucleic Acids Res., 41, D358–D365. https://
  evolution from comparative genomic data. Genome Res., 15,                         doi.org/10.1093/nar/gks1116
  1153–1160.                                                                      Waterston,R.H. et al.; Mouse Genome Sequencing Consortium. (2002) Initial




                                                                                                                                                                       Downloaded from academic.oup.com/bioinformatics/article/36/22-23/5516/6039105 by guest on 30 August 2026
Hahn,M.W. et al. (2007) Gene family evolution across 12 Drosophila                  sequencing and comparative analysis of the mouse genome. Nature, 420,
  genomes. PLoS Genet., 3, e197.                                                    520–562.
Han,M.V. et al. (2013) Estimating gene gain and loss rates in the presence of     Yang,Z. (1994) Maximum likelihood phylogenetic estimation from DNA
  error in genome assembly and annotation using CAFE 3. Mol. Biol. Evol.,           sequences with variable rates over sites: approximate methods. J. Mol.
  30, 1987–1997.                                                                    Evol., 39, 306–314.
Librado,P. et al. (2012) BadiRate: estimating family turnover rates by            Yang,Z. (1996) Among-site rate variation and its impact on phylogenetic anal-
  likelihood-based methods. Bioinformatics, 28, 279–281.                            yses. Trends Ecol. Evol., 11, 367–372.
