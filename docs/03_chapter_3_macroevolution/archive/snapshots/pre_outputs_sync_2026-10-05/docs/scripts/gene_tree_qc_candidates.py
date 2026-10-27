#!/usr/bin/env python3
"""Assess focal Vper--Vtub omega>1 pairs in resolved OrthoFinder gene trees.

The pairwise Ka/Ks screen is a candidate filter.  This script adds a
gene-tree check for each candidate: it verifies that both focal leaves are
present, identifies their most recent common ancestor (MRCA), and reports
whether the focal pair forms a two-leaf clade or whether other homologues are
present in that clade.  A two-leaf clade cannot support a multi-species
branch/site test without adding taxa from a different orthologous context.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from io import StringIO
from pathlib import Path

from Bio import Phylo


def read_tree_lines(path: Path) -> dict[str, str]:
    trees: dict[str, str] = {}
    with path.open() as handle:
        for raw in handle:
            raw = raw.strip()
            if not raw or ":" not in raw:
                continue
            og, newick = raw.split(":", 1)
            trees[og] = newick.strip()
    return trees


def species_from_leaf(name: str) -> str:
    return name.split("_pep_", 1)[0]


def focal_tree_metrics(newick: str, vper_gene: str, vtub_gene: str) -> dict[str, object]:
    tree = Phylo.read(StringIO(newick), "newick")
    leaves = [tip.name or "" for tip in tree.get_terminals()]
    vper_leaf = f"Vper_pep_{vper_gene}"
    vtub_leaf = f"Vtub_pep_{vtub_gene}"
    has_vper = vper_leaf in leaves
    has_vtub = vtub_leaf in leaves
    result: dict[str, object] = {
        "Tree_Leaves": len(leaves),
        "Tree_Species": len({species_from_leaf(x) for x in leaves}),
        "Focal_Leaves_Present": has_vper and has_vtub,
        "Focal_MRCA_Leaves": "",
        "Focal_MRCA_Nonfocal": "",
        "Focal_MRCA_Species": "",
        "Focal_MRCA_Species_Count": "",
        "Focal_MRCA_Duplicate_Species": "",
        "Focal_Pair_Sister": "",
        "Formal_Test_Eligibility": "",
    }
    if not (has_vper and has_vtub):
        result["Formal_Test_Eligibility"] = "MISSING_FOCAL_LEAF"
        return result

    mrca = tree.common_ancestor(vper_leaf, vtub_leaf)
    mrca_leaves = [tip.name or "" for tip in mrca.get_terminals()]
    mrca_species = [species_from_leaf(x) for x in mrca_leaves]
    nonfocal = [x for x in mrca_leaves if x not in {vper_leaf, vtub_leaf}]
    duplicate_species = [s for s, n in Counter(mrca_species).items() if n > 1]
    pair_sister = len(mrca_leaves) == 2
    result.update(
        {
            "Focal_MRCA_Leaves": len(mrca_leaves),
            "Focal_MRCA_Nonfocal": len(nonfocal),
            "Focal_MRCA_Species": ",".join(sorted(set(mrca_species))),
            "Focal_MRCA_Species_Count": len(set(mrca_species)),
            "Focal_MRCA_Duplicate_Species": ",".join(sorted(duplicate_species)),
            "Focal_Pair_Sister": pair_sister,
            "Formal_Test_Eligibility": (
                "POTENTIAL_MULTI_SPECIES"
                if len(mrca_leaves) >= 3 and not duplicate_species
                else "FOCAL_PAIR_ONLY"
                if pair_sister
                else "DUPLICATE_SPECIES_IN_MRCA"
            ),
        }
    )
    return result


def run(screen_path: Path, trees_path: Path, output_dir: Path) -> dict[str, object]:
    output_dir.mkdir(parents=True, exist_ok=True)
    trees = read_tree_lines(trees_path)
    with screen_path.open(newline="") as handle:
        candidates = list(csv.DictReader(handle, delimiter="\t"))
    rows: list[dict[str, object]] = []
    for row in candidates:
        og = row["Orthogroup"]
        metrics = focal_tree_metrics(
            trees[og], row["Vper_Gene"], row["Vtub_Gene"]
        ) if og in trees else {
            "Tree_Leaves": "", "Tree_Species": "", "Focal_Leaves_Present": False,
            "Focal_MRCA_Leaves": "", "Focal_MRCA_Nonfocal": "",
            "Focal_MRCA_Species": "", "Focal_MRCA_Species_Count": "",
            "Focal_MRCA_Duplicate_Species": "", "Focal_Pair_Sister": "",
            "Formal_Test_Eligibility": "MISSING_TREE",
        }
        rows.append({"Pair_ID": row["Pair_ID"], "Orthogroup": og, **metrics})

    fields = list(rows[0]) if rows else ["Pair_ID", "Orthogroup"]
    with (output_dir / "candidate_gene_tree_qc.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    # Keep a compact handoff table for the next, multi-species selection step.
    # It contains only candidates whose focal MRCA has >=3 leaves and no
    # repeated species, while retaining the original screen measurements.
    eligible = [
        (candidate, metrics)
        for candidate, metrics in zip(candidates, rows)
        if metrics["Formal_Test_Eligibility"] == "POTENTIAL_MULTI_SPECIES"
    ]
    eligible.sort(key=lambda pair: float(pair[0]["Omega_KaKs"]), reverse=True)
    shortlist_fields = [
        "Pair_ID", "Orthogroup", "Vper_Gene", "Vtub_Gene", "Omega_KaKs",
        "Ka_dN", "Ks_dS", "Flags", "Functional_Description",
        "Focal_MRCA_Leaves", "Focal_MRCA_Species", "Tree_Leaves", "Tree_Species",
    ]
    with (output_dir / "formal_test_shortlist.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=shortlist_fields, delimiter="\t")
        writer.writeheader()
        for candidate, metrics in eligible:
            writer.writerow({
                "Pair_ID": candidate["Pair_ID"],
                "Orthogroup": candidate["Orthogroup"],
                "Vper_Gene": candidate["Vper_Gene"],
                "Vtub_Gene": candidate["Vtub_Gene"],
                "Omega_KaKs": candidate["Omega_KaKs"],
                "Ka_dN": candidate["Ka_dN"],
                "Ks_dS": candidate["Ks_dS"],
                "Flags": candidate["Flags"],
                "Functional_Description": candidate["Functional_Description"],
                "Focal_MRCA_Leaves": metrics["Focal_MRCA_Leaves"],
                "Focal_MRCA_Species": metrics["Focal_MRCA_Species"],
                "Tree_Leaves": metrics["Tree_Leaves"],
                "Tree_Species": metrics["Tree_Species"],
            })

    # A conservative review queue for the sister-pair cases.  These criteria
    # are operational QC thresholds, not evidence of positive selection.
    pair_only_priority = []
    for candidate, metrics in zip(candidates, rows):
        if metrics["Formal_Test_Eligibility"] != "FOCAL_PAIR_ONLY":
            continue
        flags = candidate["Flags"]
        if (
            not flags
            and float(candidate["Ks_dS"]) >= 0.02
            and float(candidate["Protein_Identity"]) >= 0.70
            and float(candidate["Vper_Coverage"]) >= 0.70
            and float(candidate["Vtub_Coverage"]) >= 0.70
        ):
            pair_only_priority.append((candidate, metrics))
    pair_only_priority.sort(key=lambda pair: float(pair[0]["Omega_KaKs"]), reverse=True)
    with (output_dir / "pair_only_priority.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=shortlist_fields, delimiter="\t")
        writer.writeheader()
        for candidate, metrics in pair_only_priority:
            writer.writerow({
                "Pair_ID": candidate["Pair_ID"], "Orthogroup": candidate["Orthogroup"],
                "Vper_Gene": candidate["Vper_Gene"], "Vtub_Gene": candidate["Vtub_Gene"],
                "Omega_KaKs": candidate["Omega_KaKs"], "Ka_dN": candidate["Ka_dN"],
                "Ks_dS": candidate["Ks_dS"], "Flags": candidate["Flags"],
                "Functional_Description": candidate["Functional_Description"],
                "Focal_MRCA_Leaves": metrics["Focal_MRCA_Leaves"],
                "Focal_MRCA_Species": metrics["Focal_MRCA_Species"],
                "Tree_Leaves": metrics["Tree_Leaves"], "Tree_Species": metrics["Tree_Species"],
            })

    # First-pass manual review set: enough retained codons and a relatively
    # precise dS estimate, while retaining only the higher omega tail.  This
    # is a workload reduction rule, not a significance threshold.
    high_information = [
        (candidate, metrics)
        for candidate, metrics in pair_only_priority
        if float(candidate["Codons"]) >= 100
        and float(candidate["dS_SE"]) / float(candidate["Ks_dS"]) < 0.50
        and float(candidate["Omega_KaKs"]) >= 1.50
    ]
    with (output_dir / "pair_only_high_information.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=shortlist_fields, delimiter="\t")
        writer.writeheader()
        for candidate, metrics in high_information:
            writer.writerow({
                "Pair_ID": candidate["Pair_ID"], "Orthogroup": candidate["Orthogroup"],
                "Vper_Gene": candidate["Vper_Gene"], "Vtub_Gene": candidate["Vtub_Gene"],
                "Omega_KaKs": candidate["Omega_KaKs"], "Ka_dN": candidate["Ka_dN"],
                "Ks_dS": candidate["Ks_dS"], "Flags": candidate["Flags"],
                "Functional_Description": candidate["Functional_Description"],
                "Focal_MRCA_Leaves": metrics["Focal_MRCA_Leaves"],
                "Focal_MRCA_Species": metrics["Focal_MRCA_Species"],
                "Tree_Leaves": metrics["Tree_Leaves"], "Tree_Species": metrics["Tree_Species"],
            })

    counts = Counter(str(r["Formal_Test_Eligibility"]) for r in rows)
    summary = {
        "candidate_pairs": len(rows),
        "candidate_orthogroups": len({r["Orthogroup"] for r in rows}),
        "tree_lines": len(trees),
        "eligibility_counts": dict(sorted(counts.items())),
        "focal_pair_sister": sum(bool(r["Focal_Pair_Sister"]) for r in rows),
        "focal_leaf_missing": sum(not bool(r["Focal_Leaves_Present"]) for r in rows),
        "formal_test_shortlist": len(eligible),
        "pair_only_priority": len(pair_only_priority),
        "pair_only_high_information": len(high_information),
    }
    with (output_dir / "candidate_gene_tree_qc_summary.json").open("w") as handle:
        json.dump(summary, handle, indent=2)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", type=Path)
    parser.add_argument(
        "--trees",
        type=Path,
        default=Path("chapter_macroevolution/01_orthology/results/Results_Aug30/Resolved_Gene_Trees/Resolved_Gene_Trees.txt"),
    )
    args = parser.parse_args()
    summary = run(args.run_dir / "omega_gt1_screen.tsv", args.trees, args.run_dir)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
