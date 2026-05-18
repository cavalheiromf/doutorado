import json
import os

notebook_path = "/home/mfcaval/github/doutorado/analyses/07_ppi_network/scripts/PPI_Network.ipynb"

# Load existing notebook
with open(notebook_path, "r") as f:
    notebook = json.load(f)

cells = notebook.get("cells", [])

# Markdown for Functional Annotation
md_source_annot = [
    "## 6. Recuperar Anotação Funcional (Functional Annotation)\n",
    "Podemos consultar a API do STRING para obter a anotação funcional (GO, Pfam, InterPro, etc.) dos genes que compõem a nossa rede. Para isso, vamos extrair todos os nós (proteínas) únicos do TSV gerado e consultar o endpoint `/functional_annotation`."
]
cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": md_source_annot
})

# Code for Functional Annotation
code_source_annot = [
    "import os\n",
    "import requests\n",
    "import pandas as pd\n",
    "from io import StringIO\n",
    "\n",
    "# Extrair todos os nós únicos da rede (usando o df_filtered da etapa 5)\n",
    "unique_nodes = set(df_filtered['stringId_A']).union(set(df_filtered['stringId_B']))\n",
    "unique_nodes = list(unique_nodes)\n",
    "print(f\"Total de proteínas únicas na rede: {len(unique_nodes)}\")\n",
    "\n",
    "# Montar requisição para anotação funcional\n",
    "annot_url = f\"{STRING_API_URL}/{OUTPUT_FORMAT_TSV}/functional_annotation\"\n",
    "\n",
    "params_annot = {\n",
    "    \"identifiers\": \"%0d\".join(unique_nodes),\n",
    "    \"species\": SPECIES_ID,\n",
    "    \"caller_identity\": \"doutorado_mfcaval\"\n",
    "}\n",
    "\n",
    "print(\"Consultando a API para anotação funcional...\")\n",
    "resp_annot = requests.post(annot_url, data=params_annot)\n",
    "\n",
    "if resp_annot.status_code == 200:\n",
    "    df_annot = pd.read_csv(StringIO(resp_annot.text), sep='\\t')\n",
    "    print(f\"Retornadas {len(df_annot)} anotações funcionais.\")\n",
    "    display(df_annot.head())\n",
    "    \n",
    "    # Salvar em disco\n",
    "    annot_path = os.path.join(RESULTS_DIR, f\"{TARGET_SPECIES}_functional_annotation.tsv\")\n",
    "    df_annot.to_csv(annot_path, sep='\\t', index=False)\n",
    "    print(f\"✅ Anotações funcionais salvas em: {annot_path}\")\n",
    "else:\n",
    "    print(f\"❌ Erro na consulta (Status {resp_annot.status_code})\")\n",
    "    print(resp_annot.text)\n"
]

cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": code_source_annot
})

# Markdown for Enrichment
md_source_enrich = [
    "## 7. Análise de Enriquecimento (Enrichment Analysis)\n",
    "Além das anotações individuais, podemos verificar quais termos (GO, vias KEGG, domínios) estão estatisticamente enriquecidos nesse conjunto de proteínas quando comparados ao genoma completo, usando o endpoint `/enrichment`."
]
cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": md_source_enrich
})

# Code for Enrichment
code_source_enrich = [
    "enrich_url = f\"{STRING_API_URL}/{OUTPUT_FORMAT_TSV}/enrichment\"\n",
    "\n",
    "print(\"Consultando a API para análise de enriquecimento...\")\n",
    "resp_enrich = requests.post(enrich_url, data=params_annot)\n",
    "\n",
    "if resp_enrich.status_code == 200:\n",
    "    df_enrich = pd.read_csv(StringIO(resp_enrich.text), sep='\\t')\n",
    "    print(f\"Encontrados {len(df_enrich)} termos enriquecidos.\")\n",
    "    display(df_enrich.head())\n",
    "    \n",
    "    # Salvar em disco\n",
    "    enrich_path = os.path.join(RESULTS_DIR, f\"{TARGET_SPECIES}_enrichment.tsv\")\n",
    "    df_enrich.to_csv(enrich_path, sep='\\t', index=False)\n",
    "    print(f\"✅ Resultados do enriquecimento salvos em: {enrich_path}\")\n",
    "else:\n",
    "    print(f\"❌ Erro na consulta (Status {resp_enrich.status_code})\")\n",
    "    print(resp_enrich.text)\n"
]

cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": code_source_enrich
})

notebook["cells"] = cells

with open(notebook_path, "w") as f:
    json.dump(notebook, f, indent=2)

print("Appended Functional Annotation and Enrichment cells to Notebook.")
