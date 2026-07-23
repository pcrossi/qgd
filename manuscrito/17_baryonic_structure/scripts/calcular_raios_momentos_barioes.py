#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `calcular raios momentos barioes` associada ao capítulo `17_baryonic_structure`.

GDQ — Capítulo 17 / raio e momentos magnéticos reduzidos.

Calcula o raio de superfície do próton e os momentos magnéticos reduzidos:

    r_p = (1/8)*(1+alpha/4)*epsilon_eff*(3/2 Lambda_C)
    mu_p = 1 + (3/5) ln(2*pi^2)*(1+alpha/4)
    mu_n = -(3/4) delta_B*(1+alpha*3*sqrt(2)/4)

Classificação: avaliação direta da redução de superfície estrutura bariônica.
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_calcular_raios_momentos_barioes.md"

    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    epsilon_eff = 0.011591040463
    lambda_c_fm = 386.159268
    c_r = (1.0 / 8.0) * (1.0 + alpha / 4.0)
    r_b = 1.5 * lambda_c_fm
    r_p = c_r * epsilon_eff * r_b
    delta_b = math.log(2.0 * math.pi**2) * (3.0 * math.sqrt(2.0) / 5.0)
    mu_p = 1.0 + (3.0 / 5.0) * math.log(2.0 * math.pi**2) * (1.0 + alpha / 4.0)
    mu_n = -(3.0 / 4.0) * delta_b * (1.0 + alpha * 3.0 * math.sqrt(2.0) / 4.0)

    ref_rp = 0.8409
    ref_mup = 2.79284734463
    ref_mun = -1.91304273

    text = f"""# Saída — raio e momentos bariônicos

Classificação: avaliação direta da redução de superfície.

| quantidade | valor |
|---|---:|
| C_r | {c_r:.15e} |
| R_B fm | {r_b:.12f} |
| r_p fm | {r_p:.12f} |
| mu_p / mu_N | {mu_p:.12f} |
| mu_n / mu_N | {mu_n:.12f} |

## Comparação fenomenológica

| observável | GDQ | referência usada | erro relativo |
|---|---:|---:|---:|
| r_p fm | {r_p:.12f} | {ref_rp:.12f} | {(r_p-ref_rp)/ref_rp:.12e} |
| mu_p | {mu_p:.12f} | {ref_mup:.12f} | {(mu_p-ref_mup)/ref_mup:.12e} |
| mu_n | {mu_n:.12f} | {ref_mun:.12f} | {(mu_n-ref_mun)/ref_mun:.12e} |

Interpretação: esses valores pertencem à redução de superfície. A metrologia
fina exige Hessiana de superfície completa e resposta de sonda.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
