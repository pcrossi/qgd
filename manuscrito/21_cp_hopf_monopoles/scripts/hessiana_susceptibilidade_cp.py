#!/usr/bin/env python3
"""
Capítulo 21 — Hessiana angular e susceptibilidade topológica.

Classificação:
    verificação simbólica/numerica de consistência.

Para:

    V(theta) = chi * (1 - cos(theta)),

temos:

    d2V/dtheta2 = chi * cos(theta).

No mínimo theta=0, a Hessiana vale +chi. No ponto theta=pi, vale -chi.
Isso verifica que a positividade de chi_top^GDQ seleciona theta=0 mod 2*pi
como atrator estável e theta=pi mod 2*pi como máximo instável.
"""

from __future__ import annotations

import math
from pathlib import Path


def potential(theta: float, chi: float) -> float:
    return chi * (1.0 - math.cos(theta))


def second_derivative_central(theta: float, chi: float, h: float) -> float:
    return (potential(theta + h, chi) - 2.0 * potential(theta, chi) + potential(theta - h, chi)) / h**2


def main() -> None:
    chi = 1.0
    h = 1.0e-4
    points = [0.0, math.pi / 2.0, math.pi, 2.0 * math.pi]

    lines = [
        '---',
        'title: "Saída — Hessiana CP e susceptibilidade"',
        '---',
        '',
        '# Saída — Hessiana CP e susceptibilidade',
        '',
        'Potencial reduzido:',
        '',
        '$$',
        'V(\\theta)=\\chi(1-\\cos\\theta).',
        '$$',
        '',
        f'Usado $\\chi=1$ e passo de diferença finita `h={h:.1e}` apenas para verificar a identidade.',
        '',
        '| $\\theta$ | Hessiana analítica | Hessiana numérica | Classificação |',
        '|---:|---:|---:|---|',
    ]

    for theta in points:
        analytic = chi * math.cos(theta)
        numeric = second_derivative_central(theta, chi, h)
        if analytic > 1e-8:
            status = 'mínimo estável'
        elif analytic < -1e-8:
            status = 'máximo instável'
        else:
            status = 'ponto plano da projeção angular'
        lines.append(f'| `{theta:.12f}` | `{analytic:.12f}` | `{numeric:.12f}` | {status} |')

    lines += [
        '',
        'Conclusão: no canal torsional, $\\chi_{\\rm top}^{\\rm GDQ}>0$ é exatamente a curvatura positiva do mínimo CP.',
        '',
    ]

    out = Path(__file__).with_name('saida_hessiana_susceptibilidade_cp.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
