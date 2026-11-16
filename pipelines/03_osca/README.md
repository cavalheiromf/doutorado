# Família Gênica OSCA em Velloziaceae (Capítulo 3 da Tese)

Este diretório contém os pipelines computacionais, análises genômicas, transcriptômicas e evolução molecular da família gênica OSCA (canais iônicos mecanossensíveis) nas espécies *Vellozia peripherica* e *Vellozia tubiflora*.

## Estrutura do Diretório

Para garantir reprodutibilidade e conformidade com repositórios leves de bioinformática, a organização segue o padrão modular:

- `workflow/scripts/`: Todos os scripts executáveis de análise (Python, R, Bash), prefixados por etapa (ex: `01_extract_sequences.py`).
- `00_data/`: Diretório local para dados brutos des-rastreados pelo `.gitignore` (genomas, leituras RNA-Seq).

### Etapas do Pipeline

Cada subdiretório de etapa contém os seus respectivos resultados finais processados, tabelas e figuras:
- `01_gene_identification/`: Identificação dos genes via HMMER e validação de domínios Pfam.
- `02_phylogeny/`: Alinhamento e árvore de Máxima Verossimilhança (IQ-TREE).
- `03_synteny/`: Análise de macrosintenia, microssintenia e mapeamento cromossômico (MCScan).
- `04_evolutionary_rates/`: Cálculo de taxas evolutivas e testes de seleção (PAML codeml/yn00, HyPhy RELAX e CONTRAST-FEL).
- `04_promoters/`: Análise de motivos cis-reguladores promotores (PlantCARE).
- `05_rnaseq/`: Matrizes consolidadas de contagem gênica e relatórios de controle de qualidade.
- `06_expression/`: Análise de expressão diferencial (DESeq2) e perfis teciduais.
- `07_ppi_network/`: Redes de interação proteína-proteína (STRING API v12) e enriquecimento funcional.
- `figures/`: Figuras finais consolidadas em formatos raster e vetorial (`.png`, `.svg`, `.pdf`).

## Como Reproduzir

Para reproduzir uma etapa específica, utilize o orquestrador `run_pipeline.sh` ou os scripts correspondentes em `workflow/scripts/`. Eles foram desenhados para ler os dados de entrada locais e gerar as tabelas e figuras de forma determinística. Para instruções completas de execução e dependências, consulte [`REPRODUCIBILITY.md`](../../REPRODUCIBILITY.md).
