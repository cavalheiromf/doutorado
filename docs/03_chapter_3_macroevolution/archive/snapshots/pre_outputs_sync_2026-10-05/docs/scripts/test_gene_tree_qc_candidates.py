import unittest

from gene_tree_qc_candidates import focal_tree_metrics


class GeneTreeQCTests(unittest.TestCase):
    def test_focal_pair_only(self):
        result = focal_tree_metrics("(Vper_pep_a:0.1,Vtub_pep_b:0.1);", "a", "b")
        self.assertTrue(result["Focal_Pair_Sister"])
        self.assertEqual(result["Formal_Test_Eligibility"], "FOCAL_PAIR_ONLY")

    def test_third_species_is_potential(self):
        result = focal_tree_metrics(
            "((Vper_pep_a:0.1,Vtub_pep_b:0.1):0.1,Xvis_pep_c:0.1);", "a", "b"
        )
        self.assertEqual(result["Focal_MRCA_Leaves"], 2)
        self.assertEqual(result["Formal_Test_Eligibility"], "FOCAL_PAIR_ONLY")

        result = focal_tree_metrics(
            "(Vper_pep_a:0.1,Vtub_pep_b:0.1,Xvis_pep_c:0.1);", "a", "b"
        )
        self.assertEqual(result["Focal_MRCA_Leaves"], 3)
        self.assertEqual(result["Formal_Test_Eligibility"], "POTENTIAL_MULTI_SPECIES")

    def test_duplicate_species_is_flagged(self):
        result = focal_tree_metrics(
            "(Vper_pep_a:0.1,Vper_pep_c:0.1,Vtub_pep_b:0.1);", "a", "b"
        )
        self.assertEqual(result["Formal_Test_Eligibility"], "DUPLICATE_SPECIES_IN_MRCA")

    def test_missing_focal_leaf(self):
        result = focal_tree_metrics("(Vper_pep_a:0.1,Xvis_pep_c:0.1);", "a", "b")
        self.assertEqual(result["Formal_Test_Eligibility"], "MISSING_FOCAL_LEAF")


if __name__ == "__main__":
    unittest.main()
