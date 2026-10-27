# Estratégia de implementação das sete recomendações para famílias gênicas

> **For agentic workers:** Use `executing-plans` para execução sequencial por entregáveis. Delegação é opcional e depende das instruções vigentes. As caixas abaixo registram conclusão verificável.

**Goal:** Consolidar a confiança nas cópias, funções e histórias evolutivas antes de testar a associação entre mudanças de famílias e arquitetura de duplicação.

**Architecture:** Preservar as entradas e resultados de referência; produzir uma versão integrada derivada, com proveniência por gene e família. Organizar a implementação em sete frentes, com contratos de dados e critérios de passagem entre quatro marcos. Este documento define a estratégia científica e operacional; não implementa nem executa análises.

**Tech Stack:** Scripts Python e shell existentes, TSV/JSON/YAML, CAFE5, classificações MCScanX e blocos JCVI arquivados, árvores gênicas e resultados MCMCTree. Registrar versões e ambientes antes das execuções; novas dependências só serão escolhidas após o inventário.

## Restrições globais

- Caminhos neste documento são relativos à raiz do repositório.
- Data de referência: 06/10/2026. Dados revisados em 05/10/2026 são a linha de base, sujeitos a auditoria.
- O repositório contém uma reorganização extensa em andamento. Não restaurar, mover ou consolidar alterações alheias para executar este plano.
- Universo atual: 17.750 ortogrupos originais; 15 excluídos por contagem >=100; 17.735 na entrada filtrada; 12.276 testados após filtro de raiz; 196 Tier A e 58 Tier B. Verificar os números por IDs, sem fixá-los no código.
- Significância CAFE é por família; mudanças por ramo são reconstruções. Repetições de otimização não são réplicas biológicas.
- Não tratar contagens ausentes como zero, genes sem classificação como singleton, nem função transferida como função experimental.
- Não atribuir causalidade adaptativa, origem do fenótipo ou data de WGD a partir de contagens e classes estruturais isoladas.
- Outputs novos devem ir para diretórios de execução identificados por `run_id`; só promover uma versão a referência depois dos controles.
- Plano de hipóteses, universos e testes múltiplos deve ser congelado antes de executar os testes novos. Hipóteses geradas após inspeção continuam exploratórias.

## Evidências locais que orientam a ordem

- `docs/macroevolution/reviews/analises_complementares_classificacao_2026-10-05.md`: integração duplicação/CAFE desatualizada; nos 11.726 IDs compartilhados auditados, 51 diferenças de Tier e 32 de mudança em cada Vellozia. Esses números pertencem à auditoria, não são tolerâncias aceitáveis.
- `docs/macroevolution/reviews/annotation_provenance_2026-09-15.md`: divergências entre descrição de Vellozia e referência plastidial utilizada no enriquecimento.
- `chapter_macroevolution/04_gene_families/priority_gene_trees/README.md`: árvores exploratórias e funções pendentes de reconciliação.
- `chapter_macroevolution/workflow/scripts/04_build_comparative_duplication_table.py`: integração existente a atualizar, evitando duplicar sua responsabilidade.
- `chapter_macroevolution/workflow/scripts/04_classify_gene_duplications.py`: usa tabela antiga e caminho de homologia contendo `P98L0.inverse`; confrontar com o comando efetivamente usado nos resultados arquivados antes de reproduzir a classificação.
- `chapter_macroevolution/workflow/scripts/04_enrichment_run_pipeline.sh`: remove intermediários após validação; preservar os pequenos artefatos de auditoria antes da limpeza.

## Ordem e dependências

| Marco | Frentes | Produto que permite avançar |
|---|---|---|
| A — referência rastreável | R7 inicial, R1 inicial, R2 | IDs conciliados, tabelas integradas e manifesto |
| B — confiança nas cópias | R4 e R6; conclusão de R1 | Evidência por cópia, conflitos explicitados e exclusões auditadas |
| C — testes e sensibilidade | R3 e R5 | Efeitos estimados, controles e estabilidade documentados |
| D — versão científica consolidada | R7 final | Relatório, figuras e documentação consistentes com a execução validada |

R4 e R6 podem avançar independentemente após R2. R3 pode ter um piloto metodológico após R2, mas sua interpretação final depende de R4. R5 depende de uma definição congelada das entradas alternativas. R7 acompanha todos os marcos.

