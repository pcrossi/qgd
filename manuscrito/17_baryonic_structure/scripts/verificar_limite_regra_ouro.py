#!/usr/bin/env python3
"""Verifica o limite distribucional usado na Regra de Ouro.

O kernel

    delta_T(E) = |∫ exp(i E t / hbar) dt|² / (2*pi*hbar*T)

deve agir como a delta de Dirac quando T cresce. O teste usa hbar=1 e não
contém dados experimentais ou parâmetros ajustáveis.

Classificação:
    teste de consistência e convergência de uma identidade analítica.

Saída:
    ``saida_verificar_limite_regra_ouro.md`` na pasta deste script.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Callable


HBAR = 1.0
E_MAX = 12.0


def sinc(x: float) -> float:
    """Calcula sin(x)/x com sua extensão contínua na origem."""

    if abs(x) < 1.0e-12:
        return 1.0
    return math.sin(x) / x


def delta_t(energy: float, time: float) -> float:
    """Kernel positivo de tempo finito, com dimensão inversa de energia."""

    x = energy * time / (2.0 * HBAR)
    return time * sinc(x) ** 2 / (2.0 * math.pi * HBAR)


def trapezoid(func: Callable[[float], float], a: float, b: float, n: int) -> float:
    """Quadratura trapezoidal composta em n subintervalos."""

    step = (b - a) / n
    total = 0.5 * (func(a) + func(b))
    for index in range(1, n):
        total += func(a + index * step)
    return total * step


def evaluate(time: float, points_per_period: int = 80) -> tuple[float, float, float]:
    """Avalia norma truncada e a ação do kernel sobre duas funções teste."""

    periods = max(1.0, E_MAX * time / (2.0 * math.pi))
    intervals = max(20_000, int(2.0 * periods * points_per_period))
    if intervals % 2:
        intervals += 1

    norm = trapezoid(lambda energy: delta_t(energy, time), -E_MAX, E_MAX, intervals)
    gaussian = trapezoid(
        lambda energy: delta_t(energy, time) * math.exp(-(energy * energy)),
        -E_MAX,
        E_MAX,
        intervals,
    )
    lorentzian = trapezoid(
        lambda energy: delta_t(energy, time) / (1.0 + energy * energy),
        -E_MAX,
        E_MAX,
        intervals,
    )
    return norm, gaussian, lorentzian


def main() -> None:
    """Executa a série temporal e um refinamento independente da quadratura."""

    times = (5.0, 10.0, 20.0, 40.0, 80.0, 160.0, 320.0)
    rows = [(time, *evaluate(time)) for time in times]
    refinements = [
        (points, *evaluate(times[-1], points_per_period=points))
        for points in (40, 80, 160)
    ]

    lines = [
        "---",
        'title: "Saída — limite de tempo longo da Regra de Ouro"',
        "---",
        "",
        "# Verificação do kernel de tempo finito",
        "",
        "Classificação: teste de consistência e convergência; nenhum parâmetro foi",
        "ajustado a dado experimental.",
        "",
        "Unidades do teste: $\\hbar=1$ e janela $E\\in[-12,12]$.",
        "",
        "| $T$ | $\\int\\delta_T dE$ | gaussiana | erro gaussiana | lorentziana | erro lorentziana |",
        "|---:|---:|---:|---:|---:|---:|",
    ]

    for time, norm, gaussian, lorentzian in rows:
        lines.append(
            f"| {time:.1f} | {norm:.12f} | {gaussian:.12f} | "
            f"{abs(gaussian - 1.0):.3e} | {lorentzian:.12f} | "
            f"{abs(lorentzian - 1.0):.3e} |"
        )

    lines += [
        "",
        "As duas funções teste valem exatamente 1 em $E=0$. Portanto, ambas as",
        "integrais devem tender a 1.",
        "",
        "## Refinamento da quadratura em $T=320$",
        "",
        "| pontos por período | norma | gaussiana | lorentziana |",
        "|---:|---:|---:|---:|",
    ]

    for points, norm, gaussian, lorentzian in refinements:
        lines.append(
            f"| {points} | {norm:.12f} | {gaussian:.12f} | {lorentzian:.12f} |"
        )

    lines += [
        "",
        "O erro dominante da norma é o truncamento da janela energética. A",
        "estabilidade sob refinamento separa esse efeito do erro de quadratura.",
    ]

    output = Path(__file__).with_name("saida_verificar_limite_regra_ouro.md")
    text = "\n".join(lines) + "\n"
    output.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
