"""Verifica o resíduo de um integrando de Laurent GDQ em dimensão real 8."""

import sympy as sp

z = sp.symbols("z")
A0, A1, A2, A3, A4 = sp.symbols("A0 A1 A2 A3 A4")

serie = (A0 + A1*z + A2*z**2 + A3*z**3 + A4*z**4) / (4*sp.pi*z)**4
residuo = sp.simplify(sp.residue(serie, z, 0))
esperado = A3 / (4*sp.pi)**4

print("residuo =", residuo)
print("esperado =", esperado)
print("verificacao =", sp.simplify(residuo - esperado) == 0)
print("observacao = A3 so coincide com a6 se o numerador for um heat trace")
