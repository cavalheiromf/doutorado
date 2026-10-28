# Guia de Reprodutibilidade Computacional

Este documento fornece instruções detalhadas para reproduzir integralmente todos os resultados computacionais, análises filogenômicas, modelos evolutivos, análises de expressão e figuras da tese de doutorado:

**"Genômica Evolutiva e Funcional de Velloziaceae: Adaptações à Dessecação e Radiação em Inselbergs"**  
Autora: Mariana Ferreira Cavalheiro  
Laboratório de Biologia Molecular e Genômica de Plantas, Instituto de Biologia, UNICAMP

---

## 1. Requisitos de Sistema e Hardware

- **Sistema Operacional:** Linux x86_64 (testado em Ubuntu 22.04 LTS / Rocky Linux 9).
- **Gerenciador de Pacotes:** `mamba` ou `conda` (recomenda-se Miniforge/Mambaforge).
- **Recursos Mínimos (Análises Locais / Figuras / Testes):**
  - CPU: 8 núcleos
  - RAM: 16 GB
  - Armazenamento livre: 50 GB
- **Recursos Recomendados para Execuções Pesadas (PAML / CAFE5 / Alinhamentos Globais):**
  - CPU: 32+ núcleos (ou acesso a cluster HPC com escalonador SLURM)
  - RAM: 64+ GB

---

## 2. Instalação do Ambiente Computacional

Todas as dependências de Python, R/Bioconductor e ferramentas de linha de comando estão unificadas no arquivo [`environment.yml`](environment.yml).

### Criando e ativando o ambiente:

```bash
# Clone o repositório se ainda não o fez
git clone https://github.com/mfcaval/doutorado.git
cd doutorado

# Crie o ambiente Conda unificado vellozia-genomics
mamba env create -f environment.yml

# Ative o ambiente
conda activate vellozia-genomics
```

### Ferramentas externas de terceiros (se não instaladas via Conda):
- **CAFE5:** Se compilado a partir do código-fonte, garanta que o binário esteja no seu `$PATH` ou defina a variável `export CAFE5_BIN=/caminho/para/cafe5`.
- **PAML (codeml):** Disponível via conda ou `$PATH`.

---

## 3. Proveniência e Integridade dos Dados

Os dados brutos e montagens genômicas estão documentados em [`data/README.md`](data/README.md).

### Estrutura de dados:
```
data/
├── genomes/
│   ├── Vtub/        # Vellozia tubiflora (quase T2T, 9 pseudocromossomos)
│   ├── Vper/        # Vellozia plicata / intermedia (17 cromossomos)
│   └── outgroups/   # Xvis, Abra, Ptec, Dala, Ath
├── rnaseq/          # 18 bibliotecas pareadas (Folha, Caule, Raiz em Vtub e Vper)
├── pfam/            # Perfis HMM (ex.: PF02714 para OSCA/TMEM63)
└── checksums.sha256 # Hashes SHA-256 para integridade
```

### Verificação de integridade:
```bash
# Verifique se os arquivos locais correspondem aos hashes de referência:
sha256sum -c data/checksums.sha256
```

---

## 4. Pipeline do Capítulo 3: Macroevolução e Filogenômica Comparativa

O pipeline do Capítulo 3 integra a inferência de ortogrupos (OrthoFinder), calibração de modelos evolutivos de famílias gênicas (CAFE5), seleção positiva por ramos (PAML/codeml) e enriquecimento funcional (clusterProfiler/TopGO).

### Executor principal:
Localizado em [`pipelines/03_macroevolution/run_pipeline.sh`](pipelines/03_macroevolution/run_pipeline.sh).

