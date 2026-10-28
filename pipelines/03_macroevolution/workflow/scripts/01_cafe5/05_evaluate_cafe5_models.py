#!/usr/bin/env python3
"""
05_evaluate_cafe5_models.py

Avalia as réplicas de todas as etapas do CAFE5 (Etapas 1, 2 e 3):
  - Extrai o melhor -lnL, valores de lambda, alpha (Gamma) e epsilon (Error Model) de cada réplica.
  - Calcula AIC, Delta-AIC e Likelihood Ratio Tests (LRT) entre modelos aninhados:
      * Etapa 1: Base Sem Erro vs. Base Com Erro (-e) -> e copia o melhor Base_error_model.txt
        para runs/stage1_error_calibration/selected_error_model.txt.
      * Etapa 2: Base 1-lambda vs. Gamma k=2 vs. Gamma k=3.
      * Etapa 3: M1 (1-lambda) vs. M2 (2-lambda) vs. M3 (3-lambda Vellozia) vs. M4 (3-lambda Avoidant) vs. M5 (4-lambda).
  - Extrai a tabela consolidada de famílias gênicas significativamente expandidas ou contraídas (p < 0.05)
    em Vper (avoidant), Vtub (DT) e no ancestral de Vellozia.
"""

import argparse
import re
import shutil
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import chi2

BASE_DIR = Path(__file__).resolve().parents[3]
CAFE_DIR = BASE_DIR / "04_gene_families" / "cafe5"
RUNS_DIR = CAFE_DIR / "runs"
SUMMARY_DIR = CAFE_DIR / "summary"
M5_GAMMA_LABEL = "Gamma_k3_M5_4lambda_split_sisters"


def free_parameter_count(
    n_lambdas: int,
    estimate_alpha: bool = False,
    estimate_epsilon: bool = False,
    estimate_root_distribution: bool = True,
) -> int:
    """Conta apenas parâmetros efetivamente otimizados na execução.

    O modelo de erro é fixado após a Etapa 1, enquanto ``-p`` sem valor estima
    um parâmetro da distribuição Poisson na raiz em cada execução.
    """
    return (
        n_lambdas
        + int(estimate_alpha)
        + int(estimate_epsilon)
        + int(estimate_root_distribution)
    )


def get_model_specs() -> list[dict]:
    """Declara os modelos e os grupos nos quais o AIC é interpretado."""
    s1_dir = RUNS_DIR / "stage1_error_calibration"
    s2_dir = RUNS_DIR / "stage2_gamma_rates"
    s3_dir = RUNS_DIR / "stage3_branch_lambdas"
    s4_dir = RUNS_DIR / "stage4_gamma_branch_lambdas"

    return [
        {
            "path": s1_dir / "base_no_err",
            "label": "M1_1lambda_no_err",
            "n_lambdas": 1,
            "is_gamma": False,
            "estimate_alpha": False,
            "estimate_epsilon": False,
            "comparison_group": "error_model_calibration",
        },
        {
            "path": s1_dir / "base_with_err",
            "label": "M1_1lambda_with_err",
            "n_lambdas": 1,
            "is_gamma": False,
            "estimate_alpha": False,
            "estimate_epsilon": True,
            "comparison_group": "error_model_calibration",
        },
        {
            "path": s2_dir / "gamma_k2",
            "label": "Gamma_k2_1lambda",
            "n_lambdas": 1,
            "is_gamma": True,
            "estimate_alpha": True,
            "estimate_epsilon": False,
            "comparison_group": "gamma_category_sensitivity",
        },
        {
            "path": s2_dir / "gamma_k3",
            "label": "Gamma_k3_1lambda",
            "n_lambdas": 1,
            "is_gamma": True,
            "estimate_alpha": True,
            "estimate_epsilon": False,
            "comparison_group": "gamma_k3_branch_rates",
        },
        *[
            {
                "path": s3_dir / model,
                "label": model,
                "n_lambdas": n_lambdas,
                "is_gamma": False,
                "estimate_alpha": False,
                "estimate_epsilon": False,
                "comparison_group": "base_branch_rates",
            }
            for model, n_lambdas in [
                ("M2_2lambda_family", 2),
                ("M3_3lambda_vellozia_clade", 3),
                ("M4_3lambda_avoidant_shift", 3),
                ("M5_4lambda_split_sisters", 4),
            ]
        ],
        *[
            {
                "path": s4_dir / model,
                "label": f"Gamma_k3_{model}",
                "n_lambdas": n_lambdas,
                "is_gamma": True,
                "estimate_alpha": True,
                "estimate_epsilon": False,
                "comparison_group": "gamma_k3_branch_rates",
            }
            for model, n_lambdas in [
                ("M2_2lambda_family", 2),
                ("M3_3lambda_vellozia_clade", 3),
                ("M4_3lambda_avoidant_shift", 3),
                ("M5_4lambda_split_sisters", 4),
            ]
        ],
    ]


