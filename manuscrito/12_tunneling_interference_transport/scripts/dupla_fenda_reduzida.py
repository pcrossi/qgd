#!/usr/bin/env python3
"""
GDQ — Capítulo 12 / Dupla fenda reduzida

Objetivo:
    Calcular um padrão de duas gaussianas coerentes e a mistura incoerente.

Fonte teórica:
    manuscrito/12_tunneling_interference_transport/notes/dupla_fenda_madelung_fundo_fixo.md

Classificação:
    Redução efetiva Madelung/paraxial. Não é Hessiana completa da ação oficial.

Saída:
    scripts/saida_dupla_fenda_reduzida.md
"""

from __future__ import annotations

import numpy as np
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_dupla_fenda_reduzida.md"

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

    text = f"""# Saída — dupla fenda reduzida

Classificação: redução efetiva Madelung/paraxial.

| quantidade | valor |
|---|---:|
| norma coerente trapezoidal | {norm_coh:.12f} |
| norma incoerente trapezoidal | {norm_inc:.12f} |
| visibilidade bruta coerente | {visibility:.12f} |
| mínimo coerente | {coherent.min():.12e} |
| máximo coerente | {coherent.max():.12e} |

Interpretação: o script apenas ilustra o padrão reduzido de duas contribuições.
O diferencial GDQ entra na leitura de densidade/fase e no detector por
impedância.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
