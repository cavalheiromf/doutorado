#!/usr/bin/env Rscript

# ==============================================================================
# Script: run_comparative_functional_enrichment_final.R
#
# Objetivo:
#   Enriquecimento funcional de famílias gênicas evolutivamente significativas
#   identificadas pelo CAFE5 em Velloziaceae.
#
# Estratégia estatística:
#   1. Tier A define os foregrounds principais.
#   2. O universo é formado pelos ortogrupos CAFE5 anotados em cada ontologia.
#   3. Cada contraste x ontologia recebe um único ajuste BH local.
#   4. simplify() é aplicado apenas aos resultados GO, nunca ao KEGG.
#   5. Tier AB e Tier ABC são análises de sensibilidade, não novos níveis de FDR.
#
# Unidade estatística:
#   Ortogrupos (FamilyID), contados uma única vez por termo.
# ==============================================================================

suppressPackageStartupMessages({
  library(dplyr)
  library(tidyr)
  library(readr)
  library(purrr)
  library(stringr)
  library(clusterProfiler)
  library(GOSemSim)
})

# ------------------------------------------------------------------------------
# 0. Configurações
# ------------------------------------------------------------------------------

BASE_DIR <- "/home/mfcaval/github/doutorado/chapter_macroevolution/04_gene_families"

MASTER_TABLE_PATH <- file.path(
  BASE_DIR,
  "comparative_axes",
  "comparative_families_master_table_v2.tsv"
)

ANNOTATION_PATH <- file.path(
  BASE_DIR,
  "functional_enrichment",
  "orthogroup_functional_annotations.tsv"
)

KEGG_NAMES_PATH <- file.path(
  BASE_DIR,
  "functional_enrichment",
  "raw_annotations",
  "kegg",
  "ath_pathway_list.tsv"
)

GO_NAMES_PATH <- file.path(
  BASE_DIR,
  "functional_enrichment",
  "go_term_names.tsv"
)

OUTPUT_DIR <- file.path(
  BASE_DIR,
  "functional_enrichment",
  "results_final_simplify"
)

dir.create(OUTPUT_DIR, showWarnings = FALSE, recursive = TRUE)

# Parâmetros principais
MIN_TERM_UNIVERSE_N <- 5
MAX_TERM_UNIVERSE_FRACTION <- 0.90
MIN_TERM_FOREGROUND_N <- 3
FDR_THRESHOLD <- 0.05

# Simplificação GO
SIMPLIFY_GO <- TRUE
SIMPLIFY_CUTOFF <- 0.7
SIMPLIFY_BY <- "p.adjust"
SIMPLIFY_MEASURE <- "Wang"

# ------------------------------------------------------------------------------
# 1. Funções auxiliares
# ------------------------------------------------------------------------------

parse_logical <- function(x) {
  case_when(
    x %in% c("TRUE", "True", "true", "1") ~ TRUE,
    x %in% c("FALSE", "False", "false", "0") ~ FALSE,
    TRUE ~ NA
  )
}

read_names_table <- function(path, default_names = c("TermID", "TermName")) {
  if (!file.exists(path)) {
    return(tibble(
      TermID = character(),
      TermName = character()
    ))
  }

  out <- read_tsv(path, col_types = cols(.default = "c"))

  if (ncol(out) >= 2) {
    out <- out[, 1:2]
    names(out) <- default_names
  } else {
    out <- tibble(
      TermID = character(),
      TermName = character()
    )
  }

  out %>%
    mutate(
      TermID = as.character(TermID),
      TermName = as.character(TermName)
    ) %>%
    distinct(TermID, .keep_all = TRUE)
}

get_term_names <- function(ontology, go_names, kegg_names) {
  if (ontology == "KEGG") {
    return(
      kegg_names %>%
        transmute(term = TermID, name = TermName)
    )
  }

  if (nrow(go_names) > 0) {
    return(
      go_names %>%
        transmute(term = TermID, name = TermName)
    )
  }

  tibble(
    term = character(),
    name = character()
  )
}

