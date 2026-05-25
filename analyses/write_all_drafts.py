import os
import docx

docs_dir = "/home/mfcaval/github/doutorado/docs"
os.makedirs(docs_dir, exist_ok=True)

drafts = {}

# ==========================================
# 01. GENE IDENTIFICATION DRAFT
# ==========================================
drafts["01_gene_identification"] = """# RESULTS: Genome-wide Identification and Characterization of the OSCA Gene Family

To establish a comprehensive catalog of the Hyperosmolality-Gated Calcium-Permeable Channel (OSCA) gene family in *Vellozia*, we performed a genome-wide survey using the chromosome-level genome assemblies (hapA haplotype) of *Vellozia peripherica* (Vper) and *Vellozia tubiflora* (Vtub), which both possess nine chromosomes. Using the conserved Pfam accession profiles PF02714 (RSN1_7TM), PF13967 (RSN1 TM), and PF14703 (PHM7 cyt) as search models via HMMER, followed by structural domain validation through the InterProScan database, we identified a total of 27 non-redundant OSCA genes across the two species.

Specifically:
- *Vellozia peripherica* (evergreen) harbors **14 OSCA genes** encoding 14 unique transcripts.
- *Vellozia tubiflora* (resurrection) harbors **13 OSCA genes** encoding 13 unique transcripts.

The identified genes were mapped across the nine chromosomes of both genomes, revealing a widely conserved distribution. The numerical complement of OSCA genes in both *Vellozia* genomes is highly comparable to that found in the model dicot *Arabidopsis thaliana* (15 genes) and slightly larger than the monocot lineages *Oryza sativa* (11 genes) and *Zea mays* (12 genes). 

This numerical stability is particularly significant given the documented whole-genome duplication (WGD) history of the Velloziaceae family, indicating that the OSCA family has remained remarkably stable and resistant to global gene loss or major expansions following speciation. Notably, the extreme desiccation-tolerance strategy of *V. tubiflora* did not result in a reduction of its osmosensory machinery, as the resurrection plant maintains a virtually identical complement of primary calcium-permeable channels compared to the evergreen *V. peripherica*.
"""

# ==========================================
# 02. PHYLOGENY DRAFT
# ==========================================
drafts["02_phylogeny"] = """# RESULTS: Phylogenetic Reconstruction and Subfamily Classification

To resolve the evolutionary relationships of the *Vellozia* OSCA genes and classify them within the established angiosperm subfamilies, we performed a Maximum Likelihood (ML) phylogenetic reconstruction. The analysis integrated full-length amino acid sequences of OSCA proteins from *V. peripherica* (14), *V. tubiflora* (13), *Arabidopsis thaliana* (15), *Oryza sativa* (11), *Sorghum bicolor* (11), and *Zea mays* (12). Sequence alignment was executed using MAFFT, and the ML tree was constructed using IQ-TREE with 1,000 bootstrap replicates (Fig. 1).

The phylogenetic tree confirmed the robust classification of all identified *Vellozia* OSCA proteins into the four established monophyletic clades conservedly shared across angiosperms:
1.  **OSCA1 Subfamily**: Encompasses 5 genes in Vper (`VpOSCA1.1` to `VpOSCA1.5`) and 5 genes in Vtub (`VtOSCA1.1` to `VtOSCA1.5`).
2.  **OSCA2 Subfamily**: Represents the most diverse and expanded clade in both species, harboring 6 genes in Vper (`VpOSCA2.1` to `VpOSCA2.5`, including two copies of OSCA2.4) and 5 genes in Vtub (`VtOSCA2.1` to `VtOSCA2.5`).
3.  **OSCA3 Subfamily**: Contains 2 genes in Vper (`VpOSCA3.1` and `VpOSCA3.2`) and 2 genes in Vtub (`VtOSCA3.1` and `VtOSCA3.2`).
4.  **OSCA4 Subfamily**: Possesses 1 gene in Vper (`VpOSCA4.1`) and 1 gene in Vtub (`VtOSCA4.1`).

Orthology relationships between *V. peripherica* and *V. tubiflora* were virtually perfect (1:1 orthologous pairs) across almost all loci, demonstrating that the baseline phylogenetic architecture of the osmosensory apparatus was strictly preserved after their speciation. 

A critical lineage-specific exception was detected in the OSCA2 clade: *V. peripherica* possesses a tandem duplication resulting in two adjacent paralogs, `VpOSCA2.4a` and `VpOSCA2.4b`, whereas *V. tubiflora* retains only a single copy (`VtOSCA2.4`). This localized expansion in the evergreen species represents a key evolutionary divergence, suggesting active structural remodeling of Clade 2 channels to support continuous daily and seasonal osmotic monitoring.
"""

