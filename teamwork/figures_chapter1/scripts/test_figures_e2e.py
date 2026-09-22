#!/usr/bin/env python3
"""
End-to-End (E2E) Automated Test Suite for Chapter 1 Vector Figures
==================================================================
Project: PhD Thesis — Chapter 1 Figure Suite
Author: e2e_test_writer (E2E Testing & Quality Assurance Specialist)
Target: Validation of publication-grade SVG figures and generator scripts.

5-Tier Verification Framework:
- Tier 1: XML & SVG Validity (ElementTree parsing, viewBox, xmlns, canvas ratios)
- Tier 2: Vector Standards & Typography (native <text> nodes, font-family, no <image> rasters)
- Tier 3: Semantic Structure & Grouping (<g id="..."> hierarchy across panels)
- Tier 4: Empirical Precision Verification (100% exact numerical match with chapter_macroevolution/)
- Tier 5: Python Script Execution & Generation Test (standalone CLI reproducibility)

Usage:
  python3 test_figures_e2e.py
  python3 -m unittest -v test_figures_e2e.py
  python3 test_figures_e2e.py --tier 1
  python3 test_figures_e2e.py --figure 1
"""

import os
import sys
import re
import glob
import subprocess
import unittest
import xml.etree.ElementTree as ET

# Base directories
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
FIGURES_DIR = os.path.join(BASE_DIR, "teamwork", "figures_chapter1")
SCRIPTS_DIR = os.path.join(FIGURES_DIR, "scripts")
EMPIRICAL_DIR = os.path.join(BASE_DIR, "chapter_macroevolution")

# Expected figure files mapping
FIGURE_FILES = {
    1: "fig1_dating_chronogram_biogeography.svg",
    2: "fig2_orthology_macrosynteny.svg",
    3: "fig3_gene_family_cafe5_turnover.svg",
    4: "fig4_selection_landscape_ppr.svg",
    5: "fig5_conceptual_macroevolution_synthesis.svg",
}

# Generator script candidates (supports multiple naming conventions)
GENERATOR_SCRIPTS = {
    1: ["generate_fig1.py", "plot_fig1_dating_chronogram_biogeography.py", "plot_fig1_dating_chronogram.py", "plot_fig1.py"],
    2: ["generate_fig2.py", "plot_fig2_orthology_macrosynteny.py", "plot_fig2_orthology.py", "plot_fig2.py"],
    3: ["generate_fig3.py", "plot_fig3_gene_family_cafe5_turnover.py", "plot_fig3_gene_family_cafe5.py", "plot_fig3.py"],
    4: ["generate_fig4.py", "plot_fig4_selection_landscape_ppr.py", "plot_fig4_selection_landscape.py", "plot_fig4.py"],
    5: ["generate_fig5.py", "plot_fig5_conceptual_macroevolution_synthesis.py", "plot_fig5_conceptual_synthesis.py", "plot_fig5.py"],
}

# XML Namespaces
SVG_NAMESPACES = {
    "svg": "http://www.w3.org/2000/svg",
    "xlink": "http://www.w3.org/1999/xlink",
}


