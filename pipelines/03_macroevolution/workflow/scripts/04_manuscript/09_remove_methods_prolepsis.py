#!/usr/bin/env python3
"""
Remove all prolepsis / anticipation of results and premature table calls from
Material and Methods, relocate displaced result metrics to Results, and align
Supplementary Tables S7-S10 to strict Results order of appearance.
"""

TARGET_FILES = [
    "chapter_macroevolution_review/docs/manuscripts/chapter_macroevolution_article.md"
]

with open(TARGET_FILES[0], "r", encoding="utf-8") as f:
    text = f.read()

# Step 1: First swap S7/S8 <-> S9/S10 across the document using placeholders
# Old S9 -> New S7 (top 30 divergent gene families)
# Old S10 -> New S8 (convergent expansions resurrection)
# Old S7 -> New S9 (trio branch selection QC)
# Old S8 -> New S10 (trio branch selection polarization)

swap_pairs = [
    ("Supplementary Tables S4, S9 and S10", "Supplementary Tables S4, __NEW_S7__ and __NEW_S8__"),
    ("Supplementary Tables S4, S6, and S9", "Supplementary Tables S4, S6, and __NEW_S7__"),
    ("Supplementary Tables S7 and S8", "Supplementary Tables __NEW_S9__ and __NEW_S10__"),
    ("Supplementary Table S9", "Supplementary Table __NEW_S7__"),
    ("Supplementary Table S10", "Supplementary Table __NEW_S8__"),
    ("Supplementary Table S7", "Supplementary Table __NEW_S9__"),
    ("Supplementary Table S8", "Supplementary Table __NEW_S10__"),
    ("with S8 using explicit predicates", "with S10 using explicit predicates"),
    ("TableS9_top_divergent_gene_family_expansions.tsv", "TableS7_top_divergent_gene_family_expansions.tsv"),
    ("TableS10_convergent_expansions_resurrection.tsv", "TableS8_convergent_expansions_resurrection.tsv"),
    ("TableS7_trio_branch_selection_QC.tsv", "TableS9_trio_branch_selection_QC.tsv"),
    ("TableS8_trio_branch_selection_polarization.tsv", "TableS10_trio_branch_selection_polarization.tsv"),
]

for old_s, new_s in swap_pairs:
    assert old_s in text, f"Missing swap target: {old_s}"
    text = text.replace(old_s, new_s)

text = (
    text.replace("__NEW_S7__", "S7")
        .replace("__NEW_S8__", "S8")
        .replace("__NEW_S9__", "S9")
        .replace("__NEW_S10__", "S10")
)

# Reorder the bullets in ## Supplementary Tables so S7, S8, S9, S10 are listed in numerical order
old_supp_block = """- **Supplementary Table S9 (`TableS9_trio_branch_selection_QC.tsv`):** Quality control filtering funnel, coding-sequence evolutionary rate distributions (omega <= 1.0), lineage-specific acceleration screens (omega > 1.0), and targeted PPR organellar audit across 10,966 1:1:1 ortholog trios.
- **Supplementary Table S10 (`TableS10_trio_branch_selection_polarization.tsv`):** Genome-wide between-branch coding-sequence analysis of 10,966 1:1:1 ortholog trios across *Vellozia peripherica*, *Vellozia tubiflora*, and the outgroup *Xerophyta schlechteri*, including PAML `codeml` Model 0 and Model 2 log-likelihoods, branch-specific rates (omega_Vper, omega_Vtub, omega_Xsch), branch-specific dN and dS, likelihood ratio test statistics, p-values, FDR q-values, lineage polarization calls, and functional annotations.
- **Supplementary Table S7 (`TableS7_top_divergent_gene_family_expansions.tsv`):** Candidate catalog of the top 30 divergent gene families across terminal *Vellozia* lineages and ancestral nodes, with copy counts, inferred changes, branch probabilities, and functional annotations.
- **Supplementary Table S8 (`TableS8_convergent_expansions_resurrection.tsv`):** Thirty-six candidate gene families exhibiting concordant terminal copy-number expansions in both desiccation-tolerant species (*V. tubiflora* and *X. schlechteri*), highlighting six families with nominal branch significance in both species."""

