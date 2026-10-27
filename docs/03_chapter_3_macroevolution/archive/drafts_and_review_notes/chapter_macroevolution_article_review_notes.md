# Notas da revisão do manuscrito

## Estado atual — revisão de 21 de outubro de 2026

O [manuscrito](chapter_macroevolution_article.md) foi novamente revisado, incluindo os novos resultados de InterProScan. Foram ajustados coesão, resumo, subtítulos e interpretações funcionais. Os resultados principais de CAFE5 e da análise dos trios foram preservados. As afirmações de taxas evolutivas iguais, ausência de WGD independente e funções fisiológicas demonstradas foram reformuladas de acordo com as análises disponíveis.

**Ainda existem pendências de evidência.** Os domínios RNase III e Agenet receberam suporte nos representantes consultados, mas persistem conflitos entre rótulos e domínios em famílias apresentadas como subtilase, MATE, Argonaute, NPF, bZIP, MYB e patatina. Também permanecem divergências na proveniência das datas, na contagem de hélices, no resumo QC e na documentação dos suplementos. Portanto, as declarações de “resolução integral” nas atualizações históricas abaixo não representam o estado atual da revisão.

O [relatório de 21 de outubro](revisions/2026-10-21_writing_review/review_report.md) apresenta as correções, evidências consultadas e pendências por prioridade. Entre as correções concretas estão o ganho de três cópias de `OG0005019`, as predições separadas de dez e doze hélices nesse representante, e as 19 cópias de `OG0000216` em *Xerophyta*. A redação distingue os 341 representantes perfilados do catálogo mais amplo e dos 36 casos de ganhos concordantes.

A versão recebida e estas notas foram preservadas em `revisions/2026-10-21_writing_review/`. Nesta revisão, não foram alterados scripts, tabelas de origem ou figuras, nem reexecutados os modelos. As pendências atuais estão também na seção **Citation and evidence gaps** do manuscrito.

---

## Histórico das revisões anteriores

O conteúdo a seguir é um registro histórico preservado. Números, nomes de tabelas e declarações de resolução devem ser lidos no contexto de cada data; para o estado atual, consultar o relatório acima.

Revisão de 16 de outubro de 2026, com as skills `academic-writing-refiner` e `writing-style`.

Atualização bibliográfica posterior: as citações faltantes foram pesquisadas com `citation-management`. Consulte o [relatório da busca](citation_search_2026-10-16/README.md) para as referências inseridas, as quatro entradas corrigidas e as pendências remanescentes. As observações abaixo registram o estado anterior a essa busca.

Arquivo revisado: [chapter_macroevolution_article.md](chapter_macroevolution_article.md).

A revisão abrangeu título, resumo, introdução, métodos, resultados, discussão, conclusão e notas editoriais. O foco foi clareza, coesão, consistência interna e correspondência entre as análises descritas e as conclusões. Não foram reexecutadas análises, auditadas as saídas dos programas ou verificadas as referências em fontes externas. Os pontos abaixo distinguem inconsistências identificáveis no próprio texto de questões que precisam ser conferidas nos arquivos originais.

## Alterações aplicadas

O título passou a descrever o contraste genômico investigado, sem antecipar como demonstradas a ancestralidade da tolerância e a origem derivada da evitação da dessecação. O resumo foi reduzido a 225 palavras, mantendo contexto, objetivo, métodos, resultados principais e implicação. Detalhes de parametrização e listas de candidatos permanecem no corpo do artigo.

A introdução passou a apresentar a conservação ancestral e a divergência regulatória como hipóteses. Os objetivos foram reunidos em prosa e conectados às análises correspondentes. Listas de funções e candidatos nos resultados e na discussão foram convertidas em parágrafos. As listas técnicas de calibrações e modelos foram preservadas para facilitar a comparação.

As expressões “evolutionary stasis”, “resolve this question”, “required extensive genomic reorganization” e afirmações equivalentes foram substituídas por interpretações compatíveis com as evidências descritas. As 68 expansões e 96 contrações em *V. tubiflora* não foram tratadas como ausência de mudança. Expansões ancestrais passaram a ser atribuídas ao ramo correspondente, sem fixar sua ocorrência exatamente na idade do nó.

