#!/usr/bin/env python3
"""
GDQ — Capítulo 15 / Koide como saturação geométrica

Objetivo:
    Verificar que a condição ||A_perp||^2=||A_parallel||^2 equivale a Q=2/3
    e calcular os dois ramos da terceira ressonância a partir de R_e e R_mu.

Classificação:
    Teste simbólico-numérico reduzido. Não usa M_tau como entrada.

Saída:
    scripts/saida_koide_saturacao.md
"""

from __future__ import annotations

import math
from pathlib import Path


def q_value(*ratios: float) -> float:
    amps = [math.sqrt(r) for r in ratios]
    return sum(ratios) / (sum(amps) ** 2)


def branches(r1: float, r2: float) -> tuple[float, float]:
    x = math.sqrt(r1)
    y = math.sqrt(r2)
    rad = math.sqrt(3.0 * r1 + 12.0 * math.sqrt(r1 * r2) + 3.0 * r2)
    return (2.0 * (x + y) - rad) ** 2, (2.0 * (x + y) + rad) ** 2


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_koide_saturacao.md"

    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    r_e = 1.0
    r_mu = 1.5 * alpha_inv + 6.0 / 5.0 + 2.0 * alpha
    r_minus, r_plus = branches(r_e, r_mu)
    q_minus = q_value(r_e, r_mu, r_minus)
    q_plus = q_value(r_e, r_mu, r_plus)

    text = f"""# Saída — Koide como saturação geométrica

Classificação: teste simbólico-numérico reduzido.

| ramo | R_3 | Q |
|---|---:|---:|
| leve | {r_minus:.12f} | {q_minus:.12f} |
| pesado | {r_plus:.12f} | {q_plus:.12f} |

Valor alvo geométrico:

$$
Q=\\frac23={2.0/3.0:.12f}.
$$

Interpretação: os dois ramos satisfazem a mesma condição angular. O capítulo
usa o ramo pesado para o tau carregado porque é o ramo estável do tripleto
carregado; o ramo leve permanece sem interpretação física até Hessiana própria.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
