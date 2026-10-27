# Capítulo Macroevolução (Revisão — 6 Monocotiledôneas)

Este diretório concentra a análise comparativa revisada de **Velloziaceae** sem o grupo externo distante *Arabidopsis thaliana* (`Ath`) na modelagem de famílias gênicas (`CAFE5`), preservando as idades calibradas por relógio molecular (`MCMCTree`) nos 6 táxons de monocotiledôneas:
- **Gênero focal (*Vellozia*):**
  - `Vper` (*Vellozia peripherica*): Estratégia **sempre-verde / evitadora de desidratação (*avoidant*)**
  - `Vtub` (*Vellozia tubiflora*): Estratégia **tolerante à dessecação (DT)**
- **Linhagens basais de Velloziaceae (DT):**
  - `Xvis` (*Xerophyta viscosa*, África)
  - `Abra` (*Acanthochlamys bracteata*, Ásia)
- **Grupos externos em Monocotiledôneas:**
  - `Ptec` (*Pandanus tectorius*, Pandanales)
  - `Dala` (*Dioscorea alata*, Dioscoreales — raiz das 6 monocotiledôneas em 121.90 Ma)

---

## Estrutura de Diretórios

```text
chapter_macroevolution_review/
├── 00_data/                       # Genomas, GFFs e proteomas das espécies e outgroups
├── 01_orthology/                  # Resultados do OrthoFinder (Orthogroups e árvores gênicas)
├── 03_dating/                     # Cadeias MCMCTree e cronograma ultramétrico podado (6 táxons)
│   └── final_trees/
│       └── velloziaceae_6taxa_ultrametric.tre
├── 04_gene_families/
│   ├── cafe5/                     # Insumos, modelos de lambda, logs SLURM, runs e sumários AIC/LRT
│   ├── synteny/                   # Âncoras sintênicas (JCVI) e classificação de duplicações (MCScanX)
│   └── functional_enrichment/     # Anotações GO/InterPro e enriquecimento funcional das expansões
└── workflow/
    └── scripts/
        ├── 01_cafe5/                  # Etapa 1: Preparação e modelagem birth-and-death (CAFE5)
        ├── 02_duplications_synteny/   # Etapa 2: Modos de duplicação (MCScanX/JCVI) x Expansões CAFE5
        └── 03_functional_enrichment/  # Etapa 3: Enriquecimento funcional (GO) e redução de redundância
```

---

## Ordem de Execução dos Scripts (`workflow/scripts/`)

### Módulo 1: Expansão e Contração de Famílias Gênicas (`01_cafe5/`)
1. `01_prepare_6taxa_inputs.py`: Gera a árvore ultramétrica de 6 táxons, as árvores de hipóteses (`M2` a `M5`) e filtra `Orthogroups.GeneCount.tsv` (removendo `Ath` e separando famílias $\ge 100$ cópias).
2. `02_run_cafe5_stage1_error_model.slurm`: Executa 5 réplicas Base sem erro e 5 réplicas com estimativa de erro (`-e`), selecionando o `selected_error_model.txt`.
3. `03_run_cafe5_stage2_gamma_models.slurm`: Executa 5 réplicas para Gamma $k=2$ e $k=3$ (1-$\lambda$ nos ramos + erro fixado).
4. `04_run_cafe5_stage3_branch_lambdas.slurm`: Executa os modelos multi-$\lambda$ sem heterogeneidade Gamma, mantidos como análise de comparação histórica.
5. `06_run_cafe5_stage4_gamma_branch_lambdas.slurm`: Executa cinco réplicas de M2–M5 combinando Gamma $k=3$ e heterogeneidade entre ramos.
6. `07_run_cafe5_m5_gamma_reps6_10.slurm`: Acrescenta cinco inicializações independentes de M5+Gamma na partição `short`.
7. `05_evaluate_cafe5_models.py`: Compila as réplicas com a precisão completa dos logs, calcula AIC e $\Delta\text{AIC}$ e gera o sumário de convergência de M5.

