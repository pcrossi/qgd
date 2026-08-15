#!/usr/bin/env python3
"""
GDQ — Chapter 15 / 8D Hessian and Schur complement

Objective:
    Verify the product closure J=0 and the warped/mixed criterion:

        H_eff = H_B - J H_perp^{-1} J^T

    The matrix is reduced and self-contained; it illustrates the Schur operator
    used in the text, without pretending to be the full metrological 8D background.

Classification:
    Consistency test of the reduced 8D Hessian.

Output:
    scripts/output_hessian_8d_schur.md
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


def schur(h_b: np.ndarray, h_perp: np.ndarray, j: np.ndarray) -> np.ndarray:
    return h_b - j @ np.linalg.solve(h_perp, j.T)


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_hessian_8d_schur.md"

    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    r_mu = 1.5 * alpha_inv + 6.0 / 5.0 + 2.0 * alpha
    h_b = np.diag([1.0, r_mu, 3477.446405098381])

    h_perp = np.eye(3)
    j_product = np.zeros((3, 3))
    h_eff_product = schur(h_b, h_perp, j_product)

    # Reduced warped/mixed: subcritical mixture of controlled norm.
    j_mix = 0.1 * np.eye(3)
    h_eff_mix = schur(h_b, h_perp, j_mix)
    correction_norm = float(np.linalg.norm(j_mix @ np.linalg.solve(h_perp, j_mix.T), 2))
    lambda_gap = 0.5
    criterion = correction_norm < lambda_gap

    text = f"""# Output — 8D Hessian by Schur

Classflow: consistency test of the reduced 8D Hessian.

## Product

| quantity | value |
|---|---:|
| ||J|| product | {np.linalg.norm(j_product):.12e} |
| max |H_eff-H_B| product | {np.max(np.abs(h_eff_product-h_b)):.12e} |

## Reduced Warped/Mixed

| quantity | value |
|---|---:|
| ||Sigma|| | {correction_norm:.12e} |
| lambda_gap | {lambda_gap:.12e} |
| subcritical | {criterion} |

Interpretation: in the exact product, $J=0$ and the reduced hierarchy is inherited without
correction. In a mixed sector, the correction is controlled by
$j_{{\\rm mix}}^2/m_\\perp^2$ and must be compared to the gap of the material block.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
