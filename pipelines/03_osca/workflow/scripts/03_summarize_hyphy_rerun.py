#!/usr/bin/env python3

import argparse
import csv
import json
import re
from pathlib import Path


DATASETS = ("global", "osca1", "osca2", "osca3_4")
RELAX_PARAMETER = "relaxation or intensification parameter"


def load_json(path: Path) -> dict:
    with path.open() as handle:
        return json.load(handle)


def relax_row(dataset: str, path: Path) -> dict:
    result = load_json(path)
    test = result["test results"]
    alternative = result["fits"]["RELAX alternative"]
    null = result["fits"]["RELAX null"]
    return {
        "dataset": dataset,
        "starting_points": "1",
        "K": test[RELAX_PARAMETER],
        "LRT": test["LRT"],
        "relax_p_value": test["p-value"],
        "alternative_log_likelihood": alternative["Log Likelihood"],
        "null_log_likelihood": null["Log Likelihood"],
        "hyphy_version": result.get("runtime", "unknown"),
        "result_file": str(path),
    }


def contrast_fel_row(dataset: str, path: Path) -> dict:
    result = load_json(path)
    headers = [entry[0] for entry in result["MLE"]["headers"]]
    rows = result["MLE"]["content"]["0"]
    p_index = headers.index("P-value (overall)")
    q_index = headers.index("Q-value (overall)")
    nominal_sites = [index + 1 for index, row in enumerate(rows) if row[p_index] <= 0.05]
    fdr_sites = [index + 1 for index, row in enumerate(rows) if row[q_index] <= 0.20]
    return {
        "dataset": dataset,
        "codons_tested": len(rows),
        "nominal_p_le_0.05": len(nominal_sites),
        "fdr_q_le_0.20": len(fdr_sites),
        "nominal_sites": ",".join(map(str, nominal_sites)),
        "fdr_sites": ",".join(map(str, fdr_sites)),
        "hyphy_version": result.get("runtime", "unknown"),
        "result_file": str(path),
    }


def write_tsv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize a validated HyPhy rerun.")
    parser.add_argument("run_dir", type=Path)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()

    relax_rows = []
    contrast_rows = []
    for dataset in DATASETS:
        relax_path = run_dir / dataset / "relax_results.json"
        contrast_path = run_dir / dataset / "contrast_fel_results.json"
        relax_result = relax_row(dataset, relax_path)
        contrast_result = contrast_fel_row(dataset, contrast_path)
        relax_result["result_file"] = str(relax_path.relative_to(run_dir))
        contrast_result["result_file"] = str(contrast_path.relative_to(run_dir))
        relax_rows.append(relax_result)
        contrast_rows.append(contrast_result)

    robustness_rows = []
    pattern = re.compile(r"^(osca2|osca3_4)_sp(\d+)$")
    for path in sorted((run_dir / "robustness").glob("*_sp*/relax_results.json")):
        match = pattern.match(path.parent.name)
        if not match:
            continue
        row = relax_row(match.group(1), path)
        row["starting_points"] = match.group(2)
        row["result_file"] = str(path.relative_to(run_dir))
        robustness_rows.append(row)

    write_tsv(run_dir / "relax_summary.tsv", relax_rows)
    write_tsv(run_dir / "contrast_fel_summary.tsv", contrast_rows)
    write_tsv(run_dir / "relax_robustness_summary.tsv", robustness_rows)


if __name__ == "__main__":
    main()