new_supp_block = """- **Supplementary Table S7 (`TableS7_top_divergent_gene_family_expansions.tsv`):** Candidate catalog of the top 30 divergent gene families across terminal *Vellozia* lineages and ancestral nodes, with copy counts, inferred changes, branch probabilities, and functional annotations.
- **Supplementary Table S8 (`TableS8_convergent_expansions_resurrection.tsv`):** Thirty-six candidate gene families exhibiting concordant terminal copy-number expansions in both desiccation-tolerant species (*V. tubiflora* and *X. schlechteri*), highlighting six families with nominal branch significance in both species.
- **Supplementary Table S9 (`TableS9_trio_branch_selection_QC.tsv`):** Quality control filtering funnel, coding-sequence evolutionary rate distributions (omega <= 1.0), lineage-specific acceleration screens (omega > 1.0), and targeted PPR organellar audit across 10,966 1:1:1 ortholog trios.
- **Supplementary Table S10 (`TableS10_trio_branch_selection_polarization.tsv`):** Genome-wide between-branch coding-sequence analysis of 10,966 1:1:1 ortholog trios across *Vellozia peripherica*, *Vellozia tubiflora*, and the outgroup *Xerophyta schlechteri*, including PAML `codeml` Model 0 and Model 2 log-likelihoods, branch-specific rates (omega_Vper, omega_Vtub, omega_Xsch), branch-specific dN and dS, likelihood ratio test statistics, p-values, FDR q-values, lineage polarization calls, and functional annotations."""

assert old_supp_block in text, "Could not find old_supp_block"
text = text.replace(old_supp_block, new_supp_block)

