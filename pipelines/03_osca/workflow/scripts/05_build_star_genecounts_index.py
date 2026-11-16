#!/usr/bin/env python3
"""Build an isolated STAR index from a GeneCounts-compatible GTF."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
OSCA_DIR = Path(__file__).resolve().parents[1]
GFFREAD_DEFAULT = os.environ.get("GFFREAD_BIN") or shutil.which("gffread") or "gffread"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--species", choices=("Vper", "Vtub"), required=True)
    parser.add_argument("--threads", type=int, default=24)
    parser.add_argument("--star", default="STAR")
    parser.add_argument("--gffread", default=GFFREAD_DEFAULT)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    genome_dir = PROJECT_ROOT / "data" / "genomes" / args.species
    source_gff = genome_dir / f"{args.species}.hapA.v1.softmasked.gff3"
    fasta = genome_dir / f"{args.species}.hapA.v1.softmasked.fasta"
    output = OSCA_DIR / "05_rnaseq" / "results_genecounts" / "03_star_index" / args.species
    gtf = output / "annotation.gtf"
    if not source_gff.exists() or not fasta.exists():
        raise SystemExit(f"Missing genome input for {args.species}: {source_gff} or {fasta}")
    if (output / "Genome").exists():
        raise SystemExit(f"Refusing to overwrite existing STAR index: {output}")

    output.mkdir(parents=True, exist_ok=True)
    fix_gtf = PROJECT_ROOT / "analyses" / "05_rnaseq" / "scripts" / "fix_gtf.py"
    commands = [
        [args.gffread, str(source_gff), "-T", "-o", str(gtf)],
        ["python3", str(fix_gtf), str(gtf)],
        [
            args.star, "--runMode", "genomeGenerate", "--genomeDir", str(output),
            "--genomeFastaFiles", str(fasta), "--sjdbGTFfile", str(gtf),
            "--sjdbOverhang", "99", "--genomeSAindexNbases", "13",
            "--runThreadN", str(args.threads),
        ],
    ]
    for command in commands:
        print(" ".join(command))
        if not args.dry_run:
            subprocess.run(command, check=True)

    if not args.dry_run:
        exon_without_gene = subprocess.run(
            ["awk", '-F\\t', '$3 == "exon" && $9 !~ /gene_id/ {n++} END {print n+0}', str(gtf)],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        if exon_without_gene != "0":
            raise SystemExit(f"GTF validation failed: {exon_without_gene} exon records lack gene_id")
        print(f"STAR index validation PASS: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
