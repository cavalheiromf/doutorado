#!/bin/bash
#SBATCH --job-name=rev_05_selection
#SBATCH --partition=short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=32G
#SBATCH --time=02:00:00
#SBATCH --output=logs/selection_job_%j.log

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="${BASE_DIR:-$(cd "${SCRIPT_DIR}/../../.." && pwd)}"
SCRIPTS_DIR="${SCRIPT_DIR}"
OUT_DIR="${BASE_DIR}/05_selection/pair_specific_run"

echo "=== START SELECTION PIPELINE: $(date) ==="
echo "Node: $(hostname)"
echo "Base directory: ${BASE_DIR}"
echo "Output directory: ${OUT_DIR}"

if [ -d "${OUT_DIR}" ]; then
    echo "Removing previous incomplete/test run at ${OUT_DIR}"
    rm -rf "${OUT_DIR}"
fi

echo "--- 1. Running pair_specific_kaks.py (16 threads) ---"
python3 "${SCRIPTS_DIR}/pair_specific_kaks.py" \
    --base-dir "${BASE_DIR}" \
    --output-dir "${OUT_DIR}" \
    --threads 16

echo "--- 2. Running verify_pair_specific_kaks.py ---"
python3 "${SCRIPTS_DIR}/verify_pair_specific_kaks.py" "${OUT_DIR}"

echo "--- 3. Running verify_orthofinder_pair_proteins.py ---"
python3 "${SCRIPTS_DIR}/verify_orthofinder_pair_proteins.py" "${OUT_DIR}"

echo "--- 4. Running report_pair_specific_kaks.py ---"
python3 "${SCRIPTS_DIR}/report_pair_specific_kaks.py" "${OUT_DIR}"

echo "=== SELECTION PIPELINE COMPLETED SUCCESSFULLY: $(date) ==="

