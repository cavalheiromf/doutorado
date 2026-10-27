#!/usr/bin/env python3
"""
00_build_master_table_6taxa.py

Constrói a Tabela Mestre Comparativa de Famílias Gênicas (comparative_families_master_table_v2.tsv)
a partir da modelagem CAFE5 de 6 monocotiledôneas (Dala, Ptec, Abra, Xvis, Vper, Vtub):
  - Contagens das 6 espécies (+ Count_Ath do OrthoFinder mantida apenas para compatibilidade de QC de anotação).
  - Réplicas convergidas do modelo Gamma k=2 (5 réplicas: rep_1 a rep_5) e Gamma k=3 (4 réplicas ótimas: rep_1, rep_2, rep_3, rep_5).
  - Mudanças por ramo (Gamma_change.tab) e probabilidades específicas de ramo (Gamma_branch_probabilities.tab)
    com a numeração correta dos nós internos da árvore de 6 táxons:
      * <7>  = Raiz Monocots (Dala vs Pandanales)
      * <8>  = Pandanales Crown (Ptec vs Velloziaceae)
      * <9>  = Velloziaceae Crown (Abra vs Core Velloziaceae) [mapeado também para Node11 para compatibilidade]
      * <10> = Core Velloziaceae (Xvis vs Vellozia)           [mapeado também para Node12 para compatibilidade]
      * <11> = Vellozia Crown (Vper vs Vtub)                  [mapeado também para Node13 para compatibilidade]
  - Indicadores binários de expansão e contração baseados no p-valor específico do ramo (BranchProb < 0.05)
    e nos modos de duplicação gênica (Tandem/Proximal) do MCScanX.
"""

import os
import re
from pathlib import Path
import numpy as np
import pandas as pd

BASE_MACRO = "/home/mfcaval/github/doutorado/chapter_macroevolution_review"
CAFE_DIR = os.path.join(BASE_MACRO, "04_gene_families", "cafe5")
COMP_DIR = os.path.join(BASE_MACRO, "04_gene_families", "comparative_axes")
DUP_DIR = os.path.join(BASE_MACRO, "04_gene_families", "synteny", "duplications")
M5_CONVERGENCE = Path(CAFE_DIR) / "summary" / "M5_gamma_convergence_summary.tsv"

NODE_RENAME = {
    "Vper<1>": "Change_Vper",
    "Vtub<2>": "Change_Vtub",
    "Xvis<3>": "Change_Xvis",
    "Abra<4>": "Change_Abra",
    "Ptec<5>": "Change_Ptec",
    "Dala<6>": "Change_Dala",
    "<7>": "Change_Node9_Monocots",
    "<8>": "Change_Node10_Pandanales",
    "<9>": "Change_Node11_Velloziaceae_Crown",
    "<10>": "Change_Node12_Core_Velloziaceae",
    "<11>": "Change_Node13_Vellozia_Crown",
}

PROB_RENAME = {key: value.replace("Change_", "BranchProb_") for key, value in NODE_RENAME.items()}

BRANCHES = {
    "Vper": ("Change_Vper", "BranchProb_Vper"),
    "Vtub": ("Change_Vtub", "BranchProb_Vtub"),
    "Xvis": ("Change_Xvis", "BranchProb_Xvis"),
    "Abra": ("Change_Abra", "BranchProb_Abra"),
    "Ptec": ("Change_Ptec", "BranchProb_Ptec"),
    "Dala": ("Change_Dala", "BranchProb_Dala"),
    "Node10_Pandanales": ("Change_Node10_Pandanales", "BranchProb_Node10_Pandanales"),
    "Node11_Velloziaceae_Crown": (
        "Change_Node11_Velloziaceae_Crown",
        "BranchProb_Node11_Velloziaceae_Crown",
    ),
    "Node12_CoreVelloziaceae": (
        "Change_Node12_Core_Velloziaceae",
        "BranchProb_Node12_Core_Velloziaceae",
    ),
    "Node13_Vellozia": ("Change_Node13_Vellozia_Crown", "BranchProb_Node13_Vellozia_Crown"),
}


