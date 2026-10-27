#!/usr/bin/env python3
"""Family-level, stratified association analysis with explicit descriptive gates.

Inputs are immutable. --out-dir must not exist. Bootstrap resamples families
within observed groups (and within strata for the conditional estimand).
Permutation tests the size/coverage-conditioned estimand on mixed strata only.
Raw effects describe the complete eligible population, not that reduced universe.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
import yaml


def truth(value):
    return str(value).strip().lower() in {"true", "1", "yes"}


def known_false(value):
    return str(value).strip().lower() in {"false", "0", "no"}


def prepare(table, species, scenario, config):
    records, audit = [], []
    for row in table.sort_values("FamilyID").to_dict("records"):
        reasons = []
        def number(key):
            try:
                value = float(row.get(key, np.nan))
                return value if np.isfinite(value) else np.nan
            except (ValueError, TypeError):
                return np.nan
        size = number(f"Count_{species}")
        denominator = number(f"{species}_Classified")
        local = number(f"{species}_Tandem") + number(f"{species}_Proximal")
        change = number(f"Change_{species}")
        mapping = number(f"{species}_Mapping_Coverage")
        coverage = number(f"{species}_Classification_Coverage")
        anchoring = number(f"{species}_Anchoring_Coverage")
        represented = number(f"{species}_Represented")
        if str(row.get("Evidence_Tier", "")).strip() not in {"A", "Tier A", "Tier_A_High_Confidence"}:
            reasons.append("not_tier_A")
        if row.get(f"{species}_Count_Status") != "match":
            reasons.append("count_discrepancy" if row.get(f"{species}_Count_Status") == "discrepant" else "count_not_assessed")
        if truth(row.get(f"{species}_QC_Conflict")):
            reasons.append("known_QC_conflict")
        if not np.isfinite(denominator) or denominator <= 0:
            reasons.append("zero_denominator" if denominator == 0 else "missing_denominator")
        if not all(np.isfinite(x) for x in (size, local, change, mapping, coverage, represented)):
            reasons.append("missing_required_measure")
        if (size < 0 or local < 0 or local > denominator or denominator > represented
                or represented != size or any(x < 0 or x > 1 for x in (mapping, coverage))):
            reasons.append("invalid_counts_or_coverage")
        if any(np.isfinite(x) and x != int(x) for x in (size, local, denominator, represented)):
            reasons.append("noninteger_count")
        if np.isfinite(represented) and represented > 0 and np.isfinite(denominator) and not np.isclose(coverage, denominator / represented):
            reasons.append("classification_coverage_discrepancy")
        class_keys = [f"{species}_{c}" for c in ("Tandem", "Proximal", "WGD", "Dispersed", "Singleton")]
        if all(k in row for k in class_keys):
            counts = [number(k) for k in class_keys]
            unclassified = number(f"{species}_Unclassified")
            if (not all(np.isfinite(x) and x >= 0 and x == int(x) for x in counts + [unclassified])
                    or sum(counts) != denominator or denominator + unclassified != represented):
                reasons.append("class_count_discrepancy")
        if scenario == "exclude_conflicts" and not known_false(row.get(f"{species}_QC_Conflict")):
            reasons.append("conflict_or_unassessed_QC")
        if scenario == "exclude_flags" and not all(known_false(row.get(k)) for k in ("Flag_Organellar", "Flag_Transposon")):
            reasons.append("flag_or_unassessed_flag")
        indicator = f"Preserved_k3_Exp_Terminal_{species}"
        if scenario in {"restrictive_terminal", "preserved_k3"}:
            if not (truth(row.get(indicator)) or known_false(row.get(indicator))):
                reasons.append("terminal_indicator_not_assessed")
            # Restrictive expansion is a distinct label contrast. k3 sensitivity
            # retains positive families only when the terminal signal persists.
            if scenario == "preserved_k3" and change > 0 and not truth(row.get(indicator)):
                reasons.append("positive_signal_not_preserved_k3")
        if scenario == "high_coverage":
            thresholds = config["high_coverage"]
            if not all(np.isfinite(x) and x >= thresholds[k] for k, x in
                       (("mapping", mapping), ("classification", coverage), ("anchoring", anchoring))):
                reasons.append("below_high_coverage_or_unassessed")
        audit.append(dict(FamilyID=row["FamilyID"], species=species, scenario=scenario,
                          eligible=not reasons, reasons=";".join(reasons), classified=denominator,
                          local=local, size=size, mapping=mapping, coverage=coverage, anchoring=anchoring))
        if not reasons:
            group = int(truth(row.get(indicator))) if scenario == "restrictive_terminal" else int(change > 0)
            records.append(dict(FamilyID=row["FamilyID"], group=group,
                                fraction=local / denominator, size=size, coverage=coverage))
    return pd.DataFrame(records, columns=["FamilyID", "group", "fraction", "size", "coverage"]), audit


def bh(values):
    valid = sorted((p, i) for i, p in enumerate(values) if p is not None)
    result = [None] * len(values)
    running = 1.0
    for rank in range(len(valid), 0, -1):
        p, index = valid[rank - 1]
        running = min(running, p * len(values) / rank)
        result[index] = running
    return result


def difference(y, groups):
    return float(y[groups == 1].mean() - y[groups == 0].mean())


def smd(a, b):
    scale = np.sqrt((np.var(a) + np.var(b)) / 2)
    delta = float(np.mean(a) - np.mean(b))
    return delta / scale if scale > 0 else (0.0 if delta == 0 else float("inf"))


def estimate(frame, config, key):
    frame = frame.sort_values("FamilyID").reset_index(drop=True).copy()
    seed = config["seed"] + int.from_bytes(hashlib.sha256(key.encode()).digest()[:4], "big")
    rng = np.random.default_rng(seed)
    result = dict(status="descriptive", reason="insufficient_groups", n=len(frame),
                  n_positive=int(frame.group.sum()), n_nonpositive=int((frame.group == 0).sum()),
                  raw_effect=None, raw_ci_low=None, raw_ci_high=None,
                  conditional_effect=None, conditional_ci_low=None, conditional_ci_high=None,
                  p_value=None, permutable_fraction=0.0)
    strata, balance = [], []
    if frame.empty or frame.group.nunique() != 2:
        return result, strata, balance
    y, g = frame.fraction.to_numpy(), frame.group.to_numpy()
    result["raw_effect"] = difference(y, g)
    raw_boot = [float(rng.choice(y[g == 1], len(y[g == 1]), replace=True).mean()
                      - rng.choice(y[g == 0], len(y[g == 0]), replace=True).mean())
                for _ in range(config["bootstrap"])]
    result["raw_ci_low"], result["raw_ci_high"] = map(float, np.quantile(raw_boot, [0.025, 0.975]))
    frame["size_bin"] = pd.cut(frame["size"], config["size_edges"], right=False, include_lowest=True)
    frame["coverage_bin"] = pd.cut(frame["coverage"], config["coverage_edges"], right=False, include_lowest=True)
    blocks = []
    for (size_bin, coverage_bin), block in frame.groupby(["size_bin", "coverage_bin"], observed=True, sort=True):
        counts = block.group.value_counts()
        mixed = all(counts.get(i, 0) >= config["min_per_group"] for i in (0, 1))
        strata.append(dict(size_interval=str(size_bin), coverage_interval=str(coverage_bin),
                           n=len(block), positive=int(counts.get(1, 0)), nonpositive=int(counts.get(0, 0)), mixed=mixed))
        if mixed:
            blocks.append(block)
    total = sum(len(b) for b in blocks)
    result["permutable_fraction"] = total / len(frame)
    if not blocks:
        result["reason"] = "no_mixed_strata"
        return result, strata, balance
    weighted = lambda labels: float(sum(len(b) / total * difference(b.fraction.to_numpy(), lab) for b, lab in zip(blocks, labels)))
    labels = [b.group.to_numpy() for b in blocks]
    observed = weighted(labels)
    result["conditional_effect"] = observed
    bootstrap = []
    for _ in range(config["bootstrap"]):
        bootstrap.append(sum(len(b) / total * (rng.choice(b.loc[b.group == 1, "fraction"], int((b.group == 1).sum()), replace=True).mean()
                                              - rng.choice(b.loc[b.group == 0, "fraction"], int((b.group == 0).sum()), replace=True).mean()) for b in blocks))
    result["conditional_ci_low"], result["conditional_ci_high"] = map(float, np.quantile(bootstrap, [0.025, 0.975]))
    balanced = True
    for index, block in enumerate(blocks):
        for covariate in ("size", "coverage"):
            value = smd(block.loc[block.group == 1, covariate], block.loc[block.group == 0, covariate])
            passed = abs(value) <= config["max_abs_smd"]
            balanced &= passed
            balance.append(dict(stratum=index, covariate=covariate, smd=value, passed=passed))
    if not balanced:
        result["reason"] = "covariate_imbalance"
    elif total / len(frame) < config["min_permutable_fraction"]:
        result["reason"] = "insufficient_permutable_fraction"
    else:
        extreme = sum(abs(weighted([rng.permutation(lab) for lab in labels])) >= abs(observed) - 1e-12
                      for _ in range(config["permutations"]))
        result.update(status="inferential", reason="passed_gates", p_value=(extreme + 1) / (config["permutations"] + 1))
    return result, strata, balance


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--family-evidence", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    if args.out_dir.exists():
        parser.error("--out-dir must be a NEW directory")
    config = yaml.safe_load(args.config.read_text())
    if config.get("schema_version") != 1 or config.get("species") != ["Vper", "Vtub"]:
        parser.error("unsupported schema or primary species family")
    expected = ["primary", "restrictive_terminal", "exclude_conflicts", "exclude_flags", "preserved_k3", "high_coverage"]
    if config.get("scenarios") != expected:
        parser.error("scenario families must match the frozen design")
    for name in ("bootstrap", "permutations", "min_per_group"):
        if not isinstance(config.get(name), int) or config[name] < 1:
            parser.error(f"{name} must be a positive integer")
    for name in ("size_edges", "coverage_edges"):
        edges = config[name]
        if len(edges) < 2 or any(b <= a for a, b in zip(edges, edges[1:])):
            parser.error(f"{name} must be strictly increasing")
    if not isinstance(config.get("seed"), int) or config["seed"] < 0:
        parser.error("seed must be a nonnegative integer")
    if not 0 <= config.get("min_permutable_fraction", -1) <= 1 or config.get("max_abs_smd", -1) < 0:
        parser.error("invalid balance/permutability gates")
    if set(config.get("high_coverage", {})) != {"mapping", "classification", "anchoring"} or not all(0 <= x <= 1 for x in config["high_coverage"].values()):
        parser.error("invalid frozen high coverage thresholds")
    testing = config.get("multiple_testing", {})
    if testing.get("method") != "BH" or testing.get("primary") != config["species"] or testing.get("secondary_families") != expected[1:]:
        parser.error("multiple-testing declaration does not match analysis families")
    table = pd.read_csv(args.family_evidence, sep="\t", dtype={"FamilyID": str}, low_memory=False)
    required = {"FamilyID", "Evidence_Tier", "Flag_Organellar", "Flag_Transposon"}
    for sp in config["species"]:
        required.update({f"Count_{sp}", f"Change_{sp}", f"Preserved_k3_Exp_Terminal_{sp}"})
        required.update(f"{sp}_{field}" for field in ("Classified", "Represented", "Tandem", "Proximal", "WGD", "Dispersed", "Singleton", "Unclassified", "Mapping_Coverage", "Classification_Coverage", "Anchoring_Coverage", "Count_Status", "QC_Conflict"))
    if required - set(table.columns):
        parser.error("missing columns: " + ", ".join(sorted(required - set(table.columns))))
    if table.FamilyID.isna().any() or table.FamilyID.duplicated().any():
        parser.error("FamilyID must be nonmissing and unique")
    results, audits, strata_rows, balance_rows, distributions = [], [], [], [], []
    for scenario in config["scenarios"]:
        family = []
        for species in config["species"]:
            frame, audit = prepare(table, species, scenario, config)
            result, strata, balance = estimate(frame, config, f"{scenario}:{species}")
            result.update(species=species, scenario=scenario, test_family=scenario)
            family.append(result)
            audits.extend(audit)
            strata_rows.extend(dict(species=species, scenario=scenario, **r) for r in strata)
            balance_rows.extend(dict(species=species, scenario=scenario, **r) for r in balance)
            distributions.extend(dict(species=species, scenario=scenario, **r) for r in frame.to_dict("records"))
        for result, q in zip(family, bh([r["p_value"] for r in family])):
            result["q_value"] = q
        results.extend(family)
    args.out_dir.mkdir(parents=True, exist_ok=False)
    for name, rows in (("association_results", results), ("eligibility", audits), ("strata", strata_rows), ("covariate_balance_qc", balance_rows), ("family_distributions", distributions)):
        pd.DataFrame(rows).to_csv(args.out_dir / f"{name}.tsv", sep="\t", index=False)
    (args.out_dir / "frozen_config.yaml").write_text(args.config.read_text())
    manifest = {"inputs": {str(p.resolve()): hashlib.sha256(p.read_bytes()).hexdigest() for p in (args.family_evidence, args.config)},
                "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "versions": {"numpy": np.__version__, "pandas": pd.__version__, "pyyaml": yaml.__version__},
                "limitations": config.get("interpretation"), "inference": "two-sided stratified permutation; BH within each declared two-species family", "bootstrap": "family resampling within groups; conditional intervals also within fixed strata"}
    (args.out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()
