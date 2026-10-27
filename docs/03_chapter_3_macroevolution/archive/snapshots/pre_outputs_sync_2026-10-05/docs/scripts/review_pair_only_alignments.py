#!/usr/bin/env python3
"""Summarize observed changes in the high-information sister-pair alignments."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from Bio.Seq import Seq
from Bio import AlignIO


def fasta(path: Path) -> dict[str, str]:
    records, name, seq = {}, None, []
    for line in path.read_text().splitlines():
        if line.startswith(">"):
            if name is not None:
                records[name] = "".join(seq)
            name, seq = line[1:].split()[0], []
        else:
            seq.append(line.strip())
    if name is not None:
        records[name] = "".join(seq)
    return records


def observed_changes(cds: dict[str, str]) -> dict[str, int]:
    vper, vtub = cds["Vper"], cds["Vtub"]
    if len(vper) != len(vtub) or len(vper) % 3:
        raise ValueError("trimmed CDS sequences must have equal length divisible by 3")
    synonymous = nonsynonymous = codon_differences = nucleotide_differences = 0
    invalid_codons = 0
    for i in range(0, len(vper), 3):
        a, b = vper[i : i + 3], vtub[i : i + 3]
        if any(base not in "ACGT" for base in a + b):
            invalid_codons += 1
            continue
        if a == b:
            continue
        codon_differences += 1
        nucleotide_differences += sum(x != y for x, y in zip(a, b))
        if Seq(a).translate() == Seq(b).translate():
            synonymous += 1
        else:
            nonsynonymous += 1
    return {
        "Observed_Codon_Differences": codon_differences,
        "Observed_Nucleotide_Differences": nucleotide_differences,
        "Observed_Synonymous_Codons": synonymous,
        "Observed_Nonsynonymous_Codons": nonsynonymous,
        "Invalid_Retained_Codons": invalid_codons,
    }


def run(run_dir: Path) -> dict[str, int]:
    source = run_dir / "pair_only_high_information.tsv"
    candidates = list(csv.DictReader(source.open(), delimiter="\t"))
    rows = []
    for candidate in candidates:
        pair_dir = run_dir / "work" / candidate["Pair_ID"]
        metrics = json.loads((pair_dir / "result.json").read_text())
        alignment = AlignIO.read(pair_dir / "seq.phy", "phylip-sequential")
        changes = observed_changes({record.id: str(record.seq) for record in alignment})
        rows.append({**candidate, **changes, "Codons": metrics["Codons"],
                     "Ka_dN": metrics["Ka_dN"], "Ks_dS": metrics["Ks_dS"],
                     "Omega_KaKs": metrics["Omega_KaKs"],
                     "dN_SE": metrics["dN_SE"], "dS_SE": metrics["dS_SE"],
                     "Removed_Pair_Gaps": metrics["Removed_Pair_Gaps"]})
    fields = ["Pair_ID", "Orthogroup", "Omega_KaKs", "Ka_dN", "Ks_dS", "dN_SE", "dS_SE",
              "Codons", "Observed_Codon_Differences", "Observed_Nucleotide_Differences",
              "Observed_Synonymous_Codons", "Observed_Nonsynonymous_Codons",
              "Removed_Pair_Gaps", "Functional_Description"]
    with (run_dir / "pair_only_alignment_review.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})
    summary = {
        "pairs_reviewed": len(rows),
        "pairs_with_zero_observed_codon_differences": sum(r["Observed_Codon_Differences"] == 0 for r in rows),
        "total_observed_synonymous_codons": sum(r["Observed_Synonymous_Codons"] for r in rows),
        "total_observed_nonsynonymous_codons": sum(r["Observed_Nonsynonymous_Codons"] for r in rows),
    }
    (run_dir / "pair_only_alignment_review_summary.json").write_text(json.dumps(summary, indent=2))
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", type=Path)
    print(json.dumps(run(parser.parse_args().run_dir), indent=2))
