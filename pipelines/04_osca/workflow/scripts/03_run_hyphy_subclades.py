#!/usr/bin/env python3
"""
Scientific pipeline to automate sub-family (clade-level) codon alignments,
phylogenetic tree pruning, and HyPhy RELAX/Contrast-FEL configuration.

This script:
1. Groups the 27 OSCA genes into OSCA1, OSCA2, and OSCA3+4 subfamilies.
2. Extracts raw, unaligned CDS sequences for each subfamily.
3. Translates CDS to proteins, stripping trailing stop codons to avoid HyPhy errors.
4. Performs local protein alignments using MUSCLE.
5. Threads CDS back onto aligned proteins (PAL2NAL equivalent) to generate localized codon alignments.
6. Prunes the global guide tree (iqtree.treefile) to only keep the leaves of each subfamily.
7. Labels leaves programmatically with {Test} (Vtub) and {Reference} (Vper).
8. Generates directory structures and execution scripts for each subclade.
"""

import os
import sys
import re
import io
import subprocess
from Bio import Phylo
from Bio.Seq import Seq

# Define absolute paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYNTENY_DIR = os.path.dirname(SCRIPT_DIR)
PROJECT_DIR = os.path.dirname(os.path.dirname(SYNTENY_DIR))

OSCA_IDS_FILE = os.path.join(PROJECT_DIR, "analyses", "01_gene_identification", "results", "oscasIDs.txt")
VPER_CDS = os.path.join(SYNTENY_DIR, "data", "Vper.cds")
VTUB_CDS = os.path.join(SYNTENY_DIR, "data", "Vtub.cds")
GLOBAL_TREE = os.path.join(PROJECT_DIR, "analyses", "02_phylogeny", "results", "iqtree.treefile")
MUSCLE_EXE = "/home/mfcaval/.local/share/mamba/envs/jcviEnv/bin/muscle"
SUBCLADES_DIR = os.path.join(SYNTENY_DIR, "hyphy_subclades")

def read_fasta(fasta_path):
    """Simple parser to read FASTA sequences into a dict."""
    seqs = {}
    current_id = None
    current_seq = []
    
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

def read_osca_mappings():
    """Reads oscasIDs.txt and classifies genes into subfamilies."""
    mappings = []
    if not os.path.exists(OSCA_IDS_FILE):
        print(f"Error: OSCA ID mapping file not found at {OSCA_IDS_FILE}")
        sys.exit(1)
        
    with open(OSCA_IDS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) >= 2:
                gene_id = parts[0]
                mapped_name = parts[1]
                
                # Classify based on mapped name
                if "OSCA1" in mapped_name:
                    clade = "osca1"
                elif "OSCA2" in mapped_name:
                    clade = "osca2"
                elif "OSCA3" in mapped_name or "OSCA4" in mapped_name:
                    clade = "osca3_4"
                else:
                    clade = "unknown"
                    
                mappings.append({
                    "gene_id": gene_id,
                    "name": mapped_name,
                    "clade": clade
                })
    return mappings