simplify_go_result <- function(cp_result, ontology) {
  if (is.null(cp_result)) return(NULL)
  if (!ontology %in% c("GO_BP", "GO_MF", "GO_CC")) return(cp_result)

  ont_code <- c(
    GO_BP = "BP",
    GO_MF = "MF",
    GO_CC = "CC"
  )[[ontology]]

  cp_result@ontology <- ont_code

  simplified <- tryCatch(
    {
      simplify(
        cp_result,
        cutoff = SIMPLIFY_CUTOFF,
        by = SIMPLIFY_BY,
        select_fun = min,
        measure = SIMPLIFY_MEASURE
      )
    },
    error = function(e) {
      warning(
        sprintf(
          "Falha no simplify() para %s: %s",
          ontology,
          conditionMessage(e)
        )
      )
      cp_result
    }
  )

  simplified
}

# ------------------------------------------------------------------------------
# 2. Carregamento dos dados
# ------------------------------------------------------------------------------

message("[1/8] Carregando dados...")

master_df <- read_tsv(
  MASTER_TABLE_PATH,
  col_types = cols(.default = "c")
) %>%
  mutate(
    across(
      c(
        Change_Node12_Core_Velloziaceae,
        Change_Vper,
        Change_Vtub,
        Change_Xvis,
        BranchProb_Node12_CoreVelloziaceae,
        BranchProb_Vper,
        BranchProb_Vtub,
        BranchProb_Xvis
      ),
      as.numeric
    ),
    across(
      c(
        Ind_Exp_Terminal_Vper,
        Ind_Exp_Terminal_Vtub,
        Ind_Exp_Terminal_Xvis,
        Ind_Exp_Ancestral_Node12_CoreVelloziaceae,
        Preserved_k3_Exp_Terminal_Vper,
        Preserved_k3_Exp_Terminal_Vtub,
        Preserved_k3_Exp_Terminal_Xvis,
        Preserved_k3_Exp_Node12
      ),
      parse_logical
    )
  )

ann_df <- read_tsv(
  ANNOTATION_PATH,
  col_types = cols(.default = "c")
) %>%
  select(
    FamilyID,
    GO_BP_Propagated,
    GO_MF_Propagated,
    GO_CC_Propagated,
    KEGG_Pathways
  ) %>%
  distinct(FamilyID, .keep_all = TRUE)

go_names <- read_names_table(GO_NAMES_PATH)
kegg_names <- read_names_table(KEGG_NAMES_PATH)

all_term_names <- bind_rows(go_names, kegg_names) %>%
  distinct(TermID, .keep_all = TRUE)

data_full <- master_df %>%
  inner_join(ann_df, by = "FamilyID") %>%
  distinct(FamilyID, .keep_all = TRUE)

message(sprintf("   Universo integrado: %d ortogrupos.", nrow(data_full)))

# ------------------------------------------------------------------------------
# 3. Preparação das anotações por ontologia
# ------------------------------------------------------------------------------

message("[2/8] Expandindo anotações por ontologia...")

ontology_columns <- c(
  GO_BP = "GO_BP_Propagated",
  GO_MF = "GO_MF_Propagated",
  GO_CC = "GO_CC_Propagated",
  KEGG = "KEGG_Pathways"
)

long_annotations <- map(
  ontology_columns,
  function(annotation_column) {
    data_full %>%
      select(FamilyID, all_of(annotation_column)) %>%
      filter(
        !is.na(.data[[annotation_column]]),
        .data[[annotation_column]] != "",
        .data[[annotation_column]] != "0"
      ) %>%
      separate_rows(all_of(annotation_column), sep = ";") %>%
      rename(TermID = all_of(annotation_column)) %>%
      mutate(TermID = str_trim(TermID)) %>%
      filter(
        !is.na(TermID),
        TermID != "",
        TermID != "0"
      ) %>%
      distinct(FamilyID, TermID)
  }
)

names(long_annotations) <- names(ontology_columns)

# ------------------------------------------------------------------------------
# 4. Foregrounds Tier A
# ------------------------------------------------------------------------------

message("[3/8] Definindo foregrounds principais Tier A...")

