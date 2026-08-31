#!/bin/bash
#SBATCH --job-name=mcmctree_macro
#SBATCH --output=/home/mfcaval/github/doutorado/chapter_macroevolution/03_dating/mcmctree_%j.log
#SBATCH --error=/home/mfcaval/github/doutorado/chapter_macroevolution/03_dating/mcmctree_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --partition=short
#SBATCH --time=12:00:00

# ==============================================================================
# Pipeline: 03_Dating (MCMCtree)
# Chapter: Macroevolution and Genomics in Velloziaceae
# ==============================================================================

set -euo pipefail

BASE_DIR="/home/mfcaval/github/doutorado/chapter_macroevolution"
SCRIPT_DIR="${BASE_DIR}/scripts"
MCMC_DIR="${BASE_DIR}/03_dating"

mkdir -p "${MCMC_DIR}"

echo "======================================================================"
echo " Preparing MCMCtree Inputs"
echo "======================================================================"
python3 "${SCRIPT_DIR}/prep_mcmctree_inputs.py"

cd "${MCMC_DIR}"

echo "======================================================================"
echo " Step 0: Prior Check (usedata = 0)"
echo "======================================================================"
mcmctree mcmctree_prior_check.ctl > run_prior.log

echo "======================================================================"
echo " Step 1: Hessian Calculation (usedata = 3)"
echo "======================================================================"
mcmctree mcmctree_step1_bv.ctl > run_step1.log

if [ ! -f "in.BV" ]; then
    echo "[ERRO] Arquivo in.BV nao foi gerado! Algo falhou no Step 1."
    exit 1
fi

echo "======================================================================"
echo " Step 2: Posterior MCMC Sampling (usedata = 2)"
echo "======================================================================"
mcmctree mcmctree_step2_mcmc.ctl > run_step2.log

echo "======================================================================"
echo " MCMCtree Molecular Dating Complete!"
echo "======================================================================"
