"""Tests for gene-level one-to-one orthology and pairwise codon preparation."""
import importlib.util
import unittest

spec = importlib.util.find_spec('pair_specific_kaks')
if spec:
    import pair_specific_kaks as pair
else:
    pair = None


def row(og, a, b):
    return {'Orthogroup': og, 'Vper.pep': a, 'Vtub.pep': b}


class PairSpecificTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(pair, 'Pair-specific implementation is missing')

    def test_multiple_disjoint_pairs_in_same_orthogroup_are_retained(self):
        accepted, rejected = pair.select_pairs([row('OG1', 'a', 'x'), row('OG1', 'b', 'y')])
        self.assertEqual(len(accepted), 2)
        self.assertEqual(rejected, [])

    def test_singleton_row_is_not_enough_when_gene_has_other_partners(self):
        accepted, rejected = pair.select_pairs([row('OG1', 'a', 'x'), row('OG1', 'a', 'y, z')])
        self.assertEqual(accepted, [])
        self.assertEqual(len(rejected), 1)
        self.assertEqual(rejected[0]['Vper_Degree'], 3)

    def test_many_to_one_partner_is_excluded(self):
        accepted, rejected = pair.select_pairs([row('OG1', 'a', 'x'), row('OG1', 'b, c', 'x')])
        self.assertEqual(accepted, [])
        self.assertEqual(rejected[0]['Vtub_Degree'], 3)

    def test_duplicate_rows_do_not_duplicate_pairs(self):
        accepted, rejected = pair.select_pairs([row('OG1', 'a', 'x'), row('OG1', 'a', 'x')])
        self.assertEqual(len(accepted), 1)

    def test_focal_duplicates_in_other_species_are_not_required(self):
        accepted, _ = pair.select_pairs([row('OG1', 'a', 'x')])
        self.assertEqual((accepted[0]['Vper_Gene'], accepted[0]['Vtub_Gene']), ('a', 'x'))

    def test_pair_alignment_retains_translation_after_internal_insertion(self):
        full, score, algorithm = pair.align_proteins('MAVLGGKT', 'MAVLKT')
        seqs, qc = pair.kaks.prepare_pair(full, full,
            {'Vper': 'ATGGCTGTTCTTGGTGGTAAAACTTAA', 'Vtub': 'ATGGCTGTTCTTAAAACTTAA'})
        self.assertEqual(seqs['Vper'], 'ATGGCTGTTCTTAAAACT')
        self.assertEqual(seqs['Vtub'], 'ATGGCTGTTCTTAAAACT')
        self.assertEqual(qc['codons'], 6)


if __name__ == '__main__':
    unittest.main()
