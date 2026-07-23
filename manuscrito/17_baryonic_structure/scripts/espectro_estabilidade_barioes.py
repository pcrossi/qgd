#!/usr/bin/env python3
"""
GDQ — Capítulo 17 / espectro líder e estabilidade bariônica.

Classificação:
    avaliação direta de fórmulas reduzidas de estabilidade.

O script registra:

1. momento de inércia de superfície:
       I_rot = 3 M_p r_p^2 / 10;
2. escala rotacional líder:
       E_rot = 5 (hbar c)^2 / (M_p r_p^2);
3. teste qualitativo de proximidade com Delta(1232);
4. estabilidade topológica do próton como setor com carga de Cauchy/resíduo
   inteiro preservado.
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    hbarc = 197.3269804  # MeV fm
    alpha = 1.0 / 137.035999177
    me = 0.51099895000
    mp_ratio = 6.0 * math.pi**5 + alpha * (3.0 * math.pi / 2.0 + 3.0 / (4.0 * math.pi**3))
    mp = mp_ratio * me
    r_p = 0.840778765432
    i_rot = 0.3 * mp * r_p * r_p
    e_rot = 5.0 * hbarc * hbarc / (mp * r_p * r_p)
    m_delta_pred = mp + e_rot
    m_delta_ref = 1232.0
    rel_delta = (m_delta_pred - m_delta_ref) / m_delta_ref

    lines = [
        "---",
        'title: "Saída — espectro e estabilidade bariônica"',
        "---",
        "",
        "# Saída — espectro e estabilidade bariônica",
        "",
        "## Momento de inércia reduzido",
        "",
        "$$",
        "I_{\\rm rot}",
        "=",
        "\\frac12 M_p\\frac35r_p^2",
        "=",
        "\\frac{3}{10}M_pr_p^2.",
        "$$",
        "",
        "## Escala rotacional líder",
        "",
        "$$",
        "E_{\\rm rot}",
        "=",
        "\\frac{5(\\hbar c)^2}{M_pr_p^2}.",
        "$$",
        "",
        "| quantidade | valor |",
        "|---|---:|",
        f"| $M_p$ reduzido | `{mp:.9f}` MeV |",
        f"| $r_p$ | `{r_p:.12f}` fm |",
        f"| $I_{{\\rm rot}}$ | `{i_rot:.9f}` MeV fm$^2$ |",
        f"| $E_{{\\rm rot}}$ | `{e_rot:.9f}` MeV |",
        f"| $M_p+E_{{\\rm rot}}$ | `{m_delta_pred:.9f}` MeV |",
        f"| $\\Delta(1232)$ referência | `{m_delta_ref:.9f}` MeV |",
        f"| erro relativo | `{rel_delta:.12e}` |",
        "",
        "## Estabilidade estrutural",
        "",
        "No setor que preserva carga de Cauchy, fluxo de Noether e classe topológica,",
        "o próton não decai continuamente para o vácuo. O nêutron preserva número",
        "bariônico, mas possui cisalhamento torsional antiparalelo e por isso abre",
        "canal dinâmico de decaimento beta.",
        "",
        "## Classificação",
        "",
        "A escala rotacional é aproximação líder. O espectro completo de modos",
        "radiais, torsionais e de garganta exige diagonalização completa da",
        "Hessiana bariônica física.",
        "",
    ]

    out = Path(__file__).with_name("saida_espectro_estabilidade_barioes.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
