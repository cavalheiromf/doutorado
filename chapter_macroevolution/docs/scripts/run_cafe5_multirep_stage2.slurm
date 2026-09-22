#!/bin/bash
#SBATCH --job-name=cafe5_stg2
#SBATCH --output=/home/mfcaval/github/doutorado/chapter_macroevolution/04_gene_families/cafe5_stage2_%j.log
#SBATCH --error=/home/mfcaval/github/doutorado/chapter_macroevolution/04_gene_families/cafe5_stage2_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --partition=short
#SBATCH --time=12:00:00
#SBATCH --reservation=teste

# ==============================================================================
# Pipeline: CAFE5 Re-execution Stage 2 (Gamma Models with Fixed Error Model)
# Chapter: Macroevolution and Genomics in Velloziaceae
# Candidate: Mariana Feitosa Cavalheiro (UNICAMP)
# ==============================================================================

set -euo pipefail

BASE_DIR="/home/mfcaval/github/doutorado/chapter_macroevolution"
SCRIPT_DIR="${BASE_DIR}/scripts"
CAFE_DIR="${BASE_DIR}/04_gene_families"
RERUN_DIR="${CAFE_DIR}/cafe5_results/rerun"
CAFE_BIN="/home/mfcaval/.local/share/mamba/envs/cafe5_env/bin/cafe5"
THREADS="${SLURM_CPUS_PER_TASK:-8}"

INPUT_COUNTS="${CAFE_DIR}/cafe_family_input.tsv"
ULTRAMETRIC_TREE="${CAFE_DIR}/velloziaceae_ultrametric.tre"
SELECTED_ERR_MODEL="${CAFE_DIR}/error_models/selected_error_model.txt"

if [ ! -f "${SELECTED_ERR_MODEL}" ]; then
    echo "[ERRO] Modelo de erro selecionado nao encontrado em ${SELECTED_ERR_MODEL}"
    echo "Execute a Etapa 1 primeiro (run_cafe5_multirep_stage1.slurm)."
    exit 1
fi

echo "======================================================================"
echo " STAGE 2A: Running Gamma Model k=2 with Fixed Error Model (5 Replicates)"
echo "======================================================================"
mkdir -p "${RERUN_DIR}/03_gamma_k2"

for rep in {01..05}; do
    OUT_REP="${RERUN_DIR}/03_gamma_k2/rep${rep}"
    if [ -f "${OUT_REP}/Gamma_report.cafe" ]; then
        echo "[INFO] Replicate ${rep} of gamma_k2 already completed. Skipping."
    else
        echo "[INFO] Running Gamma k=2 Replicate ${rep}..."
        mkdir -p "${OUT_REP}"
        "${CAFE_BIN}" \
            -i "${INPUT_COUNTS}" \
            -t "${ULTRAMETRIC_TREE}" \
            -p \
            -P 0.05 \
            -e"${SELECTED_ERR_MODEL}" \
            -k 2 \
            -o "${OUT_REP}" \
            -c "${THREADS}"
    fi
done

echo "======================================================================"
echo " STAGE 2B: Running Gamma Model k=3 with Fixed Error Model (5 Replicates)"
echo "======================================================================"
mkdir -p "${RERUN_DIR}/04_gamma_k3"

for rep in {01..05}; do
    OUT_REP="${RERUN_DIR}/04_gamma_k3/rep${rep}"
    if [ -f "${OUT_REP}/Gamma_report.cafe" ]; then
        echo "[INFO] Replicate ${rep} of gamma_k3 already completed. Skipping."
    else
        echo "[INFO] Running Gamma k=3 Replicate ${rep}..."
        mkdir -p "${OUT_REP}"
        "${CAFE_BIN}" \
            -i "${INPUT_COUNTS}" \
            -t "${ULTRAMETRIC_TREE}" \
            -p \
            -P 0.05 \
            -e"${SELECTED_ERR_MODEL}" \
            -k 3 \
            -o "${OUT_REP}" \
            -c "${THREADS}"
    fi
done

echo "======================================================================"
echo " STAGE 2C: Running Gamma Model k=4 Sensitivity (5 Replicates)"
echo "======================================================================"
mkdir -p "${RERUN_DIR}/05_gamma_k4_sensitivity"

for rep in {01..05}; do
    OUT_REP="${RERUN_DIR}/05_gamma_k4_sensitivity/rep${rep}"
    if [ -f "${OUT_REP}/Gamma_report.cafe" ]; then
        echo "[INFO] Replicate ${rep} of gamma_k4 already completed. Skipping."
    else
        echo "[INFO] Running Gamma k=4 Sensitivity Replicate ${rep}..."
        mkdir -p "${OUT_REP}"
        "${CAFE_BIN}" \
            -i "${INPUT_COUNTS}" \
            -t "${ULTRAMETRIC_TREE}" \
            -p \
            -P 0.05 \
            -e"${SELECTED_ERR_MODEL}" \
            -k 4 \
            -o "${OUT_REP}" \
            -c "${THREADS}"
    fi
done

echo "======================================================================"
echo " STAGE 2D: Comprehensive Evaluation, Model Selection & FDR Correction"
echo "======================================================================"
python3 "${SCRIPT_DIR}/evaluate_cafe5_models.py"

echo "======================================================================"
echo " STAGE 2 COMPLETED SUCCESSFULLY!"
echo "======================================================================"
