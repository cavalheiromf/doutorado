# Figuras dos perfis de linhagens — 2026-10-05

As três figuras foram geradas a partir da tabela comparativa atual, sem reexecutar CAFE ou MCMC. A figura de turnover existente completa o conjunto proposto para a apresentação. Todas as novas figuras têm versões PNG, PDF e SVG em `04_gene_families/figures/`.

## 1. Árvore datada com mudanças nas famílias

Arquivo: `figure_current_dated_family_changes`.

**Legenda:** Distribuição das mudanças reconstruídas nas 196 famílias de consenso entre modelos ao longo da filogenia datada. Os números em cada ramo indicam quantas famílias apresentam mudança positiva ou negativa no número de cópias, segundo a reconstrução de k=2, rep01. Comprimentos dos ramos representam as médias posteriores das idades; as idades assinaladas são 33,77 e 9,68 Ma. A figura não representa a incerteza das idades. A significância no nível da família não implica significância em todos os ramos.

**Mensagem para a apresentação:** “O capítulo permite localizar as mudanças na história evolutiva. No ramo ancestral de Xerophyta e Vellozia, 117 famílias de consenso apresentam mudança positiva e 19 apresentam mudança negativa.” Esse ramo corresponde ao nó 12, não ao ancestral exclusivo das duas Vellozia (nó 13).

## 2. Figura de turnover existente

Arquivo: `figure_current_family_turnover`.

Usar para apresentar o tamanho dos conjuntos e os totais nas linhagens terminais. Não substituir o consenso de 196 famílias pelo conjunto de 254 sem explicitar os níveis de evidência.

## 3. Mapa de calor de número de cópias

Arquivo: `figure_current_lineage_copy_heatmap`.

**Legenda:** Números de cópias nas sete espécies amostradas para as 196 famílias de consenso entre modelos (A) e as 58 famílias adicionais sustentadas por todas as execuções de k=3, mas sem atingir q ≤ 0,05 em pelo menos uma execução retida de k=2 (B). As cores representam log₂(contagem + 1), com a mesma escala nos dois painéis; zero corresponde à ausência de cópias na tabela de entrada. As famílias foram ordenadas separadamente em cada conjunto por agrupamento hierárquico, ligação média e distância euclidiana sobre as contagens transformadas. As colunas seguem a ordem da árvore. A linha branca separa as três linhagens focais das demais espécies; não marca um clado exclusivo dessas três espécies em relação a toda Velloziaceae. A ordem das linhas e as contagens exatas estão no arquivo `figure_current_lineage_copy_heatmap_rows.tsv`.

**Mensagem para a apresentação:** “Além do número total de famílias, podemos comparar quais repertórios estão representados em cada linhagem.” O agrupamento descreve semelhança de contagens; não constitui um teste independente de diferenciação entre espécies. As alturas iguais dos painéis facilitam a leitura, mas cada painel contém um número diferente de famílias.

## 4. Exemplos de histórias contrastantes

Arquivo: `figure_current_family_examples`.

**Legenda:** Três famílias do consenso entre modelos escolhidas para ilustrar padrões contrastantes: OG0000035, anotada como germin-like protein, com mudança +13 no ancestral de Xerophyta–Vellozia; OG0000027, com anotação de domínio móvel de plantas/proteína não caracterizada, com mudança +50 no ramo terminal de V. peripherica; e OG0000024, anotada como família citocromo P450, com mudança −15 no mesmo ramo terminal. Barras representam contagens observadas; mudanças são reconstruções de k=2, rep01. Cada painel tem escala vertical própria. As descrições foram recuperadas da tabela EggNOG atual e não estabelecem a função de cada cópia.

**Critérios de seleção:** Pertencer ao consenso; ter anotação recuperada; representar uma expansão ancestral, uma expansão terminal e uma contração terminal. São exemplos ilustrativos escolhidos por padrão, não os resultados de uma classificação funcional ou de um ranking de importância. Não se presume que OG0000027 represente ganho de função: sua anotação de domínio móvel exige atenção à natureza dos elementos. A classificação atual não marca essas três famílias como organelares ou transposons, mas essa classificação não substitui validação das sequências. A seleção e as contagens constam de `figure_current_family_examples_selection.tsv`.

**Significado biológico:** Uma mudança positiva representa aumento estimado do repertório de cópias naquele ramo; uma mudança negativa representa redução. Alteração de dosagem, redundância e diferenciação funcional são hipóteses possíveis, não conclusões demonstradas pelas contagens. Zero na matriz tampouco estabelece perda biológica sem avaliar completude e anotação dos genomas. A figura não contém localização genômica: esse vínculo não foi validado para esses exemplos.

## Reprodução e rastreabilidade

Gerador: `docs/scripts/plot_lineage_family_profiles.py`.

Fontes: `04_gene_families/comparative_axes/comparative_families_master_table_v2.tsv` e `03_dating/mcmctree_high_ess_convergence_summary.tsv`. O arquivo `lineage_family_profiles_manifest.json` registra hashes das fontes e as escolhas de transformação e reconstrução. Os totais por ramo estão em `figure_current_dated_family_changes_counts.tsv`.

Validação: tamanhos dos conjuntos verificados (196/58), três exemplos conferidos na tabela atual, formatos exportados e inspeção visual das figuras. Os resultados de CAFE e as cadeias de datação foram preservados.
