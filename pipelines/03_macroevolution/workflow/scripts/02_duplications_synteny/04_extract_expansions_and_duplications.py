#!/usr/bin/env python3
"""
06_extract_expansions_and_duplications.py

Cruza os resultados de expansão/contração significativa (p < 0.05) do CAFE5 nos ramos:
  - Vper (Vellozia peripherica = Avoidant / sempre-verde)
  - Vtub (Vellozia tubiflora = DT / tolerante à dessecação)
  - Nó ancestral do gênero Vellozia (<Vper,Vtub>)
com os modos de duplicação gênica (Singleton, Dispersed, Proximal, Tandem, WGD/Segmental)
e testa estatisticamente (Teste Exato de Fisher) se as famílias expandidas em Vper (avoidant)
e Vtub (DT) são enriquecidas em modos específicos de duplicação (ex: Tandem e Proximal).
"""

import argparse
from pathlib import Path
import pandas as pd
from scipy.stats import fisher_exact

BASE_DIR = Path("/home/mfcaval/github/doutorado/chapter_macroevolution_review")
CAFE_SUMMARY_DIR = BASE_DIR / "04_gene_families" / "cafe5" / "summary"


def find_node_col(columns, prefix: str) -> str:
    """Encontra a coluna correspondente ao táxon no formato 'Vper<id>' gerado pelo CAFE5."""
    matches = [c for c in columns if c.startswith(f"{prefix}<") or c == prefix]
    if not matches:
        raise KeyError(f"Coluna para {prefix} não encontrada entre: {list(columns)}")
    return matches[0]


def extract_branch_changes(cafe_run_dir: Path, model_prefix: str = "Base", pval_cutoff: float = 0.05) -> pd.DataFrame:
    """
    Lê <model_prefix>_change.tab e <model_prefix>_branch_probabilities.tab de uma execução do CAFE5
    e classifica cada ortogrupo em Vper (avoidant) e Vtub (DT).
    """
    change_file = cafe_run_dir / f"{model_prefix}_change.tab"
    prob_file = cafe_run_dir / f"{model_prefix}_branch_probabilities.tab"

    if not change_file.exists() or not prob_file.exists():
        raise FileNotFoundError(f"Arquivos {change_file.name} ou {prob_file.name} ausentes em {cafe_run_dir}")

    df_chg = pd.read_csv(change_file, sep="\t")
    df_prob = pd.read_csv(prob_file, sep="\t")

    df_chg = df_chg.rename(columns={df_chg.columns[0]: "FamilyID"})
    df_prob = df_prob.rename(columns={df_prob.columns[0]: "FamilyID"})

    vper_col = find_node_col(df_chg.columns, "Vper")
    vtub_col = find_node_col(df_chg.columns, "Vtub")

    merged_tab = pd.merge(
        df_chg[["FamilyID", vper_col, vtub_col]],
        df_prob[["FamilyID", vper_col, vtub_col]],
        on="FamilyID",
        how="left",
        suffixes=("_chg", "_prob"),
    )

    df = pd.DataFrame({
        "FamilyID": merged_tab["FamilyID"],
        "Delta_Vper": pd.to_numeric(merged_tab[f"{vper_col}_chg"], errors="coerce"),
        "Pval_Vper": pd.to_numeric(merged_tab[f"{vper_col}_prob"], errors="coerce").fillna(1.0),
        "Delta_Vtub": pd.to_numeric(merged_tab[f"{vtub_col}_chg"], errors="coerce"),
        "Pval_Vtub": pd.to_numeric(merged_tab[f"{vtub_col}_prob"], errors="coerce").fillna(1.0),
    })

    def classify_branch(delta, pval):
        if pd.isna(delta) or pd.isna(pval):
            return "Unchanged"
        if pval < pval_cutoff:
            if delta > 0:
                return "Expanded_Sig"
            elif delta < 0:
                return "Contracted_Sig"
        return "Unchanged"

    df["Status_Vper_Avoidant"] = [classify_branch(d, p) for d, p in zip(df["Delta_Vper"], df["Pval_Vper"])]
    df["Status_Vtub_DT"] = [classify_branch(d, p) for d, p in zip(df["Delta_Vtub"], df["Pval_Vtub"])]

    return df


