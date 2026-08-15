#!/usr/bin/env python3
"""
Objective:
    Self-contained verification of `ideal casimir` associated with chapter `23_simple_applications`.
    Chapter 23 — ideal Casimir pressure.

Classification:
    Direct evaluation of the universal result for ideal plates.

Equation:
    P(a) = -pi^2 hbar c /(240 a^4).
"""

from __future__ import annotations

from pathlib import Path
import math


OUT = Path(__file__).with_name("output_casimir_ideal.md")


def main() -> None:
    hbar = 1.054_571_817e-34
    c = 299_792_458.0
    separations = [100e-9, 200e-9, 500e-9, 1e-6, 2e-6]

    lines = [
        "---",
        'title: "Output — Ideal Casimir"',
        "---",
        "",
        "# Output — Ideal Casimir",
        "",
        "- formula: $P=-\\pi^2\\hbar c/(240a^4)$;",
        "- classification: direct evaluation of universal ideal result.",
        "",
        "| separation $a$ | pressure [Pa] |",
        "|---:|---:|",
    ]
    for a in separations:
        pressure = -(math.pi**2 * hbar * c) / (240.0 * a**4)
        lines.append(f"| `{a:.1e}` m | `{pressure:.12e}` |")

    lines += [
        "",
        "For real plates, this value must be replaced by an evaluation with",
        "$\\mathsf R_{\\rm plate}(\\omega,k,T)$.",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
