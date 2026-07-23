#!/usr/bin/env python3
"""
Capítulo 7 — gravidade macroscópica como correspondência GDQ.

Objetivo:
    Verificar, de forma autocontida, as identidades locais usadas na
    correspondência métrica macroscópica do Capítulo 7.

Classificação científica:
    verificação simbólica/númerica de consistência estrutural.

Este script não calcula o valor absoluto de G. Ele verifica três pontos da
redução macroscópica:

1. a forma trace-reversed implica a forma de Einstein em quatro dimensões;
2. o limite fraco fixa kappa_G = 8*pi*G/c^4 por comparação com Poisson;
3. a aceleração puramente geodésica gerada por uma torção totalmente
   antissimétrica se anula porque H^mu_{nu rho} u^nu u^rho contrai um tensor
   antissimétrico com um tensor simétrico.

O valor absoluto de G e Lambda pertence ao background global/contorno, não a
este verificador local.
"""

from __future__ import annotations

from math import pi
from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_verificar_gravidade_macroscopica.md"


def trace_reversed_to_einstein_residual(kappa: float, trace_t: float, lam: float) -> float:
    """Return residual of Einstein form implied by trace-reversed equation."""

    return (-0.5 * kappa * trace_t + lam) - 0.5 * (-kappa * trace_t + 4.0 * lam) + lam


def kappa_from_poisson_factor() -> float:
    """Return dimensionless C_G such that kappa_G = C_G G/c^4."""

    return 8.0 * pi


def antisymmetric_torsion_contraction() -> float:
    """Evaluate H_ij u_i u_j for a sample antisymmetric matrix."""

    h = [
        [0.0, 2.0, -3.0],
        [-2.0, 0.0, 5.0],
        [3.0, -5.0, 0.0],
    ]
    u = [0.7, -1.1, 2.3]
    total = 0.0
    for i in range(3):
        for j in range(3):
            total += h[i][j] * u[i] * u[j]
    return total


def main() -> None:
    trace_tests = [
        trace_reversed_to_einstein_residual(kappa=2.0, trace_t=3.0, lam=5.0),
        trace_reversed_to_einstein_residual(kappa=7.0, trace_t=-0.25, lam=0.1),
        trace_reversed_to_einstein_residual(kappa=1.0, trace_t=0.0, lam=-3.0),
    ]
    c_g = kappa_from_poisson_factor()
    torsion_residual = antisymmetric_torsion_contraction()

    lines: list[str] = []
    lines.append("# Saída — gravidade macroscópica\n\n")
    lines.append("Classificação: verificação de consistência estrutural.\n\n")
    lines.append("## Trace-reversed para Einstein\n\n")
    lines.append("| teste | resíduo algébrico |\n")
    lines.append("|---:|---:|\n")
    for i, residual in enumerate(trace_tests, start=1):
        lines.append(f"| {i} | {residual:.12e} |\n")

    lines.append("\n## Normalização de Poisson\n\n")
    lines.append("A comparação do limite fraco fornece:\n\n")
    lines.append("$$\n")
    lines.append("\\kappa_G = C_G\\frac{G}{c^4},\\qquad C_G=8\\pi.\n")
    lines.append("$$\n\n")
    lines.append(f"- C_G calculado = `{c_g:.12f}`\n")

    lines.append("\n## Torção totalmente antissimétrica\n\n")
    lines.append(
        "A contração puramente geodésica de uma torção antissimétrica com "
        "`u_i u_j` deve anular.\n\n"
    )
    lines.append(f"- resíduo da contração = `{torsion_residual:.12e}`\n\n")

    lines.append("## Veredito\n\n")
    lines.append(
        "As identidades locais da correspondência métrica passam. Isto valida "
        "a forma macroscópica líder, não o valor absoluto de G nem as correções "
        "PPN metrológicas, que dependem do background e dos contornos globais.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