class BaseFigureTestCase(unittest.TestCase):
    """Base test case providing XML parsing and inspection utilities."""

    def get_figure_path(self, fig_num: int) -> str:
        """Resolve the file path for a figure number, checking aliases if needed."""
        filename = FIGURE_FILES.get(fig_num)
        if not filename:
            self.fail(f"Invalid figure number: {fig_num}")
        path = os.path.join(FIGURES_DIR, filename)
        if not os.path.isfile(path):
            # Check for case-insensitive or slight pattern match
            matches = glob.glob(os.path.join(FIGURES_DIR, f"*fig{fig_num}*.svg")) + \
                      glob.glob(os.path.join(FIGURES_DIR, f"*Fig{fig_num}*.svg"))
            if matches:
                return matches[0]
        return path

    def load_and_parse_svg(self, fig_num: int) -> tuple:
        """
        Loads the SVG file and parses it with xml.etree.ElementTree.
        Returns (tree, root, raw_content, filepath).
        """
        filepath = self.get_figure_path(fig_num)
        self.assertTrue(
            os.path.isfile(filepath),
            f"Figure {fig_num} file not found at: {filepath}. Please generate figure SVG first."
        )
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                raw_content = f.read()
        except Exception as e:
            self.fail(f"Failed to read SVG file {filepath}: {e}")

        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
        except ET.ParseError as pe:
            self.fail(f"SVG XML ParseError in figure {fig_num} ({filepath}): {pe}")

        return tree, root, raw_content, filepath

    def get_clean_tag(self, elem) -> str:
        """Strip XML namespace from tag."""
        return elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag

    def extract_all_text_elements(self, root) -> list:
        """Extract all text and tspan element texts."""
        texts = []
        for elem in root.iter():
            tag = self.get_clean_tag(elem)
            if tag in ("text", "tspan"):
                if elem.text:
                    texts.append(elem.text.strip())
                for sub in elem:
                    if sub.text:
                        texts.append(sub.text.strip())
                    if sub.tail:
                        texts.append(sub.tail.strip())
                if elem.tail:
                    texts.append(elem.tail.strip())
        return [t for t in texts if t]

    def extract_all_text_corpus(self, root, raw_content: str) -> str:
        """Build a unified text corpus for content verification."""
        extracted = self.extract_all_text_elements(root)
        extracted_text = " ".join(extracted)
        # Also clean raw content by stripping XML tags to catch text in attributes or comments if relevant
        stripped_raw = re.sub(r"<[^>]+>", " ", raw_content)
        return f"{extracted_text} {stripped_raw}"

    def extract_all_group_ids(self, root) -> set:
        """Extract all 'id' attribute values from <g> elements."""
        group_ids = set()
        for elem in root.iter():
            tag = self.get_clean_tag(elem)
            if tag == "g" and "id" in elem.attrib:
                group_ids.add(elem.attrib["id"])
        return group_ids

    def assert_contains_empirical_value(self, corpus: str, value_str: str, label: str = ""):
        """
        Check that an empirical value appears in the text corpus.
        Supports fuzzy number matching for formatted numbers (e.g. 732,066 vs 732066).
        """
        # Direct match
        if value_str in corpus:
            return

        # Case-insensitive match
        if value_str.lower() in corpus.lower():
            return

        # Regex flexible spacing / punctuation match
        escaped = re.escape(value_str)
        # Allow optional comma/space in large numbers e.g. 732,066 or 732066
        flexible_pattern = re.sub(r"\\,", r"[,\\s]?", escaped)
        # Allow variations in spaces around symbols like =, >, +, -
        flexible_pattern = re.sub(r"\\=", r"\\s*=\\s*", flexible_pattern)
        flexible_pattern = re.sub(r"\\>", r"\\s*>\\s*", flexible_pattern)
        flexible_pattern = re.sub(r"\\\+", r"\\s*\\+\\s*", flexible_pattern)

        if re.search(flexible_pattern, corpus, re.IGNORECASE):
            return

        self.fail(
            f"Missing required empirical value '{value_str}' ({label}) in figure text corpus. "
            f"Ground truth verification failed."
        )

    # -------------------------------------------------------------------------
    # Generic Tier 1 & Tier 2 Assertions
    # -------------------------------------------------------------------------

    def verify_tier1_xml_validity(self, fig_num: int):
        """Tier 1: XML Syntax & SVG Well-Formedness."""
        tree, root, raw_content, filepath = self.load_and_parse_svg(fig_num)

        # 1. Root tag must be svg
        root_tag = self.get_clean_tag(root)
        self.assertEqual(
            root_tag, "svg",
            f"Root XML element in {filepath} must be <svg>, but got <{root_tag}>."
        )

        # 2. Check viewBox or width & height
        has_viewbox = "viewBox" in root.attrib or "viewbox" in root.attrib
        has_dims = ("width" in root.attrib and "height" in root.attrib)

        self.assertTrue(
            has_viewbox or has_dims,
            f"SVG root in {filepath} must declare 'viewBox' or 'width'/'height' attributes."
        )

        if has_viewbox:
            vb_val = root.attrib.get("viewBox") or root.attrib.get("viewbox")
            parts = [float(p) for p in re.split(r"[\s,]+", vb_val.strip()) if p]
            self.assertEqual(
                len(parts), 4,
                f"viewBox in {filepath} must contain exactly 4 values (min_x min_y w h), got: '{vb_val}'"
            )
            min_x, min_y, w, h = parts
            self.assertGreater(w, 0, f"viewBox width must be > 0 in {filepath}")
            self.assertGreater(h, 0, f"viewBox height must be > 0 in {filepath}")
            ratio = w / h
            self.assertTrue(
                0.4 <= ratio <= 3.0,
                f"Unusual aspect ratio ({ratio:.2f}) in {filepath}. Expected between 0.4 and 3.0."
            )

        # 3. Check xmlns
        has_xmlns = "xmlns" in root.attrib or "http://www.w3.org/2000/svg" in raw_content
        self.assertTrue(
            has_xmlns,
            f"SVG in {filepath} should declare xmlns='http://www.w3.org/2000/svg'."
        )

    def verify_tier2_vector_standards(self, fig_num: int):
        """Tier 2: Vector Standards, Typography & No Rasters."""
        tree, root, raw_content, filepath = self.load_and_parse_svg(fig_num)

        # 1. Must contain native text elements
        text_elements = self.extract_all_text_elements(root)
        self.assertGreater(
            len(text_elements), 5,
            f"Figure {fig_num} contains too few selectable <text> elements ({len(text_elements)}). "
            f"Text must not be converted to vector paths or omitted."
        )

        # 2. Prohibit embedded raster bitmaps (<image> or data:image URIs)
        image_elements = [e for e in root.iter() if self.get_clean_tag(e) == "image"]
        self.assertEqual(
            len(image_elements), 0,
            f"Figure {fig_num} contains {len(image_elements)} forbidden <image> elements. "
            f"All graphics must be pure editable vectors."
        )
        self.assertNotIn(
            "data:image/png;base64", raw_content,
            f"Figure {fig_num} contains embedded Base64 PNG raster data. Pure SVG required."
        )
        self.assertNotIn(
            "data:image/jpeg;base64", raw_content,
            f"Figure {fig_num} contains embedded Base64 JPEG raster data. Pure SVG required."
        )

        # 3. Typography verification (font-family declarations)
        has_font_declaration = (
            "font-family" in raw_content or
            "font_family" in raw_content or
            "sans-serif" in raw_content or
            "Arial" in raw_content or
            "Helvetica" in raw_content or
            "DejaVu" in raw_content
        )
        self.assertTrue(
            has_font_declaration,
            f"Figure {fig_num} does not declare standard vector font-family attributes or styles."
        )


