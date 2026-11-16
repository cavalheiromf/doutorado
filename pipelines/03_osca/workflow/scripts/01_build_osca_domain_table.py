#!/usr/bin/env python3
"""Build the canonical Pfam-domain table from an InterProScan TSV file."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def load_mapping(path: Path, species_prefix: str) -> tuple[dict[str, str], list[str]]:
    mapping: dict[str, str] = {}
    order: list[str] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            fields = line.split()
            if not fields:
                continue
            if len(fields) != 2:
                raise ValueError(f"{path}:{line_number}: expected two columns")
            genomic_id, short_name = fields
            if not genomic_id.startswith(species_prefix):
                continue
            if genomic_id in mapping or short_name in mapping.values():
                raise ValueError(f"Duplicate mapping at {path}:{line_number}")
            mapping[genomic_id] = short_name
            order.append(genomic_id)
    return mapping, order


def build_table(interproscan: Path, mapping_file: Path, output: Path) -> None:
    mapping, order = load_mapping(mapping_file, "Vper.")
    if len(mapping) != 14:
        raise ValueError(f"Expected 14 Vper mappings, found {len(mapping)}")

    rows: list[tuple[str, int, int, str]] = []
    observed: set[str] = set()
    with interproscan.open(encoding="utf-8") as handle:
        reader = csv.reader(handle, delimiter="\t")
        for fields in reader:
            if len(fields) < 8 or fields[3] != "Pfam":
                continue
            genomic_id = fields[0]
            if genomic_id not in mapping:
                continue
            rows.append((mapping[genomic_id], int(fields[6]), int(fields[7]), fields[4]))
            observed.add(genomic_id)

    missing = set(mapping) - observed
    if missing:
        raise ValueError(f"No Pfam records for: {', '.join(sorted(missing))}")

    rank = {mapping[genomic_id]: index for index, genomic_id in enumerate(order)}
    rows.sort(key=lambda row: (rank[row[0]], row[1], row[2], row[3]))
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["gene", "start", "end", "domain"])
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--interproscan", type=Path, required=True)
    parser.add_argument("--mapping", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build_table(args.interproscan, args.mapping, args.output)


if __name__ == "__main__":
    main()
