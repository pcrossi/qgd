"""Refinamento do DtN exterior de referência por harmônicos.

Classificação: avaliação analítica/teste de convergência de um operador de
referência. Não é o gap físico da GDQ enquanto o potencial matricial do
background global não for calculado.
"""

import numpy as np


def kappa(ell, radius, mu):
    return np.sqrt(mu**2 + ell * (ell + 2.0) / radius**2)


def lambda_effective(ell, radius, mu, length=None):
    if length is None:
        length = np.pi * radius
    kap = kappa(ell, radius, mu)
    if kap == 0.0:
        return 0.0
    return kap * np.tanh(kap * length)


def spectrum(radius, mu, ell_max):
    # ell=0 é removido quando mu=0 por normalização/Noether.
    start = 1 if mu == 0.0 else 0
    values = np.array(
        [lambda_effective(ell, radius, mu) for ell in range(start, ell_max + 1)]
    )
    return values


def refinement():
    radii = [1.0, 10.0, 100.0, 1000.0]
    cutoffs = [4, 8, 16, 32, 64]
    masses = [0.0, 0.1, 1.0]
    for mu in masses:
        print(f"\nmu={mu:g}")
        print("R        ell_max       gap_ref            tail_last")
        for radius in radii:
            for cutoff in cutoffs:
                values = spectrum(radius, mu, cutoff)
                print(
                    f"{radius:8.1f} {cutoff:8d} "
                    f"{np.min(values):16.9e} {values[-1]:16.9e}"
                )
            print()


if __name__ == "__main__":
    refinement()
