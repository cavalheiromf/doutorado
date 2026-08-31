# Evidence Audit — Unified Chapter 1, Round 1

**STATUS: REVISE**

**Frozen manuscript:** `teamwork/iterations/round_1/chapter_snapshot.md`  
**Analytical ledger:** `teamwork/iterations/round_1/analysis_inventory.md`  
**Literature ledger:** `teamwork/iterations/round_1/literature_evidence.md`  
**Citation system detected:** ABNT author–date  
**Audit date:** 2026-08-30

## Summary counts

| Audit item | Count | Result |
|---|---:|---|
| In-text citation instances reviewed individually | 20 | 20 supported; 0 partial; 0 unsupported; 0 contradicted; 0 missing source |
| Unique cited works | 12 | 12 mapped to local full texts; 12 represented in the reference list |
| Uncited works in the reference list | 0 | Pass |
| Manuscript tables checked | 5 | All 250 numeric table cells match the registered outputs |
| Numerical inconsistencies | 0 | Pass |
| Base/Gamma or node-identity inconsistencies | 0 | Pass |
| Retained traceability/wording defects | 4 | Revision required |
| Material ABNT/reference defects | 1 systematic defect affecting 12 entries | Revision required |

The central quantitative account is accurate. In particular, the audit confirmed the pairwise and seven-taxon OrthoFinder totals, the distinction between 1,339 orthogroups used for concatenation and 1,424 all-species single-copy orthogroups, all focal CAFE5 counts and enrichment values, the separate Base and Gamma global fits, all Base branch-summary values, and the mapping of node 13 to (`Vper`, `Vtub`) and node 12 to (`Xvis`, (`Vper`, `Vtub`)). No synteny, Ka/Ks, ancestral-state, focal-species physiology, or seven-taxon functional result was reintroduced.

## BLOCKERS

### AUD-001 — One Table 2 annotation is stronger than its local evidence

- **Location:** Section 3.2, Table 2, line 108; echoed generically in lines 87 and 192.
- **Problem:** OG0000094 is labelled “U-box E3 ubiquitin ligase.” The registered predominant local EggNOG description is “U-box domain-containing protein”; `top_families_annotated.md` does not contain OG0000094, and the gene-level annotation table does not establish E3-ligase activity for the orthogroup.
- **Required action:** Replace the Table 2 label with “U-box domain-containing protein.” Retain ubiquitination as a candidate interpretation only if explicitly marked as interpretive and supported by a validated source.
- **Evidence:** A-008; `analyses/chapter_1_genomics/annotation_db/vellozia_comparative_master_annotation.tsv` (OG0000094 rows); `analyses/chapter_1_genomics/03_cafe5/descriptive_analysis/top_families_annotated.md`.

### AUD-002 — The broad analysis is separate, not independent

- **Location:** Section 4.1, line 180: “The independent seven-taxon Base summary...”
- **Problem:** The seven-taxon analysis reuses the same `Vper` and `Vtub` proteomes, OrthoFinder workflow, family definitions, and CAFE5 framework. It provides a separate taxonomic context but is not an independent replication of the focal result.
- **Required action:** Replace “independent” with “separate” and avoid describing agreement between the two CAFE5 runs as independent corroboration. The comparison with OrthoFinder duplication calls may remain, provided the distinct estimands are stated.
- **Evidence:** A-001, A-006, A-011, A-015–A-017; the input labels in both OrthoFinder logs.

### AUD-003 — Broad-panel species identities remain unverified but are stated unqualified in prominent locations

- **Location:** Abstract, line 7 (“*Xerophyta viscosa*”); Sections 2.1 and 3.3, lines 33 and 147; Conclusions, line 224.
- **Problem:** The manuscript correctly discloses in Section 2.1 that no accession/release/checksum manifest validates the seven file labels, but the Abstract presents `Xvis` as verified *X. viscosa*. This exceeds the available provenance.
- **Required action:** Until the manifest is registered, describe broad-panel taxa consistently as file labels intended to represent the named species, including in the Abstract. Do not present the taxon-name mapping as independently verified.
- **Evidence:** A-011 and A-013–A-015; `chapter3/01_species_data/`; `chapter3/02_orthofinder/results/Results_Aug29/Log.txt`.

### AUD-004 — “Significant” means different things in Sections 3.2 and 3.4 but the Methods do not define the branch criterion

- **Location:** Sections 2.3–2.4, lines 45–51; Section 3.4, lines 151–170 and Table 5.
- **Problem:** The 412, 661, and 460 values are family-wide significance counts from `*_family_results.txt`. By contrast, the “significant expanded/contracted” columns in Table 5 were generated from branch probabilities (`p < 0.05`). The table is numerically correct, but the current Methods may lead readers to conflate family-wide and branch-specific significance.
- **Required action:** Define the branch-specific `p < 0.05` rule in Section 2.4 and state explicitly that Table 5 branch counts are not the 661 family-wide-significant Base families partitioned by branch. Add the threshold to the Table 5 header or caption.
- **Evidence:** A-016–A-017; `chapter3/results/Table_1_Pan_Velloziaceae_CAFE5_Summary.tsv`; `chapter3/scripts/analyze_cafe5_family_results.py`; Base `*_family_results.txt` and `Base_branch_probabilities.tab`.

