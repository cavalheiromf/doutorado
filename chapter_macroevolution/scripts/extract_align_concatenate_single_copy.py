#!/usr/bin/env python3
"""
Extract, Align with MAFFT, Trim, and Concatenate 1:1 Single-Copy Orthologs.
Chapter: Macroevolution and Genomics in Velloziaceae
"""

import os
import sys
import glob
import subprocess
import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed

SPECIES_ORDER = ["Ath", "Dala", "Ptec", "Abra", "Xvis", "Vper", "Vtub"]

def parse_fasta(filepath):
    records = []
    current_id, current_seq = None, []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_id:
                    records.append((current_id, "".join(current_seq)))
                current_id = line[1:].split()[0]
                current_seq = []
            else:
                current_seq.append(line)
        if current_id:
            records.append((current_id, "".join(current_seq)))
    return records

def write_fasta(records, filepath):
    with open(filepath, 'w') as f:
        for h, s in records:
            f.write(f">{h}\n{s}\n")

def get_species_prefix(seq_id):
    # Map headers back to species names based on prefixes
    if seq_id.startswith("AT") or seq_id.startswith("NP_") or "NC_" in seq_id or "Ath" in seq_id: return "Ath"
    if seq_id.startswith("KAH") or "Dala" in seq_id: return "Dala"
    if seq_id.startswith("Vtub"): return "Vtub"
    if seq_id.startswith("Vper"): return "Vper"
    if seq_id.startswith("Abr") or seq_id.startswith("CM"): return "Abra"
    if seq_id.startswith("Ptec") or seq_id.startswith("ha"): return "Ptec"
    if seq_id.startswith("Xvis") or seq_id.startswith("MP"): return "Xvis"
    
    # Fallback checking against expected list
    for sp in SPECIES_ORDER:
        if seq_id.startswith(sp):
            return sp
    return seq_id

def trim_alignment_columns(records, max_gap_fraction=0.5):
    if not records: return []
    num_seqs = len(records)
    aln_len = len(records[0][1])
    keep_cols = []
    
    for i in range(aln_len):
        gap_count = sum(1 for _, seq in records if seq[i] == '-')
        if (gap_count / num_seqs) <= max_gap_fraction:
            keep_cols.append(i)
            
    trimmed_records = []
    for h, seq in records:
        trimmed_seq = "".join(seq[i] for i in keep_cols)
        trimmed_records.append((h, trimmed_seq))
        
    return trimmed_records

def align_and_process_og(args):
    og_file, raw_out_dir, trim_out_dir, mafft_bin, max_gap_fraction = args
    og_id = os.path.basename(og_file).replace(".fa", "").replace(".fasta", "")
    
    records = parse_fasta(og_file)
    renamed_records = []
    
    for h, seq in records:
        sp = get_species_prefix(h)
        renamed_records.append((sp, seq))
        
    unaligned_tmp = os.path.join(raw_out_dir, f"{og_id}_unaligned.fa")
    aligned_fa = os.path.join(raw_out_dir, f"{og_id}_aligned.fa")
    trimmed_fa = os.path.join(trim_out_dir, f"{og_id}_trimmed.fa")
    
    write_fasta(renamed_records, unaligned_tmp)
    
    try:
        cmd = [mafft_bin, "--auto", "--quiet", unaligned_tmp]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        with open(aligned_fa, "w") as out:
            out.write(result.stdout)
    except Exception as e:
        print(f"[WARN] MAFFT failed for {og_id}: {e}")
        return None
    finally:
        if os.path.exists(unaligned_tmp):
            os.remove(unaligned_tmp)
            
    aligned_records = parse_fasta(aligned_fa)
    trimmed_records = trim_alignment_columns(aligned_records, max_gap_fraction=max_gap_fraction)
    
    if not trimmed_records or len(trimmed_records[0][1]) == 0:
        trimmed_records = aligned_records
        
    write_fasta(trimmed_records, trimmed_fa)
    
    aln_len_raw = len(aligned_records[0][1]) if aligned_records else 0
    aln_len_trim = len(trimmed_records[0][1]) if trimmed_records else 0
    
    seq_dict = {h: seq for h, seq in trimmed_records}
    return (og_id, aln_len_raw, aln_len_trim, seq_dict)

