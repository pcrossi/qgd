#!/usr/bin/env python3
"""
GDQ — Chapter 23 / Molecular Rotor

Objective:
    Symbolically verify the leading centrifugal distortion from the radial
    minimization of the reduced molecular rotor.

Classification:
    Symbolic verification of the derivation. Does not use experimental data.

Model:
    E(R;J) = L^2/(2*mu*R^2) + (1/2)*mu*omega^2*(R-R0)^2

    With R=R0+x and low rotation, minimizing in x yields:

    E_J = B J(J+1) - D [J(J+1)]^2 + ...

    B = hbar^2/(2*mu*R0^2)
    D = hbar^4/(2*mu^3*omega^2*R0^6)

Output:
    output_rotor_distortion_symbolic.md
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


OUT = Path(__file__).with_name("output_rotor_distortion_symbolic.md")


def main() -> None:
    L2, mu, R0, omega, x = sp.symbols("L2 mu R0 omega x", positive=True)

    # Expansion up to x^2. The x^2 term multiplied by L2 would only affect L6 order
    # after substituting x*=O(L2), so it does not enter the leading D~L4 coefficient.
    E = L2 / (2 * mu * R0**2) - L2 * x / (mu * R0**3) + sp.Rational(1, 2) * mu * omega**2 * x**2
    x_star = sp.solve(sp.diff(E, x), x)[0]
    E_eff = sp.expand(E.subs(x, x_star))

    B_coeff = sp.simplify(sp.diff(E_eff, L2).subs(L2, 0))
    D_coeff = sp.simplify(-sp.diff(E_eff, L2, 2).subs(L2, 0) / 2)

    expected_B = 1 / (2 * mu * R0**2)
    expected_D = 1 / (2 * mu**3 * omega**2 * R0**6)

    lines = [
        "---",
        'title: "Output — Symbolic Derivation of Rotor Distortion"',
        "---",
        "",
        "# Output — Symbolic Derivation of Rotor Distortion",
        "",
        "Classification: symbolic verification of the radial harmonic reduction.",
        "",
        "Expanded energy:",
        "",
        "$$",
        "E(x)=\\frac{L^2}{2\\mu R_0^2}-\\frac{L^2}{\\mu R_0^3}x+\\frac{1}{2}\\mu\\omega_e^2x^2.",
        "$$",
        "",
        "Radial minimum:",
        "",
        "$$",
        f"x_\\ast={sp.latex(x_star)}.",
        "$$",
        "",
        "Effective energy:",
        "",
        "$$",
        f"E_{{\\rm eff}}={sp.latex(E_eff)}.",
        "$$",
        "",
        "Coefficients in $E=B_L L^2-D_L L^4+\\cdots$:",
        "",
        "$$",
        f"B_L={sp.latex(B_coeff)},\\qquad D_L={sp.latex(D_coeff)}.",
        "$$",
        "",
        "Check against expected form:",
        "",
        "$$",
        f"B_L-B_{{\\rm exp}}={sp.latex(sp.simplify(B_coeff-expected_B))},",
        "\\qquad",
        f"D_L-D_{{\\rm exp}}={sp.latex(sp.simplify(D_coeff-expected_D))}.",
        "$$",
        "",
        "Since $L^2=\\hbar^2J(J+1)$:",
        "",
        "$$",
        "D=\\frac{\\hbar^4}{2\\mu^3\\omega_e^2R_0^6}.",
        "$$",
        "",
    ]

    text = "\n".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
