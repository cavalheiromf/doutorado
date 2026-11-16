#!/usr/bin/env Rscript

# run_deseq2.R
# Script to run differential expression analysis with DESeq2 for Vper and Vtub.
# Incorporates a paired experimental design (~ Individual + Tissue).
# Focuses on profiling and visualizing expression for the OSCA gene family.

library(DESeq2)
library(ggplot2)
library(pheatmap)
library(tidyr)
library(dplyr)
has_enhanced_volcano <- requireNamespace("EnhancedVolcano", quietly = TRUE)

# ---------------------------------------------------------
# SETUP DIRECTORIES
# ---------------------------------------------------------
get_script_dir <- function() {
  args <- commandArgs(trailingOnly = FALSE)
  file_arg <- grep("^--file=", args, value = TRUE)
  if (length(file_arg) > 0) {
    return(dirname(normalizePath(sub("^--file=", "", file_arg[1]))))
  }
  return(getwd())
}

default_osca_dir <- normalizePath(file.path(get_script_dir(), "..", ".."), mustWork = FALSE)
if (!dir.exists(file.path(default_osca_dir, "01_gene_identification"))) {
  default_osca_dir <- normalizePath(file.path(getwd(), "pipelines", "03_osca"), mustWork = FALSE)
}

osca_dir <- Sys.getenv("OSCA_PIPELINE_DIR", default_osca_dir)
results_dir <- Sys.getenv("DESEQ_RESULTS_DIR", file.path(osca_dir, "06_expression", "results_genecounts"))
figures_dir <- Sys.getenv("DESEQ_FIGURES_DIR", file.path(osca_dir, "figures", "06_expression_genecounts"))
exclude_sample <- Sys.getenv("EXCLUDE_SAMPLE", "")

dir.create(results_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)

# ---------------------------------------------------------
# LOAD GENE ID MAPPINGS
# ---------------------------------------------------------
mapping_path <- Sys.getenv("MAPPINGS_FILE", file.path(osca_dir, "01_gene_identification", "results", "oscasIDs.txt"))
if (!file.exists(mapping_path)) {
  stop(paste("ID mapping file not found at:", mapping_path))
}
mappings <- read.table(mapping_path, header = FALSE, sep = "\t", stringsAsFactors = FALSE)
colnames(mappings) <- c("GeneID", "OSCA_Name")

cat(paste("Loaded mappings for", nrow(mappings), "OSCA genes.\n"))

