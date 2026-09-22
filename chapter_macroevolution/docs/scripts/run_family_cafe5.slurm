#!/bin/bash
#SBATCH --job-name=cafe5_macro
#SBATCH --output=/home/mfcaval/github/doutorado/chapter_macroevolution/04_gene_families/cafe5_%j.log
#SBATCH --error=/home/mfcaval/github/doutorado/chapter_macroevolution/04_gene_families/cafe5_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --partition=short
#SBATCH --time=12:00:00
#SBATCH --reservation=teste

# ==============================================================================
# Pipeline: 04_Gene_Families (CAFE5 Base & Gamma Models)
# Chapter: Macroevolution and Genomics in Velloziaceae
# Candidate: Mariana Feitosa Cavalheiro (UNICAMP)
# ==============================================================================

set -euo pipefail

BASE_DIR="/home/mfcaval/github/doutorado/chapter_macroevolution"
SCRIPT_DIR="${BASE_DIR}/scripts"
CAFE_DIR="${BASE_DIR}/04_gene_families"
PHYLO_DIR="${BASE_DIR}/02_phylogenomics"
DATING_DIR="${BASE_DIR}/03_dating"
CAFE_BIN="/home/mfcaval/.local/share/mamba/envs/cafe5_env/bin/cafe5"
THREADS="${SLURM_CPUS_PER_TASK:-8}"

mkdir -p "${CAFE_DIR}"

echo "======================================================================"
echo " 1. Preparing CAFE5 Input Table from OrthoFinder Definitive Counts"
echo "======================================================================"
python3 "${SCRIPT_DIR}/prep_family_cafe5.py"

INPUT_COUNTS="${CAFE_DIR}/cafe_family_input.tsv"
if [ ! -f "${INPUT_COUNTS}" ]; then
    echo "[ERRO] Tabela de contagens ${INPUT_COUNTS} não encontrada."
    exit 1
fi

echo "======================================================================"
echo " 2. Preparing Ultrametric Tree Calibrated with Fossils"
echo "======================================================================"
ULTRAMETRIC_TREE="${CAFE_DIR}/velloziaceae_ultrametric.tre"

if [ -f "${DATING_DIR}/velloziaceae_chronogram.tre" ]; then
    echo "[INFO] Usando cronograma ultramétrico calibrado do MCMCtree..."
    cp "${DATING_DIR}/velloziaceae_chronogram.tre" "${ULTRAMETRIC_TREE}"
elif [ -f "${PHYLO_DIR}/iqtree_pan_velloziaceae.treefile" ]; then
    echo "[INFO] Calibrando arvore do IQ-TREE com fósseis via ape::chronos..."
    Rscript "${SCRIPT_DIR}/calibrate_tree_for_cafe.R" "${PHYLO_DIR}/iqtree_pan_velloziaceae.treefile" "${ULTRAMETRIC_TREE}"
fi

if [ ! -f "${ULTRAMETRIC_TREE}" ]; then
    echo "[ERRO] Árvore ultramétrica não foi gerada em ${ULTRAMETRIC_TREE}."
    exit 1
fi

OUTPUT_DIR="${CAFE_DIR}/cafe5_results"
mkdir -p "${OUTPUT_DIR}"

echo "======================================================================"
echo " 3. Running CAFE5 Base Model (Single Lambda with p-values)"
echo "======================================================================"
rm -rf "${OUTPUT_DIR}/base_model"
"${CAFE_BIN}" \
    -i "${INPUT_COUNTS}" \
    -t "${ULTRAMETRIC_TREE}" \
    -p \
    -o "${OUTPUT_DIR}/base_model" \
    -c "${THREADS}"

echo "======================================================================"
echo " 4. Running CAFE5 Gamma Model (4 Rate Categories: -k 4)"
echo "======================================================================"
rm -rf "${OUTPUT_DIR}/gamma_model"
"${CAFE_BIN}" \
    -i "${INPUT_COUNTS}" \
    -t "${ULTRAMETRIC_TREE}" \
    -k 4 \
    -p \
    -o "${OUTPUT_DIR}/gamma_model" \
    -c "${THREADS}"

echo "======================================================================"
echo " CAFE5 Modeling Finished Successfully!"
echo " Results available in: ${OUTPUT_DIR}"
echo "======================================================================"
