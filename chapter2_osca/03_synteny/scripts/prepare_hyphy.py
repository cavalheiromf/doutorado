#!/usr/bin/env python3
"""
Automation script to prepare files and pipeline commands for HyPhy analyses 
(RELAX and Contrast-FEL) comparing Vellozia tubiflora (resurrection) 
vs Vellozia peripherica (evergreen) OSCA genes.

Updates:
- Integrates Biopython's Phylo to prune the phylogenetic tree to only contain Vellozia.
- Sanitizes FASTA headers and Newick leaf nodes by replacing '.' with '_' to avoid HyPhy auto-remap issues.
"""

import os
import re
import io
from Bio import Phylo

# Define paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYNTENY_DIR = os.path.dirname(SCRIPT_DIR)
PROJECT_DIR = os.path.dirname(os.path.dirname(SYNTENY_DIR))

OSCA_IDS_FILE = os.path.join(PROJECT_DIR, "analyses", "01_gene_identification", "results", "oscasIDs.txt")
VPER_CDS = os.path.join(SYNTENY_DIR, "data", "Vper.cds")
VTUB_CDS = os.path.join(SYNTENY_DIR, "data", "Vtub.cds")
PROTEIN_ALIGNMENT = os.path.join(PROJECT_DIR, "analyses", "02_phylogeny/results/allOSCAs.aligned.fasta")

HYPHY_OUT_DIR = os.path.join(SYNTENY_DIR, "hyphy_analysis")


def read_osca_ids():
    """Reads OSCA gene IDs and maps them to their respective Vp/Vt names."""
    osca_map = {}
    if not os.path.exists(OSCA_IDS_FILE):
        print(f"Error: {OSCA_IDS_FILE} not found.")
        return osca_map
    with open(OSCA_IDS_FILE, "r") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split("\t")
                if len(parts) >= 2:
                    osca_map[parts[0]] = parts[1]
    return osca_map


