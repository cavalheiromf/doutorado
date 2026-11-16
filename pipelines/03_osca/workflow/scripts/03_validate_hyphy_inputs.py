#!/usr/bin/env python3

import argparse
import csv
import json
import re
from io import StringIO
from pathlib import Path

from Bio import Phylo


ROOT = Path(__file__).resolve().parents[3]
ANALYSIS_DIR = ROOT / "analyses/03_synteny"
RERUN_DIR = ANALYSIS_DIR / "hyphy_rerun_20260716"
STOP_CODONS = {"TAA", "TAG", "TGA"}
DATASETS = {
    "global": {
        "alignment": ANALYSIS_DIR / "hyphy_analysis/vellozia_oscas_codon.fasta",
        "tree": ANALYSIS_DIR / "hyphy_analysis/vellozia_oscas_labeled.treefile",
        "contrast": RERUN_DIR / "global/contrast_fel_results.json",
    },
    "osca1": {
        "alignment": ANALYSIS_DIR / "hyphy_subclades/osca1/osca1_codon.fasta",
        "tree": ANALYSIS_DIR / "hyphy_subclades/osca1/osca1_labeled.treefile",
        "contrast": RERUN_DIR / "osca1/contrast_fel_results.json",
    },
    "osca2": {
        "alignment": ANALYSIS_DIR / "hyphy_subclades/osca2/osca2_codon.fasta",
        "tree": ANALYSIS_DIR / "hyphy_subclades/osca2/osca2_labeled.treefile",
        "contrast": RERUN_DIR / "osca2/contrast_fel_results.json",
    },
    "osca3_4": {
        "alignment": ANALYSIS_DIR / "hyphy_subclades/osca3_4/osca3_4_codon.fasta",
        "tree": ANALYSIS_DIR / "hyphy_subclades/osca3_4/osca3_4_labeled.treefile",
        "contrast": RERUN_DIR / "osca3_4/contrast_fel_results.json",
    },
}


def read_fasta(path: Path) -> dict[str, str]:
    sequences = {}
    current = None
    chunks = []
    with path.open() as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current is not None:
                    sequences[current] = "".join(chunks).upper()
                current = line[1:].split()[0]
                if current in sequences:
                    raise ValueError(f"Duplicate FASTA identifier in {path}: {current}")
                chunks = []
            else:
                if current is None:
                    raise ValueError(f"Sequence data before first header in {path}")
                chunks.append(line)
    if current is not None:
        sequences[current] = "".join(chunks).upper()
    return sequences


def load_tree(path: Path):
    raw = path.read_text().strip()
    clean = re.sub(r"\{(?:Test|Reference)\}", "", raw)
    return raw, Phylo.read(StringIO(clean), "newick")


def nominal_sites(path: Path) -> list[int]:
    with path.open() as handle:
        result = json.load(handle)
    headers = [entry[0] for entry in result["MLE"]["headers"]]
    p_index = headers.index("P-value (overall)")
    rows = result["MLE"]["content"]["0"]
    return [index + 1 for index, row in enumerate(rows) if row[p_index] <= 0.05]


def write_tsv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def species_group(identifier: str) -> str:
    if identifier.startswith("Vper_"):
        return "Reference"
    if identifier.startswith("Vtub_"):
        return "Test"
    return "Unknown"


