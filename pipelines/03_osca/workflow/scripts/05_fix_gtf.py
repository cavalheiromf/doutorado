#!/usr/bin/env python3
"""
GTF Fixer for Vellozia projects.
Adds missing `gene_id` attribute to 'exon' and 'CDS' features in a GTF file
by copying the value of their `transcript_id`.
"""

import sys
import re
from pathlib import Path

def patch_gtf(input_file, output_file):
    input_path = Path(input_file)
    output_path = Path(output_file)
    
    print(f"🛠️  Patching GTF: {input_path} -> {output_path}")
    
    if not input_path.exists():
        print(f"❌ Error: Input file {input_path} does not exist!")
        sys.exit(1)
        
    # Write to a temporary file first for safety
    temp_path = output_path.with_suffix(".tmp_patch")
    
    count_patched = 0
    total_lines = 0
    
    with open(input_path, "r") as f_in, open(temp_path, "w") as f_out:
        for line in f_in:
            total_lines += 1
            if line.startswith("#"):
                f_out.write(line)
                continue
            
            parts = line.strip().split("\t")
            if len(parts) < 9:
                f_out.write(line)
                continue
                
            feature_type = parts[2]
            attributes = parts[8]
            
            # Patch features like 'exon' or 'CDS' that have transcript_id but lack gene_id
            if feature_type in ["exon", "CDS"] and "gene_id" not in attributes:
                match = re.search(r'transcript_id "([^"]+)";', attributes)
                if match:
                    tx_id = match.group(1)
                    # Append gene_id matching the transcript_id
                    attrs_stripped = attributes.rstrip()
                    if not attrs_stripped.endswith(";"):
                        attrs_stripped += ";"
                    new_attributes = f'{attrs_stripped} gene_id "{tx_id}";\n'
                    parts[8] = new_attributes
                    f_out.write("\t".join(parts))
                    count_patched += 1
                    continue
            
            f_out.write(line)
            
    # Safely replace target with temp file
    if temp_path.exists():
        temp_path.replace(output_path)
        
    print(f"✅ Done! Patched {count_patched} lines out of {total_lines} total lines.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fix_gtf.py <input_gtf> [output_gtf]")
        sys.exit(1)
        
    in_file = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else in_file
    
    patch_gtf(in_file, out_file)
