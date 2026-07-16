"""Verificações simbólicas da ponte operacional de Heaviside da Q30."""

import sympy as sp

k2, mu, sigma, r = sp.symbols("k2 mu sigma r", positive=True)

phi = 1 / (k2 + mu**2)
V_k = sp.simplify(-8 * sp.pi * sigma * phi / (k2 + mu**2))
assert V_k == -8 * sp.pi * sigma / (k2 + mu**2) ** 2

V_sub = sigma * (1 - sp.exp(-mu * r)) / mu
limite = sp.simplify(sp.limit(V_sub, mu, 0, dir="+"))
assert limite == sigma * r

print("V_mu(k) =", V_k)
print("limite subtraido =", limite)
print("verificacao = True")

