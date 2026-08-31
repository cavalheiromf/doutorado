# Scientific Writer Outline — Unified Chapter 1, Round 1

## Working title and central argument

- Working title: **Gene-Family Turnover across Comparative Scales in Velloziaceae: Evidence from Paired *Vellozia* Proteomes and a Seven-Taxon Analysis**.
- Central argument: the current analyses support marked, lineage-dependent differences in gene-family turnover at both a close pairwise scale and a broader seven-taxon scale. These patterns are useful for generating hypotheses about contrasting drought strategies, but they do not establish causal adaptation, ancestral desiccation-tolerance states, or a Gondwanan-vicariance scenario.
- Evidence hierarchy: exact analytical statements derive only from A-001–A-019; biological context derives only from L-001–L-012 and respects each source's taxonomic boundary.

## Abstract

- Establish campos rupestres and Velloziaceae as a system for studying heterogeneous drought strategies.
- Summarize the three-proteome and seven-taxon OrthoFinder datasets and the two CAFE5 analyses.
- Report the central exact results: 16,953 orthogroups and 4,445 single-copy orthogroups in the three-proteome analysis; 16,532 orthogroups and 1,424 all-species single-copy orthogroups in the seven-taxon analysis; pairwise and seven-taxon branch asymmetries.
- State that exploratory functional categories differ between the two focal lineages, without claiming causality.
- End with the evidence-safe conclusion and principal limitations.

## 1. Introduction

- Introduce campos rupestres as an old, climatically buffered, infertile and species-rich landscape using L-001; add a cautious Velloziaceae nutrient-acquisition example from L-004.
- Frame plant responses to water limitation as heterogeneous strategies rather than a single continuum, using L-002, L-003, L-009 and L-010.
- Describe genomic diversity among resurrection plants using L-007, L-008 and L-012, emphasizing seed-program recruitment, convergence, and lineage specificity.
- Identify the gap: close-pair comparisons and broader phylogenetic context are often disconnected, and gene-family counts are easily overinterpreted as phenotype history.
- State objectives: quantify orthology and family turnover in a focal three-proteome comparison; place it in a seven-taxon context; distinguish observations from functional/evolutionary hypotheses.

## 2. Materials and Methods

### 2.1 Comparative datasets and scope

- Provide only minimum proteome provenance; defer sequencing, assembly, and structural annotation to the Appendix.
- Three-proteome panel: Ath, Vper and Vtub; seven-taxon panel: Abra, Ath, Dala, Ptec, Vper, Vtub and Xvis.
- Explicitly acknowledge that the seven-taxon source/version/checksum manifest remains incomplete.

### 2.2 Orthology inference

- OrthoFinder v3.1.5 with DIAMOND, FAMSA and FastTree for both analyses.
- Separate the three-proteome and seven-taxon outputs; do not cite unvalidated method papers.
- Define the OrthoFinder species tree as an analysis output, not a dated or bootstrap-supported phylogeny.

### 2.3 Gene-family evolution

- Pairwise CAFE5: 16,391 families retained by the >100-copy filter; 16,032 modeled after root-absence filtering; arbitrary branch length 1.0; Base model only; no error model documented.
- Seven-taxon CAFE5: 16,524 families after the >100-copy filter; 9,209 modeled; assumed calibration values; Base and Gamma outputs kept distinct.
- Identify the existing branch summary explicitly as Base-model output.

### 2.4 Exploratory functional analysis and interpretation policy

- Pairwise enrichment is over annotated orthogroups, using 14,210 annotated orthogroups as background and 819/1,347 expanding targets for Vtub/Vper.
- Categories derive from substring rules applied to predominant free-text annotations; report as exploratory candidate functions.
- No seven-taxon functional claims because no traceable chapter-3 functional artifact exists.

## 3. Results

### 3.1 Orthogroup structure at the focal scale

- Report A-002–A-005 exactly, including per-species assignment, rooted topology, directional orthologue totals, and duplication events.
- Warn that directional orthologue totals are not unique one-to-one pairs.

### 3.2 Pairwise CAFE5 turnover and exploratory functional signals

- Report A-006–A-009 exactly: model scale, lambda, family changes, 412 family-wide significant families.
- Present selected family counts from A-008 with corrected root/tip values and cautious annotation language.
- Present selected q-significant categories from A-009; clarify that target/background values are orthogroup hits, not gene counts.

### 3.3 Orthogroup structure in the seven-taxon panel

- Report A-011–A-014 exactly; describe topology only within sampled taxa and avoid bootstrap claims.

### 3.4 Seven-taxon CAFE5 dynamics under assumed calibrations

- Report A-015–A-018 exactly.
- Identify Base and Gamma likelihood/lambda results separately; do not infer model superiority from likelihood alone.
- Present Base branch table and correct node identities, especially nodes 12 and 13.
- State explicitly that node 13 is the Vper+Vtub ancestor and that the data do not reconstruct phenotype states.

## 4. Discussion

### 4.1 Differential turnover as a cross-scale pattern

- Integrate pairwise OrthoFinder duplication and CAFE5 asymmetry with the seven-taxon Base table.
- Interpret turnover as hypothesis-generating evidence affected by biological history, annotation, sampling, and model assumptions.

### 4.2 Candidate functional emphases in the focal pair

- Vtub: exploratory enrichment of mobile elements, plastid ribosome/translation, photosynthetic electron transport/NDH, and chloroplast import.
- Vper: exploratory enrichment of P450, UGT, wall-associated kinases, LRR receptor-like kinases, and NB-LRR categories.
- Connect only at a general comparative level to L-002, L-003, L-007, L-011 and L-012; do not assign unmeasured focal physiology or causal mechanisms.

### 4.3 What the broader analysis does not resolve

- Use L-005 to reject the Gondwanan-vicariance framing and to show why assumed ages are not estimates.
- Use L-008 and L-009 to frame convergence, parallelism and heterogeneity as live alternatives.
- State that ancestral-state reconstruction, traceable functional annotation, and defensible dating are required before phenotype-history claims.

### 4.4 Limitations and computational roadmap

- Discuss missing synteny, Ka/Ks, phylogenomic support/discordance, time calibration, seven-taxon functional annotation, proteome provenance, and enrichment ontology limitations.
- Treat all as limitations or future dry-lab analyses; do not anticipate outcomes.

## 5. Conclusions

- Reiterate that current evidence establishes differential gene-family turnover, not adaptive causation or ancestral phenotype polarity.
- State how the paired and seven-taxon scales complement one another.
- End with at most one transition sentence reserving targeted OSCA work for Chapter 2.

## References

- Include only validated L-* works actually cited in the prose.
- Apply ABNT author-date citations in text and ABNT NBR 6023-compatible entries using the validated metadata in `literature_evidence.md`.
