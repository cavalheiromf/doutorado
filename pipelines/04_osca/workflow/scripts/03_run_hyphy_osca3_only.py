#!/usr/bin/env python3
"""Reproduce HyPhy RELAX for the four Vellozia OSCA3 sequences only.

The script deliberately excludes both OSCA4 sequences. It builds a local
protein alignment, threads the original CDS onto it, prunes the established
OSCA gene tree, applies explicit codon-gap filters, runs RELAX, and records
checksums, versions, commands, logs, and a machine-readable summary.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from Bio import Phylo, SeqIO
from Bio.Seq import Seq


GENES = (
    "Vper.hapA.v1.chr1A.g020450.t1",
    "Vtub.hapA.v1.chr1A.g018250.t1",
    "Vper.hapA.v1.chr5A.g142080.t1",
    "Vtub.hapA.v1.chr5A.g129040.t1",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_fasta(paths: list[Path]) -> dict[str, str]:
    records: dict[str, str] = {}
    for path in paths:
        for record in SeqIO.parse(path, "fasta"):
            sequence = str(record.seq).upper()
            if record.id in records and records[record.id] != sequence:
                raise ValueError(f"Conflicting CDS records for {record.id}")
            records[record.id] = sequence
    missing = sorted(set(GENES) - set(records))
    if missing:
        raise ValueError(f"Missing OSCA3 CDS records: {', '.join(missing)}")
    return {gene: records[gene] for gene in GENES}


def translate_cds(cds: dict[str, str]) -> tuple[dict[str, str], dict[str, str]]:
    proteins: dict[str, str] = {}
    cleaned: dict[str, str] = {}
    for gene, sequence in cds.items():
        if len(sequence) % 3:
            raise ValueError(f"CDS length is not divisible by three: {gene}")
        protein = str(Seq(sequence).translate())
        if protein.endswith("*"):
            protein = protein[:-1]
            sequence = sequence[:-3]
        if "*" in protein:
            raise ValueError(f"Internal stop codon in {gene}")
        proteins[gene] = protein
        cleaned[gene] = sequence
    return proteins, cleaned


def write_fasta(records: dict[str, str], path: Path, sanitize: bool = False) -> None:
    with path.open("w") as handle:
        for name, sequence in records.items():
            if sanitize:
                name = name.replace(".", "_")
            handle.write(f">{name}\n{sequence}\n")


def thread_codons(aligned_proteins: dict[str, str], cds: dict[str, str]) -> dict[str, str]:
    aligned_codons: dict[str, str] = {}
    for gene, protein in aligned_proteins.items():
        codon_index = 0
        codons: list[str] = []
        for amino_acid in protein:
            if amino_acid == "-":
                codons.append("---")
            else:
                codon = cds[gene][codon_index : codon_index + 3]
                if len(codon) != 3:
                    raise ValueError(f"Protein/CDS length mismatch for {gene}")
                codons.append(codon)
                codon_index += 3
        if codon_index != len(cds[gene]):
            raise ValueError(f"Unused CDS nucleotides after threading for {gene}")
        aligned_codons[gene] = "".join(codons)
    return aligned_codons


def filter_codons(records: dict[str, str], max_gap_fraction: float) -> tuple[dict[str, str], list[int]]:
    lengths = {len(sequence) for sequence in records.values()}
    if len(lengths) != 1 or next(iter(lengths)) % 3:
        raise ValueError("Invalid codon alignment dimensions")
    codon_count = next(iter(lengths)) // 3
    retained: list[int] = []
    output = {name: [] for name in records}
    for index in range(codon_count):
        column = {name: sequence[index * 3 : index * 3 + 3] for name, sequence in records.items()}
        gap_fraction = sum("-" in codon for codon in column.values()) / len(column)
        if gap_fraction <= max_gap_fraction:
            retained.append(index + 1)
            for name, codon in column.items():
                output[name].append(codon)
    return {name: "".join(codons) for name, codons in output.items()}, retained


def prune_and_label_tree(source: Path, destination: Path) -> list[str]:
    tree = Phylo.read(source, "newick")
    for terminal in list(tree.get_terminals()):
        if terminal.name not in GENES:
            tree.prune(terminal)
    observed = sorted(terminal.name for terminal in tree.get_terminals())
    if observed != sorted(GENES):
        raise ValueError(f"Unexpected OSCA3 tree leaves: {observed}")
    for terminal in tree.get_terminals():
        terminal.name = terminal.name.replace(".", "_")
        terminal.comment = "Test" if terminal.name.startswith("Vtub_") else "Reference"
    buffer = io.StringIO()
    Phylo.write(tree, buffer, "newick")
    tree_text = buffer.getvalue().replace("[Test]", "{Test}").replace("[Reference]", "{Reference}")
    destination.write_text(tree_text)
    return observed


def run(command: list[str], stdout: Path, stderr: Path) -> None:
    with stdout.open("w") as out_handle, stderr.open("w") as err_handle:
        subprocess.run(command, check=True, stdout=out_handle, stderr=err_handle)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--muscle", type=Path, default=Path(shutil.which("muscle") or "muscle"))
    parser.add_argument("--hyphy", type=Path, default=Path(shutil.which("hyphy") or "hyphy"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    project = args.project.resolve()
    output = (args.output or project / "03_synteny/results/hyphy_osca3_only_20261026").resolve()
    output.mkdir(parents=True, exist_ok=True)

    cds_sources = [
        project / "04_evolutionary_rates/results/VpOSCA3.1_VtOSCA3.1/cds.fna",
        project / "04_evolutionary_rates/results/VpOSCA3.2_VtOSCA3.2/cds.fna",
    ]
    tree_source = project / "02_phylogeny/results/iqtree.treefile"
    for path in [*cds_sources, tree_source, args.muscle, args.hyphy]:
        if not path.exists():
            raise FileNotFoundError(path)

    cds = read_fasta(cds_sources)
    proteins, cleaned_cds = translate_cds(cds)
    protein_unaligned = output / "osca3_pep_unaligned.fasta"
    protein_aligned = output / "osca3_pep_aligned.fasta"
    write_fasta(proteins, protein_unaligned)
    run([str(args.muscle), "-in", str(protein_unaligned), "-out", str(protein_aligned)], output / "muscle.stdout.log", output / "muscle.stderr.log")

    aligned_proteins = {record.id: str(record.seq) for record in SeqIO.parse(protein_aligned, "fasta")}
    if set(aligned_proteins) != set(GENES):
        raise ValueError("MUSCLE output does not contain exactly the four OSCA3 sequences")
    codon_alignment = thread_codons(aligned_proteins, cleaned_cds)
    unfiltered_path = output / "osca3_codon_unfiltered.fasta"
    write_fasta(codon_alignment, unfiltered_path, sanitize=True)

    filter_metadata: dict[str, dict[str, object]] = {}
    alignment_paths: dict[str, Path] = {}
    for label, threshold in (("gap20", 0.20), ("gap50", 0.50)):
        filtered, retained = filter_codons(codon_alignment, threshold)
        alignment_path = output / f"osca3_codon_{label}.fasta"
        write_fasta(filtered, alignment_path, sanitize=True)
        (output / f"osca3_{label}_site_map.tsv").write_text(
            "filtered_site\tunfiltered_site\n" + "".join(f"{i}\t{site}\n" for i, site in enumerate(retained, 1))
        )
        alignment_paths[label] = alignment_path
        filter_metadata[label] = {
            "max_gap_fraction": threshold,
            "retained_codons": len(retained),
            "unfiltered_codons": len(next(iter(codon_alignment.values()))) // 3,
        }

    tree_path = output / "osca3_labeled.treefile"
    leaves = prune_and_label_tree(tree_source, tree_path)

    version = subprocess.run([str(args.hyphy), "--version"], check=True, capture_output=True, text=True).stdout.strip()
    (output / "hyphy_version.txt").write_text(version + "\n")
    muscle_version = subprocess.run([str(args.muscle), "-version"], check=True, capture_output=True, text=True)
    (output / "muscle_version.txt").write_text((muscle_version.stdout + muscle_version.stderr).strip() + "\n")

    analyses = (
        ("gap20_sp1", "gap20", 1),
        ("gap20_sp10", "gap20", 10),
        ("gap20_sp25", "gap20", 25),
        ("gap50_sp1", "gap50", 1),
    )
    summaries: list[dict[str, object]] = []
    commands: dict[str, list[str]] = {}
    for analysis, alignment_label, starting_points in analyses:
        result = output / f"relax_{analysis}.json"
        command = [
            str(args.hyphy), "relax",
            "--alignment", str(alignment_paths[alignment_label]),
            "--tree", str(tree_path),
            "--code", "Universal",
            "--mode", "Classic mode",
            "--test", "Test",
            "--reference", "Reference",
            "--grid-size", "250",
            "--starting-points", str(starting_points),
            "--multiple-hits", "None",
            "--rates", "3",
            "--models", "All",
            "--srv", "No",
            "--intermediate-fits", "/dev/null",
            "--kill-zero-lengths", "Yes",
            "--save-fit", "/dev/null",
            "--output", str(result),
        ]
        commands[analysis] = command
        run(command, output / f"relax_{analysis}.stdout.log", output / f"relax_{analysis}.stderr.log")
        payload = json.loads(result.read_text())
        test = payload["test results"]
        summaries.append({
            "analysis": analysis,
            "alignment": alignment_label,
            "starting_points": starting_points,
            "codons": filter_metadata[alignment_label]["retained_codons"],
            "K": test["relaxation or intensification parameter"],
            "LRT": test["LRT"],
            "p_value": test["p-value"],
            "result": result.name,
        })

    checksummed = [*cds_sources, tree_source, protein_unaligned, protein_aligned, unfiltered_path, *alignment_paths.values(), tree_path]
    provenance = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "biological_scope": "OSCA3 only; OSCA4 excluded",
        "genes": list(GENES),
        "tree_leaves": leaves,
        "filters": filter_metadata,
        "software": {"hyphy": version, "muscle": (muscle_version.stdout + muscle_version.stderr).strip()},
        "commands": commands,
        "sha256": {str(path): sha256(path) for path in checksummed},
    }
    (output / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    (output / "relax_summary.tsv").write_text(
        "analysis\talignment\tstarting_points\tcodons\tK\tLRT\tp_value\tresult\n"
        + "".join("\t".join(str(row[key]) for key in ("analysis", "alignment", "starting_points", "codons", "K", "LRT", "p_value", "result")) + "\n" for row in summaries)
    )
    print(json.dumps(summaries, indent=2))


if __name__ == "__main__":
    main()
