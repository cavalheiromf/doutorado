#!/bin/bash
# Local run script for clade OSCA2

echo '=== Running RELAX on osca2 ==='
hyphy relax --alignment osca2_codon.fasta --tree osca2_labeled.treefile --test Test --reference Reference --output relax_results.json

echo '=== Running Contrast-FEL on osca2 ==='
hyphy contrast-fel --alignment osca2_codon.fasta --tree osca2_labeled.treefile --output contrast_fel_results.json --branch-set Test --branch-set Reference
