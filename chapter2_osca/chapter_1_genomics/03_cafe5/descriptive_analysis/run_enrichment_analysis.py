#!/usr/bin/env python3
import pandas as pd
import re
from collections import Counter
from scipy.stats import fisher_exact
import numpy as np
import os

# Paths
gff_vtub = '/home/mfcaval/github/doutorado/data/genomes/Vtub/Vtub.hapA.v1.softmasked.gff3'
gff_vper = '/home/mfcaval/github/doutorado/data/genomes/Vper/Vper.hapA.v1.softmasked.gff3'
orthogroups_file = '/home/mfcaval/github/doutorado/analyses/chapter_1_genomics/02_orthofinder/data/OrthoFinder/Results_Aug27_2/Orthogroups/Orthogroups.tsv'
cafe_change = '/home/mfcaval/github/doutorado/analyses/chapter_1_genomics/03_cafe5/cafe5_results/Base_change.tab'
out_dir = '/home/mfcaval/github/doutorado/analyses/chapter_1_genomics/03_cafe5/descriptive_analysis'

print("1. Parsing GFF functional descriptions...")
gene_to_func = {}
def parse_gff(gff_path):
    with open(gff_path, 'r') as f:
        for line in f:
            if '\tmRNA\t' in line:
                cols = line.strip().split('\t')
                attr = cols[8]
                m = re.search(r'ID=([^;]+)', attr)
                if not m: continue
                gid = m.group(1)
                func_m = re.search(r'eggnog_free_text_desc=([^;]+)', attr)
                if func_m:
                    ftext = func_m.group(1).strip()
                    if ftext and ftext.lower() != 'na':
                        gene_to_func[gid] = ftext

parse_gff(gff_vtub)
parse_gff(gff_vper)

print("2. Mapping Orthogroups to predominant functional terms...")
og_to_func = {}
with open(orthogroups_file, 'r') as f:
    f.readline()
    for line in f:
        parts = line.strip().split('\t')
        og = parts[0]
        genes = []
        for p in parts[1:]:
            genes.extend([x.strip() for x in p.split(',') if x.strip()])
        funcs = [gene_to_func[g] for g in genes if g in gene_to_func]
        if funcs:
            og_to_func[og] = Counter(funcs).most_common(1)[0][0]

df_change = pd.read_csv(cafe_change, sep='\t')
vtub_col = [c for c in df_change.columns if 'Vtub' in c][0]
vper_col = [c for c in df_change.columns if 'Vper' in c][0]

df_change['Function'] = df_change['FamilyID'].map(lambda x: og_to_func.get(x, None))
valid_cafe = df_change.dropna(subset=['Function']).copy()

