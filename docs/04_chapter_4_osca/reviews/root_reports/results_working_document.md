# Resultados integrados da família OSCA em *Vellozia*

> Documento bilíngue de trabalho. Cada seção separa as evidências diretamente
> observadas, sua interpretação e um texto científico em inglês. As hipóteses
> funcionais permanecem identificadas como interpretações até que sejam
> sustentadas por análises independentes.

## Organização do documento

1. Identificação dos genes OSCA
2. Relações filogenéticas
3. Sintenia e evolução da família gênica
4. Taxas evolutivas
5. Elementos regulatórios em promotores
6. Expressão gênica
7. Redes de associação funcional entre proteínas
8. Comparações estruturais
9. Síntese integrada

As seções ainda não revisadas serão acrescentadas progressivamente a partir dos
arquivos de resultados correspondentes. A síntese integrada será redigida por
último, evitando que uma interpretação preliminar determine a leitura das
análises subsequentes.

## 1. Identificação dos genes OSCA

### 1.1 Evidências observadas

A busca nos proteomas preditos dos haplótipos hapA de *Vellozia peripherica* e
*Vellozia tubiflora* foi realizada com o HMMER v3.4, utilizando o perfil
PF02714.21 (`RSN1_7TM`). A análise recuperou 14 proteínas candidatas em *V.
peripherica* e 13 em *V. tubiflora*. Os alinhamentos ao perfil apresentaram
E-values entre 3,7 × 10⁻⁸⁷ e 4,3 × 10⁻²⁶ em *V. peripherica* e entre 3,1 ×
10⁻⁸⁷ e 1,3 × 10⁻²⁵ em *V. tubiflora*.

A anotação posterior com o InterProScan forneceu evidências independentes para
a classificação das 27 proteínas. Todas foram associadas à família PANTHER
PTHR13018 e apresentaram regiões transmembrana preditas. A análise dos domínios
Pfam detectou PF02714 e PF14703 em todas as proteínas. O domínio N-terminal
PF13967 foi detectado em 13 das 14 proteínas de *V. peripherica* e em 12 das 13
proteínas de *V. tubiflora*. As exceções foram VpOSCA2.2 e VtOSCA1.2,
respectivamente.

| Espécie | Proteínas candidatas | PF02714 | PF14703 | PF13967 |
| --- | ---: | ---: | ---: | ---: |
| *V. peripherica* | 14 | 14/14 | 14/14 | 13/14 |
| *V. tubiflora* | 13 | 13/13 | 13/13 | 12/13 |

O conjunto final contém uma proteína adicional em *V. peripherica*. Essa
diferença descritiva é consistente com a presença de duas sequências candidatas
posteriormente nomeadas VpOSCA2.4a e VpOSCA2.4b, enquanto uma única sequência
foi nomeada VtOSCA2.4 em *V. tubiflora*. A origem evolutiva dessa diferença será
avaliada nas seções de filogenia e sintenia.

**Arquivos de origem:**

- `analyses/01_gene_identification/results/Vper.hapA.v1.softmasked.proteins.hmmout.txt`
- `analyses/01_gene_identification/results/Vtub.hapA.v1.softmasked.proteins.hmmout.txt`
- `analyses/01_gene_identification/results/interproscan_raw/`
- `analyses/01_gene_identification/results/oscasIDs.txt`
- `analyses/01_gene_identification/scripts/build_osca_domain_table.py`
- `analyses/01_gene_identification/scripts/Pipeline.ipynb`

### 1.2 Interpretação em português

Os resultados sustentam a identificação de um conjunto de 27 candidatos OSCA
nos dois proteomas avaliados. Essa classificação não depende apenas da
similaridade com o perfil usado na busca inicial: ela também é apoiada pela
anotação da família PANTHER, pela arquitetura de domínios Pfam e pela presença
de regiões transmembrana preditas. A concordância entre essas evidências reduz a
probabilidade de que os candidatos representem correspondências espúrias ao
perfil PF02714.

A ausência de PF13967 nas anotações de VpOSCA2.2 e VtOSCA1.2 deve ser
interpretada com cautela. Ela pode refletir divergência da sequência, cobertura
insuficiente do modelo de domínio ou problemas na predição do modelo proteico,
sem necessariamente indicar perda funcional da região N-terminal. A inspeção
dos alinhamentos e das anotações gênicas será necessária antes de atribuir
significado biológico a essa diferença.

Embora *V. peripherica* apresente um candidato a mais do que *V. tubiflora*, a
contagem isolada não demonstra expansão específica de linhagem, duplicação
recente ou perda gênica. Essas hipóteses dependem do posicionamento filogenético
das sequências e da conservação de seu contexto genômico.

### 1.3 Draft in English

HMMER v3.4 searches of the predicted hapA proteomes using the PF02714.21
(`RSN1_7TM`) profile identified 14 candidate OSCA proteins in *Vellozia
peripherica* and 13 in *Vellozia tubiflora*. Full-sequence E-values ranged from
3.7 × 10⁻⁸⁷ to 4.3 × 10⁻²⁶ in *V. peripherica* and from 3.1 × 10⁻⁸⁷ to 1.3 ×
10⁻²⁵ in *V. tubiflora*. Subsequent InterProScan annotation provided additional
support for the classification of all 27 candidates. Each protein was assigned
to the PANTHER PTHR13018 family and contained predicted transmembrane regions.
Pfam annotation detected the PF02714 and PF14703 domains in every candidate,
whereas PF13967 was detected in 13 of the 14 *V. peripherica* proteins and 12 of
the 13 *V. tubiflora* proteins.

The final candidate set therefore contained one additional OSCA sequence in
*V. peripherica*. This difference was associated with two sequences subsequently
designated VpOSCA2.4a and VpOSCA2.4b, compared with a single VtOSCA2.4 sequence
in *V. tubiflora*. However, gene counts alone do not establish whether this
pattern resulted from lineage-specific duplication or differential gene loss;
these alternatives require support from phylogenetic and syntenic evidence.

### 1.4 Limitações e validações pendentes

A busca inicial foi conduzida com um único perfil HMM, PF02714.21. Os domínios
PF13967 e PF14703 foram utilizados como evidência de anotação posterior, e não
como perfis independentes na etapa de busca. Uma versão final dos resultados
deverá registrar essa distinção metodológica e confirmar a sensibilidade da
busca para proteínas divergentes ou modelos gênicos parciais.

Uma versão anterior de `Vper.osca.tsv` continha inconsistências de nomenclatura
nas linhas derivadas de `g023020` e `g023030`, incluindo uma ocorrência de
PF14703 registrada como `VpOSCA2.4`, sem sufixo. A tabela foi regenerada a
partir dos resultados brutos do InterProScan e do mapeamento canônico de
`oscasIDs.txt`. O conjunto corrigido contém 14 identificadores únicos:
`Vper.hapA.v1.chr1A.g023030.t1` corresponde a `VpOSCA2.4a` e
`Vper.hapA.v1.chr1A.g023020.t1` corresponde a `VpOSCA2.4b`. Os dois alinhamentos
de PF14703 nas posições 189–238 e 239–281 pertencem a `VpOSCA2.4a`, enquanto o
alinhamento 239–281 da outra cópia pertence a `VpOSCA2.4b`.

Também será necessário documentar a versão do InterProScan e das bases de dados
utilizadas e verificar a completude dos modelos proteicos. A nomenclatura
canônica já foi propagada à árvore filogenética e aos derivados de promotores.

### 1.5 Conexões a avaliar posteriormente

A filogenia foi compatível com a classificação dos 27 candidatos nos quatro
grupos OSCA, mas não resolveu com suporte a história do grupo OSCA2.4. A análise
de sintenia deverá distinguir entre duplicação em *V. peripherica*, perda em *V.
tubiflora* e incerteza filogenética. A arquitetura de domínios de VpOSCA2.2 e
VtOSCA1.2 também deverá ser comparada aos respectivos ortólogos e às estruturas
preditas antes de ser interpretada funcionalmente.

## 2. Relações filogenéticas

### 2.1 Evidências observadas

A reconstrução filogenética incluiu 76 sequências proteicas OSCA: 14 de
*Vellozia peripherica*, 13 de *Vellozia tubiflora*, 15 de *Arabidopsis
thaliana*, 11 de *Oryza sativa*, 11 de *Sorghum bicolor* e 12 de *Zea mays*.
As sequências completas foram alinhadas com o MAFFT v7.526, utilizando a opção
`--auto`. O alinhamento resultante apresentou 1.697 posições, das quais 857
foram informativas por parcimônia.

A árvore de máxima verossimilhança foi estimada com o IQ-TREE v3.0.1. O
ModelFinder selecionou Q.PLANT+R5 como o modelo de substituição com melhor ajuste
segundo o critério de informação bayesiano. A topologia obtida distribuiu os 27
candidatos de *Vellozia* entre os quatro grupos nomeados OSCA1–OSCA4. O grupo
OSCA2 reuniu o maior número de sequências nas duas espécies, com seis proteínas
em *V. peripherica* e cinco em *V. tubiflora*.

| Grupo | *V. peripherica* | *V. tubiflora* | Total |
| --- | ---: | ---: | ---: |
| OSCA1 | 5 | 5 | 10 |
| OSCA2 | 6 | 5 | 11 |
| OSCA3 | 2 | 2 | 4 |
| OSCA4 | 1 | 1 | 2 |

Cada uma das 13 proteínas de *V. tubiflora* formou um par-irmão com a proteína
de *V. peripherica* que recebeu a mesma designação. Isso incluiu OSCA1.1–OSCA1.5,
OSCA2.1–OSCA2.3, OSCA2.5, OSCA3.1, OSCA3.2 e OSCA4.1. No grupo OSCA2.4, a
sequência VtOSCA2.4 formou um par com
`Vper.hapA.v1.chr1A.g023020.t1`, correspondente a VpOSCA2.4b. A sequência
`Vper.hapA.v1.chr1A.g023030.t1`, correspondente a VpOSCA2.4a, apareceu como
irmã desse par.

