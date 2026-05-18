#!/usr/bin/env python3
"""
RNA-seq Pipeline for Vellozia project (SLURM + Modules version).
Handles QC, Trimming, Indexing, Alignment, and Quantification.

Usage:
    python pipeline.py --step all --species both
    python pipeline.py --step trim --species Vper
"""

import argparse
import sys
from pathlib import Path

# Allow importing from workflow/ at the project root
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from workflow.slurm_utils import generate_sbatch_script, submit_job

# --- Project Paths ---
DATA_DIR    = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "analyses" / "05_rnaseq" / "results"
LOGS_DIR    = PROJECT_ROOT / "logs"

# --- Module Mappings (Biotec02 cluster) ---
MODULES = {
    "fastqc":   "Bio/FastQC/0.12.1",
    "multiqc":  "Bio/MultiQC/1.33",
    "fastp":    "Bio/fastp/0.23.4",
    "star":     "Bio/STAR/2.7.11b",
    "subread":  "Bio/Subread/2.1.1",
    "samtools": "Bio/SAMtools/1.23",
}

GFFREAD = "/home/mfcaval/.local/share/mamba/envs/bio_env/bin/gffread"

# --- Sample Groups ---
SAMPLES = {
    "Vper": ["VP1C", "VP2C", "VP3C", "VP1F", "VP2F", "VP3F", "VP1R", "VP2R", "VP3R"],
    "Vtub": ["VT1C", "VT2C", "VT3C", "VT1F", "VT2F", "VT3F", "VT2R", "VT3R"],
}


def _submit(job_name, cpus, mem, time, partition, commands, modules=None, depend_ids=None):
    """Build sbatch script and submit it directly via stdin (no .sh file written)."""
    script = generate_sbatch_script(
        job_name, cpus, mem, time, partition, commands,
        modules=modules, logs_dir=str(LOGS_DIR)
    )
    print(f"  → Submitting: {job_name} ...", end=" ", flush=True)
    job_id = submit_job(script, depend_ids=depend_ids)
    if job_id:
        print(f"✅ JOB {job_id}")
    return job_id


# ---------------------------------------------------------------------------
# Pipeline steps
# ---------------------------------------------------------------------------

def submit_qc(species_list):
    job_ids = {}
    print("\n[QC] FastQC + MultiQC on raw reads")
    for sp in species_list:
        raw_dir = DATA_DIR / "rnaseq" / sp
        out_dir = RESULTS_DIR / "01_qc" / "raw" / sp
        out_dir.mkdir(parents=True, exist_ok=True)

        commands = [
            f"fastqc -t 12 -o {out_dir} {raw_dir}/*.fastq.gz",
            f"multiqc {out_dir} -o {out_dir} -n {sp}_raw_multiqc",
        ]
        job_ids[sp] = _submit(
            f"qc_raw_{sp}", 12, "24G", "04:00:00", "short",
            commands, modules=[MODULES["fastqc"], MODULES["multiqc"]],
        )
    return job_ids


def submit_index(species_list):
    job_ids = {}
    print("\n[INDEX] STAR genome index")
    for sp in species_list:
        index_dir = RESULTS_DIR / "03_star_index" / sp

        if (index_dir / "Genome").exists():
            print(f"  ⏩ Skipping index for {sp} (already exists)")
            job_ids[sp] = None
            continue

        genome_fa = DATA_DIR / "genomes" / sp / f"{sp}.hapA.v1.softmasked.fasta"
        gff_file  = DATA_DIR / "genomes" / sp / f"{sp}.hapA.v1.softmasked.gff3"
        index_dir.mkdir(parents=True, exist_ok=True)
        gtf_file = index_dir / "annotation.gtf"

        commands = [
            f"{GFFREAD} {gff_file} -T -o {gtf_file}",
            (
                f"STAR --runMode genomeGenerate --genomeDir {index_dir}"
                f" --genomeFastaFiles {genome_fa} --sjdbGTFfile {gtf_file}"
                f" --sjdbOverhang 99 --genomeSAindexNbases 13 --runThreadN 24"
            ),
        ]
        job_ids[sp] = _submit(
            f"index_{sp}", 24, "64G", "04:00:00", "short",
            commands, modules=[MODULES["star"]],
        )
    return job_ids


