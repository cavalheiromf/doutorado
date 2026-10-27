# História evolutiva das Velloziaceae — conversa com a orientadora

11 slides principais (~12 minutos) e 4 de apoio.

Direcionamento: recursos genômicos → comparação entre linhagens → história da variação → hipóteses sobre respostas à limitação hídrica.

## 1. História evolutiva das Velloziaceae: ancestrais e diferenciação das linhagens

A pergunta central é como o repertório de famílias gênicas mudou ao longo da história das Velloziaceae amostradas. São quatro espécies da família: Acanthochlamys bracteata, Xerophyta viscosa, Vellozia tubiflora e V. peripherica, além de três grupos externos. A amostragem não permite reconstruir toda a diversidade da família. O conjunto de 196 famílias de consenso será a base dos resultados, mas os modelos são suporte à pergunta evolutiva. O enquadramento da tese é a limitação hídrica. A história evolutiva oferece uma base para investigar possíveis relações da variação genômica com respostas à seca e à dessecação; o painel não demonstra uma relação causal.

## 2. Dos recursos genômicos à investigação da variação

Tomar como referência o parágrafo final da Introdução fornecido pela autora: a tese reúne formação computacional, recursos genômicos e análise comparativa para apoiar investigações de respostas à limitação hídrica, com foco em Velloziaceae. Capítulo1: experiência de pós-graduandos aprendendo Python. Capítulo2: genoma nuclear de Vellozia tubiflora. Capítulo3: genomas de organelas de Velloziaceae. Capítulo4: análises comparativas para investigar variação genômica e suas possíveis relações com respostas contrastantes à seca e à dessecação. Os resultados de famílias apresentados aqui usam dados nucleares; não afirmar que o CAFE integra diretamente genomas organelares. O quarto capítulo dá uso comparativo aos recursos e situa a variação em uma história evolutiva.

## 3. A árvore situa três divergências das Velloziaceae amostradas

Começar pela topologia: Acanthochlamys é irmã do grupo Xerophyta–Vellozia, e Xerophyta é irmã das duas Vellozia, no painel amostrado. A divergência de Acanthochlamys tem média 78,02 Ma; Xerophyta–Vellozia, 33,77 Ma; o par de Vellozia, 9,68 Ma. São idades condicionadas às calibrações utilizadas, não datas da origem de toda a família ou do gênero. Fonte: figure_current_dated_family_changes_counts.tsv e mcmctree_high_ess_convergence_summary.tsv. Todos os números são contagens de famílias dentre as 196 de consenso. No ramo do ancestral Xerophyta–Vellozia (nó12), 117 têm mudança positiva e 19 negativa. No ancestral exclusivo das duas Vellozia (nó13), 87 positivas e 20 negativas. Idades médias de 33,77 e 9,68 Ma respectivamente. Reconstrução k=2 rep01; não implica significância específica em cada ramo. A figura mostra médias, sem intervalos das idades. Não chamar nó12 de ancestral exclusivo de Vellozia.

## 4. As mudanças antecedem as divergências das linhagens

Fonte: tabela comparativa atual, reconstrução k=2 rep01, 196 famílias de consenso. As contagens são de famílias, não de genes nem de eventos independentes. Os ramos são sucessivos: o ramo que leva ao ancestral das quatro Velloziaceae amostradas (nó11), o que leva ao ancestral Xerophyta–Vellozia (nó12), e o que leva ao ancestral do par de Vellozia (nó13). Uma família pode mudar em mais de um ramo. Não transformar a diferença de totais em diferença de taxas, pois ramos têm durações distintas. Consenso da família não implica significância em cada ramo.

## 5. Após as divergências, os balanços terminais diferem

Conectar com o slide anterior: além das mudanças ancestrais, os ramos terminais têm balanços distintos. O gráfico focaliza Xerophyta e as duas Vellozia. No ramo de Acanthochlamys, a tabela registra +13/−145 entre as 196 famílias, mas interpretar esse sinal exige avaliar comparabilidade das contagens e anotação; não significa simplificação funcional demonstrada. Fonte: tabela comparativa atual; contagens de sinais na reconstrução k=2 rep01 entre as 196 famílias. Vper +86/−64, Vtub +56/−80, Xvis +67/−66. Uma família pode ser contada em vários ramos. Positivo/negativo representa direção de mudança reconstruída, não teste com FDR por ramo. Não interpretar os totais como número de genes ganhos ou perdidos.

## 6. Os repertórios atuais registram perfis distintos

Apontar primeiro as quatro colunas de Velloziaceae: Abra, Xvis, Vtub e Vper. Os três grupos externos contextualizam as contagens. A linha branca da figura separa apenas as três linhagens focais de Acanthochlamys e dos grupos externos; não delimita toda Velloziaceae. A comparação descreve perfis e não demonstra associação com ambiente. Fonte: figure_current_lineage_copy_heatmap_rows.tsv. Cores log2(contagem+1), mesma escala nos painéis. Linhas agrupadas dentro de cada Tier por ligação média/distância euclidiana; as linhas dos dois painéis não correspondem umas às outras. As alturas iguais dos painéis não indicam igual número de famílias. Agrupamento é descritivo, não teste independente de separação entre espécies. Zero significa zero na tabela de entrada, não perda biológica validada. Verificar completude e anotação para interpretar ausências.

## 7. Famílias ilustram trajetórias evolutivas distintas

