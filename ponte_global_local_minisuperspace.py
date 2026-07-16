#!/usr/bin/env python3
"""Auditoria simbólica do setor cosmológico homogêneo da ponte GDQ.

Classificação: avaliação direta de uma quantidade já derivada.
Não calcula a Hessiana física completa nem usa dados experimentais.
"""

import sympy as sp


x, y, tau = sp.symbols("x y tau", real=True)

# x = log L e y = log R. Constantes aditivas não afetam as variações.
W = 4 * tau * sp.exp(-2 * y) + x + 3 * y
q = sp.Matrix([x, y])
gradient = sp.Matrix([sp.diff(W, qi) for qi in q])
hessian = sp.hessian(W, q)

print("W_hom =", W)
print("grad_(log L, log R) =")
sp.pprint(gradient)
print("Hess_(log L, log R) =")
sp.pprint(hessian)
print("d2 C_L = d2 C_R = 0 para C_L=x-x_cos e C_R=y-y_cos")
print("Conclusao: os multiplicadores lineares removem os modulos, mas nao")
print("geram limiar positivo para perturbacoes locais inhomogeneas.")
