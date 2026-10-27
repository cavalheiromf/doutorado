# Supplementary Tables

## Table S1. Curated genomic coordinates, predicted protein physicochemical descriptors, and membrane topology of the OSCA mechanosensitive ion channel family in *Vellozia peripherica*, *Vellozia tubiflora*, and *Xerophyta schlechteri*

Genomic locations and structural exon-intron boundaries were derived from chromosome-scale haplotype-1 reference annotations (`Vper.hap1.v1` and `Vtub.hap1.v1`), reporting 1-based start and end coordinates along the 17 pseudochromosomes. Molecular weight (MW, in kDa) and theoretical isoelectric point (pI) were computed from deduced full-length amino acid sequences using the `Bio.SeqUtils.ProtParam` module in `Biopython`. Canonical functional domain signatures were identified using `InterProScan` and `HMMER`, verifying family assignment to PANTHER `PTHR13018` alongside Pfam profiles `PF02714` (RSN1_7TM pore-forming domain), `PF14703` (calcium-dependent channel domain), and `PF13967` (cytoplasmic domain). Transmembrane helix (TMH) counts were predicted independently using both `TMHMM` and `Phobius` integrated within the InterProScan pipeline; differences between algorithms reflect distinct topology-modeling heuristics. Note that *VpOSCA2.2* and *VtOSCA1.2* represent shortened gene models lacking a detectable `PF13967` signature, which are retained in the family inventory as locus-specific structural variants. Loci in the desiccation-tolerant sister outgroup *X. schlechteri* are reported based on the predicted proteome from Costa et al. (2017).

| Gene | Transcript | Chr | Start (1-based) | End (1-based) | Strand | Length (aa) | MW (kDa) | pI | TMHMM TMHs | Phobius TMHs | Pfam domains | PANTHER |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VpOSCA1.1 | Vper.hap1.v1.chr4.g117080.t1 | chr4 | 11237809 | 11254982 | - | 824 | 94.61 | 9.293 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA1.2 | Vper.hap1.v1.chr9.g255760.t1 | chr9 | 17564348 | 17578689 | - | 796 | 90.59 | 8.747 | 8 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA1.3 | Vper.hap1.v1.chr7.g186390.t1 | chr7 | 1154965 | 1162617 | + | 784 | 90.92 | 9.168 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA1.4 | Vper.hap1.v1.chr7.g186400.t1 | chr7 | 1165819 | 1173766 | + | 737 | 84.85 | 8.941 | 7 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA1.5 | Vper.hap1.v1.chr7.g186410.t1 | chr7 | 1190164 | 1199238 | + | 777 | 89.06 | 9.332 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA2.1 | Vper.hap1.v1.chr5.g140750.t1 | chr5 | 1645548 | 1653691 | + | 740 | 84.05 | 8.873 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA2.2 | Vper.hap1.v1.chr1.g021690.t1 | chr1 | 21367424 | 21371278 | - | 478 | 54.42 | 9.464 | 6 | 7 | PF02714;PF14703 | PTHR13018 |
| VpOSCA2.3 | Vper.hap1.v1.chr1.g013600.t1 | chr1 | 13332253 | 13336746 | + | 718 | 81.89 | 9.067 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA2.4a | Vper.hap1.v1.chr1.g023030.t1 | chr1 | 22689053 | 22697439 | + | 639 | 72.62 | 8.823 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA2.4b | Vper.hap1.v1.chr1.g023020.t1 | chr1 | 22678817 | 22687760 | + | 662 | 75.23 | 8.233 | 11 | 11 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA2.5 | Vper.hap1.v1.chr9.g257040.t1 | chr9 | 18576255 | 18590260 | - | 636 | 72.22 | 8.664 | 10 | 11 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA3.1 | Vper.hap1.v1.chr1.g020450.t1 | chr1 | 20008266 | 20014313 | + | 734 | 83.15 | 9.335 | 9 | 10 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA3.2 | Vper.hap1.v1.chr5.g142080.t1 | chr5 | 2668390 | 2675373 | - | 733 | 83.16 | 9.444 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VpOSCA4.1 | Vper.hap1.v1.chr8.g231320.t1 | chr8 | 20598463 | 20602234 | - | 802 | 89.81 | 6.553 | 10 | 10 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA1.1 | Vtub.hap1.v1.chr4.g106800.t1 | chr4 | 10819228 | 10835638 | - | 766 | 87.63 | 9.117 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA1.2 | Vtub.hap1.v1.chr9.g230740.t1 | chr9 | 17719980 | 17728315 | - | 485 | 55.12 | 8.951 | 5 | 6 | PF02714;PF14703 | PTHR13018 |
| VtOSCA1.3 | Vtub.hap1.v1.chr7.g166590.t1 | chr7 | 1018481 | 1027560 | + | 869 | 100.53 | 8.848 | 12 | 11 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA1.4 | Vtub.hap1.v1.chr7.g166600.t1 | chr7 | 1029793 | 1039945 | + | 833 | 96.53 | 9.366 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA1.5 | Vtub.hap1.v1.chr7.g166610.t1 | chr7 | 1049542 | 1057767 | + | 760 | 87.54 | 9.482 | 10 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA2.1 | Vtub.hap1.v1.chr5.g127830.t1 | chr5 | 1496337 | 1503868 | + | 676 | 76.69 | 8.584 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA2.2 | Vtub.hap1.v1.chr1.g019410.t1 | chr1 | 20232005 | 20238727 | - | 745 | 84.87 | 9.31 | 9 | 8 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA2.3 | Vtub.hap1.v1.chr1.g012080.t1 | chr1 | 12783203 | 12787679 | + | 718 | 81.88 | 9.023 | 9 | 9 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA2.4 | Vtub.hap1.v1.chr1.g020650.t1 | chr1 | 21645213 | 21654612 | + | 750 | 85.49 | 8.905 | 11 | 11 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA2.5 | Vtub.hap1.v1.chr9.g231910.t1 | chr9 | 18668637 | 18684281 | - | 634 | 71.83 | 8.669 | 10 | 11 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA3.1 | Vtub.hap1.v1.chr1.g018250.t1 | chr1 | 18922459 | 18928500 | + | 734 | 83.29 | 9.451 | 9 | 10 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA3.2 | Vtub.hap1.v1.chr5.g129040.t1 | chr5 | 2457575 | 2466320 | - | 772 | 87.49 | 9.462 | 9 | 10 | PF02714;PF13967;PF14703 | PTHR13018 |
| VtOSCA4.1 | Vtub.hap1.v1.chr8.g207990.t1 | chr8 | 24477669 | 24481020 | - | 802 | 89.96 | 6.523 | 10 | 11 | PF02714;PF13967;PF14703 | PTHR13018 |
| XsOSCA1.1 | MP011677 | - | - | - | - | 766 | 87.94 | 9.237 | - | - | PF02714;PF13967;PF14703 | PTHR13018 |
| XsOSCA2.1 | MP002111 | - | - | - | - | 744 | 84.54 | 9.110 | - | - | PF02714;PF13967;PF14703 | PTHR13018 |
| XsOSCA2.2 | MP013956 | - | - | - | - | 681 | 77.01 | 8.893 | - | - | PF02714;PF13967;PF14703 | PTHR13018 |
| XsOSCA2.3 | MP001327 | - | - | - | - | 718 | 81.83 | 9.000 | - | - | PF02714;PF13967;PF14703 | PTHR13018 |
| XsOSCA2.4 | MP002250 | - | - | - | - | 337 | 38.55 | 8.855 | - | - | PF02714;PF13967;PF14703 | PTHR13018 |
| XsOSCA3.1 | MP001991 | - | - | - | - | 734 | 83.13 | 9.368 | - | - | PF02714;PF13967;PF14703 | PTHR13018 |
| XsOSCA3.2 | MP014080 | - | - | - | - | 750 | 85.37 | 9.417 | - | - | PF02714;PF13967;PF14703 | PTHR13018 |
| XsOSCA4.1 | MP022802 | - | - | - | - | 804 | 90.05 | 6.901 | - | - | PF02714;PF13967;PF14703 | PTHR13018 |

