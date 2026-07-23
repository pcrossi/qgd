#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `matriz massas neutra` associada ao capítulo `19_electroweak_geometric_breaking`.

GDQ — Capítulo 19 / matriz neutra.

Diagonaliza:

    M0^2 = (v^2/4) [[g^2,-g g'],[-g g',g'^2]]

para verificar que um autovalor é zero (fóton) e o outro é mZ^2.

Classificação: teste de consistência estrutural.
"""

from __future__ import annotations

from pathlib import Path
import math
import numpy as np


def couplings(alpha_inv: float, sin2: float) -> tuple[float, float, float]:
    alpha = 1.0 / alpha_inv
    e = math.sqrt(4.0 * math.pi * alpha)
    s = math.sqrt(sin2)
    c = math.sqrt(1.0 - sin2)
    return e / s, e / c, e


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_matriz_massas_neutra.md"

    v = 246.111195996
    alpha_inv = 137.035999
    sin2 = 3.0 / 8.0
    g, gp, e = couplings(alpha_inv, sin2)
    mat = (v * v / 4.0) * np.array([[g * g, -g * gp], [-g * gp, gp * gp]])
    vals = np.linalg.eigvalsh(mat)
    m_gamma = math.sqrt(max(vals[0], 0.0))
    m_z = math.sqrt(vals[1])
    det = np.linalg.det(mat)

    text = f"""# Saída — matriz neutra

Classificação: teste de consistência estrutural.

| quantidade | valor |
|---|---:|
| alpha_inv | {alpha_inv:.6f} |
| sin2_theta | {sin2:.12f} |
| g | {g:.12f} |
| g_prime | {gp:.12f} |
| e | {e:.12f} |
| det M0^2 | {det:.12e} |
| m_gamma GeV | {m_gamma:.12e} |
| m_Z GeV | {m_z:.6f} |

Interpretação: o determinante nulo expressa o gerador preservado $Q=T_3+Y$.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
