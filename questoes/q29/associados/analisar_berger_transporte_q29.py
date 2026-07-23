#!/usr/bin/env python3
"""Hessiana e transporte de normas no ansatz homogêneo de Berger da Q29."""

from __future__ import annotations

import numpy as np
from scipy.optimize import root_scalar

R = 1.998411184770


def hessian_at_round(radius=R):
    pi = np.pi
    hrr = -3 / radius**2 + 36 / radius**4 - 21 / (pi**2 * radius**8)
    hrq = 8 / radius**3 - 6 / (pi**2 * radius**7)
    hqq = -1 - 4 / radius**2 - 3 / (pi**2 * radius**6)
    return np.array([[hrr, hrq], [hrq, hqq]])


def norm_ratio(q):
    # Média de um gerador SU(2)_L sobre as três direções do corpo, dividida
    # pela norma da fibra U(1)_R de Hopf.
    return (2.0 + q**2) / (3.0 * q**2)


if __name__ == "__main__":
    h = hessian_at_round()
    eigenvalues = np.linalg.eigvalsh(h)
    schur = h[1, 1] - h[1, 0] ** 2 / h[0, 0]
    target = 10.0 / 21.0
    solution = root_scalar(lambda q: norm_ratio(q) - target, bracket=(1.0, 5.0))
    q_target = solution.root
    print("Q29 — BERGER: HESSIANA E TRANSPORTE")
    print("H(R,q=1) =")
    print(h)
    print("spec(H) =", eigenvalues)
    print(f"H_q efetiva após Schur = {schur:.12f}")
    print(f"q para Z_W/Z_Y=10/21  = {q_target:.12f}")
    print(f"q²                       = {q_target**2:.12f}")
    print(f"razão calculada           = {norm_ratio(q_target):.12f}")
    assert eigenvalues[0] < 0 < eigenvalues[1]
    assert schur < 0
    assert abs(q_target**2 - 14.0 / 3.0) < 1e-12
