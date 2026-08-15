#!/usr/bin/env python3
"""
Chapter 21 — verification of CP periodicity by integer topological charge.

Classification:
    symbolic/didactic verification of topological identity.

If Q_C is an integer, the topological phase satisfies:

    exp(i (theta + 2*pi) Q_C) = exp(i theta Q_C).

The script evaluates this identity for a few integers and saves a Markdown table.
It does not use experimental data and does not fit parameters.
"""

from __future__ import annotations

import cmath
import math
from pathlib import Path


def main() -> None:
    theta = 0.731
    charges = [-2, -1, 0, 1, 2, 3]

    rows = []
    max_error = 0.0
    for charge in charges:
        phase = cmath.exp(1j * theta * charge)
        shifted = cmath.exp(1j * (theta + 2.0 * math.pi) * charge)
        error = abs(shifted - phase)
        max_error = max(max_error, error)
        rows.append((charge, phase, shifted, error))

    lines = [
        '---',
        'title: "Output — CP periodicity by integer charge"',
        '---',
        '',
        '# Output — CP periodicity by integer charge',
        '',
        'Test:',
        '',
        '$$',
        '\\exp(i(\\theta+2\\pi)Q_C)=\\exp(i\\theta Q_C),\\qquad Q_C\\in\\mathbb Z.',
        '$$',
        '',
        f'Test angle: `{theta:.12f}` rad.',
        '',
        '| $Q_C$ | original phase | shifted phase | absolute error |',
        '|---:|---:|---:|---:|',
    ]

    for charge, phase, shifted, error in rows:
        lines.append(
            '| `{}` | `{: .12f}{:+.12f}i` | `{: .12f}{:+.12f}i` | `{:.3e}` |'.format(
                charge,
                phase.real,
                phase.imag,
                shifted.real,
                shifted.imag,
                error,
                
            )
        )

    lines += [
        '',
        f'Maximum numerical error: `{max_error:.3e}`.',
        '',
        'Conclusion: periodicity comes from the integrity of $Q_C$, not from a fit of the potential.',
        '',
    ]

    out = Path(__file__).with_name('output_cp_periodicity_integer_charge.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
