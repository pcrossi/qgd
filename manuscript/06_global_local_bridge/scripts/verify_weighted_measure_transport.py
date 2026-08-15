#!/usr/bin/env python3
"""
Objective:
    Self-contained verification record of `verify_weighted_measure_transport` associated with chapter `06_global_local_bridge`.

Educational verification of weighted measure transport.

Model:
- normalized Gaussian density in local space x;
- scale change y = a x;
- the transported density must include the inverse Jacobian:

      rho_y(y) = rho_x(y/a) / a.

Without this factor, the probability norm is not preserved.
"""

from pathlib import Path
import math


OUT = Path(__file__).with_name("output_verify_weighted_measure_transport.md")


def rho_x(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def integrate(func, lo: float, hi: float, n: int = 200000) -> float:
    h = (hi - lo) / n
    total = 0.5 * (func(lo) + func(hi))
    for i in range(1, n):
        total += func(lo + i * h)
    return total * h


def main() -> None:
    a_values = [0.5, 1.0, 2.0, 4.0]
    rows = []
    for a in a_values:
        lo, hi = -10.0 * a, 10.0 * a
        correct = integrate(lambda y: rho_x(y / a) / a, lo, hi)
        wrong = integrate(lambda y: rho_x(y / a), lo, hi)
        rows.append((a, correct, wrong))

    lines = [
        "---",
        'title: "Output — weighted measure transport"',
        "---",
        "",
        "# Output — weighted measure transport",
        "",
        "Classification: consistency verification / measure toy model.",
        "",
        "| scale $a$ | norm with Jacobian | norm without Jacobian |",
        "|---:|---:|---:|",
    ]
    for a, correct, wrong in rows:
        lines.append(f"| {a:.1f} | {correct:.12f} | {wrong:.12f} |")

    lines += [
        "",
        "Conclusion: the correct transport of the measure requires the Jacobian factor.",
        "In Chapter 6, this corresponds to the care taken to identify the Hilbert",
        "spaces weighted by the square root of the measure's Jacobian, not just",
        "pulling back functions between charts.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
