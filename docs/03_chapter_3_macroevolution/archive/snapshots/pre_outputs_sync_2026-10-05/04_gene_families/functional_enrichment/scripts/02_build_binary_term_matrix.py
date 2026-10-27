#!/usr/bin/env python3
"""
Step 2: Build binary FamilyID-term association matrix and fine-scale permutation strata.
Strictly implements:
- Validation Control 2: Uniqueness of (FamilyID, Term_ID) pairs
- Precise locus-term tracking of non-IEA evidence per (FamilyID, Term_ID) pair
- Exclusion of root GO terms (GO:0008150, GO:0003674, GO:0005575)
- Multi-dimensional fine stratification for General Contrast (Tier A vs Universe):
    17 Total_Count bins x 10 Count_Ath bins x 10 Annotation_Degree bins
- Contrast-specific propensity score stratification for Conditional Contrasts (within Tier A):
    Penalized logistic propensity score balancing Total_Count, Count_Ath, and Annotation_Degree
- Covariate balance audit: exports intermediate/covariate_balance_qc.tsv demonstrating SMD < 0.10
- Outputs: intermediate/family_term_matrix.tsv, intermediate/permutation_strata.tsv, intermediate/covariate_balance_qc.tsv
"""

import os
import sys
import yaml
import numpy as np
import pandas as pd
from collections import defaultdict
from scipy.optimize import minimize

ROOT_TERMS = {"GO:0008150", "GO:0003674", "GO:0005575"}

