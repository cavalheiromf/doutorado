#!/bin/bash
# Script to run HyPhy comparative analyses

# 1. Run RELAX analysis to test selection relaxation/intensification
hyphy relax --alignment vellozia_oscas_codon.fasta --tree vellozia_oscas_labeled.treefile --test Test --reference Reference --output relax_results.json

# 2. Run Contrast-FEL to identify site-specific selective pressures between groups (non-interactive)
hyphy contrast-fel --alignment vellozia_oscas_codon.fasta --tree vellozia_oscas_labeled.treefile --output contrast_fel_results.json --contrast Test --reference Reference
