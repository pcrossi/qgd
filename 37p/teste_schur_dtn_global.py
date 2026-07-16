#!/usr/bin/env python3
"""Teste diagnóstico da rota DtN/Schur para a normalização global de alpha."""

from math import pi
import numpy as np


K_BASE = 41.594825709
DELTA_B = -0.2709378871
R = 1.998411184770


def main() -> None:
    alpha_cos = 9.0 / (8.0 * pi**4) * (pi**5 / 1920.0) ** 0.25
    z_cos = 1.0 / (4.0 * pi * alpha_cos)

    # Kernel fotônico (1,1) da matriz neutra radial já calculada.
    k0 = K_BASE / 2.0 * (1.0 + DELTA_B)

    # DtN do primeiro harmônico em uma 4-bola: lambda_DtN=l/R, l=1.
    # Cada lado contribui lambda_DtN*Area(S3_R)*<|T|²>, com <|T|²>=1/4.
    # Dois lados dão K_boundary=pi² R².
    k_boundary = pi**2 * R**2
    k_eff = k0 * k_boundary / (k0 + k_boundary)

    # Valor de K_boundary que seria exigido pela fórmula cosmológica.
    s_required = k0 / z_cos - 1.0
    k_boundary_required = k0 / s_required

    hessian = np.array(
        [[k0 + k_boundary, -k_boundary], [-k_boundary, k_boundary]],
        dtype=float,
    )

    print("Q37 — TESTE SCHUR/DTN GLOBAL SEM AJUSTE")
    print(f"K0 fotônico radial           = {k0:.12f}")
    print(f"K_boundary DtN geométrico    = {k_boundary:.12f}")
    print(f"K_eff previsto               = {k_eff:.12f}")
    print(f"alpha_DtN^(-1)               = {4*pi*k_eff:.12f}")
    print(f"Z cosmológico requerido      = {z_cos:.12f}")
    print(f"alpha_cos^(-1)               = {1/alpha_cos:.12f}")
    print(f"erro relativo em Z           = {(k_eff/z_cos-1)*100:.6f}%")
    print()
    print(f"K_boundary requerido         = {k_boundary_required:.12f}")
    print(f"desvio DtN/requerido         = {(k_boundary/k_boundary_required-1)*100:.6f}%")
    print(f"autovalores Hessiana         = {np.linalg.eigvalsh(hessian)}")

    assert np.all(np.linalg.eigvalsh(hessian) > 0.0)


if __name__ == "__main__":
    main()
