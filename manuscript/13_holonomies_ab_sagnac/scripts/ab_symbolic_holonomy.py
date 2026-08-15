#!/usr/bin/env python3
"""
GDQ — Chapter 13 / Symbolic Aharonov--Bohm

Objective:
    Verify symbolically the ideal representative

        A_harm = (Phi/(2*pi)) dtheta

    on the punctured exterior of the solenoid:

        dA_harm = 0,
        integral_gamma A_harm = Phi,
        Hol_gamma = exp(i q Phi/(hbar c)).

GDQ Interpretation:
    The script does not introduce new dynamics. It only verifies the topological
    part of the effective reduction: the exterior field is locally flat, but the
    connection is not globally exact in the punctured domain.

Classification:
    Symbolic consistency test of the ideal holonomy.

Output:
    scripts/output_ab_symbolic_holonomy.md
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_ab_symbolic_holonomy.md"

    r, theta, phi = sp.symbols("r theta phi", positive=True, real=True)
    Phi, q, hbar, c = sp.symbols("Phi q hbar c", nonzero=True, real=True)

    # In cylindrical coordinates on the exterior of the solenoid, the differential
    # representative is A = A_theta dtheta. Since A_theta is constant in r,theta,z
    # in this system of 1-forms, dA = d(A_theta) wedge dtheta = 0.
    A_theta = Phi / (2 * sp.pi)
    dA_coeff_dr_dtheta = sp.diff(A_theta, r)
    dA_coeff_dphi_dtheta = sp.diff(A_theta, phi)

    loop_integral = sp.integrate(A_theta, (theta, 0, 2 * sp.pi))
    holonomy = sp.exp(sp.I * q * loop_integral / (hbar * c))

    # Single-valued gauge transformation: lambda(theta)=a sin(theta). The closed
    # integral of d lambda must vanish.
    a = sp.symbols("a", real=True)
    lam = a * sp.sin(theta)
    gauge_loop = sp.integrate(sp.diff(lam, theta), (theta, 0, 2 * sp.pi))

    checks = {
        "dA_dr_dtheta": sp.simplify(dA_coeff_dr_dtheta),
        "dA_dphi_dtheta": sp.simplify(dA_coeff_dphi_dtheta),
        "loop_integral": sp.simplify(loop_integral),
        "gauge_loop_univoca": sp.simplify(gauge_loop),
        "holonomy": holonomy,
    }

    text = f"""# Output — symbolic AB holonomy

Classification: symbolic consistency test of the ideal holonomy.

## Representative

$$
A_{{\\rm harm}}
=
\\frac{{\\Phi}}{{2\\pi}}\\,d\\theta.
$$

## Exterior closure

The verified symbolic coefficients of $dA_{{\\rm harm}}$ are:

| Coefficient | Result |
|---|---:|
| $\\partial_r(\\Phi/2\\pi)$ | {sp.latex(checks['dA_dr_dtheta'])} |
| $\\partial_z(\\Phi/2\\pi)$ | {sp.latex(checks['dA_dphi_dtheta'])} |

Thus, in the exterior domain:

$$
dA_{{\\rm harm}}=0.
$$

## Loop integral

$$
\\oint_\\gamma A_{{\\rm harm}}
=
\\int_0^{{2\\pi}}
\\frac{{\\Phi}}{{2\\pi}}\\,d\\theta
=
{sp.latex(checks['loop_integral'])}.
$$

## Holonomy

$$
\\operatorname{{Hol}}_\\gamma(A)
=
{sp.latex(checks['holonomy'])}.
$$

## Single-valued gauge invariance

For $\\lambda(\\theta)=a\\sin\\theta$:

$$
\\oint_\\gamma d\\lambda
=
{sp.latex(checks['gauge_loop_univoca'])}.
$$

Conclusion: the representative is locally flat, but its loop integral on the
punctured loop preserves the global class $\\Phi$.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
