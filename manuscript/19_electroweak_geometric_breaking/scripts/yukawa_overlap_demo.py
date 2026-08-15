#!/usr/bin/env python3
"""
GDQ — Chapter 19 / Yukawa as overlap.

Objective:
    Demonstrates in an orthonormal basis model that an effective mass matrix
    comes from overlaps:

        Y_ij = <psi_L_i, Phi_EW psi_R_j>.

    Does not calculate real CKM/PMNS; it only documents the structure that replaces
    fundamental Yukawas.

Classification: didactic symbolic script.
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_yukawa_overlap_demo.md"

    # Toy orthonormal basis; Phi_EW acts as a geometric mixing operator.
    phi = np.array(
        [
            [1.0, 0.12, 0.01],
            [0.12, 0.35, 0.04],
            [0.01, 0.04, 0.08],
        ]
    )
    # Symmetrization to represent a real reduced Hessian/overlap.
    y_geom = 0.5 * (phi + phi.T)
    eig = np.linalg.eigvalsh(y_geom)

    text = f"""# Output — Yukawa as geometric overlap

Classification: didactic symbolic script.

Reduced overlap matrix:

| i | y_i |
|---|---:|
| 1 | {eig[0]:.12f} |
| 2 | {eig[1]:.12f} |
| 3 | {eig[2]:.12f} |

Interpretation: the effective matrix comes from mode overlaps. The numbers in this
script are toy and do not serve as a prediction; the goal is to establish the
form $Y_{{ij}}^{{geom}}=<\\psi_L,\\Phi_{{EW}}\\psi_R>$.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
