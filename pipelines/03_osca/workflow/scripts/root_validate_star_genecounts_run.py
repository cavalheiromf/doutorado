#!/usr/bin/env python3
"""Validate the completed STAR GeneCounts rerun and downstream outputs."""

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
STAR = ROOT / "analyses" / "05_rnaseq" / "results_genecounts"
EXPR = ROOT / "analyses" / "06_expression" / "results_genecounts"
QC = STAR / "06_qc" / "trimmed"
SAMPLES = {
    "Vper": ["VP1C", "VP2C", "VP3C", "VP1F", "VP2F", "VP3F", "VP1R", "VP2R", "VP3R"],
    "Vtub": ["VT1C", "VT2C", "VT3C", "VT1F", "VT2F", "VT3F", "VT2R", "VT3R"],
}


def check(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")
    print(f"PASS: {message}")


def main() -> int:
    for species, samples in SAMPLES.items():
        files = []
        for sample in samples:
            path = STAR / "04_alignment" / species / sample / f"{sample}_ReadsPerGene.out.tab"
            check(path.exists(), f"GeneCounts presente: {species}/{sample}")
            gene_rows = [line for line in path.read_text().splitlines() if line and not line.startswith("N_") and not line.startswith("MissingGeneID")]
            check(len(gene_rows) > 1000, f"GeneCounts contém linhas gênicas: {species}/{sample}")
            files.append(path)
        matrix = STAR / "05_counts" / f"{species}_star_genecounts_col4.tsv"
        check(matrix.exists(), f"matriz STAR presente: {species}")
        with matrix.open() as handle:
            header = next(csv.reader(handle, delimiter="\t"))
            rows = sum(1 for _ in handle)
        check(header[1:] == samples, f"ordem de amostras validada: {species}")
        check(rows > 1000, f"matriz contém genes: {species}")

    check(not (STAR / "04_alignment" / "Vtub" / "VT1R").exists(), "VT1R ausente do alinhamento principal")
    for species in SAMPLES:
        for contrast in ("Root_vs_Leaf", "Root_vs_Stem", "Stem_vs_Leaf"):
            check((EXPR / f"{species}_DE_{contrast}.csv").exists(), f"DESeq2 presente: {species} {contrast}")
    check((QC / "trimmed_multiqc.html").exists(), "MultiQC pós-trimming presente")
    print("STAR GeneCounts validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
