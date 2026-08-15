#!/usr/bin/env python3
"""Verifies the distributional limit used in the Golden Rule.

The kernel

    delta_T(E) = |∫ exp(i E t / hbar) dt|² / (2*pi*hbar*T)

must act as the Dirac delta as T grows. The test uses hbar=1 and contains no
experimental data or adjustable parameters.

Classification:
    consistency and convergence test of an analytical identity.

Output:
    ``output_verify_golden_rule_limit.md`` in this script's directory.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Callable


HBAR = 1.0
E_MAX = 12.0


def sinc(x: float) -> float:
    """Calculates sin(x)/x with its continuous extension at the origin."""

    if abs(x) < 1.0e-12:
        return 1.0
    return math.sin(x) / x


def delta_t(energy: float, time: float) -> float:
    """Finite time positive kernel with inverse energy dimension."""

    x = energy * time / (2.0 * HBAR)
    return time * sinc(x) ** 2 / (2.0 * math.pi * HBAR)


def trapezoid(func: Callable[[float], float], a: float, b: float, n: int) -> float:
    """Composite trapezoidal quadrature on n subintervals."""

    step = (b - a) / n
    total = 0.5 * (func(a) + func(b))
    for index in range(1, n):
        total += func(a + index * step)
    return total * step


def evaluate(time: float, points_per_period: int = 80) -> tuple[float, float, float]:
    """Evaluates truncated norm and kernel action on two test functions."""

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
    """Executes time series and an independent quadrature refinement."""

    times = (5.0, 10.0, 20.0, 40.0, 80.0, 160.0, 320.0)
    rows = [(time, *evaluate(time)) for time in times]
    refinements = [
        (points, *evaluate(times[-1], points_per_period=points))
        for points in (40, 80, 160)
    ]

    lines = [
        "---",
        'title: "Output — long-time limit of the Golden Rule"',
        "---",
        "",
        "# Verification of the finite-time kernel",
        "",
        "Classification: consistency and convergence test; no parameters were",
        "adjusted to experimental data.",
        "",
        "Test units: $\\hbar=1$ and energy window $E\\in[-12,12]$.",
        "",
        "| $T$ | $\\int\\delta_T dE$ | gaussian | gaussian error | lorentzian | lorentzian error |",
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
        "The two test functions are exactly 1 at $E=0$. Therefore, both integrals",
        "must tend to 1.",
        "",
        "## Quadrature refinement at $T=320$",
        "",
        "| points per period | norm | gaussian | lorentzian |",
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

    output = Path(__file__).with_name("output_verify_golden_rule_limit.md")
    text = "\n".join(lines) + "\n"
    output.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
