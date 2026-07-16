#!/usr/bin/env python3
"""Testes de regressão do solver comum às Q34/Q35."""

import math
import unittest

import numpy as np

from solve_polarizacao_u1 import (
    Config, alpha_eff, pi_infinity, pi_qed, pi_scalar, tensor, ward_error,
)


class PolarizacaoU1Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.cfg = Config(eta=1e-6, n_gauss=256)

    def test_subtracao(self) -> None:
        self.assertAlmostEqual(pi_scalar(0.0, self.cfg), 0.0, places=15)

    def test_ward(self) -> None:
        q = np.array([0.31, -0.47, 0.59, 0.83])
        _, relative = ward_error(q, tensor(q, pi_scalar(float(q @ q), self.cfg)))
        self.assertLess(relative, 1e-14)

    def test_saturacao(self) -> None:
        limit = pi_infinity(self.cfg)
        self.assertLess(pi_scalar(1e14, self.cfg), limit)
        self.assertLess(limit, 1.0)
        self.assertTrue(math.isfinite(alpha_eff(limit, self.cfg.alpha0)))

    def test_monotonicidade(self) -> None:
        values = [pi_scalar(float(r), self.cfg) for r in np.logspace(-6, 10, 60)]
        self.assertTrue(np.all(np.diff(values) >= -1e-13))

    def test_limite_qed(self) -> None:
        cfg = Config(eta=1e-12, n_gauss=512)
        for r in (1e-4, 1.0, 1e4):
            self.assertLess(abs(pi_scalar(r, cfg) - pi_qed(r, cfg.alpha0)), 2e-11)

    def test_refinamento(self) -> None:
        self.assertLess(
            abs(pi_scalar(1e4, self.cfg, 128) - pi_scalar(1e4, self.cfg, 256)),
            1e-11,
        )


if __name__ == "__main__":
    unittest.main()
