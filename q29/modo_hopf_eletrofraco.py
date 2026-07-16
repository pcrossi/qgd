#!/usr/bin/env python3
"""Verifica o dupleto de Hopf e a matriz de massa eletrofraca."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    g, gp, v = sp.symbols("g gp v", positive=True, real=True)
    mass_matrix = (v**2 / 4) * sp.Matrix([[g**2, -g * gp], [-g * gp, gp**2]])
    eigenvalues = mass_matrix.eigenvals()
    determinant = sp.factor(mass_matrix.det())
    trace = sp.factor(sp.trace(mass_matrix))

    # Harmônico l=1 em S3: lambda=l(l+2)/R².
    radius = sp.symbols("R", positive=True, real=True)
    laplace_l1 = sp.Integer(3) / radius**2

    print("Q29 — MODO DE HOPF ELETROFRACO")
    print("lambda_l=1 =", laplace_l1)
    print("M_neutra =")
    sp.pprint(mass_matrix)
    print("det =", determinant)
    print("trace =", trace)
    print("autovalores =", eigenvalues)

    assert determinant == 0
    assert trace == v**2 * (g**2 + gp**2) / 4
    assert laplace_l1 == 3 / radius**2


if __name__ == "__main__":
    main()