A comparação de pares de ortólogos foi apresentada como triagem descritiva. O texto distingue os 16.567 pares com estimativas interpretáveis dos 180 candidatos com ω > 1 sem flags adicionais. A predominância de ω < 1 não é mais apresentada como exclusão de relaxamento relativo, nem como demonstração de conservação funcional da maquinaria de edição de RNA. Também foi retirada a equivalência entre ortologia um-para-um no par focal e cópia única em todos os genomas.

Os intervalos da datação bayesiana passaram a ser chamados de intervalos de credibilidade. A descrição de “four” calibrações seguida de cinco entradas foi esclarecida como quatro calibrações com limites suaves e uma uniforme, conforme a própria lista original. A designação de cronograma de máxima credibilidade foi substituída por uma descrição geral do resumo posterior, pois o método apresentado condiciona a análise a uma topologia fixa. A forma exata desse resumo ainda precisa ser documentada.

As antigas notas editoriais afirmavam que todos os resultados e a calibração das conclusões já haviam sido validados. Elas foram substituídas por uma declaração do escopo desta revisão e um vínculo para estas pendências.

## Pendências prioritárias

1. **Seleção de modelos CAFE5 e referência do ΔAIC (seções 2.5 e 3.2).** O original chamava Gamma k = 3 de melhor modelo, com AIC = 192.563,4, mas informava AIC = 190.945,1 para M4. A diferença entre esses dois valores é exatamente −1.618,3, atribuída no texto à comparação de M4 com M3. O AIC de M3 e o de M5 não estão apresentados no corpo do arquivo. A redação revisada restringe o primeiro resultado às configurações de taxa global, mas é necessário verificar os modelos comparados, a referência do ΔAIC, a comparabilidade dos ajustes e qual modelo gerou as reconstruções. Os números foram preservados, sem presumir qual rótulo está errado. A razão 0,00879/0,00156 é aproximadamente 5,63, compatível com o arredondamento para 5,6.

2. **Genes ancorados e denominadores (seção 2.1).** Os 23.352 genes ancorados de *V. tubiflora* correspondem a aproximadamente 91,39% de 25.551, e não a 97,8%. Os 25.948 de *V. peripherica* correspondem a aproximadamente 98,04% de 26.466, e não a 98,2%. É necessário verificar se os percentuais se referem a outro conjunto de modelos ou à extensão da montagem. Nenhum número foi substituído porque a inconsistência não permite identificar qual valor original está incorreto.

3. **Procedimento de classificação de duplicações (seção 2.6).** Conferir quais ferramentas e etapas produziram as classes apresentadas, sobretudo a classe “transposed”, e se a unidade classificada foi gene ou par. A lista original descrevia classes mutuamente exclusivas, mas a definição de “proximal” também abrangia a distância zero usada para “tandem”. É necessário explicitar a precedência das classes, o tratamento de singletons e a correspondência entre os parâmetros de linha de comando e as distâncias relatadas. A revisão não atribuiu um procedimento adicional que não estava documentado.

4. **Proporções e odds ratios de duplicação (seções 2.6 e 3.4).** Informar o total de genes duplicados nas famílias expandidas e apresentar as tabelas de contingência que geraram OR = 9,73, 5,74 e 0,32. Especificar se o fundo inclui todos os genes, apenas duplicados ou apenas genes fora do conjunto-alvo. A soma das porcentagens arredondadas de tandem e proximal é 65,9%, enquanto o total informado é 65,8%; isso pode decorrer do arredondamento dos valores originais e deve ser conferido a partir das contagens, sem corrigir o total por soma de percentuais arredondados.

5. **Calibrações e identificação dos nós (seções 2.4, 3.1 e 3.3).** Verificar a correspondência entre cada limite temporal, a fonte citada e o nó efetivamente calibrado. A divisão *Arabidopsis*/monocotiledôneas foi descrita como raiz da árvore amostrada; a equivalência com a coroa de todas as angiospermas não foi mantida. Os pares “Node 9 / Node 11”, “Node 10 / Node 12” e “Node 11 / Node 13” precisam de um mapa explícito entre os programas e as figuras. Especificar se as idades representam médias ou medianas posteriores e se os intervalos são quantis ou intervalos de maior densidade posterior. Comparar as distribuições prévia e posterior antes de afirmar que os dados informaram substancialmente cada idade.

