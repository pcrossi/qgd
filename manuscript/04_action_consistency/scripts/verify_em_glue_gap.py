#!/usr/bin/env python3
"""
Chapter 4 — local cylindrical stoma no-go for Lambda_EM.

Classification:
    Direct evaluation and convergence test.

The radial Neumann operator in the stoma of length L has eigenvalues

    lambda_j = 4/h^2 sin^2(j*pi/(2N)),    h=L/N.

The first physical gap tends to pi^2/L^2. Therefore, in an infinite local
stoma, the gap tends to zero and does not fix a positive EM scale.
"""

from __future__ import annotations

import math
from pathlib import Path


def neumann_gap(length: float, cells: int, j: int = 1) -> float:
    h = length / cells
    return 4.0 * math.sin(j * math.pi / (2.0 * cells)) ** 2 / (h * h)


def main() -> None:
    rows = []
    for length in [1.0, 2.0, 4.0, 8.0, 16.0]:
        gap = neumann_gap(length, 800)
        exact = (math.pi / length) ** 2
        rows.append((length, 0.0, gap, exact, abs(gap - exact) / exact))

    convergence = []
    for cells in [50, 100, 200, 400, 800]:
        gap = neumann_gap(1.0, cells)
        convergence.append((cells, gap, abs(gap - math.pi**2) / math.pi**2))

    lines = [
        "---",
        'title: "Output — stoma electromagnetic gap"',
        "---",
        "",
        "# Output — stoma electromagnetic gap",
        "",
        "| $L$ | zero mode | $\\lambda_1^{\\rm num}$ | $\\pi^2/L^2$ | relative error |",
        "|---:|---:|---:|---:|---:|",
    ]
    for length, zero, gap, exact, error in rows:
        lines.append(f"| `{length:.1f}` | `{zero:.3e}` | `{gap:.10e}` | `{exact:.10e}` | `{error:.3e}` |")
    lines += [
        "",
        "## Refinement for $L=1$",
        "",
        "| cells | $\\lambda_1^{\\rm num}$ | relative error |",
        "|---:|---:|---:|",
    ]
    for cells, gap, error in convergence:
        lines.append(f"| `{cells}` | `{gap:.10e}` | `{error:.3e}` |")
    lines += [
        "",
        "Since $L^2\\lambda_1\\to\\pi^2$, it follows that",
        "",
        "$$",
        "\\lambda_1=\\frac{\\pi^2}{L^2}\\to0",
        "\\quad\\text{when}\\quad L\\to\\infty.",
        "$$",
        "",
        "The infinite local stoma does not yield a positive electromagnetic scale;",
        "the scale depends on global gluing or sectorial resolution.",
        "",
    ]
    out = Path(__file__).with_name("output_verify_em_glue_gap.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
