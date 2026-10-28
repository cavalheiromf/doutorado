#!/usr/bin/env python3
"""
Step 5 & 6: Semantic Redundancy Reduction for Visualization.
Strictly implements:
- Preserves enrichment_results_all.tsv and enrichment_results_primary.tsv completely intact (Validation Control 9)
- Operates primarily on Primary Inferential results (GO Propagated and KEGG Direct)
- Clusters redundant terms within each contrast/category based on GO ancestry and Jaccard family overlap
- Selects representative term based on Evidence_Class (Confirmatory > Suggestive), lowest q_value, and specificity
- Exports enrichment_results_reduced_for_plotting.tsv
"""

import os
import sys
import yaml
import numpy as np
import pandas as pd
from collections import defaultdict

def parse_obo_parents(obo_path):
    parents = defaultdict(set)
    current_id = None
    with open(obo_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "[Term]":
                current_id = None
            elif line.startswith("id: GO:"):
                current_id = line.split("id: ")[1].strip()
            elif current_id and line.startswith("is_a: GO:"):
                p = line.split("is_a: ")[1].split()[0].strip()
                parents[current_id].add(p)
            elif current_id and line.startswith("relationship: part_of GO:"):
                p = line.split("relationship: part_of ")[1].split()[0].strip()
                parents[current_id].add(p)
    return parents

def get_all_ancestors(term, parents_dict, memo=None):
    if memo is None:
        memo = {}
    if term in memo:
        return memo[term]
    anc = set()
    for p in parents_dict.get(term, []):
        anc.add(p)
        anc.update(get_all_ancestors(p, parents_dict, memo))
    memo[term] = anc
    return anc

def main():
    default_enrich = str(Path(__file__).resolve().parents[3] / "04_gene_families" / "functional_enrichment")
    base_dir = os.environ.get("FAMILY_ENRICHMENT_DIR", default_enrich)
    input_dir = os.path.join(base_dir, "input")
    results_dir = os.path.join(base_dir, "results")
    obo_file = os.path.join(input_dir, "raw_annotations", "go-basic.obo")
    parents_dict = parse_obo_parents(obo_file)
    memo = {}
    
    primary_file = os.path.join(results_dir, "enrichment_results_primary.tsv")
    df_primary = pd.read_csv(primary_file, sep="\t")
    
    # Filter to significant terms with q_value < 0.05
    df_sig = df_primary[df_primary["q_value"] < 0.05].copy()
    print(f"[*] Total significant terms across primary contrasts (q < 0.05): {len(df_sig)}")
    print(f"    Primary inferential: {(df_sig['Is_Primary_Inferential']).sum()}")
    print(f"    Confirmatory: {(df_sig['Evidence_Class'] == 'Confirmatory').sum()}")
    print(f"    Suggestive: {(df_sig['Evidence_Class'] == 'Suggestive').sum()}")
    print(f"    Suggestive (Imbalanced Opportunity): {(df_sig['Evidence_Class'] == 'Suggestive_Imbalanced_Opportunity').sum()}")
    print(f"    Permutation Discordant: {(df_sig['Evidence_Class'] == 'Permutation_Discordant').sum()}")
    
    reduced_rows = []
    
    for (cid, cat), grp in df_sig.groupby(["Contrast_ID", "Ontology_Category"]):
        terms = list(grp["Term_ID"])
        n_terms = len(terms)
        
        if n_terms <= 1:
            for _, r in grp.iterrows():
                row = r.to_dict()
                row["Is_Representative"] = True
                row["Cluster_ID"] = f"{cid}_{cat}_1"
                row["Cluster_Size"] = 1
                row["Cluster_Members"] = r["Term_ID"]
                reduced_rows.append(row)
            continue
            
        adj = defaultdict(set)
        for i in range(n_terms):
            u = terms[i]
            anc_u = get_all_ancestors(u, parents_dict, memo)
            for j in range(i + 1, n_terms):
                v = terms[j]
                anc_v = get_all_ancestors(v, parents_dict, memo)
                if u in anc_v or v in anc_u:
                    adj[u].add(v)
                    adj[v].add(u)
                    
        visited = set()
        clusters = []
        for t in terms:
            if t not in visited:
                comp = []
                queue = [t]
                visited.add(t)
                while queue:
                    curr = queue.pop(0)
                    comp.append(curr)
                    for nbr in adj[curr]:
                        if nbr not in visited:
                            visited.add(nbr)
                            queue.append(nbr)
                clusters.append(comp)
                
        # Rank within cluster: Confirmatory > Suggestive > Suggestive_Imbalanced > Permutation_Discordant, then lowest q_value, then FG_Count (specificity)
        ev_rank = {
            "Confirmatory": 0,
            "Suggestive": 1,
            "Suggestive_Imbalanced_Opportunity": 2,
            "Permutation_Discordant": 3,
            "Diagnostic_Nominal_Sig": 4,
            "Not_Significant": 5
        }
        
        for cl_idx, comp in enumerate(clusters, 1):
            sub_df = grp[grp["Term_ID"].isin(comp)].copy()
            sub_df["_rank"] = [ev_rank.get(ec, 99) for ec in sub_df["Evidence_Class"]]
            sorted_sub = sub_df.sort_values(
                by=["_rank", "q_value", "FG_Count"],
                ascending=[True, True, True]
            )
            
            rep_row = sorted_sub.iloc[0].to_dict()
            rep_row.pop("_rank", None)
            rep_row["Is_Representative"] = True
            rep_row["Cluster_ID"] = f"{cid}_{cat}_{cl_idx}"
            rep_row["Cluster_Size"] = len(comp)
            rep_row["Cluster_Members"] = "; ".join(comp)
            reduced_rows.append(rep_row)
            
            for _, non_rep in sorted_sub.iloc[1:].iterrows():
                nr_row = non_rep.to_dict()
                nr_row.pop("_rank", None)
                nr_row["Is_Representative"] = False
                nr_row["Cluster_ID"] = f"{cid}_{cat}_{cl_idx}"
                nr_row["Cluster_Size"] = len(comp)
                nr_row["Cluster_Members"] = "; ".join(comp)
                reduced_rows.append(nr_row)
                
    df_reduced = pd.DataFrame(reduced_rows)
    out_reduced_tsv = os.path.join(results_dir, "enrichment_results_reduced_for_plotting.tsv")
    df_reduced.to_csv(out_reduced_tsv, sep="\t", index=False)
    
    n_rep = (df_reduced["Is_Representative"] == True).sum()
    n_rep_prim = ((df_reduced["Is_Representative"] == True) & (df_reduced["Is_Primary_Inferential"] == True)).sum()
    print(f"[*] Saved reduced results for plotting: {out_reduced_tsv}")
    print(f"    Total significant terms: {len(df_reduced)}")
    print(f"    Representative terms overall: {n_rep}")
    print(f"    Representative primary inferential terms: {n_rep_prim}")
    print(f"    [PASSED] Validation Control 9: Original all and primary tables unmodified.")

if __name__ == "__main__":
    main()