# ---------------------------------------------------------
# CORE ANALYSIS FUNCTION FOR EACH SPECIES
# ---------------------------------------------------------
run_species_analysis <- function(species_name, counts_path, is_vper) {
  cat(paste("\n==================================================\n",
            "RUNNING ANALYSIS FOR:", species_name,
            "\n==================================================\n"))
  
  if (!file.exists(counts_path)) {
    stop(paste("Counts file not found at:", counts_path))
  }
  
  # Load raw count matrix. Accept both the historical featureCounts table and
  # the validated STAR GeneCounts matrix (gene_id + one column per sample).
  raw_data <- read.table(counts_path, header = TRUE, sep = "\t", comment.char = "#", row.names = 1, check.names = FALSE)

  if (all(grepl("^(VP|VT)[0-9]+[CFR]$", colnames(raw_data)))) {
    count_matrix <- raw_data
  } else {
    # Historical featureCounts format: columns 1-5 are annotation fields.
    count_matrix <- raw_data[, 6:ncol(raw_data), drop = FALSE]
  }
  
  # Simplify column headers (extract VP/VT sample ID from the BAM file path)
  colnames(count_matrix) <- sub("_Aligned.sortedByCoord.out.bam", "", basename(colnames(count_matrix)))
  
  # Sort columns to maintain a standard order (e.g. VP1C, VP1F, VP1R...)
  count_matrix <- count_matrix[, order(colnames(count_matrix)), drop = FALSE]
  if (nzchar(exclude_sample) && exclude_sample %in% colnames(count_matrix)) {
    count_matrix <- count_matrix[, setdiff(colnames(count_matrix), exclude_sample), drop = FALSE]
    cat(paste("Excluded sample for sensitivity analysis:", exclude_sample, "\n"))
  }
  
  # Define Sample factors for the Design Matrix (Paired Design)
  samples <- colnames(count_matrix)
  
  # Tissues: C = Stem (Caule), F = Leaf (Folha), R = Root (Raiz)
  tissue <- ifelse(grepl("C$", samples), "Stem",
            ifelse(grepl("F$", samples), "Leaf", "Root"))
  
  # Individuals: VP1, VP2, VP3 or VT1, VT2, VT3
  individual <- sub("[CFR]$", "", samples)
  
  # Create Sample Metadata Dataframe
  col_data <- data.frame(
    row.names = samples,
    Individual = factor(individual),
    Tissue = factor(tissue, levels = c("Leaf", "Stem", "Root")) # Setting Leaf as reference tissue
  )
  
  cat("\nExperimental Design Table:\n")
  print(col_data)
  
  # Create DESeqDataSet object
  # Design formula incorporates Individual as a blocking factor: ~ Individual + Tissue
  dds <- DESeqDataSetFromMatrix(
    countData = count_matrix,
    colData = col_data,
    design = ~ Individual + Tissue
  )
  
  # Filter out low-expressed genes (sum of counts across all samples < 10)
  # This increases statistical power by reducing the multiple-testing penalty
  keep <- rowSums(counts(dds)) >= 10
  dds <- dds[keep, ]
  cat(paste("\nFiltered out low-expressed genes. Kept", sum(keep), "out of", length(keep), "genes.\n"))
  
  # Execute DESeq2 pipeline
  dds <- DESeq(dds)
  
  # Save clean raw and normalized count tables
  norm_counts <- counts(dds, normalized = TRUE)
  write.csv(count_matrix, file.path(results_dir, paste0(species_name, "_counts_clean.csv")))
  write.csv(norm_counts, file.path(results_dir, paste0(species_name, "_counts_normalized.csv")))
  
  # Apply Variance Stabilizing Transformation (vst) for sample visualization/PCA
  vsd <- vst(dds, blind = FALSE)
  
  # ---------------------------------------------------------
  # VISUALIZATION: PCA PLOT (QC)
  # ---------------------------------------------------------
  pca_data <- plotPCA(vsd, intgroup = c("Tissue", "Individual"), returnData = TRUE)
  percentVar <- round(100 * attr(pca_data, "percentVar"))
  
  pca_plot <- ggplot(pca_data, aes(PC1, PC2, color = Tissue, shape = Individual)) +
    geom_point(size = 5, alpha = 0.9) +
    scale_color_manual(values = c(Leaf = "#2ca02c", Stem = "#ff7f0e", Root = "#1f77b4")) +
    xlab(paste0("PC1: ", percentVar[1], "% variance")) +
    ylab(paste0("PC2: ", percentVar[2], "% variance")) +
    theme_bw() +
    theme(
      text = element_text(size = 14),
      plot.title = element_text(hjust = 0.5, face = "bold"),
      legend.position = "right",
      panel.grid.minor = element_blank()
    ) +
    labs(title = paste("PCA Cluster Alignment -", species_name))
  
  ggsave(file.path(figures_dir, paste0(species_name, "_PCA.png")), pca_plot, width = 7, height = 6, dpi = 300)
  ggsave(file.path(figures_dir, paste0(species_name, "_PCA.pdf")), pca_plot, width = 7, height = 6)
  
  # ---------------------------------------------------------
  # DIFFERENTIAL EXPRESSION CONTRASTS
  # ---------------------------------------------------------
  cat("\nExtracting differential expression results...\n")
  
  # 1. Root vs Leaf
  res_root_vs_leaf <- results(dds, contrast = c("Tissue", "Root", "Leaf"))
  # 2. Root vs Stem
  res_root_vs_stem <- results(dds, contrast = c("Tissue", "Root", "Stem"))
  # 3. Stem vs Leaf
  res_stem_vs_leaf <- results(dds, contrast = c("Tissue", "Stem", "Leaf"))
  
  # Save genome-wide DEG tables
  write.csv(as.data.frame(res_root_vs_leaf), file.path(results_dir, paste0(species_name, "_DE_Root_vs_Leaf.csv")))
  write.csv(as.data.frame(res_root_vs_stem), file.path(results_dir, paste0(species_name, "_DE_Root_vs_Stem.csv")))
  write.csv(as.data.frame(res_stem_vs_leaf), file.path(results_dir, paste0(species_name, "_DE_Stem_vs_Leaf.csv")))
  
  # ---------------------------------------------------------
  # OSCA-SPECIFIC DATA EXTRACTION & ANALYSIS
  # ---------------------------------------------------------
  species_prefix <- ifelse(is_vper, "Vp", "Vt")
  species_mappings <- mappings[grepl(paste0("^", species_prefix), mappings$OSCA_Name), ]
  
  # Filter OSCA genes based on presence in the filtered DESeq dataset
  osca_ids <- species_mappings$GeneID
  present_osca_ids <- osca_ids[osca_ids %in% rownames(dds)]
  missing_osca_ids <- osca_ids[!osca_ids %in% rownames(dds)]
  
  if (length(missing_osca_ids) > 0) {
    cat("Warning: some OSCA genes were filtered out due to zero or extremely low expression counts:\n")
    print(species_mappings[species_mappings$GeneID %in% missing_osca_ids, ])
  }
  
  # Extract normalized counts for OSCA genes
  osca_norm <- norm_counts[present_osca_ids, , drop = FALSE]
  rownames(osca_norm) <- species_mappings$OSCA_Name[match(rownames(osca_norm), species_mappings$GeneID)]
  write.csv(osca_norm, file.path(results_dir, paste0(species_name, "_OSCA_normalized_counts.csv")))
  
  # Helper to extract OSCA results from standard DESeq results
  get_osca_de <- function(res, contrast_name) {
    df <- as.data.frame(res[present_osca_ids, , drop = FALSE])
    df$GeneID <- present_osca_ids
    df$OSCA_Name <- species_mappings$OSCA_Name[match(df$GeneID, species_mappings$GeneID)]
    df$Contrast <- contrast_name
    # Reorder columns
    df <- df[, c("GeneID", "OSCA_Name", "Contrast", "baseMean", "log2FoldChange", "lfcSE", "stat", "pvalue", "padj")]
    return(df)
  }
  
  osca_de_rl <- get_osca_de(res_root_vs_leaf, "Root_vs_Leaf")
  osca_de_rs <- get_osca_de(res_root_vs_stem, "Root_vs_Stem")
  osca_de_sl <- get_osca_de(res_stem_vs_leaf, "Stem_vs_Leaf")
  
  osca_de_all <- rbind(osca_de_rl, osca_de_rs, osca_de_sl)
  write.csv(osca_de_all, file.path(results_dir, paste0(species_name, "_OSCA_DE_results.csv")), row.names = FALSE)
  
  # ---------------------------------------------------------
  # VOLCANO PLOTS WITH OSCA FAMILY HIGHLIGHTED
  # ---------------------------------------------------------
  make_volcano <- function(res, contrast_title, filename) {
    df <- as.data.frame(res)
    df$is_osca <- rownames(df) %in% present_osca_ids
    df$osca_label <- species_mappings$OSCA_Name[match(rownames(df), species_mappings$GeneID)]
    
    selectLab <- species_mappings$OSCA_Name[match(present_osca_ids, species_mappings$GeneID)]
    
    if (has_enhanced_volcano) {
      vol_plot <- EnhancedVolcano::EnhancedVolcano(
        df, lab = ifelse(df$is_osca, df$osca_label, ""),
        x = 'log2FoldChange', y = 'padj',
        title = paste(species_name, "-", contrast_title),
        subtitle = 'Highlighted: OSCA Gene Family', pCutoff = 0.05,
        FCcutoff = 1.0, pointSize = ifelse(df$is_osca, 4.0, 1.0),
        labSize = 4.0, col = c('grey', 'forestgreen', 'royalblue', 'red2'),
        colAlpha = ifelse(df$is_osca, 1.0, 0.4), legendPosition = 'right',
        selectLab = selectLab, drawConnectors = TRUE, widthConnectors = 0.5,
        arrowheads = FALSE
      )
    } else {
      df <- df[is.finite(df$log2FoldChange) & is.finite(df$padj) & df$padj > 0, , drop = FALSE]
      df$significance <- df$padj < 0.05 & abs(df$log2FoldChange) >= 1
      vol_plot <- ggplot(df, aes(log2FoldChange, -log10(padj))) +
        geom_point(aes(color = is_osca, alpha = significance), size = 1.2) +
        geom_text(data = df[df$is_osca, , drop = FALSE], aes(label = osca_label), size = 3, vjust = -0.5, na.rm = TRUE) +
        scale_color_manual(values = c(`FALSE` = "grey60", `TRUE` = "forestgreen")) +
        scale_alpha_manual(values = c(`FALSE` = 0.4, `TRUE` = 1)) +
        labs(title = paste(species_name, "-", contrast_title), subtitle = "Highlighted: OSCA Gene Family", x = "log2 fold change", y = "-log10 adjusted P value") +
        theme_bw()
    }
    
    ggsave(file.path(figures_dir, paste0(species_name, "_", filename, ".png")), vol_plot, width = 9, height = 8, dpi = 300)
    ggsave(file.path(figures_dir, paste0(species_name, "_", filename, ".pdf")), vol_plot, width = 9, height = 8)
  }
  
  make_volcano(res_root_vs_leaf, "Root vs Leaf (Raiz vs Folha)", "Volcano_Root_vs_Leaf")
  make_volcano(res_root_vs_stem, "Root vs Stem (Raiz vs Caule)", "Volcano_Root_vs_Stem")
  make_volcano(res_stem_vs_leaf, "Stem vs Leaf (Caule vs Folha)", "Volcano_Stem_vs_Leaf")
  
  # ---------------------------------------------------------
  # HEATMAP OF OSCA GENES (Z-SCORE SCALED)
  # ---------------------------------------------------------
  osca_vst <- assay(vsd)[present_osca_ids, , drop = FALSE]
  rownames(osca_vst) <- species_mappings$OSCA_Name[match(rownames(osca_vst), species_mappings$GeneID)]
  
  annotation_col <- data.frame(
    Tissue = col_data$Tissue,
    Individual = col_data$Individual,
    row.names = rownames(col_data)
  )
  
  ann_colors <- list(
    Tissue = c(Leaf = "#2ca02c", Stem = "#ff7f0e", Root = "#1f77b4"),
    Individual = if (is_vper) c(VP1 = "#aec7e8", VP2 = "#ffbb78", VP3 = "#98df8a") else c(VT1 = "#aec7e8", VT2 = "#ffbb78", VT3 = "#98df8a")
  )
  
  # Render heatmaps to PNG and PDF
  png(file.path(figures_dir, paste0(species_name, "_OSCA_heatmap.png")), width = 8, height = 7, units = "in", res = 300)
  pheatmap(
    osca_vst,
    scale = "row",
    annotation_col = annotation_col,
    annotation_colors = ann_colors,
    show_colnames = TRUE,
    clustering_distance_rows = "correlation",
    clustering_distance_cols = "euclidean",
    main = paste("Z-score scaled OSCA expression in", species_name)
  )
  dev.off()
  
  pdf(file.path(figures_dir, paste0(species_name, "_OSCA_heatmap.pdf")), width = 8, height = 7)
  pheatmap(
    osca_vst,
    scale = "row",
    annotation_col = annotation_col,
    annotation_colors = ann_colors,
    show_colnames = TRUE,
    clustering_distance_rows = "correlation",
    clustering_distance_cols = "euclidean",
    main = paste("Z-score scaled OSCA expression in", species_name)
  )
  dev.off()
  
  cat(paste("Successfully completed single-species analysis for", species_name, "\n"))
  
  return(list(norm_counts = norm_counts, vsd = vsd, mappings = species_mappings))
}

