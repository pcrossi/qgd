#!/usr/bin/env python3
"""Complemento de Schur da colagem eletromagnética em série."""

from math import pi
import numpy as np

ALPHA_INV = 137.03599907
alpha = 1/ALPHA_INV
surface = alpha*(3*pi/2+3/(4*pi**3))
K0 = 1.0
Kb = K0/surface

# S(x,A)=K0*x²/2 + Kb*(A-x)²/2.
Hxx = K0+Kb
J = -Kb
KAA = Kb
Keff = KAA-J*J/Hxx

if __name__ == "__main__":
    expected = K0/(1+surface)
    print("Q29 — SCHUR ELETROMAGNÉTICO DA INTERFACE")
    print(f"S_boundary      = {surface:.12f}")
    print(f"K_boundary/K0   = {Kb/K0:.12f}")
    print(f"K_eff/K0        = {Keff/K0:.12f}")
    print(f"1/(1+S)         = {expected:.12f}")
    print(f"alpha_eff^-1    = {ALPHA_INV*Keff/K0:.12f}")
    hessian = np.array([[Hxx, J], [J, KAA]])
    print("spec Hessiana   =", np.linalg.eigvalsh(hessian))
    assert abs(Keff-expected) < 1e-14
    assert np.all(np.linalg.eigvalsh(hessian) > 0)
