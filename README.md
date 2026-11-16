# Comparative Genomics and Evolutionary History of Velloziaceae: Computational Pipelines

[![UNICAMP](https://img.shields.io/badge/UNICAMP-Institute_of_Biology-blue.svg)](https://www.ib.unicamp.br/)
[![GCCRC](https://img.shields.io/badge/GCCRC-Genomics_Center-green.svg)](https://www.gccrc.unicamp.br/)
[![NCBI BioProject](https://img.shields.io/badge/NCBI_BioProject-PRJNA984512-orange.svg)](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA984512)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Tests](https://img.shields.io/badge/pytest-passing-brightgreen.svg)](pytest.ini)

Official computational repository containing the bioinformatic pipelines, phylogenetic workflows, molecular evolution models, and reproducibility resources supporting the PhD thesis of **Mariana Feitosa Cavalheiro**, conducted within the Graduate Program in Genetics and Molecular Biology (PPG-GBM) at the Institute of Biology, University of Campinas (UNICAMP), in collaboration with the Genomics for Climate Change Research Center (GCCRC), the Center for Molecular Biology and Genetic Engineering (CBMEG), and Embrapa Digital Agriculture.

---

## Repository Overview & Scope

This repository is dedicated exclusively to the **computational code, analytical pipelines, and reproducibility frameworks** developed for the comparative genomics of *Velloziaceae*. 

To maintain a clean, lightweight, and modern codebase compliant with best bioinformatic practices:
* **Computational Pipelines (`pipelines/`):** Fully tracked, documented, and reproducible scripts for phylogenomics, gene family dynamics, molecular selection, transcriptomics, and cis-regulatory promoter modeling.
* **Genomic Data & Annotations (`data/`):** Large raw genomic sequences (`.fasta`), structural annotations (`.gff3`), and raw transcriptomic reads (`.fastq.gz`) are archived under NCBI BioProject **PRJNA984512** and are excluded from Git version control via `.gitignore`. Guidelines and checksum verification templates are provided in [`data/README.md`](data/README.md).
* **Thesis Manuscripts & Presentations:** Formal dissertation texts, qualification documents, and examination committee slide decks are archived through UNICAMP institutional repositories upon completion of the doctoral degree.

---

## Directory Architecture

```text
.
├── pipelines/
│   ├── 03_macroevolution/          # Macroevolutionary dynamics and comparative phylogenomics
│   │   ├── 01_orthology/           # Orthology delineation (OrthoFinder) across monocot lineages
│   │   ├── 02_phylogenomics/       # Supermatrix concatenation (IQ-TREE) and coalescent tree (ASTRAL-II)
│   │   ├── 03_dating/              # Fossil-calibrated relaxed molecular clock chronograms (MCMCtree)
│   │   ├── 04_gene_families/       # Stochastic turnover (CAFE5), duplication classification & GO enrichment
│   │   ├── results/                # Consolidated output tables, trees, and model summaries
│   │   ├── workflow/scripts/       # Modular execution scripts (CAFE5, MCScanX/JCVI, permutations)
│   │   └── run_pipeline.sh         # Master CLI runner for Chapter 3
│   │
│   └── 04_osca/                    # Diversification of OSCA mechanosensitive ion channels
│       ├── 01_gene_identification/ # HMMER and InterProScan structural domain curation
│       ├── 02_phylogeny/           # Maximum-likelihood phylogenetics (IQ-TREE)
│       ├── 03_synteny/             # Collinearity, micro-synteny, and tandem cluster architecture
│       ├── 04_evolutionary_rates/  # Pairwise dN/dS (PAML) and clade-specific selection (HyPhy RELAX/CONTRAST-FEL)
│       ├── 04_promoters/           # Cis-regulatory motif discovery (PlantCARE / ABRE elements)
│       ├── 05_rnaseq/              # Alignment, quality metrics, and gene-level count matrices
│       ├── 06_expression/          # Differential expression and tissue-associated profiling (DESeq2)
│       ├── 07_ppi_network/         # Protein-protein interaction network topology (STRING API v12)
│       ├── figures/                # Publication-ready vector and raster visualizations (.svg, .png, .pdf)
│       ├── workflow/scripts/       # Modular Python and R analytical workflows
│       └── run_pipeline.sh         # Master CLI runner for Chapter 4
│
├── data/
│   ├── README.md                   # Complete data inventory, NCBI accessions, and structure guide
│   └── checksums.sha256.example    # SHA-256 integrity verification template
│
├── environment.yml                 # Unified Conda/Mamba bioinformatics environment specification
├── pytest.ini                      # Pytest suite configuration for pipeline validation
├── README.md                       # Main repository overview and documentation
└── REPRODUCIBILITY.md              # Comprehensive step-by-step reproduction guide
```

---

## Analytical Pipelines

### 1. Macroevolution and Comparative Phylogenomics (`pipelines/03_macroevolution/`)
Focuses on the macroevolutionary transitions between desiccation-tolerant (*Vellozia tubiflora*, *Xerophyta viscosa*, *Acanthochlamys bracteata*) and drought-avoidant / evergreen (*Vellozia peripherica*) monocots:
- **Orthology & Phylogenomics:** Identification of 12,876 core monocot gene families; phylogenetic inference using concatenated supermatrices and multi-species coalescent methods.
- **Molecular Dating:** Fossil-calibrated molecular clock under soft bounds with MCMCtree, estimating the *V. tubiflora* – *V. peripherica* divergence at ~9.74 Ma.
- **Gene Family Turnover Modeling:** Multi-rate birth-and-death stochastic modeling with **CAFE5** incorporating branch heterogeneity and Gamma-distributed rate variation across families.
- **Duplication Classification:** Dissection of gene duplication mechanisms (WGD, tandem, proximal, dispersed, and singletons) using MCScanX and JCVI collinearity blocks.
- **Robust Functional Enrichment:** Gene Ontology (GO) and InterPro enrichment controlled via dual FDR thresholds, covariate balancing, and 10,000 stratified permutations across >30,000 hypothesis tests.

### 2. OSCA Mechanosensitive Ion Channel Diversification (`pipelines/04_osca/`)
Investigates the functional evolution of hyperosmolality-gated calcium-permeable mechanosensitive ion channels (OSCA/TMEM63):
- **Structural Curation:** Identification of 13 loci in *V. tubiflora* and 14 loci in *V. peripherica*, verifying the canonical domain triad (PF02714, PF14703, PF13967).
- **Phylogenetics & Microsynteny:** Distribution across the 4 viridiplantae clades (OSCA1–4), highlighting a conserved ancestral tandem triplication on Chromosome 7A (`OSCA1.3`/`1.4`/`1.5`) and a species-specific tandem duplication on Chromosome 1A (`VpOSCA2.4a`/`b`).
- **Molecular Selection:** Pairwise codon substitution rates via PAML (`codeml`/`yn00`), clade-partitioned selection intensity via **HyPhy RELAX**, and gap-sanitized site-specific divergence via **HyPhy CONTRAST-FEL**.
- **Transcriptomics & Cis-Regulation:** RNA-seq profiling across vegetative tissues (Leaf, Stem, Root) under seasonal field conditions, integrated with promoter motif scanning (2.0 kb upstream) targeting abscisic acid-responsive elements (ABRE).

---

## Quickstart & Reproducibility

### 1. Environment Setup

All software dependencies are managed via Conda/Mamba:

```bash
# Clone the repository
git clone https://github.com/cavalheiromf/doutorado.git
cd doutorado

# Create and activate the unified environment
mamba env create -f environment.yml
conda activate vellozia-genomics
```

### 2. Running Automated Tests

Validate pipeline scripts, parsing modules, and data integrity hooks:

```bash
pytest -v
```

### 3. Pipeline Execution

Each major pipeline features a unified command-line orchestrator:

```bash
# Macroevolution pipeline
bash pipelines/03_macroevolution/run_pipeline.sh --help

# OSCA gene family pipeline
bash pipelines/04_osca/run_pipeline.sh --help
```

For detailed step-by-step instructions, input preparations, SLURM cluster execution profiles, and checksum verifications, please refer to [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md).

---

## Data Availability & Access Policy

1. **NCBI BioProject Deposit:**
   - Raw sequencing data (PacBio HiFi, Illumina paired-end RNA-seq, and Hi-C / Omni-C) are available under NCBI BioProject **[PRJNA984512](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA984512)**.
2. **Local Data Structure:**
   - To configure local directories for pipeline reproduction, refer to [`data/README.md`](data/README.md) for expected filenames, folder hierarchies, and download instructions.
3. **Manuscripts & Thesis Documents:**
   - Following defense, the full doctoral dissertation and pedagogical materials will be accessible through the UNICAMP Institutional Library System.

---

## Institutional Information & Compliance

* **Candidate:** Mariana Feitosa Cavalheiro
* **Advisor:** Dr. Isabel Rodrigues Gerhardt (Embrapa Digital Agriculture / GCCRC / UNICAMP)
* **Co-advisors & Key Collaborators:**
  * Dr. Ricardo Augusto Dante (Embrapa / GCCRC)
  * Prof. Dr. Paulo Arruda (UNICAMP / CBMEG)
  * Dr. Francine A. N. de Almeida (UNICAMP)
* **Academic Program:** Graduate Program in Genetics and Molecular Biology (PPG-GBM), Institute of Biology, UNICAMP
* **Financial Support:**
  * São Paulo Research Foundation (FAPESP, Doctoral Fellowships and Research Grants 2020/02084-0 and 2016/23218-0)
  * National Council for Scientific and Technological Development (CNPq, Grant 140481/2020-6)
* **Legal Compliance & Genetic Heritage:**
  * **SisGen (Brazil):** Registrations AF30A4D (*Vellozia peripherica*) and A5985A4 (*Vellozia tubiflora*), Ministry of Environment, Brazil.
  * **ICMBio:** Collection permits for botanical sampling in Serra da Canastra National Park (Delfinópolis, MG, Brazil).

---

## Citation

> CAVALHEIRO, Mariana Feitosa. **Comparative genomics and OSCA gene family diversification in Vellozia species with contrasting responses to water limitation**. 2026. PhD Thesis (Doctorate in Genetics and Molecular Biology) — Institute of Biology, University of Campinas (UNICAMP), Campinas, Brazil, 2026.
