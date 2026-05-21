#!/bin/bash
# Submitter script for clade-specific HyPhy analyses on SLURM
# It submits three separate, parallel jobs to the 'short' partition, 
# routing stdout/stderr files directly to their respective clade subfolders.

CLADES=("osca1" "osca2" "osca3_4")
BASE_DIR="/home/mfcaval/github/doutorado/analyses/03_synteny/hyphy_subclades"

for CLADE in "${CLADES[@]}"; do
    echo "Submitting HyPhy job for clade: ${CLADE}"
    sbatch <<EOT
#!/bin/bash
#SBATCH --job-name=hyphy_${CLADE}
#SBATCH --partition=short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=${BASE_DIR}/${CLADE}/hyphy_slurm_%j.out
#SBATCH --error=${BASE_DIR}/${CLADE}/hyphy_slurm_%j.err

# Load conda configuration and activate environment using absolute path
source /home/mfcaval/miniforge3/etc/profile.d/conda.sh
conda activate /home/mfcaval/.local/share/mamba/envs/jcviEnv

# Set maximum threads for HyPhy's parallelized execution
export OMP_NUM_THREADS=\$SLURM_CPUS_PER_TASK

# Change directory to the clade-specific folder
cd ${BASE_DIR}/${CLADE}

echo "=========================================================="
echo "Starting HyPhy clade ${CLADE} on SLURM Cluster"
echo "Job ID: \$SLURM_JOB_ID"
echo "Using CPUs: \$SLURM_CPUS_PER_TASK"
echo "Host: \$SLURM_SUBMIT_HOST"
echo "Node list: \$SLURM_JOB_NODELIST"
echo "=========================================================="

# Run the local HyPhy execution script
bash run_hyphy.sh

echo "=========================================================="
echo "HyPhy clade ${CLADE} completed successfully!"
echo "=========================================================="
EOT
done
