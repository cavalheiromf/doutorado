#!/usr/bin/env bash
#SBATCH --job-name=osca_hyphy_codon
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=24:00:00
#SBATCH --output=logs/hyphy_%x_%A_%a.out
#SBATCH --error=logs/hyphy_%x_%A_%a.err
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
A=${ROOT}/pipelines/04_osca/03_synteny
I=${A}/hyphy_validation_20260716/filtered_alignments/gap20
O=${A}/hyphy_codon_clade_slurm_20260717
H="${HYPHY_BIN:-$(which hyphy 2>/dev/null || echo hyphy)}"

case "${SLURM_ARRAY_TASK_ID}" in
  0) D=global; M=relax; T=${A}/hyphy_analysis/vellozia_oscas_labeled.treefile;;
  1) D=global; M=contrast_fel; T=${A}/hyphy_analysis/vellozia_oscas_labeled.treefile;;
  2) D=osca1; M=relax; T=${A}/hyphy_subclades/osca1/osca1_labeled.treefile;;
  3) D=osca1; M=contrast_fel; T=${A}/hyphy_subclades/osca1/osca1_labeled.treefile;;
  4) D=osca2; M=relax; T=${A}/hyphy_subclades/osca2/osca2_labeled.treefile;;
  5) D=osca2; M=contrast_fel; T=${A}/hyphy_subclades/osca2/osca2_labeled.treefile;;
  6) D=osca3_4; M=relax; T=${A}/hyphy_subclades/osca3_4/osca3_4_labeled.treefile;;
  7) D=osca3_4; M=contrast_fel; T=${A}/hyphy_subclades/osca3_4/osca3_4_labeled.treefile;;
  *) echo "unknown array index" >&2; exit 2;;
esac

X=${I}/${D}/${D}_codon_gap_filtered.fasta
R=${O}/${D}/${M}
mkdir -p "${R}"
"${H}" --version > "${O}/hyphy_version.txt"
if [[ "${M}" == relax ]]; then
  OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-4} "${H}" relax \
    --alignment "${X}" --tree "${T}" --code Universal \
    --mode "Classic mode" --test Test --reference Reference \
    --grid-size 250 --starting-points 1 --multiple-hits None --rates 3 \
    --models All --srv No --intermediate-fits /dev/null \
    --kill-zero-lengths Yes --save-fit /dev/null \
    --output "${R}/results.json" > "${R}/run.log" 2> "${R}/run.err"
else
  OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-4} "${H}" contrast-fel \
    --alignment "${X}" --tree "${T}" --code Universal \
    --output "${R}/results.json" --branch-set Test --branch-set Reference \
    > "${R}/run.log" 2> "${R}/run.err"
fi
python3 -m json.tool "${R}/results.json" > /dev/null
sha256sum "${X}" "${T}" > "${R}/input_sha256.txt"