## Table S2. Evaluation of selection intensity shifts across the analyzed OSCA gene-tree datasets using HyPhy RELAX

Lineage-specific shifts in selection constraint were modeled with `RELAX` in `HyPhy` under the `MG94xREV` codon substitution framework. The primary analysis evaluated the codon alignment across all 27 validated *Vellozia* OSCA loci (639 codon sites retained after filtering alignment columns with $> 20\%$ gaps across taxa). A maximum-likelihood gene-tree topology was conditioned with all 13 terminal branches of the desiccation-tolerant specialist (*V. tubiflora*) designated as the Test set, and all 14 terminal branches of the evergreen congener (*V. peripherica*) designated as the Reference set. The selection intensity parameter $k$ ($\omega_{\text{Test}} = \omega_{\text{Ref}}^k$) was evaluated via a likelihood ratio test (LRT, $2\Delta\ln L \sim \chi^2_1$). The primary fit produced $k = 0.7064$ and $p = 0.000337$; the direction and significance were retained with ten optimization starting points and with an alternative gap filter.

| Dataset | Codons | K | LRT | p-value | Reference branches | Test branches | Unclassified branches |
|---|---|---|---|---|---|---|---|
| Primary full-family fit | 639 | 0.7064 | 12.8509 | 0.000337 | 14 | 13 | 24 |
| Optimization sensitivity (10 starting points) | 639 | 0.7130 | 11.2788 | 0.000784 | 14 | 13 | 24 |
| Alignment-filter sensitivity (>50% gaps removed) | 735 | 0.8105 | 5.4587 | 0.019471 | 14 | 13 | 24 |

Exploratory clade-specific fits used locally aligned codon datasets. The corrected OSCA3-only dataset contained *OSCA3.1* and *OSCA3.2* from each species and explicitly excluded the two OSCA4 loci that had been combined with OSCA3 in a superseded exploratory analysis. Because the OSCA3-only fit contained only two Test and two Reference terminal branches, it was treated as a low-power secondary analysis.

