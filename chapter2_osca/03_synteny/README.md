# Análise de Sintenia (`03_synteny`)

Este diretório contém a estrutura de dados, scripts de automação e análises de sintenia genômica (macrosintenia e microsintenia) entre as espécies de orquídeas *Vanilla peripherica* (*Vper*) e *Vanilla tubiflora* (*Vtub*).

A infraestrutura foi desenhada de forma totalmente isolada para comportar análises de sintenia cruzada (intergenômica) e análises de auto-sintenia (intragenômica) de cada genoma, eliminando qualquer risco de conflito de nomenclatura ou arquivos temporários.

---

## 📂 Estrutura do Diretório

A pasta foi reestruturada de forma modular para organizar os inputs, passos intermediários e resultados das análises:

```text
03_synteny/
├── data/                    # Dados de entrada globais compartilhados
│   ├── Vper.bed             # Coordenadas BED de V. peripherica (prefixo 'vp')
│   ├── Vtub.bed             # Coordenadas BED de V. tubiflora (prefixo 'vt')
│   ├── Vper.cds             # Link simbólico para CDS original de Vper
│   └── Vtub.cds             # Link simbólico para CDS original de Vtub
├── last_db/                 # Bancos de dados binários de indexação do LAST (limpos do ambiente de trabalho)
├── intergenomic/            # Análise de sintenia cruzada (Vper vs Vtub)
│   ├── intermediates/       # Arquivos intermediários (.last, .anchors, .simple)
│   ├── layouts/             # Arquivos de layout e configurações do JCVI (.layout, .blocks)
│   └── results/             # Imagens geradas de macrosintenia cruzada (.pdf)
├── intragenomic/            # Análises de auto-sintenia (intragenômica) isoladas
│   ├── Vper/                # Ambiente exclusivo para auto-sintenia de V. peripherica
│   │   ├── intermediates/   # Arquivos parálogos de auto-sintenia contendo duplicações (ex: P98L0)
│   │   ├── layouts/         # Arquivos .blocks e .layout específicos de Vper
│   │   └── results/         # Plot final de auto-sintenia (intragenome.pdf)
│   └── Vtub/                # Ambiente exclusivo para auto-sintenia de V. tubiflora
│       ├── intermediates/   # Arquivos parálogos e blocos duplicados de Vtub
│       ├── layouts/         # Arquivos .blocks e .layout de auto-sintenia de Vtub
│       └── results/         # Plot final de auto-sintenia (intragenome.pdf)
├── results/                 # Resultados consolidados e plots específicos
│   └── microsynteny_plots/  # Figuras de microsintenia focadas em locus (ex: genes OSCA)
└── scripts/                 # Scripts Python de suporte e automação do pipeline
```

---

## 🛠️ Scripts e Utilidades (`scripts/`)

Os scripts automatizam a preparação dos arquivos, identificação de blocos gênicos de interesse e geração de figuras de microsintenia.

### 1. `prepare_files.py`
Prepara os arquivos BED e CDS a partir dos arquivos originais GFF3 e FASTA do projeto:
*   Filtra e extrai apenas feições de `mRNA`.
*   Aplica prefixos específicos às coordenadas dos cromossomos (`vp_` para *Vper* e `vt_` para *Vtub*) para evitar qualquer colisão de eixos no MCscan.
*   Cria links simbólicos dinâmicos para os arquivos de CDS na pasta `data/`, economizando dezenas de megabytes e evitando cópias físicas desnecessárias.

```bash
python scripts/prepare_files.py
```

### 2. `find_osca_blocks.py`
Varre os alinhamentos de sintenia simples (`Vper.Vtub.simple`) e identifica quais blocos sintênicos contêm os genes da família **OSCA** com base na lista de IDs de referência (`oscasIDs.txt` da etapa `01_gene_identification`).
*   Gera um arquivo de blocos anotados (`Vper.Vtub.oscas.simple`) com as linhas contendo genes OSCA destacadas com a cor vermelha (`r*`).

```bash
python scripts/find_osca_blocks.py
```