get_strict_exp_families <- function(df, branch_code) {
  if (branch_code == "Node12") {
    df %>%
      filter(
        Evidence_Tier == "Tier_A_High_Confidence",
        Change_Node12_Core_Velloziaceae > 0,
        Ind_Exp_Ancestral_Node12_CoreVelloziaceae == TRUE,
        Preserved_k3_Exp_Node12 == TRUE
      ) %>%
      pull(FamilyID) %>%
      unique()
  } else {
    change_col <- paste0("Change_", branch_code)
    indicator_col <- paste0("Ind_Exp_Terminal_", branch_code)
    preserved_col <- paste0("Preserved_k3_Exp_Terminal_", branch_code)

    df %>%
      filter(
        Evidence_Tier == "Tier_A_High_Confidence",
        .data[[change_col]] > 0,
        .data[[indicator_col]] == TRUE,
        .data[[preserved_col]] == TRUE
      ) %>%
      pull(FamilyID) %>%
      unique()
  }
}

get_directional_con_families <- function(df, branch_code) {
  change_col <- if (branch_code == "Node12") {
    "Change_Node12_Core_Velloziaceae"
  } else {
    paste0("Change_", branch_code)
  }

  df %>%
    filter(
      Evidence_Tier == "Tier_A_High_Confidence",
      .data[[change_col]] < 0
    ) %>%
    pull(FamilyID) %>%
    unique()
}

foregrounds <- list(
  Node12_Expansion = get_strict_exp_families(data_full, "Node12"),
  Node12_Contraction = get_directional_con_families(data_full, "Node12"),
  Vtub_Expansion = get_strict_exp_families(data_full, "Vtub"),
  Vtub_Contraction = get_directional_con_families(data_full, "Vtub"),
  Xvis_Expansion = get_strict_exp_families(data_full, "Xvis"),
  Xvis_Contraction = get_directional_con_families(data_full, "Xvis"),
  Vper_Expansion = get_strict_exp_families(data_full, "Vper"),
  Vper_Contraction = get_directional_con_families(data_full, "Vper")
)

foreground_sizes <- tibble(
  Contrast = names(foregrounds),
  N_Foreground = map_int(foregrounds, length)
)

write_tsv(
  foreground_sizes,
  file.path(OUTPUT_DIR, "Foreground_sizes_TierA.tsv")
)

# ------------------------------------------------------------------------------
# 5. Função central de enriquecimento
# ------------------------------------------------------------------------------

message("[4/8] Definindo rotina de enriquecimento...")