| Clade-specific analysis | Gap-column filter | Starting points | Codons | K | LRT | p-value | Interpretation |
|---|---|---:|---:|---:|---:|---:|---|
| OSCA1 | >20% removed | 1 | 761 | 0.9262 | 0.2630 | 0.608050 | Not significant |
| OSCA2 | >20% removed | 1 | 601 | 0.8191 | 0.8931 | 0.344631 | Not significant |
| OSCA3 only, primary | >20% removed | 1 | 733 | 0.2565 | 3.1720 | 0.074910 | Not significant |
| OSCA3 only, optimization sensitivity | >20% removed | 10 | 733 | 0.2579 | 3.1806 | 0.074517 | Not significant |
| OSCA3 only, optimization sensitivity | >20% removed | 25 | 733 | 0.3188 | 3.1655 | 0.075210 | Not significant |
| OSCA3 only, alignment-filter sensitivity | >50% removed | 1 | 734 | 0.2899 | 3.3423 | 0.067520 | Not significant |

## Table S3. Pairwise nonsynonymous and synonymous substitution rate estimates ($d_N$, $d_S$, and $\omega$) across 15 focal OSCA channel comparisons in *Vellozia*

Pairwise coding-sequence divergence was estimated across 15 focal comparisons, comprising the 12 single-copy interspecific orthologous pairs, both *VpOSCA2.4a* and *VpOSCA2.4b* paired with *VtOSCA2.4*, and the intraspecific tandem duplicate pair *VpOSCA2.4a* versus *VpOSCA2.4b*. Pairwise protein alignments generated with `MAFFT` were converted into codon alignments with their corresponding coding sequences using `PAL2NAL` under strict gap and mismatch removal (`-output paml -nogap -nomismatch`). Nonsynonymous substitution rates ($d_N$ or $K_a$), synonymous substitution rates ($d_S$ or $K_s$), and their ratio ($\omega = d_N/d_S$) were estimated using the maximum-likelihood method of Yang and Nielsen (2000) implemented in `YN00` within `PAML` under the universal genetic code (`icode = 0`, `weighting = 0`, `commonf3x4 = 0`). All analyzed pairs exhibit $\omega < 1.00$, confirming pervasive purifying selection across the channel family.

| Pair | Ks | Ka | omega |
|---|---|---|---|
| VpOSCA1.1_VtOSCA1.1 | 0.0371 | 0.0124 | 0.3332 |
| VpOSCA1.2_VtOSCA1.2 | 0.0987 | 0.0416 | 0.4211 |
| VpOSCA1.3_VtOSCA1.3 | 0.0761 | 0.023 | 0.3015 |
| VpOSCA1.4_VtOSCA1.4 | 0.1094 | 0.0877 | 0.8015 |
| VpOSCA1.5_VtOSCA1.5 | 0.098 | 0.0684 | 0.6979 |
| VpOSCA2.1_VtOSCA2.1 | 0.0757 | 0.0227 | 0.2993 |
| VpOSCA2.2_VtOSCA2.2 | 0.0912 | 0.0634 | 0.6947 |
| VpOSCA2.3_VtOSCA2.3 | 0.0859 | 0.0046 | 0.053 |
| VpOSCA2.4a_VpOSCA2.4b | 0.1172 | 0.0442 | 0.377 |
| VpOSCA2.4a_VtOSCA2.4 | 0.1215 | 0.0363 | 0.2985 |
| VpOSCA2.4b_VtOSCA2.4 | 0.0343 | 0.0177 | 0.5155 |
| VpOSCA2.5_VtOSCA2.5 | 0.0589 | 0.0177 | 0.3011 |
| VpOSCA3.1_VtOSCA3.1 | 0.0471 | 0.0234 | 0.4971 |
| VpOSCA3.2_VtOSCA3.2 | 0.0634 | 0.0216 | 0.3403 |
| VpOSCA4.1_VtOSCA4.1 | 0.0775 | 0.0124 | 0.1601 |

## Table S4. Vegetative organ transcript abundance, pairwise DESeq2 differential contrasts, and STRING topological metrics for the *Vellozia* OSCA family

Normalized transcript abundance values (mean counts) and differential expression statistics across leaf, stem, and root tissues were modeled in `DESeq2` for adult field individuals ($n = 3$ biological replicates per species; 9 libraries for *V. peripherica* and 8 for *V. tubiflora*, following the exclusion of library VT1R). Statistical modeling incorporated biological individual as a blocking factor (`~ Individual + Tissue`), evaluating pairwise Wald test contrasts with false discovery rates adjusted via the Benjamini-Hochberg procedure ($p_{\text{adj}}$). Transcript abundances reflect baseline, non-stressed hydrated field conditions. Network topological metrics, including node degree and unweighted local clustering coefficients, were calculated in `NetworkX` from predicted functional-association networks retrieved from STRING (medium confidence threshold, combined score $\ge 0.400$, up to 50 added interactors). Query loci returning no edges at the adopted threshold are indicated with degree 0.

