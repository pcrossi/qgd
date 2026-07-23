#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `calcular a0 galactico` associada ao capítulo `20_gravity_cosmology`.
Capítulo 20 — avaliação da escala de aceleração galáctica.

Classificação:
    avaliação direta de escala de horizonte e comparação fenomenológica.

Fórmula principal:

    a0_GDQ = c H0 / (2 pi).

O valor típico de MOND/RAR é usado somente para comparação final.

Este script também registra a correção técnica que motivou a auditoria da
aceleração cosmológica: se o numerador escolhido for a escala de de Sitter
aproximada `5.46e-10 m/s²`, a projeção circular correta é `5.46e-10/(2*pi)`,
não `1.21e-10 m/s²`.
"""

from __future__ import annotations

from math import pi, sqrt
from pathlib import Path


def main() -> None:
    c = 299_792_458.0
    mpc = 3.085_677_581_491_367_3e22
    omega_lambda = 0.6847
    a0_ref = 1.20e-10

    cases = [
        ('H0=67.4', 67.4),
        ('H0=73.0', 73.0),
    ]

    rows = []
    for label, H0_km in cases:
        H0 = H0_km * 1000.0 / mpc
        a0 = c * H0 / (2.0 * pi)
        rows.append((label, a0, (a0 - a0_ref) / a0_ref))

    H0_planck = 67.4 * 1000.0 / mpc
    a_de_sitter = c * H0_planck * sqrt(omega_lambda) / (2.0 * pi)
    old_de_sitter_numerator = 5.46e-10
    old_de_sitter_projected = old_de_sitter_numerator / (2.0 * pi)

    lines = [
        '---',
        'title: "Saída — aceleração crítica galáctica"',
        '---',
        '',
        '# Saída — aceleração crítica galáctica',
        '',
        '## Fórmula principal',
        '',
        '$$',
        'a_0^{\\rm GDQ}=\\frac{cH_0}{2\\pi}',
        '$$',
        '',
        '## Comparação',
        '',
        '| Contorno | $a_0$ [m/s²] | erro relativo vs $1.20e-10$ |',
        '|---|---:|---:|',
    ]
    for label, value, err in rows:
        lines.append(f'| {label} | `{value:.12e}` | `{err:+.6%}` |')

    lines += [
        '',
        '## Escala alternativa auditada',
        '',
        f'- $cH_0\\sqrt{{\\Omega_\\Lambda}}/(2\\pi)={a_de_sitter:.12e}\\,{{\\rm m/s^2}}$ para $H_0=67.4$.',
        '- Essa é escala de de Sitter, não a rota principal adotada para a aceleração crítica galáctica.',
        f'- Auditoria aritmética: $5.46\\times10^{{-10}}/(2\\pi)={old_de_sitter_projected:.12e}\\,{{\\rm m/s^2}}$, não $1.21\\times10^{{-10}}\\,{{\\rm m/s^2}}$.',
        '',
        '## Classificação',
        '',
        'Avaliação direta da escala de horizonte. A comparação com MOND/RAR é fenomenológica.',
        '',
    ]

    out = Path(__file__).with_name('saida_calculo_a0_galactico.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
