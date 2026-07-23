#!/usr/bin/env python3
"""
GDQ — Capítulo 15 / Tensão intrínseca leptônica

Objetivo:
    Calcular R_mu pela fórmula reduzida intrínseca:

        R_mu = (3/2) alpha^{-1} + 6/5 + 2 alpha

    e calcular R_tau pelo ramo pesado da condição de saturação tridimensional
    equivalente a Q=2/3.

Classificação:
    Avaliação direta da construção reduzida GDQ. Não usa M_mu nem M_tau como
    alvos de ajuste.

Saída:
    scripts/saida_tensao_intrinseca_mu_tau.md
"""

from __future__ import annotations

import math
from pathlib import Path


def koide_branches(r1: float, r2: float) -> tuple[float, float]:
    """Return the two R3 branches implied by Q=2/3."""

    x = math.sqrt(r1)
    y = math.sqrt(r2)
    radical = math.sqrt(3.0 * x * x + 12.0 * x * y + 3.0 * y * y)
    z_minus = 2.0 * (x + y) - radical
    z_plus = 2.0 * (x + y) + radical
    return z_minus * z_minus, z_plus * z_plus


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_tensao_intrinseca_mu_tau.md"

    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    r_e = 1.0
    r_mu = 1.5 * alpha_inv + 6.0 / 5.0 + 2.0 * alpha
    r_light, r_tau = koide_branches(r_e, r_mu)

    exp_mu = 206.768282700
    exp_tau = 3477.150000000
    err_mu = (r_mu - exp_mu) / exp_mu
    err_tau = (r_tau - exp_tau) / exp_tau

    text = f"""# Saída — tensão intrínseca leptônica

Classificação: avaliação direta da construção reduzida.

| quantidade | valor |
|---|---:|
| alpha^-1 | {alpha_inv:.12f} |
| alpha | {alpha:.12e} |
| R_e | {r_e:.12f} |
| R_mu GDQ | {r_mu:.12f} |
| R_tau ramo pesado GDQ | {r_tau:.12f} |
| ramo leve matemático | {r_light:.12f} |

## Comparação fenomenológica

| razão | GDQ | referência | erro relativo |
|---|---:|---:|---:|
| M_mu/M_e | {r_mu:.12f} | {exp_mu:.12f} | {err_mu:.12e} |
| M_tau/M_e | {r_tau:.12f} | {exp_tau:.12f} | {err_tau:.12e} |

Interpretação: $R_\\mu$ vem da tensão biespacial reduzida e $R_\\tau$ vem da
saturação tridimensional. O ramo leve é solução matemática da condição
angular, mas não é partícula sem Hessiana própria.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
