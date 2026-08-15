#!/usr/bin/env python3
"""
GDQ — Chapter 12 / Reduced double slit

Objective:
    Calculate a pattern of two coherent Gaussians and the incoherent mixture.

Theoretical source:
    manuscript/12_tunneling_interference_transport/notes/double_slit_madelung_fixed_background.md

Classification:
    Madelung/paraxial effective reduction. It is not the complete Hessian of the official action.

Output:
    scripts/output_reduced_double_slit.md
"""

from __future__ import annotations

import numpy as np
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_reduced_double_slit.md"

    x = np.linspace(-6, 6, 2001)
    sigma = 1.2
    d = 2.0
    k = 7.0
    I1 = np.exp(-((x - d / 2) ** 2) / (2 * sigma**2))
    I2 = np.exp(-((x + d / 2) ** 2) / (2 * sigma**2))
    phase = k * x
    coherent = I1 + I2 + 2 * np.sqrt(I1 * I2) * np.cos(phase)
    incoherent = I1 + I2
    coherent = np.clip(coherent, 0, None)
    visibility = (coherent.max() - coherent.min()) / (coherent.max() + coherent.min())
    norm_coh = np.trapezoid(coherent, x)
    norm_inc = np.trapezoid(incoherent, x)

    text = f"""# Output — reduced double slit

Classification: Madelung/paraxial effective reduction.

| quantity | value |
|---|---:|
| coherent trapezoidal norm | {norm_coh:.12f} |
| incoherent trapezoidal norm | {norm_inc:.12f} |
| raw coherent visibility | {visibility:.12f} |
| coherent minimum | {coherent.min():.12e} |
| coherent maximum | {coherent.max():.12e} |

Interpretation: the script only illustrates the reduced pattern of two contributions. The GDQ differential enters in the density/phase interpretation and the detector via impedance.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
