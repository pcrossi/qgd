#!/usr/bin/env python3
"""Diagonalização generalizada do setor neutro Hopf/Bismut da Q29."""

from __future__ import annotations

import numpy as np
from scipy.linalg import eigh

K_BASE = 41.594825709
DELTA_B = -0.2709378870534


def main() -> None:
    gram = 0.25*np.array([[1.0, DELTA_B], [DELTA_B, 1.0]])
    kinetic = K_BASE*gram
    mass = 0.25*np.array([[1.0, -1.0], [-1.0, 1.0]])
    values, vectors = eigh(mass, kinetic)
    q = np.array([1.0, 1.0])
    qnorm = float(q@kinetic@q)
    alpha_inv = 4*np.pi*qnorm
    photon = vectors[:, 0]
    print("Q29 — DIAGONALIZAÇÃO GENERALIZADA NEUTRA")
    print("K =")
    print(kinetic)
    print("M² (escala comum omitida) =")
    print(mass)
    print("autovalores generalizados =", values)
    print("autovetores K-ortonormais =")
    print(vectors)
    print("kernel M² normalizado euclidiano =", q/np.linalg.norm(q))
    print(f"norma cinética de Q = {qnorm:.12e}")
    print(f"alpha^-1 se 1/e²=||Q||²_K = {alpha_inv:.12e}")
    print(f"checagem M² photon = {np.linalg.norm(mass@photon):.12e}")
    assert abs(values[0]) < 1e-12
    assert values[1] > 0
    assert np.linalg.norm(mass@photon) < 1e-12


if __name__ == "__main__":
    main()
