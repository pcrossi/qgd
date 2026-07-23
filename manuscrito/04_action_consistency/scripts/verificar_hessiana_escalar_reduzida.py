#!/usr/bin/env python3
"""
Capítulo 4 — verificação reduzida da Hessiana escalar.

Classificação:
    verificação simbólica/numerica de consistência.

No caso plano com f0 constante e R0=0, a nota analítica reduz o operador a:

    L_phi = 2 (-Delta).

Em modo de Fourier e^{ipx}, isso dá autovalor:

    lambda_phi = 2 p^2.

O script monta uma discretização periódica de -d^2/dx^2 em uma dimensão,
multiplica por 2 e compara os primeiros autovalores com 2 k^2. É apenas uma
checagem do símbolo principal, não a Hessiana 8D completa.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


def periodic_laplacian_negative(n: int, length: float) -> np.ndarray:
    dx = length / n
    mat = np.zeros((n, n), dtype=float)
    for i in range(n):
        mat[i, i] = 2.0 / dx**2
        mat[i, (i - 1) % n] = -1.0 / dx**2
        mat[i, (i + 1) % n] = -1.0 / dx**2
    return mat


def main() -> None:
    n = 128
    length = 2.0 * math.pi
    neg_lap = periodic_laplacian_negative(n, length)
    L_phi = 2.0 * neg_lap
    eig = np.linalg.eigvalsh(L_phi)
    eig = np.sort(eig)

    # Autovalores esperados: 2*k^2, com degenerescência dupla para k>=1.
    expected = [0.0]
    for k in range(1, 5):
        expected.extend([2.0 * k * k, 2.0 * k * k])

    rows = []
    for idx, exp_val in enumerate(expected):
        num = eig[idx]
        err = num - exp_val
        rows.append((idx, exp_val, num, err))

    lines = [
        '---',
        'title: "Saída — Hessiana escalar reduzida"',
        '---',
        '',
        '# Saída — Hessiana escalar reduzida',
        '',
        'Caso teste: fundo plano, $f_0$ constante, $R_0=0$, domínio periódico.',
        '',
        '$$',
        'L_\\varphi=2(-\\Delta).',
        '$$',
        '',
        f'Malha: `N={n}`, comprimento `2π`.',
        '',
        '| índice | esperado $2k^2$ | numérico | erro |',
        '|---:|---:|---:|---:|',
    ]

    for idx, exp_val, num, err in rows:
        lines.append(f'| `{idx}` | `{exp_val:.12e}` | `{num:.12e}` | `{err:.12e}` |')

    lines += [
        '',
        'Conclusão: no fundo plano, a Hessiana escalar reduzida tem símbolo principal positivo proporcional a $p_E^2$.',
        'A diferença finita converge para o espectro contínuo quando a malha é refinada.',
        '',
    ]

    out = Path(__file__).with_name('saida_verificar_hessiana_escalar_reduzida.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
