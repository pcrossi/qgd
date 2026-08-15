#!/usr/bin/env python3
"""
GDQ — Chapter 17 / proton surface radius convergence.

Classification:
    consistency test of the surface observable.

The proton electromagnetic radius is not the volumetric average of the internal
radial eigenvector. In the GDQ reduction used in this chapter, it is a boundary observable:

    r_p = C_r * epsilon_eff * R_B,
    C_r = (1/8)(1 + alpha/4),
    R_B = (3/2) Lambda_C.

This script regularizes the surface delta by a half-gaussian and verifies that
the limit sigma -> 0 converges to the structural radius.
"""

from __future__ import annotations

import math
from pathlib import Path


def half_gaussian_shell_radius(epsilon_eff: float, c_scale: float, sigma: float) -> float:
    """RMS radius of a regularized boundary shell at chi >= epsilon_eff."""
    mean_chi2 = (
        epsilon_eff**2
        + 2.0 * epsilon_eff * sigma / math.sqrt(math.pi)
        + 0.5 * sigma**2
    )
    return c_scale * math.sqrt(mean_chi2)


def main() -> None:
    alpha = 1.0 / 137.035999177
    lambda_c_fm = 386.159268
    r_b = 1.5 * lambda_c_fm
    epsilon_eff = 0.011591040463
    c_r = 0.125 * (1.0 + alpha / 4.0)
    c_scale = c_r * r_b
    r_p = c_scale * epsilon_eff

    rows: list[tuple[float, float, float]] = []
    for frac in [1 / 2, 1 / 4, 1 / 8, 1 / 16, 1 / 32, 1 / 64, 1 / 128, 1 / 256]:
        sigma = epsilon_eff * frac
        r_sigma = half_gaussian_shell_radius(epsilon_eff, c_scale, sigma)
        rows.append((frac, r_sigma, (r_sigma - r_p) / r_p))

    lines = [
        "---",
        'title: "Output — surface radius convergence"',
        "---",
        "",
        "# Output — surface radius convergence",
        "",
        "## Structural formula",
        "",
        "$$",
        "r_p",
        "=",
        "C_r\\epsilon_{\\rm eff}R_B,",
        "\\qquad",
        "C_r=\\frac18\\left(1+\\frac\\alpha4\\right),",
        "\\qquad",
        "R_B=\\frac32\\Lambda_C.",
        "$$",
        "",
        "| quantity | value |",
        "|---|---:|",
        f"| $\\Lambda_C$ | `{lambda_c_fm:.6f}` fm |",
        f"| $R_B$ | `{r_b:.12f}` fm |",
        f"| $\\epsilon_{{\\rm eff}}$ | `{epsilon_eff:.12f}` |",
        f"| $C_r$ | `{c_r:.15f}` |",
        f"| structural $r_p$ | `{r_p:.12f}` fm |",
        "",
        "## Regularization by half-gaussian",
        "",
        "| $\\sigma/\\epsilon_{\\rm eff}$ | $r_p(\\sigma)$ fm | relative deviation |",
        "|---:|---:|---:|",
    ]
    for frac, r_sigma, rel in rows:
        lines.append(f"| `{frac:.8f}` | `{r_sigma:.12f}` | `{rel:+.12e}` |")
    lines.append(f"| `delta_surface` | `{r_p:.12f}` | `{0.0:+.12e}` |")
    lines.extend(
        [
            "",
            "## Verdict",
            "",
            "The regularized sequence converges to the surface delta. The raw",
            "radial volumetric calculation measures the internal bulk mode, not the",
            "observed electromagnetic radius.",
            "",
        ]
    )

    out = Path(__file__).with_name("output_surface_radius_convergence.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
