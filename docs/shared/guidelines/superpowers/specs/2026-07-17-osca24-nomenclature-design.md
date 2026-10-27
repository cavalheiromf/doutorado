# Padronização da nomenclatura de OSCA2.4

## Objetivo

Propagar uma nomenclatura inequívoca para as duas cópias de OSCA2.4 de
*Vellozia peripherica* aos arquivos derivados do projeto, sem alterar os
identificadores genômicos originais nem apagar saídas brutas usadas como
evidência histórica.

## Contrato canônico

| Identificador genômico | Nome curto canônico |
| --- | --- |
| `Vper.hapA.v1.chr1A.g023030.t1` | `VpOSCA2.4a` |
| `Vper.hapA.v1.chr1A.g023020.t1` | `VpOSCA2.4b` |
| `Vtub.hapA.v1.chr1A.g020650.t1` | `VtOSCA2.4` |

O nome `VpOSCA2.4` sem sufixo não poderá identificar uma proteína, gene,
promotor ou folha de árvore individual. Ele poderá permanecer apenas em prosa
que se refira coletivamente ao grupo das duas parálogas.

## Estratégia

Será usada correção determinística com regeneração seletiva. O arquivo
`analyses/01_gene_identification/results/oscasIDs.txt` será a tabela de
tradução entre identificadores genômicos e nomes curtos. Quando um derivado
contiver identificadores genômicos, a substituição será feita diretamente por
essa tabela. Quando contiver apenas coordenadas, a atribuição será resolvida
pela correspondência com o locus genômico que originou a coordenada. Não serão
feitas substituições globais de `VpOSCA2.4`, pois isso poderia colapsar ou
inverter as duas cópias.

## Escopo dos arquivos derivados

A correção abrangerá:

- tabela resumida de domínios de *V. peripherica*;
- árvore filogenética com nomes curtos;
- arquivos derivados de sintenia que usam nomes curtos;
- BED e FASTA de loci e promotores;
- resultados PlantCARE processados e contagens de motivos;
- tabelas de expressão, redes e taxas evolutivas que usem nomes curtos;
- documentos de resultados e scripts que produzam esses derivados.

Saídas brutas do HMMER, InterProScan, IQ-TREE, PlantCARE e outras ferramentas
externas serão preservadas quando contiverem os identificadores originais. Um
arquivo bruto só será renomeado se o nome ambíguo tiver sido introduzido pelo
próprio projeto, e nunca se isso alterar seu conteúdo científico original.

## Fluxo de atualização

1. Confirmar, em cada registro ambíguo, o identificador genômico ou a
   coordenada de origem.
2. Corrigir primeiro os derivados mais próximos da fonte: tabela de domínios,
   árvore renomeada e arquivos de coordenadas.
3. Regenerar, quando houver script local determinístico, os derivados de nível
   posterior.
4. Ajustar diretamente apenas os derivados que não puderem ser regenerados.
5. Atualizar a documentação para remover pendências que tenham sido resolvidas
   e manter explícitas as limitações ainda existentes.

## Tratamento de erros

Uma ocorrência ambígua sem identificador ou coordenada suficiente não será
atribuída por ordem de arquivo. Ela será mantida inalterada e reportada como
bloqueio. Se um script produzir novamente `VpOSCA2.4` sem sufixo para uma cópia
individual, o script deverá ser corrigido antes que sua saída seja aceita.

## Validação e critérios de aceitação

A mudança será aceita somente se:

1. `oscasIDs.txt` mantiver uma relação um-para-um entre os 14 identificadores
   de *V. peripherica* e 14 nomes curtos únicos;
2. `g023030.t1` estiver sempre associado a `VpOSCA2.4a` e `g023020.t1` sempre a
   `VpOSCA2.4b`;
3. não existir `VpOSCA2.4` sem sufixo em campos que representam entidades
   individuais;
4. a árvore renomeada conservar exatamente o mesmo número de folhas e os
   mesmos comprimentos de ramo da árvore baseada em identificadores;
5. os arquivos de promotores conservarem coordenadas, sequências e número de
   registros, mudando apenas os identificadores;
6. as tabelas de motivos apresentarem linhas separadas para `VpOSCA2.4a` e
   `VpOSCA2.4b`;
7. `VtOSCA2.4` e os demais genes OSCA permanecerem inalterados;
8. uma busca final não encontrar inversões de `a` e `b` nem ocorrências
   individuais sem sufixo.

## Fora de escopo

Esta etapa não repetirá buscas HMM, predição de domínios, inferência
filogenética, análise de sintenia, RNA-seq, PlantCARE ou STRING. Também não
alterará interpretações biológicas além do necessário para refletir a
nomenclatura corrigida.