def parse_obo_names(obo_path):
    print(f"[*] Extracting term names from OBO: {obo_path}")
    names = {}
    current_id = None
    with open(obo_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "[Term]":
                current_id = None
            elif line.startswith("id: GO:"):
                current_id = line.split("id: ")[1].strip()
            elif current_id and line.startswith("name: "):
                names[current_id] = line.split("name: ")[1].strip()
    return names

def parse_kegg_names(list_path):
    print(f"[*] Extracting pathway names from KEGG list: {list_path}")
    names = {}
    with open(list_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                pid = parts[0].replace("path:", "").strip()
                pname = parts[1].split(" - ")[0].strip()
                names[pid] = pname
    return names

def compute_smd(x1, x0, s_pool):
    if s_pool == 0 or np.isnan(s_pool):
        return 0.0
    return (np.mean(x1) - np.mean(x0)) / s_pool

def main():
    base_dir = "/home/mfcaval/github/doutorado/chapter_macroevolution/04_gene_families/functional_enrichment"
    macro_dir = "/home/mfcaval/github/doutorado/chapter_macroevolution"
    inter_dir = os.path.join(base_dir, "intermediate")
    os.makedirs(inter_dir, exist_ok=True)
    
    config_file = os.path.join(base_dir, "config", "enrichment_config.yaml")
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)
        
    master_file = os.path.join(macro_dir, "04_gene_families", "comparative_axes", "comparative_families_master_table_v2.tsv")
    df_master = pd.read_csv(master_file, sep="\t").set_index("FamilyID")
    tier_a_fams = set(df_master[df_master["Evidence_Tier"] == "Tier_A_High_Confidence"].index)
    
    ann_file = os.path.join(base_dir, "orthogroup_functional_annotations.tsv")
    print(f"[*] Loading master annotations: {ann_file}")
    df_ann = pd.read_csv(ann_file, sep="\t").set_index("FamilyID")
    
    obo_file = os.path.join(base_dir, "raw_annotations", "go-basic.obo")
    go_names = parse_obo_names(obo_file)
    kegg_list_file = os.path.join(base_dir, "raw_annotations", "kegg", "ath_pathway_list.tsv")
    kegg_names = parse_kegg_names(kegg_list_file)
    
    # -------------------------------------------------------------
    # 1. Build Unique Binary Associations Matrix with Per-Term Non-IEA
    # -------------------------------------------------------------
    print("[*] Constructing binary term matrix with per-(family, term) non-IEA evidence...")
    records = []
    pair_tracker = set()
    family_term_count = defaultdict(int)
    
    for fam_id, row in df_ann.iterrows():
        # Sets of non-IEA supported terms for this family
        non_iea_dir_terms = set(str(row["GO_Non_IEA_Direct_Terms"]).split(";")) if pd.notna(row["GO_Non_IEA_Direct_Terms"]) else set()
        non_iea_prop_terms = set(str(row["GO_Non_IEA_Propagated_Terms"]).split(";")) if pd.notna(row["GO_Non_IEA_Propagated_Terms"]) else set()
        non_iea_dir_terms = {t.strip() for t in non_iea_dir_terms if t.strip() and t.strip() not in ROOT_TERMS}
        non_iea_prop_terms = {t.strip() for t in non_iea_prop_terms if t.strip() and t.strip() not in ROOT_TERMS}
        
        # Helper to process GO categories
        for cat, col_dir, col_prop in [
            ("GO_BP", "GO_BP_Direct", "GO_BP_Propagated"),
            ("GO_MF", "GO_MF_Direct", "GO_MF_Propagated"),
            ("GO_CC", "GO_CC_Direct", "GO_CC_Propagated")
        ]:
            dir_set = set(str(row[col_dir]).split(";")) if pd.notna(row[col_dir]) else set()
            prop_set = set(str(row[col_prop]).split(";")) if pd.notna(row[col_prop]) else set()
            dir_set = {t.strip() for t in dir_set if t.strip() and t.strip() not in ROOT_TERMS}
            prop_set = {t.strip() for t in prop_set if t.strip() and t.strip() not in ROOT_TERMS}
            all_terms = dir_set | prop_set
            
            for t in all_terms:
                pair_key = (fam_id, t)
                if pair_key in pair_tracker:
                    raise ValueError(f"Control 2 Violation: Duplicate pair {pair_key}")
                pair_tracker.add(pair_key)
                
                is_dir = (t in dir_set)
                is_prop = (t in prop_set)
                
                # Precise per-term Non-IEA classification:
                # If term is evaluated in propagated mode, non_iea_prop_terms applies;
                # if evaluated in direct mode, non_iea_dir_terms applies.
                # Here we record whether the association has non-IEA evidence in either mode.
                has_non_iea = (t in non_iea_prop_terms) or (t in non_iea_dir_terms)
                
                records.append({
                    "FamilyID": fam_id,
                    "Term_ID": t,
                    "Term_Name": go_names.get(t, t),
                    "Category": cat,
                    "Is_Direct": is_dir,
                    "Is_Propagated": is_prop,
                    "Has_Non_IEA": has_non_iea,
                    "Has_Non_IEA_Direct": (t in non_iea_dir_terms),
                    "Has_Non_IEA_Propagated": (t in non_iea_prop_terms)
                })
                family_term_count[fam_id] += 1
                
        # KEGG Pathways (Non-hierarchical, Has_Non_IEA is False/Not Applicable)
        kegg_set = set(str(row["KEGG_Pathways"]).split(";")) if pd.notna(row["KEGG_Pathways"]) else set()
        kegg_set = {t.strip() for t in kegg_set if t.strip()}
        for t in kegg_set:
            pair_key = (fam_id, t)
            if pair_key in pair_tracker:
                raise ValueError(f"Control 2 Violation: Duplicate pair {pair_key}")
            pair_tracker.add(pair_key)
            records.append({
                "FamilyID": fam_id,
                "Term_ID": t,
                "Term_Name": kegg_names.get(t, t),
                "Category": "KEGG",
                "Is_Direct": True,
                "Is_Propagated": False,
                "Has_Non_IEA": False,
                "Has_Non_IEA_Direct": False,
                "Has_Non_IEA_Propagated": False
            })
            family_term_count[fam_id] += 1
            
    df_matrix = pd.DataFrame(records)
    matrix_out = os.path.join(inter_dir, "family_term_matrix.tsv")
    df_matrix.to_csv(matrix_out, sep="\t", index=False)
    print(f"[*] Saved Binary Associations: {matrix_out} ({len(df_matrix)} rows)")
    print(f"    Validation Control 2: PASSED. Zero duplicate pairs found.")
    
    # Check non-IEA term statistics
    go_mask = df_matrix["Category"].str.startswith("GO")
    total_go_pairs = go_mask.sum()
    non_iea_pairs = (go_mask & df_matrix["Has_Non_IEA"]).sum()
    print(f"    GO term associations: {total_go_pairs:,}; Non-IEA supported: {non_iea_pairs:,} ({non_iea_pairs/total_go_pairs*100:.2f}%)")
    
    # -------------------------------------------------------------
    # -------------------------------------------------------------
    # 2. Build Defragmented Multi-Dimensional Strata for Universe
    # -------------------------------------------------------------
    print("\n[*] Constructing defragmented multi-dimensional strata for universe...")
    
    df_strata = pd.DataFrame(index=df_master.index)
    df_strata["N_Proteins_Total"] = df_master["Total_Count"]
    df_strata["N_Ath_Loci"] = df_ann.loc[df_master.index, "N_Ath_Loci"].fillna(0).astype(int)
    df_strata["Annotation_Degree"] = [family_term_count[f] for f in df_master.index]
    
    # 16 Total_Count bins x 6 Count_Ath bins x 6 Annotation_Degree bins
    tot_bins = [-1, 5, 10, 15, 20, 25, 30, 35, 45, 60, 80, 110, 150, 220, 350, 600, 100000]
    ath_bins = [-1, 1, 2, 4, 7, 12, 10000]
    deg_bins = [-1, 5, 12, 25, 45, 80, 10000]
    
    df_strata["b_tot"] = pd.cut(df_strata["N_Proteins_Total"], bins=tot_bins, labels=False)
    df_strata["b_ath"] = pd.cut(df_strata["N_Ath_Loci"], bins=ath_bins, labels=False)
    df_strata["b_deg"] = pd.cut(df_strata["Annotation_Degree"], bins=deg_bins, labels=False)
    
    df_strata["raw_stratum"] = df_strata["b_tot"].astype(str) + "_" + df_strata["b_ath"].astype(str) + "_" + df_strata["b_deg"].astype(str)
    
    is_tier_a_arr = (df_master["Evidence_Tier"] == "Tier_A_High_Confidence").astype(int).values
    strata_map = {k: k for k in df_strata["raw_stratum"].unique()}
    
    def recompute_grp(current_map):
        st = df_strata["raw_stratum"].map(current_map)
        g = pd.DataFrame({"st": st, "is_tier_a": is_tier_a_arr}).groupby("st")["is_tier_a"].agg(["count", "sum"])
        g["n_bg"] = g["count"] - g["sum"]
        return g
        
    grp = recompute_grp(strata_map)
    for st in list(grp.index):
        if grp.loc[st, "n_bg"] < 2 and grp.loc[st, "sum"] > 0:
            parts = [int(x) for x in st.split("_")]
            best_cand = None
            min_dist = 9999
            for cand in grp.index:
                if grp.loc[cand, "n_bg"] >= 2:
                    c_parts = [int(x) for x in cand.split("_")]
                    d = abs(c_parts[0] - parts[0])*50 + abs(c_parts[1] - parts[1])*5 + abs(c_parts[2] - parts[2])*1
                    if d < min_dist:
                        min_dist = d
                        best_cand = cand
            if best_cand is not None:
                for k, v in strata_map.items():
                    if v == st:
                        strata_map[k] = best_cand
                grp = recompute_grp(strata_map)
                
    df_strata["Stratum_General"] = df_strata["raw_stratum"].map(strata_map)
    print(f"    Defragmented universe strata created: {df_strata['Stratum_General'].nunique()} unique strata.")
    
    # -------------------------------------------------------------
    # 3. Category-Specific Propensity Score Strata for Conditional Contrasts
    # -------------------------------------------------------------
    tier_a_df = df_strata.loc[list(tier_a_fams)].copy()
    tier_a_master = df_master.loc[list(tier_a_fams)].copy()
    
    contrasts_list = config["contrasts"]["primary"] + config["contrasts"]["external_controls"] + config["contrasts"]["descriptive_only"]
    balance_qc_rows = []
    
    eval_categories = [
        ("Overall", "Overall", set(df_master.index)),
        ("GO_BP", "GO_BP_Propagated", set(df_matrix[(df_matrix["Category"] == "GO_BP") & (df_matrix["Is_Propagated"] == True)]["FamilyID"])),
        ("GO_MF", "GO_MF_Propagated", set(df_matrix[(df_matrix["Category"] == "GO_MF") & (df_matrix["Is_Propagated"] == True)]["FamilyID"])),
        ("GO_CC", "GO_CC_Propagated", set(df_matrix[(df_matrix["Category"] == "GO_CC") & (df_matrix["Is_Propagated"] == True)]["FamilyID"])),
        ("KEGG", "KEGG_Direct", set(df_matrix[(df_matrix["Category"] == "KEGG") & (df_matrix["Is_Direct"] == True)]["FamilyID"]))
    ]
    
    # 1. Audit General Contrast across categories
    for cat_name, cat_label, cat_fams in eval_categories:
        sub_strata = df_strata.loc[list(cat_fams)]
        sub_master = df_master.loc[list(cat_fams)]
        fg_mask = sub_master["Evidence_Tier"] == "Tier_A_High_Confidence"
        fg_sub = sub_strata[fg_mask]
        bg_sub = sub_strata[~fg_mask]
        
        if len(fg_sub) == 0 or len(bg_sub) == 0:
            continue
            
        n_fg_s = fg_sub.groupby("Stratum_General").size()
        
        cat_mat = df_matrix[df_matrix["Category"] == cat_name] if cat_name in ["GO_BP", "GO_MF", "GO_CC", "KEGG"] else df_matrix
        cat_deg_dict = cat_mat.groupby("FamilyID")["Term_ID"].nunique().to_dict()
        sub_cat_deg = np.array([cat_deg_dict.get(f, 0) for f in sub_strata.index])
        
        for var, var_label, vals_all in [
            ("N_Proteins_Total", "Total_Count", sub_strata["N_Proteins_Total"].values),
            ("N_Ath_Loci", "Count_Ath", sub_strata["N_Ath_Loci"].values),
            ("Annotation_Degree", "Annotation_Degree", sub_cat_deg)
        ]:
            fg_vals = vals_all[fg_mask.values]
            bg_vals = vals_all[(~fg_mask).values]
            s_pool = np.sqrt((np.var(fg_vals, ddof=1) + np.var(bg_vals, ddof=1)) / 2.0)
            
            s_series = pd.Series(vals_all, index=sub_strata.index)
            mean_s = s_series.groupby(sub_strata["Stratum_General"]).mean()
            exp_mean = (n_fg_s * mean_s[n_fg_s.index]).sum() / len(fg_sub)
            
            smd_raw = compute_smd(fg_vals, bg_vals, s_pool)
            smd_adj = compute_smd(fg_vals, exp_mean, s_pool)
            
            balance_qc_rows.append({
                "Contrast_ID": "Core_Tier_A_General",
                "Category": cat_label,
                "Variable": var_label,
                "FG_Mean": float(np.mean(fg_vals)),
                "BG_Raw_Mean": float(np.mean(bg_vals)),
                "BG_Adjusted_Mean": float(exp_mean),
                "Pooled_SD": float(s_pool),
                "Raw_SMD": float(smd_raw),
                "Adjusted_SMD": float(smd_adj),
                "Balance_Achieved_lt_0_10": bool(abs(smd_adj) < 0.10)
            })
            
    # 2. Build Category-Specific Strata and Audit Conditional Contrasts within Tier A
    for c_info in contrasts_list:
        cid = c_info["id"]
        if c_info["bg_universe"] == "all_annotated_in_category":
            continue
            
        for cat_name, cat_label, cat_fams in eval_categories:
            cat_sfx = "BP" if "BP" in cat_label else ("MF" if "MF" in cat_label else ("CC" if "CC" in cat_label else ("KEGG" if "KEGG" in cat_label else "Overall")))
            col_name = f"Stratum_PS_{cid}_{cat_sfx}"
            
            sub_tier_a_fams = sorted(list(tier_a_fams & cat_fams))
            if len(sub_tier_a_fams) < 5:
                continue
                
            sub_tier_a_df = df_strata.loc[sub_tier_a_fams].copy()
            sub_tier_a_master = df_master.loc[sub_tier_a_fams].copy()
            fg_mask_cond = sub_tier_a_master.eval(c_info["fg_condition"])
            n_fg = fg_mask_cond.sum()
            n_bg = len(sub_tier_a_fams) - n_fg
            
            cat_mat = df_matrix[df_matrix["Category"] == cat_name] if cat_name in ["GO_BP", "GO_MF", "GO_CC", "KEGG"] else df_matrix
            cat_deg_dict = cat_mat.groupby("FamilyID")["Term_ID"].nunique().to_dict()
            sub_tier_a_df["Cat_Degree"] = [cat_deg_dict.get(f, 0) for f in sub_tier_a_fams]
            
            if n_fg < 3 or n_bg < 3:
                # Default to fallback stratum
                df_strata.loc[sub_tier_a_fams, col_name] = df_strata.loc[sub_tier_a_fams, "Stratum_General"]
                for var, var_label in [("N_Proteins_Total", "Total_Count"), ("N_Ath_Loci", "Count_Ath"), ("Cat_Degree", "Annotation_Degree")]:
                    balance_qc_rows.append({
                        "Contrast_ID": cid,
                        "Category": cat_label,
                        "Variable": var_label,
                        "FG_Mean": float(np.mean(sub_tier_a_df.loc[fg_mask_cond, var])) if n_fg > 0 else 0.0,
                        "BG_Raw_Mean": float(np.mean(sub_tier_a_df.loc[~fg_mask_cond, var])) if n_bg > 0 else 0.0,
                        "BG_Adjusted_Mean": np.nan,
                        "Pooled_SD": np.nan,
                        "Raw_SMD": np.nan,
                        "Adjusted_SMD": np.nan,
                        "Balance_Achieved_lt_0_10": False
                    })
                continue
                
            # Fit penalized logistic propensity score within this category universe
            Z = np.column_stack([
                np.ones(len(sub_tier_a_df)),
                (np.log1p(sub_tier_a_df["N_Proteins_Total"]) - np.mean(np.log1p(sub_tier_a_df["N_Proteins_Total"]))) / (np.std(np.log1p(sub_tier_a_df["N_Proteins_Total"])) + 1e-6),
                (np.log1p(sub_tier_a_df["N_Ath_Loci"]) - np.mean(np.log1p(sub_tier_a_df["N_Ath_Loci"]))) / (np.std(np.log1p(sub_tier_a_df["N_Ath_Loci"])) + 1e-6),
                (np.log1p(sub_tier_a_df["Cat_Degree"]) - np.mean(np.log1p(sub_tier_a_df["Cat_Degree"]))) / (np.std(np.log1p(sub_tier_a_df["Cat_Degree"])) + 1e-6)
            ])
            y = fg_mask_cond.values.astype(float)
            
            def nll(w):
                z = Z.dot(w)
                p = 1.0 / (1.0 + np.exp(-np.clip(z, -25, 25)))
                eps = 1e-12
                return -np.sum(y * np.log(p + eps) + (1.0 - y) * np.log(1.0 - p + eps)) + 0.1 * np.sum(w[1:]**2)
                
            res = minimize(nll, np.zeros(Z.shape[1]), method="BFGS")
            ps = 1.0 / (1.0 + np.exp(-Z.dot(res.x)))
            
            n_strata = max(2, min(4, int(n_fg // 4) + 1))
            strata_series = pd.qcut(ps, q=n_strata, duplicates="drop").astype(str)
            sub_tier_a_df[col_name] = strata_series
            df_strata.loc[sub_tier_a_fams, col_name] = strata_series
            if cat_sfx == "Overall":
                df_strata.loc[sub_tier_a_fams, f"Stratum_PS_{cid}"] = strata_series
                
            fg_sub = sub_tier_a_df[fg_mask_cond]
            bg_sub = sub_tier_a_df[~fg_mask_cond]
            n_fg_s = fg_sub.groupby(col_name).size()
            
            for var, var_label in [("N_Proteins_Total", "Total_Count"), ("N_Ath_Loci", "Count_Ath"), ("Cat_Degree", "Annotation_Degree")]:
                x1 = fg_sub[var].values
                x0 = bg_sub[var].values
                s_pool = np.sqrt((np.var(x1, ddof=1) + np.var(x0, ddof=1)) / 2.0)
                
                mean_s = sub_tier_a_df.groupby(col_name)[var].mean()
                exp_mean = (n_fg_s * mean_s[n_fg_s.index]).sum() / len(fg_sub)
                
                smd_raw = compute_smd(x1, x0, s_pool)
                smd_adj = compute_smd(x1, exp_mean, s_pool)
                
                balance_qc_rows.append({
                    "Contrast_ID": cid,
                    "Category": cat_label,
                    "Variable": var_label,
                    "FG_Mean": float(np.mean(x1)),
                    "BG_Raw_Mean": float(np.mean(x0)),
                    "BG_Adjusted_Mean": float(exp_mean),
                    "Pooled_SD": float(s_pool),
                    "Raw_SMD": float(smd_raw),
                    "Adjusted_SMD": float(smd_adj),
                    "Balance_Achieved_lt_0_10": bool(abs(smd_adj) < 0.10)
                })
                
    df_balance_qc = pd.DataFrame(balance_qc_rows)
    balance_qc_file = os.path.join(inter_dir, "covariate_balance_qc.tsv")
    df_balance_qc.to_csv(balance_qc_file, sep="\t", index=False)
    print(f"\n[*] Saved Covariate Balance Audit Table: {balance_qc_file} ({len(df_balance_qc)} rows)")
    
    strata_out = os.path.join(inter_dir, "permutation_strata.tsv")
    df_strata.reset_index().to_csv(strata_out, sep="\t", index=False)
    print(f"[*] Saved Permutation Strata: {strata_out} ({len(df_strata)} rows)")
    
    # Audit summary
    print("\n--- Covariate Balance Verification Summary ---")
    gen_mask = df_balance_qc["Contrast_ID"] == "Core_Tier_A_General"
    gen_max_smd = df_balance_qc.loc[gen_mask, "Adjusted_SMD"].abs().max()
    print(f"  Core_Tier_A_General across ALL categories: max |Adjusted SMD| = {gen_max_smd:.4f} (Balance < 0.10: {gen_max_smd < 0.10})")
    
    cond_qc = df_balance_qc[~gen_mask]
    passed_combos = 0
    total_combos = 0
    for (cid, cat), grp in cond_qc.groupby(["Contrast_ID", "Category"]):
        total_combos += 1
        all_bal = grp["Balance_Achieved_lt_0_10"].all()
        max_smd = grp["Adjusted_SMD"].abs().max()
        if all_bal: passed_combos += 1
        status = "PASSED (<0.10)" if all_bal else f"ATTENTION (max SMD={max_smd:.3f})"
        print(f"  [{cid:25s}] {cat:18s}: {status}")
    print(f"\n[*] Audited {total_combos} conditional contrast-category combinations: {passed_combos} achieved full balance (<0.10).")

if __name__ == "__main__":
    main()
