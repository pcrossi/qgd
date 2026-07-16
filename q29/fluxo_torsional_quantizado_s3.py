#!/usr/bin/env python3
"""Extremos radiais do funcional Perelman-Bismut em S3 com fluxo inteiro."""

from __future__ import annotations

import argparse
import numpy as np


def stationary_roots(tau: float, flux: int) -> list[float]:
    # x=R^2: x^3 - 4 tau x^2 + tau n^2/pi^2 = 0.
    roots = np.roots([1.0, -4.0 * tau, 0.0, tau * flux**2 / np.pi**2])
    return sorted(float(root.real) for root in roots if abs(root.imag) < 1e-10 and root.real > 0)


def functional(radius: float, tau: float, flux: int) -> float:
    return (
        6.0 * tau / radius**2
        - tau * flux**2 / (2.0 * np.pi**2 * radius**6)
        + 3.0 * np.log(radius)
    )


def second(radius: float, tau: float, flux: int) -> float:
    return (
        36.0 * tau / radius**4
        - 21.0 * tau * flux**2 / (np.pi**2 * radius**8)
        - 3.0 / radius**2
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tau", type=float, default=1.0)
    parser.add_argument("--flux", type=int, default=1)
    args = parser.parse_args()
    if args.tau <= 0 or args.flux == 0:
        raise ValueError("tau>0 e fluxo inteiro não nulo")

    print("Q29 — FLUXO TORSIONAL QUANTIZADO EM S3")
    for x in stationary_roots(args.tau, args.flux):
        radius = np.sqrt(x)
        curvature = second(radius, args.tau, args.flux)
        nature = "mínimo" if curvature > 0 else "máximo"
        print(
            f"R²={x:.12f} R={radius:.12f} "
            f"W={functional(radius,args.tau,args.flux):.12f} "
            f"W''={curvature:.12f} {nature}"
        )

    roots = stationary_roots(args.tau, args.flux)
    assert len(roots) == 2
    assert second(np.sqrt(roots[0]), args.tau, args.flux) < 0
    assert second(np.sqrt(roots[1]), args.tau, args.flux) > 0


if __name__ == "__main__":
    main()
