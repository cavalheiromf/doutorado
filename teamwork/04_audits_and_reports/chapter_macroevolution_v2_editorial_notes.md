# Notas editoriais da versão 2

## Escopo e estrutura

Revisão do texto científico em inglês, preservando o arquivo original. A versão 2 foi organizada em torno da seguinte sequência: contexto evolutivo de Velloziaceae; contraste entre as estratégias hídricas das duas espécies de *Vellozia*; mudanças no número de cópias e duplicações locais; conservação predominante das sequências codificantes; síntese das implicações biológicas.

A introdução deve estabelecer a pergunta sem antecipar uma origem ancestral da tolerância à dessecação. Os métodos devem manter as decisões que definem os conjuntos analisados. Os resultados devem apresentar apenas os padrões necessários à interpretação. A discussão deve distinguir a história das famílias gênicas da história do fenótipo, integrando as diferenças estruturais e a divergência de sequências sem transformar associações em mecanismos demonstrados.

Foram retirados o resultado negativo dos 343 pares com anotação PPR, o histórico da reanálise, as contagens de filas de revisão, a lista extensa de candidatos individuais e as extrapolações sobre custos fisiológicos, direção da dispersão e adaptação confirmada. Os arquivos analíticos permanecem como registro técnico; esta revisão não iniciou novas análises.

## Decisões científicas e fontes locais

Os resultados de Ka/Ks foram conferidos com [summary.json](../../chapter_macroevolution/05_selection/pair_specific_2026-09-11/summary.json): 16.609 pares focais estritamente 1:1, 16.567 estimativas retidas, 233 razões acima de um e mediana de 0,2852. A definição permite ortólogos e cópias adicionais em outras espécies; exige unicidade recíproca entre as duas espécies focais. A discussão distingue esse conjunto das famílias com duplicações, que não são representadas integralmente pelo contraste 1:1. O texto não atribui significância estatística ou direção de linhagem às razões acima de um.

Os totais de expansão e contração correspondem a [Foreground_sizes_TierA.tsv](../../chapter_macroevolution/04_gene_families/functional_enrichment/results_final_simplify/Foreground_sizes_TierA.tsv), com o universo e os critérios descritos em [comparative_axes_v2_summary.md](../../chapter_macroevolution/04_gene_families/comparative_axes/comparative_axes_v2_summary.md). Foram usados os resultados da análise calibrada v2; relatórios anteriores que descrevem outros modelos e universos não foram combinados com esses totais. A conferência editorial não substitui uma revalidação dos ajustes do CAFE5.

Os exemplos funcionais foram conferidos diretamente em [comparative_families_master_table_v2.tsv](../../chapter_macroevolution/04_gene_families/comparative_axes/comparative_families_master_table_v2.tsv). Essa tabela descreve OG0000306 como "Protein kinase domain", apesar de um relatório estrutural chamá-lo de DREB. Por isso, a versão 2 usa apenas a descrição de domínio presente na tabela atual. OG0000281 aparece como "Uncharacterized protein" nessa mesma tabela e não foi apresentado como UDP-glicosiltransferase. Os exemplos de fatores de splicing e proteínas de ligação a RNA correspondem a OG0000317 e OG0000332. Essas descrições continuam sendo inferências por homologia.

As proporções de duplicatas locais e os parâmetros do classificador foram obtidos do [relatório de integração estrutural](../../chapter_macroevolution/04_gene_families/synteny/duplications/audit_and_comparative_integration_report.md). As contagens representam genes classificados, não eventos de duplicação datados. Não foi mantida a interpretação de que ancoragem cromossômica de sequências com anotação organelar demonstra função plastidial ou maior atividade fotossintética.

## Pendências de proveniência preservadas fora da narrativa

A datação ainda requer reconciliação entre versões, como documentado na [avaliação independente](avaliacao_independente_macroevolution_2026-09-10.md). Para evitar substituir resultados durante uma revisão editorial, foram preservadas as médias 31,92 e 9,74 Ma e as faixas 19,26-43,66 e 5,29-15,03 Ma da tabela [mcmctree_node_ages_summary.tsv](../../chapter_macroevolution/03_dating/mcmctree_node_ages_summary.tsv), nas colunas identificadas como HPD95. O arquivo também contém outras colunas de intervalo; a síntese combinada de cadeias apresenta médias diferentes. A versão 2 emprega o termo genérico "95% credible range", sem afirmar que o cálculo de HPD foi validado. A seleção das cadeias finais, a origem e o cálculo dos intervalos e a fundamentação de cada calibração precisam ser reconciliados antes da submissão. Não foram mantidas as afirmações de cinco calibrações fósseis independentes, independência dos priors, ESS superior a 200 em todas as cadeias ou refutação conclusiva da vicariância.

A classificação fisiológica das espécies focais foi mantida conforme o desenho do projeto. Alcantara et al. (2015) foi usado como contexto de comparações fisiológicas na família, sem lhe atribuir medições específicas de *V. peripherica* e *V. tubiflora*. Foram retiradas afirmações sobre mortalidade, potencial hídrico e desempenho dessas espécies que não estavam sustentadas por evidência específica conferida nesta revisão.

A versão 2 contém o texto científico, a autoria e as referências utilizadas. Declarações de financiamento, aprovação, depósito público e disponibilidade de dados não foram transferidas como fatos verificados. Em particular, o DOI Zenodo com sequência 12345678 do original não foi reproduzido. A versão destinada à submissão precisará das declarações confirmadas e do inventário final de acessos e versões dos genomas. A versão exata do binário local MCScanX também deve acompanhar o registro de reprodutibilidade; ela não foi inventada a partir da versão de outros programas.

## Revisão de estilo e verificação

Foram aplicadas as skills solicitadas de redação científica, estilo da Mariana e revisão de fluidez. A revisão priorizou estrutura argumentativa, precisão e concisão. O texto mantém uma única tabela comparativa, sem acrescentar figuras decorativas ou análises novas. As referências citadas no texto possuem entradas correspondentes na bibliografia, com links DOI, e as referências não utilizadas foram removidas.

O script local da skill ai-humanizer produziu escores heurísticos de 25,7/100 para o original e 10,0/100 para a versão 2. Esses valores descrevem características de estilo segundo o próprio script, não probabilidades de autoria nem resultados de detectores externos. A grande mudança de extensão e a redução da bibliografia também afetam a comparação; o escore não demonstra qualidade científica ou garante classificação por qualquer detector.

O arquivo original foi preservado, com SHA-256 `6cb0416bb3db8fb5b061785eab5e749e9dd2877849a7ba13c06d242c57dacd58`. As verificações desta etapa se limitaram à revisão documental, consistência dos números citados, correspondência entre citações e referências e preservação do original.
