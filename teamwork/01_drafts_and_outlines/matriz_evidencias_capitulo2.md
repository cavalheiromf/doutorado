# MATRIZ DE EVIDÊNCIAS EMPÍRICAS — CAPÍTULO 2
## Arquitetura Genômica, Sintenia Comparativa e Dinâmica Evolutiva da Família OSCA em *Vellozia tubiflora* e *Vellozia peripherica*

**Tese de Doutorado:** Bases Genômicas e Regulatórias da Adaptação à Seca em Velloziaceae  
**Doutoranda:** Mariana Feitosa Cavalheiro  
**Orientadora:** Profa. Dra. Isabel Rodrigues Gerhardt  
**Instituição:** Instituto de Biologia — Universidade Estadual de Campinas (UNICAMP)  

---

### 1. PANORAMA GERAL DO ESTUDO E HIPÓTESE CENTRAL

* **Pergunta Biológica Central:** Como os regimes adaptativos divergentes entre a planta de ressurreição tolerante à dessecação (*Vellozia tubiflora*) e a espécie sensível e sempre-verde (*Vellozia peripherica*) moldaram o repertório, a conservação estrutural, as taxas de evolução molecular e as redes de interação dos canais mecanossensíveis permeáveis a cálcio ativados por hiperosmolalidade (**OSCA**)?
* **Hipótese Mecanística — *Dual-Track Evolutionary Model*:**
  1. **Trilha Conservada (Clado OSCA1):** Evolui sob estrita e invariante seleção purificadora ($K = 0,9215; p = 0,5957$), mantendo conectividade de rede central e papéis essenciais e basais no osmosensoriamento radicular e vascular.
  2. **Trilha Divergente/Modulatória (Clados OSCA2 e OSCA3+4):** Exibe relaxamento seletivo drástico e altamente significativo na especialista em ressurreição *V. tubiflora* ($K = 0,2828; p = 3,4 \times 10^{-5}$ em OSCA2 e $K = 0,1349; p = 0,0061$ em OSCA3+4), decorrente da quiescência metabólica e anidrobiose durante a dessecação extrema. Em contrapartida, *V. peripherica* apresenta diversificação ativa desses canais (14 sítios de aminoácidos sob forte aceleração seletiva em Contrast-FEL no Clado OSCA2 e duplicação em tandem recente de *VpOSCA2.4a/b*), fornecendo plasticidade para ajustes dinâmicos frente a flutuações hídricas diárias.

---

### 2. REPERTÓRIO GÊNICO E ARQUITETURA ESTRUTURAL DA FAMÍLIA OSCA

Buscas genômicas estruturadas com modelos ocultos de Markov (HMMER v3.4) utilizando os perfis Pfam característicos (PF02714, PF13967 e PF14703) e validação de domínios no InterProScan v5.62 (PANTHER PTHR13018) mapearam 14 genes em *Vellozia peripherica* (haplotipo hapA) e 13 genes em *Vellozia tubiflora* (hapA).

#### Tabela 1: Caracterização Genômica e Topologia Estrutural dos Canais OSCA em *Vellozia*

