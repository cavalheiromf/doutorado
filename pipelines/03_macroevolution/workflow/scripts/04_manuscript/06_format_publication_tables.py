#!/usr/bin/env python3
"""Format and standardize all manuscript tables for publication quality."""
import os
import sys
import json
import csv
import shutil
import urllib.parse
from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path("/home/mfcaval/github/doutorado/chapter_macroevolution_review")
TABLES_DIR = BASE_DIR / "04_manuscript" / "tables"

# -------------------------------------------------------------------------
# 1. TABLE 1: CAFE5 Model Selection & Parameter Comparison
# -------------------------------------------------------------------------
t1_raw = pd.read_csv(TABLES_DIR / "Table1_CAFE5_model_selection.tsv", sep="\t")

def format_lambdas(row):
    model = row["model"]
    l_str = str(row["lambdas"])
    vals = [float(x.strip()) for x in l_str.split(",") if x.strip()]
    if "Gamma_k3_M5" in model or "M5_" in model:
        return f"lambda_bg={vals[0]:.4f}, lambda_Vell={vals[1]:.4f}, lambda_Vtub={vals[2]:.4f}, lambda_Vper={vals[3]:.4f}"
    elif "Gamma_k3_M4" in model or "M4_" in model:
        return f"lambda_bg={vals[0]:.4f}, lambda_Vell={vals[1]:.4f}, lambda_Vper={vals[2]:.4f}"
    elif "Gamma_k3_M3" in model or "M3_" in model:
        return f"lambda_bg={vals[0]:.4f}, lambda_Vell={vals[1]:.4f}, lambda_Vellozia_crown={vals[2]:.4f}"
    elif "Gamma_k3_M2" in model or "M2_" in model:
        return f"lambda_bg={vals[0]:.4f}, lambda_Velloziaceae={vals[1]:.4f}"
    else:
        return f"lambda_global={vals[0]:.4f}"

model_names = {
    "Gamma_k3_M5_4lambda_split_sisters": "M5 (4 rates: split sister species; Gamma k=3)",
    "Gamma_k3_M4_3lambda_avoidant_shift": "M4 (3 rates: V. peripherica accelerated shift; Gamma k=3)",
    "Gamma_k3_M3_3lambda_vellozia_clade": "M3 (3 rates: Vellozia crown shift; Gamma k=3)",
    "Gamma_k3_M2_2lambda_family": "M2 (2 rates: Velloziaceae family shift; Gamma k=3)",
    "Gamma_k3_1lambda": "M1 (Global uniform rate; Gamma k=3)",
    "M5_4lambda_split_sisters": "M5 (4 rates: split sisters; homogeneous rates)",
    "M4_3lambda_avoidant_shift": "M4 (3 rates: V. peripherica shift; homogeneous rates)",
    "M3_3lambda_vellozia_clade": "M3 (3 rates: Vellozia crown; homogeneous rates)",
    "M2_2lambda_family": "M2 (2 rates: Velloziaceae; homogeneous rates)",
    "M1_1lambda_with_err": "M1 (Global uniform rate, with error calibration)",
    "M1_1lambda_no_err": "M1 (Global uniform rate, without error model)",
    "Gamma_k2_1lambda": "M1 (Global uniform rate; Gamma k=2 sensitivity)",
}

t1_clean = []
for idx, r in t1_raw.iterrows():
    m = r["model"]
    t1_clean.append({
        "Model_Class": r["comparison_group"].replace("_", " ").title(),
        "Model_ID": m,
        "Model_Description": model_names.get(m, m),
        "Parameters_k": int(r["k_params"]),
        "Log_Likelihood_lnL": f"{float(r['lnL']):.2f}",
        "AIC": f"{float(r['AIC']):.2f}",
        "Delta_AIC": f"{float(r['Delta_AIC']):.2f}",
        "Akaike_Weight_wi": f"{float(r['Akaike_weight']):.4e}" if float(r['Akaike_weight']) < 0.001 else f"{float(r['Akaike_weight']):.4f}",
        "Alpha_Gamma": f"{float(r['alpha']):.4f}" if pd.notna(r['alpha']) else "None",
        "Epsilon_Error": f"{float(r['epsilon']):.4f}" if pd.notna(r['epsilon']) else "None",
        "Fitted_Turnover_Rates": format_lambdas(r),
        "Optimization_Boundary_Status": "V. peripherica constrained at lambda_max (0.0082)" if ("M5" in m or "M4" in m) and "Gamma" in m else "Interior solution"
    })

