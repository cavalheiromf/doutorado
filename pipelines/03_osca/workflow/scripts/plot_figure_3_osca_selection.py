#!/usr/bin/env python3
"""Generate publication-ready Figure 3 from audited OSCA results."""

from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/osca_matplotlib")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


PROJECT = Path(__file__).resolve().parents[2]
FIGURES = PROJECT / "figures"
KAKS = PROJECT / "04_evolutionary_rates/results_pal2nal_yn00/aggregated_kaks_pal2nal_yn00.csv"
OSCA3_RELAX = PROJECT / "03_synteny/results/hyphy_osca3_only_20261026/relax_summary.tsv"

CLADE_COLORS = {
    "OSCA1": "#0072B2",
    "OSCA2": "#E69F00",
    "OSCA3": "#009E73",
    "OSCA4": "#CC79A7",
}


def clade_for_pair(name: str) -> str:
    for clade in CLADE_COLORS:
        if clade in name:
            return clade
    raise ValueError(f"Cannot assign OSCA clade to {name}")


def pair_label(name: str) -> str:
    if name == "VpOSCA2.4a_VpOSCA2.4b":
        return "Vp2.4a / Vp2.4b (paralog)"
    left, right = name.split("_")
    left = left.replace("VpOSCA", "")
    right = right.replace("VtOSCA", "")
    return f"OSCA{left}" if left == right else f"Vp{left} / Vt{right}"


def load_relax() -> pd.DataFrame:
    osca3 = pd.read_csv(OSCA3_RELAX, sep="\t")
    primary = osca3.loc[osca3["analysis"] == "gap20_sp1"].iloc[0]
    return pd.DataFrame(
        [
            ("Global", 0.706408557, 0.000337322, "#666666"),
            ("OSCA1", 0.926177965, 0.608049990, CLADE_COLORS["OSCA1"]),
            ("OSCA2", 0.819142659, 0.344631173, CLADE_COLORS["OSCA2"]),
            ("OSCA3", float(primary["K"]), float(primary["p_value"]), CLADE_COLORS["OSCA3"]),
        ],
        columns=["dataset", "K", "p_value", "color"],
    )


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    relax = load_relax()
    kaks = pd.read_csv(KAKS)
    kaks["clade"] = kaks["Pair_Name"].map(clade_for_pair)
    kaks["label"] = kaks["Pair_Name"].map(pair_label)
    kaks["paralog"] = kaks["Pair_Name"].eq("VpOSCA2.4a_VpOSCA2.4b")
    kaks = kaks.sort_values("Ka/Ks", ascending=False).reset_index(drop=True)

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 7.5,
            "axes.labelsize": 8.0,
            "axes.titlesize": 8.8,
            "xtick.labelsize": 7.0,
            "ytick.labelsize": 6.8,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )

    fig = plt.figure(figsize=(8.5, 4.8), dpi=300)
    grid = fig.add_gridspec(
        1,
        2,
        width_ratios=[0.90, 1.35],
        wspace=0.43,
        left=0.08,
        right=0.97,
        top=0.84,
        bottom=0.22,
    )
    ax_relax = fig.add_subplot(grid[0, 0])
    ax_kaks = fig.add_subplot(grid[0, 1])

    x = np.arange(len(relax))
    bars = ax_relax.bar(x, relax["K"], width=0.55, color=relax["color"], edgecolor="none", alpha=0.92)
    ax_relax.axhline(1.0, color="#666666", linestyle="--", linewidth=0.9)
    ax_relax.text(
        1.25,
        1.025,
        r"$K$ = 1.0 (equal selection intensity)",
        ha="left",
        va="bottom",
        fontsize=6.0,
        color="#555555",
        style="italic",
    )
    for bar, (_, row) in zip(bars, relax.iterrows()):
        significance = "**" if row["p_value"] < 0.01 else "ns"
        ax_relax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.03,
            f"{row['K']:.2f}\n({significance})",
            ha="center",
            va="bottom",
            fontsize=6.8,
            fontweight="bold",
        )
    ax_relax.set_xticks(x)
    ax_relax.set_xticklabels(relax["dataset"], fontweight="bold", fontsize=7.5)
    ax_relax.set_ylabel(r"Selection-intensity parameter ($K$)")
    ax_relax.set_ylim(0, 1.28)
    ax_relax.set_title("HyPhy RELAX: Vtub vs. Vper", loc="left", pad=10, fontweight="bold")
    ax_relax.text(-0.15, 1.08, "A", transform=ax_relax.transAxes, fontsize=11, fontweight="bold", va="top")
    ax_relax.text(
        0.50,
        -0.18,
        r"$K<1$: point estimate toward relaxation" + "\n" + "Inference requires significant LRT; ** p < 0.01; ns = not significant",
        transform=ax_relax.transAxes,
        ha="center",
        va="top",
        fontsize=5.5,
        color="#333333",
        bbox={"boxstyle": "round,pad=0.25", "facecolor": "#F7F7F7", "edgecolor": "#BBBBBB", "linewidth": 0.5},
    )

    y = np.arange(len(kaks))
    for index, row in kaks.iterrows():
        color = CLADE_COLORS[row["clade"]]
        value = float(row["Ka/Ks"])
        ax_kaks.plot([0, value], [index, index], color=color, linewidth=1.2, alpha=0.85)
        ax_kaks.plot(
            value,
            index,
            marker="D" if row["paralog"] else "o",
            markersize=5.0,
            markerfacecolor="white" if row["paralog"] else color,
            markeredgecolor=color,
            markeredgewidth=1.2,
            zorder=3,
        )
        ax_kaks.text(value + 0.02, index, f"{value:.3f}", va="center", ha="left", fontsize=6.0, color="#333333")
    mean_omega = kaks.loc[~kaks["paralog"], "Ka/Ks"].mean()
    ax_kaks.axvline(mean_omega, color="#D55E00", linestyle="--", linewidth=0.9)
    ax_kaks.text(mean_omega + 0.012, len(kaks) - 1.55, rf"Mean $\omega$ = {mean_omega:.3f}", color="#D55E00", fontsize=6.2, style="italic")
    ax_kaks.set_yticks(y)
    ax_kaks.set_yticklabels(kaks["label"])
    ax_kaks.invert_yaxis()
    ax_kaks.set_xlabel(r"Whole-gene ratio ($\omega=K_a/K_s$)")
    ax_kaks.set_xlim(0, 0.95)
    ax_kaks.set_title("Pairwise rates (PAL2NAL + YN00)", loc="left", pad=10, fontweight="bold")
    ax_kaks.text(-0.13, 1.08, "B", transform=ax_kaks.transAxes, fontsize=11, fontweight="bold", va="top")

    for axis in (ax_relax, ax_kaks):
        axis.spines["top"].set_visible(False)
        axis.spines["right"].set_visible(False)
        axis.tick_params(width=0.7)

    fig.suptitle(
        "Figure 3. Selection dynamics and pairwise evolutionary rates across OSCA clades",
        fontsize=10.5,
        fontweight="bold",
        x=0.08,
        y=0.965,
        ha="left",
    )
    png = FIGURES / "Figure_3_OSCA_Evolutionary_Rates_and_Selection.png"
    pdf = FIGURES / "Figure_3_OSCA_Evolutionary_Rates_and_Selection.pdf"
    fig.savefig(png, dpi=600, bbox_inches="tight", facecolor="white")
    fig.savefig(pdf, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(png)
    print(pdf)


if __name__ == "__main__":
    main()
