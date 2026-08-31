import sys
import gzip

input_fasta = sys.argv[1]
output_fasta = sys.argv[2]

with gzip.open(input_fasta, 'rt') as fin, open(output_fasta, 'w') as fout:
    keep = False
    for line in fin:
        if line.startswith('>'):
            header = line.strip().split()[0]
            # Keeping only transcript .1
            if header.endswith('.1'):
                keep = True
                fout.write(line)
            else:
                keep = False
        else:
            if keep:
                fout.write(line)
