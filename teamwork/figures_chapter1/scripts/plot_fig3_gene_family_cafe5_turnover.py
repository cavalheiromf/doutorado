#!/usr/bin/env python3
"""
Plot script wrapper for Figure 3.
Directly calls generate_fig3.create_figure_3_svg().
"""

import sys
import os

# Add current dir to sys.path to import generate_fig3
sys.path.insert(0, os.path.dirname(__file__))
from generate_fig3 import create_figure_3_svg, validate_svg

if __name__ == "__main__":
    out_file = "/home/mfcaval/github/doutorado/teamwork/figures_chapter1/fig3_gene_family_cafe5_turnover.svg"
    if len(sys.argv) > 1:
        out_file = sys.argv[1]
    create_figure_3_svg(out_file)
    validate_svg(out_file)