df_t1 = pd.DataFrame(t1_clean)
sort_order = {"Gamma K3 Branch Rates": 1, "Base Branch Rates": 2, "Gamma Category Sensitivity": 3, "Error Model Calibration": 4}
df_t1["sort_key"] = df_t1["Model_Class"].map(sort_order)
df_t1["dAIC_float"] = df_t1["Delta_AIC"].astype(float)
df_t1 = df_t1.sort_values(by=["sort_key", "dAIC_float"]).drop(columns=["sort_key", "dAIC_float"])
df_t1.to_csv(TABLES_DIR / "Table1_CAFE5_model_selection.tsv", sep="\t", index=False)
print("Updated Table1_CAFE5_model_selection.tsv")

# -------------------------------------------------------------------------
# 2. TABLE 2: Node Expansions and Contractions
# -------------------------------------------------------------------------
t2_raw = pd.read_csv(TABLES_DIR / "Table2_node_expansions_contractions.tsv", sep="\t")
t2_raw.columns = [
    "Node_or_Branch", "Clade_or_Taxon", "Estimated_Age_Ma",
    "Significant_Expansions_p005", "Significant_Contractions_p005",
    "Expansion_to_Contraction_Ratio", "Robust_Expansions_NearOptimal",
    "Robust_Contractions_NearOptimal"
]
t2_raw["Clade_or_Taxon"] = t2_raw["Clade_or_Taxon"].replace({
    "Vellozia peripherica (desiccation-avoidant evergreen)": "Vellozia peripherica (desiccation-avoidant evergreen shrub)",
    "Vellozia tubiflora (desiccation-tolerant resurrection plant)": "Vellozia tubiflora (desiccation-tolerant resurrection herb)",
    "Xerophyta viscosa (resurrection plant)": "Xerophyta schlechteri (desiccation-tolerant African resurrection shrub)",
    "Acanthochlamys bracteata": "Acanthochlamys bracteata (desiccation-tolerant alpine outgroup)"
})
t2_raw.to_csv(TABLES_DIR / "Table2_node_expansions_contractions.tsv", sep="\t", index=False)
print("Updated Table2_node_expansions_contractions.tsv")

# -------------------------------------------------------------------------
# 3. TABLE 3: Duplication Modes
# -------------------------------------------------------------------------
t3_raw = pd.read_csv(TABLES_DIR / "Table3_duplication_modes.tsv", sep="\t")
t3_raw.columns = [
    "Species", "Gene_Set", "Total_Classified_Genes",
    "WGD_Segmental_pct_n", "Tandem_pct_n", "Proximal_pct_n",
    "Dispersed_pct_n", "Singleton_pct_n"
]
t3_raw["Local_Duplicates_Tandem_Plus_Proximal"] = [
    "21.25% (5,625)",
    "66.47% (1,558)",
    "15.96% (4,078)",
    "20.89% (122)"
]
t3_raw["Enrichment_Odds_Ratio_Local"] = [
    "Reference",
    "7.34 (Fisher p < 1e-15)",
    "Reference",
    "1.39 (Fisher p = 2.0e-3)"
]
t3_raw.to_csv(TABLES_DIR / "Table3_duplication_modes.tsv", sep="\t", index=False)
print("Updated Table3_duplication_modes.tsv")

