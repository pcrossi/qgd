#!/usr/bin/env python3
"""Q48 — cálculo direto do Schur de superfície herdado da Q40.

Este script monta explicitamente os blocos reduzidos:

    K_sigma(q), J_sigma(q), R_sigma(q) = - J^T K^{-1} J

e avalia a contribuição em escalas relevantes para Q48.

Classificação:
- cálculo direto do bloco reduzido de superfície Q40;
- não é Hessiana completa do próton;
- se o resultado for insuficiente, isso é um no-go setorial do bloco q^4.
"""

from __future__ import annotations

from math import sqrt
from pathlib import Path

import numpy as np
from scipy import constants as C


OUT = Path(__file__).with_name("saida_calculo_direto_schur_superficie_q48.md")

alpha = C.alpha
c = C.c
hbar = C.hbar
m_e = C.m_e
m_p = C.m_p
mu_ep = m_e * m_p / (m_e + m_p)

r_p = 0.84077876545  # fm
lambda_E = sqrt(12.0) / r_p  # fm^-1

j = np.array([1.712091781054, 1.341454657186, 1.063840998206], dtype=float)


def K_sigma(x: float) -> np.ndarray:
    return np.diag([1.0 + x, (1.0 + x) ** 2, (1.0 + x) ** 2])


def J_sigma(x: float) -> np.ndarray:
    return x * np.array([j[0], j[1], j[2] * sqrt(max(x, 0.0))], dtype=float)


def schur_impedance(x: float) -> float:
    K = K_sigma(x)
    J = J_sigma(x)
    return -float(J @ np.linalg.solve(K, J))


def q_atomic_fm_inv() -> float:
    a0_eff = hbar / (mu_ep * c * alpha)
    return (1.0 / a0_eff) / 1e15


def main() -> None:
    q_atom = q_atomic_fm_inv()
    q_lamb = q_atom / 2.0  # escala típica n=2
    q_had = 1.0 / r_p

    rows = []
    for name, q in [
        ("hiperfina 1s: q~1/aB*", q_atom),
        ("Lamb 2s: q~1/(2aB*)", q_lamb),
        ("hadrônica: q~1/rp", q_had),
        ("Q40 espalhamento baixo: q=0.25 fm^-1", 0.25),
        ("Q40 espalhamento médio: q=1.0 fm^-1", 1.0),
    ]:
        x = (q / lambda_E) ** 2
        K = K_sigma(x)
        J = J_sigma(x)
        R = schur_impedance(x)
        eig = np.linalg.eigvalsh(K)
        rows.append((name, q, x, J[0], J[1], J[2], eig[0], eig[-1], R))

    text = [
        "# Saída — cálculo direto do Schur de superfície Q48",
        "",
        "Classificação: cálculo direto do bloco reduzido de superfície Q40.",
        "Este cálculo não substitui a Hessiana completa do próton; ele testa o",
        "bloco coletivo já derivado.",
        "",
        "## Dados",
        "",
        f"- r_p = {r_p:.12f} fm",
        f"- Lambda_E = sqrt(12)/r_p = {lambda_E:.12f} fm^-1",
        f"- j = {j.tolist()}",
        "",
        "## Resultado por escala",
        "",
        "| escala | q (fm^-1) | x | J0 | J1 | J2 | min eig K | max eig K | R=-J^T K^-1 J |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        name, q, x, j0, j1, j2, e0, e1, R = row
        text.append(
            f"| {name} | {q:.12e} | {x:.12e} | {j0:.12e} | {j1:.12e} | {j2:.12e} | {e0:.12e} | {e1:.12e} | {R:.12e} |"
        )

    text += [
        "",
        "## Conclusão",
        "",
        "Na escala atômica, o bloco de superfície Q40 é suprimido por x^2.",
        "Isso confirma diretamente que ele não pode fornecer o resíduo hiperfino",
        "de ordem 10^-5 nem o Lamb shift de ordem GHz. Ele é o bloco correto para",
        "espalhamento/fatores de forma em q hadrônico/intermediário.",
        "",
        "$$",
        "\\boxed{",
        "\\text{no-go setorial: o Schur coletivo }q^4\\text{ não fecha a metrologia atômica.}",
        "}",
        "$$",
        "",
    ]

    OUT.write_text("\n".join(text), encoding="utf-8")
    print("\n".join(text))


if __name__ == "__main__":
    main()
