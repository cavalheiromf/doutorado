# Revisão lógica e científica — capítulo de macroevolução

> Atualização: o manuscrito integrado foi localizado posteriormente em `teamwork/01_drafts_and_outlines/chapter_macroevolution_master_draft.md`. Sua revisão e as decisões de integração estão no [parecer do manuscrito mestre](volpato_master_review_2026-09-15.md). O diagnóstico abaixo refere-se ao relatório técnico originalmente examinado.

Data: 15 de setembro de 2026. Método: skill `volpato-logical-scientific-writing`, localizada em `chapter2_osca/.agents/skills/volpato-logical-scientific-writing/`. Trata-se de uma interpretação operacional dos princípios públicos associados à Escrita Científica Lógica de Gilson Volpato, sem vínculo oficial com o autor.

## 1. Escopo e parecer

O texto principal examinado integralmente foi [cafe5_methodology_and_results_revised.md](../../04_gene_families/cafe5_methodology_and_results_revised.md), que integra Métodos, Resultados e Interpretação sobre filogenia, datação, evolução de famílias e sintenia. Esse arquivo não contém Introdução nem uma Conclusão autônoma. Assim, a avaliação do primeiro argumento é necessariamente uma proposta de estrutura, não uma revisão de uma introdução existente.

Foram consultados o relatório crítico dos eixos comparativos, o resumo v2, a auditoria de sintenia, o README de seleção e o relatório `pair_specific_2026-09-11/analysis_report.md`. Foram confrontados pontos selecionados com a tabela mestre v2, o resumo de convergência MCMCtree, o script que o produz, a árvore calibrada de entrada, a tabela de concordância IQ-TREE e a primeira linha dos 21 arquivos `*report.cafe` em `cafe5_results/rerun`. Não se executaram novamente as análises, não se recalcularam todas as estatísticas e não se validou integralmente a bibliografia. Os relatórios históricos foram tratados como contexto, não como resultados atuais intercambiáveis.

**Parecer:** o material contém resultados úteis e ressalvas metodológicas bem formuladas, especialmente a distinção entre significância por família, reconstrução por ramo e suporte estrutural. Entretanto, a cadeia argumentativa ainda não está pronta para uma versão final: há incompatibilidades documentais e conclusões que ultrapassam os testes apresentados. A prioridade é reconciliar a proveniência das análises e então ajustar a interpretação. Uma revisão exclusivamente estilística preservaria erros relevantes.

O manuscrito original permanece preservado. As propostas de reescrita estão em [volpato_rewrite_proposals_2026-09-15.md](volpato_rewrite_proposals_2026-09-15.md); são propostas editoriais, não uma versão final com resultados revalidados.

## 2. Mapa dos dois argumentos

### Argumento da Introdução

| Elo | Estado no arquivo | Encaminhamento |
| --- | --- | --- |
| Premissa: estratégias contrastantes de resposta à perda de água nas espécies focais | Implícita em métodos e interpretação | Apresentar o contraste e suas fontes fisiológicas antes das análises. |
| Premissa: contagem de genes, história de duplicação e evolução de sequência representam dimensões diferentes | Explícita em ressalvas dispersas | Reunir a distinção conceitual na construção do problema. |
| Lacuna: quais diferenças de repertório possuem suporte estatístico e estrutural nas espécies amostradas? | Implícita | Formular como problema de genômica comparada; não prometer demonstrar a origem da tolerância. |
| Objetivo operacional | Ausente como enunciado central | Caracterizar diferenças de famílias e arquitetura de duplicação em uma filogenia temporal, distinguindo candidatos de evidência funcional. |
| Justificativa de seleção pareada | Ausente do texto principal | Incluir somente se o capítulo integrar evolução de sequência, com objetivo próprio de triagem descritiva. |

### Argumento de Métodos a Conclusão

