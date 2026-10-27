# Revisão do manuscrito mestre de macroevolução

> **Estado atual:** revisão consolidada no manuscrito mestre. O original e a primeira cópia revisada estão preservados em `pre_integration_2026-09-15/`. A verificação posterior das anotações está em [Proveniência de OG0000317/OG0000332](annotation_provenance_2026-09-15.md); ela qualifica o diagnóstico M11.

Data: 15/09/2026. Manuscrito: `teamwork/01_drafts_and_outlines/chapter_macroevolution_master_draft.md`. Aplicação da skill `volpato-logical-scientific-writing` com redação orientada pela skill `writing-style`.

## Escopo e relação com o parecer anterior

Este arquivo é o manuscrito integrado, com Resumo, Introdução, Métodos, Resultados, Discussão, Conclusão e declarações. O parecer anterior incidiu sobre o relatório `cafe5_methodology_and_results_revised.md`, portanto não avaliava a Introdução agora localizada. Este adendo passa a avaliar a cadeia argumentativa completa. Os originais e os rascunhos de outros capítulos foram preservados. A integração está em `teamwork/01_drafts_and_outlines/chapter_macroevolution_master_draft_volpato_revised.md`.

Foram lidos todos os segmentos do manuscrito, incluindo a seção de seleção e as referências. A conferência documental concentrou-se nos dois relatórios IQ-TREE, na supermatriz PHYLIP, no Log e nas estatísticas OrthoFinder, nas tabelas de datação, nos controles MCMCtree e nas médias das duas cadeias, nos 21 relatórios CAFE5, na tabela mestre v2, no resumo de duplicações e nos relatórios atuais de Ka/Ks. Não houve reexecução de filogenia, CAFE5, datação ou seleção, nem auditoria integral da bibliografia.

## Mapa argumentativo

**Introdução original:** ambiente rupestre → estratégias hídricas contrastantes → homologia ou convergência da tolerância → origem ancestral e custo de uma suposta perda secundária. O problema biológico é explícito, mas o objetivo promete reconstrução do estado fenotípico ancestral e explicações causais que os métodos não operacionalizam.

**Métodos a Conclusão originais:** filogenia e idade de divergência → reconstrução de números de cópias → hipótese de tolerância ancestral tratada como demonstrada → evergreen derivado e custoso. O salto ocorre ao converter tamanho ancestral de família em estado fisiológico ancestral, sem reconstrução de caracteres e sem validação funcional. A seção 4.4 sobre Ka/Ks apresenta limites adequados, mas a seção 4.3 os contradiz ao excluir processos neutros e afirmar adaptação.

**Cadeia revisada:** contraste fisiológico como motivação → caracterização de diferenças genômicas no painel amostrado → evidência por família e arquitetura de duplicação → candidatos e hipóteses funcionais. Origem ancestral, convergência, direção da dispersão e manutenção do hábito evergreen permanecem perguntas testáveis, sem serem anunciadas como resultados demonstrados.

## Achados e decisões de integração

