#!/usr/bin/env python3
"""Verifica o fechamento negativo da Fase 2 do colar dinâmico da Q29."""

import sympy as sp


a, c, tau, ef = sp.symbols("a c tau exp_minus_f", positive=True, real=True)
ap, cp, fp = sp.symbols("ap cp fp", real=True)

momenta = sp.Matrix(
    [
        4 * tau * ef * (c * ap + a * cp - a * c * fp),
        2 * tau * ef * a * (2 * ap - a * fp),
        2 * tau * ef * a * (a * c * fp - a * cp - 2 * c * ap),
    ]
)

solution = sp.solve(list(momenta), (ap, cp, fp), dict=True)
assert solution == [{ap: 0, cp: 0, fp: 0}]

R, h = sp.symbols("R h", positive=True, real=True)
D = sp.symbols("D", real=True)  # D = f - n - lambda

# Equações Ea, Ec e restrição no ramo a=c=R, derivadas na Fase 1.
Ea = -2 * tau - tau * h**2 / (2 * R**4) - R**2 * D
Ec = -tau - tau * h**2 / (4 * R**4) - R**2 * D / 2
constraint = 6 * tau - tau * h**2 / (2 * R**4) + R**2 * D

branch = sp.solve((Ea, constraint), (h**2, D), dict=True)
assert branch == [{h**2: 4 * R**4, D: -4 * tau / R**2}]
assert sp.simplify(Ec.subs(branch[0])) == 0

L = sp.symbols("L", positive=True)
photon_density = sp.symbols("rho_gamma", positive=True)
finite_norm = sp.integrate(photon_density, (sp.Symbol("r"), 0, L))
assert finite_norm == L * photon_density
assert sp.limit(finite_norm, L, sp.oo) == sp.oo

print("Condições naturais =>", solution[0])
print("Ramo cilíndrico =>", branch[0])
print("Norma do fóton em comprimento L =>", finite_norm)
print("Limite L -> infinito => infinito")
print("FASE 2: fechamento negativo verificado.")
