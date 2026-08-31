# Round 1 Literature Evidence Report

**Target manuscript:** unified Chapter 1, integrating `teamwork/chapter_1_comparative_genomics_abnt.md` and `teamwork/chapter_macroevolution_velloziaceae_abnt.md`  
**Corpus inspected:** `docs/papers/`, with full-text use restricted to already converted sources under `teamwork/papers_local_md/`; the pre-existing OA cache under `teamwork/papers_openalex_md/` was inspected only to determine whether two cited mechanistic claims had local full-text support.  
**External retrieval:** none. OpenAlex and web search were not used because no literature gap had yet been declared by the PhD Advisor.  
**Conversion status:** no additional PDF conversion was required for the decision-critical sources.  
**Citation system:** ABNT author-date.  
**Scope rule:** OSCA is not developed here; it may appear only as a brief transition to the targeted Chapter 2 analysis.

## 1. Evidence-gate decision

The local corpus supports a strong Chapter 1 introduction on the age, edaphic severity, floristic richness, and heterogeneous drought strategies of the *campos rupestres*. It also supports cautious discussion of (i) a productivity–survival trade-off in tested Velloziaceae species, (ii) seed-program recruitment in *Xerophyta viscosa*, and (iii) recurrent, partly convergent molecular evolution of desiccation tolerance in grasses. It does **not** provide direct physiological evidence for the focal pair *Vellozia tubiflora*–*V. peripherica*.

One claim in the macroevolutionary source draft fails the evidence gate and is contradicted by a locally available dated phylogeny: a node dated to approximately 75 Ma cannot be described as preceding the South America–Africa breakup, which Alcantara, Ree and Mello-Silva (2018) place before 110 Ma. Their analysis explicitly concludes that available molecular-clock studies contradict a Gondwanan vicariance origin for Velloziaceae. Consequently, gene-family expansions at the draft's “Node 13” cannot by themselves prove that vegetative desiccation tolerance is a homologous ancestral synapomorphy, nor that the evergreen state of *V. peripherica* is a secondary loss.

The Writer should retain the local comparative-genomic results only when supported by the Analysis Inspector's `A-*` records. The literature records below supply biological context and interpretation, not validation of the chapter's numerical genomic outputs.

## 2. Validated literature evidence ledger

### L-001 — Campo rupestre as an old, species-rich OCBIL

- **Source:** SILVEIRA, Fernando A. O. et al. Ecology and evolution of plant diversity in the endangered campo rupestre: a neglected conservation priority. *Plant and Soil*, v. 403, p. 129–152, 2016. DOI: 10.1007/s11104-015-2637-8.
- **Local file:** `teamwork/papers_local_md/Silveira_2015.md`.
- **Locator:** journal pp. 129–130; Abstract/Scope; local lines 27–75.
- **Support level:** `DIRECT`.
- **Supported statement:** Campo rupestre is an extremely old montane ecosystem that meets the criteria of a classic old, climatically buffered, infertile landscape; it contains more than 5,000 plant species, nearly 15% of Brazil's plant diversity, in approximately 0.78% of the country's area.
- **Permitted use:** ecological and evolutionary setting of Chapter 1.
- **Boundary:** the bibliographic year in the final journal issue is 2016, although the article was published online in 2015. Use `(SILVEIRA et al., 2016)` for consistency with the issue metadata.

### L-002 — Heterogeneous drought strategies and productivity–desiccation trade-off in Velloziaceae

