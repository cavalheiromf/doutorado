import pandas as pd
from ete3 import Tree
import os

# Definindo os caminhos
ortho_counts_path = "../02_orthofinder/data/OrthoFinder/Results_Aug27_2/Orthogroups/Orthogroups.GeneCount.tsv"
species_tree_path = "../02_orthofinder/data/OrthoFinder/Results_Aug27_2/Species_Tree/SpeciesTree_rooted.txt"
output_counts = "cafe_input.tsv"
output_tree = "ultrametric_vellozia.tre"

print("Lendo tabela de contagens...")
df = pd.read_csv(ortho_counts_path, sep='\t')

# As colunas originais possuem Ath.canonical.pep, Vper.pep, Vtub.pep
# Queremos manter apenas as Vellozias (remover Arabidopsis e a coluna Total)
species_to_keep = [col for col in df.columns if col not in ['Orthogroup', 'Ath.canonical.pep', 'Total']]

print(f"Espécies mantidas para o CAFE5: {species_to_keep}")

# Filtrar famílias que têm 0 cópias em ambas as Vellozias
df_filtered = df[(df[species_to_keep] > 0).any(axis=1)].copy()

# Filtrar famílias absurdamente grandes (ex > 100 cópias) para não quebrar o CAFE5
max_copies = 100
df_filtered = df_filtered[~(df_filtered[species_to_keep] > max_copies).any(axis=1)]

print(f"Total de famílias retidas após filtros: {len(df_filtered)}")

# Preparar formato para o CAFE5
df_cafe = pd.DataFrame()
df_cafe['Desc'] = ['(null)'] * len(df_filtered)
df_cafe['Family ID'] = df_filtered['Orthogroup'].values
for sp in species_to_keep:
    df_cafe[sp] = df_filtered[sp].values

df_cafe.to_csv(output_counts, sep='\t', index=False)
print(f"Tabela de contagens salva em {output_counts}")

print("Lendo a árvore de espécies...")
t = Tree(species_tree_path)
print("Espécies originais na árvore:", t.get_leaf_names())

# Prune the tree to keep only the Vellozia species
t.prune(species_to_keep)
print("Espécies após poda:", t.get_leaf_names())

# Como temos apenas duas espécies, faremos uma árvore ultramétrica simples
# (ramos de tamanho igual a partir da raiz)
leaves = t.get_leaves()
for leaf in leaves:
    leaf.dist = 1.0 # Distância arbitrária de 1 para fins de análise estrutural

# Escrever a árvore sem suporte interno e apenas com a topologia e distâncias
t.write(outfile=output_tree, format=5)
print(f"Árvore ultramétrica salva em {output_tree}")