| Identificador genômico | Nome adotado | Posição na topologia estimada |
| --- | --- | --- |
| `Vper.hapA.v1.chr1A.g023020.t1` | VpOSCA2.4b | Irmã de VtOSCA2.4 |
| `Vper.hapA.v1.chr1A.g023030.t1` | VpOSCA2.4a | Irmã do par VpOSCA2.4b/VtOSCA2.4 |

**Arquivos de origem:**

- `analyses/02_phylogeny/results/allOSCAs.aligned.fasta`
- `analyses/02_phylogeny/results/iqtree.log`
- `analyses/02_phylogeny/results/iqtree.iqtree`
- `analyses/02_phylogeny/results/iqtree.treefile`
- `analyses/02_phylogeny/results/iqtree.renamed.treefile`
- `analyses/01_gene_identification/results/oscasIDs.txt`
- `analyses/02_phylogeny/scripts/rename_tree_tips.py`
- `analyses/01_gene_identification/scripts/Pipeline.ipynb`

### 2.2 Interpretação em português

A associação das sequências de *Vellozia* com homólogos nomeados dos grupos
OSCA1–OSCA4 é compatível com a classificação proposta para os candidatos. A
recuperação de 13 pares contendo uma sequência de cada espécie também sustenta,
como hipótese de trabalho, as relações de ortologia utilizadas nas comparações
de taxas evolutivas. Entretanto, essas relações não devem ser consideradas
confirmadas enquanto os nós correspondentes não forem avaliados por medidas de
suporte filogenético.

A topologia do grupo OSCA2.4 requer atenção particular. As duas cópias de *V.
peripherica* não foram recuperadas como irmãs entre si; VpOSCA2.4b apareceu mais
próxima de VtOSCA2.4 do que de VpOSCA2.4a. Portanto, a árvore atual não apresenta
o padrão mais simples esperado para uma duplicação posterior à separação das
duas espécies, que seria o agrupamento das duas cópias de *V. peripherica*. Se
essa topologia for recuperada com suporte adequado, ela poderá ser compatível
com uma duplicação mais antiga seguida de perda diferencial em *V. tubiflora*.
Alternativamente, o padrão pode refletir incerteza filogenética associada ao
alinhamento ou à ausência de avaliação do suporte dos ramos. A sintenia será
necessária para distinguir essas possibilidades.

### 2.3 Draft in English

Maximum-likelihood phylogenetic analysis was performed using 76 full-length OSCA
protein sequences, including 14 proteins from *Vellozia peripherica*, 13 from
*Vellozia tubiflora*, 15 from *Arabidopsis thaliana*, 11 from *Oryza sativa*,
11 from *Sorghum bicolor*, and 12 from *Zea mays*. The sequences were aligned
with MAFFT v7.526 using the `--auto` strategy, producing an alignment of 1,697
amino acid positions, including 857 parsimony-informative sites. IQ-TREE v3.0.1
selected Q.PLANT+R5 as the best-fitting substitution model according to the
Bayesian information criterion.

The inferred topology placed the 27 *Vellozia* proteins within the four named
OSCA groups. OSCA2 was the largest group, comprising six *V. peripherica* and
five *V. tubiflora* proteins. Each of the 13 *V. tubiflora* sequences formed a
sister pair with a correspondingly named *V. peripherica* sequence, supporting
their use as putative orthologs in subsequent comparative analyses. However,
this interpretation remains provisional because branch-support values were not
estimated in the retained IQ-TREE analysis.

Within the OSCA2.4 group, VtOSCA2.4 was recovered as sister to VpOSCA2.4b,
whereas VpOSCA2.4a was sister to this pair. Thus, the two *V. peripherica*
copies were not recovered as immediate sisters, as would be expected under the
simplest scenario of a lineage-specific duplication after species divergence.
If supported by resampling analyses, this topology may instead be consistent
with an older duplication followed by differential loss in *V. tubiflora*.
Nevertheless, alignment uncertainty and the absence of branch-support estimates
currently prevent discrimination between these alternatives, which should be
evaluated using independent syntenic evidence.

### 2.4 Limitações e validações pendentes

Uma reestimativa do IQ-TREE foi executada com `-m MFP`, 1.000 réplicas de
UFBoot (`-B 1000`) e 1.000 réplicas de SH-aLRT (`--alrt 1000`), usando o modelo
Q.PLANT+R6. Os arquivos de suporte foram preservados em
`analyses/02_phylogeny/results_support/`. A árvore consenso recuperou o par
VtOSCA2.4/VpOSCA2.4b com suporte UFBoot de 83% (SH-aLRT 33,2%) e o agrupamento
de VpOSCA2.4a com esse conjunto com suporte UFBoot de 100% (SH-aLRT 100%).
Portanto, a correspondência entre VtOSCA2.4 e VpOSCA2.4b é apoiada
moderadamente, enquanto a definição do agrupamento OSCA2.4 mais amplo é forte.
Os rótulos `Reference/Test` foram transferidos para a árvore suportada em
`iqtree_support_labeled.treefile`.

Embora a árvore seja exibida com ZmOSCA1.2 na raiz, o próprio relatório do
IQ-TREE informa que a topologia é não enraizada. Portanto, sua representação
gráfica não permite inferir diretamente a direção temporal dos eventos de
duplicação e perda.

O IQ-TREE também indicou que 74 das 76 sequências apresentaram mais de 50% de
lacunas ou caracteres ambíguos no alinhamento, cuja proporção total foi de
57,04%. Além disso, OsOSCA1.4, VtOSCA4.1 e VpOSCA4.1 falharam no teste de
homogeneidade de composição. Esses alertas não invalidam automaticamente a
análise, mas tornam necessária a inspeção visual do alinhamento, a avaliação de
regiões mal alinhadas e uma análise de sensibilidade com tratamento criterioso
das posições pouco confiáveis.

Uma versão anterior de `iqtree.renamed.treefile` apresentava as duas sequências
de *V. peripherica* como `VpOSCA2.4`, sem os sufixos `a` e `b`. O arquivo foi
regenerado a partir de `iqtree.treefile` e de `oscasIDs.txt`, preservando a
topologia e os comprimentos de ramo. A árvore atual identifica
`g023030.t1` como `VpOSCA2.4a` e `g023020.t1` como `VpOSCA2.4b`.

### 2.5 Conexões a avaliar posteriormente

A sintenia confirmou que VpOSCA2.4a e VpOSCA2.4b ocupam um arranjo adjacente e
correspondem à região que contém VtOSCA2.4, mas não distinguiu entre duplicação
em *V. peripherica* e perda ou ausência de anotação em *V. tubiflora*. Após a
reestimativa da árvore com suporte, essas informações poderão ser integradas
por reconciliação entre a árvore gênica e a árvore das espécies. Os pares usados
nas análises de Ka/Ks deverão então ser revistos, sobretudo as duas comparações
entre VtOSCA2.4 e as cópias de *V. peripherica*.

## 3. Sintenia e evolução da família gênica

### 3.1 Evidências observadas

A comparação intergenômica foi realizada a partir das anotações dos haplótipos
hapA de *Vellozia peripherica* e *Vellozia tubiflora*, utilizando o pipeline
MCscan implementado no JCVI e alinhamentos produzidos com o LAST. O ambiente
atualmente preservado contém JCVI v1.6.5 e LAST v1651. Foram recuperadas 21.309
âncoras gênicas, agrupadas em 297 blocos sintênicos.

O dot plot apresentou uma diagonal dominante ao longo dos nove pares de
cromossomos, e o maior bloco de cada cromossomo de *V. peripherica* correspondeu
ao cromossomo de mesmo número em *V. tubiflora*. Esse padrão sustenta ampla
conservação da organização cromossômica entre as espécies. Entretanto, também
foram observados blocos menores fora da diagonal, compatíveis com duplicações,
rearranjos locais ou correspondências repetitivas. Assim, os resultados mostram
macrossintenia predominante, mas não demonstram ausência de alterações
intercromossômicas.

Os genes OSCA estão distribuídos nos cromossomos 1A, 4A, 5A, 7A, 8A e 9A nas
duas espécies, sempre dentro das regiões macrossintênicas dos cromossomos
correspondentes. Fora dos agrupamentos repetidos OSCA1.3/1.4/1.5 e OSCA2.4,
nove pares com a mesma designação foram recuperados diretamente como âncoras
primárias. Na região OSCA2.4, VpOSCA2.4b foi a âncora primária de VtOSCA2.4,
enquanto VpOSCA2.4a foi recuperada como âncora adicional durante a etapa de
levantamento de correspondências próximas.

VpOSCA2.4b e VpOSCA2.4a ocupam posições consecutivas no cromossomo 1A de *V.
peripherica*, estão orientadas na mesma direção e são separadas por cerca de 1,3
kb, sem outro modelo gênico anotado entre elas. A região correspondente de *V.
tubiflora* contém apenas VtOSCA2.4. As duas cópias gênicas de *V. peripherica*
apresentaram correspondência com essa única cópia nos arquivos de âncoras, sendo
VpOSCA2.4b a correspondência primária.

Outro agrupamento conservado foi observado no cromossomo 7A. OSCA1.3, OSCA1.4 e
OSCA1.5 são genes consecutivos, sem modelos gênicos intermediários, e apresentam
a mesma ordem e orientação nas duas espécies. A janela local utilizada para a
figura contém 24 conexões de âncoras entre as regiões correspondentes. Como as
sequências desse trio são semelhantes entre si, a âncora primária não resolve
todos os pares nome a nome; as âncoras adicionais recuperam as três
correspondências propostas e também ligações cruzadas dentro do agrupamento.

A auto-sintenia identificou ainda as relações VpOSCA2.2/VpOSCA2.1 e
VpOSCA3.1/VpOSCA3.2 entre os cromossomos 1A e 5A. As relações equivalentes,
VtOSCA2.2/VtOSCA2.1 e VtOSCA3.1/VtOSCA3.2, foram recuperadas em *V. tubiflora*.

