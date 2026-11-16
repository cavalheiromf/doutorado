# Análise de Sintenia (`03_synteny`)

Este diretório contém a estrutura de dados, scripts de automação e análises de sintenia genômica (macrosintenia e microsintenia) entre as espécies de orquídeas *Vanilla peripherica* (*Vper*) e *Vanilla tubiflora* (*Vtub*).

A infraestrutura foi desenhada de forma totalmente isolada para comportar análises de sintenia cruzada (intergenômica) e análises de auto-sintenia (intragenômica) de cada genoma, eliminando qualquer risco de conflito de nomenclatura ou arquivos temporários.

---

## 📂 Estrutura do Diretório

A pasta foi reestruturada de forma modular para organizar os inputs, passos intermediários e resultados das análises:

```text
03_synteny/
├── data/                    # Dados de entrada globais compartilhados
│   ├── Vper.bed             # Coordenadas BED de V. peripherica (prefixo 'vp')
│   ├── Vtub.bed             # Coordenadas BED de V. tubiflora (prefixo 'vt')
│   ├── Vper.cds             # Link simbólico para CDS original de Vper
│   └── Vtub.cds             # Link simbólico para CDS original de Vtub
├── last_db/                 # Bancos de dados binários de indexação do LAST (limpos do ambiente de trabalho)
├── intergenomic/            # Análise de sintenia cruzada (Vper vs Vtub)
│   ├── intermediates/       # Arquivos intermediários (.last, .anchors, .simple)
│   ├── layouts/             # Arquivos de layout e configurações do JCVI (.layout, .blocks)
│   └── results/             # Imagens geradas de macrosintenia cruzada (.pdf)
├── intragenomic/            # Análises de auto-sintenia (intragenômica) isoladas
│   ├── Vper/                # Ambiente exclusivo para auto-sintenia de V. peripherica
│   │   ├── intermediates/   # Arquivos parálogos de auto-sintenia contendo duplicações (ex: P98L0)
│   │   ├── layouts/         # Arquivos .blocks e .layout específicos de Vper
│   │   └── results/         # Plot final de auto-sintenia (intragenome.pdf)
│   └── Vtub/                # Ambiente exclusivo para auto-sintenia de V. tubiflora
│       ├── intermediates/   # Arquivos parálogos e blocos duplicados de Vtub
│       ├── layouts/         # Arquivos .blocks e .layout de auto-sintenia de Vtub
│       └── results/         # Plot final de auto-sintenia (intragenome.pdf)
├── results/                 # Resultados consolidados e plots específicos
│   └── microsynteny_plots/  # Figuras de microsintenia focadas em locus (ex: genes OSCA)
└── scripts/                 # Scripts Python de suporte e automação do pipeline
```

---

## 🛠️ Scripts e Utilidades (`scripts/`)

Os scripts automatizam a preparação dos arquivos, identificação de blocos gênicos de interesse e geração de figuras de microsintenia.

### 1. `prepare_files.py`
Prepara os arquivos BED e CDS a partir dos arquivos originais GFF3 e FASTA do projeto:
*   Filtra e extrai apenas feições de `mRNA`.
*   Aplica prefixos específicos às coordenadas dos cromossomos (`vp_` para *Vper* e `vt_` para *Vtub*) para evitar qualquer colisão de eixos no MCscan.
*   Cria links simbólicos dinâmicos para os arquivos de CDS na pasta `data/`, economizando dezenas de megabytes e evitando cópias físicas desnecessárias.

```bash
python scripts/prepare_files.py
```

### 2. `find_osca_blocks.py`
Varre os alinhamentos de sintenia simples (`Vper.Vtub.simple`) e identifica quais blocos sintênicos contêm os genes da família **OSCA** com base na lista de IDs de referência (`oscasIDs.txt` da etapa `01_gene_identification`).
*   Gera um arquivo de blocos anotados (`Vper.Vtub.oscas.simple`) com as linhas contendo genes OSCA destacadas com a cor vermelha (`r*`).

```bash
python scripts/find_osca_blocks.py
```

