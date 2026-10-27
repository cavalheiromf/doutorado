#!/usr/bin/env python3
"""Genome-wide 3-way branch selection analysis with Xerophyta schlechteri as outgroup.
Compares Model 0 (one-ratio null) vs Model 2 (free-ratio branch model) in PAML codeml.
Topology: ((Vper #1, Vtub #2), Xvis #0);
"""
import argparse
import math
import os
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from scipy.stats import chi2
from statsmodels.stats.multitest import multipletests

MAFFT_BIN = "/home/program2/bin/MAFFT/7.526/bin/mafft"
CODEML_BIN = "/home/mfcaval/.local/bin/codeml"
STOPS = {"TAA", "TAG", "TGA"}


def parse_args():
    parser = argparse.ArgumentParser(description="Run 3-way codeml selection analysis")
    parser.add_argument("--output-dir", required=True, help="Directory for output files")
    parser.add_argument("--threads", type=int, default=32, help="Number of parallel worker processes")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of trios for testing")
    parser.add_argument("--batch-size", type=int, default=100, help="Progress report batch size")
    return parser.parse_args()


def load_trios_and_sequences():
    print("[1/4] Loading orthology tables and mapping 3-way 1:1:1 trios...")
    kaks_path = "/home/mfcaval/github/doutorado/chapter_macroevolution_review/04_manuscript/tables/TableS6_reciprocal_1to1_orthologs_kaks.tsv"
    df_kaks = pd.read_csv(kaks_path, sep="\t")
    vper_vtub = dict(zip(df_kaks["Vellozia_peripherica_Gene"], df_kaks["Vellozia_tubiflora_Gene"]))
    pair_map = dict(zip(df_kaks["Vellozia_peripherica_Gene"], df_kaks["Pair_ID"]))
    og_map = dict(zip(df_kaks["Vellozia_peripherica_Gene"], df_kaks["Orthogroup"]))
    pairwise_omega_map = dict(zip(df_kaks["Vellozia_peripherica_Gene"], df_kaks["Omega_KaKs"]))
    pairwise_flags_map = dict(zip(df_kaks["Vellozia_peripherica_Gene"], df_kaks["Flags"]))

    vx_file = "/home/mfcaval/github/doutorado/chapter_macroevolution_review/01_orthology/results/Results_Aug30/Orthologues/Orthologues_Vper.pep/Vper.pep__v__Xvis.pep.tsv"
    tx_file = "/home/mfcaval/github/doutorado/chapter_macroevolution_review/01_orthology/results/Results_Aug30/Orthologues/Orthologues_Vtub.pep/Vtub.pep__v__Xvis.pep.tsv"
    vx = pd.read_csv(vx_file, sep="\t")
    tx = pd.read_csv(tx_file, sep="\t")
    vx_11 = vx[~vx["Vper.pep"].str.contains(",") & ~vx["Xvis.pep"].str.contains(",")]
    tx_11 = tx[~tx["Vtub.pep"].str.contains(",") & ~tx["Xvis.pep"].str.contains(",")]
    v_to_x = dict(zip(vx_11["Vper.pep"], vx_11["Xvis.pep"]))
    t_to_x = dict(zip(tx_11["Vtub.pep"], tx_11["Xvis.pep"]))

    print("[2/4] Indexing CDS fasta files into memory...")
    vper_cds = {r.id.split()[0]: str(r.seq).upper() for r in SeqIO.parse("/home/mfcaval/github/doutorado/data/genomes/Vper/Vper.hapA.v1.softmasked.cds.fasta", "fasta")}
    vtub_cds = {r.id.split()[0]: str(r.seq).upper() for r in SeqIO.parse("/home/mfcaval/github/doutorado/data/genomes/Vtub/Vtub.hapA.v1.softmasked.cds.fasta", "fasta")}
    xvis_cds = {r.id.split()[0]: str(r.seq).upper() for r in SeqIO.parse("/home/mfcaval/github/doutorado/chapter_macroevolution_review/00_data/cds_outgroups/Xvis.cds.fa", "fasta")}

    trios = []
    for vp, vt in vper_vtub.items():
        if vp in v_to_x and vt in t_to_x and v_to_x[vp] == t_to_x[vt]:
            xv = v_to_x[vp]
            if vp in vper_cds and vt in vtub_cds and xv in xvis_cds:
                trios.append({
                    "Pair_ID": pair_map[vp],
                    "Orthogroup": og_map[vp],
                    "Vper_Gene": vp,
                    "Vtub_Gene": vt,
                    "Xvis_Gene": xv,
                    "Pairwise_Omega": pairwise_omega_map.get(vp, None),
                    "Pairwise_Flags": pairwise_flags_map.get(vp, None),
                    "Vper_CDS": vper_cds[vp],
                    "Vtub_CDS": vtub_cds[vt],
                    "Xvis_CDS": xvis_cds[xv]
                })

    print(f"Mapped {len(trios)} valid 3-way trios with complete CDS.")
    return trios