| Padrão | *V. peripherica* | *V. tubiflora* | Evidência estrutural |
| --- | --- | --- | --- |
| OSCA2.4 no chr1A | Duas cópias adjacentes | Uma cópia | VpOSCA2.4b é a âncora primária; VpOSCA2.4a é adicional |
| OSCA1.3/1.4/1.5 no chr7A | Três genes consecutivos | Três genes consecutivos | Mesma ordem e orientação; 24 conexões locais |
| Auto-sintenia chr1A–chr5A | OSCA2.2/2.1 e OSCA3.1/3.2 | OSCA2.2/2.1 e OSCA3.1/3.2 | Pares parálogos recuperados nos dois genomas |

**Arquivos de origem:**

- `analyses/03_synteny/intergenomic/intermediates/Vper.Vtub.anchors`
- `analyses/03_synteny/intergenomic/intermediates/Vper.Vtub.simple`
- `analyses/03_synteny/intergenomic/intermediates/Vper.Vtub.lifted.anchors`
- `analyses/03_synteny/microsynteny/osca_chr1A.blocks`
- `analyses/03_synteny/microsynteny/osca_cluster.blocks`
- `analyses/03_synteny/intragenomic/Vper/intermediates/Vper.Vper.anchors`
- `analyses/03_synteny/intragenomic/Vtub/intermediates/Vtub.Vtub.anchors`
- `analyses/03_synteny/data/Vper.bed`
- `analyses/03_synteny/data/Vtub.bed`
- `analyses/03_synteny/scripts/`
- `reports/figures/03_synteny/`

### 3.2 Interpretação em português

A conservação dos principais blocos cromossômicos e do contexto local dos genes
OSCA fornece uma linha de evidência independente para grande parte das relações
de ortologia propostas pela filogenia. Em particular, a correspondência entre
VpOSCA2.4b e VtOSCA2.4 é sustentada tanto pela árvore quanto pela âncora
sintênica primária.

A presença de duas cópias adjacentes de OSCA2.4 em *V. peripherica* e uma única
cópia na região correspondente de *V. tubiflora* demonstra uma diferença local
de número de cópias. Entretanto, esse padrão não determina por si só a direção
do evento evolutivo. Ele é compatível tanto com uma duplicação em tandem na
linhagem de *V. peripherica* quanto com uma duplicação anterior à especiação,
seguida de perda ou ausência de anotação da segunda cópia em *V. tubiflora*. A
segunda alternativa merece atenção porque a árvore atual agrupa VpOSCA2.4b com
VtOSCA2.4, deixando VpOSCA2.4a como irmã desse par, em vez de recuperar as duas
cópias de *V. peripherica* como irmãs imediatas.

A conservação do agrupamento OSCA1.3/1.4/1.5, com três genes consecutivos e na
mesma ordem, indica que essa organização já estava presente antes da separação
das espécies ou foi mantida de forma equivalente em ambas. O dado estrutural não
permite, isoladamente, atribuir seleção purificadora, coexpressão ou função
coordenada ao agrupamento; essas hipóteses devem ser avaliadas com as análises
de taxas evolutivas e expressão.

Por fim, a recuperação dos mesmos pares parálogos OSCA2 e OSCA3 em blocos de
auto-sintenia entre os cromossomos 1A e 5A é consistente com uma duplicação
segmental ancestral à divergência das espécies. Uma origem por duplicação do
genoma completo permanece possível, mas não é demonstrada pelos quatro pares
OSCA; essa hipótese exigiria evidência genômica mais ampla e distribuição de
idades dos blocos duplicados.

### 3.3 Draft in English

Comparative synteny analysis between the hapA genomes of *Vellozia peripherica*
and *Vellozia tubiflora* recovered 21,309 gene anchors grouped into 297 syntenic
blocks. The genome-wide dot plot showed a dominant diagonal across the nine
chromosome pairs, and the largest block associated with each *V. peripherica*
chromosome mapped to the correspondingly numbered *V. tubiflora* chromosome.
This pattern supports extensive conservation of chromosome-scale organization.
However, smaller off-diagonal blocks were also present, indicating that the
current analysis does not exclude local rearrangements, duplicated segments, or
repetitive matches.

All OSCA loci occurred within corresponding macrosyntenic regions on
chromosomes 1A, 4A, 5A, 7A, 8A, and 9A. A local copy-number difference was
observed at the OSCA2.4 locus. VpOSCA2.4b and VpOSCA2.4a are consecutive,
similarly oriented genes separated by approximately 1.3 kb on *V. peripherica*
chromosome 1A, whereas the corresponding *V. tubiflora* region contains a
single VtOSCA2.4 gene. Both *V. peripherica* copies were linked to VtOSCA2.4 in
the anchor files, although VpOSCA2.4b represented the primary syntenic anchor.

The OSCA1.3/1.4/1.5 cluster was also conserved on chromosome 7A. The three genes
were consecutive and retained the same order and orientation in both species,
while 24 anchor connections were recovered across the local windows. In
addition, self-synteny analysis identified OSCA2.2/OSCA2.1 and
OSCA3.1/OSCA3.2 paralogous relationships between chromosomes 1A and 5A in both
genomes. The recurrence of these relationships in the two species is consistent
with a segmental duplication predating their divergence, although the current
data are insufficient to attribute this pattern specifically to an ancestral
whole-genome duplication.

Together, the phylogenetic and syntenic evidence supports VpOSCA2.4b and
VtOSCA2.4 as the closest cross-species counterparts. Nevertheless, the origin
of VpOSCA2.4a remains unresolved. The local architecture is compatible with a
tandem duplication in *V. peripherica*, whereas the gene topology also permits
an older duplication followed by loss or failure to annotate the second copy in
*V. tubiflora*. Additional branch-support analyses, inspection of the
*V. tubiflora* genomic interval, and gene-tree/species-tree reconciliation are
required to distinguish these alternatives.

### 3.4 Limitações e validações pendentes

Os arquivos `Vper.Vtub.anchors`, `Vper.Vtub.lifted.anchors` e os BED utilizados
na análise estão presentes localmente, mas são ignorados pelo Git. Isso limita a
reprodutibilidade do resultado a partir de um clone limpo do repositório. Os
arquivos de entrada, parâmetros completos e metadados das versões deverão ser
preservados de forma rastreável ou descritos em um manifesto de proveniência.

O ambiente atualmente instalado contém JCVI v1.6.5 e LAST v1651, mas os
notebooks não registram explicitamente que essas eram as versões no momento da
execução. O README também identifica incorretamente as espécies como *Vanilla*
e como orquídeas; essa descrição não deve ser reutilizada em Material e Métodos.

Os pares marcados com `L` em `Vper.Vtub.lifted.anchors` são correspondências
adicionais levantadas a partir da proximidade dos blocos e não têm o mesmo papel
que as âncoras primárias. Essa distinção é especialmente importante nos
agrupamentos OSCA2.4 e OSCA1.3/1.4/1.5, nos quais a elevada similaridade entre
parálogos produz múltiplas correspondências plausíveis.

O arquivo `Vper.Vtub.orthologs_thin.simple` acrescenta miniblocos para fins de
visualização e pode completar pares ausentes com base na nomenclatura. Portanto,
as linhas vermelhas da figura correspondente não representam, por si mesmas,
uma inferência independente de ortologia.

A janela de microssintenia do cromossomo 1A reúne todos os loci OSCA desse
cromossomo e cobre aproximadamente 9,6 Mb, em vez de representar uma janela
individual de 31 genes para cada locus. Uma figura específica para OSCA2.4 deve
ser produzida antes da versão final. De modo semelhante, os PDFs intragenômicos
atuais mostram regiões selecionadas entre os cromossomos 1A e 2A, e não os
blocos OSCA entre 1A e 5A; estes últimos estão sustentados pelos arquivos de
âncoras, mas ainda precisam de visualização dedicada.

Os 297 blocos incluem segmentos menores fora da diagonal e correspondências em
contigs não posicionados. Uma conclusão formal sobre ausência de translocações
ou outros rearranjos exigiria uma análise específica de variantes estruturais,
além da inspeção do dot plot.

### 3.5 Conexões a avaliar posteriormente

A região de VtOSCA2.4 deverá ser inspecionada quanto a pseudogenes, lacunas de
montagem ou modelos gênicos não anotados. A hipótese de duplicação segmental
ancestral entre 1A e 5A deverá ser confrontada com a extensão dos blocos, a
distribuição de Ks entre parálogos e evidências de duplicação em outros grupos
gênicos. Finalmente, os agrupamentos OSCA2.4 e OSCA1.3/1.4/1.5 poderão ser
comparados aos perfis de expressão para avaliar se a proximidade física está
associada a padrões regulatórios compartilhados.

## 4. Taxas evolutivas

### 4.1 Evidências observadas

Foram obtidas estimativas pareadas das taxas de substituição não sinônima (Ka) e
sinônima (Ks) para 14 comparações interespecíficas entre genes OSCA de *Vellozia
peripherica* e *Vellozia tubiflora*. Treze comparações correspondem aos
pares-irmãos recuperados na árvore, enquanto o conjunto também inclui a
comparação adicional VpOSCA2.4a/VtOSCA2.4. Todas as razões Ka/Ks foram
inferiores a 1, variando de 0,0530 a 0,8015. Na reestimativa com alinhamento
codônico explícito (PAL2NAL + YN00), a média foi 0,4082 e a mediana, 0,3368.

O par VpOSCA2.3/VtOSCA2.3 apresentou a menor razão entre os ortólogos avaliados
(Ka = 0,0046; Ks = 0,0859; Ka/Ks = 0,0530). O par VpOSCA4.1/VtOSCA4.1 também
apresentou uma razão comparativamente baixa (Ka = 0,0124; Ks = 0,0775; Ka/Ks =
0,1601). Em contraste, VpOSCA1.4/VtOSCA1.4 exibiu o maior valor observado (Ka =
0,0877; Ks = 0,1094; Ka/Ks = 0,8015).