| Espécie | Nome do Gene | ID do Locus | Clado | Cromossomo | Início (pb) | Fim (pb) | Fita | Comprimento (aa) | MW (kDa) | Domínios Pfam Detectados |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| *V. peripherica* | *VpOSCA1.1* | `Vper.hapA.v1.chr4A.g118180.t1` | OSCA1 | chr4A | 11.237.808 | 11.254.982 | - | 774 | 88,5 | PF13967 (7–179), PF14703 (287–416), PF02714 (427–699) |
| *V. peripherica* | *VpOSCA1.2* | `Vper.hapA.v1.chr9A.g255900.t1` | OSCA1 | chr9A | 17.564.347 | 17.578.689 | - | 768 | 87,9 | PF13967 (9–177), PF14703 (236–395), PF02714 (406–678) |
| *V. peripherica* | *VpOSCA1.3* | `Vper.hapA.v1.chr7A.g179370.t1` | OSCA1 | chr7A | 1.154.964 | 1.162.617 | + | 761 | 86,8 | PF13967 (7–178), PF14703 (199–361), PF02714 (372–649) |
| *V. peripherica* | *VpOSCA1.4* | `Vper.hapA.v1.chr7A.g179380.t1` | OSCA1 | chr7A | 1.165.818 | 1.173.766 | + | 759 | 86,4 | PF13967 (7–174), PF14703 (233–316), PF02714 (327–600) |
| *V. peripherica* | *VpOSCA1.5* | `Vper.hapA.v1.chr7A.g179390.t1` | OSCA1 | chr7A | 1.190.163 | 1.199.238 | + | 763 | 87,1 | PF13967 (9–180), PF14703 (201–363), PF02714 (374–672) |
| *V. peripherica* | *VpOSCA2.1* | `Vper.hapA.v1.chr5A.g140750.t1` | OSCA2 | chr5A | 1.645.547 | 1.653.691 | + | 739 | 84,6 | PF13967 (6–165), PF14703 (186–342), PF02714 (353–586) |
| *V. peripherica* | *VpOSCA2.2* | `Vper.hapA.v1.chr1A.g021690.t1` | OSCA2 | chr1A | 21.367.423 | 21.371.278 | - | 742 | 85,1 | PF14703 (29–72), PF02714 (83–334) |
| *V. peripherica* | *VpOSCA2.3* | `Vper.hapA.v1.chr1A.g013600.t1` | OSCA2 | chr1A | 13.332.252 | 13.336.746 | + | 745 | 85,3 | PF13967 (5–165), PF14703 (186–345), PF02714 (356–622) |
| *V. peripherica* | *VpOSCA2.4a* | `Vper.hapA.v1.chr1A.g023030.t1` | OSCA2 | chr1A | 22.689.052 | 22.697.439 | + | 738 | 84,2 | PF13967 (5–168), PF14703 (189–281), PF02714 (294–558) |
| *V. peripherica* | *VpOSCA2.4b* | `Vper.hapA.v1.chr1A.g023020.t1` | OSCA2 | chr1A | 22.678.816 | 22.687.760 | + | 740 | 84,7 | PF13967 (5–168), PF14703 (239–281), PF02714 (294–581) |
| *V. peripherica* | *VpOSCA2.5* | `Vper.hapA.v1.chr9A.g257040.t1` | OSCA2 | chr9A | 18.576.254 | 18.590.260 | - | 736 | 84,0 | PF13967 (10–154), PF14703 (216–263), PF02714 (275–542) |
| *V. peripherica* | *VpOSCA3.1* | `Vper.hapA.v1.chr1A.g020450.t1` | OSCA3 | chr1A | 20.008.265 | 20.014.313 | + | 722 | 82,4 | PF13967 (5–166), PF14703 (188–355), PF02714 (367–637) |
| *V. peripherica* | *VpOSCA3.2* | `Vper.hapA.v1.chr5A.g142080.t1` | OSCA3 | chr5A | 2.668.389 | 2.675.373 | - | 726 | 82,9 | PF13967 (5–166), PF14703 (188–355), PF02714 (366–636) |
| *V. peripherica* | *VpOSCA4.1* | `Vper.hapA.v1.chr8A.g231320.t1` | OSCA4 | chr8A | 20.598.462 | 20.602.234 | - | 715 | 81,6 | PF13967 (75–174), PF14703 (199–388), PF02714 (399–735) |
| *V. tubiflora* | *VtOSCA1.1* | `Vtub.hapA.v1.chr4A.g106800.t1` | OSCA1 | chr4A | 10.819.227 | 10.835.638 | - | 772 | 88,3 | PF13967 (7–179), PF14703 (200–362), PF02714 (373–645) |
| *V. tubiflora* | *VtOSCA1.2* | `Vtub.hapA.v1.chr9A.g230740.t1` | OSCA1 | chr9A | 17.719.979 | 17.728.315 | - | 766 | 87,6 | PF14703 (21–85), PF02714 (96–368) |
| *V. tubiflora* | *VtOSCA1.3* | `Vtub.hapA.v1.chr7A.g166590.t1` | OSCA1 | chr7A | 1.018.480 | 1.027.560 | + | 760 | 86,7 | PF13967 (7–201), PF14703 (222–384), PF02714 (395–680) |
| *V. tubiflora* | *VtOSCA1.4* | `Vtub.hapA.v1.chr7A.g166600.t1` | OSCA1 | chr7A | 1.029.792 | 1.039.945 | + | 758 | 86,3 | PF13967 (54–225), PF14703 (246–410), PF02714 (421–692) |
| *V. tubiflora* | *VtOSCA1.5* | `Vtub.hapA.v1.chr7A.g166610.t1` | OSCA1 | chr7A | 1.049.541 | 1.057.767 | + | 762 | 87,0 | PF13967 (10–180), PF14703 (201–363), PF02714 (374–651) |
| *V. tubiflora* | *VtOSCA2.1* | `Vtub.hapA.v1.chr5A.g127830.t1` | OSCA2 | chr5A | 1.496.336 | 1.503.868 | + | 738 | 84,5 | PF13967 (6–165), PF14703 (203–283), PF02714 (294–531) |
| *V. tubiflora* | *VtOSCA2.2* | `Vtub.hapA.v1.chr1A.g019410.t1` | OSCA2 | chr1A | 20.232.004 | 20.238.727 | - | 741 | 85,0 | PF13967 (6–146), PF14703 (167–324), PF02714 (335–601) |
| *V. tubiflora* | *VtOSCA2.3* | `Vtub.hapA.v1.chr1A.g012080.t1` | OSCA2 | chr1A | 12.783.202 | 12.787.679 | + | 744 | 85,2 | PF13967 (5–165), PF14703 (186–345), PF02714 (356–622) |
| *V. tubiflora* | *VtOSCA2.4* | `Vtub.hapA.v1.chr1A.g020650.t1` | OSCA2 | chr1A | 21.645.212 | 21.654.612 | + | 739 | 84,4 | PF13967 (5–168), PF14703 (189–281), PF02714 (294–651) |
| *V. tubiflora* | *VtOSCA2.5* | `Vtub.hapA.v1.chr9A.g231910.t1` | OSCA2 | chr9A | 18.668.636 | 18.684.281 | - | 735 | 83,9 | PF13967 (10–152), PF14703 (214–261), PF02714 (273–540) |
| *V. tubiflora* | *VtOSCA3.1* | `Vtub.hapA.v1.chr1A.g018250.t1` | OSCA3 | chr1A | 18.922.458 | 18.928.500 | + | 721 | 82,3 | PF13967 (5–166), PF14703 (188–355), PF02714 (367–636) |
| *V. tubiflora* | *VtOSCA3.2* | `Vtub.hapA.v1.chr5A.g129040.t1` | OSCA3 | chr5A | 2.457.574 | 2.466.320 | - | 725 | 82,8 | PF13967 (5–166), PF14703 (271–394), PF02714 (405–675) |
| *V. tubiflora* | *VtOSCA4.1* | `Vtub.hapA.v1.chr8A.g207990.t1` | OSCA4 | chr8A | 24.477.668 | 24.481.020 | - | 714 | 81,5 | PF13967 (75–174), PF14703 (199–388), PF02714 (399–735) |