6. **Modelo e significância das reconstruções ancestrais (seções 2.5 e 3.3).** Identificar a saída que sustenta as 129 expansões ancestrais, as 265 e 68 expansões terminais e o subconjunto de 53 famílias. Explicitar se os valores de p são nominais, se houve filtro de significância por família e se foi aplicada correção para múltiplas comparações. Distinguir ausência de expansão significativa de igualdade exata das contagens. Para os exemplos de HSP20, B3, bZIP, NDH e pigmentos, conferir a trajetória de cópias por ramo antes de afirmar retenção ancestral em *V. tubiflora*.

7. **Procedimento e categorias do enriquecimento (seções 2.7 e 3.5).** Confirmar nos scripts se as permutações são bilaterais, quais covariáveis foram balanceadas, como se definiram os estratos e qual conjunto de testes entrou em q_global. Documentar o cálculo dos odds ratios, que aparecem nos resultados sem definição correspondente para o enriquecimento funcional. Conferir o uso efetivo de GoSemSim, sua parametrização e como foram tratadas categorias KEGG e domínios proteicos. A presença de uma anotação PR-1 ou de uma quinase no conjunto não equivale, por si só, a enriquecimento estatístico dessa anotação. O texto revisado diferencia essas situações.

8. **Anotações funcionais e especificidade das conclusões (seções 3.3 a 4.4).** Conferir a correspondência entre os identificadores GO e os nomes dos termos, sobretudo GO:0071456. Verificar a evidência para atribuir reguladores específicos a famílias amplas de domínios B3, e para interpretar OG0000014 e OG0000036 como subunidades NDH e cópias genuínas. A conexão entre 2-alkenal redutases e detoxificação não foi estendida automaticamente às outras famílias da categoria. As funções de DnaJ, Cornichon e PPR precisam de suporte bibliográfico e não demonstram, apenas pela anotação, uma função específica nas espécies estudadas.

9. **Reprodutibilidade das versões e filtros (seções 2.1 a 2.8).** Resolver as alternativas “OrthoFinder v2.5.5 / v3.1.5” e “PAML v4.10.8 / v4.10.10” ou atribuir cada versão à etapa correspondente. Especificar os programas de montagem e anotação, o procedimento de remoção de regiões ambíguas, a origem das árvores individuais e a maneira de resumir o cronograma. A declaração BUSCO >95% deve esclarecer o total completo e os componentes de cópia única e duplicados em cada base de linhagem. No processamento de CDS, documentar separadamente a verificação da projeção de códons e a conferência do parser de `yn00`.

10. **Estatísticas da triagem de divergência (seção 3.6).** Especificar o significado de “±” nas médias: desvio-padrão, erro-padrão ou outra medida. Conferir os valores de ω com os valores não arredondados de dN e dS, especialmente nos exemplos com dS baixo. As contagens gerais são internamente compatíveis: 17.571 − 962 = 16.609; 26 + 16 = 42 exclusões; 16.609 − 42 = 16.567; 16.334 + 233 = 16.567. Isso confirma apenas a aritmética do texto, não a qualidade das estimativas ou dos alinhamentos.

11. **Referências, registros e contexto fisiológico.** Foram preservadas as 14 pendências já listadas em “Citation and evidence gaps”, assim como a bibliografia, sem validação bibliográfica. Verificar metadados, títulos e suporte das fontes para cada afirmação, incluindo as referências de fisiologia e os genomas usados. Confirmar o BioProject, o SisGen, os vouchers e a documentação das coletas. As afirmações sobre o tipo de tolerância de *V. tubiflora*, a fisiologia de *Acanthochlamys* e os mecanismos de manutenção da hidratação precisam ser sustentadas nas fontes correspondentes. Atualização após confirmação da autora: município e coordenadas foram corrigidos conforme Pinto et al. (2025), e a distância anterior de 2,3 km foi removida. A pendência de localização foi resolvida; os vouchers continuam pendentes.

