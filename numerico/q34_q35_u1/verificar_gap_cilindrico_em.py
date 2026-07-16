#!/usr/bin/env python3
"""Verifica o espectro Neumann do canal fotônico no colar cilíndrico."""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from scipy.linalg import eigh


def neumann_laplacian(length: float, points: int) -> np.ndarray:
    """Volumes finitos centrados em N células, com fluxo nulo nas faces."""
    if length <= 0 or points < 3:
        raise ValueError("requer length>0 e points>=3")
    h = length / points
    matrix = np.zeros((points, points))
    diagonal = np.full(points, 2.0)
    diagonal[[0, -1]] = 1.0
    np.fill_diagonal(matrix, diagonal)
    idx = np.arange(points - 1)
    matrix[idx, idx + 1] = -1.0
    matrix[idx + 1, idx] = -1.0
    return matrix / h**2


def first_modes(length: float, points: int, count: int = 4) -> np.ndarray:
    matrix = neumann_laplacian(length, points)
    return eigh(matrix, subset_by_index=[0, count - 1], eigvals_only=True)


def main() -> int:
    lengths = [1.0, 2.0, 4.0, 8.0, 16.0]
    points = 800
    rows = []
    for length in lengths:
        values = first_modes(length, points)
        exact = (math.pi / length) ** 2
        rows.append((length, values[0], values[1], exact, abs(values[1] - exact) / exact))

    convergence = []
    for n in [50, 100, 200, 400, 800]:
        gap = first_modes(1.0, n, 2)[1]
        convergence.append((n, gap, abs(gap - math.pi**2) / math.pi**2))

    scaled = [gap * length**2 for length, _, gap, _, _ in rows]
    assert max(abs(x - math.pi**2) for x in scaled) / math.pi**2 < 3e-3
    assert abs(rows[-1][2]) < abs(rows[0][2])
    assert convergence[-1][2] < convergence[0][2]

    output = Path(__file__).with_name("saida_gap_cilindrico_em.md")
    lines = [
        "# Verificação do gap eletromagnético no colar cilíndrico",
        "",
        "## Classificação",
        "",
        "**Avaliação direta e teste de convergência** do operador radial de",
        "Neumann derivado em q35/operador_em_cilindrico_no_go.md.",
        "",
        "| $L$ | modo zero | $\\lambda_1^{\\rm num}$ | $\\pi^2/L^2$ | erro relativo |",
        "|---:|---:|---:|---:|---:|",
    ]
    for length, zero, gap, exact, error in rows:
        lines.append(f"| {length:.1f} | {zero:.3e} | {gap:.10e} | {exact:.10e} | {error:.3e} |")
    lines += [
        "",
        "## Refinamento para $L=1$",
        "",
        "| pontos | $\\lambda_1^{\\rm num}$ | erro relativo |",
        "|---:|---:|---:|",
    ]
    for n, gap, error in convergence:
        lines.append(f"| {n} | {gap:.10e} | {error:.3e} |")
    lines += [
        "",
        "A combinação $L^2\\lambda_1$ converge para $\\pi^2$. Assim,",
        "",
        "$$",
        "\\lambda_1^+=\\frac{\\pi^2}{L^2}\\longrightarrow0",
        "\\quad\\text{quando}\\quad L\\longrightarrow\\infty.",
        "$$",
        "",
        "O cálculo confirma que o colar local infinito não fornece uma escala",
        "eletromagnética positiva; no colar compacto ela depende do comprimento",
        "global $L$.",
        "",
    ]
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Relatório: {output}")
    print(f"erro final de convergência: {convergence[-1][2]:.3e}")
    print(f"gap em L=16: {rows[-1][2]:.12e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