---

### 3. FILOGENIA E CLASSIFICAÇÃO NOS QUATRO CLADOS EVOLUTIVOS

Reconstrução filogenética por Máxima Verossimilhança (IQ-TREE v2.4.0, alinhamento MAFFT L-INS-i / trimAl `-automated1`, modelo Q.plant+F+R5) com 1.000 réplicas de Ultrafast Bootstrap (UFBoot2) e SH-aLRT:

* **Distribuição por Clados:**
  * **Clado OSCA1 (5 pares ortólogos):** *OSCA1.1* (chr4A), *OSCA1.2* (chr9A), *OSCA1.3* (chr7A), *OSCA1.4* (chr7A), *OSCA1.5* (chr7A).
  * **Clado OSCA2 (Mais abundante — 6 genes em *Vper* / 5 em *Vtub*):** *OSCA2.1* (chr5A), *OSCA2.2* (chr1A), *OSCA2.3* (chr1A), *OSCA2.4a/b* (*Vper*) vs *OSCA2.4* (*Vtub*) (chr1A), *OSCA2.5* (chr9A).
  * **Clado OSCA3 (2 pares ortólogos):** *OSCA3.1* (chr1A) e *OSCA3.2* (chr5A).
  * **Clado OSCA4 (1 par ortólogo basal):** *OSCA4.1* (chr8A).
