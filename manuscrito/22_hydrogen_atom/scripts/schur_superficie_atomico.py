#!/usr/bin/env python3
"""
GDQ — Capítulo 22 / Hidrogênio

Objetivo:
    Avaliar diretamente o bloco coletivo de superfície do próton em escalas
    atômicas e hadrônicas:

        R_sigma(q) = - J_sigma(q)^T K_sigma(q)^(-1) J_sigma(q).

Classificação:
    Cálculo direto reduzido/no-go setorial. Mostra que o bloco coletivo q^4 é
    suprimido demais em q atômico para fechar a hiperfina ou o Lamb shift, mas
    é relevante em escalas de fator de forma.

Saída:
    saida_schur_superficie_atomico.md
"""

from __future__ import annotations

from math import sqrt
from pathlib import Path

import numpy as np
from scipy import constants as C


OUT = Path(__file__).with_name("saida_schur_superficie_atomico.md")

alpha = C.alpha
c = C.c
hbar = C.hbar
m_e = C.m_e
m_p = C.m_p
mu_ep = m_e * m_p / (m_e + m_p)

r_p = 0.84077876545  # fm
lambda_E = sqrt(12.0) / r_p
j = np.array([1.712091781054, 1.341454657186, 1.063840998206], dtype=float)


def K_sigma(x: float) -> np.ndarray:
    return np.diag([1.0 + x, (1.0 + x) ** 2, (1.0 + x) ** 2])


def J_sigma(x: float) -> np.ndarray:
    return x * np.array([j[0], j[1], j[2] * sqrt(max(x, 0.0))], dtype=float)


def schur(x: float) -> float:
    K = K_sigma(x)
    J = J_sigma(x)
    return -float(J @ np.linalg.solve(K, J))


def q_bohr_fm_inv() -> float:
    a0_eff = hbar / (mu_ep * c * alpha)
    return (1.0 / a0_eff) / 1e15


def main() -> None:
    q_atom = q_bohr_fm_inv()
    rows = [
        ("hiperfina 1s", q_atom),
        ("Lamb 2s", q_atom / 2.0),
        ("hadrônica 1/r_p", 1.0 / r_p),
        ("espalhamento baixo", 0.25),
        ("espalhamento médio", 1.0),
    ]

    lines = [
        "---",
        'title: "Saída — Schur de superfície em escalas atômicas"',
        "---",
        "",
        "# Saída — Schur de superfície em escalas atômicas",
        "",
        "Classificação: cálculo direto reduzido/no-go setorial.",
        "",
        f"- $r_p={r_p:.12f}$ fm",
        f"- $\\Lambda_E=\\sqrt{{12}}/r_p={lambda_E:.12f}$ fm$^{{-1}}$",
        "",
        "$$",
        "\\mathsf R_\\Sigma(q)",
        "=",
        "-J_\\Sigma(q)^T K_\\Sigma(q)^{-1}J_\\Sigma(q),",
        "\\qquad",
        "x=\\frac{q^2}{\\Lambda_E^2}.",
        "$$",
        "",
        "| escala | $q$ [fm$^{-1}$] | $x$ | min eig $K$ | max eig $K$ | $\\mathsf R_\\Sigma$ |",
        "|---|---:|---:|---:|---:|---:|",
    ]

    for name, q in rows:
        x = (q / lambda_E) ** 2
        eig = np.linalg.eigvalsh(K_sigma(x))
        lines.append(
            f"| {name} | `{q:.12e}` | `{x:.12e}` | `{eig[0]:.12e}` | `{eig[-1]:.12e}` | `{schur(x):.12e}` |"
        )

    lines += [
        "",
        "Conclusão: em escala atômica, $x\\ll1$ e o Schur coletivo é de ordem",
        "$x^2$. Portanto esse bloco não fecha o resíduo hiperfino de ordem",
        "$10^{-5}$ nem o Lamb shift. Ele pertence ao setor de fatores de forma",
        "em escalas hadrônicas/intermediárias.",
        "",
    ]

    text = "\n".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
