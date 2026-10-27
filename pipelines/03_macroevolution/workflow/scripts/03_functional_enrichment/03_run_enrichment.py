#!/usr/bin/env python3
"""
Step 3: Run Over-Representation Analysis (ORA).
Strictly implements:
- Disjoint foreground and background definitions (Validation Control 3)
- Universe pre-filtering: 5 <= count <= 0.90 * universe
- Primary inferential mode: GO Propagated (BP, MF, CC) + KEGG Direct (Is_Primary_Inferential = True)
- Diagnostic mode: GO Direct (Is_Primary_Inferential = False)
- Scenario 4 (GO non-IEA): strictly uses per-(family, term) non-IEA associations; KEGG excluded from Scenario 4
- Exclusion of root GO terms (GO:0008150, GO:0003674, GO:0005575)
- Exact one-sided Fisher test
- Exact conditional MLE odds ratio and exact 95% CI via Brent root finding on noncentral hypergeometric distribution
- Multi-testing adjustment:
    local Benjamini-Hochberg q_value per (Scenario, Contrast, Category)
    q_global_primary across all primary inferential tests in Scenario 1
- Compatibility: np.asarray(..., dtype=float) avoiding deprecated np.asarray
"""

import os
import sys
import time
import yaml
import numpy as np
import pandas as pd
from scipy.optimize import brentq
from scipy.special import gammaln
import scipy.stats as stats
from collections import defaultdict

ROOT_TERMS = {"GO:0008150", "GO:0003674", "GO:0005575"}

def fdr_bh(pvals):
    pvals = np.asarray(pvals, dtype=float)
    n = len(pvals)
    if n == 0: return np.array([])
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

def log_comb(n, k):
    return gammaln(n + 1) - gammaln(k + 1) - gammaln(n - k + 1)

def calc_conditional_odds_ratio(a, b, c, d, alpha=0.05):
    m = a + b
    n = c + d
    k = a + c
    x_min = int(max(0, k - n))
    x_max = int(min(k, m))
    
    # Haldane-Anscombe auxiliary
    or_ha = float(((a + 0.5) * (d + 0.5)) / ((b + 0.5) * (c + 0.5)))
    
    if x_min == x_max:
        return 1.0, 0.0, np.inf, or_ha
        
    xs = np.arange(x_min, x_max + 1)
    log_base = log_comb(m, xs) + log_comb(n, k - xs)
    
    def get_probs(log_theta):
        log_p = log_base + (xs - x_min) * log_theta
        log_p -= np.max(log_p)
        p = np.exp(log_p)
        s = np.sum(p)
        return p / s if s > 0 else np.ones_like(p) / len(p)

    # Conditional MLE
    if a <= x_min:
        mle_or = 0.0
    elif a >= x_max:
        mle_or = np.inf
    else:
        def f_mle(lt):
            return np.sum(xs * get_probs(lt)) - a
        try:
            log_mle = brentq(f_mle, -20.0, 20.0)
            mle_or = float(np.exp(log_mle))
        except Exception:
            mle_or = or_ha
            
    # Lower CI: P(X >= a | theta_low) = alpha / 2
    if a <= x_min:
        ci_low = 0.0
    else:
        def f_low(lt):
            p = get_probs(lt)
            return np.sum(p[xs >= a]) - (alpha / 2.0)
        try:
            ci_low = float(np.exp(brentq(f_low, -25.0, 25.0)))
        except Exception:
            ci_low = 0.0
            
    # Upper CI: P(X <= a | theta_high) = alpha / 2
    if a >= x_max:
        ci_high = np.inf
    else:
        def f_high(lt):
            p = get_probs(lt)
            return np.sum(p[xs <= a]) - (alpha / 2.0)
        try:
            ci_high = float(np.exp(brentq(f_high, -25.0, 25.0)))
        except Exception:
            ci_high = np.inf
            
    return mle_or, ci_low, ci_high, or_ha