def test_duplication_mode_enrichment(df_branch: pd.DataFrame, dup_gene_table: Path, species_tag: str, status_col: str) -> pd.DataFrame:
    """
    Cruza os genes classificados por modo de duplicação (Singleton, Dispersed, Proximal, Tandem, WGD/Segmental)
    com o status da família no CAFE5 (Expanded_Sig vs. resto do genoma avaliado pelo CAFE5) usando Teste Exato de Fisher.
    Aceita colunas ['gene_id', 'orthogroup', 'dup_type'] ou ['GeneID', 'FamilyID', 'DuplicationMode'].
    """
    df_dup = pd.read_csv(dup_gene_table, sep="\t")
    df_dup = df_dup.rename(columns={
        "orthogroup": "FamilyID",
        "dup_type": "DuplicationMode",
        "gene_id": "GeneID",
    })
    merged = df_dup.merge(df_branch[["FamilyID", status_col]], on="FamilyID", how="inner")
    merged["is_expanded"] = merged[status_col] == "Expanded_Sig"

    modes = ["Tandem", "Proximal", "WGD/Segmental", "Dispersed", "Singleton"]
    results = []

    for mode in modes:
        in_mode = merged["DuplicationMode"] == mode
        a = int((merged["is_expanded"] & in_mode).sum())
        b = int((merged["is_expanded"] & ~in_mode).sum())
        c = int((~merged["is_expanded"] & in_mode).sum())
        d = int((~merged["is_expanded"] & ~in_mode).sum())

        if (a + b) > 0 and (c + d) > 0:
            odds_ratio, pval = fisher_exact([[a, b], [c, d]], alternative="two-sided")
        else:
            odds_ratio, pval = float("nan"), float("nan")

        results.append({
            "Species": species_tag,
            "DuplicationMode": mode,
            "Genes_in_Expanded_Families": a,
            "Other_Genes_in_Expanded_Families": b,
            "Genes_in_Background_Families": c,
            "Other_Genes_in_Background_Families": d,
            "Pct_in_Expanded": (100.0 * a / (a + b)) if (a + b) > 0 else 0.0,
            "Pct_in_Background": (100.0 * c / (c + d)) if (c + d) > 0 else 0.0,
            "OddsRatio": odds_ratio,
            "Fisher_Pval": pval,
        })

    return pd.DataFrame(results)


def main():
    default_dup_dir = BASE_DIR / "04_gene_families" / "synteny" / "duplications"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cafe-run-dir", type=Path, required=True, help="Diretório da réplica vencedora do CAFE5")
    parser.add_argument("--model-prefix", type=str, default="Base", choices=["Base", "Gamma"], help="Prefixo dos arquivos do CAFE5")
    parser.add_argument("--pval", type=float, default=0.05, help="Limiar de p-valor específico por ramo")
    parser.add_argument("--vper-dup-table", type=Path, default=default_dup_dir / "vper_gene_duplications_annotated.tsv")
    parser.add_argument("--vtub-dup-table", type=Path, default=default_dup_dir / "vtub_gene_duplications_annotated.tsv")
    args = parser.parse_args()

    CAFE_SUMMARY_DIR.mkdir(parents=True, exist_ok=True)
    df_changes = extract_branch_changes(args.cafe_run_dir, args.model_prefix, args.pval)

    out_changes = CAFE_SUMMARY_DIR / f"branch_expansions_contractions_{args.model_prefix}_Vper_vs_Vtub.tsv"
    df_changes.to_csv(out_changes, sep="\t", index=False)

    print(f"[INFO] Tabela de mudanças por ramo salva em: {out_changes}")
    print("\n=== Resumo Vper (Avoidant) — p_branch < 0.05 ===")
    print(df_changes["Status_Vper_Avoidant"].value_counts().to_string())
    print("\n=== Resumo Vtub (DT) — p_branch < 0.05 ===")
    print(df_changes["Status_Vtub_DT"].value_counts().to_string())

    if args.vper_dup_table and args.vper_dup_table.exists():
        df_vper_enrich = test_duplication_mode_enrichment(df_changes, args.vper_dup_table, "Vper_Avoidant", "Status_Vper_Avoidant")
        out_vper = CAFE_SUMMARY_DIR / f"duplication_enrichment_{args.model_prefix}_Vper_Avoidant.tsv"
        df_vper_enrich.to_csv(out_vper, sep="\t", index=False)
        print(f"\n=== Enriquecimento de Modos de Duplicação em Famílias Expandidas — Vper (Avoidant) ===")
        print(df_vper_enrich[["DuplicationMode", "Genes_in_Expanded_Families", "Pct_in_Expanded", "Pct_in_Background", "OddsRatio", "Fisher_Pval"]].to_string(index=False))

    if args.vtub_dup_table and args.vtub_dup_table.exists():
        df_vtub_enrich = test_duplication_mode_enrichment(df_changes, args.vtub_dup_table, "Vtub_DT", "Status_Vtub_DT")
        out_vtub = CAFE_SUMMARY_DIR / f"duplication_enrichment_{args.model_prefix}_Vtub_DT.tsv"
        df_vtub_enrich.to_csv(out_vtub, sep="\t", index=False)
        print(f"\n=== Enriquecimento de Modos de Duplicação em Famílias Expandidas — Vtub (DT) ===")
        print(df_vtub_enrich[["DuplicationMode", "Genes_in_Expanded_Families", "Pct_in_Expanded", "Pct_in_Background", "OddsRatio", "Fisher_Pval"]].to_string(index=False))


if __name__ == "__main__":
    main()

