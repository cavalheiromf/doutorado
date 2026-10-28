#!/usr/bin/env python3
"""Pairwise codeml estimates from PAL2NAL codon alignments."""
import csv
import os
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "results_pal2nal_yn00"
OUTPUT = ROOT / "results_codeml_pairwise"
CODEML = Path(os.environ.get("CODEML_BIN") or shutil.which("codeml") or "codeml")

CTL = """seqfile = codon.paml
outfile = codeml.out
treefile = codon.tree
noisy = 0
verbose = 0
runmode = -2
seqtype = 1
CodonFreq = 2
clock = 0
icode = 0
fix_kappa = 0
kappa = 2
fix_omega = 0
omega = 0.4
model = 0
NSsites = 0
Small_Diff = 1e-6
cleandata = 1
"""


def main():
    OUTPUT.mkdir(exist_ok=True)
    rows = []
    for pair in sorted(p for p in INPUT.glob("Vp*_*" ) if p.is_dir()):
        if not (pair / "codon.paml").exists():
            continue
        out = OUTPUT / pair.name
        out.mkdir(exist_ok=True)
        (out / "codon.paml").write_bytes((pair / "codon.paml").read_bytes())
        (out / "codon.tree").write_text("(1 2);\n")
        (out / "codeml.ctl").write_text(CTL)
        for stale in ("codeml.out", "2ML.dN", "2ML.dS", "rst", "rub", "lnf"):
            path = out / stale
            if path.exists():
                path.unlink()
        subprocess.run([str(CODEML), "codeml.ctl"], cwd=out, check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        text = (out / "codeml.out").read_text()
        m = re.search(r"dN/dS=\s*([0-9.eE+-]+)\s+dN\s*=\s*([0-9.eE+-]+)\s+dS\s*=\s*([0-9.eE+-]+)", text)
        if not m:
            raise RuntimeError(f"Could not parse codeml output: {out / 'codeml.out'}")
        omega, ka, ks = map(float, m.groups())
        rows.append({"Pair_Name": pair.name, "codeml_Ks": ks,
                     "codeml_Ka": ka, "Ka/Ks": omega})
    with (OUTPUT / "aggregated_kaks_codeml_pairwise.csv").open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["Pair_Name", "codeml_Ks", "codeml_Ka", "Ka/Ks"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} pairs to {OUTPUT}")


if __name__ == "__main__":
    main()
