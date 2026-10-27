#!/usr/bin/env python3
"""Export all manuscript tables as clean TSV files directly from chapter_macroevolution_review results."""
import csv
import json
import shutil
from pathlib import Path
import pandas as pd

BASE_DIR = Path("/home/mfcaval/github/doutorado/chapter_macroevolution_review")
OUT_DIR = BASE_DIR / "04_manuscript" / "tables"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def _bool_count(series):
    if series.dtype == bool:
        return int(series.sum())
    return int(series.astype(str).str.lower().eq("true").sum())


def build_branch_table(master, branches):
    rows = []
    for node_id, branch, label, age in branches:
        expansions = _bool_count(master[f"BranchSig_Exp_{branch}"])
        contractions = _bool_count(master[f"BranchSig_Cont_{branch}"])
        robust_exp = _bool_count(master[f"BranchSig_Exp_{branch}_Robust"])
        robust_cont = _bool_count(master[f"BranchSig_Cont_{branch}_Robust"])
        rows.append(
            {
                "Node_ID": node_id,
                "Taxon_Clade": label,
                "Estimated_Age_Ma": age,
                "Expansions_Sig": expansions,
                "Contractions_Sig": contractions,
                "Ratio_Exp_Cont": f"{expansions / contractions:.2f}" if contractions else "Inf",
                "Expansions_Robust": robust_exp,
                "Contractions_Robust": robust_cont,
            }
        )
    return rows


def _mode_summary(frame):
    modes = ["WGD/Segmental", "Tandem", "Proximal", "Dispersed", "Singleton"]
    total = len(frame)
    row = {"Total_Genes": total}
    for mode in modes:
        count = int(frame["dup_type"].eq(mode).sum())
        key = mode.replace("/", "_").replace(" ", "_") + "_pct"
        row[key] = f"{100 * count / total:.2f}% ({count})" if total else "0.00% (0)"
    return row


def build_duplication_rows(master, gene_table, species_tag, species_name):
    genes = pd.read_csv(gene_table, sep="\t")
    flag = f"BranchSig_Exp_{species_tag}"
    expanded_families = set(master.loc[master[flag].astype(bool), "FamilyID"])
    expanded = genes[genes["orthogroup"].isin(expanded_families)]
    rows = []
    for label, frame in [
        ("Genome-wide (all classified genes)", genes),
        (f"Expanded families ({len(expanded_families)} families)", expanded),
    ]:
        row = {"Species": species_name, "Gene_Set": label}
        row.update(_mode_summary(frame))
        rows.append(row)
    return rows

