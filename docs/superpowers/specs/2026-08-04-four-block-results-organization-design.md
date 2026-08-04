# Organização dos resultados em quatro blocos narrativos

## Objetivo

Reorganizar `reports/results_working_document.md` em quatro blocos científicos,
preservando os resultados, valores numéricos, interpretações, limitações,
arquivos de origem e drafts em inglês já existentes.

## Escopo

A alteração será restrita ao documento de resultados. Diretórios em
`analyses/`, scripts, tabelas, figuras e demais relatórios não serão movidos,
renomeados ou editados.

## Estrutura aprovada

### Bloco I — Conservação e classificação da família OSCA

- Identificação dos genes OSCA.
- Relações filogenéticas.
- Questão orientadora: quais membros compõem a família e como se relacionam?

### Bloco II — Evolução e divergência genômica

- Sintenia e evolução da família gênica.
- Taxas evolutivas.
- Questão orientadora: quais eventos de conservação, duplicação e divergência
  explicam a organização atual da família?

### Bloco III — Conservação e divergência regulatória

- Elementos cis-regulatórios em promotores.
- RNA-seq e expressão tecido-específica.
- Questão orientadora: como a arquitetura regulatória e a expressão variam
  entre genes, tecidos e espécies?

### Bloco IV — Priorização funcional

- Redes de associação funcional entre proteínas.
- Comparações estruturais, quando a seção for incorporada.
- Genes candidatos e síntese integrada, quando essas seções forem incorporadas.
- Questão orientadora: quais genes e hipóteses merecem validação experimental?

## Estratégia editorial

1. Substituir a lista linear de seções por um sumário organizado nos quatro
   blocos.
2. Inserir uma introdução curta em cada bloco, explicitando sua pergunta
   científica e sua relação com o bloco anterior.
3. Rebaixar as seções numeradas existentes para subseções dos blocos, mantendo
   a numeração 1–9 e ajustando os níveis Markdown de seus subtítulos.
4. Preservar a ordem interna de evidências observadas, interpretação, draft em
   inglês, limitações e conexões futuras.
5. Manter afirmações preditivas claramente separadas de validação funcional.
   Em particular, expressão tecido-específica não será descrita como resposta
   direta à seca, e redes ou modelos estruturais não serão tratados como
   validação experimental.
6. Não condensar, excluir ou alterar resultados científicos nesta etapa.

## Critérios de aceitação

- O documento apresenta exatamente quatro blocos de segundo nível.
- As seções numeradas 1–7 permanecem completas e na ordem atual.
- As seções planejadas 8–9 permanecem explicitamente identificadas como
  futuras.
- Todos os valores, tabelas, arquivos de origem, limitações e drafts existentes
  são preservados.
- A hierarquia Markdown não salta níveis dentro dos quatro blocos.
- Nenhum arquivo fora de `reports/results_working_document.md` é alterado pela
  implementação.

## Verificação

- Comparar o diff para confirmar que as mudanças são estruturais e de
  transição narrativa.
- Conferir a sequência dos cabeçalhos com `rg '^#{1,4} '`.
- Verificar que números de tabelas, valores e caminhos de origem não foram
  removidos.
- Revisar as introduções dos blocos para evitar conclusões funcionais além das
  evidências disponíveis.
