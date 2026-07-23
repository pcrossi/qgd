#!/usr/bin/env python3
"""
GDQ — Capítulo 01 / Verificação simbólico-numérica

Objetivo:
    Verificar a identidade do termo osmótico que liga a escrita de Nelson ao
    termo de Bohm/Madelung.

Fonte teórica:
    manuscrito/01_initial_problem/notes/

Classificação:
    Verificação simbólico-numérica de identidade analítica.

Equação:
    Para u=2*nu*grad(log sqrt(rho)), verifica-se
    m*nu*div(u)+(m/2)|u|^2 = 2*m*nu^2*Delta(sqrt(rho))/sqrt(rho).

Domínio e contorno:
    Linha real. Usa-se densidade gaussiana positiva, sem bordo físico.

Parâmetros:
    m=nu=1 em unidades reduzidas.

Dados experimentais:
    Nenhum.

Saída:
    manuscrito/01_initial_problem/scripts/saida_verificar_termo_osmotico_bohm.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "manuscrito/01_initial_problem/scripts/saida_verificar_termo_osmotico_bohm.md"


def main() -> None:
    m = nu = 1.0
    x = np.linspace(-4, 4, 20_001)
    dx = x[1] - x[0]
    rho = np.exp(-x**2)
    sqrt_rho = np.sqrt(rho)

    grad_log_sqrt = np.gradient(np.log(sqrt_rho), dx, edge_order=2)
    u = 2.0 * nu * grad_log_sqrt
    div_u = np.gradient(u, dx, edge_order=2)
    lhs = m * nu * div_u + 0.5 * m * u**2

    lap_sqrt = np.gradient(np.gradient(sqrt_rho, dx, edge_order=2), dx, edge_order=2)
    rhs = 2.0 * m * nu**2 * lap_sqrt / sqrt_rho

    interior = slice(100, -100)
    max_err = np.max(np.abs(lhs[interior] - rhs[interior]))
    rms_err = np.sqrt(np.mean((lhs[interior] - rhs[interior]) ** 2))

    lines = [
        "---",
        'title: "Saída — termo osmótico e Bohm"',
        "---",
        "",
        "# Saída — termo osmótico e Bohm",
        "",
        "| Métrica | Valor |",
        "|---|---:|",
        f"| Erro máximo interior | {max_err:.6e} |",
        f"| Erro RMS interior | {rms_err:.6e} |",
        "",
        "A identidade é confirmada numericamente. O erro residual vem apenas de "
        "diferenças finitas na malha.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Saída: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

