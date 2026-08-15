#!/usr/bin/env python3
"""
GDQ — Chapter 15 / Leptonic intrinsic tension

Objective:
    Calculate R_mu by the intrinsic reduced formula:

        R_mu = (3/2) alpha^{-1} + 6/5 + 2 alpha

    and calculate R_tau by the heavy branch of the three-dimensional saturation
    condition equivalent to Q=2/3.

Classification:
    Direct evaluation of the reduced GDQ construction. Does not use M_mu or M_tau as
    adjustment targets.

Output:
    scripts/output_intrinsic_tension_mu_tau.md
"""

from __future__ import annotations

import math
from pathlib import Path


def koide_branches(r1: float, r2: float) -> tuple[float, float]:
    """Return the two R3 branches implied by Q=2/3."""

    x = math.sqrt(r1)
    y = math.sqrt(r2)
    radical = math.sqrt(3.0 * x * x + 12.0 * x * y + 3.0 * y * y)
    z_minus = 2.0 * (x + y) - radical
    z_plus = 2.0 * (x + y) + radical
    return z_minus * z_minus, z_plus * z_plus


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_intrinsic_tension_mu_tau.md"

    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    r_e = 1.0
    r_mu = 1.5 * alpha_inv + 6.0 / 5.0 + 2.0 * alpha
    r_light, r_tau = koide_branches(r_e, r_mu)

    exp_mu = 206.768282700
    exp_tau = 3477.150000000
    err_mu = (r_mu - exp_mu) / exp_mu
    err_tau = (r_tau - exp_tau) / exp_tau

    text = f"""# Output — leptonic intrinsic tension

Classification: direct evaluation of the reduced construction.

| quantity | value |
|---|---:|
| alpha^-1 | {alpha_inv:.12f} |
| alpha | {alpha:.12e} |
| R_e | {r_e:.12f} |
| R_mu GDQ | {r_mu:.12f} |
| R_tau GDQ heavy branch | {r_tau:.12f} |
| mathematical light branch | {r_light:.12f} |

## Phenomenological Comparison

| ratio | GDQ | reference | relative error |
|---|---:|---:|---:|
| M_mu/M_e | {r_mu:.12f} | {exp_mu:.12f} | {err_mu:.12e} |
| M_tau/M_e | {r_tau:.12f} | {exp_tau:.12f} | {err_tau:.12e} |

Interpretation: $R_\\mu$ comes from the reduced bispatial tension and $R_\\tau$ comes from
three-dimensional saturation. The light branch is a mathematical solution of the
angular condition, but it is not a particle without its own Hessian.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
