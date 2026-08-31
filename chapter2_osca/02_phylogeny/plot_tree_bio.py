import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from Bio import Phylo
import os

tree_file = "/home/mfcaval/github/doutorado/analyses/02_phylogeny/results/iqtree.renamed.treefile"
out_pdf = "/home/mfcaval/github/doutorado/reports/figures/02_phylogeny/OSCA_phylogenetic_tree.pdf"
out_png = "/home/mfcaval/github/doutorado/reports/figures/02_phylogeny/OSCA_phylogenetic_tree.png"

def get_color(name):
    if not name:
        return 'black'
    if 'OSCA1' in name or 'AT1G32090' in name or 'AT4G02900' in name or 'AT4G04340' in name or 'AT4G22120' in name or 'AT1G62320' in name or 'AT1G11960' in name or 'AT4G15430' in name or 'AT3G21620' in name:
        return '#1f77b4'
    if 'OSCA2' in name or 'AT3G54510' in name or 'AT1G58520' in name or 'AT1G10090' in name or 'AT1G69450' in name or 'AT3G01100' in name:
        return '#ff7f0e'
    if 'OSCA3' in name or 'AT1G30360' in name:
        return '#2ca02c'
    if 'OSCA4' in name or 'AT4G35870' in name:
        return '#d62728'
    return 'black'

def label_colors(label):
    return get_color(label)

tree = Phylo.read(tree_file, "newick")
tree.ladderize()

fig, ax = plt.subplots(figsize=(12, 16))

# We can customize the drawing by passing label_colors dictionary or function in newer biopython, 
# but biopython Phylo.draw label_colors takes a dict or a func mapping labels to colors.
Phylo.draw(tree, do_show=False, axes=ax, label_func=lambda x: x.name if x.name else "", label_colors=label_colors, show_confidence=False)

# Make the lines gray so labels pop out
for collection in ax.collections:
    collection.set_color('#333333')
    collection.set_linewidth(1.0)

os.makedirs(os.path.dirname(out_pdf), exist_ok=True)
plt.savefig(out_pdf, bbox_inches='tight', dpi=300)
plt.savefig(out_png, bbox_inches='tight', dpi=300)
print("Phylogenetic tree saved successfully via Biopython!")
