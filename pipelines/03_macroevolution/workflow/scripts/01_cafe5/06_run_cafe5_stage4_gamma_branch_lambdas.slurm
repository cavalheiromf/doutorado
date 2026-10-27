#!/bin/bash
#SBATCH --job-name=cafe5_rev_s4
#SBATCH --output=/home/mfcaval/github/doutorado/chapter_macroevolution_review/04_gene_families/cafe5/logs/cafe5_stage4_%A_%a.log
#SBATCH --error=/home/mfcaval/github/doutorado/chapter_macroevolution_review/04_gene_families/cafe5/logs/cafe5_stage4_%A_%a.err
#SBATCH --array=0-19
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --partition=short
#SBATCH --time=12:00:00

# Testa heterogeneidade entre famílias (Gamma k=3) e entre ramos no mesmo
# modelo. Cada tarefa do array executa uma das 5 réplicas de M2--M5.

set -euo pipefail

BASE_DIR="/home/mfcaval/github/doutorado/chapter_macroevolution_review"
CAFE_BIN="/home/mfcaval/.local/share/mamba/envs/cafe5_env/bin/cafe5"
INPUT_COUNTS="${BASE_DIR}/04_gene_families/cafe5/input/cafe_family_input_6taxa.tsv"
TREE_FILE="${BASE_DIR}/03_dating/final_trees/velloziaceae_6taxa_ultrametric.tre"
LAMBDA_DIR="${BASE_DIR}/04_gene_families/cafe5/lambda_trees"
SELECTED_ERR="${BASE_DIR}/04_gene_families/cafe5/runs/stage1_error_calibration/selected_error_model.txt"
OUT_BASE="${BASE_DIR}/04_gene_families/cafe5/runs/stage4_gamma_branch_lambdas"

THREADS="${SLURM_CPUS_PER_TASK:-8}"
ITERATIONS="${ITERATIONS:-800}"
GAMMA_CATEGORIES="${GAMMA_CATEGORIES:-3}"
N_REPS=5

MODEL_NAMES=(
    "M2_2lambda_family"
    "M3_3lambda_vellozia_clade"
    "M4_3lambda_avoidant_shift"
    "M5_4lambda_split_sisters"
)

TASK_ID="${SLURM_ARRAY_TASK_ID:-0}"
N_TASKS=$((${#MODEL_NAMES[@]} * N_REPS))
if (( TASK_ID < 0 || TASK_ID >= N_TASKS )); then
    echo "[ERRO] SLURM_ARRAY_TASK_ID=${TASK_ID}; esperado 0-$((N_TASKS - 1))."
    exit 2
fi

MODEL_INDEX=$((TASK_ID / N_REPS))
REP=$((TASK_ID % N_REPS + 1))
MODEL_NAME="${MODEL_NAMES[MODEL_INDEX]}"
ltree="${LAMBDA_DIR}/${MODEL_NAME}.tre"
REP_DIR="${OUT_BASE}/${MODEL_NAME}/rep_${REP}"

if [ ! -f "${SELECTED_ERR}" ]; then
    echo "[ERRO] Modelo de erro não encontrado: ${SELECTED_ERR}"
    exit 1
fi

mkdir -p "${OUT_BASE}/${MODEL_NAME}"
if [ -f "${REP_DIR}/Gamma_results.txt" ]; then
    echo "[INFO] ${MODEL_NAME}, Gamma k=${GAMMA_CATEGORIES}, réplica ${REP} já concluída."
    exit 0
fi

echo "[RUN] ${MODEL_NAME}, Gamma k=${GAMMA_CATEGORIES}, réplica ${REP}"
"${CAFE_BIN}" \
    -i "${INPUT_COUNTS}" \
    -t "${TREE_FILE}" \
    -k "${GAMMA_CATEGORIES}" \
    -y "${ltree}" \
    -p \
    -P 0.05 \
    -e"${SELECTED_ERR}" \
    -o "${REP_DIR}" \
    -c "${THREADS}" \
    -I "${ITERATIONS}" \
    > "${REP_DIR}.log" 2>&1

echo "[OK] ${MODEL_NAME}, réplica ${REP} concluída."