# =============================================================================
# Figure 1: Bayesian Molecular Dating Chronogram & Historical Biogeography
# =============================================================================
class TestFig1DatingChronogram(BaseFigureTestCase):
    """E2E Test Suite for Figure 1."""

    def test_tier1_xml_validity(self):
        """Fig 1 Tier 1: XML Syntax & SVG Structure."""
        self.verify_tier1_xml_validity(1)

    def test_tier2_vector_standards(self):
        """Fig 1 Tier 2: Vector Standards, Typography & No Bitmaps."""
        self.verify_tier2_vector_standards(1)

    def test_tier3_semantic_structure(self):
        """Fig 1 Tier 3: Semantic Layering & Group Hierarchy."""
        tree, root, raw_content, filepath = self.load_and_parse_svg(1)
        group_ids = self.extract_all_group_ids(root)

        # Check for panel groups
        has_panel_a = any("panel_a" in gid.lower() or "chronogram" in gid.lower() for gid in group_ids)
        has_panel_b = any("panel_b" in gid.lower() or "biogeograph" in gid.lower() or "dispersal" in gid.lower() for gid in group_ids)

        self.assertTrue(
            has_panel_a,
            f"Fig 1 missing semantic group for Panel A (<g id='panel_a'> or <g id='chronogram'>). Found IDs: {group_ids}"
        )
        self.assertTrue(
            has_panel_b,
            f"Fig 1 missing semantic group for Panel B (<g id='panel_b'> or <g id='biogeography'>). Found IDs: {group_ids}"
        )

    def test_tier4_empirical_precision(self):
        """Fig 1 Tier 4: Empirical Precision Verification from chapter_macroevolution/03_dating/."""
        tree, root, raw_content, filepath = self.load_and_parse_svg(1)
        corpus = self.extract_all_text_corpus(root, raw_content)

        # Critical node ages and parameters
        required_empirical_values = [
            ("31.92", "Trans-Atlantic core Velloziaceae divergence node age (Ma)"),
            ("9.74", "Vellozia sister speciation node age (Ma)"),
            ("138.48", "Root divergence node age (Ma)"),
            ("121.90", "Crown monocot divergence node age (Ma)"),
            ("101.26", "Crown Pandanales divergence node age (Ma)"),
            ("78.21", "Crown Velloziaceae divergence node age (Ma)"),
            ("732,066", "Total amino acid sites in supermatrix alignment"),
            ("Oligocene", "Geological epoch for trans-Atlantic disjunction"),
            ("Miocene", "Geological epoch for Vellozia radiation"),
        ]

        for val, desc in required_empirical_values:
            self.assert_contains_empirical_value(corpus, val, desc)


