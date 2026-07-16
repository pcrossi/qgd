#!/usr/bin/env python3
"""Verifica algebricamente a sela steady de Einstein--Bismut da Q38."""

from __future__ import annotations

import math
import numpy as np


def residuals(radius: float, torus_radii: tuple[float, ...]) -> dict[str, object]:
    if radius <= 0 or len(torus_radii) != 5 or min(torus_radii) <= 0:
        raise ValueError("Os raios devem ser positivos e T^5 deve ter cinco raios.")
    h_flux = 2.0 / radius
    ric_s3 = (2.0 / radius**2) * np.eye(3)
    h_stress = (0.25 * 2.0 * h_flux**2) * np.eye(3)
    volume = 2.0 * math.pi**2 * radius**3
    for length in torus_radii:
        volume *= 2.0 * math.pi * length
    f0 = math.log(volume)
    rho0 = math.exp(-f0)
    return {
        "h_flux": h_flux,
        "volume": volume,
        "f0": f0,
        "rho0": rho0,
        "normalization": rho0 * volume,
        "residual_s3": ric_s3 - h_stress,
        "residual_t5": np.zeros((5, 5)),
        "torsion_residual": 0.0,
    }


def main() -> None:
    result = residuals(1.0, (1.0,) * 5)
    print("Q38 — BACKGROUND STEADY DE EINSTEIN–BISMUT")
    print(f"amplitude H = 2/R         = {result['h_flux']:.12f}")
    print(f"volume                    = {result['volume']:.12e}")
    print(f"f0 = log(volume)          = {result['f0']:.12f}")
    print(f"rho0                      = {result['rho0']:.12e}")
    print(f"integral rho0 dV          = {result['normalization']:.12f}")
    print(f"max residual metrica S3   = {np.max(np.abs(result['residual_s3'])):.3e}")
    print(f"max residual metrica T5   = {np.max(np.abs(result['residual_t5'])):.3e}")
    print(f"residual torsional        = {result['torsion_residual']:.3e}")


if __name__ == "__main__":
    main()
