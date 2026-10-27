# Classificação das versões do CAFE5 para a apresentação

Verificação local em 5 de outubro de 2026. Escopo: consenso de famílias, perfis terminais e materiais diretamente relacionados. Os arquivos existentes foram preservados. A classificação é por conteúdo e proveniência verificável, não pelo nome ou pela data de modificação.

## Resultado principal

O conjunto sustentado pelos resultados disponíveis hoje contém **196 famílias Tier A** e **58 famílias Tier B**. A recomendação anterior de apresentar 188 foi baseada em uma revisão textual desatualizada.

Foi recalculado Benjamini–Hochberg sobre os 12.276 valores de p de cada arquivo `Gamma_family_results.txt`, sem executar novamente o CAFE5. A validade numérica das execuções foi avaliada comparando ajuste, parâmetros e falhas registrados em `Gamma_results.txt`; isso não constitui validação biológica dos modelos.

| Modelo | Execuções retidas nesta verificação | Interseção com q ≤ 0,05 |
|---|---|---:|
| Gamma k=2 | rep01, rep02, rep03, rep05 | 196 |
| Gamma k=3 | rep01–rep05 | 254 |
| Gamma k=4 | rep02–rep05 | 266 |
| Consenso k=2 ∩ k=3 | Execuções acima | 196 |
| Consenso k=2 ∩ k=3 ∩ k=4 | Execuções acima | 196 |
| Sensíveis ao modelo: k=3 menos consenso k=2 | Execuções acima | 58 |

As interseções reproduzem exatamente os IDs de `summary/high_confidence_core_196_families.tsv` e `summary/tier_b_rate_heterogeneity_58_families.tsv`.

Em k=2, rep04 tem −lnL aproximadamente 115.825 e falha registrada para OG0000001, frente a aproximadamente 107.704 nas outras quatro. Em k=4, rep01 tem −lnL aproximadamente 110.507 e falha registrada, frente a aproximadamente 106.856 nas outras quatro. Em k=3, todas as cinco estão no patamar de aproximadamente 107.175. Portanto, a descrição antiga de cinco execuções válidas em k=2 e apenas quatro em k=3 não descreve os arquivos atuais. Mesmo aplicando a seleção antiga, a interseção dos arquivos atuais permanece 196; isso não torna aquela descrição metodológica correta.

## Inventário e classificação

Todos os caminhos abaixo são relativos à raiz do projeto.