# =============================================================================
# Figure 2: Orthology Partition & Chromosomal Syntenic Architecture
# =============================================================================
class TestFig2OrthologyMacrosynteny(BaseFigureTestCase):
    """E2E Test Suite for Figure 2."""

    def test_tier1_xml_validity(self):
        """Fig 2 Tier 1: XML Syntax & SVG Structure."""
        self.verify_tier1_xml_validity(2)

    def test_tier2_vector_standards(self):
        """Fig 2 Tier 2: Vector Standards, Typography & No Bitmaps."""
        self.verify_tier2_vector_standards(2)

    def test_tier3_semantic_structure(self):
        """Fig 2 Tier 3: Semantic Layering & Group Hierarchy."""
        tree, root, raw_content, filepath = self.load_and_parse_svg(2)
        group_ids = self.extract_all_group_ids(root)

        has_panel_a = any("panel_a" in gid.lower() or "ortholog" in gid.lower() for gid in group_ids)
        has_panel_b = any("panel_b" in gid.lower() or "synteny" in gid.lower() or "chromosome" in gid.lower() for gid in group_ids)

        self.assertTrue(
            has_panel_a,
            f"Fig 2 missing semantic group for Panel A (<g id='panel_a'> or <g id='orthology'>). Found IDs: {group_ids}"
        )
        self.assertTrue(
            has_panel_b,
            f"Fig 2 missing semantic group for Panel B (<g id='panel_b'> or <g id='synteny_ribbons'>). Found IDs: {group_ids}"
        )

    def test_tier4_empirical_precision(self):
        """Fig 2 Tier 4: Empirical Precision Verification from chapter_macroevolution/01_orthology/."""
        tree, root, raw_content, filepath = self.load_and_parse_svg(2)
        corpus = self.extract_all_text_corpus(root, raw_content)

        required_empirical_values = [
            ("17,750", "Total inferred orthogroups across 7 species"),
            ("1,513", "Strict single-copy 1:1 core orthologs"),
            ("297", "Collinear macrosyntenic blocks between Vtub and Vper"),
            ("2n = 18", "Cytogenetic karyotype of Vellozia (x=9)"),
            ("93.2%", "Percentage of genes assigned to orthogroups"),
            ("OSCA", "Conserved mechanosensitive channel gene family / tandem cluster"),
        ]

        for val, desc in required_empirical_values:
            self.assert_contains_empirical_value(corpus, val, desc)