- **Source:** ALCANTARA, Suzana et al. Carbon assimilation and habitat segregation in resurrection plants: a comparison between desiccation- and non-desiccation-tolerant species of Neotropical Velloziaceae (Pandanales). *Functional Ecology*, v. 29, n. 12, p. 1499–1512, 2015. DOI: 10.1111/1365-2435.12462.
- **Local file:** `teamwork/papers_local_md/Alcantara_2015.md`.
- **Locator:** journal p. 1499, Summary; local lines 30–53; journal pp. 1504–1506, Results; local lines 316–444; journal pp. 1506–1510, Discussion; local lines 450–690.
- **Support level:** `DIRECT` for the 20 studied species; `INTERPRETIVE` if generalized to the family.
- **Supported statement:** Across the sampled species, DT plants sharply reduced metabolism during the dry season, while non-DT plants maintained positive carbon gain; DT plants were generally smaller and associated mainly with exposed rock, whereas non-DT plants occurred mainly on deeper sandy soils. The study supports a productivity–desiccation-tolerance trade-off.
- **Taxonomic boundary:** neither *V. tubiflora* nor *V. peripherica* was among the 20 species listed in the Results. This source cannot establish the physiological status, habitat, stomatal behavior, root depth, or carbon assimilation of either focal species.
- **Required wording:** “Across sampled Neotropical Velloziaceae...” rather than “*V. tubiflora* does...” or “*V. peripherica* does...”.

### L-003 — Experimental productivity–survival trade-off in two congeneric Vellozia species

- **Source:** TEODORO, Grazielle Sales et al. Desiccation tolerance implies costs to productivity but allows survival under extreme drought conditions in Velloziaceae species in campos rupestres. *Environmental and Experimental Botany*, v. 189, art. 104556, 2021. DOI: 10.1016/j.envexpbot.2021.104556.
- **Local file:** `teamwork/papers_local_md/Teodoro_2021 - Desiccation tolerance implies costs to productivity but allo.md`.
- **Locator:** article pp. 1–2, Abstract/Introduction; local lines 48–110; pp. 7–10, Results/Discussion; local lines 430–604.
- **Support level:** `DIRECT` for *V. nivea* and *V. intermedia*; `SYNTHESIS` for a family-level trade-off.
- **Supported statement:** The DT species *V. nivea* had lower productivity under mild drought but survived and rehydrated after extreme drought; the non-DT *V. intermedia* maintained higher productivity under mild drought but died after severe desiccation. The non-DT strategy involved stomatal control, osmotic adjustment, and turgor maintenance.
- **Taxonomic boundary:** this is not evidence about *V. tubiflora* or *V. peripherica*. It can motivate hypotheses about the focal pair but cannot be used to assign their exact mechanisms.

### L-004 — Vellozioid roots and phosphorus acquisition from quartzite

- **Source:** TEODORO, Grazielle Sales et al. Specialized roots of Velloziaceae weather quartzite rock while mobilizing phosphorus using carboxylates. *Functional Ecology*, v. 33, n. 5, p. 762–773, 2019. DOI: 10.1111/1365-2435.13324.
- **Local file:** `teamwork/papers_local_md/Teodoro_2019.md`.
- **Locator:** journal p. 762, Abstract; local lines 17–67; journal pp. 770–771, Discussion/Summary; local lines 500–590.
- **Support level:** `DIRECT` for the two studied *Barbacenia* species; `INTERPRETIVE` for Velloziaceae generally.
- **Supported statement:** The investigated roots penetrated and weathered quartzite and released mainly malate and citrate, increasing phosphorus solubilization; the authors coined these specializations “vellozioid roots.”
- **Taxonomic boundary:** the experiment used *Barbacenia tomentosa* and *B. macrantha*. Do not state that *V. tubiflora* or *V. peripherica* possesses the same root physiology without species-specific evidence.
- **Required wording:** “Vellozioid roots documented in rock-dwelling Velloziaceae...” rather than an unqualified genus-wide attribution.

### L-005 — Dated Velloziaceae diversification, water-strategy evolution, and rejection of Gondwanan vicariance

