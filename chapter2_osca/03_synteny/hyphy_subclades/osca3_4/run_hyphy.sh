#!/bin/bash
# Local run script for clade OSCA3_4

echo '=== Running RELAX on osca3_4 ==='
hyphy relax --alignment osca3_4_codon.fasta --tree osca3_4_labeled.treefile --test Test --reference Reference --output relax_results.json

echo '=== Running Contrast-FEL on osca3_4 ==='
hyphy contrast-fel --alignment osca3_4_codon.fasta --tree osca3_4_labeled.treefile --output contrast_fel_results.json --branch-set Test --branch-set Reference
