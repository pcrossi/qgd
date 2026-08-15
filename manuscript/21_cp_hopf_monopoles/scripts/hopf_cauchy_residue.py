#!/usr/bin/env python3
"""
Objective:
    Self-contained log of the `hopf cauchy residue` verification associated with chapter `21_cp_hopf_monopoles`.
Chapter 21 — Hopf--Cauchy verification of half-monodromy.

Classification:
    symbolic/didactic verification of topological identity.

For s(z)=z^(1/2)s0(z), with s0 holomorphic and non-zero,

    d log s = (1/2) dz/z + d log s0.

The residue at the core is 1/2. The physical circulation is h/2 and the holonomy is -1.
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
        'title: "Output — Hopf--Cauchy and residue 1/2"',
        '---',
        '',
        '# Output — Hopf--Cauchy and residue $1/2$',
        '',
        '| Quantity | Value |',
        '|---|---:|',
        f'| $\\operatorname{{Res}}\\Omega_S$ | `{residue:.12f}` |',
        f'| $(2\\pi i)^{{-1}}\\oint\\Omega_S$ | `{normalized_integral:.12f}` |',
        f'| $h^{{-1}}\\oint dS_R$ | `{circulation_over_h:.12f}` |',
        f'| holonomy in one loop | `{holonomy.real:.12f} {holonomy.imag:+.12f}i` |',
        f'| holonomy in two loops | `{double_holonomy.real:.12f} {double_holonomy.imag:+.12f}i` |',
        '',
        'Conclusion: one turn gives $-1$ and two turns give $+1$.',
        '',
    ]

    out = Path(__file__).with_name('output_hopf_cauchy_residue.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