- **Source:** ALCANTARA, Suzana; REE, Richard H.; MELLO-SILVA, Renato. Accelerated diversification and functional trait evolution in Velloziaceae reveal new insights into the origins of the campos rupestres' exceptional floristic richness. *Annals of Botany*, v. 122, n. 1, p. 165–180, 2018. DOI: 10.1093/aob/mcy063.
- **Local file:** `teamwork/papers_local_md/Alcantara_2018.md`.
- **Locator:** journal p. 165, Abstract; local lines 32–50; pp. 166–167, Introduction; local lines 100–144; p. 177, Discussion; local lines 858–873.
- **Support level:** `DIRECT`.
- **Supported statements:** *Acanthochlamys bracteata* is consistently recovered as sister to the remainder of Velloziaceae; African Velloziaceae are described as DT, whereas South American lineages include both DT and highly drought-resistant non-DT strategies; independent diversification-rate shifts occurred in *Vellozia* and *Barbacenia*.
- **Critical contradiction:** the South America–Africa separation predates 110 Ma, while the inferred Velloziaceae crown is approximately 75 Ma and African/South American stem ages are approximately 55–40 Ma. The paper explicitly says these dates contradict a Gondwanan origin.
- **Prohibited claims:** “the 75-Ma common ancestor immediately preceded Gondwanan breakup,” “Node 13 proves a Pan-Gondwanan origin,” and “gene-family expansion alone proves DT was the ancestral Velloziaceae state.”
- **Permitted alternative:** “The seven-species CAFE analysis identifies an ancestral expansion pulse, but ancestral-state reconstruction and defensible divergence-time calibration are required before linking this pulse to the origin of desiccation tolerance.”

### L-006 — Cytogenetic support for the Vellozia basic chromosome number

- **Source:** BRAZ, Guilherme T. et al. Revisiting the cytogenetics of *Vellozia* Vand.: immunolocalization of KNL1 elucidates the chromosome number for the genus. *Brazilian Journal of Botany*, v. 48, art. 6, 2025. DOI: 10.1007/s40415-024-01064-1.
- **Local file:** `teamwork/papers_local_md/Braz_2025.md`.
- **Locator:** article p. 1, Abstract; local lines 16–29; article p. 6, Discussion/Conclusion; local lines 410–434.
- **Support level:** `DIRECT` for the six studied species; `INTERPRETIVE` for the full genus.
- **Supported statement:** All six sampled, phylogenetically dispersed *Vellozia* species had 2n = 18; KNL1 immunolocalization identified the smaller pair as true chromosomes, leading the authors to propose x = 9 as the likely basic number for the genus.
- **Taxonomic boundary:** the focal species were not among the six sampled taxa. The paper supports compatibility of nine pseudomolecules with the proposed genus-wide karyotype, not independent cytogenetic validation of each focal assembly.
- **Required wording:** “consistent with the proposed genus-wide basic number x = 9” rather than “definitively validated in both focal species.”

### L-007 — Seed-program recruitment in Xerophyta viscosa

- **Source:** COSTA, Maria-Cecília D. et al. A footprint of desiccation tolerance in the genome of the resurrection plant *Xerophyta viscosa*. *Nature Plants*, v. 3, art. 17038, 2017. DOI: 10.1038/nplants.2017.38.
- **Local file:** `teamwork/papers_local_md/Costa_2017 - A footprint of desiccation tolerance in the genome of Xerophyta viscosa.md`.
- **Locator:** article p. 1, Abstract; local lines 20–30; p. 3, Orthologous clustering/Resurrection physiology; local lines 175–213.
- **Support level:** `DIRECT` for *X. viscosa*; `INTERPRETIVE` for Velloziaceae generally.
- **Supported statement:** Dehydration induces seed-desiccation-associated transcripts and involves ABI3/ABI5 orthologues, supporting redirection of seed desiccation programs into vegetative tissues. The study also reports that *X. viscosa* did not undergo extensive genome-wide gene-family expansion or contraction, although some stress-associated families expanded.
- **Boundary:** the paper does not show that a particular ancestral Velloziaceae node acquired DT, nor that the focal *Vellozia* species use the same gene copies.

### L-008 — Recurrent and partly convergent evolution of desiccation tolerance in grasses

