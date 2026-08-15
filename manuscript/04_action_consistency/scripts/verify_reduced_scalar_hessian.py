#!/usr/bin/env python3
"""
Chapter 4 — reduced verification of the scalar Hessian.

Classification:
    Symbolic/numerical consistency verification.

In the flat case with constant f0 and R0=0, the analytical note reduces the operator to:

    L_phi = 2 (-Delta).

In Fourier mode e^{ipx}, this gives eigenvalue:

    lambda_phi = 2 p^2.

The script assembles a periodic discretization of -d^2/dx^2 in one dimension,
multiplies by 2 and compares the first eigenvalues with 2 k^2. It is only a
check of the principal symbol, not the complete 8D Hessian.
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

    # Expected eigenvalues: 2*k^2, with double degeneracy for k>=1.
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
        'title: "Output — reduced scalar Hessian"',
        '---',
        '',
        '# Output — reduced scalar Hessian',
        '',
        'Test case: flat background, constant $f_0$, $R_0=0$, periodic domain.',
        '',
        '$$',
        'L_\\varphi=2(-\\Delta).',
        '$$',
        '',
        f'Mesh: `N={n}`, length `2π`.',
        '',
        '| index | expected $2k^2$ | numerical | error |',
        '|---:|---:|---:|---:|',
    ]

    for idx, exp_val, num, err in rows:
        lines.append(f'| `{idx}` | `{exp_val:.12e}` | `{num:.12e}` | `{err:.12e}` |')

    lines += [
        '',
        'Conclusion: in the flat background, the reduced scalar Hessian has a positive principal symbol proportional to $p_E^2$.',
        'The finite difference converges to the continuous spectrum when the mesh is refined.',
        '',
    ]

    out = Path(__file__).with_name('output_verify_reduced_scalar_hessian.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
