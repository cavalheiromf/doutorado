#!/usr/bin/env python3

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
ANALYSIS_DIR = ROOT / "analyses/03_synteny"
OUTPUT_DIR = ANALYSIS_DIR / "hyphy_validation_20260716/filtered_alignments"
ALIGNMENTS = {
    "global": ANALYSIS_DIR / "hyphy_analysis/vellozia_oscas_codon.fasta",
    "osca1": ANALYSIS_DIR / "hyphy_subclades/osca1/osca1_codon.fasta",
    "osca2": ANALYSIS_DIR / "hyphy_subclades/osca2/osca2_codon.fasta",
    "osca3_4": ANALYSIS_DIR / "hyphy_subclades/osca3_4/osca3_4_codon.fasta",
}
THRESHOLDS = {"gap20": 0.20, "gap50": 0.50}


def read_fasta(path: Path) -> list[tuple[str, str]]:
    records = []
    name = None
    chunks = []
    with path.open() as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if name is not None:
                    records.append((name, "".join(chunks).upper()))
                name = line[1:].split()[0]
                chunks = []
            else:
                chunks.append(line)
    if name is not None:
        records.append((name, "".join(chunks).upper()))
    return records


def write_fasta(path: Path, records: list[tuple[str, str]]) -> None:
    with path.open("w") as handle:
        for name, sequence in records:
            handle.write(f">{name}\n")
            for start in range(0, len(sequence), 80):
                handle.write(sequence[start : start + 80] + "\n")


def main() -> None:
    summary_rows = []
    for dataset, alignment_path in ALIGNMENTS.items():
        records = read_fasta(alignment_path)
        lengths = {len(sequence) for _, sequence in records}
        if len(lengths) != 1 or next(iter(lengths)) % 3:
            raise ValueError(f"Invalid codon alignment: {alignment_path}")
        codon_count = next(iter(lengths)) // 3

        gap_fractions = []
        for site in range(codon_count):
            codons = [sequence[site * 3 : site * 3 + 3] for _, sequence in records]
            gap_fractions.append(sum("-" in codon for codon in codons) / len(codons))

        for label, threshold in THRESHOLDS.items():
            threshold_dir = OUTPUT_DIR / label / dataset
            threshold_dir.mkdir(parents=True, exist_ok=True)
            kept_sites = [
                site for site, gap_fraction in enumerate(gap_fractions)
                if gap_fraction <= threshold
            ]
            filtered_records = []
            for name, sequence in records:
                filtered = "".join(
                    sequence[site * 3 : site * 3 + 3] for site in kept_sites
                )
                filtered_records.append((name, filtered))

            output_alignment = threshold_dir / f"{dataset}_codon_gap_filtered.fasta"
            write_fasta(output_alignment, filtered_records)

            filtered_index = {site: index + 1 for index, site in enumerate(kept_sites)}
            with (threshold_dir / "site_map.tsv").open("w", newline="") as handle:
                writer = csv.DictWriter(
                    handle,
                    fieldnames=[
                        "original_codon_site",
                        "filtered_codon_site",
                        "gap_fraction",
                        "retained",
                    ],
                    delimiter="\t",
                )
                writer.writeheader()
                for site, gap_fraction in enumerate(gap_fractions):
                    writer.writerow(
                        {
                            "original_codon_site": site + 1,
                            "filtered_codon_site": filtered_index.get(site, ""),
                            "gap_fraction": f"{gap_fraction:.6f}",
                            "retained": site in filtered_index,
                        }
                    )

            summary_rows.append(
                {
                    "dataset": dataset,
                    "filter": label,
                    "maximum_allowed_gap_fraction": threshold,
                    "original_codons": codon_count,
                    "retained_codons": len(kept_sites),
                    "removed_codons": codon_count - len(kept_sites),
                    "retained_fraction": f"{len(kept_sites) / codon_count:.6f}",
                }
            )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with (OUTPUT_DIR / "filter_summary.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summary_rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(summary_rows)


if __name__ == "__main__":
    main()
