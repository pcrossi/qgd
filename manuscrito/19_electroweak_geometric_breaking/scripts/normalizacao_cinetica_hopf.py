#!/usr/bin/env python3
"""
GDQ — Capítulo 19 / Normalização cinética do modo de Hopf

Objetivo:
    Calcular a norma interna do potencial de 2-forma associado ao harmônico
    eletrofraco l=1 no S^3.

Classificação:
    Avaliação direta de quantidade já derivada. Não usa dados experimentais.

Saída:
    scripts/saida_normalizacao_cinetica_hopf.md
"""

from pathlib import Path


def main() -> None:
    radius = 1.998411184770
    tau = 1.0
    lambda_l1 = 3.0 / radius**2
    mean_y2 = 0.25
    norm_a2 = mean_y2 / lambda_l1
    z_beta_over_c = tau * norm_a2

    lines = [
        "# Saída — normalização cinética do modo de Hopf",
        "",
        "Classificação: avaliação direta de quantidade derivada.",
        "",
        "| quantidade | valor |",
        "|---|---:|",
        f"| R | {radius:.12f} |",
        f"| lambda_l1=3/R^2 | {lambda_l1:.12f} |",
        f"| <Y^2> | {mean_y2:.12f} |",
        f"| <|A_EW|^2> | {norm_a2:.12f} |",
        f"| Z_beta/C_GDQ | {z_beta_over_c:.12f} |",
        "",
        "Interpretação: a integral interna está fechada; a conversão para GeV exige o prefator dimensional/causal global.",
    ]

    out = Path(__file__).with_name("saida_normalizacao_cinetica_hopf.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