def main():
    parser = argparse.ArgumentParser(description="Extract, align with MAFFT, trim, and concatenate 1:1 orthologs.")
    parser.add_argument("--threads", "-t", type=int, default=8)
    parser.add_argument("--mafft", type=str, default="mafft")
    parser.add_argument("--max-gap", type=float, default=0.5)
    args = parser.parse_args()

    base_dir = "/home/mfcaval/github/doutorado/chapter_macroevolution"
    of_dir = os.path.join(base_dir, "01_orthology")
    phylo_dir = os.path.join(base_dir, "02_phylogenomics")
    
    gene_aln_dir = os.path.join(phylo_dir, "gene_alignments")
    trim_aln_dir = os.path.join(phylo_dir, "trimmed_alignments")
    
    os.makedirs(gene_aln_dir, exist_ok=True)
    os.makedirs(trim_aln_dir, exist_ok=True)
    
    # Locate Single_Copy_Orthologue_Sequences in latest OrthoFinder results
    search_path = os.path.join(of_dir, "results", "Results_*", "Single_Copy_Orthologue_Sequences")
    sc_dirs = glob.glob(search_path)
    if not sc_dirs:
        print(f"[ERROR] Could not locate Single_Copy_Orthologue_Sequences in {of_dir}")
        sys.exit(1)
        
    sc_dir = sorted(sc_dirs)[-1] # Use the most recent if multiple
    og_files = sorted(glob.glob(os.path.join(sc_dir, "OG*.fa")))
    print(f"[INFO] Found {len(og_files)} single-copy orthogroup FASTA files in {sc_dir}")
    
    tasks = [(f, gene_aln_dir, trim_aln_dir, args.mafft, args.max_gap) for f in og_files]
    
    processed_results = []
    with ProcessPoolExecutor(max_workers=args.threads) as executor:
        futures = {executor.submit(align_and_process_og, task): task[0] for task in tasks}
        completed_count = 0
        for future in as_completed(futures):
            res = future.result()
            if res is not None:
                processed_results.append(res)
            completed_count += 1
            if completed_count % 200 == 0 or completed_count == len(og_files):
                print(f"[INFO] Processed {completed_count}/{len(og_files)} orthogroups...")
                
    processed_results.sort(key=lambda x: x[0])
    
    supermatrix = {sp: [] for sp in SPECIES_ORDER}
    partitions = []
    stats = []
    current_pos = 1
    
    for og_id, raw_len, trim_len, seq_dict in processed_results:
        for sp in SPECIES_ORDER:
            seq = seq_dict.get(sp, "-" * trim_len)
            supermatrix[sp].append(seq)
            
        start_pos = current_pos
        end_pos = current_pos + trim_len - 1
        partitions.append((og_id, start_pos, end_pos, trim_len))
        stats.append(f"{og_id}\t{raw_len}\t{trim_len}\t{start_pos}\t{end_pos}")
        current_pos = end_pos + 1
        
    total_sites = current_pos - 1
    
    fasta_out = os.path.join(phylo_dir, "pan_velloziaceae_supermatrix.fa")
    with open(fasta_out, "w") as f:
        for sp in SPECIES_ORDER:
            f.write(f">{sp}\n{''.join(supermatrix[sp])}\n")
            
    part_nexus = os.path.join(phylo_dir, "partitions.nexus")
    with open(part_nexus, "w") as f:
        f.write("#NEXUS\nbegin sets;\n")
        for og_id, s, e, _ in partitions:
            f.write(f"    charset {og_id} = {s}-{e};\n")
        f.write("end;\n")
        
    print("[INFO] Assembly Complete!")
    print(f" Total Loci:    {len(processed_results)}")
    print(f" Total Sites:   {total_sites:,} AA")

if __name__ == "__main__":
    main()
