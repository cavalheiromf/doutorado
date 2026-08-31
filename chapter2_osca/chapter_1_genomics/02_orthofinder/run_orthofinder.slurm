#!/bin/bash
#SBATCH --job-name=orthofinder
#SBATCH --output=orthofinder_%j.log
#SBATCH --error=orthofinder_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G
#SBATCH --time=48:00:00
#SBATCH --partition=long

echo "Iniciando OrthoFinder no nó: $(hostname)"
echo "Data/Hora de início: $(date)"

# Ativar o ambiente Conda
source /home/mfcaval/miniforge3/etc/profile.d/conda.sh
conda activate /home/mfcaval/.local/share/mamba/envs/of3_env

# Executar OrthoFinder
orthofinder -f /home/mfcaval/github/doutorado/analyses/chapter_1_genomics/02_orthofinder/data -t 32 -a 32

echo "OrthoFinder finalizado."
echo "Data/Hora de término: $(date)"
