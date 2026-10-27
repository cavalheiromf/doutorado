# Classificação das análises complementares — 05/10/2026

Nenhuma análise foi reexecutada. Organização não equivale a validação de todos os resultados biológicos.

| Material | Estado e decisão |
|---|---|
| Ka/Ks `pair_specific_2026-09-11` | Referência atual conforme CURRENT_RUN.txt; manter: 16.609 pares, 16.567 razões interpretáveis, 233 com ω > 1; triagem descritiva |
| Ka/Ks `corrected_2026-09-10` | Análise corrigida de outro recorte; manter os 1.513 ortogrupos de cópia única nas sete espécies para comparação |
| Três tabelas Ka/Ks antigas na raiz e anotador associado | Legacy confirmado pelo README; separados com links; erro anterior de correspondência de códons |
| Sintenia e classificação básica de duplicações | Dados reutilizáveis, sem nova auditoria de inferência; mantidos BED, CDS, homologias, blocos, gene_type, GFF, tabelas por gene e resumos genômicos |
| Integração duplicação/CAFE | Intermediária desatualizada; separados tabela conjunta, dois recortes de famílias expandidas e relatório anterior |
| Landscape de duplicação e gerador | Legacy como figura integrada; separados os dois pares PNG/PDF e o gerador com rótulos fixos anteriores |
| Cinco árvores gênicas prioritárias | Exploratórias; mantidas com README; reconciliação de anotação pendente |
| Domínios de OG0000021 | Preparatória; FASTA mantidos, results/ vazio; README explicita recorte fora do CAFE filtrado |

## Comparação verificável

A tabela integrada de duplicação contém 14.711 ortogrupos. Entre os **11.726 IDs compartilhados** com a tabela comparativa atual, há **51 diferenças de Evidence_Tier** e **32 diferenças de Change_Vper**, assim como **32 de Change_Vtub**. IDs ausentes não foram contados como discrepâncias. O recorte antigo contém 177 Tier A, 42 Tier B e 68 Tier C; os universos distintos impedem comparar esses totais diretamente a 196/58/63.

O recorte de famílias expandidas apresenta OG0000002 com Vper +9, enquanto a tabela atual registra +10. O gerador de landscape fixa esse exemplo em +9 e usa outras descrições/mudanças fixas. O painel genômico pode continuar informativo, mas a figura integrada não deve ser reutilizada inteira como evidência atual.

Resumos genômicos conferidos: Vper tem 26.466 genes, tandem 3.613 e proximal 2.012; Vtub tem 25.551 genes, tandem 2.779 e proximal 1.299. Reproduzem as proporções locais usadas no turnover, sem demonstrar o mecanismo causal das expansões.

## Árvores e domínios

As famílias das árvores (OG0000306, OG0000301, OG0000317, OG0000332 e OG0000281) são Tier A atual. As descrições atuais incluem proteína quinase para OG0000306 e proteína não caracterizada para OG0000281. Os rótulos DREB/UGT do relatório anterior não devem ser transportados automaticamente. Alinhamentos e função de cada cópia não foram revalidados.

OG0000021 está na entrada completa, mas não na filtrada nem na tabela CAFE atual. Sua pasta de domínios é uma investigação separada sobre uma família excluída do recorte CAFE; ausência de resultados finais não torna os FASTA inválidos.

## Rastreabilidade

O manifesto `legacy/2026-10-05/manifest.json` reúne **28 itens**: 15 da primeira etapa e 13 desta. Mantêm links relativos e hashes preservados. Árvores, sequências de domínios, execuções CAFE/MCMC e análises corrigidas de Ka/Ks não foram movidas.

Os scripts 11 e 13 de integração permanecem disponíveis, mas os produtos integrados precisam ser regenerados para uso atual. O script 13 ainda menciona `Tier_B_Moderate` no ordenamento: registrado, não corrigido ou executado nesta separação.
