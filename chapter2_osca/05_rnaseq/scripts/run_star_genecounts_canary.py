#!/usr/bin/env python3
"""Run and validate one STAR GeneCounts canary alignment.

The canary writes to a dedicated results tree and never overwrites the
historical featureCounts/STAR outputs.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
RESULTS_ROOT = PROJECT_ROOT / "analyses" / "05_rnaseq" / "results_genecounts"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--species", choices=("Vper", "Vtub"), help="Species for reads and index")
    parser.add_argument("--reads-species", choices=("Vper", "Vtub"))
    parser.add_argument("--index-species", choices=("Vper", "Vtub"))
    parser.add_argument("--sample", required=True, help="Canary sample, e.g. VP1C")
    parser.add_argument("--threads", type=int, default=16)
    parser.add_argument("--star", default="STAR")
    parser.add_argument("--input-stage", choices=("trimmed", "raw"), default="trimmed")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    reads_species = args.reads_species or args.species
    index_species = args.index_species or args.species
    if not reads_species or not index_species:
        raise SystemExit("Provide --species or both --reads-species and --index-species")
    if args.input_stage == "raw":
        input_dir = PROJECT_ROOT / "data" / "rnaseq" / reads_species
        r1_files = sorted(input_dir.glob(f"{args.sample}_*_R1_*.fastq.gz"))
        r2_files = sorted(input_dir.glob(f"{args.sample}_*_R2_*.fastq.gz"))
    else:
        input_dir = PROJECT_ROOT / "analyses" / "05_rnaseq" / "results" / "02_trimmed" / reads_species
        r1_files = [input_dir / f"{args.sample}_trimmed_R1.fastq.gz"]
        r2_files = [input_dir / f"{args.sample}_trimmed_R2.fastq.gz"]
    index = RESULTS_ROOT / "03_star_index" / index_species
    if args.reads_species or args.index_species:
        output_label = f"{args.sample}_against_{index_species}"
        output = RESULTS_ROOT / "cross_mapping" / reads_species / output_label
    else:
        output = RESULTS_ROOT / "04_alignment" / reads_species / args.sample
    if args.input_stage == "raw" and not args.dry_run:
        output = RESULTS_ROOT / "raw_input" / reads_species / args.sample
    r1 = r1_files
    r2 = r2_files
    prefix = output / f"{args.sample}_"
    counts = output / f"{args.sample}_ReadsPerGene.out.tab"

    missing = [str(path) for path in (index / "Genome", *r1, *r2) if not path.exists()]
    if missing:
        raise SystemExit("Missing canary input(s): " + ", ".join(missing))

    output.mkdir(parents=True, exist_ok=True)
    if args.input_stage == "raw":
        merged = []
        for mate, files in (("R1", r1), ("R2", r2)):
            merged_path = output / f"{args.sample}_raw_merged_{mate}.fastq.gz"
            partial_path = merged_path.with_suffix(merged_path.suffix + ".partial")
            if not merged_path.exists():
                with partial_path.open("wb") as destination:
                    for source in files:
                        with source.open("rb") as handle:
                            shutil.copyfileobj(handle, destination)
                partial_path.replace(merged_path)
            merged.append(merged_path)
        r1, r2 = [merged[0]], [merged[1]]
    command = [
        args.star,
        "--genomeDir", str(index),
        "--readFilesIn", *[str(path) for path in r1], *[str(path) for path in r2],
        "--readFilesCommand", "zcat",
        "--outFileNamePrefix", str(prefix),
        "--outSAMtype", "BAM", "SortedByCoordinate",
        "--quantMode", "GeneCounts",
        "--runThreadN", str(args.threads),
    ]
    print("Canary command:")
    print(" ".join(command))
    if args.dry_run:
        return 0

    subprocess.run(command, check=True)
    if not counts.exists():
        raise SystemExit(f"STAR finished without {counts}")

    lines = [line for line in counts.read_text().splitlines() if line.strip()]
    gene_rows = [line for line in lines if not line.startswith("N_") and not line.startswith("MissingGeneID")]
    if not gene_rows:
        raise SystemExit(
            "GeneCounts validation failed: ReadsPerGene.out.tab has no gene rows. "
            "Check that the STAR index was built from the corrected GTF."
        )
    print(f"GeneCounts validation PASS: {len(gene_rows)} gene rows in {counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
