#!/usr/bin/env python3
"""
Remove all internal (Section X.X) cross-references from Results, Discussion,
and Figure Legends, replacing them with direct Figure/Table references or clean prose.
"""

TARGET_FILES = [
    "chapter_macroevolution_review/docs/manuscripts/chapter_macroevolution_article.md",
    "docs/macroevolution/manuscripts/chapter_macroevolution_article.md",
]

replacements = [
    # L126 (Results 3.2)
    (
        "The family-level annotation record for the 132 ancestral expansions on the core Velloziaceae stem branch included annotations associated with stress protection and transcriptional regulation (Figure 2B; see Section 3.6). The small heat-shock protein HSP20 family (`OG0000340`) showed an inferred net gain of five copies ($p < 0.0001$). Expanded regulatory families included B3-domain proteins (`OG0000136`, net gain of five copies), basic leucine zipper (bZIP) transcription factors (`OG0000858`, gain of four copies), and MYB transcription factors (`OG0000750`, gain of four copies). Additional expansions encompassed anthocyanin 5-aromatic acyltransferase (`OG0000038`, gain of five copies) and germin-like proteins (`OG0000035`, gain of 12 copies), alongside families annotated with chloroplast NAD(P)H-quinone oxidoreductase homology (`OG0000014`, gain of 17 copies; `OG0000036`, gain of five copies; detailed in Section 3.6).",
        "The family-level annotation record for the 132 ancestral expansions on the core Velloziaceae stem branch included annotations associated with stress protection and transcriptional regulation (Figure 2B). The small heat-shock protein HSP20 family (`OG0000340`) showed an inferred net gain of five copies ($p < 0.0001$). Expanded regulatory families included B3-domain proteins (`OG0000136`, net gain of five copies), basic leucine zipper (bZIP) transcription factors (`OG0000858`, gain of four copies), and MYB transcription factors (`OG0000750`, gain of four copies). Additional expansions encompassed anthocyanin 5-aromatic acyltransferase (`OG0000038`, gain of five copies) and germin-like proteins (`OG0000035`, gain of 12 copies), alongside families annotated with chloroplast NAD(P)H-quinone oxidoreductase homology (`OG0000014`, gain of 17 copies; `OG0000036`, gain of five copies)."
    ),
    # L194 (Discussion 4.1)
    (
        "subject to gene-identity validation (Section 3.2; Supplementary Table S7).",
        "subject to gene-identity validation (Figure 5; Supplementary Table S7)."
    ),
    # L196 (Discussion 4.1)
    (
        "whereas the highlighted bZIP and MYB families differ in count (Section 3.6).",
        "whereas the highlighted bZIP and MYB families differ in count (Figure 5B; Supplementary Table S7)."
    ),
    (
        "rather than to a single point within that interval (Section 2.4).",
        "rather than to a single point within that interval (Figure 2A; Supplementary Table S3)."
    ),
    # L204 (Discussion 4.2)
    (
        "Subtilase, MATE and Argonaute annotations identify specific candidates among the families expanded in *V. peripherica* (Section 3.6).",
        "Subtilase, MATE and Argonaute annotations identify specific candidates among the families expanded in *V. peripherica* (Figure 5A; Supplementary Table S7)."
    ),
    # L210 (Discussion 4.2)
    (
        "passed the specified local/global false-discovery, permutation and balance criteria (Figure 4; Section 3.5).",
        "passed the specified local/global false-discovery, permutation and balance criteria (Figure 4; Supplementary Table S6)."
    ),
    # L218 (Discussion 4.3)
    (
        "NPF-associated `OG0000581` provides a more specific starting point: 11 copies in *V. tubiflora* versus five in *V. peripherica*, with a modeled gain of five (Section 3.6).",
        "NPF-associated `OG0000581` provides a more specific starting point: 11 copies in *V. tubiflora* versus five in *V. peripherica*, with a modeled gain of five (Figure 5A; Supplementary Table S7)."
    ),
    # L220 (Discussion 4.3)
    (
        "The gains in `OG0001778` and `OG0000643` provide additional targets for investigating lineage-specific regulation (Section 3.6; Supplementary Table S7).",
        "The gains in `OG0001778` and `OG0000643` provide additional targets for investigating lineage-specific regulation (Figure 5A; Supplementary Table S7)."
    ),
    # L226 (Discussion 4.3)
    (
        "The copy-number comparisons and their annotation limits (Sections 3.2 and 3.6) make regulatory studies especially relevant.",
        "The copy-number comparisons and their annotation limits (Supplementary Table S7) make regulatory studies especially relevant."
    ),
    # L230 (Discussion 4.4)
    (
        "The trio estimates show a predominance of $\\omega\\le1$ in both focal branches (7,798 of 8,737 trios) and median ratios below one (Section 3.7).",
        "The trio estimates show a predominance of $\\omega\\le1$ in both focal branches (7,798 of 8,737 trios) and median ratios below one (Figure 6A; Supplementary Table S9)."
    ),
    # L234 (Discussion 4.4)
    (
        "plant lipid-transfer-protein, exostosin and glycosyl-hydrolase annotations occur among the *V. peripherica* candidates (Section 3.7).",
        "plant lipid-transfer-protein, exostosin and glycosyl-hydrolase annotations occur among the *V. peripherica* candidates (Table 3)."
    ),
    # L238 (Discussion 4.5)
    (
        "The gene-family contrast is conditional on the selected annotation set, monocot-rooted family filter, dated tree and birth-death model (Sections 2.4-2.5).",
        "The gene-family contrast is conditional on the selected annotation set, monocot-rooted family filter, dated tree and birth-death model (Supplementary Tables S3 and S5)."
    ),
    # L240 (Discussion 4.5)
    (
        "Likewise, excluding organellar-annotated families in a sensitivity analysis differs from validating every copy as a functional nuclear gene (Section 2.5).",
        "Likewise, excluding organellar-annotated families in a sensitivity analysis differs from validating every copy as a functional nuclear gene (Supplementary Table S6)."
    ),
    # L272 (Figure 4 legend)
    (
        "Global correction is unavailable for the descriptive ancestral contrast (Section 2.7).",
        "Global correction is unavailable for the descriptive ancestral contrast (Supplementary Table S6)."
    ),
    # L274 (Figure 5 legend)
    (
        "The numerical comparisons are described separately from unresolved domain identities in Section 3.6 and Supplementary Table S7.",
        "The numerical comparisons and domain annotations are detailed in Supplementary Table S7."
    ),
    # L280 (Figure S1 legend)
    (
        "Block orientation, chromosome correspondence and overlap must be considered when interpreting structural differences (Section 3.1; evidence gap R4).",
        "Block orientation, chromosome correspondence and overlap must be considered when interpreting structural differences (evidence gap R4)."
    ),
]

for fp in TARGET_FILES:
    with open(fp, "r", encoding="utf-8") as f:
        text = f.read()
    for idx, (old_s, new_s) in enumerate(replacements, 1):
        assert old_s in text, f"Missing target #{idx} in {fp}: {old_s[:80]}"
        text = text.replace(old_s, new_s)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Updated {fp} ({len(replacements)} replacements)")

