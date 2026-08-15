#!/usr/bin/env python3
"""
QGD — Chapter 5 / Toy canonical polarization via Routh-Schwarz.

Objective:
    Illustrate that, for positive rho, fixed charge Q, and fixed normalization N_rho,
    the functional H[Pi,rho] = integral Pi^2/(2 A rho) is minimized by
    Pi = (Q/N_rho) rho.

Theoretical source:
    manuscript/05_equations_conservation/05.7 - What was demonstrated and what depends on physical reconstruction.md
    manuscript/notes/equations/Audit of the canonical term rho d_t S_R.md

Classification:
    Routh/Cauchy–Schwarz illustration. Not a physical prediction.

Equation:
    H >= Q^2/(2 A N_rho), equality when Pi = (Q/N_rho) rho.

Domain and boundary:
    1D interval with trapezoidal quadrature.

Parameters:
    Universal:
        none
    Apparatus/experimental data:
        none
    Numerical:
        arbitrary positive profiles.

Output:
    output_verify_canonical_polarization_toy.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def integrate(y: np.ndarray, x: np.ndarray) -> float:
    return float(np.trapezoid(y, x))


def main() -> None:
    x = np.linspace(0.0, 1.0, 5001)
    rho_raw = 1.2 + 0.4 * np.cos(2 * np.pi * x) + 0.2 * np.sin(6 * np.pi * x)
    rho = rho_raw / integrate(rho_raw, x)
    n_rho = integrate(rho, x)
    q = 1.0
    a = 2.0
    pi_min = (q / n_rho) * rho
    h_min_numeric = integrate(pi_min * pi_min / (2.0 * a * rho), x)
    h_min_bound = q * q / (2.0 * a * n_rho)
    rows = []
    for amp in [0.0, 0.1, 0.5, 1.0]:
        fluct = np.sin(2 * np.pi * x) - integrate(np.sin(2 * np.pi * x), x) * rho
        # Adjusts the fluctuation to have zero charge.
        fluct = fluct - integrate(fluct, x) * rho / n_rho
        pi = pi_min + amp * fluct
        charge = integrate(pi, x)
        h = integrate(pi * pi / (2.0 * a * rho), x)
        rows.append((amp, charge, h, h - h_min_bound))
    ok = abs(h_min_numeric - h_min_bound) < 1e-10 and all(row[3] >= -1e-10 for row in rows)

    lines: list[str] = []
    lines.append("# Output — canonical polarization toy\n\n")
    lines.append("## Classification\n\n")
    lines.append("Routh/Cauchy–Schwarz illustration. Not a physical prediction.\n\n")
    lines.append("## Inequality\n\n")
    lines.append("$$\n")
    lines.append("H[\\Pi,\\rho]=\\int\\frac{\\Pi^2}{2A\\rho}\\,d\\Sigma\n")
    lines.append("\\geq\n")
    lines.append("\\frac{Q^2}{2AN_\\rho}.\n")
    lines.append("$$\n\n")
    lines.append("Equality occurs for:\n\n")
    lines.append("$$\n")
    lines.append("\\Pi=\\frac{Q}{N_\\rho}\\rho.\n")
    lines.append("$$\n\n")
    lines.append("## Toy parameters\n\n")
    lines.append(f"- $A={a}$.\n")
    lines.append(f"- $Q={q}$.\n")
    lines.append(f"- $N_\\rho={n_rho:.12g}$.\n")
    lines.append(f"- Lower bound: `{h_min_bound:.12e}`.\n\n")
    lines.append("## Zero-charge perturbations around the minimizer\n\n")
    lines.append("| amplitude | charge | $H$ | excess $H-H_{min}$ |\n")
    lines.append("|---:|---:|---:|---:|\n")
    for amp, charge, h, excess in rows:
        lines.append(f"| {amp:.6g} | {charge:.12e} | {h:.12e} | {excess:.12e} |\n")
    lines.append("\n## Verdict\n\n")
    lines.append("The check passed.\n" if ok else "The check failed.\n")
    lines.append("\nThis output illustrates the constrained minimizer. It does not prove that QGD dynamics selects this sector without the global–local bridge/measurement theory.\n")

    out = OUT / "output_verify_canonical_polarization_toy.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
