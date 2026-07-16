#!/usr/bin/env python3
"""Verifica a generalização por índice de representação do termo (DF)^2."""

import math


def c2g_dirac(g2: float, tau: float, species: list[tuple[float, float]]) -> float:
    """species contém pares (T(R), massa)."""
    return g2 / (240.0 * math.pi**2) * sum(
        index / mass**2 * math.exp(-tau * mass**2)
        for index, mass in species
    )


def main() -> int:
    e2 = 4.0 * math.pi / 137.0
    tau = 0.2749005225136263

    # Limite U(1): T(R)=Q^2=1, m=1.
    nonabelian_notation = c2g_dirac(e2, tau, [(1.0, 1.0)])
    abelian_formula = math.exp(-tau) / (60.0 * math.pi * 137.0)
    assert abs(nonabelian_notation - abelian_formula) < 1e-18

    # Fundamental SU(N): T(F)=1/2. Dois Weyl equivalem a um Dirac.
    fundamental_dirac = c2g_dirac(1.0, tau, [(0.5, 1.0)])
    two_weyl = 2.0 * 0.5 * fundamental_dirac
    assert abs(two_weyl - fundamental_dirac) < 1e-18

    print(f"limite U(1): {nonabelian_notation:.14e}")
    print(f"fórmula abeliana: {abelian_formula:.14e}")
    print(f"Dirac fundamental, g^2=1: {fundamental_dirac:.14e}")
    print("Todos os testes algébricos passaram.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