perform_enrichment_core <- function(
    fg_family_ids,
    contrast_name,
    ontology,
    analysis_label = "Primary_TierA",
    simplify_go = FALSE
) {
  long_df <- long_annotations[[ontology]]

  if (is.null(long_df) || nrow(long_df) == 0) {
    return(list(
      res_df = tibble(),
      cp_obj = NULL
    ))
  }

  background_ids <- unique(long_df$FamilyID)
  fg_ids <- intersect(unique(fg_family_ids), background_ids)

  if (length(fg_ids) == 0) {
    return(list(
      res_df = tibble(),
      cp_obj = NULL
    ))
  }

  term_sizes <- long_df %>%
    count(TermID, name = "term_size")

  max_gs_size <- round(
    MAX_TERM_UNIVERSE_FRACTION * length(background_ids)
  )

  eligible_terms <- term_sizes %>%
    filter(
      term_size >= MIN_TERM_UNIVERSE_N,
      term_size <= max_gs_size
    ) %>%
    pull(TermID)

  term2gene <- long_df %>%
    filter(TermID %in% eligible_terms) %>%
    transmute(
      term = TermID,
      gene = FamilyID
    ) %>%
    distinct()

  term2name <- get_term_names(ontology, go_names, kegg_names)

  cp_result <- tryCatch(
    {
      enricher(
        gene = fg_ids,
        universe = background_ids,
        TERM2GENE = term2gene,
        TERM2NAME = term2name,
        minGSSize = MIN_TERM_UNIVERSE_N,
        maxGSSize = max_gs_size,
        pvalueCutoff = 1,
        qvalueCutoff = 1,
        pAdjustMethod = "BH"
      )
    },
    error = function(e) {
      warning(
        sprintf(
          "Falha em %s / %s: %s",
          contrast_name,
          ontology,
          conditionMessage(e)
        )
      )
      NULL
    }
  )

  if (is.null(cp_result)) {
    return(list(
      res_df = tibble(),
      cp_obj = NULL
    ))
  }

  cp_raw <- cp_result

  if (simplify_go && ontology %in% c("GO_BP", "GO_MF", "GO_CC")) {
    cp_result <- simplify_go_result(cp_result, ontology)
  }

  result_df <- as.data.frame(cp_result)

  if (nrow(result_df) == 0) {
    return(list(
      res_df = tibble(),
      cp_obj = cp_result
    ))
  }

  out_df <- result_df %>%
    as_tibble() %>%
    transmute(
      Contrast = contrast_name,
      Analysis = analysis_label,
      Ontology = ontology,
      TermID = ID,
      TermName = Description,
      Simplified = if_else(
        ontology %in% c("GO_BP", "GO_MF", "GO_CC") & simplify_go,
        TRUE,
        FALSE
      ),
      k_fg = Count,
      Foreground_Total = length(fg_ids),
      Foreground_Ratio = GeneRatio,
      K_bg = as.numeric(str_extract(BgRatio, "^[0-9]+")),
      Background_Total = as.numeric(str_extract(BgRatio, "[0-9]+$")),
      Background_Ratio = BgRatio,
      Odds_Ratio = NA_real_,
      CI_95_Low = NA_real_,
      CI_95_High = NA_real_,
      p_value = pvalue,
      FDR = p.adjust,
      FamilyIDs = geneID,
      Reportable = k_fg >= MIN_TERM_FOREGROUND_N
    ) %>%
    arrange(FDR, p_value)

  list(
    res_df = out_df,
    cp_obj = cp_result,
    cp_raw = cp_raw
  )
}

run_all_ontologies <- function(
    fg_ids,
    contrast_name,
    analysis_label = "Primary_TierA",
    simplify_go = FALSE
) {
  results <- map(
    names(ontology_columns),
    ~ perform_enrichment_core(
      fg_family_ids = fg_ids,
      contrast_name = contrast_name,
      ontology = .x,
      analysis_label = analysis_label,
      simplify_go = simplify_go
    )
  )

  names(results) <- names(ontology_columns)

  list(
    res_df = map_dfr(results, "res_df"),
    cp_objs = compact(map(results, "cp_obj")),
    cp_raw = compact(map(results, "cp_raw"))
  )
}

# ------------------------------------------------------------------------------
# 6. Análises principais: bruto e simplificado
# ------------------------------------------------------------------------------

message("[5/8] Executando análises principais...")

primary_raw_results <- imap(
  foregrounds,
  ~ run_all_ontologies(
    fg_ids = .x,
    contrast_name = .y,
    analysis_label = "Primary_TierA",
    simplify_go = FALSE
  )
)

primary_simpl_results <- imap(
  foregrounds,
  ~ run_all_ontologies(
    fg_ids = .x,
    contrast_name = .y,
    analysis_label = "Primary_TierA",
    simplify_go = SIMPLIFY_GO
  )
)

primary_raw_df <- map_dfr(primary_raw_results, "res_df")
primary_simpl_df <- map_dfr(primary_simpl_results, "res_df")

primary_raw_reportable <- primary_raw_df %>%
  filter(Reportable == TRUE)

primary_simpl_reportable <- primary_simpl_df %>%
  filter(Reportable == TRUE)

write_tsv(
  primary_raw_df,
  file.path(OUTPUT_DIR, "Primary_All_Terms_TierA_raw.tsv")
)

write_tsv(
  primary_raw_reportable,
  file.path(OUTPUT_DIR, "Primary_Reportable_TierA_raw.tsv")
)

write_tsv(
  primary_simpl_df,
  file.path(OUTPUT_DIR, "Primary_All_Terms_TierA_simplified.tsv")
)