# ---------------------------------------------------------
# EXECUTE SPECIES ANALYSES
# ---------------------------------------------------------
vper_counts <- Sys.getenv(
  "VPER_COUNTS_FILE", 
  file.path(osca_dir, "05_rnaseq", "results_genecounts", "05_counts", "Vper_star_genecounts_col4.tsv")
)
vtub_counts <- Sys.getenv(
  "VTUB_COUNTS_FILE", 
  file.path(osca_dir, "05_rnaseq", "results_genecounts", "05_counts", "Vtub_star_genecounts_col4.tsv")
)

vper_res <- run_species_analysis("Vper", vper_counts, TRUE)
vtub_res <- run_species_analysis("Vtub", vtub_counts, FALSE)

# ---------------------------------------------------------
# COMPARATIVE ANALYSIS OF OSCA ORTHOLOGS
# ---------------------------------------------------------
cat("\n==================================================\n",
    "RUNNING COMPARATIVE ORTHOLOG EXPRESSION ANALYSIS",
    "\n==================================================\n")

# Define the established orthologous/paralogous pairs
pairs_list <- list(
  c("VpOSCA1.1", "VtOSCA1.1"),
  c("VpOSCA1.2", "VtOSCA1.2"),
  c("VpOSCA1.3", "VtOSCA1.3"),
  c("VpOSCA1.4", "VtOSCA1.4"),
  c("VpOSCA1.5", "VtOSCA1.5"),
  c("VpOSCA2.1", "VtOSCA2.1"),
  c("VpOSCA2.2", "VtOSCA2.2"),
  c("VpOSCA2.3", "VtOSCA2.3"),
  c("VpOSCA2.4a", "VtOSCA2.4"),
  c("VpOSCA2.4b", "VtOSCA2.4"),
  c("VpOSCA2.5", "VtOSCA2.5"),
  c("VpOSCA3.1", "VtOSCA3.1"),
  c("VpOSCA3.2", "VtOSCA3.2"),
  c("VpOSCA4.1", "VtOSCA4.1")
)

