#!/usr/bin/env python3
"""Create thesis-ready summary figures for the calibrated CAFE5 analyses."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import FancyBboxPatch
from scipy.stats import gamma


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "04_gene_families"
SUMMARY = DATA_DIR / "summary" / "all_models_summary.tsv"
OUT_DIR = DATA_DIR / "figures"

COLORS = {
    "01_base_noerror": "#999999",
    "02_base_error": "#56B4E9",
    "03_gamma_k2": "#009E73",
    "04_gamma_k3": "#E69F00",
    "05_gamma_k4_sensitivity": "#CC79A7",
}

LABELS = {
    "01_base_noerror": "Base",
    "02_base_error": "Base + error",
    "03_gamma_k2": r"Gamma $k=2$",
    "04_gamma_k3": r"Gamma $k=3$",
    "05_gamma_k4_sensitivity": r"Gamma $k=4$",
}


def set_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8,
            "axes.labelsize": 8,
            "axes.titlesize": 9,
            "xtick.labelsize": 7,
            "ytick.labelsize": 7,
            "legend.fontsize": 7,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "savefig.bbox": "tight",
            "pdf.fonttype": 42,
            "svg.fonttype": "none",
        }
    )


def save_all(fig: plt.Figure, stem: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_DIR / f"{stem}.png", dpi=400, facecolor="white")
    fig.savefig(OUT_DIR / f"{stem}.pdf", facecolor="white")
    fig.savefig(OUT_DIR / f"{stem}.svg", facecolor="white")


def workflow_figure() -> None:
    fig, ax = plt.subplots(figsize=(7.2, 2.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    boxes = [
        (0.01, 0.31, 0.16, 0.43, "OrthoFinder\n17,750 families", "#E6F2F8"),
        (0.21, 0.31, 0.16, 0.43, "Copy-number filter\n<100 copies\n17,735 families", "#E8F5E9"),
        (0.41, 0.31, 0.16, 0.43, "CAFE5 root filter\n12,276 families", "#FFF3E0"),
        (0.61, 0.31, 0.16, 0.43, "Replicated models\nBase; Gamma\n$k=2,3,4$", "#F3E5F5"),
        (0.81, 0.31, 0.18, 0.43, "Genome-wide BH FDR\n$k=2$ primary\n188-family core", "#FFF8E1"),
    ]
    for x, y, w, h, text, color in boxes:
        patch = FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.015,rounding_size=0.02",
            facecolor=color,
            edgecolor="#333333",
            linewidth=0.8,
        )
        ax.add_patch(patch)
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", linespacing=1.35)
    for x in [0.18, 0.38, 0.58, 0.78]:
        ax.annotate(
            "",
            xy=(x + 0.025, 0.525),
            xytext=(x - 0.005, 0.525),
            arrowprops={"arrowstyle": "-|>", "lw": 1.0, "color": "#333333"},
        )
    ax.text(
        0.5,
        0.91,
        "Gene-family evolution workflow and decision path",
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold",
    )
    ax.text(
        0.5,
        0.10,
        "Time-calibrated ultrametric tree (Ma) and a fixed global count-error model were used in all Gamma analyses.",
        ha="center",
        va="center",
        color="#444444",
        fontsize=7.5,
    )
    save_all(fig, "cafe5_workflow")
    plt.close(fig)


def gamma_midpoint_rates(k: int, lam: float, alpha: float) -> np.ndarray:
    """Return CAFE-style midpoint-quantile multipliers rescaled to mean one."""
    distribution = gamma(a=alpha, scale=1 / alpha)
    multipliers = np.asarray([distribution.ppf((i + 0.5) / k) for i in range(k)])
    multipliers /= multipliers.mean()
    return lam * multipliers


def diagnostics_figure() -> None:
    data = pd.read_csv(SUMMARY, sep="\t")
    data["valid"] = ~(
        (data["model"] == "04_gamma_k3") & (data["replicate"] == "rep02")
    )
    order = list(LABELS)
    xpos = {model: i for i, model in enumerate(order)}

    fig, axes = plt.subplots(2, 2, figsize=(7.2, 5.7))
    rng = np.random.default_rng(20260903)

    for model in order:
        subset = data[(data["model"] == model) & data["valid"]]
        jitter = rng.uniform(-0.07, 0.07, len(subset))
        x = xpos[model] + jitter
        axes[0, 0].scatter(x, subset["score_lnL"], s=27, color=COLORS[model], edgecolor="white", linewidth=0.5)
        axes[0, 1].scatter(x, subset["lambda"], s=27, color=COLORS[model], edgecolor="white", linewidth=0.5)
        axes[1, 0].scatter(x, subset["FDR_q_le_005"], s=27, color=COLORS[model], edgecolor="white", linewidth=0.5)

    bad = data[(data["model"] == "04_gamma_k3") & ~data["valid"]].iloc[0]
    axes[0, 0].scatter(xpos["04_gamma_k3"], 112150, marker="x", s=42, color="#D55E00", linewidth=1.4, clip_on=False)
    axes[0, 0].annotate(
        r"$k=3$ rep02: 130,849.9 (clipped)",
        xy=(xpos["04_gamma_k3"], 112150),
        xytext=(1.65, 112050),
        arrowprops={"arrowstyle": "-", "lw": 0.7, "color": "#D55E00"},
        color="#D55E00",
        fontsize=7,
    )
    axes[0, 1].scatter(xpos["04_gamma_k3"], bad["lambda"], marker="x", s=42, color="#D55E00", linewidth=1.4)

    axes[0, 0].set_ylabel(r"Negative log-likelihood ($-\ln L$)")
    axes[0, 0].set_ylim(106600, 112250)
    axes[0, 0].set_title("Model fit across valid replicates")
    axes[0, 1].set_ylabel(r"Estimated turnover rate, $\lambda$ (gene$^{-1}$ Ma$^{-1}$)")
    axes[0, 1].set_title("Parameter convergence")
    axes[1, 0].set_ylabel(r"Families with BH FDR $q\leq0.05$")
    axes[1, 0].set_title("Finite-simulation variation in family-level tests")

    for ax in [axes[0, 0], axes[0, 1], axes[1, 0]]:
        ax.set_xticks(range(len(order)), [LABELS[m] for m in order], rotation=25, ha="right")
        ax.grid(axis="y", color="#DDDDDD", linewidth=0.5, alpha=0.8)

    max_lambda = 0.0072210403786136
    rate_models = [
        ("03_gamma_k2", 2),
        ("04_gamma_k3", 3),
        ("05_gamma_k4_sensitivity", 4),
    ]
    for model, k in rate_models:
        subset = data[(data["model"] == model) & data["valid"]]
        lam = subset["lambda"].mean()
        alpha = subset["alpha"].mean()
        rates = gamma_midpoint_rates(k, lam, alpha) / max_lambda * 100
        axes[1, 1].plot(
            np.arange(1, k + 1),
            rates,
            marker="o",
            markersize=4,
            linewidth=1.2,
            color=COLORS[model],
            label=LABELS[model],
        )
    axes[1, 1].axhline(100, color="#333333", linestyle="--", linewidth=0.9, label=r"Topological $\lambda_{max}$")
    axes[1, 1].set_xlabel("Discrete Gamma rate category")
    axes[1, 1].set_ylabel(r"Effective rate relative to $\lambda_{max}$ (%)")
    axes[1, 1].set_xticks([1, 2, 3, 4])
    axes[1, 1].set_ylim(0, 106)
    axes[1, 1].set_title("Approach to the topological rate ceiling")
    axes[1, 1].grid(axis="y", color="#DDDDDD", linewidth=0.5, alpha=0.8)
    axes[1, 1].legend(frameon=False, loc="upper left")

    for label, ax in zip("ABCD", axes.flat):
        ax.text(-0.13, 1.06, label, transform=ax.transAxes, fontsize=10, fontweight="bold", va="top")

    fig.suptitle("CAFE5 model diagnostics", fontsize=11, fontweight="bold", y=0.995)
    fig.tight_layout(rect=(0, 0, 1, 0.97), h_pad=2.0, w_pad=1.7)
    save_all(fig, "cafe5_model_diagnostics")
    plt.close(fig)


def main() -> None:
    set_style()
    workflow_figure()
    diagnostics_figure()


if __name__ == "__main__":
    main()
