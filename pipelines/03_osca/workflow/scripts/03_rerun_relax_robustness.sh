#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
ANALYSIS_DIR="${ROOT_DIR}/pipelines/03_osca/03_synteny"
RUN_ID="${HYPHY_RUN_ID:-20260716}"
OUT_DIR="${ANALYSIS_DIR}/hyphy_rerun_${RUN_ID}/robustness"
HYPHY_BIN="${HYPHY_BIN:-$(which hyphy 2>/dev/null || echo hyphy)}"
PYTHON_BIN="${PYTHON_BIN:-python}"
THREADS="${HYPHY_THREADS_PER_JOB:-4}"
STARTING_POINTS="${HYPHY_STARTING_POINTS:-10}"

if [[ ! -x "${HYPHY_BIN}" ]]; then
    echo "HyPhy executable not found or not executable: ${HYPHY_BIN}" >&2
    exit 1
fi

mkdir -p "${OUT_DIR}/provenance"
"${HYPHY_BIN}" --version > "${OUT_DIR}/provenance/hyphy_version.txt"
date --iso-8601=seconds > "${OUT_DIR}/provenance/run_started_sp${STARTING_POINTS}.txt"
printf 'threads_per_job\t%s\nstarting_points\t%s\n' \
    "${THREADS}" "${STARTING_POINTS}" \
    > "${OUT_DIR}/provenance/parameters_sp${STARTING_POINTS}.tsv"

validate_json() {
    local json_path="$1"
    "${PYTHON_BIN}" -c 'import json, sys; json.load(open(sys.argv[1]))' "${json_path}"
}

run_relax() {
    local name="$1"
    local alignment="$2"
    local tree="$3"
    local dataset_out="${OUT_DIR}/${name}_sp${STARTING_POINTS}"

    mkdir -p "${dataset_out}"
    echo "[$(date --iso-8601=seconds)] Starting robust RELAX: ${name}"

    OMP_NUM_THREADS="${THREADS}" "${HYPHY_BIN}" relax \
        --alignment "${alignment}" \
        --tree "${tree}" \
        --code Universal \
        --mode "Classic mode" \
        --test Test \
        --reference Reference \
        --grid-size 250 \
        --starting-points "${STARTING_POINTS}" \
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
    echo "[$(date --iso-8601=seconds)] Completed robust RELAX: ${name}"
}

run_relax \
    osca2 \
    "${ANALYSIS_DIR}/hyphy_subclades/osca2/osca2_codon.fasta" \
    "${ANALYSIS_DIR}/hyphy_subclades/osca2/osca2_labeled.treefile" &
osca2_pid=$!

run_relax \
    osca3_4 \
    "${ANALYSIS_DIR}/hyphy_subclades/osca3_4/osca3_4_codon.fasta" \
    "${ANALYSIS_DIR}/hyphy_subclades/osca3_4/osca3_4_labeled.treefile" &
osca3_4_pid=$!

wait "${osca2_pid}"
wait "${osca3_4_pid}"

date --iso-8601=seconds > "${OUT_DIR}/provenance/run_completed_sp${STARTING_POINTS}.txt"
echo "RELAX robustness analyses completed successfully: ${OUT_DIR}"
