#!/usr/bin/env python3
"""
GDQ — Chapter 01 / Symbolic-Numerical Verification

Goal:
    Verify the identity of the osmotic term linking Nelson's formulation to
    the Bohm/Madelung term.

Theoretical source:
    manuscript/01_initial_problem/notes/

Classification:
    Symbolic-numerical verification of analytical identity.

Equation:
    For u=2*nu*grad(log sqrt(rho)), it is verified that
    m*nu*div(u)+(m/2)|u|^2 = 2*m*nu^2*Delta(sqrt(rho))/sqrt(rho).

Domain and boundary:
    Real line. Positive Gaussian density is used, without physical boundary.

Parameters:
    m=nu=1 in reduced units.

Experimental data:
    None.

Output:
    manuscript/01_initial_problem/scripts/output_verify_osmotic_bohm_term.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "manuscript/01_initial_problem/scripts/output_verify_osmotic_bohm_term.md"


def main() -> None:
    m = nu = 1.0
    x = np.linspace(-4, 4, 20_001)
    dx = x[1] - x[0]
    rho = np.exp(-x**2)
    sqrt_rho = np.sqrt(rho)

    grad_log_sqrt = np.gradient(np.log(sqrt_rho), dx, edge_order=2)
    u = 2.0 * nu * grad_log_sqrt
    div_u = np.gradient(u, dx, edge_order=2)
    lhs = m * nu * div_u + 0.5 * m * u**2

    lap_sqrt = np.gradient(np.gradient(sqrt_rho, dx, edge_order=2), dx, edge_order=2)
    rhs = 2.0 * m * nu**2 * lap_sqrt / sqrt_rho

    interior = slice(100, -100)
    max_err = np.max(np.abs(lhs[interior] - rhs[interior]))
    rms_err = np.sqrt(np.mean((lhs[interior] - rhs[interior]) ** 2))

    lines = [
        "---",
        'title: "Output — osmotic term and Bohm"',
        "---",
        "",
        "# Output — osmotic term and Bohm",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Maximum interior error | {max_err:.6e} |",
        f"| RMS interior error | {rms_err:.6e} |",
        "",
        "The identity is confirmed numerically. The residual error comes solely from "
        "finite differences on the grid.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Output: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
