import os
from ete3 import Tree, TreeStyle, NodeStyle, TextFace

tree_file = "/home/mfcaval/github/doutorado/analyses/02_phylogeny/results/iqtree.renamed.treefile"
out_pdf = "/home/mfcaval/github/doutorado/reports/figures/02_phylogeny/OSCA_phylogenetic_tree.pdf"
out_png = "/home/mfcaval/github/doutorado/reports/figures/02_phylogeny/OSCA_phylogenetic_tree.png"

# Colors for clades
# OSCA1: Blue (#1f77b4), OSCA2: Orange (#ff7f0e), OSCA3: Green (#2ca02c), OSCA4: Red (#d62728)
def get_color(name):
    if not name:
        return 'black'
    if 'OSCA1' in name or 'AT1' in name or 'AT4G04340' in name or 'AT4G22120' in name or 'AT1G62320' in name or 'AT1G11960' in name or 'AT4G15430' in name or 'AT3G21620' in name or 'AT4G02900' in name or 'AT1G32090' in name:
        return '#1f77b4'
    if 'OSCA2' in name or 'AT3G54510' in name or 'AT1G58520' in name or 'AT1G10090' in name or 'AT1G69450' in name or 'AT3G01100' in name:
        return '#ff7f0e'
    if 'OSCA3' in name or 'AT1G30360' in name:
        return '#2ca02c'
    if 'OSCA4' in name or 'AT4G35870' in name:
        return '#d62728'
    return 'black'

# Load tree
t = Tree(tree_file)
t.ladderize()

# Create a TreeStyle
ts = TreeStyle()
ts.show_leaf_name = False
ts.mode = "r" # rectangular
ts.scale = 120 # pixel per branch length unit

# Iterate over all nodes
for n in t.traverse():
    ns = NodeStyle()
    
    # Hide internal nodes visually
    if not n.is_leaf():
        ns["size"] = 0
    else:
        ns["size"] = 0
        color = get_color(n.name)
        
        # Add the leaf name as a TextFace with the clade color
        face = TextFace(n.name, fsize=10, fgcolor=color)
        face.margin_left = 5
        n.add_face(face, column=0, position="branch-right")
        
    n.set_style(ns)

# Ensure output directory exists
os.makedirs(os.path.dirname(out_pdf), exist_ok=True)

# Save
t.render(out_pdf, w=800, units="px", tree_style=ts)
t.render(out_png, w=800, units="px", tree_style=ts)
print("Phylogenetic tree saved successfully!")