# Helper function to compute expression stats per tissue
get_expression_stats <- function(norm_counts, mappings, species_name) {
  df_counts <- as.data.frame(t(norm_counts))
  
  # Map Ensembl Gene IDs to OSCA names
  osca_genes <- mappings$OSCA_Name[match(colnames(df_counts), mappings$GeneID)]
  colnames(df_counts) <- osca_genes
  
  # Filter only mapped columns
  df_counts <- df_counts[, !is.na(colnames(df_counts)), drop = FALSE]
  
  # Determine tissue factor
  samples <- rownames(df_counts)
  tissue <- ifelse(grepl("C$", samples), "Stem",
            ifelse(grepl("F$", samples), "Leaf", "Root"))
  
  df_counts$Tissue <- tissue
  
  # Melt/Pivot to long format
  long_df <- df_counts %>%
    pivot_longer(cols = -Tissue, names_to = "OSCA_Gene", values_to = "Counts")
  
  # Group and summarize
  stats_df <- long_df %>%
    group_by(OSCA_Gene, Tissue) %>%
    summarise(
      Mean = mean(Counts),
      SE = sd(Counts) / sqrt(n()),
      .groups = "drop"
    )
  
  stats_df$Species <- species_name
  return(stats_df)
}

vper_stats <- get_expression_stats(vper_res$norm_counts, vper_res$mappings, "Vper")
vtub_stats <- get_expression_stats(vtub_res$norm_counts, vtub_res$mappings, "Vtub")

