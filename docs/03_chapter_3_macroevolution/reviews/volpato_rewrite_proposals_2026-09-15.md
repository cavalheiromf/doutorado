# Propostas de reescrita — macroevolução

Estas propostas acompanham o [parecer rastreável](volpato_logical_scientific_review_2026-09-15.md). Os trechos estão em inglês para acompanhar o texto principal. São substituições localizadas e uma proposta de organização argumentativa; não constituem um manuscrito integral revisado. A terminologia cautelosa também segue a skill local `writing-style`.

## 1. Objetivo operacional proposto

Inserir ao final de uma Introdução que documente o contraste fisiológico e a lacuna de conhecimento. O arquivo examinado não contém essa Introdução; o parágrafo abaixo não substitui a fundamentação bibliográfica necessária.

> This study aimed to characterize gene-family size variation and duplication architecture across the sampled Velloziaceae genomes within a phylogenomic and temporal framework. We evaluated the stability of family-level turnover signals across model configurations, examined their reconstructed branch histories, and used genomic position and collinearity to assess structural support for selected copy-number differences between *Vellozia peripherica* and *V. tubiflora*. These analyses were used to prioritize candidates for investigating contrasting responses to water loss, while distinguishing genomic variation from evidence of a causal contribution to desiccation tolerance or avoidance.

Se a seleção pareada for integrada, acrescentar um objetivo separado:

> We also screened pairwise coding-sequence divergence between reciprocally unique *V. peripherica–V. tubiflora* ortholog pairs to identify candidates for subsequent tests of selective pressure.

## 2. Substituição da alegação de nó completamente livre — §1.3

> No direct calibration was assigned to the node separating the sampled *Xerophyta* and *Vellozia* lineages. Its age nevertheless remained conditional on the calibrated ancestral and descendant nodes, the joint time prior, the substitution model and the relaxed-clock assumptions. We compared prior-only and posterior distributions to describe the contribution of sequence data under this calibration scheme; this comparison does not establish independence from the surrounding temporal constraints.

O texto dos priors específicos deve ser reconciliado com as respectivas fontes antes de integrar a versão final. Não converter calibrações secundárias ou hipóteses biogeográficas em fósseis diretos por alteração de redação.

## 3. Proveniência do CAFE5 — substituir a afirmação de uso do cronograma high-ESS

> The archived CAFE5 runs used a time-calibrated tree with a root age of 138.484 Ma, a sampled *Xerophyta–Vellozia* divergence of 31.9147 Ma, and a *V. peripherica–V. tubiflora* divergence of 9.7362 Ma. These ages differ from the two-chain dating summary presented here. The reported CAFE5 results therefore refer to the archived input tree; their sensitivity to the updated chronogram has not been evaluated in this revision.

Os três valores foram conferidos nos relatórios CAFE5. Se as análises forem reexecutadas, substituir o parágrafo e atualizar todos os resultados dependentes.

## 4. Interpretação da datação — §§2.2 e 3

> Under the specified calibration scheme, the estimated divergence between the sampled *Xerophyta* and *Vellozia* lineages was 33.77 Ma, with a 95% equal-tailed credible interval of 22.41–48.11 Ma. This estimate is younger than the continental-separation interval invoked by the vicariance hypothesis discussed here. However, the comparison is conditional on the calibration scheme and does not identify the route, direction or timing of colonization. Post-breakup dispersal is a compatible explanation, but evaluating it against alternative biogeographic histories requires broader taxon sampling and explicit consideration of ancestral ranges and calibration sensitivity.

O rótulo “equal-tailed” corresponde ao script inspecionado. Harmonizar a Tabela 1 e a Figura S3 antes de integrar esse trecho. Não manter rótulos HPD nas figuras se os mesmos percentis forem utilizados. As referências biogeográficas existentes devem acompanhar a premissa de separação continental depois de verificadas; este parágrafo não valida suas datas externamente.

## 5. Comparação funcional — substituir a conclusão de ausência de paralelismo

