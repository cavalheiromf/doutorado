# Validações dos dados e modelos HyPhy

Esta pasta reúne as validações executadas em 16 de julho de 2026 sobre os
alinhamentos, as árvores e os resultados HyPhy da família OSCA. Os arquivos
originais não foram modificados.

## Ambiente e escopo

- HyPhy 2.5.99(MP);
- MUSCLE v3.8.1551, identificado a partir do executável usado pelo script de
  preparação; o README anterior informava incorretamente MUSCLE v5;
- código genético universal;
- alinhamentos de códons produzidos por alinhamento das proteínas seguido de
  retrotradução;
- árvores podadas da filogenia global e ramos terminais classificados como
  `Test` (*V. tubiflora*) ou `Reference` (*V. peripherica*).

## Integridade dos alinhamentos e das árvores

Todos os quatro alinhamentos apresentaram comprimentos divisíveis por três,
sem códons de parada internos, códons parcialmente interrompidos por lacunas ou
caracteres ambíguos. Os identificadores das sequências coincidiram integralmente
com as folhas das árvores.

| Conjunto | Sequências | Códons | Sítios com >20% de lacunas | Sítios com >50% de lacunas |
| --- | ---: | ---: | ---: | ---: |
| Global | 27 | 1.697 | 1.058 | 962 |
| OSCA1 | 10 | 1.029 | 268 | 257 |
| OSCA2 | 11 | 889 | 288 | 238 |
| OSCA3/4 | 6 | 904 | 233 | 171 |

O alinhamento global é particularmente esparso: somente 639 códons (37,7%)
permanecem quando são removidas as colunas com mais de 20% de lacunas. Nos
subclados, a mesma filtragem retém entre 67,6% e 74,3% dos códons.

As árvores não contêm clados internos formados exclusivamente por uma das duas
espécies. Por isso, não existem ramos internos que possam ser classificados de
forma não ambígua como `Test` ou `Reference`; a rotulagem apenas dos ramos
terminais é compatível com as topologias disponíveis.

## Auditoria dos sítios do Contrast-FEL

Foram auditados os 35 sítios com p nominal menor ou igual a 0,05 na reexecução
do Contrast-FEL. Oito apresentaram mais de 20% de lacunas: os sítios globais
401, 797, 803, 821 e 842 e os sítios 241, 270 e 824 de OSCA2. Em OSCA2, os
sítios 241 e 270 apresentaram, respectivamente, 63,6% e 54,5% de lacunas.
Nenhum dos 35 sítios permaneceu significativo após o controle de FDR já
aplicado na reexecução. Consequentemente, os sítios nominais não devem ser
descritos como evidência confirmada de seleção divergente.

## Triagem de recombinação e heterogeneidade filogenética

O GARD foi executado por subclado sob modelo de nucleotídeos, sem variação de
taxa entre sítios (`rv=None`), em modo `Faster` e com máximo de cinco pontos de
quebra. A opção de tolerância numérica recomendada pelo próprio HyPhy foi
ativada após uma diferença de cache de aproximadamente 1,8 × 10⁻⁶. Todos os
JSONs finais são válidos e os arquivos de erro estão vazios.

| Conjunto | Limites de partição, nt 1-based | Pontos selecionados | Δc-AIC contra ausência de partições | Δc-AIC contra uma única topologia | Razão de evidência topológica |
| --- | --- | ---: | ---: | ---: | ---: |
| OSCA1 | 451, 1.402, 1.758, 2.205 e 2.840 | 5 | 701,88 | 284,29 | 5,39 × 10⁶¹ |
| OSCA2 | 942 e 2.437 | 2 | 239,83 | 10,20 | 164,42 |
| OSCA3/4 | 2.005 e 2.329 | 2 | 9,27 | 7,95 | 53,20 |

OSCA1 atingiu o máximo configurado de cinco pontos, e o quinto ainda melhorou
o ajuste. Assim, cinco representa um limite inferior nesta triagem, não uma
estimativa definitiva. Um dos limites de OSCA1 ocorre a até três códons de uma
região com 90% de lacunas. Em OSCA3/4, um dos limites está próximo de uma
região com 66,7% de lacunas. Os limites de OSCA2 não apresentaram lacunas no
códon correspondente nem nos três códons adjacentes.

