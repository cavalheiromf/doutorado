# OSCA3-only HyPhy RELAX verification

This directory contains a reproducible rerun restricted to the four *Vellozia* OSCA3 sequences:

- `Vper.hapA.v1.chr1A.g020450.t1` (*VpOSCA3.1*)
- `Vtub.hapA.v1.chr1A.g018250.t1` (*VtOSCA3.1*)
- `Vper.hapA.v1.chr5A.g142080.t1` (*VpOSCA3.2*)
- `Vtub.hapA.v1.chr5A.g129040.t1` (*VtOSCA3.2*)

The two OSCA4 sequences used in the legacy `osca3_4` analysis are explicitly absent from both the codon alignment and the labeled tree. The primary gap filter removed alignment columns containing gaps in more than 20% of the four sequences; because one gapped sequence corresponds to 25%, this retained 733 gap-free codons.

HyPhy RELAX v2.5.99 consistently returned a selection-intensity estimate below one, but the likelihood-ratio test was not significant. Across the primary fit and optimization sensitivities, *K* ranged from 0.2565 to 0.3188 and *p* from 0.0745 to 0.0752. The less restrictive gap filter retained 734 codons and likewise remained non-significant (*K* = 0.2899, *p* = 0.0675). The previously plotted value (*K* = 0.2563, *p* = 0.0757) is therefore closely reproduced in direction, magnitude, and inferential conclusion, although its exact digits vary with stochastic initialization.

The scientifically supported conclusion is that OSCA3 alone shows a point estimate in the direction of relaxed selection, but no statistically significant evidence of a shift in selection intensity at the adopted alpha level of 0.05. The significant legacy `osca3_4` result must not be attributed to OSCA3.

Files:

- `relax_summary.tsv`: compact results for all reruns.
- `provenance.json`: commands, versions, input and intermediate-file checksums, retained-site counts, and sequence membership.
- `osca3_codon_gap20.fasta` and `osca3_codon_gap50.fasta`: analyzed codon alignments.
- `osca3_labeled.treefile`: pruned tree with Test and Reference terminal branches.
- `relax_*.json`: complete HyPhy outputs.
- `relax_*.stdout.log` and `relax_*.stderr.log`: execution logs.
- `osca3_*_site_map.tsv`: filtered-to-unfiltered codon coordinate maps.

The analysis can be regenerated with:

```bash
/home/mfcaval/.local/share/mamba/envs/jcviEnv/bin/python \
  chapter2_osca/workflow/scripts/03_run_hyphy_osca3_only.py
```