write_tsv(
  primary_simpl_reportable,
  file.path(OUTPUT_DIR, "Primary_Reportable_TierA_simplified.tsv")
)

write_tsv(
  primary_simpl_reportable %>%
    filter(str_detect(Contrast, "^Node12_")),
  file.path(OUTPUT_DIR, "Objective1_Core_Node12.tsv")
)

write_tsv(
  primary_simpl_reportable %>%
    filter(str_detect(Contrast, "^(Vtub|Xvis)_")),
  file.path(OUTPUT_DIR, "Objective2_DT_Vtub_Xvis.tsv")
)

write_tsv(
  primary_simpl_reportable %>%
    filter(str_detect(Contrast, "^Vper_")),
  file.path(OUTPUT_DIR, "Objective3_Vper_Avoidant.tsv")
)

saveRDS(
  map(primary_simpl_results, "cp_objs"),
  file.path(OUTPUT_DIR, "Primary_enrichResult_objects_simplified.rds")
)

saveRDS(
  map(primary_raw_results, "cp_objs"),
  file.path(OUTPUT_DIR, "Primary_enrichResult_objects_raw.rds")
)

# ------------------------------------------------------------------------------
# 7. Comparação direta Vtub versus Xvis
# ------------------------------------------------------------------------------

message("[6/8] Executando comparação direta Vtub versus Xvis...")

compare_two_lineages_direct <- function(
    fg_a,
    fg_b,
    label_a = "Vtub",
    label_b = "Xvis"
) {
  map_dfr(
    names(long_annotations),
    function(ontology) {
      long_df <- long_annotations[[ontology]]

      background_ids <- unique(long_df$FamilyID)

      ids_a <- intersect(unique(fg_a), background_ids)
      ids_b <- intersect(unique(fg_b), background_ids)

      if (length(ids_a) == 0 || length(ids_b) == 0) {
        return(tibble())
      }

      term_sizes <- long_df %>%
        count(TermID, name = "term_size") %>%
        filter(
          term_size >= MIN_TERM_UNIVERSE_N,
          term_size <= round(MAX_TERM_UNIVERSE_FRACTION * length(background_ids))
        )

      term_family_lists <- long_df %>%
        semi_join(term_sizes, by = "TermID") %>%
        group_by(TermID) %>%
        summarise(
          families = list(unique(FamilyID)),
          .groups = "drop"
        )

      term_family_lists %>%
        mutate(
          k_a = map_int(families, ~ sum(ids_a %in% .x)),
          k_b = map_int(families, ~ sum(ids_b %in% .x)),
          n_a = length(ids_a),
          n_b = length(ids_b),
          p_difference = map2_dbl(
            k_a,
            k_b,
            ~ tryCatch(
              fisher.test(
                matrix(
                  c(
                    .x, length(ids_a) - .x,
                    .y, length(ids_b) - .y
                  ),
                  nrow = 2,
                  byrow = TRUE
                )
              )$p.value,
              error = function(e) NA_real_
            )
          )
        ) %>%
        select(TermID, k_a, n_a, k_b, n_b, p_difference) %>%
        mutate(
          Ontology = ontology,
          Label_A = label_a,
          Label_B = label_b
        )
    }
  ) %>%
    left_join(all_term_names, by = "TermID") %>%
    mutate(
      TermName = coalesce(TermName, TermID),
      FDR_difference = p.adjust(p_difference, method = "BH"),
      Reportable = (k_a >= MIN_TERM_FOREGROUND_N | k_b >= MIN_TERM_FOREGROUND_N)
    ) %>%
    filter(Reportable == TRUE) %>%
    select(
      Ontology,
      TermID,
      TermName,
      Label_A,
      Label_B,
      k_a,
      n_a,
      k_b,
      n_b,
      p_difference,
      FDR_difference
    ) %>%
    arrange(FDR_difference, p_difference)
}

dt_comparison <- compare_two_lineages_direct(
  fg_a = foregrounds$Vtub_Expansion,
  fg_b = foregrounds$Xvis_Expansion,
  label_a = "Vtub",
  label_b = "Xvis"
)