| Elo | Estado | Avaliação |
| --- | --- | --- |
| Objetivo → filogenia e datação | Implícito | O arcabouço é pertinente, mas sete táxons não representam toda a radiação da família. |
| Datação → CAFE5 | Explícito, documentalmente incompatível | Os relatórios do CAFE5 contêm outra árvore temporal; ver C1. |
| CAFE5 → famílias com evidência de turnover | Explícito | A separação entre significância por família e direção reconstruída é um ponto forte. |
| Famílias → funções | Explícito, parcialmente inconsistente | Há divergências de anotação e inferências funcionais excessivas; ver C4–C6. |
| Famílias → sintenia | Explícito | A organização física sustenta candidatos estruturais, sem provar adaptação ou autenticidade de todos os modelos gênicos. |
| Comparações → estratégia hídrica | Parcialmente implícito | Espécie, história filogenética e fenótipo não estão separados por desenho causal ou amostragem replicada. |
| Discussão → síntese | Explícito na seção 3 | A discussão reconhece limites, mas também afirma dispersão necessária, ausência de paralelismo e adaptações ancestrais sem testes correspondentes. |

A conclusão defensável é a identificação de diferenças de repertório e de organização de duplicatas entre os genomas amostrados, com candidatos priorizados por evidências complementares. A relação causal dessas diferenças com tolerância ou evitação permanece uma hipótese.

## 3. Achados críticos

### C1. A árvore atribuída ao CAFE5 não corresponde à árvore registrada nas execuções

**Local:** §§1.3, 2.2 e 3. O texto diz que `velloziaceae_chronogram_high_ess.tre`, com raiz de 138,43 Ma, foi fornecido às análises subsequentes.

**Evidência:** os 21 relatórios CAFE5 examinados registram a mesma árvore, com raiz de 138,484 Ma, nó *Xerophyta–Vellozia* de 31,9147 Ma e par *Vellozia* de 9,7362 Ma. O resumo high-ESS apresenta, respectivamente, 138,4309, 33,7699 e 9,6839 Ma. Os scripts SLURM apontam para `04_gene_families/velloziaceae_ultrametric.tre`.

**Diagnóstico e risco:** trata-se de uma divergência de proveniência confirmada, não de um simples arredondamento. Não demonstra que os resultados CAFE5 sejam inválidos; demonstra que não foram documentados com a mesma árvore da datação apresentada.

**Correção:** descrever a árvore efetivamente usada e separar a atualização da datação. Se a intenção for usar o cronograma high-ESS, reexecutar CAFE5 e suas etapas dependentes antes de atribuir os resultados à nova árvore. Não substituir silenciosamente a árvore mantendo os valores anteriores.

**Decisão:** pendente de integração; recomendação factual sustentada pelos relatórios.

### C2. Nó sem calibração própria é apresentado como inferência sem restrições

**Local:** §1.3, “completely unconstrained (free node)” e “unbiased empirical estimation”; §§2.2, 3 e legenda S3, rejeição definitiva de vicariância e dispersão necessária.

**Evidência:** a árvore de entrada calibra o ancestral do nó focal em 75–90 Ma e o descendente em 2–25 Ma. O nó focal não tem limite inserido diretamente, mas participa da distribuição conjunta de idades e das restrições de ordenamento. Os próprios resultados apresentam uma distribuição a priori para ele.

**Diagnóstico e risco:** a idade posterior é uma inferência condicionada às calibrações e ao modelo. Um nó não calibrado diretamente não oferece, por isso, um teste independente de toda a informação temporal imposta. A idade da divergência dos táxons amostrados também não determina, isoladamente, rota, direção ou data de colonização. A hipótese biogeográfica precisa ser explicitada para que se avalie se o nó escolhido realmente a testa.

**Correção:** usar “without a direct calibration”. Apresentar a estimativa como condicional, testar sensibilidade às calibrações e tratar dispersão como hipótese compatível. Auditar separadamente a origem de cada intervalo: fóssil direto, calibração secundária ou premissa biogeográfica. Não chamar todas as restrições de paleontologicamente validadas sem essa rastreabilidade.

