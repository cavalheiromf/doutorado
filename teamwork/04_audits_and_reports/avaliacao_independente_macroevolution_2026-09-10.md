# Avaliação independente de chapter_macroevolution

Data: 10 de setembro de 2026. Texto avaliado: `teamwork/01_drafts_and_outlines/chapter_macroevolution_master_draft.md`, 369 linhas na leitura desta avaliação.

**Parecer: revisão maior, com prioridade para corrigir a análise de Ka/Ks e reconciliar as versões dos resultados.** O capítulo tem uma pergunta biológica relevante e uma estrutura que conecta filogenômica, datação e evolução de famílias gênicas. Entretanto, algumas conclusões centrais excedem o alcance do desenho comparativo, e a inspeção dos arquivos revelou problemas computacionais concretos. A revisão necessária ultrapassa o aprimoramento da redação.

Esta avaliação combina leitura do manuscrito, inspeção de scripts e resultados locais, uma verificação de correspondência CDS–proteína dos 250 candidatos e consulta pontual à literatura. Não reexecutei IQ-TREE, MCMCtree, CAFE5 ou yn00; não realizei auditoria bibliográfica exaustiva nem inspeção visual das figuras. Nenhum arquivo do manuscrito ou das análises foi alterado. Relatórios anteriores foram consultados como contexto, sem tratar seus pareceres como validação independente.

## 1. Crítico: o alinhamento de códons compromete os candidatos de seleção

**Localização:** manuscrito, §§2.6, 3.4 e 4.4; `chapter_macroevolution/docs/scripts/calculate_kaks_1to1.py`, linhas 34–48 e 169–202.

O script lê `02_phylogenomics/trimmed_alignments/OG*_trimmed.fa`. Em seguida, `thread_cds` percorre a proteína recortada e consome os CDS originais desde a posição zero, avançando três nucleotídeos por aminoácido não correspondente a gap. Esse procedimento não recupera os códons correspondentes às colunas proteicas removidas no recorte. Quando uma coluna removida continha um aminoácido da espécie focal, os códons seguintes deixam de representar as posições proteicas corretas. Preservar múltiplos de três não basta para preservar a homologia posicional.

**Verificação nos dados:** para cada entrada de `05_selection/positive_selection_candidates_top250.tsv`, recuperei o CDS da espécie e comparei a tradução dos primeiros `3 × comprimento da proteína recortada sem gaps` nucleotídeos com essa proteína. A verificação reproduz a associação sequencial de códons feita pelo script. Houve discordância em 215 sequências de Vper e 213 de Vtub, abrangendo **247 dos 250 ortogrupos em pelo menos uma espécie**. Esse resultado demonstra falha na correspondência; não significa que todos esses genes sejam biologicamente desprovidos de seleção positiva. Também não substitui uma verificação completa de isoformas e anotações.

Exemplo: no candidato PPR `OG0011783`, a proteína recortada de Vtub tem 532 aminoácidos. Somente 49 das 532 posições concordam com a tradução associada pelo procedimento. O início da proteína é `MLLRSRVLSSKLFSTAAANLT...`; o início traduzido a partir do CDS é `MLLRSRVLSSKLFSTAAAAAANLT...`. Para Vper, no mesmo ortogrupo, as 534 posições concordam. Essa assimetria torna especialmente problemática a comparação pareada.

Além disso, a primeira linha da tabela de candidatos, `OG0010812`, apresenta `dS = -0.0000` e `omega = 99.0000`. O filtro `omega > 1 and ds < 2` aceita esse caso. A razão não deve ser interpretada como uma estimativa regular de intensidade seletiva quando seu denominador é zero. O parser também admite um fallback para Nei–Gojobori sem registrar na tabela qual estimador produziu cada resultado.

**Correção necessária:** recuperar a isoforma correspondente a cada proteína; validar sua tradução; gerar alinhamentos de códons a partir dos alinhamentos proteicos completos; aplicar depois uma máscara de recorte às trincas correspondentes; rejeitar resultados indefinidos e registrar falhas e estimadores utilizados. Recalcular o conjunto analisado, a classificação dos candidatos e todas as tabelas e interpretações dependentes. Até lá, a lista de 250 genes e a interpretação centrada em PPRs devem ser consideradas provisórias.