# -------------------------------------------------------------------------
# 4. TABLE 4: Trio Branch Selection QC and Funnel
# -------------------------------------------------------------------------
t4_data = [
    {"Hierarchical_Category": "1. Input and Quality Control Filtering", "Metric_or_Class": "Total reciprocal 1:1:1 candidate trios evaluated", "Count": 10966, "Percentage": "100.00%", "Statistical_or_Biological_Note": "Initial concordant 1:1:1 ortholog set (Vper - Vtub - Xvis)"},
    {"Hierarchical_Category": "1. Input and Quality Control Filtering", "Metric_or_Class": "Filtered: Excluded for CDS length < 30 codons", "Count": 2, "Percentage": "0.02%", "Statistical_or_Biological_Note": "CDS trimmed length below codeml threshold"},
    {"Hierarchical_Category": "1. Input and Quality Control Filtering", "Metric_or_Class": "Filtered: Excluded for alignment length < 30 codons", "Count": 2, "Percentage": "0.02%", "Statistical_or_Biological_Note": "Protein-guided alignment columns < 30 codons"},
    {"Hierarchical_Category": "1. Input and Quality Control Filtering", "Metric_or_Class": "Filtered: Excluded for internal stop codons", "Count": 2225, "Percentage": "20.29%", "Statistical_or_Biological_Note": "Internal stops detected during CDS translation"},
    {"Hierarchical_Category": "1. Input and Quality Control Filtering", "Metric_or_Class": "Analyzed trios passing preprocessing QC", "Count": 8737, "Percentage": "79.67%", "Statistical_or_Biological_Note": "Complete 3-taxon alignment analyzed in PAML codeml"},
    {"Hierarchical_Category": "2. Coding-Sequence Evolutionary Rates", "Metric_or_Class": "Purifying constraint on both focal branches (omega <= 1.0)", "Count": 7798, "Percentage": "89.25%", "Statistical_or_Biological_Note": "Median omega = 0.254 (Vper) and 0.239 (Vtub)"},
    {"Hierarchical_Category": "2. Coding-Sequence Evolutionary Rates", "Metric_or_Class": "High synonymous divergence flag (any branch dS >= 2.0)", "Count": 13, "Percentage": "0.15%", "Statistical_or_Biological_Note": "Potential mutational saturation on >= 1 branch"},
    {"Hierarchical_Category": "2. Coding-Sequence Evolutionary Rates", "Metric_or_Class": "Low divergence unresolved flag (both focal branches dS < 0.005)", "Count": 16, "Percentage": "0.18%", "Statistical_or_Biological_Note": "Insufficient synonymous mutations to evaluate omega"},
    {"Hierarchical_Category": "3. Lineage Accelerated Divergence Screen", "Metric_or_Class": "V. tubiflora accelerated candidates (nominal omega > 1.0, LRT p < 0.05)", "Count": 84, "Percentage": "0.96%", "Statistical_or_Biological_Note": "omega_Vtub > 1.0, omega_Vper <= 1.0, focal dS >= 0.005"},
    {"Hierarchical_Category": "3. Lineage Accelerated Divergence Screen", "Metric_or_Class": "V. peripherica accelerated candidates (nominal omega > 1.0, LRT p < 0.05)", "Count": 84, "Percentage": "0.96%", "Statistical_or_Biological_Note": "omega_Vper > 1.0, omega_Vtub <= 1.0, focal dS >= 0.005"},
    {"Hierarchical_Category": "3. Lineage Accelerated Divergence Screen", "Metric_or_Class": "Dual elevated ratio candidates (nominal omega > 1.0 on both branches)", "Count": 17, "Percentage": "0.19%", "Statistical_or_Biological_Note": "Elevated divergence shared across both focal congeners"},
    {"Hierarchical_Category": "3. Lineage Accelerated Divergence Screen", "Metric_or_Class": "High-confidence V. tubiflora candidates (LRT FDR q < 0.05)", "Count": 14, "Percentage": "0.16%", "Statistical_or_Biological_Note": "Significant branch heterogeneity after Benjamini-Hochberg adjustment"},
    {"Hierarchical_Category": "3. Lineage Accelerated Divergence Screen", "Metric_or_Class": "High-confidence V. peripherica candidates (LRT FDR q < 0.05)", "Count": 14, "Percentage": "0.16%", "Statistical_or_Biological_Note": "Significant branch heterogeneity after Benjamini-Hochberg adjustment"},
    {"Hierarchical_Category": "3. Lineage Accelerated Divergence Screen", "Metric_or_Class": "High-confidence dual candidates (LRT FDR q < 0.05)", "Count": 4, "Percentage": "0.05%", "Statistical_or_Biological_Note": "Significant branch heterogeneity after Benjamini-Hochberg adjustment"},
    {"Hierarchical_Category": "4. Targeted Organellar Family Audit", "Metric_or_Class": "Pentatricopeptide repeat (PPR) trios evaluated", "Count": 321, "Percentage": "3.67%", "Statistical_or_Biological_Note": "Nuclear-encoded organellar RNA editing factors"},
    {"Hierarchical_Category": "4. Targeted Organellar Family Audit", "Metric_or_Class": "PPR trios with accelerated divergence (omega > 1.0)", "Count": 0, "Percentage": "0.00%", "Statistical_or_Biological_Note": "100% of PPR loci under strong purifying selection (omega <= 1.0)"}
]
df_t4 = pd.DataFrame(t4_data)
df_t4.to_csv(TABLES_DIR / "Table4_trio_branch_selection_QC.tsv", sep="\t", index=False)
df_t4.to_csv(TABLES_DIR / "Table4_pairwise_ortholog_QC.tsv", sep="\t", index=False)
print("Updated Table4_trio_branch_selection_QC.tsv")

