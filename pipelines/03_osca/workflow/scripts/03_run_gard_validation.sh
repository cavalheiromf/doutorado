#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
ANALYSIS_DIR="${ROOT_DIR}/pipelines/03_osca/03_synteny"
OUTPUT_DIR="${ANALYSIS_DIR}/hyphy_validation_20260716/gard"
HYPHY_BIN="${HYPHY_BIN:-$(which hyphy 2>/dev/null || echo hyphy)}"
THREADS="${THREADS:-4}"
FORCE="${FORCE:-0}"

mkdir -p "${OUTPUT_DIR}"

if [[ ! -x "${HYPHY_BIN}" ]]; then
    echo "HyPhy executable not found or not executable: ${HYPHY_BIN}" >&2
    exit 1
fi

declare -A ALIGNMENTS=(
    [osca1]="${ANALYSIS_DIR}/hyphy_subclades/osca1/osca1_codon.fasta"
    [osca2]="${ANALYSIS_DIR}/hyphy_subclades/osca2/osca2_codon.fasta"
    [osca3_4]="${ANALYSIS_DIR}/hyphy_subclades/osca3_4/osca3_4_codon.fasta"
)

if (( $# == 0 )); then
    DATASETS=(osca1 osca2 osca3_4)
else
    DATASETS=("$@")
fi

"${HYPHY_BIN}" --version > "${OUTPUT_DIR}/hyphy_version.txt"
printf 'parameter\tvalue\n' > "${OUTPUT_DIR}/parameters.tsv"
printf 'data_type\tnucleotide\nrate_variation\tNone\nmaximum_breakpoints\t5\nmode\tFaster\nnumerical_error_tolerance\tTOLERATE_NUMERICAL_ERRORS=1\nthreads\t%s\n' \
    "${THREADS}" >> "${OUTPUT_DIR}/parameters.tsv"
sha256sum "${ALIGNMENTS[osca1]}" "${ALIGNMENTS[osca2]}" "${ALIGNMENTS[osca3_4]}" \
    > "${OUTPUT_DIR}/input_sha256.txt"

for dataset in "${DATASETS[@]}"; do
    if [[ -z "${ALIGNMENTS[${dataset}]+x}" ]]; then
        echo "Unknown dataset: ${dataset}. Choose osca1, osca2, or osca3_4." >&2
        exit 2
    fi

    alignment="${ALIGNMENTS[${dataset}]}"
    if [[ ! -s "${alignment}" ]]; then
        echo "Missing or empty alignment: ${alignment}" >&2
        exit 3
    fi

    dataset_dir="${OUTPUT_DIR}/${dataset}"
    mkdir -p "${dataset_dir}"

    lock_dir="${dataset_dir}/.run.lock"
    if ! mkdir "${lock_dir}" 2>/dev/null; then
        echo "Another GARD run holds the lock for ${dataset}: ${lock_dir}" >&2
        exit 4
    fi
    trap 'rmdir "${lock_dir}" 2>/dev/null || true' EXIT

    if [[ -s "${dataset_dir}/gard.json" && "${FORCE}" != 1 ]]; then
        echo "Existing GARD JSON for ${dataset}; refusing to overwrite or resume." >&2
        echo "Archive it first, or set FORCE=1 to restart this generated result." >&2
        exit 5
    fi
    if [[ "${FORCE}" == 1 ]]; then
        rm -f \
            "${dataset_dir}/gard.json" \
            "${dataset_dir}/gard.best-gard" \
            "${dataset_dir}/gard.best-gard.fit.bf" \
            "${dataset_dir}/gard.stdout.log" \
            "${dataset_dir}/gard.stderr.log"
    fi

    echo "Running GARD for ${dataset} with ${THREADS} threads"
    # HyPhy 2.5.99 can abort GARD on cache differences around 1e-6 in these
    # gappy alignments. This documented HyPhy switch converts that numerical
    # consistency check to a warning; biological/model errors still fail.
    OMP_NUM_THREADS="${THREADS}" "${HYPHY_BIN}" \
        'ENV=TOLERATE_NUMERICAL_ERRORS=1;' gard \
        --alignment "${alignment}" \
        --type nucleotide \
        --rv None \
        --max-breakpoints 5 \
        --mode Faster \
        --output "${dataset_dir}/gard.json" \
        --output-lf "${dataset_dir}/gard.best-gard" \
        > "${dataset_dir}/gard.stdout.log" \
        2> "${dataset_dir}/gard.stderr.log"

    python -m json.tool "${dataset_dir}/gard.json" > /dev/null
    echo "Completed GARD for ${dataset}"
    rmdir "${lock_dir}"
    trap - EXIT
done
