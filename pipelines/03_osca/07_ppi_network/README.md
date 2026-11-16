

## Scientific Insights

================================================================================
ASSOCIAÇÕES FUNCIONAIS DA FAMÍLIA OSCA EM VELLOZIA: RESULTADOS E LIMITES
================================================================================
Tese: Genomic Architecture, Evolutionary Dynamics, and Tissue-Specific Expression
      of OSCA Channels in Two Vellozia Species
Autora: Mariana Feitosa Cavalheiro
Atualização: 2026-09-16 — revisão crítica confrontada com os resultados arquivados
Data original: 2026-05-25

1. ESCOPO E DESENHO DA ANÁLISE
--------------------------------------------------------------------------------
As redes comparam associações funcionais previstas para proteínas OSCA de
Vellozia peripherica (Vper) e Vellozia tubiflora (Vtub). O script solicita ao STRING
network_type="functional", required_score=400 e add_nodes=50. Portanto, trata-se
de redes expandidas a partir dos OSCAs, com limiar de score de 0,400, incluindo
associações entre parceiros adicionados. As arestas não demonstram, por si só,
ligação física direta nem direção causal de regulação.

Os números de nós abaixo consideram apenas proteínas presentes nas arestas.
Três OSCAs de cada espécie não têm arestas retornadas e não entram nesse total.
A consulta não representa uma condição experimental de seca, reidratação ou
expressão basal. A comparação é descritiva entre duas espécies; não constitui
replicação independente de estratégias hídricas.

2. TOPOLOGIA COMPARADA
--------------------------------------------------------------------------------
Medida                                  Vper             Vtub
Nós presentes nas arestas                61               60
Arestas únicas                           187              217
Grau médio da rede                       6,13             7,23
Densidade                                0,1022           0,1226
Grau médio dos OSCAs conectados          6,09             7,30
OSCAs conectados / consultados           11/14            10/13
Coeficiente de agrupamento médio         0,4937           0,4718
Componentes conectados                   2                2
Tamanhos dos componentes                 55 e 6           54 e 6

A densidade foi calculada como 2E/[N(N−1)] para grafos simples não direcionados.
Vtub apresenta 16,0% mais arestas e densidade maior, enquanto o agrupamento médio
é menor. Não foi realizado teste de diferença entre redes: não cabe afirmar
que Vtub é "significativamente mais densa". Compacidade, velocidade de sinalização
e coordenação pré-anidrobiose não foram medidas.

Essas diferenças dependem da expansão de parceiros, do limiar, da cobertura de
anotação e do mapeamento nas duas espécies. Uma comparação evolutiva mais forte
requer correspondência ortológica dos nós e análise de sensibilidade a esses
parâmetros, incluindo redes sem expansão.

3. GRAU DOS MEMBROS OSCA
--------------------------------------------------------------------------------
Membro                  Vper       Vtub       Descrição limitada à rede retornada
OSCA1.1                 11         13         Graus diferentes
OSCA1.2                 18         18         Mesmo grau
OSCA1.3                  1          3         Poucas associações retornadas
OSCA1.4                  1          3         Poucas associações retornadas
OSCA1.5                  1          3         Poucas associações retornadas
OSCA2.1                  0          0         Sem aresta retornada
OSCA2.2                  0          0         Sem aresta retornada
OSCA2.3                  0          0         Sem aresta retornada
OSCA2.4 (cópia única)     —          5         Uma cópia no catálogo de Vtub
OSCA2.4a                 2          —         Cópia adjacente em Vper
OSCA2.4b                 2          —         Cópia adjacente em Vper
OSCA2.5                  4          7         Graus diferentes
OSCA3.1                  4          4         Componente de seis nós
OSCA3.2                  4          4         Componente de seis nós
OSCA4.1                 19         13         Maior grau da rede Vper

Igualdade de grau não demonstra identidade dos parceiros, conservação estrita
da topologia ou equivalência funcional. Grau é uma medida de conectividade;
não estabelece localização celular, indispensabilidade ou controle fisiológico.

4. CANDIDATOS PARA INVESTIGAÇÃO FUNCIONAL
--------------------------------------------------------------------------------
OSCA1.2
Apresenta grau 18 em ambas as redes. Na análise de expressão auditada, os contrastes
raiz–folha foram log2FC=4,3568 em Vper e 8,2653 em Vtub; os contrastes caule–folha
foram 5,3005 e 5,3692, respectivamente. Esses resultados descrevem diferenças
entre órgãos dentro de cada espécie. Não identificam células vasculares e não
constituem teste de resposta à seca ou de diferença de expressão entre espécies.