## REQUIRED_CHANGES

1. **Remove or support two uncited methodological generalizations.** At line 196, “P450s, glycosyltransferases, LRR-containing proteins, and ubiquitination components are large and functionally diverse families” and their asserted special susceptibility to annotation fragmentation/allelic redundancy are not supported by an `L-*` source. At line 210, the general sensitivity of family-size methods to annotation error is scientifically plausible but lacks a validated methods source. Either cite locally validated primary/methodological evidence or recast these as limitations specific to the present unvalidated proteome inputs and annotations.

2. **Avoid adaptation-loaded shorthand.** At line 25, replace “candidate genomic investment” with “candidate gene-repertoire differences” or equivalent. Copy-number change does not establish selective investment (A-005–A-009, A-019).

3. **Complete software provenance without guessing versions.** OrthoFinder v3.1.5 and the use of DIAMOND, FAMSA, and FastTree are traceable to both logs. No CAFE5 version, DIAMOND/FAMSA/FastTree component versions, or CAFE5 error model is recorded in the inspected execution evidence. Section 2 should either recover those versions from a run-specific environment manifest or state that they were not recorded. Add software citations only after their bibliographic records/full texts are validated locally; do not invent them.

4. **Bring the reference list into the project's strict NBR 6023 profile.** All 12 journal-article entries omit the publication place normally required in the complete NBR 6023 periodical-article pattern. If the thesis treats the sources as online articles, it should also apply one consistent institutional rule for DOI/`Disponível em:`/access date. Validate these fields locally before adding them. The existing author order, years, titles, journal names, volumes, issues, pages/article numbers, and DOIs agree with L-001–L-012.

5. **Preserve the current scope boundary.** The final OSCA sentence is acceptable as a Chapter 2 transition. Do not add OSCA mechanisms or results to Chapter 1, and do not restore unsupported synteny, Ka/Ks, dating, ancestral-state, secondary-loss, or focal physiological claims.

## Sequential citation verification

Each co-citation was split and assessed against its own source. “Supported” below means that the cited local full text supports the bounded claim at the stated taxonomic and conceptual level.