> The annotated foregrounds showed different descriptive enrichment profiles among the sampled lineages. However, the direct comparison of expansion proportions between *V. tubiflora* and *X. viscosa* detected no terms passing the multiple-testing threshold. This result does not establish equivalence between the lineages and does not test the absence of parallel expansion. Shared reconstructed increases at the orthogroup level, differences in functional-term representation, and convergence in physiological function are distinct questions and should be evaluated separately. The functional interpretation of the energy-related foregrounds also remains provisional until the inconsistent annotations of OG0000317 and OG0000332 are reconciled.

Para os resultados direcionais, empregar a forma:

> Within the families with significant overall turnover, those showing Viterbi-reconstructed decreases on the focal branch were over-represented for the reported functional annotation. The enrichment statistic applies to term representation in this foreground and does not establish a separately tested branch-specific contraction.

Preservar os q-valores somente após conferir a origem de cada conjunto e anotação. Não alegar que a auditoria já revalidou os enriquecimentos.

## 6. Duplicações e suporte estrutural — §2.7

> The two genomes contained similar proportions of genes classified as WGD/segmental duplicates: 28.18% in *V. peripherica* and 28.27% in *V. tubiflora*. In contrast, the observed proportion assigned to tandem or proximal duplication was higher in *V. peripherica* (21.25%) than in *V. tubiflora* (15.96%). These classifications describe the duplication architecture of the annotated genomes. Similar WGD/segmental proportions do not independently establish the timing or shared origin of duplication events, whereas the local arrays in selected families provide structural context for their copy-number differences. Their contribution to contrasting water-loss responses remains to be tested.

Substituir o diagnóstico categórico de artefato:

> Several prioritized families contained gene models distributed across unplaced contigs. This organization leaves their copy-number interpretation unresolved and warrants checks for assembly redundancy, fragmented gene models and organellar sequence representation. Unplaced location alone does not establish that the copies are artifacts. Likewise, chromosomal anchoring supports positional interpretation but does not by itself establish gene-model completeness or functional activity.

## 7. Integração opcional da análise pareada de sequência

> The pair-specific analysis included 16,609 reciprocally unique ortholog pairs from 12,158 orthogroups. After the estimation filters, 233 pairs had ω > 1, including 180 without the additional operational warning flags. These estimates define a descriptive screening set rather than statistically confirmed cases of positive selection. Because an orthogroup can contain more than one qualifying pair, pairs and gene families represent different units of analysis. The pairwise estimates also do not identify the lineage in which the substitutions occurred and therefore cannot independently connect sequence change to either water-loss strategy.

Fonte local: `05_selection/pair_specific_2026-09-11/analysis_report.md`. Preservar no método as regras de ortologia, alinhamento, estimação e QC. Esta revisão não reexecutou esses cálculos.

## 8. Síntese final proposta

> The comparative analyses identify variation in gene-family size and duplication architecture among the sampled Velloziaceae genomes. Local tandem and proximal arrays provide structural support for selected copy-number differences between *V. peripherica* and *V. tubiflora*, while the turnover analyses distinguish family-level statistical evidence from reconstructed changes on individual branches. These results provide candidates for investigating the genomic basis of contrasting responses to water loss. Establishing their functional or adaptive contribution will require validated gene models, reconciled annotations and evidence connecting the candidates to responses during dehydration and rehydration. The current comparisons do not establish the ancestral desiccation phenotype or the causal origin of the contrasting strategies.

Esta síntese evita depender de uma rota biogeográfica comprovada, de ausência de convergência ou de funções bioquímicas ainda não reconciliadas. Sua integração não elimina as pendências factuais descritas no parecer.

## 9. Organização sugerida do capítulo

A Introdução deve construir a passagem entre o contraste fisiológico, as dimensões genômicas que podem ser comparadas e a pergunta operacional. Nos Resultados, a filogenia sustenta o contexto comparativo; a datação apresenta estimativas condicionais; o CAFE5 delimita o conjunto de famílias; a sintenia examina a organização dos candidatos; e a análise pareada, se incluída, acrescenta uma dimensão distinta de evolução de sequência. A Discussão deve desenvolver o significado e os limites dessa integração, com a repetição de números e coordenadas concentrada nas tabelas. A conclusão deve responder à pergunta de genômica comparada sem transformar a priorização de candidatos em demonstração de adaptação.
