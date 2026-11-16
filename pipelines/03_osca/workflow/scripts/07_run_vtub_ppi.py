import os
import requests
import pandas as pd
from io import StringIO
import networkx as nx
import matplotlib.pyplot as plt

from pathlib import Path

# Definir os diretórios
SCRIPT_DIR = Path(__file__).resolve().parent
OSCA_DIR = SCRIPT_DIR.parents[1]
BASE_DIR = OSCA_DIR.parent.parent
RESULTS_DIR = OSCA_DIR / "07_ppi_network" / "results"
OSCA_IDS_FILE = OSCA_DIR / "01_gene_identification" / "results" / "oscasIDs.txt"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# Parâmetros Flexíveis para Vtub
TARGET_SPECIES = "Vtub"
STRING_SPECIES_IDS = {
    "Vper": "STRG0A77QVI",
    "Vtub": "STRG0A11TDW"
}

# Parâmetros da API
STRING_API_URL = "https://string-db.org/api"
OUTPUT_FORMAT_TSV = "tsv"
OUTPUT_FORMAT_IMAGE = "highres_image"

SPECIES_ID = STRING_SPECIES_IDS[TARGET_SPECIES]
REQUIRED_SCORE = 400     # 400 = Confiança média (medium confidence)
ADD_NODES = 50           # Quantidade de parceiros de interação para adicionar na rede
NETWORK_TYPE = "functional" # 'functional' (conhecidas e previstas) ou 'physical'

# 1. Ler os IDs originais
original_ids = []
with open(OSCA_IDS_FILE, 'r') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        orig_id, osca_name = line.split()
        
        # Filtrar pela espécie atual (Vtub.hapA...)
        if orig_id.startswith(TARGET_SPECIES):
            original_ids.append(orig_id)

print(f"Encontrados {len(original_ids)} genes para {TARGET_SPECIES}:")
print(original_ids)

# 2. Montar a requisição da rede PPI no STRING
request_url = f"{STRING_API_URL}/{OUTPUT_FORMAT_TSV}/network"
params = {
    "identifiers": "%0d".join(original_ids), # IDs separados por carriage return
    "species": SPECIES_ID,                   # ID mapeado no STRING
    "required_score": REQUIRED_SCORE,
    "add_nodes": ADD_NODES,
    "network_type": NETWORK_TYPE,
    "caller_identity": "doutorado_mfcaval"
}

print("Consultando a API do STRING-db (dados em texto)...")
response = requests.post(request_url, data=params)

if response.status_code == 200:
    df_network = pd.read_csv(StringIO(response.text), sep='\t')
    print(f"Rede retornada com {len(df_network)} interações (arestas).")
    
    # Salvar em disco
    tsv_path = os.path.join(RESULTS_DIR, f"{TARGET_SPECIES}_ppi_network.tsv")
    df_network.to_csv(tsv_path, sep='\t', index=False)
    print(f"✅ Dados da rede salvos em: {tsv_path}")
else:
    print(f"❌ Erro na consulta da API (Status {response.status_code})")
    print(response.text)
    exit(1)

# 3. Requisitar a imagem de alta resolução do STRING
image_url = f"{STRING_API_URL}/{OUTPUT_FORMAT_IMAGE}/network"
print("Consultando a API do STRING-db (imagem)...")
img_response = requests.post(image_url, data=params)
if img_response.status_code == 200:
    img_path = os.path.join(RESULTS_DIR, f"{TARGET_SPECIES}_ppi_network.png")
    with open(img_path, 'wb') as f:
        f.write(img_response.content)
    print(f"✅ Imagem original do STRING salva em: {img_path}")
else:
    print(f"❌ Erro ao baixar imagem (Status {img_response.status_code})")

# 4. Construção e Renderização da Rede usando NetworkX
df_filtered = df_network[df_network['score'] >= (REQUIRED_SCORE / 1000.0)]
print(f"Mantendo {len(df_filtered)} arestas com score >= {REQUIRED_SCORE/1000.0}")

