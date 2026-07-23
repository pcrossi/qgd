#!/usr/bin/env python3
"""Compara Hessiana KKT de Noether e Hessiana reduzida no Berger."""

import numpy as np
import sympy as sp


def main():
    r, q, torsion, multiplier = sp.symbols("r q torsion multiplier", positive=True)
    charge = 1 / sp.pi
    geometric = 2*(4-q**2)/r**2 + 3*sp.log(r) + sp.log(q)
    constraint = r**3*q*torsion - charge
    lagrangian = geometric - torsion**2/2 + multiplier*constraint
    hessian = sp.hessian(lagrangian, (r, q, torsion))
    tangent = sp.Matrix([[1, 0], [0, 1], [-3*torsion/r, -torsion/q]])
    projected = sp.simplify(tangent.T*hessian*tangent)
    reduced = geometric - 1/(2*sp.pi**2*r**6*q**2)
    reduced_hessian = sp.hessian(reduced, (r, q))

    substitutions = {
        torsion: charge/(r**3*q),
        multiplier: charge/(r**6*q**2),
    }
    difference = sp.simplify((projected-reduced_hessian).subs(substitutions))
    radius = 1.998411184770
    numeric = np.array(reduced_hessian.subs({r: radius, q: 1}).evalf(), float)
    print("Q29 — NOETHER NO BERGER")
    print("H_KKT projetada - H_reduzida =")
    print(difference)
    print("H física no ramo grande =")
    print(numeric)
    print("spec(H física) =", np.linalg.eigvalsh(numeric))
    assert difference == sp.zeros(2)
    assert np.linalg.eigvalsh(numeric)[0] < 0


if __name__ == "__main__":
    main()