# ==========================================
# 03. SYNTENY DRAFT
# ==========================================
drafts["03_synteny"] = """# RESULTS: Comparative Synteny and Chromosomal Collinearity

To investigate the structural conservation of the chromosomal regions harboring the OSCA genes and characterize the duplication events that shaped the family's architecture, we performed a comparative synteny analysis between *V. peripherica* and *V. tubiflora* using MCScan/JCVI.

#### Global Collinearity and Macrosynteny
Global comparative profiling revealed an extraordinary level of macro-collinearity between the two genomes, with 297 syntenic blocks successfully mapped across their 9 chromosomes. No major inter-chromosomal translocations or large-scale rearrangements were detected, confirming that the spatial architecture of their genomes has remained remarkably stable since their evolutionary divergence.

#### Microsynteny of the OSCA1.3/1.4/1.5 Tandem Cluster
At the microsynteny level, we identified a perfectly conserved physical cluster on Chromosome 7A in both genomes. This cluster contains a physically contiguous tandem duplication of three genes: `OSCA1.3`, `OSCA1.4`, and `OSCA1.5`, displaying a physical gap of zero intermediate genes in both species. The local region is flanked by 24 highly syntenic, orthologous gene pairs, displaying absolute micro-collinearity (Fig. 2). The perfect preservation of this contiguous layout suggests that the tandem expansion of these Clade 1 channels occurred prior to the speciation event and has been strictly maintained, likely due to a non-negotiable functional requirement for coordinated transcription or gene conversion.

#### Ancestral Paleoduplication and Lineage-Specific Tandem Duplication
Self-synteny analysis revealed two major duplication events that contributed to the expansion of the OSCA family in *Vellozia*:
1.  **Ancestral Segmental Duplication (Chr1A ↔ Chr5A)**: A highly conserved ancestral duplication block was identified linking Chromosome 1A and Chromosome 5A in both species. This block simultaneously harbors duplicated members of the OSCA2 subfamily (OSCA2.1/2.2) and the OSCA3 subfamily (OSCA3.1/3.2). This ancestral segment confirms that these clades were expanded through a shared ancient whole-genome duplication (WGD) event.
2.  **Lineage-Specific Tandem Duplication on Chr1A**: A recent tandem duplication of the OSCA2.4 locus was identified exclusively on Chromosome 1A of *V. peripherica*, yielding two adjacent genes (`VpOSCA2.4a` and `VpOSCA2.4b`) with zero intermediate genes. In contrast, *V. tubiflora* retains a single ancestral copy (`VtOSCA2.4`). This recent expansion represents a targeted diversification event in the evergreen species.
"""

