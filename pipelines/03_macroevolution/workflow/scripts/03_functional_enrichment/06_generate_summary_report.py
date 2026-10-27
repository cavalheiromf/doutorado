#!/usr/bin/env python3
"""Summarize the current 6-taxa functional enrichment outputs without Tier A nomenclature."""
from pathlib import Path
from datetime import date
import pandas as pd
import os


def main():
    macro = Path(os.environ.get("FAMILY_MACRO_DIR", str(Path(__file__).resolve().parents[2])))
    base = Path(os.environ.get("FAMILY_ENRICHMENT_DIR", str(macro / "04_gene_families/functional_enrichment")))
    master = pd.read_csv(
        os.environ.get(
            "FAMILY_MASTER_TABLE",
            str(macro / "04_gene_families/comparative_axes/comparative_families_master_table_v2.tsv"),
        ),
        sep="\t",
    ).set_index("FamilyID")
    ann = pd.read_csv(base / "results/orthogroup_functional_annotations.tsv", sep="\t").set_index("FamilyID")
    results = pd.read_csv(base / "results/enrichment_results_all.tsv", sep="\t")
    cov = pd.read_csv(base / "intermediate/covariate_balance_qc.tsv", sep="\t")

    vper_exp_ids = master.index[master["BranchSig_Exp_Vper"].eq(True)]
    vper_exp = ann.reindex(vper_exp_ids)

    lines = [
        "# Resultados de anotação e enriquecimento funcional (6 Monocotiledôneas — Sem `Ath` no CAFE5)",
        "",
        f"Atualização: {date.today().isoformat()}. Fontes: `comparative_families_master_table_v2.tsv`, anotações locais (`TAIR10`/GO/KEGG) e resultados recalculados do pipeline. A unidade de análise é a família gênica (ortogrupo).",
        "",
        f"O universo analítico na raiz das 6 monocotiledôneas contém **{len(master)} famílias gênicas**, das quais **{len(vper_exp_ids)} famílias expandiram significativamente no ramo de *V. peripherica* (`BranchSig_Exp_Vper_Avoidant`, $p_{{\\text{{branch}}}} < 0.05$)**.",
        "",
        "## Cobertura de anotação",
        "",
        f"| Categoria | Universo anotado ({len(master):,} famílias) | Expansões *V. peripherica* anotadas ({len(vper_exp_ids)} famílias) | Cobertura nas expansões de *V. peripherica* |".replace(",", "."),
        "|---|---:|---:|---:|",
    ]
    for label, col in [
        ("GO BP", "GO_BP_Propagated"),
        ("GO MF", "GO_MF_Propagated"),
        ("GO CC", "GO_CC_Propagated"),
        ("KEGG", "KEGG_Pathways"),
    ]:
        universe = int(ann[col].fillna("").ne("").sum())
        count = int(vper_exp[col].fillna("").ne("").sum())
        coverage = f"{100 * count / len(vper_exp):.2f}%" if len(vper_exp) else "not_assessed"
        lines.append(f"| {label} | {universe} | {count} | {coverage} |")

    lines += [
        "",
        "## Retenção por cenário de sensibilidade",
        "",
        "| Cenário | Famílias no Universo | Expansões *V. peripherica* (`BranchSig_Exp_Vper`) |",
        "|---|---:|---:|",
    ]
    scenario_ids = [
        "scenario_1_all_families",
        "scenario_2_exclude_transposon_high_asymmetry",
        "scenario_3_nuclear_only",
        "scenario_4_go_non_iea",
    ]
    masks = [
        pd.Series(True, index=master.index),
        ~master.Flag_Transposon & ~master.Flag_High_Copy_Asymmetry,
        ~master.Flag_Organellar,
        ann.Has_Non_IEA.reindex(master.index).fillna(False),
    ]
    for name, mask in zip(scenario_ids, masks):
        n = int(mask.sum())
        nt = int((mask & master["BranchSig_Exp_Vper"].eq(True)).sum())
        lines.append(f"| {name} | {n} | {nt} |")

    lines += [
        "",
        "## Denominadores efetivos de `BranchSig_Exp_Vper_Avoidant`",
        "",
        "| Cenário | Categoria | Foreground | Background | Universo |",
        "|---|---|---:|---:|---:|",
    ]
    vper_res = results[results.Contrast_ID.eq("BranchSig_Exp_Vper_Avoidant")]
    for row in (
        vper_res[["Scenario", "Ontology_Category", "FG_Total", "BG_Total", "Universe_Total"]]
        .drop_duplicates()
        .itertuples(index=False)
    ):
        lines.append("| " + " | ".join(map(str, row)) + " |")

    primary = results[results.Scenario.eq(scenario_ids[0]) & results.Is_Primary_Inferential]
    lines += [
        "",
        "## Classificação dos testes primários",
        "",
        f"Foram executados {len(primary)} testes primários no cenário completo.",
        "",
        "| Contraste | Classe de evidência | Número de termos |",
        "|---|---|---:|",
    ]
    for (contrast, cls), n in primary.groupby(["Contrast_ID", "Evidence_Class"]).size().items():
        lines.append(f"| {contrast} | {cls} | {n} |")

    lines += [
        "",
        "## Termos enriquecidos (`q_value < 0.05` e `p_strat < 0.05`)",
        "",
        "| Contraste | Categoria | Classe | Termo | Famílias focais | OR Condicional | q local | q global | p estratificado |",
        "|---|---|---|---|---:|---:|---:|---:|---:|",
    ]
    robust = primary[
        primary.Evidence_Class.isin(["Confirmatory", "Suggestive", "Suggestive_Imbalanced_Opportunity"])
    ].sort_values(["Contrast_ID", "q_value"])
    for row in robust.itertuples(index=False):
        name = str(row.Term_Name).replace("|", "/")
        lines.append(
            f"| {row.Contrast_ID} | {row.Ontology_Category} | {row.Evidence_Class} | {row.Term_ID}: {name} | {row.FG_Count}/{row.FG_Total} | {row.Conditional_OR:.2f} | {row.q_value:.3g} | {row.q_global_primary:.3g} | {row.p_strat:.4f} |"
        )
    if robust.empty:
        lines.append("| — | — | — | Nenhum termo nesta classe | — | — | — | — | — |")

    lines += [
        "",
        "## Balanço de covariáveis e rastreabilidade",
        "",
        f"A tabela de balanço (`covariate_balance_qc.tsv`) contém {len(cov)} registros auditados.",
        "",
    ]
    (base / "functional_enrichment_summary.md").write_text("\n".join(lines))
    print(
        f"Report generated: BranchSig_Exp_Vper={len(vper_exp_ids)}, primary tests={len(primary)}, robust terms={len(robust)}"
    )


if __name__ == "__main__":
    main()