write_tsv(
  dt_comparison,
  file.path(OUTPUT_DIR, "Objective2_Direct_Comparison_Vtub_vs_Xvis.tsv")
)

# ------------------------------------------------------------------------------
# 8. Matriz descritiva tripla
# ------------------------------------------------------------------------------

message("[7/8] Construindo matriz descritiva Vtub/Xvis/Vper...")

get_primary_expansion_results <- function(df, contrast_name) {
  df %>%
    filter(
      Contrast == contrast_name,
      Analysis == "Primary_TierA",
      Reportable == TRUE
    ) %>%
    select(
      Ontology,
      TermID,
      TermName,
      FDR,
      Odds_Ratio,
      k_fg
    )
}

vtub_exp_results <- get_primary_expansion_results(primary_simpl_df, "Vtub_Expansion") %>%
  rename(
    FDR_Vtub = FDR,
    OR_Vtub = Odds_Ratio,
    k_Vtub = k_fg
  )

xvis_exp_results <- get_primary_expansion_results(primary_simpl_df, "Xvis_Expansion") %>%
  rename(
    FDR_Xvis = FDR,
    OR_Xvis = Odds_Ratio,
    k_Xvis = k_fg
  )

vper_exp_results <- get_primary_expansion_results(primary_simpl_df, "Vper_Expansion") %>%
  rename(
    FDR_Vper = FDR,
    OR_Vper = Odds_Ratio,
    k_Vper = k_fg
  )

triple_detection <- full_join(
  vtub_exp_results,
  xvis_exp_results,
  by = c("Ontology", "TermID", "TermName")
) %>%
  full_join(
    vper_exp_results,
    by = c("Ontology", "TermID", "TermName")
  ) %>%
  mutate(
    Sig_Vtub = !is.na(FDR_Vtub) & FDR_Vtub <= FDR_THRESHOLD,
    Sig_Xvis = !is.na(FDR_Xvis) & FDR_Xvis <= FDR_THRESHOLD,
    Sig_Vper = !is.na(FDR_Vper) & FDR_Vper <= FDR_THRESHOLD,
    Detection_Pattern = case_when(
      Sig_Vtub & Sig_Xvis & !Sig_Vper ~ "Vtub_Xvis_DT_candidate",
      Sig_Vtub & Sig_Vper & !Sig_Xvis ~ "Vellozia_shared",
      Sig_Xvis & Sig_Vper & !Sig_Vtub ~ "Xvis_Vper_shared",
      Sig_Vtub & Sig_Xvis & Sig_Vper ~ "All_three_lineages",
      Sig_Vper & !Sig_Vtub & !Sig_Xvis ~ "Vper_only_avoidant_candidate",
      Sig_Vtub & !Sig_Xvis & !Sig_Vper ~ "Vtub_only",
      Sig_Xvis & !Sig_Vtub & !Sig_Vper ~ "Xvis_only",
      TRUE ~ "Not_significant"
    )
  ) %>%
  arrange(Detection_Pattern, Ontology, TermID)

write_tsv(
  triple_detection,
  file.path(OUTPUT_DIR, "Objective4_Triple_Descriptive_Patterns.tsv")
)

# ------------------------------------------------------------------------------
# 9. Sensibilidade por Tier
# ------------------------------------------------------------------------------

message("[8/8] Executando análises de sensibilidade por Tier...")

tier_sets <- list(
  Tier_A = "Tier_A_High_Confidence",
  Tier_AB = c("Tier_A_High_Confidence", "Tier_B_Rate_Heterogeneity"),
  Tier_ABC = c("Tier_A_High_Confidence", "Tier_B_Rate_Heterogeneity", "Tier_C_Exploratory")
)