| Gene | Returned in network | Degree | Clustering | Leaf mean | Stem mean | Root mean | Root vs leaf log2FC | Root vs leaf padj | Root vs stem log2FC | Root vs stem padj | Stem vs leaf log2FC | Stem vs leaf padj |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VpOSCA1.1 | True | 11 | 0.436364 | 782.493 | 215.606 | 283.503 | -1.39775 | 0.0252138 | 0.385571 | 1 | -1.78332 | 0.00301629 |
| VpOSCA1.2 | True | 18 | 0.575163 | 0.865729 | 31.2788 | 18.7347 | 4.35684 | 0.0115214 | -0.94365 | 1 | 5.30049 | 0.00141018 |
| VpOSCA1.3 | True | 1 | 0 | 102.105 | 266.265 | 282.887 | 1.37418 | 0.0928902 | 0.0639585 | 1 | 1.31022 | 0.11503 |
| VpOSCA1.4 | True | 1 | 0 | 9.6305 | 10.6598 | 9.68648 | 0.519403 | 0.817586 | 0.706704 | 1 | -0.187301 | 0.941141 |
| VpOSCA1.5 | True | 1 | 0 | 22.1649 | 0.26282 | 12.6331 | -1.03394 | 0.740306 | 2.57367 | 1 | -3.60762 | 0.18595 |
| VpOSCA2.1 | False | 0 | 0 | 135.416 | 93.1436 | 123.917 | -0.158416 | 0.823551 | 0.319853 | 1 | -0.47827 | 0.451303 |
| VpOSCA2.2 | False | 0 | 0 | 525.562 | 352.933 | 394.074 | -0.451889 | 0.440597 | 0.144816 | 1 | -0.596705 | 0.293544 |
| VpOSCA2.3 | False | 0 | 0 | 0.739602 | 15.6739 | 12.2076 | 4.21532 | 0.0401675 | 0.090009 | 1 | 4.12531 | 0.0460652 |
| VpOSCA2.4a | True | 2 | 1 | 280.762 | 543.219 | 399.869 | 0.541817 | 0.429422 | -0.591014 | 1 | 1.13283 | 0.0595769 |
| VpOSCA2.4b | True | 2 | 1 | 576.126 | 695.656 | 711.961 | 0.346628 | 0.566521 | 0.01681 | 1 | 0.329818 | 0.601002 |
| VpOSCA2.5 | True | 4 | 0 | 379.124 | 305.621 | 197.65 | -0.832986 | 0.237169 | -0.580895 | 1 | -0.252091 | 0.774947 |
| VpOSCA3.1 | True | 4 | 0 | 2696.46 | 769.969 | 1007.29 | -1.5623 | 0.00199878 | 0.120329 | 1 | -1.68263 | 0.00075662 |
| VpOSCA3.2 | True | 4 | 0 | 82.9973 | 116.959 | 111.328 | 0.635932 | 0.640002 | -0.304857 | 1 | 0.940789 | 0.477818 |
| VpOSCA4.1 | True | 19 | 0.0409357 | 242.219 | 227.43 | 147.6 | -0.819373 | 0.245954 | -0.763611 | 0.994926 | -0.0557619 | 0.954541 |
| VtOSCA1.1 | True | 13 | 0.5 | 658.212 | 153.82 | 302.037 | -1.17583 | 0.0473601 | 0.888008 | 0.187653 | -2.06383 | 2.69388e-06 |
| VtOSCA1.2 | True | 18 | 0.640523 | 0 | 5.80042 | 67.6767 | 8.26527 | 0.000167521 | 2.89609 | 0.192866 | 5.36918 | 0.0088198 |
| VtOSCA1.3 | True | 3 | 0 | 97.0986 | 226.286 | 410.114 | 2.30381 | 0.0662839 | 1.0189 | 0.517513 | 1.28491 | 0.242416 |
| VtOSCA1.4 | True | 3 | 0 | 3.27811 | 34.3111 | 4.34668 | 2.70776 | 0.275657 | -1.03625 | 0.712201 | 3.74401 | 0.0220064 |
| VtOSCA1.5 | True | 3 | 0 | 8.12599 | 4.02131 | 6.52002 | -0.390364 | 0.911289 | 0.421535 | 0.914285 | -0.811899 | 0.739772 |
| VtOSCA2.1 | False | 0 | 0 | 132.194 | 120.286 | 135.586 | -0.0159172 | 0.985008 | 0.132161 | 0.876313 | -0.148078 | 0.796684 |
| VtOSCA2.2 | False | 0 | 0 | 542.43 | 302.931 | 483.779 | -0.219651 | 0.714538 | 0.56822 | 0.288809 | -0.787871 | 0.0330851 |
| VtOSCA2.3 | False | 0 | 0 | 1.35782 | 1.89484 | 11.3014 | 1.76325 | 0.579418 | 1.8416 | 0.585927 | -0.0783476 | 0.98419 |
| VtOSCA2.4 | True | 5 | 0.1 | 930.427 | 805.862 | 1566.78 | 0.801609 | 0.0255357 | 1.0112 | 0.00622962 | -0.209587 | 0.555531 |
| VtOSCA2.5 | True | 7 | 0.047619 | 380.649 | 126.675 | 249.018 | -0.452692 | 0.411536 | 1.09995 | 0.0289874 | -1.55264 | 1.10012e-05 |
| VtOSCA3.1 | True | 4 | 0 | 3221.71 | 392.071 | 1030.8 | -1.37785 | 0.173284 | 1.53396 | 0.147245 | -2.91181 | 5.31353e-05 |
| VtOSCA3.2 | True | 4 | 0 | 19.3689 | 14.0032 | 138.743 | 4.4166 | 0.0103181 | 3.5682 | 0.0608347 | 0.848401 | 0.648987 |
| VtOSCA4.1 | True | 13 | 0.0384615 | 244.619 | 83.6536 | 322.668 | 0.397784 | 0.608887 | 1.84076 | 0.00338089 | -1.44298 | 0.00340788 |

