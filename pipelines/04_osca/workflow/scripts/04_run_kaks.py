import os
import subprocess
import glob

# Paths
RESULTS_DIR = "/home/mfcaval/github/doutorado/analyses/04_evolutionary_rates/results"
JCVI_ENV_BIN = "/home/mfcaval/.local/share/mamba/envs/jcviEnv/bin"

def run_cmd(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result

def main():
    pair_dirs = glob.glob(os.path.join(RESULTS_DIR, "Vp*"))
    
    for d in pair_dirs:
        pair_name = os.path.basename(d)
        print(f"Processing {pair_name}...")
        
        pep_file = os.path.join(d, "pep.faa")
        cds_file = os.path.join(d, "cds.fna")
        outfile = os.path.join(d, "results.ks")
        
        # Run Ka/Ks using JCVI wrapper
        # Usage: ks.py calc [prot.fasta] cds.fasta > out.ks
        jcvi_kaks_cmd = f"{JCVI_ENV_BIN}/python3 -m jcvi.compara.ks calc {pep_file} {cds_file} -o {outfile} --msa=muscle"
        
        run_cmd(jcvi_kaks_cmd)

if __name__ == "__main__":
    main()
