import subprocess


def generate_sbatch_script(
    job_name, cpus, mem, time, partition, commands,
    modules=None, gpu=False, array=None,
    logs_dir="logs"
):
    """Generates a SLURM sbatch script as a string.

    Args:
        job_name:  SLURM job name.
        cpus:      Number of CPUs per task.
        mem:       Memory string (e.g. '48G').
        time:      Wall-clock time string (e.g. '04:00:00').
        partition: SLURM partition name.
        commands:  List of shell command strings to run.
        modules:   List of module names to load (optional).
        gpu:       If True, request 1 GPU.
        array:     SLURM array specification string (optional).
        logs_dir:  Directory for .out/.err log files (default 'logs').

    Returns:
        str: Complete sbatch script content.
    """
    lines = [
        "#!/bin/bash",
        f"#SBATCH --job-name={job_name}",
        f"#SBATCH --cpus-per-task={cpus}",
        f"#SBATCH --mem={mem}",
        f"#SBATCH --time={time}",
        f"#SBATCH --partition={partition}",
        f"#SBATCH --output={logs_dir}/{job_name}_%j.out",
        f"#SBATCH --error={logs_dir}/{job_name}_%j.err",
    ]

    if gpu:
        lines.append("#SBATCH --gres=gpu:1")

    if array:
        lines.append(f"#SBATCH --array={array}")

    lines.append("\n# --- Load Modules ---")
    if modules:
        for mod in modules:
            lines.append(f"module load {mod}")

    lines.append("\n# --- Commands ---")
    lines.extend(commands)

    return "\n".join(lines)


def submit_job(script_content, depend_ids=None):
    """Submits a job by piping the script directly to sbatch (no .sh file written).

    Args:
        script_content: sbatch script string (from generate_sbatch_script).
        depend_ids:     List of job IDs to depend on (afterok). None values are ignored.

    Returns:
        str | None: Submitted job ID, or None on failure.
    """
    cmd = ["sbatch"]

    if depend_ids:
        valid_ids = [str(jid) for jid in depend_ids if jid]
        if valid_ids:
            cmd.append(f"--dependency=afterok:{':'.join(valid_ids)}")

    try:
        result = subprocess.run(
            cmd,
            input=script_content,
            capture_output=True,
            text=True,
            check=True
        )
        # Output format: "Submitted batch job 123456"
        job_id = result.stdout.strip().split()[-1]
        return job_id
    except subprocess.CalledProcessError as e:
        print(f"❌ Error submitting job: {e.stderr}")
        return None
