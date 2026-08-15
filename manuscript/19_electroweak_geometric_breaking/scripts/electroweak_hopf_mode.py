#!/usr/bin/env python3
"""
Objective:
    Self-contained record of the `electroweak Hopf mode` verification associated with chapter `19_electroweak_geometric_breaking`.

GDQ — Chapter 19 / electroweak Hopf mode.

Verifies the reduced construction:

    u=(z1,z2)^T in S^3 subset C^2,
    u ~ (1,2)_{1/2},
    Q=T3+Y preserves u0=(0,1)^T.

Classification: reduced symbolic test; does not use experimental data.
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_electroweak_hopf_mode.md"

    t3 = 0.5 * np.array([[1.0, 0.0], [0.0, -1.0]])
    y = 0.5 * np.eye(2)
    q = t3 + y
    u0 = np.array([0.0, 1.0])

    t3_u0 = t3 @ u0
    y_u0 = y @ u0
    q_u0 = q @ u0
    laplace_eigenvalue_r1 = 3.0

    text = f"""# Output — electroweak Hopf mode

Classification: reduced symbolic test.

| quantity | value |
|---|---:|
| T3 on u0 | {t3_u0[1]:.12f} |
| Y on u0 | {y_u0[1]:.12f} |
| Q=T3+Y on u0 | {q_u0[1]:.12e} |
| eigenvalue -Delta_S3 for R=1 | {laplace_eigenvalue_r1:.12f} |

Interpretation: the Hopf doublet realizes $(1,2)_{{1/2}}$ and the choice
u0=(0,1)^T exactly preserves $Q=T_3+Y$.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