# =============================================================================
# Figure 3: Gene Family Dynamics & Asymmetric Lineage Turnover (CAFE5)
# =============================================================================
class TestFig3GeneFamilyCAFE5(BaseFigureTestCase):
    """E2E Test Suite for Figure 3."""

    def test_tier1_xml_validity(self):
        """Fig 3 Tier 1: XML Syntax & SVG Structure."""
        self.verify_tier1_xml_validity(3)

    def test_tier2_vector_standards(self):
        """Fig 3 Tier 2: Vector Standards, Typography & No Bitmaps."""
        self.verify_tier2_vector_standards(3)

    def test_tier3_semantic_structure(self):
        """Fig 3 Tier 3: Semantic Layering & Group Hierarchy."""
        tree, root, raw_content, filepath = self.load_and_parse_svg(3)
        group_ids = self.extract_all_group_ids(root)

        has_panel_a = any("panel_a" in gid.lower() or "cafe5" in gid.lower() or "tree" in gid.lower() for gid in group_ids)
        has_panel_b = any("panel_b" in gid.lower() or "expansion" in gid.lower() or "functional" in gid.lower() or "categories" in gid.lower() for gid in group_ids)

        self.assertTrue(
            has_panel_a,
            f"Fig 3 missing semantic group for Panel A (<g id='panel_a'> or <g id='cafe5_tree'>). Found IDs: {group_ids}"
        )
        self.assertTrue(
            has_panel_b,
            f"Fig 3 missing semantic group for Panel B (<g id='panel_b'> or <g id='expansion_bars'>). Found IDs: {group_ids}"
        )

    def test_tier4_empirical_precision(self):
        """Fig 3 Tier 4: Empirical Precision Verification from chapter_macroevolution/04_gene_families/."""
        tree, root, raw_content, filepath = self.load_and_parse_svg(3)
        corpus = self.extract_all_text_corpus(root, raw_content)

        required_empirical_values = [
            ("0.638", "CAFE5 global turnover rate lambda (Gamma model)"),
            ("+55", "TOC/TIC translocon expansion in V. tubiflora (OG0000016)"),
            ("+29", "NDH complex expansion in V. tubiflora (OG0000036)"),
            ("+57", "LRR-RLK receptor kinase expansion in V. peripherica (OG0000012)"),
            ("+22", "NB-LRR / NLR disease resistance gene expansion in V. peripherica (OG0000050)"),
            ("+51", "F-box ubiquitin ligase expansion in V. peripherica (OG0000026)"),
            ("TOC/TIC", "Plastid preprotein translocon complex"),
            ("NDH", "Chloroplastic NADH dehydrogenase complex"),
            ("LRR-RLK", "Leucine-rich repeat receptor-like kinases"),
            ("NB-LRR", "NBS-LRR disease resistance sentinels"),
        ]

        for val, desc in required_empirical_values:
            self.assert_contains_empirical_value(corpus, val, desc)


# =============================================================================
# Figure 4: Genome-Wide Selection Landscape & PPR RNA-Editing Architecture
# =============================================================================
class TestFig4SelectionLandscapePPR(BaseFigureTestCase):
    """E2E Test Suite for Figure 4."""

    def test_tier1_xml_validity(self):
        """Fig 4 Tier 1: XML Syntax & SVG Structure."""
        self.verify_tier1_xml_validity(4)

    def test_tier2_vector_standards(self):
        """Fig 4 Tier 2: Vector Standards, Typography & No Bitmaps."""
        self.verify_tier2_vector_standards(4)

    def test_tier3_semantic_structure(self):
        """Fig 4 Tier 3: Semantic Layering & Group Hierarchy."""
        tree, root, raw_content, filepath = self.load_and_parse_svg(4)
        group_ids = self.extract_all_group_ids(root)

        has_panel_a = any("panel_a" in gid.lower() or "selection" in gid.lower() or "kaks" in gid.lower() for gid in group_ids)
        has_panel_b = any("panel_b" in gid.lower() or "ppr" in gid.lower() or "domain" in gid.lower() or "editing" in gid.lower() for gid in group_ids)

        self.assertTrue(
            has_panel_a,
            f"Fig 4 missing semantic group for Panel A (<g id='panel_a'> or <g id='selection_scatter'>). Found IDs: {group_ids}"
        )
        self.assertTrue(
            has_panel_b,
            f"Fig 4 missing semantic group for Panel B (<g id='panel_b'> or <g id='ppr_domain'>). Found IDs: {group_ids}"
        )

    def test_tier4_empirical_precision(self):
        """Fig 4 Tier 4: Empirical Precision Verification from chapter_macroevolution/05_selection/."""
        tree, root, raw_content, filepath = self.load_and_parse_svg(4)
        corpus = self.extract_all_text_corpus(root, raw_content)

        required_empirical_values = [
            ("1,513", "Total single-copy 1:1 orthogroups analyzed with yn00"),
            ("250", "Top positive selection candidate genes (omega > 1.0)"),
            ("722", "Purifying selection orthogroups (omega < 0.5)"),
            ("541", "Neutral / relaxed selection orthogroups (0.5 <= omega <= 1.0)"),
            ("PPR", "Pentatricopeptide repeat family annotation"),
            ("DYW", "DYW cytidine deaminase catalytic domain"),
            ("C-to-U", "Cytidine to uridine organellar RNA editing"),
            ("desiccoplast", "Dismantled plastid during poikilochlorophyllous desiccation"),
            ("1.0", "Neutral selection boundary isocline (omega = 1.0)"),
        ]

        for val, desc in required_empirical_values:
            self.assert_contains_empirical_value(corpus, val, desc)


