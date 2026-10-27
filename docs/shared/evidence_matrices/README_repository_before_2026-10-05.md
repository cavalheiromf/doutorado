# Genômica Comparativa, Macroevolução e Sensores de Estresse Osmótico em Velloziaceae

**Tese de Doutorado em Biologia Vegetal / Genômica**  
**Candidata:** Mariana Feitosa Cavalheiro  
**Instituição:** Universidade Estadual de Campinas (UNICAMP)  

---

## 📌 Visão Geral do Projeto

Este repositório contém os dados, scripts, pipelines bioinformáticos e manuscritos referentes à tese de doutorado focada na história evolutiva, adaptação ecológica e mecanismos moleculares de tolerância à dessecação na família **Velloziaceae** (Monocotiledôneas, Pandanales), com ênfase no contraste adaptativo entre as espécies *Vellozia tubiflora* e *Vellozia peripherica* e na caracterização de sensores de estresse da família de canais de cálcio mecanossensíveis **OSCA**.

---

## 📂 Estrutura do Repositório

```text
doutorado/
├── chapter_macroevolution/     # Capítulo de Macroevolução, Filogenômica e Seleção em Velloziaceae
│   ├── 00_data/                # GFFs, sequências CDS e anotações dos táxons
│   ├── 01_orthology/           # Ortologia pura e sem viés (OrthoFinder)
│   ├── 02_phylogenomics/       # Filogenômica baseada em 1:1 cópia única (MAFFT, IQ-TREE 2)
│   ├── 03_dating/              # Datação molecular com calibrações fósseis (MCMCtree / PAML)
│   ├── 04_gene_families/       # Dinâmica de expansão/contração de famílias gênicas (CAFE5)
│   ├── 05_selection/           # Testes de seleção positiva e divergência adaptativa (HyPhy)
│   ├── docs/                   # Documentação do capítulo
│   └── scripts/                # Scripts em Python e SLURM para cada etapa do pipeline
│
├── chapter2_osca/              # Capítulo da Família Gênica OSCA (Canais Mecanossensíveis)
│   ├── 01_gene_identification/ # Identificação e mineração genômica (HMMER / InterProScan)
│   ├── 02_phylogeny/           # Filogenia de Máxima Verossimilhança dos canais OSCA (IQ-TREE 2)
│   ├── 03_synteny/             # Análise de sintenia e duplicações (tandem/segmental)
│   ├── 04_evolutionary_rates/  # Taxas de evolução molecular (Ka/Ks)
│   ├── 04_promoters/           # Análise de elementos cis-regulatórios em promotores
│   ├── 05_rnaseq/              # Pipeline de alinhamento e quantificação de RNA-seq (STAR)
│   ├── 06_expression/          # Análise de expressão diferencial sob seca (DESeq2)
│   ├── 07_ppi_network/         # Redes de interação proteína-proteína (PPI)
│   ├── 08_structural/          # Estrutura 3D e topologia transmembrana
│   └── scripts/                # Scripts utilitários e validações específicas do OSCA
│
├── data/                       # Genomas de referência e anotações estruturais
│   ├── genomes/Vper/           # Montagem e anotação de Vellozia peripherica (hapA.v1)
│   └── genomes/Vtub/           # Montagem e anotação de Vellozia tubiflora (hapA.v1)
│
├── teamwork/                   # Organização de redação, literatura e figuras da tese
│   ├── 01_drafts_and_outlines/ # Rascunhos dos capítulos, outlines e revisões de literatura (ABNT)
│   ├── 02_literature_library/  # Biblioteca de artigos em Markdown e PDF (OpenAlex & Local)
│   ├── 03_figures/             # Figuras finais prontas para publicação e scripts geradores
│   └── 04_audits_and_reports/  # Relatórios de auditoria, matrizes de evidência e iterações
│
├── reports/                    # Relatórios de validação bioinformática
└── docs/ & workflow/           # Documentação geral e funções auxiliares de workflow
```

---

## 🧬 Capítulos da Tese

### 1. Macroevolução e Dinâmica Genômica de Velloziaceae (`chapter_macroevolution/`)

* **Abordagem "Funil":** Do tempo profundo e origem da tolerância à dessecação na família até a divergência ecológica entre *V. tubiflora* e *V. peripherica*.
* **Fluxo Metodológico:**
  1. Inferência de ortologia com proteomas primários representativos (`OrthoFinder v3`).
  2. Alinhamento de ortólogos 1:1 de cópia única e filogenômica de supermatriz com partição (`MAFFT` + `IQ-TREE 2`).
  3. Relógio molecular relaxado calibrado por fósseis para testar hipótese de vicariância gondwânica (`MCMCtree`).
  4. Modelagem de turnover de famílias gênicas na árvore ultramétrica (`CAFE5`).
  5. Testes de seleção episódica e positiva nos ramos focais (`HyPhy aBSREL / BUSTED`).

### 2. Caracterização Genômica e Funcional dos Canais OSCA (`chapter2_osca/`)

* **Foco Funcional:** Análise exaustiva da família de canais de cálcio permeáveis disparados por hiperosmolalidade (**OSCA/TMEM63**), cruciais na osmosensibilização e resposta ao dessecamento.
* **Fluxo Metodológico:**
  1. Identificação estrutural via modelo HMM (domínio DUF221 / PF02714).
  2. Reconstrução filogenética e separação em clados homólogos (OSCA1–4).
  3. Arquitetura cromossômica, colinearidade e modos de duplicação gênica.
  4. Perfil de expressão espaço-temporal sob dessecação severa e reidratação via RNA-seq.

---

## 💻 Ambiente Computacional e Requisitos

As análises são executadas em cluster de alto desempenho (HPC) gerenciado via **SLURM**, utilizando ambientes **Conda/Mamba** e módulos de software dedicados.

* **Alinhamento & Filogenia:** `MAFFT v7.520`, `IQ-TREE v2.3.6`
* **Ortologia & Evolução:** `OrthoFinder v3.1.5`, `DIAMOND`, `PAML v4.10 (MCMCtree)`, `CAFE5`, `HyPhy v2.5`
* **Expressão & Genômica:** `STAR`, `SAMtools`, `DESeq2 (R 4.5.1)`, `HMMER 3.3`

---

## 📧 Contato

* **Mariana Feitosa Cavalheiro** — cavalheiromf@gmail.com
