#!/usr/bin/env python3
"""
Prepare Codon Alignments for HyPhy
Chapter: Macroevolution and Genomics in Velloziaceae

Reads individual gene protein alignments from 02_phylogenomics/trimmed_alignments/
and threads the raw CDS sequences over them to generate codon alignments.
"""

import os
import glob
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed

def parse_fasta(filepath):
    records = {}
    current_id, current_seq = None, []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_id:
                    records[current_id] = "".join(current_seq)
                current_id = line[1:].split()[0]
                current_seq = []
            else:
                current_seq.append(line)
        if current_id:
            records[current_id] = "".join(current_seq)
    return records

def thread_cds(prot_aln, cds_unaligned):
    """Threads a CDS sequence onto a gapped protein alignment."""
    codon_aln = []
    cds_idx = 0
    for aa in prot_aln:
        if aa == '-':
            codon_aln.append('---')
        elif aa == 'X':
            # If we translated 'X', we just grab the 3 bases (which might contain Ns)
            codon = cds_unaligned[cds_idx:cds_idx+3]
            codon_aln.append(codon if len(codon) == 3 else '---')
            cds_idx += 3
        else:
            codon = cds_unaligned[cds_idx:cds_idx+3]
            codon_aln.append(codon if len(codon) == 3 else '---')
            cds_idx += 3
    return "".join(codon_aln)

def main():
    base_dir = "/home/mfcaval/github/doutorado/chapter_macroevolution"
    phylo_dir = os.path.join(base_dir, "02_phylogenomics")
    hyphy_dir = os.path.join(base_dir, "05_selection")
    codon_dir = os.path.join(hyphy_dir, "codon_alignments")
    
    os.makedirs(codon_dir, exist_ok=True)
    
    prot_aln_dir = os.path.join(phylo_dir, "trimmed_alignments")
    
    # Needs the raw CDS dictionaries
    # Wait, the protein alignments use SPECIES IDs (Ath, Dala, Vper) thanks to my extract script!
    # But the raw CDS files have original IDs. 
    # Actually, if we just use the SAME dictionary loading logic as before, we can map them.
    # However, to be perfectly robust, the CDS FASTA needs to be queried.
    # Let's save this logic for when the IQ-TREE matrix is actually built so we can read the EXACT seq IDs.
    
    print("Codon alignment script skeleton created. We will finalize this after OrthoFinder finishes and we have the exact orthogroup list.")

if __name__ == "__main__":
    main()