* **Resolução do Nó *OSCA2.4*:**
  * Nó de agrupamento *OSCA2.4* monofilético (*VpOSCA2.4a* + *VpOSCA2.4b* + *VtOSCA2.4*): **100% de suporte UFBoot**.
  * Relação cruzada *VpOSCA2.4b* com *VtOSCA2.4*: **83% de suporte**, confirmando a divergência ortóloga ancestral e a posterior duplicação em tandem de *VpOSCA2.4a* na linhagem de *V. peripherica*.

---

### 4. SINTENIA CROMOSSÔMICA, PALEODUPLICAÇÕES E MICROSSINTENIA

A reconstrução de sintenia comparativa (MCScan / JCVI) identificou 297 blocos sintênicos conservados entre os genomas de *V. peripherica* e *V. tubiflora*, demonstrando total colinearidade nos 9 cromossomos ($2n = 18$).

#### Tabela 2: Padrões de Sintenia e Mecanismos de Duplicação dos Canais OSCA

| Locus / Cluster | Cromossomo | Tipo de Duplicação | Conservação Estrutural e Arquitetura Genômica |
| :--- | :---: | :---: | :--- |
| *OSCA1.3 / 1.4 / 1.5* | chr7A | **Tandem Antigo** (Pré-especiação) | Cluster contíguo com **gap de 0 genes intermediários** em ambas as espécies, flanqueado por 24 ortólogos colineares conservados. |
| *OSCA2.1 <-> OSCA2.2* | chr5A $\leftrightarrow$ chr1A | **WGD / Segmentar Ancestral** | Bloco de paleoduplicação intercromossômico unindo chr1A e chr5A, duplicando simultaneamente loci do Clado 2. |
| *OSCA3.1 <-> OSCA3.2* | chr1A $\leftrightarrow$ chr5A | **WGD / Segmentar Ancestral** | Mesma paleoduplicação segmentar ancestral (chr1A $\leftrightarrow$ chr5A), duplicando simultaneamente loci do Clado 3. |
| *VpOSCA2.4a / 2.4b* | chr1A | **Tandem Recente** (Linhagem-específico) | Duplicação tandem contígua exclusiva de *V. peripherica* (gap = 0 genes; distância intergênica de 1.292 pb). *V. tubiflora* retém cópia única (*VtOSCA2.4*). |
| *OSCA1.1, 1.2, 2.5, 4.1* | chr4A, chr9A, chr9A, chr8A | **Sintenia 1:1 Estrita** | Inseridos em blocos macrosintênicos estáveis sem eventos de duplicação local. |

---

### 5. MODELAGEM DE TAXAS EVOLUTIVAS MOLECULARES E SELEÇÃO HYPHY

Estimativas de taxas de substituição não-sinônima ($Ka$), sinônima ($Ks$) e razão de seleção $\omega = Ka/Ks$ calculadas via PAML v4.9 (`codeml` modelo pairwise) e validadas por `PAL2NAL yn00`:

#### Tabela 3: Métricas de Evolução Molecular Pareada ($Ka/Ks$) para os Loci OSCA

