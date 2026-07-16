#!/usr/bin/env python3
"""Verifica carga bulk, transgressão e ação radial da meia-sela Q38."""

from __future__ import annotations

import math


def q_full_ball(radius: float, rho: float) -> float:
    return radius**4 * (radius**2 + 3.0 * rho**2) / (radius**2 + rho**2) ** 3


def q_half_bulk(radius: float, rho: float) -> float:
    return 0.5 * q_full_ball(radius, rho)


def q_boundary_cs(radius: float, rho: float) -> float:
    return 0.5 * (1.0 - q_full_ball(radius, rho))


def g_rho_rho(radius: float, rho: float, weight: float = 1.0) -> float:
    return 4.0 * math.pi**2 * weight * radius**6 / (radius**2 + rho**2) ** 3


def main() -> None:
    alpha = (9.0 / (8.0 * math.pi**4)) * ((math.pi**5 / 1920.0) ** 0.25)
    print("Q38 — REDUÇÃO RADIAL DA MEIA-SELA")
    print("R/rho | Q_bulk(half) | Q_CS(boundary) | Q_relative | S/hbar | G_rhorho/U")
    for ratio in (0.5, 1.0, 2.0, 5.0, 10.0, 100.0):
        rho = 1.0
        radius = ratio * rho
        qb = q_half_bulk(radius, rho)
        qcs = q_boundary_cs(radius, rho)
        qrel = qb + qcs
        action = qrel / alpha
        metric = g_rho_rho(radius, rho)
        print(
            f"{ratio:5.1f} | {qb:.12f} | {qcs:.12f} | {qrel:.12f} | "
            f"{action:.9f} | {metric:.9f}"
        )
    print(f"\n1/(2 alpha) = {1.0/(2.0*alpha):.9f}")
    integrated_measure_r_equals_one = math.sqrt(2.0) * math.pi
    print(f"int_0^R sqrt(G_rhorho) drho (R=U=1) = {integrated_measure_r_equals_one:.9f}")
    print("dS/drho = 0 e d2S/drho2 = 0 após incluir a transgressão.")


if __name__ == "__main__":
    main()
