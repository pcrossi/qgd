#!/usr/bin/env python3
"""
QGD — Chapter 5 / Global phase symmetry.

Objective:
    Illustrate that a Lagrangian density that depends only on derivatives of
    S_R is invariant under S_R -> S_R + constant, and that the sensitive
    quantity is the gradient.

Theoretical source:
    manuscript/05_equations_conservation/05.6 - Noether, constraints and boundary conditions.md

Classification:
    Continuous symmetry illustration. Not a physical prediction.

Equation:
    L = 1/2 |grad S_R|^2

Domain and boundary:
    Periodic 1D grid.

Parameters:
    Universal:
        none
    Apparatus/experimental data:
        none
    Numerical:
        constant phase shifts.

Output:
    output_verify_noether_phase_shift.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def energy(s: np.ndarray, dx: float) -> float:
    grad = (np.roll(s, -1) - np.roll(s, 1)) / (2.0 * dx)
    return float(np.trapezoid(0.5 * grad * grad, dx=dx))


def main() -> None:
    n = 2000
    x = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    dx = x[1] - x[0]
    s = np.sin(x) + 0.25 * np.sin(3.0 * x)
    e0 = energy(s, dx)
    rows = []
    for shift in [0.0, 0.1, 1.0, -3.5, 10.0]:
        e = energy(s + shift, dx)
        rows.append((shift, e, abs(e - e0)))
    ok = all(err < 1e-12 for _, _, err in rows)

    lines: list[str] = []
    lines.append("# Output — global phase symmetry\n\n")
    lines.append("## Classification\n\n")
    lines.append("Continuous symmetry illustration. Not a physical prediction.\n\n")
    lines.append("## Density used\n\n")
    lines.append("$$\n")
    lines.append("L=\\frac12|\\nabla S_R|^2.\n")
    lines.append("$$\n\n")
    lines.append("Since $L$ depends only on $\\nabla S_R$, global shifts of $S_R$ do not alter the action.\n\n")
    lines.append("## Results\n\n")
    lines.append("| shift | energy | variation |\n")
    lines.append("|---:|---:|---:|\n")
    for shift, e, err in rows:
        lines.append(f"| {shift:.6g} | {e:.12e} | {err:.3e} |\n")
    lines.append("\n## Verdict\n\n")
    lines.append("The check passed.\n" if ok else "The check failed.\n")
    lines.append("\nThis output illustrates the global symmetry. The complete QGD current includes $\\mathcal U$, $g$, and factors of the official action.\n")

    out = OUT / "output_verify_noether_phase_shift.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
