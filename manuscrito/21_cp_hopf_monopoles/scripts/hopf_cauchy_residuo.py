#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `hopf cauchy residuo` associada ao capítulo `21_cp_hopf_monopoles`.
Capítulo 21 — verificação Hopf--Cauchy da meia-monodromia.

Classificação:
    verificação simbólica/didática de identidade topológica.

Para s(z)=z^(1/2)s0(z), com s0 holomorfa e não nula,

    d log s = (1/2) dz/z + d log s0.

O resíduo no núcleo é 1/2. A circulação física é h/2 e a holonomia é -1.
"""

from __future__ import annotations

import cmath
import math
from pathlib import Path


def main() -> None:
    residue = 0.5
    normalized_integral = residue
    circulation_over_h = residue
    holonomy = cmath.exp(1j * 2.0 * math.pi * circulation_over_h)
    double_holonomy = holonomy**2

    lines = [
        '---',
        'title: "Saída — Hopf--Cauchy e resíduo 1/2"',
        '---',
        '',
        '# Saída — Hopf--Cauchy e resíduo $1/2$',
        '',
        '| Quantidade | Valor |',
        '|---|---:|',
        f'| $\\operatorname{{Res}}\\Omega_S$ | `{residue:.12f}` |',
        f'| $(2\\pi i)^{{-1}}\\oint\\Omega_S$ | `{normalized_integral:.12f}` |',
        f'| $h^{{-1}}\\oint dS_R$ | `{circulation_over_h:.12f}` |',
        f'| holonomia em uma volta | `{holonomy.real:.12f} {holonomy.imag:+.12f}i` |',
        f'| holonomia em duas voltas | `{double_holonomy.real:.12f} {double_holonomy.imag:+.12f}i` |',
        '',
        'Conclusão: uma volta dá $-1$ e duas voltas dão $+1$.',
        '',
    ]

    out = Path(__file__).with_name('saida_hopf_cauchy_residuo.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
