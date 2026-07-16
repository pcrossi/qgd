#!/usr/bin/env python3
"""Verifica a Hessiana homogênea do raio do shrinker cilíndrico GDQ."""

from __future__ import annotations

import argparse
import math


def w_homogeneous(radius: float, tau: float) -> float:
    return (
        6.0 * tau / radius**2
        + 3.0 * math.log(radius / (2.0 * math.sqrt(tau)))
        + 0.5 * math.log(math.pi)
        - 3.0
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tau", type=float, default=1.0)
    args = parser.parse_args()
    tau = args.tau
    radius = 2.0 * math.sqrt(tau)
    derivative = -12.0 * tau / radius**3 + 3.0 / radius
    hessian = 36.0 * tau / radius**4 - 3.0 / radius**2
    step = 1e-4 * radius
    finite_hessian = (
        w_homogeneous(radius + step, tau)
        - 2.0 * w_homogeneous(radius, tau)
        + w_homogeneous(radius - step, tau)
    ) / step**2
    print(f"a_star = {radius:.12e}")
    print(f"W(a_star) = {w_homogeneous(radius, tau):.12e}")
    print(f"W'(a_star) = {derivative:.12e}")
    print(f"W'' analítica = {hessian:.12e}")
    print(f"W'' diferença finita = {finite_hessian:.12e}")
    print(f"modo homogêneo estável: {hessian > 0}")


if __name__ == "__main__":
    main()
