#!/bin/bash
#SBATCH --job-name=mcmc_macro
#SBATCH --output=/home/mfcaval/github/doutorado/chapter_macroevolution/03_dating/mcmctree_%j.log
#SBATCH --error=/home/mfcaval/github/doutorado/chapter_macroevolution/03_dating/mcmctree_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --partition=short
#SBATCH --time=12:00:00
#SBATCH --reservation=teste

# ==============================================================================
# Pipeline: 03_Dating (MCMCtree Molecular Dating)
# Chapter: Macroevolution and Genomics in Velloziaceae
# Candidate: Mariana Feitosa Cavalheiro (UNICAMP)
# ==============================================================================

set -euo pipefail

BASE_DIR="/home/mfcaval/github/doutorado/chapter_macroevolution"
SCRIPT_DIR="${BASE_DIR}/scripts"
MCMC_DIR="${BASE_DIR}/03_dating"

mkdir -p "${MCMC_DIR}"

echo "======================================================================"
echo " Starting MCMCtree Dating Pipeline"
echo " Node:             $(hostname)"
echo " Start Date/Time:  $(date)"
echo "======================================================================"

python3 "${SCRIPT_DIR}/prep_mcmctree_inputs.py"

cd "${MCMC_DIR}"

echo "======================================================================"
echo " Step 1: Approximate Likelihood Gradient / Hessian Calculation (usedata = 3)"
echo "======================================================================"
mcmctree mcmctree_step1_bv.ctl > run_step1.log

if [ -f "out.BV" ]; then
    cp out.BV in.BV
elif [ ! -f "in.BV" ]; then
    echo "[ERRO] Arquivo in.BV nao foi gerado! Algo falhou no Step 1."
    exit 1
fi

echo "======================================================================"
echo " Step 2: Posterior MCMC Sampling (usedata = 2)"
echo "======================================================================"
mcmctree mcmctree_step2_mcmc.ctl > run_step2.log

echo "======================================================================"
echo " Parsing Chronogram and 95% HPD Confidence Intervals"
echo "======================================================================"
python3 "${SCRIPT_DIR}/parse_mcmctree_results.py"

echo "======================================================================"
echo " MCMCtree Molecular Dating Complete!"
echo " Results available in: ${MCMC_DIR}"
echo " End Date/Time:    $(date)"
echo "======================================================================"