## Contratos de dados

Criar produtos sob `chapter_macroevolution/04_gene_families/integrated_evidence/<run_id>/`.

| Arquivo | Chave e campos obrigatórios | Regra |
|---|---|---|
| `input_manifest.tsv` | `asset_id`, caminho, SHA256, tamanho, versão/fonte, papel, disponibilidade | Registrar também entradas indisponíveis; não substituí-las silenciosamente |
| `gene_evidence.tsv` | `Species`, `GeneID`, `TranscriptID`, `ProteinID`, `FamilyID`, montagem, coordenadas, `dup_type`, ancoragem, integridade CDS/proteína, fonte funcional, estado de conflito | Uma linha por locus selecionado; tabela auxiliar para isoformas e IDs alternativos |
| `gene_id_crosswalk.tsv` | espécie, ID original, tipo de ID, locus canônico, fonte, estado do mapeamento | Ambiguidades explícitas; sem remoção heurística de sufixos sem validação |
| `family_evidence.tsv` | `FamilyID`, contagens por espécie, mudanças por ramo, Tier, estabilidade, contagens por classe estrutural, cobertura do mapeamento, conflitos e flags de QC | Uma linha por ortogrupo do universo completo; inferência CAFE nula para famílias não testadas |
| `family_annotation_decisions.tsv` | família/gene, rótulo original, fonte, evidência, rótulo adotado, decisão, motivo | Preservar as fontes discordantes e não substituir função por votação |
| `validation.json` | teste, universo, observado, esperado, estado, evidência | Estados `pass`, `fail`, `not_assessed`; falta de dado nunca equivale a aprovação |

Os schemas serão documentados em `chapter_macroevolution/04_gene_families/integrated_evidence/README.md`. Manter contagem bruta, contagem validada e motivo de mudança em colunas distintas; atualizar entradas CAFE apenas em novas execuções.

## R7 — Rastreabilidade, primeira entrega e manutenção contínua

**Modificar:** `chapter_macroevolution/workflow/README.md`, `chapter_macroevolution/04_gene_families/README.md` e `chapter_macroevolution/workflow/scripts/04_enrichment_run_pipeline.sh`.

**Criar:** `chapter_macroevolution/workflow/scripts/04_inventory_family_evidence.py`; manifestos e relatórios no diretório integrado.

- [ ] Inventariar fontes atuais, symlinks, arquivos ignorados pelo Git, ambientes e executáveis. Verificar os caminhos em `00_data`, `01_orthology` e `03_dating`; não inferir disponibilidade apenas de `rg --files` padrão.
- [ ] Registrar entradas atuais, parâmetros, sementes, árvore, versões e hashes. Identificar explicitamente a execução CAFE representativa.
- [ ] Corrigir comandos e links após verificar o destino real. Conferir o README inteiro; trocar prefixos sem conferir dependências não basta.
- [ ] Preservar `covariate_balance_qc.tsv`, definição dos estratos, universos e saída do validador em `results/audit/<run_id>/` antes da limpeza do enriquecimento.
- [ ] Tornar falha de validação impeditiva da promoção de resultados. Registrar saídas de erro sem apagar a execução que falhou.
- [ ] No fechamento, regenerar relatórios e figuras a partir das tabelas aprovadas; manter uma lista explícita de arquivos históricos.

**Aceite:** todo número da síntese aponta para tabela, execução e fonte; nenhum comando documentado aponta para script ausente; auditoria permanece disponível após limpeza. Um teste de integração deve simular validação falha e comprovar que a execução não é promovida.

## R1 — Reconciliação funcional

**Modificar:** `chapter_macroevolution/workflow/scripts/04_enrichment_01_build_family_annotations.py`, quando houver erro demonstrado de mapeamento; documentação interpretativa só depois das decisões registradas.

**Criar:** `chapter_macroevolution/workflow/scripts/04_reconcile_family_annotations.py` e `family_annotation_decisions.tsv`.