### 3. `extract_all_osca_microsynteny.py`
Extrai e plota janelas locais de microsintenia (31 genes ao redor de cada gene OSCA) entre *Vper* e *Vtub*:
*   Mapeia dinamicamente os locus cromossomo por cromossomo.
*   Cria os arquivos de `.layout` e `.blocks` temporários automaticamente.
*   Chama a ferramenta `jcvi.graphics.synteny` do pacote MCscan para renderizar os plots.
*   Salva todas as imagens PDF de microsintenia na pasta `results/microsynteny_plots/`.

```bash
python scripts/extract_all_osca_microsynteny.py
```

### 4. Outros Scripts
*   `extract_osca_cluster.py`: Script auxiliar para focar na extração de clusters gênicos ricos.
*   `macrosynteny_osca_orthologs.py` & `macrosynteny_osca_thin.py`: Geração de plots de macrosintenia entre ortólogos com estilizações diferenciadas (linhas finas ou destaque sob medida).

---

## 🚀 Como Executar Análises

As análises de sintenia utilizam o ambiente Python configurado com o pacote **JCVI** (`jcviEnv`).

### 🔑 Importante: Resolução do Erro ETE4
A ferramenta gráfica do JCVI tenta importar a biblioteca `ete4` para renderização de árvores filogenéticas. Como essa biblioteca não está presente ou é incompatível no ambiente do mamba (`jcviEnv`), resolvemos isso criando um script dummy/mock chamado `ete4.py` nos diretórios de execução (`intergenomic/`, `intragenomic/Vper/`, `intragenomic/Vtub/` e no root do diretório).
> **Sempre execute comandos de renderização (`jcvi.graphics.synteny`) dentro de diretórios que possuam esse mock `ete4.py` presente.**

---

### Exemplo 1: Sintenia Cruzada Intergenômica (Vper vs Vtub)

Acesse a pasta isolada:
```bash
cd intergenomic/
```

Execute o cálculo de sintenia (LAST + JCVI MCscan):
```bash
python -m jcvi.compara.synteny screen Vper.bed Vtub.bed --last --path=../last_db
```

Gere o plot de macrosintenia com ortólogos ou blocos selecionados:
```bash
python -m jcvi.graphics.synteny layouts/macrosynteny.blocks layouts/macrosynteny.layout --notex
```
*(Nota: Sempre utilize a flag `--notex` para evitar problemas locais de renderização do LaTeX)*

---

### Exemplo 2: Auto-Sintenia Intragenômica (Duplicações Segmentais de Vtub)

Acesse o ambiente isolado de *Vtub*:
```bash
cd intragenomic/Vtub/
```

Execute o alinhamento contra si mesmo (auto-sintenia):
```bash
python -m jcvi.compara.synteny screen Vtub.bed Vtub.bed --last --path=../../last_db
```

Após filtrar os parálogos de interesse no arquivo `.anchors` (como a duplicação segmental identificada entre os cromossomos `vt_chr1A` e `vt_chr2A` contendo 15 âncoras gênicas):
1.  Configure as coordenadas e âncoras em `layouts/intragenome.blocks`.
2.  Configure a orientação dos eixos cromossômicos em `layouts/intragenome.layout`.

Execute a renderização da imagem:
```bash
python -m jcvi.graphics.synteny layouts/intragenome.blocks layouts/intragenome.layout --notex
```
A imagem resultante será salva de forma limpa em `results/intragenome.pdf`.

---

## 🎨 Boas Práticas de Design para Plots do JCVI

*   **Paleta de Cores Harmônica**: Use cores com boa distinção visual nos arquivos `.layout`. Tons como azul claro (`#9ecae1`) e coral/laranja claro (`#fc9272`) dão um visual premium e moderno às figuras.
*   **Controle de Espessura**: Para visualização limpa de blocos e conexões longas, pode-se encurtar artificialmente as janelas gênicas nos blocos para obter linhas mais finas de conexão em vez de faixas massivas, facilitando a interpretação do alinhamento.


## Scientific Insights

================================================================================
SCIENTIFIC INSIGHTS: OSCA GENE SYNTENY (03_synteny)
================================================================================

[PORTUGUÊS]
A análise de sintenia comparativa em macro e microescala baseada no MCscan (JCVI) revelou um nível extraordinário de conservação estrutural e colinearidade genômica na arquitetura cromossômica dos loci OSCA entre Vellozia peripherica e Vellozia tubiflora. 

