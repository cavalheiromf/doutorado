# Reexecução validada do HyPhy

Esta rodada reexecutou as análises RELAX e Contrast-FEL da família OSCA sem
alterar os JSONs anteriores. Os resultados foram produzidos com HyPhy
2.5.99(MP), usando *Vellozia peripherica* como grupo `Reference` e *Vellozia
tubiflora* como grupo `Test`.

## Proveniência e controle de qualidade

A execução completa ocorreu entre 16:52:55 e 17:24:26 de 16 de julho de 2026.
Os quatro alinhamentos estavam em quadro, sem caracteres inesperados. As
árvores continham 14 ramos `Reference` e 13 `Test` na análise global; os
subclados continham 5/5 ramos em OSCA1, 6/5 em OSCA2 e 3/3 em OSCA3+4. Os
checksums dos arquivos de entrada foram verificados após a execução.

Os oito JSONs da rodada completa foram validados por um parser JSON. Todos os
arquivos `.err` estavam vazios. A execução utilizou `p <= 0,05` para os testes
nominais do Contrast-FEL e `q <= 0,20` para o relatório de FDR.

## RELAX

| Conjunto | K | LRT | p-valor | Leitura da reexecução |
| --- | ---: | ---: | ---: | --- |
| Família completa | 0,7988 | 8,0983 | 0,00443 | Relaxamento em `Test`; concordante com a rodada anterior |
| OSCA1 | 0,9262 | 0,2540 | 0,61430 | Sem diferença significativa |
| OSCA2 | 0,8255 | 0,9939 | 0,31880 | Sem diferença significativa nesta rodada |
| OSCA3+4 | 0,2459 | 7,9757 | 0,00474 | Relaxamento em `Test`; direção concordante com a rodada anterior |

O RELAX de OSCA2 foi sensível à otimização. A execução antiga havia produzido
K = 0,2828 e p = 3,43 × 10^-5, mas combinava um ajuste alternativo melhor com
um ajuste nulo substancialmente pior. As novas execuções com 1, 10 e 25 pontos
iniciais produziram K entre 0,8154 e 0,8522 e p entre 0,3130 e 0,3367. Os logs
também registraram superfície de verossimilhança plana. Portanto, a evidência
de relaxamento significativo em OSCA2 não foi reproduzida e não deve ser usada
como conclusão biológica enquanto a otimização não for resolvida.

Em OSCA3+4, o resultado permaneceu significativo nas rodadas antiga, nova e de
robustez, com p entre 0,00364 e 0,00606. Entretanto, K variou de 0,2459 até um
valor no limite inferior do parâmetro na rodada com 25 pontos iniciais. A
direção do efeito é reprodutível, mas sua magnitude deve ser tratada com
cautela.

## Contrast-FEL

| Conjunto | Códons testados | Sítios com p nominal <= 0,05 | Sítios com FDR <= 0,20 |
| --- | ---: | ---: | ---: |
| Família completa | 1.697 | 14 | 0 |
| OSCA1 | 1.029 | 6 | 0 |
| OSCA2 | 889 | 14 | 0 |
| OSCA3+4 | 904 | 1 | 0 |

Os sítios nominais de OSCA1 foram 98, 181, 252, 430, 710 e 973. Em OSCA2,
foram 8, 71, 76, 147, 191, 241, 270, 308, 394, 395, 432, 596, 720 e 824. Em
OSCA3+4, o sítio nominal foi 593. Nenhum desses sítios permaneceu significativo
após a correção FDR do HyPhy. Eles podem ser mantidos apenas como candidatos
exploratórios e não devem ser descritos como sítios sob seleção divergente
estatisticamente confirmada.

A análise global recuperou 14 sítios nominais. O sítio 1526, presente entre os
15 candidatos da execução anterior, não se repetiu abaixo de p = 0,05. Os
sítios globais ricos em lacunas continuam inadequados para interpretação sem a
auditoria dos alinhamentos por subclado.

## Arquivos principais

- `relax_summary.tsv`: resultados RELAX da reexecução completa;
- `contrast_fel_summary.tsv`: contagens, sítios nominais e resultados de FDR;
- `relax_robustness_summary.tsv`: execuções com 10 e 25 pontos iniciais;
- `provenance/`: versão do HyPhy, datas e checksums;
- `global/`, `osca1/`, `osca2/` e `osca3_4/`: JSONs e logs completos;
- `robustness/`: JSONs e logs das análises adicionais de RELAX.

## Interpretação conservadora para o documento de resultados

A família completa apresenta evidência de relaxamento de seleção em *V.
tubiflora*, mas esse sinal não pode ser atribuído igualmente a todas as
subfamílias. OSCA1 não mostrou mudança significativa. OSCA3+4 manteve evidência
de relaxamento, embora a magnitude de K seja instável. O resultado anteriormente
relatado para OSCA2 não foi reprodutível. O Contrast-FEL não identificou nenhum
sítio significativo após correção para múltiplos testes.

Antes da redação final, ainda devem ser avaliados recombinação, qualidade local
dos alinhamentos por códons, efeito de ramos internos não classificados e
estabilidade adicional dos modelos RELAX em superfícies planas.
