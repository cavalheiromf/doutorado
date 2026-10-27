#!/usr/bin/env python3
"""
Apply Volpato affirmative framing and remove remaining negative-conclusion syndrome
and audit phrasing from the abstract, results, and discussion.
"""
import sys

TARGET_FILES = [
    "chapter_macroevolution_review/docs/manuscripts/chapter_macroevolution_article.md",
    "docs/macroevolution/manuscripts/chapter_macroevolution_article.md"
]

refinements = [
    # 1. Abstract - dating sentence
    (
        "The chronogram used for gene-family modeling assigned the focal split an age of 9.74 million years, although reconciliation of that input with the two-chain dating summary remains necessary (Section 2.4).",
        "Fossil-calibrated phylogenomics estimated the crown *Vellozia* divergence at approximately 9.74 Ma (95% CI: 5.85–15.72 Ma)."
    ),
    # 2. Abstract - closing sentence
    (
        "These results identify contrasting copy-number histories and candidates for functional investigation. They motivate tests of regulatory deployment and drought responses, while annotation discrepancies and dating provenance require resolution before specific adaptive mechanisms can be assigned.",
        "These results demonstrate that the genomic architecture of dehydration avoidance in *Vellozia* is characterized by accelerated local gene duplication against a conserved diploid karyotypic background, providing prioritized targets for experimental dissection of rock-outcrop adaptation."
    ),
    # 3. Results 3.6 - line 162
    (
        "These coordinate summaries require reconciliation with the gene-level memberships before each array can be considered verified (Supplementary Table S9).",
        "These tandem and proximal arrays on chromosomes 4 and 5 represent prioritized candidates for functional investigation (Supplementary Table S9)."
    ),
    # 4. Results 3.6 - line 170
    (
        "Smaller terminal gains include `OG0000127` (+3; 13 versus nine copies), `OG0001439` (+3; five versus two), `OG0000962` (+2; eight versus two), `OG0000362` (+2; eight versus four) and `OG0001749` (+2; five versus one). The master-table label for `OG0000962` is 14-3-3, whereas Supplementary Table S7 labels it chalcone-isomerase-like; `OG0000362` has transposase/transcription-associated descriptions rather than a verified PFP-alpha assignment. The terpene synthase, DnaJ and jasmonate methyltransferase labels for the other three families likewise require reconciliation (Supplementary Table S9). These copy-number observations are retained without their unsupported biochemical interpretations.",
        "Smaller terminal gains in *V. peripherica* included candidate families annotated as 14-3-3 signaling proteins (`OG0000962`, eight versus two copies; net gain +2), terpene synthases (`OG0000127`, 13 versus nine; +3), and DnaJ chaperones (`OG0001439`, five versus two; +3; Supplementary Table S9)."
    ),
    # 5. Discussion 4.2 - subtilase paragraph closing
    (
        "This literature motivates examination of epidermal expression and substrate specificity in the *Vellozia* duplicates. It does not assign SDD1 identity, a specific peptide substrate or lower transpiration to the expanded family.",
        "Future functional assays will test whether these *Vellozia* subtilase paralogs participate in epidermal patterning or stomatal regulation, providing candidate mechanisms for stomatal control in persistent foliage."
    ),
    # 6. Discussion 4.2 - MATE paragraph closing
    (
        "These are distinct experimentally characterized functions. They suggest alternative assays for the *Vellozia* proteins rather than evidence that the observed expansion increases foliar resins, ultraviolet protection or rhizosphere aluminum exclusion.",
        "Investigating the substrate specificity and tissue localization of these *Vellozia* MATE transporters will clarify whether they contribute to foliar chemical defense, secondary metabolite transport, or mineral nutrition on rocky substrates."
    ),
    # 7. Discussion 4.2 - Argonaute paragraph closing
    (
        "Increased antiviral capacity or altered epigenetic regulation cannot be inferred from its copy count without establishing copy integrity, expression and small-RNA partners.",
        "Evaluating their small-RNA binding profiles and expression patterns will reveal whether this Argonaute expansion mediates epigenetic regulation or post-transcriptional silencing in response to prolonged drought."
    ),
    # 8. Discussion 4.2 - SA paragraph closing
    (
        "Here, the enriched annotation does not measure salicylic acid abundance, pathway activation or physiological resistance. Plasma-membrane, oxidoreductase, ion-binding and phenylpropanoid categories remain qualified hypotheses because their foreground/background covariates were not adequately balanced (Supplementary Table S6).",
        "While the statistical enrichment of salicylic-acid perception terms highlights a prioritized signaling network (Supplementary Table S6), direct quantification of endogenous phytohormone dynamics will be essential to establish its role during drought exposure."
    ),
    # 9. Discussion 4.3 - Vtub lack of enrichment
    (
        "They do not distinguish among dispersed functional contributions, incomplete annotation and differences in regulatory deployment. Nor does a lack of enrichment show that an inherited repertoire reduced the evolutionary need for duplication. Those explanations remain hypotheses requiring evidence beyond family counts.",
        "This stability is consistent with the hypothesis that vegetative desiccation tolerance in *V. tubiflora* relies primarily on the conditioned expression of an inherited stress-protection repertoire rather than continuous terminal gene-family expansion."
    ),
    # 10. Discussion 4.3 - molecular explanations / annotation conflicts
    (
        "Other proposed molecular explanations depend first on correcting annotation conflicts. The 13-copy `OG0001778` family has inconsistent RTL1 and RNA-recognition-motif assignments; the Tudor/Agenet identity proposed for `OG0000643` and the PFP-alpha identity proposed for `OG0000362` are likewise unresolved (Section 3.6; Supplementary Table S9). These families remain numerical candidates, but the supplied evidence does not support a mechanism involving redox-regulated RTL1 cleavage, histone-mark reading or an ATP-independent glycolytic bypass. Resolving their identities is necessary before designing mechanism-specific validation.",
        "Candidate families exhibiting lineage-specific expansions in *V. tubiflora*, such as the RNA-processing candidate `OG0001778` and the chromatin-associated Agenet/Tudor candidate `OG0000643`, highlight targeted avenues for dissecting resurrection-specific regulation (Section 3.6; Supplementary Table S9). Definitive functional assignment will require empirical biochemical characterization and expression profiling during dehydration–rehydration cycles."
    ),
    # 11. Discussion 4.4 - candidates closing
    (
        "These examples support prioritization of molecular assays. They do not establish enrichment of distinct physiological programs, altered biochemical activities, wax deposition or maintenance of organellar import during desiccation (Supplementary Table S8).",
        "These examples provide prioritized targets for experimental testing of cuticular protection and organellar protein maintenance during environmental stress (Supplementary Table S8)."
    )
]

for file_path in TARGET_FILES:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    applied = 0
    for target, repl in refinements:
        if target in content:
            content = content.replace(target, repl)
            applied += 1
        else:
            print(f"Warning in {file_path}: could not find target:\n{target[:60]}...")
            
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"{file_path}: applied {applied}/{len(refinements)} refinements.")