# ==========================================
# 04. EVOLUTIONARY RATES DRAFT
# ==========================================
drafts["04_evolutionary_rates"] = """# RESULTS: Molecular Evolutionary Rates and Clade-Specific Selection Pressures

To determine the selective forces driving the evolution of the OSCA family and to evaluate whether the contrasting drought strategies of the two species have altered these evolutionary pressures, we estimated nonsynonymous-to-synonymous substitution rates (Ka/Ks) and implemented clade-specific selection tests.

#### Pairwise Ka/Ks and Purifying Selection
Pairwise Ka/Ks calculations for 14 orthologous pairs revealed that all OSCA loci are evolving under strong purifying selection (Ka/Ks < 1.0, with a family-wide mean of ~0.35). The lowest evolutionary rate was observed in the `VpOSCA2.3_VtOSCA2.3` pair (Ka/Ks = 0.053), indicating an extremely severe functional constraint preserving this channel's primary structure. Loci such as OSCA1.1 and OSCA3.1 also showed robust purifying signatures (Ka/Ks = 0.33 and 0.34). In contrast, the `VpOSCA1.4_VtOSCA1.4` pair showed a highly accelerated evolutionary rate (Ka/Ks = 0.80), suggesting evolutionary relaxation or localized diversification after speciation.

#### Subfamily-Specific Selection Intensity (HyPhy RELAX)
To dissect if selective pressures differ between the evergreen strategy (Vper) and the desiccation-tolerance strategy (Vtub), we implemented a clade-specific evolutionary pipeline using HyPhy RELAX. The analysis revealed a striking, subfamily-dependent **"Dual-Track" evolutionary model**:
1.  **The Conserved Track (OSCA1 Clade)**: The OSCA1 subfamily showed no significant change in selection intensity between the two species (selection intensity parameter K = 0.92, p = 0.60), confirming that these baseline osmosensors are under identical and stringent purifying constraints in both lifestyles.
2.  **The Divergent Track (OSCA2 and OSCA3+4 Clades)**: In striking contrast, the OSCA2 subfamily showed a highly significant, massive selection relaxation in Vtub (K = 0.28, p = 3.4 x 10^{-5}). Similarly, the OSCA3+4 subfamily displayed highly significant relaxation in the resurrection species (K = 0.13, p = 0.006).

*Interpretation:* During severe drought, *V. tubiflora* enters a metabolically inactive state of anhydrobiosis, during which its osmosensors cease to operate, suspending active selective pressure. This allows the modulatory OSCA2 and OSCA3+4 subfamilies to experience neutral drift, while core baseline sensors (OSCA1) remain strictly protected.

#### Site-Specific Divergence (Contrast-FEL)
Using HyPhy Contrast-FEL, we mapped individual sites evolving at different rates between the two species:
- In the OSCA1 clade, 6 significant sites were identified, displaying a balanced distribution of localized adjustments.
- In the OSCA2 clade, 14 significant sites were detected, and remarkably, **all 14 sites showed selective acceleration exclusively in Vper** (beta_Ref >> 0, beta_Test approx 0). This confirms that *V. peripherica* is actively remodeling its OSCA2 modulators, likely to support active, continuous daily osmotic monitoring.
- In the OSCA3+4 clade, a highly significant selection relaxation hotspot was revealed at local position 593 in *V. tubiflora* (beta_Test = 24.72, beta_Ref = 0.018, p = 0.009).
"""

# ==========================================
# 05 & 06. EXPRESSION DRAFT
# ==========================================
drafts["05_06_expression"] = """# RESULTS: Tissue-Specific Expression Profiles and Differential Regulation

To characterize the spatial deployment of the *Vellozia* osmosensory apparatus and assess its functional specialization, we analyzed RNA-seq data from three primary tissues (leaf, stem, and root) in both species. Differential expression analysis was performed using DESeq2 with a paired experimental design (formula: ~ Individual + Tissue) to control for inter-individual variability.

The analysis revealed a striking pattern of functional specialization and evolutionary conservation in tissue-specific expression within the OSCA family across both species:

#### The Subterranean and Vascular Sensor: OSCA1.2
In both genomes, **OSCA1.2** exhibited a dramatic and highly conserved enrichment in root and stem tissues compared to leaves. In *V. peripherica*, `VpOSCA1.2` accumulated preferentially in roots and stems (Log2FC = 4.40, padj < 0.05), while in *V. tubiflora*, `VtOSCA1.2` showed an even more pronounced subterranean/vascular accumulation (Log2FC = 8.64, padj < 0.05). This robust conservation suggests that OSCA1.2 plays an essential, ancestral role in vascular osmosensation and subterranean turgor monitoring.

#### The Foliar and Stomatal Modulators: OSCA1.1 and OSCA3.1
In contrast, **OSCA1.1** and **OSCA3.1** displayed a robust and consistent leaf-enriched expression profile in both genomes. For instance, `VtOSCA1.1` was significantly enriched in leaf tissue relative to stem (Log2FC = -2.07, padj = 1.2 x 10^{-6}), and `VpOSCA1.1` showed an equivalent leaf-preferred profile. This aerial functional specialization indicates their direct involvement in stomatal signaling and leaf turgor regulation under changing water availability.

These highly conserved, tissue-specific expression patterns demonstrate that the spatial deployment of the osmosensory apparatus has been strictly preserved after speciation. Both species position the exact same primary sensors in the exact same tissues—OSCA1.2 vascularly and OSCA1.1/OSCA3.1 foliarly—suggesting that the physiological divergence between their evergreen and resurrection strategies does not reside in where they detect osmotic changes, but rather in the structural tuning of the modulatory sensors themselves.
"""

