#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `potencial quartico eletrofraco` associada ao capítulo `19_electroweak_geometric_breaking`.

GDQ — Capítulo 19 / potencial quartico eletrofraco.

Avalia os coeficientes consolidados:

    a2 < 0          instabilidade eletrofraca;
    a4_total > 0   estabilização por interface a volume fixo;
    beta_*         mínimo adimensional.

Classificação: avaliação direta de quantidades já derivadas no setor eletrofraco.
"""

from __future__ import annotations

from pathlib import Path
import math


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_potencial_quartico_eletrofraco.md"

    alpha_inv = 137.035999
    alpha = 1.0 / alpha_inv
    R = 1.998411184770
    b0 = 1.0 / (math.pi * R**3)
    s_surface = alpha * (1.5 * math.pi + 3.0 / (4.0 * math.pi**3))
    a4_surface = 5.0 * s_surface / (32.0 * b0**4)
    a4_bulk = -0.805755288
    a4_total = a4_surface + a4_bulk
    a2 = -0.253196676
    beta_star = math.sqrt(-a2 / a4_total)
    epsilon_star = beta_star / b0

    text = f"""# Saída — potencial quartico eletrofraco

Classificação: avaliação direta de quantidade derivada.

| quantidade | valor |
|---|---:|
| alpha usado | {alpha:.15f} |
| R | {R:.12f} |
| b0 | {b0:.12f} |
| S_surface | {s_surface:.12f} |
| a4_surface | {a4_surface:.6f} |
| a4_bulk | {a4_bulk:.9f} |
| a4_total | {a4_total:.6f} |
| a2 | {a2:.9f} |
| beta_star | {beta_star:.10f} |
| epsilon_star | {epsilon_star:.9f} |

Interpretação: a torção de bulk fornece $a_2<0$; a interface a volume fixo
fornece $a_4>0$ e estabiliza o modo.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