def simplify_func(f):
    f_lower = f.lower()
    if 'translocon' in f_lower or 'translocation complex' in f_lower or 'protein precursor import into chloroplast' in f_lower:
        return 'Chloroplast protein translocation (TOC/TIC)'
    elif 'ndh' in f_lower or 'nad(p)h-quinone oxidoreductase' in f_lower or 'photosynthetic electron transport' in f_lower:
        return 'Photosynthetic electron transport & NDH complex'
    elif 'photosystem ii' in f_lower or 'psba' in f_lower or 'psb' in f_lower:
        return 'Photosystem II core & assembly'
    elif 'photosystem i' in f_lower or 'ycf4' in f_lower:
        return 'Photosystem I assembly & reaction center'
    elif '16s rrna' in f_lower or 'ribosomal' in f_lower or 'rrna binding' in f_lower:
        return 'Plastid ribosome biogenesis & translation'
    elif 'lrr' in f_lower or 'leucine-rich repeat' in f_lower or 'receptor-like' in f_lower or 'receptor protein kinase' in f_lower:
        return 'LRR Receptor-Like Kinases & Cell Wall Signaling'
    elif 'disease resistance' in f_lower or 'nb-lrr' in f_lower or 'rga' in f_lower:
        return 'NB-LRR Immune Receptors & Disease Resistance'
    elif 'peptidase a1' in f_lower or 'aspartic peptidase' in f_lower or 'aspartic proteinase' in f_lower:
        return 'Aspartic Peptidases (Family A1)'
    elif 'ubiquitin' in f_lower or 'u-box' in f_lower or 'f-box' in f_lower or 'ring' in f_lower:
        return 'Ubiquitin-Proteasome System & Quality Control'
    elif 'pentatricopeptide' in f_lower or 'ppr' in f_lower:
        return 'Pentatricopeptide Repeat (PPR) RNA Processing'
    elif 'transpos' in f_lower or 'mobile domain' in f_lower or 'retrovirus' in f_lower:
        return 'Transposases & Mobile Genetic Elements'
    elif 'acetyl-coenzyme a carboxylase' in f_lower or 'biotin carboxylase' in f_lower or 'acc' in f_lower:
        return 'Fatty Acid & Lipid Biosynthesis (ACC)'
    elif 'organonitrogen' in f_lower or 'amino acid' in f_lower or 'proline' in f_lower:
        return 'Organonitrogen & Amino Acid Metabolism'
    elif 'duf295' in f_lower:
        return 'DUF295 Domain Signaling'
    elif 'adp binding' in f_lower or 'adp-binding' in f_lower:
        return 'ADP-Binding Regulatory Proteins'
    elif 'cytochrome p450' in f_lower:
        return 'Cytochrome P450 Monooxygenases'
    elif 'udp-glycosyltransferase' in f_lower:
        return 'UDP-Glycosyltransferases (UGTs)'
    elif 'wall-associated' in f_lower or 'wak' in f_lower:
        return 'Wall-Associated Receptor Kinases (WAKs)'
    elif 'terpene synthase' in f_lower:
        return 'Terpene Synthase Secondary Defense'
    elif 'atp synthase' in f_lower:
        return 'Plastid ATP Synthase Machinery'
    else:
        return f[:50]

valid_cafe['Category'] = valid_cafe['Function'].apply(simplify_func)

def compute_enrichment(df, target_col, species_label):
    target = df[df[target_col] > 0]
    bg = df
    n_target = len(target)
    n_bg = len(bg)
    
    target_counts = target['Category'].value_counts()
    bg_counts = bg['Category'].value_counts()
    
    records = []
    for cat, k in target_counts.items():
        if k < 2: continue
        M = n_bg
        n = bg_counts[cat]
        N = n_target
        a = k
        b = N - k
        c = n - k
        d = (M - N) - c
        odds, pval = fisher_exact([[a, b], [c, d]], alternative='greater')
        records.append({
            'Species': species_label,
            'Functional_Category': cat,
            'Target_Hits': a,
            'Target_Total': N,
            'Background_Hits': n,
            'Background_Total': M,
            'Fold_Enrichment': round((a/N) / (n/M), 2),
            'p_value': pval
        })
    
    res = pd.DataFrame(records).sort_values(by='p_value')
    m = len(res)
    res['FDR_q_value'] = res['p_value'] * m / (np.arange(1, m + 1))
    res['FDR_q_value'] = np.minimum.accumulate(res['FDR_q_value'][::-1])[::-1]
    res['FDR_q_value'] = np.clip(res['FDR_q_value'], 0, 1.0)
    return res

print("3. Computing Fisher's Exact Test with Benjamini-Hochberg FDR...")
res_vtub = compute_enrichment(valid_cafe, vtub_col, 'Vellozia_tubiflora')
res_vper = compute_enrichment(valid_cafe, vper_col, 'Vellozia_peripherica')

combined = pd.concat([res_vtub, res_vper])
out_tsv = os.path.join(out_dir, 'functional_enrichment_results.tsv')
combined.to_csv(out_tsv, sep='\t', index=False)
print(f"4. Successfully exported results to {out_tsv}")

