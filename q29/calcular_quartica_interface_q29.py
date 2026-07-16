#!/usr/bin/env python3
"""Combina retroação l=1 e rigidez superficial torsional da Q40."""

from __future__ import annotations

import math


def main() -> None:
    alpha = 1.0 / 137.03599907
    radius = 1.998411184770
    a2_bulk = -0.2531966759616
    a4_bulk = -0.8057552880937

    b0 = 1.0 / (math.pi * radius**3)
    surface_rigidity = alpha * (3.0 * math.pi / 2.0 + 3.0 / (4.0 * math.pi**3))
    area_quartic = 5.0 / 128.0
    # V_surface = S * (5/128) * (beta/b0)^4 = (a4/4) beta^4.
    a4_interface = 4.0 * surface_rigidity * area_quartic / b0**4
    a4_total = a4_bulk + a4_interface
    beta_vacuum = math.sqrt(-a2_bulk / a4_total)
    epsilon_vacuum = beta_vacuum / b0

    proton_mass = 0.93827208816
    kahler_volume = 6.0 * math.pi**5
    v_geometry = proton_mass * kahler_volume / 7.0
    field_normalization = v_geometry / beta_vacuum

    print("Q29 — QUÁRTICA DE INTERFACE")
    print(f"alpha = {alpha:.12e}")
    print(f"R = {radius:.12f}")
    print(f"b0 = {b0:.12e}")
    print(f"S_boundary = {surface_rigidity:.12e}")
    print(f"a4_bulk = {a4_bulk:.12e}")
    print(f"a4_interface = {a4_interface:.12e}")
    print(f"a4_total = {a4_total:.12e}")
    print(f"beta_vac = {beta_vacuum:.12e}")
    print(f"epsilon_vac = beta/b0 = {epsilon_vacuum:.12e}")
    print(f"v_geom = {v_geometry:.12f} GeV")
    print(f"Z_beta^(1/2) = v/beta = {field_normalization:.12f} GeV")

    assert a2_bulk < 0.0
    assert a4_interface > abs(a4_bulk)
    assert a4_total > 0.0
    assert beta_vacuum > 0.0


if __name__ == "__main__":
    main()