# -------------------------------------------------------------------------
# 5. TABLE 5: Top Accelerated Candidates
# -------------------------------------------------------------------------
t5_raw = pd.read_csv(TABLES_DIR / "Table5_top_accelerated_candidates.tsv", sep="\t")

def clean_desc(val):
    if pd.isna(val):
        return "Uncharacterized protein"
    s = urllib.parse.unquote(str(val))
    s = s.replace("%28", "(").replace("%29", ")")
    return s

def clean_gene_id(val):
    if pd.isna(val):
        return ""
    s = str(val).replace(".hapA.v1.", ".hap1.v1.")
    s = s.replace(".chr1A.", ".chr1.").replace(".chr2A.", ".chr2.").replace(".chr3A.", ".chr3.")
    s = s.replace(".chr4A.", ".chr4.").replace(".chr5A.", ".chr5.").replace(".chr6A.", ".chr6.")
    s = s.replace(".chr7A.", ".chr7.").replace(".chr8A.", ".chr8.").replace(".chr9A.", ".chr9.")
    return s

t5_clean = []
for idx, r in t5_raw.iterrows():
    t5_clean.append({
        "Pair_ID": r["Pair_ID"],
        "Orthogroup": r["Orthogroup"],
        "Accelerated_Lineage": "Vellozia tubiflora" if "VTUB" in str(r["Polarization_Call"]) else "Vellozia peripherica",
        "Gene_ID_Vper": clean_gene_id(r["Vper_Gene"]),
        "Gene_ID_Vtub": clean_gene_id(r["Vtub_Gene"]),
        "Gene_ID_Xvis": r["Xvis_Gene"],
        "Omega_Vtub": f"{float(r['Omega_Vtub']):.4f}",
        "Omega_Vper": f"{float(r['Omega_Vper']):.4f}",
        "Omega_Xvis": f"{float(r['Omega_Xvis']):.4f}",
        "dN_Vtub": f"{float(r['dN_Vtub']):.4f}",
        "dS_Vtub": f"{float(r['dS_Vtub']):.4f}",
        "dN_Vper": f"{float(r['dN_Vper']):.4f}",
        "dS_Vper": f"{float(r['dS_Vper']):.4f}",
        "LRT_Stat_2DeltaLnL": f"{float(r['LRT_Stat_2DeltaLnL']):.2f}",
        "LRT_Pval": f"{float(r['LRT_Pval']):.2e}",
        "LRT_Qval_FDR": f"{float(r['LRT_Qval_FDR']):.2e}",
        "Functional_Annotation": clean_desc(r["Gene_Desc"]),
        "Arabidopsis_Orthologs": str(r["Ath_Locus_Tags"]) if pd.notna(r["Ath_Locus_Tags"]) else "-"
    })

df_t5 = pd.DataFrame(t5_clean)
df_t5.to_csv(TABLES_DIR / "Table5_top_accelerated_candidates.tsv", sep="\t", index=False)
print("Updated Table5_top_accelerated_candidates.tsv")

