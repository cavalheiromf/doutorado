#!/bin/bash
#SBATCH --job-name=iqtree_macro
#SBATCH --output=/home/mfcaval/github/doutorado/chapter_macroevolution/02_phylogenomics/iqtree_%j.log
#SBATCH --error=/home/mfcaval/github/doutorado/chapter_macroevolution/02_phylogenomics/iqtree_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --partition=short
#SBATCH --time=2-00:00:00

# ==============================================================================
# Pipeline: 02_Phylogenomics (IQ-TREE 2)
# Chapter: Macroevolution and Genomics in Velloziaceae
# ==============================================================================

set -euo pipefail

BASE_DIR="/home/mfcaval/github/doutorado/chapter_macroevolution"
SCRIPT_DIR="${BASE_DIR}/scripts"
OUT_DIR="${BASE_DIR}/02_phylogenomics"
THREADS="${SLURM_CPUS_PER_TASK:-16}"

mkdir -p "${OUT_DIR}"

echo "======================================================================"
echo " 1. Extracting, Aligning and Concatenating Single-Copy Orthologs"
echo "======================================================================"
# Usa MAFFT (requer módulo do MAFFT)
module load Bio/MAFFT/7.520-GCC-12.3.0-with-extensions

python3 "${SCRIPT_DIR}/extract_align_concatenate_single_copy.py" -t "${THREADS}"

# Verifica se a supermatriz foi criada com sucesso
MATRIX_FA="${OUT_DIR}/pan_velloziaceae_supermatrix.fa"
if [ ! -f "${MATRIX_FA}" ]; then
    echo "[ERRO] Supermatriz não encontrada. O script Python falhou."
    exit 1
fi

echo "======================================================================"
echo " 2. Running IQ-TREE 2 (Phylogenomic Inference)"
echo "======================================================================"
module purge
module load Bio/IQ-TREE/2.3.6-omp

cd "${OUT_DIR}"

iqtree2 -s "${MATRIX_FA}" \
        -p partitions.nexus \
        -m MFP \
        -B 1000 \
        -T AUTO \
        -ntmax "${THREADS}" \
        --prefix "iqtree_pan_velloziaceae"

echo "======================================================================"
echo " Phylogenomics Pipeline Complete!"
echo "======================================================================"
