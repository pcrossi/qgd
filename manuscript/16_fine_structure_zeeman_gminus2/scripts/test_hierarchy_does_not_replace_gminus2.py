#!/usr/bin/env python3
"""
QGD — Chapter 16 / leptonic hierarchy does not replace g-2.

Tests the bad reduced hypothesis:

    residual_l ∝ 1/R_l

normalized by the electron residual. The objective is to record, in a clean way,
that the leptonic hierarchy provides the background, but not the complete magnetic
transverse source.
"""

from __future__ import annotations

import math
from pathlib import Path


def koide_branches(r1: float, r2: float) -> tuple[float, float]:
    x = math.sqrt(r1)
    y = math.sqrt(r2)
    rad = math.sqrt(3.0 * r1 + 12.0 * math.sqrt(r1 * r2) + 3.0 * r2)
    return (2.0 * (x + y) - rad) ** 2, (2.0 * (x + y) + rad) ** 2


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_test_hierarchy_does_not_replace_gminus2.md"

    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    a1 = alpha / (2.0 * math.pi)
    r_mu = 1.5 * alpha_inv + 6.0 / 5.0 + 2.0 * alpha
    _, r_tau = koide_branches(1.0, r_mu)

    a_e_obs = 2.002319304361180 / 2.0 - 1.0
    a_mu_obs = 116592059e-11
    resid_e = a_e_obs - a1
    resid_mu = a_mu_obs - a1
    pred_mu = resid_e / r_mu
    pred_tau = resid_e / r_tau

    text = f"""# Output — hierarchy does not replace g-2

Classification: diagnostic of non-replacement.

| quantity | value |
|---|---:|
| R_mu leptonic hierarchy | {r_mu:.12f} |
| R_tau leptonic hierarchy | {r_tau:.12f} |
| a1 | {a1:.15e} |
| electron residual | {resid_e:.15e} |
| observed muon residual | {resid_mu:.15e} |
| muon residual by 1/R_mu | {pred_mu:.15e} |
| predicted/observed ratio | {pred_mu/resid_mu:.15e} |
| tau residual by 1/R_tau | {pred_tau:.15e} |

Interpretation: the mass/hierarchy scale does not by itself determine the anomaly.
The physical calculation needs $H_{{C,\\ell}}^+m_{{\\perp,\\ell}}$.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
