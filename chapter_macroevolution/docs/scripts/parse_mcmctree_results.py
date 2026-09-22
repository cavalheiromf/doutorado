#!/usr/bin/env python3
"""
Parse MCMCtree FigTree output to a clean chronogram (in Millions of Years).
Chapter: Macroevolution and Genomics in Velloziaceae
"""

import os
import re

def main():
    base_dir = "/home/mfcaval/github/doutorado/chapter_macroevolution"
    mcmc_dir = os.path.join(base_dir, "03_dating")
    figtree_file = os.path.join(mcmc_dir, "FigTree.tre")
    out_tree_100ma = os.path.join(mcmc_dir, "velloziaceae_chronogram_100ma.tre")
    out_tree_ma = os.path.join(mcmc_dir, "velloziaceae_chronogram_ma.tre")
    out_summary_tsv = os.path.join(mcmc_dir, "mcmctree_node_ages_summary.tsv")

    if not os.path.exists(figtree_file):
        print(f"[ERROR] FigTree.tre not found in {mcmc_dir}")
        return

    with open(figtree_file, "r") as f:
        content = f.read()

    tree_match = re.search(r"UTREE\s+\d+\s*=\s*(.+?;)", content)
    if not tree_match:
        tree_match = re.search(r"tree\s+\w+\s*=\s*(.+?;)", content)
        
    if not tree_match:
        print("[ERROR] Could not parse tree string from FigTree.tre")
        return
        
    tree_annotated = tree_match.group(1)
    
    # Strip HPD annotations for clean Newick: [&95%HPD={...}]
    clean_tree_100ma = re.sub(r"\s*\[\&95\%HPD=\{[^\}]+\}\]", "", tree_annotated)
    
    with open(out_tree_100ma, "w") as f:
        f.write(clean_tree_100ma + "\n")
        
    # Scale branch lengths from 100 Ma units to Ma (multiply by 100)
    def scale_branch(match):
        val = float(match.group(1)) * 100.0
        return f":{val:.4f}"
        
    clean_tree_ma = re.sub(r":\s*([\d\.]+)", scale_branch, clean_tree_100ma)
    with open(out_tree_ma, "w") as f:
        f.write(clean_tree_ma + "\n")
        
    # Default chronogram pointer
    with open(os.path.join(mcmc_dir, "velloziaceae_chronogram.tre"), "w") as f:
        f.write(clean_tree_ma + "\n")
        
    # Parse Node Ages table from out_posterior.txt
    post_file = os.path.join(mcmc_dir, "out_posterior.txt")
    nodes_data = []
    if os.path.exists(post_file):
        with open(post_file, "r") as f:
            post_txt = f.read()
            
        # Parse table: t_n8 1.3848 ( 1.3017, 1.4515) ( 1.3030, 1.4525)
        lines = post_txt.splitlines()
        for l in lines:
            m = re.search(r"(t_n\d+)\s+([\d\.]+)\s+\(\s*([\d\.]+),\s*([\d\.]+)\)\s+\(\s*([\d\.]+),\s*([\d\.]+)\)", l)
            if m:
                node_name = m.group(1)
                mean_age = float(m.group(2)) * 100.0
                ci_low = float(m.group(3)) * 100.0
                ci_high = float(m.group(4)) * 100.0
                hpd_low = float(m.group(5)) * 100.0
                hpd_high = float(m.group(6)) * 100.0
                nodes_data.append((node_name, mean_age, ci_low, ci_high, hpd_low, hpd_high))
                
    node_desc = {
        "t_n8": "Root (Eudicots vs Monocots)",
        "t_n9": "Monocots Crown (Dioscoreales vs Pandanales)",
        "t_n10": "Pandanales Crown (Pandanaceae vs Velloziaceae)",
        "t_n11": "Velloziaceae Crown (Acanthochlamys vs Core Velloziaceae)",
        "t_n12": "Core Velloziaceae (Xerophyta vs Vellozia) [UNCONSTRAINED]",
        "t_n13": "Vellozia Sister Divergence (V. peripherica vs V. tubiflora)"
    }
    
    with open(out_summary_tsv, "w") as f:
        f.write("Node_ID\tClade_Description\tMean_Age_Ma\tCI95_Lower_Ma\tCI95_Upper_Ma\tHPD95_Lower_Ma\tHPD95_Upper_Ma\n")
        for node_name, mean_age, ci_low, ci_high, hpd_low, hpd_high in nodes_data:
            desc = node_desc.get(node_name, "Internal Node")
            f.write(f"{node_name}\t{desc}\t{mean_age:.2f}\t{ci_low:.2f}\t{ci_high:.2f}\t{hpd_low:.2f}\t{hpd_high:.2f}\n")
            
    print(f"[INFO] Parsed chronogram (100 Ma units) saved to {out_tree_100ma}")
    print(f"[INFO] Parsed chronogram (Ma units) saved to {out_tree_ma}")
    print(f"[INFO] Summary node ages table saved to {out_summary_tsv}")

if __name__ == "__main__":
    main()
