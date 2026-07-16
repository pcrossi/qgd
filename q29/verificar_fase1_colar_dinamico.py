#!/usr/bin/env python3
"""Verificação simbólica da redução radial da Fase 1 da Q29.

Não resolve o background. Reconstrói as equações de Euler--Lagrange, a
restrição do lapse, os momentos de bordo e a matriz principal diretamente da
lagrangiana radial documentada.
"""

import sympy as sp


r = sp.symbols("r", real=True)
tau, h, n, lam = sp.symbols("tau h n lambda", nonzero=True, real=True)
N = sp.Function("N")(r)
a = sp.Function("a")(r)
c = sp.Function("c")(r)
f = sp.Function("f")(r)

ap, cp, fp = (sp.diff(x, r) for x in (a, c, f))

T_r = (
    2 * c * ap**2
    + 4 * a * ap * cp
    - 4 * a * c * fp * ap
    - 2 * a**2 * fp * cp
    + a**2 * c * fp**2
)
V_r = 8 * c - 2 * c**3 / a**2 - h**2 / (2 * a**2 * c)
L = sp.exp(-f) * (
    tau * T_r / N + N * tau * V_r + N * a**2 * c * (f - n - lam)
)


def euler_lagrange(x):
    """Convenção d/dr(dL/dx') - dL/dx."""
    return sp.simplify(sp.diff(sp.diff(L, sp.diff(x, r)), r) - sp.diff(L, x))


restriction = sp.factor(sp.exp(f) * sp.diff(L, N))
expected_restriction = sp.factor(-tau * T_r / N**2 + tau * V_r + a**2 * c * (f - n - lam))
assert sp.simplify(restriction - expected_restriction) == 0

momenta = sp.Matrix([sp.diff(L, sp.diff(x, r)) for x in (a, c, f)])
expected_momenta = sp.exp(-f) * sp.Matrix(
    [
        4 * tau * (c * ap + a * cp - a * c * fp) / N,
        2 * tau * a * (2 * ap - a * fp) / N,
        2 * tau * a * (a * c * fp - a * cp - 2 * c * ap) / N,
    ]
)
assert all(sp.simplify(x) == 0 for x in momenta - expected_momenta)

fields = (a, c, f)
principal = sp.Matrix(
    [[sp.diff(L, sp.diff(x, r), sp.diff(y, r)) for y in fields] for x in fields]
)
expected_det = 16 * tau**3 * sp.exp(-3 * f) * a**4 * c / N**3
assert sp.simplify(principal.det() - expected_det) == 0

print("Restrição do lapse verificada:")
sp.pprint(restriction)
print("\nMomentos de bordo verificados:")
sp.pprint(momenta)
print("\nDeterminante da matriz principal:")
sp.pprint(sp.factor(principal.det()))
print("\nEquações de Euler--Lagrange na gauge N=1 (divididas por 2 exp(-f)):")
for name, field in (("E_a", a), ("E_c", c), ("E_f", f)):
    equation = sp.simplify(sp.exp(f) * euler_lagrange(field).subs(N, 1) / 2)
    print(f"\n{name} =")
    sp.pprint(equation)

print("\nFASE 1: verificações simbólicas aprovadas.")
