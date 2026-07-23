#!/usr/bin/env python3
"""
GDQ — Capítulo 11 / Deflexão reduzida de Stern--Gerlach

Objetivo:
    Calcular a separação geométrica dos dois canais em um modelo de ímã ideal.

Fonte teórica:
    manuscrito/11_stern_gerlach_classical_quantum/notes/forca_deflexao_sg_setor_reduzido.md

Classificação:
    Redução efetiva/aparelho. Parâmetros são dados clássicos do aparelho.

Saída:
    scripts/saida_simular_deflexao_sg.md
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_simular_deflexao_sg.md"

    mu_B = 9.2740100783e-24
    mass_ag = 1.790e-25
    L = 0.03
    vy = 500.0
    grad_B = 100.0

    dz = mu_B * L**2 * grad_B / (2 * mass_ag * vy**2)
    sep = 2 * dz

    text = f"""# Saída — deflexão reduzida Stern--Gerlach

Classificação: redução efetiva/aparelho.

Parâmetros de exemplo:

| parâmetro | valor |
|---|---:|
| momento magnético usado | {mu_B:.12e} J/T |
| massa efetiva do átomo | {mass_ag:.12e} kg |
| comprimento do ímã | {L:.12e} m |
| velocidade longitudinal | {vy:.12e} m/s |
| gradiente de campo | {grad_B:.12e} T/m |

Resultado:

| canal | deflexão |
|---|---:|
| + | {dz:.12e} m |
| - | {-dz:.12e} m |
| separação | {sep:.12e} m |

Interpretação: os valores são de aparelho idealizado. A fórmula valida a
redução de canal fixo; não é metrologia de um aparato real.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