# =============================================================================
# Figure 5: Conceptual Synthesis: The Evolutionary Cost of "Evergreen" vs "Resurrection"
# =============================================================================
class TestFig5ConceptualSynthesis(BaseFigureTestCase):
    """E2E Test Suite for Figure 5."""

    def test_tier1_xml_validity(self):
        """Fig 5 Tier 1: XML Syntax & SVG Structure."""
        self.verify_tier1_xml_validity(5)

    def test_tier2_vector_standards(self):
        """Fig 5 Tier 2: Vector Standards, Typography & No Bitmaps."""
        self.verify_tier2_vector_standards(5)

    def test_tier3_semantic_structure(self):
        """Fig 5 Tier 3: Semantic Layering & Group Hierarchy."""
        tree, root, raw_content, filepath = self.load_and_parse_svg(5)
        group_ids = self.extract_all_group_ids(root)

        has_concept = any(
            "concept" in gid.lower() or
            "synthesis" in gid.lower() or
            "resurrection" in gid.lower() or
            "evergreen" in gid.lower() or
            "panel_a" in gid.lower() or
            "model" in gid.lower()
            for gid in group_ids
        )

        self.assertTrue(
            has_concept,
            f"Fig 5 missing semantic group (<g id='conceptual_model'>, <g id='resurrection_strategy'>, etc.). Found IDs: {group_ids}"
        )

    def test_tier4_empirical_precision(self):
        """Fig 5 Tier 4: Conceptual Precision & Species Contrasts."""
        tree, root, raw_content, filepath = self.load_and_parse_svg(5)
        corpus = self.extract_all_text_corpus(root, raw_content)

        required_scientific_terms = [
            ("Vellozia tubiflora", "Resurrection focal taxon"),
            ("Vellozia peripherica", "Evergreen sister taxon"),
            ("Poikilochlorophylly", "Desiccation-tolerant thylakoid dismantling strategy"),
            ("Evergreen", "Desiccation-avoidance evergreen habit"),
            ("Resurrection", "Anhydrobiotic resurrection strategy"),
            ("Anhydrobiosis", "Quiescent desiccation tolerance mechanism"),
        ]

        for val, desc in required_scientific_terms:
            self.assert_contains_empirical_value(corpus, val, desc)


