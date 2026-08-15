#!/usr/bin/env python3
"""
GDQ — Chapter 4 / Variation of the constitutive measure.

Goal:
    Verify numerically, in small perturbations, the identity
    delta U / U = -delta(f + fbar)/2 for fixed metric and fixed z_tau.

Theoretical Source:
    manuscript/04_action_consistency/04.3 - Fields, measure and structural data.md
    manuscript/notes/action/First variation of the GDQ action - complete structure.md

Classification:
    Symbolic test of constitutive identity. Not a physical prediction.

Equation:
    U = exp(-(f+fbar)/2)/(4*pi*z_tau)^n

Domain and Boundary:
    Pointwise check; no differential operator.

Parameters:
    Universal:
        n = 4
    Apparatus/experiment data:
        none
    Numerical:
        small perturbations eps.

Output:
    output_verify_measure_variation.md
"""

from __future__ import annotations

from pathlib import Path
import math


OUT = Path(__file__).resolve().parent


def measure(real_f_sum: float, z_tau: float = 1.0, n: int = 4) -> float:
    return math.exp(-real_f_sum / 2.0) / ((4.0 * math.pi * z_tau) ** n)


def main() -> None:
    f_sum = 0.7
    u0 = measure(f_sum)
    rows = []
    for eps in [1e-2, 1e-4, 1e-6, 1e-8]:
        u1 = measure(f_sum + eps)
        finite_ratio = (u1 - u0) / u0
        linear_prediction = -eps / 2.0
        error = abs(finite_ratio - linear_prediction)
        rows.append((eps, finite_ratio, linear_prediction, error))
    ok = rows[-1][-1] < 1e-12

    lines: list[str] = []
    lines.append("# Output — variation of the constitutive measure\n\n")
    lines.append("## Classification\n\n")
    lines.append("Symbolic test of constitutive identity. Not a physical prediction.\n\n")
    lines.append("## Linearized identity\n\n")
    lines.append("For fixed metric and fixed $z_\\tau$:\n\n")
    lines.append("$$\n")
    lines.append("\\frac{\\delta\\mathcal U}{\\mathcal U}\n")
    lines.append("=-\\frac12\\delta(f+\\bar f).\n")
    lines.append("$$\n\n")
    lines.append("## Finite difference test\n\n")
    lines.append("| $\\epsilon$ | exact relative variation | linear prediction | error |\n")
    lines.append("|---:|---:|---:|---:|\n")
    for eps, finite_ratio, linear_prediction, error in rows:
        lines.append(
            f"| {eps:.0e} | {finite_ratio:.16e} | "
            f"{linear_prediction:.16e} | {error:.3e} |\n"
        )
    lines.append("\n## Verdict\n\n")
    lines.append("The check passed in the linear limit.\n" if ok else "The check failed.\n")
    lines.append("\nThis output only verifies the constitutive variation of the measure, not the equations of motion.\n")

    out = OUT / "output_verify_measure_variation.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
