#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `avaliar hessiana anomalia` associada ao capítulo `16_fine_structure_zeeman_gminus2`.

GDQ — Capítulo 16 / Hessiana operacional da anomalia.

Testa o bloco líder:

    H = [[1, -1], [-1, 2*pi/alpha]]
    c = (1, 0)
    m_perp = (0, 1)

e verifica:

    <c,H^-1 m_perp>/<c,H^-1 c> = alpha/(2*pi)

Este é um teste de consistência do operador reduzido; não é cálculo
metrológico completo dos canais superiores.
"""

from __future__ import annotations

import math
from pathlib import Path


def inverse_2x2(a: float, b: float, c: float, d: float) -> tuple[float, float, float, float]:
    det = a * d - b * c
    return d / det, -b / det, -c / det, a / det


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_avaliar_hessiana_anomalia.md"

    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    k1 = 2.0 * math.pi / alpha

    h00, h01, h10, h11 = 1.0, -1.0, -1.0, k1
    inv00, inv01, inv10, inv11 = inverse_2x2(h00, h01, h10, h11)

    numerator = inv01
    denominator = inv00
    ratio = numerator / denominator
    target = alpha / (2.0 * math.pi)
    eig_min_est = min(1.0, k1)  # lower diagnostic only; true eig is not needed.

    text = f"""# Saída — Hessiana operacional da anomalia

Classificação: teste de consistência do operador reduzido.

| quantidade | valor |
|---|---:|
| alpha^-1 | {alpha_inv:.12f} |
| K1 = 2*pi/alpha | {k1:.12e} |
| <c,H^-1 m_perp>/<c,H^-1 c> | {ratio:.15e} |
| alpha/(2*pi) | {target:.15e} |
| diferença | {ratio-target:.3e} |
| diagnóstico de positividade | {eig_min_est:.12e} |

Interpretação: o bloco líder reproduz $\\alpha/(2\\pi)$ por contração Hessiana
reduzida. Os canais superiores exigem uma Hessiana física maior.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
