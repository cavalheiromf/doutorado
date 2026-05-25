import os
import docx

docs_dir = "/home/mfcaval/github/doutorado/docs"
os.makedirs(docs_dir, exist_ok=True)

content = """# REVISÃO BIBLIOGRÁFICA: SEÇÃO 6

## Dinâmica Evolutiva e Pressões de Seleção Molecular na Família OSCA

A evolução molecular de famílias de genes associadas ao sensoriamento ambiental é fortemente moldada pelas pressões ecológicas enfrentadas pelas linhagens. Na transição filogenética para ambientes com restrições extremas de água, a maquinaria osmosensorial de plantas pode seguir diferentes trajetórias evolutivas. 

Esta seção revisa as bases teóricas de modelagem evolutiva aplicadas à família OSCA na tese, detalhando a dinâmica de seleção purificadora, o modelo inovador de **"Dual-Track Evolution"** revelado pelo método HyPhy RELAX, e a caracterização sítio-específica por meio do Contrast-FEL.

---

### 6.1. Taxas de Substituição de Códons (Ka/Ks) e Restrição Funcional
A estimativa da razão entre taxas de substituições não-sinônimas (Ka) e sinônimas (Ks) é o método clássico para inferir a natureza da seleção natural atuando sobre sequências codificantes de proteínas (Suyama et al., 2006; Yang, 2007). 

Em nível global, a família gênica OSCA in *Vellozia* é governada por uma robusta **seleção purificadora** (Ka/Ks < 1.0, com uma média de ~0.35 para os pares ortólogos). Essa assinatura conservativa demonstra que a estrutura geral dos canais mecanossensíveis é mantida sob severa restrição funcional, onde mutações que alterem drasticamente a conformação proteica do poro ou dos domínios reguladores são desvantajosas e eliminadas pela seleção natural.
*   **O Caso Extremo de OSCA2.3**: O par ortólogo `VpOSCA2.3_VtOSCA2.3` exibe a taxa de Ka/Ks mais baixa de toda a família (Ka/Ks = 0.053). Essa restrição molecular sugere uma função biológica primária e altamente especializada que não tolera qualquer desvio estrutural na sequência de aminoácidos.
*   **A Aceleração Localizada de OSCA1.4**: Em contrapartida, o par `VpOSCA1.4_VtOSCA1.4` exibe uma taxa de Ka/Ks excepcionalmente elevada (0.80), sugerindo que este membro do cluster em tandem no Chr7A experimenta um relaxamento seletivo ou divergência funcional acelerada pós-especiação.

---

### 6.2. O Modelo "Dual-Track Evolution" (HyPhy RELAX)
A modelagem clássica de Ka/Ks global é incapaz de detectar se a intensidade da seleção natural mudou de forma direcional entre as linhagens estudadas. Para responder a essa questão biológica central, a tese implementou o método **HyPhy RELAX** (Wertheim et al., 2015), utilizando a espécie sempre-verde *V. peripherica* (Vper) como linhagem de Referência e a planta de ressurreição *V. tubiflora* (Vtub) como linhagem de Teste. 

O RELAX estima o parâmetro de intensidade de seleção ($K$). Valores de $K < 1.0$ indicam um relaxamento seletivo em direção à neutralidade ($Ka/Ks \\\\to 1.0$) na linhagem de teste, enquanto $K > 1.0$ indica uma intensificação da seleção (seja purificadora ou diversificadora). Os resultados revelaram um comportamento evolutivo altamente heterogêneo entre as subfamílias OSCA, fundamentando o modelo conceitual de **Dual-Track Evolution**:

```
                       ┌──► OSCA1 (K = 0.92, p = 0.60): Track Conservada (Purificação idêntica)
                       │
Ancestral Vellozia OSCA─┤
                       │
                       └──► OSCA2/3+4 (K < 0.30): Track Divergente (Relaxamento drástico em Vtub)
```

#### A. A Track Conservada (Subfamília OSCA1)
*   **Resultado**: O clado OSCA1 (composto por 10 genes) apresentou uma intensidade de seleção equivalente em ambas as espécies ($K = 0.92$, $p = 0.60$).
*   **Interpretação**: A subfamília OSCA1 abriga o cluster tandem estruturalmente conservado `OSCA1.3/1.4/1.5` no Chr7A e os principais sensores de turgor. Esse clado representa a "Track Conservada" do osmossensoriamento basal. Independentemente de a espécie evitar a desidratação (sempre-verde) ou tolerá-la por completo (ressurreição), o sensor básico primário de presença de água celular é uma maquinaria não-maleável que precisa ser preservada de forma invariável sob forte seleção purificadora nas duas espécies.

#### B. A Track Divergente (Subfamílias OSCA2 e OSCA3+4)
*   **Resultado**: A subfamília OSCA2 (11 genes) exibiu um relaxamento seletivo maciço e altamente significativo em *V. tubiflora* ($K = 0.28$, $p = 3.4 \\\\times 10^{-5}$). Paralelamente, o clado OSCA3+4 (6 genes) exibiu uma assinatura equivalente de relaxamento severo nesta espécie ($K = 0.13$, $p = 0.006$).
*   **Fisiologia e Significado Evolutivo**: Esse relaxamento seletivo correlaciona-se elegantemente com a ecofisiologia da planta de ressurreição. Durante os prolongados períodos de seca extrema nos Campos Rupestres, a *V. tubiflora* desidrata e entra em **anidrobiose**, desativando completamente o seu metabolismo celular. No estado de dormência seca, a água livre está ausente e os canais mecanossensíveis OSCA2 e OSCA3+4 permanecem fisicamente silenciados, não realizando qualquer trabalho fisiológico. Em termos evolutivos, a ausência de atividade funcional prolongada "desliga" temporariamente a cobrança da seleção natural sobre a estrutura dos canais. Sem pressão seletiva para manter os resíduos estruturalmente otimizados, essas duas subfamílias acumulam mutações neutras por deriva (drift), manifestando-se na assinatura matemática de relaxamento evolutivo severo ($K \\\\ll 1.0$).

---

### 6.3. Divergência Sítio-Específica (HyPhy Contrast-FEL)
Para refinar a resolução do Dual-Track em nível de resíduos individuais de aminoácidos, a tese utilizou o método **HyPhy Contrast-FEL** (Kosakovsky Pond et al.), que avalia a ocorrência de divergência nas taxas não-sinônimas sítio por sítio entre as duas linhagens.

#### A. Aceleração Adaptativa e Remodelamento em *V. peripherica* (OSCA2)
No clado OSCA2, o teste identificou **14 sítios de divergência significativa**, onde **todos os 14 resíduos apresentaram aceleração seletiva extrema exclusivamente na sempre-verde *V. peripherica*** (beta_Ref >> 0, beta_Test approx 0). 
*   **Significado**: Ao contrário do relaxamento de Vtub, a espécie sempre-verde Vper é submetida a uma pressão evolutiva contínua de refinamento. Para manter suas folhas verdes e turgidas, a *V. peripherica* depende de um monitoramento hidrostático ultra-sensível e de respostas dinâmicas diárias de regulação de turgor. A seleção natural acelera a evolução desses 14 resíduos chave em Vper para remodelar a conformação mecânica e o gating de seus canais OSCA2, adaptando-os à sua estratégia de evitação ativa.

#### B. O Hotspot de Sobrevivência 593 em *V. tubiflora* (OSCA3+4)
No clado OSCA3+4, o Contrast-FEL expôs um único resíduo na posição local 593 com aceleração adaptativa gigantesca em Vtub (beta_Test = 24.72, beta_Ref = 0.018, p = 0.009).
*   **Significado**: Longe de representar mero desvio neutro, esse resíduo pontual localizado no domínio transmembrana do poro pode ser uma **adaptação molecular específica da poiquilohidria**. Sugere-se que essa alteração sítio-específica estabiliza a proteína OSCA no estado seco, prevenindo o colapso e facilitando a rápida ativação e abertura do poro no momento crítico de reidratação celular, funcionando como um gatilho de reativação mecânica da ressurreição.
"""

# Save TXT
txt_path = os.path.join(docs_dir, "06_evolutionary_dynamics_review.txt")
with open(txt_path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Saved TXT to: {txt_path}")

# Save DOCX
docx_path = os.path.join(docs_dir, "06_evolutionary_dynamics_review.docx")
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
