#!/usr/bin/env python3
"""Calcula as normas espectrais e os acoplamentos geométricos da Q28."""

from __future__ import annotations

import math


def main() -> None:
    alpha = 1.0 / 137.03599907
    e = math.sqrt(4.0 * math.pi * alpha)

    # Índices quadráticos de uma geração quiral.
    # T(fundamental SU(N)) = 1/2.
    index_su3 = 2.0 * 0.5 + 0.5 + 0.5  # Q_L (dupleto), u^c, d^c
    index_su2 = 3.0 * 0.5 + 0.5        # três cores de Q_L e L_L
    norm_y = (
        6.0 * (1.0 / 6.0) ** 2
        + 3.0 * (-2.0 / 3.0) ** 2
        + 3.0 * (1.0 / 3.0) ** 2
        + 2.0 * (-1.0 / 2.0) ** 2
        + 1.0**2
    )

    ratio_gp2_g2 = index_su2 / norm_y
    sin2_theta = ratio_gp2_g2 / (1.0 + ratio_gp2_g2)
    g = e / math.sqrt(sin2_theta)
    gp = e / math.sqrt(1.0 - sin2_theta)
    gs_matching = g * math.sqrt(index_su2 / index_su3)

    # Resultado hadrônico independente já derivado na Q30.
    alpha_s_hadronic = 3.0 / (8.0 * math.pi)
    gs_hadronic = math.sqrt(4.0 * math.pi * alpha_s_hadronic)

    print("Q28 — ACOPLAMENTOS POR NORMAS DO FIBRADO")
    print(f"I_SU3 = {index_su3:.12f}")
    print(f"I_SU2 = {index_su2:.12f}")
    print(f"||Y||^2 = {norm_y:.12f}")
    print(f"g'^2/g^2 = {ratio_gp2_g2:.12f}")
    print(f"sin^2(theta_W) = {sin2_theta:.12f}")
    print(f"alpha = {alpha:.12f}")
    print(f"e = {e:.12f}")
    print(f"g_s (matching) = {gs_matching:.12f}")
    print(f"g = {g:.12f}")
    print(f"g' = {gp:.12f}")
    print(f"alpha_s hadrônica Q30 = {alpha_s_hadronic:.12f}")
    print(f"g_s hadrônico Q30 = {gs_hadronic:.12f}")

    assert math.isclose(index_su3, 2.0)
    assert math.isclose(index_su2, 2.0)
    assert math.isclose(norm_y, 10.0 / 3.0)
    assert math.isclose(ratio_gp2_g2, 3.0 / 5.0)
    assert math.isclose(sin2_theta, 3.0 / 8.0)
    assert math.isclose(gs_matching, g)
    assert math.isclose(gs_hadronic, math.sqrt(1.5))


if __name__ == "__main__":
    main()