## 2. Alta prioridade: estatísticas de seis táxons atribuídas a sete

**Localização:** manuscrito, §§2.3 e 3.1, especialmente linhas 66 e 94–96.

O capítulo descreve sete espécies, mas apresenta log-verossimilhança, critérios de informação e comprimento total da árvore que pertencem ao arquivo `iqtree_pan_velloziaceae.iqtree`, cujo cabeçalho identifica **seis táxons**. Existe uma execução distinta de sete táxons em `iqtree_pan_velloziaceae_7taxa.iqtree`.

| Estatística | Manuscrito / execução de 6 táxons | Execução de 7 táxons |
| --- | ---: | ---: |
| Log-verossimilhança | −5.290.825,0851 | −6.024.349,3677 |
| AIC | 10.589.364,17 | 12.056.416,7353 |
| AICc | 10.589.405,04 | 12.056.457,6461 |
| BIC | 10.633.733,66 | 12.100.809,2279 |
| Comprimento total da árvore | 1,6741 | 2,0089 |
| Comprimento dos ramos internos | 0,3171 | 0,4110 |

Esses valores não devem ser comparados para escolher o melhor modelo entre conjuntos de táxons distintos. A tabela serve para identificar a origem dos números transcritos. É necessário fixar a execução de referência e reconciliar texto, árvores, figuras e entradas das análises seguintes.

O suporte UFBoot de 100% é um resultado útil, mas não equivale a ausência de discordância entre genes. O arquivo `concordance_7taxa.cf.tree` informa gCF aproximados de 62,5%, 88,0%, 97,2% e 93,9% nos quatro ramos internos avaliados, com sCF de 42,6%, 55,4%, 79,1% e 86,4%. Esses resultados já disponíveis devem integrar a interpretação. A distância Robinson–Foulds igual a zero entre a árvore concatenada e seu consenso bootstrap não mede concordância entre árvores gênicas.

## 3. Alta prioridade: datação dependente das calibrações e de versões divergentes

**Localização:** manuscrito, §§2.4, 3.2 e 4.1.

Deixar `t_n12` sem calibração direta não produz uma estimativa independente das outras calibrações. A árvore impõe uma calibração de 75–90 Ma ao seu ancestral `t_n11`; portanto, o prior conjunto já restringe fortemente a possibilidade de uma idade cretácea antiga para o descendente. Como os limites são suaves, isso não é uma exclusão lógica absoluta, mas invalida a apresentação do desenho como um teste temporal completamente livre ou imparcial. O resultado pode favorecer uma divergência cenozoica **condicionalmente às calibrações e ao modelo**, sem estabelecer por si só o percurso ou a direção da dispersão.

A expressão “five fossil calibrations” também precisa de revisão: a justificativa fornecida para 2–25 Ma no par de Vellozia é uma interpretação de radiação neogênica e história da paisagem, não a descrição de um fóssil. Para cada calibração, informar espécime ou fonte secundária, posição filogenética, idade, justificativa dos limites e distribuição. A referência local de Wanga et al. (2021) inspecionada descreve comparação de plastomas e inferência filogenética; não localizei nela a calibração campaniana que o manuscrito lhe atribui.

Há ainda duas sínteses numéricas locais:

| Nó | Tabela citada no manuscrito | Média combinada das duas cadeias |
| --- | ---: | ---: |
| `t_n12` | 31,92 Ma | 33,7699 Ma |
| `t_n13` | 9,74 Ma | 9,6839 Ma |

A segunda fonte é `03_dating/mcmctree_high_ess_convergence_summary.tsv`. Não recomendo substituir valores automaticamente: primeiro é necessário documentar a origem das cadeias e escolher a análise final. Para `t_n12`, essa tabela informa ESS de aproximadamente 99,6 e 129,5 nas cadeias individuais, e 261,8 combinado; a afirmação genérica de que todos os ESS excederam 200 precisa especificar a que diagnóstico se refere.