### Módulo 2: Sintenia e Modos de Duplicação (`02_duplications_synteny/`)
1. `01_jcvi_mcscan.ipynb` & `02_update_jcvi_mcscan.py`: Alinhamento colinear via `LAST` e `JCVI`.
2. `03_classify_gene_duplications.py`: Classificação de todos os genes de `Vper` e `Vtub` via `duplicate_gene_classifier` (`Singleton`, `Dispersed`, `Proximal`, `Tandem`, `WGD/Segmental`).
3. `04_extract_expansions_and_duplications.py`: Extrai as famílias significativamente expandidas/contraídas ($p < 0.05$) em `Vper` (*avoidant*) e `Vtub` (DT) e aplica o Teste Exato de Fisher contra os modos de duplicação.
4. `05_test_expansion_duplication_association.py`: Testes estatísticos adicionais de associação entre expansão e modo de duplicação.
5. `06_audit_priority_copies.py` & `07_build_priority_gene_trees.sh`: Auditoria e árvores gênicas das famílias prioritárias.

### Módulo 3: Enriquecimento Funcional (`03_functional_enrichment/`)
0. `00_build_master_table_6taxa.py`: Constrói a tabela mestra (`04_gene_families/comparative_axes/comparative_families_master_table_v2.tsv`, 12.876 famílias presentes na raiz das seis monocotiledôneas) usando M5+Gamma réplica 4 como análise primária e a interseção das réplicas 4, 6 e 8 como controle de robustez.
1. `01_build_family_annotations.py`: Constrói anotações funcionais por ortogrupo (`TAIR10`/GO/KEGG).
2. `02_build_binary_term_matrix.py`: Gera matriz binária de termos GO/KEGG e estratos de permutação balanceados ($|\text{Adjusted SMD}| < 0.10$).
3. `03_run_enrichment.py`: Executa enriquecimento funcional exato de Fisher unilateral nas famílias expandidas/contraídas.
4. `04_run_stratified_permutations.py`: Validação por 10.000 permutações estratificadas pelo tamanho da família, número de loci em `Ath` e grau de anotação.
5. `05_reduce_go_redundancy.py`: Redução de redundância semântica dos termos GO enriquecidos.
6. `06_generate_summary_report.py` & `07_validate_outputs.py`: Geração do relatório final e auditoria dos 12 controles obrigatórios + balanço de covariáveis.
7. `09_run_enrichment_pipeline.sh`: Script SLURM integrador para rodar o módulo de enriquecimento de ponta a ponta.

---

## Principais Resultados (6 Monocotiledôneas — Sem `Ath` no CAFE5)

1. **M5+Gamma é o modelo selecionado e o ótimo foi reproduzido:** M5 apresentou $\text{AIC}=190.947,35$, com $\Delta\text{AIC}=43,63$ para M4 e $1.616,06$ para o modelo global Gamma $k=3$. As réplicas 4, 6 e 8 convergiram a menos de 0,1 unidade de $-\ln L$ entre si. A réplica 4 é a análise primária.
2. **A assimetria entre as espécies irmãs é robusta, mas a razão exata é limitada pela fronteira:** $\lambda_{Vper}=0,008204$ e $\lambda_{Vtub}=0,002092$, razão de aproximadamente 3,9. O valor de `Vper` atingiu o máximo permitido pela topologia nas três soluções próximas, de modo que a direção da diferença é mais segura que sua magnitude exata.
3. **Chamadas de ramo:** na réplica primária, `Vper` tem 217 expansões e 66 contrações, enquanto `Vtub` tem 50 expansões e 63 contrações. A interseção entre as réplicas 4, 6 e 8 preserva 199/62 eventos em `Vper` e 50/57 em `Vtub`.
4. **Duplicações locais predominam nas expansões de `Vper`:** genes Tandem (46,25%; OR = 9,50) e Proximais (20,22%; OR = 5,46) somam 66,47% dos 2.344 genes classificados nas 217 famílias expandidas; WGD/Segmental representa 12,16% (OR = 0,29). Em `Vtub`, as 50 famílias expandidas são dominadas por Singletons (42,64%; OR = 3,60).
5. **Enriquecimento funcional estratificado:** os 12 controles mandatórios foram aprovados. Entre os termos representativos confirmatórios estão resposta ao ácido salicílico nas expansões de `Vper` (OR = 7,41; $q=0,00133$; $p_{strat}=0,0232$), reconhecimento de pólen em `Vper` (OR = 17,40) e, no conjunto de evolução rápida na árvore, reconhecimento de pólen (OR = 30,26) e biossíntese de diterpenoides (OR = 29,95). Sinais de membrana plasmática, atividade oxidorredutase, ligação iônica e metabolismo de fenilpropanoides no subconjunto com duplicações locais são reportados como sugestivos por desequilíbrio de oportunidade específico de categoria.

