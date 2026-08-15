#!/usr/bin/env python3
"""GDQ — Chapter 20: thermal-axial chain of the gravitational exponent.

Classification:
    symbolic-numerical evaluation of a conditional chain.

This script verifies:

    beta_E = 2*pi*R_H
    tau_* = beta_E^2/16
    lambda_ax = 2/R^2
    Delta u_v = tau_* * pi^2 * lambda_ax

and shows that the gluing condition R = pi^2*sqrt(alpha)*R_H implies
Delta u_v = 1/(2*alpha). The value of alpha used is the Einstein geometric mean
preserved in Chapter 16.
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    alpha = 9.0 / (8.0 * math.pi**4) * (math.pi**5 / 1920.0) ** 0.25

    # The chain depends only on the ratio R/R_H; hence R_H=1 is sufficient.
    R_H = 1.0
    beta_E = 2.0 * math.pi * R_H
    tau_star = beta_E**2 / 16.0
    R = math.pi**2 * math.sqrt(alpha) * R_H
    lambda_ax = 2.0 / R**2
    delta_u = tau_star * math.pi**2 * lambda_ax
    target = 1.0 / (2.0 * alpha)
    second_winding_suppression = math.exp(-12.0)

    text = f"""# Output — thermal-axial chain of G

Classification: symbolic-numerical evaluation of a conditional chain.

| quantity | value |
|---|---:|
| $\\alpha_E^{{\\rm mean}}$ | {alpha:.15e} |
| $(\\alpha_E^{{\\rm mean}})^{{-1}}$ | {1.0 / alpha:.12f} |
| normalized $R_H$ | {R_H:.12f} |
| $\\beta_E=2\\pi R_H$ | {beta_E:.12f} |
| $\\tau_*=\\beta_E^2/16$ | {tau_star:.12f} |
| $R=\\pi^2\\sqrt\\alpha R_H$ | {R:.12f} |
| $\\lambda_{{\\rm ax}}=2/R^2$ | {lambda_ax:.12f} |
| $\\Delta u_v=\\tau_*\\pi^2\\lambda_{{\\rm ax}}$ | {delta_u:.12f} |
| $1/(2\\alpha)$ | {target:.12f} |
| difference | {delta_u - target:.3e} |
| relative suppression of the second winding $e^{{-12}}$ | {second_winding_suppression:.12e} |

Interpretation: the thermal saddle and the axial mode are calculated directly. The
equality with $1/(2\\alpha)$ requires the global gluing condition
$R=\\pi^2\\sqrt\\alpha R_H$.
"""

    assert abs(delta_u - target) < 1e-12
    out = Path(__file__).resolve().parent / "output_calculate_thermal_axial_g_chain.md"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