Além das comparações entre espécies, foi analisado separadamente o par de
parálogos VpOSCA2.4a/VpOSCA2.4b, cuja razão Ka/Ks foi 0,3770 (Ka = 0,0442; Ks =
0,1172). Essa comparação representa divergência após duplicação gênica e,
portanto, não deve ser agrupada com os pares que divergiram por especiação.

A auditoria dos 15 arquivos `results.ks` confirmou dois registros por par,
alinhamentos proteicos com comprimento consistente, CDS terminando em códon de
parada e ausência de valores ausentes, Ks não positivo ou razões acima de 1.
Essa verificação confirma a integridade técnica da tabela, mas não transforma a
razão global em teste de seleção positiva; o valor extremo de OSCA1.4 deverá ser
rechecado com alinhamento codônico explícito antes da interpretação final.

| Comparação | Ka | Ks | Ka/Ks | Leitura descritiva |
| --- | ---: | ---: | ---: | --- |
| VpOSCA2.3/VtOSCA2.3 | 0,0046 | 0,0859 | 0,0530 | Menor razão entre os ortólogos |
| VpOSCA4.1/VtOSCA4.1 | 0,0124 | 0,0775 | 0,1601 | Razão comparativamente baixa |
| VpOSCA1.4/VtOSCA1.4 | 0,0877 | 0,1094 | 0,8015 | Maior razão entre os ortólogos |
| VpOSCA2.4a/VpOSCA2.4b | 0,0442 | 0,1172 | 0,3770 | Comparação entre parálogos |

**Arquivos de origem:**

- `analyses/04_evolutionary_rates/results/aggregated_kaks.csv`
- `analyses/04_evolutionary_rates/results_pal2nal_yn00/aggregated_kaks_pal2nal_yn00.csv`
- `analyses/04_evolutionary_rates/scripts/rerun_pal2nal_yn00.py`
- `analyses/04_evolutionary_rates/results/*/results.ks`
- `analyses/04_evolutionary_rates/scripts/run_kaks.py`
- `analyses/03_synteny/hyphy_rerun_20260716/relax_summary.tsv`
- `analyses/03_synteny/hyphy_rerun_20260716/relax_robustness_summary.tsv`
- `analyses/03_synteny/hyphy_rerun_20260716/contrast_fel_summary.tsv`

### 4.2 Interpretação em português

O predomínio de razões Ka/Ks inferiores a 1 é compatível com seleção
purificadora atuando sobre as regiões codificantes dos genes OSCA. Nesse
contexto, o valor reduzido observado para OSCA2.3 sugere maior restrição relativa
à fixação de alterações de aminoácidos quando comparado aos demais pares
avaliados. O resultado de OSCA4.1 aponta na mesma direção, embora de forma menos
acentuada.

Por outro lado, a razão mais elevada de OSCA1.4 sugere restrição seletiva
comparativamente mais fraca ou maior divergência não sinônima entre as duas
espécies. Como o valor permanece abaixo de 1, esse resultado isolado não
constitui evidência de seleção positiva nem permite concluir que ocorreu
neofuncionalização. Essas possibilidades devem ser tratadas como hipóteses a
serem confrontadas com modelos filogenéticos de seleção, conservação de
domínios, localização das substituições e dados funcionais.

### 4.3 Draft in English

Pairwise estimates of nonsynonymous and synonymous substitution rates were
obtained for 14 interspecific OSCA comparisons between *Vellozia peripherica*
and *Vellozia tubiflora*. Thirteen comparisons corresponded to sister pairs in
the inferred topology, whereas the dataset also included the additional
VpOSCA2.4a/VtOSCA2.4 comparison. All Ka/Ks ratios were below 1, ranging from
0.0530 to 0.8015, with a mean of 0.4082 and a median of 0.3403 in the explicit
codon re-estimation. This overall
pattern is consistent with the predominance of purifying selection across OSCA
coding sequences. The VpOSCA2.3/VtOSCA2.3 pair showed the lowest Ka/Ks ratio
(Ka = 0.0046; Ks = 0.0859; Ka/Ks = 0.0530), indicating the strongest relative
evolutionary constraint among the evaluated interspecific comparisons. The
VpOSCA4.1/VtOSCA4.1 pair also exhibited a comparatively low ratio (Ka = 0.0124;
Ks = 0.0775; Ka/Ks = 0.1601), supporting substantial conservation of its
protein-coding sequence.

Conversely, VpOSCA1.4/VtOSCA1.4 displayed the highest ratio (Ka = 0.0877; Ks =
0.1094; Ka/Ks = 0.8015), suggesting weaker selective constraint or
comparatively accelerated nonsynonymous divergence. However, because this
estimate remains below 1, it does not constitute direct evidence of positive
selection. The paralogous pair VpOSCA2.4a/VpOSCA2.4b showed a Ka/Ks ratio of
0.3770 and was considered separately because it represents divergence following
gene duplication rather than speciation.

### 4.4 Limitações e validações dos modelos HyPhy

A razão Ka/Ks calculada para o gene completo representa uma média entre sítios e
linhagens. Por isso, ela pode ocultar seleção localizada em poucos códons ou em
ramos específicos.

Os valores pareados desta seção foram inicialmente calculados pelo
`jcvi.compara.ks calc` (JCVI 1.6.5), usando alinhamento proteico MUSCLE e as
estimativas YN/NG. A validação independente PAL2NAL + YN00 confirmou a ordem dos
valores extremos. Uma segunda análise com `codeml` pareado (PAML 4.10.10,
`runmode = -2`, M0) produziu média 0,3752, mediana 0,3124 e intervalo
0,0518–0,7172 para os 14 ortólogos; OSCA1.4 continuou sendo o maior par, sem
ultrapassar 1. A conclusão permanece descritiva: predominam razões Ka/Ks abaixo
de 1, sem evidência isolada de seleção positiva.

A afirmação de relaxamento significativo da seleção em OSCA2 não foi mantida.
A reexecução do HyPhy RELAX v2.5.99 produziu K = 0,8255 e p = 0,3188, e as
análises adicionais com 10 e 25 pontos iniciais também não foram significativas
(p = 0,3367 e p = 0,3130, respectivamente). Além disso, os logs registraram uma
superfície de verossimilhança plana. Portanto, o resultado anterior para OSCA2
não foi reproduzido e não sustenta relaxamento significativo.

Uma nova rodada independente foi executada com os alinhamentos codônicos
filtrados em `gap20` e os mesmos quatro clados. O RELAX reproduziu relaxamento
significativo na família completa (K = 0,7064; p = 0,000337) e em OSCA3+4 (K =
0,2404; p = 0,003866), mas não em OSCA1 (K = 0,9262; p = 0,6081) nem em OSCA2
(K = 0,8191; p = 0,3446). O Contrast-FEL encontrou 11, 6, 11 e 1 sítios
nominais nos quatro conjuntos, respectivamente; nenhum passou FDR <= 0,20.
Essa rodada confirma a interpretação conservadora: o sinal de relaxamento é
concentrado em OSCA3+4 e os sítios nominais não são evidência confirmada de
seleção divergente.

A auditoria dos quatro alinhamentos confirmou comprimentos divisíveis por três,
ausência de códons de parada internos, ausência de códons parcialmente
interrompidos por lacunas e correspondência integral entre as sequências e as
folhas das árvores. Não foram identificados clados internos formados
exclusivamente por uma das espécies. Dessa forma, não existem ramos internos
que possam ser classificados de maneira não ambígua como `Test` ou
`Reference`, e a rotulagem somente dos ramos terminais é compatível com as
topologias disponíveis. A inspeção do ambiente também mostrou que os
alinhamentos foram produzidos com MUSCLE v3.8.1551, e não MUSCLE v5 como
informado no README anterior.

Apesar da integridade da moldura de leitura, os alinhamentos apresentaram
regiões esparsas. O alinhamento global continha 1.058 dos 1.697 sítios com mais
de 20% de lacunas. Nos subclados, essa condição ocorreu em 268 dos 1.029 sítios
de OSCA1, 288 dos 889 sítios de OSCA2 e 233 dos 904 sítios de OSCA3/4. Entre os
35 sítios com p nominal menor ou igual a 0,05 no Contrast-FEL, oito continham
mais de 20% de lacunas. Esse conjunto incluiu os sítios 241 e 270 de OSCA2, com
63,6% e 54,5% de lacunas, respectivamente. Como nenhum sítio permaneceu
significativo após o controle de FDR, esses resultados devem ser tratados como
exploratórios.

Para avaliar a sensibilidade do RELAX, foram removidos, em análises separadas,
os códons com mais de 20% ou mais de 50% de lacunas. As oito análises foram
executadas com dez pontos iniciais e não produziram erros.

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
em OSCA3/4, enquanto OSCA1 e OSCA2 permaneceram não significativos. Assim, a
direção geral do resultado de OSCA3/4 é robusta à remoção de colunas esparsas,
e a ausência de evidência reprodutível em OSCA2 foi novamente confirmada.

O rastreamento com GARD selecionou cinco pontos de quebra em OSCA1, dois em
OSCA2 e dois em OSCA3/4. A comparação entre topologias por segmento e uma única
topologia produziu razões de evidência de 5,39 × 10⁶¹, 164,42 e 53,20,
respectivamente. Pelo limiar operacional de 100 utilizado pelo HyPhy Vision,
OSCA1 e OSCA2 apresentam suporte para incongruência topológica, enquanto
OSCA3/4 permanece abaixo desse limiar. Em OSCA1, o algoritmo atingiu o máximo
configurado de cinco pontos, e um dos limites ficou próximo de uma região com
90% de lacunas. Portanto, esses resultados demonstram heterogeneidade
filogenética, mas ainda não distinguem recombinação, conversão gênica, histórias
distintas entre domínios ou artefatos de alinhamento.

