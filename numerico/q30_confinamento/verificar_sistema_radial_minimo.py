#!/usr/bin/env python3
"""Deriva simbolicamente as E-L radiais e a condição de compatibilidade."""

import sympy as sp

r = sp.symbols("r", positive=True)
c0, c1, q, n = sp.symbols("c0 c1 q n", nonzero=True)
a = sp.Function("a")(r)
u = sp.Function("u")(r)
v = sp.Function("v")(r)

lagrangian = r * sp.exp(-u) * (
    c1 * (
        -sp.diff(a, r) ** 2 / (2 * r**2)
        + sp.diff(u, r) ** 2
        + sp.diff(v, r) ** 2
        + (n - q * a) ** 2 / r**2
    )
    + c0 * (u - 4)
)


def euler(field: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.diff(sp.diff(lagrangian, sp.diff(field, r)), r) - sp.diff(lagrangian, field))


el_a = euler(a)
el_u = sp.simplify(sp.exp(u) * euler(u) / r)
el_v = euler(v)

expected_u = c1 * (
    2 * sp.diff(u, r, 2)
    + 2 * sp.diff(u, r) / r
    - sp.diff(u, r) ** 2
    + sp.diff(v, r) ** 2
    + (n - q * a) ** 2 / r**2
    - sp.diff(a, r) ** 2 / (2 * r**2)
) + c0 * (u - 5)

elongation = c1 * (
    2 * sp.diff(u, r, 2)
    + 2 * sp.diff(u, r) / r
    - sp.diff(u, r) ** 2
    + sp.diff(v, r) ** 2
    + (n - q * a) ** 2 / r**2
    - 3 * sp.diff(a, r) ** 2 / (2 * r**2)
) + c0 * (u - 4)

compatibility = sp.simplify(elongation - expected_u)

print("u_equation_residual=", sp.simplify(el_u - expected_u))
print("compatibility=", compatibility)
print("a_equation=", el_a)
print("v_equation=", el_v)

if sp.simplify(el_u - expected_u) != 0:
    raise SystemExit("Falha na equação de u.")
if sp.simplify(compatibility - (c0 - c1 * sp.diff(a, r) ** 2 / r**2)) != 0:
    raise SystemExit("Falha na condição de compatibilidade.")
