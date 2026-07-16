#!/usr/bin/env python3
"""Verifica simbolicamente a variação linear do modo de elongação S."""

import sympy as sp

r = sp.symbols("r", positive=True)
eps = sp.symbols("eps")
c0, c1 = sp.symbols("c0 c1")
u = sp.Function("u")(r)
s = sp.Function("s")(r)
kf = sp.Function("K_f")(r)
f2 = sp.Function("F2")(r)

# S=eps*s. R_KK=-1/4 exp(2S)F2-2(S''+S'/r)-2(S')^2.
S = eps * s
r_kk = -sp.exp(2 * S) * f2 / 4 - 2 * (sp.diff(S, r, 2) + sp.diff(S, r) / r) - 2 * sp.diff(S, r) ** 2
density = r * sp.exp(S - u) * (c1 * (r_kk + kf) + c0 * (u - 4))
linear_density = sp.diff(density, eps).subs(eps, 0)

# Euler operator em s; ele produz o coeficiente local da variação.
euler = (
    sp.diff(linear_density, s)
    - sp.diff(sp.diff(linear_density, sp.diff(s, r)), r)
    + sp.diff(sp.diff(linear_density, sp.diff(s, r, 2)), r, 2)
)
reduced = sp.simplify(sp.exp(u) * euler / r)
expected = c1 * (
    -3 * f2 / 4
    + kf
    + 2 * (sp.diff(u, r, 2) + sp.diff(u, r) / r)
    - 2 * sp.diff(u, r) ** 2
) + c0 * (u - 4)

residual = sp.simplify(reduced - expected)
print("elongation_variation_residual=", residual)
if residual != 0:
    raise SystemExit("Falha na variação do modo de elongação.")
