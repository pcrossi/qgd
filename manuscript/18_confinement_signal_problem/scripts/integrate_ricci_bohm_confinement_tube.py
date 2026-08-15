#!/usr/bin/env python3
"""
Objective:
    Register in a self-contained way the verification `integrate ricci bohm confinement tube` associated with chapter `18_confinement_signal_problem`.

GDQ — Chapter 18 / direct integration of the Ricci--Bohm tube.

Calculates:

    sigma = ∫_0^r 2*pi*s ds * hbarc/r^4 = pi*hbarc/r^2
    Delta = hbarc/r

Classification: direct evaluation of reduced tension.
"""

from __future__ import annotations

from pathlib import Path
import math


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_integrate_ricci_bohm_confinement_tube.md"

    hbarc = 0.1973269804
    r = 0.86
    area = math.pi * r * r
    delta = hbarc / r
    sigma = math.pi * hbarc / (r * r)
    gev2 = sigma * hbarc

    text = f"""# Output — Ricci-Bohm tube

Classification: direct evaluation of the reduced tension.

| quantity | value |
|---|---:|
| r_perp fm | {r:.12f} |
| area fm^2 | {area:.12f} |
| Delta GeV | {delta:.12f} |
| sigma GeV/fm | {sigma:.12f} |
| sigma GeV^2 | {gev2:.12f} |
| sqrt(sigma GeV^2) GeV | {math.sqrt(gev2):.12f} |

Interpretation: the factor pi comes from the transverse circular integral.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
