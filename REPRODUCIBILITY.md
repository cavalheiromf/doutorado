# Computational Reproducibility Guide

This document provides detailed instructions to fully reproduce all computational results, phylogenomic analyses, evolutionary models, expression analyses, figures, and tables from the PhD thesis:

**"Computational and Genomic Approaches to Investigating Plant Responses to Drought Stress: *Velloziaceae* as a Model System"**  
Author: Mariana Feitosa Cavalheiro  
Genomics for Climate Change Research Center (GCCRC), University of Campinas (UNICAMP)  
Graduate Program in Genetics and Molecular Biology (PPG-GBM), Institute of Biology, UNICAMP

---

## 1. System Requirements and Hardware

- **Operating System:** Linux x86_64 (tested on Ubuntu 22.04 LTS and Rocky Linux 9).
- **Package Manager:** `mamba` or `conda` (Miniforge/Mambaforge strongly recommended).
- **Minimum Resources (Local Analyses / Figures / Tests):**
  - CPU: 8 cores
  - RAM: 16 GB
  - Free disk space: 50 GB
- **Recommended Resources for Computationally Intensive Workflows (PAML / CAFE5 / Global Alignments):**
  - CPU: 32+ cores (or access to an HPC cluster with a SLURM scheduler)
  - RAM: 64+ GB

---

## 2. Computational Environment Setup

All dependencies across Python, R/Bioconductor, and command-line bioinformatics tools are unified in [`environment.yml`](environment.yml).

### Creating and activating the environment:

```bash
# Clone the repository
git clone https://github.com/mfcaval/doutorado.git
cd doutorado

# Create the unified vellozia-genomics Conda environment
mamba env create -f environment.yml

# Activate the environment
conda activate vellozia-genomics
```

### External Third-Party Tools (if compiled outside Conda):
- **CAFE5:** If compiled from source, ensure the binary is in your `$PATH` or set the environment variable `export CAFE5_BIN=/path/to/cafe5`.
- **PAML (codeml):** Available via conda or system `$PATH`.

---

## 3. Data Provenance and Integrity

Raw datasets and genome assemblies are fully documented in [`data/README.md`](data/README.md).

### Data directory structure:
```
data/
├── genomes/
│   ├── Vtub/        # Vellozia tubiflora (near-T2T assembly, 9 pseudochromosomes)
│   ├── Vper/        # Vellozia plicata / intermedia (17 chromosomes)
│   └── outgroups/   # Xvis, Abra, Ptec, Dala, Ath
├── rnaseq/          # 18 paired-end libraries (Leaf, Stem, Root in Vtub and Vper)
├── pfam/            # HMM profiles (e.g., PF02714 for OSCA/TMEM63)
└── checksums.sha256 # SHA-256 integrity hashes
```

### Integrity verification:
```bash
# Verify that local files match the reference hashes:
sha256sum -c data/checksums.sha256
```

---

## 4. Chapter 3 Pipeline: Macroevolution and Comparative Phylogenomics

The Chapter 3 pipeline integrates orthogroup inference (OrthoFinder), evolutionary gene family turnover modeling (CAFE5), branch-specific positive selection testing (PAML/codeml), and functional enrichment analysis (clusterProfiler/TopGO).

### Master pipeline runner:
Located at [`pipelines/03_macroevolution/run_pipeline.sh`](pipelines/03_macroevolution/run_pipeline.sh).

```bash
# View available options
bash pipelines/03_macroevolution/run_pipeline.sh --help

# 1. Execute all steps sequentially on a local machine:
bash pipelines/03_macroevolution/run_pipeline.sh --step all --threads 16 --mode local

# 2. Execute the CAFE5 gene family turnover step:
bash pipelines/03_macroevolution/run_pipeline.sh --step cafe5 --threads 8

# 3. Execute the gene duplication classification step (WGD / DupPipe / synteny):
bash pipelines/03_macroevolution/run_pipeline.sh --step duplications --threads 8

# 4. Execute functional enrichment analysis:
bash pipelines/03_macroevolution/run_pipeline.sh --step enrichment --threads 8

# 5. Generate manuscript figures and tables:
bash pipelines/03_macroevolution/run_pipeline.sh --step manuscript

# To submit compute-intensive steps via SLURM on an HPC cluster:
bash pipelines/03_macroevolution/run_pipeline.sh --step cafe5 --mode slurm
```

---

## 5. Chapter 4 Pipeline: OSCA Gene Family Evolution

The Chapter 4 pipeline carries out comparative genomic identification, phylogeny, gene structure modeling, promoter cis-regulatory profiling, and RNA-seq expression analysis of the OSCA mechanosensitive channel family across *Vellozia tubiflora* and *Vellozia plicata*.

### Master pipeline runner:
Located at [`pipelines/04_osca/run_pipeline.sh`](pipelines/04_osca/run_pipeline.sh).

```bash
# View available options
bash pipelines/04_osca/run_pipeline.sh --help

# 1. Execute the complete pipeline locally:
bash pipelines/04_osca/run_pipeline.sh --step all --threads 8 --mode local

# 2. Curation and sequence extraction of OSCA loci:
bash pipelines/04_osca/run_pipeline.sh --step sequences

# 3. Evolutionary rate analysis and synteny (Ka/Ks):
bash pipelines/04_osca/run_pipeline.sh --step rates

# 4. Promoter and cis-acting element discovery (PlantCARE):
bash pipelines/04_osca/run_pipeline.sh --step promoters

# 5. Differential expression and heatmaps (DESeq2 / RNA-seq):
bash pipelines/04_osca/run_pipeline.sh --step expression

# 6. Verify integrity of generated outputs:
bash pipelines/04_osca/run_pipeline.sh --step verify
```

---

## 6. Reproduction of Figures and Tables

### Chapter 3 Figures:
- **Figure 1 (Phylogeny and WGD History):** `pipelines/03_macroevolution/workflow/scripts/manuscript_figures/generate_figure1_wgd.py`
- **Figure 2 (CAFE5 Expansions and Contractions):** `pipelines/03_macroevolution/workflow/scripts/manuscript_figures/generate_figure2_cafe5.py`
- **Figure 3 (Functional Enrichment of Stress Clades):** `pipelines/03_macroevolution/workflow/scripts/09_run_enrichment_pipeline.sh`

### Chapter 4 Figures:
- **Figure 1 (OSCA Phylogenetic Tree and Domain Architectures):** `pipelines/04_osca/workflow/scripts/figures/generate_figure1_osca_phylogeny.py`
- **Figure 2 (Synteny and Physical Collinearity):** `pipelines/04_osca/workflow/scripts/figures/generate_figure2_synteny.py`
- **Figure 3 (Stress-Responsive Cis-Regulatory Elements):** `pipelines/04_osca/workflow/scripts/figures/generate_figure3_promoters.py`
- **Figure 4 (Tissue Expression and Desiccation Heatmap):** `pipelines/04_osca/workflow/scripts/figures/generate_figure4_expression_heatmap.R`

---

## 7. Automated Test Suite

The repository includes automated unit and integration tests using `pytest` to verify master table consistency, gene identifier integrity, evolutionary model specifications, and output formatting:

```bash
# Run the complete test suite
pytest -v

# Run Chapter 3 tests only
pytest pipelines/03_macroevolution/workflow/tests/ -v

# Run Chapter 4 tests only
pytest pipelines/04_osca/workflow/tests/ -v
```

---

## 8. Contact and Support

- Mariana Feitosa Cavalheiro: [marianacavalheiro@unicamp.br](mailto:marianacavalheiro@unicamp.br)
- Genomics for Climate Change Research Center (GCCRC), UNICAMP
