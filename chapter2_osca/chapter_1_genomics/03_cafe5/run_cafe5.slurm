#!/bin/bash
#SBATCH --job-name=cafe5
#SBATCH --output=cafe5_%j.log
#SBATCH --error=cafe5_%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=24:00:00

# Ativar ambiente conda
source ~/miniforge3/etc/profile.d/conda.sh
conda activate ~/.local/share/mamba/envs/cafe5_env

echo "=========================================="
echo "Preparando arquivos de entrada..."
python prep_cafe_input.py

echo "=========================================="
echo "Rodando CAFE5..."
# O CAFE5 exige -i (input) e -t (tree)
# -p calcula p-values, -o define a pasta de output, -c define o numero de cores
cafe5 -i cafe_input.tsv -t ultrametric_vellozia.tre -p -o cafe5_results -c ${SLURM_CPUS_PER_TASK:-4}

echo "=========================================="
echo "Finalizado."
