#!/usr/bin/env python3
"""
QGD — Chapter 5 / Fisher-Bohm variation in 1D.

Objective:
    Numerically verify that the variational derivative of the Fisher energy
    E = integral (rho_x^2/rho) dx is proportional to the operator
    -4 sqrt(rho)''/sqrt(rho), in the interior of the grid.

Theoretical source:
    manuscript/05_equations_conservation/05.4 - Density variation and dynamic equilibrium.md
    manuscript/notes/equations/From amplitude energy to the Bohm term.md

Classification:
    Numerical/symbolic variation test. Not a physical prediction.

Equation:
    delta/delta rho integral rho_x^2/rho dx
    = -4 (sqrt(rho))''/sqrt(rho)

Domain and boundary:
    Periodic 1D interval [0, 2pi].

Parameters:
    Universal:
        none
    Apparatus/experimental data:
        none
    Numerical:
        periodic grid.

Output:
    output_verify_bohm_fisher_variation.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def ddx_periodic(f: np.ndarray, dx: float) -> np.ndarray:
    return (np.roll(f, -1) - np.roll(f, 1)) / (2.0 * dx)


def d2dx2_periodic(f: np.ndarray, dx: float) -> np.ndarray:
    return (np.roll(f, -1) - 2.0 * f + np.roll(f, 1)) / (dx * dx)


def fisher_variational(rho: np.ndarray, dx: float) -> np.ndarray:
    rho_x = ddx_periodic(rho, dx)
    rho_xx = d2dx2_periodic(rho, dx)
    return -2.0 * rho_xx / rho + (rho_x * rho_x) / (rho * rho)


def bohm_operator_form(rho: np.ndarray, dx: float) -> np.ndarray:
    root = np.sqrt(rho)
    root_xx = d2dx2_periodic(root, dx)
    return -4.0 * root_xx / root


def main() -> None:
    rows = []
    for n in [200, 400, 800, 1600]:
        x = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
        dx = x[1] - x[0]
        rho = 1.5 + 0.2 * np.cos(x) + 0.1 * np.sin(2.0 * x)
        lhs = fisher_variational(rho, dx)
        rhs = bohm_operator_form(rho, dx)
        err = float(np.max(np.abs(lhs - rhs)))
        scale = float(np.max(np.abs(rhs)))
        rel = err / scale
        rows.append((n, err, rel))
    ok = rows[-1][2] < 1e-4

    lines: list[str] = []
    lines.append("# Output — Fisher-Bohm variation\n\n")
    lines.append("## Classification\n\n")
    lines.append("Numerical/symbolic variation test. Not a physical prediction.\n\n")
    lines.append("## Verified identity\n\n")
    lines.append("$$\n")
    lines.append("\\frac{\\delta}{\\delta\\rho}\\int\\frac{|\\nabla\\rho|^2}{\\rho}\\,dx\n")
    lines.append("=-4\\frac{\\Delta\\sqrt\\rho}{\\sqrt\\rho}.\n")
    lines.append("$$\n\n")
    lines.append("## Periodic grid results\n\n")
    lines.append("| N | maximum error | relative error |\n")
    lines.append("|---:|---:|---:|\n")
    for n, err, rel in rows:
        lines.append(f"| {n} | {err:.12e} | {rel:.12e} |\n")
    lines.append("\n## Verdict\n\n")
    lines.append("The check passed at the refinement used.\n" if ok else "The check failed at the chosen tolerance.\n")
    lines.append("\nThis output verifies the differential identity in 1D periodic; the general QGD form uses $\\Delta_g$ and its own domain/boundary.\n")

    out = OUT / "output_verify_bohm_fisher_variation.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
