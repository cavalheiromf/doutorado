#!/usr/bin/env python3
"""
scripts/04_classify_gene_duplications.py

Classifica os modos de duplicação gênica em Vellozia peripherica (Vper) e Vellozia tubiflora (Vtub)
utilizando o duplicate_gene_classifier (MCScanX / MCScanX_Assistant) e cruza os resultados com os
ortogrupos e a dinâmica evolutiva de famílias inferida pelo CAFE5.

Categorias de duplicação:
  0: Singleton (cópia única / sem duplicata detectada)
  1: Dispersed (duplicação dispersa em regiões não-sintênicas)
  2: Proximal (duplicação no mesmo cromossomo, <= 10 genes)
  3: Tandem (duplicação em tandem contígua em série, adjacente ou <= 1 gene de gap)
  4: WGD/Segmental (duplicações ancoradas em blocos colineares sintênicos)
"""

import os
import sys
import subprocess
import pandas as pd

BASE_DIR = "/home/mfcaval/github/doutorado/chapter_macroevolution_review"
SYNTENY_DIR = os.path.join(BASE_DIR, "04_gene_families", "synteny")
DUP_DIR = os.path.join(SYNTENY_DIR, "duplications")
TOOLS_BIN = os.path.join(SYNTENY_DIR, "tools", "MCScanX_Assistant", "scripts", "MCScanX", "duplicate_gene_classifier")
ORTHOGROUPS_TSV = os.path.join(BASE_DIR, "01_orthology", "results", "Results_Aug30", "Orthogroups", "Orthogroups.tsv")
MASTER_TABLE = os.path.join(BASE_DIR, "04_gene_families", "summary", "master_family_table.tsv")

CODE_MAP = {
    0: "Singleton",
    1: "Dispersed",
    2: "Proximal",
    3: "Tandem",
    4: "WGD/Segmental"
}

SPECIES_CONFIG = {
    "vper": {
        "name": "Vellozia peripherica",
        "bed": os.path.join(SYNTENY_DIR, "vper.bed"),
        "last": os.path.join(SYNTENY_DIR, "vper.vper.last.P98L0.inverse"),
        "og_pattern": "vper",
        "change_col": "ViterbiChange_Vper",
        "obs_col": "Obs_Vper",
        "class_col": "Classification_Vper"
    },
    "vtub": {
        "name": "Vellozia tubiflora",
        "bed": os.path.join(SYNTENY_DIR, "vtub.bed"),
        "last": os.path.join(SYNTENY_DIR, "vtub.vtub.last.P98L0.inverse"),
        "og_pattern": "vtub",
        "change_col": "ViterbiChange_Vtub",
        "obs_col": "Obs_Vtub",
        "class_col": "Classification_Vtub"
    }
}

def setup_environment():
    os.makedirs(DUP_DIR, exist_ok=True)
    if not os.path.exists(TOOLS_BIN):
        raise FileNotFoundError(f"duplicate_gene_classifier não encontrado em: {TOOLS_BIN}")
    os.chmod(TOOLS_BIN, 0o755)

def prepare_inputs(sp_key):
    cfg = SPECIES_CONFIG[sp_key]
    bed_file = cfg["bed"]
    last_file = cfg["last"]
    
    gff_out = os.path.join(DUP_DIR, f"{sp_key}.gff")
    blast_out = os.path.join(DUP_DIR, f"{sp_key}.blast")
    
    print(f"[{sp_key}] Preparando {gff_out} a partir de {bed_file}...")
    with open(bed_file, "r") as f_in, open(gff_out, "w") as f_out:
        for line in f_in:
            parts = line.strip().split("\t")
            if len(parts) >= 4:
                chrom, start, end, gene_id = parts[0], parts[1], parts[2], parts[3]
                f_out.write(f"{chrom}\t{gene_id}\t{start}\t{end}\n")
                
    print(f"[{sp_key}] Preparando {blast_out} a partir de {last_file}...")
    if os.path.exists(blast_out):
        os.remove(blast_out)
    os.symlink(last_file, blast_out)

