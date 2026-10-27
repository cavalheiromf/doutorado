#!/usr/bin/env python3
"""
scripts/analyze_mcmctree_chains.py

Diagnóstico bayesiano de convergência, cálculo de ESS e geração do cronograma final
a partir de duas cadeias independentes de alto ESS do MCMCTree.
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

DATING_DIR = "/home/mfcaval/github/doutorado/chapter_macroevolution/03_dating"
CHAIN1_DIR = os.path.join(DATING_DIR, "chain1")
CHAIN2_DIR = os.path.join(DATING_DIR, "chain2")
FIGURES_DIR = os.path.join(os.path.dirname(DATING_DIR), "04_gene_families", "figures")
OUT_SUMMARY = os.path.join(DATING_DIR, "mcmctree_high_ess_convergence_summary.tsv")
OUT_TREE = os.path.join(DATING_DIR, "velloziaceae_chronogram_high_ess.tre")
OUT_FIG = os.path.join(FIGURES_DIR, "figure_s3_mcmctree_dating_convergence.png")
OUT_FIG_PDF = os.path.join(FIGURES_DIR, "figure_s3_mcmctree_dating_convergence.pdf")

NODE_NAMES = {
    "t_n8": "Root (Angiosperms: Eudicots vs Monocots)",
    "t_n9": "Monocots (Dioscoreales vs Pandanales)",
    "t_n10": "Pandanales (Pandanaceae vs Velloziaceae)",
    "t_n11": "Velloziaceae Crown (Acanthochlamys vs Core)",
    "t_n12": "Core Velloziaceae (Xerophyta vs Vellozia) [FREE]",
    "t_n13": "Vellozia Speciation (V. peripherica vs V. tubiflora)"
}

def compute_ess(series):
    """Calcula o Effective Sample Size (ESS) via FFT para máxima velocidade."""
    n = len(series)
    x = series.values - np.mean(series)
    f = np.fft.fft(x, n=2*n)
    autocorr = np.fft.ifft(f * np.conj(f))[:n].real
    autocorr = autocorr / autocorr[0]
    cutoff = 1
    while cutoff < len(autocorr) and autocorr[cutoff] > 0:
        cutoff += 1
    act = 1 + 2 * np.sum(autocorr[1:cutoff])
    return n / act if act > 0 else n

def compute_gelman_rubin(chain1, chain2):
    """Calcula o diagnóstico de convergência de Gelman-Rubin (R-hat)."""
    n = len(chain1)
    m = 2
    mean1 = np.mean(chain1)
    mean2 = np.mean(chain2)
    overall_mean = (mean1 + mean2) / 2
    
    # Between-chain variance
    B = (n / (m - 1)) * ((mean1 - overall_mean)**2 + (mean2 - overall_mean)**2)
    
    # Within-chain variance
    W = (np.var(chain1, ddof=1) + np.var(chain2, ddof=1)) / 2
    
    # Pooled variance
    var_plus = ((n - 1) / n) * W + (1 / n) * B
    r_hat = np.sqrt(var_plus / W) if W > 0 else 1.0
    return r_hat

def main():
    print("======================================================================")
    print(" Diagnóstico de Convergência MCMCTree (Replicatas Independentes)")
    print("======================================================================")
    
    mcmc1_file = os.path.join(CHAIN1_DIR, "mcmc.txt")
    mcmc2_file = os.path.join(CHAIN2_DIR, "mcmc.txt")
    
    if not (os.path.exists(mcmc1_file) and os.path.exists(mcmc2_file)):
        print(f"[ERRO] Arquivos mcmc.txt não encontrados em {CHAIN1_DIR} e/ou {CHAIN2_DIR}")
        sys.exit(1)
        
    df1 = pd.read_csv(mcmc1_file, sep="\t")
    df2 = pd.read_csv(mcmc2_file, sep="\t")
    
    print(f"Cadeia 1: {len(df1):,} amostras | Cadeia 2: {len(df2):,} amostras")
    
    # Parâmetros temporais e de taxa
    time_nodes = ["t_n8", "t_n9", "t_n10", "t_n11", "t_n12", "t_n13"]
    other_params = ["mu", "sigma2"]
    all_params = [p for p in time_nodes + other_params if p in df1.columns]
    
    summary_rows = []
    
    print("\n" + "="*95)
    print(f"{'Parâmetro':<10} {'Clade/Descrição':<45} {'Média (Ma)':<12} {'IC 95% HPD':<18} {'ESS':<8} {'R-hat':<6}")
    print("="*95)
    
    for param in all_params:
        is_time = param.startswith("t_")
        scale = 100.0 if is_time else 1.0
        
        c1 = df1[param] * scale
        c2 = df2[param] * scale
        comb = pd.concat([c1, c2])
        
        ess1 = compute_ess(c1)
        ess2 = compute_ess(c2)
        comb_ess = compute_ess(comb)
        r_hat = compute_gelman_rubin(c1, c2)
        
        mean_val = np.mean(comb)
        hpd_low = np.percentile(comb, 2.5)
        hpd_high = np.percentile(comb, 97.5)
        
        desc = NODE_NAMES.get(param, param)
        
        summary_rows.append({
            "Parameter": param,
            "Description": desc,
            "Chain1_Mean": np.mean(c1),
            "Chain1_ESS": ess1,
            "Chain2_Mean": np.mean(c2),
            "Chain2_ESS": ess2,
            "Combined_Mean": mean_val,
            "Combined_HPD95_Lower": hpd_low,
            "Combined_HPD95_Upper": hpd_high,
            "Combined_ESS": comb_ess,
            "Gelman_Rubin_Rhat": r_hat
        })
        
        val_str = f"{mean_val:.2f}"
        ci_str = f"[{hpd_low:.2f}, {hpd_high:.2f}]"
        print(f"{param:<10} {desc[:44]:<45} {val_str:<12} {ci_str:<18} {comb_ess:<8.0f} {r_hat:<6.3f}")
        
    df_summary = pd.DataFrame(summary_rows)
    df_summary.to_csv(OUT_SUMMARY, sep="\t", index=False)
    print(f"\n[INFO] Tabela salva em: {OUT_SUMMARY}")
    
    # 2. Gerar Nova Árvore Newick Ultramétrica
    means = {row["Parameter"]: row["Combined_Mean"] for row in summary_rows if row["Parameter"].startswith("t_")}
    
    # Newick com tempos combinados de alto ESS:
    # t_n13 = Vper/Vtub; t_n12 = Xvis vs Vellozia; t_n11 = Abra vs Core; t_n10 = Ptec; t_n9 = Dala; t_n8 = Ath
    vper_vtub = means["t_n13"]
    xvis_node = means["t_n12"]
    abra_node = means["t_n11"]
    ptec_node = means["t_n10"]
    dala_node = means["t_n9"]
    ath_node  = means["t_n8"]
    
    bl_vper = vper_vtub
    bl_xvis_branch = xvis_node - vper_vtub
    bl_xvis_tip = xvis_node
    bl_abra_branch = abra_node - xvis_node
    bl_abra_tip = abra_node
    bl_ptec_branch = ptec_node - abra_node
    bl_ptec_tip = ptec_node
    bl_dala_branch = dala_node - ptec_node
    bl_dala_tip = dala_node
    bl_ath_branch = ath_node - dala_node
    bl_ath_tip = ath_node
    
    newick_high_ess = f"((((((Vper:{bl_vper:.4f},Vtub:{bl_vper:.4f}):{bl_xvis_branch:.4f},Xvis:{bl_xvis_tip:.4f}):{bl_abra_branch:.4f},Abra:{bl_abra_tip:.4f}):{bl_ptec_branch:.4f},Ptec:{bl_ptec_tip:.4f}):{bl_dala_branch:.4f},Dala:{bl_dala_tip:.4f}):{bl_ath_branch:.4f},Ath:{bl_ath_tip:.4f});\n"
    
    with open(OUT_TREE, "w") as f:
        f.write(newick_high_ess)
    print(f"[INFO] Árvore ultramétrica atualizada salva em: {OUT_TREE}")
    print(f"       {newick_high_ess.strip()}")
    
    # 3. Gerar Figuras com Diagnósticos em Português e Inglês
    def render_plot(lang="pt"):
        is_en = (lang == "en")
        suffix = "_en" if is_en else ""
        out_png = os.path.join(FIGURES_DIR, f"figure_s3_mcmctree_dating_convergence{suffix}.png")
        out_pdf = os.path.join(FIGURES_DIR, f"figure_s3_mcmctree_dating_convergence{suffix}.pdf")
        
        plt.rcParams.update({
            'font.sans-serif': ['Arial', 'DejaVu Sans', 'Helvetica'],
            'font.family': 'sans-serif',
            'font.size': 8.5,
            'axes.labelsize': 9.5,
            'axes.titlesize': 10.5,
            'figure.titlesize': 12.0
        })
        
        fig = plt.figure(figsize=(10, 8), dpi=300)
        gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1], hspace=0.35, wspace=0.3)
        
        # Painel A: Dispersão Replicata 1 vs Replicata 2
        ax1 = fig.add_subplot(gs[0, 0])
        c1_means = [row["Chain1_Mean"] for row in summary_rows if row["Parameter"].startswith("t_")]
        c2_means = [row["Chain2_Mean"] for row in summary_rows if row["Parameter"].startswith("t_")]
        labels = [row["Parameter"] for row in summary_rows if row["Parameter"].startswith("t_")]
        
        ax1.scatter(c1_means, c2_means, color="#0072B2", s=60, edgecolors="k", zorder=3)
        min_v, max_v = min(c1_means) * 0.8, max(c1_means) * 1.05
        ax1.plot([min_v, max_v], [min_v, max_v], "r--", lw=1.2, label="1:1 Identity Line" if is_en else "Linha de Identidade (1:1)")
        
        corr = np.corrcoef(c1_means, c2_means)[0, 1]**2
        ax1.set_xlabel("Posterior Mean Age — Chain 1 (Ma)" if is_en else "Idade Posterior Média — Cadeia 1 (Ma)")
        ax1.set_ylabel("Posterior Mean Age — Chain 2 (Ma)" if is_en else "Idade Posterior Média — Cadeia 2 (Ma)")
        ax1.set_title(f"A. Inter-chain Convergence ($r^2 = {corr:.4f}$)" if is_en else f"A. Convergência Inter-Cadeias ($r^2 = {corr:.4f}$)")
        ax1.legend(frameon=False, loc="upper left")
        ax1.grid(True, linestyle=":", alpha=0.6)
        
        for lbl, x, y in zip(labels, c1_means, c2_means):
            ax1.annotate(lbl, (x, y), textcoords="offset points", xytext=(-10, 8), fontsize=8)
            
        # Painel B: Traço de MCMC (Mixing)
        ax2 = fig.add_subplot(gs[0, 1])
        gens = np.arange(len(df1)) * 100
        l_c1 = "Chain 1 (t_n12: Xerophyta vs Vellozia)" if is_en else "Cadeia 1 (t_n12: Xerophyta vs Vellozia)"
        l_c2 = "Chain 2 (t_n12: Xerophyta vs Vellozia)" if is_en else "Cadeia 2 (t_n12: Xerophyta vs Vellozia)"
        l_cm = f"Combined Mean ({means['t_n12']:.1f} Ma)" if is_en else f"Média Combinada ({means['t_n12']:.1f} Ma)"
        
        ax2.plot(gens[::5], (df1["t_n12"] * 100)[::5], color="#D55E00", alpha=0.7, lw=0.8, label=l_c1)
        ax2.plot(gens[::5], (df2["t_n12"] * 100)[::5], color="#009E73", alpha=0.7, lw=0.8, label=l_c2)
        ax2.axhline(means["t_n12"], color="black", linestyle="--", lw=1.0, label=l_cm)
        ax2.set_xlabel("Post-burnin MCMC generations" if is_en else "Gerações MCMC pós-burnin")
        ax2.set_ylabel("Node Age (Ma)" if is_en else "Idade do Nó (Ma)")
        ax2.set_title("B. Stationarity and Chain Mixing (t_n12)" if is_en else "B. Estacionariedade e Mistura da Cadeia (t_n12)")
        ax2.legend(frameon=False, fontsize=7.5, loc="upper right")
        ax2.grid(True, linestyle=":", alpha=0.6)
        
        # Painel C: Distribuição Posterior do Nó Não-Calibrado (Xerophyta vs Vellozia)
        ax3 = fig.add_subplot(gs[1, 0])
        combined_n12 = pd.concat([df1["t_n12"], df2["t_n12"]]) * 100.0
        ax3.hist(combined_n12, bins=50, density=True, color="#56B4E9", alpha=0.7, edgecolor="k", lw=0.5)
        m_lbl = f"Mean: {means['t_n12']:.2f} Ma" if is_en else f"Média: {means['t_n12']:.2f} Ma"
        ci_lbl = f"95% HPD: [{np.percentile(combined_n12, 2.5):.1f}, {np.percentile(combined_n12, 97.5):.1f}] Ma" if is_en else f"IC 95%: [{np.percentile(combined_n12, 2.5):.1f}, {np.percentile(combined_n12, 97.5):.1f}]"
        
        ax3.axvline(means["t_n12"], color="red", lw=1.5, linestyle="-", label=m_lbl)
        ax3.axvline(np.percentile(combined_n12, 2.5), color="gray", lw=1.2, linestyle="--", label=ci_lbl)
        ax3.axvline(np.percentile(combined_n12, 97.5), color="gray", lw=1.2, linestyle="--")
        ax3.set_xlabel("Geological Time (Ma)" if is_en else "Tempo Geológico (Ma)")
        ax3.set_ylabel("Posterior Density" if is_en else "Densidade Posterior")
        ax3.set_title("C. Core Velloziaceae (Xerophyta vs Vellozia) [Unconstrained]" if is_en else "C. Idade Estimada: Core Velloziaceae (Xvis vs Vper/Vtub)")
        ax3.legend(frameon=False, fontsize=8)
        ax3.grid(True, linestyle=":", alpha=0.6)
        
        # Painel D: Distribuição Posterior do Nó de Especiação em Vellozia
        ax4 = fig.add_subplot(gs[1, 1])
        combined_n13 = pd.concat([df1["t_n13"], df2["t_n13"]]) * 100.0
        ax4.hist(combined_n13, bins=50, density=True, color="#E69F00", alpha=0.7, edgecolor="k", lw=0.5)
        m_lbl13 = f"Mean: {means['t_n13']:.2f} Ma" if is_en else f"Média: {means['t_n13']:.2f} Ma"
        ci_lbl13 = f"95% HPD: [{np.percentile(combined_n13, 2.5):.1f}, {np.percentile(combined_n13, 97.5):.1f}] Ma" if is_en else f"IC 95%: [{np.percentile(combined_n13, 2.5):.1f}, {np.percentile(combined_n13, 97.5):.1f}]"
        
        ax4.axvline(means["t_n13"], color="red", lw=1.5, linestyle="-", label=m_lbl13)
        ax4.axvline(np.percentile(combined_n13, 2.5), color="gray", lw=1.2, linestyle="--", label=ci_lbl13)
        ax4.axvline(np.percentile(combined_n13, 97.5), color="gray", lw=1.2, linestyle="--")
        ax4.set_xlabel("Geological Time (Ma)" if is_en else "Tempo Geológico (Ma)")
        ax4.set_ylabel("Posterior Density" if is_en else "Densidade Posterior")
        ax4.set_title("D. Vellozia Speciation: V. peripherica vs V. tubiflora" if is_en else "D. Especiação Vellozia: V. peripherica vs V. tubiflora")
        ax4.legend(frameon=False, fontsize=8)
        ax4.grid(True, linestyle=":", alpha=0.6)
        
        plt.savefig(out_png, dpi=300, bbox_inches='tight')
        plt.savefig(out_pdf, bbox_inches='tight')
        plt.close()
        print(f"[INFO] Figura ({lang.upper()}) salva em: {out_png}")
        print(f"       PDF: {out_pdf}")
        
    render_plot(lang="pt")
    render_plot(lang="en")

if __name__ == "__main__":
    main()
