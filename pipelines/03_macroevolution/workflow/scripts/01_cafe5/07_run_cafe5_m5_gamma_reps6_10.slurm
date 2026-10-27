#!/bin/bash
#SBATCH --job-name=cafe5_m5_r6_10
#SBATCH --output=/home/mfcaval/github/doutorado/chapter_macroevolution_review/04_gene_families/cafe5/logs/cafe5_m5_extra_%A_%a.log
#SBATCH --error=/home/mfcaval/github/doutorado/chapter_macroevolution_review/04_gene_families/cafe5/logs/cafe5_m5_extra_%A_%a.err
#SBATCH --array=6-10
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --partition=short
#SBATCH --time=12:00:00

# Réplicas adicionais, independentes, do modelo M5 com heterogeneidade
# entre famílias (Gamma k=3). Mantém os parâmetros da etapa 4 e grava
# exclusivamente em rep_6--rep_10.

set -euo pipefail

BASE_DIR="/home/mfcaval/github/doutorado/chapter_macroevolution_review"
CAFE_BIN="/home/mfcaval/.local/share/mamba/envs/cafe5_env/bin/cafe5"
INPUT_COUNTS="${BASE_DIR}/04_gene_families/cafe5/input/cafe_family_input_6taxa.tsv"
TREE_FILE="${BASE_DIR}/03_dating/final_trees/velloziaceae_6taxa_ultrametric.tre"
SELECTED_ERR="${BASE_DIR}/04_gene_families/cafe5/runs/stage1_error_calibration/selected_error_model.txt"
OUT_BASE="${BASE_DIR}/04_gene_families/cafe5/runs/stage4_gamma_branch_lambdas"

MODEL_NAME="M5_4lambda_split_sisters"
LAMBDA_TREE="${BASE_DIR}/04_gene_families/cafe5/lambda_trees/${MODEL_NAME}.tre"
GAMMA_CATEGORIES=3
ITERATIONS=800
THREADS="${SLURM_CPUS_PER_TASK:-8}"
REP="${SLURM_ARRAY_TASK_ID:?SLURM_ARRAY_TASK_ID is required}"

if (( REP < 6 || REP > 10 )); then
    echo "[ERRO] Réplica ${REP}; esperado 6--10."
    exit 2
fi

for required_file in "${CAFE_BIN}" "${INPUT_COUNTS}" "${TREE_FILE}" "${SELECTED_ERR}" "${LAMBDA_TREE}"; do
    if [ ! -f "${required_file}" ]; then
        echo "[ERRO] Arquivo obrigatório ausente: ${required_file}"
        exit 1
    fi
done

REP_DIR="${OUT_BASE}/${MODEL_NAME}/rep_${REP}"
mkdir -p "${OUT_BASE}/${MODEL_NAME}"

if [ -f "${REP_DIR}/Gamma_results.txt" ]; then
    echo "[INFO] M5+Gamma k=3, réplica ${REP}, já concluída; nada foi sobrescrito."
    exit 0
fi

echo "[RUN] M5+Gamma k=${GAMMA_CATEGORIES}, réplica ${REP}"
echo "[RUN] Saída: ${REP_DIR}"

"${CAFE_BIN}" \
    -i "${INPUT_COUNTS}" \
    -t "${TREE_FILE}" \
    -k "${GAMMA_CATEGORIES}" \
    -y "${LAMBDA_TREE}" \
    -p \
    -P 0.05 \
    -e"${SELECTED_ERR}" \
    -o "${REP_DIR}" \
    -c "${THREADS}" \
    -I "${ITERATIONS}" \
    > "${REP_DIR}.log" 2>&1

echo "[OK] M5+Gamma k=${GAMMA_CATEGORIES}, réplica ${REP}, concluída."
