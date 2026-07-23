#!/usr/bin/env python3
"""
GDQ — Capítulo 13 / Estimativa COW reduzida

Objetivo:
    Estimar Delta phi_COW = m g A/(hbar v) para interferometria de matéria.

Fonte teórica:
    manuscrito/13_holonomies_ab_sagnac/notes/cow_interferometria_gravitacional.md

Classificação:
    Estimativa fenomenológica reduzida. Não é previsão metrológica de um
    interferômetro real.

Saída:
    scripts/saida_cow_estimativa_reduzida.md
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_cow_estimativa_reduzida.md"

    hbar = 1.054571817e-34
    m_n = 1.67492749804e-27
    g = 9.80665
    area = 1.0e-4
    velocity = 2000.0

    phase = m_n * g * area / (hbar * velocity)

    text = f"""# Saída — estimativa COW reduzida

Classificação: estimativa fenomenológica reduzida.

| parâmetro | valor |
|---|---:|
| massa nêutron | {m_n:.12e} kg |
| g | {g:.12e} m/s² |
| área | {area:.12e} m² |
| velocidade | {velocity:.12e} m/s |

Resultado:

| quantidade | valor |
|---|---:|
| Delta phi COW | {phase:.12e} rad |

Interpretação: COW é tratado aqui apenas como extensão interferométrica de
fase gravitacional reduzida.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
