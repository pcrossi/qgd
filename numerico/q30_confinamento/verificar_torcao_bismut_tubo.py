#!/usr/bin/env python3
"""Verificação simbólica da norma e do fechamento da torção tubular."""

import sympy as sp

r = sp.symbols("r", positive=True)
B = sp.Function("B")(r)
W = sp.Function("W")(r)
P = sp.Function("P")(r)
Q = sp.Function("Q")(r)

# Cada coeficiente de 3-forma é 2 r X' exp(2X). A contração possui 3! termos.
def norm_component(X: sp.Expr) -> sp.Expr:
    h = 2 * r * sp.diff(X, r) * sp.exp(2 * X)
    inverse_metric_product = sp.exp(-2 * B) / r**2 * sp.exp(-4 * X)
    return sp.factor(sp.factorial(3) * h**2 * inverse_metric_product)


norm_h = sp.simplify(sum(norm_component(X) for X in (W, P, Q)))
expected = 24 * sp.exp(-2 * B) * sum(sp.diff(X, r) ** 2 for X in (W, P, Q))

print("norm_residual=", sp.simplify(norm_h - expected))

# dH=0 requer derivada radial nula de cada coeficiente independente.
closure = [sp.diff(2 * r * sp.diff(X, r) * sp.exp(2 * X), r) for X in (W, P, Q)]
for name, expression in zip(("W", "P", "Q"), closure):
    target = sp.diff(r * sp.diff(sp.exp(2 * {"W": W, "P": P, "Q": Q}[name]), r), r)
    print(f"closure_residual_{name}=", sp.simplify(expression - target))

if sp.simplify(norm_h - expected) != 0 or any(sp.simplify(x) != 0 for x in [
    closure[0] - sp.diff(r * sp.diff(sp.exp(2 * W), r), r),
    closure[1] - sp.diff(r * sp.diff(sp.exp(2 * P), r), r),
    closure[2] - sp.diff(r * sp.diff(sp.exp(2 * Q), r), r),
]):
    raise SystemExit("Falha na verificação simbólica.")