def parse_cafe_results_file(results_file: Path) -> dict:
    """Lê Base_results.txt ou Gamma_results.txt de uma réplica do CAFE5."""
    info = {
        "results_file": str(results_file),
        "neg_lnL": None,
        "lambdas": None,
        "alpha": None,
        "epsilon": None,
        "maximum_lambda": None,
        "converged": False,
    }
    if not results_file.exists():
        return info

    text = results_file.read_text(encoding="utf-8", errors="replace")

    m_lnl = re.search(r"Final (?:Likelihood \(-lnL\)|-lnL):\s*([0-9.]+)", text)
    if m_lnl:
        info["neg_lnL"] = float(m_lnl.group(1))
        info["converged"] = True

    m_lam = re.search(r"Lambda:\s*([^\n]+)", text)
    if m_lam:
        info["lambdas"] = m_lam.group(1).strip()

    m_alpha = re.search(r"Alpha:\s*([0-9.]+)", text)
    if m_alpha:
        info["alpha"] = float(m_alpha.group(1))

    m_eps = re.search(r"Epsilon:\s*([0-9.]+)", text)
    if m_eps:
        info["epsilon"] = float(m_eps.group(1))

    m_max = re.search(r"Maximum possible lambda for this topology:\s*([0-9.eE+-]+)", text)
    if m_max:
        info["maximum_lambda"] = float(m_max.group(1))

    # The compact results file rounds -lnL and alpha.  The adjacent run log
    # preserves full optimizer precision and is therefore preferred when it
    # exists (rep_4/Gamma_results.txt -> rep_4.log).
    run_log = results_file.parent.parent / f"{results_file.parent.name}.log"
    if run_log.exists():
        log_text = run_log.read_text(encoding="utf-8", errors="replace")
        final_scores = re.findall(r"Final -lnL:\s*([0-9.eE+-]+)", log_text)
        if final_scores:
            info["neg_lnL"] = float(final_scores[-1])
            info["converged"] = True
        best_matches = re.findall(r"Best matches are:\s*([^\n]+)", log_text)
        if best_matches and results_file.name.startswith("Gamma"):
            values = [float(value.strip()) for value in best_matches[-1].split(",")]
            if len(values) >= 2:
                info["lambdas"] = ",".join(str(value) for value in values[:-1])
                info["alpha"] = values[-1]
        max_values = re.findall(
            r"Maximum possible lambda for this topology:\s*([0-9.eE+-]+)", log_text
        )
        if max_values:
            info["maximum_lambda"] = float(max_values[-1])

    return info


def collect_model_replicates(model_dir: Path, model_label: str, n_params: int, is_gamma: bool = False) -> list:
    rows = []
    if not model_dir.exists():
        return rows

    res_filename = "Gamma_results.txt" if is_gamma else "Base_results.txt"
    for rep_dir in sorted(model_dir.glob("rep_*")):
        if not rep_dir.is_dir():
            continue
        res_path = rep_dir / res_filename
        parsed = parse_cafe_results_file(res_path)
        neg_lnl = parsed["neg_lnL"]
        aic = (2 * n_params + 2 * neg_lnl) if neg_lnl is not None else None
        rows.append({
            "model": model_label,
            "replicate": rep_dir.name,
            "rep_dir": str(rep_dir),
            "k_params": n_params,
            "neg_lnL": neg_lnl,
            "lnL": -neg_lnl if neg_lnl is not None else None,
            "AIC": aic,
            "lambdas": parsed["lambdas"],
            "alpha": parsed["alpha"],
            "epsilon": parsed["epsilon"],
            "maximum_lambda": parsed["maximum_lambda"],
            "converged": parsed["converged"],
        })
    return rows


def lrt_test(lnl_null: float, lnl_alt: float, df_diff: int) -> tuple:
    stat = max(0.0, 2.0 * (lnl_alt - lnl_null))
    pval = chi2.sf(stat, df_diff)
    return stat, pval


def parse_lambda_vector(value) -> list[float]:
    """Return the numerical lambda vector stored by CAFE5."""
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return []
    return [float(part.strip()) for part in str(value).split(",") if part.strip()]


def summarize_m5_convergence(
    replicate_table: pd.DataFrame, near_optimal_delta: float = 0.1
) -> pd.DataFrame:
    """Summarize convergence of the Gamma k=3 M5 multistart search.

    For the M5 lambda tree, rate classes 3 and 4 correspond to Vtub and
    Vper, respectively.  Runs within 0.1 -lnL unit of the best solution are
    retained as near-optimal sensitivity replicates.
    """
    columns = [
        "model", "replicate", "rep_dir", "neg_lnL", "delta_neg_lnL",
        "near_optimal", "selected_primary", "lambda_background",
        "lambda_velloziaceae", "lambda_Vtub", "lambda_Vper",
        "Vper_to_Vtub_ratio", "alpha", "maximum_lambda",
        "Vper_at_lambda_boundary",
    ]
    if replicate_table.empty:
        return pd.DataFrame(columns=columns)

    mask = (replicate_table["model"] == M5_GAMMA_LABEL) & replicate_table["converged"].fillna(False)
    result = replicate_table.loc[mask].copy().sort_values("neg_lnL").reset_index(drop=True)
    if result.empty:
        return pd.DataFrame(columns=columns)

    result["delta_neg_lnL"] = result["neg_lnL"] - result["neg_lnL"].min()
    result["near_optimal"] = result["delta_neg_lnL"] <= near_optimal_delta
    result["selected_primary"] = False
    result.loc[0, "selected_primary"] = True

    parsed = result["lambdas"].map(parse_lambda_vector)
    for index, name in enumerate(
        ["lambda_background", "lambda_velloziaceae", "lambda_Vtub", "lambda_Vper"]
    ):
        result[name] = parsed.map(lambda values: values[index] if len(values) > index else np.nan)
    result["Vper_to_Vtub_ratio"] = result["lambda_Vper"] / result["lambda_Vtub"]
    if "maximum_lambda" not in result:
        result["maximum_lambda"] = np.nan
    result["Vper_at_lambda_boundary"] = np.isclose(
        result["lambda_Vper"], result["maximum_lambda"], rtol=0, atol=1e-8
    )
    return result[columns]