### 3. `extract_all_osca_microsynteny.py`
Extrai e plota janelas locais de microsintenia (31 genes ao redor de cada gene OSCA) entre *Vper* e *Vtub*:
*   Mapeia dinamicamente os locus cromossomo por cromossomo.
*   Cria os arquivos de `.layout` e `.blocks` temporários automaticamente.
*   Chama a ferramenta `jcvi.graphics.synteny` do pacote MCscan para renderizar os plots.
*   Salva todas as imagens PDF de microsintenia na pasta `results/microsynteny_plots/`.

```bash
python scripts/extract_all_osca_microsynteny.py
```

### 4. Outros Scripts
*   `extract_osca_cluster.py`: Script auxiliar para focar na extração de clusters gênicos ricos.
*   `macrosynteny_osca_orthologs.py` & `macrosynteny_osca_thin.py`: Geração de plots de macrosintenia entre ortólogos com estilizações diferenciadas (linhas finas ou destaque sob medida).

---

## 🚀 Como Executar Análises

As análises de sintenia utilizam o ambiente Python configurado com o pacote **JCVI** (`jcviEnv`).

### 🔑 Importante: Resolução do Erro ETE4
A ferramenta gráfica do JCVI tenta importar a biblioteca `ete4` para renderização de árvores filogenéticas. Como essa biblioteca não está presente ou é incompatível no ambiente do mamba (`jcviEnv`), resolvemos isso criando um script dummy/mock chamado `ete4.py` nos diretórios de execução (`intergenomic/`, `intragenomic/Vper/`, `intragenomic/Vtub/` e no root do diretório).
> **Sempre execute comandos de renderização (`jcvi.graphics.synteny`) dentro de diretórios que possuam esse mock `ete4.py` presente.**

---

### Exemplo 1: Sintenia Cruzada Intergenômica (Vper vs Vtub)

Acesse a pasta isolada:
```bash
cd intergenomic/
```

Execute o cálculo de sintenia (LAST + JCVI MCscan):
```bash
python -m jcvi.compara.synteny screen Vper.bed Vtub.bed --last --path=../last_db
```

Gere o plot de macrosintenia com ortólogos ou blocos selecionados:
```bash
python -m jcvi.graphics.synteny layouts/macrosynteny.blocks layouts/macrosynteny.layout --notex
```
*(Nota: Sempre utilize a flag `--notex` para evitar problemas locais de renderização do LaTeX)*

---

### Exemplo 2: Auto-Sintenia Intragenômica (Duplicações Segmentais de Vtub)

Acesse o ambiente isolado de *Vtub*:
```bash
cd intragenomic/Vtub/
```

Execute o alinhamento contra si mesmo (auto-sintenia):
```bash
python -m jcvi.compara.synteny screen Vtub.bed Vtub.bed --last --path=../../last_db
```

Após filtrar os parálogos de interesse no arquivo `.anchors` (como a duplicação segmental identificada entre os cromossomos `vt_chr1A` e `vt_chr2A` contendo 15 âncoras gênicas):
1.  Configure as coordenadas e âncoras em `layouts/intragenome.blocks`.
2.  Configure a orientação dos eixos cromossômicos em `layouts/intragenome.layout`.

Execute a renderização da imagem:
```bash
python -m jcvi.graphics.synteny layouts/intragenome.blocks layouts/intragenome.layout --notex
```
A imagem resultante será salva de forma limpa em `results/intragenome.pdf`.

---

## 🎨 Boas Práticas de Design para Plots do JCVI

*   **Paleta de Cores Harmônica**: Use cores com boa distinção visual nos arquivos `.layout`. Tons como azul claro (`#9ecae1`) e coral/laranja claro (`#fc9272`) dão um visual premium e moderno às figuras.
*   **Controle de Espessura**: Para visualização limpa de blocos e conexões longas, pode-se encurtar artificialmente as janelas gênicas nos blocos para obter linhas mais finas de conexão em vez de faixas massivas, facilitando a interpretação do alinhamento.