# Merge orthologous pairs into a unified dataframe
combined_stats <- data.frame()

for (pair in pairs_list) {
  vp_gene <- pair[1]
  vt_gene <- pair[2]
  
  # Extract Vper stats for this gene
  vp_data <- vper_stats %>% filter(OSCA_Gene == vp_gene)
  if (nrow(vp_data) > 0) {
    vp_data$Pair_Label <- paste(vp_gene, vt_gene, sep = " / ")
    # Create a nice group header for facet plotting (e.g. OSCA1.1, OSCA2.4a, etc.)
    vp_data$Group <- sub("^Vp", "", vp_gene)
    combined_stats <- rbind(combined_stats, vp_data)
  }
  
  # Extract Vtub stats for this gene
  vt_data <- vtub_stats %>% filter(OSCA_Gene == vt_gene)
  if (nrow(vt_data) > 0) {
    vt_data$Pair_Label <- paste(vp_gene, vt_gene, sep = " / ")
    vt_data$Group <- sub("^Vp", "", vp_gene)
    combined_stats <- rbind(combined_stats, vt_data)
  }
}

# Fix ordering of tissues on the x-axis
combined_stats$Tissue <- factor(combined_stats$Tissue, levels = c("Leaf", "Stem", "Root"))

# Make sure groups follow numerical order
combined_stats$Group <- factor(
  combined_stats$Group, 
  levels = c(
    "OSCA1.1", "OSCA1.2", "OSCA1.3", "OSCA1.4", "OSCA1.5",
    "OSCA2.1", "OSCA2.2", "OSCA2.3", "OSCA2.4a", "OSCA2.4b", "OSCA2.5",
    "OSCA3.1", "OSCA3.2", "OSCA4.1"
  )
)