G = nx.Graph()
for _, row in df_filtered.iterrows():
    node_a = row.get("preferredName_A", row["stringId_A"])
    node_b = row.get("preferredName_B", row["stringId_B"])
    G.add_edge(node_a, node_b, weight=row["score"])

degrees = dict(G.degree())
node_sizes = [v * 100 + 300 for v in degrees.values()]
edge_weights = nx.get_edge_attributes(G, 'weight')
edge_widths = [weight * 3 for weight in edge_weights.values()]
node_colors = list(degrees.values())

plt.figure(figsize=(14, 10))
plt.title(f"Rede de Interação Proteína-Proteína - {TARGET_SPECIES} (NetworkX)", fontsize=18)
pos = nx.spring_layout(G, k=0.5, seed=42)
nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, cmap=plt.cm.viridis, alpha=0.9)
nx.draw_networkx_edges(G, pos, width=edge_widths, alpha=0.5, edge_color="gray")
nx.draw_networkx_labels(G, pos, font_size=9, font_family="sans-serif", font_weight="bold")

cbar = plt.colorbar(nodes, pad=0.02)
cbar.set_label('Número de Conexões (Grau)', rotation=270, labelpad=15)

plt.axis("off")
plt.tight_layout()
out_img_nx = os.path.join(RESULTS_DIR, f"{TARGET_SPECIES}_networkx.png")
plt.savefig(out_img_nx, dpi=300, bbox_inches="tight")
plt.close()
print(f"✅ Imagem NetworkX salva em: {out_img_nx}")

# 5. Recuperar Anotação Funcional (Functional Annotation)
unique_nodes = set(df_filtered['stringId_A']).union(set(df_filtered['stringId_B']))
unique_nodes = list(unique_nodes)
print(f"Total de proteínas únicas na rede: {len(unique_nodes)}")

annot_url = f"{STRING_API_URL}/{OUTPUT_FORMAT_TSV}/functional_annotation"
params_annot = {
    "identifiers": "%0d".join(unique_nodes),
    "species": SPECIES_ID,
    "caller_identity": "doutorado_mfcaval"
}

print("Consultando a API para anotação funcional...")
resp_annot = requests.post(annot_url, data=params_annot)
if resp_annot.status_code == 200:
    df_annot = pd.read_csv(StringIO(resp_annot.text), sep='\t')
    print(f"Retornadas {len(df_annot)} anotações funcionais.")
    annot_path = os.path.join(RESULTS_DIR, f"{TARGET_SPECIES}_functional_annotation.tsv")
    df_annot.to_csv(annot_path, sep='\t', index=False)
    print(f"✅ Anotações funcionais salvas em: {annot_path}")
else:
    print(f"❌ Erro na consulta de anotação (Status {resp_annot.status_code})")

# 6. Análise de Enriquecimento (Enrichment Analysis)
enrich_url = f"{STRING_API_URL}/{OUTPUT_FORMAT_TSV}/enrichment"
print("Consultando a API para análise de enriquecimento...")
resp_enrich = requests.post(enrich_url, data=params_annot)
if resp_enrich.status_code == 200:
    df_enrich = pd.read_csv(StringIO(resp_enrich.text), sep='\t')
    print(f"Encontrados {len(df_enrich)} termos enriquecidos.")
    enrich_path = os.path.join(RESULTS_DIR, f"{TARGET_SPECIES}_enrichment.tsv")
    df_enrich.to_csv(enrich_path, sep='\t', index=False)
    print(f"✅ Resultados do enriquecimento salvos em: {enrich_path}")
    
    # 7. Filtrar por NetworkNeighborAL e salvar como solicitado
    df_neighbor = df_enrich[df_enrich['category'] == "NetworkNeighborAL"]
    neighbor_path = os.path.join(RESULTS_DIR, f"{TARGET_SPECIES}_NetworkNeighborAL.tsv")
    df_neighbor.to_csv(neighbor_path, sep='\t', index=False)
    print(f"✅ Resultados do NetworkNeighborAL salvos em: {neighbor_path}")
else:
    print(f"❌ Erro na consulta de enriquecimento (Status {resp_enrich.status_code})")

print("🎉 Análise concluída com sucesso para Vtub!")
