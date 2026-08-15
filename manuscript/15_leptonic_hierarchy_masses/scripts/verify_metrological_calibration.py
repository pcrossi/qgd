#!/usr/bin/env python3
"""
GDQ — Chapter 15 / metrological scale calibration.

Classification:
    symbolic-numerical verification of dimensional relationships.

This script does not try to derive the MeV unit from nothing. It verifies:

1. normalized eigenvalues produce scale-independent ratios;
2. a scale E0 converts pure numbers into energies;
3. calibrating by M_e preserves ratio predictions;
4. the beta bridge Q_beta=(delta_B-1) M_e c^2 is a metrological calibration,
   not an absolute mass without dimensional input.

The script is self-contained and writes the Markdown output used by the chapter.
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv

    r_e = 1.0
    r_mu = 1.5 * alpha_inv + 6.0 / 5.0 + 2.0 * alpha

    m_e_mev = 0.51099895000
    m_mu_from_ratio = m_e_mev * r_mu

    # Posterior reference for comparison, not input to the formula.
    m_mu_ref = 105.6583755
    err_mu = (m_mu_from_ratio - m_mu_ref) / m_mu_ref

    # Geometric mean of Einstein space used as a pure number.
    delta_b = math.log(2.0 * math.pi**2) * (3.0 * math.sqrt(2.0) / 5.0)
    q_beta_from_me = (delta_b - 1.0) * m_e_mev

    # Illustrative metrological value of the free beta endpoint used as a standard
    # of comparison; does not enter the derivation of delta_B.
    q_beta_ref = 0.782333
    m_e_from_beta = q_beta_ref / (delta_b - 1.0)
    err_me_beta = (m_e_from_beta - m_e_mev) / m_e_mev

    e0_a = 1.0
    e0_b = 7.3
    lambda_e_hat = r_e * r_e
    lambda_mu_hat = r_mu * r_mu
    ratio_a = (e0_a * math.sqrt(lambda_mu_hat)) / (e0_a * math.sqrt(lambda_e_hat))
    ratio_b = (e0_b * math.sqrt(lambda_mu_hat)) / (e0_b * math.sqrt(lambda_e_hat))

    lines = [
        "---",
        'title: "Output — metrological calibration"',
        "---",
        "",
        "# Output — metrological calibration",
        "",
        "## 1. Scale-independent Ratio",
        "",
        "| scale $E_0$ | reconstructed $M_\\mu/M_e$ |",
        "|---:|---:|",
        f"| `{e0_a:.6f}` | `{ratio_a:.12f}` |",
        f"| `{e0_b:.6f}` | `{ratio_b:.12f}` |",
        "",
        "The ratio does not change when the dimensional ruler is changed.",
        "",
        "## 2. Calibration by $M_e$",
        "",
        "| quantity | value |",
        "|---|---:|",
        f"| $M_e$ used as metrological standard | `{m_e_mev:.11f}` MeV |",
        f"| $R_\\mu^{{\\rm GDQ}}$ | `{r_mu:.12f}` |",
        f"| $M_\\mu=M_eR_\\mu$ | `{m_mu_from_ratio:.9f}` MeV |",
        f"| posterior reference $M_\\mu$ | `{m_mu_ref:.9f}` MeV |",
        f"| relative error | `{err_mu:.12e}` |",
        "",
        "## 3. Beta Bridge as Calibration",
        "",
        "$$",
        "\\delta_B=\\ln(2\\pi^2)\\frac{3\\sqrt2}{5}.",
        "$$",
        "",
        "| quantity | value |",
        "|---|---:|",
        f"| $\\delta_B$ | `{delta_b:.12f}` |",
        f"| $(\\delta_B-1)M_e$ | `{q_beta_from_me:.9f}` MeV |",
        f"| comparative $Q_\\beta$ | `{q_beta_ref:.9f}` MeV |",
        f"| $M_e=Q_\\beta/(\\delta_B-1)$ | `{m_e_from_beta:.11f}` MeV |",
        f"| relative error of reconstructed $M_e$ | `{err_me_beta:.12e}` |",
        "",
        "## Classification",
        "",
        "Verification of metrological calibration. The script does not derive the MeV",
        "unit without dimensional input; it shows how pure geometric numbers become",
        "energies after a declared physical ruler.",
        "",
    ]

    out = Path(__file__).with_name("output_verify_metrological_calibration.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
