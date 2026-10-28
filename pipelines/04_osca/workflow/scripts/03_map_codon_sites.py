import os
import sys
from pathlib import Path
from Bio import AlignIO

SCRIPT_DIR = Path(__file__).resolve().parent
OSCA_DIR = SCRIPT_DIR.parents[1]

global_fasta_path = os.environ.get("GLOBAL_OSCA_FASTA", str(OSCA_DIR / "03_synteny" / "hyphy_analysis" / "vellozia_oscas_codon.fasta"))
base_dir = os.environ.get("HYPHY_SUBCLADES_DIR", str(OSCA_DIR / "03_synteny" / "hyphy_subclades"))

clades = ["osca1", "osca2", "osca3_4"]

# Local significant sites from our Contrast-FEL runs:
# OSCA1: 98, 181, 252, 430, 710, 973
# OSCA2: 8, 71, 76, 147, 191, 241, 270, 308, 394, 395, 432, 596, 720, 824
# OSCA3_4: 593
clade_sig_sites = {
    "osca1": [98, 181, 252, 430, 710, 973],
    "osca2": [8, 71, 76, 147, 191, 241, 270, 308, 394, 395, 432, 596, 720, 824],
    "osca3_4": [593]
}

# Load global alignment
if not os.path.exists(global_fasta_path):
    print(f"Error: Global FASTA not found at {global_fasta_path}")
    sys.exit(1)
global_align = AlignIO.read(global_fasta_path, "fasta")

# Build a mapping of global sequence IDs (with .) to sequences
global_seqs = {}
for record in global_align:
    global_seqs[record.id] = str(record.seq)

print("================================================================================")
print("            CODON COORDINATE MAPPING: LOCAL CLADES TO GLOBAL ALIGNMENT          ")
print("================================================================================")

for clade in clades:
    local_fasta_path = os.path.join(base_dir, clade, f"{clade}_codon.fasta")
    if not os.path.exists(local_fasta_path):
        print(f"\nLocal FASTA not found for clade {clade}: {local_fasta_path}")
        continue
        
    local_align = AlignIO.read(local_fasta_path, "fasta")
    
    # Map local sequence IDs to sequences
    local_seqs = {}
    for record in local_align:
        local_seqs[record.id] = str(record.seq)
        
    print(f"\n>>> Clade: {clade.upper()} <<<")
    sig_sites = clade_sig_sites[clade]
    
    if not sig_sites:
        print("  No significant sites to map.")
        continue
        
    # We will pick a reference sequence present in both
    # Local has _ instead of .
    ref_local_id = list(local_seqs.keys())[0]
    # Reconstruct global ID
    ref_global_id = ref_local_id.replace("_t1", ".t1") if "_t1" in ref_local_id else ref_local_id
    if ref_global_id not in global_seqs:
        # Try generic replace
        ref_global_id = ref_local_id.replace("_", ".") # fall back
        
    # Find matching global ID
    matched_global_id = None
    for g_id in global_seqs.keys():
        if g_id.replace(".", "_") == ref_local_id:
            matched_global_id = g_id
            break
            
    if not matched_global_id:
        print(f"  Error: Could not find global match for reference sequence {ref_local_id}")
        continue
        
    # Get sequence strings
    local_ref_seq = local_seqs[ref_local_id]
    global_ref_seq = global_seqs[matched_global_id]
    
    print(f"  Mapping using reference sequence: {ref_local_id} -> {matched_global_id}")
    print(f"  {'Local Codon':<12} | {'Global Codon':<12} | {'Global Gap %':<12} | {'Interpretation'}")
    print(f"  {'-'*75}")
    
    for s_local in sig_sites:
        # local codon starts at 3*(s_local-1) to 3*s_local
        local_start = 3 * (s_local - 1)
        local_end = 3 * s_local
        
        # 1. Count actual (ungapped) nucleotides in local sequence up to local_start
        seq_prefix = local_ref_seq[:local_start]
        num_nucs = len(seq_prefix.replace("-", ""))
        
        # Also check if the local codon itself is a gap
        local_codon = local_ref_seq[local_start:local_end]
        is_local_gap = "-" in local_codon
        
        # 2. Find corresponding position in global sequence
        # We scan global sequence until we see num_nucs actual nucleotides
        global_start = -1
        nuc_count = 0
        
        for idx, char in enumerate(global_ref_seq):
            if char != "-":
                if nuc_count == num_nucs:
                    global_start = idx
                    break
                nuc_count += 1
                
        if global_start == -1:
            print(f"  {s_local:<12d} | {'N/A (out)':<12} | {'N/A':<12} | Out of bounds in global sequence")
            continue
            
        global_end = global_start + 3
        # Ensure we don't exceed alignment length
        if global_end > len(global_ref_seq):
            global_end = len(global_ref_seq)
            
        s_global = (global_start // 3) + 1
        
        # 3. Calculate global gap percentage at this global codon site
        gap_count = 0
        for record in global_align:
            codon = str(record.seq[global_start:global_end])
            if '-' in codon or 'N' in codon:
                gap_count += 1
        gap_pct = (gap_count / len(global_align)) * 100
        
        # Check if this global site corresponds to one of the 15 global divergent sites
        global_divergent_sites = [401, 484, 486, 797, 803, 821, 842, 957, 1045, 1093, 1232, 1268, 1329, 1332, 1526]
        is_previous_divergent = s_global in global_divergent_sites
        
        note = "New Clade Site"
        if is_previous_divergent:
            note = f"Matches previous Global Site {s_global}!"
            
        print(f"  {s_local:<12d} | {s_global:<12d} | {gap_pct:<12.1f}% | {note}")
        
print("================================================================================")