def _as_bool(series):
    if series.dtype == bool:
        return series
    return series.astype(str).str.lower().eq("true")


def resolve_m5_runs(summary_path=M5_CONVERGENCE):
    """Return the selected M5 run and all near-optimal sensitivity runs."""
    summary = pd.read_csv(summary_path, sep="\t")
    selected = summary[_as_bool(summary["selected_primary"])]
    near = summary[_as_bool(summary["near_optimal"])].copy()
    if "neg_lnL" in near:
        near = near.sort_values("neg_lnL")
    if len(selected) != 1 or near.empty:
        raise ValueError("M5 convergence summary must contain one primary and >=1 near-optimal run")
    return Path(selected.iloc[0]["rep_dir"]), [Path(value) for value in near["rep_dir"]]


def intersect_flags(flags):
    """Strict robustness call: a family must be significant in every run."""
    if not flags:
        raise ValueError("At least one replicate flag series is required")
    return pd.concat(flags, axis=1).fillna(False).all(axis=1)


def load_branch_run(rep_dir):
    change = pd.read_csv(Path(rep_dir) / "Gamma_change.tab", sep="\t").set_index("FamilyID")
    change = change.rename(columns=NODE_RENAME)
    probability = pd.read_csv(Path(rep_dir) / "Gamma_branch_probabilities.tab", sep="\t")
    probability = probability.rename(columns={probability.columns[0]: "FamilyID"}).set_index("FamilyID")
    probability = probability.rename(columns=PROB_RENAME)
    for column in probability.columns:
        probability[column] = pd.to_numeric(probability[column], errors="coerce")
    return change, probability