| ID / classe | Localização original e evidência | Diagnóstico e risco | Decisão e correção integrada |
| --- | --- | --- | --- |
| M1 — crítico | Resumo; §§1.4, 4.3 e 5: “ancestral ground state”, “secondary evergreen”, “paradigm shift” | Cópias reconstruídas não estabelecem tolerância ancestral nem perda secundária. | Aceita: reformulados objetivo, resumo, discussão e conclusão; cenários mantidos como hipóteses. |
| M2 — crítico | §§2.3 e 3.1: lnL = −5.290.825,0851 e comprimento 1,6741 | Esses valores pertencem ao relatório de **seis** táxons. O relatório `iqtree_pan_velloziaceae_7taxa.iqtree` registra lnL = −6.024.349,3677 e comprimento 2,0089. | Aceita: usados os valores do relatório de sete táxons; métricas de seis táxons removidas. |
| M3 — crítico | §§2.2, 3.1 e 5: “0% missing data” | Presença de todos os táxons por partição não implica ausência de gaps. Contagem direta na supermatriz: Ath 3,56%; Dala 3,99%; Ptec 1,92%; Abra 3,65%; Xvis 15,33%; Vper 1,86%; Vtub 1,95% de caracteres −, ? ou X. | Aceita: distinguida ocupação por táxon de completude de sítios. |
| M4 — crítico | §2.2: 17.571 ortólogos “strict pairwise 1:1” | São linhas contendo um identificador por espécie antes de excluir parceiros adicionais. O conjunto reciprocamente único contém 16.609 pares. | Aceita: critérios harmonizados com §2.6; métodos/resultados de Ka/Ks preservados. |
| M5 — crítico | §§3.3, 4.3 e resumo: 100 expansões e saldo +83 | Na Tier A, há 112 mudanças positivas no nó 12 na reconstrução k2; 100 preservam a classificação positiva em todas as réplicas k3 válidas. As 17 negativas vêm da reconstrução k2. O saldo mistura critérios e tampouco mede saldo de genes. | Aceita: 112, 100 e 17 apresentados com definições distintas, sem saldo. |
| M6 — crítico | §3.3: 72 versus 31 “expansions” | Na tabela mestre há 85 mudanças positivas em Vper e 52 em Vtub; 72/31 exigem, adicionalmente, maior contagem que as demais Velloziaceae. | Aceita: dois níveis de filtragem explícitos; 61/80 mudanças negativas identificadas como reconstruções k2. |
| M7 — crítico | §§3.3, 4.3 e 5: “42 anchored copies” | As contagens Vper dos três OGs são 67, 18 e 6 (=91); 42 é a soma de +31, +8 e +3 reconstruídos. | Aceita: separados genes anotados e mudança inferida; retirada a conclusão de fluxo cíclico elevado. |
| M8 — crítico | §3.3: OG0000026, F-box, +51 paralogos | Tabela v2: 21 cópias em Vper, mudança +4, Tier B; descrição LRR-repeat/uncharacterized. | Aceita: removido o exemplo incompatível, sem lhe atribuir nova função validada. |
| M9 — crítico | §§2.4, 4.1: “unbiased”, nó “unconstrained”, dispersão oeste necessária | O nó não tem calibração própria, mas depende de calibrações vizinhas e prior conjunto. Data de divergência não estima diretamente colonização ou rota. | Aceita: inferência temporal condicional; removidas rota, direção e rejeição categórica de cenários não testados. |
| M10 — crítico | §4.3: explicações neutras excluídas e cópias intactas com cobertura canônica | Não são apresentados testes demográficos nem auditoria de integridade/cobertura suficiente para essas conclusões. | Aceita: neutralidade e adaptação permanecem alternativas não resolvidas; posição cromossômica não é validação funcional. |
| M11 — crítico | §3.3: OG0000317/OG0000332 como NDH e artefatos comprovados | Anotações conflitam com splicing/RNA-binding na tabela mestre; contigs não ancorados não provam artefato. | Aceita com ajuste: exemplos funcionais suspensos; pendência de anotação e autenticidade explicitada. |
| M12 — relevante | §§2.4 e 3.2: execução curta de datação e ESS >200 | O mestre usa a versão antiga, coerente com as idades no CAFE5, enquanto o relatório técnico usa a atualização de duas cadeias. Essas versões não devem ser fundidas. | Aceita com ajuste: a revisão usa a tabela posterior de duas cadeias, separa explicitamente a árvore CAFE5 anterior e informa ESS por cadeia <200 no nó focal. Não reatribui os resultados CAFE5 à árvore nova. |
| M13 — relevante | §3.3 e discussão: WGD ancestral idêntico, zero translocações, 297 blocos | Proporções de categoria não datam WGD; afirmações estruturais requerem rastreabilidade própria. | Aceita com ajuste: mantidas proporções verificadas; retiradas conclusões não estabelecidas por esses totais. |
| M14 — relevante | Introdução e §4.2: fisiologia quantitativa atribuída às espécies focais | Estudos de outras espécies são usados para detalhar mortalidade, potenciais hídricos e mecanismos focais. | Aceita com ajuste: contexto geral separado da classificação operacional das espécies; limiares e mecanismos focais sem evidência direta removidos. |
| M15 — editorial | Títulos grandiosos, métodos com resultados, repetição extensa da narrativa causal | A argumentação antecipa como fato o que deseja explicar. | Aceita: títulos descritivos, resultados no local adequado, discussão organizada por inferências permitidas. |

## Datação: decisão de versão

