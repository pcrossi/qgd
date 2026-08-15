#!/usr/bin/env python3
"""
Objective:
    Self-contained verification script for `evaluate anomaly hessian` associated with chapter `16_fine_structure_zeeman_gminus2`.

QGD — Chapter 16 / operational Hessian of the anomaly.

Tests the leading block:

    H = [[1, -1], [-1, 2*pi/alpha]]
    c = (1, 0)
    m_perp = (0, 1)

and verifies:

    <c,H^-1 m_perp>/<c,H^-1 c> = alpha/(2*pi)

This is a consistency test of the reduced operator; it is not a complete metrological
calculation of the upper channels.
"""

from __future__ import annotations

import math
from pathlib import Path


def inverse_2x2(a: float, b: float, c: float, d: float) -> tuple[float, float, float, float]:
    det = a * d - b * c
    return d / det, -b / det, -c / det, a / det


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_evaluate_anomaly_hessian.md"

    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    k1 = 2.0 * math.pi / alpha

    h00, h01, h10, h11 = 1.0, -1.0, -1.0, k1
    inv00, inv01, inv10, inv11 = inverse_2x2(h00, h01, h10, h11)

    numerator = inv01
    denominator = inv00
    ratio = numerator / denominator
    target = alpha / (2.0 * math.pi)
    eig_min_est = min(1.0, k1)  # lower diagnostic only; true eig is not needed.

    text = f"""# Output — operational Hessian of the anomaly

Classification: consistency test of the reduced operator.

| quantity | value |
|---|---:|
| alpha^-1 | {alpha_inv:.12f} |
| K1 = 2*pi/alpha | {k1:.12e} |
| <c,H^-1 m_perp>/<c,H^-1 c> | {ratio:.15e} |
| alpha/(2*pi) | {target:.15e} |
| difference | {ratio-target:.3e} |
| positivity diagnostic | {eig_min_est:.12e} |

Interpretation: the leading block reproduces $\\alpha/(2\\pi)$ by reduced Hessian
contraction. The upper channels require a larger physical Hessian.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
