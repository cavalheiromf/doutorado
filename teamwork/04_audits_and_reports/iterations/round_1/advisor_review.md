# PhD Advisor Review — Unified Chapter 1, Round 1

STATUS: REVISE

## STRENGTHS

- The manuscript has a coherent biological argument centred on lineage-dependent gene-family turnover rather than reproducing the sequence of analyses from the two source drafts.
- The Introduction establishes the ecological setting, distinguishes drought resistance from desiccation survival, and respects the taxonomic boundaries of the physiological literature.
- The manuscript correctly removes unsupported synteny, Ka/Ks, positive-selection, ancestral-state, and Gondwanan-vicariance conclusions.
- The seven-taxon node map is now biologically correct: node 13 is the ancestor of the two sampled *Vellozia* proteomes, whereas node 12 joins that pair with *Xerophyta viscosa*.
- The Results consistently distinguish observed counts from functional interpretation. The focal enrichment is explicitly described as substring-based and exploratory.
- The Discussion repeatedly separates copy-number association from expression, biochemical activity, phenotype, and adaptation. This is appropriately cautious for desiccation tolerance, gene-family dynamics, and evolutionary mechanism.
- Assembly, sequencing, structural annotation, and associated quality control remain outside the chapter body and are correctly assigned to Appendix material.
- OSCA is restricted to one transition sentence reserving the targeted family analysis for Chapter 2.

## BLOCKERS

[]

## MAJOR_REVISIONS

### ADV-001 — Do not present the focal and seven-taxon analyses as independent replication

- **Location:** Results 3.1, final paragraph; Discussion 4.1, first and third paragraphs; Abstract and Conclusions where the analyses are said to “establish” a cross-scale pattern.
- **Problem:** The same focal proteomes occur in both datasets, and both OrthoFinder and CAFE5 depend on the same underlying gene models and family-size information. The two OrthoFinder runs also define different family universes, and no orthogroup crosswalk was presented. Consequently, the seven-taxon analysis is a broader analytical context, not an independent replication of the focal result. The phrases “independently indicate,” “independent seven-taxon Base summary,” and “tests how exceptional” overstate the inferential relationship between the analyses.
- **Required action:** State explicitly that the analyses are methodologically and taxonomically distinct but non-independent. Describe the repeated direction of the focal-terminal asymmetry as qualitative consistency under two analytical contexts. Replace “tests how exceptional” with language such as “places the focal branch totals in a broader descriptive context.” Replace “establish” with “document, under the current inputs and models,” where appropriate.
- **Affected claims:** cross-scale convergence; robustness of the *V. peripherica*–*V. tubiflora* asymmetry; exceptionalness of focal turnover.
- **Evidence needed:** A-001–A-007, A-011–A-017.

### ADV-002 — Make the non-comparability of family universes explicit before comparing branch totals

- **Location:** Methods 2.1–2.4; Discussion 4.1.
- **Problem:** The chapter compares the direction of focal branch counts across a two-tip model of 16,032 families and a seven-taxon model of 9,209 root-present families, but it does not explicitly state that the family sets, orthogroup identifiers, filtering, taxon context, and branch-length scales differ. Readers could interpret the counts as directly comparable or as estimates from a harmonized model.
- **Required action:** Add a concise Methods statement that no one-to-one orthogroup crosswalk or formal cross-model effect-size comparison was performed. In the Discussion, restrict the comparison to directionality and avoid direct magnitude comparisons between the two CAFE5 runs.
- **Affected claims:** “correspondence across analyses”; “two complementary comparative scales.”
- **Evidence needed:** A-006–A-007, A-015–A-017.

### ADV-003 — Qualify CAFE5 significance as model-defined and nominal

