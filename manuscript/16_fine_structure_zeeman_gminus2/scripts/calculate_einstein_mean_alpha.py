#!/usr/bin/env python3
"""
Objective:
    Self-contained verification script for `calculate einstein mean alpha` associated with chapter `16_fine_structure_zeeman_gminus2`.

QGD — Chapter 16 / alpha as Einstein mean.

This script evaluates the geometric expression

    alpha_E = 9/(8*pi^4) * (pi^5/1920)^(1/4)

without using the experimental value of alpha. The classification is direct evaluation of
an already derived quantity in the isotropic mean/Hessian of the fine structure by isotropic mean/Hessian.
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_einstein_mean_alpha.md"

    p_iso = 9.0 / (8.0 * math.pi**4)
    c_e = (math.pi**5 / 1920.0) ** 0.25
    alpha = p_iso * c_e
    z_q = 1.0 / (4.0 * math.pi * alpha)

    text = f"""# Output — alpha as Einstein mean

Classification: direct evaluation of already derived quantity; does not use CODATA.

| quantity | value |
|---|---:|
| P_iso | {p_iso:.15e} |
| C_E | {c_e:.15e} |
| alpha_E_mean | {alpha:.15e} |
| alpha_E_mean^-1 | {1.0/alpha:.12f} |
| Z_Q = 1/(4*pi*alpha) | {z_q:.12f} |

Interpretation: the value is the global isotropic mean of the electromagnetic channel in the
Einstein cosmological space, inherited by the laboratory under the global-local bridge.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
