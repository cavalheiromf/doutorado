#!/usr/bin/env python3
"""
Format OrthoFinder Orthogroups.GeneCount.tsv for CAFE5 Analysis.
Filters out orthogroups with extreme copy numbers (>= 100)
to ensure robust error modeling and accurate lambda parameter convergence.

Chapter: Macroevolution and Genomics in Velloziaceae
"""

import os
import sys
import glob

def parse_tsv(filepath):
    with open(filepath, 'r') as f:
        lines = [line.strip().split('\t') for line in f if line.strip()]
    return lines

def main():
    base_dir = "/home/mfcaval/github/doutorado/chapter_macroevolution"
    of_dir = os.path.join(base_dir, "01_orthology")
    cafe_dir = os.path.join(base_dir, "04_gene_families")
    os.makedirs(cafe_dir, exist_ok=True)
    
    # Locate Orthogroups.GeneCount.tsv
    search_path = os.path.join(of_dir, "results", "Results_*", "Orthogroups", "Orthogroups.GeneCount.tsv")
    gc_files = glob.glob(search_path)
    if not gc_files:
        print(f"[ERROR] Could not find Orthogroups.GeneCount.tsv in {of_dir}")
        sys.exit(1)
        
    gc_file = sorted(gc_files)[-1]
    print(f"[INFO] Reading OrthoFinder counts from: {gc_file}")
    
    rows = parse_tsv(gc_file)
    header = rows[0]
    
    # Identify column indices
    og_idx = 0
    # Clean species names (e.g. Ath.pep -> Ath)
    species_indices = []
    clean_header = []
    for i, col in enumerate(header):
        if col in ["Orthogroup", "Total"]:
            continue
        clean_name = col.replace(".pep", "").replace(".fa", "").replace(".fasta", "")
        species_indices.append((i, clean_name))
        
    out_filtered = os.path.join(cafe_dir, "cafe_family_input.tsv")
    out_full = os.path.join(cafe_dir, "cafe_family_input_full.tsv")
    
    kept_count = 0
    total_count = 0
    
    with open(out_filtered, 'w') as f_filt, open(out_full, 'w') as f_full:
        # Write Header: Desc \t FamilyID \t Sp1 \t Sp2 ...
        header_str = "Desc\tFamilyID\t" + "\t".join([sp for _, sp in species_indices]) + "\n"
        f_filt.write(header_str)
        f_full.write(header_str)
        
        for row in rows[1:]:
            total_count += 1
            og_id = row[og_idx]
            counts = [int(row[idx]) for idx, _ in species_indices]
            
            line_str = f"{og_id}\t{og_id}\t" + "\t".join(map(str, counts)) + "\n"
            f_full.write(line_str)
            
            # Filter < 100 copies
            if max(counts) < 100:
                f_filt.write(line_str)
                kept_count += 1
                
    print(f"[INFO] Saved full unfiltered CAFE input: {out_full} ({total_count} families)")
    print(f"[INFO] Saved filtered CAFE input (<100 copies): {out_filtered} ({kept_count} families)")
    print(f"[INFO] Excluded {total_count - kept_count} families with >= 100 copies.")

if __name__ == "__main__":
    main()
