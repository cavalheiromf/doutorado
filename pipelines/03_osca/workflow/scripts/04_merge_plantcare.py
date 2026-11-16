#!/usr/bin/env python3
"""
merge_plantcare.py

Merge overlapping PlantCARE motifs of the same kind for each gene promoter,
emulating bedtools merge behavior.

Generates:
  - Vper_motif_counts_merged.tsv
  - Vtub_motif_counts_merged.tsv
  - Vper_plantcare_merged.tsv
  - Vtub_plantcare_merged.tsv
  - merge_comparison_summary.txt
"""

import os
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(SCRIPT_DIR, "../results")

def load_promoter_names(bed_path):
    mapping = {}
    with open(bed_path, encoding="utf-8") as handle:
        for line in handle:
            fields = line.rstrip("\n").split("\t")
            if len(fields) < 6:
                continue
            chrom, start, end, short_name, _, strand = fields[:6]
            signature = f"{chrom}:{start}-{end}({strand})"
            mapping[signature] = short_name
    return mapping

def canonicalize_sequence_name(sequence_name, promoter_names):
    if pd.isna(sequence_name):
        return sequence_name
    parts = str(sequence_name).split("::", maxsplit=1)
    if len(parts) != 2 or parts[1] not in promoter_names:
        raise ValueError(f"Unknown PlantCARE sequence name: {sequence_name}")
    return f"{promoter_names[parts[1]]}::{parts[1]}"

def merge_intervals(df):
    """
    Given a dataframe of motifs for a single gene and single motif_name,
    sort by start and merge overlapping intervals.
    """
    sorted_df = df.sort_values(by="Position")
    merged = []
    
    for _, row in sorted_df.iterrows():
        start = int(row["Position"])
        length = int(row["Length"]) if pd.notnull(row["Length"]) else len(str(row["Motif_Sequence"]))
        end = start + length
        
        if not merged:
            merged.append({
                "Gene": row["Gene"],
                "Motif_Name": row["Motif_Name"],
                "Position": start,
                "End": end,
                "Length": length,
                "Strand": row["Strand"],
                "Organism": row["Organism"],
                "Description": row["Description"],
                "Merged_Count": 1
            })
        else:
            prev = merged[-1]
            if start <= prev["End"]:
                # Overlap found: extend end
                prev["End"] = max(prev["End"], end)
                prev["Length"] = prev["End"] - prev["Position"]
                prev["Merged_Count"] += 1
            else:
                merged.append({
                    "Gene": row["Gene"],
                    "Motif_Name": row["Motif_Name"],
                    "Position": start,
                    "End": end,
                    "Length": length,
                    "Strand": row["Strand"],
                    "Organism": row["Organism"],
                    "Description": row["Description"],
                    "Merged_Count": 1
                })
    return pd.DataFrame(merged)

def process_species(species_prefix, tab_file, promoter_bed):
    print(f"\n--- Processing {species_prefix} ({os.path.basename(tab_file)}) ---")
    columns = [
        'Sequence_Name', 'Motif_Name', 'Motif_Sequence', 
        'Position', 'Length', 'Strand', 'Organism', 'Description'
    ]
    df = pd.read_csv(tab_file, sep='\t', header=None, names=columns)
    
    promoter_names = load_promoter_names(promoter_bed)
    df['Sequence_Name'] = df['Sequence_Name'].apply(
        canonicalize_sequence_name, promoter_names=promoter_names
    )
    df['Gene'] = df['Sequence_Name'].apply(lambda x: x.split('::')[0] if pd.notnull(x) else x)
    
    # Normalize case variants of identical motif families
    case_normalization = {
        'G-Box': 'G-box',
        'Myc': 'MYC',
        'Myb': 'MYB'
    }
    df['Motif_Name'] = df['Motif_Name'].replace(case_normalization)
    
    # Raw counts (with normalized names)
    raw_counts = df.groupby(['Gene', 'Motif_Name']).size().unstack(fill_value=0)
    
    # Perform merge per (Gene, Motif_Name)
    merged_records = []
    for (gene, motif), grp in df.groupby(['Gene', 'Motif_Name']):
        merged_grp = merge_intervals(grp)
        merged_records.append(merged_grp)
        
    df_merged = pd.concat(merged_records, ignore_index=True)
    
    # Merged counts
    merged_counts = df_merged.groupby(['Gene', 'Motif_Name']).size().unstack(fill_value=0)
    
    # Ensure all columns from raw are present
    for col in raw_counts.columns:
        if col not in merged_counts.columns:
            merged_counts[col] = 0
    merged_counts = merged_counts[raw_counts.columns]
    
    # Save files
    merged_counts_file = os.path.join(RESULTS_DIR, f"{species_prefix}_motif_counts_merged.tsv")
    merged_counts.to_csv(merged_counts_file, sep='\t')
    
    merged_cleaned_file = os.path.join(RESULTS_DIR, f"{species_prefix}_plantcare_merged.tsv")
    df_merged.to_csv(merged_cleaned_file, sep='\t', index=False)
    
    print(f"Saved merged counts to: {merged_counts_file}")
    print(f"Saved merged records to: {merged_cleaned_file}")
    
    # Key motifs summary
    key_motifs = ["ABRE", "MBS", "G-box", "ARE", "LTR", "TC-rich repeats", "W box", "Box 4", "MYC", "MYB"]
    summary = []
    summary.append(f"=== Summary for {species_prefix} ===")
    summary.append(f"Total raw motif occurrences: {len(df)}")
    summary.append(f"Total merged motif occurrences: {len(df_merged)} (reduced by {len(df) - len(df_merged)})")
    summary.append("\nKey motifs comparison (Sum across all genes):")
    summary.append(f"{'Motif':<15}{'Raw':<10}{'Merged':<10}{'Diff':<10}")
    summary.append("-" * 45)
    for m in key_motifs:
        r_sum = raw_counts[m].sum() if m in raw_counts.columns else 0
        m_sum = merged_counts[m].sum() if m in merged_counts.columns else 0
        summary.append(f"{m:<15}{r_sum:<10}{m_sum:<10}{r_sum - m_sum:<10}")
    
    return "\n".join(summary), raw_counts, merged_counts

def main():
    vper_tab = os.path.join(RESULTS_DIR, "plantCARE_output_PlantCARE_28265.tab")
    vper_bed = os.path.join(RESULTS_DIR, "Vper.promoters.2k.bed")
    
    vtub_tab = os.path.join(RESULTS_DIR, "plantCARE_output_PlantCARE_28346.tab")
    vtub_bed = os.path.join(RESULTS_DIR, "Vtub.promoters.2k.bed")
    
    s_vper, r_vper, m_vper = process_species("Vper", vper_tab, vper_bed)
    s_vtub, r_vtub, m_vtub = process_species("Vtub", vtub_tab, vtub_bed)
    
    full_summary = s_vper + "\n\n" + s_vtub
    summary_path = os.path.join(RESULTS_DIR, "merge_comparison_summary.txt")
    with open(summary_path, "w") as f:
        f.write(full_summary)
    
    print("\n" + "="*50)
    print(full_summary)
    print("="*50)

if __name__ == "__main__":
    main()

