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
- Vellozia speciation (Vper vs Vtub): >0.02 <0.25 (2 - 25 Ma)
"""

import os

def fasta_to_phylip(fa_file, phy_file):
    records = {}
    current_id, current_seq = None, []
    with open(fa_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_id:
                    records[current_id] = "".join(current_seq)
                current_id = line[1:].split()[0]
                current_seq = []
            else:
                current_seq.append(line)
        if current_id:
            records[current_id] = "".join(current_seq)
            
    num_seqs = len(records)
    seq_len = len(next(iter(records.values())))
    
    with open(phy_file, 'w') as f:
        f.write(f" {num_seqs} {seq_len}\n")
        for sp, seq in records.items():
            f.write(f"{sp:<10}  {seq}\n")
    print(f"[INFO] Converted {fa_file} -> {phy_file} ({num_seqs} taxa, {seq_len} sites)")

def main():
    base_dir = "/home/mfcaval/github/doutorado/chapter_macroevolution"
    phylo_dir = os.path.join(base_dir, "02_phylogenomics")
    mcmc_dir = os.path.join(base_dir, "03_dating")
    os.makedirs(mcmc_dir, exist_ok=True)
    
    supermatrix_fa = os.path.join(phylo_dir, "pan_velloziaceae_supermatrix.fa")
    supermatrix_phy = os.path.join(phylo_dir, "pan_velloziaceae_supermatrix.phy")
    
    print("======================================================================")
    print(" Preparing MCMCtree Dating Inputs for Pan-Velloziaceae")
    print(f" Output Directory: {mcmc_dir}")
    print("======================================================================")
    
    fasta_to_phylip(supermatrix_fa, supermatrix_phy)
    
    tree_file = os.path.join(mcmc_dir, "mcmctree_tree.trees")
    calibrated_tree = """7 1

((((((Vper, Vtub) '>0.02<0.25', Xvis), Abra) '>0.75<0.90', Ptec) '>0.90<1.05', Dala) '>1.15<1.28', Ath) '>1.30<1.45';
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
       usedata = 2 in.BV
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
    ctl_prior_content = ctl_step2_content.replace("usedata = 2 in.BV", "usedata = 0").replace("out_posterior.txt", "out_prior.txt").replace("mcmc.txt", "mcmc_prior.txt")
    with open(ctl_prior, "w") as f:
        f.write(ctl_prior_content)

    print("[INFO] Successfully generated MCMCtree inputs.")

if __name__ == "__main__":
    main()
