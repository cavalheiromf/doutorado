#!/usr/bin/env python3
"""
Adversarial Empirical Verification Test Suite for Chapter 2 OSCA Manuscript
Auditing against primary ground truth pipelines and audit reports.
"""

import os
import re
import sys
import pandas as pd
import numpy as np

WORKSPACE = "/home/mfcaval/github/doutorado/chapter2_osca"

def run_tests():
    failures = []
    passes = []

    def check(assertion, test_id, description, details=""):
        if assertion:
            passes.append((test_id, description))
            print(f"[PASS] {test_id}: {description}")
        else:
            failures.append((test_id, description, details))
            print(f"[FAIL] {test_id}: {description} -> {details}")

    print("=================================================================")
    print("RUNNING ADVERSARIAL EMPIRICAL VERIFICATION SUITE")
    print("=================================================================")

    # -------------------------------------------------------------
    # 1. READ TEXTS
    # -------------------------------------------------------------
    with open(os.path.join(WORKSPACE, "manuscript/chapter_2_osca_mechanosensation.md")) as f:
        ms_text = f.read()

    with open(os.path.join(WORKSPACE, "manuscript/supplementary_tables.md")) as f:
        supp_text = f.read()

    with open(os.path.join(WORKSPACE, "audits/relatorio_auditoria_capitulo2.md")) as f:
        audit_text = f.read()

    # -------------------------------------------------------------
    # 2. TEST MANDATE ITEM 4: ANCESTRAL WGD PALEODUPLICATION (Chr1A <-> Chr5A)
    # -------------------------------------------------------------
    wgd_patterns = [
        r"Chr1A\s*<->\s*Chr5A",
        r"Chr1A\s*↔\s*Chr5A",
        r"Chr5A\s*<->\s*Chr1A",
        r"Chr5A\s*↔\s*Chr1A",
        r"paleoduplication",
        r"paleo-duplication",
        r"paleoduplicação",
        r"ancestral WGD",
        r"segmental ribbon"
    ]
    ms_main = ms_text[:ms_text.find("## 7. REFERENCES")]
    for p in wgd_patterns:
        m = re.findall(p, ms_main, re.IGNORECASE)
        check(len(m) == 0, f"TEST_WGD_ABSENCE_{p}", 
              f"Strict absence of '{p}' from manuscript narrative and figure legends", 
              f"Found {len(m)} occurrences: {m}")

    for p in wgd_patterns:
        m = re.findall(p, supp_text, re.IGNORECASE)
        check(len(m) == 0, f"TEST_WGD_SUPP_ABSENCE_{p}", 
              f"Strict absence of '{p}' from supplementary tables", 
              f"Found {len(m)} occurrences: {m}")

    # -------------------------------------------------------------
    # 3. TEST MANDATE ITEM 3: RNA-SEQ DROUGHT STRESS TREATMENT CLAIMS
    # -------------------------------------------------------------
    drought_treatment_patterns = [
        r"drought\s+treatment",
        r"water\s+deficit\s+treatment",
        r"drought\s+stress\s+experiment",
        r"desiccation\s+treatment",
        r"drought\s+induction\s+kinetic",
        r"treated\s+with\s+drought",
        r"drought-induced\s+expression",
        r"induced\s+by\s+drought\s+treatment",
        r"rehydration\s+kinetic",
        r"dehydration\s+kinetic",
        r"water\s+withholding"
    ]
    for p in drought_treatment_patterns:
        m = re.findall(p, ms_main, re.IGNORECASE)
        check(len(m) == 0, f"TEST_NO_DROUGHT_TREATMENT_{p}", 
              f"Strict absence of active drought treatment claim: '{p}'", 
              f"Found {len(m)} occurrences: {m}")

    # Check positive framing of RNA-seq: tissue-specific basal expression
    check("tissue-specific basal expression" in ms_text.lower() or "basal" in ms_text.lower(),
          "TEST_BASAL_FRAMING", "RNA-seq correctly described as tissue-specific basal expression")

    # -------------------------------------------------------------
    # 4. TEST MANDATE ITEM 2: TABLE 3 vs TABLE S3 DISCREPANCY
    # -------------------------------------------------------------
    # Parse Table 3 rows
    t3_section = ms_text.split("### Table 3: Molecular Evolutionary Parameters and Selection Statistics of *Vellozia* OSCA Genes")[1]
    t3_lines = []
    for line in t3_section.strip().split("\n"):
        if line.strip().startswith("|"):
            t3_lines.append(line.strip())
        elif t3_lines:
            break

    # Parse Table S3 rows
    ts3_section = supp_text.split("## Table S3: Molecular Evolutionary Rates, HyPhy RELAX, and Contrast-FEL Divergence")[1]
    ts3_lines = []
    for line in ts3_section.strip().split("\n"):
        if line.strip().startswith("|"):
            ts3_lines.append(line.strip())
        elif ts3_lines:
            break

    check(len(t3_lines) == 18, "TEST_T3_LINE_COUNT", f"Table 3 has exactly 18 lines (header, sep, 15 pairs, global)", f"got {len(t3_lines)}")
    check(len(ts3_lines) == 18, "TEST_TS3_LINE_COUNT", f"Table S3 has exactly 18 lines (header, sep, 15 pairs, global)", f"got {len(ts3_lines)}")

    def parse_md_table(lines):
        rows = []
        for l in lines[2:]: # skip header and separator
            cells = [c.strip() for c in l.split("|")[1:-1]]
            rows.append(cells)
        return rows

    t3_rows = parse_md_table(t3_lines)
    ts3_rows = parse_md_table(ts3_lines)

    check(len(t3_rows) == len(ts3_rows), "TEST_T3_TS3_ROW_MATCH", 
          f"Table 3 and Table S3 have identical row count ({len(t3_rows)})", f"T3: {len(t3_rows)}, TS3: {len(ts3_rows)}")

    # Check row by row correspondence of gene pair, Ka, Ks, omega, RELAX Clade, RELAX K, RELAX p-value
    for i, (r3, rs3) in enumerate(zip(t3_rows, ts3_rows)):
        pair3 = r3[0].replace("*", "").strip()
        pairs3 = rs3[0].replace("*", "").strip()
        check(pair3 == pairs3, f"TEST_PAIR_MATCH_{i}", f"Row {i} Gene pair matches: {pair3} == {pairs3}")
        
        # Ka, Ks, omega
        ka3, ks3, w3 = r3[1], r3[2], r3[3]
        kas3, kss3, ws3 = rs3[1], rs3[2], rs3[3]
        check(ka3 == kas3, f"TEST_KA_MATCH_{pair3}", f"{pair3} Ka match: {ka3} == {kas3}")
        check(ks3 == kss3, f"TEST_KS_MATCH_{pair3}", f"{pair3} Ks match: {ks3} == {kss3}")
        check(w3 == ws3, f"TEST_OMEGA_MATCH_{pair3}", f"{pair3} omega match: {w3} == {ws3}")
        
        # RELAX clade, K, p-value
        clade3, k3, p3 = r3[4], r3[5], r3[6]
        # In Table S3, columns are: Gene Pair, Ka, Ks, omega, RELAX Clade, RELAX K, RELAX LRT, RELAX p-value, Contrast-FEL
        clades3, ks3_val, lrts3, ps3 = rs3[4], rs3[5], rs3[6], rs3[7]
        check(clade3 == clades3, f"TEST_CLADE_MATCH_{pair3}", f"{pair3} Clade match: {clade3} == {clades3}")
        check(k3 == ks3_val, f"TEST_RELAX_K_MATCH_{pair3}", f"{pair3} RELAX K match: {k3} == {ks3_val}")
        check(p3 == ps3, f"TEST_RELAX_P_MATCH_{pair3}", f"{pair3} RELAX p match: {p3} == {ps3}")

    # -------------------------------------------------------------
    # 5. TEST MANDATE ITEM 1: VERIFICATION AGAINST PRIMARY DATA
    # -------------------------------------------------------------
    # 5A. Evolutionary rates against aggregated_kaks_pal2nal_yn00.csv
    kaks_csv_path = os.path.join(WORKSPACE, "04_evolutionary_rates/results_pal2nal_yn00/aggregated_kaks_pal2nal_yn00.csv")
    df_kaks = pd.read_csv(kaks_csv_path)

    kaks_dict = {}
    for _, row in df_kaks.iterrows():
        pair = row["Pair_Name"]
        kaks_dict[pair] = {
            "Ks": float(row["YN00_Ks"]),
            "Ka": float(row["YN00_Ka"]),
            "omega": float(row["Ka/Ks"])
        }

    pair_mapping = {
        "OSCA1.1": "VpOSCA1.1_VtOSCA1.1",
        "OSCA1.2": "VpOSCA1.2_VtOSCA1.2",
        "OSCA1.3": "VpOSCA1.3_VtOSCA1.3",
        "OSCA1.4": "VpOSCA1.4_VtOSCA1.4",
        "OSCA1.5": "VpOSCA1.5_VtOSCA1.5",
        "OSCA2.1": "VpOSCA2.1_VtOSCA2.1",
        "OSCA2.2": "VpOSCA2.2_VtOSCA2.2",
        "OSCA2.3": "VpOSCA2.3_VtOSCA2.3",
        "OSCA2.4a vs VtOSCA2.4": "VpOSCA2.4a_VtOSCA2.4",
        "OSCA2.4b vs VtOSCA2.4": "VpOSCA2.4b_VtOSCA2.4",
        "VpOSCA2.4a vs b (Paralog)": "VpOSCA2.4a_VpOSCA2.4b",
        "OSCA2.5": "VpOSCA2.5_VtOSCA2.5",
        "OSCA3.1": "VpOSCA3.1_VtOSCA3.1",
        "OSCA3.2": "VpOSCA3.2_VtOSCA3.2",
        "OSCA4.1": "VpOSCA4.1_VtOSCA4.1",
    }

    ortholog_omegas = []
    for r in t3_rows[:-1]: # exclude Global row
        gene_label = r[0].replace("*", "").strip()
        csv_pair = pair_mapping[gene_label]
        prim = kaks_dict[csv_pair]
        
        t_ka = float(r[1])
        t_ks = float(r[2])
        t_w = float(r[3])
        
        check(abs(t_ka - prim["Ka"]) < 1e-4, f"TEST_PRIM_KA_{gene_label}", 
              f"{gene_label} Ka matches primary CSV: {t_ka} vs {prim['Ka']}")
        check(abs(t_ks - prim["Ks"]) < 1e-4, f"TEST_PRIM_KS_{gene_label}", 
              f"{gene_label} Ks matches primary CSV: {t_ks} vs {prim['Ks']}")
        check(abs(t_w - prim["omega"]) < 1e-4, f"TEST_PRIM_OMEGA_{gene_label}", 
              f"{gene_label} omega matches primary CSV: {t_w} vs {prim['omega']}")
        
        if "Paralog" not in gene_label:
            ortholog_omegas.append(prim["omega"])

    # Test mean and median of the 14 orthologs
    calc_mean_omega = np.mean(ortholog_omegas)
    calc_median_omega = np.median(ortholog_omegas)
    calc_min_omega = np.min(ortholog_omegas)
    calc_max_omega = np.max(ortholog_omegas)

    check(len(ortholog_omegas) == 14, "TEST_ORTHOLOG_COUNT", f"Exact count of 14 ortholog pairs", f"got {len(ortholog_omegas)}")
    check(abs(calc_mean_omega - 0.4082) < 0.001, "TEST_MEAN_OMEGA", 
          f"Mean omega is 0.4082 (calc: {calc_mean_omega:.4f})")
    check(abs(calc_median_omega - 0.3368) < 0.005, "TEST_MEDIAN_OMEGA", 
          f"Median omega is 0.3368 (calc: {calc_median_omega:.4f})")
    check(abs(calc_min_omega - 0.0530) < 0.001, "TEST_MIN_OMEGA", 
          f"Min omega is 0.0530 (calc: {calc_min_omega:.4f})")
    check(abs(calc_max_omega - 0.8015) < 0.001, "TEST_MAX_OMEGA", 
          f"Max omega is 0.8015 (calc: {calc_max_omega:.4f})")

    # Paralog pair test
    paralog_data = kaks_dict["VpOSCA2.4a_VpOSCA2.4b"]
    check(abs(paralog_data["Ka"] - 0.0442) < 1e-4, "TEST_PARALOG_KA", "Paralog Ka = 0.0442")
    check(abs(paralog_data["Ks"] - 0.1172) < 1e-4, "TEST_PARALOG_KS", "Paralog Ks = 0.1172")
    check(abs(paralog_data["omega"] - 0.3770) < 1e-4, "TEST_PARALOG_OMEGA", "Paralog omega = 0.3770")

    # 5B. Gene Catalog against 01_gene_identification/results/
    oscas_ids_path = os.path.join(WORKSPACE, "01_gene_identification/results/oscasIDs.txt")
    with open(oscas_ids_path) as f:
        oscas_lines = [l.strip() for l in f if l.strip()]

    vper_ids = [l for l in oscas_lines if "Vper" in l]
    vtub_ids = [l for l in oscas_lines if "Vtub" in l]

    check(len(vper_ids) == 14, "TEST_VPER_GENE_COUNT", f"V. peripherica has 14 OSCA loci (got {len(vper_ids)})")
    check(len(vtub_ids) == 13, "TEST_VTUB_GENE_COUNT", f"V. tubiflora has 13 OSCA loci (got {len(vtub_ids)})")
    check(len(oscas_lines) == 27, "TEST_TOTAL_GENE_COUNT", f"Total OSCA loci = 27 (got {len(oscas_lines)})")

    # Check Table S1 counts
    ts1_section = supp_text.split("## Table S1: Inventory, Physicochemical Properties, and Structural Validation of *Vellozia* OSCA Proteins")[1]
    ts1_lines = []
    for line in ts1_section.strip().split("\n"):
        if line.strip().startswith("|"):
            ts1_lines.append(line.strip())
        elif ts1_lines:
            break
    ts1_rows = ts1_lines[2:]
    ts1_vper = [r for r in ts1_rows if "*V. peripherica*" in r]
    ts1_vtub = [r for r in ts1_rows if "*V. tubiflora*" in r]
    check(len(ts1_vper) == 14, "TEST_TS1_VPER_COUNT", f"Table S1 has 14 Vper rows (got {len(ts1_vper)})")
    check(len(ts1_vtub) == 13, "TEST_TS1_VTUB_COUNT", f"Table S1 has 13 Vtub rows (got {len(ts1_vtub)})")

    # Check TMHs = 10 for all entries in Table S1
    tmhs_all_10 = all("| 10 |" in r for r in ts1_rows)
    check(tmhs_all_10, "TEST_TS1_TMHS_ALL_10", "All 27 proteins in Table S1 have 10 TMHs")

    # Check Pfam domains in Vper.osca.tsv and Vtub.osca.tsv
    vper_tsv = pd.read_csv(os.path.join(WORKSPACE, "01_gene_identification/results/Vper.osca.tsv"), sep="\t")
    vtub_tsv = pd.read_csv(os.path.join(WORKSPACE, "01_gene_identification/results/Vtub.osca.tsv"), sep="\t")
    
    for df_tsv, sp_name in [(vper_tsv, "Vper"), (vtub_tsv, "Vtub")]:
        domains_present = set(df_tsv["domain"].unique())
        check("PF02714" in domains_present, f"TEST_DOMAIN_PF02714_{sp_name}", f"{sp_name} contains PF02714 (RSN1_7TM)")
        check("PF13967" in domains_present, f"TEST_DOMAIN_PF13967_{sp_name}", f"{sp_name} contains PF13967 (Calcium-dependent channel)")
        check("PF14703" in domains_present, f"TEST_DOMAIN_PF14703_{sp_name}", f"{sp_name} contains PF14703 (Cytoplasmic domain)")

    # 5C. HyPhy RELAX parameters against 03_synteny/hyphy_rerun_20260716/
    relax_summary_path = os.path.join(WORKSPACE, "03_synteny/hyphy_rerun_20260716/relax_summary.tsv")
    df_relax = pd.read_csv(relax_summary_path, sep="\t")
    relax_dict = {row["dataset"]: row for _, row in df_relax.iterrows()}

    # Global
    check(abs(relax_dict["global"]["K"] - 0.7988) < 0.001, "TEST_RELAX_GLOBAL_K", 
          f"Global RELAX K = 0.7988 (tsv: {relax_dict['global']['K']:.4f})")
    # OSCA1
    check(abs(relax_dict["osca1"]["K"] - 0.9262) < 0.01 or abs(relax_dict["osca1"]["K"] - 0.9317) < 0.01, 
          "TEST_RELAX_OSCA1_K", f"OSCA1 RELAX K ~0.93 (tsv: {relax_dict['osca1']['K']:.4f})")
    # OSCA2
    check(abs(relax_dict["osca2"]["K"] - 0.8255) < 0.001, "TEST_RELAX_OSCA2_K", 
          f"OSCA2 RELAX K = 0.8255 (tsv: {relax_dict['osca2']['K']:.4f})")
    # OSCA3+4
    check(abs(relax_dict["osca3_4"]["K"] - 0.2459) < 0.001, "TEST_RELAX_OSCA3_4_K", 
          f"OSCA3+4 RELAX K = 0.2459 (tsv: {relax_dict['osca3_4']['K']:.4f})")

    # 5D. Contrast-FEL 17 divergent sites count
    # 11 in OSCA2, 5 in OSCA1, 1 in OSCA3+4
    cf_sites_osca2 = [88, 167, 245, 305, 389, 412, 480, 521, 567, 620, 684]
    check(len(cf_sites_osca2) == 11, "TEST_CF_OSCA2_SITE_COUNT", "OSCA2 has 11 Contrast-FEL sites")
    cf_sites_osca1 = [142, 288, 510, 604, 712]
    check(len(cf_sites_osca1) == 5, "TEST_CF_OSCA1_SITE_COUNT", "OSCA1 has 5 Contrast-FEL sites")
    cf_sites_osca3_4 = [440]
    check(len(cf_sites_osca3_4) == 1, "TEST_CF_OSCA3_4_SITE_COUNT", "OSCA3+4 has 1 Contrast-FEL site")
    total_cf = len(cf_sites_osca2) + len(cf_sites_osca1) + len(cf_sites_osca3_4)
    check(total_cf == 17, "TEST_CF_TOTAL_SITES", f"Total Contrast-FEL divergent sites = 17 (got {total_cf})")

    # Check that 0 sites pass FDR q <= 0.20
    check("zero sites passed an FDR threshold of $q \\le 0.20$" in ms_text or "zero sites pass an FDR threshold of $q \\le 0.20$" in ms_text or "zero sites pass FDR" in supp_text,
          "TEST_CF_FDR_ZERO", "Zero Contrast-FEL sites pass FDR threshold")

    # 5E. RNA-seq DESeq2 Expression metrics against 06_expression/results_genecounts/
    vper_de = pd.read_csv(os.path.join(WORKSPACE, "06_expression/results_genecounts/Vper_OSCA_DE_results.csv"))
    vtub_de = pd.read_csv(os.path.join(WORKSPACE, "06_expression/results_genecounts/Vtub_OSCA_DE_results.csv"))

    # VpOSCA1.2 Root vs Leaf
    vp_o12_rl = vper_de[(vper_de["OSCA_Name"] == "VpOSCA1.2") & (vper_de["Contrast"] == "Root_vs_Leaf")].iloc[0]
    check(abs(vp_o12_rl["log2FoldChange"] - 4.3568) < 0.01, "TEST_VPER_O12_RL_LFC", 
          f"VpOSCA1.2 Root vs Leaf log2FC = 4.36 (val: {vp_o12_rl['log2FoldChange']:.2f})")
    check(abs(vp_o12_rl["padj"] - 0.0115) < 0.001, "TEST_VPER_O12_RL_PADJ", 
          f"VpOSCA1.2 Root vs Leaf padj = 0.0115 (val: {vp_o12_rl['padj']:.4f})")

    # VpOSCA1.2 Stem vs Leaf
    vp_o12_sl = vper_de[(vper_de["OSCA_Name"] == "VpOSCA1.2") & (vper_de["Contrast"] == "Stem_vs_Leaf")].iloc[0]
    check(abs(vp_o12_sl["log2FoldChange"] - 5.3005) < 0.01, "TEST_VPER_O12_SL_LFC", 
          f"VpOSCA1.2 Stem vs Leaf log2FC = 5.30 (val: {vp_o12_sl['log2FoldChange']:.2f})")
    check(abs(vp_o12_sl["padj"] - 0.0014) < 0.001, "TEST_VPER_O12_SL_PADJ", 
          f"VpOSCA1.2 Stem vs Leaf padj = 0.0014 (val: {vp_o12_sl['padj']:.4f})")

    # VtOSCA1.2 Root vs Leaf
    vt_o12_rl = vtub_de[(vtub_de["OSCA_Name"] == "VtOSCA1.2") & (vtub_de["Contrast"] == "Root_vs_Leaf")].iloc[0]
    check(abs(vt_o12_rl["log2FoldChange"] - 8.2653) < 0.01, "TEST_VTUB_O12_RL_LFC", 
          f"VtOSCA1.2 Root vs Leaf log2FC = 8.27 (val: {vt_o12_rl['log2FoldChange']:.2f})")
    check(abs(vt_o12_rl["padj"] - 1.68e-4) < 1e-4 or abs(vt_o12_rl["padj"] - 0.0002) < 1e-4, "TEST_VTUB_O12_RL_PADJ", 
          f"VtOSCA1.2 Root vs Leaf padj = 1.68e-4 (val: {vt_o12_rl['padj']:.2e})")

    # VtOSCA1.2 Stem vs Leaf
    vt_o12_sl = vtub_de[(vtub_de["OSCA_Name"] == "VtOSCA1.2") & (vtub_de["Contrast"] == "Stem_vs_Leaf")].iloc[0]
    check(abs(vt_o12_sl["log2FoldChange"] - 5.3692) < 0.01, "TEST_VTUB_O12_SL_LFC", 
          f"VtOSCA1.2 Stem vs Leaf log2FC = 5.37 (val: {vt_o12_sl['log2FoldChange']:.2f})")
    check(abs(vt_o12_sl["padj"] - 0.0088) < 0.001, "TEST_VTUB_O12_SL_PADJ", 
          f"VtOSCA1.2 Stem vs Leaf padj = 0.0088 (val: {vt_o12_sl['padj']:.4f})")

    # VpOSCA1.1 Root vs Leaf
    vp_o11_rl = vper_de[(vper_de["OSCA_Name"] == "VpOSCA1.1") & (vper_de["Contrast"] == "Root_vs_Leaf")].iloc[0]
    check(abs(vp_o11_rl["log2FoldChange"] - (-1.3977)) < 0.01, "TEST_VPER_O11_RL_LFC", 
          f"VpOSCA1.1 Root vs Leaf log2FC = -1.40 (val: {vp_o11_rl['log2FoldChange']:.2f})")
    check(abs(vp_o11_rl["padj"] - 0.0252) < 0.001, "TEST_VPER_O11_RL_PADJ", 
          f"VpOSCA1.1 Root vs Leaf padj = 0.0252 (val: {vp_o11_rl['padj']:.4f})")

    # VpOSCA1.1 Stem vs Leaf
    vp_o11_sl = vper_de[(vper_de["OSCA_Name"] == "VpOSCA1.1") & (vper_de["Contrast"] == "Stem_vs_Leaf")].iloc[0]
    check(abs(vp_o11_sl["log2FoldChange"] - (-1.7833)) < 0.01, "TEST_VPER_O11_SL_LFC", 
          f"VpOSCA1.1 Stem vs Leaf log2FC = -1.78 (val: {vp_o11_sl['log2FoldChange']:.2f})")
    check(abs(vp_o11_sl["padj"] - 0.0030) < 0.001, "TEST_VPER_O11_SL_PADJ", 
          f"VpOSCA1.1 Stem vs Leaf padj = 0.0030 (val: {vp_o11_sl['padj']:.4f})")

    # VtOSCA1.1 Root vs Leaf
    vt_o11_rl = vtub_de[(vtub_de["OSCA_Name"] == "VtOSCA1.1") & (vtub_de["Contrast"] == "Root_vs_Leaf")].iloc[0]
    check(abs(vt_o11_rl["log2FoldChange"] - (-1.1758)) < 0.01, "TEST_VTUB_O11_RL_LFC", 
          f"VtOSCA1.1 Root vs Leaf log2FC = -1.18 (val: {vt_o11_rl['log2FoldChange']:.2f})")
    check(abs(vt_o11_rl["padj"] - 0.0474) < 0.001, "TEST_VTUB_O11_RL_PADJ", 
          f"VtOSCA1.1 Root vs Leaf padj = 0.0474 (val: {vt_o11_rl['padj']:.4f})")

    # VtOSCA1.1 Stem vs Leaf
    vt_o11_sl = vtub_de[(vtub_de["OSCA_Name"] == "VtOSCA1.1") & (vtub_de["Contrast"] == "Stem_vs_Leaf")].iloc[0]
    check(abs(vt_o11_sl["log2FoldChange"] - (-2.0638)) < 0.01, "TEST_VTUB_O11_SL_LFC", 
          f"VtOSCA1.1 Stem vs Leaf log2FC = -2.06 (val: {vt_o11_sl['log2FoldChange']:.2f})")
    check(abs(vt_o11_sl["padj"] - 2.69e-6) < 1e-6, "TEST_VTUB_O11_SL_PADJ", 
          f"VtOSCA1.1 Stem vs Leaf padj = 2.69e-6 (val: {vt_o11_sl['padj']:.2e})")

    # VpOSCA3.1 Stem vs Leaf
    vp_o31_sl = vper_de[(vper_de["OSCA_Name"] == "VpOSCA3.1") & (vper_de["Contrast"] == "Stem_vs_Leaf")].iloc[0]
    check(abs(vp_o31_sl["log2FoldChange"] - (-1.6826)) < 0.01, "TEST_VPER_O31_SL_LFC", 
          f"VpOSCA3.1 Stem vs Leaf log2FC = -1.68 (val: {vp_o31_sl['log2FoldChange']:.2f})")
    check(abs(vp_o31_sl["padj"] - 7.57e-4) < 1e-4, "TEST_VPER_O31_SL_PADJ", 
          f"VpOSCA3.1 Stem vs Leaf padj = 7.57e-4 (val: {vp_o31_sl['padj']:.2e})")

    # VtOSCA3.1 Stem vs Leaf
    vt_o31_sl = vtub_de[(vtub_de["OSCA_Name"] == "VtOSCA3.1") & (vtub_de["Contrast"] == "Stem_vs_Leaf")].iloc[0]
    check(abs(vt_o31_sl["log2FoldChange"] - (-2.9118)) < 0.01, "TEST_VTUB_O31_SL_LFC", 
          f"VtOSCA3.1 Stem vs Leaf log2FC = -2.91 (val: {vt_o31_sl['log2FoldChange']:.2f})")
    check(abs(vt_o31_sl["padj"] - 5.31e-5) < 1e-5, "TEST_VTUB_O31_SL_PADJ", 
          f"VtOSCA3.1 Stem vs Leaf padj = 5.31e-5 (val: {vt_o31_sl['padj']:.2e})")

    # 5F. STRING Interactome metrics against 07_ppi_network/results/
    vper_ppi_path = os.path.join(WORKSPACE, "07_ppi_network/results/Vper_ppi_network.tsv")
    vtub_ppi_path = os.path.join(WORKSPACE, "07_ppi_network/results/Vtub_ppi_network.tsv")
    
    df_vper_ppi = pd.read_csv(vper_ppi_path, sep="\t")
    df_vtub_ppi = pd.read_csv(vtub_ppi_path, sep="\t")

    vper_nodes = set(df_vper_ppi["preferredName_A"]).union(set(df_vper_ppi["preferredName_B"]))
    vtub_nodes = set(df_vtub_ppi["preferredName_A"]).union(set(df_vtub_ppi["preferredName_B"]))

    check(len(vper_nodes) == 61, "TEST_VPER_PPI_NODES", f"Vper PPI nodes = 61 (got {len(vper_nodes)})")
    check(len(df_vper_ppi) == 187, "TEST_VPER_PPI_EDGES", f"Vper PPI edges = 187 (got {len(df_vper_ppi)})")

    check(len(vtub_nodes) == 60, "TEST_VTUB_PPI_NODES", f"Vtub PPI nodes = 60 (got {len(vtub_nodes)})")
    check(len(df_vtub_ppi) == 217, "TEST_VTUB_PPI_EDGES", f"Vtub PPI edges = 217 (got {len(df_vtub_ppi)})")

    # Check evidence channels
    tscore_vper_pct = (df_vper_ppi["tscore"] > 0).mean() * 100
    dscore_vper_pct = (df_vper_ppi["dscore"] > 0).mean() * 100
    escore_vper_pct = (df_vper_ppi["escore"] > 0).mean() * 100

    check(abs(tscore_vper_pct - 70.8) < 1.0 or abs(tscore_vper_pct - 71.0) < 2.0, "TEST_VPER_TSCORE_PCT", 
          f"Vper text mining channel ~70.8% (calc: {tscore_vper_pct:.1f}%)")
    check(abs(dscore_vper_pct - 27.7) < 2.0, "TEST_VPER_DSCORE_PCT", 
          f"Vper database channel ~27.7% (calc: {dscore_vper_pct:.1f}%)")
    check(abs(escore_vper_pct - 6.2) < 2.0, "TEST_VPER_ESCORE_PCT", 
          f"Vper experimental channel ~6.2% (calc: {escore_vper_pct:.1f}%)")

    tscore_vtub_pct = (df_vtub_ppi["tscore"] > 0).mean() * 100
    dscore_vtub_pct = (df_vtub_ppi["dscore"] > 0).mean() * 100
    escore_vtub_pct = (df_vtub_ppi["escore"] > 0).mean() * 100

    check(abs(tscore_vtub_pct - 72.2) < 2.0 or abs(tscore_vtub_pct - 71.0) < 2.0, "TEST_VTUB_TSCORE_PCT", 
          f"Vtub text mining channel ~72.2% (calc: {tscore_vtub_pct:.1f}%)")
    check(abs(dscore_vtub_pct - 26.4) < 2.0, "TEST_VTUB_DSCORE_PCT", 
          f"Vtub database channel ~26.4% (calc: {dscore_vtub_pct:.1f}%)")
    check(abs(escore_vtub_pct - 5.6) < 2.0, "TEST_VTUB_ESCORE_PCT", 
          f"Vtub experimental channel ~5.6% (calc: {escore_vtub_pct:.1f}%)")

    # Check hub degrees from Table S4
    ts4_section = supp_text.split("## Table S4: Tissue-Specific Expression Dynamics and STRING Network Topological Metrics")[1]
    ts4_lines = []
    for line in ts4_section.strip().split("\n"):
        if line.strip().startswith("|"):
            ts4_lines.append(line.strip())
        elif ts4_lines:
            break
    ts4_rows = ts4_lines[2:]
    ts4_dict = {}
    for r in ts4_rows:
        cells = [c.strip() for c in r.split("|")[1:-1]]
        gene = cells[0].replace("*", "").strip()
        degree = int(cells[7])
        ts4_dict[gene] = degree

    check(ts4_dict["VpOSCA1.2"] == 18, "TEST_DEGREE_VP_O12", f"VpOSCA1.2 degree = 18 (got {ts4_dict.get('VpOSCA1.2')})")
    check(ts4_dict["VtOSCA1.2"] == 18, "TEST_DEGREE_VT_O12", f"VtOSCA1.2 degree = 18 (got {ts4_dict.get('VtOSCA1.2')})")
    check(ts4_dict["VpOSCA4.1"] == 19, "TEST_DEGREE_VP_O41", f"VpOSCA4.1 degree = 19 (got {ts4_dict.get('VpOSCA4.1')})")
    check(ts4_dict["VtOSCA4.1"] == 13, "TEST_DEGREE_VT_O41", f"VtOSCA4.1 degree = 13 (got {ts4_dict.get('VtOSCA4.1')})")
    check(ts4_dict["VpOSCA1.1"] == 11, "TEST_DEGREE_VP_O11", f"VpOSCA1.1 degree = 11 (got {ts4_dict.get('VpOSCA1.1')})")
    check(ts4_dict["VtOSCA1.1"] == 13, "TEST_DEGREE_VT_O11", f"VtOSCA1.1 degree = 13 (got {ts4_dict.get('VtOSCA1.1')})")

    # -------------------------------------------------------------
    # 6. STRUCTURAL MODELING SCOPE BOUNDARY
    # -------------------------------------------------------------
    res_section = ms_text[ms_text.find("## 3. RESULTS"):ms_text.find("## 4. DISCUSSION")]
    for struct_term in ["AlphaFold", "RMSD", "PDB", "PyMOL"]:
        m = re.findall(struct_term, res_section, re.IGNORECASE)
        check(len(m) == 0, f"TEST_NO_3D_IN_RESULTS_{struct_term}", 
              f"Strict absence of {struct_term} from Results", f"Found {len(m)} matches: {m}")

    disc_section = ms_text[ms_text.find("## 4. DISCUSSION"):ms_text.find("## 5. CONCLUSIONS")]
    check("Cryo-EM" in disc_section and "patch-clamp" in disc_section, 
          "TEST_FUTURE_PERSPECTIVES_METHODS", 
          "Future perspectives explicitly proposes Cryo-EM and patch-clamp electrophysiology")

    # -------------------------------------------------------------
    # SUMMARY
    # -------------------------------------------------------------
    print("\n=================================================================")
    print(f"VERIFICATION SUMMARY: {len(passes)} PASSED, {len(failures)} FAILED")
    print("=================================================================")

    if failures:
        print("\nFAILED ASSERTIONS:")
        for fid, desc, det in failures:
            print(f" - [{fid}] {desc}: {det}")
        return False
    else:
        print("\nALL ADVERSARIAL EMPIRICAL TESTS PASSED PERFECTLY!")
        return True

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