| Par de Genes Analisado | $Ks$ (`codeml`) | $Ka$ (`codeml`) | $\omega = Ka/Ks$ | Pressão de Seleção Observada |
| :--- | :---: | :---: | :---: | :--- |
| *VpOSCA1.1* $\leftrightarrow$ *VtOSCA1.1* | 0,0429 | 0,0120 | **0,2794** | Seleção Purificadora Severa |
| *VpOSCA1.2* $\leftrightarrow$ *VtOSCA1.2* | 0,1114 | 0,0397 | **0,3560** | Seleção Purificadora Estrita |
| *VpOSCA1.3* $\leftrightarrow$ *VtOSCA1.3* | 0,0795 | 0,0230 | **0,2889** | Seleção Purificadora Estrita |
| *VpOSCA1.4* $\leftrightarrow$ *VtOSCA1.4* | 0,1209 | 0,0867 | **0,7172** | Relaxamento Seletivo / Taxa Acelerada no Cluster Tandem |
| *VpOSCA1.5* $\leftrightarrow$ *VtOSCA1.5* | 0,1035 | 0,0687 | **0,6638** | Divergência Moderada no Cluster Tandem |
| *VpOSCA2.1* $\leftrightarrow$ *VtOSCA2.1* | 0,0784 | 0,0225 | **0,2870** | Seleção Purificadora Estrita |
| *VpOSCA2.2* $\leftrightarrow$ *VtOSCA2.2* | 0,0992 | 0,0626 | **0,6317** | Relaxamento Pós-Paleoduplicação |
| *VpOSCA2.3* $\leftrightarrow$ *VtOSCA2.3* | 0,0886 | 0,0046 | **0,0518** | **Seleção Purificadora Mais Extrema da Família** |
| *VpOSCA2.4a* $\leftrightarrow$ *VpOSCA2.4b* | 0,1228 | 0,0443 | **0,3606** | Parálogo Tandem (*Vper*) em Purificação |
| *VpOSCA2.4a* $\leftrightarrow$ *VtOSCA2.4* | 0,1230 | 0,0367 | **0,2987** | Ortólogo 1 (*Vper* vs *Vtub*) em Purificação |
| *VpOSCA2.4b* $\leftrightarrow$ *VtOSCA2.4* | 0,0361 | 0,0177 | **0,4909** | Ortólogo 2 (*Vper* vs *Vtub*) em Purificação Moderada |
| *VpOSCA2.5* $\leftrightarrow$ *VtOSCA2.5* | 0,0636 | 0,0170 | **0,2681** | Seleção Purificadora Estrita |
| *VpOSCA3.1* $\leftrightarrow$ *VtOSCA3.1* | 0,0520 | 0,0231 | **0,4436** | Seleção Purificadora Moderada |
| *VpOSCA3.2* $\leftrightarrow$ *VtOSCA3.2* | 0,0663 | 0,0216 | **0,3260** | Seleção Purificadora Estrita |
| *VpOSCA4.1* $\leftrightarrow$ *VtOSCA4.1* | 0,0824 | 0,0123 | **0,1498** | **Forte Restrição Funcional no Clado Basal** |

#### Tabela 4: Teste de Intensidade de Seleção por Clado (HyPhy RELAX)
*Designação de Linhagens:* Teste = *Vellozia tubiflora* (Ressurreição); Referência = *Vellozia peripherica* (Sempre-verde).

| Subfamília / Clado | N° de Genes | Parâmetro de Intensidade ($K$) | $p\text{-value}$ ($\chi^2$) | Assinatura Evolutiva e Interpretação Biológica |
| :--- | :---: | :---: | :---: | :--- |
| **Clado OSCA1** | 10 | **0,9215** | $0,5957$ (NS) | **Seleção Estável e Invariante ($K \approx 1$):** Purificação idêntica entre os dois estilos de vida; preservação da maquinaria osmosensorial basal. |
| **Clado OSCA2** | 11 | **0,2828** | $\mathbf{3,4 \times 10^{-5}}$ (***) | **Relaxamento Seletivo Maciço em *V. tubiflora* ($K \ll 1$):** Liberação de restrição funcional decorrente do desligamento metabólico (anidrobiose). |
| **Clado OSCA3+4** | 6 | **0,1349** | $\mathbf{0,0061}$ (**) | **Relaxamento Seletivo Extremo em *V. tubiflora* ($K \ll 1$):** Acúmulo neutro de mutações em canais secundários de cálcio. |

