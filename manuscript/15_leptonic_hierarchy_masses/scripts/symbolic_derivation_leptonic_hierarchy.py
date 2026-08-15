#!/usr/bin/env python3
"""Symbolic derivation of the reduced leptonic hierarchy.

Classification:
    symbolic derivation / direct evaluation of the reduced GDQ construction.

This script exists for the self-containment of the manuscript. It does not adjust masses.
It shows, symbolically, how the formulas used in Chapter 15 are obtained:

1. the electron fixes the reduced scale, $R_e=1$;
2. the muon comes from the bispatial support;
3. the interface impedance and the circulation self-energy correct the leading term;
4. the third charged ratio comes from the geometric saturation $Q=2/3$.

The experimental target of $M_\mu$ or $M_\tau$ does not enter the derivation. The
accepted values appear only in the final comparison.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


OUT = Path(__file__).resolve().parent / "output_symbolic_derivation_leptonic_hierarchy.md"


def main() -> None:
    alpha = sp.symbols("alpha", positive=True)
    z = sp.symbols("z", positive=True)

    r_e = sp.Integer(1)
    nu_2 = sp.Rational(2, 3)
    delta_boundary = sp.Rational(6, 5)
    delta_self = 2 * alpha

    r_mu_0 = sp.simplify(1 / (nu_2 * alpha))
    r_mu = sp.simplify(r_mu_0 + delta_boundary + delta_self)

    x = sp.sqrt(r_e)
    y = sp.sqrt(r_mu)
    q_expr = sp.simplify((r_e + r_mu + z**2) / (x + y + z) ** 2)
    equation = sp.Eq(q_expr, sp.Rational(2, 3))
    poly = sp.factor(sp.together(q_expr - sp.Rational(2, 3)).as_numer_denom()[0])
    branches_z = sp.solve(poly, z)
    branches_r = [sp.simplify(branch**2) for branch in branches_z]

    alpha_inv_value = sp.Float("137.035999177")
    alpha_value = 1 / alpha_inv_value
    r_mu_value = sp.N(r_mu.subs(alpha, alpha_value), 18)
    branch_values = [sp.N(branch.subs(alpha, alpha_value), 18) for branch in branches_r]
    branch_values_sorted = sorted(float(v) for v in branch_values)

    ref_mu = 206.768282700
    ref_tau = 3477.150000000
    err_mu = (float(r_mu_value) - ref_mu) / ref_mu
    err_tau = (branch_values_sorted[-1] - ref_tau) / ref_tau

    lines = ["# Output — symbolic derivation of the leptonic hierarchy\n\n"]
    lines.append("Classification: symbolic derivation / direct evaluation.\n\n")
    lines.append("## 1. Electronic sector\n\n")
    lines.append("The electron defines the reduced scale:\n\n")
    lines.append("$$\nR_e=1.\n$$\n\n")
    lines.append("## 2. Muon ratio\n\n")
    lines.append("Bispatial support:\n\n")
    lines.append("$$\n\\nu_2=\\frac23.\n$$\n\n")
    lines.append("Leading term:\n\n")
    lines.append("$$\nR_\\mu^{(0)}=\\frac{1}{\\nu_2\\alpha}=\\frac{3}{2}\\alpha^{-1}.\n$$\n\n")
    lines.append("Interface impedance and self-energy:\n\n")
    lines.append("$$\n\\Delta_\\partial=\\frac65,\n\\qquad\n\\Delta_{\\rm self}=2\\alpha.\n$$\n\n")
    lines.append("Thus:\n\n")
    lines.append("$$\nR_\\mu=\n")
    lines.append(sp.latex(r_mu))
    lines.append(".\n$$\n\n")
    lines.append("## 3. Geometric saturation of the third ratio\n\n")
    lines.append("With $R_3=z^2$, the condition is:\n\n")
    lines.append("$$\n")
    lines.append(sp.latex(equation))
    lines.append(".\n$$\n\n")
    lines.append("The equivalent polynomial numerator is:\n\n")
    lines.append("$$\n")
    lines.append(sp.latex(poly))
    lines.append("=0.\n$$\n\n")
    lines.append("The two solutions for $R_3$ are:\n\n")
    lines.append("$$\nR_{3,\\pm}=\n")
    lines.append("\\left[\n")
    lines.append("2(\\sqrt{R_1}+\\sqrt{R_2})\n")
    lines.append("\\pm\n")
    lines.append("\\sqrt{3R_1+12\\sqrt{R_1R_2}+3R_2}\n")
    lines.append("\\right]^2")
    lines.append(".\n$$\n\n")
    lines.append("The direct symbolic solution of the polynomial in $z$ was used by the script; the form above is the simplified form in terms of $R_1$ and $R_2$.\n\n")
    lines.append("## 4. Numerical evaluation\n\n")
    lines.append("| quantity | value |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| alpha^-1 | {float(alpha_inv_value):.12f} |\n")
    lines.append(f"| R_mu | {float(r_mu_value):.12f} |\n")
    lines.append(f"| R_3 light branch | {branch_values_sorted[0]:.12f} |\n")
    lines.append(f"| R_3 heavy branch | {branch_values_sorted[-1]:.12f} |\n")
    lines.append("\n## 5. Posterior comparison\n\n")
    lines.append("| ratio | GDQ | reference | relative error |\n")
    lines.append("|---|---:|---:|---:|\n")
    lines.append(f"| M_mu/M_e | {float(r_mu_value):.12f} | {ref_mu:.12f} | {err_mu:.12e} |\n")
    lines.append(f"| M_tau/M_e | {branch_values_sorted[-1]:.12f} | {ref_tau:.12f} | {err_tau:.12e} |\n")
    lines.append("\n## Verdict\n\n")
    lines.append(
        "The symbolic derivation produces the muon formula and the two branches of the "
        "third ratio without using experimental masses as input. The choice of the heavy "
        "branch is a physical selection of the charged triplet; the light branch "
        "remains mathematical until it has its own Hessian.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
