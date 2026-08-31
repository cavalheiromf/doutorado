#!/usr/bin/env python3
"""
Lightweight helper tool & API to query the Vellozia Annotation Databases.
Usage from command line:
    python3 vellozia_query.py --species Vtub --query "translocon"
    python3 vellozia_query.py --species Vper --expanding
    python3 vellozia_query.py --gene Vtub.hapA.v1.chr1A.g000010.t1
"""

import sqlite3
import argparse
import os
import pandas as pd

DB_VTUB = '/home/mfcaval/github/doutorado/data/genomes/Vtub/vtub_annotation.db'
DB_VPER = '/home/mfcaval/github/doutorado/data/genomes/Vper/vper_annotation.db'
DB_MASTER = '/home/mfcaval/github/doutorado/analyses/chapter_1_genomics/annotation_db/vellozia_master_annotation.db'

def get_connection(species='all'):
    if species.lower() in ['vtub', 'vellozia_tubiflora']:
        return sqlite3.connect(DB_VTUB)
    elif species.lower() in ['vper', 'vellozia_peripherica']:
        return sqlite3.connect(DB_VPER)
    else:
        return sqlite3.connect(DB_MASTER)

def query_by_keyword(keyword, species='all', limit=20):
    conn = get_connection(species)
    sql = f"""
    SELECT transcript_id, species, chromosome, start, end, protein_len_aa, orthogroup_id, expansion_status, delta_change, eggnog_desc
    FROM v_master_annotation
    WHERE eggnog_desc LIKE ?
    LIMIT ?;
    """
    df = pd.read_sql_query(sql, conn, params=(f'%{keyword}%', limit))
    conn.close()
    return df

def query_by_gene_id(gene_or_tx_id):
    conn = get_connection('all')
    sql = """
    SELECT * FROM v_master_annotation
    WHERE transcript_id = ? OR gene_id = ?;
    """
    df = pd.read_sql_query(sql, conn, params=(gene_or_tx_id, gene_or_tx_id))
    conn.close()
    return df

def query_expanding_families(species='all', limit=20):
    conn = get_connection(species)
    sql = """
    SELECT orthogroup_id, species, COUNT(transcript_id) as gene_count, delta_change, eggnog_desc
    FROM v_master_annotation
    WHERE expansion_status = 'Expanded' AND family_is_significant = 1
    GROUP BY orthogroup_id, species
    ORDER BY delta_change DESC
    LIMIT ?;
    """
    df = pd.read_sql_query(sql, conn, params=(limit,))
    conn.close()
    return df

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Query Vellozia Annotation Databases")
    parser.add_argument('--species', choices=['Vtub', 'Vper', 'all'], default='all', help="Target species database")
    parser.add_argument('--query', type=str, help="Keyword search in functional annotation")
    parser.add_argument('--gene', type=str, help="Exact transcript or gene ID lookup")
    parser.add_argument('--expanding', action='store_true', help="List significantly expanding families")
    parser.add_argument('--limit', type=int, default=15, help="Number of records to display")
    
    args = parser.parse_args()
    
    if args.gene:
        res = query_by_gene_id(args.gene)
        print(f"=== LOOKUP RESULT FOR {args.gene} ===")
        print(res.to_string(index=False) if not res.empty else "No matching record found.")
    elif args.expanding:
        res = query_expanding_families(args.species, args.limit)
        print(f"=== TOP EXPANDING FAMILIES IN {args.species.upper()} ===")
        print(res.to_string(index=False))
    elif args.query:
        res = query_by_keyword(args.query, args.species, args.limit)
        print(f"=== KEYWORD SEARCH '{args.query}' IN {args.species.upper()} ===")
        print(res.to_string(index=False) if not res.empty else "No matching records found.")
    else:
        parser.print_help()