| Material | Classificação | Motivo e uso recomendado |
|---|---|---|
| `docs/01_thesis_and_chapters/chapter_01_draft.md` e figuras conceituais antigas com 250 candidatos/PPR ou datas 31,92 e 9,74 Ma | Legacy para os resultados revisados | Preservar como histórico; não reutilizar números e interpretações sem comparação com as análises específicas atuais. |
| `teamwork/01_drafts_and_outlines/chapter_macroevolution_master_draft_v4.md` | Intermediário | Usa 188 e confunde em alguns trechos o indicador de enriquecimento terminal com todas as mudanças positivas. |
| `teamwork/01_drafts_and_outlines/chapter_macroevolution_master_draft_volpato_revised.md` | Intermediário, desatualizado em CAFE5 | Mantém 188 e a seleção antiga de execuções. Seus cuidados inferenciais continuam úteis, mas não é fonte dos números atuais. |
| `chapter_macroevolution/docs/reviews/pre_integration_2026-09-15/` | Arquivo histórico | Registra estados anteriores; não é fonte preferencial para slides. Há versões distintas dentro do próprio arquivo. |
| `chapter_macroevolution/04_gene_families/cafe5_methodology_and_results_revised.md` | Intermediário | Descreve 188 + 43 e estatísticas de execuções que diferem dos resultados brutos atuais. |
| `chapter_macroevolution/04_gene_families/comparative_axes/comparative_axes_v2_summary.md` | Intermediário | Texto ainda descreve 188 + 43, enquanto a tabela v2 já contém 196 + 58. |
| `chapter_macroevolution/04_gene_families/summary/all_models_summary.tsv` | Intermediário, misto | Contagens de famílias refletem resultados atuais, mas vários ajustes e parâmetros não correspondem aos `Gamma_results.txt` atuais; faltam parâmetros para parte de k=4. Não usar como resumo final de ajuste. |
| `chapter_macroevolution/04_gene_families/summary/k3_additional_heterogeneity_43_families.tsv` | Intermediário, substituído para a seleção atual | Contém 43 linhas; a diferença de conjuntos atual é 58. |
| `chapter_macroevolution/04_gene_families/summary/high_confidence_core_188_families.tsv` | Conteúdo atual, nome legacy | Tem 196 famílias e é idêntico byte a byte ao arquivo nomeado 196. Não representa uma lista histórica preservada de 188. |
| `chapter_macroevolution/04_gene_families/summary/high_confidence_core_196_families.tsv` | Atual para a seleção Tier A | 196 IDs reproduzidos pela correção BH e pelas interseções atuais. |
| `chapter_macroevolution/04_gene_families/summary/tier_b_rate_heterogeneity_58_families.tsv` | Atual para a seleção Tier B | 58 IDs reproduzidos como consenso k=3 menos consenso k=2. |
| `chapter_macroevolution/04_gene_families/comparative_axes/comparative_families_master_table_v2.tsv` | Atual para os conjuntos e perfis verificados | Contém 196 Tier A e 58 Tier B. As mudanças de Vper e Vtub nas 196 famílias coincidem com k=2 rep01. As demais colunas não foram integralmente auditadas nesta verificação. |
| `chapter_macroevolution/04_gene_families/summary/master_family_table.tsv` | Atual quanto ao tamanho do Tier A | Marca 196 famílias como consenso. Não foi integralmente auditada. |
| `chapter_macroevolution/04_gene_families/functional_enrichment/functional_enrichment_summary.md` e scripts `06_make_figures.py`, `07_generate_summary_report.py` | Mistos; atualização necessária | Relatório combina cabeçalho N=188 com 196 famílias; scripts contêm denominadores e contagens fixos de 188. O enriquecimento não foi recalculado ou validado aqui. |
| `teamwork/01_drafts_and_outlines/chapter_macroevolution_master_draft.md` | Mais atualizado no total 196, ainda intermediário na integração | Usa 196 + 58, mas mantém descrições de execuções e outros números que precisam ser sincronizados. Não deve ser tratado integralmente como versão final. |

## Perfis que podem orientar os slides

Contagens obtidas da lista atual de 196 famílias, com reconstruções de k=2 rep01:

| Espécie | Famílias com mudança positiva | Famílias com mudança negativa | Sem mudança | Indicador de enriquecimento terminal |
|---|---:|---:|---:|---:|
| V. peripherica | 86 | 64 | 46 | 73 |
| V. tubiflora | 56 | 80 | 60 | 35 |
| X. viscosa | 67 | 66 | 63 | 33 |

O indicador terminal exige condições adicionais, incluindo maior contagem extante entre as Velloziaceae amostradas; é um subconjunto das mudanças positivas. As contagens são de famílias, não de cópias ganhas ou perdidas. A significância é familiar, e as direções em ramos são reconstruídas; não se demonstrou controle independente de FDR por ramo.

Formulação recomendada: **“Identificamos 196 famílias com evidência de turnover mantida entre as configurações avaliadas. Nesse conjunto, as reconstruções indicam mais mudanças positivas em V. peripherica e mais mudanças negativas em V. tubiflora.”**

## Pendências antes da montagem final

Atualizar a descrição das execuções válidas e parâmetros a partir dos resultados brutos; sincronizar os perfis terminais; conferir a árvore temporal efetivamente fornecida às execuções atuais antes de declarar que são baseadas na datação atualizada; verificar os conjuntos e denominadores efetivamente usados no enriquecimento e regenerar os gráficos afetados. A identidade dos arquivos 188 e 196 impede recuperar as oito famílias adicionadas usando apenas essas duas listas; seria necessário um snapshot histórico real.

Esta verificação não alterou manuscritos, gráficos, scripts analíticos ou resultados biológicos.

## Atualização após a sincronização dos manuscritos

Na etapa seguinte, autorizada pela autora, os dois manuscritos `chapter_macroevolution_master_draft.md` e `chapter_macroevolution_master_draft_volpato_revised.md` foram atualizados nas passagens de CAFE5. As classificações acima descrevem o estado anterior a essa edição. Os originais foram preservados em `pre_sync_2026-10-05/`, com hashes no manifesto `manuscript_sync_manifest_2026-10-05.json`.

