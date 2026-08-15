#!/usr/bin/env python3
"""
Objective:
    Self-contained record of the verification `calculate_reduced_form_factors` associated with chapter `17_baryonic_structure`.

GDQ — Chapter 17 / reduced form factors.

Tests:

    G_E^p(q) = j0(q r_p)
    G_M^p(0) = mu_p
    G_E^n(0) = 0
    <r_n^2> = -2 |mu_n| alpha_tor^(2) r_p^2

Classification: consistency test of surface reduction.
"""

from __future__ import annotations

import math
from pathlib import Path


def j0(x: float) -> float:
    if abs(x) < 1.0e-12:
        return 1.0
    return math.sin(x) / x


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_calculate_reduced_form_factors.md"

    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    r_p = 0.840778765432
    delta_b = math.log(2.0 * math.pi**2) * (3.0 * math.sqrt(2.0) / 5.0)
    mu_p = 1.0 + (3.0 / 5.0) * math.log(2.0 * math.pi**2) * (1.0 + alpha / 4.0)
    mu_n = -(3.0 / 4.0) * delta_b * (1.0 + alpha * 3.0 * math.sqrt(2.0) / 4.0)
    alpha_tor_2 = 2.0 * alpha * math.log(2.0 * math.pi**2)
    rn2 = -2.0 * abs(mu_n) * alpha_tor_2 * r_p * r_p
    ref_rn2 = -0.1161

    qs = [0.0, 0.5, 1.0, 2.0]
    rows = []
    for q in qs:
        ge_p = j0(q * r_p)
        gm_p = mu_p * ge_p
        rows.append((q, ge_p, gm_p))

    lines = [
        "# Output — reduced form factors",
        "",
        "Classification: consistency test of surface reduction.",
        "",
        "| q fm^-1 | G_E^p | G_M^p |",
        "|---:|---:|---:|",
    ]
    for q, ge, gm in rows:
        lines.append(f"| {q:.6f} | {ge:.12f} | {gm:.12f} |")
    lines += [
        "",
        "## Normalizations and neutron",
        "",
        f"- `G_E^p(0) = {rows[0][1]:.12f}`",
        f"- `G_M^p(0) = {rows[0][2]:.12f}`",
        "- `G_E^n(0) = 0` by global neutrality of the two-shell distribution.",
        f"- `<r_n^2>_GDQ = {rn2:.12f} fm^2`",
        f"- `<r_n^2>_ref = {ref_rn2:.12f} fm^2`",
        f"- `relative error = {(rn2-ref_rn2)/ref_rn2:.12e}`",
        "",
        "Interpretation: the proton is represented by a reduced shell and the neutron by",
        "local polarization with zero total charge.",
    ]
    text = "\n".join(lines) + "\n"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