def branch_flag(change, probability, branch, direction):
    change_col, prob_col = BRANCHES[branch]
    values = pd.to_numeric(change[change_col], errors="coerce").fillna(0)
    pvalues = probability[prob_col].reindex(change.index).fillna(1.0)
    sign = values.gt(0) if direction == "Exp" else values.lt(0)
    return sign & pvalues.lt(0.05)


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
    os.makedirs(COMP_DIR, exist_ok=True)

    # 1. Contagens brutas (incluindo Ath para rastreamento de anotação TAIR, mas Total_Count reflete as 6 monocots)
    og_counts_file = os.path.join(
        BASE_MACRO, "01_orthology", "results", "Results_Aug30", "Orthogroups", "Orthogroups.GeneCount.tsv"
    )
    df_og_counts = pd.read_csv(og_counts_file, sep="\t").set_index("Orthogroup")
    df_og_counts = df_og_counts.rename(columns={c: c.replace(".pep", "") for c in df_og_counts.columns})

    monocot_cols = ["Abra", "Dala", "Ptec", "Vper", "Vtub", "Xvis"]
    all_sp_cols = ["Abra", "Ath", "Dala", "Ptec", "Vper", "Vtub", "Xvis"]
    for sc in all_sp_cols:
        df_og_counts[sc] = df_og_counts[sc].astype(int)
    df_og_counts["Total_Count"] = df_og_counts[monocot_cols].sum(axis=1)

    # 2. Réplicas globais retidas para o controle de evolução rápida na árvore
    s2_dir = os.path.join(CAFE_DIR, "runs", "stage2_gamma_rates")
    k2_valid_reps = ["rep_1", "rep_2", "rep_3", "rep_4", "rep_5"]
    k3_valid_reps = ["rep_1", "rep_2", "rep_3", "rep_5"]  # rep_4 ficou em ótimo local (-96610.5 vs -96278.7)

    k2_qvals = {}
    for r in k2_valid_reps:
        res_f = os.path.join(s2_dir, "gamma_k2", r, "Gamma_family_results.txt")
        df_res = load_family_results(res_f)
        k2_qvals[f"qval_k2_{r}"] = df_res["qvalue"]
    df_k2 = pd.DataFrame(k2_qvals)

    k3_qvals = {}
    for r in k3_valid_reps:
        res_f = os.path.join(s2_dir, "gamma_k3", r, "Gamma_family_results.txt")
        df_res = load_family_results(res_f)
        k3_qvals[f"qval_k3_{r}"] = df_res["qvalue"]
    df_k3 = pd.DataFrame(k3_qvals)

    # 3. Mudanças e probabilidades por ramo do modelo selecionado: M5+Gamma.
    primary_run, sensitivity_runs = resolve_m5_runs()
    df_change_prim, df_prob_prim = load_branch_run(primary_run)

    # 4. Índice mestre: todas as 12.876 famílias avaliadas na raiz das 6 monocotiledôneas
    master_index = df_change_prim.index
    df_master = pd.DataFrame(index=master_index)

    for sc in all_sp_cols:
        df_master[f"Count_{sc}"] = df_og_counts.reindex(master_index)[sc]
    df_master["Total_Count"] = df_og_counts.reindex(master_index)["Total_Count"]

    for col in NODE_RENAME.values():
        if col in df_change_prim.columns:
            df_master[col] = df_change_prim.reindex(master_index)[col]

    df_prob_reindexed = df_prob_prim.reindex(master_index)
    for col in df_prob_reindexed.columns:
        df_master[col] = pd.to_numeric(df_prob_reindexed[col], errors="coerce").fillna(1.0)

    df_master["CAFE_Primary_Model"] = "Gamma_k3_M5_4lambda_split_sisters"
    df_master["CAFE_Primary_Replicate"] = primary_run.name
    df_master["CAFE_Sensitivity_Replicates"] = ",".join(path.name for path in sensitivity_runs)

    for c in df_k2.columns:
        df_master[c] = df_k2.reindex(master_index)[c]
    for c in df_k3.columns:
        df_master[c] = df_k3.reindex(master_index)[c]

    df_master["k2_mean_qval"] = df_k2.reindex(master_index).mean(axis=1)
    df_master["k3_mean_qval"] = df_k3.reindex(master_index).mean(axis=1)
    df_master["k2_sig_reps_count"] = (df_k2.reindex(master_index) <= 0.05).sum(axis=1)
    df_master["k3_sig_reps_count"] = (df_k3.reindex(master_index) <= 0.05).sum(axis=1)

    # 5. Famílias com evolução rápida significativa na árvore inteira (consenso k=2 e k=3)
    df_master["Family_Wide_Significant"] = (
        (df_master["k2_sig_reps_count"] == len(k2_valid_reps))
        & (df_master["k3_sig_reps_count"] == len(k3_valid_reps))
    )

    # 6. Anotações funcionais (EggNOG de Vper e Vtub)
    ann_dir = "/home/mfcaval/github/doutorado/data/genomes"
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
                    if a.strip():
                        ann_dict[og]["ath"].add(a.strip())

    df_master["EggNOG_Description"] = [
        " | ".join(sorted(list(ann_dict[og]["desc"]))[:2]) if (og in ann_dict and ann_dict[og]["desc"]) else "Sem anotacao EggNOG recuperada"
        for og in master_index
    ]
    df_master["Arabidopsis_Orthologs"] = [
        ", ".join(sorted(list(ann_dict[og]["ath"]))[:3]) if (og in ann_dict and ann_dict[og]["ath"]) else "None"
        for og in master_index
    ]

    # 7. Flags de controle de qualidade (Organelar, Transposon, Assimetria de cópias nas 6 espécies)
    re_te = re.compile(
        r"\b(transpos(on|ase|able|ing)?|retrotranspos(on|ase)?|gag(-pro)?|reverse transcriptase|integrase|gypsy|copia|helitron|mobile element|pol polyprotein|ltr retro(transposon|element)|line-1|transposable element)\b",
        re.IGNORECASE,
    )
    re_org = re.compile(
        r"\b(chloroplast(s|ic)?|plastid(s|ial)?|mitochondri(on|a|al)?|ycf\d*|matk|rbcl|psa[a-z]?|psb[a-z]?|cox\d*|ndh[a-z]?|nadh dehydrogenase|photosystem(\s+[i|v|x]+)?|psii|psi)\b",
        re.IGNORECASE,
    )

    df_master["Flag_Organellar"] = [bool(re_org.search(d)) for d in df_master["EggNOG_Description"]]
    df_master["Flag_Transposon"] = [bool(re_te.search(d)) for d in df_master["EggNOG_Description"]]

    max_6 = df_master[[f"Count_{s}" for s in monocot_cols]].max(axis=1)
    df_master["Flag_High_Copy_Asymmetry"] = (df_master["Total_Count"] >= 20) & ((max_6 / df_master["Total_Count"]) >= 0.85)

    # 8. Integração com Modos de Duplicação (MCScanX) por família em Vper e Vtub
    df_dup_vper = pd.read_csv(os.path.join(DUP_DIR, "vper_gene_duplications_annotated.tsv"), sep="\t")
    vper_local_ogs = set(
        df_dup_vper[df_dup_vper["dup_type"].isin(["Tandem", "Proximal"])]["orthogroup"].unique()
    )
    df_master["Has_Vper_Tandem_Proximal"] = df_master.index.isin(vper_local_ogs)

    # 9. Indicadores binários do modelo primário e consenso entre ótimos próximos.
    primary_flags = {}
    sensitivity_flags = {branch: {direction: {} for direction in ("Exp", "Cont")} for branch in BRANCHES}
    for branch in BRANCHES:
        for direction in ("Exp", "Cont"):
            primary_flags[(branch, direction)] = branch_flag(
                df_change_prim, df_prob_prim, branch, direction
            )

    for run_dir in sensitivity_runs:
        change_run, prob_run = load_branch_run(run_dir)
        rep = run_dir.name
        for branch in BRANCHES:
            for direction in ("Exp", "Cont"):
                values = branch_flag(change_run, prob_run, branch, direction).reindex(master_index).fillna(False)
                sensitivity_flags[branch][direction][rep] = values
                df_master[f"BranchSig_{direction}_{branch}_{rep}"] = values

    for branch in BRANCHES:
        for direction in ("Exp", "Cont"):
            df_master[f"BranchSig_{direction}_{branch}"] = primary_flags[(branch, direction)].reindex(master_index)
            df_master[f"BranchSig_{direction}_{branch}_Robust"] = intersect_flags(
                sensitivity_flags[branch][direction]
            ).reindex(master_index).fillna(False)

    df_master["BranchSig_Exp_Vper_LocalDup"] = df_master["BranchSig_Exp_Vper"] & df_master["Has_Vper_Tandem_Proximal"]
    # Compatibility alias consumed by existing enrichment configuration.
    df_master["BranchSig_Exp_Node12_CoreVelloz"] = df_master["BranchSig_Exp_Node12_CoreVelloziaceae"]

    out_tsv = os.path.join(COMP_DIR, "comparative_families_master_table_v2.tsv")
    df_master.to_csv(out_tsv, sep="\t")
    print("=" * 80)
    print(f"[SUCCESS] Tabela Mestre de 6 Táxons salva em: {out_tsv}")
    print(f"          Total de famílias avaliadas na raiz: {len(df_master)}")
    print(f"          Evolução rápida na árvore inteira (Family_Wide_Significant): {df_master['Family_Wide_Significant'].sum()}")
    print(f"          Expansões significativas no ramo Vper (Avoidant, p < 0.05): {df_master['BranchSig_Exp_Vper'].sum()}")
    print(f"          Expansões Vper com duplicação Tandem/Proximal: {df_master['BranchSig_Exp_Vper_LocalDup'].sum()}")
    print(f"          Contrações significativas no ramo Vper (Avoidant, p < 0.05): {df_master['BranchSig_Cont_Vper'].sum()}")
    print(f"          Expansões significativas no ramo Vtub (DT, p < 0.05): {df_master['BranchSig_Exp_Vtub'].sum()}")
    print(f"          Contrações significativas no ramo Vtub (DT, p < 0.05): {df_master['BranchSig_Cont_Vtub'].sum()}")
    print(f"          Modelo/replicata primária: M5+Gamma/{primary_run.name}")
    print(f"          Replicatas de sensibilidade: {', '.join(path.name for path in sensitivity_runs)}")
    print(f"          Expansões Vper robustas nas replicatas: {df_master['BranchSig_Exp_Vper_Robust'].sum()}")
    print("=" * 80)


if __name__ == "__main__":
    main()

