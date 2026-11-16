# Arquitetura e Navegação do Repositório

Este repositório reúne os pipelines bioinformáticos, rotinas de evolução molecular e recursos de reprodutibilidade computacional da tese de doutorado de **Mariana Feitosa Cavalheiro**:

> **"Comparative genomics and OSCA gene family diversification in Vellozia species with contrasting responses to water limitation"**  
> *(Genômica comparativa e diversificação da família gênica OSCA em espécies de Vellozia com respostas contrastantes à limitação hídrica)*  
> Programa de Pós-Graduação em Genética e Biologia Molecular (PPG-GBM), Instituto de Biologia, UNICAMP.

---

## 1. Pipelines Analíticos (`pipelines/`)

Módulos bioinformáticos dedicados à execução e reprodutibilidade científica:
* **[pipelines/02_macroevolution/](pipelines/02_macroevolution/)**: Rotinas de ortologia (OrthoFinder), datação molecular com relógio relaxado (MCMCtree), filogenômica, modelagem estocástica multi-$\lambda$ com Gamma de ganho e perda gênica (CAFE5 M5), modos de duplicação gênica (MCScanX/JCVI) e enriquecimento funcional com 10.000 permutações estratificadas.
* **[pipelines/03_osca/](pipelines/03_osca/)**: Rotinas de busca estrutural HMMER/InterProScan, filogenia de máxima verossimilhança (IQ-TREE), microssintenia e cluster em tandem (MCScan), seleção molecular (HyPhy RELAX e CONTRAST-FEL com saneamento de gaps), taxas de substituição de códons (PAML codeml/yn00), expressão tecidual a campo (STAR/DESeq2) e redes de interação proteína-proteína (STRING API v12).

*(Para assegurar compatibilidade contínua com chamadas de scripts históricos, os links simbólicos de conveniência `chapter_macroevolution_review` e `chapter2_osca` apontam diretamente para `pipelines/02_macroevolution` e `pipelines/03_osca`, respectivamente).*

---

## 2. Dados e Metadados (`data/`)

* **[`data/README.md`](data/README.md)**: Inventário completo de dados de entrada, identificadores de acesso do NCBI BioProject (**PRJNA984512**) e instruções para organização local.
* **[`data/checksums.sha256.example`](data/checksums.sha256.example)**: Modelo de integridade criptográfica SHA-256 para validação dos arquivos locais.

---

## 3. Guia de Reprodutibilidade

Para instruções passo a passo de configuração do ambiente Conda/Mamba, execução sequencial ou via SLURM e reprodução de figuras, consulte [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md).
