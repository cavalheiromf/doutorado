#!/usr/bin/env python3
"""
Builds comprehensive SQLite annotation databases and master TSVs for:
1. Vellozia tubiflora (vtub_annotation.db)
2. Vellozia peripherica (vper_annotation.db)
3. Unified comparative database (vellozia_master_annotation.db)
"""

import sqlite3
import os
import re
import pandas as pd
from collections import defaultdict, Counter

BASE_DIR = '/home/mfcaval/github/doutorado'
VTUB_GFF = os.path.join(BASE_DIR, 'data/genomes/Vtub/Vtub.hapA.v1.softmasked.gff3')
VPER_GFF = os.path.join(BASE_DIR, 'data/genomes/Vper/Vper.hapA.v1.softmasked.gff3')

ORTHOGROUPS_TSV = os.path.join(BASE_DIR, 'analyses/chapter_1_genomics/02_orthofinder/data/OrthoFinder/Results_Aug27_2/Orthogroups/Orthogroups.tsv')
UNASSIGNED_TSV = os.path.join(BASE_DIR, 'analyses/chapter_1_genomics/02_orthofinder/data/OrthoFinder/Results_Aug27_2/Orthogroups/Orthogroups_UnassignedGenes.tsv')
SINGLE_COPY_TXT = os.path.join(BASE_DIR, 'analyses/chapter_1_genomics/02_orthofinder/data/OrthoFinder/Results_Aug27_2/Orthogroups/Orthogroups_SingleCopyOrthologues.txt')

CAFE_CHANGE_TAB = os.path.join(BASE_DIR, 'analyses/chapter_1_genomics/03_cafe5/cafe5_results/Base_change.tab')
CAFE_COUNT_TAB = os.path.join(BASE_DIR, 'analyses/chapter_1_genomics/03_cafe5/cafe5_results/Base_count.tab')
CAFE_FAM_TXT = os.path.join(BASE_DIR, 'analyses/chapter_1_genomics/03_cafe5/cafe5_results/Base_family_results.txt')

OUT_DIR_VTUB = os.path.join(BASE_DIR, 'data/genomes/Vtub')
OUT_DIR_VPER = os.path.join(BASE_DIR, 'data/genomes/Vper')
OUT_DIR_COMP = os.path.join(BASE_DIR, 'analyses/chapter_1_genomics/annotation_db')
os.makedirs(OUT_DIR_COMP, exist_ok=True)

print("1. Parsing single-copy orthogroups and CAFE5 dynamics...")
single_copy_ogs = set()
if os.path.exists(SINGLE_COPY_TXT):
    with open(SINGLE_COPY_TXT, 'r') as f:
        single_copy_ogs = set(line.strip() for line in f if line.strip())

cafe_sig_fams = set()
if os.path.exists(CAFE_FAM_TXT):
    with open(CAFE_FAM_TXT, 'r') as f:
        for line in f:
            if line.startswith('#'): continue
            parts = line.strip().split('\t')
            if len(parts) >= 3 and parts[2] == 'y':
                cafe_sig_fams.add(parts[0])

cafe_change_dict = {}
if os.path.exists(CAFE_CHANGE_TAB):
    df_ch = pd.read_csv(CAFE_CHANGE_TAB, sep='\t')
    vt_col = [c for c in df_ch.columns if 'Vtub' in c][0]
    vp_col = [c for c in df_ch.columns if 'Vper' in c][0]
    for _, r in df_ch.iterrows():
        cafe_change_dict[r['FamilyID']] = {
            'vtub_change': int(r[vt_col]),
            'vper_change': int(r[vp_col])
        }

cafe_count_dict = {}
if os.path.exists(CAFE_COUNT_TAB):
    df_cnt = pd.read_csv(CAFE_COUNT_TAB, sep='\t')
    for _, r in df_cnt.iterrows():
        fam = r['FamilyID']
        # Find ancestral and tip counts
        anc_cols = [c for c in df_cnt.columns if '<' in c or 'node' in c.lower() or 'root' in c.lower()]
        anc_val = int(r[anc_cols[0]]) if anc_cols else None
        cafe_count_dict[fam] = {
            'ancestral_count': anc_val
        }

