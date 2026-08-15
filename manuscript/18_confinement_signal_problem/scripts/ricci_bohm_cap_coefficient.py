#!/usr/bin/env python3
"""
GDQ — Chapter 18 / coefficient of the Ricci--Bohm cap.

Objective:
    Verify that C_GDQ = pi comes from Gauss--Bonnet on the transverse
    hemispherical cap with a geodesic boundary, and calculate the associated reduced tension.

Classification:
    Direct evaluation of quantity derived in the reduced transverse sector.
    Does not use QCD/Yang--Mills as a fundamental action and does not adjust to the hadronic target.

Output:
    scripts/output_ricci_bohm_cap_coefficient.md
"""

from __future__ import annotations

from pathlib import Path
import math


HBARC_GEV_FM = 0.1973269804
R_PERP_FM = 0.86
SIGMA_HAD_GEV_PER_FM = 0.89


def main() -> None:
    r = R_PERP_FM
    cap_area = 2.0 * math.pi * r * r
    disk_area = math.pi * r * r
    scalar_curvature = 2.0 / (r * r)
    int_r_da = scalar_curvature * cap_area
    c_gdq = 0.25 * int_r_da
    delta = HBARC_GEV_FM / r
    sigma = c_gdq * HBARC_GEV_FM / (r * r)
    sigma_gev2 = sigma * HBARC_GEV_FM
    sqrt_sigma = math.sqrt(sigma_gev2)
    err = (sigma - SIGMA_HAD_GEV_PER_FM) / SIGMA_HAD_GEV_PER_FM

    lines = [
        "# Output — coefficient of the Ricci-Bohm cap",
        "",
        "Classification: direct evaluation of derived quantity.",
        "",
        "| quantity | value |",
        "|---|---:|",
        f"| r_perp fm | {r:.12f} |",
        f"| cap intrinsic area fm^2 | {cap_area:.12f} |",
        f"| disc projected area fm^2 | {disk_area:.12f} |",
        f"| R2 fm^-2 | {scalar_curvature:.12f} |",
        f"| integral R2 dA | {int_r_da:.12f} |",
        f"| C_GDQ=(1/4) integral R2 dA | {c_gdq:.12f} |",
        f"| Delta GeV | {delta:.12f} |",
        f"| sigma GeV/fm | {sigma:.12f} |",
        f"| sigma GeV^2 | {sigma_gev2:.12f} |",
        f"| sqrt(sigma) GeV | {sqrt_sigma:.12f} |",
        f"| deviation vs 0.89 GeV/fm | {err:.6%} |",
        "",
        "Interpretation: C_GDQ=pi comes from the curvature index of the Ricci--Bohm cap.",
    ]

    out = Path(__file__).with_name("output_ricci_bohm_cap_coefficient.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