# Plotting the comparative figure
comp_plot <- ggplot(combined_stats, aes(x = Tissue, y = Mean, fill = Species)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7, alpha = 0.9) +
  geom_errorbar(
    aes(ymin = pmax(0, Mean - SE), ymax = Mean + SE), 
    position = position_dodge(width = 0.8), 
    width = 0.25, 
    color = "grey30"
  ) +
  facet_wrap(~ Group, scales = "free_y", ncol = 4) +
  scale_fill_manual(values = c(Vper = "#1f77b4", Vtub = "#aec7e8")) + # Conserved dark vs light blue palette
  theme_bw() +
  theme(
    strip.background = element_rect(fill = "grey95"),
    strip.text = element_text(face = "bold", size = 11),
    axis.text.x = element_text(size = 11, angle = 30, hjust = 1),
    axis.text.y = element_text(size = 10),
    axis.title = element_text(size = 13, face = "bold"),
    legend.title = element_text(size = 12, face = "bold"),
    legend.text = element_text(size = 11),
    legend.position = "top",
    plot.title = element_text(hjust = 0.5, face = "bold", size = 15),
    panel.grid.minor = element_blank()
  ) +
  labs(
    x = "Tissue Type",
    y = "Mean Normalized Counts",
    title = "Tissue-Specific Expression Profiles of OSCA Orthologs",
    fill = "Species"
  )

# Save the comparative expression figures
ggsave(file.path(figures_dir, "OSCA_orthologs_comparative_expression.png"), comp_plot, width = 14, height = 10, dpi = 300)
ggsave(file.path(figures_dir, "OSCA_orthologs_comparative_expression.pdf"), comp_plot, width = 14, height = 10)

cat("\n==================================================\n",
    "ALL RNA-SEQ下游 EXPR & DE ANALYSIS COMPLETED!",
    "\n==================================================\n")