def main():
    t_start = time.time()
    base_dir = os.environ.get("FAMILY_ENRICHMENT_DIR", "/home/mfcaval/github/doutorado/chapter_macroevolution_review/04_gene_families/functional_enrichment")
    input_dir = os.path.join(base_dir, "input")
    results_dir = os.path.join(base_dir, "results")
    macro_dir = os.environ.get("FAMILY_MACRO_DIR", "/home/mfcaval/github/doutorado/chapter_macroevolution_review")
    
    config_file = os.path.join(input_dir, "config", "enrichment_config.yaml")
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)
        
    master_file = os.environ.get("FAMILY_MASTER_TABLE", os.path.join(macro_dir, "04_gene_families", "comparative_axes", "comparative_families_master_table_v2.tsv"))
    df_master = pd.read_csv(master_file, sep="\t").set_index("FamilyID")
    
    matrix_file = os.path.join(base_dir, "intermediate", "family_term_matrix.tsv")
    print(f"[*] Loading binary associations: {matrix_file}", flush=True)
    df_matrix = pd.read_csv(matrix_file, sep="\t")
    
    ann_file = os.path.join(results_dir, "orthogroup_functional_annotations.tsv")
    df_ann = pd.read_csv(ann_file, sep="\t").set_index("FamilyID")
    
    # Pre-index term associations
    term_fams_direct = defaultdict(set)
    term_fams_prop = defaultdict(set)
    term_fams_non_iea_direct = defaultdict(set)
    term_fams_non_iea_prop = defaultdict(set)
    term_meta = {}
    terms_by_cat = defaultdict(list)
    
    for row in df_matrix.itertuples(index=False):
        t = row.Term_ID
        if t in ROOT_TERMS:
            continue
        if t not in term_meta:
            term_meta[t] = (row.Term_Name, row.Category)
            terms_by_cat[row.Category].append(t)
            
        f = row.FamilyID
        if row.Is_Direct:
            term_fams_direct[t].add(f)
            if row.Has_Non_IEA_Direct:
                term_fams_non_iea_direct[t].add(f)
        if row.Is_Propagated:
            term_fams_prop[t].add(f)
            if row.Has_Non_IEA_Propagated:
                term_fams_non_iea_prop[t].add(f)
                
    # Pre-compute category-specific non-IEA universes for Scenario 4
    cat_non_iea_fams_prop = {
        cat: set(df_matrix[(df_matrix["Category"] == cat) & (df_matrix["Is_Propagated"] == True) & (df_matrix["Has_Non_IEA_Propagated"] == True)]["FamilyID"])
        for cat in ["GO_BP", "GO_MF", "GO_CC"]
    }
    cat_non_iea_fams_direct = {
        cat: set(df_matrix[(df_matrix["Category"] == cat) & (df_matrix["Is_Direct"] == True) & (df_matrix["Has_Non_IEA_Direct"] == True)]["FamilyID"])
        for cat in ["GO_BP", "GO_MF", "GO_CC"]
    }
    for cat in ["GO_BP", "GO_MF", "GO_CC"]:
        print(f"    Scenario 4 universe for {cat}: Propagated = {len(cat_non_iea_fams_prop[cat]):,} families, Direct = {len(cat_non_iea_fams_direct[cat]):,} families.")
                
    print(f"[*] Indexed {len(term_meta)} unique non-root terms across categories.", flush=True)
    
    contrasts_list = config["contrasts"]["primary"] + config["contrasts"]["external_controls"] + config["contrasts"]["descriptive_only"]
    
    # Define analytical scenarios
    scenarios = [
        ("scenario_1_all_families", set(df_master.index)),
        ("scenario_2_exclude_transposon_high_asymmetry", set(df_master[(~df_master["Flag_Transposon"]) & (~df_master["Flag_High_Copy_Asymmetry"])].index)),
        ("scenario_3_nuclear_only", set(df_master[~df_master["Flag_Organellar"]].index)),
        ("scenario_4_go_non_iea", set(df_master.index)) # Denominator will be strictly category-specific
    ]
    
    # Categories: GO Propagated and KEGG Direct are Primary Inferential
    categories = [
        ("GO_BP", True, "GO_BP_Propagated", True),
        ("GO_MF", True, "GO_MF_Propagated", True),
        ("GO_CC", True, "GO_CC_Propagated", True),
        ("KEGG", False, "KEGG_Direct", True),
        ("GO_BP", False, "GO_BP_Direct", False),
        ("GO_MF", False, "GO_MF_Direct", False),
        ("GO_CC", False, "GO_CC_Direct", False)
    ]
    
    all_results = []
    
    print("[*] Running enrichment across contrasts and sensitivity scenarios...", flush=True)
    
    for sc_id, sc_fams in scenarios:
        t_sc = time.time()
        print(f"\n--- Processing {sc_id} (N={len(sc_fams)}) ---", flush=True)
        
        for c_info in contrasts_list:
            cid = c_info["id"]
            ctype = c_info["type"]
            fg_cond = c_info["fg_condition"]
            
            fg_mask = df_master.eval(fg_cond)
            raw_fg = set(df_master[fg_mask].index) & sc_fams
            raw_bg = sc_fams - raw_fg
                
            # Validation Control 3: Disjoint check
            if len(raw_fg & raw_bg) > 0:
                raise ValueError(f"Control 3 Violation in {cid}: FG and BG overlap!")
                
            for cat_name, is_prop, cat_label, is_primary in categories:
                # In Scenario 4 (GO non-IEA), exclude KEGG because KEGG has no GAF evidence codes
                if sc_id == "scenario_4_go_non_iea" and cat_name == "KEGG":
                    continue
                    
                # Find eligible annotated families in this category
                if sc_id == "scenario_4_go_non_iea":
                    cat_annotated = cat_non_iea_fams_prop[cat_name] if is_prop else cat_non_iea_fams_direct[cat_name]
                elif cat_name.startswith("GO"):
                    ann_col = f"{cat_name}_Propagated" if is_prop else f"{cat_name}_Direct"
                    cat_annotated = set(df_ann[df_ann[ann_col].notna() & (df_ann[ann_col] != "") & (df_ann[ann_col] != "nan")].index)
                else:
                    cat_annotated = set(df_ann[df_ann["KEGG_Pathways"].notna() & (df_ann["KEGG_Pathways"] != "") & (df_ann["KEGG_Pathways"] != "nan")].index)
                    
                fg_annotated = raw_fg & cat_annotated
                bg_annotated = raw_bg & cat_annotated
                
                n_fg = len(fg_annotated)
                n_bg = len(bg_annotated)
                univ_annotated = fg_annotated | bg_annotated
                n_univ = len(univ_annotated)
                
                if len(fg_annotated & bg_annotated) > 0 or len(univ_annotated) != (n_fg + n_bg):
                    raise ValueError(f"Control 3 Violation: Universe not disjoint partition in {cid} {cat_label}")
                    
                if n_fg == 0 or n_bg == 0:
                    continue
                    
                # Select appropriate term lookup dictionary
                if sc_id == "scenario_4_go_non_iea":
                    term_dict = term_fams_non_iea_prop if is_prop else term_fams_non_iea_direct
                elif is_prop:
                    term_dict = term_fams_prop
                else:
                    term_dict = term_fams_direct
                    
                contrast_rows = []
                for t in terms_by_cat[cat_name]:
                    if t in ROOT_TERMS:
                        continue
                        
                    fams = term_dict.get(t)
                    if not fams or len(fams) < 5:
                        continue
                        
                    a = len(fams & fg_annotated)
                    c = len(fams & bg_annotated)
                    cnt_univ = a + c
                    
                    if cnt_univ < 5 or cnt_univ > 0.90 * n_univ:
                        continue
                        
                    b = n_fg - a
                    d = n_bg - c
                    
                    # Validation Control 4 check
                    if (a + b != n_fg) or (c + d != n_bg) or (a + c != cnt_univ):
                        raise ValueError(f"Control 4 Violation: 2x2 table mismatch for term {t}")
                        
                    p_val = stats.fisher_exact([[a, b], [c, d]], alternative="greater")[1]
                    mle_or, ci_low, ci_high, ha_or = calc_conditional_odds_ratio(a, b, c, d)
                    fold_enrich = ((a / n_fg) / (c / n_bg)) if (c > 0 and n_bg > 0) else np.inf
                    
                    contrast_rows.append({
                        "Scenario": sc_id,
                        "Contrast_ID": cid,
                        "Contrast_Type": ctype,
                        "Ontology_Category": cat_label,
                        "Is_Propagated": is_prop,
                        "Is_Primary_Inferential": is_primary,
                        "Term_ID": t,
                        "Term_Name": term_meta[t][0],
                        "FG_Count": a,
                        "FG_Total": n_fg,
                        "BG_Count": c,
                        "BG_Total": n_bg,
                        "Universe_Count": cnt_univ,
                        "Universe_Total": n_univ,
                        "GeneRatio": f"{a}/{n_fg}",
                        "BgRatio": f"{c}/{n_bg}",
                        "Fold_Enrichment": fold_enrich,
                        "Conditional_OR": mle_or,
                        "CI_95_Low": ci_low,
                        "CI_95_High": ci_high,
                        "Haldane_Anscombe_OR": ha_or,
                        "p_value": p_val
                    })
                    
                if contrast_rows:
                    df_c = pd.DataFrame(contrast_rows)
                    df_c["q_value"] = fdr_bh(df_c["p_value"].values)
                    violations = (df_c["q_value"] < df_c["p_value"] - 1e-12).sum()
                    if violations > 0:
                        raise ValueError(f"Control 6 Violation: {violations} instances of q < p in {cid} {cat_label}")
                    all_results.extend(df_c.to_dict("records"))
                    
        print(f"[*] Finished {sc_id} in {time.time() - t_sc:.2f} s.", flush=True)
        
    df_all_results = pd.DataFrame(all_results)
    
    # Calculate q_global_primary strictly across primary inferential tests in Scenario 1
    primary_ids = [c["id"] for c in config["contrasts"]["primary"]]
    primary_mask = (
        (df_all_results["Scenario"] == "scenario_1_all_families") &
        (df_all_results["Is_Primary_Inferential"] == True) &
        (df_all_results["Contrast_ID"].isin(primary_ids))
    )
    primary_pvals = df_all_results.loc[primary_mask, "p_value"].values
    df_all_results["q_global_primary"] = np.nan
    df_all_results.loc[primary_mask, "q_global_primary"] = fdr_bh(primary_pvals)
    print(f"[*] Calculated q_global_primary across {len(primary_pvals)} primary inferential tests in this run.")
    
    out_all_tsv = os.path.join(results_dir, "enrichment_results_all.tsv")
    df_all_results.to_csv(out_all_tsv, sep="\t", index=False)
    print(f"\n[*] Saved complete enrichment results: {out_all_tsv}")
    print(f"    Total tests executed: {len(df_all_results)}")
    
    df_primary = df_all_results[df_all_results["Scenario"] == "scenario_1_all_families"]
    df_primary_tsv = os.path.join(results_dir, "enrichment_results_primary.tsv")
    df_primary.to_csv(df_primary_tsv, sep="\t", index=False)
    print(f"[*] Saved primary results: {df_primary_tsv} ({len(df_primary)} rows)")
    
    df_sens = df_all_results[df_all_results["Scenario"] != "scenario_1_all_families"]
    df_sens_tsv = os.path.join(results_dir, "enrichment_results_sensitivity.tsv")
    df_sens.to_csv(df_sens_tsv, sep="\t", index=False)
    print(f"[*] Saved sensitivity results: {df_sens_tsv} ({len(df_sens)} rows)")
    print(f"[*] Total execution time: {time.time() - t_start:.2f} s.", flush=True)

if __name__ == "__main__":
    main()