A conferência dos 15 arquivos `Gamma_asr.tre` e do relatório representativo confirmou que as execuções Gamma atuais usam a árvore atualizada: raiz 138,431 Ma, Xerophyta–Vellozia 33,7699 Ma e Vellozia 9,6839 Ma. Essa pendência está resolvida para as execuções Gamma verificadas. O parâmetro de erro atual é epsilon=0,00588995. O ajuste representativo de k=2 tem lambda=0,0036237762462708, alpha=0,899434 e −lnL aproximadamente 107.704. Para k=3 e k=4, os ajustes representativos são aproximadamente 107.175 e 106.856. Os valores são reportados arredondados nos resultados brutos; não foram mantidas diferenças de AIC com precisão herdada da tabela antiga.

Também foram conferidos os 117 sinais positivos e 19 negativos em Node 12, com 104 sinais positivos preservados em todas as cinco execuções k=3 e 106 em todas as quatro k=4 retidas. OG0000026 pertence agora ao Tier A. As seções de métodos e resultados de Ka/Ks foram preservadas literalmente nas duas cópias. Figuras, enriquecimento, descrição metodológica específica do CAFE5 e tabelas-resumo externas aos manuscritos ainda precisam de atualização; nenhuma análise foi reexecutada nesta edição.

## Atualização dos produtos derivados

As tabelas de modelos e a tabela comparativa foram regeneradas das execuções atuais. As seleções permanecem 196 Tier A e 58 Tier B; o Tier C atual contém 63 famílias, pois a execução inválida k=2 rep04 foi retirada do cálculo. A tabela comparativa usa k=2 rep01 e todas as cinco execuções k=3 para os indicadores de preservação. O resumo comparativo e o documento metodológico foram sincronizados.

O enriquecimento foi recalculado com as anotações locais e 10.000 permutações, semente 20260904. Entre 7.269 testes primários, houve 1 termo confirmatório (GO:0005739, mitochondrion), 21 sugestivos com desequilíbrio e 53 discordantes na permutação. Não houve termos robustos balanceados nos contrastes condicionais. As contagens Tier A por cenário são 196, 178, 183 e 155; os denominadores efetivos variam por categoria. O manifesto antigo foi preservado e um registro dos insumos desta nova execução foi gerado. Todos os controles do validador passaram após essa atualização. Isso não significa que todos os contrastes atingiram equilíbrio: a classificação mantém explicitamente os sinais desequilibrados.

Foram regeneradas as figuras de fluxo, diagnósticos e enriquecimento; foi criada `figure_current_family_turnover` em PNG, PDF e SVG. A inspeção visual corrigiu legendas sobrepostas, contraste de números no heatmap e o caso de resultado nulo no gráfico de sobreposição. As figuras conceituais legacy e os objetos da simplificação separada em R permanecem históricos/intermediários. Consulte `04_gene_families/CURRENT_OUTPUTS.md` para escolher os produtos atuais.

## Nomenclatura esclarecida para o manuscrito e a apresentação

**Consenso entre modelos (196 famílias; Tier A nas tabelas):** famílias com q ≤ 0,05 em todas as execuções retidas de k=2 e k=3. Todas também atendem ao critério em todas as execuções retidas de k=4. O consenso descreve repetibilidade da significância familiar nas configurações avaliadas.

**Conjunto adicional apoiado por k=3 (58 famílias; Tier B nas tabelas):** famílias com q ≤ 0,05 nas cinco execuções k=3, mas que não atendem ao critério em pelo menos uma execução retida k=2. Portanto, não pertencem ao consenso entre modelos. Isso não significa que sejam não significativas em todas as execuções k=2, nem que sejam biologicamente menos importantes.

Os conjuntos são distintos: 196 + 58 = 254 famílias no consenso k=3. Essa classificação se refere ao suporte estatístico para mudanças no tamanho das famílias ao longo da árvore, não à validação funcional ou à significância de cada expansão em um ramo. O enriquecimento funcional é uma análise posterior e usa uma classificação própria de evidência.

Na apresentação: “Encontramos 196 famílias cujo sinal de turnover se mantém entre os modelos avaliados. Outras 58 têm suporte recorrente em k=3, mas esse suporte não se mantém em todas as execuções de k=2.”
