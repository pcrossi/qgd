#!/usr/bin/env python3
"""Separa a curvatura radial da rigidez Robin de calibre na Q29."""

from math import pi, sqrt

A2 = -0.2531966759616
A4 = 2133.554507
Z_OVER_C = 0.332803938618
PROTON_MASS_GEV = 0.93827208816

if __name__ == "__main__":
    beta2 = -A2 / A4
    beta = sqrt(beta2)
    radial_curvature = -2.0 * A2
    robin_over_c = Z_OVER_C * beta2
    v = PROTON_MASS_GEV * (6.0 * pi**5) / 7.0
    print("Q29 — RIGIDEZ RADIAL E RIGIDEZ ROBIN")
    print(f"beta_*²                   = {beta2:.12e}")
    print(f"beta_*                    = {beta:.12e}")
    print(f"V''(beta_*)               = {radial_curvature:.12e}")
    print(f"kappa_partial/C_GDQ       = {robin_over_c:.12e}")
    print(f"kappa_partial físico=v²   = {v**2:.12e} GeV²")
    assert abs(beta - 0.010893743) < 1e-8
    assert radial_curvature > 0 and robin_over_c > 0