Usar os exemplos para mostrar que uma mudança ancestral pode coexistir com mudanças posteriores, e que diferentes famílias seguem trajetórias distintas. Não narrar uma progressão obrigatória de complexidade. Fonte: figure_current_family_examples_selection.tsv. Todas são Tier A. OG0000035: germin-like, +13 no nó12, ancestral Xerophyta–Vellozia. OG0000027: domínio móvel de plantas / proteína não caracterizada, +50 terminal Vper. OG0000024: citocromo P450, −15 terminal Vper. Escalas verticais próprias; barras observadas, mudanças reconstruídas em k=2 rep01. Seleção ilustrativa por contraste de padrões, não por enriquecimento ou ranking de relevância. Anotações EggNOG não confirmam função de todas as cópias. A natureza móvel de OG0000027 merece avaliação antes de interpretação funcional. Posições genômicas não foram validadas para esses exemplos.

## 8. A história das cópias orienta hipóteses biológicas

Fala: o resultado direto é alteração estimada do repertório de cópias por ramo. Duplicações podem motivar hipóteses de dosagem, redundância ou diferenciação funcional, mas não demonstram esses mecanismos. Contração indica redução reconstruída, não perda funcional automaticamente. Validar identidade, integridade e organização dos genes; função e resposta ao ambiente exigem evidências próprias. Conectar à pergunta da tese: verificar futuramente se as trajetórias das famílias se relacionam a respostas contrastantes à seca e à dessecação. Não usar estes termos como equivalentes nem presumir associações com os padrões de cópias.

## 9. O painel revela parte da história evolutiva da família

Delimitar o alcance: quatro espécies não representam toda Velloziaceae. O capítulo conta a história dos ramos amostrados, com grupos externos, e oferece hipóteses para ampliar a comparação. Mais amostragem pode alterar a distribuição inferida das mudanças. Fala: a defesa do capítulo deve se apoiar no conjunto de famílias e nos padrões de linhagem. Consenso entre modelos não é validação independente dos dados de entrada. Anotações e qualidade dos genomas afetam contagens. Diagnósticos de MCMC estão nos slides de apoio; Rhat próximo de 1 não substitui ESS e avaliação das cadeias. Não usar enriquecimento funcional amplo ou seleção positiva como eixo central sem validação específica.

## 10. Proposta: um capítulo sobre a história do repertório gênico

Organizar o capítulo em relações e tempo, mudanças ancestrais, diferenciação terminal e casos biológicos. A comparação de modelos sustenta a confiança na história reconstruída e entra depois dos resultados biológicos ou no apoio. Proposta concreta: organizar o capítulo em história evolutiva, consistência das famílias, perfis de linhagem e exemplos. Usar o conjunto adicional como análise de sensibilidade claramente separado. Prioridades: validar famílias selecionadas, reconciliar anotações e explicitar qualidade do genoma; conferir a proveniência das calibrações antes da versão final. O trabalho já feito torna essa uma proposta de capítulo delimitado, sem prometer validações ainda inexistentes. Em consonância com a Introdução, a contribuição é fornecer uma base comparativa para investigar variação genômica e suas possíveis relações com respostas à limitação hídrica. Essa função não exige demonstrar causalidade adaptativa neste capítulo.

## 11. O capítulo acrescenta uma história evolutiva à tese

Fechamento alinhado à Introdução proposta: os capítulos2 e3 estabelecem recursos genômicos; o capítulo4 usa análises comparativas para investigar a variação. A história evolutiva das linhagens situa essa variação e oferece uma base para investigar suas possíveis relações com respostas contrastantes à seca e à dessecação. Aqui são apresentados padrões de famílias nucleares e hipóteses para aprofundamento, não associação ambiental demonstrada. Proponho incluir o capítulo por essa contribuição à arquitetura da tese.

## 12. A história se apoia em famílias de consenso entre modelos

Fonte: comparative_families_master_table_v2.tsv e comparative_axes_v2_summary.md. O universo contém 12.276 famílias. Tier A: q≤0,05 em todas as quatro execuções retidas de k=2 e cinco de k=3; as 196 também passam em todas as quatro retidas de k=4. Tier B: 58 passam em todas as cinco de k=3, mas falham em pelo menos uma retida de k=2. Não afirmar ausência de sinal em todas as execuções de k=2. k representa categorias discretas de taxa de turnover. Execuções sem ótimo aceitável foram excluídas conforme auditoria atual.

## 13. Visão conjunta dos resultados atuais

Apoio. Fonte: figura atual de turnover. Os percentuais de genes tandem+proximal são 21,25% em Vper e 15,96% em Vtub; denominadores são genes anotados de cada genoma. Não demonstram sozinhos o mecanismo de expansão das famílias selecionadas. Contagens e níveis de evidência estão nos painéis A/B.

## 14. Diagnósticos e execuções retidas de CAFE

Apoio. Fonte: resumo atual dos relatórios Gamma. k2 rep04 e k4 rep01 foram excluídos do conjunto de execuções retidas por ajuste incompatível com o ótimo aceito. Critérios da auditoria estão no relatório de classificação. Diagnóstico do ajuste não é validação biológica das contagens.

## 15. Diagnósticos da datação: avaliar R-hat e ESS

Apoio. Figura atual corrigida. Intervalos são de credibilidade de caudas iguais (percentis 2,5/97,5), não HPD. Nó12: Rhat1,0063, ESS por cadeia99,6/129,5; nó13 Rhat1,0061, ESS257,8/265,5. Correlação das médias não demonstra convergência. Sem calibração direta refere-se ao nó12; ele continua condicionado às demais calibrações. A proveniência individual das calibrações requer reconciliação antes da versão final.
