import io
import unittest
from Bio import Phylo
import audit_pair_specific_kaks as audit


class AuditTests(unittest.TestCase):
    def test_gap_flanks_keep_original_codon_coordinates(self):
        full = {'Vper': 'MA-KLMN', 'Vtub': 'MAGKLMN'}
        cds = {'Vper': 'ATGGCTAAACTGATGAAT', 'Vtub': 'ATGGCTGGTAAACTGATGAAT'}
        seq, qc = audit.project_with_mask(full, cds, flank=1)
        self.assertEqual(qc['kept_columns_1based'], [1, 5, 6, 7])
        self.assertEqual(seq['Vper'], 'ATGCTGATGAAT')
        self.assertEqual(seq['Vtub'], 'ATGCTGATGAAT')

    def test_no_gap_mask_keeps_all_valid_codons(self):
        seq, qc = audit.project_with_mask({'Vper': 'MA', 'Vtub': 'MA'},
                                        {'Vper': 'ATGGCT', 'Vtub': 'ATGGCC'}, flank=3)
        self.assertEqual(qc['codons'], 2)
        self.assertEqual(seq['Vtub'], 'ATGGCC')

    def test_multiple_outgroup_copies_are_retained(self):
        maps = {'Vper': {'a': {'x', 'y', 'z'}}, 'Vtub': {'b': {'x', 'y'}}}
        self.assertEqual(audit.shared_orthologs(maps, 'a', 'b'), {'x', 'y'})

    def test_unilateral_ortholog_is_not_shared(self):
        maps = {'Vper': {'a': {'x'}}, 'Vtub': {'b': {'y'}}}
        self.assertEqual(audit.shared_orthologs(maps, 'a', 'b'), set())

    def test_tree_reports_extra_focal_paralog(self):
        tree = Phylo.read(io.StringIO('((Vper_pep_a,Vper_pep_c),(Vtub_pep_b,Xvis_pep_x));'), 'newick')
        info = audit.focal_tree_context(tree, 'a', 'b')
        self.assertEqual(info['Focal_MRCA_Extra_Focal_Copies'], 1)

    def test_tree_with_many_external_copies_keeps_focal_one_to_one(self):
        tree = Phylo.read(io.StringIO('((Vper_pep_a,Vtub_pep_b),(Xvis_pep_x,Xvis_pep_y));'), 'newick')
        info = audit.focal_tree_context(tree, 'a', 'b')
        self.assertEqual(info['Focal_MRCA_Extra_Focal_Copies'], 0)

    def test_invalid_variant_prevents_stable_classification(self):
        rows = [{'QC_Status': 'PASS', 'Omega_KaKs': 1.2}, {'QC_Status': 'HIGH_DS', 'Omega_KaKs': 2}]
        self.assertEqual(audit.stability_class(rows), 'INCOMPLETE_QC')

    def test_crossing_one_is_sensitive(self):
        rows = [{'QC_Status': 'PASS', 'Omega_KaKs': 1.2}, {'QC_Status': 'PASS', 'Omega_KaKs': 0.9}]
        self.assertEqual(audit.stability_class(rows), 'CROSSES_ONE')


if __name__ == '__main__':
    unittest.main()
