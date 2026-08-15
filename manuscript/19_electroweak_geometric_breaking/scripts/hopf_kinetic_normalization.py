#!/usr/bin/env python3
"""
GDQ — Chapter 19 / Kinetic normalization of the Hopf mode

Objective:
    Calculate the internal norm of the 2-form potential associated with the
    electroweak harmonic l=1 on S^3.

Classification:
    Direct evaluation of derived quantity. Does not use experimental data.

Output:
    scripts/output_hopf_kinetic_normalization.md
"""

from pathlib import Path


def main() -> None:
    radius = 1.998411184770
    tau = 1.0
    lambda_l1 = 3.0 / radius**2
    mean_y2 = 0.25
    norm_a2 = mean_y2 / lambda_l1
    z_beta_over_c = tau * norm_a2

    lines = [
        "# Output — kinetic normalization of the Hopf mode",
        "",
        "Classification: direct evaluation of derived quantity.",
        "",
        "| quantity | value |",
        "|---|---:|",
        f"| R | {radius:.12f} |",
        f"| lambda_l1=3/R^2 | {lambda_l1:.12f} |",
        f"| <Y^2> | {mean_y2:.12f} |",
        f"| <|A_EW|^2> | {norm_a2:.12f} |",
        f"| Z_beta/C_GDQ | {z_beta_over_c:.12f} |",
        "",
        "Interpretation: the internal integral is closed; the conversion to GeV requires the global dimensional/causal prefactor.",
    ]

    out = Path(__file__).with_name("output_hopf_kinetic_normalization.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
