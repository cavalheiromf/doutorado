#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
ANALYSIS_DIR="${ROOT_DIR}/pipelines/03_osca/03_synteny"
FILTERED_DIR="${ANALYSIS_DIR}/hyphy_validation_20260716/filtered_alignments"
OUTPUT_DIR="${ANALYSIS_DIR}/hyphy_validation_20260716/relax_gap_sensitivity"
HYPHY_BIN="${HYPHY_BIN:-$(which hyphy 2>/dev/null || echo hyphy)}"
THREADS="${THREADS:-4}"
STARTING_POINTS="${STARTING_POINTS:-10}"

declare -A TREES=(
    [global]="${ANALYSIS_DIR}/hyphy_analysis/vellozia_oscas_labeled.treefile"
    [osca1]="${ANALYSIS_DIR}/hyphy_subclades/osca1/osca1_labeled.treefile"
    [osca2]="${ANALYSIS_DIR}/hyphy_subclades/osca2/osca2_labeled.treefile"
    [osca3_4]="${ANALYSIS_DIR}/hyphy_subclades/osca3_4/osca3_4_labeled.treefile"
)

mkdir -p "${OUTPUT_DIR}/provenance"
"${HYPHY_BIN}" --version > "${OUTPUT_DIR}/provenance/hyphy_version.txt"
printf 'threads\t%s\nstarting_points\t%s\n' \
    "${THREADS}" "${STARTING_POINTS}" \
    > "${OUTPUT_DIR}/provenance/parameters.tsv"

for filter in gap20 gap50; do
    for dataset in global osca1 osca2 osca3_4; do
        alignment="${FILTERED_DIR}/${filter}/${dataset}/${dataset}_codon_gap_filtered.fasta"
        tree="${TREES[${dataset}]}"
        result_dir="${OUTPUT_DIR}/${filter}/${dataset}"
        mkdir -p "${result_dir}"

        if [[ -s "${result_dir}/relax_results.json" ]]; then
            echo "Existing result; skipping ${filter}/${dataset}"
            continue
        fi

        echo "[$(date --iso-8601=seconds)] Starting RELAX ${filter}/${dataset}"
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
            --output "${result_dir}/relax_results.json" \
            > "${result_dir}/relax.log" \
            2> "${result_dir}/relax.err"

        python -m json.tool "${result_dir}/relax_results.json" > /dev/null
        echo "[$(date --iso-8601=seconds)] Completed RELAX ${filter}/${dataset}"
    done
done

sha256sum "${FILTERED_DIR}"/gap*/{global,osca1,osca2,osca3_4}/*.fasta \
    > "${OUTPUT_DIR}/provenance/input_sha256.txt"
