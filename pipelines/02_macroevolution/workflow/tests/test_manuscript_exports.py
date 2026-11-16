import importlib.util
import tempfile
import unittest
from pathlib import Path

import pandas as pd


REVIEW_DIR = Path(__file__).resolve().parents[2]
EXPORTER = REVIEW_DIR / "workflow" / "scripts" / "04_manuscript" / "01_export_manuscript_tables.py"


def load_exporter():
    spec = importlib.util.spec_from_file_location("manuscript_exporter", EXPORTER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class ManuscriptExportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_exporter()

    def test_branch_table_counts_current_boolean_flags(self):
        master = pd.DataFrame(
            {
                "BranchSig_Exp_Vper": [True, True, False],
                "BranchSig_Cont_Vper": [False, False, True],
                "BranchSig_Exp_Vper_Robust": [True, False, False],
                "BranchSig_Cont_Vper_Robust": [False, False, True],
            }
        )
        rows = self.module.build_branch_table(master, branches=[("Terminal Vper", "Vper", "V. peripherica", "Terminal")])
        self.assertEqual(rows[0]["Expansions_Sig"], 2)
        self.assertEqual(rows[0]["Contractions_Sig"], 1)
        self.assertEqual(rows[0]["Expansions_Robust"], 1)

    def test_duplication_table_uses_singleton_not_transposed(self):
        master = pd.DataFrame({"FamilyID": ["OG1", "OG2"], "BranchSig_Exp_Vper": [True, False]})
        genes = pd.DataFrame(
            {
                "gene_id": ["g1", "g2", "g3", "g4"],
                "orthogroup": ["OG1", "OG1", "OG2", "OG2"],
                "dup_type": ["Tandem", "Singleton", "Dispersed", "Singleton"],
            }
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "dup.tsv"
            genes.to_csv(path, sep="\t", index=False)
            rows = self.module.build_duplication_rows(master, path, "Vper", "V. peripherica")

        self.assertIn("Singleton_pct", rows[0])
        self.assertNotIn("Transposed_pct", rows[0])
        self.assertEqual(rows[1]["Total_Genes"], 2)


if __name__ == "__main__":
    unittest.main()