def submit_trim(species_list):
    job_ids = {}
    print("\n[TRIM] fastp trimming")
    for sp in species_list:
        raw_dir = DATA_DIR / "rnaseq" / sp
        out_dir = RESULTS_DIR / "02_trimmed" / sp
        out_dir.mkdir(parents=True, exist_ok=True)

        for sample in SAMPLES[sp]:
            r1_files = sorted(raw_dir.glob(f"{sample}_*_R1_*.fastq.gz"))
            r2_files = sorted(raw_dir.glob(f"{sample}_*_R2_*.fastq.gz"))

            if not r1_files:
                print(f"  ⚠️  No R1 files found for {sample}, skipping.")
                continue

            m1   = out_dir / f"{sample}_R1_merged.fastq.gz"
            m2   = out_dir / f"{sample}_R2_merged.fastq.gz"
            out1 = out_dir / f"{sample}_trimmed_R1.fastq.gz"
            out2 = out_dir / f"{sample}_trimmed_R2.fastq.gz"

            commands = [
                f"cat {' '.join(str(f) for f in r1_files)} > {m1}",
                f"cat {' '.join(str(f) for f in r2_files)} > {m2}",
                (
                    f"fastp --in1 {m1} --in2 {m2} --out1 {out1} --out2 {out2}"
                    f" --json {out_dir}/{sample}_fastp.json"
                    f" --html {out_dir}/{sample}_fastp.html"
                    f" --thread 8 --detect_adapter_for_pe"
                ),
                f"rm {m1} {m2}",
            ]
            job_ids[sample] = _submit(
                f"trim_{sample}", 8, "16G", "02:00:00", "short",
                commands, modules=[MODULES["fastp"]],
            )
    return job_ids


def submit_align(species_list, index_jids, trim_jids):
    job_ids = {}
    print("\n[ALIGN] STAR alignment")
    for sp in species_list:
        index_dir   = RESULTS_DIR / "03_star_index" / sp
        trimmed_dir = RESULTS_DIR / "02_trimmed" / sp
        out_dir     = RESULTS_DIR / "04_alignment" / sp
        out_dir.mkdir(parents=True, exist_ok=True)

        sp_ids = []
        for sample in SAMPLES[sp]:
            r1 = trimmed_dir / f"{sample}_trimmed_R1.fastq.gz"
            r2 = trimmed_dir / f"{sample}_trimmed_R2.fastq.gz"
            sample_out = out_dir / sample

            deps = [index_jids.get(sp), trim_jids.get(sample)]
            commands = [
                f"mkdir -p {sample_out}",
                (
                    f"STAR --genomeDir {index_dir} --readFilesIn {r1} {r2}"
                    f" --readFilesCommand zcat"
                    f" --outFileNamePrefix {sample_out}/{sample}_"
                    f" --outSAMtype BAM SortedByCoordinate"
                    f" --quantMode GeneCounts --runThreadN 16"
                ),
            ]
            jid = _submit(
                f"align_{sample}", 16, "48G", "04:00:00", "short",
                commands, modules=[MODULES["star"]], depend_ids=deps,
            )
            sp_ids.append(jid)
        job_ids[sp] = sp_ids
    return job_ids


def submit_count(species_list, align_jids):
    print("\n[COUNT] featureCounts")
    for sp in species_list:
        gff_file   = DATA_DIR / "genomes" / sp / f"{sp}.hapA.v1.softmasked.gff3"
        out_dir    = RESULTS_DIR / "05_counts"
        align_dir  = RESULTS_DIR / "04_alignment" / sp
        out_dir.mkdir(parents=True, exist_ok=True)

        gtf_file   = out_dir / f"{sp}_annotation.gtf"
        count_file = out_dir / f"{sp}_gene_counts.txt"

        commands = [
            f"{GFFREAD} {gff_file} -T -o {gtf_file}",
            f"python3 {PROJECT_ROOT}/analyses/05_rnaseq/scripts/fix_gtf.py {gtf_file}",
            (
                f"featureCounts -T 16 -p -t exon -g gene_id"
                f" -a {gtf_file} -o {count_file}"
                f" {align_dir}/*/*_Aligned.sortedByCoord.out.bam"
            ),
        ]
        _submit(
            f"count_{sp}", 16, "16G", "01:00:00", "short",
            commands, modules=[MODULES["subread"]],
            depend_ids=align_jids.get(sp, []),
        )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RNA-seq Pipeline (SLURM, no .sh files)")
    parser.add_argument(
        "--step",
        choices=["qc", "trim", "index", "align", "count", "all"],
        default="all",
        help="Pipeline step to run (default: all)",
    )
    parser.add_argument(
        "--species",
        choices=["Vper", "Vtub", "both"],
        default="both",
        help="Target species (default: both)",
    )
    args = parser.parse_args()

    species_list = ["Vper", "Vtub"] if args.species == "both" else [args.species]
    LOGS_DIR.mkdir(exist_ok=True)

    if args.step == "all":
        qc_jids    = submit_qc(species_list)
        idx_jids   = submit_index(species_list)
        trim_jids  = submit_trim(species_list)
        align_jids = submit_align(species_list, idx_jids, trim_jids)
        submit_count(species_list, align_jids)

    elif args.step == "qc":
        submit_qc(species_list)
    elif args.step == "index":
        submit_index(species_list)
    elif args.step == "trim":
        submit_trim(species_list)
    elif args.step == "align":
        submit_align(species_list, {}, {})
    elif args.step == "count":
        submit_count(species_list, {})