def run_classifier(sp_key):
    print(f"[{sp_key}] Executando duplicate_gene_classifier...")
    cmd = [TOOLS_BIN, sp_key, "-s", "5", "-m", "25", "-n", "10"]
    res = subprocess.run(cmd, cwd=DUP_DIR, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print(f"Erro ao executar classificador para {sp_key}:")
        print(res.stderr)
        sys.exit(1)
    print(res.stdout)

def annotate_species(sp_key, df_og, df_master):
    cfg = SPECIES_CONFIG[sp_key]
    gene_type_file = os.path.join(DUP_DIR, f"{sp_key}.gene_type")
    bed_file = cfg["bed"]
    
    # 1. Ler gene_type
    df_types = pd.read_csv(gene_type_file, sep="\t", header=None, names=["gene_id", "dup_code"])
    df_types["dup_type"] = df_types["dup_code"].map(CODE_MAP)
    
    # 2. Ler coordenadas BED
    bed_cols = ["chrom", "start", "end", "gene_id", "score", "strand"]
    df_bed = pd.read_csv(bed_file, sep="\t", header=None, names=bed_cols)
    df_merged = pd.merge(df_types, df_bed[["chrom", "start", "end", "strand", "gene_id"]], on="gene_id", how="left")
    
    # 3. Mapear gene -> Orthogroup
    sp_col = None
    for c in df_og.columns:
        if cfg["og_pattern"] in c.lower():
            sp_col = c
            break
            
    gene_to_og = {}
    if sp_col:
        for _, row in df_og.dropna(subset=[sp_col]).iterrows():
            og_id = row["Orthogroup"]
            genes = [g.strip() for g in str(row[sp_col]).split(",") if g.strip()]
            for g in genes:
                gene_to_og[g] = og_id
                
    df_merged["orthogroup"] = df_merged["gene_id"].map(gene_to_og).fillna("Unassigned")
    
    out_annotated = os.path.join(DUP_DIR, f"{sp_key}_gene_duplications_annotated.tsv")
    df_merged.to_csv(out_annotated, sep="\t", index=False)
    
    # 4. Sumário
    summary = df_merged["dup_type"].value_counts().reset_index()
    summary.columns = ["dup_type", "count"]
    summary["percentage"] = (summary["count"] / len(df_merged)) * 100
    summary["species"] = cfg["name"]
    out_summary = os.path.join(DUP_DIR, f"{sp_key}_duplication_summary.tsv")
    summary.to_csv(out_summary, sep="\t", index=False)
    
    # 5. Cruzamento com famílias expandidas do CAFE5
    if df_master is not None:
        change_col = cfg["change_col"]
        obs_col = cfg["obs_col"]
        class_col = cfg["class_col"]
        
        exp_sp = df_master[(df_master["Family_pval"] < 0.05) & (df_master[change_col] > 0)].copy()
        og_breakdown = df_merged[df_merged["orthogroup"].isin(exp_sp["FamilyID"])].groupby(["orthogroup", "dup_type"]).size().unstack(fill_value=0)
        
        breakdown_merged = pd.merge(exp_sp[["FamilyID", obs_col, change_col, "Family_pval", class_col, "Ath_Locus_Tags"]], 
                                    og_breakdown, left_on="FamilyID", right_index=True, how="left").fillna(0)
        
        out_exp = os.path.join(DUP_DIR, f"{sp_key}_expanded_families_duplication_breakdown.tsv")
        breakdown_merged.to_csv(out_exp, sep="\t", index=False)
    
    return summary

def main():
    print("=" * 70)
    print("CLASSIFICAÇÃO DE MODOS DE DUPLICAÇÃO EM VELLOZIA (Vper e Vtub)")
    print("=" * 70)
    setup_environment()
    
    print("\nCarregando dados de ortogrupos e tabela mestre do CAFE5...")
    df_og = pd.read_csv(ORTHOGROUPS_TSV, sep="\t")
    df_master = pd.read_csv(MASTER_TABLE, sep="\t") if os.path.exists(MASTER_TABLE) else None
    
    summaries = []
    for sp_key in ["vper", "vtub"]:
        print(f"\n>>> Processando {SPECIES_CONFIG[sp_key]['name']} ({sp_key}) <<<")
        prepare_inputs(sp_key)
        run_classifier(sp_key)
        sp_sum = annotate_species(sp_key, df_og, df_master)
        summaries.append(sp_sum)
        
    df_all_sum = pd.concat(summaries, ignore_index=True)
    pivot_sum = df_all_sum.pivot(index="dup_type", columns="species", values=["count", "percentage"])
    out_comp = os.path.join(DUP_DIR, "vellozia_comparative_duplication_summary.tsv")
    df_all_sum.to_csv(out_comp, sep="\t", index=False)
    
    print("\n" + "=" * 70)
    print("QUADRO COMPARATIVO DE DUPLICAÇÕES: V. peripherica vs V. tubiflora")
    print("=" * 70)
    # Tabela comparativa limpa
    comp_table = df_all_sum.pivot(index="dup_type", columns="species", values="count")
    comp_pct = df_all_sum.pivot(index="dup_type", columns="species", values="percentage").round(2)
    
    merged_view = pd.DataFrame()
    for col in comp_table.columns:
        merged_view[f"{col} (N)"] = comp_table[col]
        merged_view[f"{col} (%)"] = comp_pct[col]
        
    print(merged_view.to_string())
    print("=" * 70)
    print(f"\nArquivos gerados com sucesso no diretório: {DUP_DIR}\n")

if __name__ == "__main__":
    main()