def translate_cds(cds_seq):
    """
    Translates CDS sequence to protein sequence and handles reading frames 
    and stop codons to prevent HyPhy compilation crashes.
    """
    # Enforce multiple of 3 length
    if len(cds_seq) % 3 != 0:
        cds_seq = cds_seq[:(len(cds_seq) // 3) * 3]
        
    pep_seq = str(Seq(cds_seq).translate())
    
    # If protein ends in a stop codon (*), strip it from both protein and CDS
    if pep_seq.endswith("*"):
        pep_seq = pep_seq[:-1]
        cds_seq = cds_seq[:-3]
        
    # Check for internal stop codons (indicative of pseudogenes or frame issues)
    if "*" in pep_seq:
        print("Warning: Internal stop codon found! Sequence might contain a pseudogene or frameshift.")
        
    return pep_seq, cds_seq

def thread_codon_alignment(pep_aligned, cds_unaligned):
    """Threads CDS sequences onto an aligned protein sequence template."""
    codon_aligned = {}
    for header, pep_seq in pep_aligned.items():
        if header not in cds_unaligned:
            print(f"Warning: CDS for {header} not found, skipping codon thread.")
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
                    codon = codon.ljust(3, "-")
                codon_seq.append(codon)
                cds_idx += 3
                
        codon_aligned[header] = "".join(codon_seq)
    return codon_aligned

def label_newick_tree(tree_content):
    """Adds {Test} and {Reference} annotations to leaves for HyPhy relax/contrast-fel."""
    def replace_vt(match):
        node = match.group(1)
        return f"{node}{{Test}}"
        
    def replace_vp(match):
        node = match.group(1)
        return f"{node}{{Reference}}"
        
    labeled = re.sub(r"(Vtub_[a-zA-Z0-9_\-]+)", replace_vt, tree_content)
    labeled = re.sub(r"(Vper_[a-zA-Z0-9_\-]+)", replace_vp, labeled)
    return labeled

def process_subclade(clade_name, clade_genes, cds_dict):
    """Main execution block to align, thread, prune and output files for a single clade."""
    print(f"\n>>> PROCESSING CLADE: {clade_name.upper()} ({len(clade_genes)} genes) <<<")
    
    clade_dir = os.path.join(SUBCLADES_DIR, clade_name)
    os.makedirs(clade_dir, exist_ok=True)
    
    # 1. Translate and clean CDS
    pep_unaligned = {}
    cds_cleaned = {}
    for gene_id in clade_genes:
        if gene_id not in cds_dict:
            print(f"Warning: Gene {gene_id} not found in CDS databases!")
            continue
        raw_cds = cds_dict[gene_id]
        pep, clean_cds = translate_cds(raw_cds)
        pep_unaligned[gene_id] = pep
        cds_cleaned[gene_id] = clean_cds
        
    # Write unaligned proteins to file
    pep_unaligned_path = os.path.join(clade_dir, f"{clade_name}_pep_unaligned.fasta")
    with open(pep_unaligned_path, "w") as f:
        for gene_id, seq in pep_unaligned.items():
            f.write(f">{gene_id}\n{seq}\n")
            
    # 2. Align proteins using MUSCLE
    pep_aligned_path = os.path.join(clade_dir, f"{clade_name}_pep_aligned.fasta")
    print(f"Running MUSCLE alignment for {clade_name} proteins...")
    cmd = [MUSCLE_EXE, "-in", pep_unaligned_path, "-out", pep_aligned_path]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Protein alignment completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running MUSCLE: {e.stderr.decode()}")
        sys.exit(1)
        
    # Read aligned proteins
    pep_aligned = read_fasta(pep_aligned_path)
    
    # 3. Thread Codons
    print("Threading codons onto protein alignment...")
    codon_aligned = thread_codon_alignment(pep_aligned, cds_cleaned)
    
    # Save sanitized codon alignment (replace '.' with '_')
    codon_out_path = os.path.join(clade_dir, f"{clade_name}_codon.fasta")
    with open(codon_out_path, "w") as f:
        for gene_id, seq in codon_aligned.items():
            sanitized_id = gene_id.replace(".", "_")
            f.write(f">{sanitized_id}\n{seq}\n")
    print(f"Codon alignment written to: {codon_out_path}")
    
    # 4. Prune Guide Tree
    print("Pruning phylogenetic guide tree...")
    if os.path.exists(GLOBAL_TREE):
        tree = Phylo.read(GLOBAL_TREE, "newick")
        all_leaves = [leaf.name for leaf in tree.get_terminals()]
        clade_set = set(clade_genes)
        
        # Prune leaves that do not belong to this clade
        for leaf_name in all_leaves:
            if leaf_name not in clade_set:
                tree.prune(leaf_name)
                
        # Validate leaf count matches clade gene count
        pruned_leaves = [leaf.name for leaf in tree.get_terminals()]
        print(f"Original leaves: {len(all_leaves)} | Pruned leaves remaining: {len(pruned_leaves)}")
        
        # Sanitize names in the tree (replace '.' with '_')
        for leaf in tree.get_terminals():
            leaf.name = leaf.name.replace(".", "_")
            
        # Output Newick Newick string
        out_buf = io.StringIO()
        Phylo.write(tree, out_buf, "newick")
        tree_str = out_buf.getvalue().strip()
        
        # Label leaves for HyPhy
        labeled_tree_str = label_newick_tree(tree_str)
        
        tree_out_path = os.path.join(clade_dir, f"{clade_name}_labeled.treefile")
        with open(tree_out_path, "w") as f:
            f.write(labeled_tree_str)
        print(f"Sanitized and labeled tree written to: {tree_out_path}")
    else:
        print(f"Error: Global tree file not found at {GLOBAL_TREE}!")
        sys.exit(1)
        
    # 5. Generate local HyPhy execution script
    sh_script_path = os.path.join(clade_dir, "run_hyphy.sh")
    with open(sh_script_path, "w") as f:
        f.write(f"#!/bin/bash\n")
        f.write(f"# Local run script for clade {clade_name.upper()}\n\n")
        f.write(f"echo '=== Running RELAX on {clade_name} ==='\n")
        f.write(f"hyphy relax --alignment {clade_name}_codon.fasta --tree {clade_name}_labeled.treefile --test Test --reference Reference --output relax_results.json\n\n")
        f.write(f"echo '=== Running Contrast-FEL on {clade_name} ==='\n")
        f.write(f"hyphy contrast-fel --alignment {clade_name}_codon.fasta --tree {clade_name}_labeled.treefile --output contrast_fel_results.json --branch-set Test --branch-set Reference\n")
    os.chmod(sh_script_path, 0o755)
    print(f"Execution script generated: {sh_script_path}")

def main():
    print("================================================================================")
    print("            SUB-FAMILY HYPHY SELECTION PIPELINE GENERATOR                       ")
    print("================================================================================")
    
    # 1. Load mappings and CDS
    mappings = read_osca_mappings()
    print(f"Loaded {len(mappings)} OSCA gene mappings.")
    
    print("Loading Vper and Vtub CDS sequences...")
    vper_cds_dict = read_fasta(VPER_CDS)
    vtub_cds_dict = read_fasta(VTUB_CDS)
    combined_cds = {**vper_cds_dict, **vtub_cds_dict}
    print(f"Loaded {len(combined_cds)} CDS sequences total.")
    
    # Group genes by clade
    clades = {"osca1": [], "osca2": [], "osca3_4": []}
    for m in mappings:
        clade = m["clade"]
        if clade in clades:
            clades[clade].append(m["gene_id"])
            
    # Process each clade
    for clade_name, clade_genes in clades.items():
        if clade_genes:
            process_subclade(clade_name, clade_genes, combined_cds)
            
    print("\n" + "="*80)
    print("            ALL SUB-CLADE PREPARATIONS COMPLETED SUCCESSFULLY!                 ")
    print("="*80)

if __name__ == "__main__":
    main()