Nenhum limite selecionado pelo GARD de nucleotídeos coincidiu exatamente com
uma fronteira de códon. Antes da versão final, ainda será necessário confirmar
as partições com uma estratégia codon-aware ou com blocos biologicamente
justificados e repetir o alinhamento com um método independente. Se a
incongruência for mantida, as análises de seleção deverão ser repetidas por
bloco com árvores próprias, pois o RELAX pressupõe uma história filogenética
consistente.

**Arquivos de validação:**

- `analyses/03_synteny/hyphy_validation_20260716/README.md`
- `analyses/03_synteny/hyphy_validation_20260716/alignment_qc.tsv`
- `analyses/03_synteny/hyphy_validation_20260716/nominal_site_gap_audit.tsv`
- `analyses/03_synteny/hyphy_validation_20260716/gard/gard_summary.tsv`
- `analyses/03_synteny/hyphy_validation_20260716/relax_gap_sensitivity/relax_gap_sensitivity_summary.tsv`

### 4.5 Conexões a avaliar posteriormente

A interpretação final deverá considerar se os genes com razões Ka/Ks extremas
também apresentam diferenças consistentes de expressão, conservação de
microssintenia, conectividade em redes de interação ou alterações localizadas em
regiões estruturais relevantes. Essas associações não serão consideradas
evidência funcional enquanto não forem avaliadas diretamente nas respectivas
análises.

## 5. Elementos cis-regulatórios em regiões promotoras

### 5.1 Evidências observadas

Foram extraídas regiões de 2.000 pb a montante dos genes OSCA, considerando a
orientação de cada gene, para 14 loci de *Vellozia peripherica* e 13 loci de
*Vellozia tubiflora*. As 27 sequências recuperadas apresentaram o comprimento
esperado, totalizando 54.000 pb analisados. A busca por elementos
cis-regulatórios foi realizada no PlantCARE.

As saídas continham 2.175 ocorrências com nomes de motivos em *V. peripherica* e
2.021 em *V. tubiflora*, após a remoção de registros vazios e identificadores
`Unnamed`. Esses totais foram dominados por elementos associados ao promotor
basal, principalmente TATA-box e CAAT-box. Para a síntese descritiva abaixo,
foram excluídos CAAT-box e motivos contendo “TATA”, e foram harmonizadas apenas
variações de maiúsculas e minúsculas, como G-Box/G-box, MYB/Myb e MYC/Myc. Esse
procedimento reteve 672 ocorrências candidatas distribuídas entre os 14
promotores de *V. peripherica* e 653 entre os 13 promotores de *V. tubiflora*. A
mediana foi de 49 ocorrências por promotor em *V. peripherica* e 46 em *V.
tubiflora*, enquanto as médias foram, respectivamente, 48,0 e 50,2.

| Motivo ou grupo de motivos | *V. peripherica*: ocorrências; promotores | *V. tubiflora*: ocorrências; promotores |
| --- | ---: | ---: |
| Família ABRE (ABRE, ABRE3a e ABRE4) | 68; 13/14 | 71; 10/13 |
| ARE | 20; 11/14 | 19; 10/13 |
| MBS | 13; 10/14 | 13; 10/13 |
| LTR | 17; 8/14 | 13; 8/13 |
| G-box | 53; 13/14 | 60; 11/13 |
| Box 4 | 59; 14/14 | 38; 11/13 |
| STRE | 13; 9/14 | 16; 11/13 |
| CGTCA-motif e TGACG-motif | 36; 11/14 | 46; 12/13 |

Motivos nomeados como MYB ou Myb foram encontrados nos 14 promotores de *V.
peripherica* e nos 13 de *V. tubiflora*. Motivos MYC/Myc também ocorreram em
todos os promotores de *V. peripherica*, mas em 10 dos 13 promotores de *V.
tubiflora*. Em conjunto, os resultados mostram a presença recorrente de
elementos previamente associados a respostas hormonais, luminosas e a
estresses abióticos ou bióticos. A tabela representa ocorrência e prevalência,
e não enriquecimento ou atividade regulatória.

Foi identificada uma inconsistência específica no locus duplicado OSCA2.4 de
*V. peripherica*. Os dois intervalos promotores foram nomeados como
`VpOSCA2.4`, fazendo com que o resumo e o mapa de calor originais agregassem
duas sequências independentes em uma única linha de 4.000 pb. A correspondência
com os modelos gênicos indica que o intervalo BED
chr1A:22687052–22689052 pertence a `VpOSCA2.4a`, enquanto
chr1A:22676816–22678816 pertence a `VpOSCA2.4b`. Após a separação por
coordenadas, cada promotor apresentou 49 ocorrências candidatas. Apesar do
mesmo total, a composição foi diferente: `VpOSCA2.4a` apresentou duas
ocorrências de G-box, quatro de ARE e duas de STRE, enquanto `VpOSCA2.4b`
apresentou seis, uma e zero ocorrências, respectivamente. Essas diferenças são
descritivas e ainda não foram submetidas a um teste de enriquecimento.

**Arquivos de origem:**

- `analyses/04_promoters/results/Vper.promoters.2k.fasta`
- `analyses/04_promoters/results/Vtub.promoters.2k.fasta`
- `analyses/04_promoters/results/Vper_plantcare_cleaned.tsv`
- `analyses/04_promoters/results/Vtub_plantcare_cleaned.tsv`
- `analyses/04_promoters/scripts/extract_promoters.py`
- `analyses/04_promoters/scripts/parse_plantcare.py`
- `analyses/04_promoters/scripts/plot_heatmaps.py`

### 5.2 Interpretação em português

A recorrência de motivos associados a ABA, jasmonato, luz e diferentes classes
de estresse é compatível com uma arquitetura regulatória potencialmente capaz
de integrar múltiplos sinais ambientais nos genes OSCA. Essa leitura é
biologicamente plausível para uma família envolvida em percepção osmótica, mas
deve permanecer no nível de hipótese. A presença de um motivo curto em uma
sequência de 2 kb não demonstra ligação de um fator de transcrição, resposta a
um tratamento ou contribuição efetiva para a expressão do gene.

As prevalências semelhantes de ARE, MBS e LTR nas duas espécies sugerem um
componente regulatório compartilhado, ao passo que diferenças em ABRE, G-box,
Box 4, STRE e motivos responsivos a jasmonato definem candidatos para uma
comparação mais direcionada. Os totais brutos, entretanto, não sustentam uma
conclusão de maior complexidade regulatória em uma das espécies, pois *V.
peripherica* possui um promotor adicional e a frequência esperada de cada
motivo depende da composição das sequências.

A separação de `VpOSCA2.4a` e `VpOSCA2.4b` levanta uma hipótese específica de
divergência cis-regulatória após a duplicação em tandem. A diferença na
composição dos motivos, mesmo com totais iguais, pode orientar a busca por
respostas distintas entre os parálogos. A hipótese de subfuncionalização só
ganhará suporte se essas diferenças forem acompanhadas por perfis de expressão
divergentes e, idealmente, por evidências independentes de acessibilidade da
cromatina ou ligação de fatores de transcrição.

### 5.3 Draft in English

Strand-aware 2-kb upstream regions were extracted for 14 OSCA loci from
*Vellozia peripherica* and 13 from *Vellozia tubiflora*, yielding 27 promoter
sequences of the expected length. PlantCARE analysis identified 2,175 named
motif occurrences in *V. peripherica* and 2,021 in *V. tubiflora* after empty
and unnamed records were removed. Because these totals were dominated by
TATA- and CAAT-associated core promoter elements, the descriptive comparison
excluded CAAT-box and motifs containing “TATA” and harmonized case variants of
otherwise identical names. This retained 672 candidate occurrences across the
14 *V. peripherica* promoters and 653 across the 13 *V. tubiflora* promoters.
The median numbers of candidate occurrences per promoter were 49 and 46,
respectively.

Both species displayed a broad repertoire of putative cis-regulatory elements.
The ABRE family occurred in 13 of 14 *V. peripherica* promoters and 10 of 13
*V. tubiflora* promoters, whereas ARE and MBS elements were present in most
promoters from both species. Light-associated G-box and Box 4 elements were
also widespread, and CGTCA- and TGACG-motifs were detected in 11 of 14 *V.
peripherica* promoters and 12 of 13 *V. tubiflora* promoters. These patterns
define candidate promoter architectures associated with hormonal,
light-responsive, and stress-related regulation, but they do not demonstrate
motif enrichment or regulatory activity.

The two *V. peripherica* OSCA2.4 promoters had been assigned the same
`VpOSCA2.4` label in the original output, causing their motif counts to be
collapsed into a single heatmap row. Coordinate-based reassignment separated
`VpOSCA2.4a` and `VpOSCA2.4b`, each of which contained 49 candidate motif
occurrences. Their motif composition nevertheless differed, including two
versus six G-box occurrences and four versus one ARE occurrences,
respectively. This contrast provides a testable hypothesis of cis-regulatory
divergence following tandem duplication, which will require expression and
functional regulatory evidence.

### 5.4 Limitações e validações pendentes

As anotações do PlantCARE são predições baseadas em correspondência de
sequência. Motivos curtos e degenerados podem ocorrer ao acaso, se sobrepor ou
ser reportados sob nomes parcialmente redundantes. Não foi empregado um
conjunto de promotores de fundo, controle por conteúdo GC, permutação,
correção para múltiplos testes ou modelo de enriquecimento. Assim, diferenças
de contagem entre genes ou espécies não devem ser interpretadas como diferenças
de atividade regulatória.

A janela fixa de 2 kb ainda precisa ser confrontada com a distância ao gene
vizinho, possíveis sobreposições entre regiões regulatórias, conteúdo repetitivo
e conservação de sequência. Isso é particularmente importante nos agrupamentos
em tandem. A versão ou data de acesso do PlantCARE não foi registrada, e a
versão de BEDTools disponível atualmente é 2.31.1, mas não há confirmação da
versão utilizada na execução original.

