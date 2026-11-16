#!/bin/bash
set -e

# Base directories
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="${BASE_DIR:-$(cd "${SCRIPT_DIR}/../../.." && pwd)}"
ORTHO_SEQ_DIR="$BASE_DIR/01_orthology/results/Results_Aug30/Orthogroup_Sequences"
OUT_DIR="$BASE_DIR/04_gene_families/priority_gene_trees"

mkdir -p "$OUT_DIR"

# Priority families
FAMILIES=("OG0000306" "OG0000301" "OG0000317" "OG0000332" "OG0000281")

# Load modules
module load Bio/MAFFT/7.526
module load Bio/IQ-TREE/2.4.0

echo "Starting Orthology Validation via Gene Trees for Priority Families..."

for FAM in "${FAMILIES[@]}"; do
    echo "Processing $FAM..."
    
    FASTA_IN="$ORTHO_SEQ_DIR/${FAM}.fa"
    ALN_OUT="$OUT_DIR/${FAM}_aligned.fasta"
    
    if [ ! -f "$FASTA_IN" ]; then
        echo "Error: Sequence file for $FAM not found at $FASTA_IN"
        continue
    fi
    
    # 1. Alignment with MAFFT (auto mode for best strategy)
    if [ ! -f "$ALN_OUT" ]; then
        echo "  Running MAFFT..."
        mafft --auto --thread 4 "$FASTA_IN" > "$ALN_OUT"
    else
        echo "  Alignment already exists for $FAM, skipping MAFFT."
    fi
    
    # 2. Tree inference with IQ-TREE (ModelFinder + UFBoot 1000)
    # Using -T AUTO for threads, -B 1000 for ultrafast bootstrap
    TREE_OUT="$OUT_DIR/${FAM}.treefile"
    if [ ! -f "$TREE_OUT" ]; then
        echo "  Running IQ-TREE..."
        iqtree2 -s "$ALN_OUT" -m TEST -B 1000 -T AUTO --prefix "$OUT_DIR/$FAM"
    else
        echo "  Tree already exists for $FAM, skipping IQ-TREE."
    fi
    
    echo "$FAM completed!"
done

echo "All priority gene trees generated successfully in $OUT_DIR."
