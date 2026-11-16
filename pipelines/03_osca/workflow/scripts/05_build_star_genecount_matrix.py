#!/usr/bin/env python3
"""Build a STAR GeneCounts matrix from reverse-stranded libraries."""

from __future__ import annotations

import argparse
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
SAMPLES = {
    "Vper": ["VP1C", "VP2C", "VP3C", "VP1F", "VP2F", "VP3F", "VP1R", "VP2R", "VP3R"],
    "Vtub": ["VT1C", "VT2C", "VT3C", "VT1F", "VT2F", "VT3F", "VT2R", "VT3R"],
}


def read_counts(path: Path, column: int) -> dict[str, int]:
    counts = {}
    for line in path.read_text().splitlines():
        if not line or line.startswith("N_") or line.startswith("MissingGeneID"):
            continue
        fields = line.split("\t")
        if len(fields) < column:
            raise ValueError(f"Malformed GeneCounts line in {path}: {line}")
        counts[fields[0]] = int(fields[column - 1])
    if not counts:
        raise ValueError(f"No gene rows found in {path}")
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--species", choices=tuple(SAMPLES), required=True)
    parser.add_argument("--column", type=int, default=4, help="ReadsPerGene column (1-based; default: antisense column 4)")
    args = parser.parse_args()

    alignment_root = PROJECT_ROOT / "analyses" / "05_rnaseq" / "results_genecounts" / "04_alignment" / args.species
    output_dir = PROJECT_ROOT / "analyses" / "05_rnaseq" / "results_genecounts" / "05_counts"
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / f"{args.species}_star_genecounts_col{args.column}.tsv"

    matrices = {}
    for sample in SAMPLES[args.species]:
        path = alignment_root / sample / f"{sample}_ReadsPerGene.out.tab"
        if not path.exists():
            raise SystemExit(f"Missing GeneCounts file: {path}")
        matrices[sample] = read_counts(path, args.column)

    gene_sets = {frozenset(counts) for counts in matrices.values()}
    if len(gene_sets) != 1:
        raise SystemExit("Gene ID sets differ across samples; matrix construction stopped")

    genes = sorted(next(iter(gene_sets)))
    with output.open("w") as handle:
        handle.write("gene_id\t" + "\t".join(SAMPLES[args.species]) + "\n")
        for gene in genes:
            handle.write(gene + "\t" + "\t".join(str(matrices[sample][gene]) for sample in SAMPLES[args.species]) + "\n")
    print(f"Matrix validation PASS: {len(genes)} genes x {len(SAMPLES[args.species])} samples -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
