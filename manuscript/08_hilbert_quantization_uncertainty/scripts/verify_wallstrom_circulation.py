#!/usr/bin/env python3
"""
Reduced verification of circulation quantization.

Classification: symbolic/topological test.

This script does not prove the global structure of GDQ. It records, in a
self-contained manner, two algebraic consequences used in the proof of Chapter 8:

1. regular maps S^1 -> S^1 close only for integer winding;
2. the first Chern class of a U(1) bundle requires integer flux.

For chi(theta)=N theta:

    (1/2pi) integral_0^{2pi} d chi = N.

Non-integer values can be written locally, but do not define a single-valued
map S^1 -> S^1, as exp(i alpha(theta+2pi)) != exp(i alpha theta).

For the Chern example on T^2, with x,y in [0,2pi), use:

    F = N/(2pi) dx wedge dy.

Then:

    (1/2pi) integral_{T^2} F = N.
"""

from __future__ import annotations

from pathlib import Path
import cmath
import math

OUT = Path(__file__).with_name("output_verify_wallstrom_circulation.md")


def closes_s1(alpha: float, tol: float = 1e-12) -> tuple[bool, float]:
    """Returns whether exp(i alpha theta) closes at theta~theta+2pi."""
    defect = abs(cmath.exp(1j * 2.0 * math.pi * alpha) - 1.0)
    return defect < tol, defect


def chern_number_on_t2(N: float) -> float:
    """Calculates (1/2pi) integral F for F=N/(2pi) dx^dy on T^2."""
    area_t2 = (2.0 * math.pi) ** 2
    flux = (N / (2.0 * math.pi)) * area_t2
    return flux / (2.0 * math.pi)


def main() -> None:
    winding_values = [-2, -1, 0, 1, 2, 0.5, 1.3]
    chern_values = [-2, -1, 0, 1, 3, 0.5]

    lines = [
        "---",
        'title: "Output — Wallstrom circulation"',
        "---",
        "",
        "# Output — Wallstrom circulation",
        "",
        "Classification: symbolic/topological test.",
        "",
        "## Maps $S^1\\to S^1$",
        "",
        "| parameter $\\alpha$ | phase closes? | defect $|e^{i2\\pi\\alpha}-1|$ | formal winding |",
        "|---:|---:|---:|---:|",
    ]

    for alpha in winding_values:
        closes, defect = closes_s1(alpha)
        lines.append(f"| {alpha} | {str(closes)} | {defect:.6e} | {alpha} |")

    lines += [
        "",
        "Conclusion: the integral can be formally calculated for any",
        "$\\alpha$, but only integers close the regular global map",
        "$S^1\\to S^1$.",
        "",
        "## Example of Chern Flux on $T^2$",
        "",
        "For $F=N(2\\pi)^{-1}dx\\wedge dy$ on $[0,2\\pi)^2$:",
        "",
        "| parameter $N$ | $(2\\pi)^{-1}\\int_{T^2}F$ | integer flux? |",
        "|---:|---:|---:|",
    ]

    for N in chern_values:
        c1 = chern_number_on_t2(N)
        is_integer = abs(c1 - round(c1)) < 1e-12
        lines.append(f"| {N} | {c1:.12f} | {str(is_integer)} |")

    lines += [
        "",
        "Additional conclusion: the curvature can be formally written with any",
        "$N$, but only integer classes represent the first Chern class of",
        "a globally admissible $U(1)$ line bundle.",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