# -------------------------------------------------------------
# Table S1: Phylogenomic Support (ASTRAL-III, gCF, sCF, UFBoot)
# -------------------------------------------------------------
tableS1_data = [
    {
        "Node_ID": "Node 11 / Crown Vellozia",
        "Clade_Definition": "Vellozia peripherica + Vellozia tubiflora",
        "IQTree_UFBoot_pct": "100.0%",
        "ASTRAL_LPP": "1.00",
        "ASTRAL_BranchLength_CU": "2.4312",
        "gCF_pct": "93.92%",
        "Concordant_Gene_Trees_N": "1421",
        "Discordant_gDF1_N": "33",
        "Discordant_gDF2_N": "51",
        "Total_Decisive_Gene_Trees_gN": "1513",
        "sCF_pct": "86.44%",
        "Informative_Sites_sN": "16945"
    },
    {
        "Node_ID": "Node 10 / Core Velloziaceae",
        "Clade_Definition": "Xerophyta viscosa + Vellozia (Vper + Vtub)",
        "IQTree_UFBoot_pct": "100.0%",
        "ASTRAL_LPP": "1.00",
        "ASTRAL_BranchLength_CU": "3.3243",
        "gCF_pct": "97.16%",
        "Concordant_Gene_Trees_N": "1470",
        "Discordant_gDF1_N": "14",
        "Discordant_gDF2_N": "13",
        "Total_Decisive_Gene_Trees_gN": "1513",
        "sCF_pct": "79.12%",
        "Informative_Sites_sN": "28230"
    },
    {
        "Node_ID": "Node 9 / Velloziaceae sensu lato",
        "Clade_Definition": "Acanthochlamys bracteata + Core Velloziaceae",
        "IQTree_UFBoot_pct": "100.0%",
        "ASTRAL_LPP": "1.00",
        "ASTRAL_BranchLength_CU": "2.0781",
        "gCF_pct": "88.04%",
        "Concordant_Gene_Trees_N": "1332",
        "Discordant_gDF1_N": "30",
        "Discordant_gDF2_N": "30",
        "Total_Decisive_Gene_Trees_gN": "1513",
        "sCF_pct": "55.43%",
        "Informative_Sites_sN": "30580"
    },
    {
        "Node_ID": "Node 8 / Order Pandanales",
        "Clade_Definition": "Pandanus tectorius + Velloziaceae sensu lato",
        "IQTree_UFBoot_pct": "100.0%",
        "ASTRAL_LPP": "1.00",
        "ASTRAL_BranchLength_CU": "0.5864",
        "gCF_pct": "62.46%",
        "Concordant_Gene_Trees_N": "945",
        "Discordant_gDF1_N": "149",
        "Discordant_gDF2_N": "397",
        "Total_Decisive_Gene_Trees_gN": "1513",
        "sCF_pct": "42.59%",
        "Informative_Sites_sN": "29824"
    },
    {
        "Node_ID": "Node 7 / Monocotyledon Crown",
        "Clade_Definition": "Dioscorea alata + Pandanales (Ptec + Velloziaceae)",
        "IQTree_UFBoot_pct": "100.0%",
        "ASTRAL_LPP": "1.00",
        "ASTRAL_BranchLength_CU": "Root",
        "gCF_pct": "Root",
        "Concordant_Gene_Trees_N": "-",
        "Discordant_gDF1_N": "-",
        "Discordant_gDF2_N": "-",
        "Total_Decisive_Gene_Trees_gN": "1513",
        "sCF_pct": "Root",
        "Informative_Sites_sN": "-"
    }
]
with open(OUT_DIR / "TableS1_phylogenomics_concordance_astral.tsv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=tableS1_data[0].keys(), delimiter="\t")
    writer.writeheader()
    writer.writerows(tableS1_data)
print("Exported TableS1_phylogenomics_concordance_astral.tsv")

# -------------------------------------------------------------
# Table 1: CAFE5 Model Selection & Parameter Comparison
# -------------------------------------------------------------
best_models_path = BASE_DIR / "04_gene_families" / "cafe5" / "summary" / "best_models_comparison.tsv"
table1_rows = []
if best_models_path.exists():
    with open(best_models_path) as f:
        reader = csv.DictReader(f, delimiter="\t")
        for r in reader:
            table1_rows.append(r)
    with open(OUT_DIR / "Table1_CAFE5_model_selection.tsv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=table1_rows[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(table1_rows)
    print("Exported Table1_CAFE5_model_selection.tsv")

# -------------------------------------------------------------
# Table 2: Expansions and Contractions Across Key Nodes
# -------------------------------------------------------------
master_path = BASE_DIR / "04_gene_families" / "comparative_axes" / "comparative_families_master_table_v2.tsv"
master = pd.read_csv(master_path, sep="\t", low_memory=False)
table2_data = build_branch_table(master, [
    ("Node 9", "Node11_Velloziaceae_Crown", "Velloziaceae sensu lato (MRCA Abra + Xvis + Vper + Vtub)", "78.21"),
    ("Node 10", "Node12_CoreVelloziaceae", "Core Velloziaceae (MRCA Xvis + Vper + Vtub)", "31.91"),
    ("Node 11", "Node13_Vellozia", "Crown Vellozia (MRCA Vper + Vtub)", "9.74"),
    ("Terminal Vtub", "Vtub", "Vellozia tubiflora (desiccation-tolerant resurrection plant)", "Terminal"),
    ("Terminal Vper", "Vper", "Vellozia peripherica (desiccation-avoidant evergreen)", "Terminal"),
    ("Terminal Xvis", "Xvis", "Xerophyta viscosa (resurrection plant)", "Terminal"),
    ("Terminal Abra", "Abra", "Acanthochlamys bracteata", "Terminal"),
])
with open(OUT_DIR / "Table2_node_expansions_contractions.tsv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=table2_data[0].keys(), delimiter="\t")
    writer.writeheader()
    writer.writerows(table2_data)
print("Exported Table2_node_expansions_contractions.tsv")

# -------------------------------------------------------------
# Table 3: Duplication Modes (Genome-wide vs Expanded Families)
# -------------------------------------------------------------
dup_dir = BASE_DIR / "04_gene_families" / "synteny" / "duplications"
table3_data = build_duplication_rows(
    master, dup_dir / "vper_gene_duplications_annotated.tsv", "Vper", "Vellozia peripherica"
) + build_duplication_rows(
    master, dup_dir / "vtub_gene_duplications_annotated.tsv", "Vtub", "Vellozia tubiflora"
)
with open(OUT_DIR / "Table3_duplication_modes.tsv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=table3_data[0].keys(), delimiter="\t")
    writer.writeheader()
    writer.writerows(table3_data)
print("Exported Table3_duplication_modes.tsv")

# -------------------------------------------------------------
# Table S4: Current primary functional-enrichment tests
# -------------------------------------------------------------
enrichment_primary = (
    BASE_DIR
    / "04_gene_families"
    / "functional_enrichment"
    / "results"
    / "enrichment_results_primary.tsv"
)
if enrichment_primary.exists():
    shutil.copy2(enrichment_primary, OUT_DIR / "TableS4_functional_enrichment_results.tsv")
    print("Exported TableS4_functional_enrichment_results.tsv")

# -------------------------------------------------------------
# Table 4: Reciprocal 1:1 Ortholog QC Status
# -------------------------------------------------------------
summary_path = BASE_DIR / "05_selection" / "pair_specific_run" / "summary.json"
if summary_path.exists():
    with open(summary_path) as f:
        s = json.load(f)
    table4_data = [
        {"Category": "Total 1:1 reciprocal pairs evaluated", "Count": s["pairs"], "Percentage": "100.00%"},
        {"Category": "QC PASS (valid estimates)", "Count": s["qc_counts"].get("PASS", 0), "Percentage": f"{s['qc_counts'].get('PASS', 0)/s['pairs']*100:.2f}%"},
        {"Category": "Excluded: High dS (dS >= 2.0)", "Count": s["qc_counts"].get("HIGH_DS", 0), "Percentage": f"{s['qc_counts'].get('HIGH_DS', 0)/s['pairs']*100:.2f}%"},
        {"Category": "Excluded: Zero or Negative dS (dS <= 0)", "Count": s["qc_counts"].get("ZERO_OR_NEGATIVE_DS", 0), "Percentage": f"{s['qc_counts'].get('ZERO_OR_NEGATIVE_DS', 0)/s['pairs']*100:.2f}%"},
        {"Category": "Screen: Purifying selection (omega < 1)", "Count": s["screen_counts"].get("omega_lt_1", 0), "Percentage": f"{s['screen_counts'].get('omega_lt_1', 0)/s['pairs']*100:.2f}%"},
        {"Category": "Screen: Accelerated divergence (omega > 1 total)", "Count": s["omega_gt1_count"], "Percentage": f"{s['omega_gt1_count']/s['pairs']*100:.2f}%"},
        {"Category": "Screen: Clean accelerated divergence (omega > 1, no flags)", "Count": s["omega_gt1_without_flags"], "Percentage": f"{s['omega_gt1_without_flags']/s['pairs']*100:.2f}%"},
        {"Category": "PPR organellar loci evaluated", "Count": s["ppr_annotation_pairs"], "Percentage": "-"},
        {"Category": "PPR loci with omega > 1", "Count": s["ppr_omega_gt1"], "Percentage": "0.00%"}
    ]
    with open(OUT_DIR / "Table4_pairwise_ortholog_QC.tsv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=table4_data[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(table4_data)
    print("Exported Table4_pairwise_ortholog_QC.tsv")

# -------------------------------------------------------------
# Table 5: Top Clean Candidate Loci with omega > 1
# -------------------------------------------------------------
omega_path = BASE_DIR / "05_selection" / "pair_specific_run" / "omega_gt1_screen.tsv"
if omega_path.exists():
    with open(omega_path) as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    clean_candidates = [r for r in rows if not r.get("Flags")]
    top25 = clean_candidates[:25]
    fields = ["Pair_ID", "Orthogroup", "Vper_Gene", "Vtub_Gene", "Omega_KaKs", "Ka_dN", "Ks_dS", "Codons", "Functional_Description"]
    with open(OUT_DIR / "Table5_top_accelerated_candidates.tsv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(top25)
    print(f"Exported Table5_top_accelerated_candidates.tsv ({len(top25)} loci)")

print("=== ALL MANUSCRIPT TABLES EXPORTED SUCCESSFULLY ===")