Entre os vizinhos de OSCA1.2, 16 em Vper e 17 em Vtub pertencem à união das listas
de anotações cujas descrições contêm "amylase" ou "Starch and sucrose" nos arquivos
functional_annotation.tsv. Esse critério conta cada vizinho uma única vez e
não equivale a demonstrar que todos são enzimas caracterizadas experimentalmente.
A associação permite priorizar uma possível relação funcional com metabolismo
de carboidratos. Não demonstra interação física direta, indução de hidrólise de
amido por cálcio, produção de osmoprotetores ou ajuste osmótico vascular.

OSCA4.1
Apresenta grau 19 em Vper, o maior grau observado nessa rede, e 13 em Vtub.
Essa diferença permite priorizar a comparação de parceiros e canais de evidência.
Não demonstra uma função de monitoramento térmico ou proteção contra estresse
proteotóxico. As atribuições anteriores a HSP70 e aos identificadores abreviados
Vper_030510/Vtub_030510 não são mantidas sem reconciliação explícita com os IDs
canônicos, as arestas e as anotações de cada parceiro.

OSCA1.1
Apresenta graus 11 e 13. O RNA-seq auditado mostrou maior abundância em folha
em relação a raiz e caule nas duas espécies. Esse padrão orienta estudos de
localização e função em tecidos foliares, mas não identifica células-guarda
nem demonstra regulação do fechamento estomático.

OSCA3.1 e OSCA3.2
Integram um componente de seis nós em cada espécie, com grau quatro por OSCA.
A similaridade desses resumos topológicos não prova identidade ortológica de
todos os parceiros. Anotações de compartimentos nos nós não demonstram que os
OSCAs se localizam nesses compartimentos. A desconexão no grafo não estabelece
isolamento físico ou uma unidade funcional de tonoplasto e cloroplasto.

5. OSCA2.4: CONFIGURAÇÃO DE CÓPIAS E PARCEIROS
--------------------------------------------------------------------------------
A comparação genômica identifica duas cópias adjacentes em Vper e uma em Vtub.
Sem polarização com outros táxons, a configuração não resolve ganho em Vper versus
perda em Vtub; Vtub não deve ser tratado como ancestral de cópia única.

VpOSCA2.4a e VpOSCA2.4b possuem exatamente os mesmos dois vizinhos retornados:
  - Vper.hapA.v1.chr6A.g166880.t1
  - Vper.hapA.v1.chr8A.g231320.t1

VtOSCA2.4 possui cinco vizinhos:
  - Vtub.hapA.v1.chr3A.g086460.t1
  - Vtub.hapA.v1.chr4A.g119600.t1
  - Vtub.hapA.v1.chr5A.g132630.t1
  - Vtub.hapA.v1.chr6A.g149120.t1
  - Vtub.hapA.v1.chr8A.g207990.t1

Não há partição de parceiros entre as duas cópias de Vper nessa rede. Portanto,
o resultado não sustenta a alegação anterior de subfuncionalização. A igualdade
dos vizinhos também não prova redundância funcional. Testar subfuncionalização
requer reconstrução da história das cópias e evidências de partição de funções
ou regulação, além de correspondência ortológica dos parceiros entre espécies.

6. OSCAs SEM ARESTAS RETORNADAS
--------------------------------------------------------------------------------
OSCA2.1, OSCA2.2 e OSCA2.3 têm grau zero nas duas consultas. Isso pode refletir
cobertura insuficiente, mapeamento, limiar de score ou ausência de associações
conhecidas. Não permite inferir silêncio biológico, pseudogenização, limiar
mecânico alto ou ativação exclusiva durante desidratação extrema.

O Ka/Ks pareado de OSCA2.3 (0,0530) descreve restrição média de sequência e não
explica a ausência de arestas. Para VpOSCA2.2, o modelo curto e a ausência de
PF13967 nos resultados arquivados permanecem questões de anotação a validar.
Não há evidência apresentada de uma estratégia adaptativa de "blindagem contra
ruído" nem de uma rede constitutiva específica desses canais.

