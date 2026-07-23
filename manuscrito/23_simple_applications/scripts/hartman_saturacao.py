#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `hartman saturacao` associada ao capítulo `23_simple_applications`.
Capítulo 23 — saturação geométrica do efeito Hartman.

Classificação:
    Avaliação direta de fórmula reduzida. Nenhum alvo experimental é usado.

Equação:
    D(L)=sqrt(g0)/kappa * (1-exp(-kappa L)).
"""

from __future__ import annotations

from pathlib import Path
import math


OUT = Path(__file__).with_name("saida_hartman_saturacao.md")


def main() -> None:
    kappa = 1.0
    g0 = 1.0
    v0 = 1.0
    limit = math.sqrt(g0) / kappa
    lengths = [0.1, 0.5, 1.0, 2.0, 4.0, 8.0]

    lines = [
        "---",
        'title: "Saída — Hartman reduzido"',
        "---",
        "",
        "# Saída — Hartman reduzido",
        "",
        "- parâmetros reduzidos: $\\kappa=1$, $g_0=1$, $v_0=1$;",
        f"- limite próprio: `{limit:.12f}`;",
        "- classificação: avaliação direta de fórmula reduzida.",
        "",
        "| $L$ | $D_{\\rm prop}(L)$ | $\\tau_{\\rm GDQ}(L)$ | fração do limite |",
        "|---:|---:|---:|---:|",
    ]
    for length in lengths:
        dprop = math.sqrt(g0) / kappa * (1.0 - math.exp(-kappa * length))
        tau = dprop / v0
        lines.append(f"| `{length:.1f}` | `{dprop:.12f}` | `{tau:.12f}` | `{dprop/limit:.12f}` |")

    lines += [
        "",
        "Interpretação: o comprimento próprio satura; isso não é velocidade de frente",
        "superluminal.",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
