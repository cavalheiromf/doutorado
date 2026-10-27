# Proveniência das anotações de OG0000317 e OG0000332

## Resultado

A associação dessas famílias à via KEGG ath00190 é rastreável aos membros de Arabidopsis presentes nos ortogrupos. Os rótulos de splicing e ligação a RNA pertencem a outra camada: descrições herdadas de Vellozia. A discrepância entre essas fontes não demonstra, por si só, um erro no mapeamento KEGG. A função de cada cópia em Vellozia continua sem validação nesta revisão.

| Ortogrupo | Membro de Arabidopsis no OrthoFinder | Locus no arquivo de enriquecimento | Anotação da referência | Descrição de Vellozia na tabela funcional | KEGG arquivado |
| --- | --- | --- | --- | --- | --- |
| OG0000317 | lcl\|NC_000932.1_cds_NP_051114.1_48257 | ARTHCP079 | ndhA, NADH dehydrogenase subunit 1, chloroplast | Pre-mRNA-splicing factor | ath00190; ath01100 |
| OG0000332 | lcl\|NC_000932.1_cds_NP_051113.1_48256 | ARTHCP078 | ndhI, NAD(P)H-quinone oxidoreductase subunit I | Glycine-rich RNA-binding protein | ath00190; ath01100 |

A identidade de ndhA/ArthCp079 foi conferida no [registro NCBI](https://www.ncbi.nlm.nih.gov/gene/844804). A associação de ArthCp078 a ndhI, à via map00190 e ao módulo de cloroplastos/cianobactérias consta do [registro KEGG K05580](https://www.kegg.jp/entry/K05580). Os nomes de subunidades foram consultados em 15/09/2026; não foi executada nova anotação de sequências.

## Arquivos locais confrontados

Os membros foram conferidos em `01_orthology/results/Results_Aug30/Orthogroups/Orthogroups.tsv`. A tabela `04_gene_families/functional_enrichment/orthogroup_functional_annotations.tsv` registra separadamente `Ath_Sequence_IDs`, `Ath_Locus_Tags`, `KEGG_Pathways`, `Vper_Annotation` e `Vtub_Annotation`. A presença dos dois ortogrupos na via também foi conferida em `functional_enrichment/intermediate/family_term_matrix.tsv`.

A tabela mestre v2 resume descrições e identificadores de outra forma. Seus rótulos não devem ser usados isoladamente para substituir a proveniência explícita dos membros de Arabidopsis. Ainda é necessário reconciliar a origem dos identificadores nucleares apresentados no campo `Arabidopsis_Orthologs` dessa tabela com o membro plastidial efetivamente presente no OrthoFinder.

## Posição dos modelos gênicos

As coordenadas e categorias foram extraídas das tabelas `vper_gene_duplications_annotated.tsv` e `vtub_gene_duplications_annotated.tsv`. Os 65 registros estão na [tabela de posições](annotation_gene_positions_2026-09-15.tsv).

| Ortogrupo | Espécie | Modelos | Em pseudomoléculas cromossômicas | Em contigs não ancorados |
| --- | --- | ---: | ---: | ---: |
| OG0000317 | V. peripherica | 5 | 0 | 5 |
| OG0000317 | V. tubiflora | 28 | 0 | 28 |
| OG0000332 | V. peripherica | 7 | 2 | 5 |
| OG0000332 | V. tubiflora | 25 | 0 | 25 |

Os dois modelos cromossômicos de OG0000332 em V. peripherica são `Vper.hapA.v1.chr5A.g155360.t1` e `Vper.hapA.v1.chr5A.g155370.t1`. Portanto, uma afirmação de que todos os membros dessa família estão em contigs não ancorados seria incorreta. O classificador atribui a categoria singleton a esses modelos; categoria de duplicação intra-genômica e pertencimento a ortogrupo são definições diferentes e não foram equiparadas nesta revisão.

## Decisão editorial

No manuscrito, distinguir “membro de referência NDH usado no mapeamento funcional” de “função demonstrada de todas as cópias em Vellozia”. Manter a interpretação fisiológica como hipótese. Não remover a associação KEGG apenas pela divergência das descrições, nem interpretar essa associação como validação da composição do ortogrupo. Não houve alteração dos arquivos de anotação originais, dos conjuntos de enriquecimento ou dos q-valores.

Esta conferência resolve a proveniência da atribuição e a distribuição física registrada. Não resolve integridade dos modelos, homologia gene a gene, possíveis transferências organelares, redundância de montagem ou atividade funcional.
