#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
ANALYSIS_DIR="${ROOT_DIR}/analyses/03_synteny"
RUN_ID="${HYPHY_RUN_ID:-20260716}"
OUT_DIR="${ANALYSIS_DIR}/hyphy_rerun_${RUN_ID}"
HYPHY_BIN="${HYPHY_BIN:-/home/mfcaval/.local/share/mamba/envs/jcviEnv/bin/hyphy}"
PYTHON_BIN="${PYTHON_BIN:-python}"
THREADS="${HYPHY_THREADS:-8}"

if [[ ! -x "${HYPHY_BIN}" ]]; then
    echo "HyPhy executable not found or not executable: ${HYPHY_BIN}" >&2
    exit 1
fi

mkdir -p "${OUT_DIR}/provenance"

"${HYPHY_BIN}" --version > "${OUT_DIR}/provenance/hyphy_version.txt"
date --iso-8601=seconds > "${OUT_DIR}/provenance/run_started.txt"

sha256sum \
    "${ANALYSIS_DIR}/hyphy_analysis/vellozia_oscas_codon.fasta" \
    "${ANALYSIS_DIR}/hyphy_analysis/vellozia_oscas_labeled.treefile" \
    "${ANALYSIS_DIR}/hyphy_subclades/osca1/osca1_codon.fasta" \
    "${ANALYSIS_DIR}/hyphy_subclades/osca1/osca1_labeled.treefile" \
    "${ANALYSIS_DIR}/hyphy_subclades/osca2/osca2_codon.fasta" \
    "${ANALYSIS_DIR}/hyphy_subclades/osca2/osca2_labeled.treefile" \
    "${ANALYSIS_DIR}/hyphy_subclades/osca3_4/osca3_4_codon.fasta" \
    "${ANALYSIS_DIR}/hyphy_subclades/osca3_4/osca3_4_labeled.treefile" \
    > "${OUT_DIR}/provenance/input_sha256.txt"

validate_json() {
    local json_path="$1"
    "${PYTHON_BIN}" -c 'import json, sys; json.load(open(sys.argv[1]))' "${json_path}"
}

run_dataset() {
    local name="$1"
    local alignment="$2"
    local tree="$3"
    local dataset_out="${OUT_DIR}/${name}"

    mkdir -p "${dataset_out}"
    echo "[$(date --iso-8601=seconds)] Starting ${name} RELAX"

    OMP_NUM_THREADS="${THREADS}" "${HYPHY_BIN}" relax \
        --alignment "${alignment}" \
        --tree "${tree}" \
        --code Universal \
        --mode "Classic mode" \
        --test Test \
        --reference Reference \
        --grid-size 250 \
        --starting-points 1 \
        --multiple-hits None \
        --rates 3 \
        --models All \
        --srv No \
        --intermediate-fits /dev/null \
        --kill-zero-lengths Yes \
        --save-fit /dev/null \
        --output "${dataset_out}/relax_results.json" \
        > "${dataset_out}/relax.log" \
        2> "${dataset_out}/relax.err"

    validate_json "${dataset_out}/relax_results.json"
    echo "[$(date --iso-8601=seconds)] Completed ${name} RELAX"
    echo "[$(date --iso-8601=seconds)] Starting ${name} Contrast-FEL"

    OMP_NUM_THREADS="${THREADS}" "${HYPHY_BIN}" contrast-fel \
        --alignment "${alignment}" \
        --tree "${tree}" \
        --code Universal \
        --branch-set Test \
        --branch-set Reference \
        --srv Yes \
        --permutations Yes \
        --p-value 0.05 \
        --q-value 0.20 \
        --limit-to-sites null \
        --save-lf-for-sites null \
        --intermediate-fits /dev/null \
        --kill-zero-lengths Yes \
        --output "${dataset_out}/contrast_fel_results.json" \
        > "${dataset_out}/contrast_fel.log" \
        2> "${dataset_out}/contrast_fel.err"

    validate_json "${dataset_out}/contrast_fel_results.json"
    echo "[$(date --iso-8601=seconds)] Completed ${name} Contrast-FEL"
}

run_dataset \
    global \
    "${ANALYSIS_DIR}/hyphy_analysis/vellozia_oscas_codon.fasta" \
    "${ANALYSIS_DIR}/hyphy_analysis/vellozia_oscas_labeled.treefile"

run_dataset \
    osca1 \
    "${ANALYSIS_DIR}/hyphy_subclades/osca1/osca1_codon.fasta" \
    "${ANALYSIS_DIR}/hyphy_subclades/osca1/osca1_labeled.treefile"

run_dataset \
    osca2 \
    "${ANALYSIS_DIR}/hyphy_subclades/osca2/osca2_codon.fasta" \
    "${ANALYSIS_DIR}/hyphy_subclades/osca2/osca2_labeled.treefile"

run_dataset \
    osca3_4 \
    "${ANALYSIS_DIR}/hyphy_subclades/osca3_4/osca3_4_codon.fasta" \
    "${ANALYSIS_DIR}/hyphy_subclades/osca3_4/osca3_4_labeled.treefile"

date --iso-8601=seconds > "${OUT_DIR}/provenance/run_completed.txt"
echo "All HyPhy datasets completed successfully: ${OUT_DIR}"
