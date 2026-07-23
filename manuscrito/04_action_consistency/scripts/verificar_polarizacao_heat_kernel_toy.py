#!/usr/bin/env python3
"""
GDQ — Capítulo 4 / Polarização heat-kernel toy.

Objetivo:
    Ilustrar que um regulador heat-kernel pode transformar uma integral
    logarítmica em uma quantidade saturada no ultravioleta. Este script não
    reproduz a nota completa de polarização; é apenas uma demonstração mínima.

Fonte teórica:
    manuscrito/04_action_consistency/04.7 - O que significa consistência em loops.md
    manuscrito/04_action_consistency/notes/ausencia_polo_landau_u1.md

Classificação:
    Ilustração heat-kernel. Não é previsão física.

Equação:
    I(Lambda) = integral_0^Lambda k/(k^2+m^2) exp(-tau k^2) dk

Domínio e contorno:
    Integral radial 1D toy.

Parâmetros:
    Universais:
        nenhum
    Dados de aparelho/experimento:
        nenhum
    Numéricos:
        m = 1, tau = 0.25, Lambda variável.

Saída:
    saida_verificar_polarizacao_heat_kernel_toy.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def integral(Lambda: float, m: float = 1.0, tau: float = 0.25, n: int = 200000) -> float:
    k = np.linspace(0.0, Lambda, n)
    integrand = k / (k * k + m * m) * np.exp(-tau * k * k)
    return float(np.trapezoid(integrand, k))


def integral_unregulated(Lambda: float, m: float = 1.0) -> float:
    return 0.5 * np.log((Lambda * Lambda + m * m) / (m * m))


def main() -> None:
    lambdas = [1, 2, 4, 8, 16, 32]
    rows = []
    for L in lambdas:
        reg = integral(float(L))
        unreg = integral_unregulated(float(L))
        rows.append((L, reg, unreg))
    saturation_delta = abs(rows[-1][1] - rows[-2][1])
    ok = saturation_delta < 1e-5

    lines: list[str] = []
    lines.append("# Saída — polarização heat-kernel toy\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Ilustração heat-kernel. Não é previsão física.\n\n")
    lines.append("## Integral toy\n\n")
    lines.append("$$\n")
    lines.append("I(\\Lambda)=\\int_0^\\Lambda\\frac{k}{k^2+m^2}e^{-\\tau k^2}\\,dk.\n")
    lines.append("$$\n\n")
    lines.append("A comparação sem regulador é:\n\n")
    lines.append("$$\n")
    lines.append("I_0(\\Lambda)=\\frac12\\log\\left(\\frac{\\Lambda^2+m^2}{m^2}\\right).\n")
    lines.append("$$\n\n")
    lines.append("## Parâmetros\n\n")
    lines.append("- $m=1$.\n")
    lines.append("- $\\tau=0.25$.\n\n")
    lines.append("## Resultados\n\n")
    lines.append("| $\\Lambda$ | regulado | não regulado |\n")
    lines.append("|---:|---:|---:|\n")
    for L, reg, unreg in rows:
        lines.append(f"| {L} | {reg:.12e} | {unreg:.12e} |\n")
    lines.append("\n## Veredito\n\n")
    lines.append("A integral regulada satura numericamente no UV neste toy model.\n" if ok else "A saturação não atingiu a tolerância escolhida.\n")
    lines.append("\nEsta saída não prova finitude universal da GDQ. Ela apenas ilustra o efeito de um fator heat-kernel.\n")

    out = OUT / "saida_verificar_polarizacao_heat_kernel_toy.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
