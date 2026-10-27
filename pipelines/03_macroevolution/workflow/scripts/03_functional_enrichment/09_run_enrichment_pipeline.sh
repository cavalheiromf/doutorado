#!/usr/bin/env bash
#SBATCH --job-name=func_enrich_6taxa
#SBATCH --partition=short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=02:00:00
#SBATCH --output=/home/mfcaval/github/doutorado/chapter_macroevolution_review/04_gene_families/functional_enrichment/logs/slurm_enrichment_%j.out
#SBATCH --error=/home/mfcaval/github/doutorado/chapter_macroevolution_review/04_gene_families/functional_enrichment/logs/slurm_enrichment_%j.err

set -euo pipefail

MACRO_DIR="/home/mfcaval/github/doutorado/chapter_macroevolution_review"
SCRIPT_DIR="${MACRO_DIR}/workflow/scripts/03_functional_enrichment"
BASE_DIR="${MACRO_DIR}/04_gene_families/functional_enrichment"
MASTER_TABLE="${MACRO_DIR}/04_gene_families/comparative_axes/comparative_families_master_table_v2.tsv"

mkdir -p "${BASE_DIR}/results" "${BASE_DIR}/intermediate" "${BASE_DIR}/logs"

export FAMILY_MACRO_DIR="${MACRO_DIR}"
export FAMILY_ENRICHMENT_DIR="${BASE_DIR}"
export FAMILY_MASTER_TABLE="${MASTER_TABLE}"

echo "[*] Generating provenance run_manifest.json..."
python3 - <<'PY'
import hashlib, json, os
from pathlib import Path

macro = Path(os.environ["FAMILY_MACRO_DIR"]).resolve()
base = Path(os.environ["FAMILY_ENRICHMENT_DIR"]).resolve()
master = Path(os.environ["FAMILY_MASTER_TABLE"]).resolve()
script_dir = macro / "workflow/scripts/03_functional_enrichment"

def inventory(root):
    return [
        {
            "path": str(path.relative_to(root)),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "bytes": path.stat().st_size,
        }
        for path in sorted(root.rglob("*"))
        if path.is_file()
    ]

external = [
    macro / "00_data/cds_outgroups/Ath.cds.fa",
    macro / "01_orthology/results/Results_Aug30/Orthogroups/Orthogroups.tsv",
]
assets = [
    {
        "path": str(path.resolve()),
        "availability": "available" if path.is_file() else "missing",
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None,
    }
    for path in external
]
scripts = [
    {
        "path": str(path.resolve()),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }
    for path in sorted(script_dir.glob("0[1-7]_*.py"))
    if path.is_file()
]

manifest = {
    "inputs": inventory(base / "input"),
    "master_sha256": hashlib.sha256(master.read_bytes()).hexdigest(),
    "external_assets": assets,
    "scripts": scripts,
}
(base / "run_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
print("    Saved:", base / "run_manifest.json")
PY

for stage in \
    01_build_family_annotations \
    02_build_binary_term_matrix \
    03_run_enrichment \
    04_run_stratified_permutations \
    05_reduce_go_redundancy \
    06_generate_summary_report \
    07_validate_outputs; do
    echo "=================================================================="
    echo "[*] Running stage: ${stage}.py"
    echo "=================================================================="
    python3 "${SCRIPT_DIR}/${stage}.py" 2>&1 | tee "${BASE_DIR}/logs/${stage}.log"
done

printf 'Validated 6-taxa enrichment run completed successfully.\n' > "${BASE_DIR}/SUCCESS"
echo "[*] Pipeline finished successfully: ${BASE_DIR}"