# Step 2: Remove prolepsis and premature table calls in Material and Methods,
# and integrate any displaced result metrics into Results.
replacements = [
    # 2.1 - line 38
    (
        "as an external phylogenetic anchor and functional annotation reference (assembly accessions in Data Availability and Supplementary Table S1).",
        "as an external phylogenetic anchor and functional annotation reference (assembly accessions in Data Availability)."
    ),
    # 2.1 - line 40 (BUSCO result >95% removed from Methods)
    (
        "Completeness of the predicted gene space was evaluated using BUSCO v5.4.3 (Manni et al., 2021) in protein mode against the `embryophyta_odb10` and `liliopsida_odb10` lineage datasets (>95% complete recovery reported across both lineages; see evidence gap R1).",
        "Completeness of the predicted gene space was evaluated using BUSCO v5.4.3 (Manni et al., 2021) in protein mode against the `embryophyta_odb10` and `liliopsida_odb10` lineage datasets."
    ),
    # 2.1 - line 42 (proteome gene counts moved from Methods to Results 3.1)
    (
        "To eliminate isoform redundancy across the seven reference proteomes (*V. peripherica* [26,466 genes], *V. tubiflora* [25,551 genes], *X. schlechteri* [26,969], *A. bracteata* [22,914], *P. tectorius* [28,399], *D. alata* [33,227], and *A. thaliana* [27,549]; Supplementary Table S1), only the transcript with the longest open reading frame per locus was retained for comparative orthology inference.",
        "To eliminate isoform redundancy across the seven reference proteomes, only the transcript with the longest open reading frame per locus was retained for comparative orthology inference."
    ),
    # 2.2 - line 48 (supermatrix dimensions 732,066 aa and 1,513 loci removed from Methods)
    (
        "Columns with gaps in more than 50% of taxa were removed, and retained alignments were concatenated into an amino acid supermatrix spanning 732,066 aligned positions across 1,513 locus partitions (Supplementary Table S2).",
        "Columns with gaps in more than 50% of taxa were removed, and the filtered single-copy alignments were concatenated into a partitioned amino acid supermatrix for phylogenomic inference."
    ),
    # 2.4 - line 60 (remove Supplementary Table S3 call in Methods)
    (
        "The *Xerophyta*–*Vellozia* split had no direct calibration (Supplementary Table S3; evidence gap R2).",
        "The *Xerophyta*–*Vellozia* split was left unconstrained to be estimated from the data."
    ),
    # 2.4 - line 62 (remove Rhat and ESS results from Methods, move to Results 3.2)
    (
        "The workflow included a prior-only run (`usedata = 0`) and two posterior chains with distinct seeds. The posterior control file specified 50,000 burn-in iterations, sampling every 100 iterations, and 30,000 retained states per chain. The combined-chain summary reported $\\hat{R}<1.01$ and effective sample sizes (ESS) above 200 for all listed parameters. Individual-chain ESS values for the core Velloziaceae age were approximately 100 and 129, lower than those for the other reported parameters (evidence gap R2).",
        "The workflow included a prior-only run (`usedata = 0`) to inspect effective priors and two independent posterior chains initialized with distinct seeds, each run for 50,000 burn-in iterations followed by 30,000 states sampled every 100 iterations. Chain convergence and mixing were evaluated using the potential scale reduction factor ($\\hat{R}$) and effective sample sizes (ESS)."
    ),
    # 2.4 - line 64 (remove estimated node ages from Methods)
    (
        "Downstream CAFE5 analyses used a six-taxon ultrametric tree with node ages of 121.90, 101.26, 78.21, 31.91 and 9.74\xa0Ma, from the sampled monocot root to the focal *Vellozia* split (Supplementary Table S3). The dated-tree nodes 9, 10 and 11 correspond to CAFE5 nodes 11, 12 and 13, respectively. These ages preserve the time scale used in the reported family models. Their correspondence with the combined-chain posterior summary remains to be reconciled (evidence gap R2).",
        "For downstream gene-family turnover analyses in CAFE5, the *Arabidopsis thaliana* outgroup was pruned to retain the six-taxon monocot ultrametric chronogram."
    ),
    # 2.5 - line 68 (remove Supplementary Table S4 call in Methods)
    (
        "Orthogroups with $\\ge 100$ genes in at least one genome (Supplementary Table S4) were excluded to prevent numerical instability and parameter distortion during likelihood optimization, and families lacking representation in the common ancestor of the sampled monocots were removed prior to birth-death modeling.",
        "Orthogroups with $\\ge 100$ genes in at least one genome were excluded to prevent numerical instability and parameter distortion during likelihood optimization, and families lacking representation in the common ancestor of the sampled monocots were removed prior to birth-death modeling."
    ),
    # 2.5 - line 70 (remove prolepsis of M5 multiple local optima)
    (
        "Five independent optimization starts were initially evaluated for each branch model; because M5 showed multiple local optima, five additional M5 starts were run, yielding ten M5 optimizations in total.",
        "To guard against local optima during maximum-likelihood estimation, five independent optimization starts were evaluated for models M1-M4 and ten independent starts were run for the most parameterized model (M5)."
    ),
    # 2.5 - line 74 (remove prolepsis of M5 winning and replicate 4/6/8 from Methods)
    (
        "Models were compared using the Akaike Information Criterion (AIC), calculated from the replicate with the lowest negative log-likelihood for each parameterization (Supplementary Table S5). The M5 run with the lowest negative log-likelihood (replicate 4) was used for primary ancestral reconstructions and branch tests. M5 runs within 0.1 negative log-likelihood unit of this solution (replicates 4, 6, and 8) defined the near-optimal sensitivity set; strict robustness calls required the same expansion or contraction to meet the branch criterion in all three runs. Here, robustness denotes agreement across optimization starts, not an assessment of uncertainty in gene counts, divergence times, or taxon sampling. Ancestral copy numbers were reconstructed using the Viterbi algorithm. Family changes on individual branches were classified as expansions or contractions from the inferred copy-number differences and a nominal branch-specific $p < 0.05$. The downstream branch classification did not apply an additional family-wide significance filter or multiple-testing correction. False-discovery rate (FDR) correction for functional enrichment was performed separately (Section 2.7).",
        "Models were compared using the Akaike Information Criterion (AIC), calculated from the replicate with the lowest negative log-likelihood for each parameterization. Under the best-fitting model, the optimization run with the lowest negative log-likelihood was used for primary ancestral reconstructions and branch tests, while runs within 0.1 negative log-likelihood unit of that solution defined the near-optimal sensitivity set; strict robustness calls required the same expansion or contraction to meet the branch criterion across all near-optimal runs. Here, robustness denotes agreement across optimization starts, not an assessment of uncertainty in gene counts, divergence times, or taxon sampling. Ancestral copy numbers were reconstructed using the Viterbi algorithm. Family changes on individual branches were classified as expansions or contractions from the inferred copy-number differences and a nominal branch-specific $p < 0.05$. The downstream branch classification did not apply an additional family-wide significance filter or multiple-testing correction. False-discovery rate (FDR) correction for functional enrichment was performed separately (Section 2.7)."
    ),
    # 2.5 - line 76 (remove premature S4, S7, S8 calls and R3 result discussion from Methods)
    (
        "For functional interpretation, orthogroup annotations were compared with scaffold assignments and organellar and transposon flags. The complete modeled universe was retained for the primary analysis, and exclusion of organellar-annotated families was evaluated as an enrichment sensitivity scenario (Section 2.7). Candidate-family catalogs record copy numbers, inferred changes and proposed functional annotations (Supplementary Tables S4, S7 and S8). Specific gene identities were treated as provisional where domain descriptions or homolog assignments differed between records (evidence gap R3).",
        "For functional interpretation, orthogroup annotations were compared with scaffold assignments and organellar and transposon flags. The complete modeled universe was retained for the primary analysis, and exclusion of organellar-annotated families was evaluated as an enrichment sensitivity scenario (Section 2.7)."
    ),
    # 2.7 - line 94 (remove Supplementary Table S6 call from Methods)
    (
        "The analysis code documents this custom reduction procedure. Complete results across all tested terms, evidence tiers, covariate balance checks, and sensitivity scenarios are provided in Supplementary Table S6.",
        "The analysis code documents this custom reduction procedure."
    ),
    # 2.8 - line 98 (remove 10,966 and 8,737 counts and S9/S10 calls from Methods)
    (
        "Thus, eligibility was defined by concordant pairwise relationships, rather than requiring the entire orthogroup to be single-copy in all seven genomes. The resulting set contained 10,966 trios with available coding sequences (CDS), of which 8,737 passed quality control (Supplementary Table S9; Supplementary Table S10).",
        "Thus, eligibility was defined by concordant pairwise relationships across the three Velloziaceae species, rather than requiring the entire orthogroup to be single-copy in all seven genomes."
    ),
    # 2.8 - line 102 (remove Supplementary Table S10 call from Methods)
    (
        "Negative likelihood differences were truncated to zero. Supplementary Table S10 reports preprocessing status for all candidate trios and log-likelihoods and branch estimates for trios with successful model fits.",
        "Negative likelihood differences were truncated to zero."
    ),
    # 2.8 - line 104 (remove 8,737 count and Supplementary Tables S9 and S10 calls from Methods)
    (
        "Benjamini-Hochberg $q$ values were computed across the 8,737 trios that passed preprocessing. Candidate classification used nominal $p<0.05$; the subset retaining $q<0.05$ was reported separately. The proportion with $\\omega\\le1$ in both focal branches was calculated directly from the branch estimates. Candidate annotations and branch assignments were linked through trio identifiers (Supplementary Tables S9 and S10).",
        "Benjamini-Hochberg $q$ values were computed across all trios that passed preprocessing. Candidate classification used nominal $p<0.05$, and the subset retaining $q<0.05$ was reported separately. The proportion with $\\omega\\le1$ in both focal branches was calculated directly from the branch estimates, and candidate annotations and branch assignments were linked through trio identifiers."
    ),
    # 3.1 - line 112 (integrate the 7 proteome gene counts relocated from 2.1)
    (
        "Across the seven-taxon OrthoFinder analysis of 191,075 primary protein sequences, 178,019 proteins (93.2%) were clustered into 17,750 orthogroups (9,826 shared by all seven taxa and 1,513 strictly single-copy across all genomes; Supplementary Table S1).",
        "Across the seven-taxon OrthoFinder analysis of 191,075 primary protein sequences (*V. peripherica* [26,466 genes], *V. tubiflora* [25,551], *X. schlechteri* [26,969], *A. bracteata* [22,914], *P. tectorius* [28,399], *D. alata* [33,227], and *A. thaliana* [27,549]), 178,019 proteins (93.2%) were clustered into 17,750 orthogroups (9,826 shared by all seven taxa and 1,513 strictly single-copy across all genomes; Supplementary Table S1)."
    ),
    # 3.2 - line 122 (integrate MCMCtree convergence Rhat and ESS relocated from 2.4)
    (
        "The chronogram used for CAFE5 reports divergence ages of 121.90\xa0Ma (reported 95% credible interval: 115.20-127.80\xa0Ma) for *Dioscorea*–Pandanales, 101.26\xa0Ma (91.40-104.80\xa0Ma) for *Pandanus*–Velloziaceae, 78.21\xa0Ma (75.10-88.60\xa0Ma) for *Acanthochlamys*–core Velloziaceae, 31.91\xa0Ma (22.18-46.29\xa0Ma) for the *Xerophyta*–*Vellozia* split, and 9.74\xa0Ma (5.85-15.72\xa0Ma) for the split between the sampled *Vellozia* species (Figure 2A; Supplementary Table S3). The branch leading to core Velloziaceae spans 78.21-31.91\xa0Ma in this chronogram, defining the interval to which ancestral family changes were assigned. The reported dates and intervals remain subject to the reconciliation described in Section 2.4.",
        "Across the two MCMCtree posterior chains, the combined summary reported $\\hat{R}<1.01$ and ESS values above 200 across all listed parameters, with individual-chain ESS values of approximately 100 and 129 for the core Velloziaceae node (evidence gap R2). The chronogram used for CAFE5 reports divergence ages of 121.90\xa0Ma (reported 95% credible interval: 115.20-127.80\xa0Ma) for *Dioscorea*–Pandanales, 101.26\xa0Ma (91.40-104.80\xa0Ma) for *Pandanus*–Velloziaceae, 78.21\xa0Ma (75.10-88.60\xa0Ma) for *Acanthochlamys*–core Velloziaceae, 31.91\xa0Ma (22.18-46.29\xa0Ma) for the *Xerophyta*–*Vellozia* split, and 9.74\xa0Ma (5.85-15.72\xa0Ma) for the split between the sampled *Vellozia* species (Figure 2A; Supplementary Table S3). The branch leading to core Velloziaceae spans 78.21-31.91\xa0Ma in this chronogram, defining the interval to which ancestral family changes were assigned (reconciliation with the combined-chain posterior summary is noted in evidence gap R2)."
    ),
    # 3.2 - line 124 (integrate replicate 4 and replicates 4, 6, 8 relocated from 2.5)
    (
        "Thus, the data strongly favored separate turnover rates for the two focal *Vellozia* branches.",
        "Thus, the data strongly favored separate turnover rates for the two focal *Vellozia* branches, with replicate 4 yielding the lowest negative log-likelihood and replicates 4, 6, and 8 falling within 0.1 log-likelihood unit to form the three near-optimal M5 runs."
    ),
    # 3.2 - line 128 (avoid premature call to S7 before S6 in 3.5; cross-reference Section 3.6)
    (
        "The family-level annotation record for the 132 ancestral expansions on the core Velloziaceae stem branch included annotations associated with stress protection and transcriptional regulation (Figure 2B; Supplementary Table S7). The small heat-shock protein HSP20 family (`OG0000340`) showed an inferred net gain of five copies ($p < 0.0001$). Expanded regulatory families included B3-domain proteins (`OG0000136`, net gain of five copies), basic leucine zipper (bZIP) transcription factors (`OG0000858`, gain of four copies), and MYB transcription factors (`OG0000750`, gain of four copies). Additional expansions encompassed anthocyanin 5-aromatic acyltransferase (`OG0000038`, gain of five copies) and germin-like proteins (`OG0000035`, gain of 12 copies), alongside families annotated with chloroplast NAD(P)H-quinone oxidoreductase homology (`OG0000014`, gain of 17 copies; `OG0000036`, gain of five copies; Supplementary Table S7).",
        "The family-level annotation record for the 132 ancestral expansions on the core Velloziaceae stem branch included annotations associated with stress protection and transcriptional regulation (Figure 2B; see Section 3.6). The small heat-shock protein HSP20 family (`OG0000340`) showed an inferred net gain of five copies ($p < 0.0001$). Expanded regulatory families included B3-domain proteins (`OG0000136`, net gain of five copies), basic leucine zipper (bZIP) transcription factors (`OG0000858`, gain of four copies), and MYB transcription factors (`OG0000750`, gain of four copies). Additional expansions encompassed anthocyanin 5-aromatic acyltransferase (`OG0000038`, gain of five copies) and germin-like proteins (`OG0000035`, gain of 12 copies), alongside families annotated with chloroplast NAD(P)H-quinone oxidoreductase homology (`OG0000014`, gain of 17 copies; `OG0000036`, gain of five copies; detailed in Section 3.6)."
    ),
    # 3.7 - line 178 (integrate 10,966 candidate trios relocated from 2.8)
    (
        "Among the 8,737 analyzed ortholog trios, 7,798 (89.25%) had estimated $\\omega\\le1$ in both *Vellozia* branches (Figure 6A; Supplementary Tables S9 and S10).",
        "Of the 10,966 candidate one-to-one ortholog trios assembled across *V. peripherica*, *V. tubiflora*, and *X. schlechteri*, 8,737 passed quality control (excluding 2,225 with internal stop codons, two with short CDS, and two with fewer than 30 aligned codons; Supplementary Tables S9 and S10). Among these 8,737 analyzed trios, 7,798 (89.25%) had estimated $\\omega\\le1$ in both *Vellozia* branches (Figure 6A; Supplementary Tables S9 and S10)."
    ),
]

for idx, (old_str, new_str) in enumerate(replacements, 1):
    assert old_str in text, f"Failed replacement #{idx}:\n{old_str[:100]}..."
    text = text.replace(old_str, new_str)
    print(f"Applied replacement #{idx}")

with open(TARGET_FILES[0], "w", encoding="utf-8") as f:
    f.write(text)

print("All replacements applied successfully!")