- [ ] Rastrear membro real do ortogrupo até proteína, locus e referência funcional usada pelo enriquecimento.
- [ ] Revisar primeiro OG0000306, OG0000281, OG0000317 e OG0000332; expandir para todas as famílias destacadas no manuscrito e os conflitos detectados automaticamente.
- [ ] Manter separadas descrição transferida, domínio observado, ortologia inferida e validação experimental.
- [ ] Classificar rótulos como sustentados, provisórios, conflitantes ou não caracterizados, com justificativa por fonte.
- [ ] Medir o impacto de qualquer correção na matriz funcional. Se a associação família-termo mudar, regenerar enriquecimento e auditoria; se apenas a redação mudar, registrar que os testes não mudaram.

**Aceite:** zero rótulos mecanísticos sem fonte na lista prioritária; conflitos não resolvidos ficam visíveis. Uma família pode concluir esta etapa como não caracterizada.

## R2 — Integração por gene e família

**Modificar:** `chapter_macroevolution/workflow/scripts/04_build_comparative_duplication_table.py` para consumir a referência atual e caminhos configuráveis.

**Criar:** `chapter_macroevolution/workflow/scripts/04_build_gene_evidence.py`, `chapter_macroevolution/workflow/scripts/integrity/04_test_family_evidence.py` e schemas descritos acima.

- [ ] Construir crosswalk proteína–transcrito–locus–ortogrupo por espécie; documentar a regra de isoforma representativa do conjunto original.
- [ ] Integrar classes e coordenadas das duas Vellozia, preservando genes sem mapeamento e sem classificação.
- [ ] Integrar contagens das sete espécies e campos CAFE exclusivamente por `FamilyID`; reportar junções sem correspondência e cardinalidade.
- [ ] Agregar por família sem multiplicar linhas por isoformas, descrições ou múltiplos termos GO.
- [ ] Comparar os campos CAFE da integração com a tabela atual: concordância exata dos IDs compartilhados, Tier e mudanças reconstruídas.

**Aceite:** soma das classes conhecidas mais não classificadas igual ao total de loci representados; diferenças em relação à contagem CAFE são identificadas por gene e justificadas, nunca corrigidas silenciosamente.

**Casos de teste necessários:** mesmo locus com duas isoformas; mesmo GeneID em espécies diferentes; locus sem coordenadas; associação ambígua a famílias; família excluída do CAFE; join que duplicaria linhas; discrepância real entre contagem e membros.

## R4 — Validação estrutural e de cópias

**Criar:** `chapter_macroevolution/workflow/scripts/04_audit_priority_copies.py`; resultados em `integrated_evidence/<run_id>/copy_qc/`.

**Reutilizar:** sequências, BED/GFF, blocos sintênicos, classificações e árvores existentes. Verificar a proveniência da homologia MCScanX antes de qualquer rerun.

- [ ] Definir lote piloto: as cinco famílias com árvores prioritárias; OG0000014, OG0000156 e OG0000278; OG0000021 como caso excluído; controles de famílias sem sinal CAFE e com tamanhos comparáveis quando disponíveis.
- [ ] Para cada cópia, conferir comprimento, completude CDS, tradução, stops internos, ambiguidades, sobreposição entre modelos e suporte de domínios.
- [ ] Avaliar vizinhança, blocos, identidade e cobertura de alinhamento; similaridade alta isolada não autoriza eliminar cópias.
- [ ] Para origem organelar, comparar homologia e contexto; distinguir sequência organelar, inserção nuclear candidata e origem não resolvida.
- [ ] Inventariar reads e RNA-seq compatíveis com montagem/amostra. Se ausentes, registrar cobertura e expressão como não avaliadas e continuar com a evidência estrutural.
- [ ] Atualizar as tabelas integradas e repetir a auditoria dos totais. Expandir o protocolo do piloto aos grupos prioritários definidos por critérios explícitos.

**Aceite:** cada cópia examinada tem evidências e estado; nenhuma exclusão automática por estar em contig não ancorado. Critérios de contagem corrigida só entram em R5 após revisão do motivo por cópia.

## R6 — Famílias excluídas e ausências

**Modificar:** `chapter_macroevolution/workflow/scripts/04_prep_family_cafe5.py` para emitir razão de retenção/exclusão sem mudar inadvertidamente o filtro de referência.

**Criar:** `chapter_macroevolution/workflow/scripts/04_audit_excluded_families.py`; `excluded_families.tsv` e `absence_review.tsv` no diretório integrado.