- **Location:** Abstract; Methods 2.3–2.4; Results 3.2 and 3.4; Tables 2 and 5.
- **Problem:** The wording “significant” can be read as a generally multiplicity-controlled biological result. The inspected outputs show CAFE5 family-wide or branch classifications at the software's 0.05 threshold, whereas the evidence record does not document an additional false-discovery-rate correction for these CAFE5 tests. This differs from the explicitly FDR-adjusted exploratory enrichment results.
- **Required action:** Use formulations such as “flagged by CAFE5 at the nominal family-wide threshold of p <= 0.05” and “CAFE5-classified branch changes.” Add the threshold and model name to Table 5's caption or note. Preserve the distinction from the q-values in Table 3.
- **Affected claims:** 412 focal families; 661 Base and 460 Gamma families; all “significant expanded/contracted” branch counts.
- **Evidence needed:** A-007, A-016–A-017.

### ADV-004 — Complete the methodological citation foundation

- **Location:** Methods 2.2–2.5 and References.
- **Problem:** OrthoFinder, CAFE5, DIAMOND, FAMSA, FastTree, and the annotation/enrichment basis are described without validated method citations. A thesis chapter should cite the primary software or method sources, especially where the Discussion contrasts gene-tree reconciliation with birth–death modelling. The local literature pass explicitly marks the OrthoFinder and CAFE5 papers as unvalidated.
- **Required action:** Ask the Literature Curator to retrieve and validate the primary method sources, prioritising OrthoFinder and CAFE5. Cite only sources whose metadata and content have been verified and saved locally. DIAMOND, FAMSA, FastTree, and EggNOG should also be cited if they remain named in the final Methods.
- **Affected claims:** method description and the methodological contrast in Discussion 4.1.
- **Evidence needed:** new validated L-* records.

## MINOR_REVISIONS

### ADV-MIN-001 — Clarify the status of focal ecological labels

- **Location:** Introduction, third paragraph.
- **Problem:** “Contrasting ecological descriptions associated with” the focal species is deliberately cautious but still leaves the origin of those working classifications opaque.
- **Required action:** Either cite a direct focal-species source after targeted retrieval or state that the classifications originate from the project design and remain unvalidated by the local literature corpus. Do not let family-level studies appear to validate either focal taxon.

### ADV-MIN-002 — Avoid implying that the broad analysis establishes exceptionalness

- **Location:** Discussion 4.1, second and third paragraphs.
- **Problem:** Raw family-change counts across proteomes of different sizes and provenance do not provide a normalized test of whether a lineage is exceptional.
- **Required action:** Describe `Dala`, `Xvis`, and `Abra` as evidence of heterogeneity under the current Base model, not as a formal ranking of evolutionary rates or exceptionalness.

### ADV-MIN-003 — Improve taxon readability without overstating provenance

- **Location:** Table 4, Table 5, Results 3.3–3.4.
- **Problem:** File labels protect against unverified provenance but reduce biological readability.
- **Required action:** Where space permits, present “intended taxon (file label)” once, then retain file labels in model-specific tables. Preserve the explicit warning that accession and release provenance remain unaudited.

### ADV-MIN-004 — Tighten the final limitations paragraph

- **Location:** Discussion 4.4, final paragraph.
- **Problem:** The paragraph is scientifically sound but repeats several caveats already established in Sections 4.1–4.3.
- **Required action:** Retain the association-versus-adaptation distinction while shortening repeated statements. Use the recovered space to state the chapter's positive contribution: a traceable inventory of branch-level turnover and prioritised candidate families.

## MISSING_COMPUTATIONAL_ANALYSES

### ANA-001

- **analysis:** Proteome provenance and comparability audit for all seven inputs.
- **biological_question:** Are branch-specific turnover differences robust to taxon identity, release, isoform-selection, assembly completeness, and gene-model quality rather than driven by heterogeneous input annotation?
- **required_input_files:** The seven source proteomes; source accessions/releases; annotation GFF3 files where available; BUSCO or equivalent completeness outputs; checksums; canonical-isoform selection records.
- **expected_output:** A versioned manifest containing taxon, accession, release, protein count, isoform rule, completeness metrics, duplicate/haplotig warnings, and checksum, plus a comparability assessment for each proteome.
- **priority:** USEFUL
- **affected_claim:** Interpretation of unusually high turnover in `Dala`, `Xvis`, and the focal branches.
- **disposition:** RECORD_AS_LIMITATION
- **evidence_tier:** Community standard.

### ANA-002

