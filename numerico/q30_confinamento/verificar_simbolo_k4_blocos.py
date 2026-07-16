#!/usr/bin/env python3
"""Verifica a ordem do inverso de um símbolo Hessiano 2x2."""

import sympy as sp

x = sp.symbols("x", positive=True)  # x=k^2
a, b, c = sp.symbols("a b c", nonzero=True)
aa, bb, cc = sp.symbols("aa bb cc")

m2 = sp.Matrix([[a, b], [b, c]])
m4 = sp.Matrix([[aa, bb], [bb, cc]])
hessian = x * m2 + x**2 * m4
determinant = sp.factor(hessian.det())
leading = sp.factor(sp.limit(determinant / x**2, x, 0))

print("det_H=", determinant)
print("leading_det_coefficient=", leading)
print("generic_inverse_order=k^-2 when a*c-b^2 != 0")
print("k^-4 requires a*c-b^2=0 plus positive fourth-order projection")

if leading != a * c - b**2:
    raise SystemExit("Falha na ordem principal do determinante.")

tau = sp.symbols("tau", positive=True)
g = sp.exp(-tau * x) / x
print("heat_kernel_IR=", sp.series(g, x, 0, 3))
