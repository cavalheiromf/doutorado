import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import argparse

# Common functional categorization for PlantCARE motifs
MOTIF_CATEGORIES = {
    'Hormone': [
        'ABRE', 'CGTCA-motif', 'TGACG-motif', 'TCA-element', 
        'GARE-motif', 'P-box', 'TGA-element', 'AuxRR-core', 'TATC-box', 'SARE'
    ],
    'Stress': [
        'MBS', 'TC-rich repeats', 'LTR', 'ARE', 'W box', 'STRE', 
        'WUN-motif', 'MRE', 'GC-motif', 'DRE core', 'DRE1'
    ],
    'Light': [
        'G-box', 'G-Box', 'Sp1', 'Box 4', 'GT1-motif', 'AE-box',
        'I-box', 'GATA-motif', 'Box II', 'Box III', 'TCT-motif', 'ACE', 
        'LAMP-element', 'ATCT-motif'
    ],
    'Development & Other': [
        'O2-site', 'CAT-box', 'RY-element', 'MBSI', 'HD-Zip 3', 
        'GCN4_motif', 'A-box', 'circadian', 'CAAAT'
    ]
}

def clean_data(df):
    """
    Remove ubiquitous elements and parsing artifacts
    """
    cols_to_drop = [c for c in df.columns if c in ['TATA-box', 'CAAT-box', 'TATA'] or 'Unnamed' in c]
    df_clean = df.drop(columns=cols_to_drop, errors='ignore')
    return df_clean

def plot_heatmap(df, species, output_dir):
    # Ensure index is Gene
    if 'Gene' in df.columns:
        df = df.set_index('Gene')
    
    df_clean = clean_data(df)
    
    # Identify motifs that are in our dictionary and present in the dataframe
    selected_motifs = []
    category_colors = []
    
    # We will map colors to categories for annotation
    cat_palette = sns.color_palette("Set2", len(MOTIF_CATEGORIES))
    cat_color_map = {cat: cat_palette[i] for i, cat in enumerate(MOTIF_CATEGORIES.keys())}
    
    col_colors_dict = {}
    for cat, motifs in MOTIF_CATEGORIES.items():
        for m in motifs:
            if m in df_clean.columns:
                selected_motifs.append(m)
                col_colors_dict[m] = cat_color_map[cat]
                
    # Filter df to only known categorized motifs for cleaner visualization
    if selected_motifs:
        df_plot = df_clean[selected_motifs]
    else:
        df_plot = df_clean # Fallback if none matched
        
    # Remove genes (rows) that have 0 motifs across all selected motifs
    df_plot = df_plot.loc[(df_plot != 0).any(axis=1)]
    
    # Create column colors series for seaborn
    col_colors = pd.Series(col_colors_dict).reindex(df_plot.columns)
    
    plt.figure(figsize=(14, 10))
    g = sns.clustermap(
        df_plot, 
        cmap="YlOrRd", 
        linewidths=1, 
        linecolor='white',
        col_colors=col_colors if selected_motifs else None,
        col_cluster=True,
        row_cluster=True,
        figsize=(12, 8),
        cbar_kws={'label': 'Number of occurrences'}
    )
    
    g.fig.suptitle(f'Cis-acting Elements in {species} OSCA Promoters', y=1.05, fontsize=16)
    
    # Adjust rotation
    plt.setp(g.ax_heatmap.get_xticklabels(), rotation=45, ha='right')
    plt.setp(g.ax_heatmap.get_yticklabels(), rotation=0)
    
    # Create custom legend for categories
    if selected_motifs:
        from matplotlib.patches import Patch
        legend_elements = [Patch(facecolor=cat_color_map[cat], label=cat) for cat in MOTIF_CATEGORIES.keys()]
        g.ax_heatmap.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.05, 1.05), title='Motif Category')
        
    plt.tight_layout()
    
    output_path = os.path.join(output_dir, f"{species}_promoter_heatmap.png")
    g.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Heatmap saved to {output_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", default="../results", help="Directory with _motif_counts.tsv files")
    parser.add_argument("--output_dir", default="../results", help="Directory to save the plots")
    args = parser.parse_args()
    
    for species in ["Vper", "Vtub"]:
        file_path = os.path.join(args.input_dir, f"{species}_motif_counts.tsv")
        if os.path.exists(file_path):
            print(f"Plotting for {species}...")
            df = pd.read_csv(file_path, sep='\t')
            plot_heatmap(df, species, args.output_dir)
        else:
            print(f"File not found: {file_path}")

if __name__ == "__main__":
    main()
