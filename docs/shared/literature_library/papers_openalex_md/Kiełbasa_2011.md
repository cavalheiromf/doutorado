# Adaptive seeds tame genomic sequence comparison

**Authors:** Kiełbasa, S. M., Wan, R., Sato, K., Horton, P., & Frith, M. C. (2011)
**DOI:** 10.1101/gr.113985.110

## Abstract

The main way of analyzing biological sequences is by comparing and aligning them to each other. It remains difficult, however, to compare modern multi-billionbase DNA data sets. The difficulty is caused by the nonuniform (oligo)nucleotide composition of these sequences, rather than their size per se. To solve this problem, we modified the standard seed-and-extend approach (e.g., BLAST) to use adaptive seeds. Adaptive seeds are matches that are chosen based on their rareness, instead of using fixed-length matches. This method guarantees that the number of matches, and thus the running time, increases linearly, instead of quadratically, with sequence length. LAST, our open source implementation of adaptive seeds, enables fast and sensitive comparison of large sequences with arbitrarily nonuniform composition.
