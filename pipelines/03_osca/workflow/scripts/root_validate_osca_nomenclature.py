#!/usr/bin/env python3
"""Validate propagation of the canonical OSCA2.4 nomenclature."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAPPING_PATH = ROOT / "analyses/01_gene_identification/results/oscasIDs.txt"
RESULTS_01 = ROOT / "analyses/01_gene_identification/results"
RESULTS_02 = ROOT / "analyses/02_phylogeny/results"
RESULTS_04 = (
    ROOT / "08_promoters/results"
    if (ROOT / "08_promoters/results").exists()
    else ROOT / "analyses/04_promoters/results"
)

CANONICAL = {
    "Vper.hapA.v1.chr1A.g023030.t1": "VpOSCA2.4a",
    "Vper.hapA.v1.chr1A.g023020.t1": "VpOSCA2.4b",
    "Vtub.hapA.v1.chr1A.g020650.t1": "VtOSCA2.4",
}

EXPECTED_BED = {
    "Vper.osca.coords.bed": {
        "VpOSCA2.4a": ("chr1A", "22689052", "22697439", "+"),
        "VpOSCA2.4b": ("chr1A", "22678816", "22687760", "+"),
    },
    "Vper.promoters.2k.bed": {
        "VpOSCA2.4a": ("chr1A", "22687052", "22689052", "+"),
        "VpOSCA2.4b": ("chr1A", "22676816", "22678816", "+"),
    },
}


def load_mapping() -> dict[str, str]:
    mapping: dict[str, str] = {}
    with MAPPING_PATH.open(encoding="utf-8") as handle:
        for line in handle:
            fields = line.split()
            if fields:
                if len(fields) != 2:
                    raise AssertionError(f"Invalid mapping line: {line.rstrip()}")
                mapping[fields[0]] = fields[1]
    vper = {key: value for key, value in mapping.items() if key.startswith("Vper.")}
    assert len(vper) == 14, f"Expected 14 Vper IDs, found {len(vper)}"
    assert len(set(vper.values())) == 14, "Vper short names are not unique"
    for genomic_id, short_name in CANONICAL.items():
        assert mapping.get(genomic_id) == short_name
    return mapping


def validate_domain_tables() -> None:
    for filename in ["Vper.osca.tsv", "Vper.osca.tsv.fixed", "Vper.osca.tsv.tmp"]:
        path = RESULTS_01 / filename
        with path.open(encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle, delimiter="\t"))
        names = {row["gene"] for row in rows}
        assert len(names) == 14, f"{filename}: expected 14 names, found {len(names)}"
        assert "VpOSCA2.4" not in names, f"{filename}: unsuffixed OSCA2.4"
        a_hits = {(row["start"], row["end"], row["domain"]) for row in rows if row["gene"] == "VpOSCA2.4a"}
        b_hits = {(row["start"], row["end"], row["domain"]) for row in rows if row["gene"] == "VpOSCA2.4b"}
        assert ("189", "238", "PF14703") in a_hits
        assert ("239", "281", "PF14703") in a_hits
        assert ("239", "281", "PF14703") in b_hits


def validate_tree(mapping: dict[str, str]) -> None:
    original = (RESULTS_02 / "iqtree.treefile").read_text(encoding="utf-8")
    renamed = (RESULTS_02 / "iqtree.renamed.treefile").read_text(encoding="utf-8")
    restored = renamed
    for genomic_id, short_name in mapping.items():
        pattern = rf"(?<=[(,]){re.escape(short_name)}(?=:)"
        assert len(re.findall(pattern, restored)) == 1, f"Tree tip count for {short_name}"
        restored = re.sub(pattern, genomic_id, restored)
    assert restored == original, "Renaming changed tree topology or branch lengths"


def read_bed(path: Path) -> dict[str, tuple[str, str, str, str]]:
    records = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            chrom, start, end, name, _, strand = line.rstrip("\n").split("\t")
            records[name] = (chrom, start, end, strand)
    return records


def validate_promoters() -> None:
    for filename, expected in EXPECTED_BED.items():
        records = read_bed(RESULTS_04 / filename)
        assert len(records) == 14, f"{filename}: expected 14 unique records"
        for name, coordinates in expected.items():
            assert records.get(name) == coordinates, f"{filename}: wrong coordinates for {name}"

    fasta = (RESULTS_04 / "Vper.promoters.2k.fasta").read_text(encoding="utf-8")
    headers = [line[1:] for line in fasta.splitlines() if line.startswith(">")]
    assert len(headers) == 14 and len(set(headers)) == 14
    assert "VpOSCA2.4a::chr1A:22687052-22689052(+)" in headers
    assert "VpOSCA2.4b::chr1A:22676816-22678816(+)" in headers

    cleaned = RESULTS_04 / "Vper_plantcare_cleaned.tsv"
    with cleaned.open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert len(rows) == 2509, f"Unexpected PlantCARE record count: {len(rows)}"
    assert {row["Gene"] for row in rows} == {
        line.split("::", maxsplit=1)[0] for line in headers
    }
    assert all(row["Gene"] != "VpOSCA2.4" for row in rows)

    counts = RESULTS_04 / "Vper_motif_counts.tsv"
    with counts.open(encoding="utf-8") as handle:
        count_rows = list(csv.DictReader(handle, delimiter="\t"))
    count_names = {row["Gene"] for row in count_rows}
    assert len(count_names) == 14
    assert {"VpOSCA2.4a", "VpOSCA2.4b"} <= count_names
    assert "VpOSCA2.4" not in count_names


def validate_no_ambiguous_derived_names() -> None:
    paths = [
        RESULTS_01 / "Vper.osca.tsv",
        RESULTS_01 / "Vper.osca.tsv.fixed",
        RESULTS_01 / "Vper.osca.tsv.tmp",
        RESULTS_02 / "iqtree.renamed.treefile",
        RESULTS_04 / "Vper.osca.coords.bed",
        RESULTS_04 / "Vper.promoters.2k.bed",
        RESULTS_04 / "Vper.promoters.2k.fasta",
        RESULTS_04 / "allOSCAs.promoters.2k.fasta",
        RESULTS_04 / "Vper_plantcare_cleaned.tsv",
        RESULTS_04 / "Vper_motif_counts.tsv",
    ]
    ambiguous = re.compile(r"VpOSCA2\.4(?![ab])")
    failures = [str(path.relative_to(ROOT)) for path in paths if ambiguous.search(path.read_text(encoding="utf-8"))]
    assert not failures, f"Unsuffixed individual names in: {', '.join(failures)}"


def main() -> None:
    mapping = load_mapping()
    validate_domain_tables()
    validate_tree(mapping)
    validate_promoters()
    validate_no_ambiguous_derived_names()
    print("OSCA2.4 nomenclature validation: PASS")


if __name__ == "__main__":
    main()
