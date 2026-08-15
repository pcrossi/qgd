#!/usr/bin/env python3
"""
GDQ — Chapter 14 / Couplings as bundle norms

Objective:
    Calculate the ratios I_3, I_2, I_Y of a generation and extract:

        g_s = g,
        g'^2/g^2 = 3/5,
        sin^2(theta_W) = 3/8.

Classification:
    Direct evaluation of the geometric norms at the common matching point.

Output:
    scripts/output_couplings_norms.md
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_couplings_norms.md"

    alpha = 1.0 / 137.03599907
    e_charge = math.sqrt(4.0 * math.pi * alpha)

    # T(fundamental SU(N)) = 1/2.
    index_su3 = 2.0 * 0.5 + 0.5 + 0.5
    index_su2 = 3.0 * 0.5 + 0.5
    index_y = (
        6.0 * (1.0 / 6.0) ** 2
        + 3.0 * (-2.0 / 3.0) ** 2
        + 3.0 * (1.0 / 3.0) ** 2
        + 2.0 * (-1.0 / 2.0) ** 2
        + 1.0
    )

    ratio_gp2_g2 = index_su2 / index_y
    sin2 = ratio_gp2_g2 / (1.0 + ratio_gp2_g2)
    g = e_charge / math.sqrt(sin2)
    gp = e_charge / math.sqrt(1.0 - sin2)
    gs = g * math.sqrt(index_su2 / index_su3)

    assert math.isclose(index_su3, 2.0)
    assert math.isclose(index_su2, 2.0)
    assert math.isclose(index_y, 10.0 / 3.0)
    assert math.isclose(ratio_gp2_g2, 3.0 / 5.0)
    assert math.isclose(sin2, 3.0 / 8.0)
    assert math.isclose(gs, g)

    text = f"""# Output — couplings by bundle norms

Classification: direct evaluation of geometric norms.

| quantity | value |
|---|---:|
| I_3 | {index_su3:.12f} |
| I_2 | {index_su2:.12f} |
| I_Y | {index_y:.12f} |
| g'^2/g^2 | {ratio_gp2_g2:.12f} |
| sin²(theta_W) | {sin2:.12f} |
| alpha used for illustrative normalization | {alpha:.12e} |
| e | {e_charge:.12f} |
| g_s at the common point | {gs:.12f} |
| g at the common point | {g:.12f} |
| g' at the common point | {gp:.12f} |

Interpretation: the ratios $g_s=g$, $g'^2/g^2=3/5$ and
$\\sin^2\\theta_W=3/8$ follow from the generator norms in one generation. The
absolute normalization by $\\alpha$ is only the electromagnetic scale used
to express the numbers at the common point.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