make_tier_foregrounds <- function(df, tiers) {
  list(
    Node12_Expansion = df %>% filter(Evidence_Tier %in% tiers, Change_Node12_Core_Velloziaceae > 0) %>% pull(FamilyID),
    Node12_Contraction = df %>% filter(Evidence_Tier %in% tiers, Change_Node12_Core_Velloziaceae < 0) %>% pull(FamilyID),
    Vtub_Expansion = df %>% filter(Evidence_Tier %in% tiers, Change_Vtub > 0) %>% pull(FamilyID),
    Vtub_Contraction = df %>% filter(Evidence_Tier %in% tiers, Change_Vtub < 0) %>% pull(FamilyID),
    Xvis_Expansion = df %>% filter(Evidence_Tier %in% tiers, Change_Xvis > 0) %>% pull(FamilyID),
    Xvis_Contraction = df %>% filter(Evidence_Tier %in% tiers, Change_Xvis < 0) %>% pull(FamilyID),
    Vper_Expansion = df %>% filter(Evidence_Tier %in% tiers, Change_Vper > 0) %>% pull(FamilyID),
    Vper_Contraction = df %>% filter(Evidence_Tier %in% tiers, Change_Vper < 0) %>% pull(FamilyID)
  )
}

sensitivity_results <- imap_dfr(
  tier_sets,
  function(tiers, tier_label) {
    tier_foregrounds <- make_tier_foregrounds(data_full, tiers)

    imap_dfr(
      tier_foregrounds,
      function(fg_ids, contrast_name) {
        if (length(unique(fg_ids)) < MIN_TERM_FOREGROUND_N) {
          return(tibble())
        }

        run_all_ontologies(
          fg_ids = fg_ids,
          contrast_name = contrast_name,
          analysis_label = tier_label,
          simplify_go = SIMPLIFY_GO
        )$res_df
      }
    )
  }
)

write_tsv(
  sensitivity_results,
  file.path(OUTPUT_DIR, "Objective5_Tier_Sensitivity_All.tsv")
)

stability_summary <- sensitivity_results %>%
  filter(
    Reportable == TRUE,
    FDR <= FDR_THRESHOLD
  ) %>%
  group_by(Contrast, Ontology, TermID, TermName) %>%
  summarise(
    Tiers_Significant = paste(sort(unique(Analysis)), collapse = ","),
    N_Tiers_Significant = n_distinct(Analysis),
    Min_FDR = min(FDR, na.rm = TRUE),
    Max_FDR = max(FDR, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  mutate(
    Robustness_Category = case_when(
      N_Tiers_Significant == 3 ~ "Significativo_em_Tier_A_AB_ABC",
      str_detect(Tiers_Significant, "Tier_A") & N_Tiers_Significant >= 2 ~ "Inclui_Tier_A_e_replica_em_outro_tier",
      Tiers_Significant == "Tier_A" ~ "Especifico_Tier_A",
      TRUE ~ "Sensivel_ao_tier"
    )
  ) %>%
  arrange(Contrast, Ontology, desc(N_Tiers_Significant), Min_FDR)

write_tsv(
  stability_summary,
  file.path(OUTPUT_DIR, "Objective5_Tier_Stability_Summary.tsv")
)

# ------------------------------------------------------------------------------
# 10. Mensagem final
# ------------------------------------------------------------------------------

message("")
message("Análise concluída.")
message(sprintf("Resultados salvos em: %s", OUTPUT_DIR))
message("")
message("Arquivos principais:")
message("  - Primary_All_Terms_TierA_raw.tsv")
message("  - Primary_Reportable_TierA_raw.tsv")
message("  - Primary_All_Terms_TierA_simplified.tsv")
message("  - Primary_Reportable_TierA_simplified.tsv")
message("  - Objective1_Core_Node12.tsv")
message("  - Objective2_DT_Vtub_Xvis.tsv")
message("  - Objective2_Direct_Comparison_Vtub_vs_Xvis.tsv")
message("  - Objective3_Vper_Avoidant.tsv")
message("  - Objective4_Triple_Descriptive_Patterns.tsv")
message("  - Objective5_Tier_Sensitivity_All.tsv")
message("  - Objective5_Tier_Stability_Summary.tsv")
message("")
message("FDR principal: coluna FDR")
message("FDR da comparação direta: FDR_difference")
message("GO simplificado: Simplified == TRUE")
message("KEGG não simplificado")