7. ENRIQUECIMENTO FUNCIONAL
--------------------------------------------------------------------------------
Termo / conjunto                         Vper: n; FDR        Vtub: n; FDR
Amido e sacarose (map00500)               22; 2,60e-26        23; 3,57e-28
Alfa-amilase (GO:0004556)                  3; 6,93e-05         3; 5,09e-05
Canal catiônico ativado por cálcio
  (GO:0005227)                           11; 5,64e-20        10; 8,80e-18
Plasmodesmo (GO:0009506)                  7; 7,60e-03         7; 8,80e-03
Periferia celular (GOCC:0071944)          16; 2,90e-04        15; 3,10e-04

Os valores foram conferidos nos arquivos de enriquecimento; n indica proteínas
do conjunto associadas ao termo, não o número de genes individualmente
"enriquecidos". O arquivo functional_annotation.tsv descreve anotações; os
valores de FDR provêm de enrichment.tsv.

O script envia os nós presentes nas arestas da rede expandida ao endpoint de
enriquecimento, sem informar um universo experimental personalizado. Assim,
os testes descrevem esse conjunto em relação ao background usado pelo STRING.
A seleção de parceiros por associação funcional pode favorecer a recuperação
de categorias relacionadas; os FDRs não corrigem essa dependência da seleção.
O enriquecimento não constitui confirmação independente do mecanismo proposto.

O termo GO:0005227 é uma anotação funcional e não comprova experimentalmente
ativação dos OSCAs de Vellozia por cálcio. Canal permeável a cálcio e canal
ativado por cálcio são propriedades distintas. Da mesma forma, enriquecimento
de plasmodesmos não demonstra propagação sistêmica de um sinal originado em
OSCA, e anotação de periferia celular não equivale especificamente a membrana
plasmática para todos os nós.

8. CANAIS DE EVIDÊNCIA E SÍNTESE EVOLUTIVA
--------------------------------------------------------------------------------
Na rede Vper, 132/187 arestas (70,59%) têm score de mineração de texto maior que
zero; em Vtub, 157/217 (72,35%). Há score experimental não nulo em cinco arestas
por rede e score de banco curado em 109 e 119 arestas, respectivamente. Os canais
se sobrepõem. A presença de score experimental não demonstra que o experimento
foi realizado nas espécies focais nem que a associação é uma ligação direta.

As redes mostram semelhanças e diferenças descritivas que podem orientar testes
do modelo evolutivo de duas vertentes. Não estabelecem vias bioquímicas distintas,
conservação funcional invariável ou reconfiguração adaptativa para anidrobiose.
A história de cópias e os testes de seleção fornecem evidências evolutivas em
escalas próprias; a rede agrega associações previstas e não valida causalmente
esses resultados. Em particular, a semelhança dos graus de OSCA3 não anula nem
explica o resultado de RELAX para OSCA3+4.

Uma síntese sustentada é: as redes expandidas apresentam diferenças de
conectividade e enriquecimento de anotações relacionadas a amido e sacarose.
Essas observações priorizam candidatos para investigação de metabolismo,
localização e sinalização, mantendo em aberto a ligação entre percepção
mecânica, resposta celular e sobrevivência à dessecação.

Próximos testes pertinentes incluem análise sem expansão, sensibilidade ao
limiar, comparação de parceiros por ortologia e por canal de evidência,
enriquecimento separado dos OSCAs e dos parceiros e validação experimental
de associações selecionadas, expressão espacial e atividade dos canais.

9. PROVENIÊNCIA
--------------------------------------------------------------------------------
Dados locais usados (caminhos relativos à raiz de chapter2_osca):
  07_ppi_network/results/Vper_ppi_network.tsv
  07_ppi_network/results/Vtub_ppi_network.tsv
  07_ppi_network/results/Vper_functional_annotation.tsv
  07_ppi_network/results/Vtub_functional_annotation.tsv
  07_ppi_network/results/Vper_enrichment.tsv
  07_ppi_network/results/Vtub_enrichment.tsv
  07_ppi_network/scripts/run_vtub_ppi.py
  01_gene_identification/results/oscasIDs.txt
  manuscript/chapter_2_osca_mechanosensation.md (contrastes de expressão auditados)

Referências de interpretação do STRING:
  https://string-db.org/help/scores/
  https://string-db.org/help/api/

Nota de reprodutibilidade: run_vtub_ppi.py ainda aponta para diretórios sob
/home/mfcaval/github/doutorado/analyses/. Esses caminhos precisam ser reconciliados
com a estrutura atual antes de uma nova execução. Esta revisão utiliza os
resultados arquivados; não representa uma nova consulta à API.
================================================================================
