#!/usr/bin/env python3
"""
Step 4: Run Stratified Permutations and Covariate-Adjusted Logistic Regression.
Strictly implements:
- Validation Control 7: 10,000 stratified permutations preserving foreground size and stratum composition
- Deterministic execution: sorted family IDs and seed 20260904
- General Contrast uses fine 540-strata grid (residual SMD < 0.012 on Total_Count, Count_Ath, Annotation_Degree)
- Conditional Contrasts use contrast-specific propensity score strata
- Covariate-adjusted logistic regression model for significant terms (q < 0.05)
- Evidence classification:
    Confirmatory: q_local < 0.05, q_global_primary < 0.05, p_strat < 0.05
    Suggestive:   q_local < 0.05, q_global_primary >= 0.05, p_strat < 0.05
    Size_Artifact: q_local < 0.05, p_strat >= 0.05
    Not_Significant: q_local >= 0.05
- Updates enrichment_results_primary.tsv and enrichment_results_all.tsv
"""

import os
import sys
import time
import yaml
import numpy as np
import pandas as pd
from collections import defaultdict
from scipy.optimize import minimize
import scipy.stats as stats

ROOT_TERMS = {"GO:0008150", "GO:0003674", "GO:0005575"}

def fit_covariate_model(y, fg_vec, total_vec, ath_vec, deg_vec):
    """
    Fits covariate-adjusted logistic regression model:
    logit(P(Y=1)) = b0 + b1*FG + b2*log1p(Total) + b3*log1p(Ath) + b4*log1p(Deg)
    Returns: adjusted_or, p_lrt (one-sided)
    """
    n = len(y)
    if y.sum() == 0 or y.sum() == n:
        return 1.0, 1.0
        
    X = np.column_stack([
        np.ones(n),
        fg_vec.astype(float),
        np.log1p(total_vec),
        np.log1p(ath_vec),
        np.log1p(deg_vec)
    ])
    
    # Standardize continuous covariates for numerical stability
    for col in [2, 3, 4]:
        std = np.std(X[:, col])
        if std > 0:
            X[:, col] = (X[:, col] - np.mean(X[:, col])) / std
            
    def nll(w):
        z = X.dot(w)
        p = 1.0 / (1.0 + np.exp(-np.clip(z, -25, 25)))
        eps = 1e-12
        return -np.sum(y * np.log(p + eps) + (1.0 - y) * np.log(1.0 - p + eps))
        
    res = minimize(nll, np.zeros(X.shape[1]), method="BFGS")
    
    # Null model without FG
    X_null = np.column_stack([X[:, 0], X[:, 2], X[:, 3], X[:, 4]])
    def nll_null(w):
        z = X_null.dot(w)
        p = 1.0 / (1.0 + np.exp(-np.clip(z, -25, 25)))
        eps = 1e-12
        return -np.sum(y * np.log(p + eps) + (1.0 - y) * np.log(1.0 - p + eps))
        
    res_null = minimize(nll_null, np.zeros(X_null.shape[1]), method="BFGS")
    
    lrt_stat = max(0.0, 2.0 * (res_null.fun - res.fun))
    b1 = res.x[1]
    adj_or = float(np.exp(b1))
    p_lrt = float(stats.chi2.sf(lrt_stat, df=1) / 2.0 if b1 > 0 else 1.0)
    
    return adj_or, p_lrt