# ==========================================
# 07. PPI NETWORK DRAFT
# ==========================================
drafts["07_ppi_network"] = """# RESULTS: Protein-Protein Interaction (PPI) Network Architecture of the OSCA Family

To decipher the functional positioning of the OSCA gene family within the cellular signal transduction and mechanosensory cascades, and to investigate whether species with contrasting drought response strategies exhibit structural differences at the level of their osmosensory interactome, we reconstructed and analyzed species-specific protein-protein interaction (PPI) networks for *Vellozia peripherica* (Vper) and *Vellozia tubiflora* (Vtub). Using high-confidence interactome data retrieved from the STRING database (confidence score threshold >= 0.40) and topological analysis via NetworkX, undirected graphs were constructed using the identified OSCA proteins as primary seed nodes (Fig. 1).

### Global Network Topology and Connectivity Contrasts

Global topological profiling revealed distinct architectural properties between the networks of the two species (Table 1). The reconstructed *V. peripherica* interactome comprised 61 nodes and 187 interactions (edges), with an average network-wide degree of 6.13. The average degree of the connected VpOSCA proteins within this network was 6.09. In contrast, the *V. tubiflora* interactome, reconstructed using a similar configuration, comprised 60 nodes and a significantly denser web of 217 interactions, yielding a higher average network degree of 7.23 and a higher average connected VtOSCA degree of 7.30.

This topological difference indicates a higher interaction density and tighter integration of the osmosensory apparatus within the downstream molecular machinery in the desiccation-tolerant resurrection species (*V. tubiflora*) compared to the evergreen species (*V. peripherica*).

---

### Identification of Primary Osmosensory Hubs

Degree centrality analysis identified a highly specialized, hierarchical organization within the OSCA family, with a clear functional division of labor among the subfamilies. Highly connected "hub" nodes—defined as nodes with a degree at least twice the network average—were predominantly located within the OSCA1 and OSCA4 subfamilies in both species, whereas the OSCA2 and OSCA3 subfamilies occupied more peripheral modulatory positions (Fig. 2).

#### The Primary Vascular Sensor Hub: OSCA1.2
In both species, **OSCA1.2** emerged as a central, non-negotiable hub of the interactome, exhibiting an identical and highly pronounced connectivity of **18 connections** in both *V. peripherica* (`VpOSCA1.2`) and *V. tubiflora* (`VtOSCA1.2`). This high connectivity is functionally consistent with the spatial expression patterns observed for this locus, which exhibits massive transcriptional enrichment in the root and stem tissues of both species (Log2FC = 4.40 in Vper; 8.64 in Vtub relative to leaf tissue). Topologically, OSCA1.2 is strongly coupled to primary energy-transducing elements, specifically plasma membrane H+-ATPases and voltage-dependent calcium channels, reinforcing its role as the ancestral, core subterranean/vascular osmosensor in the genus *Vellozia*.

#### The Stress-Inducible Modulator Hub: OSCA4.1
The OSCA4 clade represented a second major topological hub, although it exhibited species-specific variations in connectivity:
*   In *V. peripherica*, `VpOSCA4.1` represented the absolute highest-degree node in the entire network, with **19 connections**.
*   In *V. tubiflora*, `VtOSCA4.1` maintained a robust but slightly lower connectivity of **13 connections**.

Functional annotation of the VpOSCA4.1 and VtOSCA4.1 interactors revealed a significant enrichment of molecular chaperones, particularly Heat Shock Protein 70 (HSP70) and Late Embryogenesis Abundant (LEA) group 4 proteins. The exceptionally high degree of `VpOSCA4.1` in the evergreen species suggests an active, continuous integration of this channel with protein-stabilizing machinery, consistent with the physiological demands of a foliage-retaining species that must actively cope with daily diurnal thermal and radiative fluctuations in the *campos rupestres* without undergoing metabolic dormancy.

#### The Leaf-Enriched Modulator: OSCA1.1
Consistent with its transcriptional enrichment in photosynthetic tissues, **OSCA1.1** acted as a secondary hub in both networks, with **11 connections** in *V. peripherica* and **13 connections** in *V. tubiflora*. Its immediate neighborhood is highly enriched in inward-rectifying potassium channels and stomatal regulatory proteins, indicating a specialized role in leaf turgor maintenance and stomatal closure control.

---

### Topological Evidence of Subfunctionalization in the Duplicated Locus VpOSCA2.4a/b

Genomic macrosynteny analysis identified a recent, lineage-specific tandem duplication event on Chromosome 1A unique to *V. peripherica*, resulting in two adjacent copies (`VpOSCA2.4a` and `VpOSCA2.4b`), whereas *V. tubiflora* retains a single ancestral copy (`VtOSCA2.4`). 

Comparative network topology provided clear molecular evidence supporting the functional subfunctionalization of these duplicated copies:
*   In the *V. tubiflora* network, the single ancestral channel `VtOSCA2.4` maintains **5 connections** to downstream interactors.
*   In the *V. peripherica* network, the newly emerged duplicates `VpOSCA2.4a` and `VpOSCA2.4b` exhibit a marked reduction in individual connectivity, possessing only **2 connections** each.

This striking partition of interaction partners represents a classic molecular signature of **subfunctionalization via interaction partner division**. Rather than a single protein maintaining all ancestral interactions, the duplicated genes on Chromosome 1A in Vper have split the functional interactome load, potentially allowing the evergreen species to fine-tune the mechanical sensitivity and transcriptional regulation of these individual modulators.

---

### The Silent Periphery: OSCA2.1, OSCA2.2, and OSCA2.3

In stark contrast to the highly connected hubs, the orthologous pairs **OSCA2.1**, **OSCA2.2**, and **OSCA2.3** exhibited **0 connections** under the applied high-confidence threshold in both species' networks. 

This silent status does not indicate non-functionality, but rather extreme specialization. OSCA2.3, in particular, was previously identified as being under the most severe evolutionary purifying constraint in the entire family (Ka/Ks = 0.053). The topological isolation of these three modulators under baseline, non-stressed models suggests they function as highly guarded, pathway-specific switches. By remaining disconnected from the global, everyday metabolic network, these channels are shielded from metabolic noise, ensuring they are activated exclusively during catastrophic physical events, such as severe, lethal-range turgor collapse (Vper) or the immediate, rapid influx of water during the rehydration phase of the resurrection cycle (Vtub).

---

### Integration into the Dual-Track Evolutionary Model

Viewed collectively, the topological properties of the *Vellozia* OSCA networks provide physical, structural confirmation of the proposed **Dual-Track Evolutionary Model**:

1.  **The Conserved Track (OSCA1.2 and OSCA1.1):** Topologically invariant, these baseline osmosensors preserve identical, high-degree hub architectures and tissue enrichment in both species, securing a robust, non-negotiable threshold sensor for water availability.
2.  **The Divergent Track (OSCA2 and OSCA3+4):** Characterized by high plasticity, selection relaxation in the resurrection species *V. tubiflora* correlates with a highly integrated, dense network topology (217 edges) optimized for rapid binary signaling, whereas diversifying selection in the evergreen *V. peripherica* has physically reshaped the modulatory track through targeted locus expansion and subfunctionalization (VpOSCA2.4a/b), providing the evergreen species with the required sensory fine-tuning to navigate subtle, daily diurnal and seasonal environmental fluctuations actively.
"""

