#!/bin/bash
#SBATCH -p short
#SBATCH -N 1
#SBATCH -n 32
#SBATCH --mem=32G
#SBATCH -t 04:00:00
#SBATCH -J trio_codeml
#SBATCH -o /home/mfcaval/github/doutorado/chapter_macroevolution_review/05_selection/trio_outgroup_run/slurm_trio_codeml_%j.log
#SBATCH -e /home/mfcaval/github/doutorado/chapter_macroevolution_review/05_selection/trio_outgroup_run/slurm_trio_codeml_%j.err

set -euo pipefail

echo "=========================================================="
echo "Starting 3-way codeml selection analysis on Slurm"
echo "Job ID: $SLURM_JOB_ID"
echo "Node: $SLURMD_NODENAME"
echo "Cores allocated: 32"
echo "Start time: $(date)"
echo "=========================================================="

OUTPUT_DIR="/home/mfcaval/github/doutorado/chapter_macroevolution_review/05_selection/trio_outgroup_run"
mkdir -p "$OUTPUT_DIR"

PYTHON="/home/mfcaval/miniforge3/bin/python3"
SCRIPT="/home/mfcaval/github/doutorado/chapter_macroevolution_review/workflow/scripts/05_selection/run_trio_branch_selection.py"

$PYTHON "$SCRIPT" \
  --output-dir "$OUTPUT_DIR" \
  --threads 32 \
  --batch-size 250

echo "=========================================================="
echo "Analysis completed successfully at: $(date)"
echo "=========================================================="