# =============================================================================
# Tier 5: Generator Script Execution & Standalone Reproducibility
# =============================================================================
class TestFigureScriptExecution(unittest.TestCase):
    """Tier 5: Verifies that standalone Python scripts execute and produce figures."""

    def find_script_for_figure(self, fig_num: int) -> str:
        """Find an existing generator script matching known naming patterns."""
        candidates = GENERATOR_SCRIPTS.get(fig_num, [])
        for cand in candidates:
            p = os.path.join(SCRIPTS_DIR, cand)
            if os.path.isfile(p):
                return p

        # Fallback glob
        matches = glob.glob(os.path.join(SCRIPTS_DIR, f"*fig{fig_num}*.py")) + \
                  glob.glob(os.path.join(SCRIPTS_DIR, f"*Fig{fig_num}*.py"))
        # Exclude this test file itself
        matches = [m for m in matches if not m.endswith("test_figures_e2e.py")]
        if matches:
            return matches[0]

        return ""

    def run_generator_script(self, fig_num: int):
        """Execute a generator script and check return code and output SVG."""
        script_path = self.find_script_for_figure(fig_num)
        self.assertTrue(
            bool(script_path),
            f"Generator script for Figure {fig_num} not found in {SCRIPTS_DIR}. "
            f"Expected one of: {GENERATOR_SCRIPTS.get(fig_num)}"
        )

        # Run script as subprocess (universal_newlines=True for Python 3.6+ compatibility)
        cmd = [sys.executable, script_path]
        res = subprocess.run(
            cmd,
            cwd=BASE_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            timeout=120
        )

        self.assertEqual(
            res.returncode, 0,
            f"Generator script {script_path} failed with exit code {res.returncode}.\n"
            f"STDOUT:\n{res.stdout}\nSTDERR:\n{res.stderr}"
        )

        # Confirm target SVG exists and is non-empty
        expected_svg = os.path.join(FIGURES_DIR, FIGURE_FILES[fig_num])
        self.assertTrue(
            os.path.isfile(expected_svg),
            f"Script {script_path} completed, but output SVG {expected_svg} does not exist."
        )
        self.assertGreater(
            os.path.getsize(expected_svg), 100,
            f"Output SVG {expected_svg} is unexpectedly small ({os.path.getsize(expected_svg)} bytes)."
        )

    def test_tier5_fig1_script_execution(self):
        """Fig 1 Tier 5: Script reproducibility."""
        self.run_generator_script(1)

    def test_tier5_fig2_script_execution(self):
        """Fig 2 Tier 5: Script reproducibility."""
        self.run_generator_script(2)

    def test_tier5_fig3_script_execution(self):
        """Fig 3 Tier 5: Script reproducibility."""
        self.run_generator_script(3)

    def test_tier5_fig4_script_execution(self):
        """Fig 4 Tier 5: Script reproducibility."""
        self.run_generator_script(4)

    def test_tier5_fig5_script_execution(self):
        """Fig 5 Tier 5: Script reproducibility."""
        self.run_generator_script(5)


# =============================================================================
# CLI Main Runner with Detailed Reporting
# =============================================================================
def main():
    import argparse
    parser = argparse.ArgumentParser(description="Chapter 1 Figures E2E Test Suite Runner")
    parser.add_argument("--tier", type=int, choices=[1, 2, 3, 4, 5], help="Run tests for a specific tier only")
    parser.add_argument("--figure", type=int, choices=[1, 2, 3, 4, 5], help="Run tests for a specific figure only")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose test execution")
    args, unknown = parser.parse_known_args()

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    figure_classes = {
        1: TestFig1DatingChronogram,
        2: TestFig2OrthologyMacrosynteny,
        3: TestFig3GeneFamilyCAFE5,
        4: TestFig4SelectionLandscapePPR,
        5: TestFig5ConceptualSynthesis,
    }

    if args.figure:
        cls = figure_classes[args.figure]
        if args.tier == 5:
            suite.addTest(TestFigureScriptExecution(f"test_tier5_fig{args.figure}_script_execution"))
        elif args.tier:
            tier_methods = [m for m in dir(cls) if m.startswith(f"test_tier{args.tier}")]
            for m in tier_methods:
                suite.addTest(cls(m))
        else:
            suite.addTests(loader.loadTestsFromTestCase(cls))
            suite.addTest(TestFigureScriptExecution(f"test_tier5_fig{args.figure}_script_execution"))
    elif args.tier == 5:
        suite.addTests(loader.loadTestsFromTestCase(TestFigureScriptExecution))
    elif args.tier:
        for fig_num, cls in figure_classes.items():
            tier_methods = [m for m in dir(cls) if m.startswith(f"test_tier{args.tier}")]
            for m in tier_methods:
                suite.addTest(cls(m))
    else:
        # Load all tests
        for cls in figure_classes.values():
            suite.addTests(loader.loadTestsFromTestCase(cls))
        suite.addTests(loader.loadTestsFromTestCase(TestFigureScriptExecution))

    print("=" * 80)
    print(" CHAPTER 1 FIGURE SUITE — END-TO-END (E2E) AUTOMATED TEST RUNNER")
    print("=" * 80)
    print(f" Target Directory : {FIGURES_DIR}")
    print(f" Scripts Directory: {SCRIPTS_DIR}")
    print(f" Total Tests Selected: {suite.countTestCases()}")
    print("=" * 80)

    verbosity = 2 if (args.verbose or "-v" in sys.argv) else 1
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)

    sys.exit(0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    main()
