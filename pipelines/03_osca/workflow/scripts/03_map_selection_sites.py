#!/usr/bin/env python3
import csv
from pathlib import Path

# Translate dictionary
CODON_TABLE = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 'TGA':'_'
}

def translate(codon):
    return CODON_TABLE.get(codon.upper(), 'X')

def read_fasta(path: Path) -> dict:
    records = {}
    name = None
    chunks = []
    with path.open() as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if name is not None:
                    records[name] = "".join(chunks).upper()
                name = line[1:].split()[0]
                chunks = []
            else:
                chunks.append(line)
    if name is not None:
        records[name] = "".join(chunks).upper()
    return records

def main():
    root = Path(__file__).resolve().parents[3]
    analysis_dir = root / "analyses/03_synteny"
    gene_id_dir = root / "analyses/01_gene_identification/results"
    
    # 1. Load ID mapping
    id_mapping = {}
    with (gene_id_dir / "oscasIDs.txt").open() as f:
        for line in f:
            if line.strip():
                parts = line.strip().split("\t")
                if len(parts) == 2:
                    id_mapping[parts[0]] = parts[1]
                    # Also support underscore version for matching headers
                    id_mapping[parts[0].replace(".", "_")] = parts[1]

    # 2. Load Pfam domains
    domains = {}  # gene -> list of (start, end, domain_name)
    for filename in ["Vper.osca.tsv", "Vtub.osca.tsv"]:
        path = gene_id_dir / filename
        if not path.exists():
            continue
        with path.open() as f:
            reader = csv.DictReader(f, delimiter="\t")
            for row in reader:
                gene = row.get("gene") or row.get("id")
                if not gene:
                    continue
                if gene not in domains:
                    domains[gene] = []
                domains[gene].append({
                    "start": int(row["start"]),
                    "end": int(row["end"]),
                    "domain": row["domain"]
                })

    # 3. Read Contrast-FEL nominal sites
    contrast_fel_summary_path = analysis_dir / "hyphy_rerun_20260716/contrast_fel_summary.tsv"
    nominal_sites_by_dataset = {}
    with contrast_fel_summary_path.open() as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            dataset = row["dataset"]
            sites_str = row["nominal_sites"].strip()
            if sites_str:
                nominal_sites_by_dataset[dataset] = [int(x) for x in sites_str.split(",")]
            else:
                nominal_sites_by_dataset[dataset] = []

    # Alignments lookup
    alignments_paths = {
        "global": analysis_dir / "hyphy_analysis/vellozia_oscas_codon.fasta",
        "osca1": analysis_dir / "hyphy_subclades/osca1/osca1_codon.fasta",
        "osca2": analysis_dir / "hyphy_subclades/osca2/osca2_codon.fasta",
        "osca3_4": analysis_dir / "hyphy_subclades/osca3_4/osca3_4_codon.fasta",
    }

    results = []

    for dataset, nominal_sites in nominal_sites_by_dataset.items():
        if not nominal_sites:
            continue
        
        # Load site map
        site_map_path = analysis_dir / f"hyphy_validation_20260716/filtered_alignments/gap20/{dataset}/site_map.tsv"
        site_map = {} # original -> filtered
        with site_map_path.open() as f:
            reader = csv.DictReader(f, delimiter="\t")
            for row in reader:
                if row["original_codon_site"]:
                    site_map[int(row["original_codon_site"])] = row["filtered_codon_site"]

        # Load alignment
        alignment_path = alignments_paths[dataset]
        alignment = read_fasta(alignment_path)

        for original_site in nominal_sites:
            filtered_site = site_map.get(original_site, "N/A")

            for header, seq in alignment.items():
                # Check if it's a Vellozia sequence
                is_vper = "Vper" in header or "Vp" in header or header.startswith("VpOSCA")
                is_vtub = "Vtub" in header or "Vt" in header or header.startswith("VtOSCA")
                if not (is_vper or is_vtub):
                    continue

                # Get short gene name
                short_name = id_mapping.get(header, header)

                # Map alignment site to native coordinate
                native_pos = 0
                target_codon = ""
                for site_idx in range(original_site):
                    codon = seq[site_idx * 3 : site_idx * 3 + 3]
                    if "-" not in codon:
                        native_pos += 1
                        if site_idx == original_site - 1:
                            target_codon = codon

                # If the target codon has gap, then this sequence has gap at this position
                if not target_codon or "-" in target_codon:
                    residue = "-"
                    native_pos_str = "Gap"
                    domain_found = "Gap"
                else:
                    residue = translate(target_codon)
                    native_pos_str = str(native_pos)
                    
                    # Find domain
                    domain_found = "None (Linker)"
                    gene_domains = domains.get(short_name, [])
                    for dom in gene_domains:
                        if dom["start"] <= native_pos <= dom["end"]:
                            domain_found = dom["domain"]
                            break

                results.append({
                    "Dataset": dataset,
                    "FilteredSite": filtered_site,
                    "OriginalSite": original_site,
                    "GeneID": header,
                    "GeneShortName": short_name,
                    "NativeResidue": residue,
                    "NativePosition": native_pos_str,
                    "Domain": domain_found
                })

    # Save results
    out_dir = analysis_dir / "results"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "selection_sites_to_domains.tsv"
    
    with out_file.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "Dataset", "FilteredSite", "OriginalSite", "GeneID", 
            "GeneShortName", "NativeResidue", "NativePosition", "Domain"
        ], delimiter="\t")
        writer.writeheader()
        writer.writerows(results)

    # Print summary
    print(f"Results written to: {out_file}")
    print("\nSummary by Dataset and Domain:")
    summary = {}
    for r in results:
        key = (r["Dataset"], r["Domain"])
        summary[key] = summary.get(key, 0) + 1
    
    for key, count in sorted(summary.items()):
        print(f"Dataset: {key[0]} | Domain: {key[1]} | Count: {count}")

if __name__ == "__main__":
    main()
