# Capítulo 2: Família OSCA (Vellozia)

Este diretório contém as análises genômicas e transcriptômicas da família gênica OSCA (mecanossensores) nas espécies *Vellozia peripherica* e *Vellozia tubiflora*.

## Estrutura do Repositório (Refatorada)

Para garantir reprodutibilidade e evitar o acúmulo de arquivos intermediários pesados, a organização segue o padrão centralizado:

- `workflow/scripts/`: Todos os scripts geradores de análise (Python, R, Bash), prefixados por etapa (ex: `01_extract_sequences.py`).
- `00_data/`: (Se aplicável) Dados crus, incluindo leituras brutas de RNA-Seq.
- `docs/drafts/`: Versões do manuscrito e notas metodológicas.

### Etapas do Pipeline

Cada subdiretório de etapa contém os seus respectivos resultados finais ou dados estruturados (e um `README.md` local detalhando a etapa, se aplicável):
- `01_gene_identification/`: Identificação dos genes via HMMER e validação de domínios.
- `02_phylogeny/`: Alinhamento e árvore ML (IQ-TREE).
- `03_synteny/`: Análise de macrosintenia (MCScanX) e mapeamento cromossômico.
- `04_evolutionary_rates/`: Cálculo de taxas evolutivas (PAML, HyPhy).
- `04_promoters/`: Análise de motivos promotores (PlantCARE).
- `05_rnaseq/`: Matrizes finais de contagem (`results/05_counts/`) e relatórios de QC. (Arquivos intermediários de alinhamento e trimagem foram removidos para economizar espaço).
- `06_expression/`: Expressão diferencial (DESeq2) e plotagens.
- `07_ppi_network/`: Redes de interação proteína-proteína (STRING).
- `figures/`: Figuras finais para a publicação.

## Como Reproduzir

Para reproduzir uma etapa específica, utilize os scripts correspondentes em `workflow/scripts/`. Eles foram desenhados para ler os dados das etapas anteriores (ou de `00_data/`) e escrever na pasta de resultados. 
Arquivos gigantescos gerados no processo (como alinhamentos `.bam` do RNA-Seq) não são mantidos rastreados, priorizando o armazenamento das matrizes de contagem consolidadas.
