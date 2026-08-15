#!/usr/bin/env python3
"""
Objective:
    Self-contained verification record of `verify_localization_gap_toy` associated with chapter `06_global_local_bridge`.

Toy model of localization and uniform gap.

Discrete operator:

    K_L = -d^2/dx^2 + V(x)

on [-L,L], Dirichlet, with local well V=-V0 in |x|<a and exterior V=0.

We increase L. The bound mode remains localized and separated from the discretized
continuum, illustrating the role of Agmon/IMS. This is not real GDQ Hessian.
"""

from pathlib import Path
import numpy as np


OUT = Path(__file__).with_name("output_verify_localization_gap_toy.md")


def operator(L: float, h: float = 0.04, V0: float = 8.0, a: float = 1.0):
    # Internal points with Dirichlet boundary conditions at the endpoints.
    n = int(round(2.0 * L / h)) - 1
    x = np.linspace(-L + h, L - h, n)
    h = x[1] - x[0]
    diag = np.full(n, 2.0 / h**2)
    off = np.full(n - 1, -1.0 / h**2)
    V = np.where(np.abs(x) < a, -V0, 0.0)
    K = np.diag(diag + V) + np.diag(off, 1) + np.diag(off, -1)
    return x, K


def main() -> None:
    rows = []
    for L in [4, 6, 8, 10, 14, 18]:
        x, K = operator(L)
        vals, vecs = np.linalg.eigh(K)
        bound = vals[0]
        next_val = vals[1]
        gap = next_val - bound
        psi = vecs[:, 0]
        psi = psi / np.sqrt(np.trapezoid(psi * psi, x))
        outside = np.trapezoid((psi * psi)[np.abs(x) > 2.0], x[np.abs(x) > 2.0])
        rows.append((L, bound, next_val, gap, outside))

    lines = [
        "---",
        'title: "Output — toy gap and localization"',
        "---",
        "",
        "# Output — toy gap and localization",
        "",
        "Classification: spectral toy model / consistency verification.",
        "",
        "| $L$ | bound eigenvalue | next eigenvalue | gap | mass outside $|x|>2$ |",
        "|---:|---:|---:|---:|---:|",
    ]
    for L, bound, next_val, gap, outside in rows:
        lines.append(
            f"| {L:.0f} | {bound:.10f} | {next_val:.10f} | {gap:.10f} | {outside:.3e} |"
        )

    lines += [
        "",
        "Conclusion: the bound mode remains localized in the core as the external",
        "domain grows. This illustrates why the global-local bridge must use the physical",
        "gap of the defect, not the artificial compactification gap.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
