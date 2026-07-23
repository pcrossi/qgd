#!/usr/bin/env python3
"""
GDQ — Capítulo 18 / coeficiente do cap Ricci--Bohm.

Objetivo:
    Verificar que C_GDQ = pi sai de Gauss--Bonnet no cap transversal
    hemisférico com bordo geodésico, e calcular a tensão reduzida associada.

Classificação:
    Avaliação direta de quantidade derivada no setor transversal reduzido.
    Não usa QCD/Yang--Mills como ação fundamental e não ajusta ao alvo
    hadrônico.

Saída:
    scripts/saida_coeficiente_cap_ricci_bohm.md
"""

from __future__ import annotations

from pathlib import Path
import math


HBARC_GEV_FM = 0.1973269804
R_PERP_FM = 0.86
SIGMA_HAD_GEV_PER_FM = 0.89


def main() -> None:
    r = R_PERP_FM
    cap_area = 2.0 * math.pi * r * r
    disk_area = math.pi * r * r
    scalar_curvature = 2.0 / (r * r)
    int_r_da = scalar_curvature * cap_area
    c_gdq = 0.25 * int_r_da
    delta = HBARC_GEV_FM / r
    sigma = c_gdq * HBARC_GEV_FM / (r * r)
    sigma_gev2 = sigma * HBARC_GEV_FM
    sqrt_sigma = math.sqrt(sigma_gev2)
    err = (sigma - SIGMA_HAD_GEV_PER_FM) / SIGMA_HAD_GEV_PER_FM

    lines = [
        "# Saída — coeficiente do cap Ricci-Bohm",
        "",
        "Classificação: avaliação direta de quantidade derivada.",
        "",
        "| quantidade | valor |",
        "|---|---:|",
        f"| r_perp fm | {r:.12f} |",
        f"| área intrínseca cap fm^2 | {cap_area:.12f} |",
        f"| área projetada disco fm^2 | {disk_area:.12f} |",
        f"| R2 fm^-2 | {scalar_curvature:.12f} |",
        f"| integral R2 dA | {int_r_da:.12f} |",
        f"| C_GDQ=(1/4) integral R2 dA | {c_gdq:.12f} |",
        f"| Delta GeV | {delta:.12f} |",
        f"| sigma GeV/fm | {sigma:.12f} |",
        f"| sigma GeV^2 | {sigma_gev2:.12f} |",
        f"| sqrt(sigma) GeV | {sqrt_sigma:.12f} |",
        f"| desvio vs 0.89 GeV/fm | {err:.6%} |",
        "",
        "Interpretação: C_GDQ=pi vem do índice de curvatura do cap Ricci--Bohm.",
    ]

    out = Path(__file__).with_name("saida_coeficiente_cap_ricci_bohm.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

