import importlib.util
import unittest
from pathlib import Path

import pandas as pd


REVIEW_DIR = Path(__file__).resolve().parents[2]
EVALUATOR = REVIEW_DIR / "workflow" / "scripts" / "01_cafe5" / "05_evaluate_cafe5_models.py"
STAGE4 = REVIEW_DIR / "workflow" / "scripts" / "01_cafe5" / "06_run_cafe5_stage4_gamma_branch_lambdas.slurm"
M5_EXTRA_REPS = REVIEW_DIR / "workflow" / "scripts" / "01_cafe5" / "07_run_cafe5_m5_gamma_reps6_10.slurm"


def load_evaluator():
    spec = importlib.util.spec_from_file_location("cafe5_model_evaluation", EVALUATOR)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class Cafe5ModelEvaluationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_evaluator()

    def test_counts_only_parameters_optimized_in_the_run(self):
        self.assertEqual(
            self.module.free_parameter_count(
                n_lambdas=4,
                estimate_alpha=True,
                estimate_epsilon=False,
                estimate_root_distribution=True,
            ),
            6,
        )

    def test_declares_gamma_k3_branch_model_grid(self):
        specs = {spec["label"]: spec for spec in self.module.get_model_specs()}

        expected = {
            "Gamma_k3_M2_2lambda_family": 2,
            "Gamma_k3_M3_3lambda_vellozia_clade": 3,
            "Gamma_k3_M4_3lambda_avoidant_shift": 3,
            "Gamma_k3_M5_4lambda_split_sisters": 4,
        }
        for label, n_lambdas in expected.items():
            with self.subTest(label=label):
                self.assertIn(label, specs)
                self.assertTrue(specs[label]["is_gamma"])
                self.assertEqual(specs[label]["n_lambdas"], n_lambdas)
                self.assertEqual(specs[label]["comparison_group"], "gamma_k3_branch_rates")

    def test_stage4_combines_gamma_and_lambda_tree_options(self):
        text = STAGE4.read_text(encoding="utf-8")
        self.assertIn('-k "${GAMMA_CATEGORIES}"', text)
        self.assertIn('-y "${ltree}"', text)
        self.assertIn("stage4_gamma_branch_lambdas", text)

    def test_additional_m5_run_is_limited_to_replicates_6_through_10(self):
        text = M5_EXTRA_REPS.read_text(encoding="utf-8")
        self.assertIn("#SBATCH --array=6-10", text)
        self.assertIn('MODEL_NAME="M5_4lambda_split_sisters"', text)
        self.assertIn('REP="${SLURM_ARRAY_TASK_ID:?', text)
        self.assertIn('REP_DIR="${OUT_BASE}/${MODEL_NAME}/rep_${REP}"', text)
        self.assertIn('if (( REP < 6 || REP > 10 )); then', text)
        self.assertIn('if [ -f "${REP_DIR}/Gamma_results.txt" ]; then', text)
        self.assertIn('-k "${GAMMA_CATEGORIES}"', text)
        self.assertIn('-y "${LAMBDA_TREE}"', text)

    def test_summarizes_near_optimal_m5_replicates_and_rate_ratio(self):
        replicates = pd.DataFrame(
            [
                {
                    "model": "Gamma_k3_M5_4lambda_split_sisters",
                    "replicate": "rep_4",
                    "neg_lnL": 100.00,
                    "lambdas": "0.002,0.003,0.004,0.008",
                    "alpha": 1.1,
                    "converged": True,
                    "rep_dir": "/tmp/rep_4",
                },
                {
                    "model": "Gamma_k3_M5_4lambda_split_sisters",
                    "replicate": "rep_6",
                    "neg_lnL": 100.08,
                    "lambdas": "0.0021,0.0031,0.0041,0.0082",
                    "alpha": 1.2,
                    "converged": True,
                    "rep_dir": "/tmp/rep_6",
                },
                {
                    "model": "Gamma_k3_M5_4lambda_split_sisters",
                    "replicate": "rep_7",
                    "neg_lnL": 102.00,
                    "lambdas": "0.002,0.003,0.004,0.008",
                    "alpha": 1.0,
                    "converged": True,
                    "rep_dir": "/tmp/rep_7",
                },
            ]
        )

        observed = self.module.summarize_m5_convergence(replicates, near_optimal_delta=0.1)

        self.assertEqual(observed["replicate"].tolist(), ["rep_4", "rep_6", "rep_7"])
        self.assertEqual(observed["near_optimal"].tolist(), [True, True, False])
        self.assertAlmostEqual(observed.loc[0, "delta_neg_lnL"], 0.0)
        self.assertAlmostEqual(observed.loc[1, "delta_neg_lnL"], 0.08)
        self.assertAlmostEqual(observed.loc[0, "lambda_Vper"], 0.008)
        self.assertAlmostEqual(observed.loc[0, "lambda_Vtub"], 0.004)
        self.assertAlmostEqual(observed.loc[0, "Vper_to_Vtub_ratio"], 2.0)


if __name__ == "__main__":
    unittest.main()
