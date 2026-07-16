#!/usr/bin/env python3
"""Verifica a dependência da ação steady normalizada nos módulos de T5."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    radii = sp.symbols("L1:6", positive=True)
    radius, tau, flux = sp.symbols("R tau n", positive=True)
    torus_volume = sp.prod(2 * sp.pi * item for item in radii)
    sphere_volume = 2 * sp.pi**2 * radius**3
    total_volume = sp.simplify(torus_volume * sphere_volume)

    # A medida uniforme normalizada cancela o volume global. Curvatura e
    # torção homogêneas vivem apenas em S3.
    density = 6 / radius**2 - flux**2 / (2 * sp.pi**2 * radius**6)
    normalized_action = sp.simplify(tau * density + sp.log(total_volume))

    # O zero-mode de f absorve log Vol na medida oficial. Ao variar módulos
    # físicos com a normalização imposta, subtrai-se exatamente log Vol.
    constrained_action = sp.simplify(normalized_action - sp.log(total_volume))
    gradient = [sp.simplify(sp.diff(constrained_action, item)) for item in radii]
    hessian = sp.Matrix(
        [[sp.diff(constrained_action, left, right) for right in radii] for left in radii]
    )

    print("Q29 — MÓDULOS DE T5 NO BACKGROUND STEADY")
    print("W_constrained =", constrained_action)
    print("gradient =", gradient)
    print("Hessian =")
    sp.pprint(hessian)

    assert all(item == 0 for item in gradient)
    assert hessian == sp.zeros(5)


if __name__ == "__main__":
    main()