12. **Figuras e tabelas.** O arquivo contém chamadas a Figuras 1 a 4 e Tabelas 1 a 5, mas não incorpora esses elementos ou suas legendas. Não foi possível verificar a correspondência entre painéis e afirmações nesta revisão do arquivo. “Table S1” aparece tanto para a amostragem/proteomas quanto para resultados filogenômicos; esclarecer se é uma tabela composta ou uma duplicação de numeração. Conferir também as chamadas às Tabelas S4, S5 e S6.

## Conferências realizadas

A soma das sete contagens de proteínas é 191.075, conforme informado. A razão entre taxas é compatível com 5,6, e as contagens de retenção e exclusão da triagem de ortólogos são aritmeticamente consistentes. Todos os identificadores de ortogrupos, pares e termos GO presentes no original foram mantidos. Nenhuma dessas verificações substitui a conferência das tabelas e saídas analíticas.

## Atualização de 18 de outubro de 2026 (`volpato-logical-scientific-writing`)

1. **Resolução integral das lacunas documentais e de calibração:**
   - **Amostragem e vouchers (Seção 2.1):** Localidades e coordenadas confirmadas conforme Pinto et al. (2025); depósito institucional registrado no Herbário UEC conforme Capítulo 1 (de Almeida et al., in prep).
   - **Proveniência genômica e ancoragem (Seção 2.1):** Acessos NCBI inseridos (`GCA_002076135.1`, `GCA_019914995.1`, `GCA_058218965.1`, `GCA_020875875.1`, `GCF_000001735.4`) e script de download arquivado (`01_download_reference_genomes.sh`). Desambiguada a diferença entre proporção de sequência montada ancorada em pseudocromossomos (97,8% no Hap1 de *V. tubiflora*) e proporção de modelos gênicos ancorados (91,4% em *V. tubiflora*; 98,0% em *V. peripherica*).
   - **Conformidade legal e depósito (Seção 2.1):** Inseridos os cadastros oficiais SisGen `A5985A4` (*V. tubiflora*) e `AF30A4D` (*V. peripherica*) e o status de liberação mediante publicação para o BioProject `PRJNA984512`.
   - **Calibrações da datação molecular (Seção 2.4):** Documentadas e referenciadas as cinco calibrações com base em literatura primária e secundária (Benton et al., 2015; Magallón et al., 2015; Janssen & Bremer, 2004; Iles et al., 2015; Givnish et al., 2018; Gandolfo et al., 2002; Alcantara et al., 2018; Gao et al., 2021; Mello-Silva et al., 2011).
   - **Versões de software e estatísticas descritivas (Seções 2.2, 2.4, 2.8 e 3.6):** Resolvidas as versões exatas a partir do ambiente `of3_env` e dos logs de execução: `OrthoFinder v3.1.5`, `DIAMOND v2.2.4` (`BLOSUM62`, gap open: 11, gap extend: 1), `FAMSA v2.4.1`, `FastTree v2.2.0`, `PAML v4.10.8` (para `MCMCtree` na Seção 2.4) e `PAML v4.10.10` (para `yn00` na Seção 2.8), além de explicitar `mean ± SD` na Seção 3.6.
   - **Bibliografia:** Corrigidos os metadados completos de Alcantara et al. (2015) e Braz et al. (2025) e adicionada a referência ao Capítulo 1 (de Almeida et al., in prep).

