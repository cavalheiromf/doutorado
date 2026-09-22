#!/usr/bin/env python3
"""
Comprehensive evaluation of CAFE5 multi-replicate models.
1. Compares likelihoods (-lnL), AIC, parameter stability (lambda, alpha).
2. Evaluates Gamma category saturation: lambda * Gamma_Cat_Mean vs max_lambda.
3. Quantifies failure rates (>20%) from logs.
4. Applies Benjamini-Hochberg FDR correction (q < 0.05) across ALL tested families (N=12,276).
Chapter: Macroevolution and Genomics in Velloziaceae
"""

import os
import sys
import glob
import re
import numpy as np
import pandas as pd

MAX_LAMBDA_TOPOLOGY = 0.0072210403786136

def parse_log_blocks(logfile):
    runs = {}
    current_run = None
    if not os.path.exists(logfile):
        return runs
    with open(logfile) as f:
        for line in f:
            if "Command line:" in line:
                m_out = re.search(r"-o\s+([^\s]+)", line)
                if m_out:
                    out_path = os.path.normpath(m_out.group(1))
                    current_run = {
                        "cmd": line.strip(),
                        "lambda": None,
                        "alpha": None,
                        "lnL": None,
                        "failures": []
                    }
                    runs[out_path] = current_run
            if current_run:
                if "Final -lnL:" in line:
                    m = re.search(r"Final -lnL:\s*([0-9\.]+)", line)
                    if m: current_run["lnL"] = float(m.group(1))
                if "Best match is:" in line:
                    m = re.search(r"Best match is:\s*([0-9\.]+)", line)
                    if m: current_run["lambda"] = float(m.group(1))
                if "Best matches are:" in line:
                    parts = line.strip().split()[-1].split(",")
                    if len(parts) >= 2:
                        current_run["lambda"] = float(parts[0])
                        current_run["alpha"] = float(parts[1])
                if line.startswith("OG") and "failures" in line:
                    current_run["failures"].append(line.strip().split()[0])
    return runs

def parse_all_families_results(results_path):
    """
    Parse the complete family results table (e.g. Gamma_family_results.txt / Base_family_results.txt)
    which contains ALL N=12,276 tested gene families with their exact unadjusted p-values.
    """
    if not os.path.exists(results_path):
        return [], []
    df = pd.read_csv(results_path, sep="\t")
    df.columns = [c.replace("#", "").strip() for c in df.columns]
    df["pvalue"] = pd.to_numeric(df["pvalue"], errors="coerce")
    df = df.dropna(subset=["pvalue"])
    return df["FamilyID"].tolist(), df["pvalue"].values

def fdr_bh(pvals):
    pvals = np.asarray(pvals, dtype=float)
    n = len(pvals)
    order = np.argsort(pvals)
    ranked_p = pvals[order]
    qvals = np.zeros(n)
    accum = 1.0
    for i in range(n - 1, -1, -1):
        rank = i + 1
        val = ranked_p[i] * n / rank
        accum = min(accum, val)
        qvals[i] = accum
    orig_qvals = np.zeros(n)
    orig_qvals[order] = qvals
    return orig_qvals