print("2. Parsing Orthogroups...")
gene_to_og = {}
og_members = defaultdict(lambda: {'Vtub': [], 'Vper': [], 'Ath': []})

def process_og_file(filepath):
    with open(filepath, 'r') as f:
        header = f.readline().strip().split('\t')
        sp_cols = header[1:]
        for line in f:
            parts = line.strip().split('\t')
            og = parts[0]
            for idx, sp in enumerate(sp_cols):
                if idx + 1 < len(parts):
                    genes = [g.strip() for g in parts[idx + 1].split(',') if g.strip()]
                    sp_key = 'Vtub' if 'Vtub' in sp else ('Vper' if 'Vper' in sp else 'Ath')
                    og_members[og][sp_key].extend(genes)
                    for g in genes:
                        gene_to_og[g] = og

process_og_file(ORTHOGROUPS_TSV)
if os.path.exists(UNASSIGNED_TSV):
    process_og_file(UNASSIGNED_TSV)

print("3. Parsing GFFs for Vtub and Vper...")
def parse_species_gff(gff_path, species_name):
    records = []
    # Collect exon counts and CDS info per transcript
    tx_exons = defaultdict(int)
    tx_cds_len = defaultdict(int)
    tx_info = {}
    
    with open(gff_path, 'r') as f:
        for line in f:
            if line.startswith('#'): continue
            cols = line.strip().split('\t')
            if len(cols) < 9: continue
            chrom, source, ftype, start, end, score, strand, phase, attr = cols
            start, end = int(start), int(end)
            
            if ftype == 'mRNA' or ftype == 'transcript':
                m_id = re.search(r'ID=([^;]+)', attr)
                m_parent = re.search(r'Parent=([^;]+)', attr)
                m_desc = re.search(r'eggnog_free_text_desc=([^;]+)', attr)
                
                tx_id = m_id.group(1) if m_id else ''
                gene_id = m_parent.group(1) if m_parent else tx_id
                desc = m_desc.group(1).strip() if m_desc else 'Uncharacterized protein'
                if desc.lower() == 'na': desc = 'Uncharacterized protein'
                
                tx_info[tx_id] = {
                    'species': species_name,
                    'gene_id': gene_id,
                    'transcript_id': tx_id,
                    'chromosome': chrom,
                    'start': start,
                    'end': end,
                    'strand': strand,
                    'length_bp': end - start + 1,
                    'eggnog_desc': desc
                }
            elif ftype == 'exon':
                m_parent = re.search(r'Parent=([^;]+)', attr)
                if m_parent:
                    tx_exons[m_parent.group(1)] += 1
            elif ftype == 'CDS':
                m_parent = re.search(r'Parent=([^;]+)', attr)
                if m_parent:
                    tx_cds_len[m_parent.group(1)] += (end - start + 1)
                    
    # Assemble master list
    for tx_id, d in tx_info.items():
        d['exon_count'] = tx_exons.get(tx_id, 1)
        d['cds_len_bp'] = tx_cds_len.get(tx_id, d['length_bp'])
        d['protein_len_aa'] = d['cds_len_bp'] // 3
        
        # Orthology info
        og = gene_to_og.get(tx_id, 'Unassigned')
        d['orthogroup_id'] = og
        d['is_single_copy'] = 1 if og in single_copy_ogs else 0
        
        # Sister orthologs & Ath orthologs
        members = og_members.get(og, {'Vtub': [], 'Vper': [], 'Ath': []})
        if species_name == 'Vellozia_tubiflora':
            d['sister_orthologs'] = ','.join(members['Vper']) if members['Vper'] else 'None'
        else:
            d['sister_orthologs'] = ','.join(members['Vtub']) if members['Vtub'] else 'None'
        d['ath_orthologs'] = ','.join(members['Ath']) if members['Ath'] else 'None'
        
        # CAFE dynamics
        ch = cafe_change_dict.get(og, {'vtub_change': 0, 'vper_change': 0})
        cnt = cafe_count_dict.get(og, {'ancestral_count': None})
        d['ancestral_count'] = cnt['ancestral_count']
        d['family_is_significant'] = 1 if og in cafe_sig_fams else 0
        if species_name == 'Vellozia_tubiflora':
            d['delta_change'] = ch['vtub_change']
            d['expansion_status'] = 'Expanded' if ch['vtub_change'] > 0 else ('Contracted' if ch['vtub_change'] < 0 else 'Stable')
        else:
            d['delta_change'] = ch['vper_change']
            d['expansion_status'] = 'Expanded' if ch['vper_change'] > 0 else ('Contracted' if ch['vper_change'] < 0 else 'Stable')
            
        records.append(d)
        
    return pd.DataFrame(records)

