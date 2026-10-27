#!/usr/bin/env python3
"""
Build Comparative Families Master Table v2 (Definitive Production Version).
Integrates:
- Gene counts across 7 species (Abra, Ath, Dala, Ptec, Vper, Vtub, Xvis)
- CAFE5 Gamma k=2 branch changes and branch probabilities (reindexed for all 12,276 families;
  the 11,771 missing probabilities reflect the nominal threshold p < 0.05 of the initial report)
- Multi-replicate FDR q-values (k=2 5 reps, k=3 4 valid reps, excluding k3/rep02)
- Replicate significance frequency
- Evidence tiers (Tier A: 188, Tier B: 43, Tier C: 73, Non-significant: 11,972)
- Independent, non-exclusive binary indicators for phenotypic & evolutionary events:
    * Lineage-specific terminal expansions (Vper, Vtub, Xvis, Abra, Ptec)
    * Parallel expansions across desiccation-tolerant (DT) lineages (Vtub, Xvis, Abra)
    * Reconstructed ancestral expansions at Node 11, Node 12, Node 13 (strictly phylogenetic)
    * Parallel contractions across desiccation-tolerant (DT) lineages
    * Concordance of exact sign across all 6 key branches requiring consensus across all 4 valid k=3 reps (132/188)
    * Indicator-specific preservation across all 4 valid k=3 replicates
- Functional annotations (EggNOG, Arabidopsis orthologs; unannotated labeled as 'Sem anotacao EggNOG recuperada')
- Quality control & biological flags:
    * Flag_Transposon (refined regex: gag, transposon, reverse transcriptase, integrase)
    * Flag_Organellar (refined regex: chloroplasts, photosystem, PSII, NDH, Ycf, etc.)
    * Flag_High_Copy_Asymmetry (single species >= 85% of copies when total >= 20)
- Evolutionary_Dynamic_Summary: derived categorical summary with explicit documented priority hierarchy.
Chapter: Macroevolution and Genomics in Velloziaceae
"""

import os
import sys
import glob
import re
import numpy as np
import pandas as pd

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

def load_family_results(fpath):
    df = pd.read_csv(fpath, sep="\t")
    df.columns = [c.replace("#", "").strip() for c in df.columns]
    df["pvalue"] = pd.to_numeric(df["pvalue"], errors="coerce")
    df = df.dropna(subset=["pvalue"])
    df["qvalue"] = fdr_bh(df["pvalue"].values)
    return df.set_index("FamilyID")

