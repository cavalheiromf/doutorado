import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import os
from collections import Counter

# Caminhos
cafe_change = "../cafe5_results/Base_change.tab"
orthogroups_file = "../../02_orthofinder/data/OrthoFinder/Results_Aug27_2/Orthogroups/Orthogroups.tsv"
gff_vper = "../../../../data/genomes/Vper/Vper.hapA.v1.softmasked.gff3"
gff_vtub = "../../../../data/genomes/Vtub/Vtub.hapA.v1.softmasked.gff3"

out_dir = "./"

print("Lendo Base_change.tab...")
df_change = pd.read_csv(cafe_change, sep='\t')
# Colunas: FamilyID, Vtub.pep<1>, Vper.pep<2>, <3> (raiz)
vper_col = [c for c in df_change.columns if 'Vper' in c][0]
vtub_col = [c for c in df_change.columns if 'Vtub' in c][0]

# Summary counts
exp_vper = (df_change[vper_col] > 0).sum()
con_vper = (df_change[vper_col] < 0).sum()
exp_vtub = (df_change[vtub_col] > 0).sum()
con_vtub = (df_change[vtub_col] < 0).sum()

print(f"Vper Expansions: {exp_vper}, Contractions: {con_vper}")
print(f"Vtub Expansions: {exp_vtub}, Contractions: {con_vtub}")

# Gráfico 1: Expansões vs Contrações Gerais
plt.figure(figsize=(8, 6))
sns.set_style("whitegrid")
bar_df = pd.DataFrame({
    'Espécie': ['V. peripherica', 'V. peripherica', 'V. tubiflora', 'V. tubiflora'],
    'Evento': ['Expansão', 'Contração', 'Expansão', 'Contração'],
    'Quantidade': [exp_vper, con_vper, exp_vtub, con_vtub]
})
sns.barplot(data=bar_df, x='Espécie', y='Quantidade', hue='Evento', palette=['#2ca02c', '#d62728'])
plt.title("Total de Famílias em Expansão e Contração")
plt.ylabel("Número de Famílias Gênicas")
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "expansion_contraction_summary.png"), dpi=300)
plt.close()

# Top 15 Expansions e Contrações
top_vper_exp = df_change.sort_values(by=vper_col, ascending=False).head(15)
top_vtub_exp = df_change.sort_values(by=vtub_col, ascending=False).head(15)
top_vper_con = df_change.sort_values(by=vper_col, ascending=True).head(15)
top_vtub_con = df_change.sort_values(by=vtub_col, ascending=True).head(15)

top_fams = pd.concat([top_vper_exp, top_vtub_exp, top_vper_con, top_vtub_con])['FamilyID'].unique()

print("Mapeando Ortogrupos para Genes...")
og_to_genes = {}
with open(orthogroups_file, 'r') as f:
    header = f.readline()
    for line in f:
        parts = line.strip().split('\t')
        og = parts[0]
        if og in top_fams:
            genes = []
            for p in parts[1:]:
                # Cada gene está separado por vírgula
                genes.extend([x.strip() for x in p.split(',') if x.strip()])
            og_to_genes[og] = genes

print("Lendo GFF3s para extrair EggNOG...")
gene_to_func = {}
def parse_gff(gff_path):
    with open(gff_path, 'r') as f:
        for line in f:
            if line.startswith('#'): continue
            if '\tmRNA\t' in line:
                cols = line.strip().split('\t')
                attr = cols[8]
                m = re.search(r'ID=([^;]+)', attr)
                if not m: continue
                gid = m.group(1)
                
                func_m = re.search(r'eggnog_free_text_desc=([^;]+)', attr)
                if func_m:
                    func = func_m.group(1)
                    if func.strip() != "" and func.lower() != "na":
                        gene_to_func[gid] = func.strip()

parse_gff(gff_vper)
parse_gff(gff_vtub)

def get_og_func(og):
    genes = og_to_genes.get(og, [])
    funcs = []
    for g in genes:
        if g in gene_to_func:
            funcs.append(gene_to_func[g])
    if not funcs: return "Função Desconhecida / Hipotética"
    return Counter(funcs).most_common(1)[0][0]

print("Anotando Top famílias...")

# Gerar tabela em Markdown
res_lines = []
res_lines.append("### Top Famílias em Expansão na *V. peripherica*")
res_lines.append("| Orthogroup | Mudança Vper | Mudança Vtub | Função Predominante (EggNOG) |")
res_lines.append("|------------|-------------|-------------|------------------------------|")
for _, row in top_vper_exp.iterrows():
    if row[vper_col] <= 0: continue
    og = row['FamilyID']
    func = get_og_func(og)
    res_lines.append(f"| {og} | +{row[vper_col]} | {row[vtub_col]} | {func} |")

res_lines.append("\n### Top Famílias em Expansão na *V. tubiflora*")
res_lines.append("| Orthogroup | Mudança Vtub | Mudança Vper | Função Predominante (EggNOG) |")
res_lines.append("|------------|-------------|-------------|------------------------------|")
for _, row in top_vtub_exp.iterrows():
    if row[vtub_col] <= 0: continue
    og = row['FamilyID']
    func = get_og_func(og)
    res_lines.append(f"| {og} | +{row[vtub_col]} | {row[vper_col]} | {func} |")

res_lines.append("\n### Top Famílias em Contração (Maior Perda) Geral")
res_lines.append("| Orthogroup | Mudança Vper | Mudança Vtub | Função Predominante (EggNOG) |")
res_lines.append("|------------|-------------|-------------|------------------------------|")
# Combine top contractions
combined_con = pd.concat([top_vper_con, top_vtub_con]).drop_duplicates(subset=['FamilyID']).sort_values(by=vper_col, ascending=True).head(15)
for _, row in combined_con.iterrows():
    if row[vper_col] >= 0 and row[vtub_col] >= 0: continue
    og = row['FamilyID']
    func = get_og_func(og)
    res_lines.append(f"| {og} | {row[vper_col]} | {row[vtub_col]} | {func} |")

with open(os.path.join(out_dir, "top_families_annotated.md"), 'w') as f:
    f.write("\n".join(res_lines))

print("Finalizado com Sucesso!")
