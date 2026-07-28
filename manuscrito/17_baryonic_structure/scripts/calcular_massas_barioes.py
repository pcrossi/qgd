#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `calcular massas barioes` associada ao capítulo `17_baryonic_structure`.

GDQ — Capítulo 17 / massas bariônicas reduzidas.

Calcula:

    Mp/Me = 6*pi^5 + alpha*(3*pi/2 + 3/(4*pi^3))
    Mn/Me = Mp/Me + ln(2*pi^2)*(3*sqrt(2)/5)

Classificação: avaliação direta de fórmulas condicionais do modelo reduzido.
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_calcular_massas_barioes.md"

    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    bulk = 6.0 * math.pi**5
    surface = alpha * (3.0 * math.pi / 2.0 + 3.0 / (4.0 * math.pi**3))
    mp_me = bulk + surface
    delta_b = math.log(2.0 * math.pi**2) * (3.0 * math.sqrt(2.0) / 5.0)
    mn_me = mp_me + delta_b

    # CODATA 2022; não entram na construção das fórmulas.
    ref_mp_me = 1836.152673426
    ref_mn_me = 1838.68366200
    err_p = (mp_me - ref_mp_me) / ref_mp_me
    err_n = (mn_me - ref_mn_me) / ref_mn_me

    text = f"""# Saída — massas bariônicas reduzidas

Classificação: avaliação direta de fórmulas condicionais do modelo reduzido.

| quantidade | valor |
|---|---:|
| alpha^-1 | {alpha_inv:.12f} |
| bulk 6*pi^5 | {bulk:.12f} |
| superfície torsional | {surface:.12f} |
| Mp/Me GDQ | {mp_me:.12f} |
| delta_B | {delta_b:.12f} |
| Mn/Me GDQ | {mn_me:.12f} |

## Comparação fenomenológica

| razão | GDQ | referência usada | erro relativo |
|---|---:|---:|---:|
| Mp/Me | {mp_me:.12f} | {ref_mp_me:.12f} | {err_p:.12e} |
| Mn/Me | {mn_me:.12f} | {ref_mn_me:.12f} | {err_n:.12e} |

Interpretação: fixadas as hipóteses geométricas da redução, a massa dominante
é volume bariônico e a diferença fina vem da superfície torsional e do
cisalhamento antiparalelo. A sela 8D completa ainda deve selecionar os
coeficientes usados.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
