# Validação da rerun RNA-seq com STAR GeneCounts

As matrizes novas foram construídas a partir de `ReadsPerGene.out.tab`, usando
a coluna antissenso (coluna 4), apropriada para as bibliotecas reversas. Foram
mantidas 9 bibliotecas de *V. peripherica* e 8 de *V. tubiflora*; `VT1R` não
possui biblioteca sequenciada e permaneceu ausente.

## Comparação com a análise anterior

| Espécie | Contraste | DEGs antigos | DEGs novos | Sobreposição | Correlação log2FC | Concordância de direção |
|---|---|---:|---:|---:|---:|---:|
| Vper | Root vs Leaf | 6.619 | 6.404 | 6.167 | 0,940 | 98,3% |
| Vper | Root vs Stem | 159 | 79 | 64 | 0,830 | 97,1% |
| Vper | Stem vs Leaf | 6.838 | 6.606 | 6.389 | 0,932 | 98,3% |
| Vtub | Root vs Leaf | 6.238 | 5.919 | 5.777 | 0,974 | 98,3% |
| Vtub | Root vs Stem | 4.498 | 4.064 | 3.921 | 0,930 | 98,2% |
| Vtub | Stem vs Leaf | 7.848 | 7.508 | 7.347 | 0,947 | 98,5% |

Os números usam `padj < 0,05` como critério de significância. A rerun reduz
moderadamente o número de genes significativos, mas preserva fortemente a
direção dos efeitos e a ordenação dos `log2FC`. A principal diferença esperada
é metodológica: a análise nova usa contagens de fragmentos orientadas do STAR,
enquanto a análise anterior utilizava a tabela featureCounts sem orientação e
sem `--countReadPairs`.

## Conclusão operacional

As conclusões globais de expressão são robustas à troca de matriz, mas os
valores da rerun devem substituir os valores preliminares no texto final. As
interpretações de `VT2R` continuam condicionadas à sua baixa taxa de
mapeamento; o mapeamento cruzado não sustentou troca de identidade com `VP2R`.

## Sensibilidade sem `VT2R`

Foi executada uma análise adicional excluindo `VT2R`. Essa análise deixou
*V. tubiflora* com apenas uma réplica de raiz (`VT3R`); portanto, os contrastes
envolvendo raiz nessa condição não têm replicação suficiente para sustentar uma
inferência confirmatória. A sensibilidade pode ser usada apenas para avaliar a
estabilidade descritiva dos resultados, não para substituir a análise
principal. A análise principal mantém `VT2R`, com a baixa qualidade de
alinhamento explicitamente registrada como limitação.

## `lfcShrink` para visualização

Foi aplicado `lfcShrink(type = "normal")` aos seis contrastes, exclusivamente
para estabilizar os efeitos exibidos nos gráficos e nas tabelas de expressão
OSCA. Os testes de significância e os valores de `padj` continuam sendo os da
análise DESeq2 principal. Os métodos `apeglm` e `ashr` não estavam disponíveis
no ambiente R utilizado; por isso, os efeitos shrinkados devem ser tratados
como suporte visual, não como uma nova análise inferencial.
