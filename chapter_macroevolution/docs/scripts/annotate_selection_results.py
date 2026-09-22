#!/usr/bin/env python3
"""
Annotate Genome-Wide Ka/Ks Selection Results with Functional Descriptions (eggNOG, Pfam)
and Perform Functional Profiling of Positive Selection Candidates (omega > 1.0).

Chapter: Macroevolution and Genomics in Velloziaceae
"""

import os
import sys
import glob
import re
from collections import Counter

def parse_tsv(filepath):
    with open(filepath, 'r') as f:
        lines = [line.strip().split('\t') for line in f if line.strip()]
    return lines

def main():
    base_dir = "/home/mfcaval/github/doutorado/chapter_macroevolution"
    sel_file = os.path.join(base_dir, "05_selection", "vellozia_pairwise_kaks_1to1.tsv")
    of_dir = os.path.join(base_dir, "01_orthology", "results", "Results_Aug30", "Orthogroups", "Orthogroups.tsv")
    
    vtub_annot_file = "/home/mfcaval/github/doutorado/data/genomes/Vtub/vtub_master_annotation.tsv"
    vper_annot_file = "/home/mfcaval/github/doutorado/data/genomes/Vper/vper_master_annotation.tsv"
    
    print("[INFO] Loading OrthoFinder Orthogroups...")
    og_rows = parse_tsv(of_dir)
    og_header = og_rows[0]
    
    # Identify column indices
    col_idx = {}
    for i, col in enumerate(og_header):
        clean_name = col.replace(".pep.fa", "").replace(".pep", "").replace(".fa", "").replace(".fasta", "")
        col_idx[clean_name] = i
        
    og_to_genes = {}
    for row in og_rows[1:]:
        og_id = row[0]
        def get_col(sp):
            idx = col_idx.get(sp)
            if idx is not None and idx < len(row):
                return row[idx]
            return ""
            
        og_to_genes[og_id] = {
            "Vtub": get_col("Vtub"),
            "Vper": get_col("Vper"),
            "Ath": get_col("Ath"),
            "Xvis": get_col("Xvis")
        }
        
    print("[INFO] Loading Functional Annotations...")
    annot_dict = {}
    for annot_path in [vtub_annot_file, vper_annot_file]:
        if os.path.exists(annot_path):
            rows = parse_tsv(annot_path)
            header = rows[0]
            g_idx = header.index("gene_id") if "gene_id" in header else 1
            desc_idx = header.index("eggnog_desc") if "eggnog_desc" in header else 8
            for r in rows[1:]:
                if len(r) > max(g_idx, desc_idx):
                    gid = r[g_idx]
                    desc = r[desc_idx]
                    if desc and desc != "None":
                        annot_dict[gid] = desc
                        annot_dict[gid + ".t1"] = desc
                        # also strip prefix if needed
                        short_id = re.sub(r"\.t\d+", "", gid)
                        annot_dict[short_id] = desc
                        
    print("[INFO] Annotating Ka/Ks Results...")
    sel_rows = parse_tsv(sel_file)
    sel_header = sel_rows[0]
    
    annotated_results = []
    pos_selection_list = []
    
    for row in sel_rows[1:]:
        og_id = row[0]
        codons = row[1]
        dn = row[2]
        ds = row[3]
        omega = float(row[4])
        regime = row[5]
        
        genes = og_to_genes.get(og_id, {})
        vtub_id = genes.get("Vtub", "")
        vper_id = genes.get("Vper", "")
        ath_id = genes.get("Ath", "")
        
        # Get description from Vtub or Vper
        desc = annot_dict.get(vtub_id, annot_dict.get(vper_id, "Uncharacterized protein"))
        if not desc or desc == "None":
            desc = "Uncharacterized protein"
            
        annotated_results.append((og_id, vtub_id, vper_id, ath_id, codons, dn, ds, f"{omega:.4f}", regime, desc))
        
        if regime == "Positive_Selection":
            pos_selection_list.append((og_id, vtub_id, vper_id, ath_id, codons, dn, ds, f"{omega:.4f}", desc))
            
    # Write full annotated table
    out_all = os.path.join(base_dir, "05_selection", "vellozia_pairwise_kaks_annotated.tsv")
    with open(out_all, 'w') as f:
        f.write("Orthogroup\tVtub_Gene\tVper_Gene\tAth_Gene\tCodons\tKa_dN\tKs_dS\tOmega_KaKs\tSelection_Regime\tFunctional_Description\n")
        for r in annotated_results:
            f.write("\t".join(r) + "\n")
            
    # Write positive selection top candidates table
    pos_selection_list.sort(key=lambda x: float(x[7]), reverse=True)
    out_pos = os.path.join(base_dir, "05_selection", "positive_selection_candidates_top250.tsv")
    with open(out_pos, 'w') as f:
        f.write("Orthogroup\tVtub_Gene\tVper_Gene\tAth_Gene\tCodons\tKa_dN\tKs_dS\tOmega_KaKs\tFunctional_Description\n")
        for r in pos_selection_list:
            f.write("\t".join(r) + "\n")
            
    print(f"[INFO] Master annotated table saved: {out_all}")
    print(f"[INFO] Top positive selection table saved: {out_pos} ({len(pos_selection_list)} genes)")
    
    # Keyword Frequency Analysis among Positive Selection genes
    words = []
    stop_words = {"protein", "family", "domain", "belongs", "the", "to", "and", "of", "in", "like", "uncharacterized", "containing", "type", "with", "subunit", "putative", "binding", "involved"}
    for r in pos_selection_list:
        desc = r[8].lower()
        clean_words = re.findall(r"[a-z0-9\-]+", desc)
        for w in clean_words:
            if len(w) > 3 and w not in stop_words:
                words.append(w)
                
    counts = Counter(words).most_common(25)
    print("\n" + "="*70)
    print(" TOP FUNCTIONAL KEYWORDS ENRICHED IN POSITIVE SELECTION (omega > 1.0)")
    print("="*70)
    for word, cnt in counts:
        print(f"  - {word.capitalize():<25} : {cnt} genes")
    print("="*70)

if __name__ == "__main__":
    main()
