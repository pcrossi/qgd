#!/usr/bin/env python3
"""
GDQ — Chapter 23 / Ideal Casimir

Objective:
    Symbolically verify the universal coefficient of the ideal Casimir effect
    between perfect parallel plates.

Classification:
    Symbolic consistency test of spectral reduction. It is not an experimental
    fit and does not model real plates.

Equations:
    E/A = (hbar*c/2)*2*sum_n int d^2k/(2*pi)^2 sqrt(k^2 + (n*pi/a)^2)

    int d^2k/(2*pi)^2 sqrt(k^2+m^2) -> -m^3/(6*pi)

    zeta(-3)=1/120

    E/A = -pi^2*hbar*c/(720*a^3)
    P   = -pi^2*hbar*c/(240*a^4)

Output:
    output_casimir_zeta_derivation.md
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


OUT = Path(__file__).with_name("output_casimir_zeta_derivation.md")


def main() -> None:
    zeta_minus_3 = Fraction(1, 120)

    # Energy coefficient:
    # -(1/(6*pi))*(pi^3)*zeta(-3) = -pi^2*(zeta(-3)/6).
    energy_coeff = -zeta_minus_3 / 6

    # If E/A = -C/a^3, then P = -d(E/A)/da = -3C/a^4.
    pressure_coeff = 3 * energy_coeff

    lines = [
        "---",
        'title: "Output — Zeta Derivation of Ideal Casimir"',
        "---",
        "",
        "# Output — Zeta Derivation of Ideal Casimir",
        "",
        "Classification: symbolic spectral consistency test.",
        "",
        "The regularized integral used is:",
        "",
        "$$",
        "\\int\\frac{d^2k}{(2\\pi)^2}\\sqrt{k^2+m^2}",
        "\\longmapsto",
        "-\\frac{m^3}{6\\pi}.",
        "$$",
        "",
        "The spectral sum is:",
        "",
        "$$",
        "\\zeta(-3)=\\frac{1}{120}.",
        "$$",
        "",
        "Coefficient obtained for the energy:",
        "",
        "$$",
        f"\\frac{{\\Delta E}}{{A}}={energy_coeff}\\,\\frac{{\\pi^2\\hbar c}}{{a^3}}.",
        "$$",
        "",
        "Coefficient obtained for the pressure:",
        "",
        "$$",
        f"P={pressure_coeff}\\,\\frac{{\\pi^2\\hbar c}}{{a^4}}.",
        "$$",
        "",
        "Conventional form:",
        "",
        "$$",
        "\\frac{\\Delta E}{A}=-\\frac{\\pi^2\\hbar c}{720a^3},",
        "\\qquad",
        "P=-\\frac{\\pi^2\\hbar c}{240a^4}.",
        "$$",
        "",
        "Interpretation: the factor of 720 comes from two transverse polarizations,",
        "dimensional continuation of the transverse integral, and zeta(-3)=1/120.",
        "In GDQ, this is the evaluation of the determinant of the ideal effective Hessian,",
        "not an alteration of the official action.",
        "",
    ]

    text = "\n".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
