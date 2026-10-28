#!/bin/bash
#SBATCH --job-name=cafe5_rev_s3
#SBATCH --output=logs/cafe5_stage3_%j.log
#SBATCH --error=logs/cafe5_stage3_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --partition=short
#SBATCH --time=12:00:00
#SBATCH --reservation=teste

# ==============================================================================
# 04_run_cafe5_stage3_branch_lambdas.slurm
#
# Etapa 3 do protocolo CAFE5 (6 monocotiledôneas):
#   - Testa as hipóteses macroevolutivas de variação de taxa (lambda) ENTRE RAMOS (-y),
#     com o modelo de erro fixado na Etapa 1:
#       * M2 (2-lambda): Velloziaceae vs. Outgroups (Ptec, Dala)
#       * M3 (3-lambda): Clado Vellozia (tronco + Vper + Vtub) vs. Velloziaceae basais (Abra, Xvis) vs. Outgroups
#       * M4 (3-lambda): Ramo Avoidant (Vper) vs. Linhagens DT de Velloziaceae (Abra, Xvis, tronco, Vtub) vs. Outgroups
#       * M5 (4-lambda): Assimetria entre irmãs: Vper (lambda4) vs. Vtub (lambda3) vs. Basais DT (lambda2) vs. Outgroups (lambda1)
#   - Ao final, executa 05_evaluate_cafe5_models.py para consolidar AIC e LRT de todas as etapas.
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="${BASE_DIR:-$(cd "${SCRIPT_DIR}/../../.." && pwd)}"
CAFE_BIN="${CAFE_BIN:-$(which cafe5 2>/dev/null || which cafe 2>/dev/null || echo cafe5)}"
INPUT_COUNTS="${BASE_DIR}/04_gene_families/cafe5/input/cafe_family_input_6taxa.tsv"
TREE_FILE="${BASE_DIR}/03_dating/final_trees/velloziaceae_6taxa_ultrametric.tre"
LAMBDA_DIR="${BASE_DIR}/04_gene_families/cafe5/lambda_trees"
SELECTED_ERR="${BASE_DIR}/04_gene_families/cafe5/runs/stage1_error_calibration/selected_error_model.txt"
OUT_BASE="${BASE_DIR}/04_gene_families/cafe5/runs/stage3_branch_lambdas"

THREADS="${SLURM_CPUS_PER_TASK:-8}"
N_REPS="${N_REPS:-5}"
ITERATIONS="${ITERATIONS:-600}"

if [ ! -f "${SELECTED_ERR}" ]; then
    echo "[ERRO] Arquivo ${SELECTED_ERR} não encontrado. Execute a Etapa 1 primeiro."
    exit 1
fi

declare -A MODELS=(
    ["M2_2lambda_family"]="${LAMBDA_DIR}/M2_2lambda_family.tre"
    ["M3_3lambda_vellozia_clade"]="${LAMBDA_DIR}/M3_3lambda_vellozia_clade.tre"
    ["M4_3lambda_avoidant_shift"]="${LAMBDA_DIR}/M4_3lambda_avoidant_shift.tre"
    ["M5_4lambda_split_sisters"]="${LAMBDA_DIR}/M5_4lambda_split_sisters.tre"
)

for model_name in "M2_2lambda_family" "M3_3lambda_vellozia_clade" "M4_3lambda_avoidant_shift" "M5_4lambda_split_sisters"; do
    ltree="${MODELS[$model_name]}"
    mkdir -p "${OUT_BASE}/${model_name}"
    echo "======================================================================"
    echo " ETAPA 3: Modelo ${model_name} (${N_REPS} réplicas)"
    echo "======================================================================"
    for rep in $(seq 1 "${N_REPS}"); do
        REP_DIR="${OUT_BASE}/${model_name}/rep_${rep}"
        if [ -f "${REP_DIR}/Base_results.txt" ]; then
            echo "[INFO] ${model_name} - Réplica ${rep} já concluída. Pulando."
        else
            echo "[RUN] ${model_name} - Réplica ${rep}..."
            "${CAFE_BIN}" \
                -i "${INPUT_COUNTS}" \
                -t "${TREE_FILE}" \
                -y "${ltree}" \
                -p \
                -P 0.05 \
                -e"${SELECTED_ERR}" \
                -o "${REP_DIR}" \
                -c "${THREADS}" \
                -I "${ITERATIONS}" \
                > "${REP_DIR}.log" 2>&1
        fi
    done
done

echo "======================================================================"
echo " ETAPA 3B: Consolidando Avaliação Global de Modelos (AIC / LRT)"
echo "======================================================================"
python3 "${SCRIPT_DIR}/05_evaluate_cafe5_models.py"

echo "======================================================================"
echo " ETAPA 3 CONCLUÍDA COM SUCESSO!"
echo "======================================================================"

