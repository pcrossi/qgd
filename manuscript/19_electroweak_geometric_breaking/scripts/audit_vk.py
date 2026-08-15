#!/usr/bin/env python3
"""
Objective:
    Self-contained record of the `audit vk` verification associated with chapter `19_electroweak_geometric_breaking`.

GDQ — Chapter 19 / audit of the auxiliary scale v_K.

Calculates:

    v_K = M_e/alpha * (1 - 3/(4*pi^2))^{-1/2}

to demonstrate that this expression yields a MeV scale, not 246 GeV.

Classification: numerical/dimensional audit.
"""

from __future__ import annotations

from pathlib import Path
import math


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_audit_vk.md"

    me_mev = 0.51099895
    alpha_inv = 137.035999
    alpha = 1.0 / alpha_inv
    factor = (1.0 - 3.0 / (4.0 * math.pi**2)) ** -0.5
    vk_mev = me_mev / alpha * factor
    vk_gev = vk_mev / 1000.0
    v_ew = 246.111195996

    text = f"""# Output — audit of v_K

Classification: numerical/dimensional audit.

| quantity | value |
|---|---:|
| M_e MeV | {me_mev:.8f} |
| alpha_inv | {alpha_inv:.6f} |
| geometric factor | {factor:.12f} |
| v_K MeV | {vk_mev:.6f} |
| v_K GeV | {vk_gev:.9f} |
| v_EW used GeV | {v_ew:.12f} |

Interpretation: $v_K$ is a low-energy auxiliary scale; it is not the electroweak
scale.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
