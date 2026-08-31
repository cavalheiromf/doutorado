# COMPÊNDIO E RESUMO CRÍTICO DOS ARTIGOS DA BASE BIBLIOGRÁFICA

**Projeto de Doutorado:** Bases Genômicas e Regulatórias da Adaptação à Seca em Velloziaceae  
**Candidata:** Mariana Feitosa Cavalheiro  
**Orientadora:** Isabel Rodrigues Gerhardt  
**Instituição:** Universidade Estadual de Campinas (UNICAMP)  
**Data:** Agosto de 2026  

---

## 📑 Sumário Executivo por Eixos Temáticos

1. [Eixo 1: Biologia Estrutural, Mecanossensibilidade e Gating Biofísico dos Canais OSCA](#eixo-1-biologia-estrutural-mecanossensibilidade-e-gating-biofísico-dos-canais-osca) (4 artigos)
2. [Eixo 2: Biologia Funcional, Vias de Sinalização e Respostas a Estresses Abióticos e Bióticos](#eixo-2-biologia-funcional-vias-de-sinalização-e-respostas-a-estresses-abióticos-e-bióticos) (7 artigos)
3. [Eixo 3: Identificação Genômica Ampla e Evolução da Família OSCA em Linhagens Vegetais](#eixo-3-identificação-genômica-ampla-e-evolução-da-família-osca-em-linhagens-vegetais) (23 artigos)
4. [Eixo 4: Ecofisiologia, Tolerância à Dessecação e Adaptação em Velloziaceae e Plantas Ressurreição](#eixo-4-ecofisiologia-tolerância-à-dessecação-e-adaptação-em-velloziaceae-e-plantas-ressurreição) (7 artigos)
5. [Eixo 5: Métodos Genômicos, Montagem, Anotação e Filogenômica em Monocotiledôneas](#eixo-5-métodos-genômicos-montagem-anotação-e-filogenômica-em-monocotiledôneas) (2 artigos)

---

# Eixo 1: Biologia Estrutural, Mecanossensibilidade e Gating Biofísico dos Canais OSCA

---

### 1.1 Zhang et al. (2018) — *Structure of the mechanosensitive OSCA channels*
- **Referência:** Zhang, M., Wang, D., Kang, Y., Wu, J. X., Yao, W., Pan, C., ... & Chen, L. (2018). *Nature Structural & Molecular Biology*, 25(9), 850–858. [DOI: 10.1038/s41594-018-0117-6](https://doi.org/10.1038/s41594-018-0117-6)
- **Sistema / Espécie:** *Arabidopsis thaliana* (*AtOSCA1.1*, *AtOSCA1.2*, *AtOSCA3.1*).
- **Metodologia:** Criomicroscopia eletrônica de partícula única (crio-EM), eletrofisiologia (*patch-clamp* de canal único e célula inteira), mutagênese sítio-dirigida e ensaios de imagem de $Ca^{2+}$.
- **Principais Achados:**
  - Determinou as primeiras estruturas crio-EM de canais OSCA vegetais com resolução atômica (3,1–3,5 Å), revelando que o canal opera como um **homodímero simétrico** com eixo rotacional $C_2$.
  - Cada monômero possui 11 hélices transmembranares (M0–M10) organizadas em três domínios funcionais: âncora N-terminal (RSN1_TM), domínio citosólico central tipo RRM (PHM7_cyt) e poro condutor de cátions C-terminal (DUF221 / RSN1_7TM).
  - Identificou o mecanismo biofísico de abertura (*force-from-lipid*): o estiramento da bicamada lipídica traciona uma âncora citosólica hidrofóbica (`LGFLGLWG`), alavancando a hélice M6 ao redor de uma dobradiça conservada de glicina (Gly528 em AtOSCA1.1), abrindo um poro $>5,5\text{ \AA}$ para influxo de $Ca^{2+}$.
- **Relevância para a Tese:** Fornece o modelo biofísico e estrutural de referência para a modelagem 3D (AlphaFold2) e a análise de seleção purificadora nas hélices do poro dos ortólogos de *Vellozia tubiflora* e *Vellozia peripherica*.

---

### 1.2 Liu et al. (2018) — *Structure of the hyperosmolality-gated calcium-permeable channel OSCA1.2*
- **Referência:** Liu, X., Wang, J., & Sun, L. (2018). *Nature Structural & Molecular Biology*, 25(9), 845–849. [DOI: 10.1038/s41594-018-0118-5](https://doi.org/10.1038/s41594-018-0118-5)
- **Sistema / Espécie:** *Arabidopsis thaliana* (AtOSCA1.2).
- **Metodologia:** Estrutura crio-EM (resolução de 3,1 Å) de AtOSCA1.2 na conformação fechada/desativada e eletrofisiologia de membrana lipídica.
- **Principais Achados:**
  - Demonstrou a homologia estrutural distante do clã Anoctamina (CL0416) entre OSCA e os canais/escramblases animais TMEM16 e TMC1/TMC2, apesar de uma sequência primária altamente divergente.
  - Caracterizou a cavidade hidrofóbica central entre as subunidades e os anéis de constrição do poro formados por resíduos aromáticos (Phe516, Phe517, Tyr520 na hélice M6; Val477 na hélice M5).
- **Relevância para a Tese:** Complementa a caracterização topológica das subfamílias de OSCA e estabelece os resíduos críticos para alinhamentos de conservação funcional no Capítulo 2.

---

### 1.3 Hartmann et al. (2021) — *Between Stress and Response: Function and Localization of Mechanosensitive $Ca^{2+}$ Channels in Herbaceous and Woody Plants*
- **Referência:** Hartmann, F., & Fiedler, M. (2021). *International Journal of Molecular Sciences*, 22(18), 9857. [DOI: 10.3390/ijms22189857](https://doi.org/10.3390/ijms22189857)
- **Sistema / Espécie:** Revisão comparativa integrando espécies herbáceas (*Arabidopsis*, arroz) e arbóreas/lenhosas (*Populus*, *Eucalyptus*).
- **Metodologia:** Síntese mecanicista integrando dados de biofísica, biologia celular, sinalização de cálcio e fisiologia do estresse hídrico.
- **Principais Achados:**
  - Mapeou a hierarquia funcional entre os sensores mecânicos primários da membrana plasmática (OSCA, MSL, MCA e Piezo) e os receptores tipo quinase (CrRLK1Ls, FERONIA/THE1) associados à parede celular.
  - Demonstrou que os canais OSCA são os únicos canais mecanossensíveis cuja abertura é ativada por hiperosmolaridade gerando ondas rápidas de cálcio citosólico ($OICI_{cyt}$) em segundos, enquanto MSL atua primariamente na liberação sob hipo-osmolaridade.
- **Relevância para a Tese:** Fundamenta teoricamente a Seção 4 da revisão de literatura, demonstrando por que OSCA foi priorizado em relação a outras famílias mecanossensíveis.

---

### 1.4 Kaur et al. (2021) — *Mechanosensitive ion channels in plants*
- **Referência:** Kaur, A., Madhu, & Upadhyay, S. K. (2021). In *Sensory Biology of Plants* (pp. 375–387). Springer, Singapore. [DOI: 10.1007/978-981-16-0421-8_16](https://doi.org/10.1007/978-981-16-0421-8_16)
- **Sistema / Espécie:** Panorama abrangente do reino vegetal (*Plantae*).
- **Metodologia:** Revisão enciclopédica e comparativa de famílias gênicas de canais iônicos mecanossensíveis.
- **Principais Achados:**
  - Sistematizou a taxonomia molecular dos canais MS em plantas: MscS-like (MSL), Mid1-complementing activity (MCA), Piezo e OSCA.
  - Destacou a expansão evolutiva e diversificação de funções dos canais OSCA especificamente durante a colonização do ambiente terrestre pelas plantas.
- **Relevância para a Tese:** Serve de embasamento para a contextualização filogenética e conceitual dos canais mecanossensíveis.

---

# Eixo 2: Biologia Funcional, Vias de Sinalização e Respostas a Estresses Abióticos e Bióticos

---

### 2.1 Thor et al. (2020) — *The calcium-permeable channel OSCA1.3 regulates plant stomatal immunity*
- **Referência:** Thor, K., Jiang, S., Michard, E., George, J., Scherzer, S., Huang, S., ... & Zipfel, C. (2020). *Nature*, 585(7826), 569–573. [DOI: 10.1038/s41586-020-2702-1](https://doi.org/10.1038/s41586-020-2702-1)
- **Sistema / Espécie:** *Arabidopsis thaliana* (*AtOSCA1.3*).
- **Metodologia:** Fosfoproteômica quantitativa, ensaios *in vitro/in vivo* de fosforilação, eletrofisiologia em ovócitos de *Xenopus* e ensaios de fechamento estomático frente a PAMPs (flg22).
- **Principais Achados:**
  - Descobriu que o canal OSCA1.3 é fosforilado rapidamente no resíduo Ser54 pela quinase imune BIK1 (associada ao complexo FLS2-BAK1) após a percepção de flagelina bacteriana.
  - A fosforilação ativa o influxo de $Ca^{2+}$ nas células-guarda, desencadeando o fechamento estomático em resposta a patógenos.
  - Comprovou a existência de regulação pós-traducional direta e *cross-talk* entre estresses bióticos e a mecânica estomática mediada por canais OSCA.
- **Relevância para a Tese:** Fornece a base experimental para a análise de redes de interação proteica (PPI / STRING) e identificação de resíduos fosforiláveis nos canais OSCA de *Vellozia*.

---

### 2.2 Han et al. (2022) — *OsOSCA1.1 Mediates Hyperosmolality and Salt Stress Sensing in Rice*
- **Referência:** Han, Y., Wang, Y., Zhai, Y., Wen, Z., Liu, J., Xi, C., ... & Han, S. (2022). *International Journal of Molecular Sciences*, 23(24), 15993. [DOI: 10.3390/ijms232415993](https://doi.org/10.3390/ijms232415993)
- **Sistema / Espécie:** Arroz (*Oryza sativa* L. ssp. *japonica*).
- **Metodologia:** Mutantes de nocaute via CRISPR/Cas9 (*osca1.1*), ensaios de imagem de cálcio citosólico com apoaequorina, fenotipagem de tolerância ao sal e estresse osmótico.
- **Principais Achados:**
  - O knockout *OsOSCA1.1* aboliu a elevação de cálcio citosólico induzida por hiperosmolaridade ($OICI_{cyt}$) e sal ($SICI_{cyt}$), resultando em hipersensibilidade ao estresse osmótico e salino.
  - Demonstrou a conservação estrita da função primária do Clado I de OSCA entre monocotiledôneas (arroz) e eudicotiledôneas (*Arabidopsis*).
- **Relevância para a Tese:** Comprova a funcionalidade de membros do Clado I em monocotiledôneas, servindo de modelo direto para a interpretação dos ortólogos em Velloziaceae.

---

### 2.3 Zhai et al. (2020) — *Heterogeneous expression of plasma-membrane-localised OsOSCA1.4 complements osmotic sensing*
- **Referência:** Zhai, Y., Wen, Z., Han, Y., Zhuo, W., Wang, F., Xi, C., ... & Han, S. (2020). *Cell Calcium*, 91, 102264. [DOI: 10.1016/j.ceca.2020.102264](https://doi.org/10.1016/j.ceca.2020.102264)
- **Sistema / Espécie:** Arroz (*Oryza sativa*) expresso em mutante *osca1* de *Arabidopsis* e levedura.
- **Metodologia:** Expressão heteróloga, microscopia confocal de fluorescência (localização subcelular) e medição de influxo de $Ca^{2+}$.
- **Principais Achados:**
  - OsOSCA1.4 localiza-se na membrana plasmática e complementa funcionalmente os defeitos de sinalização de cálcio no mutante *osca1* de *Arabidopsis*.
- **Relevância para a Tese:** Demonstra a plasticidade funcional de paralogos do Clado I em monocotiledôneas.

---

### 2.4 Zhai et al. (2021) — *Functional analysis of rice OSCA genes overexpressed in the arabidopsis osca1 mutant*
- **Referência:** Zhai, Y., Wen, Z., Fang, W., Wang, Y., Xi, C., Liu, J., ... & Han, S. (2021). *Plant Cell Reports*, 40(10), 1935–1946. [DOI: 10.1007/s00299-021-02758-6](https://doi.org/10.1007/s00299-021-02758-6)
- **Sistema / Espécie:** *Oryza sativa* e *Arabidopsis thaliana*.
- **Metodologia:** Super-expressão gênica em mutante *osca1*, ensaios de perda de água foliar e cinética de abertura/fechamento estomático.
- **Principais Achados:**
  - Membros dos Clados I e II restauram a regulação estomática e o crescimento de raiz sob seca e sal, enquanto membros basais (Clado IV) não conseguem resgatar totalmente o fenótipo osmótico.
- **Relevância para a Tese:** Fundamenta a hipótese de subfuncionalização entre os clados filogenéticos de OSCA.

---

### 2.5 Lv et al. (2024) — *Cloning a novel reduced-height (Rht) gene TaOSCA1.4 from a QTL in wheat*
- **Referência:** Lv, G., Jin, X., Wang, H., Wang, Y., Wu, Q., Wu, H., ... & Zhang, K. (2024). *Theoretical and Applied Genetics*, 137(3), 60. [DOI: 10.1007/s00122-024-04566-5](https://doi.org/10.1007/s00122-024-04566-5)
- **Sistema / Espécie:** Trigo (*Triticum aestivum*).
- **Metodologia:** Mapeamento fino de QTL, clonagem posicional, silenciamento gênico induzido por vírus (VIGS) e medições agronômicas.
- **Principais Achados:**
  - Identificou *TaOSCA1.4* como um gene associado à altura de planta reduzida (*Rht*) e arquitetura vegetal favorável, acoplando a sinalização de cálcio e turgor ao alongamento celular do caule.
- **Relevância para a Tese:** Destaca que os canais OSCA não atuam apenas na resposta aguda ao estresse, mas afetam o desenvolvimento vegetativo e arquitetura foliar.

---

### 2.6 Su et al. (2025) — *Isolation of OSCAs in wheat and over-expression of TaOSCA14D increased salt stress tolerance*
- **Referência:** Su, R., Wang, Y., Cui, P., Tian, G., & Qin, Y. (2025). *Journal of Plant Physiology*, 306, 154449. [DOI: 10.1016/j.jplph.2025.154449](https://doi.org/10.1016/j.jplph.2025.154449)
- **Sistema / Espécie:** Trigo (*Triticum aestivum*).
- **Metodologia:** Caracterização genômica de 42 *TaOSCA*, qPCR em 12 tecidos sob estresse salino e superexpressão transgênica de *TaOSCA1.4-4D*.
- **Principais Achados:**
  - A superexpressão de *TaOSCA1.4-4D* aumentou a retenção de $K^+$, reduziu o acúmulo de $Na^+$ tóxico e aumentou os níveis de enzimas antioxidantes (SOD/CAT) sob estresse salino.
- **Relevância para a Tese:** Exemplifica o papel citoprotetor da cascata de cálcio induzida por OSCA na mitigação do estresse oxidativo secundário.

---

### 2.7 Kang et al. (2023) — *Calcium Signaling and the Response to Heat Shock in Crop Plants*
- **Referência:** Kang, X., Zhao, L., & Liu, X. (2023). *International Journal of Molecular Sciences*, 25(1), 324. [DOI: 10.3390/ijms25010324](https://doi.org/10.3390/ijms25010324)
- **Sistema / Espécie:** Revisão focada em culturas agrícolas sob estresse térmico.
- **Metodologia:** Síntese mecanística de canais de $Ca^{2+}$ (OSCA, CNGC, GLR, TPC1) e cascatas downstream (CaMs, CMLs, CDPKs, CBL-CIPKs).
- **Principais Achados:**
  - A termossensibilidade de membrana modula a fluidez lipídica e ativa canais mecanossensíveis de cálcio, preparando a expressão de proteínas de choque térmico (HSPs).
- **Relevância para a Tese:** Conecta os canais OSCA à regulação de respostas combinadas de seca e choque térmico (fatores co-ocorrentes nos campos rupestres).

---

# Eixo 3: Identificação Genômica Ampla e Evolução da Família OSCA em Linhagens Vegetais

---

### 3.1 Wu et al. (2022) — *Evolution of osmosensing OSCA1 $Ca^{2+}$ channel family coincident with plant transition from water to land*
- **Referência:** Wu, X., Yuan, F., Wang, X., Zhu, S., & Pei, Z. M. (2022). *The Plant Genome*, 15(2), e20198. [DOI: 10.1002/tpg2.20198](https://doi.org/10.1002/tpg2.20198)
- **Sistema / Espécie:** Análise filogenômica de larga escala em 45 genomas representativos (desde algas verdes até angiospermas).
- **Metodologia:** Mineração HMMER (PF02714), filogenia bayesiana/máxima verossimilhança, relógio molecular ($Ks$) e análise de conservação de motivos.
- **Principais Achados:**
  - Demonstrou que a família OSCA se expandiu e diversificou criticamente durante a transição água-terra das plantas (há ~500 Ma, no Cambriano/Ordoviciano).
  - Algas aquáticas possuem cópias únicas com baixa sensibilidade mecânica, enquanto embriófitas expandiram os 4 clados monofiléticos para equipar tecidos vasculares, estômatos e raízes.
- **Relevância para a Tese:** **Artigo central de referência filogenética e evolutiva** para o enquadramento do Capítulo 2 da tese.

---

### 3.2 Li et al. (2015) — *Genome-wide survey and expression analysis of the OSCA gene family in rice*
- **Referência:** Li, Y., Yuan, F., Wen, Z., Li, Y., Wang, F., Zhuo, W., ... & Wang, Y. (2015). *BMC Plant Biology*, 15, 261. [DOI: 10.1186/s12870-015-0653-8](https://doi.org/10.1186/s12870-015-0653-8)
- **Sistema / Espécie:** Arroz (*Oryza sativa*).
- **Metodologia:** Primeiro mapeamento sistemático de OSCA em monocotiledôneas; qPCR sob PEG, NaCl e ABA; predição de elementos cis promotores.
- **Principais Achados:**
  - Identificou 11 genes *OsOSCA* distribuídos em 7 cromossomos; revelou que *OsOSCA1.1*, *1.2* e *3.1* são induzidos fortemente por déficit hídrico e desidratação foliar.
- **Relevância para a Tese:** Estabeleceu a nomenclatura padrão dos clados de OSCA em monocotiledôneas.

---

### 3.3 Gu et al. (2018) — *Genome-wide identification and expression analysis of the OSCA gene family in Pyrus bretschneideri*
- **Referência:** Gu, X., Wang, P., Liu, Z., Wang, L., Zhang, Y., & Zhao, B. (2018). *International Journal of Biological Macromolecules*, 114, 831–838. [DOI: 10.1016/j.ijbiomac.2018.03.176](https://doi.org/10.1016/j.ijbiomac.2018.03.176)
- **Sistema / Espécie:** Pera chinesa (*Pyrus bretschneideri*).
- **Metodologia:** Identificação genômica, sintenia com eudicotiledôneas, cálculo de $Ka/Ks$ e qRT-PCR sob seca e salinidade.
- **Principais Achados:**
  - Identificou 16 genes *PbOSCA*; todos sob forte seleção purificadora ($Ka/Ks < 1$), com enriquecimento de elementos promotores DRE e ABRE.
- **Relevância para a Tese:** Suporta a análise de seleção purificadora em árvores de frutos e plantas perenes.

---

### 3.4 Ding et al. (2019) — *Genome-wide analysis of maize OSCA family members and their involvement in drought stress*
- **Referência:** Ding, S., Feng, X., Du, H., & Wang, H. (2019). *Plant Science*, 286, 11–21. [DOI: 10.1016/j.plantsci.2019.05.019](https://doi.org/10.1016/j.plantsci.2019.05.019)
- **Sistema / Espécie:** Milho (*Zea mays*).
- **Metodologia:** Identificação *in silico*, análise de duplicação segmentar, qRT-PCR sob dessecação rápida e perfil temporal.
- **Principais Achados:**
  - 12 genes *ZmOSCA*; duplicações segmentares foram os motores primários da expansão da família em milho; *ZmOSCA1.1* e *ZmOSCA2.4* responderam imediatamente à desidratação radicular.
- **Relevância para a Tese:** Fornece comparação para monocotiledôneas C4 com duplicações cromossômicas segmentares.

---

### 3.5 YANG et al. (2019) — *Genome-wide identification of OSCA gene family and their potential function in dehydration and salt stress in Gossypium hirsutum*
- **Referência:** Yang, X., Xu, Y., Yang, F., Magwanga, R. O., Cai, X., Wang, X., ... & Zhou, Z. (2019). *BMC Genomics*, 20, 831. [DOI: 10.1186/s12864-019-6184-7](https://doi.org/10.1186/s12864-019-6184-7)
- **Sistema / Espécie:** Algodão (*Gossypium hirsutum*, *G. arboreum*, *G. raimondii*).
- **Metodologia:** Análise genômica comparativa poliplóide, RNA-seq sob seca e sal, predição de redes PPI.
- **Principais Achados:**
  - 35 genes em *G. hirsutum* (alotetraploide), duplicando exatamente as cópias dos progenitores diploides (18 em *G. arboreum*, 17 em *G. raimondii*), demonstrando expansão por poliploidização/WGD.
- **Relevância para a Tese:** Demonstra o impacto de Whole-Genome Duplication (WGD) no número de cópias de OSCA.

---

### 3.6 Cao et al. (2020) — *Systematic Analysis of the Maize OSCA Genes Revealing ZmOSCA Involved in Osmotic Stress*
- **Referência:** Cao, Y., Liu, Y., Zhao, J., Zhao, X., Li, X., & Wang, G. (2020). *International Journal of Molecular Sciences*, 21(11), 3844. [DOI: 10.3390/ijms21113844](https://doi.org/10.3390/ijms21113844)
- **Sistema / Espécie:** Milho (*Zea mays*).
- **Metodologia:** Ensaios de duplo híbrido em levedura (Y2H) e BiFC para identificar interações proteicas com fatores de transcrição AP2/EREBP.
- **Principais Achados:**
  - Comprovou a interação física direta entre ZmOSCA2.3/2.4 e o fator de transcrição ZmEREB198, modulando a síntese de prolina sob seca.
- **Relevância para a Tese:** Fornece evidência direta de integração de OSCA com fatores regulatórios de transcrição na Seção 4.3.

---

### 3.7 Tong et al. (2021) — *Genome-Wide Identification and Expression Profile of OSCA Gene Family Members in Triticum aestivum L.*
- **Referência:** Tong, K., Wu, X., He, L., Qiu, S., Liu, S., Cai, L., ... & Chen, J. (2021). *International Journal of Molecular Sciences*, 23(1), 469. [DOI: 10.3390/ijms23010469](https://doi.org/10.3390/ijms23010469)
- **Sistema / Espécie:** Trigo (*Triticum aestivum*).
- **Metodologia:** Análise genômica do hexaploide (subgenomas A, B, D), microrredes de expressão sob seca e frio.
- **Principais Achados:**
  - 42 genes *TaOSCA* organizados em tríades homeólogas funcionais, com retenção assimétrica de expressão entre subgenomas sob estresse osmótico.
- **Relevância para a Tese:** Demonstra os padrões de retenção e viés de expressão pós-poliploidia em gramíneas.

---

### 3.8 Yin et al. (2021) — *Genome-wide analysis of OSCA gene family members in Vigna radiata*
- **Referência:** Yin, L., Zhang, M., Wu, R., Chen, X., Liu, F., & Xing, B. (2021). *BMC Plant Biology*, 21, 574. [DOI: 10.1186/s12870-021-03362-z](https://doi.org/10.1186/s12870-021-03362-z)
- **Sistema / Espécie:** Feijão-mungo (*Vigna radiata*).
- **Metodologia:** Caracterização in silico, sintenia com soja e qRT-PCR sob estresse osmótico.
- **Principais Achados:**
  - Identificou 13 genes *VrOSCA*; alta conservação estrutural de éxons e íntrons com leguminosas proximamente aparentadas.
- **Relevância para a Tese:** Apoia o padrão de conservação da arquitetura gênica introngênica de OSCA.

---

### 3.9 Jie et al. (2022) — *Identification of Populus tomentosa OSCA Genes*
- **Referência:** Jie, L., et al. (2022). *Plant Gene and Trait*, 13(1), 1–10.
- **Sistema / Espécie:** Álamo chinês (*Populus tomentosa*).
- **Metodologia:** Identificação em espécie lenhosa perene e perfil transcricional em folhas e xilema.
- **Principais Achados:**
  - 18 genes *PtoOSCA*; expressão diferencial no câmbio e xilema, sugerindo papel na regulação da tensão hídrica e embolia em vasos condutores.
- **Relevância para a Tese:** Apoia a hipótese do envolvimento de OSCA na sinalização de tensão hidráulica no sistema vascular.

---

### 3.10 Kaur et al. (2022) — *OSCA Genes in Bread Wheat: Molecular Characterization, Expression Profiling, and Evolutionary Analysis*
- **Referência:** Kaur, A., Sharma, A., Madhu, Dixit, S., Singh, K., & Upadhyay, S. K. (2022). *International Journal of Molecular Sciences*, 23(17), 9687. [DOI: 10.3390/ijms23179687](https://doi.org/10.3390/ijms23179687)
- **Sistema / Espécie:** Trigo (*Triticum aestivum*).
- **Metodologia:** Evolução cromossômica, modelagem estrutural de sítios de ligação de íons e perfil RNA-seq sob estresses múltiplos.
- **Principais Achados:**
  - Mapeamento detalhado dos resíduos conservados de ligação de $Ca^{2+}$ e resíduos hidrofóbicos do poro condutor entre os subgenomas A, B e D.
- **Relevância para a Tese:** Fornece matriz comparativa de resíduos essenciais para o poro condutor.

---

### 3.11 Ke et al. (2022) — *OSCA Genes in Liriodendron chinense: Characterization, Evolution and Abiotic Stress Responses*
- **Referência:** Ke, Y., Xu, M., Hwarari, D., Ahmad, B., Li, R., Guan, Y., Chen, J., & Yang, L. (2022). *Frontiers in Plant Science*, 13, 893630. [DOI: 10.3389/fpls.2022.893630](https://doi.org/10.3389/fpls.2022.893630)
- **Sistema / Espécie:** Árvore-tulipa (*Liriodendron chinense*, Magnoliaceae / angiosperma basal).
- **Metodologia:** Filogenômica em linhagem basal de magnoliídeas, análise de promotores e expressão sob seca e frio.
- **Principais Achados:**
  - 11 genes *LcOSCA*; revelou que a divisão em 4 clados já estava plenamente estabelecida antes da divergência entre monocotiledôneas e eudicotiledôneas.
- **Relevância para a Tese:** Confirma a antiguidade evolutiva dos 4 clados de OSCA antes da irradiação de monocotiledôneas como Velloziaceae.

---

### 3.12 Li et al. (2022) — *Preliminary Expression Analysis of the OSCA Gene Family in Medicago sativa*
- **Referência:** Li, Y., Zhang, Y., Li, B., Hou, L., Yu, J., Jia, C., ... & Qin, J. (2022). *International Journal of Molecular Sciences*, 23(19), 11467. [DOI: 10.3390/ijms231911467](https://doi.org/10.3390/ijms231911467)
- **Sistema / Espécie:** Alfafa (*Medicago sativa*).
- **Metodologia:** Genômica em autotetraploide e qPCR sob desidratação e estresse salino.
- **Principais Achados:**
  - 16 genes *MsOSCA*; identificação de expressão tecido-específica preponderante em raízes e nódulos radiculares sob seca.
- **Relevância para a Tese:** Demonstra o papel de OSCA na osmorregulação radicular em leguminosas.

---

### 3.13 Liu et al. (2022) — *Systematic Characterization of the OSCA Family Members in Soybean and Validation of GmOSCA1.2 and GmOSCA1.4*
- **Referência:** Liu, C., Wang, H., Zhang, Y., Cheng, H., Hu, Z., Pei, Z. M., & Li, Q. (2022). *International Journal of Molecular Sciences*, 23(17), 9673. [DOI: 10.3390/ijms23179673](https://doi.org/10.3390/ijms23179673)
- **Sistema / Espécie:** Soja (*Glycine max*).
- **Metodologia:** Identificação de 22 *GmOSCA*, análise de duplicações paleopoliplóides e validação funcional de *GmOSCA1.2* e *1.4* em ensaios de cálcio.
- **Principais Achados:**
  - 22 membros divididos nos 4 clados; *GmOSCA1.2* e *GmOSCA1.4* mediam o influxo rápido de $Ca^{2+}$ e aumentam a tolerância à seca quando superexpressos.
- **Relevância para a Tese:** Fornece evidências robustas de funcionalidade in vivo em espécies diploides paleopoliplóides.

---

### 3.14 Miao et al. (2022) — *Identification of OSCA gene family in Solanum habrochaites and its function analysis under stress*
- **Referência:** Miao, S., Li, F., Han, Y., Yao, Z., Xu, Z., Chen, X., ... & Wang, A. (2022). *BMC Genomics*, 23, 547. [DOI: 10.1186/s12864-022-08675-6](https://doi.org/10.1186/s12864-022-08675-6)
- **Sistema / Espécie:** Tomate silvestre tolerante a estresse (*Solanum habrochaites*).
- **Metodologia:** Genômica comparativa com tomate cultivado (*S. lycopersicum*), qPCR sob frio, seca e ataque por patógenos (*Phytophthora*).
- **Principais Achados:**
  - 11 genes *ShOSCA*; todos localizados na membrana plasmática; genes do Clado I exibiram ativação coordenada frente a múltiplos estresses.
- **Relevância para a Tese:** Apoia o uso de parentes silvestres extremófilos como modelo de comparação com espécies cultivadas.

---

### 3.15 She et al. (2022) — *Genome-Wide Identification, Evolution and Expressional Analysis of OSCA Gene Family in Barley (Hordeum vulgare L.)*
- **Referência:** She, K., Pan, W., Yan, Y., Shi, T., Chu, Y., Cheng, Y., Ma, B., & Song, W. (2022). *International Journal of Molecular Sciences*, 23(21), 13027. [DOI: 10.3390/ijms232113027](https://doi.org/10.3390/ijms232113027)
- **Sistema / Espécie:** Cevada (*Hordeum vulgare*).
- **Metodologia:** Identificação genômica, sintenia cromossômica com trigo e arroz, RNA-seq sob estresse abiótico.
- **Principais Achados:**
  - 12 genes *HvOSCA*; fortes assinaturas de purificação evolutiva e conservação sintênica estrita com arroz e trigo.
- **Relevância para a Tese:** Reforça a conservação da família em monocotiledôneas graminóides.

---

### 3.16 Yang et al. (2022) — *Identification and Expression Profile Analysis of the OSCA Gene Family Related to Abiotic and Biotic Stress Response in Cucumber*
- **Referência:** Yang, S., Zhu, C., Chen, J., Zhao, J., Hu, Z., Liu, S., & Zhou, Y. (2022). *Biology*, 11(8), 1134. [DOI: 10.3390/biology11081134](https://doi.org/10.3390/biology11081134)
- **Sistema / Espécie:** Pepino (*Cucumis sativus*).
- **Metodologia:** Caracterização de 9 genes *CsOSCA*, análise de elementos promotores e resposta transcricional sob dessecação e infecção fúngica.
- **Principais Achados:**
  - Pepino possui um repertório compacto (9 membros), com elementos promotores ABRE e W-box altamente enriquecidos.
- **Relevância para a Tese:** Fornece modelo de repertório mínimo/compacto de OSCA em dicotiledôneas.

---

### 3.17 Chakraborty et al. (2023) — *Genome-wide characterization and comparative analysis of the OSCA gene family in Camelina sativa*
- **Referência:** Chakraborty, S., et al. (2023). *Scientific Reports*, 13, 5914. [DOI: 10.1038/s41598-023-33226-8](https://doi.org/10.1038/s41598-023-33226-8)
- **Sistema / Espécie:** Falsa-linhaça (*Camelina sativa*, Brassicaceae alohexaploide).
- **Metodologia:** Análise de 39 genes *CsOSCA* em genoma triplicado, cálculo de $Ka/Ks$ e modelagem tridimensional.
- **Principais Achados:**
  - Demonstrou a preservação em triplicata dos membros de *Arabidopsis* e conservação quase absoluta dos resíduos do poro hidrofóbico.
- **Relevância para a Tese:** Suporta a predição da integridade estrutural do poro condutor após eventos de duplicação.

---

### 3.18 Li et al. (2023) — *Genome-wide investigation and expression analysis of OSCA gene family in response to abiotic stress in alfalfa*
- **Referência:** Li, X., Wang, X., Mu, X., Zhang, F., Wang, Z., & Gao, J. (2023). *BMC Genomics*, 24, 765. [DOI: 10.1186/s12864-023-09857-8](https://doi.org/10.1186/s12864-023-09857-8)
- **Sistema / Espécie:** Alfafa (*Medicago sativa*).
- **Metodologia:** Identificação em genoma montado a nível cromossômico, RNA-seq sob PEG, NaCl, ABA e frio, predição de microRNAs alvo.
- **Principais Achados:**
  - 17 genes *MsOSCA*; identificação de regulação pós-transcricional por microRNAs direcionando transcritos de OSCA sob estresse osmótico prolongado.
- **Relevância para a Tese:** Amplia o espectro de regulação gênica para além dos fatores de transcrição clássicos.

---

### 3.19 Shan et al. (2023) — *Evolutionary analysis of the OSCA gene family in sunflower (Helianthus annuus L.) and expression analysis under NaCl stress*
- **Referência:** Shan, F., Wu, Y., Du, R., Yang, Q., Liu, C., Wang, Y., Zhang, C., & Chen, Y. (2023). *PeerJ*, 11, e15089. [DOI: 10.7717/peerj.15089](https://doi.org/10.7717/peerj.15089)
- **Sistema / Espécie:** Girassol (*Helianthus annuus*).
- **Metodologia:** Mineração HMM, sintenia, análise de promotores e perfil transcriptômico sob estresse osmótico salino.
- **Principais Achados:**
  - 17 genes *HaOSCA*; expansão mediada por duplicações dispersas e segmentares com fortes respostas transcricionais em raízes.
- **Relevância para a Tese:** Modelo de asterídea com expansão de OSCA em ambiente xerofítico.

---

### 3.20 Zhang et al. (2023) — *Genome-wide analysis of hyperosmolality-gated calcium-permeable channel (OSCA) family members in Brassica napus*
- **Referência:** Zhang, X., Cheng, X., Zhang, C., Ma, X., Zhang, Y., Song, J., & Xie, M. (2023). *Gene*, 856, 147137. [DOI: 10.1016/j.gene.2022.147137](https://doi.org/10.1016/j.gene.2022.147137)
- **Sistema / Espécie:** Colza / Canola (*Brassica napus*, alotetraploide AACC).
- **Metodologia:** Mapeamento de 28 genes *BnOSCA*, sintenia com *B. rapa* (AA) e *B. oleracea* (CC), qPCR sob estresse osmótico e frio.
- **Principais Achados:**
  - Demonstrou a retenção simétrica de genes OSCA em ambos os subgenomas após a alopoliploidização, mantendo fortes respostas regulatórias a ABA.
- **Relevância para a Tese:** Exemplifica a dinâmica de retenção pós-poliploidia em Brassicaceae.

---

### 3.21 Zhang et al. (2025) — *Genome-Wide Identification, Phylogeny, and Abiotic Stress Response Analysis of OSCA Family Genes in Notopterygium franchetii*
- **Referência:** Zhang, Q. Y., He, X. J., Xie, Y. Z., Zhou, L. P., Meng, X., Kang, J., Luo, C. Y., Wang, Y. N., Li, Z. H., & Guan, T. X. (2025). *International Journal of Molecular Sciences*, 26(11), 5043. [DOI: 10.3390/ijms26115043](https://doi.org/10.3390/ijms26115043)
- **Sistema / Espécie:** Erva medicinal alpina (*Notopterygium franchetii*, Apiaceae).
- **Metodologia:** Genômica em espécie adaptada a altas altitudes, qPCR sob estresse hídrico e choque térmico.
- **Principais Achados:**
  - 13 genes *NfOSCA*; adaptação a ambientes montanhosos extremos correlacionada à ativação ultra-rápida de transcritos do Clado I sob desidratação.
- **Relevância para a Tese:** Muito próxima ao contexto ecológico dos campos rupestres (ecossistema montanhoso com alta radiação e oscilação térmica diária).

---

### 3.22 Zhu et al. (2025) — *Genome-wide identification and characterization of OSCA genes in white clover revealing their function in response to abiotic stresses*
- **Referência:** Zhu, X., Li, M., Li, S., Zhao, X., Zhang, T., Guo, M., Guo, C., & Shu, Y. (2025). *BMC Plant Biology*, 25, 45. [DOI: 10.1186/s12870-025-06045-3](https://doi.org/10.1186/s12870-025-06045-3)
- **Sistema / Espécie:** Trevo branco (*Trifolium repens* L., alotetraploide).
- **Metodologia:** Identificação genômica, cálculo de $Ka/Ks$, qRT-PCR sob dessecação (PEG) e frio prolongado.
- **Principais Achados:**
  - 20 genes *TrOSCA*; alta conservação estrutural com duplicações mantidas sob seleção purificadora severa; membros do Clado I apresentaram resposta precoce em tecidos foliares.
- **Relevância para a Tese:** Demonstra a preservação do Clado I como sensor preferencial em folhas sob dessecação.

---

### 3.23 Yang et al. (2026) — *Genome-wide identification of castor bean OSCA genes and analysis of their function under drought and salt stress*
- **Referência:** Yang, L., et al. (2026). *BMC Plant Biology*, 26, 661. [DOI: 10.1186/s12870-026-06610-w](https://doi.org/10.1186/s12870-026-06610-w)
- **Sistema / Espécie:** Mamona (*Ricinus communis* L., Euphorbiaceae altamente tolerante à seca).
- **Metodologia:** Análise genômica em planta diploide tolerante à seca, RNA-seq de múltiplos tecidos, validação por qPCR.
- **Principais Achados:**
  - 14 genes *RcOSCA*; identificou subfuncionalização marcante entre pares parálogos pós-duplicação: *RcOSCA1* com expressão estrita em raiz vs. *RcOSCA8* expresso exclusivamente em sementes durante a dessecação terminal.
- **Relevância para a Tese:** Evidência crucial de subfuncionalização tecido-específica pós-duplicação na Seção 4.3 da revisão.

---

# Eixo 4: Ecofisiologia, Tolerância à Dessecação e Adaptação em Velloziaceae e Plantas Ressurreição

---

### 4.1 Fernandes et al. (2020) — *Biodiversity and ecosystem services in the Campo Rupestre: A neglected conservation hotspot*
- **Referência:** Fernandes, G. W., Arantes-Garcia, L., Barbosa, M., Buisson, E., Callisto, M., Centeri, C., ... & Silveira, F. A. (2020). *Perspectives in Ecology and Conservation*, 18(4), 213–222. [DOI: 10.1016/j.pecon.2020.09.006](https://doi.org/10.1016/j.pecon.2020.09.006)
- **Sistema / Espécie:** Ecossistema dos *Campos Rupestres* (Cadeia do Espinhaço e Serra da Canastra).
- **Metodologia:** Síntese ecológica, biogeográfica e conservacionista integrando serviços ecossistêmicos e ameaças climáticas.
- **Principais Achados:**
  - Consolida os campos rupestres como um hotspot global de endemismo e diversidade vegetal antiga (OCBIL), destacando a vulnerabilidade crítica a regimes alterados de seca e fogo.
- **Relevância para a Tese:** Contextualização macroecológica da Seção 1 da revisão de literatura.

---

### 4.2 Teodoro et al. (2021) — *Desiccation tolerance implies costs to productivity but allows survival under extreme drought conditions in Velloziaceae*
- **Referência:** Teodoro, G. S., Costa, P. B., Brum, M., Signori-Müller, C., Alcantara, S., Dawson, T. E., West, A. G., Lambers, H., & Oliveira, R. S. (2021). *Environmental and Experimental Botany*, 189, 104556. [DOI: 10.1016/j.envexpbot.2021.104556](https://doi.org/10.1016/j.envexpbot.2021.104556)
- **Sistema / Espécie:** Velloziaceae simpátricas nos campos rupestres (*Vellozia caruncularis*, *Vellozia nivea*, *Barbacenia gentianoides*, *Barbacenia graminifolia*).
- **Metodologia:** Medições de fluorescência de clorofila (*in situ* e laboratório), curvas de vulnerabilidade hidráulica ($\Psi_{TLP}$), teor relativo de água (RWC) e taxas anuais de crescimento de biomassa.
- **Principais Achados:**
  - Demonstrou o *trade-off* fundamental: plantas tolerantes à dessecação (DT) sofrem paralisação do ganho de carbono durante a seca e possuem custos metabólicos de reparo, resultando em baixíssimas taxas de crescimento anual, mas com sobrevivência de 100% sob secas severas. Espécies com escape/evasão sustentam fotossíntese contínua, mas sofrem mortalidade massiva se ultrapassarem o $\Psi_{TLP}$.
- **Relevância para a Tese:** **Artigo basilar da tese** para fundamentar os custos adaptativos e a segregação de nicho na Seção 1.4/1.5 e Tabela 1.

---

### 4.3 Oung et al. (2021) — *Differential response of the photosynthetic machinery to dehydration in older and younger resurrection plants*
- **Referência:** Oung, H. M. O., Mukhopadhyay, R., Svoboda, V., Charuvi, D., Reich, Z., & Kirchhoff, H. (2021). *Journal of Experimental Botany*, 73(5), 1566–1580. [DOI: 10.1093/jxb/erab485](https://doi.org/10.1093/jxb/erab485)
- **Sistema / Espécie:** Planta ressurreição modelo (*Craterostigma pumilum*).
- **Metodologia:** Espectroscopia de absorbância e fluorescência, termoluminescência e proteômica de tilacóides durante desidratação e reidratação.
- **Principais Achados:**
  - Caracterizou o desmantelamento reversível e ordenado do fotossistema II (PSII) e o papel do fluxo cíclico de elétrons (CET) ao redor do PSI para evitar estresse foto-oxidativo durante a dessecação foliar.
- **Relevância para a Tese:** Apoia a explicação dos mecanismos de fotoproteção e dessecação celular na Seção 2.2.

---

### 4.4 Vieira et al. (2022) — *Water retention and metabolic changes improve desiccation tolerance in Barbacenia graminifolia (Velloziaceae)*
- **Referência:** Vieira, E. A., Silva, K. R., Rossi, M. L., Martinelli, A. P., Gaspar, M., & Braga, M. R. (2022). *Functional Plant Biology*, 49(10), 875–887. [DOI: 10.1071/FP21307](https://doi.org/10.1071/FP21307)
- **Sistema / Espécie:** *Barbacenia graminifolia* (Velloziaceae endêmica da Serra do Cipó).
- **Metodologia:** Anatomia foliar quantitativa, microscopia eletrônica de varredura (MEV), perfil de carboidratos solúveis e açúcares da família da rafinose (RFOs).
- **Principais Achados:**
  - A dessecação foliar induz acúmulo massivo de sacarose e rafinose associado à mucilagem rica em polissacarídeos ácidos nas células do parênquima paliçádico, desacelerando a perda de água e permitindo a vitrificação citoplasmática.
- **Relevância para a Tese:** Evidência anatômica e metabólica direta de tolerância à dessecação em Velloziaceae na Seção 1.3 e 2.2.

---

### 4.5 Vieira et al. (2025) — *Surviving water scarcity: seasonal contrasts in drought and desiccation tolerance of co-occurring Barbacenia gentianoides and Vellozia caruncularis*
- **Referência:** Vieira, E. A., Silva, G. M., Gaspar, M., Braga, M. R., & Caldeira, C. F. (2025). *Plant Biology*, 27(2), 180–194. [DOI: 10.1111/plb.13745](https://doi.org/10.1111/plb.13745)
- **Sistema / Espécie:** *Barbacenia gentianoides* (evasão/evergreen) e *Vellozia caruncularis* (tolerante à dessecação/DT) co-ocorrentes em campo.
- **Metodologia:** Acompanhamento sazonal *in situ* (estação seca vs. chuvosa), dinâmica de carboidratos não estruturais (NSC), translocação de carbono basal e potencial hídrico foliar.
- **Principais Achados:**
  - *B. gentianoides* sobrevive à seca remobilizando carbono para a base das folhas e mantendo água foliar através de fendas de rocha profundas; *V. caruncularis* seca completamente em afloramentos rasos e acumula osmorreguladores para reativação imediata na chuva.
- **Relevância para a Tese:** Fornece o paralelo ecológico e fisiológico perfeito para o nosso par comparativo de espécies (*V. tubiflora* vs. *V. peripherica*).

---

### 4.6 Bondi et al. (2023) — *Demystifying the convergent ecological specialization of desiccation tolerance in grasses*
- **Referência:** Bondi, L. M., Marks, R. A., & VanBuren, R. (2023). *Annals of Botany*, 131(3), 521–531. [DOI: 10.1093/aob/mcad005](https://doi.org/10.1093/aob/mcad005)
- **Sistema / Espécie:** Gramíneas ressurreição (*Tripogon loliiformis*, *Oropetium thomaeum*, *Sporobolus stapfianus*).
- **Metodologia:** Revisão comparativa e filogenômica de especialização ecológica de dessecação em Poaceae.
- **Principais Achados:**
  - Demonstra que a tolerância à dessecação vegetativa evoluiu múltiplas vezes convergentemente em monocotiledôneas através da cooptação e religamento (*rewiring*) de redes transcricionais ancestrais de dessecação de sementes (elementos ABRE, sHSPs, LEAs).
- **Relevância para a Tese:** Embasamento da hipótese de cooptação regulatória e convergência adaptativa em monocotiledôneas.

---

### 4.7 Marks et al. (2024) — *Convergent evolution of desiccation tolerance in grasses*
- **Referência:** Marks, R. A., Van Der Pas, L., Schuster, J., Gilman, I. S., & VanBuren, R. (2024). *Nature Plants*, 10(7), 1112–1125. [DOI: 10.1038/s41477-024-01729-5](https://doi.org/10.1038/s41477-024-01729-5)
- **Sistema / Espécie:** Genômica comparativa em múltiplas gramíneas ressurreição e sensíveis.
- **Metodologia:** Montagens de genomas em escala cromossômica, transcriptômica comparativa de séries temporais de dessecação e análise de redes regulatórias sintênicas.
- **Principais Achados:**
  - Revelou que a evolução convergente da tolerância à dessecação opera por ativação de blocos gênicos sintênicos conservados combinada com duplicações em tandem específicas de linhagem (ex: ELIPs e chaperonas moleculares).
- **Relevância para a Tese:** **Modelo metodológico e conceitual direto** para as análises de sintenia, duplicação e transcriptômica comparativa do Capítulo 1 da tese.

---

# Eixo 5: Métodos Genômicos, Montagem, Anotação e Filogenômica em Monocotiledôneas

---

### 5.1 Vuruputoor et al. (2023) — *Welcome to the big leaves: Best practices for improving genome annotation in non-model plant genomes*
- **Referência:** Vuruputoor, V. S., Monyak, D., Fetter, K. C., Webster, C., Bhattarai, A., Shrestha, B., ... & Wegrzyn, J. L. (2023). *Applications in Plant Sciences*, 11(2), e11533. [DOI: 10.1002/aps3.11533](https://doi.org/10.1002/aps3.11533)
- **Sistema / Espécie:** Guia metodológico para anotação estrutural e funcional de genomas de plantas não-modelo.
- **Metodologia:** Benchmarking de pipelines de anotação (BRAKER, MAKER, TSEBRA, StringTie), métricas BUSCO e filtragem de elementos de transposição (TEs).
- **Principais Achados:**
  - Estabeleceu as melhores práticas para superar os desafios de genomas vegetais complexos (alta carga de retrotransposons LTR, heterozigosidade e ploidia variável), preconizando a integração mandatória de RNA-seq multi-tecido e validação de ortologia.
- **Relevância para a Tese:** **Guia metodológico do pipeline de anotação** das montagens cromossômicas de *Vellozia tubiflora* e *Vellozia peripherica* no Capítulo 1.

---

### 5.2 Wanga et al. (2021) — *Complete Chloroplast Genomes of Acanthochlamys bracteata (China) and Xerophyta (Africa) (Velloziaceae): Comparative Genomics and Phylogenomic Placement*
- **Referência:** Wanga, V. O., Dong, X., Oulo, M. A., Mkala, E. M., Yang, J. X., Onjalalaina, G. E., ... & Wang, Q. F. (2021). *Frontiers in Plant Science*, 12, 691833. [DOI: 10.3389/fpls.2021.691833](https://doi.org/10.3389/fpls.2021.691833)
- **Sistema / Espécie:** *Acanthochlamys bracteata* (espécie asiática relictual basal de Velloziaceae) e *Xerophyta* (linhagem africana de Velloziaceae).
- **Metodologia:** Sequenciamento de nova geração (NGS), montagem de plastomas completos (153–155 kb), análise de limites de regiões invertidas repetidas (IRs) e filogenômica de Pandanales.
- **Principais Achados:**
  - Confirmou que *Acanthochlamys* é o grupo irmão de todas as demais Velloziaceae, delimitando a arquitetura ancestral do plastoma da família e fornecendo marcadores para filogenia de alta resolução.
- **Relevância para a Tese:** Fornece o contexto filogenético macroevolutivo e dados de referência genômica para a ordem Pandanales e a família Velloziaceae.

---

## 📊 Matriz Comparativa Síntese: Família OSCA nos Artigos Analisados

A tabela a seguir consolida o número de genes OSCA identificados, o tipo de estresse avaliado e os principais achados em cada espécie descrita na base:

| Artigo | Espécie / Sistema | N° de Genes OSCA | Clados | Foco Experimental / Estresse | Principal Achado |
|---|---|---|---|---|---|
| **Zhang et al. (2018)** | *Arabidopsis thaliana* | 15 | I–IV | Crio-EM / Biofísica | Estrutura homodimérica crio-EM (3,1 Å), mecanismo *force-from-lipid* e poro DUF221. |
| **Liu et al. (2018)** | *Arabidopsis thaliana* | 15 | I–IV | Crio-EM / Topologia | Resolução de AtOSCA1.2 e constrição hidrofóbica do poro. |
| **Thor et al. (2020)** | *Arabidopsis thaliana* | 15 | I–IV | Imunidade / Fosfoproteômica | Fosforilação de OSCA1.3 por BIK1 na Ser54 induzindo fechamento estomático. |
| **Han et al. (2022)** | *Oryza sativa* | 11 | I–IV | CRISPR / Sinalização $Ca^{2+}$ | OsOSCA1.1 é essencial para ondas de cálcio osmóticas ($OICI_{cyt}$) e salinas ($SICI_{cyt}$). |
| **Zhai et al. (2020/21)** | *Oryza sativa* | 11 | I–IV | Expressão Heteróloga | OsOSCA1.4 e membros do Clado I resgatam o fenótipo no mutante *osca1*. |
| **Lv et al. (2024)** | *Triticum aestivum* | 42 | I–IV | Mapeamento QTL / VIGS | TaOSCA1.4 acopla sinalização mecânica ao porte de planta (*Rht*). |
| **Su et al. (2025)** | *Triticum aestivum* | 42 | I–IV | Transgenia / Salinidade | TaOSCA1.4-4D melhora homeostase iônica e atividade antioxidante sob sal. |
| **Wu et al. (2022)** | 45 Genomas Vegetais | Variável | I–IV | Filogenômica Comparativa | Expansão e diversificação funcional coincidente com a transição água-terra. |
| **Li et al. (2015)** | *Oryza sativa* | 11 | I–IV | Genoma / qPCR | Primeiro mapeamento em monocotiledôneas; resposta a PEG e desidratação. |
| **Ding et al. (2019)** | *Zea mays* | 12 | I–IV | Genoma / qPCR | Duplicações segmentares geraram a família em milho; indução por seca. |
| **Cao et al. (2020)** | *Zea mays* | 12 | I–IV | Y2H / BiFC | ZmOSCA2.3/2.4 interagem com fator de transcrição ZmEREB198. |
| **YANG et al. (2019)** | *Gossypium hirsutum* | 35 | I–IV | Poliploidia / RNA-seq | Alotetraploide dobrou o número de genes dos ancestrais diploides. |
| **Tong / Kaur (2021/22)** | *Triticum aestivum* | 42 | I–IV | Hexaploide / Sintenia | Conservação em tríades A, B, D e mapeamento de resíduos hidrofóbicos do poro. |
| **Yin et al. (2021)** | *Vigna radiata* | 13 | I–IV | Genoma / qPCR | Estrutura introngênica conservada com leguminosas. |
| **Jie et al. (2022)** | *Populus tomentosa* | 18 | I–IV | Lenhosa / Xilema | Expressão diferencial no sistema vascular condutor. |
| **Ke et al. (2022)** | *Liriodendron chinense* | 11 | I–IV | Angiosperma Basal | Estabelecimento dos 4 clados antes da divisão monocot/eudicot. |
| **Liu et al. (2022)** | *Glycine max* | 22 | I–IV | Transgenia / Seca | GmOSCA1.2 e 1.4 conferem tolerância a estresse hídrico. |
| **Miao et al. (2022)** | *Solanum habrochaites* | 11 | I–IV | Parente Silvestre | Ativação coordenada frente a seca, frio e patógenos. |
| **She et al. (2022)** | *Hordeum vulgare* | 12 | I–IV | Sintenia / Cevada | Alta conservação sintênica e seleção purificadora severa. |
| **Yang et al. (2022)** | *Cucumis sativus* | 9 | I–IV | Genoma Compacto | Repertório mínimo de 9 genes com promotores ABRE e W-box. |
| **Chakraborty (2023)** | *Camelina sativa* | 39 | I–IV | Alohexaploide | Preservação em triplicata dos resíduos do poro condutor. |
| **Li et al. (2023)** | *Medicago sativa* | 17 | I–IV | RNA-seq / microRNAs | Regulação pós-transcricional de transcritos OSCA por microRNAs sob seca. |
| **Shan et al. (2023)** | *Helianthus annuus* | 17 | I–IV | Genoma / Salinidade | Expansão por duplicações dispersas com expressão radicular. |
| **Zhang et al. (2023)** | *Brassica napus* | 28 | I–IV | Alotetraploide | Retenção simétrica em subgenomas AA e CC. |
| **Zhang et al. (2025)** | *Notopterygium franchetii*| 13 | I–IV | Alpina / Altitude | Ativação ultra-rápida do Clado I em ambiente montanhoso. |
| **Zhu et al. (2025)** | *Trifolium repens* | 20 | I–IV | Alotetraploide | Preservação do Clado I sob seleção purificadora para desidratação. |
| **Yang et al. (2026)** | *Ricinus communis* | 14 | I–IV | Transcriptômica | Subfuncionalização: RcOSCA1 (raiz) vs. RcOSCA8 (semente na dessecação). |
| **Teodoro et al. (2021)** | *Velloziaceae spp.* | N/A | N/A | Ecofisiologia / TLP | *Trade-off* entre dessecação (sobrevivência) e evasão (produtividade). |
| **Vieira et al. (2022/25)**| *Velloziaceae spp.* | N/A | N/A | Anatomia / Vitrificação | Açúcares RFOs, mucilagem e remobilização de carbono basal. |
| **Marks et al. (2024)** | Gramíneas Ressurreição | N/A | N/A | Genômica Comparativa | Evolução convergente por blocos sintênicos e duplicações tandem (ELIPs). |
| **Vuruputoor (2023)** | Plantas Não-Modelo | N/A | N/A | Bioinformática / RNA-seq | Boas práticas para anotação estrutural de genomas vegetais complexos. |
| **Wanga et al. (2021)** | *Acanthochlamys / Xerophyta*| N/A | N/A | Plastomas / Pandanales | Posicionamento filogenômico basal e evolução do plastoma em Velloziaceae. |


---

## 6. Eixo Temático VI: Genômica Comparativa de Modelos de Dessecação (DT vs. Sensível)

### 6.1. VanBuren et al. (2015) — *Nature*
- **Referência:** VanBuren, R., Bryant, D., Bushagan, V. G., et al. (2015). Single-molecule sequencing of the desiccation-tolerant grass *Oropetium thomaeum*. *Nature*, 527(7579), 498–502.
- **Sistema / Modelo Biológico:** *Oropetium thomaeum* (gramínea modelo tolerante à dessecação, genoma ultracompacto de ~245 Mb).
- **Abordagem Metodológica:** Sequenciamento de moléculas únicas PacBio de alta cobertura, montagem cromossômica de *novo*, transcriptômica de dessecação/reidratação e genômica comparativa com arroz e sorgo.
- **Principais Achados:**
  - Primeiro genoma de alta contiguidade de uma gramínea tolerante à dessecação, revelando manutenção de integridade genômica com baixa densidade de retrotransposons LTR.
  - Demonstrou que a dessecação vegetativa recrutou e reprogramou redes ancestrais de proteção de sementes (LEAs, chaperonas e fatores de transcrição ABI/HSF).
  - Identificou duplicações em tandem em famílias de fotoproteção e resposta osmótica.
- **Relevância para a Tese:** Fornece o paradigma metodológico de genômica comparativa para espécies DT com montagens de alta contiguidade, servindo como modelo direto para o Capítulo 1 e a Seção 3 da revisão.

---

### 6.2. Costa et al. (2017) — *Nature Plants*
- **Referência:** Costa, M.-C. D., Artur, M. A. S., Maia, J., Jonkheer, E. M., et al. (2017). A footprint of desiccation tolerance in the genome of the resurrection plant *Xerophyta viscosa*. *Nature Plants*, 3(4), 17038.
- **Sistema / Modelo Biológico:** *Xerophyta viscosa* (Velloziaceae africana, monocotiledônea tolerante à dessecação).
- **Abordagem Metodológica:** Sequenciamento genômico cromossômico (Illumina + PacBio), anotação estrutural/funcional, transcriptômica de cinética temporal de desidratação e genômica comparativa com monocotiledôneas sensíveis.
- **Principais Achados:**
  - Genoma de referência fundador para Velloziaceae, comprovando a pegada genômica da anidrobiose na família.
  - Expansão maciça de famílias de fotoproteção (ELIPs) e chaperonas moleculares (sHSPs e LEAs) via duplicações em tandem.
  - Remodelagem cis-regulatória de promotores que cooptaram elementos de resposta a dessecação de sementes para expressão foliar constitutiva e induzida.
- **Relevância para a Tese:** É a pedra angular genômica em Velloziaceae, fundamentando diretamente o desenho experimental comparativo com *Vellozia tubiflora* e *Vellozia peripherica*.

---

### 6.3. Xiao et al. (2015) — *PNAS*
- **Referência:** Xiao, L., Yang, G., Lie, L., et al. (2015). Genome sequencing of the resurrection plant *Boea hygrometrica* provides the first insight into the desiccation tolerance of the eudicot. *PNAS*, 112(18), 5838–5843.
- **Sistema / Modelo Biológico:** *Boea hygrometrica* (Gesneriaceae, eudicotiledônea tolerante à dessecação).
- **Abordagem Metodológica:** Sequenciamento genômico de *novo*, montagem cromossômica, transcriptômica comparativa e evolução de famílias gênicas.
- **Principais Achados:**
  - Primeira evidência genômica em eudicotiledôneas de que a tolerância à dessecação evoluiu por seleção positiva e reorganização regulatória, e não por originação de novos genes.
  - Expansão de genes de modificação de parede celular e síntese de oligossacarídeos protetores (RFOs).
- **Relevância para a Tese:** Sustenta a hipótese de que *Vellozia* compartilha mecanismos conservados de regulação transcricional e integridade de membrana celular sob desidratação extrema.

---

### 6.4. VanBuren et al. (2018) — *PNAS*
- **Referência:** VanBuren, R., Wai, C. M., Ou, S., et al. (2018). The resurrection plant *Selaginella lepidophylla* has a compact genome with duplicate gene retention. *PNAS*, 115(7), E1591–E1599.
- **Sistema / Modelo Biológico:** *Selaginella lepidophylla* (licófita de dessecação) vs. *S. moellendorffii* (licófita sensível).
- **Abordagem Metodológica:** Genômica comparativa pareada, análise de sintenia, datação de duplicações via $Ks$ e transcriptômica comparativa.
- **Principais Achados:**
  - Retenção diferencial de duplicatas gênicas associadas a estresse osmótico e proteção antioxidante no modelo tolerante.
  - Demonstração de que a anidrobiose em traqueófitas basais utiliza um núcleo conservado de osmorregulação.
- **Relevância para a Tese:** Valida o modelo comparativo de retenção de duplicatas gênicas em linhagens tolerantes.

---

### 6.5. Yuan et al. (2014) — *Nature*
- **Referência:** Yuan, F., Yang, H., Xue, Y., Kong, D., et al. (2014). OSCA1 mediates osmotic-stress-evoked $Ca^{2+}$ increases vital for osmosensing in *Arabidopsis*. *Nature*, 514(7522), 367–371.
- **Sistema / Modelo Biológico:** *Arabidopsis thaliana* (mutante *osca1* vs. selvagem).
- **Abordagem Metodológica:** Triagem genética direta com imagem de cálcio ratiométrica (YC3.6), eletrofisiologia (*patch-clamp* de protoplastos) e ensaios fisiológicos de fechamento estomático.
- **Principais Achados:**
  - Descoberta seminal do primeiro canal mecanossensível de cálcio com abertura direta por hiperosmolalidade (*hyperosmolality-gated calcium channel*).
  - Demonstração de que *osca1* perde o influxo rápido de $Ca^{2+}$ ($OICI_{cyt}$) sob choque osmótico e exibe murchamento foliar acelerado.
- **Relevância para a Tese:** É o artigo fundador de todo o arcabouço funcional do canal OSCA, base direta do Capítulo 2 e da Seção 4 da revisão.

---

## 7. Eixo Temático VII: Ecologia, Ecofisiologia e Evolução em Velloziaceae e Campos Rupestres

### 7.1. Alcantara et al. (2015) — *Functional Ecology*
- **Referência:** Alcantara, S., de Mello-Silva, R., Teodoro, G. S., Drequeceler, K., Ackerly, D. D., & Oliveira, R. S. (2015). Carbon assimilation and habitat segregation in resurrection plants: a comparison between desiccation- and non-desiccation-tolerant species of Neotropical Velloziaceae. *Functional Ecology*, 29(12), 1499–1508.
- **Sistema / Modelo Biológico:** 8 espécies de Velloziaceae simpátricas nos campos rupestres da Serra do Cipó (incluindo pares DT vs. não-DT).
- **Abordagem Metodológica:** Ecofisiologia de campo e casa de vegetação (trocas gasosas $A/Ci$, fluorescência de clorofila, curvas de vulnerabilidade hidráulica e segregação de microhabitat).
- **Principais Achados:**
  - Demonstrou o trade-off ecológico fundamental: espécies tolerantes à dessecação possuem menores taxas máximas de fotossíntese ($A_{max}$) e menor crescimento anual, mas toleram desidratação letal em fendas de rocha; espécies não-DT mantêm fotossíntese contínua em solos mais profundos.
  - Estabeleceu a base ecológica do par comparativo *V. tubiflora* (DT) vs. *V. peripherica* (não-DT).
- **Relevância para a Tese:** Fundamentação direta da hipótese ecológica da tese e da Tabela 1 da revisão.

---

### 7.2. Alcantara et al. (2018) — *Annals of Botany*
- **Referência:** Alcantara, S., Ree, R. H., & Mello-Silva, R. (2018). Accelerated diversification and functional trait evolution in Velloziaceae reveal new insights into the origins of the campos rupestres’ exceptional floristic richness. *Annals of Botany*, 122(1), 165–180.
- **Sistema / Modelo Biológico:** Filogenia molecular e traços funcionais de 142 espécies de Velloziaceae.
- **Abordagem Metodológica:** Filogenética comparativa, modelos macroevolutivos de especiação/extinção (BAMM, BioGeoBEARS) e reconstrução de estados ancestrais.
- **Principais Achados:**
  - Radiação adaptativa explosiva de Velloziaceae impulsionada pela especialização edáfica nos campos rupestres.
  - A dessecação e os traços de resistência à seca surgiram e se diversificaram repetidamente em linhagens neotropicais.
- **Relevância para a Tese:** Contexto macroevolutivo da diversificação de Velloziaceae na Seção 1.

---

### 7.3. Teodoro et al. (2019) — *Functional Ecology*
- **Referência:** Teodoro, G. S., Lambers, H., Nascimento, D. L., et al. (2019). Specialized roots of Velloziaceae weather quartzite rock while mobilizing phosphorus using carboxylates. *Functional Ecology*, 33(5), 762–773.
- **Sistema / Modelo Biológico:** *Vellozia* e *Barbacenia* nos campos rupestres.
- **Abordagem Metodológica:** Morfologia e histoquímica radicular, cromatografia iônica de exsudatos radiculares e microscopia eletrônica de rochas intemperizadas.
- **Principais Achados:**
  - Caracterização das raízes vellozioides especializadas na exsudação maciça de carboxilatos (citrato e malato) para intemperismo de rochas de quartzo e absorção de fósforo indisponível.
- **Relevância para a Tese:** Embasamento da Seção 1 sobre adaptações nutricionais e radiculares em solos oligotróficos.

---

### 7.4. De Mello-Silva (2005) — *Botanical Journal of the Linnean Society*
- **Referência:** De Mello-Silva, R. (2005). Morphological analysis, phylogenies and classification in Velloziaceae. *Botanical Journal of the Linnean Society*, 148(2), 157–173.
- **Sistema / Modelo Biológico:** Família Velloziaceae (gêneros *Vellozia*, *Barbacenia*, *Xerophyta*, *Pleurostima*, *Nanuza*).
- **Abordagem Metodológica:** Cladística morfológica e anatômica abrangente da família.
- **Principais Achados:**
  - Estabeleceu a sistemática filogenética e os limites genéricos modernos de Velloziaceae.
- **Relevância para a Tese:** Autoridade taxonômica e sistemática para a circunscrição de *Vellozia*.
