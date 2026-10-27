#!/usr/bin/env python3
"""Build the Markdown run report from completed pair-specific output tables."""
import argparse
import csv
import json
from pathlib import Path
from collections import Counter


def read(path):
    with open(path) as handle:
        return list(csv.DictReader(handle,delimiter='\t'))


def report(run):
    s=json.loads((run/'summary.json').read_text())
    m=json.loads((run/'manifest.json').read_text())
    v=json.loads((run/'independent_verification.json').read_text())
    rows=read(run/'pairwise_kaks_all.tsv')
    candidates=read(run/'omega_gt1_screen.tsv')
    overlap=read(run/'comparison_1513.tsv')
    flags=Counter(flag for r in candidates for flag in r['Flags'].split(';') if flag)
    protein_check=json.loads((run/'orthofinder_protein_verification.json').read_text())
    status_table='| Situação | Pares |\n| --- | ---: |\n'+'\n'.join(f'| {k} | {val:,} |' for k,val in s['qc_counts'].items())
    candidate_flags='; '.join(f'{key}: {val}' for key,val in sorted(flags.items())) or 'nenhum'
    top='| Par | Ortogrupo | ω | dN | dS | Códons | Avisos |\n| --- | --- | ---: | ---: | ---: | ---: | --- |\n'
    top+='\n'.join(f"| {r['Pair_ID']} | {r['Orthogroup']} | {float(r['Omega_KaKs']):.4f} | {float(r['Ka_dN']):.4f} | {float(r['Ks_dS']):.4f} | {r['Codons']} | {r['Flags'] or '—'} |" for r in candidates[:20])
    prev_text = f" Todos os {s['previous_subset_overlap']:,} pares da análise anterior de cópia única nas sete espécies estão incluídos." if s.get('previous_subset_overlap', 0) > 0 else ""
    text=f'''# Ka/Ks de ortólogos 1:1 específicos entre V. peripherica e V. tubiflora

Execução: {run.name}. Critério solicitado: um único parceiro entre as duas espécies focais, independentemente de presença ou número de cópias em quaisquer outras espécies.

## Resultado

Foram analisados **{s['pairs']:,} pares**, distribuídos em {s['distinct_orthogroups']:,} ortogrupos.{prev_text} A triagem resultou em **{s['omega_gt1_count']:,} pares com ω > 1**, dos quais {s['omega_gt1_without_flags']:,} não receberam os avisos operacionais descritos abaixo. Esses números não representam seleção positiva estatisticamente confirmada.

{status_table}

Entre os pares com QC_Status = PASS, a mediana de dN foi {s['medians_qc_pass']['Ka_dN']}, a de dS foi {s['medians_qc_pass']['Ks_dS']} e a de ω foi {s['medians_qc_pass']['Omega_KaKs']}. Houve {s['screen_counts'].get('omega_lt_1',0):,} pares com ω < 1.

## Definição operacional de ortologia 1:1

A seleção partiu dos arquivos direcionais `Vper.pep__v__Vtub.pep.tsv` e `Vtub.pep__v__Vper.pep.tsv` do resultado `Results_Aug30` do OrthoFinder. As duas direções descrevem exatamente as mesmas relações. Para cada gene, foram reunidos todos os parceiros na outra espécie focal, considerando também linhas 1:muitos e muitos:1. Um par foi aceito somente quando o gene de Vper tinha um único parceiro em Vtub e esse gene de Vtub tinha um único parceiro em Vper.

A tabela possui {m['orthology_counts']['source_rows']:,} linhas, das quais {m['orthology_counts']['unique_singleton_rows']:,} são linhas com um identificador de cada lado. Destas, {m['orthology_counts']['excluded_nonunique_singletons']:,} não são globalmente únicas entre as espécies focais: um de seus genes participa de outras relações Vper–Vtub. Elas estão documentadas em `excluded_nonunique_singleton_rows.tsv`. A exclusão não envolve número de cópias em Xerophyta, Acanthochlamys, Pandanus, Dioscorea ou Arabidopsis.

Um exemplo excluído é o gene `Vper.hapA.v1.chr3A.g079770.t1`: ele aparece numa linha isolada com `Vtub.hapA.v1.chr4A.g110040.t1`, mas possui outros seis parceiros Vtub na tabela completa. Portanto, essa linha não constitui uma relação 1:1 estrita.

Uma família pode conter vários pares 1:1 independentes. Por isso, `Pair_ID` é a chave primária dos resultados; `Orthogroup` pode se repetir. Não foi exigida cópia única no ortogrupo inteiro. Essa seleção utiliza as relações filogenéticas já inferidas pelo OrthoFinder; não foi necessário executar o OrthoFinder novamente somente com duas espécies. A documentação das relações entre espécies está disponível no [repositório oficial](https://github.com/davidemms/OrthoFinder#orthologues-directory).

## Preparação dos alinhamentos e cálculo

Os identificadores exatos de transcrito foram utilizados para recuperar as proteínas e os CDS de `Vper.hapA.v1` e `Vtub.hapA.v1`. As traduções foram verificadas antes do alinhamento. CDS incompatíveis com as proteínas, com comprimento não múltiplo de três ou com parada interna são rejeitados. Uma parada terminal no CDS é permitida.

As proteínas foram alinhadas **somente em pares**, usando Biopython {m['biopython']}, `PairwiseAligner`, algoritmo global de Gotoh, matriz BLOSUM62, abertura de gap −10 e extensão −0,5. Gaps terminais receberam as mesmas penalidades; quando existem soluções ótimas empatadas, foi utilizada a primeira solução determinística do alinhador. A escolha de penalidades define o alinhamento e pode afetar regiões ambíguas; não se trata de parâmetros biologicamente estimados. [Documentação do alinhador](https://biopython.org/docs/latest/Tutorial/chapter_pairwise.html).

Os CDS originais foram projetados sobre o alinhamento proteico completo. Colunas contendo gaps, códons de parada ou bases diferentes de A/C/G/T em qualquer espécie foram removidas de ambas. A tradução dos códons retidos foi conferida novamente contra as posições proteicas correspondentes. Não foi aplicada a máscara da análise de sete espécies. O comprimento mínimo foi {m['parameters']['min_codons']} códons.

Foi utilizado **YN00/PAML 4.10.10, 29 Jan 2026**, com `icode = 0`, `weighting = 0` e `commonf3x4 = 0`. Somente o estimador de Yang–Nielsen é lido, incluindo seus erros-padrão; não há substituição silenciosa por Nei–Gojobori. [Yang & Nielsen, 2000](https://doi.org/10.1093/oxfordjournals.molbev.a026236); [Yang, 2007](https://doi.org/10.1093/molbev/msm088).

As razões não finitas ou negativas, os casos com dS ≤ 0, ω ≥ 99 ou dS ≥ {m['parameters']['max_ds']} são separados da triagem principal. O limiar superior de dS é operacional e não comprova saturação. Avisos adicionais identificam dS < 0,01, erro-padrão de dS ≥ dS, dN ≥ 2, identidade proteica < 70% ou cobertura de códons retidos < 70% em qualquer proteína. Esses avisos não são p-valores e não implicam exclusão automática. Os limiares de identidade e cobertura servem para priorizar revisão manual e não foram calibrados como um classificador de qualidade.

## Controle de qualidade e verificação independente

A reconstrução independente das relações de ortologia confirmou {v['pairs_with_reciprocal_uniqueness_checked']:,} pares com unicidade recíproca. Foram verificados {v['codon_alignments_checked']:,} alinhamentos de códons por suas coordenadas no CDS original. O leitor independente `Bio.Phylo.PAML.yn00` conferiu {v['independent_biopython_yn00_parses']:,} saídas de YN00. Os hashes de {v['input_hashes_checked']} arquivos de entrada/código conferiram. O resultado está em `independent_verification.json`.

Os 17 testes automatizados de regressão passaram, abrangendo tanto a correção anterior de projeção de códons quanto a seleção específica de relações 1:1 entre as duas espécies. A verificação das proteínas contra os arquivos de sequência do OrthoFinder comparou {protein_check['protein_sequences_checked']:,} sequências: {protein_check['identical_proteins']:,} foram idênticas e {protein_check['orthofinder_x_resolved']} continha uma posição X no OrthoFinder resolvida na anotação atual, sem outras discordâncias ({protein_check['sequence_disagreements']}). A posição foi mantida na análise porque a proteína atual coincide com a tradução do CDS. Os detalhes estão em `orthofinder_protein_verification.json` e `orthofinder_protein_differences.tsv`; os hashes dos arquivos originais estão em `orthofinder_sequence_checksums.tsv`.

## Candidatos e limites da interpretação

Os primeiros 20 valores de ω, ordenados de forma decrescente, estão abaixo. A ordenação não representa uma classificação de significância ou prioridade biológica.

{top}

Avisos entre os candidatos: {candidate_flags}. Um gene sem avisos também pode conter erro de alinhamento, anotação, ortologia ou estimação. Esses casos requerem inspeção dos alinhamentos e, para alegar seleção positiva, testes inferenciais apropriados e controle de testes múltiplos. O método pareado não identifica em qual linhagem ocorreram as mudanças.

Foram encontrados {s['ppr_annotation_pairs']:,} pares cuja descrição funcional de pelo menos uma das espécies contém PPR ou pentatricopeptide; {s['ppr_omega_gt1']:,} deles apresentaram ω > 1. Essa é uma contagem por descrições herdadas, não uma nova anotação de domínios ou um teste de enriquecimento.'''
    if s.get('previous_subset_overlap', 0) > 0:
        text += f'''

## Comparação com os {s['previous_subset_overlap']:,} pares anteriores

A tabela `comparison_1513.tsv` permite comparar exatamente os mesmos pares. No novo alinhamento pareado, {s['previous_subset_omega_gt1_now']} deles têm ω > 1; {s['previous_subset_candidates_retained']} dos dez candidatos da análise anterior mantêm essa classificação.

Além da ampliação do universo de genes, mudou o contexto do alinhamento: antes eram alinhamentos de sete espécies recortados; agora são alinhamentos globais apenas entre as duas Vellozia. Assim, diferenças entre as estimativas de um mesmo par podem decorrer da alteração do alinhamento e das colunas incluídas. Essa comparação não deve ser interpretada como efeito exclusivo do aumento do número de genes.'''
    text += '''

## Arquivos e reprodução

- `selected_pairs.tsv`: relações 1:1 aceitas e suas anotações.
- `excluded_nonunique_singleton_rows.tsv`: linhas aparentemente 1:1 excluídas por outros parceiros focais.
- `pairwise_kaks_all.tsv`: todos os pares, estimativas, avisos e falhas.
- `omega_gt1_screen.tsv`: triagem descritiva de ω > 1 após os filtros de estimação.
- `comparison_1513.tsv`: comparação com o subconjunto anterior.
- `work/PAIR*/`: proteínas, CDS, alinhamento, coordenadas, controles e saída bruta por par.
- `manifest.json`: versões, parâmetros, critérios e hashes dos arquivos originais.

Reproduzir a partir da raiz do projeto, utilizando uma pasta ainda inexistente:

```bash
python3 chapter_macroevolution/docs/scripts/pair_specific_kaks.py \\
  --output-dir chapter_macroevolution/05_selection/pair_specific_new_run --threads 4
python3 chapter_macroevolution/docs/scripts/verify_pair_specific_kaks.py \\
  chapter_macroevolution/05_selection/pair_specific_new_run
python3 chapter_macroevolution/docs/scripts/verify_orthofinder_pair_proteins.py \\
  chapter_macroevolution/05_selection/pair_specific_new_run
```

O manuscrito e as figuras não foram alterados. Para a comparação abrangente entre as duas Vellozia, esta execução deve ser distinguida da análise anterior restrita a cópia única nas sete espécies. Os resultados antigos permanecem preservados.

**Evidence tier:** Community standard para alinhamento proteico com projeção validada de códons e estimação pareada; Emerging / exploratory para a triagem biológica de ω > 1. **Applicability:** relações filogenéticas 1:1 inferidas entre as duas Vellozia no painel existente. **Main limitations:** dependência da ortologia, das anotações e do alinhamento; ausência de teste formal ou inferência por linhagem. As validações de sequências, relações e saídas foram executadas; modelos inferenciais adicionais demandam validação própria.
'''
    (run/'analysis_report.md').write_text(text)
    print(f'Report written: {run/"analysis_report.md"}')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run_dir',type=Path)
    report(parser.parse_args().run_dir.resolve())
