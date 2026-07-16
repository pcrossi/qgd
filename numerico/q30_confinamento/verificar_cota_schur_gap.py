#!/usr/bin/env python3
"""Verifica simbolicamente o critério de positividade da cota em blocos."""

import sympy as sp

ma2, mf2, b = sp.symbols("ma2 mf2 b", positive=True)
matrix = sp.Matrix([[ma2, -b], [-b, mf2]])
eigenvalues = list(matrix.eigenvals().keys())
lambda_minus = (ma2 + mf2 - sp.sqrt((ma2 - mf2) ** 2 + 4 * b**2)) / 2

print("characteristic=", sp.factor(matrix.det()))
print("lambda_minus_check=", [sp.simplify(ev - lambda_minus) for ev in eigenvalues])
print("positivity_criterion: b^2 < ma2*mf2")

if sp.factor(matrix.det()) != ma2 * mf2 - b**2:
    raise SystemExit("Falha no determinante de Schur.")
