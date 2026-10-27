import pandas as pd
import glob
import os
import argparse


def load_promoter_names(bed_path):
    """Map genomic promoter signatures to their canonical short names."""
    mapping = {}
    with open(bed_path, encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            fields = line.rstrip("\n").split("\t")
            if len(fields) < 6:
                raise ValueError(f"{bed_path}:{line_number}: expected BED6")
            chrom, start, end, short_name, _, strand = fields[:6]
            signature = f"{chrom}:{start}-{end}({strand})"
            if signature in mapping:
                raise ValueError(f"Duplicate promoter signature: {signature}")
            mapping[signature] = short_name
    return mapping


def canonicalize_sequence_name(sequence_name, promoter_names):
    if pd.isna(sequence_name):
        return sequence_name
    parts = str(sequence_name).split("::", maxsplit=1)
    if len(parts) != 2 or parts[1] not in promoter_names:
        raise ValueError(f"Unknown PlantCARE sequence name: {sequence_name}")
    return f"{promoter_names[parts[1]]}::{parts[1]}"

def parse_plantcare(file_path, promoter_bed):
    """
    Parses a PlantCARE output .tab file and returns a summary DataFrame.
    """
    # PlantCARE tab outputs usually don't have headers
    columns = [
        'Sequence_Name', 'Motif_Name', 'Motif_Sequence', 
        'Position', 'Length', 'Strand', 'Organism', 'Description'
    ]
    
    # Read the tab-separated file
    try:
        df = pd.read_csv(file_path, sep='\t', header=None, names=columns)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

    promoter_names = load_promoter_names(promoter_bed)
    df['Sequence_Name'] = df['Sequence_Name'].apply(
        canonicalize_sequence_name, promoter_names=promoter_names
    )

    # Clean the Sequence_Name to just keep the canonical Gene ID.
    df['Gene'] = df['Sequence_Name'].apply(lambda x: x.split('::')[0] if pd.notnull(x) else x)
    
    # Count motif occurrences per gene
    motif_counts = df.groupby(['Gene', 'Motif_Name']).size().unstack(fill_value=0)
    
    return motif_counts, df

def main():
    parser = argparse.ArgumentParser(description="Process PlantCARE output files.")
    parser.add_argument("--input_dir", default="../results", help="Directory containing PlantCARE .tab files")
    parser.add_argument("--output_dir", default="../results", help="Directory to save summary tables")
    args = parser.parse_args()

    # Find all .tab files in the input directory
    tab_files = glob.glob(os.path.join(args.input_dir, "*.tab"))
    
    if not tab_files:
        print(f"No .tab files found in {args.input_dir}")
        return

    for file_path in tab_files:
        filename = os.path.basename(file_path)
        species_prefix = "Vper" if "28265" in filename else "Vtub" if "28346" in filename else "Unknown"
        if species_prefix == "Unknown":
            print(f"Skipping unrecognized PlantCARE file: {filename}")
            continue
        promoter_bed = os.path.join(args.input_dir, f"{species_prefix}.promoters.2k.bed")
        
        print(f"Processing {filename} ({species_prefix})...")
        counts_df, raw_df = parse_plantcare(file_path, promoter_bed)
        
        if counts_df is not None:
            output_file = os.path.join(args.output_dir, f"{species_prefix}_motif_counts.tsv")
            counts_df.to_csv(output_file, sep='\t')
            print(f"Saved summary to {output_file}")
            
            # Also save a cleaned version of the raw data with the Gene column
            raw_output = os.path.join(args.output_dir, f"{species_prefix}_plantcare_cleaned.tsv")
            raw_df.to_csv(raw_output, sep='\t', index=False)

if __name__ == "__main__":
    main()