**Decisão:** pendente; reescrita proposta. O [tutorial oficial de MCMCtree](https://github.com/abacus-gene/paml-tutorial/blob/main/mcmctree-approxlnL-aa/README.md) distingue calibrações especificadas e distribuições marginais efetivas e recomenda examinar o prior conjunto.

### C3. Intervalos e diagnósticos de datação não estão corretamente reconciliados

**Local:** §2.2, Tabela 1 e legenda S3; `03_dating/analyze_mcmctree_chains.py`, função `main`.

**Evidência:** o script usa `np.percentile(comb, 2.5)` e `np.percentile(comb, 97.5)`, embora nomeie as colunas como HPD. Esses são intervalos de caudas iguais. Na Tabela 1, as médias das cadeias para o nó focal são 33,52 e 34,02 Ma, com ESS 138 e 124; no TSV são 33,2580 e 34,2818 Ma, com ESS 99,6052 e 129,4764. O ESS combinado reportado é 261,8409. A tabela também apresenta μ = 0,260, enquanto o TSV contém 0,2637025. Há outras diferenças por cadeia.

**Diagnóstico e risco:** os valores de diferentes versões estão misturados; a terminologia do intervalo não corresponde ao cálculo. ESS combinado superior a 200 não significa ESS superior a 200 em cada cadeia. O script concatena as cadeias ao calcular o ESS combinado; esse diagnóstico merece revisão própria, não apenas renomeação.

**Correção:** estabelecer uma única versão de saída, gerar a tabela automaticamente e informar o tipo de intervalo efetivamente calculado. Se HPD for necessário, calculá-lo explicitamente. Informar os ESS por cadeia e moderar “virtually complete convergence” e “exceptionally high”. Correlação entre médias de nós de idades muito diferentes não deve ser a evidência principal de convergência.

**Decisão:** pendente; não corrigir apenas a prosa deixando figuras e tabela divergentes. A [documentação oficial de HPDinterval](https://search.r-project.org/CRAN/refmans/coda/html/HPDinterval.html) descreve o cálculo de intervalos de maior densidade, distinto da seleção fixa dos percentis 2,5 e 97,5.

### C4. Contagens de três famílias na Tabela 3 divergem da tabela mestre

**Local:** Tabela 3, linha “NDH module”.

| Ortogrupo | Xvis no manuscrito | Xvis na tabela mestre | Abra no manuscrito | Abra na tabela mestre |
| --- | ---: | ---: | ---: | ---: |
| OG0000014 | 14 | 30 | 9 | 4 |
| OG0000156 | 2 | 8 | 1 | 3 |
| OG0000278 | 0 | 2 | 0 | 1 |

**Evidência:** `comparative_axes/comparative_families_master_table_v2.tsv`, colunas `Count_Xvis` e `Count_Abra`; para OG0000014, o relatório da réplica k2/rep02 também registra Xvis = 30 e Abra = 4.

**Diagnóstico e risco:** diferenças de presença e ausência modificam a interpretação evolutiva. Não são detalhes editoriais.

**Correção:** reconciliar a Tabela 3 com a matriz de entrada da execução escolhida e verificar as demais linhas antes de publicar. Preservar a origem de cada número.

**Decisão:** pendente; os valores acima são divergências verificadas, não novos resultados calculados.

### C5. As anotações de OG0000317 e OG0000332 não são consistentes entre documentos

**Local:** §2.6, Tabela 3, §2.7 e seção 3.

**Evidência:** o manuscrito associa as duas famílias a NADH desidrogenase. Na tabela mestre, `EggNOG_Description` registra “Pre-mRNA-splicing factor” para OG0000317 e “Glycine-rich RNA-binding protein” para OG0000332. A auditoria de sintenia também as descreve como fator de splicing e proteína de ligação a RNA. OG0000317 está sem ortólogo de Arabidopsis recuperado nesse campo da tabela; OG0000332 contém AT3G23830.1, AT4G13850.1 e AT5G47320.1.

**Diagnóstico e risco:** a narrativa usa funções não reconciliadas para interpretar vias energéticas. A divergência não permite decidir automaticamente qual anotação é correta, mas impede tratar a função NDH como estabelecida.

**Correção:** rastrear identificadores, fontes de anotação e associação a GO/KEGG gene a gene. Revisar o enriquecimento se houver mapeamento incorreto. Até lá, retirar essas famílias dos exemplos funcionais de NDH e identificá-las como anotações pendentes de reconciliação.

**Decisão:** pendente de auditoria funcional; não substituí automaticamente uma função por outra.

### C6. Teste de diferença é convertido em teste de ausência de paralelismo

**Local:** §2.6 e seção 3. O texto relata zero termos significativos no contraste Vtub–Xvis, mas conclui “no statistically supported parallel expansion” e que tolerância não evoluiu por expansão paralela de módulos idênticos.

**Diagnóstico e risco:** o contraste apresentado testa diferenças de proporção. Sua não significância não demonstra equivalência, ausência de paralelismo nem mecanismos distintos. Enriquecimento significativo em uma linhagem e não significativo em outra também não demonstra diferença entre elas. O resumo v2, adicionalmente, registra 28 famílias com mudanças positivas reconstruídas em pelo menos duas espécies tolerantes; isso é um padrão descritivo em outro nível, não prova de convergência adaptativa.

**Correção:** afirmar apenas que o contraste não detectou diferenças após FDR. Separar perfis descritivos por linhagem, compartilhamento de famílias e teste de convergência. Excluir “ancestral defense adaptations” e “reinforcement” fisiológico quando a evidência é contagem anotada.

**Decisão:** pendente; proposta de parágrafo fornecida no arquivo de reescritas.

### C7. Significância do enriquecimento é atribuída à contração de um ramo

**Local:** §2.6, “oxidative phosphorylation in X. viscosa underwent significant directional contraction”.

**Diagnóstico e risco:** o q apresentado é de sobre-representação funcional em um conjunto definido por reconstrução Viterbi. Não constitui teste de contração da via nem de cada família no ramo. O texto contradiz suas próprias ressalvas metodológicas.

**Correção:** “Families with reconstructed decreases on the X. viscosa branch were over-represented for oxidative phosphorylation annotations”. Acrescentar a pendência das anotações discutida em C5.

**Decisão:** pendente; alteração textual recomendada sem mudar o q reportado.

### C8. Posição em contigs não ancorados é tratada como prova de artefato

**Local:** §2.7, item 7, “were found to be artifacts of assembly contiguity”; Tabela 3, OG0000301.

**Diagnóstico e risco:** modelos em contigs separados podem refletir limitações de montagem, duplicatas reais ou sequências organelares; localização não demonstra qual explicação é correta. Em sentido inverso, ancoragem cromossômica não demonstra que todo modelo corresponde a uma cópia funcional intacta.

**Correção:** descrever suporte estrutural ainda não resolvido e risco de redundância ou fragmentação. Reservar “artifact” para validação de cobertura, sequência, continuidade ou outra evidência específica. Reavaliar enriquecimentos com e sem famílias sinalizadas.

**Decisão:** pendente; reescrita proposta.

## 4. Achados relevantes

### R1. Proporções WGD/segmental semelhantes não estabelecem um evento ancestral compartilhado

**Local:** §2.7, Tabela 4, legenda da Figura 3 e seção 3. A fração próxima de 28,2% é uma observação; “shared ancestral polyploid footprint” acrescenta uma interpretação temporal. Colinearidade entre genomas aumenta o contexto estrutural, mas os totais não datam eventos nem excluem histórias distintas de perda e duplicação. Restringir a comparação às duas espécies e deixar a atribuição a WGD ancestral condicionada à história dos blocos e duplicações. **Decisão: pendente.**

### R2. Diferenças descritivas são chamadas de significativas e de retenção histórica

**Local:** §2.7, “diverged significantly”; Tabela 4, fração de singletons. Há 21,25% versus 15,96% de genes classificados como tandem/proximais, mas o trecho não apresenta teste para essa diferença. Uma diferença no complemento anotado não estima diretamente taxas de duplicação ou retenção. Usar “a higher observed proportion” e evitar um teste ingênuo que trate genes da mesma família como réplicas independentes. **Decisão: pendente.**

### R3. Uma espécie evitante não permite separar efeito do fenótipo de efeito de linhagem

**Local:** §§1.6, 2.6 e seção 3. O contraste pode priorizar candidatos associados às espécies comparadas, mas não isola uma assinatura causal ou geral de evitação. Explicitar essa limitação no objetivo e na conclusão e documentar as fontes da classificação fenotípica de cada espécie, inclusive A. bracteata. **Decisão: pendente.**

### R4. Amostragem reduzida é narrada como história de clados inteiros

**Local:** §§1.2, 2.1 e 2.2, “Pan-Velloziaceae radiation”, “all remaining Velloziaceae”, “explosive radiation”. Restringir enunciados aos táxons amostrados. O nó entre duas espécies de Vellozia não é automaticamente a idade da coroa do gênero, e uma estimativa de divergência não é teste de diversificação acelerada. Auditar também os rótulos crown angiosperms/monocots e o mapeamento das calibrações: o ancestral comum dos representantes amostrados não deve ser equiparado a toda a coroa sem justificativa filogenética. **Decisão: pendente.**

### R5. Fluxo atual é dominado por procedimentos, com repetição de candidatos

**Local:** §§2.3–2.5, Tabela 3, §2.7 e seção 3. O rigor dos diagnósticos merece ser preservado, mas o texto repete coordenadas, contagens e funções. Organizar resultados pelas perguntas: qual arcabouço filogenético; qual conjunto de famílias é estável; quais mudanças têm contexto estrutural; qual relação com fenótipo permanece possível. Manter os detalhes completos na tabela e reduzir a repetição em prosa. **Decisão: pendente.**

### R6. A seleção pareada precisa permanecer uma linha de evidência distinta

**Local:** `05_selection/README.md` e relatório de 11/09. A versão atual apresenta 16.609 pares, 233 com ω > 1 e 180 sem os avisos operacionais. O relatório delimita corretamente que esses não são casos estatisticamente confirmados de seleção positiva e que o método não localiza a mudança em uma linhagem. Preservar essas ressalvas ao integrar ao capítulo; não cruzar os números de pares com os de ortogrupos como se fossem a mesma unidade. Os arquivos anteriores ao reparo de códons são históricos. **Decisão: manter a cautela do relatório; integração pendente.**

## 5. Achados editoriais e de apresentação

**E1 — Figuras e tabelas.** Há duas figuras identificadas como Figure 1: workflow e filogenômica. A legenda da segunda anuncia três métricas e lista quatro. A Tabela 3 tem sete colunas de cabeçalho, mas oito células no separador Markdown. Renumerar o workflow ou movê-lo ao suplemento, corrigir chamadas e conferir a renderização. **Decisão: pendente.**

**E2 — Adjetivação.** Retirar “authoritative”, “absolute”, “overwhelming” e equivalentes. Os valores de suporte comunicam melhor a força da evidência. A completude não é uniformemente excepcional: o próprio texto informa 15,33% de gaps em Xvis. **Decisão: pendente.**

**E3 — Definição de gCF.** Definir o denominador como árvores decisivas. Neste conjunto, `concordance_7taxa.cf.stat` registra gN = 1.513 nos quatro ramos; portanto, os números apresentados são compatíveis, mas a definição geral precisa de precisão. A [documentação do IQ-TREE](https://www.iqtree.org/doc/Concordance-Factor) explicita esse denominador. **Decisão: pendente.**

**E4 — Escala temporal.** Não reduzir o intervalo 22,41–48,11 Ma a uma localização exclusivamente oligocênica nem o intervalo 5,85–15,72 Ma a uma localização exclusivamente no Mioceno tardio. Distinguir a média e a amplitude do intervalo; harmonizar texto e legendas. **Decisão: pendente.**

## 6. Ordem de integração e limites residuais

A primeira etapa é fixar a proveniência da árvore, das contagens e das anotações usadas. Em seguida, reconciliar tabela e figuras de datação, incluindo nomenclatura dos intervalos e diagnósticos por cadeia. A terceira etapa é reavaliar os exemplos funcionais e, se necessário, os enriquecimentos. Só então deve ser integrada a redação final de Resultados e Discussão. As correções de inferência C2, C6–C8 e R1–R4 já possuem direção editorial clara; não dependem de inventar novos resultados.

A discussão deve partir da contribuição mais sustentada: diferenças na organização e no tamanho de famílias nos genomas comparados. As explicações sobre estratégia hídrica devem aparecer como hipóteses derivadas dessa evidência, acompanhadas das observações que ainda faltam para distingui-las. O texto não deve concluir ausência de convergência nem origem causal da tolerância a partir dos contrastes atuais.

A cadeia completa permanece parcialmente aberta porque a Introdução não está no arquivo examinado e há divergências factuais relevantes. Esta revisão fornece diagnóstico e propostas concretas, mas não certifica todos os números, parâmetros, fontes bibliográficas, fósseis ou modelos. As figuras não foram inspecionadas visualmente nem regeneradas. Nenhuma reanálise computacional foi realizada.


## Atualização da proveniência funcional

A conferência posterior detalha a origem das anotações discutidas em C5: os rótulos NDH são rastreáveis aos membros de Arabidopsis usados no KEGG, enquanto splicing/RNA-binding provêm de Vellozia. A divergência não comprova erro de mapeamento. Ver [a reconciliação das fontes e posições gênicas](annotation_provenance_2026-09-15.md).
