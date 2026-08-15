#!/usr/bin/env python3
"""
GDQ — Chapter 15 / Koide as geometric saturation

Objective:
    Verify that the condition ||A_perp||^2=||A_parallel||^2 is equivalent to Q=2/3
    and calculate the two branches of the third resonance from R_e and R_mu.

Classification:
    Reduced symbolic-numerical test. Does not use M_tau as input.

Output:
    scripts/output_koide_saturation.md
"""

from __future__ import annotations

import math
from pathlib import Path


def q_value(*ratios: float) -> float:
    amps = [math.sqrt(r) for r in ratios]
    return sum(ratios) / (sum(amps) ** 2)


def branches(r1: float, r2: float) -> tuple[float, float]:
    x = math.sqrt(r1)
    y = math.sqrt(r2)
    rad = math.sqrt(3.0 * r1 + 12.0 * math.sqrt(r1 * r2) + 3.0 * r2)
    return (2.0 * (x + y) - rad) ** 2, (2.0 * (x + y) + rad) ** 2


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_koide_saturation.md"

    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    r_e = 1.0
    r_mu = 1.5 * alpha_inv + 6.0 / 5.0 + 2.0 * alpha
    r_minus, r_plus = branches(r_e, r_mu)
    q_minus = q_value(r_e, r_mu, r_minus)
    q_plus = q_value(r_e, r_mu, r_plus)

    text = f"""# Output — Koide as geometric saturation

Classification: reduced symbolic-numerical test.

| branch | R_3 | Q |
|---|---:|---:|
| light | {r_minus:.12f} | {q_minus:.12f} |
| heavy | {r_plus:.12f} | {q_plus:.12f} |

Geometric target value:

$$
Q=\\frac23={2.0/3.0:.12f}.
$$

Interpretation: both branches satisfy the same angular condition. The chapter
uses the heavy branch for the charged tau because it is the stable branch of the
charged triplet; the light branch remains without physical interpretation until a
proper Hessian is established.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