def select_stage1_error_model():
    s1_dir = RUNS_DIR / "stage1_error_calibration"
    rows = []
    rows.extend(collect_model_replicates(s1_dir / "base_no_err", "M1_Base_NoErr", n_params=1, is_gamma=False))
    rows.extend(collect_model_replicates(s1_dir / "base_with_err", "M1_Base_WithErr", n_params=2, is_gamma=False))

    df = pd.DataFrame(rows)
    if df.empty or df["neg_lnL"].isna().all():
        print("[AVISO] Nenhuma réplica concluída encontrada na Etapa 1.")
        return None

    SUMMARY_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(SUMMARY_DIR / "stage1_replicates_summary.tsv", sep="\t", index=False)

    df_err = df[(df["model"] == "M1_Base_WithErr") & (df["converged"])].sort_values("neg_lnL")
    if not df_err.empty:
        best_rep = Path(df_err.iloc[0]["rep_dir"])
        err_src = best_rep / "Base_error_model.txt"
        err_dst = s1_dir / "selected_error_model.txt"
        if err_src.exists():
            shutil.copy2(err_src, err_dst)
            print(f"[INFO] Melhor modelo de erro selecionado ({best_rep.name}, -lnL={df_err.iloc[0]['neg_lnL']:.2f}) -> {err_dst}")
    return df


def evaluate_all_models():
    all_rows = []
    for spec in get_model_specs():
        n_params = free_parameter_count(
            n_lambdas=spec["n_lambdas"],
            estimate_alpha=spec["estimate_alpha"],
            estimate_epsilon=spec["estimate_epsilon"],
            estimate_root_distribution=True,
        )
        rows = collect_model_replicates(
            spec["path"],
            spec["label"],
            n_params=n_params,
            is_gamma=spec["is_gamma"],
        )
        for row in rows:
            row["comparison_group"] = spec["comparison_group"]
            row["n_lambdas"] = spec["n_lambdas"]
            row["alpha_estimated"] = spec["estimate_alpha"]
            row["epsilon_estimated"] = spec["estimate_epsilon"]
        all_rows.extend(rows)

    df_all = pd.DataFrame(all_rows)
    if df_all.empty:
        print("[AVISO] Nenhum resultado encontrado.")
        return

    SUMMARY_DIR.mkdir(parents=True, exist_ok=True)
    df_all.to_csv(SUMMARY_DIR / "all_cafe5_replicates.tsv", sep="\t", index=False)

    m5_convergence = summarize_m5_convergence(df_all)
    m5_convergence.to_csv(
        SUMMARY_DIR / "M5_gamma_convergence_summary.tsv", sep="\t", index=False
    )

    # Selecionar a melhor réplica por modelo
    df_valid = df_all[df_all["converged"]].copy()
    if df_valid.empty:
        print("[AVISO] Nenhuma réplica convergiu ainda.")
        return

    best_per_model = (
        df_valid.sort_values("neg_lnL")
        .groupby("model", as_index=False)
        .first()
    )
    group_min = best_per_model.groupby("comparison_group")["AIC"].transform("min")
    best_per_model["Delta_AIC"] = best_per_model["AIC"] - group_min
    relative_likelihood = np.exp(-0.5 * best_per_model["Delta_AIC"])
    best_per_model["Akaike_weight"] = relative_likelihood / relative_likelihood.groupby(best_per_model["comparison_group"]).transform("sum")
    best_per_model = best_per_model.sort_values(["comparison_group", "AIC"])
    best_per_model.to_csv(SUMMARY_DIR / "best_models_comparison.tsv", sep="\t", index=False)
    print("\n=== Comparação dos Melhores Modelos (Delta AIC dentro de cada grupo) ===")
    print(best_per_model[["comparison_group", "model", "replicate", "k_params", "neg_lnL", "AIC", "Delta_AIC", "Akaike_weight", "lambdas", "alpha"]].to_string(index=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", type=int, choices=[1, 2, 3], help="Avaliar etapa específica (1 seleciona o Error Model)")
    args = parser.parse_args()

    if args.stage == 1:
        select_stage1_error_model()
    else:
        select_stage1_error_model()
        evaluate_all_models()


if __name__ == "__main__":
    main()

