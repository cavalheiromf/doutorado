#!/usr/bin/env python3
"""
Parse MCMCtree FigTree output to a clean chronogram.
Chapter: Macroevolution and Genomics in Velloziaceae
"""

import os
import re

def main():
    base_dir = "/home/mfcaval/github/doutorado/chapter_macroevolution"
    mcmc_dir = os.path.join(base_dir, "03_dating")
    figtree_file = os.path.join(mcmc_dir, "FigTree.tre")
    output_tree = os.path.join(mcmc_dir, "velloziaceae_chronogram.tre")

    if not os.path.exists(figtree_file):
        print(f"[ERROR] FigTree.tre not found in {mcmc_dir}")
        return

    with open(figtree_file, "r") as f:
        content = f.read()

    # MCMCtree FigTree.tre output contains multiple blocks.
    # The actual calibrated tree is the last string before the end.
    tree_matches = re.findall(r"tree TREE1 = (.+?;)", content)
    
    if not tree_matches:
        print("[ERROR] Could not parse tree string from FigTree.tre")
        return
        
    final_tree = tree_matches[-1]
    
    with open(output_tree, "w") as f:
        f.write(final_tree + "\n")
        
    print(f"[INFO] Parsed chronogram saved to {output_tree}")

if __name__ == "__main__":
    main()