## Table S5. Gene Ontology and KEGG pathway functional enrichment of predicted OSCA interactomes in *Vellozia peripherica* and *Vellozia tubiflora*

Functional enrichment statistics retrieved from STRING for the reconstructed OSCA functional-association networks of both species. Observed query proteins within each category are compared against the total annotated genome-wide background. Significant enrichment was defined at a Benjamini-Hochberg false discovery rate (FDR) $< 0.05$ in at least one species. Enriched terms are categorized across Gene Ontology (GO) Biological Process, Molecular Function, Cellular Component, and KEGG Metabolic Pathways, highlighting predominant functional associations with carbohydrate catabolism (starch and sucrose metabolism, amylase activities), ion transport, and cellular homeostasis.

| Category | Term ID | Description | *V. peripherica* Genes | *V. peripherica* Background | *V. peripherica* FDR | *V. tubiflora* Genes | *V. tubiflora* Background | *V. tubiflora* FDR |
|---|---|---|---|---|---|---|---|---|
| Biological Process (GO) | GO:0016052 | Carbohydrate catabolic process | 15 | 239 | 3.48e-14 | 16 | 245 | 1.81e-15 |
| Biological Process (GO) | GO:0005975 | Carbohydrate metabolic process | 16 | 1029 | 8.12e-07 | - | - | - |
| Biological Process (GO) | GO:0009056 | Catabolic process | 19 | 1779 | 3.76e-06 | 19 | 1619 | 1.20e-06 |
| Biological Process (GO) | GO:0008219 | Cell death | 4 | 88 | 8.10e-03 | - | - | - |
| Biological Process (GO) | GO:0044275 | Cellular carbohydrate catabolic process | 7 | 65 | 3.31e-07 | 7 | 62 | 2.20e-07 |
| Biological Process (GO) | GO:0044262 | Cellular carbohydrate metabolic process | 8 | 448 | 1.40e-03 | - | - | - |
| Biological Process (GO) | GO:0044248 | Cellular catabolic process | 11 | 1300 | 1.92e-02 | 10 | 1142 | 3.82e-02 |
| Biological Process (GO) | GO:0006073 | Cellular glucan metabolic process | 6 | 184 | 8.50e-04 | 6 | 181 | 1.00e-03 |
| Biological Process (GO) | GO:0044247 | Cellular polysaccharide catabolic process | 6 | 39 | 7.40e-07 | 6 | 37 | 5.13e-07 |
| Biological Process (GO) | GO:0009987 | Cellular process | 50 | 15523 | 1.18e-02 | - | - | - |
| Biological Process (GO) | GO:0051085 | Chaperone cofactor-dependent protein refolding | 3 | 53 | 2.97e-02 | - | - | - |
| Biological Process (GO) | GO:0046352 | Disaccharide catabolic process | 4 | 15 | 2.70e-05 | 4 | 15 | 2.89e-05 |
| Biological Process (GO) | GO:0009251 | Glucan catabolic process | 6 | 44 | 1.02e-06 | 6 | 41 | 6.02e-07 |
| Biological Process (GO) | GO:0005980 | Glycogen catabolic process | 2 | 2 | 4.40e-03 | 2 | 2 | 5.10e-03 |
| Biological Process (GO) | GO:0005977 | Glycogen metabolic process | 3 | 10 | 6.30e-04 | 3 | 10 | 8.10e-04 |
| Biological Process (GO) | GO:0006559 | L-phenylalanine catabolic process | 2 | 13 | 4.83e-02 | - | - | - |
| Biological Process (GO) | GO:0051179 | Localization | - | - | - | 19 | 3175 | 1.11e-02 |
| Biological Process (GO) | GO:0009057 | Macromolecule catabolic process | 15 | 911 | 1.04e-06 | 16 | 810 | 4.98e-08 |
| Biological Process (GO) | GO:0034051 | Negative regulation of plant-type hypersensitive response | 2 | 6 | 1.74e-02 | 2 | 7 | 2.39e-02 |
| Biological Process (GO) | GO:1901575 | Organic substance catabolic process | 18 | 1566 | 3.64e-06 | 18 | 1432 | 1.20e-06 |
| Biological Process (GO) | GO:0000272 | Polysaccharide catabolic process | 14 | 137 | 1.54e-15 | 15 | 132 | 2.10e-17 |
| Biological Process (GO) | GO:0042026 | Protein refolding | 3 | 41 | 1.74e-02 | - | - | - |
| Biological Process (GO) | GO:0005983 | Starch catabolic process | 4 | 13 | 1.78e-05 | 4 | 13 | 1.91e-05 |
| Biological Process (GO) | GO:0005987 | Sucrose catabolic process | 3 | 11 | 7.30e-04 | 3 | 11 | 9.20e-04 |
| Biological Process (GO) | GO:0006810 | Transport | 22 | 2899 | 5.54e-05 | 18 | 3001 | 1.67e-02 |
| Biological Process (GO) | GO:0006572 | Tyrosine catabolic process | 2 | 9 | 2.92e-02 | - | - | - |
| Biological Process (GO) | GO:1990961 | Xenobiotic detoxification by transmembrane export across the plasma membrane | 3 | 41 | 1.74e-02 | - | - | - |
| Molecular Function (GO) | GO:0004556 | Alpha-amylase activity | 3 | 5 | 6.93e-05 | 3 | 4 | 5.09e-05 |
| Molecular Function (GO) | GO:0016160 | Amylase activity | 9 | 13 | 3.22e-16 | 9 | 13 | 3.74e-16 |
| Molecular Function (GO) | GO:0102229 | Amylopectin maltohydrolase activity | 7 | 7 | 4.14e-13 | 8 | 8 | 3.61e-15 |
| Molecular Function (GO) | GO:0016161 | Beta-amylase activity | 6 | 8 | 9.95e-11 | 6 | 9 | 2.14e-10 |
| Molecular Function (GO) | GO:0005227 | Calcium activated cation channel activity | 11 | 15 | 5.64e-20 | 10 | 14 | 8.80e-18 |
| Molecular Function (GO) | GO:0008324 | Cation transmembrane transporter activity | - | - | - | 12 | 453 | 1.11e-07 |
| Molecular Function (GO) | GO:0008184 | Glycogen phosphorylase activity | 2 | 2 | 3.00e-03 | 2 | 2 | 3.00e-03 |
| Molecular Function (GO) | GO:0031072 | Heat shock protein binding | 3 | 68 | 4.66e-02 | - | - | - |
| Molecular Function (GO) | GO:0016787 | Hydrolase activity | 20 | 3299 | 3.00e-03 | 20 | 3013 | 1.00e-03 |
| Molecular Function (GO) | GO:0004553 | Hydrolase activity, hydrolyzing O-glycosyl compounds | 12 | 367 | 1.05e-08 | 13 | 353 | 6.88e-10 |
| Molecular Function (GO) | GO:0022890 | Inorganic cation transmembrane transporter activity | - | - | - | 11 | 415 | 5.69e-07 |
| Molecular Function (GO) | GO:0102250 | Linear malto-oligosaccharide phosphorylase activity | 2 | 2 | 3.00e-03 | 2 | 2 | 3.00e-03 |
| Molecular Function (GO) | GO:0008381 | Mechanosensitive ion channel activity | 3 | 13 | 6.50e-04 | 3 | 11 | 4.90e-04 |
| Molecular Function (GO) | GO:0102499 | SHG alpha-glucan phosphorylase activity | 2 | 2 | 3.00e-03 | 2 | 2 | 3.00e-03 |
| Molecular Function (GO) | GO:0022857 | Transmembrane transporter activity | 18 | 1496 | 6.84e-07 | 15 | 1642 | 4.90e-04 |
| Cellular Component (GO) | GO:0098588 | Bounding membrane of organelle | 9 | 970 | 2.35e-02 | - | - | - |
| Cellular Component (GO) | GO:0110165 | Cellular anatomical entity | 61 | 22201 | 7.60e-03 | 60 | 21115 | 8.80e-03 |
| Cellular Component (GO) | GO:0009507 | Chloroplast | 17 | 2378 | 7.60e-03 | - | - | - |
| Cellular Component (GO) | GO:0000793 | Condensed chromosome | - | - | - | 3 | 54 | 2.41e-02 |
| Cellular Component (GO) | GO:0000796 | Condensin complex | 2 | 7 | 1.25e-02 | 2 | 6 | 1.21e-02 |
| Cellular Component (GO) | GO:0005737 | Cytoplasm | 45 | 11248 | 6.10e-04 | 42 | 11428 | 8.80e-03 |
| Cellular Component (GO) | GO:0005886 | Plasma membrane | 17 | 2512 | 7.60e-03 | 16 | 2155 | 8.80e-03 |
| Cellular Component (GO) | GO:0009506 | Plasmodesma | 7 | 363 | 7.60e-03 | 7 | 343 | 8.80e-03 |
| Cellular Component (GO) | GO:0009536 | Plastid | 18 | 2652 | 7.60e-03 | - | - | - |
| KEGG Pathway | map01110 | Biosynthesis of secondary metabolites | 29 | 2417 | 7.10e-13 | 31 | 2196 | 7.61e-16 |
| KEGG Pathway | map01100 | Metabolic pathways | 30 | 5617 | 6.49e-05 | 32 | 5722 | 9.53e-06 |
| KEGG Pathway | map00500 | Starch and sucrose metabolism | 22 | 255 | 2.60e-26 | 23 | 248 | 3.57e-28 |
| KEGG Pathway | map00350 | Tyrosine metabolism | 3 | 66 | 2.07e-02 | - | - | - |

