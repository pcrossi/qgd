#!/usr/bin/env python3
"""Jacobiana do equilíbrio torsional local sobre squashings do C3."""

import numpy as np


if __name__ == "__main__":
    angles = 2*np.pi*np.arange(3)/3
    directions = np.vstack((np.cos(angles), np.sin(angles)))
    # Fator t'(q) comum omitido: não altera kernel/rank.
    jacobian = directions
    _, singular, vh = np.linalg.svd(jacobian)
    common = np.ones(3)/np.sqrt(3)
    print("Q29 — EQUILÍBRIO LOCAL DE TORÇÃO NO BERGER")
    print("direções C3 =")
    print(directions)
    print("soma direções =", directions.sum(axis=1))
    print("valores singulares D C =", singular)
    print("kernel numérico =", vh[-1])
    print("D C . modo comum =", jacobian@common)
    assert np.allclose(directions.sum(axis=1), 0.0, atol=1e-14)
    assert np.linalg.matrix_rank(jacobian, tol=1e-12) == 2
    assert np.allclose(jacobian@common, 0.0, atol=1e-14)
