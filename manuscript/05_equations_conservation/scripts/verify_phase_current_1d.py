#!/usr/bin/env python3
"""
QGD — Chapter 5 / Phase current in 1D.

Objective:
    Illustrate that zero divergence preserves integrated charge and that flux
    through the boundary changes the charge according to the divergence theorem.

Theoretical source:
    manuscript/05_equations_conservation/05.3 - Phase variation and flux conservation.md
    manuscript/notes/equations/Derivation of the phase current.md

Classification:
    Current conservation illustration. Not a physical prediction.

Equation:
    dQ/dt = -J(right boundary) + J(left boundary)

Domain and boundary:
    1D interval [0,1]. Compares constant current and current with net
    boundary flux.

Parameters:
    Universal:
        none
    Apparatus/experimental data:
        none
    Numerical:
        1D grid.

Output:
    output_verify_phase_current_1d.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def divergence(j: np.ndarray, x: np.ndarray) -> np.ndarray:
    return np.gradient(j, x)


def main() -> None:
    x = np.linspace(0.0, 1.0, 1001)
    currents = {
        "constant": np.ones_like(x) * 2.0,
        "linear": 1.0 + 0.3 * x,
        "no_net_flux": 1.0 + 0.2 * np.sin(2.0 * np.pi * x),
    }
    rows = []
    for name, j in currents.items():
        div_int = float(np.trapezoid(divergence(j, x), x))
        boundary_balance = float(j[-1] - j[0])
        charge_rate = -boundary_balance
        rows.append((name, div_int, boundary_balance, charge_rate))

    ok = all(abs(div_int - balance) < 1e-6 for _, div_int, balance, _ in rows)

    lines: list[str] = []
    lines.append("# Output — phase current in 1D\n\n")
    lines.append("## Classification\n\n")
    lines.append("Current conservation illustration. Not a physical prediction.\n\n")
    lines.append("## Verified identity\n\n")
    lines.append("In an interval:\n\n")
    lines.append("$$\n")
    lines.append("\\int_0^1\\partial_xJ\\,dx=J(1)-J(0).\n")
    lines.append("$$\n\n")
    lines.append("Therefore:\n\n")
    lines.append("$$\n")
    lines.append("\\frac{dQ}{dt}=-J(1)+J(0).\n")
    lines.append("$$\n\n")
    lines.append("## Results\n\n")
    lines.append("| case | $\\int\\partial_xJdx$ | $J(1)-J(0)$ | $dQ/dt$ |\n")
    lines.append("|---|---:|---:|---:|\n")
    for name, div_int, boundary_balance, charge_rate in rows:
        lines.append(f"| {name} | {div_int:.12e} | {boundary_balance:.12e} | {charge_rate:.12e} |\n")
    lines.append("\n## Verdict\n\n")
    lines.append("The check passed.\n" if ok else "The check failed.\n")
    lines.append("\nThis output illustrates integrated conservation; the real QGD current depends on $\\mathcal U$, $g$, and $S_R$.\n")

    out = OUT / "output_verify_phase_current_1d.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
