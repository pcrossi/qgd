#!/usr/bin/env python3
"""
GDQ — Chapter 13 / Reduced COW estimation

Objective:
    Estimate Delta phi_COW = m g A/(hbar v) for matter interferometry.

Theoretical source:
    manuscript/13_holonomies_ab_sagnac/notes/cow_gravitational_interferometry.md

Classification:
    Reduced phenomenological estimation. It is not a metrological prediction of a
    real interferometer.

Output:
    scripts/output_reduced_cow_estimation.md
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_reduced_cow_estimation.md"

    hbar = 1.054571817e-34
    m_n = 1.67492749804e-27
    g = 9.80665
    area = 1.0e-4
    velocity = 2000.0

    phase = m_n * g * area / (hbar * velocity)

    text = f"""# Output — reduced COW estimation

Classification: reduced phenomenological estimation.

| parameter | value |
|---|---:|
| neutron mass | {m_n:.12e} kg |
| g | {g:.12e} m/s² |
| area | {area:.12e} m² |
| velocity | {velocity:.12e} m/s |

Result:

| quantity | value |
|---|---:|
| Delta phi COW | {phase:.12e} rad |

Interpretation: COW is treated here only as an interferometric extension of reduced gravitational phase.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
