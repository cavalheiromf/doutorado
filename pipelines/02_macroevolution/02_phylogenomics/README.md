# Filogenômica (02_phylogenomics)

Esta pasta contém as análises para inferir a árvore de espécies a partir de genes ortólogos de cópia única.

## Estrutura Atual

```text
02_phylogenomics/
  input/
    pan_velloziaceae_supermatrix.*
    pan_velloziaceae_supermatrix_6taxa_backup.*
    partitions.nexus
  results/
    astral/
    concatenated_7taxa/
    concatenated_original/
    concordance/
    gene_trees/
  README.md
```

### Detalhes
* **`input/`**: Contém apenas as supermatrizes finais e o arquivo de partições, prontos para a inferência no IQ-TREE. Alinhamentos intermediários e temporários que ocupavam espaço foram removidos para garantir um ambiente mais limpo.
* **`results/`**: Contém as árvores inferidas, relatórios do IQ-TREE, checkpoints e resultados de concordância (gCF/sCF). O output de cada execução específica está segregado na sua subpasta respectiva (`astral`, `concatenated_7taxa`, etc.). A árvore preferida principal geralmente serve como input para o próximo passo (`03_dating`).

*(**Nota de Limpeza:** Atalhos de retrocompatibilidade, manifestos antigos e logs inúteis foram deletados em Outubro/2026 para simplificar a reprodutibilidade).*
