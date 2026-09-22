#!/usr/bin/env python3
"""
Evaluate and select the most stable error model from CAFE5 Base model replicates.
Extracts lambda, epsilon, and -lnL from logs and Base_report.cafe.
Chapter: Macroevolution and Genomics in Velloziaceae
"""

import os
import sys
import glob
import re
import shutil
import pandas as pd

def parse_base_run(rep_dir):
    report_file = os.path.join(rep_dir, "Base_report.cafe")
    err_file = os.path.join(rep_dir, "Base_error_model.txt")
    
    if not os.path.exists(report_file) or not os.path.exists(err_file):
        return None
        
    lambda_val = None
    score_lnL = None
    epsilon_val = None
    
    # Parse Base_report.cafe
    with open(report_file, "r") as f:
        for line in f:
            if line.startswith("Lambda:"):
                parts = line.strip().split()
                if len(parts) >= 2:
                    lambda_val = float(parts[1])
            elif "Score (-lnL):" in line:
                m = re.search(r"Score \(-lnL\):\s*([0-9\.]+)", line)
                if m:
                    score_lnL = float(m.group(1))
                    
    # Parse Base_error_model.txt for epsilon
    with open(err_file, "r") as f:
        err_lines = [l.strip().split() for l in f if l.strip()]
        if len(err_lines) >= 2:
            try:
                diag_p = float(err_lines[1][1])
                epsilon_val = (1.0 - diag_p) / 2.0
            except Exception:
                epsilon_val = None
                
    return {
        "dir": rep_dir,
        "report": report_file,
        "error_file": err_file,
        "lambda": lambda_val,
        "score_lnL": score_lnL,
        "epsilon_approx": epsilon_val
    }

def main():
    base_dir = "/home/mfcaval/github/doutorado/chapter_macroevolution/04_gene_families"
    err_reps_dir = os.path.join(base_dir, "cafe5_results", "rerun", "02_base_error")
    error_models_dir = os.path.join(base_dir, "error_models")
    summary_dir = os.path.join(base_dir, "summary")
    os.makedirs(error_models_dir, exist_ok=True)
    os.makedirs(summary_dir, exist_ok=True)
    
    rep_dirs = sorted(glob.glob(os.path.join(err_reps_dir, "rep*")))
    if not rep_dirs:
        print(f"[ERROR] No replicates found in {err_reps_dir}")
        sys.exit(1)
        
    results = []
    for rdir in rep_dirs:
        rep_name = os.path.basename(rdir)
        info = parse_base_run(rdir)
        if info:
            info["replicate"] = rep_name
            results.append(info)
            # Archive individual error models
            dest_err = os.path.join(error_models_dir, f"Base_error_model_{rep_name}.txt")
            shutil.copyfile(info["error_file"], dest_err)
        else:
            print(f"[WARN] Incomplete run in {rdir}")
            
    if not results:
        print("[ERROR] No valid finished replicates found.")
        sys.exit(1)
        
    df = pd.DataFrame(results)
    summary_tsv = os.path.join(summary_dir, "base_error_replicates_summary.tsv")
    df[["replicate", "lambda", "score_lnL", "epsilon_approx"]].to_csv(summary_tsv, sep="\t", index=False)
    print(f"[INFO] Saved summary of error replicates to: {summary_tsv}")
    print(df[["replicate", "lambda", "score_lnL", "epsilon_approx"]].to_string())
    
    # Sort by score_lnL (lowest -lnL = highest likelihood)
    best_rep = df.sort_values(by="score_lnL").iloc[0]
    best_err_src = best_rep["error_file"]
    selected_dest = os.path.join(error_models_dir, "selected_error_model.txt")
    shutil.copyfile(best_err_src, selected_dest)
    
    print("=" * 70)
    print(f"[SUCCESS] Selected Error Model from: {best_rep['replicate']}")
    print(f"          Lambda: {best_rep['lambda']}")
    print(f"          -lnL:   {best_rep['score_lnL']}")
    print(f"          Destination: {selected_dest}")
    print("=" * 70)

if __name__ == "__main__":
    main()
