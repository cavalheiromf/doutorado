#!/usr/bin/env python3
"""Re-estimate pairwise Ka/Ks from explicit PAL2NAL codon alignments."""
import csv
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "results"
OUTPUT = ROOT / "results_pal2nal_yn00"
BIN = Path("/home/mfcaval/.local/share/mamba/envs/jcviEnv/bin")
PAL2NAL = BIN / "pal2nal.pl"
YN00 = BIN / "yn00"


def main():
    OUTPUT.mkdir(exist_ok=True)
    rows = []
    for pair in sorted(p for p in INPUT.glob("Vp*_*" ) if p.is_dir()):
        pep = pair / "pep.aln"
        cds = pair / "cds.fna"
        if not pep.exists() or not cds.exists():
            continue
        out = OUTPUT / pair.name
        out.mkdir(exist_ok=True)
        codon = out / "codon.paml"
        ynout = out / "yn00.out"
        ctl = out / "yn00.ctl"
        if ynout.exists():
            ynout.unlink()
        subprocess.run(
            [str(PAL2NAL), str(pep), str(cds), "-output", "paml", "-nogap", "-nomismatch"],
            check=True, stdout=codon.open("w"), stderr=subprocess.PIPE, text=True,
        )
        ctl.write_text(
            "seqfile = codon.paml\noutfile = yn00.out\nverbose = 0\n"
            "icode = 0\nweighting = 0\ncommonf3x4 = 0\n"
        )
        # Keep paths short: this PAML build has a fixed-size path buffer.
        subprocess.run([str(YN00), "yn00.ctl"], cwd=out, check=True,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        text = ynout.read_text()
        m = re.search(r"^\s*2\s+1\s+\S+\s+\S+\s+\S+\s+\S+\s+(\S+)\s+(\S+)\s+\+-\s+\S+\s+(\S+)\s+\+-\s+\S+", text, re.M)
        if not m:
            raise RuntimeError(f"Could not parse YN00 output: {ynout}")
        omega, ka, ks = map(float, m.groups())
        rows.append({"Pair_Name": pair.name, "YN00_Ks": ks, "YN00_Ka": ka,
                     "Ka/Ks": omega})
    with (OUTPUT / "aggregated_kaks_pal2nal_yn00.csv").open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["Pair_Name", "YN00_Ks", "YN00_Ka", "Ka/Ks"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} pairs to {OUTPUT}")


if __name__ == "__main__":
    main()
