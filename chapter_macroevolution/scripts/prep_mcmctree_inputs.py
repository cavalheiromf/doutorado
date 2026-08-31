#!/usr/bin/env python3
"""
Prepare MCMCtree (PAML) Inputs and Fossil Calibrations.
Chapter: Macroevolution and Genomics in Velloziaceae

Time unit: 100 Ma = 1.0
Calibrations:
- Root (Ath vs Monocots): >1.30 <1.45 (130 - 145 Ma)
- Monocots (Dala vs Pandanales): >1.15 <1.28 (115 - 128 Ma)
- Pandanales (Ptec vs Velloziaceae): >0.90 <1.05 (90 - 105 Ma)
- Crown Velloziaceae (Abra vs core): >0.75 <0.90 (75 - 90 Ma)
- Core Velloziaceae (Xvis vs Vellozia): UNCONSTRAINED (Tested freely!)
- Vellozia speciation (Vper vs Vtub): >0.02 <0.25 (2 - 25 Ma)
"""

import os

def main():
    base_dir = "/home/mfcaval/github/doutorado/chapter_macroevolution"
    phylo_dir = os.path.join(base_dir, "02_phylogenomics")
    mcmc_dir = os.path.join(base_dir, "03_dating")
    os.makedirs(mcmc_dir, exist_ok=True)
    
    supermatrix_phy = os.path.join(phylo_dir, "pan_velloziaceae_supermatrix.phy")
    
    print("======================================================================")
    print(" Preparing MCMCtree Dating Inputs for Pan-Velloziaceae")
    print(f" Output Directory: {mcmc_dir}")
    print("======================================================================")
    
    tree_file = os.path.join(mcmc_dir, "mcmctree_tree.trees")
    
    calibrated_tree = """7 1

(((Ath, (Dala, (Ptec, (Abra, (Xvis, (Vper, Vtub) '>0.02<0.25') ) '>0.75<0.90') ) '>0.90<1.05') ) '>1.15<1.28') ) '>1.30<1.45';
"""
    with open(tree_file, "w") as f:
        f.write(calibrated_tree)
    
    ctl_step1 = os.path.join(mcmc_dir, "mcmctree_step1_bv.ctl")
    ctl_step1_content = f"""          seed = -1
       seqfile = {supermatrix_phy}
      treefile = mcmctree_tree.trees
      mcmcfile = mcmc.txt
       outfile = out_step1.txt

         ndata = 1
       seqtype = 2
       usedata = 3
         clock = 2
       RootAge = '<1.50'

         model = 0
         alpha = 0.5
         ncatG = 5
     cleandata = 0

       BDparas = 1 1 0.1
   kappa_gamma = 6 2
   alpha_gamma = 1 1

   rgene_gamma = 2 20 1
  sigma2_gamma = 1 10 1

      finetune = 1: 0.1 0.1 0.1 0.1 0.1 0.1

         print = 1
        burnin = 10000
      sampfreq = 5
       nsample = 20000
"""
    with open(ctl_step1, "w") as f:
        f.write(ctl_step1_content)

    ctl_step2 = os.path.join(mcmc_dir, "mcmctree_step2_mcmc.ctl")
    ctl_step2_content = f"""          seed = -1
       seqfile = {supermatrix_phy}
      treefile = mcmctree_tree.trees
      mcmcfile = mcmc.txt
       outfile = out_posterior.txt

         ndata = 1
       seqtype = 2
       usedata = 2
         clock = 2
       RootAge = '<1.50'

         model = 0
         alpha = 0.5
         ncatG = 5
     cleandata = 0

       BDparas = 1 1 0.1
   kappa_gamma = 6 2
   alpha_gamma = 1 1

   rgene_gamma = 2 20 1
  sigma2_gamma = 1 10 1

      finetune = 1: 0.1 0.1 0.1 0.1 0.1 0.1

         print = 1
        burnin = 20000
      sampfreq = 10
       nsample = 20000
"""
    with open(ctl_step2, "w") as f:
        f.write(ctl_step2_content)

    ctl_prior = os.path.join(mcmc_dir, "mcmctree_prior_check.ctl")
    ctl_prior_content = ctl_step2_content.replace("usedata = 2", "usedata = 0").replace("out_posterior.txt", "out_prior.txt").replace("mcmc.txt", "mcmc_prior.txt")
    with open(ctl_prior, "w") as f:
        f.write(ctl_prior_content)

    print("[INFO] Successfully generated MCMCtree inputs.")

if __name__ == "__main__":
    main()
