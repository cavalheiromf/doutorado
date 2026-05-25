import os
import docx

docs_dir = "/home/mfcaval/github/doutorado/docs"
os.makedirs(docs_dir, exist_ok=True)

content = """# REVISÃO BIBLIOGRÁFICA: SEÇÃO 1

## Contexto Ecológico e Fisiológico: O Cenário dos Campos Rupestres e o Gênero *Vellozia*

### 1.1. Campos Rupestres: Estresse Hídrico Sazonal e Radiação Extrema
Os Campos Rupestres brasileiros constituem uma ecorregião montanhosa de megadiversidade e elevado endemismo, localizada principalmente ao longo da Cadeia do Espinhaço, na porção oriental do Brasil. Trata-se de um ecossistema fascinante, porém extremamente hostil, caracterizado por altitudes superiores a 900 metros, solos quartzo-arenosos altamente intemperizados, ácidos e extremamente deficientes em nutrientes essenciais como o fósforo (Oliveira et al., 2016; Alcantara et al., 2018).

Além das severas limitações nutricionais do solo, a vegetação dos Campos Rupestres é submetida a um regime microclimático drástico:
*   **Sazonalidade Hídrica Pronunciada**: Alternância marcante entre uma estação chuvosa curta e uma estação seca prolongada que pode durar de quatro a cinco meses sem qualquer precipitação significativa.
*   **Radiação Solar Extrema e Flutuações Térmicas**: A elevada altitude e a ausência de dossel florestal expõem a vegetação a altíssimos níveis de radiação ultravioleta incidente durante o dia, acompanhados de resfriamento radiativo acentuado à noite.
*   **Ventos Fortes**: Que aceleram a evapotranspiração foliar e intensificam a perda de água do solo raso.

Para sobreviver a esse complexo de estresses abióticos simultâneos, as linhagens vegetais residentes evoluíram um arsenal diversificado de adaptações morfo-fisiológicas e metabólicas estruturais, tornando os Campos Rupestres um laboratório natural único para o estudo da ecofisiologia vegetal e da biologia molecular adaptativa (Alcantara et al., 2018; Pinto et al., 2025).

---

### 1.2. Dicotomia Fisiológica de Sobrevivência no Gênero *Vellozia*
Dentre os táxons botânicos que dominam a paisagem dos Campos Rupestres, a família **Velloziaceae** (Pandanales) destaca-se como um elemento ecológico e evolutivo dominante (Alcantara et al., 2018). Dentro desta família, o gênero *Vellozia* evoluiu caminhos adaptativos extraordinários e radicalmente divergentes para contornar ou tolerar a severa restrição de água no solo. As duas espécies-modelo investigadas nesta tese exemplificam perfeitamente essa dicotomia adaptativa:

#### A. Vellozia tubiflora: A Estratégia da Tolerância à Dessecação (Desiccation Tolerance)
*   **Fenótipo**: Conhecida classicamente como "planta de ressurreição" (resurrection plant), a *V. tubiflora* tolera a perda de até 95% do conteúdo hídrico celular em seus tecidos vegetativos sem sofrer danos letais (Gaff, 1987; Alcantara et al., 2015).
*   **Fisiologia**: Durante os meses de seca severa, a planta inicia um programa genético de desidratação controlada. Suas folhas e raízes dessecam por completo, degradando a clorofila (comportamento poiquilohidrofílico) e interrompendo as atividades fotossintéticas e respiratórias ativas (Nadal et al., 2023).
*   **Anidrobiose**: A planta entra em um estado de "vida suspensa" ou **anidrobiose**, caracterizado pelo acúmulo massivo de solutos compatíveis (como açúcares da família da rafinose - RFOs, prolina e aminoácidos de estresse como o GABA), chaperonas protetoras (proteínas LEA e desidrinas) e sistemas antioxidantes enzimáticos potentes (CAT, APX) que evitam o colapso celular por estresse oxidativo (Suguiyama et al., 2014; Vieira et al., 2022).
*   **Recuperação**: Ao cair das primeiras chuvas, a integridade de suas membranas e organelas permite que a planta reidrate rapidamente e retome seu metabolismo ativo e capacidade fotossintética em poucas horas, ressurgindo do estado dormente.

#### B. Vellozia peripherica: A Estratégia Sempre-verde de Evitação da Desidratação (Dehydration Avoidance)
*   **Fenótipo**: Em contraposição à ressurreição, a *V. peripherica* adota uma estratégia baseada na **evitação da dessecação**, mantendo suas folhas verdes, turgidas e fisiologicamente ativas mesmo após meses de estiagem contínua nos afloramentos rochosos (Pinto et al., 2025).
*   **Fisiologia**: Esta espécie evita a desidratação por meio de uma regulação hídrica extremamente ativa e morfoanatomia especializada. Suas folhas possuem cutículas espessas, células mucilaginosas com alta capacidade de retenção de água e sistemas vasculares protegidos (Vieira et al., 2022).
*   **Controle Estomático Fino**: Seus estômatos atuam como "válvulas de segurança" de altíssima sensibilidade (Nadal et al., 2023), fechando imediatamente aos primeiros sinais de déficit hidrostático para evitar a ocorrência de embolia no xilema, permitindo que a planta sustente o turgor celular interno próximo a 80-90% e evite flutuações severas em seu status de água.

---

### 1.3. O Enigma Molecular: Como as Duas Estratégias Percebem a Água?
Essa marcante divergência fisiológica entre *V. tubiflora* (anidrobiose passiva / binária) e *V. peripherica* (regulação hídrica ativa / dinâmica diária) levanta uma questão evolutiva profunda:

> **Será que a maquinaria sensorial primária que detecta as variações de água plasmáticas também evoluiu de maneira diferente nestas duas linhagens?**

A percepção de estresse hídrico depende do turgor mecânico e da tensão da bicamada lipídica. Enquanto a sempre-verde *V. peripherica* precisa de um monitoramento contínuo, oscilatório e extremamente sensível para guiar a transpiração e o fechamento estomático a cada hora, a planta de ressurreição *V. tubiflora* necessita de uma detecção que ative o programa protetor e, em seguida, permita o silenciamento funcional mecânico durante a dessecação completa.

Esta dicotomia de estilo de vida estabelece a justificativa perfeita para investigar a família de canais iônicos mecanossensíveis **OSCA** em nível genômico comparativo nessas duas espécies, fornecendo o cenário molecular ideal para compreender como forças de seleção natural concorrentes (relaxamento seletivo vs. aceleração adaptativa) esculpiram o aparato sensorial primário das plantas terrestres.
"""

# Save TXT
txt_path = os.path.join(docs_dir, "01_campos_rupestres_review.txt")
with open(txt_path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Saved TXT to: {txt_path}")

# Save DOCX
docx_path = os.path.join(docs_dir, "01_campos_rupestres_review.docx")
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
