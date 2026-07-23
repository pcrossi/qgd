#!/usr/bin/env python3
"""
GDQ — Capítulo 5 / Variação Fisher-Bohm em 1D.

Objetivo:
    Verificar numericamente que a derivada variacional da energia de Fisher
    E = integral (rho_x^2/rho) dx é proporcional ao operador
    -4 sqrt(rho)''/sqrt(rho), no interior da malha.

Fonte teórica:
    manuscrito/05_equations_conservation/05.4 - Variação da densidade e equilíbrio dinâmico.md
    manuscrito/notes/equations/Da energia de amplitude ao termo de Bohm.md

Classificação:
    Teste numérico/simbólico de variação. Não é previsão física.

Equação:
    delta/delta rho integral rho_x^2/rho dx
    = -4 (sqrt(rho))''/sqrt(rho)

Domínio e contorno:
    Intervalo 1D periódico [0, 2pi].

Parâmetros:
    Universais:
        nenhum
    Dados de aparelho/experimento:
        nenhum
    Numéricos:
        malha periódica.

Saída:
    saida_verificar_bohm_fisher_variacao.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def ddx_periodic(f: np.ndarray, dx: float) -> np.ndarray:
    return (np.roll(f, -1) - np.roll(f, 1)) / (2.0 * dx)


def d2dx2_periodic(f: np.ndarray, dx: float) -> np.ndarray:
    return (np.roll(f, -1) - 2.0 * f + np.roll(f, 1)) / (dx * dx)


def fisher_variational(rho: np.ndarray, dx: float) -> np.ndarray:
    rho_x = ddx_periodic(rho, dx)
    rho_xx = d2dx2_periodic(rho, dx)
    return -2.0 * rho_xx / rho + (rho_x * rho_x) / (rho * rho)


def bohm_operator_form(rho: np.ndarray, dx: float) -> np.ndarray:
    root = np.sqrt(rho)
    root_xx = d2dx2_periodic(root, dx)
    return -4.0 * root_xx / root


def main() -> None:
    rows = []
    for n in [200, 400, 800, 1600]:
        x = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
        dx = x[1] - x[0]
        rho = 1.5 + 0.2 * np.cos(x) + 0.1 * np.sin(2.0 * x)
        lhs = fisher_variational(rho, dx)
        rhs = bohm_operator_form(rho, dx)
        err = float(np.max(np.abs(lhs - rhs)))
        scale = float(np.max(np.abs(rhs)))
        rel = err / scale
        rows.append((n, err, rel))
    ok = rows[-1][2] < 1e-4

    lines: list[str] = []
    lines.append("# Saída — variação Fisher-Bohm\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Teste numérico/simbólico de variação. Não é previsão física.\n\n")
    lines.append("## Identidade verificada\n\n")
    lines.append("$$\n")
    lines.append("\\frac{\\delta}{\\delta\\rho}\\int\\frac{|\\nabla\\rho|^2}{\\rho}\\,dx\n")
    lines.append("=-4\\frac{\\Delta\\sqrt\\rho}{\\sqrt\\rho}.\n")
    lines.append("$$\n\n")
    lines.append("## Resultados de malha periódica\n\n")
    lines.append("| N | erro máximo | erro relativo |\n")
    lines.append("|---:|---:|---:|\n")
    for n, err, rel in rows:
        lines.append(f"| {n} | {err:.12e} | {rel:.12e} |\n")
    lines.append("\n## Veredito\n\n")
    lines.append("A checagem passou no refinamento usado.\n" if ok else "A checagem falhou na tolerância escolhida.\n")
    lines.append("\nEsta saída verifica a identidade diferencial em 1D periódica; a forma GDQ geral usa $\\Delta_g$ e domínio/contorno próprios.\n")

    out = OUT / "saida_verificar_bohm_fisher_variacao.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

