"""Regression tests for codon homology and transparent YN00 estimation."""
import unittest

import calculate_kaks_1to1 as kaks


class CodonTests(unittest.TestCase):
    def test_trimmed_protein_cannot_be_threaded_from_original_cds(self):
        with self.assertRaises(ValueError):
            kaks.thread_cds('MK', 'ATGGCTGCTAAGTAA')

    def test_full_alignment_preserves_gaps_and_terminal_stop(self):
        self.assertEqual(kaks.thread_cds('M-AK', 'ATGGCTAAGTAA'), 'ATG---GCTAAG')

    def test_internal_stop_is_rejected(self):
        with self.assertRaises(ValueError):
            kaks.thread_cds('MXK', 'ATGTAAAAG')

    def test_non_triplet_cds_is_rejected(self):
        with self.assertRaises(ValueError):
            kaks.thread_cds('MA', 'ATGGCTA')

    def test_trim_mask_applies_to_corresponding_codons(self):
        self.assertTrue(hasattr(kaks, 'prepare_pair'), 'Missing validated codon preparation')
        full = {'Vper': 'MAAK', 'Vtub': 'M--K', **{f'S{i}': 'M--K' for i in range(5)}}
        trimmed = {s: 'MK' for s in full}
        seqs, qc = kaks.prepare_pair(full, trimmed, {'Vper': 'ATGGCTGCTAAGTAA', 'Vtub': 'ATGAAGTAA'})
        self.assertEqual(seqs, {'Vper': 'ATGAAG', 'Vtub': 'ATGAAG'})
        self.assertEqual(qc['kept_columns_1based'], [1, 4])

    def test_unreproducible_trim_mask_is_rejected(self):
        self.assertTrue(hasattr(kaks, 'prepare_pair'))
        with self.assertRaises(ValueError):
            kaks.prepare_pair({'Vper': 'MAK', 'Vtub': 'MAK'}, {'Vper': 'MK', 'Vtub': 'MK'},
                              {'Vper': 'ATGGCTAAG', 'Vtub': 'ATGGCTAAG'})

    def test_ambiguous_codon_is_removed_as_a_pair(self):
        self.assertTrue(hasattr(kaks, 'prepare_pair'))
        seqs, qc = kaks.prepare_pair({'Vper': 'MXK', 'Vtub': 'MAK'}, {'Vper': 'MXK', 'Vtub': 'MAK'},
                                    {'Vper': 'ATGNNNAAG', 'Vtub': 'ATGGCTAAG'})
        self.assertEqual(seqs['Vtub'], 'ATGAAG')
        self.assertEqual(qc['removed_invalid_codons'], 1)


class EstimationTests(unittest.TestCase):
    def test_no_silent_nei_gojobori_fallback(self):
        with self.assertRaises(ValueError):
            kaks.parse_yn00_output('(A) Nei-Gojobori\nVtub 2.0 (0.2 0.1)\n')

    def test_parse_yn00_with_standard_errors(self):
        result = kaks.parse_yn00_output('(B) Yang & Nielsen (2000) method\n'
            ' 2 1 100.0 300.0 0.12 2.5 0.25 0.0200 +- 0.0040 0.0800 +- 0.0100\n(C) Other\n')
        self.assertIsInstance(result, dict)
        self.assertEqual(result['dN'], 0.02)
        self.assertEqual(result['dS_SE'], 0.01)

    def test_zero_ds_and_boundary_are_not_screen_candidates(self):
        self.assertTrue(hasattr(kaks, 'classify_estimate'))
        row = {'dN': 0.0286, 'dS': -0.0, 'omega': 99.0, 'dN_SE': 0.01, 'dS_SE': 0.0}
        status, screen, flags = kaks.classify_estimate(row)
        self.assertNotEqual(status, 'PASS')
        self.assertNotEqual(screen, 'omega_gt_1')

    def test_omega_below_one_is_not_called_neutral(self):
        self.assertTrue(hasattr(kaks, 'classify_estimate'))
        status, screen, flags = kaks.classify_estimate(
            {'dN': 0.06, 'dS': 0.08, 'omega': 0.75, 'dN_SE': 0.01, 'dS_SE': 0.01})
        self.assertEqual((status, screen), ('PASS', 'omega_lt_1'))


if __name__ == '__main__':
    unittest.main()
