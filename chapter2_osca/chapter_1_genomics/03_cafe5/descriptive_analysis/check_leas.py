import pandas as pd
import re

gff_path = '/home/mfcaval/github/doutorado/data/genomes/Vtub/Vtub.hapA.v1.softmasked.gff3'
og_path = '/home/mfcaval/github/doutorado/analyses/chapter_1_genomics/02_orthofinder/data/OrthoFinder/Results_Aug27_2/Orthogroups/Orthogroups.tsv'
cafe_path = '/home/mfcaval/github/doutorado/analyses/chapter_1_genomics/03_cafe5/cafe5_results/Base_change.tab'

# 1. Find LEA genes in Vtub
lea_genes = set()
with open(gff_path, 'r') as f:
    for line in f:
        if 'mRNA' in line and re.search(r'late embryogenesis abundant|LEA protein', line, re.IGNORECASE):
            match = re.search(r'ID=([^;]+)', line)
            if match:
                gene_id = match.group(1)
                lea_genes.add(gene_id)

print(f"Total LEA genes found in Vtub GFF: {len(lea_genes)}")

# 2. Find Orthogroups for these genes
og_df = pd.read_csv(og_path, sep='\t', low_memory=False)
target_ogs = []
for index, row in og_df.iterrows():
    vtub_genes = str(row['Vtub.pep'])
    if pd.isna(vtub_genes) or vtub_genes == 'nan':
        continue
    vtub_genes_list = vtub_genes.split(', ')
    # If any Vtub gene in this OG is a LEA
    if any(g in lea_genes for g in vtub_genes_list):
        target_ogs.append(row['Orthogroup'])

print(f"Total Orthogroups containing Vtub LEA genes: {len(target_ogs)}")

# 3. Check CAFE expansions for LEAs
cafe_df = pd.read_csv(cafe_path, sep='\t')
lea_cafe_df = cafe_df[cafe_df['FamilyID'].isin(target_ogs)]

vtub_changes = lea_cafe_df[['FamilyID', 'Vtub.pep<1>']].rename(columns={'Vtub.pep<1>': 'Vtub_change'})
print("\nExpansions/Contractions of LEA Orthogroups in Vtub:")
for _, row in vtub_changes.iterrows():
    print(f"{row['FamilyID']}: {row['Vtub_change']}")

# 4. Check ELIP Orthogroups (using Arabidopsis ELIP1 and ELIP2)
elip_genes = ['AT3G22840', 'AT4G14690'] # ELIP1 and ELIP2
elip_ogs = []
for index, row in og_df.iterrows():
    atha_genes = str(row['Ath.canonical.pep'])
    if pd.isna(atha_genes) or atha_genes == 'nan':
        continue
    if any(g in atha_genes for g in elip_genes):
        elip_ogs.append(row['Orthogroup'])

print(f"\nOrthogroups containing Arabidopsis ELIP genes: {elip_ogs}")
elip_cafe_df = cafe_df[cafe_df['FamilyID'].isin(elip_ogs)]
elip_changes = elip_cafe_df[['FamilyID', 'Vtub.pep<1>']].rename(columns={'Vtub.pep<1>': 'Vtub_change'})
print("Expansions/Contractions of ELIP Orthogroups in Vtub:")
for _, row in elip_changes.iterrows():
    print(f"{row['FamilyID']}: {row['Vtub_change']}")