- **Source:** MARKS, Rose A. et al. Convergent evolution of desiccation tolerance in grasses. *Nature Plants*, v. 10, n. 7, p. 1112–1125, 2024. DOI: 10.1038/s41477-024-01729-5.
- **Local file:** `teamwork/papers_local_md/Marks_2024 - Convergent evolution of desiccation tolerance in grasses.md`.
- **Locator:** journal p. 1112, Abstract/Introduction; local lines 23–57; Results and Discussion throughout pp. 1113–1123.
- **Support level:** `DIRECT` for the studied grasses; `SYNTHESIS` for evolutionary framing.
- **Supported statement:** Desiccation tolerance evolved repeatedly in grasses; shared syntenic genes, convergent duplication/expression patterns, different genes feeding similar metabolic pathways, and lineage-specific mechanisms all contribute.
- **Boundary:** this work supports a mixed model of parallelism, convergence, and lineage specificity. It does not support a single universal genomic architecture, and it cannot resolve ancestral-state polarity in Velloziaceae.

### L-009 — Desiccation-tolerant plants are ecologically heterogeneous

- **Source:** BONDI, Luiz; DE PAULA, Luiza F. A.; ROSADO, Bruno H. P.; POREMBSKI, Stefan. Demystifying the convergent ecological specialization of desiccation-tolerant vascular plants for water deficit. *Annals of Botany*, v. 131, n. 3, p. 521–531, 2023. DOI: 10.1093/aob/mcad005.
- **Local file:** `teamwork/papers_local_md/Bondi_2023 - Demystifying the convergent ecological specialization of des.md`.
- **Locator:** journal p. 521, Abstract; local lines 26–45; pp. 521–523, Introduction; local lines 52–150.
- **Support level:** `DIRECT`.
- **Supported statement:** A comparison of 27 DT and 27 phylogenetically related desiccation-sensitive plants did not support the assumption that all DT plants converge on the same water-deficit specialization or uniformly conservative resource-use strategy. DT plants are ecologically heterogeneous.
- **Use in Chapter 1:** this source requires caution against presenting all resurrection plants, or *V. tubiflora* by analogy, as occupying one invariant functional endpoint.
- **Metadata correction:** the two drafts attribute this paper to “Bondi, Marks and VanBuren”; that authorship is incorrect. The local article lists Bondi, de Paula, Rosado and Porembski.

### L-010 — Time- and trait-based distinction between drought resistance and drought survival

- **Source:** VOLAIRE, Florence et al. From growth potential to drought survival: a trait- and time-based framework for plant water economics across vascular species. *New Phytologist*, v. 250, p. 21–40, 2026. DOI: 10.1111/nph.70922.
- **Local file:** `teamwork/papers_local_md/Volaire_2026.md`.
- **Locator:** journal p. 21, Summary; local lines 23–69; p. 22, Figure 1 caption and framework definition; local lines 104–123.
- **Support level:** `DIRECT` as a conceptual framework.
- **Supported statement:** Phase II drought resistance comprises growth/turgor maintenance under declining water availability, primarily via dehydration avoidance; Phase III drought survival begins after persistent growth cessation and includes dehydration/desiccation tolerance, water storage, and other survival strategies.
- **Metadata correction:** the comparative-genomics draft gives v. 249, n. 3, p. 1120–1135 and DOI 10.1111/nph.20450. The local published article is v. 250, p. 21–40, DOI 10.1111/nph.70922.

### L-011 — Photosynthetic protection and degradation during desiccation

- **Source:** OUNG, Hui Min Olivia et al. Differential response of the photosynthetic machinery to dehydration in older and younger resurrection plants. *Journal of Experimental Botany*, v. 73, n. 5, p. 1566–1580, 2022. DOI: 10.1093/jxb/erab485.
- **Local file:** `teamwork/papers_local_md/Oung_2021 - Differential response of the photosynthetic machinery to deh.md`.
- **Locator:** journal p. 1566, Abstract; local lines 39–50; pp. 1566–1568, Introduction; local lines 58–170; pp. 1575–1577, Results/Discussion; local lines 511–620.
- **Support level:** `DIRECT` for *Craterostigma pumilum*; `INTERPRETIVE` for resurrection plants generally.
- **Supported statement:** Younger plants favored photoprotective high-energy quenching and D1 repair, whereas older plants relied more on degradation of D1 and cytochrome b6f subunits; both strategies prepared tissues for desiccation, and younger plants recovered faster.
- **Boundaries:** this paper is on a homoiochlorophyllous eudicot, not Velloziaceae. It does not establish a 48–72 h recovery interval for *V. tubiflora*, nor does it validate a “kinetic rehydration bottleneck” caused by chloroplast-translocon copy number.
- **Metadata correction:** cite the journal year as 2022; 2021 is the advance-online year.

