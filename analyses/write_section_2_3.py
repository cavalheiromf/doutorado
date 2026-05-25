import os
import docx

docs_dir = "/home/mfcaval/github/doutorado/docs"
os.makedirs(docs_dir, exist_ok=True)

content = """# REVISÃO BIBLIOGRÁFICA: SEÇÕES 2 E 3

## Mecanismos de Osmopercepção e Canais Mecanossensíveis em Plantas

---

### Seção 2. Mecanismos de Osmopercepção em Plantas

A percepção do status hídrico do ambiente pelas células vegetais é o evento primário que precede todas as cascatas de adaptação bioquímica ao déficit de água. De acordo com a revisão integrativa de Gorgues et al. (2022) e análises filogenéticas recentes de osmosensoriamento (Rawat et al., 2025), a detecção celular do estresse osmótico é dividida em três classes principais de mecanismos:

#### 2.1. Sensores de Membrana: A Via das Histidina Quinases
Os sistemas de sinalização de dois componentes baseados em histidina quinases foram os primeiros candidatos a osmossensores em plantas, inspirados no modelo bacteriano EnvZ/OmpR e de leveduras SLN1. 
*   **AtHK1 (*Arabidopsis thaliana* Histidine Kinase 1)**: Localizado na membrana plasmática, o AtHK1 atua como um regulador positivo das respostas ao estresse hídrico e salino, disparando cascatas de fosforilação que regulam genes responsivos à seca via sinalização do ácido abscísico (ABA) (Osakabe et al., 2013; Tran et al., 2007).
*   **Controvérsias**: Entretanto, o papel do AtHK1 como o osmossensor primário e universal em plantas tem sido severamente questionado. Estudos de perda de função demonstraram que mutantes de *Arabidopsis* nulos para *athk1* não apresentam fenótipos anômalos evidentes em sinalização hiperosmótica basal (Kumar et al., 2013). Isso sugere a existência de redundância funcional ou de vias mecanossensoriais paralelas mais sensíveis.

#### 2.2. Sensores de Integridade da Parede Celular: A Família RLK
A parede celular das plantas é uma barreira mecânica dinâmica intimamente conectada à membrana plasmática. Sob déficit hídrico, a diminuição da pressão de turgor celular altera a tensão mecânica e as conexões físicas entre a parede e a membrana, disparando sensores de integridade da parede celular (*Cell Wall Integrity - CWI*):
*   **Receptor-Like Kinases (RLKs)**: Destacam-se as quinases semelhantes a CrRLK1 (de *Catharanthus roseus*), quinases associadas à parede (WAKs), quinases de lectina (LRKs) e quinases semelhantes a extensina ricas em prolina (PERKs) (Wolf et al., 2012).
*   **THESEUS1 (THE1)**: Este receptor CWI modula a rigidez celular e atua coordenando o acúmulo de ABA e a resposta celular a deformações mecânicas sob estresse osmótico (Bacete et al., 2022).
*   **FERONIA (FER)**: Um dos moduladores mais importantes do CWI. Sob estresse salino ou hídrico, a FERONIA induz um influxo tardio de cálcio citosólico essencial para desencadear o reforço estrutural da parede vegetal (Feng et al., 2018). Estudos sugerem que o sensor FERONIA detecta a deformação física induzida pela perda de turgor nas pectinas da parede celular, acoplando estresse físico a cascatas químicas de proteção (Chen et al., 2016; Feng et al., 2018).

#### 2.3. Sensores de Tensão de Membrana Plasmática
A terceira e mais rápida classe de sensores consiste de canais iônicos ativados diretamente por estiramento mecânico da bicamada lipídica. Variações na pressão osmótica do meio induzem fluxo de água, alterando o volume celular e, consequentemente, a tensão física da membrana plasmática. Essa força de estiramento abre mecanicamente canais permeáveis a cátions, funcionando como transdutores instantâneos de sinal mecânico em sinal elétrico e químico.

---

### Seção 3. Canais Mecanossensíveis e Sinalização por Cálcio

#### 3.1. O Cálcio citosólico ([Ca²⁺]i) como Mensageiro Secundário e a "Assinatura de Cálcio"
O influxo de íons cálcio através da membrana plasmática é a resposta molecular mais rápida e universal das plantas a estímulos mecânicos, como toque, vento, ferimento e estresse osmótico (White, 2003; Jin et al., 2025). As diferentes intensidades, durações e localizações celulares dessas elevações de [Ca²⁺]i definem as denominadas **"Assinaturas de Cálcio"** (*calcium signatures*), que são decodificadas por proteínas sensores (como CDPKs, CBLs e calmodulinas) para ativar programas transcricionais específicos no núcleo (Guerringue et al., 2026; Zhou et al., 2025).

#### 3.2. As Famílias de Canais Mecanossensíveis em Plantas
Várias famílias de canais iônicos operados por estiramento mecânico participam da transdução inicial de estresse hídrico em plantas:

##### A. Canais MscS-Like (MSL)
Baseados nos homólogos bacterianos MscS (Mechanosensitive Channel of Small Conductance), os MSLs regulam o potencial eletroquímico celular.
*   **MSL10**: O canal mais estudado, atua como um canal ativado por estiramento com preferência por ânions, mediando respostas ao estresse hipo-osmótico celular (Maksaev & Haswell, 2012).
*   **O Caso da Dioneia (*Dionaea muscipula*)**: Estudos revolucionários recentes demonstraram que o homólogo **DmMSL10/FLYC1** é o sensor tátil de alta sensibilidade localizado nos pelos gatilho da planta carnívora. Ele gera o potencial de receptor (*receptor potential - RP*) que dispara os potenciais de ação de cálcio de longo alcance para capturar as presas (Suda et al., 2025). Esse achado eleva o papel dos MSLs como transdutores mecânicos primários ultrarrápidos em plantas.

##### B. Canais MCA (Mid1-Complementing Activity)
Os canais MCA1 e MCA2 são proteínas exclusivas de plantas que promovem o influxo de cálcio induzido por estresse de gravidade, toque e crescimento radicular no solo (Nakagawa et al., 2007). Embora mutantes *mca1/mca2* não apresentem defeitos claros no influxo imediato induzido por choque osmótico (Yamanaka et al., 2010), eles participam de forma coordenada no sensoriamento físico de rigidez em tecidos subterrâneos.

##### C. Canais PIEZO
Homólogos aos canais PIEZO de mamíferos (descobertos por Patapoutian), os canais PIEZO de plantas são sensores de grande peso molecular que regulam o crescimento radicular adaptativo ao penetrar obstáculos físicos no solo. Descobriu-se recentemente que o **PIEZO1** atua como um hub de *mecanoimunidade* em plantas, convertendo as forças mecânicas geradas pela picada de insetos vetores (como moscas-brancas) em sinais rápidos de cálcio que ativam as defesas da planta (Huang et al., 2026). Ele também coordena vias fitohormonais de auxina e giberelina sob sinalizações combinadas de luz azul e campos magnéticos (Peng et al., 2025).

##### D. Canais RMA (Rapid Mechanically Activated)
Publicado muito recentemente na *New Phytologist*, o canal **RMA** (*Rapid Mechanically Activated*) foi caracterizado como um canal permeável a Ca²⁺ e ativado por força que reside na membrana plasmática. Utilizando patch-clamp, Guerringue et al. (2026) demonstraram que o RMA ativa instantaneamente em resposta à tensão de membrana e sofre inativação rápida, funcionando como um filtro de passagem de banda eletrofisiológico que transduz estímulos mecânicos de alta frequência na membrana plasmática.

#### 3.3. A Transição para a Família OSCA
Apesar da diversidade de canais mecanossensíveis listados, a maioria (como os MSLs) apresenta preferência por ânions ou atua sob limiares mecânicos elevados. O sensoriamento fino de hiperosmolaridade celular induzido especificamente por desidratação severa e estresse salino dependia da identificação de canais de cálcio de ativação rápida sob estiramento. Essa lacuna fisiológica levou à identificação da família **OSCA**, cujas propriedades de gating mecânico e poros revestidos por lipídeos os consagraram como os osmossensores mecânicos fundamentais do reino vegetal, conectando a deformação física da membrana à resposta transcricional da tese.
"""

# Save TXT
txt_path = os.path.join(docs_dir, "02_03_signaling_review.txt")
with open(txt_path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Saved TXT to: {txt_path}")

# Save DOCX
docx_path = os.path.join(docs_dir, "02_03_signaling_review.docx")
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
