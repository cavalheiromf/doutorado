#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
A="${ROOT_DIR}/pipelines/03_osca/03_synteny"
I="${A}/hyphy_validation_20260716/filtered_alignments/gap20"
O="${A}/hyphy_codon_clade_rerun_20260717"
H="${HYPHY_BIN:-$(which hyphy 2>/dev/null || echo hyphy)}"
mkdir -p "${O}/provenance"
"${H}" --version > "${O}/provenance/hyphy_version.txt"
DATASETS=( ${DATASETS:-global osca1 osca2 osca3_4} )
for d in "${DATASETS[@]}"; do
  case "$d" in
    global) t="${A}/hyphy_analysis/vellozia_oscas_labeled.treefile";;
    osca1) t="${A}/hyphy_subclades/osca1/osca1_labeled.treefile";;
    osca2) t="${A}/hyphy_subclades/osca2/osca2_labeled.treefile";;
    osca3_4) t="${A}/hyphy_subclades/osca3_4/osca3_4_labeled.treefile";;
  esac
  x="${I}/${d}/${d}_codon_gap_filtered.fasta"
  mkdir -p "${O}/${d}"
  OMP_NUM_THREADS=4 "${H}" contrast-fel --alignment "$x" --tree "$t" \
    --code Universal --output "${O}/${d}/contrast_fel_results.json" \
    --branch-set Test --branch-set Reference \
    > "${O}/${d}/contrast_fel.log" 2> "${O}/${d}/contrast_fel.err"
  python3 -m json.tool "${O}/${d}/contrast_fel_results.json" >/dev/null
done
sha256sum "${I}"/*/*_codon_gap_filtered.fasta > "${O}/provenance/input_sha256.txt"
date --iso-8601=seconds > "${O}/provenance/contrast_fel_completed.txt"
