#!/bin/bash
#SBATCH -p short
#SBATCH -N 1
#SBATCH -n 32
#SBATCH --mem=32G
#SBATCH -t 04:00:00
#SBATCH -J trio_codeml
#SBATCH -o logs/slurm_trio_codeml_%j.log
#SBATCH -e logs/slurm_trio_codeml_%j.err

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MACRO_DIR="$(cd "${SCRIPT_DIR}/../../.." && pwd)"
OUTPUT_DIR="${MACRO_DIR}/05_selection/trio_outgroup_run"
mkdir -p "$OUTPUT_DIR"

PYTHON="${PYTHON:-python3}"
SCRIPT="${SCRIPT_DIR}/run_trio_branch_selection.py"

$PYTHON "$SCRIPT" \
  --output-dir "$OUTPUT_DIR" \
  --threads 32 \
  --batch-size 250

echo "=========================================================="
echo "Analysis completed successfully at: $(date)"
echo "=========================================================="

