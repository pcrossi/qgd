#!/usr/bin/env python3
"""
Objective:
    Self-contained record of the verification `verify_cotangent_kepler` associated with chapter `07_classical_limit`.

Verifies the local limit of the cotangent potential.

In cosmological space:

    K_R(r) = (1/R) cot(r/R).

For small r/R:

    K_R(r) = 1/r - r/(3R^2) + O(r^3/R^4).
"""

from pathlib import Path
import math


OUT = Path(__file__).with_name("output_verify_cotangent_kepler.md")


def main() -> None:
    r = 1.0
    rows = []
    for R in [5, 10, 20, 50, 100, 200]:
        exact = (1.0 / R) / math.tan(r / R)
        kepler = 1.0 / r
        corrected = kepler - r / (3.0 * R * R)
        err_kepler = abs(exact - kepler)
        err_corrected = abs(exact - corrected)
        rows.append((R, exact, err_kepler, err_corrected, err_kepler * R * R))

    lines = [
        "---",
        'title: "Output — cotangent to Kepler"',
        "---",
        "",
        "# Output — cotangent to Kepler",
        "",
        "Classification: asymptotic consistency verification.",
        "",
        "Fixed local radius: $r=1$.",
        "",
        "| $R$ | $R^{-1}\\cot(r/R)$ | error against $1/r$ | error with correction $-r/(3R^2)$ | error$\\cdot R^2$ |",
        "|---:|---:|---:|---:|---:|",
    ]
    for R, exact, err_k, err_c, scaled in rows:
        lines.append(f"| {R} | {exact:.12f} | {err_k:.6e} | {err_c:.6e} | {scaled:.8f} |")

    lines += [
        "",
        "Conclusion: the cotangent kernel tends locally to the Kepler potential,",
        "with leading correction of order $R^{-2}$.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
