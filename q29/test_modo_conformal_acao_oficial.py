#!/usr/bin/env python3
"""Teste exato do modo conformal homogêneo na ação oficial GDQ."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    sigma, tau, curvature, dimension, prefactor = sp.symbols(
        "sigma tau R d C", real=True, positive=True
    )
    # Medida preservada por f -> f + d sigma.
    potential = prefactor * (
        tau * curvature * sp.exp(-2 * sigma) + dimension * sigma
    )
    derivatives = [sp.simplify(sp.diff(potential, sigma, order)) for order in range(1, 5)]
    exp_stationary = dimension / (2 * tau * curvature)
    at_stationary = [
        sp.simplify(item.subs(sp.exp(-2 * sigma), exp_stationary))
        for item in derivatives
    ]

    print("Q29 — MODO CONFORMAL HOMOGÊNEO")
    print("V(sigma) =", potential)
    for order, item in enumerate(derivatives, start=1):
        print(f"V^{order} =", item)
    print("e^{-2 sigma_*} =", exp_stationary)
    for order, item in enumerate(at_stationary, start=1):
        print(f"V^{order}(sigma_*) =", item)

    assert sp.simplify(at_stationary[0]) == 0
    assert sp.simplify(at_stationary[1] - 2 * prefactor * dimension) == 0
    assert sp.simplify(at_stationary[3] - 8 * prefactor * dimension) == 0


if __name__ == "__main__":
    main()
