#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `gmenos2 termo lider` associada ao capítulo `16_fine_structure_zeeman_gminus2`.

GDQ — Capítulo 16 / termo líder de g-2.

Calcula:

    a1 = alpha/(2*pi)
    g1 = 2*(1+a1)

e compara com valores de referência já registrados em setor Zeeman/g-2. A comparação é
fenomenológica; os resíduos não são ajustados.
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_gmenos2_termo_lider.md"

    cases = [
        ("alpha metrologica registrada", 137.035999177),
        ("alpha geometrica GDQ", 137.036082448164),
    ]
    g_e_ref = 2.002319304361180
    a_mu_ref = 116592059e-11

    rows = []
    for label, alpha_inv in cases:
        alpha = 1.0 / alpha_inv
        a1 = alpha / (2.0 * math.pi)
        g1 = 2.0 * (1.0 + a1)
        rows.append((label, alpha_inv, a1, g1, g_e_ref - g1, a_mu_ref - a1))

    lines = [
        "# Saída — termo líder de g-2",
        "",
        "Classificação: avaliação direta do termo líder; não é metrologia completa.",
        "",
        "| caso | alpha^-1 | a1 | g1 | g_e_ref-g1 | a_mu_ref-a1 |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row[0]} | {row[1]:.12f} | {row[2]:.15e} | {row[3]:.15f} | {row[4]:.15e} | {row[5]:.15e} |"
        )
    lines += [
        "",
        "Interpretação: $a_1=\\alpha/(2\\pi)$ é o termo líder geométrico. Os",
        "resíduos indicam canais superiores da Hessiana física, não parâmetros a",
        "ajustar dentro deste capítulo.",
    ]
    text = "\n".join(lines) + "\n"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
