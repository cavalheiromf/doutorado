#!/usr/bin/env python3

import csv
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
ANALYSIS_DIR = ROOT / "analyses/03_synteny"
GARD_DIR = ANALYSIS_DIR / "hyphy_validation_20260716/gard"
ALIGNMENTS = {
    "osca1": ANALYSIS_DIR / "hyphy_subclades/osca1/osca1_codon.fasta",
    "osca2": ANALYSIS_DIR / "hyphy_subclades/osca2/osca2_codon.fasta",
    "osca3_4": ANALYSIS_DIR / "hyphy_subclades/osca3_4/osca3_4_codon.fasta",
}


def read_fasta(path: Path) -> dict[str, str]:
    sequences = {}
    name = None
    with path.open() as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line:
                continue
            if line.startswith(">"):
                name = line[1:].split()[0]
                sequences[name] = ""
            else:
                sequences[name] += line.upper()
    return sequences


def gap_fraction(sequences: dict[str, str], codon_site: int) -> float:
    start = (codon_site - 1) * 3
    codons = [sequence[start : start + 3] for sequence in sequences.values()]
    return sum("-" in codon for codon in codons) / len(codons)


def main() -> None:
    rows = []
    for dataset, alignment in ALIGNMENTS.items():
        dataset_dir = GARD_DIR / dataset
        if (dataset_dir / ".run.lock").exists():
            continue
        result_path = dataset_dir / "gard.json"
        if not result_path.is_file() or result_path.stat().st_size == 0:
            continue

        with result_path.open() as handle:
            result = json.load(handle)
        improvements = result.get("improvements", {})
        if improvements:
            final_key = max(improvements, key=lambda key: int(key))
            breakpoints = [item[0] for item in improvements[final_key]["breakpoints"]]
        else:
            breakpoints = []

        sequences = read_fasta(alignment)
        # GARD stores zero-based breakpoint indices in JSON. The corresponding
        # one-based NEXUS partition endpoint is therefore breakpoint + 1.
        breakpoint_ends = [breakpoint + 1 for breakpoint in breakpoints]
        codon_sites = [(endpoint + 2) // 3 for endpoint in breakpoint_ends]
        gap_at_break = [gap_fraction(sequences, site) for site in codon_sites]
        gap_near_break = []
        codon_count = len(next(iter(sequences.values()))) // 3
        for site in codon_sites:
            neighborhood = range(max(1, site - 3), min(codon_count, site + 3) + 1)
            gap_near_break.append(
                max(gap_fraction(sequences, neighbor) for neighbor in neighborhood)
            )

        baseline = result["baselineScore"]
        best = result["bestModelAICc"]
        single_tree = result["singleTreeAICc"]
        topology_delta = single_tree - best
        rows.append(
            {
                "dataset": dataset,
                "sequences": result["input"]["number of sequences"],
                "nucleotide_sites": result["input"]["number of sites"],
                "selected_breakpoint_end_nt_1based": ",".join(
                    map(str, breakpoint_ends)
                ),
                "breakpoint_containing_codon": ",".join(map(str, codon_sites)),
                "selected_breakpoint_count": len(breakpoints),
                "reached_configured_maximum_of_5": len(breakpoints) == 5,
                "all_breakpoints_on_codon_boundary": all(
                    endpoint % 3 == 0 for endpoint in breakpoint_ends
                ),
                "gap_fraction_at_breakpoint_codon": ",".join(
                    f"{value:.3f}" for value in gap_at_break
                ),
                "max_gap_fraction_within_3_codons": ",".join(
                    f"{value:.3f}" for value in gap_near_break
                ),
                "baseline_aicc": f"{baseline:.6f}",
                "best_partitioned_aicc": f"{best:.6f}",
                "delta_aicc_vs_baseline": f"{baseline - best:.6f}",
                "single_tree_aicc": f"{single_tree:.6f}",
                "delta_aicc_partitioned_vs_single_tree": f"{topology_delta:.6f}",
                "topology_evidence_ratio": f"{math.exp(topology_delta / 2):.6g}",
                "topology_evidence_ratio_ge_100": math.exp(topology_delta / 2)
                >= 100,
                "models_evaluated": result["totalModelCount"],
                "runtime_seconds": result["timeElapsed"],
            }
        )

    output = GARD_DIR / "gard_summary.tsv"
    if rows:
        with output.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t")
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    main()