def main():
    t_start = time.time()
    base_dir = "/home/mfcaval/github/doutorado/chapter_macroevolution/04_gene_families/functional_enrichment"
    macro_dir = "/home/mfcaval/github/doutorado/chapter_macroevolution"
    
    config_file = os.path.join(base_dir, "config", "enrichment_config.yaml")
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)
        
    seed = config["parameters"]["random_seed"]
    B = config["parameters"]["n_permutations"]
    print(f"[*] Initializing stratified permutations with seed={seed}, B={B}...", flush=True)
    rng = np.random.RandomState(seed)
    
    master_file = os.path.join(macro_dir, "04_gene_families", "comparative_axes", "comparative_families_master_table_v2.tsv")
    df_master = pd.read_csv(master_file, sep="\t").set_index("FamilyID")
    tier_a_fams = set(df_master[df_master["Evidence_Tier"] == "Tier_A_High_Confidence"].index)
    
    strata_file = os.path.join(base_dir, "intermediate", "permutation_strata.tsv")
    df_strata = pd.read_csv(strata_file, sep="\t").set_index("FamilyID")
    
    matrix_file = os.path.join(base_dir, "intermediate", "family_term_matrix.tsv")
    print(f"[*] Loading binary term matrix: {matrix_file}", flush=True)
    df_matrix = pd.read_csv(matrix_file, sep="\t")
    
    ann_file = os.path.join(base_dir, "orthogroup_functional_annotations.tsv")
    df_ann = pd.read_csv(ann_file, sep="\t").set_index("FamilyID")
    
    # Load Covariate Balance Audit
    cov_file = os.path.join(base_dir, "intermediate", "covariate_balance_qc.tsv")
    print(f"[*] Loading covariate balance audit: {cov_file}", flush=True)
    df_cov = pd.read_csv(cov_file, sep="\t")
    balance_map = {}
    for (c_id_cov, cat_cov), grp in df_cov.groupby(["Contrast_ID", "Category"]):
        balance_map[(c_id_cov, cat_cov)] = bool(grp["Balance_Achieved_lt_0_10"].all())
        
    primary_res_file = os.path.join(base_dir, "enrichment_results_primary.tsv")
    df_primary = pd.read_csv(primary_res_file, sep="\t")
    print(f"[*] Loaded {len(df_primary)} primary test results.", flush=True)
    
    term_fams_direct = defaultdict(set)
    term_fams_prop = defaultdict(set)
    for row in df_matrix.itertuples(index=False):
        t = row.Term_ID
        if t in ROOT_TERMS:
            continue
        if row.Is_Direct:
            term_fams_direct[t].add(row.FamilyID)
        if row.Is_Propagated:
            term_fams_prop[t].add(row.FamilyID)
            
    groups = df_primary.groupby(["Contrast_ID", "Ontology_Category", "Is_Propagated"])
    print(f"[*] Processing {len(groups)} distinct contrast/category combinations...", flush=True)
    
    p_strat_map = {}
    adj_or_map = {}
    p_adj_map = {}
    
    comb_idx = 0
    total_combs = len(groups)
    
    for (cid, cat_label, is_prop), df_grp in groups:
        comb_idx += 1
        t_grp = time.time()
        
        c_info = next((c for c in (config["contrasts"]["primary"] + config["contrasts"]["external_controls"] + config["contrasts"]["descriptive_only"]) if c["id"] == cid), None)
        if c_info is None:
            continue
            
        fg_cond = c_info["fg_condition"]
        bg_univ_type = c_info["bg_universe"]
        
        fg_mask = df_master.eval(fg_cond)
        raw_fg = set(df_master[fg_mask].index)
        
        if bg_univ_type == "all_annotated_in_category":
            raw_bg = set(df_master.index) - raw_fg
            is_general = True
        else:
            raw_bg = tier_a_fams - raw_fg
            is_general = False
            
        cat_name = cat_label.split("_Direct")[0].split("_Propagated")[0]
        if cat_name.startswith("GO"):
            ann_col = f"{cat_name}_Propagated" if is_prop else f"{cat_name}_Direct"
            cat_annotated = set(df_ann[df_ann[ann_col].notna() & (df_ann[ann_col] != "") & (df_ann[ann_col] != "nan")].index)
        else:
            cat_annotated = set(df_ann[df_ann["KEGG_Pathways"].notna() & (df_ann["KEGG_Pathways"] != "") & (df_ann["KEGG_Pathways"] != "nan")].index)
            
        fg_annotated = raw_fg & cat_annotated
        bg_annotated = raw_bg & cat_annotated
        
        # Strictly deterministic sorted list of families in declared universe
        univ_annotated = sorted(list(fg_annotated | bg_annotated))
        n_univ = len(univ_annotated)
        n_fg = len(fg_annotated)
        
        if n_fg == 0 or n_univ == 0:
            for t in df_grp["Term_ID"]:
                key = (cid, cat_label, t)
                p_strat_map[key] = 1.0
                adj_or_map[key] = 1.0
                p_adj_map[key] = 1.0
            continue
            
        fam_to_idx = {f: i for i, f in enumerate(univ_annotated)}
        fg_indices = np.array([fam_to_idx[f] for f in fg_annotated], dtype=np.int32)
        fg_mask_arr = np.zeros(n_univ, dtype=bool)
        fg_mask_arr[fg_indices] = True
        
        # Select appropriate stratum column:
        # General contrast uses fine Stratum_General; Conditional contrasts use category-specific Stratum_PS_{cid}_{cat_sfx}
        if is_general:
            stratum_col = "Stratum_General"
        else:
            cat_sfx = "BP" if "BP" in cat_label else ("MF" if "MF" in cat_label else ("CC" if "CC" in cat_label else ("KEGG" if "KEGG" in cat_label else "Overall")))
            cand_col = f"Stratum_PS_{cid}_{cat_sfx}"
            if cand_col in df_strata.columns:
                stratum_col = cand_col
            elif f"Stratum_PS_{cid}" in df_strata.columns:
                stratum_col = f"Stratum_PS_{cid}"
            else:
                stratum_col = "Stratum_General"
            
        univ_strata = df_strata.loc[univ_annotated, stratum_col].values
        unique_strata = np.unique(univ_strata)
        
        # Build permutation matrix P of shape (B, n_univ)
        P = np.zeros((B, n_univ), dtype=np.float32)
        
        for s in unique_strata:
            s_indices = np.where(univ_strata == s)[0]
            n_s = len(s_indices)
            k_s = int(fg_mask_arr[s_indices].sum())
            if k_s == 0:
                continue
            if k_s == n_s:
                P[:, s_indices] = 1.0
                continue
            keys = rng.rand(B, n_s)
            sel = np.argpartition(keys, -k_s, axis=1)[:, -k_s:]
            rows = np.repeat(np.arange(B), k_s)
            cols = s_indices[sel.ravel()]
            P[rows, cols] = 1.0
            
        # Validation Control 7 check
        row_sums = P.sum(axis=1)
        if not np.allclose(row_sums, n_fg):
            raise ValueError(f"Control 7 Violation in {cid} {cat_label}: Permutation foreground sum mismatch!")
            
        term_dict = term_fams_prop if is_prop else term_fams_direct
        
        # Covariate vectors for logistic regression
        total_vec = df_strata.loc[univ_annotated, "N_Proteins_Total"].values
        ath_vec = df_strata.loc[univ_annotated, "N_Ath_Loci"].values
        deg_vec = df_strata.loc[univ_annotated, "Annotation_Degree"].values
        
        zero_terms = []
        eval_terms = []
        eval_a_obs = []
        term_indicators = []
        
        for r in df_grp.itertuples(index=False):
            t = r.Term_ID
            a_obs = r.FG_Count
            key = (cid, cat_label, t)
            if a_obs == 0:
                zero_terms.append(t)
                p_strat_map[key] = 1.0
                adj_or_map[key] = 0.0
                p_adj_map[key] = 1.0
            else:
                eval_terms.append(t)
                eval_a_obs.append(a_obs)
                t_fams = term_dict[t]
                ind = np.array([1.0 if f in t_fams else 0.0 for f in univ_annotated], dtype=np.float32)
                term_indicators.append(ind)
                
                # Fit covariate model if nominal q < 0.05
                if r.q_value < 0.05:
                    adj_or, p_lrt = fit_covariate_model(ind, fg_mask_arr, total_vec, ath_vec, deg_vec)
                    adj_or_map[key] = adj_or
                    p_adj_map[key] = p_lrt
                else:
                    adj_or_map[key] = r.Conditional_OR
                    p_adj_map[key] = r.p_value
                    
        if eval_terms:
            V = np.column_stack(term_indicators)
            perm_counts = P.dot(V)
            obs_arr = np.array(eval_a_obs, dtype=np.float32)
            ge_count = (perm_counts >= obs_arr).sum(axis=0)
            p_strats = (1.0 + ge_count) / (1.0 + B)
            
            for t, ps in zip(eval_terms, p_strats):
                key = (cid, cat_label, t)
                p_strat_map[key] = float(ps)
                
        if comb_idx % 10 == 0 or comb_idx == total_combs:
            print(f"[{comb_idx}/{total_combs}] Completed {cid} {cat_label} in {time.time() - t_grp:.2f} s.", flush=True)
            
    # Assign new fields to df_primary
    p_strat_list = []
    adj_or_list = []
    p_adj_list = []
    
    for r in df_primary.itertuples(index=False):
        key = (r.Contrast_ID, r.Ontology_Category, r.Term_ID)
        p_strat_list.append(p_strat_map.get(key, 1.0))
        adj_or_list.append(adj_or_map.get(key, r.Conditional_OR))
        p_adj_list.append(p_adj_map.get(key, r.p_value))
        
    df_primary["p_strat"] = p_strat_list
    df_primary["Adjusted_OR"] = adj_or_list
    df_primary["p_covar_adj"] = p_adj_list
    
    # Classify Evidence
    evidence_classes = []
    for r in df_primary.itertuples(index=False):
        q_loc = r.q_value
        q_glob = r.q_global_primary
        p_st = r.p_strat
        is_prim_inf = r.Is_Primary_Inferential
        cid = r.Contrast_ID
        cat_lbl = r.Ontology_Category
        is_prop = r.Is_Propagated
        full_cat = f"{cat_lbl}_Propagated" if (cat_lbl.startswith("GO") and is_prop) else (f"{cat_lbl}_Direct" if cat_lbl == "KEGG" else cat_lbl)
        
        # Diagnostic tests (GO Direct) must never be Confirmatory/Suggestive
        if not is_prim_inf:
            if q_loc < 0.05:
                evidence_classes.append("Diagnostic_Nominal_Sig")
            else:
                evidence_classes.append("Not_Significant")
            continue
            
        # Primary inferential tests (GO Propagated + KEGG Direct)
        if q_loc < 0.05:
            if p_st < 0.05:
                # Check covariate balance gate
                balance_achieved = balance_map.get((cid, full_cat), balance_map.get((cid, cat_lbl), balance_map.get((cid, "Overall"), False)))
                if balance_achieved:
                    if pd.notna(q_glob) and q_glob < 0.05:
                        evidence_classes.append("Confirmatory")
                    else:
                        evidence_classes.append("Suggestive")
                else:
                    evidence_classes.append("Suggestive_Imbalanced_Opportunity")
            else:
                evidence_classes.append("Permutation_Discordant")
        else:
            evidence_classes.append("Not_Significant")
            
    df_primary["Evidence_Class"] = evidence_classes
    df_primary["Robust_Stratified"] = df_primary["Evidence_Class"].isin(["Confirmatory", "Suggestive", "Suggestive_Imbalanced_Opportunity"])
    
    df_primary.to_csv(primary_res_file, sep="\t", index=False)
    print(f"\n[*] Updated primary results: {primary_res_file}")
    
    # Update enrichment_results_all.tsv
    all_res_file = os.path.join(base_dir, "enrichment_results_all.tsv")
    df_all = pd.read_csv(all_res_file, sep="\t")
    
    df_all["p_strat"] = np.nan
    df_all["Adjusted_OR"] = np.nan
    df_all["p_covar_adj"] = np.nan
    df_all["Evidence_Class"] = "Not_Evaluated"
    df_all["Robust_Stratified"] = False
    
    mask_primary = (df_all["Scenario"] == "scenario_1_all_families")
    primary_indices = df_all[mask_primary].index
    
    df_all.loc[primary_indices, "p_strat"] = df_primary["p_strat"].values
    df_all.loc[primary_indices, "Adjusted_OR"] = df_primary["Adjusted_OR"].values
    df_all.loc[primary_indices, "p_covar_adj"] = df_primary["p_covar_adj"].values
    df_all.loc[primary_indices, "Evidence_Class"] = df_primary["Evidence_Class"].values
    df_all.loc[primary_indices, "Robust_Stratified"] = df_primary["Robust_Stratified"].values
    
    df_all.to_csv(all_res_file, sep="\t", index=False)
    print(f"[*] Updated all results: {all_res_file}")
    
    # Print summary breakdown
    print("\n--- Evidence Classification Breakdown (Primary Scenario) ---")
    print(df_primary.groupby(["Is_Primary_Inferential", "Evidence_Class"]).size())
    print(f"\n[*] Total execution time: {time.time() - t_start:.2f} s.")
    print("[*] [PASSED] Validation Control 7 strictly verified with deterministic sorting.")

if __name__ == "__main__":
    main()
