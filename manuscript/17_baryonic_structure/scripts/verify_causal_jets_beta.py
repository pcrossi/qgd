#!/usr/bin/env python3
"""GDQ — Chapter 17 / Causal jets of the beta overlap."""

from __future__ import annotations

from pathlib import Path

import sympy as sp


def main() -> None:
    z = sp.symbols("z")
    p0, p1, p2, p3 = sp.symbols("P0 P1 P2 P3")
    n0, n1, n2, n3 = sp.symbols("N0 N1 N2 N3")
    x1, x2, x3, e0 = sp.symbols("x1 x2 x3 E0")

    pullback = p0 + p1 * z + p2 * z**2 / 2 + p3 * z**3 / 6
    vertex = n0 + n1 * z + n2 * z**2 / 2 + n3 * z**3 / 6
    coeff = sp.expand(pullback * vertex).coeff(z, 3)
    expected = (p0 * n3 + 3 * p1 * n2 + 3 * p2 * n1 + p3 * n0) / 6
    residual_coeff = sp.simplify(coeff - expected)

    distortion = x1 * z + x2 * z**2 / 2 + x3 * z**3 / 6
    energy = e0 * sp.exp(-distortion)
    third = sp.simplify(sp.diff(energy, z, 3).subs(z, 0))
    expected_third = e0 * (-x1**3 + 3 * x1 * x2 - x3)
    residual_third = sp.simplify(third - expected_third)

    lines = [
        "# Output — causal jets of the beta overlap",
        "",
        "Classification: symbolic consistency test; does not assign physical values to the jets.",
        "",
        "```text",
        f"[z^3](P N) = {sp.sstr(coeff)}",
        f"residual coefficient = {sp.sstr(residual_coeff)}",
        f"E_T'''(0) = {sp.sstr(third)}",
        f"residual third jet = {sp.sstr(residual_third)}",
        "```",
        "",
        "Conclusion: physical jets must be calculated from the causal background; the identity only fixes the algebraic composition.",
        "",
    ]
    out = Path(__file__).with_name("output_verify_causal_jets_beta.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