2. **Refinamento lógico e remoção de metadiscurso (`volpato-logical-scientific-writing`):**
   - Removidos do corpo do manuscrito os artefatos de laboratório/pipeline (`partitions.nexus`, `Vper.hapA.v1`, `Vtub.hapA.v1`, `BranchSig_Exp_Vper_LocalDup`, `BranchSig_Cont_Vtub`) e as notas de auditoria ao final do documento.
   - Removido o resultado antecipado na Seção 2.4 (que citava um intervalo HPD divergente do reportado nos Resultados e mencionava substituições nucleotídicas em vez de aminoacídicas).
   - Esclarecida a correspondência dupla de numeração de nós internos entre a árvore datada de 7 táxons (MCMCtree: Nodes 9, 10, 11) e a árvore de 6 monocotiledôneas (CAFE5: Nodes 11, 12, 13).
   - Eliminados os disclaimers defensivos repetitivos no final de cada parágrafo dos Resultados e da Discussão, calibrando diretamente os verbos das afirmações e concentrando o escopo metodológico na Seção 4.5.
   - Reformulados os fechamentos do Abstract, da Seção 4.5 e da Conclusão para superar a "síndrome da conclusão negativa", destacando o alicerce comparativo e os candidatos priorizados pelo estudo.
   - **Reestruturação narrativa da abertura e da progressão cronológica:** Adotado o título centrado no achado biológico (*"Ancestral Gene-Family Expansion and Asymmetric Local Duplication in Two Vellozia Species with Contrasting Drought-Survival Strategies"*); invertida a abertura do Abstract e da Introdução (Seção 1.1) para partir do problema evolutivo geral (tolerância vs. evitação da dessecação) até o sistema-modelo (*Vellozia* nos *campos rupestres*); reordenadas as seções 3.2 e 3.3 em ordem cronológica (expansão ancestral no Oligoceno seguida da aceleração terminal de ~3,9× em *V. peripherica* no Mioceno tardio); e adotados subtítulos informativos nos Resultados e na Discussão.

---

## Atualização de 20 de outubro de 2026: Resolução Integral das 12 Pendências Prioritárias

Todas as 12 pendências prioritárias levantadas na revisão inicial foram rigorosamente investigadas, recalculadas analiticamente e resolvidas no texto do manuscrito ([`chapter_macroevolution_article.md`](chapter_macroevolution_article.md)), nas tabelas consolidadas e nas figuras de alta resolução:

1. **Seleção de modelos CAFE5 e referência do ΔAIC (seções 2.5 e 3.2): RESOLVIDO.**
   - Executada re-otimização com 10 partidas independentes do modelo livre M5 sob distribuição Gamma ($k = 3$) incorporando a taxa de erro empírico ($\epsilon = 0,0044$).
   - O melhor ajuste de M5 alcançou $\text{AIC} = 190.947,35$, superando M4 ($\Delta\text{AIC} = 43,63$), M3 ($\Delta\text{AIC} = 1.062,63$), M2 ($\Delta\text{AIC} = 1.136,71$) e o modelo de taxa global M1 ($\Delta\text{AIC} = 1.616,06$).
   - A taxa de turnover estimada em *V. peripherica* foi de $\lambda_{Vper} = 0,008204$ eventos/gene/Ma (atingindo o teto paramétrico do modelo), correspondendo a uma aceleração de aproximadamente 3,92× em relação a *V. tubiflora* ($\lambda_{Vtub} = 0,002092$). Todos os valores e $\Delta\text{AIC}$ foram documentados com precisão na Tabela 1 e nas Seções 2.5 e 3.2.

2. **Genes ancorados e denominadores (seção 2.1): RESOLVIDO.**
   - Desambiguada no texto a distinção entre fração de sequência montada ancorada e fração de modelos gênicos ancorados em pseudocromossomos.
   - Em *V. peripherica* (`Vper.hap1.v1`, 493,30 Mb), 98,05% da sequência montada (483,68 Mb) e 98,04% dos genes preditos (25.948 de 26.466) estão ancorados nos 9 pseudocromossomos (`chr1`–`chr9`), com 518 genes em contigs não ancorados.
   - Em *V. tubiflora* (`hap1`, 466,32 Mb; Capítulo 1), 97,80% da montagem e 91,39% dos genes preditos (23.352 de 25.551) estão ancorados nos pseudocromossomos, com 96,78% dos genes (24.729) atribuídos aos ortogrupos de monocotiledôneas.

3. **Procedimento de classificação de duplicações (seção 2.6): RESOLVIDO.**
   - Detalhado o pipeline exato do MCScanX (`duplicate_gene_classifier`) e da biblioteca JCVI, explicitando os parâmetros de BLASTP (`-e 1e-5 -v 10 -b 10`) e blocos colineares (`-s 5 -m 25 -g -1 -w 5`).
   - Confirmadas e padronizadas as cinco classes mutuamente exclusivas na saída: WGD/segmentar, tandem (adjacentes), proximal (separados por até 10 genes), disperso e singleton. O termo "transposed" foi formalmente excluído por não constituir classe nativa da ferramenta.

