import importlib.util
import tempfile
import unittest
from pathlib import Path

import pandas as pd


REVIEW_DIR = Path(__file__).resolve().parents[2]
MASTER_BUILDER = (
    REVIEW_DIR
    / "workflow"
    / "scripts"
    / "03_functional_enrichment"
    / "00_build_master_table_6taxa.py"
)


def load_builder():
    spec = importlib.util.spec_from_file_location("cafe5_master_builder", MASTER_BUILDER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class Cafe5MasterTableTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_builder()

    def test_resolves_primary_and_near_optimal_m5_runs(self):
        table = pd.DataFrame(
            {
                "replicate": ["rep_4", "rep_6", "rep_8", "rep_2"],
                "rep_dir": ["/runs/rep_4", "/runs/rep_6", "/runs/rep_8", "/runs/rep_2"],
                "selected_primary": [True, False, False, False],
                "near_optimal": [True, True, True, False],
            }
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "summary.tsv"
            table.to_csv(path, sep="\t", index=False)
            primary, sensitivity = self.module.resolve_m5_runs(path)

        self.assertEqual(primary.name, "rep_4")
        self.assertEqual([path.name for path in sensitivity], ["rep_4", "rep_6", "rep_8"])

    def test_robust_flags_are_intersection_of_near_optimal_runs(self):
        flags = {
            "rep_4": pd.Series([True, True, False], index=["OG1", "OG2", "OG3"]),
            "rep_6": pd.Series([True, False, False], index=["OG1", "OG2", "OG3"]),
            "rep_8": pd.Series([True, True, False], index=["OG1", "OG2", "OG3"]),
        }

        observed = self.module.intersect_flags(flags)

        self.assertEqual(observed.to_dict(), {"OG1": True, "OG2": False, "OG3": False})


if __name__ == "__main__":
    unittest.main()