## Table S6. Functional classification, consensus sequences, and responsive annotations of curated *cis*-regulatory elements in OSCA promoters

Systematic classification framework for *cis*-acting elements adapted from Qu et al. (2019) and PlantCARE standards. The table details each curated motif identifier, its consensus or representative sequence motif, its established functional response category (Phytohormone Signaling, Abiotic Stress Response, Growth & Development, Light Responsiveness, and Core Promoter Elements), its predicted biological responsiveness (e.g., ABA responsiveness, drought inducibility, low-temperature induction, or bHLH/MYB binding), and primary literature citations validating the motif model.

| Functional Category | Motif Name | Consensus / Representative Sequence | Predicted Biological Function / Responsiveness | References |
|---|---|---|---|---|
| Phytohormone Signaling | ABRE | ACGTG / TACGTG / CCGTG | Abscisic acid (ABA) responsiveness; dehydration and osmotic stress | Lescot et al. (2002); Qu et al. (2019) |
| Phytohormone Signaling | CGTCA-motif | CGTCA | Methyl jasmonate (MeJA) responsiveness | Lescot et al. (2002) |
| Phytohormone Signaling | TGACG-motif | TGACG | Methyl jasmonate (MeJA) responsiveness | Lescot et al. (2002) |
| Phytohormone Signaling | TCA-element | CCATCTTTTT / CAGAAAAGGA | Salicylic acid (SA) responsiveness; defense and stress signaling | Lescot et al. (2002) |
| Abiotic Stress Response | MBS | TAACTG / CAACTG | MYB binding site involved in drought inducibility and osmotic regulation | Lescot et al. (2002) |
| Abiotic Stress Response | LTR | CCGAAA | Low-temperature and cold responsiveness | Lescot et al. (2002) |
| Abiotic Stress Response | ARE | TGGTTT / AAACCA | Anaerobic induction essential for hypoxia-induced expression | Lescot et al. (2002) |
| Abiotic Stress Response | TC-rich repeats | ATTTTCTTCA / GTTTTCTTAC | Defense and stress responsiveness | Lescot et al. (2002) |
| Abiotic Stress Response | W box | TTGACC | WRKY transcription factor binding site; pathogen defense and wounding | Lescot et al. (2002) |
| Growth & Development | MYC | CANNTG (e.g., CACATG, CATGTG) | bHLH transcription factor binding site; drought, ABA, and cold response | Lescot et al. (2002) |
| Growth & Development | MYB | CAACCA / WAACCA / YAACKG | MYB transcription factor binding site; development and stress response | Lescot et al. (2002) |
| Growth & Development | RY-element | CATGCA | Seed-specific and embryo-development regulation | Lescot et al. (2002) |
| Light Responsiveness | G-box | CACGTG / CACGTC | Light responsiveness and multi-factor stress signaling hub | Lescot et al. (2002) |
| Light Responsiveness | Box 4 | ATTAAT | Conserved DNA module involved in light responsiveness | Lescot et al. (2002) |
| Light Responsiveness | GT1-motif | GGTTAA | Light-responsive element; GT-1 factor binding | Lescot et al. (2002) |
| Core Promoter Elements | TATA-box | TATA(A/T)A(A/T) | Core promoter element initiating transcription | Lescot et al. (2002) |
| Core Promoter Elements | CAAT-box | CAAT / CAAAT / CCAAT | Common cis-acting element in promoter and enhancer regions | Lescot et al. (2002) |

