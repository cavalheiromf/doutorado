# Comparative Genomics and Evolutionary History of Velloziaceae

[![UNICAMP](https://img.shields.io/badge/UNICAMP-Institute_of_Biology-blue.svg)](https://www.ib.unicamp.br/)
[![GCCRC](https://img.shields.io/badge/GCCRC-Genomics_Center-green.svg)](https://www.gccrc.unicamp.br/)
[![BioProject](https://img.shields.io/badge/NCBI_BioProject-PRJNA984512-orange.svg)](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA984512)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Official repository of data, analyses, computational pipelines, and manuscripts for the PhD thesis of **Mariana Feitosa Cavalheiro**, conducted within the Graduate Program in Genetics and Molecular Biology (PPG-GBM) at the Institute of Biology, University of Campinas (UNICAMP), in collaboration with the Genomics for Climate Change Research Center (GCCRC), the Center for Molecular Biology and Genetic Engineering (CBMEG), and Embrapa Digital Agriculture.

---

## Institutional Information

* **Candidate**: Mariana Feitosa Cavalheiro
* **Advisor**: Dr. Isabel Rodrigues Gerhardt (Embrapa Digital Agriculture / GCCRC / UNICAMP)
* **Co-advisors and Primary Collaborators**: Dr. Ricardo Augusto Dante (Embrapa / GCCRC), Prof. Dr. Paulo Arruda (UNICAMP / CBMEG), Dr. Francine A. N. de Almeida (UNICAMP)
* **Graduate Program**: Graduate Program in Genetics and Molecular Biology (PPG-GBM), Institute of Biology, UNICAMP
* **Financial Support**:
  * São Paulo Research Foundation (FAPESP, doctoral fellowships and research grants 2020/02084-0 and 2016/23218-0)
  * National Council for Scientific and Technological Development (CNPq, grant 140481/2020-6 and productivity research fellowship)
* **Legal Compliance and Genetic Heritage Access**:
  * **SisGen**: Registrations AF30A4D (*Vellozia peripherica*) and A5985A4 (*Vellozia tubiflora*), Ministry of Environment, Brazil.
  * **ICMBio**: Botanical collection permits in Serra da Canastra National Park (Delfinópolis, MG, Brazil).

---

## Thesis Structure

| Component | Title / Topic | Canonical Manuscript | Directory |
| :--- | :--- | :--- | :--- |
| **00_Introduction** | *General Introduction and Literature Review* | [Text](docs/00_introduction/general_introduction_thesis_181026.md) | [docs/00_introduction/](docs/00_introduction/) |
| **01_Chapter_1** | *A Haplotype-Resolved, Near Telomere-to-Telomere Genome Assembly of the Desiccation-Tolerant Plant Vellozia tubiflora* | [Manuscript](docs/01_chapter_1_tubiflora/manuscripts/chapter_tubiflora_master_draft.md) | [docs/01_chapter_1_tubiflora/](docs/01_chapter_1_tubiflora/) |
| **02_Chapter_2** | *Organellar Genomes: Plastome and Mitochondrion in Velloziaceae* | *(Contextualized in thesis)* | [docs/00_introduction/](docs/00_introduction/) |
| **03_Chapter_3** | *Ancestral Gene-Family Expansion and Asymmetric Local Duplication in Two Vellozia Species with Contrasting Drought-Survival Strategies* | [Manuscript](docs/03_chapter_3_macroevolution/manuscripts/chapter_macroevolution_article.md) | [docs/03_chapter_3_macroevolution/](docs/03_chapter_3_macroevolution/) |
| **04_Chapter_4** | *Genome-Wide Identification, Comparative Synteny, and Evolutionary Divergence of OSCA Mechanosensitive Ion Channels in Resurrection and Evergreen Vellozia* | [Manuscript](docs/04_chapter_4_osca/manuscripts/chapter_4_osca_mechanosensation.md) | [docs/04_chapter_4_osca/](docs/04_chapter_4_osca/) |
| **06_Discussion** | *General Cross-Cutting Discussion and Conclusions* | [Text](docs/06_general_discussion_and_conclusions/discussao_transversal_tese.md) | [docs/06_general_discussion_and_conclusions/](docs/06_general_discussion_and_conclusions/) |

---

## Analytical Pipelines and Reproducibility

Bioinformatics workflows and scripts are structured into modular, reproducible execution units:

* **[pipelines/03_macroevolution/](pipelines/03_macroevolution/)**:
  - Orthology delineation across monocots and outgroups (OrthoFinder).
  - Phylogenomics via concatenated supermatrix and multi-species coalescent model (ASTRAL-II).
  - Molecular dating under fossil-calibrated relaxed molecular clock (MCMCtree).
  - Stochastic modeling of gene family expansion and contraction (CAFE5, M5 model with Gamma rate distribution).
  - Duplication mechanism classification and macrosynteny analysis (MCScanX / JCVI).
  - Nonsynonymous and synonymous substitution rates (PAML / codeml) across orthologous trios polarized by *Xerophyta schlechteri*.
  - Functional enrichment (GO and KEGG) with FDR correction and stratified permutations.

* **[pipelines/04_osca/](pipelines/04_osca/)**:
  - Genome-wide identification and Pfam domain curation (PF02714, PF13967, PF14703 via HMMER and InterProScan).
  - Molecular phylogeny and transmembrane topology prediction (IQ-TREE and Phobius/TMHMM).
  - Comparative microsynteny and physical collinearity analysis (MCScan).
  - Selection intensity modeling (HyPhy RELAX) and pairwise evolutionary rates (PAML YN00).
  - Tissue-associated expression profiles under field conditions (STAR, featureCounts, DESeq2).
  - Protein-protein functional association network reconstruction (STRING API v12) and module enrichment.
  - Cis-regulatory promoter architecture and motif discovery (PlantCARE).

* For comprehensive instructions on recreating environments, validating data checksums, and executing pipelines locally or via SLURM, see [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md).

---

## Directory Organization in `docs/`

* **`docs/00_introduction/`** through **`docs/06_general_discussion_and_conclusions/`**: Markdown manuscripts with high-resolution embedded figures, consolidated tables, and formatted bibliographies.
* **[docs/literature/](docs/literature/)**: Reference library, OpenAlex metadata, and BibTeX files (`.bib`).
* **[docs/qualification_and_forms/](docs/qualification_and_forms/)**: Qualification outlines and institutional documentation.

---

## Data Availability

1. **Raw Genomic Sequencing Data and Assemblies**:
   - Deposited at NCBI under BioProject **PRJNA984512**.
2. **Supplementary Packages**:
   - Complete supplementary tables for each chapter are available in `.xlsx` and `.tsv` formats in their respective `docs/` and `pipelines/` subdirectories.
3. **High-Resolution Figures**:
   - Available individually in vector and raster formats (`.svg`, `.pdf`, `.png`) within each chapter's figures directory.

---

## How to Cite

> CAVALHEIRO, Mariana Feitosa. **Computational and Genomic Approaches to Investigating Plant Responses to Drought Stress: Velloziaceae as a Model System**. 2026. PhD Thesis (Doctorate in Genetics and Molecular Biology) — Institute of Biology, University of Campinas (UNICAMP), Campinas, Brazil, 2026.
