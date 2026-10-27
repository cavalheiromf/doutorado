#!/bin/bash
#SBATCH --job-name=cafe5_rev_s2
#SBATCH --output=/home/mfcaval/github/doutorado/chapter_macroevolution_review/04_gene_families/cafe5/logs/cafe5_stage2_%j.log
#SBATCH --error=/home/mfcaval/github/doutorado/chapter_macroevolution_review/04_gene_families/cafe5/logs/cafe5_stage2_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --partition=short
#SBATCH --time=12:00:00
#SBATCH --reservation=teste

# ==============================================================================
# 03_run_cafe5_stage2_gamma_models.slurm
#
# Etapa 2 do protocolo CAFE5 (6 monocotiledôneas):
#   - Testa heterogeneidade de taxas ENTRE famílias gênicas sob 1-lambda nos ramos
#     (mantendo a mesma régua estatística entre Vper e Vtub).
#   - Executa 5 réplicas para Gamma k=2 e 5 réplicas para Gamma k=3, utilizando
#     o modelo de erro fixado na Etapa 1 (selected_error_model.txt).
# ==============================================================================

set -euo pipefail

BASE_DIR="/home/mfcaval/github/doutorado/chapter_macroevolution_review"
CAFE_BIN="/home/mfcaval/.local/share/mamba/envs/cafe5_env/bin/cafe5"
INPUT_COUNTS="${BASE_DIR}/04_gene_families/cafe5/input/cafe_family_input_6taxa.tsv"
TREE_FILE="${BASE_DIR}/03_dating/final_trees/velloziaceae_6taxa_ultrametric.tre"
SELECTED_ERR="${BASE_DIR}/04_gene_families/cafe5/runs/stage1_error_calibration/selected_error_model.txt"
OUT_BASE="${BASE_DIR}/04_gene_families/cafe5/runs/stage2_gamma_rates"

THREADS="${SLURM_CPUS_PER_TASK:-8}"
N_REPS="${N_REPS:-5}"
ITERATIONS="${ITERATIONS:-500}"

if [ ! -f "${SELECTED_ERR}" ]; then
    echo "[ERRO] Arquivo ${SELECTED_ERR} não encontrado. Execute a Etapa 1 (02_run_cafe5_stage1_error_model.slurm) primeiro."
    exit 1
fi

mkdir -p "${OUT_BASE}/gamma_k2" "${OUT_BASE}/gamma_k3"

for k in 2 3; do
    echo "======================================================================"
    echo " ETAPA 2: Modelo Gamma k=${k} com Error Model Fixo (${N_REPS} réplicas)"
    echo "======================================================================"
    for rep in $(seq 1 "${N_REPS}"); do
        REP_DIR="${OUT_BASE}/gamma_k${k}/rep_${rep}"
        if [ -f "${REP_DIR}/Gamma_results.txt" ]; then
            echo "[INFO] Gamma k=${k} - Réplica ${rep} já concluída. Pulando."
        else
            echo "[RUN] Gamma k=${k} - Réplica ${rep}..."
            "${CAFE_BIN}" \
                -i "${INPUT_COUNTS}" \
                -t "${TREE_FILE}" \
                -p \
                -P 0.05 \
                -e"${SELECTED_ERR}" \
                -k "${k}" \
                -o "${REP_DIR}" \
                -c "${THREADS}" \
                -I "${ITERATIONS}" \
                > "${REP_DIR}.log" 2>&1
        fi
    done
done

echo "======================================================================"
echo " ETAPA 2 CONCLUÍDA COM SUCESSO!"
echo "======================================================================"