- [ ] Fazer diferenças de conjuntos de IDs: originais, filtrados e efetivamente testados. Distinguir famílias sem presença inferida na raiz, contagem extrema e qualquer perda inesperada de processamento.
- [ ] Descrever funções e contagens das 15 famílias grandes sem atribuir q-valores CAFE a elas.
- [ ] Priorizar OG0000021 e ausências que mudam a interpretação dos contrastes. Buscar homologia também na sequência genômica, além do proteoma anotado, quando a montagem estiver disponível.
- [ ] Conferir sintenia e qualidade da região para classificar ausência anotada, sequência candidata não anotada, região não resolvida ou perda candidata sustentada.
- [ ] Manter famílias excluídas em análise descritiva/filogenética própria. Só avaliar outro limiar CAFE depois de diagnóstico numérico; não dividir famílias para forçar inclusão.

**Aceite:** todos os IDs originais têm destino documentado; ausência não é convertida automaticamente em perda evolutiva. Mudanças de composição de ortogrupos exigem mapa entre versões.

## R3 — Associação entre expansão e duplicação local

**Criar:** `chapter_macroevolution/workflow/config/family_duplication_hypotheses.yaml`, `chapter_macroevolution/workflow/scripts/04_test_expansion_duplication_association.py` e `chapter_macroevolution/workflow/scripts/integrity/04_test_expansion_duplication_association.py`.

**Pergunta primária:** entre famílias Tier A avaliáveis estruturalmente em cada Vellozia, mudanças terminais positivas estão associadas a maior fração atual de genes tandem/proximais?

- [ ] Congelar dois contrastes primários, um por espécie: `Change_species > 0` versus `Change_species <= 0`, dentro de Tier A. O indicador terminal restritivo é análise secundária distinta.
- [ ] Usar família como unidade. Desfecho: `(tandem + proximal) / genes_com_classificacao`; reportar separadamente cobertura de classificação e ancoragem. Fração local não mede a fração de ganhos causada por duplicação local.
- [ ] Reportar inicialmente distribuições, diferença média entre grupos e intervalos por reamostragem de famílias. Escolher o número de reamostragens e semente no arquivo de configuração antes da execução.
- [ ] Testar a associação por permutação de rótulos de mudança entre famílias comparáveis por tamanho e cobertura, com 10.000 permutações e semente 20261006. Registrar limites dos estratos e exigir presença de ambos os grupos para contribuição inferencial.
- [ ] Mostrar efeito bruto e condicionado por tamanho: tamanho atual também pode refletir expansão, portanto o ajuste responde a uma pergunta condicional e pode remover parte do sinal biológico.
- [ ] Aplicar BH aos dois testes primários. Contrastes secundários e cenários de QC devem ser identificados separadamente e ter sua própria família de testes declarada previamente.
- [ ] Sensibilidades: excluir cópias/famílias com conflitos demonstrados; excluir flags organelares/transposons; restringir a sinais preservados em k=3; repetir com subconjunto de alta cobertura estrutural definido antes dos resultados.
- [ ] Testar código em casos sem associação, associação construída, denominador zero, estratos sem permutabilidade e ordens diferentes de linhas. Simulação verifica comportamento, não valida o modelo biológico.

**Aceite:** efeitos e incerteza reportados inclusive quando não significativos; denominadores rastreáveis; falta de balanço ou permutabilidade leva a resultado descritivo. Não tratar as duas espécies ou todos os genes de uma família como réplicas evolutivas independentes.

## R5 — Sensibilidade de idades, contagens e ortogrupos

**Criar:** `chapter_macroevolution/workflow/config/family_sensitivity.yaml`, `chapter_macroevolution/workflow/scripts/04_prepare_family_sensitivity.py`, `chapter_macroevolution/workflow/scripts/04_summarize_family_sensitivity.py`.

**Reutilizar com revisão de parâmetros e saídas:** `04_run_cafe5_multirep_stage1.slurm`, `04_run_cafe5_multirep_stage2.slurm`, `04_select_error_model.py` e `04_evaluate_cafe5_models.py`, todos em `chapter_macroevolution/workflow/scripts/`.