Segundo o critério de razão de evidência igual ou superior a 100 usado pelo
HyPhy Vision, OSCA1 e OSCA2 apresentam suporte para incongruência topológica
entre segmentos; OSCA3/4 permanece abaixo desse limiar. Entretanto, os
conjuntos contêm parálogos, são pequenos e apresentam regiões esparsas. Por
isso, a triagem demonstra heterogeneidade filogenética, mas não distingue por
si só recombinação, conversão gênica, erro de alinhamento ou histórias distintas
entre domínios.

Nenhum limite selecionado coincidiu exatamente com uma fronteira de códon. A
saída de nucleotídeos não deve, portanto, ser usada diretamente para cortar os
alinhamentos de códons. A confirmação codon-aware ou a definição biologicamente
justificada de blocos permanece necessária.

## Sensibilidade do RELAX à filtragem de lacunas

Foram geradas duas versões de cada alinhamento, removendo códons cuja fração de
lacunas fosse maior que 20% ou maior que 50%. O RELAX foi repetido com dez
pontos iniciais; os oito JSONs são válidos e os arquivos `relax.err` estão
vazios.

| Filtro | Conjunto | Códons retidos | K | p |
| --- | --- | ---: | ---: | ---: |
| >20% removidos | Global | 639 | 0,7130 | 0,000784 |
| >20% removidos | OSCA1 | 761 | 0,9047 | 0,5750 |
| >20% removidos | OSCA2 | 601 | 0,8017 | 0,3288 |
| >20% removidos | OSCA3/4 | 671 | 0,2435 | 0,00391 |
| >50% removidos | Global | 735 | 0,8105 | 0,0195 |
| >50% removidos | OSCA1 | 772 | 0,9274 | 0,6129 |
| >50% removidos | OSCA2 | 651 | 0,9482 | 0,7516 |
| >50% removidos | OSCA3/4 | 733 | 0,2649 | 0,00737 |

As duas filtragens mantiveram o relaxamento significativo no conjunto global e
em OSCA3/4. OSCA1 e OSCA2 permaneceram não significativos. Em especial, os
novos resultados reforçam que a antiga afirmação de relaxamento significativo
em OSCA2 não é reproduzível.

O resultado de OSCA3/4 é robusto à remoção de colunas esparsas, mas ainda deve
ser apresentado com cautela porque o GARD detectou partições preferenciais,
embora sem atingir a razão de evidência topológica de 100. O resultado global
também é robusto aos dois filtros, mas sua interpretação é limitada pela grande
fração de colunas removidas e pela reunião de subfamílias divergentes.

## Validações ainda necessárias

1. Repetir a triagem de heterogeneidade com configuração codon-aware ou com
   blocos definidos em fronteiras de códon.
2. Reavaliar os subclados com um segundo método de alinhamento de proteínas e
   comparar a estabilidade das partições, especialmente em OSCA1.
3. Se a incongruência de OSCA1 ou OSCA2 for confirmada, executar análises por
   bloco não recombinante com árvores e rótulos próprios. O RELAX requer uma
   filogenia consistente e não deve receber automaticamente a saída
   particionada do GARD.
4. Manter os sítios do Contrast-FEL como resultados exploratórios nominais,
   pois nenhum resistiu ao controle de FDR.

## Arquivos principais

- `alignment_qc.tsv`, `tree_qc.tsv` e `sequence_qc.tsv`: auditoria estrutural;
- `nominal_site_gap_audit.tsv`: ocupação dos sítios nominais;
- `filtered_alignments/`: alinhamentos filtrados e mapas de coordenadas;
- `gard/gard_summary.tsv`: síntese do GARD;
- `relax_gap_sensitivity/relax_gap_sensitivity_summary.tsv`: síntese do RELAX;
- `../scripts/validate_hyphy_inputs.py`;
- `../scripts/filter_hyphy_codon_alignments.py`;
- `../scripts/run_gard_validation.sh`;
- `../scripts/summarize_gard_validation.py`;
- `../scripts/run_relax_gap_sensitivity.sh`;
- `../scripts/summarize_relax_gap_sensitivity.py`.

Referências operacionais: [documentação oficial do
GARD](https://hyphy.org/methods/gard/) e [tutorial de linha de comando do
HyPhy](https://hyphy.org/tutorials/CL-prompt-tutorial/).