#### Tabela 5: Sítios Específicos sob Divergência Seletiva Saneada (HyPhy Contrast-FEL, $p \le 0,05$)

| Clado | Sítio Local (Sítio Global) | Taxa $\beta_\text{Test}$ (*Vtub*) | Taxa $\beta_\text{Ref}$ (*Vper*) | $p\text{-value}$ | Comportamento Evolutivo e Mapeamento |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **OSCA1** | Local 181 (Global 484) | 8,20 | 0,03 | 0,035 | Aceleração em *Vtub* em alinhamento de alta fidelidade (sem gaps). |
| **OSCA1** | Local 710 (Global 1232) | 7,66 | 0,00 | 0,020 | Aceleração em *Vtub* em alinhamento de alta fidelidade. |
| **OSCA1** | Locais 252, 430, 973 | $\approx 0$ | $\gg 0$ | $\le 0,05$ | Taxas não-sinônimas elevadas em *V. peripherica* (ajuste adaptativo perene). |
| **OSCA2** | **14 Sítios:** 8, 71, 76, 147, 191, 241, 270, 308, 394, 395, 432, 596, 720, 824 | $\approx 0$ | $\gg 0$ | $\le 0,05$ | **Aceleração Seletiva Unidirecional em *V. peripherica*:** 100% dos sítios significativos mostram diversificação adaptativa ativa na sempre-verde. |
| **OSCA3+4** | Local 593 (Global 1094) | 24,72 | 0,018 | 0,0085 | Hotspot exclusivo de relaxamento/seleção positiva na planta de ressurreição. |

---

### 6. ARQUITETURA CIS-REGULATÓRIA EM PROMOTORES (PlantCARE 2,0 kb)

Mapeamento de motivos em regiões 2.000 pb a montante do códon de início (ATG), filtrando promotores basais gerais (TATA-box e CAAT-box):

#### Tabela 6: Contagem de Motivos Cis-Regulatórios Chave por Locus