```bash
# Ver opções disponíveis
bash pipelines/03_macroevolution/run_pipeline.sh --help

# 1. Executar todas as etapas sequencialmente em máquina local:
bash pipelines/03_macroevolution/run_pipeline.sh --step all --threads 16 --mode local

# 2. Executar etapa específica de CAFE5:
bash pipelines/03_macroevolution/run_pipeline.sh --step cafe5 --threads 8

# 3. Executar etapa de duplicações gênicas (WGD / DupPipe / synteny):
bash pipelines/03_macroevolution/run_pipeline.sh --step duplications --threads 8

# 4. Executar enriquecimento funcional:
bash pipelines/03_macroevolution/run_pipeline.sh --step enrichment --threads 8

# 5. Gerar tabelas e figuras do manuscrito:
bash pipelines/03_macroevolution/run_pipeline.sh --step manuscript

# Para submeter as etapas pesadas via SLURM no cluster:
bash pipelines/03_macroevolution/run_pipeline.sh --step cafe5 --mode slurm
```

---

## 5. Pipeline do Capítulo 4: Evolução da Família OSCA

O pipeline do Capítulo 4 realiza a caracterização genômica comparativa, filogenia, estrutura gênica, análise de promotores/cis-regulatórios e perfil de expressão gênica da família de canais mecanossensíveis OSCA em *Vellozia tubiflora* e *Vellozia plicata*.

### Executor principal:
Localizado em [`pipelines/04_osca/run_pipeline.sh`](pipelines/04_osca/run_pipeline.sh).

```bash
# Ver opções disponíveis
bash pipelines/04_osca/run_pipeline.sh --help

# 1. Executar pipeline completo localmente:
bash pipelines/04_osca/run_pipeline.sh --step all --threads 8 --mode local

# 2. Curadoria e extração de sequências OSCA:
bash pipelines/04_osca/run_pipeline.sh --step sequences

# 3. Análise de taxas evolutivas e sintenia (Ka/Ks):
bash pipelines/04_osca/run_pipeline.sh --step rates

# 4. Análise de promotores e elementos cis (PlantCARE):
bash pipelines/04_osca/run_pipeline.sh --step promoters

# 5. Expressão diferencial e heatmaps (DESeq2 / RNA-seq):
bash pipelines/04_osca/run_pipeline.sh --step expression

# 6. Verificação de integridade dos arquivos gerados:
bash pipelines/04_osca/run_pipeline.sh --step verify
```

---

## 6. Regeneração de Figuras e Tabelas

### Figuras do Capítulo 3:
- **Figura 1 (Filogenia e Histórico de WGDs):** `pipelines/03_macroevolution/workflow/scripts/manuscript_figures/generate_figure1_wgd.py`
- **Figura 2 (Expansões/Contrações CAFE5):** `pipelines/03_macroevolution/workflow/scripts/manuscript_figures/generate_figure2_cafe5.py`
- **Figura 3 (Enriquecimento Funcional de Clados de Tolerância):** `pipelines/03_macroevolution/workflow/scripts/09_run_enrichment_pipeline.sh`

### Figuras do Capítulo 4:
- **Figura 1 (Árvore Filogenética OSCA e Arquitetura de Domínios):** `pipelines/04_osca/workflow/scripts/figures/generate_figure1_osca_phylogeny.py`
- **Figura 2 (Sintenia e Colinearidade Genômica):** `pipelines/04_osca/workflow/scripts/figures/generate_figure2_synteny.py`
- **Figura 3 (Elementos cis-regulatórios de Estresse):** `pipelines/04_osca/workflow/scripts/figures/generate_figure3_promoters.py`
- **Figura 4 (Heatmap de Expressão Tecidual e Dessecação):** `pipelines/04_osca/workflow/scripts/figures/generate_figure4_expression_heatmap.R`

---

## 7. Suíte de Testes Automatizados

O repositório inclui testes automatizados com `pytest` para verificar a consistência de tabelas mestre, integridade de IDs, modelos de substituição e formatação de saídas:

```bash
# Executar todos os testes da tese
pytest -v

# Executar apenas testes do Capítulo 3
pytest pipelines/03_macroevolution/workflow/tests/ -v

# Executar apenas testes do Capítulo 4
pytest pipelines/04_osca/workflow/tests/ -v
```

---

## 8. Contato e Suporte

- Mariana Ferreira Cavalheiro: [marianacavalheiro@unicamp.br](mailto:marianacavalheiro@unicamp.br)
- Laboratório de Genômica e Expressão (LGE) / LBMGP — UNICAMP
