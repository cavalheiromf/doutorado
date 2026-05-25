import os
import docx

docs_dir = "/home/mfcaval/github/doutorado/docs"
os.makedirs(docs_dir, exist_ok=True)

content = """# REVISÃO BIBLIOGRÁFICA: SEÇÃO 4

## A Família Gênica OSCA e sua Arquitetura Molecular Tridimensional

### 4.1. Descoberta e Identificação da Família OSCA
A percepção da osmolaridade em plantas terrestres permaneceu, por décadas, como uma das maiores lacunas da fisiologia vegetal. Esse cenário mudou drasticamente em 2014, quando o grupo de Patapoutian (Yuan et al., 2014) identificou a proteína OSCA1.1 em *Arabidopsis thaliana* como o primeiro canal de cálcio permeável e ativado diretamente por hiperosmolaridade celular. O gene foi classificado como um sensor osmótico mecânico essencial, capaz de transduzir o estresse físico da membrana em um influxo rápido de cálcio citosólico ([Ca²⁺]i).

Estudos subsequentes revelaram que os genes OSCA codificam proteínas transmembrana conservadas evolutivamente, caracterizadas pela presença do domínio **PF02714** (anteriormente DUF221 ou RSN1_7TM) da família de proteínas Pfam, frequentemente flanqueado pelos domínios auxiliares **PF13967** (RSN1 TM, domínio transmembrana) e **PF14703** (PHM7 cyt, domínio citosólico). Essa família é amplamente distribuída em eucariotos, incluindo homólogos em animais (denominados TMEM63), sugerindo um papel ancestral fundamental na mecanossensibilidade celular (Murthy et al., 2018; Hou et al., 2014).

---

### 4.2. A Revolução Estrutural por Criomicroscopia Eletrônica (Cryo-EM)
A compreensão do mecanismo físico de ativação dos canais OSCA avançou rapidamente com a elucidação das primeiras estruturas tridimensionais de alta resolução obtidas por criomicroscopia eletrônica (Cryo-EM) a partir de 2018 (Jojoa-Cruz et al., 2018; Zhang et al., 2018). 

A estrutura de **OSCA1.2** de *Arabidopsis thaliana* e *Oryza sativa* revelou que esses canais se organizam como **homodímeros simétricos**, exibindo uma arquitetura única composta por 11 hélices transmembranares (TM1 a TM11) por subunidade. Surpreendentemente, as análises revelaram uma homologia estrutural marcante com a superfamília de proteínas TMEM16 (canais de cloreto ativados por cálcio e escramblases de lipídeos) e com as proteínas TMC (Transmembrane Channel-like), sugerindo uma origem evolutiva compartilhada para a mecanossensibilidade em eucariotos.

---

### 4.3. O Mecanismo de Abertura Mecânica (Gating) e a Teoria do Poro Revestido por Lipídeos
Diferente dos canais iônicos clássicos controlados por ligantes químicos ou voltagem, os canais OSCA respondem diretamente à **tensão da bicamada lipídica** decorrente da perda de turgor celular ou hiperosmolalidade. Pesquisas estruturais de altíssimo impacto publicadas recentemente refinaram drasticamente o nosso entendimento sobre este mecanismo de abertura:

1.  **O Domínio "Cytoplasmic Beam" (Alavanca Citosólica)**: Localizado na interface intracelular, um longo domínio helicoidal atua como uma alavanca mecânica direta. Variações na tensão ou espessura da membrana deformam essa hélice, amplificando o sinal físico e puxando as hélices transmembranares do poro para abrir o canal (Jojoa-Cruz et al., 2018).
2.  **O Acoplamento Mecânico e Lipídeos Moduladores ("Plug Lipids")**: Zhang et al. (2023) identificaram que a cavidade central criada na interface dimérica dos canais OSCA/TMEM63 acomoda lipídeos específicos da bicamada que controlam a sensibilidade à força. Além disso, o lado citosólico do poro fechado é bloqueado por um "lipídeo tampão" (*plug lipid*), que impede a passagem de íons em estado de repouso celular.
3.  **O Poro Revestido por Lipídeos ("Lipid-Lined Pore")**: Em um achado revolucionário publicado na *Nature*, Han et al. (2024) demonstraram que a ativação mecânica dos canais OSCA abre um caminho de condução iônica que é, na verdade, **revestido por lipídeos** da própria membrana na sua conformação aberta, permitindo um influxo rápido e massivo de cátions divalentes (especialmente Ca²⁺).
4.  **Atividade Dual: Canal Iônico e Escramblase de Lipídeos**: Consolidando a homologia com a família TMEM16, estudos de 2026 (Lin et al., 2026) revelaram que os canais OSCA1.1, OSCA1.2 e OSCA2.2 atuam de forma dual como **canais iônicos mecanossensíveis e escramblases de lipídeos ativadas por força**, translocando fosfolipídeos através de seus poros abertos para aumentar a resiliência mecânica da membrana plasmática sob estresse físico severo.

---

### 4.4. A Importância da Dimerização na Sensibilidade Mecânica
Uma descoberta evolutiva crucial para a interpretação dos dados da sua tese diz respeito ao papel do **segundo linker intracelular (IL2)**. Pesquisas recentes (Zheng et al., 2023) mostraram que, enquanto os homólogos de mamíferos (TMEM63) atuam frequentemente como monômeros de alta ativação (limiar de força elevado), as proteínas OSCA de plantas evoluíram um domínio IL2 altamente especializado que estabiliza a **dimerização estável**. 

Mutações no domínio IL2 que forçam o canal OSCA a se comportar como monômero elevam drasticamente o limiar de força necessário para a sua abertura física (Zheng et al., 2023). Isso demonstra que a dimerização dos canais OSCA em plantas é um requisito essencial para garantir que os sensores consigam detectar variações extremamente sutis de pressão osmótica diária e sazonal.

---

### 4.5. Conexão com os Dados da Tese (*V. peripherica* vs. *V. tubiflora*)
Esta fundamentação estrutural de ponta dá suporte direto para explicar os dados experimentais da sua tese:
*   **O Cluster OSCA1.3/1.4/1.5**: O alto grau de conservação deste cluster tandem no cromossomo 7A de ambas as espécies pode estar associado à necessidade de manter a estabilidade física de canais constituintes da base estrutural da "Track Conservada" do osmosensoriamento.
*   **Os 14 Sítios Contrast-FEL em OSCA2 em Vper**: Os sítios sob seleção positiva acelerada em *V. peripherica* mapeiam-se prioritariamente nas regiões expostas à bicamada lipídica e na alavanca citosólica (*beam domain*), sugerindo que a sempre-verde remodelou ativamente a "alavanca" e as regiões sensíveis à tensão lipídica para ajustar a cinética de abertura fina dos canais.
*   **O Sítio Hotspot 593 em Vtub**: Localizado no domínio transmembrana de abertura, este sítio sob forte relaxamento em *V. tubiflora* pode representar um ponto chave de plasticidade estrutural, permitindo que a proteína sofra desidratação extrema sem perder a integridade estrutural, facilitando o rápido acoplamento com a bicamada lipídica no momento da reidratação celular pós-dessecação.
"""

# Save TXT
txt_path = os.path.join(docs_dir, "04_osca_structure_review.txt")
with open(txt_path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Saved TXT to: {txt_path}")

# Save DOCX
docx_path = os.path.join(docs_dir, "04_osca_structure_review.docx")
doc = docx.Document()
lines = content.split('\n')
for line in lines:
    if line.startswith('# '):
        doc.add_heading(line[2:], level=1)
    elif line.startswith('## '):
        doc.add_heading(line[3:], level=2)
    elif line.startswith('### '):
        doc.add_heading(line[4:], level=3)
    elif line.startswith('#### '):
        doc.add_heading(line[5:], level=4)
    elif line.startswith('*   '):
        doc.add_paragraph(line[4:], style='List Bullet')
    elif line.startswith('-   '):
        doc.add_paragraph(line[4:], style='List Bullet')
    elif line.strip() == '---':
        doc.add_paragraph('────────────────────────────────────────')
    else:
        doc.add_paragraph(line)
        
doc.save(docx_path)
print(f"Saved DOCX to: {docx_path}")
