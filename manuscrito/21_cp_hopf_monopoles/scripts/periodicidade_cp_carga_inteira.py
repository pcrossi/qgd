#!/usr/bin/env python3
"""
Capítulo 21 — verificação da periodicidade CP por carga topológica inteira.

Classificação:
    verificação simbólica/didática de identidade topológica.

Se Q_C é inteiro, a fase topológica satisfaz:

    exp(i (theta + 2*pi) Q_C) = exp(i theta Q_C).

O script avalia essa identidade para alguns inteiros e salva uma tabela em
Markdown. Ele não usa dados experimentais e não ajusta parâmetros.
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
        'title: "Saída — periodicidade CP por carga inteira"',
        '---',
        '',
        '# Saída — periodicidade CP por carga inteira',
        '',
        'Teste:',
        '',
        '$$',
        '\\exp(i(\\theta+2\\pi)Q_C)=\\exp(i\\theta Q_C),\\qquad Q_C\\in\\mathbb Z.',
        '$$',
        '',
        f'Ângulo de teste: `{theta:.12f}` rad.',
        '',
        '| $Q_C$ | fase original | fase deslocada | erro absoluto |',
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
        f'Erro máximo numérico: `{max_error:.3e}`.',
        '',
        'Conclusão: a periodicidade vem da integralidade de $Q_C$, não de ajuste do potencial.',
        '',
    ]

    out = Path(__file__).with_name('saida_periodicidade_cp_carga_inteira.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