Os arquivos BED e FASTA foram regenerados com identificadores separados para
`VpOSCA2.4a` e `VpOSCA2.4b`, sem alteração das coordenadas ou sequências. Os
resultados processados do PlantCARE foram recalculados com 14 linhas para
*V. peripherica*, e a duplicação de `MRE` entre categorias funcionais foi
removida do script de visualização. Os mapas de calor permanecem exploratórios
por causa das limitações do modelo de motivos e da ausência de um teste de
enriquecimento, não por ambiguidade de nomenclatura.

### 5.5 Conexões a avaliar posteriormente

Os candidatos regulatórios deverão ser integrados aos dados de RNA-seq para
testar se genes com arquiteturas promotoras distintas apresentam respostas de
expressão coerentes sob os tratamentos avaliados. Para pares ortólogos, será
útil alinhar as regiões promotoras e distinguir ganho ou perda de motivos de
simples alterações no número de correspondências. Para `VpOSCA2.4a` e
`VpOSCA2.4b`, a comparação prioritária será verificar se a divergência de
motivos acompanha expressão diferencial entre os parálogos. Evidências de
ATAC-seq, DAP-seq, ChIP-seq ou ensaios com promotores seriam necessárias para
validar atividade cis-regulatória.

## 6. RNA-seq e expressão tecido-específica

### 6.1 Evidências observadas

O conjunto de RNA-seq compreende bibliotecas paired-end de folha, caule e raiz.
Foram processadas nove amostras de *Vellozia peripherica*, correspondentes a
três indivíduos com os três tecidos, e oito amostras de *Vellozia tubiflora*.
Nesta última espécie, há três amostras de folha e caule, mas apenas duas de raiz,
pois `VT1R` não está presente nos dados analisados. As duas lanes de cada amostra
foram concatenadas antes da filtragem com fastp.

O processamento disponível registra FastQC 0.12.1, fastp 0.23.4, STAR 2.7.11b
e featureCounts 2.1.1. A mediana de retenção após fastp foi 90,38% em *V.
peripherica* e 91,34% em *V. tubiflora*. A proporção mediana de bases Q30 após
a filtragem foi 95,27% e 95,32%, respectivamente. Portanto, a qualidade de bases
após a filtragem foi elevada, embora isso não tenha se traduzido em taxas
uniformes de alinhamento.

A proporção de pares mapeados unicamente pelo STAR variou de 37,22% a 85,68% em
*V. peripherica*, com mediana de 72,29%, e de 18,41% a 86,17% em *V.
tubiflora*, com mediana de 70,13%. Apenas quatro das 17 bibliotecas superaram
80% de mapeamento único. `VP2R` apresentou 37,22% de mapeamento único e 56,73%
de pares classificados como “unmapped: too short”, enquanto `VT2R` apresentou
18,41% e 80,71%, respectivamente. Assim, essas duas bibliotecas representam os
principais desvios de qualidade do alinhamento e precisam ser investigadas
antes da análise definitiva.

O featureCounts atribuiu entre 80,85% e 84,51% das unidades classificadas em
*V. peripherica* e entre 82,72% e 85,22% em *V. tubiflora*. Entretanto, esses
percentuais referem-se à configuração de contagem atual e não compensam a perda
anterior de pares no alinhamento. Além disso, os arquivos `ReadsPerGene` do STAR
mostram de 38 a 97 vezes mais atribuições na orientação reversa do que na
orientação direta, indicando bibliotecas fortemente reverso-orientadas. O
featureCounts foi executado sem parâmetro de fita e com `-p`, mas sem a opção
explícita de contagem por pares. Os totais resultantes são compatíveis com
contagem de read ends, e não de fragmentos. Por esse motivo, os resultados de
expressão diferencial descritos a seguir devem ser considerados preliminares.

Após a remoção de genes com soma inferior a 10 contagens, foram mantidos 22.532
de 26.466 modelos gênicos em *V. peripherica* e 20.968 de 25.551 em *V.
tubiflora*. A análise foi realizada separadamente por espécie com DESeq2,
utilizando o modelo `~ Individual + Tissue`. A análise de componentes
principais separou os tecidos predominantemente no primeiro componente, que
explicou 80% da variância em *V. peripherica* e 81% em *V. tubiflora*. O segundo
componente explicou 7% e 10%, respectivamente. Em *V. peripherica*, folha foi
separada de caule e raiz ao longo do primeiro componente; em *V. tubiflora*, os
três tecidos ocuparam regiões distintas nos dois primeiros componentes.

Considerando simultaneamente `padj < 0,05` e `|log2FC| >= 1`, os números de genes
diferencialmente expressos no genoma foram:

| Contraste | *V. peripherica* | *V. tubiflora* |
| --- | ---: | ---: |
| Raiz versus folha | 5.978 | 5.691 |
| Raiz versus caule | 79 | 3.867 |
| Caule versus folha | 6.160 | 6.881 |

A diferença acentuada entre as espécies no contraste raiz versus caule precisa
ser interpretada à luz do menor número de raízes, do desbalanceamento do modelo
e dos desvios de alinhamento observados em *V. tubiflora*.

Entre os genes OSCA, três padrões significativos foram compartilhados entre as
espécies. Valores positivos indicam maior expressão no primeiro tecido do
contraste; valores negativos indicam maior expressão no segundo.

| Gene e contraste | *V. peripherica*: log2FC; padj | *V. tubiflora*: log2FC; padj |
| --- | ---: | ---: |
| OSCA1.1, raiz versus folha | -1,398; 0,0252 | -1,176; 0,0474 |
| OSCA1.1, caule versus folha | -1,783; 0,00302 | -2,064; 2,69 × 10^-6 |
| OSCA1.2, raiz versus folha | 4,357; 0,0115 | 8,265; 1,68 × 10^-4 |
| OSCA1.2, caule versus folha | 5,300; 0,00141 | 5,369; 0,00882 |
| OSCA3.1, caule versus folha | -1,683; 7,57 × 10^-4 | -2,912; 5,31 × 10^-5 |

Em *V. peripherica*, quatro genes OSCA apresentaram `padj < 0,05` no contraste
raiz versus folha, nenhum no contraste raiz versus caule e quatro no contraste
caule versus folha. Além dos padrões compartilhados acima, `VpOSCA2.3`
apresentou maior expressão no caule do que na folha (log2FC = 4,125; padj =
0,0461). Em *V. tubiflora*, foram identificados quatro, três e sete genes OSCA
com `padj < 0,05` nos mesmos contrastes. Entre os resultados com
`|log2FC| >= 1`, destacaram-se `VtOSCA3.2` em raiz versus folha (log2FC = 4,417;
padj = 0,0103), `VtOSCA2.4` em raiz versus caule (log2FC = 1,012; padj =
0,00623), `VtOSCA2.5` em raiz versus caule e caule versus folha (log2FC = 1,100
e -1,553; padj = 0,0290 e 1,10 × 10^-5) e `VtOSCA4.1` nesses mesmos contrastes
(log2FC = 1,841 e -1,443; padj = 0,00338 e 0,00341).

Nenhum dos parálogos `VpOSCA2.4a` e `VpOSCA2.4b` apresentou expressão
diferencial com `padj < 0,05` nos três contrastes. As médias normalizadas de
`VpOSCA2.4a` foram 572,73 em folha, 1.083,84 em caule e 801,08 em raiz; para
`VpOSCA2.4b`, foram 1.164,58, 1.386,94 e 1.422,97, respectivamente. Esses
valores mostram diferenças descritivas entre os parálogos, mas o modelo atual
não testou diretamente a expressão de uma cópia contra a outra.

**Arquivos de origem:**

- `analyses/05_rnaseq/results/02_trimmed/*/*_fastp.json`
- `analyses/05_rnaseq/results_genecounts/04_alignment/*/*/*_Log.final.out`
- `analyses/05_rnaseq/results_genecounts/04_alignment/*/*/*_ReadsPerGene.out.tab`
- `analyses/05_rnaseq/results_genecounts/05_counts/*_star_genecounts_col4.tsv`
- `analyses/05_rnaseq/scripts/pipeline.py`
- `analyses/06_expression/results_genecounts/*_OSCA_DE_results.csv`
- `analyses/06_expression/results_genecounts/*_OSCA_normalized_counts.csv`
- `analyses/06_expression/scripts/run_deseq2.R`
- `reports/figures/06_expression_genecounts/`

### 6.2 Interpretação em português

O padrão mais consistente é a conservação de vieses teciduais para OSCA1.1,
OSCA1.2 e OSCA3.1. OSCA1.2 apresentou expressão muito reduzida em folha e maior
expressão em caule e raiz nas duas espécies. Em sentido oposto, OSCA1.1 foi mais
expresso em folha do que nos outros dois tecidos, e OSCA3.1 apresentou viés
foliar significativo no contraste com caule. Esses resultados sustentam uma
distribuição tecidual parcialmente conservada após a divergência das espécies.

Os valores elevados de log2FC de OSCA1.2 devem ser interpretados juntamente com
sua expressão basal baixa e com contagens próximas de zero em algumas amostras
de folha. O resultado é compatível com expressão preferencial em tecidos não
foliares, mas não demonstra, por si só, uma função ancestral na percepção
osmótica vascular ou subterrânea. De modo semelhante, o enriquecimento foliar
de OSCA1.1 e OSCA3.1 não comprova atuação em células-guarda, regulação estomática
ou controle do turgor, pois os dados não possuem resolução celular nem ensaio
funcional.

Os perfis adicionais de `VpOSCA2.3`, `VtOSCA2.4`, `VtOSCA2.5`, `VtOSCA3.2` e
`VtOSCA4.1` definem candidatos para divergência regulatória entre as espécies.
Contudo, a forte diferença no número de genes diferencialmente expressos entre
raiz e caule, aliada ao menor número de raízes e à baixa taxa de alinhamento de
`VT2R`, impede atribuir essa diferença imediatamente à estratégia de tolerância
à dessecação. Além disso, o experimento compara tecidos e não inclui, nos
metadados disponíveis, um contraste explícito de déficit hídrico. Portanto,
esses resultados não constituem evidência direta de resposta à seca.

### 6.3 Draft in English