def process_single_trio(item):
    pair_id = item["Pair_ID"]
    og = item["Orthogroup"]
    vp_gene = item["Vper_Gene"]
    vt_gene = item["Vtub_Gene"]
    xv_gene = item["Xvis_Gene"]
    pair_omega = item["Pairwise_Omega"]
    pair_flags = item["Pairwise_Flags"]

    c_vp = item["Vper_CDS"]
    c_vt = item["Vtub_CDS"]
    c_xv = item["Xvis_CDS"]

    # Trim to multiple of 3
    c_vp = c_vp[:len(c_vp) - (len(c_vp) % 3)]
    c_vt = c_vt[:len(c_vt) - (len(c_vt) % 3)]
    c_xv = c_xv[:len(c_xv) - (len(c_xv) % 3)]

    if len(c_vp) < 90 or len(c_vt) < 90 or len(c_xv) < 90:
        return {"Pair_ID": pair_id, "Orthogroup": og, "Vper_Gene": vp_gene, "Vtub_Gene": vt_gene, "Xvis_Gene": xv_gene,
                "QC_Status": "FAIL_CDS_TOO_SHORT"}

    p_vp = str(Seq(c_vp).translate()).removesuffix("*")
    p_vt = str(Seq(c_vt).translate()).removesuffix("*")
    p_xv = str(Seq(c_xv).translate()).removesuffix("*")

    if "*" in p_vp or "*" in p_vt or "*" in p_xv:
        return {"Pair_ID": pair_id, "Orthogroup": og, "Vper_Gene": vp_gene, "Vtub_Gene": vt_gene, "Xvis_Gene": xv_gene,
                "QC_Status": "FAIL_INTERNAL_STOP"}

    with tempfile.TemporaryDirectory() as tmpdir:
        fa_in = os.path.join(tmpdir, "in.fa")
        fa_out = os.path.join(tmpdir, "aln.fa")
        with open(fa_in, "w") as f:
            f.write(f">Vper\n{p_vp}\n>Vtub\n{p_vt}\n>Xvis\n{p_xv}\n")

        try:
            subprocess.run([MAFFT_BIN, "--quiet", "--auto", fa_in], stdout=open(fa_out, "w"), check=True, timeout=60)
        except Exception as e:
            return {"Pair_ID": pair_id, "Orthogroup": og, "Vper_Gene": vp_gene, "Vtub_Gene": vt_gene, "Xvis_Gene": xv_gene,
                    "QC_Status": "FAIL_MAFFT_ERROR"}

        alns = {r.id: str(r.seq).upper() for r in SeqIO.parse(fa_out, "fasta")}
        if not alns or "Vper" not in alns or "Vtub" not in alns or "Xvis" not in alns:
            return {"Pair_ID": pair_id, "Orthogroup": og, "Vper_Gene": vp_gene, "Vtub_Gene": vt_gene, "Xvis_Gene": xv_gene,
                    "QC_Status": "FAIL_EMPTY_ALIGNMENT"}

        cds_dict = {"Vper": c_vp, "Vtub": c_vt, "Xvis": c_xv}
        threaded = {}
        for sp in ["Vper", "Vtub", "Xvis"]:
            seq = cds_dict[sp]
            idx = 0
            codons = []
            for aa in alns[sp]:
                if aa == "-":
                    codons.append("---")
                else:
                    codons.append(seq[idx:idx+3])
                    idx += 3
            threaded[sp] = codons

        n_codons = len(alns["Vper"])
        retained = {"Vper": [], "Vtub": [], "Xvis": []}
        for i in range(n_codons):
            c_p = threaded["Vper"][i]
            c_t = threaded["Vtub"][i]
            c_x = threaded["Xvis"][i]
            if any("-" in c for c in [c_p, c_t, c_x]): continue
            if any(c in STOPS for c in [c_p, c_t, c_x]): continue
            if any(set(c) - set("ACGT") for c in [c_p, c_t, c_x]): continue
            retained["Vper"].append(c_p)
            retained["Vtub"].append(c_t)
            retained["Xvis"].append(c_x)

        final_codon_len = len(retained["Vper"])
        if final_codon_len < 30:
            return {"Pair_ID": pair_id, "Orthogroup": og, "Vper_Gene": vp_gene, "Vtub_Gene": vt_gene, "Xvis_Gene": xv_gene,
                    "QC_Status": "FAIL_RETAINED_CODONS_LT_30", "Aligned_Codons": final_codon_len}

        # Write phylip file
        phy_file = os.path.join(tmpdir, "aln.phy")
        tree_file = os.path.join(tmpdir, "tree.nwk")
        with open(phy_file, "w") as f:
            f.write(f"  3  {final_codon_len * 3}\n")
            for sp in ["Vper", "Vtub", "Xvis"]:
                f.write(f"{sp:<10} {''.join(retained[sp])}\n")

        with open(tree_file, "w") as f:
            # Unrooted tree with branch labels: #1 for Vper, #2 for Vtub, #0 for Xvis
            f.write(" 3 1\n(Vper #1, Vtub #2, Xvis #0);\n")

        # 1. Run Model 0 (M0: one-ratio)
        ctl_m0 = os.path.join(tmpdir, "m0.ctl")
        out_m0 = os.path.join(tmpdir, "m0.out")
        with open(ctl_m0, "w") as f:
            f.write(f"""      seqfile = {phy_file}
     treefile = {tree_file}
      outfile = {out_m0}
        noisy = 0
      verbose = 0
      runmode = 0
      seqtype = 1
    CodonFreq = 2
        clock = 0
        model = 0
      NSsites = 0
        icode = 0
    fix_kappa = 0
        kappa = 2
    fix_omega = 0
        omega = 0.4
""")
        proc_m0 = subprocess.run([CODEML_BIN, ctl_m0], cwd=tmpdir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if proc_m0.returncode != 0 or not os.path.exists(out_m0):
            return {"Pair_ID": pair_id, "Orthogroup": og, "Vper_Gene": vp_gene, "Vtub_Gene": vt_gene, "Xvis_Gene": xv_gene,
                    "QC_Status": "FAIL_CODEML_M0"}

        lnL_m0 = None
        omega_m0 = None
        with open(out_m0) as f:
            for l in f:
                if "lnL(ntime:" in l:
                    try: lnL_m0 = float(l.split(":")[3].split()[0])
                    except: pass
                if "omega (dN/dS) =" in l:
                    try: omega_m0 = float(l.split("=")[-1].strip())
                    except: pass

        if lnL_m0 is None:
            return {"Pair_ID": pair_id, "Orthogroup": og, "Vper_Gene": vp_gene, "Vtub_Gene": vt_gene, "Xvis_Gene": xv_gene,
                    "QC_Status": "FAIL_PARSE_M0"}

        # 2. Run Model 2 (Branch model: independent omegas for Vper, Vtub, Xvis)
        ctl_m2 = os.path.join(tmpdir, "m2.ctl")
        out_m2 = os.path.join(tmpdir, "m2.out")
        with open(ctl_m2, "w") as f:
            f.write(f"""      seqfile = {phy_file}
     treefile = {tree_file}
      outfile = {out_m2}
        noisy = 0
      verbose = 1
      runmode = 0
      seqtype = 1
    CodonFreq = 2
        clock = 0
        model = 2
      NSsites = 0
        icode = 0
    fix_kappa = 0
        kappa = 2
    fix_omega = 0
        omega = 0.4
""")
        proc_m2 = subprocess.run([CODEML_BIN, ctl_m2], cwd=tmpdir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if proc_m2.returncode != 0 or not os.path.exists(out_m2):
            return {"Pair_ID": pair_id, "Orthogroup": og, "Vper_Gene": vp_gene, "Vtub_Gene": vt_gene, "Xvis_Gene": xv_gene,
                    "QC_Status": "FAIL_CODEML_M2"}

        lnL_m2 = None
        w_vper = None
        w_vtub = None
        w_xvis = None
        dn_vper, ds_vper = None, None
        dn_vtub, ds_vtub = None, None
        dn_xvis, ds_xvis = None, None

        with open(out_m2) as f:
            lines = f.readlines()

        for idx_l, l in enumerate(lines):
            if "lnL(ntime:" in l:
                try: lnL_m2 = float(l.split(":")[3].split()[0])
                except: pass
            if "dN & dS for each branch" in l:
                # Table follows
                for sub in lines[idx_l:idx_l+10]:
                    parts = sub.split()
                    if len(parts) >= 7 and ".." in parts[0]:
                        branch = parts[0]
                        w_val = float(parts[4])
                        dn_val = float(parts[5])
                        ds_val = float(parts[6])
                        if branch == "4..1":
                            w_vper, dn_vper, ds_vper = w_val, dn_val, ds_val
                        elif branch == "4..2":
                            w_vtub, dn_vtub, ds_vtub = w_val, dn_val, ds_val
                        elif branch == "4..3":
                            w_xvis, dn_xvis, ds_xvis = w_val, dn_val, ds_val

        if lnL_m2 is None or w_vper is None or w_vtub is None:
            return {"Pair_ID": pair_id, "Orthogroup": og, "Vper_Gene": vp_gene, "Vtub_Gene": vt_gene, "Xvis_Gene": xv_gene,
                    "QC_Status": "FAIL_PARSE_M2"}

        # Likelihood ratio test
        # Model 2 has 2 additional parameters compared to Model 0 (df = 2)
        lrt_stat = max(0.0, 2.0 * (lnL_m2 - lnL_m0))
        p_val = float(1.0 - chi2.cdf(lrt_stat, df=2))

        # Polarization call
        call = "CONSERVED"
        # Require minimal dS to avoid 0 denominator artifact
        min_ds = 0.005
        max_ds = 2.0

        if ds_vper > max_ds or ds_vtub > max_ds or ds_xvis > max_ds:
            call = "HIGH_DS_SATURATION"
        elif ds_vper < min_ds and ds_vtub < min_ds:
            call = "LOW_DIVERGENCE_UNRESOLVED"
        elif w_vtub > 1.0 and w_vper <= 1.0 and p_val < 0.05 and ds_vtub >= min_ds:
            call = "ACCELERATED_VTUB"
        elif w_vper > 1.0 and w_vtub <= 1.0 and p_val < 0.05 and ds_vper >= min_ds:
            call = "ACCELERATED_VPER"
        elif w_vtub > 1.0 and w_vper > 1.0 and p_val < 0.05:
            call = "ACCELERATED_BOTH"
        elif w_vtub > 1.0 and ds_vtub >= min_ds:
            call = "SUGGESTIVE_VTUB"
        elif w_vper > 1.0 and ds_vper >= min_ds:
            call = "SUGGESTIVE_VPER"

        return {
            "Pair_ID": pair_id,
            "Orthogroup": og,
            "Vper_Gene": vp_gene,
            "Vtub_Gene": vt_gene,
            "Xvis_Gene": xv_gene,
            "Pairwise_Omega_YN00": pair_omega,
            "Pairwise_Flags": pair_flags,
            "Aligned_Codons": final_codon_len,
            "lnL_M0": lnL_m0,
            "Omega_M0": omega_m0,
            "lnL_M2": lnL_m2,
            "LRT_Stat_2DeltaLnL": round(lrt_stat, 4),
            "LRT_Pval": p_val,
            "Omega_Vper": w_vper,
            "dN_Vper": dn_vper,
            "dS_Vper": ds_vper,
            "Omega_Vtub": w_vtub,
            "dN_Vtub": dn_vtub,
            "dS_Vtub": ds_vtub,
            "Omega_Xvis": w_xvis,
            "dN_Xvis": dn_xvis,
            "dS_Xvis": ds_xvis,
            "Polarization_Call": call,
            "QC_Status": "PASS"
        }


def main():
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    trios = load_trios_and_sequences()
    if args.limit:
        trios = trios[:args.limit]
        print(f"Limiting execution to first {args.limit} trios.")

    total = len(trios)
    results = []
    t_start = time.time()
    print(f"[3/4] Launching parallel processing of {total} trios on {args.threads} workers...")

    completed = 0
    with ProcessPoolExecutor(max_workers=args.threads) as executor:
        futures = {executor.submit(process_single_trio, item): item["Pair_ID"] for item in trios}
        for fut in as_completed(futures):
            res = fut.result()
            results.append(res)
            completed += 1
            if completed % args.batch_size == 0 or completed == total:
                elapsed = time.time() - t_start
                rate = completed / elapsed if elapsed > 0 else 0
                rem_time = (total - completed) / rate if rate > 0 else 0
                print(f"  [{completed}/{total}] {completed/total*100:.1f}% done | {rate:.1f} trios/sec | ETA: {rem_time/60:.1f} min")

    print("[4/4] Finalizing results, computing FDR, and exporting TSV...")
    df_res = pd.DataFrame(results)

    # Compute FDR for LRT_Pval among PASS items
    pass_mask = (df_res["QC_Status"] == "PASS") & df_res["LRT_Pval"].notna()
    if pass_mask.sum() > 0:
        pvals = df_res.loc[pass_mask, "LRT_Pval"].values
        qvals = multipletests(pvals, method="fdr_bh")[1]
        df_res.loc[pass_mask, "LRT_Qval_FDR"] = qvals
    else:
        df_res["LRT_Qval_FDR"] = None

    tsv_out = out_dir / "trio_branch_selection_results.tsv"
    df_res.to_csv(tsv_out, sep="\t", index=False)
    print(f"Saved complete results to {tsv_out}")

    # Summary
    print("\n=== SUMMARY OF POLARIZATION CALLS ===")
    if "Polarization_Call" in df_res:
        print(df_res["Polarization_Call"].value_counts(dropna=False).to_string())

    print(f"\nTotal execution time: {(time.time() - t_start)/60:.2f} minutes.")


if __name__ == "__main__":
    main()

