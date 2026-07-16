#!/usr/bin/env python3
"""Verifica a seleção r_c=sqrt(6 tau) pela curvatura média ponderada."""

from __future__ import annotations

import argparse
import math


def weighted_mean_curvature(radius: float, tau: float) -> float:
    return -3.0 / radius + radius / (2.0 * tau)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tau", type=float, default=1.0)
    args = parser.parse_args()
    if args.tau <= 0:
        raise ValueError("tau deve ser positivo")
    radius = math.sqrt(6.0 * args.tau)
    k = -3.0 / radius
    normal_f = -radius / (2.0 * args.tau)
    residual = weighted_mean_curvature(radius, args.tau)
    # Derivada positiva prova que a raiz radial é simples.
    derivative = 3.0 / radius**2 + 1.0 / (2.0 * args.tau)
    print(f"tau = {args.tau:.12e}")
    print(f"r_c = {radius:.12e}")
    print(f"K = {k:.12e}")
    print(f"n(F) = {normal_f:.12e}")
    print(f"K_F = {residual:.12e}")
    print(f"dK_F/dr = {derivative:.12e} > 0")


if __name__ == "__main__":
    main()
