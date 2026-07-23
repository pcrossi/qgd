#!/usr/bin/env python3
"""
GDQ — Capítulo 12 / Efeito Hartman reduzido

Objetivo
--------
Verificar numericamente a fórmula reduzida de saturação de comprimento próprio
no canal evanescente:

    D_prop(L) = sqrt(g0)/kappa * (1-exp(-kappa*L))

e o tempo próprio efetivo:

    tau_GDQ(L) = D_prop(L)/v0.

Classificação
-------------
Avaliação direta de fórmula reduzida. Nenhum alvo experimental é usado.
Não é evolução da métrica completa GDQ.

Saída
-----
saida_hartman_saturacao_reduzida.md
"""

from __future__ import annotations

import math
from pathlib import Path


def d_prop(length: float, kappa: float, g0: float) -> float:
    """Comprimento próprio reduzido dentro da barreira."""

    return math.sqrt(g0) / kappa * (1.0 - math.exp(-kappa * length))


def tau_gdq(length: float, kappa: float, g0: float, v0: float) -> float:
    """Tempo próprio efetivo para velocidade física local v0."""

    return d_prop(length, kappa, g0) / v0


def main() -> None:
    out = Path(__file__).with_name("saida_hartman_saturacao_reduzida.md")

    kappa = 1.0
    g0 = 1.0
    v0 = 1.0
    lengths = [0.1, 0.5, 1.0, 2.0, 4.0, 8.0]
    limit = math.sqrt(g0) / kappa
    tau_limit = limit / v0

    lines = [
        "# Saída — Hartman reduzido no Capítulo 12",
        "",
        "Classificação: avaliação direta de fórmula reduzida.",
        "",
        "Parâmetros reduzidos:",
        "",
        f"- `kappa = {kappa}`",
        f"- `g0 = {g0}`",
        f"- `v0 = {v0}`",
        f"- `D_prop(infinito) = {limit:.12f}`",
        f"- `tau_GDQ(infinito) = {tau_limit:.12f}`",
        "",
        "| L | D_prop(L) | tau_GDQ(L) | fração do limite |",
        "|---:|---:|---:|---:|",
    ]

    for length in lengths:
        d = d_prop(length, kappa, g0)
        tau = tau_gdq(length, kappa, g0, v0)
        lines.append(
            f"| {length:.1f} | {d:.12f} | {tau:.12f} | {d/limit:.12f} |"
        )

    lines += [
        "",
        "Leitura: a distância própria e o tempo próprio efetivo saturam. A razão",
        "`L/tau_GDQ(L)` não é velocidade local nem velocidade de frente.",
        "",
    ]

    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