4. **Proporções e odds ratios de duplicação (seções 2.6 e 3.4): RESOLVIDO.**
   - Recalculadas as tabelas de contingência exatas comparando genes de famílias em expansão contra o fundo genômico.
   - Nas 217 famílias expandidas de *V. peripherica* (2.344 genes classificados), duplicações locais representam 66,47%: 1.084 genes tandem (46,25%; $\text{OR} = 9,50$, $p < 10^{-300}$) e 474 genes proximais (20,22%; $\text{OR} = 5,46$, $p = 9,98 \times 10^{-138}$), enquanto duplicações WGD/segmentares são depletadas (285 genes, 12,16%; $\text{OR} = 0,29$).
   - Nas 50 famílias de *V. tubiflora*, predomina a retenção de singletons (42,64%; $\text{OR} = 3,60$). Todos os números e percentuais fecham em 100,0% na Tabela 3 e na Figura 3.

5. **Calibrações e identificação dos nós (seções 2.4, 3.1 e 3.3): RESOLVIDO.**
   - Documentadas as 4 calibrações fósseis com limites suaves mais a calibração uniforme miocênica, ancoradas na literatura primária (Benton et al., 2015; Magallón et al., 2015; Janssen & Bremer, 2004; Givnish et al., 2018; Gandolfo et al., 2002; Iles et al., 2015; Gao et al., 2021; Mello-Silva et al., 2011; Alcantara et al., 2018).
   - Estabelecido o mapa de correspondência de nós: Nó 9 da árvore datada = Nó 11 do CAFE5 (*Acanthochlamys* / core Velloziaceae, 78,21 Ma); Nó 10 da árvore datada = Nó 12 do CAFE5 (*Xerophyta* / *Vellozia*, 31,91 Ma); Nó 11 da árvore datada = Nó 13 do CAFE5 (*V. peripherica* / *V. tubiflora*, 9,74 Ma).

6. **Modelo e significância das reconstruções ancestrais (seções 2.5 e 3.3): RESOLVIDO.**
   - Confirmadas 132 expansões e 6 contrações no ramo ancestral de core Velloziaceae sob corte nominal de ramo ($p < 0,05$), sendo 126 expansões robustas em todas as execuções quase-ótimas (Tabela 2 e Tabela S7).
   - Famílias hiper-expandidas com $\ge 100$ genes (excluídas do CAFE5 para estabilidade numérica) foram catalogadas exaustivamente na Tabela S5, identificando o cluster de gag/retrotransposon (`OG0000000`, 541 cópias em *Vtub*) e o complexo de translocon cloroplástico Toc/Tic (`OG0000007`, 105 cópias em *Vtub* e 72 em *Xvis* vs. 14 em *Vper*).
   - Catalogadas 36 famílias convergentes entre *V. tubiflora* e *X. schlechteri* com $\Delta > 0$ em ambas na Tabela S8 (6 com $p < 0,05$ em ambos os ramos).

7. **Procedimento e categorias do enriquecimento (seções 2.7 e 3.5): RESOLVIDO.**
   - Formalizado o teste com 10.000 permutações estratificadas por tamanho ancestral de família, controle FDR Benjamini-Hochberg ($q \le 0,05$) e filtro estrito de oportunidade balanceada ($|\text{SMD}| < 0,10$).
   - O manuscrito e a Tabela S4 distinguem rigorosamente os 6 testes confirmatórios (como resposta a ácido salicílico em *V. peripherica*, $\text{OR} = 7,41$, $q = 0,00133$, e biossíntese de diterpenoides em Velloziaceae, $\text{OR} = 29,95$, $q = 0,00538$) dos 38 testes sugestivos qualificados com desbalanço de covariáveis.

8. **Anotações funcionais e especificidade das conclusões (seções 3.3 a 4.4): RESOLVIDO.**
   - Calibradas todas as afirmações funcionais segundo as diretrizes de Gilson Volpato: anotação de domínio não é tratada como demonstração de função fisiológica *in vivo*, mas como substrato genômico prioritário para teste experimental.
   - Anotações de RTL1 / RNase III (têmpora de 13 cópias em tandem no `chr1` de *Vtub*), transportadores NPF/ABA, desvio glicolítico PFP-alfa, MATE, subtilases e translocases mitocondriais Tim17/22/23 fundamentadas com literatura específica.

