#!/usr/bin/env python3
"""
Objective:
    Self-contained registration of the verification `calculate_galactic_a0` associated with the chapter `20_gravity_cosmology`.
    Chapter 20 — evaluation of the galactic acceleration scale.

Classification:
    direct evaluation of horizon scale and phenomenological comparison.

Main formula:

    a0_GDQ = c H0 / (2 pi).

The typical MOND/RAR value is used only for final comparison.

This script also records the technical correction that motivated the audit of the
cosmological acceleration: if the chosen numerator is the approximate de Sitter scale
`5.46e-10 m/s²`, the correct circular projection is `5.46e-10/(2*pi)`, not
`1.21e-10 m/s²`.
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
        'title: "Output — galactic critical acceleration"',
        '---',
        '',
        '# Output — galactic critical acceleration',
        '',
        '## Main formula',
        '',
        '$$',
        'a_0^{\\rm GDQ}=\\frac{cH_0}{2\\pi}',
        '$$',
        '',
        '## Comparison',
        '',
        '| Boundary | $a_0$ [m/s²] | relative error vs $1.20e-10$ |',
        '|---|---:|---:|',
    ]
    for label, value, err in rows:
        lines.append(f'| {label} | `{value:.12e}` | `{err:+.6%}` |')

    lines += [
        '',
        '## Audited alternative scale',
        '',
        f'- $cH_0\\sqrt{{\\Omega_\\Lambda}}/(2\\pi)={a_de_sitter:.12e}\\,{{\\rm m/s^2}}$ for $H_0=67.4$.',
        '- This is the de Sitter scale, not the main route adopted for the galactic critical acceleration.',
        f'- Arithmetic audit: $5.46\\times10^{{-10}}/(2\\pi)={old_de_sitter_projected:.12e}\\,{{\\rm m/s^2}}$, not $1.21\\times10^{{-10}}\\,{{\\rm m/s^2}}$.',
        '',
        '## Classification',
        '',
        'Direct evaluation of the horizon scale. Comparison with MOND/RAR is phenomenological.',
        '',
    ]

    out = Path(__file__).with_name('output_calculate_galactic_a0.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
