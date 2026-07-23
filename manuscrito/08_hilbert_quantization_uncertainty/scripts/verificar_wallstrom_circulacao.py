#!/usr/bin/env python3
"""
Verificação reduzida da quantização de circulação.

Classificação: teste simbólico/topológico.

Este script não prova a estrutura global da GDQ. Ele registra, de modo
autocontido, duas consequências algébricas usadas na prova do Capítulo 8:

1. mapas regulares S^1 -> S^1 fecham apenas para enrolamento inteiro;
2. a primeira classe de Chern de um fibrado U(1) exige fluxo inteiro.

Para chi(theta)=N theta:

    (1/2pi) integral_0^{2pi} d chi = N.

Valores não inteiros podem ser escritos localmente, mas não definem mapa
monovalorado S^1 -> S^1, pois exp(i alpha(theta+2pi)) != exp(i alpha theta).

Para o exemplo de Chern em T^2, com x,y em [0,2pi), use:

    F = N/(2pi) dx wedge dy.

Então:

    (1/2pi) integral_{T^2} F = N.
"""

from __future__ import annotations

from pathlib import Path
import cmath
import math


OUT = Path(__file__).with_name("saida_verificar_wallstrom_circulacao.md")


def closes_s1(alpha: float, tol: float = 1e-12) -> tuple[bool, float]:
    """Retorna se exp(i alpha theta) fecha em theta~theta+2pi."""
    defect = abs(cmath.exp(1j * 2.0 * math.pi * alpha) - 1.0)
    return defect < tol, defect


def chern_number_on_t2(N: float) -> float:
    """Calcula (1/2pi) integral F para F=N/(2pi) dx^dy em T^2."""
    area_t2 = (2.0 * math.pi) ** 2
    flux = (N / (2.0 * math.pi)) * area_t2
    return flux / (2.0 * math.pi)


def main() -> None:
    winding_values = [-2, -1, 0, 1, 2, 0.5, 1.3]
    chern_values = [-2, -1, 0, 1, 3, 0.5]

    lines = [
        "---",
        'title: "Saída — circulação Wallstrom"',
        "---",
        "",
        "# Saída — circulação Wallstrom",
        "",
        "Classificação: teste simbólico/topológico.",
        "",
        "## Mapas $S^1\\to S^1$",
        "",
        "| parâmetro $\\alpha$ | fase fecha? | defeito $|e^{i2\\pi\\alpha}-1|$ | enrolamento formal |",
        "|---:|---:|---:|---:|",
    ]

    for alpha in winding_values:
        closes, defect = closes_s1(alpha)
        lines.append(f"| {alpha} | {str(closes)} | {defect:.6e} | {alpha} |")

    lines += [
        "",
        "Conclusão: a integral pode ser formalmente calculada para qualquer",
        "$\\alpha$, mas apenas inteiros fecham o mapa global regular",
        "$S^1\\to S^1$.",
        "",
        "## Exemplo de fluxo de Chern em $T^2$",
        "",
        "Para $F=N(2\\pi)^{-1}dx\\wedge dy$ em $[0,2\\pi)^2$:",
        "",
        "| parâmetro $N$ | $(2\\pi)^{-1}\\int_{T^2}F$ | fluxo inteiro? |",
        "|---:|---:|---:|",
    ]

    for N in chern_values:
        c1 = chern_number_on_t2(N)
        is_integer = abs(c1 - round(c1)) < 1e-12
        lines.append(f"| {N} | {c1:.12f} | {str(is_integer)} |")

    lines += [
        "",
        "Conclusão adicional: a curvatura pode ser escrita formalmente com qualquer",
        "$N$, mas apenas classes inteiras representam a primeira classe de Chern de",
        "um fibrado de linha $U(1)$ globalmente admissível.",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
