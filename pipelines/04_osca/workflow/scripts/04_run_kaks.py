import os
import subprocess
import glob
import sys
from pathlib import Path

# Dynamic paths resolution
SCRIPT_DIR = Path(__file__).resolve().parent
OSCA_DIR = SCRIPT_DIR.parents[1]
RESULTS_DIR = OSCA_DIR / "04_evolutionary_rates" / "results"
PYTHON_BIN = os.environ.get("JCVI_PYTHON", sys.executable)

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
        jcvi_kaks_cmd = f"{PYTHON_BIN} -m jcvi.compara.ks calc {pep_file} {cds_file} -o {outfile} --msa=muscle"
        
        run_cmd(jcvi_kaks_cmd)

if __name__ == "__main__":
    main()
