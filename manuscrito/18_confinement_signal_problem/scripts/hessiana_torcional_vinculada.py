#!/usr/bin/env python3
"""
GDQ — Capítulo 18 / Hessiana torsional vinculada.

Objetivo:
    Avaliar a Hessiana radial homogênea da garganta com carga torsional
    conservada:

        K_R = 6*(3*R^2 - 8*tau)/R^4.

Classificação:
    Avaliação direta de Hessiana setorial já derivada.

Saída:
    scripts/saida_hessiana_torcional_vinculada.md
"""

from __future__ import annotations

from pathlib import Path


R = 1.03707435228632
TAU = 0.274900522513626


def main() -> None:
    ratio = R * R / TAU
    threshold = 8.0 / 3.0
    k_r = 6.0 * (3.0 * R * R - 8.0 * TAU) / (R**4)
    inv = 1.0 / k_r

    lines = [
        "# Saída — Hessiana torsional vinculada",
        "",
        "Classificação: avaliação direta de Hessiana setorial.",
        "",
        "| quantidade | valor |",
        "|---|---:|",
        f"| R | {R:.14f} |",
        f"| tau | {TAU:.15f} |",
        f"| R^2/tau | {ratio:.14f} |",
        f"| limiar 8/3 | {threshold:.14f} |",
        f"| K_R | {k_r:.14f} |",
        f"| K_R^-1 | {inv:.14f} |",
        "",
        f"Estável no modo homogêneo vinculado: {k_r > 0 and ratio > threshold}.",
    ]

    out = Path(__file__).with_name("saida_hessiana_torcional_vinculada.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