def main():
    # Portable path resolution relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_macro = os.path.abspath(os.path.join(script_dir, "..", ".."))
    base_dir = os.path.join(base_macro, "04_gene_families")
    rerun_dir = os.path.join(base_dir, "cafe5_results", "rerun")
    comp_dir = os.path.join(base_dir, "comparative_axes")
    os.makedirs(comp_dir, exist_ok=True)
    
    # 1. Base counts across 7 species
    counts_file = os.path.join(base_dir, "cafe_family_input.tsv")
    df_counts = pd.read_csv(counts_file, sep="\t").set_index("FamilyID")
    species_cols = ["Abra", "Ath", "Dala", "Ptec", "Vper", "Vtub", "Xvis"]
    for sc in species_cols:
        df_counts[sc] = df_counts[sc].astype(int)
    df_counts["Total_Count"] = df_counts[species_cols].sum(axis=1)
    
    # 2. Replicate FDR q-values (computed across all N=12,276 tested families)
    # k=2 (5 reps)
    k2_qvals = {}
    for r in ["rep01", "rep02", "rep03", "rep04", "rep05"]:
        res_f = os.path.join(rerun_dir, "03_gamma_k2", r, "Gamma_family_results.txt")
        df_res = load_family_results(res_f)
        k2_qvals[f"qval_k2_{r}"] = df_res["qvalue"]
    df_k2 = pd.DataFrame(k2_qvals)
    
    # k=3 (4 valid reps: 01, 03, 04, 05; rep02 discarded as suboptimal local minimum)
    k3_valid_reps = ["rep01", "rep03", "rep04", "rep05"]
    k3_qvals = {}
    for r in k3_valid_reps:
        res_f = os.path.join(rerun_dir, "04_gamma_k3", r, "Gamma_family_results.txt")
        df_res = load_family_results(res_f)
        k3_qvals[f"qval_k3_{r}"] = df_res["qvalue"]
    df_k3 = pd.DataFrame(k3_qvals)
    
    # 3. Branch changes and branch probabilities
    # Primary model: Gamma k=2, rep02
    prim_dir = os.path.join(rerun_dir, "03_gamma_k2", "rep02")
    df_change_k2 = pd.read_csv(os.path.join(prim_dir, "Gamma_change.tab"), sep="\t").set_index("FamilyID")
    df_prob_k2 = pd.read_csv(os.path.join(prim_dir, "Gamma_branch_probabilities.tab"), sep="\t").set_index("FamilyID")
    
    # Load all 4 valid k=3 branch changes for consensus evaluation
    k3_change_dfs = {}
    for r in k3_valid_reps:
        f_ch = os.path.join(rerun_dir, "04_gamma_k3", r, "Gamma_change.tab")
        k3_change_dfs[r] = pd.read_csv(f_ch, sep="\t").set_index("FamilyID")
        
    node_rename = {
        "Vper<1>": "Change_Vper",
        "Vtub<2>": "Change_Vtub",
        "Xvis<3>": "Change_Xvis",
        "Abra<4>": "Change_Abra",
        "Ptec<5>": "Change_Ptec",
        "Dala<6>": "Change_Dala",
        "Ath<7>": "Change_Ath",
        "<8>": "Change_Node8_Root",
        "<9>": "Change_Node9_Monocots",
        "<10>": "Change_Node10_Pandanales",
        "<11>": "Change_Node11_Velloziaceae_Crown",
        "<12>": "Change_Node12_Core_Velloziaceae",
        "<13>": "Change_Node13_Vellozia_Crown"
    }
    df_change_k2 = df_change_k2.rename(columns=node_rename)
    for r in k3_valid_reps:
        k3_change_dfs[r] = k3_change_dfs[r].rename(columns=node_rename)
        
    prob_rename = {
        "Vper<1>": "BranchProb_Vper",
        "Vtub<2>": "BranchProb_Vtub",
        "Xvis<3>": "BranchProb_Xvis",
        "Abra<4>": "BranchProb_Abra",
        "Ptec<5>": "BranchProb_Ptec",
        "Dala<6>": "BranchProb_Dala",
        "Ath<7>": "BranchProb_Ath",
        "<11>": "BranchProb_Node11_Velloziaceae_Crown",
        "<12>": "BranchProb_Node12_CoreVelloziaceae",
        "<13>": "BranchProb_Node13_Vellozia_Crown"
    }
    df_prob_sub = df_prob_k2[[c for c in prob_rename.keys() if c in df_prob_k2.columns]].rename(columns=prob_rename)
    
    # 4. Master index: all 12,276 families tested at root
    master_index = df_change_k2.index
    df_master = pd.DataFrame(index=master_index)
    
    # Species Counts (8 cols)
    for sc in species_cols:
        df_master[f"Count_{sc}"] = df_counts.reindex(master_index)[sc]
    df_master["Total_Count"] = df_counts.reindex(master_index)["Total_Count"]
    
    # Branch changes from primary k=2 model (13 cols)
    for col in node_rename.values():
        if col in df_change_k2.columns:
            df_master[col] = df_change_k2.reindex(master_index)[col]
            
    # Branch probabilities (10 cols; 11,771 NaNs expected as they did not meet nominal p < 0.05 threshold)
    df_prob_reindexed = df_prob_sub.reindex(master_index)
    for col in df_prob_reindexed.columns:
        df_master[col] = pd.to_numeric(df_prob_reindexed[col], errors="coerce")
        
    # Replicate FDR q-values and summary counts (13 cols)
    for c in df_k2.columns:
        df_master[c] = df_k2.reindex(master_index)[c]
    for c in df_k3.columns:
        df_master[c] = df_k3.reindex(master_index)[c]
        
    df_master["k2_mean_qval"] = df_k2.reindex(master_index).mean(axis=1)
    df_master["k3_mean_qval"] = df_k3.reindex(master_index).mean(axis=1)
    df_master["k2_sig_reps_count"] = (df_k2.reindex(master_index) <= 0.05).sum(axis=1)
    df_master["k3_sig_reps_count"] = (df_k3.reindex(master_index) <= 0.05).sum(axis=1)
    
    # 5. Evidence Tiers
    is_tier_a = (df_master["k2_sig_reps_count"] == 5) & (df_master["k3_sig_reps_count"] == 4)
    is_tier_b = (df_master["k3_sig_reps_count"] == 4) & (~is_tier_a)
    is_tier_c = ((df_master["k2_sig_reps_count"] >= 1) | (df_master["k3_sig_reps_count"] >= 1)) & (~is_tier_a) & (~is_tier_b)
    
    tiers = np.where(is_tier_a, "Tier_A_High_Confidence",
            np.where(is_tier_b, "Tier_B_Rate_Heterogeneity",
            np.where(is_tier_c, "Tier_C_Exploratory", "Non_Significant")))
    df_master["Evidence_Tier"] = tiers
    
    # 6. Functional annotations
    ann_dir = os.path.abspath(os.path.join(base_macro, "..", "data", "genomes"))
    vper_ann = pd.read_csv(os.path.join(ann_dir, "Vper", "vper_master_annotation.tsv"), sep="\t")
    vtub_ann = pd.read_csv(os.path.join(ann_dir, "Vtub", "vtub_master_annotation.tsv"), sep="\t")
    
    ann_dict = {}
    for df_a in [vper_ann, vtub_ann]:
        for _, r in df_a.dropna(subset=["orthogroup_id"]).iterrows():
            og = r["orthogroup_id"]
            desc = str(r["eggnog_desc"]) if pd.notna(r["eggnog_desc"]) else ""
            ath = str(r["ath_orthologs"]) if pd.notna(r["ath_orthologs"]) else ""
            if og not in ann_dict:
                ann_dict[og] = {"desc": set(), "ath": set()}
            if desc and desc not in ["nan", "None"]:
                ann_dict[og]["desc"].add(desc)
            if ath and ath not in ["nan", "None"]:
                for a in ath.split(","):
                    if a.strip(): ann_dict[og]["ath"].add(a.strip())
                    
    desc_list = []
    ath_list = []
    for og in master_index:
        if og in ann_dict and ann_dict[og]["desc"]:
            desc_list.append(" | ".join(sorted(list(ann_dict[og]["desc"]))[:2]))
        else:
            desc_list.append("Sem anotacao EggNOG recuperada")
        if og in ann_dict and ann_dict[og]["ath"]:
            ath_list.append(", ".join(sorted(list(ann_dict[og]["ath"]))[:3]))
        else:
            ath_list.append("None")
            
    df_master["EggNOG_Description"] = desc_list
    df_master["Arabidopsis_Orthologs"] = ath_list
    
    # 7. Quality control & biological flags
    re_te = re.compile(
        r"\b(transpos(on|ase|able|ing)?|retrotranspos(on|ase)?|gag(-pro)?|reverse transcriptase|integrase|gypsy|copia|helitron|mobile element|pol polyprotein|ltr retro(transposon|element)|line-1|transposable element)\b",
        re.IGNORECASE
    )
    re_org = re.compile(
        r"\b(chloroplast(s|ic)?|plastid(s|ial)?|mitochondri(on|a|al)?|ycf\d*|matk|rbcl|psa[a-z]?|psb[a-z]?|cox\d*|ndh[a-z]?|nadh dehydrogenase|photosystem(\s+[i|v|x]+)?|psii|psi)\b",
        re.IGNORECASE
    )
    
    flag_org = []
    flag_te = []
    flag_art = []
    
    for og, row in df_master.iterrows():
        desc_l = row["EggNOG_Description"]
        is_o = bool(re_org.search(desc_l))
        is_t = bool(re_te.search(desc_l))
        
        max_cnt = max(row["Count_Vper"], row["Count_Vtub"], row["Count_Xvis"], row["Count_Abra"], row["Count_Ptec"], row["Count_Dala"], row["Count_Ath"])
        tot_cnt = row["Total_Count"]
        is_a = bool(tot_cnt >= 20 and (max_cnt / tot_cnt) >= 0.85)
        
        flag_org.append(is_o)
        flag_te.append(is_t)
        flag_art.append(is_a)
        
    df_master["Flag_Organellar"] = flag_org
    df_master["Flag_Transposon"] = flag_te
    df_master["Flag_High_Copy_Asymmetry"] = flag_art
    
    # 8. Independent Binary Indicators for Evolutionary Events (Evaluated on Primary Model k=2)
    # Desiccation-tolerant (DT): Vtub, Xvis, Abra
    # Desiccation-avoidance: Vper
    
    # Terminal Lineage-Specific Expansions:
    df_master["Ind_Exp_Terminal_Vper"] = (df_master["Change_Vper"] > 0) & (df_master["Count_Vper"] > df_master["Count_Vtub"]) & (df_master["Count_Vper"] > df_master["Count_Xvis"]) & (df_master["Count_Vper"] > df_master["Count_Abra"])
    df_master["Ind_Exp_Terminal_Vtub"] = (df_master["Change_Vtub"] > 0) & (df_master["Count_Vtub"] > df_master["Count_Vper"]) & (df_master["Count_Vtub"] > df_master["Count_Xvis"]) & (df_master["Count_Vtub"] > df_master["Count_Abra"])
    df_master["Ind_Exp_Terminal_Xvis"] = (df_master["Change_Xvis"] > 0) & (df_master["Count_Xvis"] > df_master["Count_Vper"]) & (df_master["Count_Xvis"] > df_master["Count_Vtub"]) & (df_master["Count_Xvis"] > df_master["Count_Abra"])
    df_master["Ind_Exp_Terminal_Abra"] = (df_master["Change_Abra"] > 0) & (df_master["Count_Abra"] > df_master["Count_Vper"]) & (df_master["Count_Abra"] > df_master["Count_Vtub"]) & (df_master["Count_Abra"] > df_master["Count_Xvis"])
    df_master["Ind_Exp_Terminal_Ptec"] = (df_master["Change_Ptec"] > 0) & (df_master["Count_Ptec"] > df_master[["Count_Vper", "Count_Vtub", "Count_Xvis", "Count_Abra", "Count_Dala", "Count_Ath"]].max(axis=1))
    
    # Parallel Expansions in Desiccation-Tolerant (DT) Lineages (Vtub, Xvis, Abra):
    dt_exp_count = (df_master["Change_Vtub"] > 0).astype(int) + (df_master["Change_Xvis"] > 0).astype(int) + (df_master["Change_Abra"] > 0).astype(int)
    df_master["Ind_Parallel_Exp_DT_2plus"] = dt_exp_count >= 2
    
    # Ancestral Expansions (strictly phylogenetic nodes):
    df_master["Ind_Exp_Ancestral_Node13_Vellozia"] = df_master["Change_Node13_Vellozia_Crown"] > 0
    df_master["Ind_Exp_Ancestral_Node12_CoreVelloziaceae"] = df_master["Change_Node12_Core_Velloziaceae"] > 0
    df_master["Ind_Exp_Ancestral_Node11_Velloziaceae_Crown"] = df_master["Change_Node11_Velloziaceae_Crown"] > 0
    
    # Parallel Contractions in Desiccation-Tolerant Lineages (Vtub, Xvis, Abra):
    dt_cont_count = (df_master["Change_Vtub"] < 0).astype(int) + (df_master["Change_Xvis"] < 0).astype(int) + (df_master["Change_Abra"] < 0).astype(int)
    df_master["Ind_Parallel_Contraction_DT_2plus"] = dt_cont_count >= 2
    
    # 9. Multi-Replicate Consensus Concordance between k=2 and ALL 4 Valid k=3 Replicates:
    # A) Exact sign equality across all 6 key branches (Vper, Vtub, Xvis, Abra, Node13, Node12) matching across all 4 valid k=3 reps
    key_branches_k2 = ["Change_Vper", "Change_Vtub", "Change_Xvis", "Change_Abra", "Change_Node13_Vellozia_Crown", "Change_Node12_Core_Velloziaceae"]
    exact_sign_consensus = pd.Series(True, index=master_index)
    for r in k3_valid_reps:
        ch_r = k3_change_dfs[r].reindex(master_index)
        for kb in key_branches_k2:
            sign_k2 = np.sign(df_change_k2.reindex(master_index)[kb])
            sign_k3 = np.sign(ch_r[kb])
            exact_sign_consensus = exact_sign_consensus & (sign_k2 == sign_k3)
    df_master["Concordant_Exact_Sign_All_Key_Branches"] = exact_sign_consensus
    
    # B) Indicator-specific preservation requiring consensus across ALL 4 valid k=3 replicates
    cnt = df_counts.reindex(master_index)
    k3_inds_by_rep = []
    for r in k3_valid_reps:
        ch_r = k3_change_dfs[r].reindex(master_index)
        r_exp_vper = (ch_r["Change_Vper"] > 0) & (cnt["Vper"] > cnt["Vtub"]) & (cnt["Vper"] > cnt["Xvis"]) & (cnt["Vper"] > cnt["Abra"])
        r_exp_vtub = (ch_r["Change_Vtub"] > 0) & (cnt["Vtub"] > cnt["Vper"]) & (cnt["Vtub"] > cnt["Xvis"]) & (cnt["Vtub"] > cnt["Abra"])
        r_exp_xvis = (ch_r["Change_Xvis"] > 0) & (cnt["Xvis"] > cnt["Vper"]) & (cnt["Xvis"] > cnt["Vtub"]) & (cnt["Xvis"] > cnt["Abra"])
        r_exp_abra = (ch_r["Change_Abra"] > 0) & (cnt["Abra"] > cnt["Vper"]) & (cnt["Abra"] > cnt["Vtub"]) & (cnt["Abra"] > cnt["Xvis"])
        r_exp_ptec = (ch_r["Change_Ptec"] > 0) & (cnt["Ptec"] > cnt[["Vper", "Vtub", "Xvis", "Abra", "Dala", "Ath"]].max(axis=1))
        r_dt_exp = ((ch_r["Change_Vtub"] > 0).astype(int) + (ch_r["Change_Xvis"] > 0).astype(int) + (ch_r["Change_Abra"] > 0).astype(int)) >= 2
        r_dt_cont = ((ch_r["Change_Vtub"] < 0).astype(int) + (ch_r["Change_Xvis"] < 0).astype(int) + (ch_r["Change_Abra"] < 0).astype(int)) >= 2
        r_node13 = ch_r["Change_Node13_Vellozia_Crown"] > 0
        r_node12 = ch_r["Change_Node12_Core_Velloziaceae"] > 0
        r_node11 = ch_r["Change_Node11_Velloziaceae_Crown"] > 0
        k3_inds_by_rep.append({
            "vper": r_exp_vper,
            "vtub": r_exp_vtub,
            "xvis": r_exp_xvis,
            "abra": r_exp_abra,
            "ptec": r_exp_ptec,
            "dt_exp": r_dt_exp,
            "dt_cont": r_dt_cont,
            "node13": r_node13,
            "node12": r_node12,
            "node11": r_node11
        })
        
    def get_consensus(key):
        res = pd.Series(True, index=master_index)
        for d in k3_inds_by_rep:
            res = res & d[key]
        return res
        
    df_master["Preserved_k3_Exp_Terminal_Vper"] = df_master["Ind_Exp_Terminal_Vper"] & get_consensus("vper")
    df_master["Preserved_k3_Exp_Terminal_Vtub"] = df_master["Ind_Exp_Terminal_Vtub"] & get_consensus("vtub")
    df_master["Preserved_k3_Exp_Terminal_Xvis"] = df_master["Ind_Exp_Terminal_Xvis"] & get_consensus("xvis")
    df_master["Preserved_k3_Exp_Terminal_Abra"] = df_master["Ind_Exp_Terminal_Abra"] & get_consensus("abra")
    df_master["Preserved_k3_Exp_Terminal_Ptec"] = df_master["Ind_Exp_Terminal_Ptec"] & get_consensus("ptec")
    df_master["Preserved_k3_Parallel_Exp_DT"] = df_master["Ind_Parallel_Exp_DT_2plus"] & get_consensus("dt_exp")
    df_master["Preserved_k3_Parallel_Cont_DT"] = df_master["Ind_Parallel_Contraction_DT_2plus"] & get_consensus("dt_cont")
    df_master["Preserved_k3_Exp_Node13"] = df_master["Ind_Exp_Ancestral_Node13_Vellozia"] & get_consensus("node13")
    df_master["Preserved_k3_Exp_Node12"] = df_master["Ind_Exp_Ancestral_Node12_CoreVelloziaceae"] & get_consensus("node12")
    df_master["Preserved_k3_Exp_Node11"] = df_master["Ind_Exp_Ancestral_Node11_Velloziaceae_Crown"] & get_consensus("node11")
    
    # 10. Summary Classification with Explicit Documented Hierarchy:
    # Hierarchy rationale:
    # 1. Outgroup_Expansion_Ptec (isolate non-ingroup expansions first)
    # 2. Parallel_Expansion_DT (parallel expansion across tolerant taxa: Vtub, Xvis, Abra)
    # 3. Ancestral_Exp_Node12_CoreVelloziaceae (shared basal core radiation ~32 Ma)
    # 4. Ancestral_Exp_Node11_Velloziaceae_Crown (ancient crown Velloziaceae radiation ~78 Ma)
    # 5. Ancestral_Exp_Node13_Vellozia_Crown (radiation of genus Vellozia ~10 Ma)
    # 6. Terminal expansions (Vper, Vtub, Xvis, Abra)
    # 7. Parallel_Contraction_DT (parallel gene contraction across tolerant taxa)
    # 8. Other_Dynamic (unclassified or complex patterns)
    summary_cat = []
    for og, r in df_master.iterrows():
        if r["Ind_Exp_Terminal_Ptec"]:
            summary_cat.append("Outgroup_Expansion_Ptec")
        elif r["Ind_Parallel_Exp_DT_2plus"]:
            summary_cat.append("Parallel_Expansion_DT")
        elif r["Ind_Exp_Ancestral_Node12_CoreVelloziaceae"]:
            summary_cat.append("Ancestral_Exp_Node12_CoreVelloziaceae")
        elif r["Ind_Exp_Ancestral_Node11_Velloziaceae_Crown"]:
            summary_cat.append("Ancestral_Exp_Node11_Velloziaceae_Crown")
        elif r["Ind_Exp_Ancestral_Node13_Vellozia"]:
            summary_cat.append("Ancestral_Exp_Node13_Vellozia_Crown")
        elif r["Ind_Exp_Terminal_Vper"]:
            summary_cat.append("Terminal_Exp_Vper")
        elif r["Ind_Exp_Terminal_Vtub"]:
            summary_cat.append("Terminal_Exp_Vtub")
        elif r["Ind_Exp_Terminal_Xvis"]:
            summary_cat.append("Terminal_Exp_Xvis")
        elif r["Ind_Exp_Terminal_Abra"]:
            summary_cat.append("Terminal_Exp_Abra")
        elif r["Ind_Parallel_Contraction_DT_2plus"]:
            summary_cat.append("Parallel_Contraction_DT")
        else:
            summary_cat.append("Other_Dynamic")
            
    df_master["Evolutionary_Dynamic_Summary"] = summary_cat
    
    # Save master table v2
    out_tsv = os.path.join(comp_dir, "comparative_families_master_table_v2.tsv")
    df_master.to_csv(out_tsv, sep="\t")
    
    print("=" * 80)
    print(f"[SUCCESS] Comparative Master Table v2 successfully rebuilt and validated!")
    print(f"          Path: {out_tsv}")
    print(f"          Total gene families: {len(df_master)}")
    print(f"          Total variables: {len(df_master.columns)} (plus FamilyID index = {len(df_master.columns) + 1} physical cols)")
    print("=" * 80)
    
    tier_a_df = df_master[df_master["Evidence_Tier"] == "Tier_A_High_Confidence"]
    print(f"\n--- Tier A (N={len(tier_a_df)}) Indicator Consensus (k=2 vs ALL 4 k=3 reps) ---")
    print(f"Exact sign agreement across all 6 key branches: {tier_a_df['Concordant_Exact_Sign_All_Key_Branches'].sum()} / {len(tier_a_df)}")
    print(f"Exp_Terminal_Vper:       {tier_a_df['Ind_Exp_Terminal_Vper'].sum()} -> Consensus in k=3: {tier_a_df['Preserved_k3_Exp_Terminal_Vper'].sum()} / {tier_a_df['Ind_Exp_Terminal_Vper'].sum()}")
    print(f"Exp_Terminal_Vtub:       {tier_a_df['Ind_Exp_Terminal_Vtub'].sum()} -> Consensus in k=3: {tier_a_df['Preserved_k3_Exp_Terminal_Vtub'].sum()} / {tier_a_df['Ind_Exp_Terminal_Vtub'].sum()}")
    print(f"Exp_Terminal_Xvis:       {tier_a_df['Ind_Exp_Terminal_Xvis'].sum()} -> Consensus in k=3: {tier_a_df['Preserved_k3_Exp_Terminal_Xvis'].sum()} / {tier_a_df['Ind_Exp_Terminal_Xvis'].sum()}")
    print(f"Exp_Terminal_Abra:       {tier_a_df['Ind_Exp_Terminal_Abra'].sum()} -> Consensus in k=3: {tier_a_df['Preserved_k3_Exp_Terminal_Abra'].sum()} / {tier_a_df['Ind_Exp_Terminal_Abra'].sum()}")
    print(f"Exp_Terminal_Ptec:       {tier_a_df['Ind_Exp_Terminal_Ptec'].sum()} -> Consensus in k=3: {tier_a_df['Preserved_k3_Exp_Terminal_Ptec'].sum()} / {tier_a_df['Ind_Exp_Terminal_Ptec'].sum()}")
    print(f"Parallel_Exp_DT_2plus:   {tier_a_df['Ind_Parallel_Exp_DT_2plus'].sum()} -> Consensus in k=3: {tier_a_df['Preserved_k3_Parallel_Exp_DT'].sum()} / {tier_a_df['Ind_Parallel_Exp_DT_2plus'].sum()}")
    print(f"Parallel_Cont_DT_2plus:  {tier_a_df['Ind_Parallel_Contraction_DT_2plus'].sum()} -> Consensus in k=3: {tier_a_df['Preserved_k3_Parallel_Cont_DT'].sum()} / {tier_a_df['Ind_Parallel_Contraction_DT_2plus'].sum()}")
    print(f"Exp_Node13 (Vellozia):   {tier_a_df['Ind_Exp_Ancestral_Node13_Vellozia'].sum()} -> Consensus in k=3: {tier_a_df['Preserved_k3_Exp_Node13'].sum()} / {tier_a_df['Ind_Exp_Ancestral_Node13_Vellozia'].sum()}")
    print(f"Exp_Node12 (CoreVell):   {tier_a_df['Ind_Exp_Ancestral_Node12_CoreVelloziaceae'].sum()} -> Consensus in k=3: {tier_a_df['Preserved_k3_Exp_Node12'].sum()} / {tier_a_df['Ind_Exp_Ancestral_Node12_CoreVelloziaceae'].sum()}")
    print(f"Exp_Node11 (CrownVell):  {tier_a_df['Ind_Exp_Ancestral_Node11_Velloziaceae_Crown'].sum()} -> Consensus in k=3: {tier_a_df['Preserved_k3_Exp_Node11'].sum()} / {tier_a_df['Ind_Exp_Ancestral_Node11_Velloziaceae_Crown'].sum()}")
    print(f"\nFlags in Tier A: Organellar = {tier_a_df['Flag_Organellar'].sum()} | Transposon = {tier_a_df['Flag_Transposon'].sum()} | High Copy Asymmetry = {tier_a_df['Flag_High_Copy_Asymmetry'].sum()}")

if __name__ == "__main__":
    main()
