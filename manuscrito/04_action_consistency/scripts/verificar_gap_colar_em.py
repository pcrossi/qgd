#!/usr/bin/env python3
"""
Capítulo 4 — no-go do colar cilíndrico local para Lambda_EM.

Classificação:
    avaliação direta e teste de convergência.

O operador radial Neumann no colar de comprimento L tem autovalores

    lambda_j = 4/h^2 sin^2(j*pi/(2N)),    h=L/N.

O primeiro gap físico tende a pi^2/L^2. Portanto, em um colar local
infinito, o gap tende a zero e não fixa uma escala EM positiva.
"""

from __future__ import annotations

import math
from pathlib import Path


def neumann_gap(length: float, cells: int, j: int = 1) -> float:
    h = length / cells
    return 4.0 * math.sin(j * math.pi / (2.0 * cells)) ** 2 / (h * h)


def main() -> None:
    rows = []
    for length in [1.0, 2.0, 4.0, 8.0, 16.0]:
        gap = neumann_gap(length, 800)
        exact = (math.pi / length) ** 2
        rows.append((length, 0.0, gap, exact, abs(gap - exact) / exact))

    convergence = []
    for cells in [50, 100, 200, 400, 800]:
        gap = neumann_gap(1.0, cells)
        convergence.append((cells, gap, abs(gap - math.pi**2) / math.pi**2))

    lines = [
        "---",
        'title: "Saída — gap eletromagnético do colar"',
        "---",
        "",
        "# Saída — gap eletromagnético do colar",
        "",
        "| $L$ | modo zero | $\\lambda_1^{\\rm num}$ | $\\pi^2/L^2$ | erro relativo |",
        "|---:|---:|---:|---:|---:|",
    ]
    for length, zero, gap, exact, error in rows:
        lines.append(f"| `{length:.1f}` | `{zero:.3e}` | `{gap:.10e}` | `{exact:.10e}` | `{error:.3e}` |")
    lines += [
        "",
        "## Refinamento para $L=1$",
        "",
        "| células | $\\lambda_1^{\\rm num}$ | erro relativo |",
        "|---:|---:|---:|",
    ]
    for cells, gap, error in convergence:
        lines.append(f"| `{cells}` | `{gap:.10e}` | `{error:.3e}` |")
    lines += [
        "",
        "Como $L^2\\lambda_1\\to\\pi^2$, segue que",
        "",
        "$$",
        "\\lambda_1=\\frac{\\pi^2}{L^2}\\to0",
        "\\quad\\text{quando}\\quad L\\to\\infty.",
        "$$",
        "",
        "O colar local infinito não fornece uma escala eletromagnética positiva;",
        "a escala depende da colagem global ou da resolução setorial.",
        "",
    ]
    out = Path(__file__).with_name("saida_verificar_gap_colar_em.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