| Gene | ABRE (ABA) | MBS (Seca/MYB) | LTR (Frio) | ARE (Oxidativo) | TC-rich (Defesa) | G-box (Luz/BZIP) | Box 4 (Luz) | DRE (Desidratação) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| *VpOSCA1.1* | 3 | 0 | 0 | 1 | 0 | 3 | 14 | 1 |
| *VpOSCA1.2* | 3 | 1 | 4 | 2 | 0 | 3 | 2 | 0 |
| *VpOSCA1.3* | 2 | 0 | 0 | 1 | 0 | 3 | 5 | 2 |
| *VpOSCA1.4* | 1 | 2 | 1 | 1 | 0 | 1 | 1 | 0 |
| *VpOSCA1.5* | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 |
| *VpOSCA2.1* | **13** | 2 | 0 | 0 | 1 | 7 | 4 | 0 |
| *VpOSCA2.2* | 2 | 1 | 1 | 4 | 0 | 3 | 3 | 0 |
| *VpOSCA2.3* | 1 | 0 | 0 | 1 | 1 | 3 | 10 | 0 |
| *VpOSCA2.4a* | 7 | 1 | 2 | 4 | 0 | 2 | 2 | 1 |
| *VpOSCA2.4b* | 8 | 0 | 1 | 1 | 0 | 6 | 6 | 0 |
| *VpOSCA2.5* | 6 | 1 | 6 | 1 | 0 | 4 | 4 | 0 |
| *VpOSCA3.1* | 3 | 1 | 1 | 1 | 0 | 4 | 1 | 2 |
| *VpOSCA3.2* | **14** | 1 | 0 | 0 | 0 | **11** | 2 | 2 |
| *VpOSCA4.1* | 5 | 2 | 1 | 3 | 1 | 3 | 3 | 0 |
| *VtOSCA1.1* | **11** | 1 | 0 | 1 | 0 | 10 | 11 | 1 |
| *VtOSCA1.2* | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 1 |
| *VtOSCA1.3* | 4 | 1 | 0 | 1 | 0 | 4 | 1 | 2 |
| *VtOSCA1.4* | 5 | 1 | 1 | 1 | 1 | 2 | 0 | 0 |
| *VtOSCA1.5* | 0 | 0 | 0 | 0 | 1 | 1 | 6 | 0 |
| *VtOSCA2.1* | **15** | 3 | 1 | 2 | 1 | **14** | 5 | 4 |
| *VtOSCA2.2* | 5 | 0 | 3 | 1 | 0 | 3 | 1 | 0 |
| *VtOSCA2.3* | 2 | 1 | 0 | 1 | 1 | 2 | 3 | 1 |
| *VtOSCA2.4* | **12** | 0 | 2 | 2 | 0 | 8 | 4 | 0 |
| *VtOSCA2.5* | 9 | 1 | 2 | 0 | 1 | 9 | 4 | 0 |
| *VtOSCA3.1* | 2 | 1 | 1 | 5 | 0 | 2 | 1 | 1 |
| *VtOSCA3.2* | 6 | 1 | 2 | 0 | 0 | 5 | 1 | 0 |
| *VtOSCA4.1* | 0 | 2 | 1 | 3 | 1 | 0 | 1 | 0 |

---

### 7. PERFIL TRANSCRIPTÔMICO TECIDUAL E REGULAÇÃO DIFERENCIAL (RNA-seq DESeq2)

Análise de expressão diferencial estratificada por tecidos vegetais (Raiz, Caule, Folha) com modelo pareado `~ Individual + Tissue` (STAR >80% de mapeamento único, featureCounts):

#### Tabela 7: Expressão Diferencial dos Canais OSCA em *Vellozia*

| Gene | Espécie | Contraste | $\text{baseMean}$ | $\log_2\text{FC}$ | Erro Padrão (lfcSE) | $p\text{-adj}$ (FDR) | Padrão Tecidual Biológico |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| *VpOSCA1.1* | *V. peripherica* | Raiz vs Folha | 707,7 | -1,88 | 0,39 | $1,7 \times 10^{-5}$ | Enriquecimento Foliar em *Vper* |
| *VtOSCA1.1* | *V. tubiflora* | Raiz vs Folha | 762,1 | -1,19 | 0,46 | 0,0357 | Enriquecimento Foliar em *Vtub* |
| *VpOSCA1.2* | *V. peripherica* | Raiz vs Folha | 58,1 | **+4,40** | 1,00 | $1,8 \times 10^{-4}$ | **Especialização Vascular/Radicular** |
| *VtOSCA1.2* | *V. tubiflora* | Raiz vs Folha | 39,0 | **+8,64** | 1,76 | $\mathbf{1,0 \times 10^{-5}}$ | **Especialização Vascular/Radicular Extrema** |
| *VpOSCA1.2* | *V. peripherica* | Caule vs Folha | 58,1 | **+5,01** | 0,91 | $4,5 \times 10^{-7}$ | Expressão Preferencial Caulinhar |
| *VtOSCA1.2* | *V. tubiflora* | Caule vs Folha | 39,0 | **+5,52** | 1,60 | 0,0024 | Expressão Preferencial Caulinhar |
| *VpOSCA2.3* | *V. peripherica* | Caule vs Folha | 19,2 | +3,84 | 1,53 | 0,0424 | Indução Caulinhar Específica em *Vper* |
| *VpOSCA2.4a* | *V. peripherica* | Caule vs Folha | 819,2 | +1,08 | 0,46 | 0,0641 | Leve Viés Caulinhar no Parálogo Tandem A |
| *VpOSCA2.4b* | *V. peripherica* | Caule vs Folha | 1324,8 | +0,31 | 0,41 | 0,6310 | Expressão Constitutiva Ampla no Parálogo Tandem B |
| *VtOSCA2.4* | *V. tubiflora* | Raiz vs Folha | 2082,4 | +0,79 | 0,28 | 0,0214 | Enriquecimento Radicular em *Vtub* |
| *VtOSCA3.2* | *V. tubiflora* | Raiz vs Folha | 96,2 | **+4,55** | 1,44 | 0,0075 | Forte Enriquecimento Radicular em *Vtub* |
| *VpOSCA3.1* | *V. peripherica* | Caule vs Folha | 2985,4 | -1,69 | 0,44 | $9,5 \times 10^{-4}$ | Predominância Foliar em *Vper* |
| *VtOSCA3.1* | *V. tubiflora* | Caule vs Folha | 3222,3 | -2,92 | 0,66 | $5,8 \times 10^{-5}$ | Predominância Foliar em *Vtub* |
| *VtOSCA4.1* | *V. tubiflora* | Raiz vs Caule | 405,2 | +1,85 | 0,49 | 0,0018 | Modulação Subterrânea em *Vtub* |

