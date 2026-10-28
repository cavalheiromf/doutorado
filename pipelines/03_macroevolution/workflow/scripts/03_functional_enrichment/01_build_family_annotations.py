#!/usr/bin/env python3
"""
Step 1: Build comprehensive functional annotations per FamilyID (orthogroup).
Strictly implements:
- Direct reconciliation of Ath.pep in Orthogroups.tsv with Ath.cds.fa locus_tag (Validation Control 1)
- Parsing of Arabidopsis GAF file (ARATH-mod.gaf.gz) excluding NOT qualifiers and resolving alternate/replaced IDs
- Tracking of non-IEA evidence per (locus, GO_term) pair and hierarchical inheritance along DAG
- Exclusion of root GO terms (GO:0008150, GO:0003674, GO:0005575)
- Parsing of KEGG pathway annotations (ath_pathway_links.tsv, ath_pathway_list.tsv)
- Output: intermediate/ath_sequence_to_locus.tsv, orthogroup_functional_annotations.tsv, functional_annotation_qc.tsv
"""

import os
import sys
import gzip
import re
import yaml
import numpy as np
import pandas as pd
from collections import defaultdict

ROOT_TERMS = {"GO:0008150", "GO:0003674", "GO:0005575"}

def parse_obo(obo_path):
    print(f"[*] Parsing Gene Ontology OBO file: {obo_path}")
    terms = {}
    alt_map = {}
    replaced_map = {}
    parents_map = defaultdict(set)
    children_map = defaultdict(set)
    
    current_term = None
    obo_version = "releases/2026-07-26"
    with open(obo_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("data-version:"):
                obo_version = line.split("data-version:")[1].strip()
            elif line == "[Term]":
                if current_term and "id" in current_term:
                    tid = current_term["id"]
                    terms[tid] = current_term
                current_term = {"parents": set(), "is_obsolete": False}
            elif line == "[Typedef]":
                if current_term and "id" in current_term:
                    tid = current_term["id"]
                    terms[tid] = current_term
                current_term = None
            elif current_term is not None:
                if line.startswith("id: GO:"):
                    current_term["id"] = line.split("id: ")[1].strip()
                elif line.startswith("name: "):
                    current_term["name"] = line.split("name: ")[1].strip()
                elif line.startswith("namespace: "):
                    ns = line.split("namespace: ")[1].strip()
                    if ns == "biological_process": current_term["namespace"] = "BP"
                    elif ns == "molecular_function": current_term["namespace"] = "MF"
                    elif ns == "cellular_component": current_term["namespace"] = "CC"
                    else: current_term["namespace"] = ns
                elif line.startswith("alt_id: GO:"):
                    alt = line.split("alt_id: ")[1].strip()
                    alt_map[alt] = current_term["id"]
                elif line.startswith("is_obsolete: true"):
                    current_term["is_obsolete"] = True
                elif line.startswith("replaced_by: GO:"):
                    rep = line.split("replaced_by: ")[1].strip()
                    replaced_map[current_term["id"]] = rep
                elif line.startswith("is_a: GO:"):
                    p = line.split("is_a: ")[1].split()[0].strip()
                    parents_map[current_term["id"]].add(p)
                    children_map[p].add(current_term["id"])
                elif line.startswith("relationship: part_of GO:"):
                    p = line.split("relationship: part_of ")[1].split()[0].strip()
                    parents_map[current_term["id"]].add(p)
                    children_map[p].add(current_term["id"])
                    
        if current_term and "id" in current_term:
            tid = current_term["id"]
            terms[tid] = current_term
            
    print(f"    Loaded {len(terms)} GO terms, {len(alt_map)} alternate IDs, {len(replaced_map)} replacement IDs (OBO version: {obo_version}).")
    
    # Compute recursive ancestor map
    print("    Computing hierarchical ancestor closure for terms...")
    ancestors_map = {}
    def get_ancestors(t):
        if t in ancestors_map:
            return ancestors_map[t]
        anc = set()
        for p in parents_map.get(t, []):
            anc.add(p)
            anc.update(get_ancestors(p))
        ancestors_map[t] = anc
        return anc

    for t in terms:
        get_ancestors(t)

    return terms, alt_map, replaced_map, ancestors_map, obo_version

def parse_gaf(gaf_path, terms, alt_map, replaced_map, ancestors_map):
    print(f"[*] Parsing Arabidopsis GAF file: {gaf_path}")
    
    # locus -> namespace -> set of direct terms
    locus_go_direct = defaultdict(lambda: {"BP": set(), "MF": set(), "CC": set()})
    # locus -> set of direct non-IEA terms
    locus_non_iea_direct = defaultdict(set)
    # locus -> set of all observed evidence codes
    locus_ev_codes = defaultdict(set)
    
    skipped_not = 0
    skipped_obsolete = 0
    skipped_root = 0
    resolved_alt = 0
    resolved_rep = 0
    total_annotations = 0
    gaf_version = "2026-08-02"
    gaf_date = "2026-08-04"
    
    with gzip.open(gaf_path, "rt", encoding="utf-8") as f:
        for line in f:
            if line.startswith("!"):
                if line.startswith("!go-version:"):
                    m = re.search(r'releases/(\d{4}-\d{2}-\d{2})', line)
                    if m: gaf_version = m.group(1)
                elif line.startswith("!date-generated:"):
                    m = re.search(r'(\d{4}-\d{2}-\d{2})', line)
                    if m: gaf_date = m.group(1)
                continue
            if not line.strip():
                continue
            cols = line.strip().split("\t")
            if len(cols) < 15:
                continue
                
            locus = cols[1].strip().upper()
            qualifier = cols[3].strip()
            go_id = cols[4].strip()
            ev_code = cols[6].strip()
            aspect = cols[8].strip() # P, F, C
            
            # 1. Exclude NOT annotations
            if "NOT" in qualifier or "not" in qualifier:
                skipped_not += 1
                continue
                
            # 2. Resolve alt_id and replaced_by
            if go_id in alt_map:
                go_id = alt_map[go_id]
                resolved_alt += 1
            elif go_id in replaced_map:
                go_id = replaced_map[go_id]
                resolved_rep += 1
                
            # 3. Check term validity in ontology
            if go_id not in terms or terms[go_id]["is_obsolete"]:
                skipped_obsolete += 1
                continue
                
            # 4. Exclude root terms
            if go_id in ROOT_TERMS:
                skipped_root += 1
                continue
                
            ns = terms[go_id]["namespace"] # BP, MF, CC
            locus_go_direct[locus][ns].add(go_id)
            locus_ev_codes[locus].add(ev_code)
            
            # Non-IEA evidence tracking per (locus, go_id)
            if ev_code not in {"IEA", "ND"}:
                locus_non_iea_direct[locus].add(go_id)
                
            total_annotations += 1
            
    print(f"    Loaded {total_annotations} valid annotations across {len(locus_go_direct)} unique loci.")
    print(f"    QC: Excluded {skipped_not} NOT; Excluded {skipped_obsolete} obsolete; Excluded {skipped_root} root terms; Resolved {resolved_alt} alt, {resolved_rep} replaced.")
    
    # Propagate terms and non-IEA evidence hierarchically
    print("    Propagating terms and non-IEA evidence along DAG...")
    locus_go_prop = defaultdict(lambda: {"BP": set(), "MF": set(), "CC": set()})
    locus_non_iea_prop = defaultdict(set)
    
    for locus, ns_dict in locus_go_direct.items():
        direct_non_iea_set = locus_non_iea_direct[locus]
        
        for ns, t_set in ns_dict.items():
            prop_set = set(t_set)
            for t in t_set:
                t_has_non_iea = (t in direct_non_iea_set)
                if t_has_non_iea:
                    locus_non_iea_prop[locus].add(t)
                    
                for anc in ancestors_map.get(t, set()):
                    if anc not in ROOT_TERMS and anc in terms and terms[anc]["namespace"] == ns:
                        prop_set.add(anc)
                        if t_has_non_iea:
                            locus_non_iea_prop[locus].add(anc)
                            
            locus_go_prop[locus][ns] = prop_set
            
    return locus_go_direct, locus_go_prop, locus_non_iea_direct, locus_non_iea_prop, locus_ev_codes, gaf_version, gaf_date

def parse_kegg(links_path, list_path):
    print(f"[*] Parsing KEGG pathway files: {links_path}, {list_path}")
    path_names = {}
    with open(list_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                pid = parts[0].replace("path:", "").strip()
                pname = parts[1].split(" - ")[0].strip()
                path_names[pid] = pname
                
    locus_kegg = defaultdict(lambda: {"pathways": set(), "pathway_names": set()})
    with open(links_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                loc = parts[0].replace("ath:", "").strip().upper()
                pid = parts[1].replace("path:", "").strip()
                pname = path_names.get(pid, pid)
                locus_kegg[loc]["pathways"].add(pid)
                locus_kegg[loc]["pathway_names"].add(pname)
                
    print(f"    Loaded KEGG annotations for {len(locus_kegg)} unique Arabidopsis loci across {len(path_names)} pathways.")
    return locus_kegg

def main():
    default_macro = str(Path(__file__).resolve().parents[3])
    default_enrich = str(Path(__file__).resolve().parents[3] / "04_gene_families" / "functional_enrichment")
    base_dir = os.environ.get("FAMILY_ENRICHMENT_DIR", default_enrich)
    input_dir = os.path.join(base_dir, "input")
    results_dir = os.path.join(base_dir, "results")
    macro_dir = os.environ.get("FAMILY_MACRO_DIR", default_macro)
    inter_dir = os.path.join(base_dir, "intermediate")
    os.makedirs(inter_dir, exist_ok=True)
    
    # 1. Parse OBO Ontology
    obo_file = os.path.join(input_dir, "raw_annotations", "go-basic.obo")
    terms, alt_map, replaced_map, ancestors_map, obo_ver = parse_obo(obo_file)
    
    # 2. Parse GAF File
    gaf_file = os.path.join(input_dir, "raw_annotations", "ARATH-mod.gaf.gz")
    loc_go_dir, loc_go_prop, loc_non_iea_dir, loc_non_iea_prop, loc_ev_codes, gaf_ver, gaf_date = parse_gaf(
        gaf_file, terms, alt_map, replaced_map, ancestors_map
    )
    
    # 3. Parse KEGG
    kegg_links = os.path.join(input_dir, "raw_annotations", "kegg", "ath_pathway_links.tsv")
    kegg_list = os.path.join(input_dir, "raw_annotations", "kegg", "ath_pathway_list.tsv")
    loc_kegg = parse_kegg(kegg_links, kegg_list)
    
    # 4. Parse Arabidopsis CDS fasta for mapping
    cds_file = os.path.join(macro_dir, "00_data", "cds_outgroups", "Ath.cds.fa")
    print(f"[*] Parsing Ath.cds.fa for sequence-to-locus reconciliation: {cds_file}")
    seq_to_locus = {}
    with open(cds_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith(">"):
                header = line[1:].strip()
                seq_id = header.split()[0]
                m = re.search(r'\[locus_tag=([^\]]+)\]', header)
                if m:
                    seq_to_locus[seq_id] = m.group(1).upper()
                else:
                    m2 = re.search(r'(AT[1-5MC]G\d+)', header)
                    if m2:
                        seq_to_locus[seq_id] = m2.group(1).upper()
                        
    print(f"    Loaded {len(seq_to_locus)} sequence header mappings from Ath.cds.fa.")
    
    # 5. Parse Orthogroups.tsv for Ath.pep members
    og_file = os.path.join(macro_dir, "01_orthology", "results", "Results_Aug30", "Orthogroups", "Orthogroups.tsv")
    print(f"[*] Parsing Orthogroups.tsv: {og_file}")
    df_og = pd.read_csv(og_file, sep="\t")
    
    master_file = os.environ.get("FAMILY_MASTER_TABLE", os.path.join(macro_dir, "04_gene_families", "comparative_axes", "comparative_families_master_table_v2.tsv"))
    df_master = pd.read_csv(master_file, sep="\t").set_index("FamilyID")
    
    df_og_master = df_og[df_og["Orthogroup"].isin(df_master.index)].set_index("Orthogroup")
    
    og_to_seqs = {}
    og_to_loci = {}
    seq_rows = []
    unmapped_seqs = []
    
    for fam_id in df_master.index:
        if fam_id in df_og_master.index:
            ath_val = df_og_master.loc[fam_id, "Ath.pep"]
            if pd.notna(ath_val) and str(ath_val).strip() != "":
                seqs = [s.strip() for s in str(ath_val).split(",") if s.strip()]
            else:
                seqs = []
        else:
            seqs = []
        og_to_seqs[fam_id] = seqs
        
        loci_set = set()
        for s in seqs:
            if s in seq_to_locus:
                loc = seq_to_locus[s]
                loci_set.add(loc)
                seq_rows.append({
                    "FamilyID": fam_id,
                    "Ath_Sequence_ID": s,
                    "Ath_Locus_Tag": loc,
                    "Mapping_Status": "MAPPED"
                })
            else:
                unmapped_seqs.append(s)
                seq_rows.append({
                    "FamilyID": fam_id,
                    "Ath_Sequence_ID": s,
                    "Ath_Locus_Tag": "UNMAPPED",
                    "Mapping_Status": "UNMAPPED_HEADER"
                })
        og_to_loci[fam_id] = sorted(list(loci_set))
        
    df_seq_map = pd.DataFrame(seq_rows, columns=['FamilyID', 'Ath_Sequence_ID', 'Ath_Locus_Tag', 'Mapping_Status'])
    seq_map_out = os.path.join(inter_dir, "ath_sequence_to_locus.tsv")
    df_seq_map.to_csv(seq_map_out, sep="\t", index=False)
    print(f"[*] Saved intermediate mapping: {seq_map_out}")
    print(f"    Total sequences mapped: {len(df_seq_map)}")
    print(f"    Total unique loci mapped: {df_seq_map['Ath_Locus_Tag'].nunique()}")
    print(f"    Unmapped sequence count: {len(unmapped_seqs)}")
    
    # Validation Control 1 check
    expected_sequences = sum(len(seqs) for seqs in og_to_seqs.values())
    if not df_master.index.is_unique or not df_og_master.index.is_unique or set(df_master.index) != set(df_og_master.index) or len(df_seq_map) != expected_sequences or len(unmapped_seqs) > 0 or df_seq_map.duplicated(['FamilyID', 'Ath_Sequence_ID']).any():
        raise ValueError(f"Control 1 Failure! fams={len(df_master)}, seqs={len(df_seq_map)}, unmapped={len(unmapped_seqs)}")
    print(f"    [PASSED] Validation Control 1: {len(df_master)} families and {expected_sequences} Ath.pep reconciled.")

    species_cols = ["Count_Abra", "Count_Ath", "Count_Dala", "Count_Ptec", "Count_Vper", "Count_Vtub", "Count_Xvis"]
    
    print("[*] Consolidating functional annotations per FamilyID...")
    master_ann_rows = []
    
    qc_stats = {
        "Total_Families": len(df_master),
        "Families_With_Loci": 0,
        "Families_With_GO_Direct": 0,
        "Families_With_GO_BP_Direct": 0,
        "Families_With_GO_MF_Direct": 0,
        "Families_With_GO_CC_Direct": 0,
        "Families_With_GO_Propagated": 0,
        "Families_With_GO_BP_Propagated": 0,
        "Families_With_GO_MF_Propagated": 0,
        "Families_With_GO_CC_Propagated": 0,
        "Families_With_Non_IEA": 0,
        "Families_With_KEGG": 0,
        "BranchSig_Exp_Vper_Total": 0,
        "BranchSig_Exp_Vper_With_GO": 0,
        "BranchSig_Exp_Vper_With_KEGG": 0
    }
    
    focal_fams = set(df_master[df_master["BranchSig_Exp_Vper"] == True].index)
    qc_stats["BranchSig_Exp_Vper_Total"] = len(focal_fams)
    
    for fam_id, row in df_master.iterrows():
        seqs = og_to_seqs[fam_id]
        loci = og_to_loci[fam_id]
        n_loci = len(loci)
        n_proteins_tot = row["Total_Count"]
        n_species_pres = (row[species_cols] > 0).sum()
        
        direct_bp = set()
        direct_mf = set()
        direct_cc = set()
        
        prop_bp = set()
        prop_mf = set()
        prop_cc = set()
        
        non_iea_dir_terms = set()
        non_iea_prop_terms = set()
        
        ev_codes = set()
        annotated_loci = set()
        
        kegg_pathways = set()
        kegg_genes = set()
        
        if n_loci > 0:
            qc_stats["Families_With_Loci"] += 1
            
        for loc in loci:
            if loc in loc_go_dir:
                annotated_loci.add(loc)
                direct_bp.update(loc_go_dir[loc]["BP"])
                direct_mf.update(loc_go_dir[loc]["MF"])
                direct_cc.update(loc_go_dir[loc]["CC"])
                
                prop_bp.update(loc_go_prop[loc]["BP"])
                prop_mf.update(loc_go_prop[loc]["MF"])
                prop_cc.update(loc_go_prop[loc]["CC"])
                
                non_iea_dir_terms.update(loc_non_iea_dir[loc])
                non_iea_prop_terms.update(loc_non_iea_prop[loc])
                
                ev_codes.update(loc_ev_codes[loc])
                
            if loc in loc_kegg:
                kegg_genes.add(loc)
                kegg_pathways.update(loc_kegg[loc]["pathways"])
                
        has_any_go_dir = bool(direct_bp or direct_mf or direct_cc)
        has_any_go_prop = bool(prop_bp or prop_mf or prop_cc)
        has_non_iea = bool(non_iea_prop_terms)
        
        if has_any_go_dir: qc_stats["Families_With_GO_Direct"] += 1
        if direct_bp: qc_stats["Families_With_GO_BP_Direct"] += 1
        if direct_mf: qc_stats["Families_With_GO_MF_Direct"] += 1
        if direct_cc: qc_stats["Families_With_GO_CC_Direct"] += 1
        
        if has_any_go_prop: qc_stats["Families_With_GO_Propagated"] += 1
        if prop_bp: qc_stats["Families_With_GO_BP_Propagated"] += 1
        if prop_mf: qc_stats["Families_With_GO_MF_Propagated"] += 1
        if prop_cc: qc_stats["Families_With_GO_CC_Propagated"] += 1
        
        if has_non_iea: qc_stats["Families_With_Non_IEA"] += 1
        if kegg_pathways: qc_stats["Families_With_KEGG"] += 1
        
        if fam_id in focal_fams:
            if has_any_go_prop: qc_stats["BranchSig_Exp_Vper_With_GO"] += 1
            if kegg_pathways: qc_stats["BranchSig_Exp_Vper_With_KEGG"] += 1
            
        vper_desc = row.get("EggNOG_Description", "Sem anotacao EggNOG recuperada")
        vtub_desc = row.get("EggNOG_Description", "Sem anotacao EggNOG recuperada")
        
        master_ann_rows.append({
            "FamilyID": fam_id,
            "Ath_Sequence_IDs": ";".join(seqs),
            "Ath_Locus_Tags": ";".join(loci),
            "N_Ath_Loci": n_loci,
            "N_Proteins_Total": n_proteins_tot,
            "N_Species_Present": n_species_pres,
            "GO_BP_Direct": ";".join(sorted(direct_bp)),
            "GO_MF_Direct": ";".join(sorted(direct_mf)),
            "GO_CC_Direct": ";".join(sorted(direct_cc)),
            "GO_BP_Propagated": ";".join(sorted(prop_bp)),
            "GO_MF_Propagated": ";".join(sorted(prop_mf)),
            "GO_CC_Propagated": ";".join(sorted(prop_cc)),
            "GO_Non_IEA_Direct_Terms": ";".join(sorted(non_iea_dir_terms)),
            "GO_Non_IEA_Propagated_Terms": ";".join(sorted(non_iea_prop_terms)),
            "GO_Evidence_Codes": ";".join(sorted(ev_codes)),
            "N_GO_Annotated_Loci": len(annotated_loci),
            "Has_Non_IEA": has_non_iea,
            "KEGG_Genes": ";".join(sorted(kegg_genes)),
            "KEGG_Pathways": ";".join(sorted(kegg_pathways)),
            "Vper_Annotation": vper_desc,
            "Vtub_Annotation": vtub_desc,
            "Annotation_Sources": "TAIR_GAF;KEGG_Pathways",
            "Annotation_Versions": f"ARATH-mod.gaf:{gaf_ver}(gen:{gaf_date});go-basic.obo:{obo_ver};KEGG:ath:2026-09-04"
        })
        
    df_master_ann = pd.DataFrame(master_ann_rows)
    master_ann_tsv = os.path.join(results_dir, "orthogroup_functional_annotations.tsv")
    df_master_ann.to_csv(master_ann_tsv, sep="\t", index=False)
    print(f"[*] Saved Master Annotations Table: {master_ann_tsv} ({len(df_master_ann)} rows)")
    
    # Save functional_annotation_qc.tsv
    qc_rows = []
    for k, v in qc_stats.items():
        pct = (v / qc_stats["Total_Families"]) * 100 if "Total" not in k else 100.0
        if "BranchSig_Exp_Vper" in k and k != "BranchSig_Exp_Vper_Total":
            pct = (v / qc_stats["BranchSig_Exp_Vper_Total"]) * 100.0
        qc_rows.append({"Metric": k, "Value": v, "Percentage": f"{pct:.2f}%"})
        
    df_qc = pd.DataFrame(qc_rows)
    qc_tsv = os.path.join(results_dir, "functional_annotation_qc.tsv")
    df_qc.to_csv(qc_tsv, sep="\t", index=False)
    print(f"[*] Saved QC Summary: {qc_tsv}")
    for _, r in df_qc.iterrows():
        print(f"    {r['Metric']:32s}: {r['Value']:>6} ({r['Percentage']})")

if __name__ == "__main__":
    main()
