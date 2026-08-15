#!/usr/bin/env python3
"""
GDQ — Chapter 13 / Ideal Aharonov--Bohm

Objective:
    Calculate the ideal AB phase Delta phi = q Phi/(hbar c). In SI units,
    for the electron, the phase can be written as 2*pi*Phi/Phi0, where
    Phi0=h/e is the AB flux quantum.

Theoretical source:
    manuscript/13_holonomies_ab_sagnac/notes/ab_holonomy_by_mayer_vietoris_patches.md

Classification:
    Direct evaluation of ideal holonomy. Does not include a real solenoid.

Output:
    scripts/output_ab_ideal_phase.md
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_ab_ideal_phase.md"

    h = 6.62607015e-34
    e = 1.602176634e-19
    phi0 = h / e
    fractions = [0.0, 0.25, 0.5, 1.0, 2.0]

    rows = []
    for f in fractions:
        phase = 2.0 * math.pi * f
        hol_re = math.cos(phase)
        hol_im = math.sin(phase)
        rows.append((f, phase, hol_re, hol_im))

    table = "\n".join(
        f"| {f:.2f} | {phase:.12f} | {re:.12f} | {im:.12e} |"
        for f, phase, re, im in rows
    )

    text = f"""# Output — ideal AB phase

Classification: direct evaluation of ideal holonomy.

Used flux quantum:

$$
\\Phi_0=h/e={phi0:.12e}\\,\\mathrm{{Wb}}.
$$

| Phi/Phi0 | Delta phi rad | Re(Hol) | Im(Hol) |
|---:|---:|---:|---:|
{table}

Interpretation: the phase depends only on the ideal holonomy of the enclosed flux.
Real solenoid corrections do not enter this script.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