### L-012 — Genomic diversity among resurrection-plant models

- **Sources:**
  - VANBUREN, Robert et al. Single-molecule sequencing of the desiccation-tolerant grass *Oropetium thomaeum*. *Nature*, v. 527, p. 508–511, 2015. DOI: 10.1038/nature15714.
  - VANBUREN, Robert et al. Extreme haplotype variation in the desiccation-tolerant clubmoss *Selaginella lepidophylla*. *Nature Communications*, v. 9, art. 13, 2018. DOI: 10.1038/s41467-017-02546-5.
- **Local files:** `teamwork/papers_local_md/VanBuren_2015 - Single-molecule sequencing of the desiccation-tolerant grass Oropetium thomaeum.md`; `teamwork/papers_local_md/VanBuren_2018.md`.
- **Locator:** *Oropetium*, journal p. 508, opening summary; local lines 20–43. *Selaginella*, article p. 1, Abstract; local lines 17–33.
- **Support level:** `DIRECT` for the respective taxa; `SYNTHESIS` for diversity of genomic routes.
- **Supported statement:** *Oropetium* has a compact, highly contiguous grass genome and survives loss of more than 95% of cellular water; *Selaginella* lacks evidence of a lineage-wide WGD and instead shows extensive haplotype variation and tandem-duplication patterns associated with extreme drying.
- **Boundary:** these studies demonstrate that genome compactness, repeat dynamics, tandem duplication, and stress-gene retention differ among lineages. They do not show that expanded transposases universally provide stress-responsive promoters, and they do not date the focal *Vellozia* Chr1A–Chr5A duplication.

## 3. Draft-claim audit: findings that require revision