- [ ] Primeiro reproduzir a leitura e sumarização da referência arquivada, sem uma nova execução pesada.
- [ ] Idades: validar amostras posteriores conjuntas disponíveis em `03_dating/results/`, burn-in, convergência e unidades. Não montar árvores combinando limites marginais de nós independentemente.
- [ ] Piloto computacional: selecionar 10 árvores posteriores válidas de forma reproduzível, mantendo a topologia; iniciar com k=2 e três otimizações por entrada. Esses números são orçamento inicial, não garantia de precisão. Expandir se as conclusões ou otimizações forem instáveis.
- [ ] Contagens: comparar a entrada de referência com versão corrigida apenas por evidência de R4/R6. Para ambiguidades, usar cenários explicitamente delimitados, sem aplicar +/-1 arbitrário ao genoma inteiro.
- [ ] Ortogrupos: examinar famílias com heterogeneidade sustentada por árvore/domínios. Se houver nova delimitação, reconstruir entradas e registrar relações um-para-muitos; não comparar q-valores como se os IDs representassem a mesma hipótese.
- [ ] Variar um eixo por vez no piloto. Em entradas modificadas, reestimar parâmetros e erro quando aplicável; manter constantes apenas os componentes que definem o contraste de sensibilidade.
- [ ] Registrar falhas e critérios de retenção das otimizações antes de olhar a lista de significância. Recalcular FDR sobre o universo efetivamente testado de cada execução.
- [ ] Resumir persistência de famílias, sinal por ramo, magnitude de mudança e falhas. Frequência entre cenários é estabilidade, não probabilidade posterior de adaptação.

**Aceite:** nenhuma árvore com comprimentos inválidos ou unidades desconhecidas; cenários rastreáveis; conclusões classificadas como estáveis, sensíveis ou não avaliadas. Se não houver amostras posteriores utilizáveis, sensibilidade temporal permanece não avaliada até recuperar/regerar a datação.

## Validação e publicação interna dos produtos

- [ ] Executar somente testes pertinentes aos scripts alterados, usando os casos de integridade acima; em scripts shell, verificar sintaxe e testar falha/limpeza com entradas pequenas.
- [ ] Após o piloto, registrar tempo, memória, disponibilidade de dados e número de famílias aprovadas para estimar o lote completo. Não prometer duração do CAFE ou da anotação sem esse benchmark local.
- [ ] Revisar tabela de hipóteses e resultados, incluindo efeitos nulos, conflitos e limitações.
- [ ] Gerar três produtos científicos: história das mudanças; associação com arquitetura de duplicação; catálogo de candidatos com evidência por cópia.
- [ ] Gerar síntese em `docs/macroevolution/reviews/gene_family_evidence_consolidation.md` com links para execuções e status das sete recomendações.
- [ ] Promover a execução somente se os controles obrigatórios passarem; análises biologicamente inconclusivas podem ser completas e corretamente reportadas.

## Escopo e recursos

O primeiro ciclo entrega R7 inicial + R1 piloto + R2. O segundo resolve R4/R6 e fecha decisões de anotação. O terceiro executa R3 e o piloto R5. O quarto expande apenas as análises que precisam de mais evidência e consolida o capítulo. Leituras/integrações podem rodar localmente; buscas extensas, novas árvores e CAFE devem ter recursos estimados no piloto antes de submissão ao cluster.

Reads, RNA-seq e ferramentas de anotação disponíveis ainda precisam de inventário. Sua ausência limita as perguntas correspondentes, mas não bloqueia toda a estratégia. Novas ferramentas e bases devem ter versão, licença e compatibilidade verificadas antes da implementação.

## Base metodológica e limites

- R1, R2, R4 e R7: **Community standard**, aplicadas à consistência, validação e proveniência deste conjunto.
- R3, R5 e R6: **Emerging / exploratory** para os contrastes e desenhos novos propostos aqui; isso não classifica CAFE ou sintenia como métodos emergentes.
- CAFE5: https://doi.org/10.1093/bioinformatics/btaa1022 ; documentação oficial: https://github.com/hahnlab/CAFE5 .
- Inferência filogenética de ortologia e duplicações: https://doi.org/10.1186/s13059-019-1832-y .
- Aplicabilidade: genômica comparativa nas sete espécies da tabela e contexto estrutural principalmente nas duas Vellozia. O desenho atual não oferece replicação suficiente para atribuir diferenças gerais à estratégia hídrica.
- Validação prévia: identidade dos loci, proveniência de montagens/árvores, oportunidade de classificação estrutural e integridade das entradas. Uma análise estável continua condicionada a essas fontes.