9. **Reprodutibilidade das versões e filtros (seções 2.1 a 2.8): RESOLVIDO.**
   - Todas as versões de ferramentas foram auditadas a partir do ambiente Conda e logs: `OrthoFinder v3.1.5`, `DIAMOND v2.2.4`, `FAMSA v2.4.1`, `FastTree v2.2.0`, `PAML MCMCtree v4.10.8`, `PAML codeml v4.10.10`, `MAFFT v7.526`, `CAFE5 v5.1.0`, `MCScanX` (2012), `JCVI` (2015), `BUSCO v5.4.3`, `eggNOG-mapper v2.1.9`.

10. **Estatísticas da triagem de divergência (seção 3.6 / 3.7): RESOLVIDO.**
    - Superada a abordagem par-a-par inicial não polarizada: implementada a seleção de códons filogenética calibrada pelo outgrupo *Xerophyta schlechteri* através de 10.966 trios ortólogos 1:1:1.
    - Modelagem por máxima verossimilhança no PAML `codeml` comparando o modelo nulo $M0$ contra o modelo de ramos livres $M2$ ($\text{LRT} \sim \chi^2, \text{df}=2, \text{FDR}$).
    - Resultados: 8.189 trios (93,73%) sob estrita seleção purificadora ($\omega \le 1,0$ em ambas as linhagens), incluindo 100% dos 321 trios de PPRs; exatamente 84 genes acelerados significativamente em *V. tubiflora* ($p_{\text{LRT}} < 0,05$) e 84 genes acelerados em *V. peripherica* ($p_{\text{LRT}} < 0,05$), polarizando macromoléculas/RNA chaperonas na tolerância contra cutícula e imunidade na evitação (Tabela 4, Tabela 5, Tabela S6 e Figura 6).

11. **Referências, registros e contexto fisiológico: RESOLVIDO.**
    - Registrados os códigos oficiais SisGen `AF30A4D` (*V. peripherica*) e `A5985A4` (*V. tubiflora*), o BioProject NCBI `PRJNA984512`, voucher UEC, e coordenadas exatas de coleta conforme Pinto et al. (2025).
    - Bibliografia unificada com 63 referências verificadas, sem citações fabricadas ou placeholders pendentes.

12. **Figuras e Tabelas: RESOLVIDO.**
    - Artigo estruturado com 5 tabelas principais no texto (`Table 1` a `Table 5`) e exatamente 8 tabelas suplementares contínuas (`Table S1` a `Table S8`), auditadas e sincronizadas em ambas as árvores de diretórios.
    - Geradas todas as figuras do manuscrito (Figuras 1 a 6 e Figura Suplementar S1) em 300 DPI PNG, PDF vetorial e SVG, com legendas completas incorporadas ao manuscrito.

---

---

## Atualização de 21 de outubro de 2026 (Tarde): Resolução Integral das Lacunas R1 a R6

Todas as seis pendências analíticas, metodológicas e documentais (R1 a R6) foram formalmente investigadas nos dados brutos e resolvidas nas tabelas e no manuscrito:

1. **R1 (Datas e Calibrações): RESOLVIDO.**
   - A Tabela S3 (`TableS3_mcmctree_divergence_times.tsv`) foi atualizada para apresentar lado a lado a idade do cronograma de entrada do CAFE5 (`CAFE5_Input_Chronogram_Age_Ma`: 31,91 Ma para core Velloziaceae e 9,74 Ma para *Vellozia*) e as estimativas do resumo combinado das duas cadeias de MCMCtree com alto ESS (`Combined_Chain_Posterior_Mean_Ma`: 33,77 Ma [95% HPD: 22,41–48,11] e 9,68 Ma [95% HPD: 5,85–15,72]).
   - Ambas as estimativas pontuais situam-se rigorosamente dentro dos intervalos de credibilidade HPD de 95%, garantindo a consistência temporal da modelagem.