O script `03_dating/analyze_mcmctree_chains.py`, linhas 110–111, calcula percentis 2,5 e 97,5 e os rotula como HPD. Trata-se de um intervalo de credibilidade de caudas iguais, que não é, em geral, um intervalo de maior densidade posterior. Corrigir a terminologia ou calcular o HPD adequadamente. Os intervalos amplos também não sustentam atribuir a divergência a um episódio climático específico com precisão equivalente à da média pontual.

**Correção necessária:** reconciliar versões, revisar a fundamentação das calibrações, apresentar prior versus posterior e realizar análises de sensibilidade antes de sustentar a refutação forte da vicariância ou uma história direcional de dispersão.

## 4. Alta prioridade: expansão ancestral de genes não demonstra ancestralidade do fenótipo

**Localização:** manuscrito, linhas 119, 183–187 e 207–209.

Os totais de expansão e contração de CAFE5 citados no manuscrito conferem com `04_gene_families/functional_enrichment/results_final_simplify/Foreground_sizes_TierA.tsv`: nó 12 = 100/17, Vper = 72/61 e Vtub = 31/80. Essa concordância numérica é um ponto favorável, embora não constitua uma revalidação do ajuste de CAFE5.

O salto está entre reconstruir números ancestrais de cópias e concluir que o ancestral expressava tolerância vegetativa à dessecação. Genes de proteção contra estresse podem ter funções em sementes e outros tecidos; homologia de componentes moleculares não demonstra homologia do fenótipo vegetativo integrado. O desenho tem apenas quatro espécies de Velloziaceae, com um único contraste focal entre duas espécies de Vellozia. Ele não estabelece a polaridade do caráter em toda a família, nem demonstra que as duas espécies sejam irmãs quando outros representantes do gênero forem incluídos.

**Correção necessária:** apresentar a ancestralidade da tolerância como hipótese compatível com parte dos padrões genômicos. Para testá-la diretamente, ampliar a amostragem de fenótipos e táxons, reconstruir estados ancestrais sob modelos alternativos e distinguir presença de genes, regulação vegetativa e resposta fisiológica. Mostrar também quais ortogrupos sustentam especificamente a alegação sobre LEA, sHSPs e metabolismo de açúcares, em vez de chamar as 100 expansões coletivamente de “stress-protective”.

## 5. Alta prioridade: seleção e adaptação são afirmadas além do teste realizado

**Localização:** manuscrito, linhas 42, 86, 127 e 187–199.

