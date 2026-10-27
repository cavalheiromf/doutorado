# Genômica Comparativa e História Evolutiva de Velloziaceae

[![UNICAMP](https://img.shields.io/badge/UNICAMP-Instituto_de_Biologia-blue.svg)](https://www.ib.unicamp.br/)
[![GCCRC](https://img.shields.io/badge/GCCRC-Genomics_Center-green.svg)](https://www.gccrc.unicamp.br/)
[![BioProject](https://img.shields.io/badge/NCBI_BioProject-PRJNA984512-orange.svg)](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA984512)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Repositório oficial de dados, análises, pipelines computacionais e manuscritos da tese de doutorado de **Mariana Feitosa Cavalheiro**, desenvolvida no Programa de Pós-Graduação em Genética e Biologia Molecular do Instituto de Biologia da Universidade Estadual de Campinas (UNICAMP), em colaboração com o Centro de Pesquisa em Genômica Aplicada às Mudanças Climáticas (GCCRC), o Centro de Biologia Molecular e Engenharia Genética (CBMEG) e a Embrapa Agricultura Digital.

---

## Informações Institucionais

* **Candidata**: Mariana Feitosa Cavalheiro
* **Orientadora**: Dra. Isabel Rodrigues Gerhardt (Embrapa Agricultura Digital / GCCRC / UNICAMP)
* **Coorientadores e Colaboradores Principais**: Dr. Ricardo Augusto Dante (Embrapa / GCCRC), Prof. Dr. Paulo Arruda (UNICAMP / CBMEG), Dra. Francine A. N. de Almeida (UNICAMP)
* **Programa**: Pós-Graduação em Genética e Biologia Molecular (PPG-GBM), Instituto de Biologia, UNICAMP
* **Apoio Financeiro**:
  * Fundação de Amparo à Pesquisa do Estado de São Paulo (FAPESP, bolsas e auxílios de pesquisa 2020/02084-0 e 2016/23218-0)
  * Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq, processo 140481/2020-6 e bolsa de produtividade em pesquisa)
* **Conformidade Legal e Patrimônio Genético**:
  * **SisGen**: Registros AF30A4D (*Vellozia peripherica*) e A5985A4 (*Vellozia tubiflora*), Ministério do Meio Ambiente, Brasil.
  * **ICMBio**: Autorizações de coleta botânica no Parque Nacional da Serra da Canastra (Delfinópolis, MG, Brasil).

---

## Estrutura da Tese de Doutorado

| Componente | Título / Tema | Manuscrito Canônico | Pasta |
| :--- | :--- | :--- | :--- |
| **00_Introduction** | *Introdução Geral e Revisão Bibliográfica* | [Texto](docs/00_introduction/general_introduction_thesis_181026.md) | [docs/00_introduction/](docs/00_introduction/) |
| **01_Chapter_1** | *A Haplotype-Resolved, Near Telomere-to-Telomere Genome Assembly of the Desiccation-Tolerant Plant Vellozia tubiflora* | [Manuscrito](docs/01_chapter_1_tubiflora/manuscripts/chapter_tubiflora_master_draft.md) | [docs/01_chapter_1_tubiflora/](docs/01_chapter_1_tubiflora/) |
| **02_Chapter_2** | *Genomas Organelares: Plastoma e Mitocôndria em Velloziaceae* | *(Contextualização na tese)* | [docs/00_introduction/](docs/00_introduction/) |
| **03_Chapter_3** | *Ancestral Gene-Family Expansion and Asymmetric Local Duplication in Two Vellozia Species with Contrasting Drought-Survival Strategies* | [Manuscrito](docs/03_chapter_3_macroevolution/manuscripts/chapter_macroevolution_article.md) | [docs/03_chapter_3_macroevolution/](docs/03_chapter_3_macroevolution/) |
| **04_Chapter_4** | *Genome-Wide Identification, Comparative Synteny, and Evolutionary Divergence of OSCA Mechanosensitive Ion Channels in Resurrection and Evergreen Vellozia* | [Manuscrito](docs/04_chapter_4_osca/drafts/chapter_2_osca_mechanosensation.md) | [docs/04_chapter_4_osca/](docs/04_chapter_4_osca/) |
| **05_Chapter_5** | *The Experience of Teaching Introductory Programming Skills to Bioscientists in Brazil* (*PLOS Comp. Biol.*, 2021) | [Manuscrito](docs/05_chapter_5_python/manuscripts/chapter_python_master_draft.md) | [docs/05_chapter_5_python/](docs/05_chapter_5_python/) |
| **06_Discussion** | *Discussão Geral Transversal e Conclusões da Tese* | [Texto](docs/06_general_discussion_and_conclusions/discussao_transversal_tese.md) | [docs/06_general_discussion_and_conclusions/](docs/06_general_discussion_and_conclusions/) |

---

## Pipelines Analíticos e Reprodutibilidade

Os códigos e scripts de bioinformática estão organizados em módulos analíticos reprodutíveis:

* **[pipelines/03_macroevolution/](pipelines/03_macroevolution/)**:
  - Delineamento de ortologia (OrthoFinder).
  - Filogenômica por supermatriz concatenada e modelo multiespécies coalescente (ASTRAL-II).
  - Datação molecular sob relógio relaxado calibrado por fósseis (MCMCtree).
  - Modelagem estocástica de ganho e perda de famílias gênicas (CAFE5, modelo M5 com distribuição Gamma).
  - Classificação de mecanismos de duplicação gênica e macrossintenia (MCScanX / JCVI).
  - Taxas de substituição não-sinônima e sinônima (PAML / codeml) em trios ortólogos polarizados por *Xerophyta schlechteri*.
  - Enriquecimento funcional (GO e KEGG) com correção de FDR e permutações estratificadas.

* **[pipelines/04_osca/](pipelines/04_osca/)**:
  - Identificação genômica e curadoria de domínios Pfam (PF02714, PF13967, PF14703 via HMMER e InterProScan).
  - Filogenia molecular e topologia transmembrana (IQ-TREE e Phobius/TMHMM).
  - Microssintenia comparativa e colinearidade física (MCScan).
  - Análise de intensidades de seleção (HyPhy RELAX) e taxas evolutivas pareadas (PAML YN00).
  - Perfis de expressão tecidual sob condições de campo (STAR, featureCounts, DESeq2).
  - Modelagem de redes de associação funcional (STRING API v12) e enriquecimento modular.
  - Arquitetura cis-regulatória e predição de promotores (PlantCARE).

---

## Organização do Diretório `docs/`

* **`docs/00_introduction/`** a **`docs/06_general_discussion_and_conclusions/`**: Manuscritos em formato Markdown com figuras de alta resolução embutidas, tabelas consolidadas e referências padronizadas (ABNT NBR 6023).
* **[docs/literature/](docs/literature/)**: Biblioteca de referências bibliográficas da tese, metadados OpenAlex e arquivos BibTeX (`.bib`).
* **[docs/qualification_and_forms/](docs/qualification_and_forms/)**: Roteiros e documentação institucional de qualificação.

---

## Disponibilidade de Dados

1. **Dados Genômicos Brutos e Montagens**:
   - Depositados no NCBI sob o BioProject **PRJNA984512**.
2. **Pacotes Suplementares**:
   - As tabelas suplementares completas de cada capítulo encontram-se disponíveis nos formatos `.xlsx` e `.tsv` nas respectivas pastas de `docs/` e `pipelines/`.
3. **Imagens de Alta Resolução**:
   - Disponíveis individualmente nos formatos vetoriais e rasterizados (`.svg`, `.pdf`, `.png`) nas pastas de figuras de cada capítulo.

---

## Como Citar

> CAVALHEIRO, Mariana Feitosa. **Genômica Comparativa e História Evolutiva de Velloziaceae: Adaptações à Limitação Hídrica e Mecanismos de Sobrevivência à Seca e Dessecação em Campos Rupestres**. 2026. Tese (Doutorado em Genética e Biologia Molecular) — Instituto de Biologia, Universidade Estadual de Campinas, Campinas, 2026.