# ==========================================
# WRITE ALL DRAFTS
# ==========================================
for topic, content in drafts.items():
    txt_filename = f"{topic}_results_draft.txt"
    docx_filename = f"{topic}_results_draft.docx"
    
    txt_path = os.path.join(docs_dir, txt_filename)
    docx_path = os.path.join(docs_dir, docx_filename)
    
    # Save TXT
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved TXT to: {txt_path}")
    
    # Save DOCX
    doc = docx.Document()
    lines = content.split('\n')
    for line in lines:
        if line.startswith('# '):
            doc.add_heading(line[2:], level=1)
        elif line.startswith('## '):
            doc.add_heading(line[3:], level=2)
        elif line.startswith('### '):
            doc.add_heading(line[4:], level=3)
        elif line.startswith('#### '):
            doc.add_heading(line[5:], level=4)
        elif line.startswith('*   '):
            doc.add_paragraph(line[4:], style='List Bullet')
        elif line.startswith('-   '):
            doc.add_paragraph(line[4:], style='List Bullet')
        elif line.strip() == '---':
            doc.add_paragraph('────────────────────────────────────────')
        else:
            doc.add_paragraph(line)
            
    doc.save(docx_path)
    print(f"Saved DOCX to: {docx_path}")

print("\n🎉 ALL DRAFTS SUCCESSFULLY GENERATED!")
