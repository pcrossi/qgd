#!/usr/bin/env python3
"""
GDQ — Chapter 4 / Heat-kernel polarization toy.

Goal:
    Illustrate that a heat-kernel regulator can transform a logarithmic integral
    into a saturated quantity in the ultraviolet. This script does not
    reproduce the complete polarization note; it is only a minimal demonstration.

Theoretical Source:
    manuscript/04_action_consistency/04.7 - What consistency in loops means.md
    manuscript/notes/action/Absence of Landau pole in the effective U(1) sector.md

Classification:
    Heat-kernel illustration. Not a physical prediction.

Equation:
    I(Lambda) = integral_0^Lambda k/(k^2+m^2) exp(-tau k^2) dk

Domain and Boundary:
    1D toy radial integral.

Parameters:
    Universal:
        none
    Apparatus/experiment data:
        none
    Numerical:
        m = 1, tau = 0.25, variable Lambda.

Output:
    output_verify_heat_kernel_polarization_toy.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def integral(Lambda: float, m: float = 1.0, tau: float = 0.25, n: int = 200000) -> float:
    k = np.linspace(0.0, Lambda, n)
    integrand = k / (k * k + m * m) * np.exp(-tau * k * k)
    return float(np.trapezoid(integrand, k))


def integral_unregulated(Lambda: float, m: float = 1.0) -> float:
    return 0.5 * np.log((Lambda * Lambda + m * m) / (m * m))


def main() -> None:
    lambdas = [1, 2, 4, 8, 16, 32]
    rows = []
    for L in lambdas:
        reg = integral(float(L))
        unreg = integral_unregulated(float(L))
        rows.append((L, reg, unreg))
    saturation_delta = abs(rows[-1][1] - rows[-2][1])
    ok = saturation_delta < 1e-5

    lines: list[str] = []
    lines.append("# Output — heat-kernel polarization toy\n\n")
    lines.append("## Classification\n\n")
    lines.append("Heat-kernel illustration. Not a physical prediction.\n\n")
    lines.append("## Toy integral\n\n")
    lines.append("$$\n")
    lines.append("I(\\Lambda)=\\int_0^\\Lambda\\frac{k}{k^2+m^2}e^{-\\tau k^2}\,dk.\n")
    lines.append("$$\n\n")
    lines.append("The comparison without regulator is:\n\n")
    lines.append("$$\n")
    lines.append("I_0(\\Lambda)=\\frac12\\log\\left(\\frac{\\Lambda^2+m^2}{m^2}\\right).\n")
    lines.append("$$\n\n")
    lines.append("## Parameters\n\n")
    lines.append("- $m=1$.\n")
    lines.append("- $\\tau=0.25$.\n\n")
    lines.append("## Results\n\n")
    lines.append("| $\\Lambda$ | regulated | unregulated |\n")
    lines.append("|---:|---:|---:|\n")
    for L, reg, unreg in rows:
        lines.append(f"| {L} | {reg:.12e} | {unreg:.12e} |\n")
    lines.append("\n## Verdict\n\n")
    lines.append("The regulated integral saturates numerically in the UV in this toy model.\n" if ok else "The saturation did not reach the chosen tolerance.\n")
    lines.append("\nThis output does not prove universal finiteness of GDQ. It only illustrates the effect of a heat-kernel factor.\n")

    out = OUT / "output_verify_heat_kernel_polarization_toy.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
