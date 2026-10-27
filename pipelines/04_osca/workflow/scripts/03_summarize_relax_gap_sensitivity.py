#!/usr/bin/env python3

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
VALIDATION_DIR = ROOT / "analyses/03_synteny/hyphy_validation_20260716"
RESULT_DIR = VALIDATION_DIR / "relax_gap_sensitivity"
FILTER_SUMMARY = VALIDATION_DIR / "filtered_alignments/filter_summary.tsv"
RELAX_PARAMETER = "relaxation or intensification parameter"


def main() -> None:
    with FILTER_SUMMARY.open() as handle:
        filter_rows = {
            (row["filter"], row["dataset"]): row
            for row in csv.DictReader(handle, delimiter="\t")
        }

    rows = []
    for filter_name in ("gap20", "gap50"):
        for dataset in ("global", "osca1", "osca2", "osca3_4"):
            result_path = RESULT_DIR / filter_name / dataset / "relax_results.json"
            if not result_path.is_file() or result_path.stat().st_size == 0:
                continue
            with result_path.open() as handle:
                result = json.load(handle)
            test = result["test results"]
            metadata = filter_rows[(filter_name, dataset)]
            rows.append(
                {
                    "filter": filter_name,
                    "dataset": dataset,
                    "retained_codons": metadata["retained_codons"],
                    "retained_fraction": metadata["retained_fraction"],
                    "K": test[RELAX_PARAMETER],
                    "LRT": test["LRT"],
                    "p_value": test["p-value"],
                    "result_file": str(result_path.relative_to(VALIDATION_DIR)),
                }
            )

    if rows:
        with (RESULT_DIR / "relax_gap_sensitivity_summary.tsv").open(
            "w", newline=""
        ) as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t")
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    main()