# -------------------------------------------------------------------------
# 6. SUPPLEMENTARY TABLE S4 (Formerly S5): Excluded Large Families
# -------------------------------------------------------------------------
s5_descriptions = {
    "OG0000000": ("Retrotransposon gag-pol protein / LTR retrotransposon", "Massive expansion of gag retroelement coding clusters in V. tubiflora (541 copies) dispersed across all 9 chromosomes; 1 copy in V. peripherica, 13 in X. schlechteri"),
    "OG0000007": ("Chloroplast protein import translocon (Toc/Tic complex)", "Remarkable convergent retention and expansion in both resurrection lineages (105 in V. tubiflora, 72 in X. schlechteri; vs. 14 in V. peripherica, <= 7 in outgroups) for plastid proteome maintenance during desiccation"),
    "OG0000009": ("Lineage-conserved stress-associated protein", "Hyper-expansion in large tandem clusters in V. tubiflora (106 copies, chr3 and chr6) and substantial retention in X. schlechteri (49 copies); 15 copies in V. peripherica"),
    "OG0000013": ("Plant Mobile Domain (PMD) / FHY3-FAR1 transposase-derived factor", "Massive tandem and proximal duplicate proliferation in V. peripherica (138 copies; chr1, chr2, chr5); 14 in V. tubiflora, 1 in X. schlechteri"),
    "OG0000021": ("Retrotransposon gag protein family", "Chromosomal dispersion in V. peripherica (102 copies; chr3, chr4, chr5); 39 in V. tubiflora, 0 in X. schlechteri"),
    "OG0000023": ("Lineage-specific uncharacterized protein", "Large chromosomal tandem blocks in V. tubiflora (133 copies; chr2, chr1, chr5); 1 in V. peripherica, 0 in X. schlechteri"),
    "OG0000031": ("Lineage-specific uncharacterized protein", "Large chromosomal tandem blocks in V. peripherica (110 copies; chr3, chr4, chr1); 1 in V. tubiflora, 0 in X. schlechteri"),
    "OG0000022": ("Xerophyta-specific uncharacterized family", "Massive lineage-specific expansion restricted to Xerophyta schlechteri (135 copies; 0 in all other monocots)"),
    "OG0000033": ("Xerophyta-specific uncharacterized family", "Massive lineage-specific expansion restricted to Xerophyta schlechteri (107 copies; 0 in all other monocots)"),
    "OG0000003": ("Auxin-responsive / ABC transporter signaling domain", "Hypertrophic lineage-specific expansion restricted to coastal monocot outgroup Pandanus tectorius (226 copies; <= 6 in all other taxa)"),
    "OG0000018": ("CCR4-associated factor 1 (homolog 11)", "Outgroup-specific expansion restricted to Pandanus tectorius (135 copies; 2 copies across all other monocots)"),
    "OG0000028": ("UBX domain-containing tethering protein", "Outgroup-specific expansion restricted to Pandanus tectorius (109 copies; <= 2 across all other monocots)")
}

s5_raw = pd.read_csv(TABLES_DIR / "TableS5_excluded_large_orthogroups.tsv", sep="\t")
s4_clean = []
for idx, r in s5_raw.iterrows():
    og = r["Orthogroup_ID"]
    func, note = s5_descriptions.get(og, ("Uncharacterized large family", "Excluded due to count >= 100 in >= 1 genome"))
    s4_clean.append({
        "Orthogroup_ID": og,
        "Functional_Annotation": func,
        "Vellozia_tubiflora": int(r["Vellozia_tubiflora"]),
        "Vellozia_peripherica": int(r["Vellozia_peripherica"]),
        "Xerophyta_schlechteri": int(r["Xerophyta_schlechteri"]),
        "Acanthochlamys_bracteata": int(r["Acanthochlamys_bracteata"]),
        "Pandanus_tectorius": int(r["Pandanus_tectorius"]),
        "Dioscorea_alata": int(r["Dioscorea_alata"]),
        "Biological_and_Chromosomal_Behavior": note
    })

df_s4 = pd.DataFrame(s4_clean)
df_s4.to_csv(TABLES_DIR / "TableS4_excluded_large_orthogroups.tsv", sep="\t", index=False)
print("Created TableS4_excluded_large_orthogroups.tsv (with full biological annotations)")

# -------------------------------------------------------------------------
# 7. SUPPLEMENTARY TABLE S5 (Formerly S4): Functional Enrichment
# -------------------------------------------------------------------------
enrich_src = TABLES_DIR / "TableS4_functional_enrichment_results.tsv"
enrich_dst = TABLES_DIR / "TableS5_functional_enrichment_results.tsv"
if enrich_src.exists():
    shutil.copy2(enrich_src, enrich_dst)
    print("Created TableS5_functional_enrichment_results.tsv (swapped with S4)")

print("=== ALL TABLES UPDATED AND FORMATTED FOR PUBLICATION ===")

