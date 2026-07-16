#!/usr/bin/env python3
"""Localiza o fold do ramo radial homogêneo de Berger na Q29."""

import numpy as np
from scipy.optimize import root


def equations(values):
    radius, q = values
    pi = np.pi
    d1 = -4*(4-q*q)/radius**3 + 3/(pi*pi*radius**7*q*q) + 3/radius
    d2 = 12*(4-q*q)/radius**4 - 21/(pi*pi*radius**8*q*q) - 3/radius**2
    return np.array([d1, d2])


if __name__ == "__main__":
    result = root(equations, [0.62, 1.89])
    radius, qcrit = result.x
    qtarget = np.sqrt(14.0/3.0)
    print("Q29 — FOLD DO RAMO DE BERGER")
    print("success             =", result.success)
    print(f"R_crit              = {radius:.12f}")
    print(f"q_crit              = {qcrit:.12f}")
    print(f"q_target            = {qtarget:.12f}")
    print(f"q_target-q_crit     = {qtarget-qcrit:.12f}")
    print(f"residual            = {np.linalg.norm(equations(result.x)):.3e}")
    assert result.success and qtarget > qcrit
