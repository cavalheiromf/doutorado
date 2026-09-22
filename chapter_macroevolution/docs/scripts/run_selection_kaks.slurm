#!/bin/bash
#SBATCH --job-name=kaks_macro
#SBATCH --output=/home/mfcaval/github/doutorado/chapter_macroevolution/05_selection/kaks_%j.log
#SBATCH --error=/home/mfcaval/github/doutorado/chapter_macroevolution/05_selection/kaks_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --partition=short
#SBATCH --time=12:00:00
#SBATCH --reservation=teste

# ==============================================================================
# Pipeline: 05_Selection (Pairwise Ka/Ks with PAML yn00 for 1:1 Orthologs)
# Chapter: Macroevolution and Genomics in Velloziaceae
# Candidate: Mariana Feitosa Cavalheiro (UNICAMP)
# ==============================================================================

set -euo pipefail

BASE_DIR="/home/mfcaval/github/doutorado/chapter_macroevolution"
SCRIPT_DIR="${BASE_DIR}/docs/scripts"
SEL_DIR="${BASE_DIR}/05_selection"
RUN_DIR="${SEL_DIR}/validated_yn00_${SLURM_JOB_ID:?Submit this script with sbatch}"

mkdir -p "${SEL_DIR}"

echo "======================================================================"
echo " Starting Genome-Wide Pairwise Ka/Ks Analysis (PAML yn00)"
echo " Node:             $(hostname)"
echo " Start Date/Time:  $(date)"
echo "======================================================================"

python3 "${SCRIPT_DIR}/calculate_kaks_1to1.py" \
    --output-dir "${RUN_DIR}" --threads "${SLURM_CPUS_PER_TASK:-8}"

echo "======================================================================"
echo " Ka/Ks Analysis Complete!"
echo " Results available in: ${RUN_DIR}/pairwise_kaks_all.tsv"
echo " End Date/Time:    $(date)"
echo "======================================================================"