Paired-end RNA-seq data were analyzed for leaf, stem, and root tissues from
three *Vellozia peripherica* individuals and for leaf and stem tissues from
three *Vellozia tubiflora* individuals, with root represented by two individuals
in the latter species. After fastp filtering, median read retention was 90.38%
in *V. peripherica* and 91.34% in *V. tubiflora*, and median Q30 base rates were
95.27% and 95.32%, respectively. Unique mapping rates were more variable,
ranging from 37.22% to 85.68% in *V. peripherica* and from 18.41% to 86.17% in
*V. tubiflora*. In particular, VP2R and VT2R exhibited low unique mapping and
high proportions of reads classified as too short to map. Principal component
analysis nevertheless showed strong tissue-level structure, with PC1 explaining
80% and 81% of the variance in *V. peripherica* and *V. tubiflora*,
respectively.

The validated differential expression analysis was performed separately for each
species using an individual-blocked design (`~ Individual + Tissue`). A
conserved tissue-biased pattern was observed for three OSCA genes. OSCA1.2 was
more highly expressed in root than leaf in both species (log2FC = 4.357, padj =
0.0115 in *V. peripherica*; log2FC = 8.265, padj = 1.68 × 10^-4 in *V.
tubiflora*) and was also enriched in stem relative to leaf. Conversely, OSCA1.1
was consistently leaf-enriched in both root-versus-leaf and stem-versus-leaf
comparisons. OSCA3.1 also showed significant leaf enrichment relative to stem
in both species. These results support partially conserved tissue-biased
expression across species, although they do not establish the cell types or
physiological processes in which these channels operate.

Additional species-specific candidates included VpOSCA2.3, which was enriched
in stem relative to leaf, and VtOSCA2.4, VtOSCA2.5, VtOSCA3.2, and VtOSCA4.1,
which showed significant differences in contrasts involving root or stem. The
two *V. peripherica* OSCA2.4 paralogs differed descriptively in their normalized
expression profiles but were not significantly differentially expressed in
any tissue contrast. Direct tests of paralog expression and ortholog-by-tissue
interactions will be required before inferring regulatory subfunctionalization
or interspecific expression divergence.

### 6.4 Limitações e validações pendentes

A configuração de contagem foi validada por uma rerun independente com STAR
GeneCounts. A coluna antissenso foi selecionada para as bibliotecas
reverso-orientadas, e os resultados antigos de featureCounts foram preservados
apenas como comparação. A comparação quantitativa está em
`reports/star_genecounts_validation.md`; os resultados novos devem ser usados
como base principal para a interpretação final.

Os relatórios FastQC foram gerados para as reads brutas e pós-filtragem, com
consolidação MultiQC. As causas das taxas reduzidas de alinhamento de
`VP2R` e, principalmente, `VT2R` devem ser avaliadas por inspeção de
contaminação, composição taxonômica, conteúdo de RNA ribossomal, identidade da
amostra e compatibilidade com o genoma de referência. Critérios de exclusão ou
retenção precisam ser definidos antes de examinar novamente os resultados de
expressão.

A ausência de `VT1R` produz um desenho desbalanceado e deixa o tecido raiz com
apenas duas réplicas em *V. tubiflora*. A amostra não foi sequenciada porque,
após inúmeras tentativas de extração, o RNA de `VT1R` não atingiu quantidade e
métricas de qualidade suficientes para preparação da biblioteca. Portanto,
`VT1R` é biologicamente indisponível para o rerun e não deve ser tratado como
uma amostra removida pelo processamento computacional. A adequação dos graus
de liberdade do desenho desbalanceado deve permanecer documentada.

Um teste de mapeamento cruzado não sustentou a hipótese de troca entre `VT2R`
e `VP2R`. `VT2R` apresentou 18,41% de mapeamento único contra o índice de
*V. tubiflora* e 15,85% contra o índice de *V. peripherica*; `VP2R` apresentou
37,22% no índice de *V. peripherica* e 32,26% no índice de *V. tubiflora*.
Assim, as reads de `VT2R` permanecem mais compatíveis com a espécie atribuída,
embora a biblioteca continue sendo um outlier de baixa qualidade/compatibilidade
e deva ser interpretada com cautela.

Uma análise de sensibilidade sem `VT2R` foi executada, mas deixa *V. tubiflora*
com apenas uma réplica de raiz (`VT3R`). Por isso, seus contrastes envolvendo
raiz são descritivos e não substituem a análise principal, que mantém `VT2R`.

As contagens normalizadas foram calculadas separadamente por espécie. Portanto,
a figura comparativa de ortólogos não deve ser usada para concluir que um gene
é mais expresso em uma espécie do que na outra a partir da altura das barras.
Uma comparação interespecífica deverá utilizar ortólogos definidos, respostas
relativas dentro de cada espécie ou um modelo conjunto que represente
explicitamente a interação entre espécie e tecido. A duplicação de
`VtOSCA2.4` nos painéis comparativos de `VpOSCA2.4a` e `VpOSCA2.4b` também deve
ser indicada visualmente como uma relação um-para-muitos, e não como duas
observações independentes.

Por fim, a execução validada usou R 4.5.1 e registrou o término do DESeq2; não
foi aplicado shrinkage dos log2FC e os critérios de
significância usados nas tabelas (`padj < 0,05`) e nos volcano plots
(`padj < 0,05` e `|log2FC| >= 1`) precisam ser harmonizados. Os metadados de
preparo das bibliotecas, orientação, lote, qualidade do RNA e condição hídrica
também devem ser incorporados antes da redação final de Material e Métodos.

### 6.5 Conexões a avaliar posteriormente

Após a recontagem e a repetição da análise estatística, os contrastes de
expressão poderão ser relacionados aos motivos promotores. A associação mais
informativa será verificar se diferenças cis-regulatórias entre
`VpOSCA2.4a` e `VpOSCA2.4b` acompanham respostas teciduais distintas. Para os
pares OSCA1.1, OSCA1.2 e OSCA3.1, a conservação de direção entre espécies poderá
ser testada formalmente por efeitos de interação, em vez de ser inferida apenas
pela comparação de análises separadas.

Os perfis de expressão também deverão ser confrontados com a conectividade nas
redes de associação funcional entre proteínas. Essa integração poderá
priorizar genes que combinam expressão tecido-específica e posição central na
rede, mas não deverá ser usada para atribuir função sem validação experimental.

## 7. Redes de associação funcional entre proteínas

### 7.1 Evidências observadas

As redes foram obtidas pelo endpoint `/network` do STRING a partir dos 14 genes
OSCA de *Vellozia peripherica* e dos 13 genes OSCA de *Vellozia tubiflora*. A
consulta utilizou o tipo de rede `functional`, limiar de confiança média
(`required_score = 400`, equivalente a escore combinado ≥ 0,400) e adição de
50 proteínas associadas a cada conjunto de genes-semente. Portanto, as arestas
representam associações funcionais conhecidas ou previstas pelo STRING e não
devem ser tratadas, de forma geral, como interações físicas diretas.

A rede retornada para *V. peripherica* continha 61 nós e 187 arestas, enquanto a
rede de *V. tubiflora* continha 60 nós e 217 arestas. Ambas foram divididas em
dois componentes conectados; os tamanhos dos componentes foram 55 e 6 nós em
*V. peripherica* e 54 e 6 nós em *V. tubiflora*. As métricas descritivas foram:

| Métrica | *V. peripherica* | *V. tubiflora* |
| --- | ---: | ---: |
| Genes OSCA consultados | 14 | 13 |
| Genes OSCA presentes na rede retornada | 11 | 10 |
| Nós totais | 61 | 60 |
| Arestas | 187 | 217 |
| Grau médio | 6,13 | 7,23 |
| Densidade | 0,102 | 0,123 |
| Coeficiente médio de agrupamento | 0,494 | 0,472 |

Os genes OSCA2.1, OSCA2.2 e OSCA2.3 não apareceram nos arquivos de arestas de
nenhuma das espécies. Esse resultado significa apenas que nenhuma associação
acima do limiar foi retornada para esses genes nas condições da consulta; não
indica ausência de função, expressão ou interação no organismo.

Entre os genes-semente recuperados, OSCA1.2 apresentou grau 18 nas duas
espécies. OSCA4.1 foi o gene OSCA de maior grau em *V. peripherica* (19), mas
teve grau 13 em *V. tubiflora*. OSCA1.1 apresentou graus 11 e 13,
respectivamente. A distribuição completa dos graus foi:

| Grupo OSCA | *V. peripherica* | *V. tubiflora* |
| --- | ---: | ---: |
| OSCA1.1 | 11 | 13 |
| OSCA1.2 | 18 | 18 |
| OSCA1.3 | 1 | 3 |
| OSCA1.4 | 1 | 3 |
| OSCA1.5 | 1 | 3 |
| OSCA2.1 | 0 | 0 |
| OSCA2.2 | 0 | 0 |
| OSCA2.3 | 0 | 0 |
| OSCA2.4 | VpOSCA2.4a: 2; VpOSCA2.4b: 2 | VtOSCA2.4: 5 |
| OSCA2.5 | 4 | 7 |
| OSCA3.1 | 4 | 4 |
| OSCA3.2 | 4 | 4 |
| OSCA4.1 | 19 | 13 |

VpOSCA2.4a e VpOSCA2.4b apresentaram exatamente os mesmos dois vizinhos:
VpOSCA4.1 e `Vper.hapA.v1.chr6A.g166880.t1`, com escores combinados de 0,456 e
0,484, respectivamente. VtOSCA2.4 apresentou cinco vizinhos, incluindo
VtOSCA4.1. Assim, os dados atuais não mostram partição de parceiros entre as
duas cópias de *V. peripherica*.

As 65 arestas incidentes em genes OSCA de *V. peripherica* e as 72 de *V.
tubiflora* foram também separadas pelos canais de evidência fornecidos pelo
STRING. Uma mesma aresta pode receber contribuição de mais de um canal.

