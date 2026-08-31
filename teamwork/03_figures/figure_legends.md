# Scientific Figure Legends: Chapter 1

**Manuscript Title:** Large-Scale Comparative Genomics of *Vellozia tubiflora* and *Vellozia peripherica*  
**Candidate:** Mariana Feitosa Cavalheiro  
**Advisor:** Isabel Rodrigues Gerhardt  
**Institution:** Universidade Estadual de Campinas (UNICAMP)  

---

### Figure 1. Pairwise assembly quality, chromosomal macrosynteny, and karyotypic stasis between *Vellozia tubiflora* and *Vellozia peripherica*.
**(A)** High-resolution pairwise chromosomal dotplot between *Vellozia tubiflora* (X-axis, Chr1A–Chr9A, cumulative Mb) and *Vellozia peripherica* (Y-axis, Chr1A–Chr9A, cumulative Mb). Blue dots depict 1:1 collinear syntenic anchors extracted from MCScanX/JCVI alignments. Purple off-diagonal dots highlight the ancestral whole-genome paleoduplication block between Chromosome 1A and Chromosome 5A ($2n = 18, x = 9$; BRAZ et al., 2025). Alternating grey shaded regions delineate individual chromosome boundaries.  
**(B)** Whole-genome dual-track macrosynteny ribbon map across all 9 homologous chromosome pairs (Chr1A–Chr9A) between *V. tubiflora* (top, amber) and *V. peripherica* (bottom, green). Colored Bezier ribbons represent 297 high-confidence 1:1 collinear synteny blocks, demonstrating complete macrosyntenic stasis with zero inter-chromosomal translocations.  
**(C)** Pairwise evaluation of nuclear genome assembly completeness and contiguity. Stacked horizontal bars show Benchmarking Universal Single-Copy Orthologs (BUSCO v5.4.3, Embryophyta ODB10) for *V. tubiflora* ($>95.2\%$) and *V. peripherica* ($>95.6\%$), partitioned into complete single-copy (blue), complete duplicated (sky blue), fragmented (orange), and missing (rust) fractions. The inset box summarizes chromosomal scaffolding stats ($>97.8\%$ anchored to 9 pseudomolecules).

---

### Figure 2. Orthology landscape, core proteome partitions, and chromosomal gene distributions.
**(A)** Proteome overlap and orthology partition matrix between *Vellozia tubiflora* and *Vellozia peripherica*. Bars delineate the shared Velloziaceae core proteome (18,690 orthologous genes/pairs, including 7,061 universal single-copy 1:1:1 orthologs), species-specific family expansions (2,019 genes in *Vtub* vs. 3,526 genes in *Vper*), and unassigned species-specific singletons.  
**(B)** Violin and box plot distributions of orthogroup cluster sizes (genes per orthogroup, $\log_{10}$ scale) for *V. tubiflora* (amber) and *V. peripherica* (green), illustrating comparable median cluster compactness and multi-copy duplicate retention.  
**(C)** Chromosomal gene distribution and 1:1 ortholog density across the 9 homologous pseudomolecules (Chr1A–Chr9A) in *V. tubiflora* (amber) and *V. peripherica* (green), with solid darker overlays indicating the number of 1:1 single-copy orthologs per chromosome.

---

### Figure 3. Macroevolutionary gene family dynamics (CAFE5) and statistical functional enrichment.
**(A)** Calibrated phylogenetic tree displaying branch-specific gene family expansion ($+$) and contraction ($-$) node badges modeled via CAFE5 ($\lambda = 0.07456$ gains/losses per gene per million years, 412 statistically significant families at $p \le 0.05$). Nodes reflect divergence times calibrated from Cretaceous radiation (~145 Mya) to the Neogene *Vellozia* radiation (~25 Mya).  
**(B)** Functional overrepresentation bubble plot of expanding gene families evaluated via two-sided Fisher's exact tests against the whole-genome background. The $x$-axis indicates Fold Enrichment ($\ge 2.0\times$) and the $y$-axis shows statistical significance ($-\log_{10}[\text{FDR } q\text{-value}]$). Bubble size is proportional to the number of expanding genes per term. Amber bubbles represent *V. tubiflora* adaptations (TOC/TIC translocons, NDH electron transport, PSII reaction center, ACC lipid repair, plastid ribosome biogenesis); green bubbles represent *V. peripherica* adaptations (LRR receptor kinases, U-box E3 ubiquitin ligases, UDP-glycosyltransferases, Cytochrome P450s, NB-ARC disease sentinels).  
**(C)** Comparative gene copy-number trajectories across the ancestral node, *V. tubiflora*, and *V. peripherica* for the top 10 diagnostic adaptive gene families, with exact copy-number net changes ($\Delta$) indicated next to each bar.

---

### Figure 4. Codon selection regimes ($Ka/Ks$) and pathway-specific evolutionary constraints.
**(A)** Raincloud distribution plot combining a probability density histogram, kernel density estimate (KDE), and raw data jitter strip of pairwise non-synonymous to synonymous substitution rates ($\omega = Ka/Ks$) across 7,061 single-copy orthologs between *V. tubiflora* and *V. peripherica*. The dashed orange line marks the genome-wide mean selection ratio ($\omega = 0.3542$), and the dotted grey line indicates neutral evolution ($\omega = 1.0$).  
**(B)** Scatter plot of non-synonymous substitution rate ($Ka$) versus synonymous substitution rate ($Ks$) across single-copy orthologs. Reference isoclines indicate neutral evolution ($\omega = 1.0$, grey), moderate purifying selection ($\omega = 0.5$, orange), and extreme evolutionary constraint ($\omega = 0.1$, green).  
**(C)** Mean selective constraint ($\text{Mean } \omega \pm \text{SD}$) ranked across representative biological and functional categories. Each category aggregates multiple distinct 1:1:1 single-copy orthogroups sharing the same functional domain (e.g., 204 distinct 1:1 LRR receptor kinase orthogroups, 87 distinct 1:1 ABC transporter orthogroups, 23 distinct 1:1 TOC/TIC translocon subunit orthogroups, 101 distinct 1:1 ribosomal protein orthogroups, 24 distinct 1:1 histone orthogroups). Housekeeping cellular machinery undergoes severe purifying selection ($\omega < 0.20$), whereas membrane-bound environmental perception and transport systems exhibit elevated rates ($0.50 < \omega < 0.70$) reflecting relaxed constraint and adaptive divergence.
