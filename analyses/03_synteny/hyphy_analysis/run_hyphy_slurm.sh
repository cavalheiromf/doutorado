#!/bin/bash
#SBATCH --job-name=hyphy_osca
#SBATCH --partition=short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=hyphy_slurm_%j.out
#SBATCH --error=hyphy_slurm_%j.err

# Load conda configuration and activate environment using absolute path
source /home/mfcaval/miniforge3/etc/profile.d/conda.sh
conda activate /home/mfcaval/.local/share/mamba/envs/jcviEnv

# Set maximum threads for HyPhy's parallelized execution
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

echo "=========================================================="
echo "Starting HyPhy Analyses on SLURM Cluster"
echo "Job ID: $SLURM_JOB_ID"
echo "Using CPUs: $SLURM_CPUS_PER_TASK"
echo "Host: $SLURM_SUBMIT_HOST"
echo "Node list: $SLURM_JOB_NODELIST"
echo "=========================================================="

echo "[1/2] Running RELAX..."
hyphy relax --alignment vellozia_oscas_codon.fasta --tree vellozia_oscas_labeled.treefile --test Test --reference Reference --output relax_results.json

echo "[2/2] Running Contrast-FEL..."
hyphy contrast-fel --alignment vellozia_oscas_codon.fasta --tree vellozia_oscas_labeled.treefile --output contrast_fel_results.json --branch-set Test --branch-set Reference


echo "=========================================================="
echo "All HyPhy analyses completed successfully!"
echo "=========================================================="
