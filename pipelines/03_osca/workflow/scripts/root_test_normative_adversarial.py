#!/usr/bin/env python3
"""
Adversarial Formatting and Normative Verification Suite for Chapter 2 Manuscript
Target: chapter2_osca/manuscript/chapter_2_osca_mechanosensation.md

Stress-tests:
1. Word counts of Resumo and Abstract (~250 words: 230 to 265 words).
2. Presence of all 5 structured sections in Resumo and Abstract.
3. Keywords (5 PT, 5 EN, period-delimited and alphabetized).
4. Strict zero bullet lists in narrative text.
5. Strict zero external citations in Results.
6. Alphabetical order of Section 7 references (TANG before TEODORO).
7. 100% two-way concordance between in-text citations and reference list.
8. Uniform et al. for works with >3 authors.
"""

import os
import re
import sys
import unicodedata

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]
MANUSCRIPT_PATH = str(PROJECT_ROOT / "docs" / "04_chapter_4_osca" / "manuscripts" / "chapter_4_osca_mechanosensation.md")

def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")

def run_adversarial_suite():
    print("=" * 80)
    print("CHAPTER 2 ADVERSARIAL FORMATTING & NORMATIVE AUDIT SUITE")
    print("Target Manuscript:", MANUSCRIPT_PATH)
    print("=" * 80)

    if not os.path.exists(MANUSCRIPT_PATH):
        print(f"[FATAL] Manuscript not found at {MANUSCRIPT_PATH}")
        sys.exit(1)

    with open(MANUSCRIPT_PATH, "r", encoding="utf-8") as f:
        full_text = f.read()

    passes = []
    failures = []

    def record_check(test_id, passed, description, details=""):
        if passed:
            passes.append((test_id, description, details))
            print(f"[PASS] {test_id}: {description}")
            if details:
                print(f"       Details: {details}")
        else:
            failures.append((test_id, description, details))
            print(f"[FAIL] {test_id}: {description}")
            print(f"       Details: {details}")

    # -------------------------------------------------------------------------
    # Parsing Sections
    # -------------------------------------------------------------------------
    lines = full_text.splitlines()

    # Extract Resumo and Abstract
    resumo_text = ""
    resumo_kw = ""
    abstract_text = ""
    abstract_kw = ""

    in_resumo = False
    in_abstract = False

    for line in lines:
        if line.startswith("## RESUMO"):
            in_resumo = True
            in_abstract = False
            continue
        elif line.startswith("## ABSTRACT"):
            in_resumo = False
            in_abstract = True
            continue
        elif line.startswith("## 1. INTRODUCTION"):
            in_resumo = False
            in_abstract = False
            break

        if in_resumo:
            if line.startswith("**Palavras-chave:**"):
                resumo_kw = line
            elif line.strip() and not line.startswith("#"):
                resumo_text += line.strip() + " "
        elif in_abstract:
            if line.startswith("**Keywords:**"):
                abstract_kw = line
            elif line.strip() and not line.startswith("#"):
                abstract_text += line.strip() + " "

    resumo_text = resumo_text.strip()
    abstract_text = abstract_text.strip()

    # Extract Sections
    sec_intro = re.search(r"## 1\. INTRODUCTION(.*?)(?=## 2\. MATERIAL AND METHODS)", full_text, re.DOTALL).group(1)
    sec_methods = re.search(r"## 2\. MATERIAL AND METHODS(.*?)(?=## 3\. RESULTS)", full_text, re.DOTALL).group(1)
    sec_results = re.search(r"## 3\. RESULTS(.*?)(?=## 4\. DISCUSSION)", full_text, re.DOTALL).group(1)
    sec_discussion = re.search(r"## 4\. DISCUSSION(.*?)(?=## 5\. CONCLUSIONS)", full_text, re.DOTALL).group(1)
    sec_conclusions = re.search(r"## 5\. CONCLUSIONS(.*?)(?=## 6\. FIGURE LEGENDS)", full_text, re.DOTALL).group(1)
    sec_figures = re.search(r"## 6\. FIGURE LEGENDS(.*?)(?=## 7\. REFERENCES)", full_text, re.DOTALL).group(1)
    sec_references = full_text.split("## 7. REFERENCES")[1].strip()

    narrative_sections = {
        "Resumo": resumo_text,
        "Abstract": abstract_text,
        "Section 1 (Introduction)": sec_intro,
        "Section 2 (Material and Methods)": sec_methods,
        "Section 3 (Results)": sec_results,
        "Section 4 (Discussion)": sec_discussion,
        "Section 5 (Conclusions)": sec_conclusions,
    }

    # -------------------------------------------------------------------------
    # TEST 1: Word counts of Resumo and Abstract (~250 words: 230 to 265 words)
    # -------------------------------------------------------------------------
    print("\n--- TEST 1: Word counts of Resumo and Abstract ---")
    resumo_words_raw = len(resumo_text.split())
    abstract_words_raw = len(abstract_text.split())

    # Stripped of markdown bold markers
    clean_resumo = re.sub(r"\*\*([^*]+)\*\*", r"\1", resumo_text)
    clean_abstract = re.sub(r"\*\*([^*]+)\*\*", r"\1", abstract_text)
    resumo_words_clean = len(clean_resumo.split())
    abstract_words_clean = len(clean_abstract.split())

    t1_resumo_pass = (230 <= resumo_words_raw <= 265)
    t1_abstract_pass = (230 <= abstract_words_raw <= 265)

    record_check(
        "T1_RESUMO_WORDCOUNT",
        t1_resumo_pass,
        "Resumo word count is within strict bounds (230-265 words)",
        f"Actual: {resumo_words_raw} words (clean: {resumo_words_clean})"
    )

    record_check(
        "T1_ABSTRACT_WORDCOUNT",
        t1_abstract_pass,
        "Abstract word count is within strict bounds (230-265 words)",
        f"Actual: {abstract_words_raw} words (clean: {abstract_words_clean})"
    )

    # -------------------------------------------------------------------------
    # TEST 2: Presence of all 5 structured sections in Resumo and Abstract
    # -------------------------------------------------------------------------
    print("\n--- TEST 2: Presence of all 5 structured sections ---")
    resumo_headers = ["Contexto:", "Objetivo:", "Métodos:", "Resultados:", "Conclusão:"]
    abstract_headers = ["Background:", "Objective:", "Methods:", "Results:", "Conclusion:"]

    resumo_missing = [h for h in resumo_headers if h not in resumo_text]
    abstract_missing = [h for h in abstract_headers if h not in abstract_text]

    # Verify sequential order in Resumo
    resumo_indices = [resumo_text.find(h) for h in resumo_headers]
    resumo_ordered = resumo_indices == sorted(resumo_indices) and (-1 not in resumo_indices)

    # Verify sequential order in Abstract
    abstract_indices = [abstract_text.find(h) for h in abstract_headers]
    abstract_ordered = abstract_indices == sorted(abstract_indices) and (-1 not in abstract_indices)

    record_check(
        "T2_RESUMO_STRUCTURE",
        len(resumo_missing) == 0 and resumo_ordered,
        "Resumo contains all 5 required structured sections in sequential order",
        f"Found: {resumo_headers if not resumo_missing else 'Missing: ' + str(resumo_missing)}"
    )

    record_check(
        "T2_ABSTRACT_STRUCTURE",
        len(abstract_missing) == 0 and abstract_ordered,
        "Abstract contains all 5 required structured sections in sequential order",
        f"Found: {abstract_headers if not abstract_missing else 'Missing: ' + str(abstract_missing)}"
    )

    # -------------------------------------------------------------------------
    # TEST 3: Keywords (5 PT, 5 EN, period-delimited)
    # -------------------------------------------------------------------------
    print("\n--- TEST 3: Keywords Formatting and Count ---")
    pt_match = re.search(r"\*\*Palavras-chave:\*\*\s*(.*)", resumo_kw)
    en_match = re.search(r"\*\*Keywords:\*\*\s*(.*)", abstract_kw)

    pt_raw = pt_match.group(1).strip() if pt_match else ""
    en_raw = en_match.group(1).strip() if en_match else ""

    pt_terms = [t.strip() for t in pt_raw.split(".") if t.strip()]
    en_terms = [t.strip() for t in en_raw.split(".") if t.strip()]

    # Check termination with period
    pt_terminated = pt_raw.endswith(".")
    en_terminated = en_raw.endswith(".")

    # Check alphabetical order
    pt_sorted = pt_terms == sorted(pt_terms, key=lambda s: strip_accents(s.lower()))
    en_sorted = en_terms == sorted(en_terms, key=lambda s: s.lower())

    record_check(
        "T3_KEYWORDS_PT_COUNT",
        len(pt_terms) == 5,
        "Resumo has exactly 5 Portuguese keywords",
        f"Count={len(pt_terms)}: {pt_terms}"
    )
    record_check(
        "T3_KEYWORDS_PT_FORMAT",
        pt_terminated and pt_sorted,
        "Resumo keywords are period-delimited, period-terminated, and alphabetized",
        f"Terminated={pt_terminated}, Sorted={pt_sorted}"
    )

    record_check(
        "T3_KEYWORDS_EN_COUNT",
        len(en_terms) == 5,
        "Abstract has exactly 5 English keywords",
        f"Count={len(en_terms)}: {en_terms}"
    )
    record_check(
        "T3_KEYWORDS_EN_FORMAT",
        en_terminated and en_sorted,
        "Abstract keywords are period-delimited, period-terminated, and alphabetized",
        f"Terminated={en_terminated}, Sorted={en_sorted}"
    )

    # -------------------------------------------------------------------------
    # TEST 4: Strict zero bullet lists in narrative text
    # -------------------------------------------------------------------------
    print("\n--- TEST 4: Strict zero bullet lists in narrative text ---")
    bullet_violations = []

    for sec_name, sec_content in narrative_sections.items():
        sec_lines = sec_content.splitlines()
        for idx, s_line in enumerate(sec_lines, start=1):
            s_stripped = s_line.strip()
            # Check markdown bullet syntax at beginning of line
            if re.match(r"^[-*+]\s+", s_stripped):
                bullet_violations.append((sec_name, idx, s_stripped))
            # Check numbered list syntax at beginning of line (excluding markdown headers)
            elif re.match(r"^\d+\.\s+", s_stripped) and not s_line.startswith("#"):
                bullet_violations.append((sec_name, idx, s_stripped))

    record_check(
        "T4_ZERO_BULLETS",
        len(bullet_violations) == 0,
        "Strict zero bullet lists or numbered lists in all narrative sections",
        f"Violations found: {len(bullet_violations)} {bullet_violations}"
    )

    # -------------------------------------------------------------------------
    # TEST 5: Strict zero external citations in Results
    # -------------------------------------------------------------------------
    print("\n--- TEST 5: Strict zero external citations in Results ---")
    # Check for 4-digit years in Section 3
    years_in_results = re.findall(r"\b(19\d\d|20\d\d)\b", sec_results)

    # Check for author names followed by year or parenthetical citations
    citations_in_results = re.findall(r"\([A-Z]{3,}[^)]*\)", sec_results)
    # Filter out false positives like KEGG pathway map: (KEGG map00500)
    actual_author_citations = [
        c for c in citations_in_results
        if not c.startswith("(KEGG") and not c.startswith("(Figure") and not c.startswith("(Supplementary")
    ]

    record_check(
        "T5_ZERO_YEARS_IN_RESULTS",
        len(years_in_results) == 0,
        "Strict zero 4-digit years (19xx/20xx) in Section 3 (Results)",
        f"Matches: {years_in_results}"
    )

    record_check(
        "T5_ZERO_CITATIONS_IN_RESULTS",
        len(actual_author_citations) == 0,
        "Strict zero author-date citations in Section 3 (Results)",
        f"Matches: {actual_author_citations}"
    )

    # -------------------------------------------------------------------------
    # TEST 6: Alphabetical order of Section 7 references (TANG before TEODORO)
    # -------------------------------------------------------------------------
    print("\n--- TEST 6: Alphabetical order of Section 7 references ---")
    ref_entries = [e.strip() for e in re.split(r"\n\s*\n", sec_references) if e.strip()]

    ref_heads = []
    first_author_surnames = []
    for entry in ref_entries:
        head = entry.split(".")[0].strip()
        ref_heads.append(head)
        first_surname = re.split(r"[,;]", head)[0].strip()
        first_author_surnames.append(first_surname)

    # Verify TANG before TEODORO
    tang_idx = -1
    teodoro_idx = -1
    for i, s in enumerate(first_author_surnames):
        if s == "TANG":
            tang_idx = i
        elif s == "TEODORO":
            teodoro_idx = i

    tang_before_teodoro = (tang_idx != -1 and teodoro_idx != -1 and tang_idx < teodoro_idx)
    record_check(
        "T6_TANG_BEFORE_TEODORO",
        tang_before_teodoro,
        "TANG appears before TEODORO in Section 7 references",
        f"TANG index: {tang_idx}, TEODORO index: {teodoro_idx}"
    )

    # Check standard lexicographical order of entries under Python default sort
    is_lex_sorted = (ref_heads == sorted(ref_heads))
    record_check(
        "T6_PYTHON_LEXICOGRAPHICAL_SORT",
        is_lex_sorted,
        "Section 7 references are strictly sorted under standard Python lexicographical comparison",
        f"Reference count: {len(ref_entries)}, Lexicographically sorted: {is_lex_sorted}"
    )

    # -------------------------------------------------------------------------
    # TEST 7: 100% two-way concordance between in-text citations and reference list
    # -------------------------------------------------------------------------
    print("\n--- TEST 7: 100% Two-way citation concordance ---")
    body_text = full_text.split("## 7. REFERENCES")[0]

    # Find all parenthetical citation groups in body
    paren_groups = re.findall(r"\(([^)]*?\b(?:19\d\d|20\d\d)[^)]*?)\)", body_text)

    # Split distinct citations inside parentheses:
    # In ABNT, authors within one citation are separated by semicolons (e.g. "BASU; HASWELL, 2017").
    # Distinct citations are separated by semicolons preceded by a year (e.g. "... 2017; HASWELL...").
    in_text_citations = []
    for pg in paren_groups:
        splits = re.split(r"(?<=\b\d{4})\s*;\s*", pg)
        for s in splits:
            s_clean = re.sub(r"\s+", " ", s).strip()
            if re.search(r"\b\d{4}\b", s_clean):
                in_text_citations.append(s_clean)

    unique_in_text = sorted(set(in_text_citations))
    print(f"Extracted {len(in_text_citations)} total citation instances ({len(unique_in_text)} unique):")
    for cit in unique_in_text:
        print(f"  In-text: {cit}")

    # Build reference signatures: (Primary Author Surname, Year)
    ref_signatures = {}
    for i, entry in enumerate(ref_entries):
        ym = re.search(r"\b(19\d\d|20\d\d)\b", entry)
        year = ym.group(1) if ym else "NO_YEAR"
        first_word = entry.split()[0]
        surname = re.split(r"[,;]", first_word)[0].strip()
        ref_signatures[i] = (surname, year, entry)

    # Concordance matching
    unmatched_in_text = []
    matched_refs = set()

    for cit in unique_in_text:
        ym = re.search(r"\b(19\d\d|20\d\d)\b", cit)
        cit_year = ym.group(1) if ym else None
        first_word = cit.split()[0]
        cit_surname = re.split(r"[,;]", first_word)[0].strip()

        matched = False
        for ref_idx, (r_surname, r_year, r_entry) in ref_signatures.items():
            if cit_year == r_year and cit_surname == r_surname:
                matched = True
                matched_refs.add(ref_idx)
                break
        if not matched:
            unmatched_in_text.append(cit)

    unreferenced_bib = [ref_signatures[idx][2][:60] + "..." for idx in range(len(ref_entries)) if idx not in matched_refs]

    record_check(
        "T7_FORWARD_CONCORDANCE",
        len(unmatched_in_text) == 0,
        "Every in-text citation has a matching reference in Section 7 (0 orphaned citations)",
        f"Orphaned in-text citations: {unmatched_in_text}"
    )

    record_check(
        "T7_BACKWARD_CONCORDANCE",
        len(unreferenced_bib) == 0,
        "Every Section 7 reference is cited in the manuscript (0 unreferenced bibliography entries)",
        f"Unreferenced bibliography entries: {unreferenced_bib}"
    )

    record_check(
        "T7_TOTAL_REFERENCE_COUNT",
        len(ref_entries) == 28,
        "Section 7 contains exactly 28 reference entries matching audited catalog",
        f"Actual count: {len(ref_entries)}"
    )

    # -------------------------------------------------------------------------
    # TEST 8: Uniform et al. for works with >3 authors
    # -------------------------------------------------------------------------
    print("\n--- TEST 8: Uniform et al. for works with >3 authors ---")

    # Author count ground truth from verified bibliography:
    # 1 author: EDDY (2011), YANG (2007)
    # 2 authors: BASU; HASWELL (2017), HASWELL; VERSLUES (2015), LYNCH; FORCE (2000), QUINLAN; HALL (2010), YANG; NIELSEN (2000)
    # 3 authors: HAGBERG; SCHULT; SWART (2008), KÄLL; KROGH; SONNHAMMER (2004), LIU; WANG; SUN (2018), LOVE; HUBER; ANDERS (2014), SUYAMA; TORRENTS; BORK (2006)
    # >3 authors (16 works): ALCANTARA, COCK, DOBIN, KOSAKOVSKY POND (2020), KOSAKOVSKY POND (2021), LESCOT, MINH, MURTHY, PINTO, SZKLARCZYK, TANG, TEODORO, VIEIRA, WERTHEIM, YUAN, ZHANG

    greater_than_3_authors = {
        ("ALCANTARA", "2015"), ("COCK", "2009"), ("DOBIN", "2013"),
        ("KOSAKOVSKY POND", "2020"), ("KOSAKOVSKY POND", "2021"),
        ("LESCOT", "2002"), ("MINH", "2020"), ("MURTHY", "2018"),
        ("PINTO", "2025"), ("SZKLARCZYK", "2023"), ("TANG", "2008"),
        ("TEODORO", "2021"), ("VIEIRA", "2025"), ("WERTHEIM", "2015"),
        ("YUAN", "2014"), ("ZHANG", "2018")
    }

    up_to_3_authors = {
        ("EDDY", "2011"), ("YANG", "2007"),
        ("BASU", "2017"), ("HASWELL", "2015"), ("LYNCH", "2000"),
        ("QUINLAN", "2010"), ("YANG", "2000"),
        ("HAGBERG", "2008"), ("KÄLL", "2004"), ("LIU", "2018"),
        ("LOVE", "2014"), ("SUYAMA", "2006")
    }

    # Verify Section 7 references formatting
    et_al_bib_violations = []
    for idx, (s_name, year, entry) in ref_signatures.items():
        key = (s_name, year)
        has_et_al = "et al." in entry
        if key in greater_than_3_authors:
            if not has_et_al:
                et_al_bib_violations.append((key, "Expected et al. in bibliography, but missing"))
        elif key in up_to_3_authors:
            if has_et_al:
                et_al_bib_violations.append((key, "Expected explicit author list (<=3 authors), but found et al."))

    # Verify in-text citations formatting
    et_al_in_text_violations = []
    for cit in unique_in_text:
        ym = re.search(r"\b(19\d\d|20\d\d)\b", cit)
        cit_year = ym.group(1) if ym else None
        first_word = cit.split()[0]
        cit_surname = re.split(r"[,;]", first_word)[0].strip()
        key = (cit_surname, cit_year)

        has_et_al = "et al." in cit
        if key in greater_than_3_authors:
            if not has_et_al:
                et_al_in_text_violations.append((cit, "Expected et al. in in-text citation, but missing"))
        elif key in up_to_3_authors:
            if has_et_al:
                et_al_in_text_violations.append((cit, "Expected explicit author list (<=3 authors), but found et al."))

    record_check(
        "T8_UNIFORM_ET_AL_BIBLIOGRAPHY",
        len(et_al_bib_violations) == 0,
        "All works with >3 authors use uniform 'et al.' in Section 7 references, and works with <=3 authors list all authors",
        f"Violations: {et_al_bib_violations}"
    )

    record_check(
        "T8_UNIFORM_ET_AL_IN_TEXT",
        len(et_al_in_text_violations) == 0,
        "All in-text citations for works with >3 authors use uniform 'et al.', and works with <=3 authors list all authors",
        f"Violations: {et_al_in_text_violations}"
    )

    # -------------------------------------------------------------------------
    # Summary and Final Verdict
    # -------------------------------------------------------------------------
    print("\n" + "=" * 80)
    print("AUDIT SUMMARY & VERDICT")
    print("=" * 80)
    print(f"Total Checks Run : {len(passes) + len(failures)}")
    print(f"Total Passed     : {len(passes)}")
    print(f"Total Failed     : {len(failures)}")

    if len(failures) == 0:
        verdict = "APPROVE"
        print("\n>>> FINAL VERDICT: APPROVE <<<")
        print("All 8 adversarial formatting and normative tests passed with 100% compliance.")
    else:
        verdict = "REJECT"
        print("\n>>> FINAL VERDICT: REJECT <<<")
        print("The manuscript failed one or more adversarial normative checks:")
        for f_id, f_desc, f_det in failures:
            print(f"  - {f_id}: {f_desc} -> {f_det}")

    return verdict, passes, failures

if __name__ == "__main__":
    verdict, passes, failures = run_adversarial_suite()
    sys.exit(0 if verdict == "APPROVE" else 1)