| ID | Manuscript location | Citation | Verdict | Local evidence and reasoning |
|---|---|---|---|---|
| CIT-001 | Introduction, line 13, first claim | SILVEIRA et al., 2016 | Supported | `Silveira_2015.md`, lines 27–75 and pp. 129–132: explicitly reports an old OCBIL, >5,000 species, nearly 15%, and 0.78%. |
| CIT-002 | Introduction, line 13, root claim | TEODORO et al., 2019 | Supported | `Teodoro_2019.md`, lines 17–67 and 500–590: two *Barbacenia* species penetrated/weathered quartzite and released carboxylates that mobilized P; the manuscript preserves the focal-species boundary. |
| CIT-003 | Introduction, line 15, family comparison | ALCANTARA et al., 2015 | Supported | `Alcantara_2015.md`, lines 30–53 and 316–690: sampled DT plants reduced metabolism and were generally rock-associated; non-DT plants maintained carbon gain and were mainly on deeper sandy soils. |
| CIT-004 | Introduction, line 15, experiment | TEODORO et al., 2021 | Supported | `Teodoro_2021...md`, lines 48–110 and 430–604: *V. nivea* had lower mild-drought productivity and recovered after severe drought; *V. intermedia* did not survive severe desiccation. |
| CIT-005 | Introduction, line 15, ecological heterogeneity | BONDI et al., 2023 | Supported | `Bondi_2023...md`, lines 26–150: 27 DT versus 27 related sensitive taxa did not converge on one specialization or resource-use strategy. |
| CIT-006 | Introduction, line 17 | VOLAIRE et al., 2026 | Supported | `Volaire_2026.md`, lines 23–123: distinguishes Phase II drought resistance/growth maintenance from Phase III survival after growth cessation. |
| CIT-007 | Introduction, line 19, *Xerophyta* | COSTA et al., 2017 | Supported | `Costa_2017...md`, lines 20–30 and 175–213: seed-associated transcripts and ABI3/ABI5 involvement; no extensive genome-wide family turnover, with some stress-family expansions. |
| CIT-008 | Introduction, line 19, *Oropetium* | VANBUREN et al., 2015 | Supported | `VanBuren_2015...md`, lines 20–43 and surrounding Results: compact 245-Mb, highly contiguous genome. |
| CIT-009 | Introduction, line 19, *Selaginella* | VANBUREN et al., 2018 | Supported | `VanBuren_2018.md`, lines 17–145 and Comparative Genomics: extensive haplotype structural variation, no lineage-wide WGD evidence, and tandem-duplication patterns. |
| CIT-010 | Introduction, line 19, grass convergence | MARKS et al., 2024 | Supported | `Marks_2024...md`, lines 23–57 and Discussion: repeated origins with shared syntenic genes, convergent duplication/expression, pathway convergence, and species-specific modules. |
| CIT-011 | Introduction, line 21 | ALCANTARA; REE; MELLO-SILVA, 2018 | Supported | `Alcantara_2018.md`, lines 100–167 and 858–873: *Acanthochlamys* sister placement, strategy diversity, crown near 75 Ma, breakup before 110 Ma, and explicit rejection of Gondwanan vicariance. |
| CIT-012 | Results, line 147 | ALCANTARA; REE; MELLO-SILVA, 2018 | Supported | Same full text: the published family tree supports *A. bracteata* as sister to the remaining Velloziaceae; “broadly compatible” is appropriately cautious. |
| CIT-013 | Discussion, line 190, ontogenetic photosynthesis | OUNG et al., 2022 | Supported | `Oung_2021...md`, lines 39–170 and 511–620: younger plants emphasize qE/D1 repair; older plants show greater D1 and cytochrome-b6f degradation. |
| CIT-014 | Discussion, line 190, *Xerophyta* | COSTA et al., 2017 | Supported | Same full text as CIT-007; the manuscript does not transfer the mechanism to focal *Vellozia*. |
| CIT-015 | Discussion, line 194, seasonal carbon gain | ALCANTARA et al., 2015 | Supported | Same full text as CIT-003; the wording remains at the sampled-family level. |
| CIT-016 | Discussion, line 194, focal analogue | TEODORO et al., 2021 | Supported | Same full text as CIT-004; stomatal control, osmotic adjustment, and turgor maintenance apply to *V. intermedia*, and the manuscript explicitly prevents transfer to *V. peripherica*. |
| CIT-017 | Discussion, line 202, chronology | ALCANTARA; REE; MELLO-SILVA, 2018 | Supported | Same full text as CIT-011; the stated ages and anti-vicariance conclusion are accurate. |
| CIT-018 | Discussion, line 204, repeated grass evolution | MARKS et al., 2024 | Supported | Same full text as CIT-010; the mixed parallel/convergent/lineage-specific account is accurate. |
| CIT-019 | Discussion, line 204, ecological heterogeneity | BONDI et al., 2023 | Supported | Same full text as CIT-005; “functionally heterogeneous” accurately summarizes the results. |
| CIT-020 | Discussion, line 204, South American strategies | ALCANTARA; REE; MELLO-SILVA, 2018 | Supported | Same full text as CIT-011; it documents DT and highly drought-resistant non-DT strategies in South American lineages. |

## Numerical and model-label audit

- **Tables 1 and 4:** every input, assigned, unassigned, percentage, and species-specific value matches the corresponding `Statistics_Overall.tsv` and `Statistics_PerSpecies.tsv` files (A-002–A-003; A-012–A-013).
- **Table 2:** all root/tip counts and changes match `Base_count.tab` and `Base_change.tab`; all 16 listed families are flagged `y` with a family p-value printed as `0` in `Base_family_results.txt`. The manuscript correctly avoids interpreting printed zero as mathematical zero. Only the OG0000094 annotation wording fails, as specified in AUD-001.
- **Table 3:** all target/background hits, folds, p-values, and q-values match `functional_enrichment_results.tsv`; the 14,210-background, 819-*Vtub*, and 1,347-*Vper* universes are correct (A-009).
- **Table 5:** every Base-derived branch count, significant branch count, and net gain matches `Table_1_Pan_Velloziaceae_CAFE5_Summary.tsv` (A-017). Base/Gamma labels are not mixed in the manuscript.
- **Nodes:** node 13 = (`Vper`, `Vtub`); node 12 = (`Xvis`, node 13); nodes 11, 10, 9, and root 8 are correctly described (A-018; `Base_report.cafe`).
- **Tool records:** OrthoFinder v3.1.5, DIAMOND, FAMSA, and FastTree are verified in both logs. CAFE5's version is not present in the inspected run records and must not be inferred from the current environment.

## OPTIONAL_SUGGESTIONS

- Replace repeated prose reproductions of full tables with shorter synthesis where chapter length is a concern; the repetition is not currently contradictory.
- In Table 5, italicize mapped taxon names only after provenance validation; retaining file labels meanwhile makes the evidentiary status visible.
- Consider adding stable table/paragraph anchors in the next snapshot so claim-level ledgers remain stable when line numbers change.

## Approval conditions for the next round

Approval requires correction of AUD-001–AUD-004, resolution or explicit limitation of software/taxon provenance, and a consistently complete ABNT NBR 6023 reference profile. No new numerical analysis is required for these corrections.
