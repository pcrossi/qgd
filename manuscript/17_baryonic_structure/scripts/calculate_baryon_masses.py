#!/usr/bin/env python3
"""
Objective:
    Self-contained record of the verification `calculate_baryon_masses` associated with chapter `17_baryonic_structure`.

GDQ — Chapter 17 / reduced baryon masses.

Calculates:

    Mp/Me = 6*pi^5 + alpha*(3*pi/2 + 3/(4*pi^3))
    Mn/Me = Mp/Me + ln(2*pi^2)*(3*sqrt(2)/5)

Classification: direct evaluation of currently active reduced formulas of baryonic structure.
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_calculate_baryon_masses.md"

    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    bulk = 6.0 * math.pi**5
    surface = alpha * (3.0 * math.pi / 2.0 + 3.0 / (4.0 * math.pi**3))
    mp_me = bulk + surface
    delta_b = math.log(2.0 * math.pi**2) * (3.0 * math.sqrt(2.0) / 5.0)
    mn_me = mp_me + delta_b

    ref_mp_me = 1836.15267343
    ref_mn_me = 1838.68366173
    err_p = (mp_me - ref_mp_me) / ref_mp_me
    err_n = (mn_me - ref_mn_me) / ref_mn_me

    text = f"""# Output — reduced baryon masses

Classification: direct evaluation of currently active reduced formulas.

| quantity | value |
|---|---:|
| alpha^-1 | {alpha_inv:.12f} |
| bulk 6*pi^5 | {bulk:.12f} |
| torsional surface | {surface:.12f} |
| Mp/Me GDQ | {mp_me:.12f} |
| delta_B | {delta_b:.12f} |
| Mn/Me GDQ | {mn_me:.12f} |

## Phenomenological comparison

| ratio | GDQ | reference used | relative error |
|---|---:|---:|---:|
| Mp/Me | {mp_me:.12f} | {ref_mp_me:.12f} | {err_p:.12e} |
| Mn/Me | {mn_me:.12f} | {ref_mn_me:.12f} | {err_n:.12e} |

Interpretation: the dominant mass is reduced baryonic volume; the fine difference
comes from the torsional surface and the antiparallel shear of the neutron.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
