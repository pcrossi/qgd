#!/usr/bin/env python3
"""
GDQ — Chapter 18 / effective radius, form factor, and tension.

Objective:
    Calculate the Ricci--Bohm tension for the canonical surface radius and for the
    compressed probe radius. The comparison with 0.89 GeV/fm is done only
    after the calculations.

Classification:
    Direct evaluation + posterior phenomenological comparison.

Output:
    scripts/output_radius_form_factor_tension.md
"""

from __future__ import annotations

from pathlib import Path
import math


HBARC_GEV_FM = 0.1973269804
ALPHA = 1.0 / 137.03599907
LAMBDA_C_FM = 386.159268
R_PRIMITIVE_FM = 0.86
R_COMPRESSED_FM = 0.8354
SIGMA_REF_GEV_PER_FM = 0.89


def sigma_from_radius(r_fm: float) -> float:
    return math.pi * HBARC_GEV_FM / (r_fm * r_fm)


def main() -> None:
    epsilon_eff = 5.0 * ALPHA / math.pi - ((4.0 / 9.0) * ALPHA**2 - (math.pi / 2.0) * ALPHA**3)
    c_r = 0.125 * (1.0 + ALPHA / 4.0)
    r_b = 1.5 * LAMBDA_C_FM
    r_p = c_r * epsilon_eff * r_b

    rows = []
    for label, r in [
        ("primitive cap", R_PRIMITIVE_FM),
        ("canonical surface radius", r_p),
        ("compressed probe radius", R_COMPRESSED_FM),
    ]:
        sigma = sigma_from_radius(r)
        rows.append(
            (
                label,
                r,
                (R_PRIMITIVE_FM / r) ** 2,
                sigma,
                sigma * HBARC_GEV_FM,
                math.sqrt(sigma * HBARC_GEV_FM),
                (sigma - SIGMA_REF_GEV_PER_FM) / SIGMA_REF_GEV_PER_FM,
            )
        )

    lines = [
        "# Output — effective radius, form factor, and tension",
        "",
        "Classification: direct evaluation; posterior comparison.",
        "",
        "| quantity | value |",
        "|---|---:|",
        f"| alpha | {ALPHA:.12f} |",
        f"| epsilon_eff | {epsilon_eff:.12f} |",
        f"| C_r | {c_r:.12f} |",
        f"| R_B fm | {r_b:.12f} |",
        f"| canonical r_p fm | {r_p:.12f} |",
        "",
        "| case | r fm | F_shape vs 0.86 | sigma GeV/fm | sigma GeV^2 | sqrt(sigma) GeV | deviation vs 0.89 |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for label, r, f_shape, sigma, sigma_gev2, sqrt_sigma, err in rows:
        lines.append(
            f"| {label} | {r:.12f} | {f_shape:.12f} | {sigma:.12f} | {sigma_gev2:.12f} | {sqrt_sigma:.12f} | {err:.6%} |"
        )

    lines += [
        "",
        "Interpretation: the canonical radius closes the structural scale; the compressed probe radius closes the metrology almost completely, but remains a probe boundary until re-derived in the same transverse background.",
    ]

    out = Path(__file__).with_name("output_radius_form_factor_tension.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
