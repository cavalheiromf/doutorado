# Auditoria dos resultados Ka/Ks

## Escopo

Foram auditados `analyses/04_evolutionary_rates/results/aggregated_kaks.csv`, os
15 arquivos `results.ks` por par e o script
`analyses/04_evolutionary_rates/scripts/run_kaks.py`.

## Resultado da auditoria

- 15 comparações foram recuperadas: 14 interespecíficas e 1 paralógica
  (`VpOSCA2.4a/VpOSCA2.4b`).
- Todos os arquivos por par têm dois CDS, dois peptídeos e alinhamentos
  proteicos com comprimento consistente entre as sequências.
- Todos os CDS terminam em códon de parada e não apresentam parada interna nos
  peptídeos. A diferença de um aminoácido entre `len(CDS)/3` e o comprimento
  proteico é explicada pelo códon de parada terminal, que não é traduzido no
  FASTA de proteína.
- Não foram encontrados valores ausentes/não finitos, Ks <= 0 ou razões Ka/Ks
  acima de 1.
- Para os 14 ortólogos, a média é 0,3920 e a mediana 0,3375; o intervalo é
  0,0536–0,8016. O par paralógico tem Ka/Ks = 0,3771 e foi mantido separado.

## Valores extremos

| Par | Ka | Ks | Ka/Ks | Situação |
| --- | ---: | ---: | ---: | --- |
| VpOSCA2.3/VtOSCA2.3 | 0,0046 | 0,0859 | 0,0536 | menor entre ortólogos |
| VpOSCA4.1/VtOSCA4.1 | 0,0124 | 0,0775 | 0,1600 | baixo |
| VpOSCA1.4/VtOSCA1.4 | 0,0877 | 0,1094 | 0,8016 | maior entre ortólogos; requer rechecagem |
| VpOSCA2.4a/VpOSCA2.4b | 0,0442 | 0,1172 | 0,3771 | parálogos; não misturar à média interespecífica |

## Reestimativa codônica

O rerun foi concluído para os 15 pares com PAL2NAL v14 (`-nogap -nomismatch`)
seguido de YN00 do PAML 4.10.10. Os alinhamentos codônicos e os relatórios
individuais estão em `analyses/04_evolutionary_rates/results_pal2nal_yn00/`.
Para os 14 ortólogos, a nova média é 0,4082 e a mediana 0,3368, com intervalo
0,0530–0,8015. O valor de OSCA1.4 permaneceu estável (0,8016 → 0,8015), assim
como OSCA2.3 (0,0536 → 0,0530) e OSCA4.1 (0,1600 → 0,1601). As maiores
diferenças ocorreram em OSCA1.2 (0,3527 → 0,4211) e OSCA2.2 (0,5481 → 0,6947),
por isso a síntese do documento principal passa a usar a reestimativa codônica.

## Sensibilidade com codeml

O `codeml` do PAML 4.10.10 foi executado em modo pareado (`runmode = -2`,
`model = 0`, `NSsites = 0`, `CodonFreq = 2`) sobre os mesmos alinhamentos
codônicos. Para os 14 ortólogos, a média foi 0,3752, a mediana 0,3124 e o
intervalo 0,0518–0,7172. O par VpOSCA1.4/VtOSCA1.4 continuou sendo o maior
valor (Ka/Ks = 0,7172), mas permaneceu abaixo de 1. A conclusão qualitativa é
robusta ao método: predominam razões compatíveis com restrição purificadora,
sem evidência global de seleção positiva.

## Limitação metodológica remanescente

O resultado PAL2NAL + YN00 é agora a confirmação independente baseada em
alinhamento codônico explícito. A razão global continua sendo uma média entre
sítios e linhagens e não testa seleção localizada; essa interpretação continua
dependendo das análises HyPhy já revalidadas.

Assim, os resultados atuais sustentam uma leitura descritiva de predominância de
razões abaixo de 1, mas não evidenciam seleção positiva em nenhum par. A
interpretação de seleção localizada deve continuar baseada nas análises HyPhy
já revalidadas.

## Proveniência

- JCVI: 1.6.5 (`jcviEnv`)
- Script: `analyses/04_evolutionary_rates/scripts/run_kaks.py`
- Tabela agregada: `analyses/04_evolutionary_rates/results/aggregated_kaks.csv`
- Rerun codônico: `analyses/04_evolutionary_rates/results_pal2nal_yn00/aggregated_kaks_pal2nal_yn00.csv`
- Script do rerun: `analyses/04_evolutionary_rates/scripts/rerun_pal2nal_yn00.py`
- Sensibilidade codeml: `analyses/04_evolutionary_rates/results_codeml_pairwise/aggregated_kaks_codeml_pairwise.csv`
- Script codeml: `analyses/04_evolutionary_rates/scripts/rerun_codeml_pairwise.py`
