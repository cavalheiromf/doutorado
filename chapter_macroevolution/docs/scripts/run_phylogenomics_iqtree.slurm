#!/bin/bash
#SBATCH --job-name=iqtree_macro
#SBATCH --output=/home/mfcaval/github/doutorado/chapter_macroevolution/02_phylogenomics/iqtree_%j.log
#SBATCH --error=/home/mfcaval/github/doutorado/chapter_macroevolution/02_phylogenomics/iqtree_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --partition=short
#SBATCH --time=12:00:00
#SBATCH --reservation=teste

# ==============================================================================
# Pipeline: 02_Phylogenomics (MAFFT Alignment + IQ-TREE 2)
# Chapter: Macroevolution and Genomics in Velloziaceae
# Candidate: Mariana Feitosa Cavalheiro (UNICAMP)
# ==============================================================================

set -euo pipefail

BASE_DIR="/home/mfcaval/github/doutorado/chapter_macroevolution"
SCRIPT_DIR="${BASE_DIR}/scripts"
OF_DIR="${BASE_DIR}/01_orthology"
PHYLO_DIR="${BASE_DIR}/02_phylogenomics"
THREADS="${SLURM_CPUS_PER_TASK:-8}"

echo "======================================================================"
echo " Starting Post-OrthoFinder Phylogenomics Pipeline"
echo " Node:             $(hostname)"
echo " Start Date/Time:  $(date)"
echo " Threads:          ${THREADS}"
echo "======================================================================"

# 1. Extrair, Alinhar com MAFFT e Concatenar Ortólogos 1:1 de Cópia Única
echo "======================================================================"
echo " 1. Extracting, Aligning with MAFFT and Concatenating 1:1 Orthologs"
echo "======================================================================"
mkdir -p "${PHYLO_DIR}"

module purge
module load Bio/MAFFT/7.520

python3 "${SCRIPT_DIR}/extract_align_concatenate_single_copy.py" -t "${THREADS}"

MATRIX_FA="${PHYLO_DIR}/pan_velloziaceae_supermatrix.fa"
if [ ! -f "${MATRIX_FA}" ]; then
    echo "[ERRO] Supermatriz ${MATRIX_FA} não foi gerada. Abortando IQ-TREE."
    exit 1
fi

# 2. Executar IQ-TREE 2 com Seleção de Modelos e 1000 Ultrafast Bootstraps
echo "======================================================================"
echo " 2. Running IQ-TREE 2 Phylogenomics"
echo "======================================================================"
module purge
module load Bio/IQ-TREE/2.3.6

cd "${PHYLO_DIR}"

iqtree2 -s "${MATRIX_FA}" \
        -p partitions.nexus \
        -m MFP \
        -B 1000 \
        -T "${THREADS}" \
        --prefix "iqtree_pan_velloziaceae"

echo "======================================================================"
echo " Phylogenomics Pipeline Complete!"
echo " End Date/Time:    $(date)"
echo "======================================================================"
