#!/usr/bin/env python3
"""Testa em Berger a transgressão de superfície já documentada na Q40."""

from __future__ import annotations

import numpy as np
from scipy.optimize import root

ALPHA = 1.0 / 137.03599907


def potential(values):
    r, q = values
    bulk = 2*(4-q*q)/r**2 - 1/(2*np.pi**2*r**6*q**2) + 3*np.log(r) + np.log(q)
    boundary = ALPHA * (3*np.pi/2 + 3/(4*np.pi**3*r**3*q))
    return bulk + boundary


def gradient(values):
    r, q = values
    d_r = -4*(4-q*q)/r**3 + 3/(np.pi**2*r**7*q**2) + 3/r
    d_q = -4*q/r**2 + 1/(np.pi**2*r**6*q**3) + 1/q
    coeff = ALPHA * 3/(4*np.pi**3)
    return np.array([d_r - 3*coeff/(r**4*q), d_q - coeff/(r**3*q**2)])


def numerical_hessian(point, step=1e-4):
    result = np.empty((2, 2))
    for j in range(2):
        delta = np.zeros(2); delta[j] = step
        result[:, j] = (gradient(point+delta)-gradient(point-delta))/(2*step)
    return 0.5*(result+result.T)


if __name__ == "__main__":
    solutions = []
    for seed in ([2,1], [.4,1], [1,1.5], [.6,1.8], [2,2]):
        answer = root(gradient, seed)
        if answer.success and np.all(answer.x > 0):
            if not any(np.linalg.norm(answer.x-old) < 1e-7 for old in solutions):
                solutions.append(answer.x)
    print("Q29 — TRANSGRESSÃO Q40 NO BERGER")
    for point in solutions:
        eig = np.linalg.eigvalsh(numerical_hessian(point))
        print(f"R={point[0]:.12f} q={point[1]:.12f} V={potential(point):.12f}")
        print("  spec Hess =", eig)
    print("número de mínimos locais =", sum(np.all(np.linalg.eigvalsh(numerical_hessian(p))>0) for p in solutions))
    assert solutions
    assert not any(np.all(np.linalg.eigvalsh(numerical_hessian(p)) > 0) for p in solutions)
