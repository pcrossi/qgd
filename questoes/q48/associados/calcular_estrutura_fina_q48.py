#!/usr/bin/env python3
"""Q48 — comparação entre espectro exato Dirac e expansão de estrutura fina."""

from __future__ import annotations

from math import sqrt
from pathlib import Path

from scipy import constants as C


OUT = Path(__file__).with_name("saida_estrutura_fina_q48.md")

alpha = C.alpha
c = C.c
e = C.e
m_e = C.m_e
m_p = C.m_p
mu = m_e * m_p / (m_e + m_p)
mu_c2_eV = mu * c**2 / e


def dirac_binding(n: int, kappa: int) -> float:
    gamma = sqrt(kappa * kappa - alpha * alpha)
    denom = n - abs(kappa) + gamma
    energy = mu_c2_eV / sqrt(1.0 + (alpha / denom) ** 2)
    return energy - mu_c2_eV


def fine_expansion(n: int, j: float) -> float:
    return (
        -mu_c2_eV * alpha**2 / (2 * n**2)
        -mu_c2_eV * alpha**4 / (2 * n**4) * (n / (j + 0.5) - 0.75)
    )


def main() -> None:
    cases = [
        ("1s1/2", 1, -1, 0.5),
        ("2s1/2", 2, -1, 0.5),
        ("2p1/2", 2, +1, 0.5),
        ("2p3/2", 2, -2, 1.5),
        ("3d5/2", 3, -3, 2.5),
    ]
    text = [
        "# Saída — estrutura fina Q48",
        "",
        "Classificação: teste de consistência entre fórmula exata e expansão em",
        "potências de alpha.",
        "",
        "| nível | E Dirac bind (eV) | expansão O(alpha^4) (eV) | diferença (eV) |",
        "|---|---:|---:|---:|",
    ]
    for label, n, kappa, j in cases:
        exact = dirac_binding(n, kappa)
        approx = fine_expansion(n, j)
        text.append(f"| {label} | {exact:.12f} | {approx:.12f} | {exact-approx:.6e} |")

    split_exact = dirac_binding(2, -2) - dirac_binding(2, +1)
    split_approx = fine_expansion(2, 1.5) - fine_expansion(2, 0.5)
    text += [
        "",
        "## Separação fina 2p3/2 - 2p1/2",
        "",
        f"- Exata Dirac = {split_exact:.12e} eV",
        f"- Expansão O(alpha^4) = {split_approx:.12e} eV",
        f"- Diferença = {split_exact-split_approx:.6e} eV",
        "",
    ]
    OUT.write_text("\n".join(text), encoding="utf-8")
    print("\n".join(text))


if __name__ == "__main__":
    main()
