#!/usr/bin/env python3
"""
GDQ — Capítulo 5 / Polarização canônica toy por Routh-Schwarz.

Objetivo:
    Ilustrar que, para rho positiva, carga Q fixa e normalização N_rho fixa,
    o funcional H[Pi,rho] = integral Pi^2/(2 A rho) é minimizado por
    Pi = (Q/N_rho) rho.

Fonte teórica:
    manuscrito/05_equations_conservation/05.7 - O que foi demonstrado e o que depende da reconstrução física.md
    manuscrito/notes/equations/Auditoria do termo canonico rho d_t S_R.md

Classificação:
    Ilustração de Routh/Cauchy-Schwarz. Não é previsão física.

Equação:
    H >= Q^2/(2 A N_rho), igualdade quando Pi = (Q/N_rho) rho.

Domínio e contorno:
    Intervalo 1D com quadratura trapezoidal.

Parâmetros:
    Universais:
        nenhum
    Dados de aparelho/experimento:
        nenhum
    Numéricos:
        perfis positivos arbitrários.

Saída:
    saida_verificar_polarizacao_canonica_toy.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def integrate(y: np.ndarray, x: np.ndarray) -> float:
    return float(np.trapezoid(y, x))


def main() -> None:
    x = np.linspace(0.0, 1.0, 5001)
    rho_raw = 1.2 + 0.4 * np.cos(2 * np.pi * x) + 0.2 * np.sin(6 * np.pi * x)
    rho = rho_raw / integrate(rho_raw, x)
    n_rho = integrate(rho, x)
    q = 1.0
    a = 2.0
    pi_min = (q / n_rho) * rho
    h_min_numeric = integrate(pi_min * pi_min / (2.0 * a * rho), x)
    h_min_bound = q * q / (2.0 * a * n_rho)
    rows = []
    for amp in [0.0, 0.1, 0.5, 1.0]:
        fluct = np.sin(2 * np.pi * x) - integrate(np.sin(2 * np.pi * x), x) * rho
        # Corrige a flutuação para ter carga zero.
        fluct = fluct - integrate(fluct, x) * rho / n_rho
        pi = pi_min + amp * fluct
        charge = integrate(pi, x)
        h = integrate(pi * pi / (2.0 * a * rho), x)
        rows.append((amp, charge, h, h - h_min_bound))
    ok = abs(h_min_numeric - h_min_bound) < 1e-10 and all(row[3] >= -1e-10 for row in rows)

    lines: list[str] = []
    lines.append("# Saída — polarização canônica toy\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Ilustração de Routh/Cauchy--Schwarz. Não é previsão física.\n\n")
    lines.append("## Desigualdade\n\n")
    lines.append("$$\n")
    lines.append("H[\\Pi,\\rho]=\\int\\frac{\\Pi^2}{2A\\rho}\\,d\\Sigma\n")
    lines.append("\\geq\n")
    lines.append("\\frac{Q^2}{2AN_\\rho}.\n")
    lines.append("$$\n\n")
    lines.append("A igualdade ocorre para:\n\n")
    lines.append("$$\n")
    lines.append("\\Pi=\\frac{Q}{N_\\rho}\\rho.\n")
    lines.append("$$\n\n")
    lines.append("## Parâmetros toy\n\n")
    lines.append(f"- $A={a}$.\n")
    lines.append(f"- $Q={q}$.\n")
    lines.append(f"- $N_\\rho={n_rho:.12g}$.\n")
    lines.append(f"- Limite inferior: `{h_min_bound:.12e}`.\n\n")
    lines.append("## Perturbações de carga zero em torno do minimizador\n\n")
    lines.append("| amplitude | carga | $H$ | excesso $H-H_{min}$ |\n")
    lines.append("|---:|---:|---:|---:|\n")
    for amp, charge, h, excess in rows:
        lines.append(f"| {amp:.6g} | {charge:.12e} | {h:.12e} | {excess:.12e} |\n")
    lines.append("\n## Veredito\n\n")
    lines.append("A checagem passou.\n" if ok else "A checagem falhou.\n")
    lines.append("\nEsta saída ilustra o minimizador condicionado. Ela não prova que a dinâmica GDQ seleciona esse setor sem a ponte global--local/medida.\n")

    out = OUT / "saida_verificar_polarizacao_canonica_toy.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

