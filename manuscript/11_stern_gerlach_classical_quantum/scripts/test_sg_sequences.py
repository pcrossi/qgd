#!/usr/bin/env python3
"""
GDQ — Chapter 11 / Sequential Measurements

Goal:
    Test p(s'|s;b,a)=(1+s*s'*a·b)/2 for z and x axes.

Theoretical source:
    manuscript/11_stern_gerlach_classical_quantum/11.7 - Sequential measurements and axis incompatibility.md

Classification:
    Symbolic test of operational consistency.

Output:
    scripts/output_test_sg_sequences.md
"""

from __future__ import annotations

import numpy as np
from pathlib import Path


def prob(s: int, sp: int, a: np.ndarray, b: np.ndarray) -> float:
    return 0.5 * (1.0 + s * sp * float(np.dot(a, b)))


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_test_sg_sequences.md"

    z = np.array([0.0, 0.0, 1.0])
    x = np.array([1.0, 0.0, 0.0])

    p_z_to_z_plus = prob(+1, +1, z, z)
    p_z_to_x_plus = prob(+1, +1, z, x)
    p_z_to_x_minus = prob(+1, -1, z, x)
    p_x_to_z_plus = prob(+1, +1, x, z)
    p_x_to_z_minus = prob(+1, -1, x, z)

    text = f"""# Output — Stern--Gerlach sequences

Classification: symbolic test of operational consistency.

| sequence | probability |
|---|---:|
| z+ -> z+ | {p_z_to_z_plus:.12f} |
| z+ -> x+ | {p_z_to_x_plus:.12f} |
| z+ -> x- | {p_z_to_x_minus:.12f} |
| x+ -> z+ | {p_x_to_z_plus:.12f} |
| x+ -> z- | {p_x_to_z_minus:.12f} |

Interpretation: incompatible axes redefine the decomposition of the channels; the
apparatus does not reveal an absolute table of simultaneous values.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
