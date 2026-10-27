#!/bin/bash
#SBATCH --job-name=cafe5_rev_s1
#SBATCH --output=/home/mfcaval/github/doutorado/chapter_macroevolution_review/04_gene_families/cafe5/logs/cafe5_stage1_%j.log
#SBATCH --error=/home/mfcaval/github/doutorado/chapter_macroevolution_review/04_gene_families/cafe5/logs/cafe5_stage1_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --partition=short
#SBATCH --time=12:00:00
#SBATCH --reservation=teste

# ==============================================================================
# 02_run_cafe5_stage1_error_model.slurm
#
# Etapa 1 do protocolo CAFE5 (6 monocotiledôneas):
#   - Garante que os insumos de 6 táxons existam (rodando 01_prepare_6taxa_inputs.py se necessário)
#   - 5 réplicas do Modelo Base (1-lambda, distribuição de Poisson na raiz -p, sem modelo de erro)
#   - 5 réplicas do Modelo Base + Error Model (-e, estimando erro global de anotação/montagem)
#   - Seleciona automaticamente a réplica de maior verossimilhança (menor -lnL)
#     e copia o arquivo Base_error_model.txt ótimo para selected_error_model.txt.
# ==============================================================================

set -euo pipefail

BASE_DIR="/home/mfcaval/github/doutorado/chapter_macroevolution_review"
SCRIPT_DIR="${BASE_DIR}/workflow/scripts/01_cafe5"
CAFE_BIN="/home/mfcaval/.local/share/mamba/envs/cafe5_env/bin/cafe5"
INPUT_COUNTS="${BASE_DIR}/04_gene_families/cafe5/input/cafe_family_input_6taxa.tsv"
TREE_FILE="${BASE_DIR}/03_dating/final_trees/velloziaceae_6taxa_ultrametric.tre"
OUT_BASE="${BASE_DIR}/04_gene_families/cafe5/runs/stage1_error_calibration"

THREADS="${SLURM_CPUS_PER_TASK:-8}"
N_REPS="${N_REPS:-5}"
ITERATIONS="${ITERATIONS:-500}"

# 0. Garantir que os insumos de 6 táxons estejam gerados
if [ ! -f "${INPUT_COUNTS}" ] || [ ! -f "${TREE_FILE}" ]; then
    echo "[INFO] Gerando insumos de 6 táxons..."
    python3 "${SCRIPT_DIR}/01_prepare_6taxa_inputs.py"
fi

# Sanity check: remover espaços em branco na árvore
tr -d '[:blank:]' < "${TREE_FILE}" > "${TREE_FILE}.clean" && mv "${TREE_FILE}.clean" "${TREE_FILE}"

mkdir -p "${OUT_BASE}/base_no_err" "${OUT_BASE}/base_with_err"

echo "======================================================================"
echo " ETAPA 1A: Base 1-lambda SEM Modelo de Erro (${N_REPS} réplicas)"
echo "======================================================================"
for rep in $(seq 1 "${N_REPS}"); do
    REP_DIR="${OUT_BASE}/base_no_err/rep_${rep}"
    if [ -f "${REP_DIR}/Base_results.txt" ]; then
        echo "[INFO] Base sem erro - Réplica ${rep} já concluída. Pulando."
    else
        echo "[RUN] Base sem erro - Réplica ${rep}..."
        "${CAFE_BIN}" \
            -i "${INPUT_COUNTS}" \
            -t "${TREE_FILE}" \
            -p \
            -P 0.05 \
            -o "${REP_DIR}" \
            -c "${THREADS}" \
            -I "${ITERATIONS}" \
            > "${REP_DIR}.log" 2>&1
    fi
done

echo "======================================================================"
echo " ETAPA 1B: Base 1-lambda COM Modelo de Erro -e (${N_REPS} réplicas)"
echo "======================================================================"
for rep in $(seq 1 "${N_REPS}"); do
    REP_DIR="${OUT_BASE}/base_with_err/rep_${rep}"
    if [ -f "${REP_DIR}/Base_error_model.txt" ] && [ -f "${REP_DIR}/Base_results.txt" ]; then
        echo "[INFO] Base com erro (-e) - Réplica ${rep} já concluída. Pulando."
    else
        echo "[RUN] Base com erro (-e) - Réplica ${rep}..."
        "${CAFE_BIN}" \
            -i "${INPUT_COUNTS}" \
            -t "${TREE_FILE}" \
            -p \
            -P 0.05 \
            -e \
            -o "${REP_DIR}" \
            -c "${THREADS}" \
            -I "${ITERATIONS}" \
            > "${REP_DIR}.log" 2>&1
    fi
done

echo "======================================================================"
echo " ETAPA 1C: Selecionando o Melhor Modelo de Erro"
echo "======================================================================"
python3 "${SCRIPT_DIR}/05_evaluate_cafe5_models.py" --stage 1

echo "======================================================================"
echo " ETAPA 1 CONCLUÍDA COM SUCESSO!"
echo "======================================================================"