| Draft claim or citation | Verdict | Required action |
|---|---|---|
| The common ancestor at “Node 13” existed immediately before Gondwanan breakup at ~75 Ma. | `CONTRADICTED` by L-005 | Remove the Gondwanan-vicariance framing. South America–Africa separation predates 110 Ma; a ~75 Ma crown is too young. |
| The Node 13 expansions prove DT is a homologous ancestral synapomorphy rather than convergence. | `UNSUPPORTED` | Recast as an untested ancestral-state hypothesis. Gene-family counts do not reconstruct a phenotype; trait mapping and functional annotation are required. |
| The evergreen state of *V. peripherica* is a demonstrated secondary loss/suppression of ancestral anhydrobiosis. | `UNSUPPORTED` | Present only as a hypothesis, if retained. No focal-species ancestral-state analysis or direct physiological source was found. |
| *V. peripherica* co-occurs with *V. tubiflora* in the same microhabitat and maintains hydration through deep roots, tight stomatal control, and osmotic adjustment. | `MISSING FOCAL-SPECIES SOURCE` | Remove species-specific mechanisms or label them as hypotheses derived from other non-DT *Vellozia* species (L-003). |
| *V. tubiflora* is an obligate, poikilochlorophyllous resurrection plant losing >90–95% of its water and occupying exposed pavements. | `MISSING FOCAL-SPECIES SOURCE` | Do not retain as a factual focal-species statement until a local source directly documenting the taxon is supplied. |
| Alcantara et al. (2015) directly supports physiological contrast of the focal pair. | `SOURCE-MISMATCH` | The study sampled 20 other Velloziaceae species (L-002); cite only for family-level patterns. |
| Teodoro et al. (2021) directly supports the focal pair's strategies. | `SOURCE-MISMATCH` | The experiment compared *V. nivea* and *V. intermedia* (L-003). |
| Vellozioid roots and massive citrate/malate exudation are established in both focal species. | `OVERGENERALIZED` | The direct evidence is from two *Barbacenia* species (L-004). |
| Braz et al. (2025) cytogenetically confirms nine chromosomes in each focal species. | `OVERSTATED` | The six sampled taxa did not include the focal species. Say the assemblies are consistent with the proposed x = 9 genus-level standard (L-006). |
| A Chr1A–Chr5A block confirms a WGD. | `UNSUPPORTED BY LITERATURE` | A single self-syntenic block may represent WGD or segmental duplication. Require Analysis Inspector evidence plus Ks/syntenic-depth analysis before asserting WGD or timing it. |
| Expanded TOC/TIC copy number removes a rehydration kinetic bottleneck and permits high-throughput protein import within hours. | `MECHANISTIC OVERREACH` | Present enrichment/copy number as an observation. The causal physiological interpretation is a hypothesis; no focal expression, localization, import-rate, or rehydration-time evidence was found. |
| NDH, PSII, ACC, organonitrogen, LRR-RLK, NLR, U-box, P450, UGT, and PPR expansions are demonstrated adaptive mechanisms in the focal species. | `ANNOTATION-TO-FUNCTION OVERREACH` | Report annotations/enrichment as candidate functions. Avoid “drives,” “endows,” “requires,” “ensures,” or “underpins” without functional evidence. |
| Elevated category-level Ka/Ks (all ω < 1) demonstrates positive diversifying selection. | `CONCEPTUALLY UNSUPPORTED` | Values below 1 show purifying selection at the pairwise-gene level; relative elevation may indicate weaker constraint, but not positive selection without branch/site tests. |
| Dormancy allows neutral sequence drift to accumulate in *V. tubiflora*. | `UNSUPPORTED` | Remove. No analysis or local source links seasonal anhydrobiosis to increased neutral coding-sequence drift in the focal lineage. |
| Hydrated evergreen foliage necessarily explains expanded pathogen receptors in *V. peripherica*. | `UNSUPPORTED ADAPTIVE STORY` | Reframe as one possible interpretation and acknowledge alternative explanations (demography, tandem duplication, assembly/annotation differences). |
| OSCA is introduced as the necessary next mechanistic target. | `OUT OF CHAPTER 1 SCOPE` | Limit to one transition sentence identifying Chapter 2; do not discuss OSCA structure, expression, or function in Chapter 1. |

## 4. Bibliographic and ABNT corrections

1. **Alcantara et al. (2015):** the macroevolution draft's reference title “Transcriptomic response to dehydration in *Vellozia* species” is incorrect. Use the title and metadata in L-002.
2. **Bondi et al. (2023):** authors are Bondi, de Paula, Rosado and Porembski, not Bondi, Marks and VanBuren. Use L-009. In parenthetical ABNT form, use `(BONDI et al., 2023)`.
3. **Silveira et al.:** use journal-year 2016, v. 403, p. 129–152, with DOI 10.1007/s11104-015-2637-8. The DOI contains 2015 because of online-first publication; this does not change the issue year.
4. **Volaire et al. (2026):** replace the draft's volume, pages, and DOI with v. 250, p. 21–40, DOI 10.1111/nph.70922 (L-010).
5. **Oung et al.:** use 2022 in text and references, v. 73, n. 5, p. 1566–1580, DOI 10.1093/jxb/erab485 (L-011).
6. **Braz et al. (2025):** treat “6” as an article number, not an ordinary page range: v. 48, art. 6.
7. Use uppercase surnames in parenthetical citations and semicolons between works: `(ALCANTARA et al., 2015; TEODORO et al., 2021)`.
8. Include in the final reference list only works actually cited in the unified chapter. Several entries in the comparative-genomics draft are not cited in its running text.
9. Do not use `et al.` immediately after a semicolon-delimited first author in the reference list as a substitute for locally validated authorship when the complete author list is available in the source.

## 5. Cited sources not validated from a local full text in this pass

The following works are cited in one or both source drafts but no matching primary full text was found among the prioritized local Markdown corpus. Their metadata may appear in the draft, but neither their claims nor their reference fields are evidence-validated here:

- Farrant et al. (2007), desiccation-tolerance review;
- Mello-Silva et al. (2011), purported Velloziaceae biogeography/vicariance source;
- Emms and Kelly (2019), OrthoFinder;
- Wang et al. (2012), MCScanX;
- Mendes et al. (2020), CAFE5;
- Yang (2007), PAML 4;
- Hopper (2009), OCBIL theory;
- James (1992), “karyotypic orthoselection” analogy;
- Paterson et al. (2004), cereal paleogenomics;
- Ming et al. (2015), pineapple genome;
- Zhang et al. (2017), *Apostasia* genome;
- Watson, Sowden and Jarvis (2018); Ling et al. (2021); Gao et al. (2022); Chen et al. (2023); Liu et al. (2023); Nellaepalli, Lau and Jarvis (2023); Sun and Jarvis (2023); Xing et al. (2025), chloroplast proteostasis/import claims;
- Vaher et al. (2024), cell-wall integrity signaling.

Two previously downloaded OA Markdown files, `teamwork/papers_openalex_md/Colin_2023.md` and `teamwork/papers_openalex_md/Verslues_2023.md`, contain general discussions of cell-wall and abiotic-stress signaling. They do not establish that the focal LRR-RLK expansions sense turgor or that their expansion is adaptive in *V. peripherica*. They were therefore not promoted to `L-*` evidence.

## 6. Writer-ready synthesis constraints

- Open with the well-supported OCBIL and floristic-diversity context (L-001), then introduce Velloziaceae as a lineage containing heterogeneous water-use strategies (L-002, L-003, L-005, L-009).
- State explicitly that the focal ecological assignments are working classifications unless focal-species physiological evidence is supplied.
- Use the seven-species phylogenomic/CAFE analysis to broaden the pairwise comparison, but separate observed topology and family-size change from phenotype-state inference.
- Replace “proves,” “confirms the origin,” “definitively,” “endows,” and “requires” with calibrated formulations such as “is consistent with,” “suggests,” “identifies a candidate association,” or “motivates testing.”
- Explain that gene-family enrichment supplies hypotheses about functional investment. It does not establish expression, biochemical activity, ecological benefit, or causation.
- Discuss pairwise Ka/Ks < 1 as purifying selection. Relative differences among functional categories can be described as differing constraint only if the Analysis Inspector confirms that those category values were genuinely computed from gene-level results.
- Treat sequencing, assembly, structural annotation, and their detailed quality-control workflows as Appendix material. In Chapter 1, retain only the minimum dataset provenance necessary to interpret comparative results.
- End with a concise transition to Chapter 2. Mention OSCA only as a future targeted family analysis; do not import Chapter 2 results or mechanisms.

## 7. Source files used as evidence

1. `teamwork/papers_local_md/Silveira_2015.md`
2. `teamwork/papers_local_md/Alcantara_2015.md`
3. `teamwork/papers_local_md/Teodoro_2021 - Desiccation tolerance implies costs to productivity but allo.md`
4. `teamwork/papers_local_md/Teodoro_2019.md`
5. `teamwork/papers_local_md/Alcantara_2018.md`
6. `teamwork/papers_local_md/Braz_2025.md`
7. `teamwork/papers_local_md/Costa_2017 - A footprint of desiccation tolerance in the genome of Xerophyta viscosa.md`
8. `teamwork/papers_local_md/Marks_2024 - Convergent evolution of desiccation tolerance in grasses.md`
9. `teamwork/papers_local_md/Bondi_2023 - Demystifying the convergent ecological specialization of des.md`
10. `teamwork/papers_local_md/Volaire_2026.md`
11. `teamwork/papers_local_md/Oung_2021 - Differential response of the photosynthetic machinery to deh.md`
12. `teamwork/papers_local_md/VanBuren_2015 - Single-molecule sequencing of the desiccation-tolerant grass Oropetium thomaeum.md`
13. `teamwork/papers_local_md/VanBuren_2018.md`

`EVIDENCE_STATUS: COMPLETE_FOR_INITIAL_LOCAL_PASS`

