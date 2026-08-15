#!/usr/bin/env python3
"""
GDQ — Chapter 19 / Product, Berger and collar no-go

Objective:
    Numerically record the consolidated negative diagnostics:
      - product/local preserves Z_W/Z_Y=1 and sin²(theta_W)=3/8;
      - homogeneous Berger mode has negative effective Hessian;
      - photon in the infinite cylindrical collar has divergent norm.

Classification:
    Consistency test/no-go. Preserved negative result.

Output:
    scripts/output_no_go_berger_collar.md
"""

from pathlib import Path


def main() -> None:
    z_ratio_product = 1.0
    gprime2_over_g2_match = 3.0 / 5.0
    sin2_product = gprime2_over_g2_match * z_ratio_product / (
        1.0 + gprime2_over_g2_match * z_ratio_product
    )

    hq_eff = -2.67090856
    collar_lengths = [1.0, 10.0, 100.0, 1000.0]
    photon_norm_density = 1.0

    lines = [
        "# Output — product/Berger/collar no-go",
        "",
        "Classification: consistency test with negative result.",
        "",
        "| quantity | value |",
        "|---|---:|",
        f"| Z_W/Z_Y in the local product | {z_ratio_product:.12f} |",
        f"| sin2_theta in the local product | {sin2_product:.12f} |",
        f"| H_q_eff Berger | {hq_eff:.8f} |",
        "",
        "## Photonic norm in the cylindrical collar",
        "",
        "| length L | proportional norm |",
        "|---:|---:|",
    ]

    for length in collar_lengths:
        lines.append(f"| {length:.1f} | {photon_norm_density * length:.1f} |")

    lines += [
        "",
        "Interpretation: in the infinite collar, the norm grows without bound; therefore, the cylindrical ansatz does not localize the photon and does not predict alpha.",
    ]

    out = Path(__file__).with_name("output_no_go_berger_collar.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
