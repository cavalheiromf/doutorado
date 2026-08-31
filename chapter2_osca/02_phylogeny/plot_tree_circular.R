library(ggtree)
library(treeio)
library(ggplot2)

tree <- read.newick("results/iqtree.renamed.treefile")

tips <- tree$tip.label
groupInfo <- list(
  OSCA1 = tips[grepl("OSCA1|AT1G32090|AT4G02900|AT4G04340|AT4G22120|AT1G62320|AT1G11960|AT4G15430|AT3G21620", tips)],
  OSCA2 = tips[grepl("OSCA2|AT3G54510|AT1G58520|AT1G10090|AT1G69450|AT3G01100", tips)],
  OSCA3 = tips[grepl("OSCA3|AT1G30360", tips)],
  OSCA4 = tips[grepl("OSCA4|AT4G35870", tips)]
)
tree <- groupOTU(tree, groupInfo)

p <- ggtree(tree, layout="circular", aes(color=group), size=1.0) + 
     geom_tiplab(size=3.5, offset=0.05) + 
     scale_color_manual(values=c("OSCA1"="#1f77b4", "OSCA2"="#ff7f0e", "OSCA3"="#2ca02c", "OSCA4"="#d62728", "0"="black")) +
     theme(legend.position="right")

dir.create("../../reports/figures/02_phylogeny", showWarnings = FALSE, recursive = TRUE)
ggsave("../../reports/figures/02_phylogeny/OSCA_phylogenetic_tree_circular.pdf", p, width = 10, height = 10)
ggsave("../../reports/figures/02_phylogeny/OSCA_phylogenetic_tree_circular.png", p, width = 10, height = 10, dpi=300)
print("Circular tree saved successfully!")
