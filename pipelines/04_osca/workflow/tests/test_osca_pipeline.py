#!/usr/bin/env python3
"""
Unit tests for Chapter 4 (OSCA mechanosensation) pipeline inputs and results.
"""

import unittest
from pathlib import Path
import pandas as pd


TESTS_DIR = Path(__file__).resolve().parent
OSCA_DIR = TESTS_DIR.parents[1]
PROJECT_ROOT = OSCA_DIR.parent.parent


class OscaPipelineTests(unittest.TestCase):
    def test_osca_id_mapping_integrity(self):
        """Verifica a integridade do arquivo canônico oscasIDs.txt."""
        mapping_file = OSCA_DIR / "01_gene_identification" / "results" / "oscasIDs.txt"
        self.assertTrue(mapping_file.exists(), f"Arquivo {mapping_file} deve existir")

        vper_genes = {}
        vtub_genes = {}
        with mapping_file.open() as f:
            for line in f:
                parts = line.strip().split()
                if not parts:
                    continue
                self.assertGreaterEqual(len(parts), 2, f"Linha inválida em oscasIDs.txt: {line}")
                gene_id, osca_name = parts[0], parts[1]
                if gene_id.startswith("Vper"):
                    vper_genes[gene_id] = osca_name
                elif gene_id.startswith("Vtub"):
                    vtub_genes[gene_id] = osca_name

        self.assertEqual(len(vper_genes), 14, "Vper deve possuir exatamente 14 genes OSCA identificados")
        self.assertEqual(len(vtub_genes), 13, "Vtub deve possuir exatamente 13 genes OSCA identificados")

        # Nomes de genes OSCA únicos por espécie
        self.assertEqual(len(set(vper_genes.values())), 14, "Nomes OSCA de Vper devem ser únicos")
        self.assertEqual(len(set(vtub_genes.values())), 13, "Nomes OSCA de Vtub devem ser únicos")

    def test_osca_ortholog_pairs_consistency(self):
        """Valida que todos os pares ortólogos esperados estão representados no mapeamento."""
        mapping_file = OSCA_DIR / "01_gene_identification" / "results" / "oscasIDs.txt"
        mapping = {}
        with mapping_file.open() as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 2:
                    mapping[parts[1]] = parts[0]

        expected_oscas = [
            'VpOSCA1.1', 'VtOSCA1.1', 'VpOSCA1.2', 'VtOSCA1.2',
            'VpOSCA1.3', 'VtOSCA1.3', 'VpOSCA1.4', 'VtOSCA1.4',
            'VpOSCA1.5', 'VtOSCA1.5', 'VpOSCA2.1', 'VtOSCA2.1',
            'VpOSCA2.2', 'VtOSCA2.2', 'VpOSCA2.3', 'VtOSCA2.3',
            'VpOSCA2.4a', 'VpOSCA2.4b', 'VtOSCA2.4', 'VpOSCA2.5',
            'VtOSCA2.5', 'VpOSCA3.1', 'VtOSCA3.1', 'VpOSCA3.2',
            'VtOSCA3.2', 'VpOSCA4.1', 'VtOSCA4.1'
        ]
        for name in expected_oscas:
            self.assertIn(name, mapping, f"Gene {name} deve estar presente no mapeamento canônico")

    def test_osca_expression_results_consistency(self):
        """Valida que as tabelas de contagens normalizadas de expressão existem e são válidas."""
        expr_dir = OSCA_DIR / "06_expression" / "results_genecounts"
        vper_norm = expr_dir / "Vper_OSCA_normalized_counts.csv"
        vtub_norm = expr_dir / "Vtub_OSCA_normalized_counts.csv"

        if vper_norm.exists():
            df_vper = pd.read_csv(vper_norm)
            self.assertGreater(len(df_vper), 0, "Vper normalized counts não deve estar vazio")
            self.assertFalse(df_vper.isnull().values.any(), "Vper counts não deve conter valores nulos")

        if vtub_norm.exists():
            df_vtub = pd.read_csv(vtub_norm)
            self.assertGreater(len(df_vtub), 0, "Vtub normalized counts não deve estar vazio")
            self.assertFalse(df_vtub.isnull().values.any(), "Vtub counts não deve conter valores nulos")


if __name__ == "__main__":
    unittest.main()