A tabela de duas cadeias contém médias 33,7699 e 9,6839 Ma para os nós focais, diferentes de 31,9147 e 9,7362 Ma na árvore dos 21 relatórios CAFE5. A cópia revisada não oculta essa diferença. O texto e a Tabela 1 foram gerados a partir do TSV high-ESS, cujo script usa percentis 2,5 e 97,5: são intervalos de caudas iguais, embora as colunas tenham “HPD” no nome. As médias das cadeias foram conferidas contra os arquivos brutos, cada qual com 30.001 estados. Os ESS e R-hat são os valores arquivados, não novos diagnósticos certificados.

## Verificação bibliográfica pontual e limites

O [resumo do artigo de Teodoro et al. (2021)](https://www.sciencedirect.com/science/article/abs/pii/S0098847221001866) identifica V. nivea como espécie tolerante no experimento. Ele sustenta contexto sobre compromisso entre produtividade e sobrevivência, mas não autoriza transplantar medidas para V. tubiflora e V. peripherica. A classificação focal e suas fontes devem ser documentadas diretamente. Não foi feita uma auditoria completa das citações.

A [página do artigo de Costa et al. (2017)](https://www.nature.com/articles/nplants201738) confirma autoria com Maia como terceira autora; a entrada original do mestre apresentava outra sequência de autores. Na cópia revisada, a entrada foi normalizada para os três primeiros autores seguidos de et al. A atualização não constitui revisão de toda a bibliografia.

As declarações de depósito público, licenciamento, financiamento e aprovação autoral foram preservadas como material fornecido, mas sinalizadas como não verificadas na cópia de trabalho. O DOI Zenodo terminado em 12345678 e os demais identificadores devem ser conferidos antes de uma versão pública; não foram tratados como depósitos validados. As chamadas de figuras não localizadas no corpo foram retiradas dos trechos reescritos; os arquivos gráficos não foram regenerados.

## Limites residuais

A revisão restaura a correspondência entre objetivo, método e conclusão e corrige inconsistências verificáveis. Ainda requerem trabalho factual: justificativa individual das calibrações e sensibilidade temporal; reconciliação funcional de famílias conflitantes; validação das cópias prioritárias; fontes fisiológicas específicas; verificação bibliográfica e das declarações; e montagem final das figuras. Nenhuma dessas etapas é declarada concluída apenas pela reescrita. Os métodos de sintenia foram incorporados com base no relatório técnico e nas tabelas locais, sem nova execução do classificador.

## Verificação da integração

A cópia revisada preserva literalmente as seções 2.6, 3.4 (incluindo Tabela 2) e 4.4 de Ka/Ks. Os links locais resolvem e as tabelas têm números consistentes de colunas. O manuscrito mestre original, o relatório técnico e o rascunho `chapter_01_draft.md` não foram modificados. O manifesto SHA-256 registra as versões de origem e revisada. Não foram produzidos novos gráficos nem executadas análises biológicas.

## Consolidação no manuscrito principal

A revisão foi integrada em `teamwork/01_drafts_and_outlines/chapter_macroevolution_master_draft.md`, com a cópia `_volpato_revised.md` sincronizada. As afirmações anteriores neste relatório de que o mestre não havia sido modificado descrevem a etapa de revisão em cópia, anterior à consolidação. O estado atual e os hashes constam de `volpato_consolidation_manifest_2026-09-15.json`.

A bibliografia do manuscrito foi restringida às 23 entradas citadas; 44 entradas sem chamada no texto atual permanecem nos arquivos anteriores preservados. As duas citações Zhang et al. (2018) foram diferenciadas em 2018a (ASTRAL) e 2018b (OSCA). A entrada CAFE5 foi corrigida para o título e paginação publicados, consultáveis na [página do artigo](https://academic.oup.com/bioinformatics/article/36/22-23/5516/6039105). A manutenção de uma entrada não significa que seu apoio a todas as afirmações foi auditado.

**Atualização de M11:** o uso de NDH tem origem identificável nos membros plastidiais de Arabidopsis presentes no OrthoFinder e no mapeamento KEGG. As descrições de Vellozia divergem, mas essa divergência não estabelece automaticamente que o enriquecimento está errado. O manuscrito distingue as fontes e mantém a função das cópias focais como pendência. Também diferencia as posições de cada espécie, incluindo dois modelos cromossômicos de OG0000332 em V. peripherica.

As próximas pendências substantivas são a validação das calibrações e a sensibilidade à árvore temporal, a validação gene a gene dos candidatos e as fontes fisiológicas específicas. Esses pontos permanecem explícitos; nenhuma análise foi reexecutada nesta consolidação.
