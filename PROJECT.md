# Arquitetura e Navegação do Repositório

Este repositório reúne os recursos genômicos, pipelines bioinformáticos e manuscritos da tese de doutorado de **Mariana Feitosa Cavalheiro**.

---

## 1. Manuscritos e Documentação (`docs/`)

Os capítulos da tese encontram-se estruturados por ordem de apresentação:
* **[00_introduction/](docs/00_introduction/)**: Introdução Geral e Revisão de Literatura da tese.
* **[01_chapter_1_tubiflora/](docs/01_chapter_1_tubiflora/)**: Montagem genômica quase telômero-a-telômero (*near-T2T*) de *Vellozia tubiflora*.
* **[03_chapter_3_macroevolution/](docs/03_chapter_3_macroevolution/)**: Dinâmica macroevolutiva de famílias gênicas e duplicações locais em *Vellozia*.
* **[04_chapter_4_osca/](docs/04_chapter_4_osca/)**: Caracterização evolutiva e expressão da família de canais mecanossensíveis OSCA.
* **[05_chapter_5_python/](docs/05_chapter_5_python/)**: Artigo pedagógico sobre ensino de programação para biocientistas (*PLOS Comp. Biol.*).
* **[06_general_discussion_and_conclusions/](docs/06_general_discussion_and_conclusions/)**: Síntese transversal e conclusões integradas da tese.
* **[literature/](docs/literature/)**: Biblioteca de referências, resumos bibliográficos e arquivos `.bib`.
* **[qualification_and_forms/](docs/qualification_and_forms/)**: Documentos e roteiros institucionais.

---

## 2. Pipelines Analíticos (`pipelines/`)

Módulos bioinformáticos dedicados à execução e reprodutibilidade científica:
* **[pipelines/03_macroevolution/](pipelines/03_macroevolution/)**: Rotinas de ortologia (OrthoFinder), datação molecular (MCMCtree), filogenômica, modelagem de ganho e perda gênica (CAFE5) e taxas evolutivas (PAML).
* **[pipelines/04_osca/](pipelines/04_osca/)**: Rotinas de busca HMMER/InterProScan, filogenia (IQ-TREE), microssintenia (MCScan), seleção molecular (HyPhy RELAX/Contrast-FEL), expressão tecidual (STAR/DESeq2) e redes de interação (STRING).

*(Para assegurar compatibilidade contínua com scripts históricos, os links simbólicos de conveniência `chapter2_osca` e `chapter_macroevolution_review` apontam diretamente para suas respectivas pastas em `pipelines/`).*
