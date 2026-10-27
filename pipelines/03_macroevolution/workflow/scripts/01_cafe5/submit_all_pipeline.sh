#!/bin/bash
set -euo pipefail

SCRIPT_DIR="/home/mfcaval/github/doutorado/chapter_macroevolution_review/workflow/scripts"

JOB1="846260"
echo "[INFO] Etapa 1 já está em execução no SLURM (Job ID: ${JOB1})"

# Submeter Etapa 2 e Etapa 3 dependendo do término bem-sucedido da Etapa 1 (afterok)
JOB2=$(sbatch --dependency=afterok:${JOB1} "${SCRIPT_DIR}/03_run_cafe5_stage2_gamma_models.slurm" | awk '{print $4}')
echo "[INFO] Etapa 2 (Gamma) submetida com dependência de Job ${JOB1} -> Job ID: ${JOB2}"

JOB3=$(sbatch --dependency=afterok:${JOB1} "${SCRIPT_DIR}/04_run_cafe5_stage3_branch_lambdas.slurm" | awk '{print $4}')
echo "[INFO] Etapa 3 (Branch Lambdas) submetida com dependência de Job ${JOB1} -> Job ID: ${JOB3}"

echo "[INFO] Pipeline encadeado no SLURM com sucesso!"
