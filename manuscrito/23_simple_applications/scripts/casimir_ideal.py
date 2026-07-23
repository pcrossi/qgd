#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `casimir ideal` associada ao capítulo `23_simple_applications`.
Capítulo 23 — pressão de Casimir ideal.

Classificação:
    Avaliação direta do resultado universal de placas ideais.

Equação:
    P(a) = -pi^2 hbar c /(240 a^4).
"""

from __future__ import annotations

from pathlib import Path
import math


OUT = Path(__file__).with_name("saida_casimir_ideal.md")


def main() -> None:
    hbar = 1.054_571_817e-34
    c = 299_792_458.0
    separations = [100e-9, 200e-9, 500e-9, 1e-6, 2e-6]

    lines = [
        "---",
        'title: "Saída — Casimir ideal"',
        "---",
        "",
        "# Saída — Casimir ideal",
        "",
        "- fórmula: $P=-\\pi^2\\hbar c/(240a^4)$;",
        "- classificação: avaliação direta de resultado ideal universal.",
        "",
        "| separação $a$ | pressão [Pa] |",
        "|---:|---:|",
    ]
    for a in separations:
        pressure = -(math.pi**2 * hbar * c) / (240.0 * a**4)
        lines.append(f"| `{a:.1e}` m | `{pressure:.12e}` |")

    lines += [
        "",
        "Para placas reais, esse valor deve ser substituído por uma avaliação com",
        "$\\mathsf R_{\\rm plate}(\\omega,k,T)$.",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