- **analysis:** Harmonised cross-run orthogroup mapping and sensitivity analysis.
- **biological_question:** Does the qualitative *V. peripherica*–*V. tubiflora* turnover asymmetry persist for matched families across the focal and seven-taxon family universes?
- **required_input_files:** Focal and seven-taxon `Orthogroups.GeneCount.tsv` files; both CAFE5 input/count/change/family-result files; gene-to-orthogroup membership tables.
- **expected_output:** Crosswalk of shared genes/families, matched-family branch-change comparison, and sensitivity summary showing which conclusions persist after harmonisation.
- **priority:** USEFUL
- **affected_claim:** Cross-scale consistency of focal lineage asymmetry.
- **disposition:** LIMIT_CLAIM
- **evidence_tier:** Community standard.

### ANA-003

- **analysis:** CAFE5 error-model and Base-versus-Gamma model-selection audit.
- **biological_question:** How sensitive are family-wide and branch-specific turnover classifications to annotation error and among-family rate heterogeneity?
- **required_input_files:** Both CAFE5 count matrices; Base and Gamma outputs; replicate or independently assessed annotation error estimates; exact commands and software version.
- **expected_output:** Documented model comparison, error-model fit where supportable, model-specific branch tables, and a stability table for focal conclusions.
- **priority:** USEFUL
- **affected_claim:** Confidence in significant family and branch-change classifications.
- **disposition:** RECORD_AS_LIMITATION
- **evidence_tier:** Community standard.

### ANA-004

- **analysis:** Dedicated species-tree support and gene-tree discordance analysis.
- **biological_question:** How strongly do the single-copy loci support the inferred placement of *X. viscosa*, *A. bracteata*, and the focal *Vellozia* pair, and is there substantial gene-tree conflict?
- **required_input_files:** Verified single-copy orthologue alignments; per-locus gene trees; validated taxon manifest.
- **expected_output:** Supported concatenated tree, coalescent species tree, concordance/discordance statistics, and sensitivity to alignment/model choices.
- **priority:** USEFUL
- **affected_claim:** Seven-taxon topology and interpretation of internal CAFE5 nodes.
- **disposition:** RECORD_AS_LIMITATION
- **evidence_tier:** Benchmark-backed.

### ANA-005

- **analysis:** Branch-specific functional annotation ledger and ontology-based enrichment for the seven-taxon analysis.
- **biological_question:** Which traceable gene families underlie the inferred internal and terminal turnover profiles, and do any functional signals remain after using predefined ontologies and a documented background?
- **required_input_files:** Seven-taxon orthogroup membership; CAFE5 branch changes and probabilities; protein annotations with stable identifiers; GO/InterPro or equivalent annotations.
- **expected_output:** Branch-to-orthogroup-to-gene ledger, ontology-based enrichment tables with adjusted p-values, and auditable candidate-family lists.
- **priority:** USEFUL
- **affected_claim:** Any biological interpretation of the seven-taxon branch counts.
- **disposition:** RECORD_AS_LIMITATION
- **evidence_tier:** Community standard.

### ANA-006

- **analysis:** Species-level trait coding and ancestral-state reconstruction.
- **biological_question:** Is desiccation tolerance better explained as ancestral retention, repeated gain, or secondary loss within the sampled and expanded Velloziaceae phylogeny?
- **required_input_files:** Verified species phylogeny with branch-length uncertainty; taxonomically validated desiccation-tolerance states; denser family sampling.
- **expected_output:** Model-compared ancestral-state probabilities with uncertainty and sensitivity to trait coding and phylogenetic uncertainty.
- **priority:** OPTIONAL
- **affected_claim:** Origin of desiccation tolerance and putative secondary loss in *V. peripherica*.
- **disposition:** RECORD_AS_LIMITATION
- **evidence_tier:** Community standard.

### ANA-007

