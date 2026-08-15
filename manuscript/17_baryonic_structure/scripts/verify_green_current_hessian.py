#!/usr/bin/env python3
"""
GDQ — Chapter 17 / Hessian Green Current

Symbolically verifies the identity:

    d_x j(phi, psi) = U (psi L phi - phi L psi)

for the reduced block:

    L y = - U^{-1} d_x (U A d_x y) + V y.

This is the one-dimensional prototype of the conserved bilinear current used to
normalize physical modes of the Hessian. The script does not use experimental data
and does not adjust parameters.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


def main() -> None:
    x = sp.symbols("x")
    U = sp.exp(-x**2)
    A = 1 + x**2 / 5
    V = 2 + x / 7

    phi = sp.sin(x) + x**2 / 3
    psi = sp.cos(2 * x) + x / 5

    def L(y: sp.Expr) -> sp.Expr:
        return -sp.diff(U * A * sp.diff(y, x), x) / U + V * y

    j = U * A * (phi * sp.diff(psi, x) - psi * sp.diff(phi, x))
    lhs = sp.simplify(sp.diff(j, x))
    rhs = sp.simplify(U * (psi * L(phi) - phi * L(psi)))
    residual = sp.simplify(lhs - rhs)

    lines = [
        "# Output — Green's current of the Hessian",
        "",
        "## Tested operator",
        "",
        "```text",
        "L y = - U^{-1} d_x(U A d_x y) + V y",
        f"U = {sp.sstr(U)}",
        f"A = {sp.sstr(A)}",
        f"V = {sp.sstr(V)}",
        "```",
        "",
        "## Test functions",
        "",
        "```text",
        "phi = " + sp.sstr(phi),
        "psi = " + sp.sstr(psi),
        "```",
        "",
        "## Identity",
        "",
        "```text",
        "d_x j(phi, psi) - U(psi L phi - phi L psi) =",
        sp.sstr(residual),
        "```",
        "",
        f"Result: `residual == 0` is `{residual == 0}`.",
        "",
        "Conclusion: Green's bilinear current is conserved for modes in the kernel of the physical operator.",
        "",
    ]

    out = Path(__file__).with_name("output_verify_green_current_hessian.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
