#!/usr/bin/env python3
"""Testes da varredura multiespécie Q34/Q35."""

import unittest

from sweep_especies_u1 import (
    audit_scenario,
    charged_fermion_benchmark,
    critical_scale,
    leptons_gdq,
    pi_infinity,
)


class SweepSpeciesTests(unittest.TestCase):
    def test_pesos(self) -> None:
        self.assertAlmostEqual(sum(x.weight for x in leptons_gdq()), 3.0)
        self.assertAlmostEqual(sum(x.weight for x in charged_fermion_benchmark()), 8.0)

    def test_raiz_leptonica(self) -> None:
        species = leptons_gdq()
        root = critical_scale(species)
        self.assertAlmostEqual(pi_infinity(root, species), 1.0, places=11)
        self.assertLess(pi_infinity(root - 1.0, species), 1.0)
        self.assertGreater(pi_infinity(root + 1.0, species), 1.0)

    def test_raiz_todas_especies(self) -> None:
        species = charged_fermion_benchmark()
        root = critical_scale(species)
        self.assertAlmostEqual(pi_infinity(root, species), 1.0, places=11)

    def test_monotonicidade(self) -> None:
        self.assertTrue(audit_scenario("teste", leptons_gdq())["monotone"])


if __name__ == "__main__":
    unittest.main()
