#!/usr/bin/env python3
"""Extract and rename the OSCA transcript structures from a Helixer GTF."""
import re
import sys
from pathlib import Path

src, mapping_path, out = map(Path, sys.argv[1:])
mapping = {}
for line in mapping_path.read_text().splitlines():
    if line.strip():
        original, short = line.split('\t')
        mapping[original] = short

rank = {name: i for i, name in enumerate(mapping.values())}
records = []
for line in src.read_text().splitlines():
    if not line or line.startswith('#'):
        continue
    fields = line.split('\t')
    if len(fields) != 9:
        continue
    match = re.search(r'transcript_id "([^"]+)"', fields[8])
    if not match or match.group(1) not in mapping:
        continue
    short = mapping[match.group(1)]
    fields[8] = re.sub(r'transcript_id "[^"]+"', f'transcript_id "{short}"', fields[8])
    fields[8] = re.sub(r'gene_id "[^"]+"', f'gene_id "{short}"', fields[8])
    records.append((rank[short], int(fields[3]), fields))

records.sort(key=lambda x: (x[0], x[1], {'transcript': 0, 'exon': 1, 'CDS': 2}.get(x[2][2], 9)))
out.write_text('\n'.join('\t'.join(fields) for _, _, fields in records) + '\n')
print(f'{out}: {len(records)} records')