df_vtub = parse_species_gff(VTUB_GFF, 'Vellozia_tubiflora')
df_vper = parse_species_gff(VPER_GFF, 'Vellozia_peripherica')
df_all = pd.concat([df_vtub, df_vper], ignore_index=True)

print(f"Parsed {len(df_vtub)} Vtub records and {len(df_vper)} Vper records.")

def create_sqlite_db(df, db_path, table_name):
    if os.path.exists(db_path):
        os.remove(db_path)
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, index=False, if_exists='replace')
    
    # Create indices for fast lookup
    cursor = conn.cursor()
    cursor.execute(f"CREATE INDEX idx_{table_name}_gene_id ON {table_name}(gene_id);")
    cursor.execute(f"CREATE INDEX idx_{table_name}_tx_id ON {table_name}(transcript_id);")
    cursor.execute(f"CREATE INDEX idx_{table_name}_chrom ON {table_name}(chromosome);")
    cursor.execute(f"CREATE INDEX idx_{table_name}_og ON {table_name}(orthogroup_id);")
    cursor.execute(f"CREATE INDEX idx_{table_name}_desc ON {table_name}(eggnog_desc);")
    
    # Create Master View
    cursor.execute(f"""
    CREATE VIEW v_master_annotation AS
    SELECT 
        transcript_id, gene_id, species, chromosome, start, end, strand, length_bp, exon_count, protein_len_aa,
        eggnog_desc, orthogroup_id, is_single_copy, sister_orthologs, ath_orthologs,
        expansion_status, delta_change, family_is_significant
    FROM {table_name};
    """)
    conn.commit()
    conn.close()
    print(f"Created SQLite database: {db_path} (Table: {table_name}, View: v_master_annotation)")

# 4. Generate Databases
db_vtub = os.path.join(OUT_DIR_VTUB, 'vtub_annotation.db')
db_vper = os.path.join(OUT_DIR_VPER, 'vper_annotation.db')
db_comp = os.path.join(OUT_DIR_COMP, 'vellozia_master_annotation.db')

create_sqlite_db(df_vtub, db_vtub, 'vtub_genes')
create_sqlite_db(df_vper, db_vper, 'vper_genes')
create_sqlite_db(df_all, db_comp, 'vellozia_genes')

# 5. Export TSVs
tsv_vtub = os.path.join(OUT_DIR_VTUB, 'vtub_master_annotation.tsv')
tsv_vper = os.path.join(OUT_DIR_VPER, 'vper_master_annotation.tsv')
tsv_comp = os.path.join(OUT_DIR_COMP, 'vellozia_comparative_master_annotation.tsv')

df_vtub.to_csv(tsv_vtub, sep='\t', index=False)
df_vper.to_csv(tsv_vper, sep='\t', index=False)
df_all.to_csv(tsv_comp, sep='\t', index=False)

print(f"Exported master TSVs:\n- {tsv_vtub}\n- {tsv_vper}\n- {tsv_comp}")
print("Database construction completed successfully!")

