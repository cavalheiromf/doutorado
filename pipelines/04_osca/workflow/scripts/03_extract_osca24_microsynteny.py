#!/usr/bin/env python3
"""Generate a dedicated microsynteny plot for the OSCA2.4 locus."""

from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BED_VPER = ROOT / "data" / "Vper.bed"
BED_VTUB = ROOT / "data" / "Vtub.bed"
ANCHORS = ROOT / "intergenomic" / "intermediates" / "Vper.Vtub.anchors"
WORK = ROOT / "microsynteny_osca24"
OUT = ROOT / "results" / "microsynteny_plots" / "osca24_chr1A.pdf"

TARGETS = {
    "Vper": ["Vper.hapA.v1.chr1A.g023020.t1", "Vper.hapA.v1.chr1A.g023030.t1"],
    "Vtub": ["Vtub.hapA.v1.chr1A.g020650.t1"],
}


def read_bed(path):
    genes = []
    with path.open() as handle:
        for line in handle:
            fields = line.rstrip("\n").split("\t")
            if len(fields) >= 4:
                genes.append(fields[3])
    return genes


def main():
    vper, vtub = read_bed(BED_VPER), read_bed(BED_VTUB)
    vper_indices = [vper.index(g) for g in TARGETS["Vper"]]
    vtub_indices = [vtub.index(g) for g in TARGETS["Vtub"]]
    vper_window = set(vper[max(0, min(vper_indices) - 15): max(vper_indices) + 16])
    vtub_window = set(vtub[max(0, min(vtub_indices) - 15): max(vtub_indices) + 16])

    links = []
    with ANCHORS.open() as handle:
        for line in handle:
            if line.startswith("#") or not line.strip():
                continue
            a, b = line.rstrip("\n").split("\t")[:2]
            if a in vper_window and b in vtub_window:
                links.append((a, b))

    WORK.mkdir(parents=True, exist_ok=True)
    blocks = WORK / "osca24.blocks"
    blocks.write_text("".join(f"{a}\t{b}\n" for a, b in links))
    (WORK / "osca24.layout").write_text(
        "# x, y, rotation, ha, va, color, ratio, label\n"
        "0.5, 0.6, 0, left, center, m, 1, vp_chr1A\n"
        "0.5, 0.4, 0, left, center, #fc8d62, 1, vt_chr1A\n"
        "# edges\n"
        "e, 0, 1\n"
    )
    command = [
        "/home/mfcaval/.local/share/mamba/envs/jcviEnv/bin/python", "-m",
        "jcvi.graphics.synteny", str(blocks), str(ROOT / "data" / "all.bed"),
        str(WORK / "osca24.layout"), "--notex",
    ]
    subprocess.run(command, cwd=ROOT, check=True)
    generated = WORK / "osca24.pdf"
    if not generated.exists():
        raise SystemExit("JCVI did not produce osca24.pdf")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    generated.replace(OUT)
    print(f"OSCA2.4 microsynteny PASS: {len(links)} anchors -> {OUT}")


if __name__ == "__main__":
    main()
