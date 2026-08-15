#!/usr/bin/env python3
"""
GDQ — Chapter 14 / Monotonicity and stability

Objective:
    Illustrate by self-contained calculation the difference between:

    1. having a monotonic Lyapunov functional along a flow;
    2. proving stability by positive Hessian in the physical sector.

    The script uses two quadratic models:

        E_min(x,y) = 0.5*(x^2 + 2 y^2)
        E_saddle(x,y) = 0.5*(x^2 - y^2)

    In the first, the Hessian is positive and the gradient flow relaxes.
    In the second, there is a negative direction: the origin is a critical point, but it is a saddle.

    This mirrors the GDQ criterion: Perelman--Bismut provides Lyapunov; particle
    stability requires the Jacobi/Hessian operator in the projected physical
    space.

Classification:
    Symbolic-numerical illustration of stability criterion.
    Not a physical prediction.

Output:
    output_monotonicity_vs_hessian.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


def gradient_flow(hessian: np.ndarray, x0: np.ndarray, dt: float, steps: int) -> tuple[np.ndarray, np.ndarray]:
    """Integrates dx/dt = -H x by small explicit Euler."""
    x = x0.astype(float).copy()
    energies = []
    norms = []
    for _ in range(steps):
        energies.append(0.5 * float(x @ hessian @ x))
        norms.append(float(np.linalg.norm(x)))
        x = x - dt * (hessian @ x)
    return np.array(energies), np.array(norms)


def main() -> None:
    root = Path(__file__).resolve().parent
    h_min = np.diag([1.0, 2.0])
    h_saddle = np.diag([1.0, -1.0])
    x0 = np.array([0.8, 0.2])
    dt = 0.01
    steps = 600

    e_min, n_min = gradient_flow(h_min, x0, dt, steps)
    e_sad, n_sad = gradient_flow(h_saddle, x0, dt, steps)

    eig_min = np.linalg.eigvalsh(h_min)
    eig_sad = np.linalg.eigvalsh(h_saddle)

    monotone_min = bool(np.all(np.diff(e_min) <= 1e-14))

    # In the saddle case, the energy also decreases for the gradient flow,
    # but the state runs away in the negative direction and the norm grows.
    monotone_sad = bool(np.all(np.diff(e_sad) <= 1e-14))
    norm_growth_sad = float(n_sad[-1] / n_sad[0])

    lines: list[str] = []
    lines.append('---\n')
    lines.append('title: "Output — Monotonicity versus Hessian"\n')
    lines.append('---\n\n')
    lines.append("# Output — Monotonicity versus Hessian\n\n")
    lines.append("## Classification\n\n")
    lines.append("Symbolic-numerical illustration of stability criterion. Not a physical prediction.\n\n")
    lines.append("## Models\n\n")
    lines.append("$$\n")
    lines.append("E_{\\rm min}=\\frac12(x^2+2y^2),\n")
    lines.append("\\qquad\n")
    lines.append("E_{\\rm saddle}=\\frac12(x^2-y^2).\n")
    lines.append("$$\n\n")
    lines.append("Flow used:\n\n")
    lines.append("$$\n")
    lines.append("\\dot X=-\\nabla E=-HX.\n")
    lines.append("$$\n\n")
    lines.append("## Hessians\n\n")
    lines.append("| case | Hessian eigenvalues | interpretation |\n")
    lines.append("|---|---:|---|\n")
    lines.append(f"| minimum | {eig_min.tolist()} | stable |\n")
    lines.append(f"| saddle | {eig_sad.tolist()} | unstable due to negative direction |\n\n")
    lines.append("## Evolution\n\n")
    lines.append("| case | initial energy | final energy | monotonic energy? | final/initial norm ratio |\n")
    lines.append("|---|---:|---:|---|---:|\n")
    lines.append(f"| minimum | {e_min[0]:.12e} | {e_min[-1]:.12e} | {monotone_min} | {n_min[-1]/n_min[0]:.12e} |\n")
    lines.append(f"| saddle | {e_sad[0]:.12e} | {e_sad[-1]:.12e} | {monotone_sad} | {norm_growth_sad:.12e} |\n\n")
    lines.append("## Verdict\n\n")
    lines.append(
        "Energy can be monotonic along the flow even when the critical point "
        "is a saddle. Therefore, for GDQ, Perelman--Bismut monotonicity "
        "is a Lyapunov condition, but soliton stability requires a physical Hessian "
        "without negative eigenvalues after projecting gauge, symmetries, and moduli.\n"
    )

    out = root / "output_monotonicity_vs_hessian.md"
    out.write_text("".join(lines), encoding="utf-8")
    print("".join(lines))


if __name__ == "__main__":
    main()