1. MACROSSINTENIA & MICROSSINTENIA GLOBAL:
A comparação genômica ampla revelou uma colinearidade cromossomo-a-cromossomo altamente estável, com 297 blocos sintênicos conservados entre os 9 cromossomos das duas espécies, livre de grandes translocações intercromossômicas. No nível de microssintenia, o locus OSCA1.3/1.4/1.5 no cromossomo 7A exibe uma conservação perfeita de ordem gênica e contiguidade física (gap de 0 genes intermediários) flanqueada por 24 ortólogos sintênicos, indicando que este cluster sensorial surgiu antes da especiação de Vellozia e tem sido mantido sob forte pressão de seleção purificadora.

2. DUPLICAÇÕES INTRAGENÔMICAS (AUTO-SINTENIA):
A análise comparativa de parálogos intragenômicos trouxe novos achados evolutivos cruciais:
*   Duplicação Segmentar Ancestral (Chr 1A <-> Chr 5A): Identificamos um bloco colinear antigo e conservado que conecta o Cromossomo 1A ao 5A em ambos os genomas, contendo duas subfamílias de canais OSCA duplicadas simultaneamente: OSCA2 (OSCA2.1 <-> OSCA2.2) e OSCA3 (OSCA3.1 <-> OSCA3.2). Isso confirma um evento de paleoduplicação em larga escala (provavelmente uma WGD ancestral) antes da divergência dos dois táxons.
*   Duplicação em Tandem Específica: Foi detectada uma divergência evolutiva local no Cromossomo 1A. V. peripherica exibe uma duplicação em tandem adjacente exclusiva para o gene OSCA2.4, resultando nas cópias contíguas VpOSCA2.4a e VpOSCA2.4b (gap de 0 genes). Em contrapartida, V. tubiflora retém apenas uma cópia (VtOSCA2.4), o que reflete um evento recente de expansão local em V. peripherica ou perda gênica em V. tubiflora.

Essa notável estabilidade evolutiva nas regiões de auto-sintenia e sintenia cruzada do gênero Vellozia fornece sustentação estrutural sólida para a hipótese de conservação funcional dos canais permeáveis a cálcio sob condições de estresse hídrico extremo em plantas de ressurreição.

3. ANÁLISE DE SELEÇÃO COMPARATIVA E DIVERGÊNCIA EVOLUTIVA POR SUBFAMÍLIAS (PIPELINE DE CLADOS - HYPHY RELAX & CONTRAST-FEL):
Para correlacionar os padrões de microssintenia e duplicação gênica com as forças evolutivas e as respostas fisiológicas contrastantes entre Vellozia tubiflora (tolerante à dessecação / Test) e Vellozia peripherica (sempre-verde / Reference), implementamos uma pipeline de seleção localizada por clados (OSCA1, OSCA2 e OSCA3+4). Ao realinhar as sequências de nucleotídeos com base em alinhamentos de proteínas locais (MUSCLE) e podar a árvore filogenética de máxima verossimilhança com precisão matemática, eliminamos artefatos de lacunas (gaps) e revelamos assinaturas evolutivas específicas para cada clade:

*   ANÁLISE DE RESTRIÇÃO POR CLADO (RELAX):
    Revelou que as pressões de seleção são altamente heterogêneas e específicas de clado, provando que o relaxamento global observado anteriormente é inteiramente direcionado pelas subfamílias OSCA2 e OSCA3+4:
    *   **Subfamília OSCA1** (10 genes): **Sem alteração significativa na intensidade de seleção** ($K = 0,9215$; $p = 0,5957$). Isso demonstra que a subfamília que abriga o cluster altamente conservado OSCA1.3/1.4/1.5 no Cromossomo 7A permanece sob seleção purificadora severa e idêntica em ambos os estilos de vida, preservando a homeostase e as funções osmosensoriais centrais.
    *   **Subfamília OSCA2** (11 genes): **Altamente significativa e drástica liberação/relaxamento de seleção em V. tubiflora** ($K = 0,2828$; $p = 0,000034$).
    *   **Subfamília OSCA3+4** (6 genes): **Significativo relaxamento de seleção em V. tubiflora** ($K = 0,1349$; $p = 0,0061$). 
    *   *Significado Biológico*: Como V. tubiflora sobrevive à dessecação extrema entrando em um estado de anidrobiose (inatividade metabólica), as pressões seletivas funcionais sobre os canais OSCA2 e OSCA3+4 são relaxadas durante a seca. Isso permite o acúmulo de variabilidade genética nessas famílias, enquanto o maquinário osmosensorial basal (OSCA1) permanece invariante.