| Canal de evidência em arestas com OSCA | *V. peripherica* | *V. tubiflora* |
| --- | ---: | ---: |
| Mineração de texto | 46/65 (70,8%) | 52/72 (72,2%) |
| Bancos de dados curados | 18/65 (27,7%) | 19/72 (26,4%) |
| Evidência experimental no registro do STRING | 4/65 (6,2%) | 4/72 (5,6%) |
| Coocorrência filogenética | 4/65 (6,2%) | 2/72 (2,8%) |
| Coexpressão | 0/65 | 0/72 |
| Vizinhança genômica | 0/65 | 0/72 |
| Fusão gênica | 0/65 | 0/72 |

Trinta e nove arestas com OSCA em *V. peripherica* e 47 em *V. tubiflora*
foram sustentadas exclusivamente por mineração de texto. Outras 18 e 19,
respectivamente, foram sustentadas exclusivamente pelo canal de bancos de
dados. A presença de um componente experimental no STRING não demonstra que a
interação tenha sido testada nas duas espécies de *Vellozia*, pois as evidências
podem ter sido transferidas de proteínas homólogas.

O enriquecimento funcional foi calculado sobre todos os nós das redes
expandidas. Entre os termos coerentes com a família OSCA, a atividade de canal
catiônico ativado por cálcio incluiu 11 proteínas em *V. peripherica* (FDR =
5,64 × 10^-20) e 10 em *V. tubiflora* (FDR = 8,80 × 10^-18). A atividade de
canal mecanossensível incluiu três proteínas em cada espécie (FDR = 6,50 ×
10^-4 e 4,90 × 10^-4), correspondentes aos grupos OSCA1.3, OSCA1.4 e OSCA1.5.
Termos associados à membrana plasmática e à periferia celular também foram
enriquecidos nas duas redes.

Contudo, os resultados de enriquecimento foram dominados por anotações de
metabolismo de amido, sacarose e atividade de amilase entre os 50 parceiros
adicionados. As tabelas também contêm termos incompatíveis com o contexto
vegetal, como complexo receptor de amilina, sistema imune inato e degranulação
de neutrófilos. Esses termos evidenciam transferência de anotações e não foram
considerados evidência biológica para *Vellozia*.

**Arquivos de origem:**

- `analyses/01_gene_identification/results/oscasIDs.txt`
- `analyses/07_ppi_network/results/Vper_ppi_network.tsv`
- `analyses/07_ppi_network/results/Vtub_ppi_network.tsv`
- `analyses/07_ppi_network/results/Vper_enrichment.tsv`
- `analyses/07_ppi_network/results/Vtub_enrichment.tsv`
- `analyses/07_ppi_network/results/Vper_functional_annotation.tsv`
- `analyses/07_ppi_network/results/Vtub_functional_annotation.tsv`
- `analyses/07_ppi_network/scripts/run_vtub_ppi.py`
- `analyses/07_ppi_network/scripts/PPI_Network.ipynb`
- `analyses/07_ppi_network/results/Vper_networkx.png`
- `analyses/07_ppi_network/results/Vtub_networkx.png`
- `analyses/07_ppi_network/results/Vper_ppi_network.png`
- `analyses/07_ppi_network/results/Vtub_ppi_network.png`

### 7.2 Interpretação em português

A conservação do grau de OSCA1.2 nas duas redes torna esse gene um candidato
consistente para estudos posteriores de contexto funcional. A elevada
conectividade de OSCA4.1 em *V. peripherica* também é descritivamente relevante,
mas a redução de grau em *V. tubiflora* não pode ser atribuída a diferenças de
adaptação, resposta ao estresse ou estratégia de dessecação. As redes não foram
comparadas por um teste estatístico e sua topologia depende da cobertura do
STRING, da transferência entre homólogos e da escolha automática dos 50
parceiros adicionais.

Pelo mesmo motivo, a maior quantidade de arestas e a maior densidade da rede de
*V. tubiflora* não demonstram uma resposta molecular mais rápida ou mais
integrada nessa espécie. A diferença é uma observação sobre duas redes
preditas, construídas a partir de números distintos de genes-semente e sem
controle para a anotação disponível em cada proteoma.

A comparação de OSCA2.4 é particularmente informativa para delimitar o que os
dados não mostram. Embora VtOSCA2.4 tenha grau 5 e cada paráloga de *V.
peripherica* tenha grau 2, VpOSCA2.4a e VpOSCA2.4b compartilham todos os seus
vizinhos. Portanto, a topologia atual não sustenta subfuncionalização das
duplicatas. Para testar essa hipótese, seria necessário comparar parceiros
ortólogos em redes construídas sem expansão automática e obter evidência
experimental específica para cada cópia.

Os termos de canal catiônico, mecanossensibilidade e localização em membrana
são compatíveis com a classificação dos genes como OSCAs. Entretanto, esse
enriquecimento não constitui validação independente, porque os próprios genes
OSCA e os parceiros selecionados pelo STRING foram usados como conjunto de
entrada. Os termos taxonomicamente incompatíveis mostram ainda que anotações
transferidas precisam ser filtradas antes de qualquer interpretação funcional.

### 7.3 Draft in English

STRING functional association networks were generated from 14 *Vellozia
peripherica* and 13 *Vellozia tubiflora* OSCA proteins using a medium-confidence
combined-score threshold of 0.400 and network expansion with 50 additional
proteins. The resulting *V. peripherica* network comprised 61 nodes and 187
edges, whereas the *V. tubiflora* network comprised 60 nodes and 217 edges.
Their mean degrees were 6.13 and 7.23, respectively. Eleven *V. peripherica*
and ten *V. tubiflora* OSCA queries were retained in the returned edge lists;
OSCA2.1, OSCA2.2, and OSCA2.3 had no associations above the selected threshold
in either species.

OSCA1.2 had 18 associations in both networks. OSCA4.1 had the highest degree
among *V. peripherica* OSCA proteins (degree 19), compared with degree 13 in
*V. tubiflora*, while OSCA1.1 had degrees 11 and 13, respectively. These
differences are descriptive because no orthology-aware statistical comparison
of network topology was performed. Moreover, VpOSCA2.4a and VpOSCA2.4b each
had degree 2 and shared the same two predicted neighbors. Thus, the present
network does not provide evidence for partner partitioning between the tandem
duplicates.

Most OSCA-associated edges included text-mining evidence: 46 of 65 edges in
*V. peripherica* and 52 of 72 edges in *V. tubiflora*. Only four edges in each
species included an experimental evidence component in the STRING records,
and this component does not establish direct experimental support in
*Vellozia*. Functional enrichment recovered calcium-activated cation channel
activity, mechanosensitive ion channel activity, and plasma-membrane-related
terms in both species. However, the enrichment was performed on networks that
had already been expanded by STRING and was accompanied by transferred,
taxonomically incongruent annotations. The networks should therefore be used
for hypothesis generation rather than as evidence of physical interactions or
species-specific functional adaptation.

### 7.4 Limitações e validações pendentes

A consulta não registrou a versão do STRING, a data de recuperação nem os
metadados completos da resposta. Embora os parâmetros estejam presentes nos
scripts, a reprodução exata dependerá do estado futuro do banco. As redes
também foram construídas com `network_type = functional`; consequentemente,
uma aresta pode representar associação indireta e não contato físico entre as
proteínas.

A adição de 50 parceiros introduz dependência circular entre a expansão da rede
e o enriquecimento funcional posterior. Antes da redação final, as consultas
devem ser repetidas sem nós adicionais e comparadas com redes `physical`, com
limiares mais estritos e com análises que removam ou separem o canal de
mineração de texto. O enriquecimento deverá utilizar um universo de fundo
explicitamente definido e adequado ao proteoma de cada espécie.

Os parceiros das duas espécies ainda não foram relacionados por ortologia.
Assim, diferenças de grau não distinguem ganho ou perda biológica de interação
de diferenças de anotação e cobertura. Termos incompatíveis com plantas devem
ser excluídos ou rastreados até sua espécie de origem. Os arquivos locais não
registram evidência de interação física específica de *Vellozia*.

As figuras atuais são úteis para inspeção, mas os identificadores longos se
sobrepõem e dificultam a leitura. A figura final deverá distinguir genes-semente
de parceiros adicionados, substituir os identificadores dos OSCAs pelos nomes
curtos, omitir rótulos não essenciais e representar separadamente os canais de
evidência. Também deverá informar que nós ausentes não equivalem a proteínas
sem função.

Interações prioritárias poderão ser testadas por métodos adequados a proteínas
de membrana, como sistema split-ubiquitin, complementação de fluorescência ou
luminescência, coimunoprecipitação e marcação de proximidade. A localização
subcelular e a expressão simultânea dos pares deverão ser verificadas antes da
seleção experimental.

### 7.5 Conexões a avaliar posteriormente

OSCA1.2 combina grau elevado e conservado com o viés de expressão em caule e
raiz observado nas duas espécies, o que o torna um candidato para integração
posterior. Essa coincidência não demonstra que os parceiros previstos atuem nos
mesmos tecidos; a coexpressão deverá ser testada diretamente. OSCA4.1 também
pode ser priorizado após a filtragem das evidências, sobretudo para avaliar se
sua maior conectividade prevista em *V. peripherica* persiste em redes sem
mineração de texto e com parceiros ortólogos.

Para OSCA2.4, a ausência de divergência entre os vizinhos previstos das duas
cópias de *V. peripherica* deverá ser confrontada com as diferenças de
promotores, expressão e estrutura. A próxima análise estrutural poderá indicar
se há alterações em regiões potencialmente envolvidas em interação, mas não
será suficiente, isoladamente, para confirmar parceiros moleculares.

## Próxima etapa de revisão

A próxima etapa é revisar as comparações estruturais em
`analyses/08_structural`. Antes da versão final do capítulo, as redes deverão
ser reconsultadas com parâmetros que separem associações funcionais de
interações físicas, controlem a expansão automática e registrem a versão do
STRING. A etapa de RNA-seq também deverá retornar ao pipeline de contagem para
corrigir orientação, unidade de contagem e documentação de qualidade.
