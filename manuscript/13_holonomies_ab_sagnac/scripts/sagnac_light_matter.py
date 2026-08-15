#!/usr/bin/env python3
"""
GDQ — Chapter 13 / Ideal Sagnac

Objective:
    Calculate Delta t, optical phase and matter phase for a rotating circuit.

Theoretical source:
    manuscript/13_holonomies_ab_sagnac/notes/sagnac_clock_form.md

Classification:
    Direct ideal evaluation. Does not include real fiber, dispersion or losses.

Output:
    scripts/output_sagnac_light_matter.md
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_sagnac_light_matter.md"

    c = 299_792_458.0
    hbar = 1.054571817e-34
    omega = 7.2921150e-5
    area = 1.0
    wavelength = 632.8e-9
    mass_neutron = 1.67492749804e-27

    dt = 4.0 * omega * area / c**2
    phase_light = 8.0 * math.pi * omega * area / (wavelength * c)
    phase_matter = 4.0 * mass_neutron * omega * area / hbar

    text = f"""# Output — Sagnac light and matter

Classification: direct ideal evaluation.

Example parameters:

| parameter | value |
|---|---:|
| Omega | {omega:.12e} rad/s |
| area | {area:.12e} m^2 |
| optical lambda | {wavelength:.12e} m |
| neutron mass | {mass_neutron:.12e} kg |

Results:

| quantity | value |
|---|---:|
| Delta t Sag | {dt:.12e} s |
| optical phase | {phase_light:.12e} rad |
| matter phase | {phase_matter:.12e} rad |

Interpretation: Sagnac measures clock/rotating boundary holonomy, not AB electromagnetic holonomy.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