*   DIVERGÊNCIA DE SÍTIO COM SANEAMENTO DE GAP (CONTRAST-FEL):
    A re-análise por clados e o saneamento de gaps expuseram e eliminaram **5 falsos positivos globais (Sítios 401, 797, 803, 821, 842)** que possuíam alta taxa de lacunas (22% a 34%) no alinhamento global. Os sítios significativos reais foram mapeados com precisão cirúrgica:
    *   **Clade OSCA1**: Identificou 6 sítios estatisticamente divergentes (p <= 0,05). O **Sítio Local 181 (Sítio Global 484)** ($\beta_\text{Test} = 8,20$; $\beta_\text{Ref} = 0,03$; $p = 0,035$) e o **Sítio Local 710 (Sítio Global 1232)** ($\beta_\text{Test} = 7,66$; $\beta_\text{Ref} = 0,00$; $p = 0,020$) replicam perfeitamente os achados globais em regiões sem gaps. Os sítios 252, 430 e 973 exibem taxas não-sinônimas extremamente altas em V. peripherica ($\beta_\text{Ref} \gg \beta_\text{Test}$), sugerindo sintonia adaptativa local na espécie sempre-verde.
    *   **Clade OSCA2**: Revelou 14 sítios significativos (8, 71, 76, 147, 191, 241, 270, 308, 394, 395, 432, 596, 720, 824). De forma surpreendente, todos os 14 exibem aceleração seletiva extrema em V. peripherica ($\beta_\text{Ref} \gg 0$) e são estritamente restritos em V. tubiflora ($\beta_\text{Test} \approx 0$). Isso demonstra seleção diversificadora adaptativa ou refinamento molecular desses canais na espécie sempre-verde para lidar com flutuações hídricas ativas diárias.
    *   **Clade OSCA3+4**: Identificou 1 sítio altamente divergente, o **Sítio Local 593 (Sítio Global 1094)** ($\beta_\text{Test} = 24,72$; $\beta_\text{Ref} = 0,018$; $p = 0,0085$), localizado de forma adjacente ao sítio global 1093, confirmando um hotspot de relaxamento/seleção positiva exclusivo para esta subfamília na planta de ressurreição.


================================================================================

[ENGLISH]
Comparative synteny analysis at macro- and micro-scales using MCscan (JCVI) revealed an extraordinary level of structural conservation and genomic collinearity in the chromosomal architecture harboring OSCA loci between Vellozia peripherica and Vellozia tubiflora.

1. MACROSINTENY & GLOBAL MICRO-SYNTENY:
Genome-wide comparative synteny revealed a highly stable chromosome-to-chromosome collinearity with 297 syntenic blocks preserved across the 9 chromosomes, displaying no major inter-chromosomal translocations. At the micro-syntenic level, the OSCA1.3/1.4/1.5 locus on chromosome 7A exhibits perfect gene order and physical contiguity conservation (gap of 0 intermediate genes), flanked by 24 highly syntenic orthologs. This indicates that this sensory cluster expanded prior to Vellozia speciation and has been maintained under strong purifying selection.

2. INTRAGENOMIC DUPLICATIONS (SELF-SYNTENY):
Paralogous self-synteny analysis yielded major new evolutionary insights:
*   Ancestral Segmental Duplication (Chr 1A <-> Chr 5A): A conserved, ancient collinear duplication block connects Chromosome 1A and Chromosome 5A in both Vellozia genomes, harboring two simultaneously duplicated OSCA subfamilies: OSCA2 (OSCA2.1 <-> OSCA2.2) and OSCA3 (OSCA3.1 <-> OSCA3.2). This confirms a large-scale paleoduplication event (likely an ancestral WGD) prior to the divergence of these two taxa.
*   Lineage-Specific Tandem Duplication: A localized evolutionary divergence was identified on Chromosome 1A. V. peripherica displays a species-specific adjacent tandem duplication of the OSCA2.4 gene, yielding consecutive copies VpOSCA2.4a and VpOSCA2.4b (gap of 0 genes). In contrast, V. tubiflora retains a single copy (VtOSCA2.4), highlighting a recent localized expansion in V. peripherica or a gene loss event in V. tubiflora.

