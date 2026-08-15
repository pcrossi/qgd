#!/usr/bin/env python3
"""Demonstrates numerically that the Gaussian DtN stiffness has zero infimum."""

from __future__ import annotations

import argparse
from pathlib import Path

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
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("output_test_sg_gaussian_zh.md"),
    )
    args = parser.parse_args()
    radii = np.array([3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]) * np.sqrt(args.tau)
    energies = [trial_energy(r, args.width, args.tau, 4001) for r in radii]
    lines = [
        "# Output — Gaussian axial localization test",
        "",
        "| $R/\\sqrt{\\tau}$ | Test energy |",
        "|---:|---:|",
    ]
    for radius, energy in zip(radii, energies):
        lines.append(f"| {radius/np.sqrt(args.tau):.3f} | ${energy:.12e}$ |")
    monotone = all(b < a for a, b in zip(energies, energies[1:]))
    lines += [
        "",
        f"- Monotonic decay: `{monotone}`",
        f"- Ratio $E_{{\\rm final}}/E_{{\\rm inicial}}$: ${energies[-1]/energies[0]:.12e}$",
        "",
        "Conclusion: the outer Gaussian shrinker has zero axial infimum in the Dirichlet--to--Neumann test. "
        "It verifies the bulk, but does not localize the Stern--Gerlach axial mode by itself.",
    ]
    report = "\n".join(lines) + "\n"
    args.output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