def audit_dataset(name: str, paths: dict[str, Path]):
    sequences = read_fasta(paths["alignment"])
    lengths = {len(sequence) for sequence in sequences.values()}
    if len(lengths) != 1:
        raise ValueError(f"Unequal aligned lengths in {name}: {sorted(lengths)}")
    nucleotide_count = lengths.pop()
    if nucleotide_count % 3:
        raise ValueError(f"Alignment length is not divisible by three in {name}")
    codon_count = nucleotide_count // 3

    sequence_rows = []
    internal_stop_total = 0
    partial_gap_total = 0
    for identifier, sequence in sequences.items():
        internal_stops = []
        partial_gaps = 0
        full_gap_codons = 0
        ambiguous_codons = 0
        for site in range(codon_count):
            codon = sequence[site * 3 : site * 3 + 3]
            dash_count = codon.count("-")
            if dash_count == 3:
                full_gap_codons += 1
            elif dash_count:
                partial_gaps += 1
            if any(base not in "ACGT-" for base in codon):
                ambiguous_codons += 1
            if site < codon_count - 1 and codon in STOP_CODONS:
                internal_stops.append(site + 1)
        internal_stop_total += len(internal_stops)
        partial_gap_total += partial_gaps
        sequence_rows.append(
            {
                "dataset": name,
                "sequence": identifier,
                "species_group": species_group(identifier),
                "codons": codon_count,
                "full_gap_codons": full_gap_codons,
                "partial_gap_codons": partial_gaps,
                "ambiguous_codons": ambiguous_codons,
                "internal_stop_codons": len(internal_stops),
                "internal_stop_sites": ",".join(map(str, internal_stops)),
            }
        )

    site_gap_counts = []
    codon_columns = []
    for site in range(codon_count):
        codons = [sequence[site * 3 : site * 3 + 3] for sequence in sequences.values()]
        gap_count = sum("-" in codon for codon in codons)
        site_gap_counts.append(gap_count)
        codon_columns.append(codons)

    any_gap_sites = sum(count > 0 for count in site_gap_counts)
    gap_gt_20 = sum(count / len(sequences) > 0.20 for count in site_gap_counts)
    gap_gt_50 = sum(count / len(sequences) > 0.50 for count in site_gap_counts)
    all_gap_sites = sum(count == len(sequences) for count in site_gap_counts)
    variable_sites = sum(len(set(codons)) > 1 for codons in codon_columns)

    raw_tree, tree = load_tree(paths["tree"])
    leaves = [terminal.name for terminal in tree.get_terminals()]
    fasta_ids = set(sequences)
    tree_ids = set(leaves)
    missing_from_tree = sorted(fasta_ids - tree_ids)
    missing_from_alignment = sorted(tree_ids - fasta_ids)

    pure_reference_internal = 0
    pure_test_internal = 0
    mixed_internal = 0
    for clade in tree.get_nonterminals():
        groups = {species_group(terminal.name) for terminal in clade.get_terminals()}
        if groups == {"Reference"}:
            pure_reference_internal += 1
        elif groups == {"Test"}:
            pure_test_internal += 1
        else:
            mixed_internal += 1

    tree_row = {
        "dataset": name,
        "tree_leaves": len(leaves),
        "alignment_sequences": len(sequences),
        "test_labels_in_file": len(re.findall(r"\{Test\}", raw_tree)),
        "reference_labels_in_file": len(re.findall(r"\{Reference\}", raw_tree)),
        "test_leaves_by_prefix": sum(species_group(leaf) == "Test" for leaf in leaves),
        "reference_leaves_by_prefix": sum(
            species_group(leaf) == "Reference" for leaf in leaves
        ),
        "missing_from_tree": ",".join(missing_from_tree),
        "missing_from_alignment": ",".join(missing_from_alignment),
        "pure_reference_internal_clades": pure_reference_internal,
        "pure_test_internal_clades": pure_test_internal,
        "mixed_internal_clades": mixed_internal,
        "zero_length_terminal_branches": sum(
            (terminal.branch_length or 0) == 0 for terminal in tree.get_terminals()
        ),
        "zero_length_internal_branches": sum(
            (clade.branch_length or 0) == 0 for clade in tree.get_nonterminals()
        ),
    }

    nominal_rows = []
    for site in nominal_sites(paths["contrast"]):
        codons = {
            identifier: sequence[(site - 1) * 3 : site * 3]
            for identifier, sequence in sequences.items()
        }
        nominal_rows.append(
            {
                "dataset": name,
                "site": site,
                "sequence_count": len(sequences),
                "gap_sequences": sum("-" in codon for codon in codons.values()),
                "gap_fraction": sum("-" in codon for codon in codons.values())
                / len(sequences),
                "partial_gap_sequences": sum(
                    0 < codon.count("-") < 3 for codon in codons.values()
                ),
                "ambiguous_sequences": sum(
                    any(base not in "ACGT-" for base in codon)
                    for codon in codons.values()
                ),
                "stop_codon_sequences": sum(
                    codon in STOP_CODONS for codon in codons.values()
                ),
                "codons": ";".join(
                    f"{identifier}={codon}" for identifier, codon in codons.items()
                ),
            }
        )

    alignment_row = {
        "dataset": name,
        "sequences": len(sequences),
        "nucleotides": nucleotide_count,
        "codons": codon_count,
        "variable_codon_sites": variable_sites,
        "sites_with_any_gap": any_gap_sites,
        "sites_gap_fraction_gt_0.20": gap_gt_20,
        "sites_gap_fraction_gt_0.50": gap_gt_50,
        "all_gap_sites": all_gap_sites,
        "partial_gap_codon_cells": partial_gap_total,
        "internal_stop_codons": internal_stop_total,
        "tree_alignment_ids_match": not missing_from_tree and not missing_from_alignment,
    }
    return alignment_row, tree_row, sequence_rows, nominal_rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit HyPhy codon inputs and trees.")
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    alignment_rows = []
    tree_rows = []
    sequence_rows = []
    nominal_rows = []
    for name, paths in DATASETS.items():
        alignment, tree, sequences, nominal = audit_dataset(name, paths)
        alignment_rows.append(alignment)
        tree_rows.append(tree)
        sequence_rows.extend(sequences)
        nominal_rows.extend(nominal)

    write_tsv(output_dir / "alignment_qc.tsv", alignment_rows)
    write_tsv(output_dir / "tree_qc.tsv", tree_rows)
    write_tsv(output_dir / "sequence_qc.tsv", sequence_rows)
    write_tsv(output_dir / "nominal_site_gap_audit.tsv", nominal_rows)

    summary = {
        "datasets": len(DATASETS),
        "all_alignments_in_frame": all(row["codons"] * 3 == row["nucleotides"] for row in alignment_rows),
        "all_tree_alignment_ids_match": all(
            row["tree_alignment_ids_match"] for row in alignment_rows
        ),
        "total_internal_stop_codons": sum(
            row["internal_stop_codons"] for row in alignment_rows
        ),
        "total_partial_gap_codon_cells": sum(
            row["partial_gap_codon_cells"] for row in alignment_rows
        ),
        "nominal_sites_audited": len(nominal_rows),
        "nominal_sites_gap_fraction_gt_0.20": sum(
            row["gap_fraction"] > 0.20 for row in nominal_rows
        ),
    }
    (output_dir / "validation_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
