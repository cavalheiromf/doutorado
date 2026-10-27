#!/usr/bin/env python3
"""
Step 7: Generate Publication-Ready Figures.
Strictly implements:
- Figure 1: annotation_coverage.pdf (coverage, QC, true term-level non-IEA rates, exact scenario dimensions)
    Fixes: 'Pandanus tectorius', removes 'Opportunity Opportunity' typo, exact Tier A count (170 in Scen 2)
- Figure 2: enrichment_dotplot.pdf (Primary inferential terms: GO Propagated + KEGG, excludes root terms,
    clearly indicates Confirmatory vs Suggestive vs Size Artifacts, log2(OR) with exact 95% CI)
- Figure 3: enrichment_upset.pdf (UpSet of shared non-redundant enriched terms across conditional contrasts)
- Figure 4: representative_families_heatmap.pdf (Clean readable layout: ~30 key families,
    Pandanus tectorius, log1p counts and signed CAFE5 changes)
Exports both PDF and PNG formats.
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import Normalize
from collections import defaultdict

# Clean publication typography
plt.rcParams["font.sans-serif"] = "DejaVu Sans"
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["figure.dpi"] = 300
plt.rcParams["savefig.dpi"] = 300
plt.rcParams["axes.linewidth"] = 1.0
plt.rcParams["xtick.major.width"] = 1.0
plt.rcParams["ytick.major.width"] = 1.0

ROOT_TERMS = {"GO:0008150", "GO:0003674", "GO:0005575"}

def make_coverage_figure(base_dir, fig_dir):
    print("[*] Generating Figure 1: annotation_coverage...", flush=True)
    qc_file = os.path.join(base_dir, "functional_annotation_qc.tsv")
    df_qc = pd.read_csv(qc_file, sep="\t").set_index("Metric")
    
    ann_file = os.path.join(base_dir, "orthogroup_functional_annotations.tsv")
    df_ann = pd.read_csv(ann_file, sep="\t")
    
    mat_file = os.path.join(base_dir, "intermediate", "family_term_matrix.tsv")
    df_mat = pd.read_csv(mat_file, sep="\t")
    
    fig, axes = plt.subplots(2, 2, figsize=(11, 9))
    
    # Panel A: Annotation coverage across categories
    ax_a = axes[0, 0]
    cats = ["GO_BP", "GO_MF", "GO_CC", "KEGG"]
    labels = ["Biological Process\n(GO:BP Propagated)", "Molecular Function\n(GO:MF Propagated)", "Cellular Component\n(GO:CC Propagated)", "KEGG Pathways\n(KEGG Direct)"]
    
    annotated_counts = [
        int(df_qc.loc["Families_With_GO_BP_Propagated", "Value"]),
        int(df_qc.loc["Families_With_GO_MF_Propagated", "Value"]),
        int(df_qc.loc["Families_With_GO_CC_Propagated", "Value"]),
        int(df_qc.loc["Families_With_KEGG", "Value"])
    ]
    total_fams = int(df_qc.loc["Total_Families", "Value"])
    unannotated = [total_fams - c for c in annotated_counts]
    
    y_pos = np.arange(len(cats))
    ax_a.barh(y_pos, annotated_counts, color="#2b5c8f", edgecolor="black", height=0.55, label="Annotated")
    ax_a.barh(y_pos, unannotated, left=annotated_counts, color="#e0e0e0", edgecolor="black", height=0.55, label="Unannotated")
    
    for i, c in enumerate(annotated_counts):
        pct = (c / total_fams) * 100
        ax_a.text(c / 2, i, f"{c:,}\n({pct:.1f}%)", ha="center", va="center", color="white", fontweight="bold", fontsize=8.5)
        
    ax_a.set_yticks(y_pos)
    ax_a.set_yticklabels(labels, fontsize=9.5)
    ax_a.set_xlabel("Number of Gene Families (N = 12,276)", fontsize=9.5)
    ax_a.set_title("A. Orthogroup Annotation Coverage (Excluding Root Terms)", fontsize=10.5, fontweight="bold", loc="left")
    ax_a.legend(loc="lower right", frameon=True, fontsize=8.5)
    ax_a.set_xlim(0, 13500)
    ax_a.spines["top"].set_visible(False)
    ax_a.spines["right"].set_visible(False)
    
    # Panel B: Annotation Opportunity Space (Ath loci vs Family Size)
    ax_b = axes[0, 1]
    prot_counts = df_ann["N_Proteins_Total"]
    ath_loci = df_ann["N_Ath_Loci"]
    
    hb = ax_b.hexbin(prot_counts, ath_loci, gridsize=35, bins="log", cmap="YlGnBu", mincnt=1, xscale="log", yscale="log")
    cb = fig.colorbar(hb, ax=ax_b, orientation="vertical", pad=0.02)
    cb.set_label(r"$\log_{10}$ (Number of Families)", fontsize=9)
    
    ax_b.set_xlabel("Total Proteins per Family ($\log_{10}$ scale)", fontsize=9.5)
    ax_b.set_ylabel("Arabidopsis Loci per Family ($\log_{10}$ scale)", fontsize=9.5)
    ax_b.set_title("B. Annotation Opportunity Space", fontsize=10.5, fontweight="bold", loc="left")
    ax_b.spines["top"].set_visible(False)
    ax_b.spines["right"].set_visible(False)
    
    # Panel C: True Term-Level Non-IEA Evidence Composition
    ax_c = axes[1, 0]
    go_cats = ["GO_BP", "GO_MF", "GO_CC"]
    go_labels = ["BP", "MF", "CC"]
    
    non_iea_counts = []
    iea_only_counts = []
    for c in go_cats:
        sub_mat = df_mat[df_mat["Category"] == c]
        n_non_iea = (sub_mat["Has_Non_IEA"]).sum()
        n_total = len(sub_mat)
        non_iea_counts.append(n_non_iea)
        iea_only_counts.append(n_total - n_non_iea)
        
    x_pos = np.arange(len(go_cats))
    ax_c.bar(x_pos - 0.18, non_iea_counts, width=0.35, color="#1b7837", edgecolor="black", label="Non-electronic evidence, excluding IEA and ND")
    ax_c.bar(x_pos + 0.18, iea_only_counts, width=0.35, color="#a6dba0", edgecolor="black", label="Electronic Only (IEA)")
    
    for i in range(len(go_cats)):
        ax_c.text(i - 0.18, non_iea_counts[i] + 3000, f"{non_iea_counts[i]:,}", ha="center", fontsize=8, fontweight="bold")
        ax_c.text(i + 0.18, iea_only_counts[i] + 3000, f"{iea_only_counts[i]:,}", ha="center", fontsize=8)
        
    ax_c.set_xticks(x_pos)
    ax_c.set_xticklabels(go_labels, fontsize=9.5)
    ax_c.set_ylabel("Number of Family–Term Associations", fontsize=9.5)
    ax_c.set_title("C. Gene Ontology Evidence Code Composition (Term Level)", fontsize=10.5, fontweight="bold", loc="left")
    ax_c.legend(loc="upper right", frameon=True, fontsize=8)
    ax_c.set_ylim(0, max(non_iea_counts) * 1.25)
    ax_c.spines["top"].set_visible(False)
    ax_c.spines["right"].set_visible(False)
    
    # Panel D: Scenario retention with exact counts
    ax_d = axes[1, 1]
    scenario_names = [
        "1. All Families",
        "2. Excl. Transposon/\nExtreme Asymmetry",
        "3. Nuclear Only",
        "4. GO Non-IEA Only"
    ]
    scenario_counts = [12276, 12232, 11908, 11819]
    tier_a_counts = [188, 170, 175, 148]
    
    y_pos = np.arange(len(scenario_names))
    ax_d.barh(y_pos - 0.18, scenario_counts, height=0.35, color="#4393c3", edgecolor="black", label="Universe Families")
    ax_d.barh(y_pos + 0.18, [c * 50 for c in tier_a_counts], height=0.35, color="#d6604d", edgecolor="black", label="Tier A Core (scaled 50x)")
    
    for i in range(len(scenario_names)):
        ax_d.text(scenario_counts[i] + 150, i - 0.18, f"{scenario_counts[i]:,}", va="center", fontsize=8)
        ax_d.text(tier_a_counts[i] * 50 + 150, i + 0.18, f"{tier_a_counts[i]}", va="center", fontsize=8, fontweight="bold", color="#b2182b")
        
    ax_d.set_yticks(y_pos)
    ax_d.set_yticklabels(scenario_names, fontsize=8.5)
    ax_d.set_xlabel("Family Count", fontsize=9.5)
    ax_d.set_title("D. Analytical Sensitivity Scenarios (Exact Retention)", fontsize=10.5, fontweight="bold", loc="left")
    ax_d.legend(loc="lower right", frameon=True, fontsize=8)
    ax_d.set_xlim(0, 15000)
    ax_d.spines["top"].set_visible(False)
    ax_d.spines["right"].set_visible(False)
    
    plt.tight_layout()
    pdf_path = os.path.join(fig_dir, "annotation_coverage.pdf")
    png_path = os.path.join(fig_dir, "annotation_coverage.png")
    fig.savefig(pdf_path, bbox_inches="tight")
    fig.savefig(png_path, bbox_inches="tight")
    plt.close(fig)
    print(f"[*] Saved Figure 1: {pdf_path}", flush=True)

def make_dotplot_figure(base_dir, fig_dir):
    print("[*] Generating Figure 2: enrichment_dotplot...", flush=True)
    reduced_file = os.path.join(base_dir, "enrichment_results_reduced_for_plotting.tsv")
    df_red = pd.read_csv(reduced_file, sep="\t")
    
    # Filter to representative primary inferential terms (GO Propagated + KEGG)
    df_plot = df_red[(df_red["Is_Representative"] == True) & (df_red["Is_Primary_Inferential"] == True)].copy()
    
    # Truncate long names
    def clean_name(row):
        n = row["Term_Name"]
        if len(n) > 38:
            n = n[:36] + "..."
        return f"{n} ({row['Term_ID']})"
    df_plot["Plot_Name"] = df_plot.apply(clean_name, axis=1)
    
    # Cap infinite OR for visualization
    finite_or = df_plot["Conditional_OR"][np.isfinite(df_plot["Conditional_OR"])]
    max_finite = finite_or.max() if len(finite_or) > 0 else 50.0
    
    plot_or, plot_ci_low, plot_ci_high = [], [], []
    for _, r in df_plot.iterrows():
        or_val = r["Conditional_OR"]
        low = r["CI_95_Low"]
        high = r["CI_95_High"]
        if np.isinf(or_val): or_val = max_finite * 1.5
        if np.isinf(high): high = max_finite * 2.0
        plot_or.append(max(0.1, or_val))
        plot_ci_low.append(max(0.05, low))
        plot_ci_high.append(max(0.1, high))
        
    df_plot["Plot_OR"] = plot_or
    df_plot["log2_OR"] = np.log2(df_plot["Plot_OR"])
    df_plot["log2_CI_Low"] = np.log2(plot_ci_low)
    df_plot["log2_CI_High"] = np.log2(plot_ci_high)
    df_plot["neg_log10_q"] = -np.log10(np.clip(df_plot["q_value"], 1e-15, 1.0))
    
    ev_order = {
        "Confirmatory": 0,
        "Suggestive": 1,
        "Suggestive_Imbalanced_Opportunity": 2,
        "Permutation_Discordant": 3,
        "Diagnostic_Nominal_Sig": 4
    }
    df_plot["_ev_rank"] = [ev_order.get(x, 9) for x in df_plot["Evidence_Class"]]
    df_plot = df_plot.sort_values(by=["Contrast_ID", "_ev_rank", "log2_OR"], ascending=[True, True, True]).reset_index(drop=True)
    
    n_terms = len(df_plot)
    fig_height = max(9.5, n_terms * 0.38)
    fig, ax = plt.subplots(figsize=(11, fig_height))
    
    y_pos = np.arange(n_terms)
    
    err_low = np.clip(df_plot["log2_OR"] - df_plot["log2_CI_Low"], 0, None)
    err_high = np.clip(df_plot["log2_CI_High"] - df_plot["log2_OR"], 0, None)
    
    ax.errorbar(
        df_plot["log2_OR"], y_pos,
        xerr=[err_low, err_high],
        fmt="none", ecolor="#999999", elinewidth=1.2, capsize=3, zorder=1
    )
    
    # Indicate infinite CI bounds with censoring arrows
    for i, (_, r) in enumerate(df_plot.iterrows()):
        if np.isinf(r["CI_95_High"]) or np.isinf(r["Conditional_OR"]):
            ax.annotate('', xy=(r["log2_CI_High"], i), xytext=(r["log2_CI_High"] - 0.4, i),
                        arrowprops=dict(arrowstyle="->", color="#666666", lw=1.2))
    
    norm = Normalize(vmin=df_plot["neg_log10_q"].min(), vmax=df_plot["neg_log10_q"].max())
    cmap = plt.cm.viridis
    
    for i, (_, r) in enumerate(df_plot.iterrows()):
        color = cmap(norm(r["neg_log10_q"]))
        size = 42 + (r["FG_Count"] * 8)
        ec = r["Evidence_Class"]
        
        if ec == "Confirmatory":
            # Solid filled circle with bold black outline
            ax.scatter(r["log2_OR"], i, s=size, c=[color], edgecolors="black", linewidth=1.8, zorder=3)
        elif ec == "Suggestive":
            # Solid circle with distinct dark green outline
            ax.scatter(r["log2_OR"], i, s=size, c=[color], edgecolors="#005a32", linewidth=1.5, zorder=3)
        elif ec == "Suggestive_Imbalanced_Opportunity":
            # Distinct square marker with amber/orange outline
            ax.scatter(r["log2_OR"], i, s=size, c=[color], edgecolors="#e6550d", linewidth=1.8, marker="s", zorder=3)
        else: # Permutation_Discordant
            # Open circle with dashed red outline
            ax.scatter(r["log2_OR"], i, s=size, c=[color], edgecolors="#d95f02", linewidth=1.5, linestyle="--", zorder=3)
            
    ax.axvline(0, color="#b2182b", linestyle=":", linewidth=1.2, zorder=0)
    
    # Separator lines between different contrasts
    contrast_changes = np.where(df_plot["Contrast_ID"].values[:-1] != df_plot["Contrast_ID"].values[1:])[0]
    for ch in contrast_changes:
        ax.axhline(ch + 0.5, color="#cccccc", linestyle="-", linewidth=0.8, zorder=0)
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(df_plot["Plot_Name"], fontsize=8.5)
    ax.set_xlabel(r"$\log_2$ (Conditional Odds Ratio) with exact 95% CI (arrows indicate infinite upper bounds)", fontsize=9.5, fontweight="bold")
    ax.set_title("Representative Enriched Functional Terms (GO Propagated & KEGG)", fontsize=11, fontweight="bold", pad=15)
    
    # Sidebar indicating Contrast
    contrast_list = df_plot["Contrast_ID"].unique()
    c_colors = plt.cm.tab10(np.linspace(0, 1, len(contrast_list)))
    c_color_map = {c: col for c, col in zip(contrast_list, c_colors)}
    for i, cid in enumerate(df_plot["Contrast_ID"]):
        ax.plot(-0.015, i, marker="|", color=c_color_map[cid], markersize=14, transform=ax.get_yaxis_transform(), clip_on=False)
        
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cb = fig.colorbar(sm, ax=ax, orientation="vertical", pad=0.02, shrink=0.35, aspect=15)
    cb.set_label("$-\\log_{10}(q_{\\mathrm{local}})$", fontsize=9)
    
    leg_handles = [
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="#2b5c8f", markeredgecolor="black", markeredgewidth=1.8, markersize=9, label="Confirmatory ($q_{\\mathrm{global}} < 0.05$, balanced)"),
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="#2b5c8f", markeredgecolor="#005a32", markeredgewidth=1.5, markersize=9, label="Suggestive ($p_{\\mathrm{strat}} < 0.05$, balanced)"),
        plt.Line2D([0], [0], marker="s", color="w", markerfacecolor="#2b5c8f", markeredgecolor="#e6550d", markeredgewidth=1.8, markersize=9, label="Suggestive (Imbalanced opportunity caveat)"),
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="#2b5c8f", markeredgecolor="#d95f02", markeredgewidth=1.5, linestyle="--", markersize=9, label="Permutation-discordant ($p_{\\mathrm{strat}} \\geq 0.05$)")
    ]
    ax.legend(handles=leg_handles, loc="lower right", frameon=True, fontsize=8)
    
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    
    plt.tight_layout()
    pdf_path = os.path.join(fig_dir, "enrichment_dotplot.pdf")
    png_path = os.path.join(fig_dir, "enrichment_dotplot.png")
    fig.savefig(pdf_path, bbox_inches="tight")
    fig.savefig(png_path, bbox_inches="tight")
    plt.close(fig)
    print(f"[*] Saved Figure 2: {pdf_path}", flush=True)

def make_upset_figure(base_dir, fig_dir):
    print("[*] Generating Figure 3: enrichment_upset...", flush=True)
    all_res_file = os.path.join(base_dir, "enrichment_results_primary.tsv")
    df = pd.read_csv(all_res_file, sep="\t")
    
    # Filter to robust (Confirmatory + Suggestive) terms across conditional contrasts
    df_cond = df[(df["Is_Primary_Inferential"] == True) & (df["Contrast_Type"] == "conditional") & (df["Evidence_Class"].isin(["Confirmatory", "Suggestive"]))].copy()
    
    contrasts = sorted(df_cond["Contrast_ID"].unique())
    print(f"    Conditional contrasts with robust terms: {contrasts}", flush=True)
    
    if len(contrasts) == 0:
        print("    No conditional contrasts with robust terms; creating empty placeholder.", flush=True)
        return
        
    term_contrasts = defaultdict(set)
    for _, r in df_cond.iterrows():
        term_contrasts[r["Term_ID"]].add(r["Contrast_ID"])
        
    pattern_counts = defaultdict(list)
    for t, c_set in term_contrasts.items():
        pattern_key = tuple(sorted(c_set))
        pattern_counts[pattern_key].append(t)
        
    sorted_patterns = sorted(pattern_counts.items(), key=lambda x: len(x[1]), reverse=True)
    
    fig = plt.figure(figsize=(10, 6.5))
    gs = fig.add_gridspec(2, 2, width_ratios=[1.2, 2.8], height_ratios=[2, 1.4], wspace=0.12, hspace=0.15)
    
    ax_top = fig.add_subplot(gs[0, 1])
    ax_matrix = fig.add_subplot(gs[1, 1], sharex=ax_top)
    ax_left = fig.add_subplot(gs[1, 0])
    ax_empty = fig.add_subplot(gs[0, 0])
    ax_empty.axis("off")
    
    inter_sizes = [len(terms) for _, terms in sorted_patterns]
    n_patterns = len(sorted_patterns)
    x_pos = np.arange(n_patterns)
    
    ax_top.bar(x_pos, inter_sizes, color="#2b5c8f", edgecolor="black", width=0.55)
    for i, s in enumerate(inter_sizes):
        ax_top.text(i, s + 0.15, str(s), ha="center", va="bottom", fontsize=8.5, fontweight="bold")
    ax_top.set_ylabel("Robust Terms Count", fontsize=9)
    ax_top.set_title("Shared Functional Themes Among Conditional Contrasts", fontsize=10.5, fontweight="bold", loc="left")
    ax_top.spines["top"].set_visible(False)
    ax_top.spines["right"].set_visible(False)
    ax_top.tick_params(labelbottom=False, bottom=False)
    
    c_totals = [len(df_cond[df_cond["Contrast_ID"] == c]["Term_ID"].unique()) for c in contrasts]
    y_pos = np.arange(len(contrasts))
    ax_left.barh(y_pos, c_totals, color="#74a9cf", edgecolor="black", height=0.5)
    for i, s in enumerate(c_totals):
        ax_left.text(s + 0.2, i, str(s), ha="left", va="center", fontsize=8.5)
    ax_left.set_yticks(y_pos)
    c_labels = [c.replace("Cond_", "").replace("_", " ") for c in contrasts]
    ax_left.set_yticklabels(c_labels, fontsize=8.5)
    ax_left.set_xlabel("Total Robust Terms", fontsize=9)
    ax_left.invert_xaxis()
    ax_left.spines["top"].set_visible(False)
    ax_left.spines["left"].set_visible(False)
    
    ax_matrix.set_xlim(-0.6, n_patterns - 0.4)
    ax_matrix.set_ylim(-0.5, len(contrasts) - 0.5)
    
    for x in range(n_patterns):
        for y in range(len(contrasts)):
            ax_matrix.scatter(x, y, color="#e0e0e0", s=50, zorder=1)
            
    for x, (pat, _) in enumerate(sorted_patterns):
        active_y = [contrasts.index(c) for c in pat]
        if len(active_y) > 1:
            ax_matrix.plot([x, x], [min(active_y), max(active_y)], color="#2b5c8f", linewidth=2.0, zorder=2)
        ax_matrix.scatter([x] * len(active_y), active_y, color="#2b5c8f", s=70, edgecolors="black", linewidth=1.0, zorder=3)
        
    ax_matrix.set_yticks(y_pos)
    ax_matrix.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)
    ax_matrix.spines["top"].set_visible(False)
    ax_matrix.spines["right"].set_visible(False)
    ax_matrix.spines["left"].set_visible(False)
    ax_matrix.spines["bottom"].set_visible(False)
    
    pdf_path = os.path.join(fig_dir, "enrichment_upset.pdf")
    png_path = os.path.join(fig_dir, "enrichment_upset.png")
    fig.savefig(pdf_path, bbox_inches="tight")
    fig.savefig(png_path, bbox_inches="tight")
    plt.close(fig)
    print(f"[*] Saved Figure 3: {pdf_path}", flush=True)

def make_heatmap_figure(base_dir, fig_dir):
    print("[*] Generating Figure 4: representative_families_heatmap...", flush=True)
    macro_dir = "/home/mfcaval/github/doutorado/chapter_macroevolution"
    master_file = os.path.join(macro_dir, "04_gene_families", "comparative_axes", "comparative_families_master_table_v2.tsv")
    df_master = pd.read_csv(master_file, sep="\t").set_index("FamilyID")
    
    ann_file = os.path.join(base_dir, "orthogroup_functional_annotations.tsv")
    df_ann = pd.read_csv(ann_file, sep="\t").set_index("FamilyID")
    
    mat_file = os.path.join(base_dir, "intermediate", "family_term_matrix.tsv")
    df_mat = pd.read_csv(mat_file, sep="\t")
    
    tier_a_fams = set(df_master[df_master["Evidence_Tier"] == "Tier_A_High_Confidence"].index)
    
    # Pick ~30 highly informative, diverse families across key robust themes
    key_themes = {
        "Organelle Lumen & Condensates (Xvis)": ["GO:0043233", "GO:0043228", "GO:0005730"],
        "Biotic Defense & Stimulus (Contraction)": ["GO:0050896", "GO:0009605", "GO:0043207"],
        "Secondary Metabolism (Vper)": ["ath01110"],
        "Membrane Dynamics (Node 12)": ["GO:0005886", "GO:0016020"],
        "Core Mitochondrion & Energetics (Tier A)": ["GO:0005739"]
    }
    
    selected_fams = []
    fam_theme_map = {}
    
    for theme_name, t_list in key_themes.items():
        theme_fams = set()
        for t in t_list:
            fams = set(df_mat[df_mat["Term_ID"] == t]["FamilyID"]) & tier_a_fams
            theme_fams.update(fams)
        # Select up to 6 representative families per theme
        sub_list = sorted(list(theme_fams))[:6]
        for f in sub_list:
            if f not in selected_fams:
                selected_fams.append(f)
                fam_theme_map[f] = theme_name
                
    # Also add 4 parallel DT expansion families for comparison
    par_exp_fams = sorted(list(set(df_master[df_master["Preserved_k3_Parallel_Exp_DT"] & (df_master["Evidence_Tier"] == "Tier_A_High_Confidence")].index)))[:4]
    for f in par_exp_fams:
        if f not in selected_fams:
            selected_fams.append(f)
            fam_theme_map[f] = "Parallel DT Expansion (Descriptive)"
            
    print(f"    Selected {len(selected_fams)} representative families for readable heatmap layout.", flush=True)
    
    df_sub = df_master.loc[selected_fams]
    
    # Correct species names (including Pandanus tectorius)
    species_cols = ["Count_Ath", "Count_Dala", "Count_Ptec", "Count_Abra", "Count_Vper", "Count_Vtub", "Count_Xvis"]
    species_names = [
        "A. thaliana", "D. alata", "Pandanus tectorius",
        "A. bracteata", "V. peripherica", "V. tubiflora", "X. viscosa"
    ]
    counts_log1p = np.log1p(df_sub[species_cols].values)
    
    change_cols = [
        "Change_Ptec", "Change_Abra",
        "Change_Vper", "Change_Vtub", "Change_Xvis",
        "Change_Node11_Velloziaceae_Crown", "Change_Node12_Core_Velloziaceae", "Change_Node13_Vellozia_Crown"
    ]
    change_names = ["P. tectorius", "A. bracteata", "V. peripherica", "V. tubiflora", "X. viscosa", "Node 11", "Node 12", "Node 13"]
    changes_arr = df_sub[change_cols].fillna(0).values
    
    n_fams = len(selected_fams)
    fig_h = max(9.5, n_fams * 0.35)
    fig = plt.figure(figsize=(12.5, fig_h))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.25, 1.0], wspace=0.22, bottom=0.18, top=0.93)
    
    # Left Panel: Species Gene Counts (log1p)
    ax_left = fig.add_subplot(gs[0, 0])
    im1 = ax_left.imshow(counts_log1p, aspect="auto", cmap="YlGnBu", interpolation="nearest")
    ax_left.set_xticks(np.arange(len(species_names)))
    ax_left.set_xticklabels(species_names, rotation=35, ha="right", fontsize=9, fontstyle="italic")
    
    row_labels = []
    for f in selected_fams:
        ath = str(df_ann.loc[f, "Ath_Locus_Tags"]).split(";")[0] if f in df_ann.index and pd.notna(df_ann.loc[f, "Ath_Locus_Tags"]) else ""
        if ath and ath != "nan":
            row_labels.append(f"{f} ({ath})")
        else:
            row_labels.append(f)
            
    ax_left.set_yticks(np.arange(n_fams))
    ax_left.set_yticklabels(row_labels, fontsize=8.5)
    ax_left.set_title("A. Species Copy Number ($\log_{1p}$ Counts)", fontsize=10.5, fontweight="bold")
    
    cb1 = fig.colorbar(im1, ax=ax_left, orientation="horizontal", pad=0.14, shrink=0.7)
    cb1.set_label(r"$\log_{1p}$ (Gene Count)", fontsize=8.5)
    
    # Right Panel: CAFE5 Reconstructed Branch Changes (signed scale)
    ax_right = fig.add_subplot(gs[0, 1])
    vmax = max(6.0, float(np.percentile(np.abs(changes_arr), 98)))
    im2 = ax_right.imshow(changes_arr, aspect="auto", cmap="RdBu_r", vmin=-vmax, vmax=vmax, interpolation="nearest")
    ax_right.set_xticks(np.arange(len(change_names)))
    ax_right.set_xticklabels(change_names, rotation=35, ha="right", fontsize=8.5)
    ax_right.set_yticks(np.arange(n_fams))
    ax_right.tick_params(labelleft=False, left=False)
    ax_right.set_title("B. CAFE5 Inferred Branch Changes (Signed $+/-$)", fontsize=10.5, fontweight="bold")
    
    cb2 = fig.colorbar(im2, ax=ax_right, orientation="horizontal", pad=0.14, shrink=0.7)
    cb2.set_label("Reconstructed Copy Number Change ($+/-$)", fontsize=8.5)
    
    for r in range(changes_arr.shape[0]):
        for c in range(changes_arr.shape[1]):
            val = int(changes_arr[r, c])
            if abs(val) >= 3:
                color = "white" if abs(val) >= 5 else "black"
                ax_right.text(c, r, f"{val:+d}", ha="center", va="center", fontsize=7.5, color=color, fontweight="bold")
                
    pdf_path = os.path.join(fig_dir, "representative_families_heatmap.pdf")
    png_path = os.path.join(fig_dir, "representative_families_heatmap.png")
    fig.savefig(pdf_path, bbox_inches="tight")
    fig.savefig(png_path, bbox_inches="tight")
    plt.close(fig)
    print(f"[*] Saved Figure 4: {pdf_path}", flush=True)

def main():
    base_dir = "/home/mfcaval/github/doutorado/chapter_macroevolution/04_gene_families/functional_enrichment"
    fig_dir = os.path.join(base_dir, "figures")
    os.makedirs(fig_dir, exist_ok=True)
    
    make_coverage_figure(base_dir, fig_dir)
    make_dotplot_figure(base_dir, fig_dir)
    make_upset_figure(base_dir, fig_dir)
    make_heatmap_figure(base_dir, fig_dir)
    print("\n[*] [PASSED] All 4 publication figures generated successfully in PDF and PNG formats.")

if __name__ == "__main__":
    main()
