#!/bin/bash
# Local run script for clade OSCA1

echo '=== Running RELAX on osca1 ==='
hyphy relax --alignment osca1_codon.fasta --tree osca1_labeled.treefile --test Test --reference Reference --output relax_results.json

echo '=== Running Contrast-FEL on osca1 ==='
hyphy contrast-fel --alignment osca1_codon.fasta --tree osca1_labeled.treefile --output contrast_fel_results.json --branch-set Test --branch-set Reference
