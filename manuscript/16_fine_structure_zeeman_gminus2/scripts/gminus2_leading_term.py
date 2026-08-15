#!/usr/bin/env python3
"""
Objective:
    Self-contained verification script for `gminus2 leading term` associated with chapter `16_fine_structure_zeeman_gminus2`.

QGD — Chapter 16 / leading term of g-2.

Calculates:

    a1 = alpha/(2*pi)
    g1 = 2*(1+a1)

and compares with reference values already recorded in the Zeeman/g-2 sector. The comparison is
phenomenological; the residuals are not fitted.
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_gminus2_leading_term.md"

    cases = [
        ("registered metrological alpha", 137.035999177),
        ("QGD geometric alpha", 137.036082448164),
    ]
    g_e_ref = 2.002319304361180
    a_mu_ref = 116592059e-11

    rows = []
    for label, alpha_inv in cases:
        alpha = 1.0 / alpha_inv
        a1 = alpha / (2.0 * math.pi)
        g1 = 2.0 * (1.0 + a1)
        rows.append((label, alpha_inv, a1, g1, g_e_ref - g1, a_mu_ref - a1))

    lines = [
        "# Output — leading term of g-2",
        "",
        "Classification: direct evaluation of the leading term; it is not complete metrology.",
        "",
        "| case | alpha^-1 | a1 | g1 | g_e_ref-g1 | a_mu_ref-a1 |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row[0]} | {row[1]:.12f} | {row[2]:.15e} | {row[3]:.15f} | {row[4]:.15e} | {row[5]:.15e} |"
        )
    lines += [
        "",
        "Interpretation: $a_1=\\alpha/(2\\pi)$ is the geometric leading term. The",
        "residuals indicate upper channels of the physical Hessian, not parameters to",
        "adjust within this chapter.",
    ]
    text = "\n".join(lines) + "\n"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
