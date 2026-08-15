#!/usr/bin/env python3
"""
GDQ — Chapter 18 / Constrained torsional Hessian.

Objective:
    Evaluate the homogeneous radial Hessian of the throat with conserved torsional charge:

        K_R = 6*(3*R^2 - 8*tau)/R^4.

Classification:
    Direct evaluation of sectorial Hessian already derived.

Output:
    scripts/output_constrained_torsional_hessian.md
"""

from __future__ import annotations

from pathlib import Path


R = 1.03707435228632
TAU = 0.274900522513626


def main() -> None:
    ratio = R * R / TAU
    threshold = 8.0 / 3.0
    k_r = 6.0 * (3.0 * R * R - 8.0 * TAU) / (R**4)
    inv = 1.0 / k_r

    lines = [
        "# Output — constrained torsional Hessian",
        "",
        "Classification: direct evaluation of sectorial Hessian.",
        "",
        "| quantity | value |",
        "|---|---:|",
        f"| R | {R:.14f} |",
        f"| tau | {TAU:.15f} |",
        f"| R^2/tau | {ratio:.14f} |",
        f"| threshold 8/3 | {threshold:.14f} |",
        f"| K_R | {k_r:.14f} |",
        f"| K_R^-1 | {inv:.14f} |",
        "",
        f"Stable in the constrained homogeneous mode: {k_r > 0 and ratio > threshold}.",
    ]

    out = Path(__file__).with_name("output_constrained_torsional_hessian.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
