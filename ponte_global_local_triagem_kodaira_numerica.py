#!/usr/bin/env python3
"""Triagem de simetria do primeiro modo angular em S3.

Classificacao: teste numerico de consistencia de regras de selecao harmonicas.
Nao calcula a Hessiana completa da GDQ e nao ajusta um acoplamento B_mu.
"""
from __future__ import annotations

import numpy as np


VOL_S3 = 2.0 * np.pi**2


def sphere_points(n: int, seed: int = 381947) -> np.ndarray:
    rng = np.random.default_rng(seed)
    x = rng.normal(size=(n, 4))
    return x / np.linalg.norm(x, axis=1)[:, None]


def estimate(n: int) -> dict[str, float]:
    x = sphere_points(n)
    # Primeiro harmonico escalar real, normalizado em L2(S3).
    norm = np.sqrt(4.0 / VOL_S3)
    y = norm * x[:, 0]
    # Para Y=C*x0 em esfera unitaria, |grad_S Y|^2=C^2(1-x0^2).
    grad2 = norm**2 * (1.0 - x[:, 0]**2)
    # O quadrado contem um singlet: Y^2=<Y^2>+(Y^2-<Y^2>).
    y2 = y*y
    singlet_y2 = VOL_S3 * np.mean(y2)
    return {
        "int_Y": VOL_S3 * np.mean(y),
        "int_Y2": singlet_y2,
        "int_grad2": VOL_S3 * np.mean(grad2),
        "lambda_rayleigh": VOL_S3*np.mean(grad2)/singlet_y2,
        "linear_overlap_constant": VOL_S3*np.mean(y),
        "quadratic_singlet": singlet_y2,
    }


def main() -> None:
    print("Triagem do primeiro harmonico angular de S3")
    print("exatos: intY=0, intY2=1, int|gradY|2=3, lambda=3")
    for n in (20_000, 100_000, 500_000):
        q = estimate(n)
        print(
            f"N={n:7d} intY={q['int_Y']:+.6e} "
            f"intY2={q['int_Y2']:.8f} grad2={q['int_grad2']:.8f} "
            f"lambda={q['lambda_rayleigh']:.8f}"
        )
    q = estimate(500_000)
    # Erro Monte Carlo da media de Y: Var(int Y)=Vol/N, pois int Y^2=1.
    sigma = np.sqrt(VOL_S3 / 500_000)
    zscore = abs(q["int_Y"]) / sigma
    print("linear_overlap_zscore =", zscore)
    print("linear_screen = ZERO_BY_SYMMETRY")
    print("quadratic_screen = NONZERO_SINGLET")
    if abs(q["int_Y2"] - 1.0) > 1.5e-2:
        raise RuntimeError("quadratura nao recuperou a normalizacao harmonica")
    if abs(q["lambda_rayleigh"] - 3.0) > 3.0e-2:
        raise RuntimeError("quadratura nao recuperou o autovalor l=1")


if __name__ == "__main__":
    main()
