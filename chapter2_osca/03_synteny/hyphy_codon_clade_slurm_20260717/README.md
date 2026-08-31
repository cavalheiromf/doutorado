# HyPhy por clados com alinhamentos codônicos filtrados

Rodada SLURM `799356`, concluída sem erros em 17 de julho de 2026.

## Configuração

- HyPhy 2.5.99(MP)
- Alinhamentos codônicos `gap20` da validação de 2026-07-16
- Quatro conjuntos: família completa, OSCA1, OSCA2 e OSCA3+4
- *V. peripherica* como `Reference` e *V. tubiflora* como `Test`
- RELAX com MG94×REV, três classes de ômega e um ponto inicial
- Contrast-FEL com modelo global MG94×REV

## Síntese

RELAX detectou relaxamento significativo na família completa (`K = 0,7064`,
`p = 0,000337`) e em OSCA3+4 (`K = 0,2404`, `p = 0,003866`). OSCA1 (`K =
0,9262`, `p = 0,6081`) e OSCA2 (`K = 0,8191`, `p = 0,3446`) não apresentaram
evidência significativa.

O Contrast-FEL identificou 11, 6, 11 e 1 sítios nominais (`p <= 0,05`) em
global, OSCA1, OSCA2 e OSCA3+4, respectivamente. Nenhum sítio passou a
correção FDR (`q <= 0,20`). Portanto, os sítios nominais permanecem
exploratórios e não sustentam seleção divergente confirmada.

Os resultados são complementares aos Ka/Ks pareados: RELAX/Contrast-FEL
avaliam heterogeneidade entre ramos e sítios dentro de clados, enquanto os
Ka/Ks resumem divergência média de cada par.