def read_fasta(fasta_path):
    """Simple parser to read FASTA sequences into a dict."""
    seqs = {}
    current_id = None
    current_seq = []
    
    # Handle symlinks properly by opening real path
    real_path = os.path.realpath(fasta_path)
    if not os.path.exists(real_path):
        print(f"Warning: FASTA file not found at {fasta_path}")
        return seqs
        
    with open(real_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_id:
                    seqs[current_id] = "".join(current_seq)
                # Extract first word as ID
                current_id = line[1:].split()[0]
                current_seq = []
            else:
                current_seq.append(line)
        if current_id:
            seqs[current_id] = "".join(current_seq)
    return seqs


def thread_codon_alignment(pep_aligned, cds_unaligned):
    """
    Python implementation of pal2nal. Threads unaligned CDS onto 
    aligned protein sequences to construct a perfect codon alignment.
    """
    codon_aligned = {}
    for header, pep_seq in pep_aligned.items():
        if header not in cds_unaligned:
            print(f"Warning: CDS for {header} not found, skipping codon alignment.")
            continue
            
        cds_seq = cds_unaligned[header]
        codon_seq = []
        cds_idx = 0
        
        for aa in pep_seq:
            if aa == "-":
                codon_seq.append("---")
            else:
                codon = cds_seq[cds_idx:cds_idx+3]
                if len(codon) < 3:
                    print(f"Warning: Short codon at end of {header}. Padding.")
                    codon = codon.ljust(3, "-")
                codon_seq.append(codon)
                cds_idx += 3
                
        codon_aligned[header] = "".join(codon_seq)
    return codon_aligned


def label_newick_tree(tree_content):
    """
    Adds branch labels to leaf nodes for HyPhy parsing:
    - Vtub leaf nodes receive {Test}
    - Vper leaf nodes receive {Reference}
    """
    def replace_vt(match):
        node = match.group(1)
        return f"{node}{{Test}}"
        
    def replace_vp(match):
        node = match.group(1)
        return f"{node}{{Reference}}"
        
    # Replace Vtub with {Test}
    labeled = re.sub(r"(Vtub_[a-zA-Z0-9_\-]+)", replace_vt, tree_content)
    # Replace Vper with {Reference}
    labeled = re.sub(r"(Vper_[a-zA-Z0-9_\-]+)", replace_vp, labeled)
    
    return labeled


def main():
    print("=== HYPHY ANALYSIS PREPARATION PIPELINE ===")
    os.makedirs(HYPHY_OUT_DIR, exist_ok=True)
    
    # 1. Load OSCA IDs and sequences
    osca_map = read_osca_ids()
    if not osca_map:
        print("Failed to load OSCA IDs. Aborting.")
        return
        
    print(f"Loaded {len(osca_map)} OSCA gene mappings.")
    
    print("Reading CDS files...")
    vper_cds_dict = read_fasta(VPER_CDS)
    vtub_cds_dict = read_fasta(VTUB_CDS)
    
    # Combine both Vellozia CDS dictionaries
    vellozia_cds = {**vper_cds_dict, **vtub_cds_dict}
    print(f"Loaded {len(vellozia_cds)} Vellozia CDS sequences.")

    # 2. Extract and parse protein alignment
    print("Parsing protein alignments...")
    if not os.path.exists(PROTEIN_ALIGNMENT):
        print(f"Error: Protein alignment not found at {PROTEIN_ALIGNMENT}")
        return
        
    all_pep_align = read_fasta(PROTEIN_ALIGNMENT)
    
    # Filter alignment to include ONLY Vper and Vtub sequences
    vellozia_pep_align = {}
    for header, seq in all_pep_align.items():
        if header.startswith("Vper.") or header.startswith("Vtub."):
            vellozia_pep_align[header] = seq
            
    print(f"Extracted {len(vellozia_pep_align)} Vellozia OSCA aligned protein sequences.")

    # 3. Perform Codon Threading (pal2nal python equivalent)
    print("Threading codon alignment (pal2nal)...")
    codon_aligned = thread_codon_alignment(vellozia_pep_align, vellozia_cds)
    
    # Save the codon alignment with sanitized headers (replace '.' with '_')
    codon_out_path = os.path.join(HYPHY_OUT_DIR, "vellozia_oscas_codon.fasta")
    with open(codon_out_path, "w") as f:
        for header, seq in codon_aligned.items():
            sanitized_header = header.replace(".", "_")
            f.write(f">{sanitized_header}\n{seq}\n")
            
    print(f"Codon alignment (sanitized) successfully written to: {codon_out_path}")

    # 4. Generate the Labeled and Pruned Guide Tree for HyPhy
    print("Preparing and pruning phylogenetic guide tree...")
    tree_in_path = os.path.join(PROJECT_DIR, "analyses", "02_phylogeny", "results", "iqtree.treefile")
    
    if os.path.exists(tree_in_path):
        # Read Newick tree using Biopython Phylo
        tree = Phylo.read(tree_in_path, "newick")
        all_leaves = [leaf.name for leaf in tree.get_terminals()]
        vellozia_names = set(vellozia_pep_align.keys())
        
        # Prune non-Vellozia branches
        print(f"Pruning original tree of {len(all_leaves)} leaves down to {len(vellozia_names)} Vellozia leaves...")
        for leaf_name in all_leaves:
            if leaf_name not in vellozia_names:
                tree.prune(leaf_name)
                
        # Sanitize names in the tree: replace '.' with '_'
        for leaf in tree.get_terminals():
            leaf.name = leaf.name.replace(".", "_")
            
        # Write to Newick string
        out_buf = io.StringIO()
        Phylo.write(tree, out_buf, "newick")
        tree_content = out_buf.getvalue().strip()
        
        # Label leaves for HyPhy
        labeled_tree = label_newick_tree(tree_content)
        
        tree_out_path = os.path.join(HYPHY_OUT_DIR, "vellozia_oscas_labeled.treefile")
        with open(tree_out_path, "w") as f:
            f.write(labeled_tree)
            
        print(f"Labeled phylogenetic tree successfully written to: {tree_out_path}")
    else:
        print("Warning: Original treefile not found. You will need to build the tree manually.")
        tree_out_path = "[treefile]"

    # 5. Output Shell Script Instructions (non-interactive mode)
    sh_script_path = os.path.join(HYPHY_OUT_DIR, "run_hyphy.sh")
    with open(sh_script_path, "w") as f:
        f.write("#!/bin/bash\n")
        f.write("# Script to run HyPhy comparative analyses\n\n")
        f.write("# 1. Run RELAX analysis to test selection relaxation/intensification\n")
        f.write(f"hyphy relax --alignment vellozia_oscas_codon.fasta --tree vellozia_oscas_labeled.treefile --test Test --reference Reference --output relax_results.json\n\n")
        f.write("# 2. Run Contrast-FEL to identify site-specific selective pressures between groups (non-interactive)\n")
        f.write(f"hyphy contrast-fel --alignment vellozia_oscas_codon.fasta --tree vellozia_oscas_labeled.treefile --output contrast_fel_results.json --contrast Test --reference Reference\n")
        
    os.chmod(sh_script_path, 0o755)
    
    print("\n" + "="*60)
    print(" PIPELINE SUCCESSFULLY SET UP! ")
    print("="*60)
    print(f"1. Labeled Tree: {tree_out_path}")
    print(f"2. Codon Alignment: {codon_out_path}")
    print(f"3. Run Script: {sh_script_path}")
    print("\nTo execute the analyses, run:")
    print(f"  cd {HYPHY_OUT_DIR}")
    print("  ./run_hyphy.sh")
    print("="*60)


if __name__ == "__main__":
    main()