- **analysis:** Reproducible synteny, syntenic-depth, and Ks analysis.
- **biological_question:** Are focal copy-number differences embedded in conserved collinear blocks, tandem arrays, segmental duplications, or a whole-genome-duplication signature?
- **required_input_files:** Focal genome assemblies, GFF3/BED annotations, CDS and protein sequences, and verified orthology mappings.
- **expected_output:** Anchor and collinearity files, syntenic-depth profiles, validated block plots, duplication-mode classification, and Ks distributions with uncertainty.
- **priority:** OPTIONAL
- **affected_claim:** Any future claim about conserved blocks, translocations, paleoduplication, or duplication mechanism.
- **disposition:** RECORD_AS_LIMITATION
- **evidence_tier:** Community standard.

### ANA-008

- **analysis:** Codon-aware branch/site selection analysis for validated orthologues.
- **biological_question:** Do selected candidate families show evidence of altered selective constraint or episodic positive selection on focal branches?
- **required_input_files:** Verified coding sequences; high-confidence orthology/paralogy assignments; protein alignments; codon alignments; supported species/gene trees.
- **expected_output:** Alignment-quality report, branch/site model results with multiple-testing correction, and gene-level evidence ledger.
- **priority:** OPTIONAL
- **affected_claim:** Any future inference of purifying, relaxed, or positive selection.
- **disposition:** RECORD_AS_LIMITATION
- **evidence_tier:** Benchmark-backed.

## LITERATURE_GAPS

### LIT-001 — OrthoFinder primary method source

- **section_or_claim:** Methods 2.2; Discussion 4.1 distinction between reconciliation-based duplication inference and CAFE5 family-size modelling.
- **why_local_corpus_is_insufficient:** Emms and Kelly (2019) is cited in a source draft but was not validated from local full text during the literature pass.
- **suggested_openalex_query:** `OrthoFinder phylogenetic orthology inference comparative genomics Emms Kelly 2019 DOI`
- **priority:** CRITICAL

### LIT-002 — CAFE5 primary method source

- **section_or_claim:** Methods 2.3–2.4; interpretation of Base/Gamma birth–death models, family-wide probabilities, and error sensitivity.
- **why_local_corpus_is_insufficient:** Mendes et al. (2020) is cited in a source draft but was not validated from local full text during the literature pass.
- **suggested_openalex_query:** `CAFE5 gene family evolution computational analysis Mendes 2020 DOI`
- **priority:** CRITICAL

### LIT-003 — Direct ecological and physiological evidence for the focal *Vellozia* species

- **section_or_claim:** Introduction, third paragraph; rationale for contrasting *V. tubiflora* and *V. peripherica*.
- **why_local_corpus_is_insufficient:** The validated family-level and congeneric studies do not include either focal species, so they cannot establish their drought strategy, habitat, or physiology.
- **suggested_openalex_query:** `("Vellozia tubiflora" OR "Vellozia peripherica") desiccation tolerance drought physiology habitat`
- **priority:** USEFUL

### LIT-004 — Supporting software and annotation sources

- **section_or_claim:** Methods 2.2 and 2.5 for DIAMOND, FAMSA, FastTree, and EggNOG-derived annotation.
- **why_local_corpus_is_insufficient:** No validated primary method articles for these named tools were included in the current L-* ledger.
- **suggested_openalex_query:** `DIAMOND sequence aligner FAMSA multiple sequence alignment FastTree EggNOG mapper primary papers`
- **priority:** USEFUL

## OPTIONAL_SUGGESTIONS

- Consider a compact schematic distinguishing the focal and seven-taxon inputs, family universes, tree scales, and admissible inferences. This would make the non-independence and different inferential roles immediately visible.
- If a visual is added, prioritise a carefully labelled species-tree/CAFE branch summary over the existing two-tip bar plot, because the chapter's main contribution is the integration of comparative scales. Do not imply branch support or temporal calibration that was not estimated.

---

**Evidence tier:** Community standard for the review framework; manuscript-specific judgements are grounded in A-001–A-019 and L-001–L-012.
**Applicability:** Review applies only to `teamwork/iterations/round_1/chapter_snapshot.md` and the assigned round-1 evidence files.
**Main limitations:** The review did not re-run analyses, inspect sources outside the assigned evidence ledgers, or validate unregistered taxon provenance.
**What would need to be validated before implementation:** Software/method citations, proteome provenance, and any new computational analyses listed above.
