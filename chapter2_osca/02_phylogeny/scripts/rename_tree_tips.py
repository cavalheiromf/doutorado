#!/usr/bin/env python3
"""Rename Newick tip labels using the canonical OSCA identifier map."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def load_mapping(path: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    names: set[str] = set()
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            fields = line.split()
            if not fields:
                continue
            if len(fields) != 2:
                raise ValueError(f"{path}:{line_number}: expected two columns")
            genomic_id, short_name = fields
            if genomic_id in mapping or short_name in names:
                raise ValueError(f"Duplicate mapping at {path}:{line_number}")
            mapping[genomic_id] = short_name
            names.add(short_name)
    return mapping


def rename_tree(input_path: Path, mapping_path: Path, output_path: Path) -> None:
    tree = input_path.read_text(encoding="utf-8")
    mapping = load_mapping(mapping_path)
    for genomic_id, short_name in mapping.items():
        pattern = rf"(?<=[(,]){re.escape(genomic_id)}(?=:)"
        matches = len(re.findall(pattern, tree))
        if matches != 1:
            raise ValueError(f"Expected one tree tip for {genomic_id}, found {matches}")
        tree = re.sub(pattern, short_name, tree)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(tree, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--mapping", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rename_tree(args.input, args.mapping, args.output)


if __name__ == "__main__":
    main()
