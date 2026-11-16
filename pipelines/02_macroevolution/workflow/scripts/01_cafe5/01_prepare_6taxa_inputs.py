#!/usr/bin/env python3
"""
01_prepare_6taxa_inputs.py

Prepara os insumos de 6 táxons (Monocotiledôneas: Dala, Ptec, Abra, Xvis, Vper, Vtub)
para o CAFE5 a partir da árvore calibrada do MCMCTree e da matriz Orthogroups.GeneCount.tsv.

Decisões metodológicas:
1. Remove Arabidopsis thaliana (Ath) da árvore ultramétrica e da tabela de contagem para evitar
   distorção das taxas birth-death (lambda) pelo ramo longo Eudicot-Monocot (~138.5 Ma).
2. Preserva estritamente as idades posteriores do MCMCTree nos nós internos das monocotiledôneas
   (Raiz Monocots = 121.8979 Ma; Pandanales = 101.2579 Ma; Velloziaceae = 78.2090 Ma;
   Core Velloziaceae = 31.9147 Ma; Vellozia Vper-Vtub = 9.7362 Ma).
3. Separa famílias com >= 100 cópias em pelo menos uma espécie (cafe_family_input_large_6taxa.tsv)
   das famílias padrão (< 100 cópias, cafe_family_input_6taxa.tsv) para evitar falhas numéricas
   na matriz de transição durante a estimativa de lambda, permitindo avaliá-las posteriormente
   com o lambda fixado.
4. Gera os arquivos de topologia de taxas (--lambda_tree / -y) para os modelos M2, M3, M4 e M5.
"""

import glob
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[3]
ORTHO_DIR = BASE_DIR / "01_orthology"
TREE_OUT_DIR = BASE_DIR / "03_dating" / "final_trees"
CAFE_IN_DIR = BASE_DIR / "04_gene_families" / "cafe5" / "input"
LAMBDA_TREES_DIR = BASE_DIR / "04_gene_families" / "cafe5" / "lambda_trees"

SPECIES_COLS = {
    "Dala": "Dala.pep",
    "Ptec": "Ptec.pep",
    "Abra": "Abra.pep",
    "Xvis": "Xvis.pep",
    "Vper": "Vper.pep",
    "Vtub": "Vtub.pep",
}

MAX_COUNT_EXCLUSIVE = 100

# Árvore ultramétrica calibrada de 6 táxons (unidades em Ma)
ULTRAMETRIC_TREE_6TAXA = (
    "(((((Vper:9.7362,Vtub:9.7362):22.1785,Xvis:31.9147):46.2943,"
    "Abra:78.2090):23.0490,Ptec:101.2579):20.6399,Dala:121.8979);"
)

# Árvores de hipóteses para múltiplos lambdas (-y)
# Vper = Avoidant (sempre-verde) | Vtub, Xvis, Abra = DT (tolerantes à dessecação)
LAMBDA_TREES = {
    "M2_2lambda_family.tre": (
        "(((((Vper:2,Vtub:2):2,Xvis:2):2,Abra:2):2,Ptec:1):1,Dala:1);"
    ),
    "M3_3lambda_vellozia_clade.tre": (
        "(((((Vper:3,Vtub:3):3,Xvis:2):2,Abra:2):2,Ptec:1):1,Dala:1);"
    ),
    "M4_3lambda_avoidant_shift.tre": (
        "(((((Vper:3,Vtub:2):2,Xvis:2):2,Abra:2):2,Ptec:1):1,Dala:1);"
    ),
    "M5_4lambda_split_sisters.tre": (
        "(((((Vper:4,Vtub:3):2,Xvis:2):2,Abra:2):2,Ptec:1):1,Dala:1);"
    ),
}