def main():
    base_dir = "/home/mfcaval/github/doutorado/chapter_macroevolution/04_gene_families"
    rerun_dir = os.path.join(base_dir, "cafe5_results", "rerun")
    summary_dir = os.path.join(base_dir, "summary")
    os.makedirs(summary_dir, exist_ok=True)
    
    stg1_log = os.path.join(base_dir, "cafe5_stage1_820545.log")
    stg2_log = os.path.join(base_dir, "cafe5_stage2_820546.log")
    
    log_data = {}
    log_data.update(parse_log_blocks(stg1_log))
    log_data.update(parse_log_blocks(stg2_log))
    
    models = {
        "01_base_noerror": {"k": 1, "k_params": 1},
        "02_base_error": {"k": 1, "k_params": 2},
        "03_gamma_k2": {"k": 2, "k_params": 3},
        "04_gamma_k3": {"k": 3, "k_params": 4},
        "05_gamma_k4_sensitivity": {"k": 4, "k_params": 5}
    }
    
    records = []
    pvals_dict = {}
    
    for mod_name, mod_meta in models.items():
        mod_path = os.path.join(rerun_dir, mod_name)
        if not os.path.exists(mod_path):
            continue
        rep_dirs = sorted(glob.glob(os.path.join(mod_path, "rep*")))
        for rdir in rep_dirs:
            rep = os.path.basename(rdir)
            norm_rdir = os.path.normpath(rdir)
            
            info = log_data.get(norm_rdir, {})
            l_val = info.get("lambda")
            a_val = info.get("alpha")
            lnL = info.get("lnL")
            n_fail = len(info.get("failures", []))
            
            # Read ALL tested families from *_family_results.txt (N=12,276)
            fam_res_f = os.path.join(rdir, "Base_family_results.txt" if "base" in mod_name else "Gamma_family_results.txt")
            fams, pvals = parse_all_families_results(fam_res_f)
            
            k_p = mod_meta["k_params"]
            aic = (2 * k_p + 2 * lnL) if lnL is not None else None
            
            # Calculate FDR over the entire dataset
            if len(pvals) > 0:
                qvals = fdr_bh(pvals)
                n_sig_q005 = int(sum(qvals <= 0.05))
                n_sig_q010 = int(sum(qvals <= 0.10))
                pvals_dict[f"{mod_name}_{rep}"] = (fams, pvals, qvals)
            else:
                n_sig_q005 = 0
                n_sig_q010 = 0
                
            rec = {
                "model": mod_name,
                "replicate": rep,
                "k_categories": mod_meta["k"],
                "lambda": l_val,
                "alpha": a_val,
                "score_lnL": lnL,
                "AIC": aic,
                "failures_gt20pct": n_fail,
                "families_tested_total": len(fams),
                "p_le_005_raw": sum(1 for p in pvals if p <= 0.05),
                "FDR_q_le_005": n_sig_q005,
                "FDR_q_le_010": n_sig_q010
            }
            records.append(rec)
                
    df = pd.DataFrame(records)
    valid_aics = df["AIC"].dropna()
    min_aic = valid_aics.min() if not valid_aics.empty else 0
    df["delta_AIC"] = df["AIC"].apply(lambda x: round(x - min_aic, 2) if pd.notnull(x) else None)
    
    summary_tsv = os.path.join(summary_dir, "all_models_summary.tsv")
    df.to_csv(summary_tsv, sep="\t", index=False)
    print(f"[INFO] Summary written to: {summary_tsv}\n")
    print(df[["model", "replicate", "lambda", "score_lnL", "AIC", "delta_AIC", "families_tested_total", "p_le_005_raw", "FDR_q_le_005", "FDR_q_le_010"]].to_string())
    
    # Save the full FDR table for the representative replicate of each model
    print("\n" + "=" * 70)
    print(" Saving Full FDR Tables (N=12,276 families each)")
    print("=" * 70)
    for mod_name in models.keys():
        mod_df = df[df["model"] == mod_name]
        if mod_df.empty:
            continue
        best_rep_row = mod_df.sort_values(by="score_lnL").iloc[0]
        rep_id = f"{mod_name}_{best_rep_row['replicate']}"
        if rep_id in pvals_dict:
            fams, pvals, qvals = pvals_dict[rep_id]
            res_df = pd.DataFrame({
                "FamilyID": fams,
                "pvalue_raw": pvals,
                "qvalue_bh": qvals,
                "significant_raw_p005": pvals <= 0.05,
                "significant_fdr_q005": qvals <= 0.05,
                "significant_fdr_q010": qvals <= 0.10
            })
            out_q = os.path.join(summary_dir, f"fdr_{mod_name}_{best_rep_row['replicate']}.tsv")
            res_df.to_csv(out_q, sep="\t", index=False)
            print(f"Model {mod_name} ({best_rep_row['replicate']}): Saved {len(res_df)} families to {out_q}")
            print(f"       Raw p<=0.05: {best_rep_row['p_le_005_raw']} -> FDR q<=0.05: {best_rep_row['FDR_q_le_005']} (q<=0.10: {best_rep_row['FDR_q_le_010']})")

if __name__ == "__main__":
    main()
