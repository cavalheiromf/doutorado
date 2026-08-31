import json

vper_file = "/home/mfcaval/github/doutorado/analyses/04_promoters/results/Vper.osca.coords.bed"
vtub_file = "/home/mfcaval/github/doutorado/analyses/04_promoters/results/Vtub.osca.coords.bed"

def parse_bed(filepath, species_name):
    genes = []
    with open(filepath) as f:
        for line in f:
            if not line.strip(): continue
            parts = line.strip().split("\t")
            chrom, start, end, gene_id, _, strand = parts
            
            # Extract clade (e.g., OSCA1 from VpOSCA1.1)
            # The gene_id looks like VpOSCA1.1 or VtOSCA2.4
            clade = gene_id[2:7] # 'OSCA1'
            genes.append({
                "Species": species_name,
                "Gene Name": gene_id,
                "Clade": clade,
                "Chromosome": chrom,
                "Start": start,
                "End": end,
                "Strand": strand
            })
    return genes

all_genes = parse_bed(vper_file, "V. peripherica") + parse_bed(vtub_file, "V. tubiflora")

# Sort by species, then Clade, then Chromosome, then Start
all_genes.sort(key=lambda x: (x["Species"], x["Clade"], x["Chromosome"], int(x["Start"])))

md_table = "## Table 1: OSCA Gene Family Identification in *Vellozia* Species\n\n"
md_table += "| Species | Gene Name | Clade | Chromosome | Start | End | Strand |\n"
md_table += "|---|---|---|---|---|---|---|\n"

for g in all_genes:
    md_table += f"| *{g['Species']}* | {g['Gene Name']} | {g['Clade']} | {g['Chromosome']} | {g['Start']} | {g['End']} | {g['Strand']} |\n"

with open("/home/mfcaval/github/doutorado/docs/table_1.md", "w") as f:
    f.write(md_table)
    
print("Table 1 generated successfully at docs/table_1.md")