def main():
    TREE_OUT_DIR.mkdir(parents=True, exist_ok=True)
    CAFE_IN_DIR.mkdir(parents=True, exist_ok=True)
    LAMBDA_TREES_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Salvar árvore ultramétrica de 6 táxons
    tree_path = TREE_OUT_DIR / "velloziaceae_6taxa_ultrametric.tre"
    tree_path.write_text(ULTRAMETRIC_TREE_6TAXA + "\n", encoding="utf-8")
    print(f"[INFO] Árvore ultramétrica (6 táxons) salva em: {tree_path}")

    # 2. Salvar árvores de hipóteses de múltiplos lambdas
    for fname, ltree in LAMBDA_TREES.items():
        lpath = LAMBDA_TREES_DIR / fname
        lpath.write_text(ltree + "\n", encoding="utf-8")
        print(f"[INFO] Lambda tree salva em: {lpath}")

    # 3. Filtrar Orthogroups.GeneCount.tsv para os 6 táxons
    gene_count_files = sorted(
        glob.glob(str(ORTHO_DIR / "results" / "Results_*" / "Orthogroups" / "Orthogroups.GeneCount.tsv"))
    )
    if not gene_count_files:
        raise FileNotFoundError(f"Orthogroups.GeneCount.tsv não encontrado em {ORTHO_DIR}")

    df_raw = pd.read_csv(gene_count_files[0], sep="\t")
    print(f"[INFO] Lendo {gene_count_files[0]} ({len(df_raw)} ortogrupos brutos)")

    full_rows = []
    retained_rows = []
    large_rows = []
    decisions = []

    for _, row in df_raw.iterrows():
        og = row["Orthogroup"]
        counts = {sp: int(row[col]) for sp, col in SPECIES_COLS.items()}
        total_6 = sum(counts.values())
        max_c = max(counts.values())

        # Verifica presença nos dois lados da raiz das 6 monocotiledôneas:
        # Lado 1: Dala | Lado 2: Clado Pandanales (Ptec, Abra, Xvis, Vper, Vtub)
        in_dala = counts["Dala"] > 0
        in_pandanales = (
            counts["Ptec"] + counts["Abra"] + counts["Xvis"] + counts["Vper"] + counts["Vtub"]
        ) > 0
        present_at_root = in_dala and in_pandanales

        if total_6 == 0:
            decisions.append({
                "FamilyID": og,
                "status": "dropped_ath_only",
                "max_count_6taxa": 0,
                "total_6taxa": 0,
                "present_both_sides_of_root": False,
            })
            continue

        cafe_row = {"Desc": og, "FamilyID": og, **counts}
        full_rows.append(cafe_row)

        if max_c >= MAX_COUNT_EXCLUSIVE:
            status = "excluded_large_ge100"
            large_rows.append(cafe_row)
        else:
            status = "retained_for_cafe"
            retained_rows.append(cafe_row)

        decisions.append({
            "FamilyID": og,
            "status": status,
            "max_count_6taxa": max_c,
            "total_6taxa": total_6,
            "present_both_sides_of_root": present_at_root,
        })

    df_full = pd.DataFrame(full_rows)
    df_retained = pd.DataFrame(retained_rows)
    df_large = pd.DataFrame(large_rows)
    df_decisions = pd.DataFrame(decisions)

    df_full.to_csv(CAFE_IN_DIR / "cafe_family_input_full_6taxa.tsv", sep="\t", index=False)
    df_retained.to_csv(CAFE_IN_DIR / "cafe_family_input_6taxa.tsv", sep="\t", index=False)
    df_large.to_csv(CAFE_IN_DIR / "cafe_family_input_large_6taxa.tsv", sep="\t", index=False)
    df_decisions.to_csv(CAFE_IN_DIR / "family_filter_decisions_6taxa.tsv", sep="\t", index=False)

    print(f"[RESUMO] Total no OrthoFinder (7 táxons): {len(df_raw)}")
    print(f"[RESUMO] Exclusivos de Arabidopsis (removidos): {(df_decisions['status'] == 'dropped_ath_only').sum()}")
    print(f"[RESUMO] Presentes nas 6 monocotiledôneas: {len(df_full)}")
    print(f"[RESUMO] Retidos para estimativa de lambda (<{MAX_COUNT_EXCLUSIVE} cópias): {len(df_retained)}")
    print(f"[RESUMO] Segregados como famílias grandes (>={MAX_COUNT_EXCLUSIVE} cópias): {len(df_large)}")


if __name__ == "__main__":
    main()