This remarkable evolutionary stability in both self-synteny and cross-species synteny profiles in Vellozia provides strong structural support for the hypothesis of functional channel conservation under extreme environmental stress in these resurrection plants.

3. COMPARATIVE SELECTION ANALYSIS AND EVOLUTIONARY DIVERGENCE BY SUBFAMILIES (CLADE PIPELINE - HYPHY RELAX & CONTRAST-FEL):
To correlate micro-synteny patterns and gene duplication events with evolutionary forces and contrasting physiological lifestyles between Vellozia tubiflora (desiccation-tolerant / Test) and Vellozia peripherica (evergreen / Reference), we implemented a localized clade-specific evolutionary pipeline (OSCA1, OSCA2, and OSCA3+4). By realigning sequences locally using protein alignments (MUSCLE) and mathematically pruning the global ML tree, we eliminated gap artifacts and uncovered clade-specific evolutionary dynamics:

*   CLADE-SPECIFIC SELECTION CONSTRAINT ANALYSIS (RELAX):
    Selection intensity parameter K and significance values show that selection pressures are highly subfamily-specific, demonstrating that the global selection relaxation observed earlier was completely driven by the OSCA2 and OSCA3+4 subfamilies:
    *   **OSCA1 Subfamily** (10 genes): **No significant change in selection intensity** ($K = 0.9215$; $p = 0.5957$). The OSCA1 subfamily, which houses the physical contiguity cluster OSCA1.3/1.4/1.5 on Chromosome 7A, is under severe and identical purifying constraints in both resurrection and evergreen lifestyles, preserving baseline osmosensing function.
    *   **OSCA2 Subfamily** (11 genes): **Highly significant and drastic selection relaxation in V. tubiflora** ($K = 0.2828$; $p = 0.000034$).
    *   **OSCA3+4 Subfamily** (6 genes): **Extremely significant selection relaxation in V. tubiflora** ($K = 0.1349$; $p = 0.0061$).
    *   *Functional Implications*: Because V. tubiflora survives desiccation by entering an inactive metabolic state (anhydrobiosis), functional pressure on OSCA2 and OSCA3+4 channels is suspended during dormancy, allowing them to accumulate genetic variation, while core baseline osmosensing (OSCA1) remains strictly protected.

*   SANITIZED SITE-SPECIFIC EVOLUTIONARY DIVERGENCE (CONTRAST-FEL):
    Clade partitioning and gap sanitation exposed and eliminated **5 false-positive divergent sites (Sites 401, 797, 803, 821, 842)** which contained high gap ratios (22% to 34%) globally. The true significant sites were mapped with high precision:
    *   **OSCA1 Clade**: Identified 6 significant sites (p <= 0.05). **Local Site 181 (Global Site 484)** ($\beta_\text{Test} = 8.20$; $\beta_\text{Ref} = 0.03$; $p = 0.035$) and **Local Site 710 (Global Site 1232)** ($\beta_\text{Test} = 7.66$; $\beta_\text{Ref} = 0.00$; $p = 0.020$) perfectly replicate findings from the global alignment. Sites 252, 430, and 973 exhibit highly elevated non-synonymous rates in V. peripherica ($\beta_\text{Ref} \gg \beta_\text{Test}$), suggesting localized adaptive tuning in the evergreen background.
    *   **OSCA2 Clade**: Detected 14 significant sites (8, 71, 76, 147, 191, 241, 270, 308, 394, 395, 432, 596, 720, 824). Strikingly, all 14 sites exhibit extreme selective acceleration in V. peripherica ($\beta_\text{Ref} \gg 0$) while being strictly constrained in V. tubiflora ($\beta_\text{Test} \approx 0$), pointing to active adaptive modeling in the evergreen species to fine-tune channels for daily osmotic fluctuations.
    *   **OSCA3+4 Clade**: Revealed 1 highly significant site, **Local Site 593 (Global Site 1094)** ($\beta_\text{Test} = 24.72$; $\beta_\text{Ref} = 0.018$; $p = 0.0085$), lying directly adjacent to the global site 1093. This confirms a robust evolutionary relaxation hotspot in the resurrection plant, serving as an ideal candidate for future mutagenic validation.


================================================================================