## Table S7. Curated non-redundant *cis*-acting regulatory element occurrence counts across 2.0-kb upstream promoters of *Vellozia* OSCA genes

Putative regulatory motifs were identified by scanning 2,000-bp promoter sequences immediately upstream of annotated transcription start sites using the `PlantCARE` database. Raw database hits were processed through a custom curation pipeline to resolve orthographic redundancies (standardizing case variants such as `G-box`/`G-Box`, `MYC`/`Myc`, and `MYB`/`Myb`) and to merge overlapping coordinate intervals of identical motif classes on the same promoter into single non-redundant regulatory sites (`start <= previous_end`), preventing artificial count inflation caused by palindromic hits or nested matches. Motif profiles are reported for major functional categories, including core promoter elements, light-responsive modules, development-associated transcription factor binding sites, phytohormone-responsive elements (abscisic acid, jasmonate, salicylic acid), and abiotic stress-responsive elements (drought, low temperature, hypoxia, defense/wounding). Computational motif occurrences represent exploratory sequence annotations and do not demonstrate *in vivo* transcription factor binding or transcriptional activation.

| Species | Gene | ABRE | CGTCA-motif | TGACG-motif | TCA-element | MBS | LTR | ARE | TC-rich repeats | W box | G-box | Box 4 | GT1-motif | MYC | MYB | RY-element | TATA-box | CAAT-box |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vper | VpOSCA1.1 | 2 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 9 | 1 | 3 | 3 | 0 | 18 | 32 |
| Vper | VpOSCA1.2 | 1 | 1 | 1 | 0 | 1 | 4 | 2 | 0 | 0 | 3 | 2 | 1 | 3 | 3 | 0 | 14 | 28 |
| Vper | VpOSCA1.3 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 3 | 1 | 1 | 1 | 0 | 17 | 28 |
| Vper | VpOSCA1.4 | 1 | 0 | 0 | 1 | 2 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 5 | 0 | 31 | 32 |
| Vper | VpOSCA1.5 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 3 | 2 | 0 | 19 | 24 |
| Vper | VpOSCA2.1 | 6 | 1 | 1 | 0 | 2 | 0 | 0 | 1 | 0 | 6 | 4 | 1 | 4 | 8 | 0 | 22 | 24 |
| Vper | VpOSCA2.2 | 2 | 0 | 0 | 1 | 1 | 1 | 3 | 0 | 0 | 3 | 3 | 0 | 8 | 9 | 1 | 17 | 33 |
| Vper | VpOSCA2.3 | 1 | 2 | 2 | 0 | 0 | 0 | 1 | 1 | 1 | 3 | 10 | 0 | 1 | 2 | 0 | 42 | 28 |
| Vper | VpOSCA2.4a | 2 | 2 | 2 | 0 | 1 | 2 | 4 | 0 | 1 | 2 | 2 | 0 | 4 | 3 | 0 | 18 | 34 |
| Vper | VpOSCA2.4b | 4 | 2 | 2 | 0 | 0 | 1 | 1 | 0 | 3 | 4 | 5 | 0 | 4 | 2 | 0 | 26 | 30 |
| Vper | VpOSCA2.5 | 2 | 4 | 4 | 1 | 1 | 6 | 1 | 0 | 1 | 2 | 4 | 2 | 6 | 4 | 0 | 26 | 30 |
| Vper | VpOSCA3.1 | 3 | 2 | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 3 | 1 | 1 | 2 | 7 | 0 | 20 | 29 |
| Vper | VpOSCA3.2 | 6 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 2 | 7 | 2 | 0 | 1 | 4 | 0 | 13 | 29 |
| Vper | VpOSCA4.1 | 2 | 1 | 1 | 0 | 2 | 1 | 3 | 1 | 0 | 2 | 3 | 1 | 10 | 5 | 0 | 19 | 35 |
| Vtub | VtOSCA1.1 | 5 | 2 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 5 | 9 | 0 | 7 | 2 | 0 | 31 | 35 |
| Vtub | VtOSCA1.2 | 0 | 0 | 0 | 2 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 3 | 5 | 5 | 0 | 13 | 33 |
| Vtub | VtOSCA1.3 | 3 | 3 | 3 | 0 | 1 | 0 | 1 | 0 | 0 | 3 | 1 | 1 | 3 | 3 | 0 | 26 | 32 |
| Vtub | VtOSCA1.4 | 3 | 2 | 2 | 0 | 1 | 1 | 1 | 1 | 1 | 2 | 0 | 1 | 0 | 4 | 0 | 26 | 20 |
| Vtub | VtOSCA1.5 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 6 | 1 | 1 | 2 | 0 | 28 | 30 |
| Vtub | VtOSCA2.1 | 7 | 3 | 3 | 0 | 2 | 1 | 2 | 1 | 1 | 10 | 5 | 4 | 0 | 5 | 0 | 23 | 30 |
| Vtub | VtOSCA2.2 | 3 | 4 | 4 | 0 | 0 | 3 | 1 | 0 | 1 | 3 | 1 | 0 | 6 | 2 | 0 | 20 | 24 |
| Vtub | VtOSCA2.3 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 3 | 0 | 1 | 6 | 0 | 20 | 26 |
| Vtub | VtOSCA2.4 | 6 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 1 | 6 | 3 | 0 | 2 | 4 | 0 | 27 | 25 |
| Vtub | VtOSCA2.5 | 3 | 1 | 1 | 1 | 1 | 2 | 0 | 1 | 0 | 4 | 4 | 1 | 9 | 6 | 0 | 30 | 25 |
| Vtub | VtOSCA3.1 | 2 | 1 | 1 | 0 | 1 | 1 | 5 | 0 | 0 | 2 | 1 | 0 | 2 | 5 | 0 | 12 | 37 |
| Vtub | VtOSCA3.2 | 2 | 2 | 2 | 1 | 1 | 2 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 4 | 0 | 15 | 30 |
| Vtub | VtOSCA4.1 | 0 | 1 | 1 | 1 | 2 | 1 | 3 | 1 | 1 | 0 | 1 | 2 | 6 | 4 | 0 | 11 | 33 |
