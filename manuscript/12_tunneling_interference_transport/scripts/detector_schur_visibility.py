#!/usr/bin/env python3
"""
GDQ — Chapter 12 / Schur detector and visibility

Objective:
    Evaluate R_det=lambda*coth(lambda*L), Gamma_det and exp(-Gamma_det).

Theoretical source:
    manuscript/12_tunneling_interference_transport/notes/detector_dtn_schur_visibility.md

Classification:
    Effective reduction/apparatus. It is not real material detector metrology.

Output:
    scripts/output_detector_schur_visibility.md
"""

from __future__ import annotations

import math
from pathlib import Path


def coth(x: float) -> float:
    return math.cosh(x) / math.sinh(x)


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_detector_schur_visibility.md"

    lam = 1.3
    L = 1.0
    r_det = lam * coth(lam * L)
    zetas = [0.0, 0.5, 1.0, 2.0, 4.0]
    rows = []
    for zeta in zetas:
        gamma = 0.5 * r_det * zeta**2
        c = math.exp(-gamma)
        rows.append((zeta, gamma, c))

    table = "\n".join(f"| {z:.3f} | {g:.12f} | {c:.12f} |" for z, g, c in rows)

    text = f"""# Output — Schur detector and visibility

Classification: effective reduction/apparatus.

Parameters:

- lambda = `{lam}`
- L = `{L}`
- R_det = `{r_det:.12f}`

| zeta_det | Gamma_det | exp(-Gamma_det) |
|---:|---:|---:|
{table}

Interpretation: the coherence of the cross-term decays monotonically with the quadratic cost of path distinguishing.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
