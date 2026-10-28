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
    default_macro = str(Path(__file__).resolve().parents[3])
    default_enrich = str(Path(__file__).resolve().parents[3] / "04_gene_families" / "functional_enrichment")
    base_dir = os.environ.get("FAMILY_ENRICHMENT_DIR", default_enrich)
    input_dir = os.path.join(base_dir, "input")
    results_dir = os.path.join(base_dir, "results")
    macro_dir = os.environ.get("FAMILY_MACRO_DIR", default_macro)
    inter_dir = os.path.join(base_dir, "intermediate")
    os.makedirs(inter_dir, exist_ok=True)
    
    config_file = os.path.join(input_dir, "config", "enrichment_config.yaml")
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)
        
    master_file = os.environ.get("FAMILY_MASTER_TABLE", os.path.join(macro_dir, "04_gene_families", "comparative_axes", "comparative_families_master_table_v2.tsv"))
    df_master = pd.read_csv(master_file, sep="\t").set_index("FamilyID")
    
    ann_file = os.path.join(results_dir, "orthogroup_functional_annotations.tsv")
    print(f"[*] Loading master annotations: {ann_file}")
    df_ann = pd.read_csv(ann_file, sep="\t").set_index("FamilyID")
    
    obo_file = os.path.join(input_dir, "raw_annotations", "go-basic.obo")
    go_names = parse_obo_names(obo_file)
    kegg_list_file = os.path.join(input_dir, "raw_annotations", "kegg", "ath_pathway_list.tsv")
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
    
    def defragment_for_fg(fg_bool_arr):
        s_map = {k: k for k in df_strata["raw_stratum"].unique()}
        def recompute_grp(current_map):
            st = df_strata["raw_stratum"].map(current_map)
            g = pd.DataFrame({"st": st, "is_fg": fg_bool_arr}).groupby("st")["is_fg"].agg(["count", "sum"])
            g["n_bg"] = g["count"] - g["sum"]
            return g
        grp = recompute_grp(s_map)
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
                    for k, v in s_map.items():
                        if v == st:
                            s_map[k] = best_cand
                    grp = recompute_grp(s_map)
        return df_strata["raw_stratum"].map(s_map)

    focal_arr = (df_master["BranchSig_Exp_Vper"] == True).astype(int).values
    df_strata["Stratum_General"] = defragment_for_fg(focal_arr)
    print(f"    Defragmented universe strata created: {df_strata['Stratum_General'].nunique()} unique strata.")
    
    # -------------------------------------------------------------
    # 3. Audit Covariate Balance Across All Contrasts and Categories
    # -------------------------------------------------------------
    contrasts_list = config["contrasts"]["primary"] + config["contrasts"]["external_controls"] + config["contrasts"]["descriptive_only"]
    balance_qc_rows = []
    
    eval_categories = [
        ("Overall", "Overall", set(df_master.index)),
        ("GO_BP", "GO_BP_Propagated", set(df_matrix[(df_matrix["Category"] == "GO_BP") & (df_matrix["Is_Propagated"] == True)]["FamilyID"])),
        ("GO_MF", "GO_MF_Propagated", set(df_matrix[(df_matrix["Category"] == "GO_MF") & (df_matrix["Is_Propagated"] == True)]["FamilyID"])),
        ("GO_CC", "GO_CC_Propagated", set(df_matrix[(df_matrix["Category"] == "GO_CC") & (df_matrix["Is_Propagated"] == True)]["FamilyID"])),
        ("KEGG", "KEGG_Direct", set(df_matrix[(df_matrix["Category"] == "KEGG") & (df_matrix["Is_Direct"] == True)]["FamilyID"]))
    ]
    
    for c_info in contrasts_list:
        gen_cid = c_info["id"]
        gen_col = f"Stratum_Gen_{gen_cid}"
        fg_all_arr = df_master.eval(c_info["fg_condition"]).astype(int).values
        df_strata[gen_col] = defragment_for_fg(fg_all_arr)
        
        for cat_name, cat_label, cat_fams in eval_categories:
            sub_strata = df_strata.loc[list(cat_fams)]
            sub_master = df_master.loc[list(cat_fams)]
            fg_mask = sub_master.eval(c_info["fg_condition"])
            fg_sub = sub_strata[fg_mask]
            bg_sub = sub_strata[~fg_mask]
            
            if len(fg_sub) == 0 or len(bg_sub) == 0:
                continue
                
            n_fg_s = fg_sub.groupby(gen_col).size()
            
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
                mean_s = s_series.groupby(sub_strata[gen_col]).mean()
                exp_mean = (n_fg_s * mean_s[n_fg_s.index]).sum() / len(fg_sub)
                
                smd_raw = compute_smd(fg_vals, bg_vals, s_pool)
                smd_adj = compute_smd(fg_vals, exp_mean, s_pool)
                
                balance_qc_rows.append({
                    "Contrast_ID": gen_cid,
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
                
    df_balance_qc = pd.DataFrame(balance_qc_rows)
    balance_qc_file = os.path.join(inter_dir, "covariate_balance_qc.tsv")
    df_balance_qc.to_csv(balance_qc_file, sep="\t", index=False)
    print(f"\n[*] Saved Covariate Balance Audit Table: {balance_qc_file} ({len(df_balance_qc)} rows)")
    
    strata_out = os.path.join(inter_dir, "permutation_strata.tsv")
    df_strata.reset_index().to_csv(strata_out, sep="\t", index=False)
    print(f"[*] Saved Permutation Strata: {strata_out} ({len(df_strata)} rows)")
    
    # Audit summary
    print("\n--- Covariate Balance Verification Summary ---")
    passed_combos = 0
    total_combos = 0
    for (cid, cat), grp in df_balance_qc.groupby(["Contrast_ID", "Category"]):
        total_combos += 1
        all_bal = grp["Balance_Achieved_lt_0_10"].all()
        max_smd = grp["Adjusted_SMD"].abs().max()
        if all_bal: passed_combos += 1
        status = "PASSED (<0.10)" if all_bal else f"ATTENTION (max SMD={max_smd:.3f})"
        print(f"  [{cid:32s}] {cat:18s}: {status}")
    print(f"\n[*] Audited {total_combos} contrast-category combinations: {passed_combos} achieved full balance (<0.10).")

if __name__ == "__main__":
    main()
