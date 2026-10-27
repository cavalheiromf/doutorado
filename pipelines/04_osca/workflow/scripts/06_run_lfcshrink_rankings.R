#!/usr/bin/env Rscript

library(DESeq2)

root <- "/home/mfcaval/github/doutorado"
out_dir <- file.path(root, "analyses/06_expression/results_genecounts_lfcshrink")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

samples <- list(
  Vper = c("VP1C", "VP2C", "VP3C", "VP1F", "VP2F", "VP3F", "VP1R", "VP2R", "VP3R"),
  Vtub = c("VT1C", "VT2C", "VT3C", "VT1F", "VT2F", "VT3F", "VT2R", "VT3R")
)

run_species <- function(species, sample_names) {
  path <- file.path(root, "analyses/05_rnaseq/results_genecounts/05_counts", paste0(species, "_star_genecounts_col4.tsv"))
  counts <- read.table(path, header = TRUE, sep = "\t", row.names = 1, check.names = FALSE)
  counts <- counts[, sample_names, drop = FALSE]
  tissue <- factor(ifelse(grepl("C$", sample_names), "Stem", ifelse(grepl("F$", sample_names), "Leaf", "Root")), levels = c("Leaf", "Stem", "Root"))
  individual <- factor(sub("[CFR]$", "", sample_names))
  col_data <- data.frame(row.names = sample_names, Individual = individual, Tissue = tissue)
  dds <- DESeqDataSetFromMatrix(countData = round(as.matrix(counts)), colData = col_data, design = ~ Individual + Tissue)
  dds <- dds[rowSums(counts(dds)) >= 10, ]
  dds <- DESeq(dds, quiet = TRUE)
  for (contrast in list(c("Tissue", "Root", "Leaf"), c("Tissue", "Root", "Stem"), c("Tissue", "Stem", "Leaf"))) {
    label <- paste(contrast[2], "vs", contrast[3], sep = "_")
    shrunk <- lfcShrink(dds, contrast = contrast, type = "normal")
    out <- as.data.frame(shrunk)
    out$gene_id <- rownames(out)
    out <- out[, c("gene_id", setdiff(names(out), "gene_id"))]
    write.csv(out, file.path(out_dir, paste0(species, "_", label, "_lfcShrink.csv")), row.names = FALSE)
    rank <- out[is.finite(out$log2FoldChange), c("gene_id", "log2FoldChange")]
    rank <- rank[order(rank$log2FoldChange, decreasing = TRUE), ]
    write.table(rank, file.path(out_dir, paste0(species, "_", label, "_lfcShrink.rnk")), sep = "\t", quote = FALSE, row.names = FALSE, col.names = FALSE)
  }
}

run_species("Vper", samples$Vper)
run_species("Vtub", samples$Vtub)
cat("lfcShrink ranking preparation: PASS\n")
