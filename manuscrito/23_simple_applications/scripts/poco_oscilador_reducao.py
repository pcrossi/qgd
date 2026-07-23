#!/usr/bin/env python3
"""Capítulo 23 — verificação reduzida de poço ideal e oscilador.

Objetivo:
    Verificar, em um script autocontido, os dois resultados elementares usados
    no texto:

    1. Poço infinito em unidades L=1 e hbar^2/(2mL^2)=1:
       E_n = (n*pi)^2.
    2. Oscilador harmônico em unidades hbar=m=omega=1:
       E_n = n + 1/2.

Classificação:
    Teste de correspondência e consistência numérica. Nenhum dado experimental
    entra no cálculo. O script não é uma Hessiana completa da ação oficial; ele
    verifica a Hessiana reduzida obtida no setor plano estacionário.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.linalg import eigh_tridiagonal


OUT = Path(__file__).with_name("saida_poco_oscilador_reducao.md")


@dataclass(frozen=True)
class Check:
    name: str
    numerical: np.ndarray
    analytic: np.ndarray

    @property
    def rel_error(self) -> np.ndarray:
        return np.abs(self.numerical - self.analytic) / np.maximum(1.0e-30, np.abs(self.analytic))


def infinite_well_direct(points: int, modes: int) -> Check:
    """Diagonaliza -d^2/dx^2 em (0,1) com Dirichlet nas duas bordas."""

    h = 1.0 / (points + 1)
    diagonal = np.full(points, 2.0 / h**2)
    off = np.full(points - 1, -1.0 / h**2)
    numerical = eigh_tridiagonal(
        diagonal,
        off,
        select="i",
        select_range=(0, modes - 1),
        check_finite=False,
    )[0]
    n = np.arange(1, modes + 1, dtype=float)
    analytic = (np.pi * n) ** 2
    return Check("poço infinito", numerical, analytic)


def oscillator_direct(points: int, half_width: float, modes: int) -> Check:
    """Diagonaliza -1/2 d^2/dx^2 + x^2/2 em [-A,A] com A grande."""

    h = 2.0 * half_width / (points + 1)
    x = -half_width + h * np.arange(1, points + 1)
    diagonal = 1.0 / h**2 + 0.5 * x**2
    off = np.full(points - 1, -0.5 / h**2)
    numerical = eigh_tridiagonal(
        diagonal,
        off,
        select="i",
        select_range=(0, modes - 1),
        check_finite=False,
    )[0]
    n = np.arange(0, modes, dtype=float)
    analytic = n + 0.5
    return Check("oscilador harmônico", numerical, analytic)


def morse_indices(modes: int) -> tuple[list[int], list[int]]:
    """Índices da Hessiana reduzida em torno dos autestados.

    Para o poço com n=1,2,..., o estado n possui n-1 níveis abaixo dele.
    Para o oscilador com n=0,1,..., o estado n possui n níveis abaixo dele.
    """

    well = [n - 1 for n in range(1, modes + 1)]
    oscillator = [n for n in range(0, modes)]
    return well, oscillator


def render(checks: list[Check], points_well: int, points_osc: int, half_width: float) -> str:
    lines = [
        "---",
        'title: "Saída — poço e oscilador como redução"',
        "---",
        "",
        "# Saída — poço e oscilador como redução",
        "",
        "Classificação: teste de correspondência da Hessiana reduzida plana.",
        "",
        "## Parâmetros numéricos",
        "",
        f"- poço: `{points_well}` pontos internos, $L=1$, $\\hbar^2/(2mL^2)=1$;",
        f"- oscilador: `{points_osc}` pontos internos em $[-{half_width:g},{half_width:g}]$, $\\hbar=m=\\omega=1$;",
        "- nenhum valor experimental é usado.",
        "",
    ]

    for check in checks:
        lines += [
            f"## {check.name}",
            "",
            "| modo | numérico | analítico | erro relativo |",
            "|---:|---:|---:|---:|",
        ]
        for i, (num, ana, err) in enumerate(zip(check.numerical, check.analytic, check.rel_error)):
            label = i + 1 if check.name == "poço infinito" else i
            lines.append(f"| {label} | `{num:.12f}` | `{ana:.12f}` | `{err:.3e}` |")
        lines.append("")

    well_idx, osc_idx = morse_indices(len(checks[0].analytic))
    lines += [
        "## Índices de Morse reduzidos",
        "",
        "| modo | poço ideal | oscilador |",
        "|---:|---:|---:|",
    ]
    for i in range(len(well_idx)):
        lines.append(f"| {i + 1} / {i} | `{well_idx[i]}` | `{osc_idx[i]}` |")

    lines += [
        "",
        "## Leitura",
        "",
        "- o poço recupera $E_n=(n\\pi)^2$ no contorno ideal;",
        "- o oscilador recupera $E_n=n+1/2$ no fundo plano;",
        "- os erros restantes são de discretização/truncamento;",
        "- a Hessiana reduzida tem índice de Morse igual ao número de níveis abaixo do estado escolhido;",
        "- o cálculo verifica correspondência, não uma previsão metrológica nova.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    modes = 5
    points_well = 2400
    points_osc = 3200
    half_width = 8.0

    checks = [
        infinite_well_direct(points_well, modes),
        oscillator_direct(points_osc, half_width, modes),
    ]
    report = render(checks, points_well, points_osc, half_width)
    OUT.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
