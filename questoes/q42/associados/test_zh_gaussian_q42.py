#!/usr/bin/env python3
"""Demonstra numericamente que a rigidez DtN gaussiana tem ínfimo zero."""

from __future__ import annotations

import argparse

import numpy as np


def trial_energy(radius: float, width: float, tau: float, points: int) -> float:
    r = np.linspace(radius, radius + width, points)
    derivative = -np.ones_like(r) / width
    weight = r**3 * np.exp(-r**2 / (4.0 * tau))
    return 0.5 * float(np.trapezoid(weight * derivative**2, r))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tau", type=float, default=1.0)
    parser.add_argument("--width", type=float, default=1.0)
    args = parser.parse_args()
    radii = np.array([3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]) * np.sqrt(args.tau)
    energies = [trial_energy(r, args.width, args.tau, 4001) for r in radii]
    print("R/sqrt(tau) | energia teste")
    for radius, energy in zip(radii, energies):
        print(f"{radius/np.sqrt(args.tau):12.3f} | {energy:.12e}")
    monotone = all(b < a for a, b in zip(energies, energies[1:]))
    print(f"decaimento monotônico: {monotone}")
    print(f"razão E_final/E_inicial: {energies[-1]/energies[0]:.12e}")


if __name__ == "__main__":
    main()
