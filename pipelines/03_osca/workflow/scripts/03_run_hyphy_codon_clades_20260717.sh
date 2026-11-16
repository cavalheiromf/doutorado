#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
ANALYSIS_DIR="${ROOT_DIR}/pipelines/03_osca/03_synteny"
ALIGN_DIR="${ANALYSIS_DIR}/hyphy_validation_20260716/filtered_alignments/gap20"
OUT_DIR="${ANALYSIS_DIR}/hyphy_codon_clade_rerun_20260717"
HYPHY_BIN="${HYPHY_BIN:-$(which hyphy 2>/dev/null || echo hyphy)}"
THREADS="${THREADS:-4}"
STARTING_POINTS="${STARTING_POINTS:-10}"

declare -A TREES=(
  [global]="${ANALYSIS_DIR}/hyphy_analysis/vellozia_oscas_labeled.treefile"
  [osca1]="${ANALYSIS_DIR}/hyphy_subclades/osca1/osca1_labeled.treefile"
  [osca2]="${ANALYSIS_DIR}/hyphy_subclades/osca2/osca2_labeled.treefile"
  [osca3_4]="${ANALYSIS_DIR}/hyphy_subclades/osca3_4/osca3_4_labeled.treefile"
)

mkdir -p "${OUT_DIR}/provenance"
"${HYPHY_BIN}" --version > "${OUT_DIR}/provenance/hyphy_version.txt"
printf 'parameter\tvalue\nfilter\tgap20\nthreads\t%s\nstarting_points\t%s\nmodels\tMG94xREV\n' \
  "${THREADS}" "${STARTING_POINTS}" > "${OUT_DIR}/provenance/parameters.tsv"

for dataset in global osca1 osca2 osca3_4; do
  alignment="${ALIGN_DIR}/${dataset}/${dataset}_codon_gap_filtered.fasta"
  tree="${TREES[${dataset}]}"
  result_dir="${OUT_DIR}/${dataset}"
  mkdir -p "${result_dir}"
  test -s "${alignment}"
  test -s "${tree}"

  OMP_NUM_THREADS="${THREADS}" "${HYPHY_BIN}" relax \
    --alignment "${alignment}" --tree "${tree}" --code Universal \
    --mode "Classic mode" --test Test --reference Reference \
    --grid-size 250 --starting-points "${STARTING_POINTS}" \
    --multiple-hits None --rates 3 --models All --srv No \
    --intermediate-fits /dev/null --kill-zero-lengths Yes \
    --save-fit /dev/null --output "${result_dir}/relax_results.json" \
    > "${result_dir}/relax.log" 2> "${result_dir}/relax.err"

  OMP_NUM_THREADS="${THREADS}" "${HYPHY_BIN}" contrast-fel \
    --alignment "${alignment}" --tree "${tree}" --code Universal \
    --output "${result_dir}/contrast_fel_results.json" \
    --branch-set Test --branch-set Reference \
    > "${result_dir}/contrast_fel.log" 2> "${result_dir}/contrast_fel.err"

  python3 -m json.tool "${result_dir}/relax_results.json" > /dev/null
  python3 -m json.tool "${result_dir}/contrast_fel_results.json" > /dev/null
done

sha256sum "${ALIGN_DIR}"/*/*_codon_gap_filtered.fasta > "${OUT_DIR}/provenance/input_sha256.txt"
sha256sum "${TREES[@]}" > "${OUT_DIR}/provenance/tree_sha256.txt"
date --iso-8601=seconds > "${OUT_DIR}/provenance/run_completed.txt"
