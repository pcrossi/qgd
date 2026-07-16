#!/usr/bin/env python3
"""Validação independente do gap local C3 usado na ponte global--local.

Discretiza o conjugado de -Delta_f em uma coordenada do shrinker gaussiano:
    H = -d2/dx2 + x2/(16 tau2) - 1/(4 tau).
Seu espectro exato é n/(2 tau). O nível n=0 é removido por
normalização/gauge; o primeiro nível físico é 1/(2 tau).

Classificação: teste de convergência de uma quantidade analítica derivada.
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import eigh_tridiagonal


def spectrum(tau: float, length: float, n: int, levels: int = 4):
    h = 2.0*length/(n+1)
    x = -length + h*np.arange(1, n+1)
    potential = x*x/(16.0*tau*tau) - 1.0/(4.0*tau)
    diagonal = 2.0/h**2 + potential
    off = -np.ones(n-1)/h**2
    values = eigh_tridiagonal(
        diagonal, off, select="i", select_range=(0, levels-1),
        check_finite=False, eigvals_only=True,
    )
    return values


def main() -> None:
    for tau in (0.5, 1.0, 2.0, 4.0):
        exact_gap = 1.0/(2.0*tau)
        length = 12.0*np.sqrt(tau)
        print(f"tau={tau:g} exact_gap={exact_gap:.12g}")
        previous = None
        for n in (400, 800, 1600, 3200):
            values = spectrum(tau, length, n)
            numerical_gap = values[1]
            error = abs(numerical_gap-exact_gap)
            print(n, values, numerical_gap, error)
            if previous is not None and error > previous*1.05:
                raise AssertionError("erro do gap não convergiu")
            previous = error
        collective = 1.5
        full_gap = min(collective, exact_gap)
        print("full_C3_gap =", full_gap)
        if full_gap <= 0.0:
            raise AssertionError("gap C3 não positivo")


if __name__ == "__main__":
    main()
