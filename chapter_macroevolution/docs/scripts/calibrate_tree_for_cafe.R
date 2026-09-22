#!/usr/bin/env Rscript
# ==============================================================================
# Pipeline: Ultrametric Tree Calibration for CAFE5
# Uses Penalized Likelihood (ape::chronos) with Fossil Age Constraints
# Chapter: Macroevolution and Genomics in Velloziaceae
# ==============================================================================

suppressPackageStartupMessages(library(ape))

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 2) {
    stop("Usage: calibrate_tree_for_cafe.R <iqtree.treefile> <output_ultrametric.tre>")
}

treefile <- args[1]
outfile <- args[2]

cat("[INFO] Reading ML tree from:", treefile, "\n")
tree <- read.tree(treefile)

# 1. Garantir que a arvore esta enraizada em Ath
if (!is.rooted(tree)) {
    cat("[INFO] Enraizando arvore em Arabidopsis thaliana (Ath)...\n")
    tree <- root(tree, outgroup = "Ath", resolve.root = TRUE)
}

# 2. Localizar os nós ancestrais para calibração fóssil (em Milhões de Anos - Ma)
# Calibrações:
# - Raiz (Ath vs Monocots): 130 - 145 Ma
# - Monocots (Dala vs Pandanales): 115 - 128 Ma
# - Pandanales (Ptec vs Velloziaceae): 90 - 105 Ma
# - Crown Velloziaceae (Abra vs core): 75 - 90 Ma
# - Vellozia speciation (Vper vs Vtub): 2 - 25 Ma

taxa <- tree$tip.label
cat("[INFO] Taxons na arvore:", paste(taxa, collapse=", "), "\n")

node_root <- getMRCA(tree, c("Ath", "Vtub"))
node_monocots <- getMRCA(tree, c("Dala", "Vtub"))
node_pandanales <- getMRCA(tree, c("Ptec", "Vtub"))
node_velloziaceae <- getMRCA(tree, c("Abra", "Vtub"))
node_vellozia <- getMRCA(tree, c("Vper", "Vtub"))

calib <- data.frame(
    node = c(node_root, node_monocots, node_pandanales, node_velloziaceae, node_vellozia),
    age.min = c(130, 115, 90, 75, 2),
    age.max = c(145, 128, 105, 90, 25)
)

cat("[INFO] Aplicando calibracao temporal via Penalized Likelihood (chronos)...\n")
chronotree <- chronos(tree, lambda = 1, calibration = calib)

# Garantir que a classe seja phylo e remover atributos desnecessarios para o CAFE5
class(chronotree) <- "phylo"

cat("[INFO] Arvore ultrametrica gerada com sucesso!\n")
cat("[INFO] Salvando arvore calibrada em:", outfile, "\n")
write.tree(chronotree, file = outfile)
