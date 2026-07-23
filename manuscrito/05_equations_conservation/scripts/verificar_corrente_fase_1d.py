#!/usr/bin/env python3
"""
GDQ — Capítulo 5 / Corrente de fase em 1D.

Objetivo:
    Ilustrar que divergência nula preserva carga integrada e que fluxo
    através do bordo altera a carga conforme o teorema da divergência.

Fonte teórica:
    manuscrito/05_equations_conservation/05.3 - Variação da fase e conservação do fluxo.md
    manuscrito/notes/equations/Derivação da corrente de fase.md

Classificação:
    Ilustração de conservação de corrente. Não é previsão física.

Equação:
    dQ/dt = -J(borda direita) + J(borda esquerda)

Domínio e contorno:
    Intervalo 1D [0,1]. Compara corrente constante e corrente com fluxo
    líquido de bordo.

Parâmetros:
    Universais:
        nenhum
    Dados de aparelho/experimento:
        nenhum
    Numéricos:
        malha 1D.

Saída:
    saida_verificar_corrente_fase_1d.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def divergence(j: np.ndarray, x: np.ndarray) -> np.ndarray:
    return np.gradient(j, x)


def main() -> None:
    x = np.linspace(0.0, 1.0, 1001)
    currents = {
        "constante": np.ones_like(x) * 2.0,
        "linear": 1.0 + 0.3 * x,
        "sem_fluxo_liquido": 1.0 + 0.2 * np.sin(2.0 * np.pi * x),
    }
    rows = []
    for name, j in currents.items():
        div_int = float(np.trapezoid(divergence(j, x), x))
        boundary_balance = float(j[-1] - j[0])
        charge_rate = -boundary_balance
        rows.append((name, div_int, boundary_balance, charge_rate))

    ok = all(abs(div_int - balance) < 1e-6 for _, div_int, balance, _ in rows)

    lines: list[str] = []
    lines.append("# Saída — corrente de fase em 1D\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Ilustração de conservação de corrente. Não é previsão física.\n\n")
    lines.append("## Identidade verificada\n\n")
    lines.append("Em um intervalo:\n\n")
    lines.append("$$\n")
    lines.append("\\int_0^1\\partial_xJ\\,dx=J(1)-J(0).\n")
    lines.append("$$\n\n")
    lines.append("Logo:\n\n")
    lines.append("$$\n")
    lines.append("\\frac{dQ}{dt}=-J(1)+J(0).\n")
    lines.append("$$\n\n")
    lines.append("## Resultados\n\n")
    lines.append("| caso | $\\int\\partial_xJdx$ | $J(1)-J(0)$ | $dQ/dt$ |\n")
    lines.append("|---|---:|---:|---:|\n")
    for name, div_int, boundary_balance, charge_rate in rows:
        lines.append(f"| {name} | {div_int:.12e} | {boundary_balance:.12e} | {charge_rate:.12e} |\n")
    lines.append("\n## Veredito\n\n")
    lines.append("A checagem passou.\n" if ok else "A checagem falhou.\n")
    lines.append("\nEsta saída ilustra conservação integrada; a corrente GDQ real depende de $\\mathcal U$, $g$ e $S_R$.\n")

    out = OUT / "saida_verificar_corrente_fase_1d.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