Mesmo após corrigir os alinhamentos, uma classificação por `omega > 1` não fornece, sozinha, um teste de significância para chamar as assinaturas de “statistically robust”. O yn00 implementa um estimador aproximado; a expressão “maximum-likelihood counting method” não corresponde à distinção feita no artigo original. Comparações pareadas também não localizam em qual das duas linhagens ocorreram as mudanças. Portanto, não sustentam atribuir seleção especificamente a Vtub. A faixa `0,5 <= omega < 1` não deve ser denominada automaticamente neutra. Ver [Yang & Nielsen (2000)](https://academic.oup.com/mbe/article/17/1/32/975527).

A rejeição de deriva, gargalos e relaxamento de seleção na linha 187 não decorre de expansão funcionalmente desigual, ancoragem cromossômica ou ORFs completas. A análise de seleção usa ortólogos de cópia única e não testa diretamente a evolução dos parálogos cuja retenção está sendo explicada. Trata-se de conjuntos de genes distintos. Tampouco o contraste de duas espécies separa o efeito do hábito evergreen das demais diferenças entre essas linhagens.

**Correção necessária:** manter “Genomic Burden of Being Evergreen” como hipótese interpretativa; definir qual quantidade mensurável constitui o suposto custo; discutir alternativas; usar testes de seleção adequados ao desenho e correção de multiplicidade quando aplicável. “Enriquecimento” requer universo de comparação, teste, tamanho de efeito e ajuste estatístico explícitos. Contagem de palavras ou presença de domínios não equivale a enriquecimento estatístico.

## 6. Questões importantes de mecanismo e suporte bibliográfico

**Localização:** manuscrito, linhas 36, 117–123, 179 e 185–187.

A comparação entre duplicações em contigs e em cromossomos é pertinente, mas ancoragem cromossômica não demonstra por si só que 42 cópias codifiquem componentes plastidiais funcionais ou elevem o fluxo cíclico de elétrons. A inferência precisa distinguir identidade das subunidades, localização nuclear/plastidial/mitocondrial, integridade, expressão e eventual inserção de DNA organelar. Os métodos apresentados também não documentam suficientemente a classificação de duplicações, a sintenia e os testes de cobertura usados nessas afirmações.

Da mesma forma, conservar o número cromossômico não basta para excluir duplicação genômica histórica. Os resultados estruturais devem ser descritos com o alcance efetivo dos métodos, sem transformar ausência de um sinal relatado em exclusão geral do mecanismo.

Na conferência bibliográfica pontual, Vieira et al. (2025), usado para fundamentar características específicas de V. tubiflora e V. peripherica, estudou **Barbacenia gentianoides e Vellozia caruncularis**. É uma fonte de comparação fisiológica, mas não valida diretamente as medidas ou mecanismos atribuídos ao par focal. A distinção é verificável no [artigo original](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2025.1642013/full). Recomendo verificar individualmente alegações como mortalidade quase nula, limiares hídricos e manutenção de hidratação durante todo o ano, sem pressupor que um conjunto de citações forneça evidência específica para cada espécie.

## 7. Estrutura e redação

A progressão ambiente → contraste fisiológico → hipóteses → análises é clara. A organização em resultados e discussão separados facilita a leitura, e a ponte final com OSCA pode funcionar bem no contexto da tese. O material tabular oferece identificadores úteis para rastrear candidatos.

O problema editorial principal é o excesso de certeza, que acompanha problemas inferenciais reais. Expressões como “fundamental paradigm shift”, “definitively established”, “fully established” e “reject neutral duplicate accumulation” prometem demonstrações que o desenho não oferece. Elas devem ser revistas depois de corrigir as análises, e não apenas substituídas por sinônimos mais cautelosos.

O resumo está sobrecarregado de parâmetros e detalhes de pipeline. Pode concentrar-se na pergunta, no desenho, em dois ou três resultados confirmados e numa conclusão proporcional. A introdução e a discussão repetem amplamente o contraste fisiológico; reduzir essa repetição abriria espaço para alternativas e limitações. Valores de log-verossimilhança, critérios de informação e comprimento da árvore aparecem em Métodos e Resultados; devem ter uma localização principal. “Micro-evolutionary” merece revisão quando se refere a divergência entre espécies por milhões de anos. Há ainda a palavra portuguesa “enxuto” no texto em inglês e inconsistência entre cinco gêneros reconhecidos e a enumeração posterior de Nanuza/Pleurostima.

As declarações finais precisam de conferência documental antes de circulação: financiamento, permissões, depósito, aprovação dos autores e disponibilidade de código são afirmações factuais. O DOI Zenodo terminado em `12345678` tem aparência de marcador provisório; não verifiquei sua titularidade nem os demais identificadores nesta avaliação. Não apresentá-los como depósitos confirmados sem verificar os registros correspondentes.

## Ordem de revisão proposta

1. Corrigir a correspondência CDS–proteína e recalcular Ka/Ks; atualizar todas as inferências dependentes.
2. Fixar uma versão final dos resultados filogenéticos e de datação, corrigindo números, diagnósticos e intervalos.
3. Revisar calibrações e testar a sensibilidade da inferência temporal aos priors.
4. Reposicionar ancestralidade da tolerância e custo do hábito evergreen como hipóteses, ou acrescentar análises capazes de testá-las.
5. Documentar métodos estruturais e conferir o suporte específico das citações e declarações.
6. Reescrever resumo e conclusão com os resultados estabilizados; condensar repetições e incorporar limitações.

A contribuição mais defensável, após essas correções, é uma comparação filogenômica e de dinâmica de famílias gênicas entre linhagens com estratégias hídricas contrastantes. O capítulo pode formular hipóteses relevantes sobre ancestralidade e manutenção do hábito evergreen, mas os arquivos examinados ainda não sustentam apresentá-las como mecanismos demonstrados.
