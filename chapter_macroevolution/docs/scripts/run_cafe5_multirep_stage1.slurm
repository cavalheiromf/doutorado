#!/bin/bash
#SBATCH --job-name=cafe5_stg1
#SBATCH --output=/home/mfcaval/github/doutorado/chapter_macroevolution/04_gene_families/cafe5_stage1_%j.log
#SBATCH --error=/home/mfcaval/github/doutorado/chapter_macroevolution/04_gene_families/cafe5_stage1_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --partition=short
#SBATCH --time=12:00:00
#SBATCH --reservation=teste

# ==============================================================================
# Pipeline: CAFE5 Re-execution Stage 1 (Base Replicates & Error Estimation)
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

# 1. Sanity check: Ensure clean tree without whitespace
tr -d '[:blank:]' < "${ULTRAMETRIC_TREE}" > "${ULTRAMETRIC_TREE}.clean" && mv "${ULTRAMETRIC_TREE}.clean" "${ULTRAMETRIC_TREE}"

echo "======================================================================"
echo " STAGE 1A: Running Base Model Without Error (5 Replicates)"
echo "======================================================================"
mkdir -p "${RERUN_DIR}/01_base_noerror"

for rep in {01..05}; do
    OUT_REP="${RERUN_DIR}/01_base_noerror/rep${rep}"
    if [ -f "${OUT_REP}/Base_report.cafe" ]; then
        echo "[INFO] Replicate ${rep} of base_noerror already completed. Skipping."
    else
        echo "[INFO] Running Base NoError Replicate ${rep}..."
        mkdir -p "${OUT_REP}"
        "${CAFE_BIN}" \
            -i "${INPUT_COUNTS}" \
            -t "${ULTRAMETRIC_TREE}" \
            -p \
            -P 0.05 \
            -o "${OUT_REP}" \
            -c "${THREADS}"
    fi
done

echo "======================================================================"
echo " STAGE 1B: Running Base Model Estimating Count Error (5 Replicates)"
echo "======================================================================"
mkdir -p "${RERUN_DIR}/02_base_error"

for rep in {01..05}; do
    OUT_REP="${RERUN_DIR}/02_base_error/rep${rep}"
    if [ -f "${OUT_REP}/Base_error_model.txt" ] && [ -f "${OUT_REP}/Base_report.cafe" ]; then
        echo "[INFO] Replicate ${rep} of base_error already completed. Skipping."
    else
        echo "[INFO] Running Base With Error Estimation Replicate ${rep}..."
        mkdir -p "${OUT_REP}"
        "${CAFE_BIN}" \
            -i "${INPUT_COUNTS}" \
            -t "${ULTRAMETRIC_TREE}" \
            -p \
            -P 0.05 \
            -e \
            -o "${OUT_REP}" \
            -c "${THREADS}"
    fi
done

echo "======================================================================"
echo " STAGE 1C: Evaluating Error Models and Selecting Stable Matrix"
echo "======================================================================"
python3 "${SCRIPT_DIR}/select_error_model.py"

echo "======================================================================"
echo " STAGE 1 COMPLETED SUCCESSFULLY!"
echo "======================================================================"
