import os
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
OSCA_DIR = SCRIPT_DIR.parents[1]

mapping_file = OSCA_DIR / "01_gene_identification" / "results" / "oscasIDs.txt"
promoters_dir = OSCA_DIR / "04_promoters" / "results"

# Load mapping
mapping = {}
with open(mapping_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) >= 2:
            orig_id = parts[0]
            new_id = parts[1]
            mapping[orig_id] = new_id

# Process files
for root, dirs, files in os.walk(promoters_dir):
    for file in files:
        if file.endswith((".fasta", ".bed")):
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                content = f.read()
            
            # Replace
            modified = False
            for orig_id, new_id in mapping.items():
                if orig_id in content:
                    content = content.replace(orig_id, new_id)
                    modified = True
            
            if modified:
                with open(file_path, "w") as f:
                    f.write(content)
                print(f"Updated {file_path}")