---

### 8. PROPRIEDADES TOPOLÓGICAS DA REDE DE INTERAÇÃO PROTEÍNA-PROTEÍNA (STRING / NetworkX)

Redes reconstruídas a partir da base STRING v12.0 (score de confiança $\ge 0,400$) expandidas com os 50 principais interatores funcionais de primeira camada:

#### Tabela 8: Parâmetros Topológicos Globais das Redes PPI

| Métrica Topológica | *Vellozia peripherica* (Sempre-verde) | *Vellozia tubiflora* (Ressurreição) | Implicação Biológica |
| :--- | :---: | :---: | :--- |
| **Número Total de Nós** | 61 | 60 | Tamanho de rede equivalente. |
| **Número Total de Arestas** | 187 | **217** | Rede de *V. tubiflora* é **16% mais densamente interconectada**. |
| **Grau Médio de Conectividade Geral** | 6,13 | **7,23** | Maior coesão na sinalização da planta de ressurreição. |
| **Grau Médio dos Canais OSCA Conectados** | 6,09 | **7,30** | Canais OSCA em *Vtub* estão mais acoplados a transdutores celulares. |

#### Tabela 9: Caracterização dos Principais Nós Centrais (Hubs)

| Canal OSCA Hub | Espécie | Grau de Conectividade (Arestas) | Perfil Funcional e Interatores Enriquecidos |
| :--- | :--- | :---: | :--- |
| **OSCA1.2** | *V. peripherica* | **18 conexões** | **Hub Vascular/Subterrâneo Conservado:** Interação com bombas de prótons vacuolares (V-ATPases), transportadores de cátions e quinases dependentes de cálcio (CDPKs). |
| **OSCA1.2** | *V. tubiflora* | **18 conexões** | **Topologia Perfeitamente Conservada:** Exatamente as mesmas 18 conexões de alta confiança, reforçando seu papel não-maleável no sensoriamento vascular basal. |
| **OSCA4.1** | *V. peripherica* | **19 conexões** (Maior hub da rede) | **Hub Integrador de Resposta a Estresse Térmico/Luz:** Fortemente conectado a chaperonas moleculares Hsp70/Hsp90 e quinases MAP. |
| **OSCA4.1** | *V. tubiflora* | 13 conexões | Conexões preservadas com complexos de resposta a estresse proteotóxico. |
| **OSCA2.4a vs 2.4b** | *V. peripherica* | Divisão de parceiros | Subfuncionalização de interatores após a duplicação em tandem recente em *V. peripherica*. |

---
*Matriz finalizada e auditada contra todos os arquivos brutos do diretório `chapter2_osca`.*

