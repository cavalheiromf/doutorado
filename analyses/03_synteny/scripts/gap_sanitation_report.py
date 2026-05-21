#!/usr/bin/env python3
"""
Scientific Gap Sanitation Audit for OSCA Gene Contrast-FEL Divergent Sites.
Calculates gap frequencies in the global alignment for significant sites 
to identify potential alignment-driven false positives.
"""

import os
import json
from Bio import AlignIO

# Define paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYNTENY_DIR = os.path.dirname(SCRIPT_DIR)
RESULTS_JSON = os.path.join(SYNTENY_DIR, "hyphy_analysis", "contrast_fel_results.json")
CODON_FASTA = os.path.join(SYNTENY_DIR, "hyphy_analysis", "vellozia_oscas_codon.fasta")

def main():
    print("=== GAP SANITATION AUDIT REPORT (SANEAMENTO DE GAPS) ===")
    
    if not os.path.exists(RESULTS_JSON):
        print(f"Error: Contrast-FEL results not found at {RESULTS_JSON}")
        return
        
    if not os.path.exists(CODON_FASTA):
        print(f"Error: Codon alignment not found at {CODON_FASTA}")
        return

    # 1. Parse Contrast-FEL JSON and extract significant sites
    with open(RESULTS_JSON, 'r') as f:
        data = json.load(f)

    if 'MLE' not in data:
        print("Error: 'MLE' section not found in JSON results.")
        return
        
    mle = data['MLE']
    headers = [h[0] for h in mle['headers']]
    content = mle['content']
    
    p_idx = -1
    for i, h in enumerate(headers):
        if 'p-value' in h.lower():
            p_idx = i
            break
            
    if p_idx == -1:
        print("Error: Could not identify P-value column in MLE headers.")
        return
        
    sig_sites = []
    
    # Process partitions (usually key '0' for global)
    if isinstance(content, dict):
        for partition, sites_data in content.items():
            if isinstance(sites_data, list):
                for s_idx, row in enumerate(sites_data):
                    pval = row[p_idx]
                    if pval is not None and pval <= 0.05:
                        sig_sites.append((s_idx + 1, pval, row))
    elif isinstance(content, list):
        for s_idx, row in enumerate(content):
            pval = row[p_idx]
            if pval is not None and pval <= 0.05:
                sig_sites.append((s_idx + 1, pval, row))

    print(f"Identified {len(sig_sites)} significant divergent sites (p <= 0.05).")

    # 2. Parse Codon Alignment and calculate gap fractions
    alignment = AlignIO.read(CODON_FASTA, "fasta")
    num_seqs = len(alignment)
    alignment_len = alignment.get_alignment_length()
    
    gap_fractions = []
    for i in range(alignment_len // 3):
        gap_count = 0
        for seq in alignment:
            codon = str(seq.seq[3*i:3*i+3])
            if '-' in codon or 'N' in codon:
                gap_count += 1
        gap_fractions.append(gap_count / num_seqs)

    # 3. Print report
    print("\n" + "="*80)
    print(f"{'Site':6s} | {'p-value':8s} | {'beta_Ref':8s} | {'beta_Test':9s} | {'Gap %':8s} | {'Status'}")
    print("="*80)
    
    warnings_count = 0
    for s, pval, row in sorted(sig_sites, key=lambda x: x[0]):
        if s <= len(gap_fractions):
            gap_pct = gap_fractions[s - 1] * 100
            if gap_pct >= 20.0:
                status = "WARNING (GAP-RICH / HYPERVARIABLE)"
                warnings_count += 1
            else:
                status = "SAFE"
                
            print(f"{s:6d} | {pval:8.4f} | {row[1]:8.3f} | {row[2]:9.3f} | {gap_pct:7.2f}% | {status}")
        else:
            print(f"{s:6d} | Out of bounds")
            
    print("="*80)
    print(f"Summary: {len(sig_sites) - warnings_count} safe sites, {warnings_count} gap-rich sites under warning.")
    print("="*80)

if __name__ == "__main__":
    main()