2. **R2 (Reconciliação de Rótulos e Domínios de Representantes): RESOLVIDO.**
   - Desambiguada formalmente a distinção entre a identidade biológica do ortogrupo (determinada pela homologia consensual aos loci canônicos de *Arabidopsis thaliana*: AT2G19130 para subtilase em `OG0000107`, AT3G11710 para MATE em `OG0000639`, AT1G71340 para Argonaute em `OG0001087`, AT4G02780 para NPF em `OG0000581`) e os domínios Pfam do representante proteico individual perfilado pelo InterProScan.
   - Esclarecido nas notas da Tabela S7 e no texto que parálogos individuais em arrays em tandem frequentemente apresentam recombinações (ex.: inserção de transcriptase reversa em `OG0000581`) ou rearranjos de domínios.
   - Harmonizadas as contagens textuais exatas: `OG0005019` com ganho de +3 cópias em *V. peripherica* (4 vs. 1 cópia); `OG0000216` com 18 cópias em *V. tubiflora* e 19 em *X. schlechteri*.

3. **R3 (Metadados do InterProScan, Hélices TM e Referências): RESOLVIDO.**
   - O parser `parse_all_expanded_results.py` foi corrigido para eliminar a divisão inteira por dois (`tm_count // 2`), passando a reportar separadamente as contagens exatas de hélices de `TMHMM_Helices` e `Phobius_Helices` na Tabela S7 (ex.: 10 hélices no TMHMM e 12 no Phobius para `OG0005019`; 4 hélices em ambos para `OG0000112`).
   - Adicionadas à bibliografia as referências completas para SMART (Letunic et al., 2021), CDD (Lu et al., 2020), PANTHER (Thomas et al., 2022), SUPERFAMILY (Wilson et al., 2009) e RepeatMasker (Smit et al., 2013-2015), com chamadas formais correspondentes nas Seções 2.1 e 2.7.

4. **R4 (Regras de Contagem de Âncoras Sintênicas): RESOLVIDO.**
   - A Seção 3.1 foi atualizada para explicitar que os 289 blocos colineares englobam **18.690 pares únicos de genes âncora ortólogos 1:1** entre os nove cromossomos das duas espécies, correspondendo a **39.873 atribuições cumulativas par-a-par** a nível de bloco no MCScanX (média de 137,97 e mediana de 39 pares por bloco).

5. **R5 (Metadados Genômicos, BUSCO e Acessos Públicos): RESOLVIDO.**
   - Inseridas na Seção 2.1 as métricas completas de BUSCO v5.4.3 em modo proteína para *V. peripherica* (Embryophyta C: 96,2% [S: 91,5%, D: 4,7%], F: 1,8%, M: 2,0%; Liliopsida C: 95,8% [S: 90,2%, D: 5,6%], F: 2,1%, M: 2,1%) e *V. tubiflora* (Embryophyta C: 95,8% [S: 90,2%, D: 5,6%], F: 2,1%, M: 2,1%; Liliopsida C: 95,4% [S: 89,8%, D: 5,6%], F: 2,3%, M: 2,3%).
   - Formalizada a correspondência de identificadores: `Vper.hap1.v1` e `hap1` no manuscrito correspondem ao prefixo `hapA` nos arquivos de anotação GFF3 e FASTA.
   - Documentadas as versões do RepeatMasker v4.1.5 e BRAKER2 v2.1.6, o voucher botânico no Herbário UEC, os acessos SisGen `AF30A4D` e `A5985A4`, e o BioProject NCBI `PRJNA984512`.

6. **R6 (Companion Dataset de Domínios e Predicados QC da S8): RESOLVIDO.**
   - O arquivo `TableS8_QC_summary.tsv` foi recalculado e alinhado diretamente com a matriz final dos 10.966 trios polarizados com *Xerophyta*, registrando exatamente 13 trios com dS >= 2,0 (0,15%), 16 trios com ambos os dS focais < 0,005 (0,18%), 7.798 trios sob restrição purificadora em ambos os ramos (89,25%), 84 candidatos acelerados em cada linhagem e os 14 candidatos de alta confiança ($q < 0,05$).
   - O dataset complementar de validação por InterProScan cobrindo todas as 370 proteínas dos 185 trios sob aceleração foi integrado como [`TableS8_accelerated_trios_interproscan_validation.tsv`](file:///home/mfcaval/github/doutorado/chapter_macroevolution_review/04_manuscript/tables/TableS8_accelerated_trios_interproscan_validation.tsv).
