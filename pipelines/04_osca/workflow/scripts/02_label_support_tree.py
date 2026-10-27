#!/usr/bin/env python3
"""Annotate IQ-TREE support consensus tree tips for HyPhy-compatible use."""
import re
from pathlib import Path
from Bio import Phylo

ROOT = Path(__file__).resolve().parents[3]
src = ROOT / "analyses/02_phylogeny/results_support/iqtree_support.contree"
out = ROOT / "analyses/02_phylogeny/results_support/iqtree_support_labeled.treefile"
summary = ROOT / "analyses/02_phylogeny/results_support/osca24_support.tsv"

raw = src.read_text().strip()
raw = re.sub(r"(Vtub\.[^,:()]+)(?=[:,)])", r"\1{Test}", raw)
raw = re.sub(r"(Vper\.[^,:()]+)(?=[:,)])", r"\1{Reference}", raw)
out.write_text(raw + "\n")

tree = Phylo.read(str(src), "newick")
targets = {
    "cross_species_2.4b": {
        "Vtub.hapA.v1.chr1A.g020650.t1", "Vper.hapA.v1.chr1A.g023020.t1"
    },
    "osca2.4_cluster": {
        "Vtub.hapA.v1.chr1A.g020650.t1", "Vper.hapA.v1.chr1A.g023020.t1",
        "Vper.hapA.v1.chr1A.g023030.t1"
    },
}
with summary.open("w") as fh:
    fh.write("clade\tn_leaves\tsupport\tleaves\n")
    for name, target in targets.items():
        matches = []
        for clade in tree.find_clades(order="postorder"):
            leaves = {x.name for x in clade.get_terminals()}
            if leaves == target:
                matches.append(clade)
        if len(matches) != 1:
            raise RuntimeError(f"Expected one clade for {name}, found {len(matches)}")
        c = matches[0]
        fh.write(f"{name}\t{len(target)}\t{c.confidence}\t{';'.join(sorted(target))}\n")
print(out)
print(summary)
