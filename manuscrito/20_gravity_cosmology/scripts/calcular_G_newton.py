#!/usr/bin/env python3
"""GDQ — Capítulo 20: avaliação reduzida de G.

Classificação:
    comparação fenomenológica forte.

O script avalia a fórmula reduzida:

    Pi_G = alpha^4 (1 + alpha) exp[-1/(2 alpha)] / chi_Fano

com:

    chi_Fano = 3 sqrt(2) / 5
    G = (hbar c / M_p^2) Pi_G.

O valor aceito de G entra apenas depois, na comparação final. A primeira linha
usa a alpha geométrica herdada do Capítulo 16; a segunda linha usa a referência
metrológica histórica para mostrar a sensibilidade.
"""

from __future__ import annotations

import math
from pathlib import Path


def pi_g_reduced(alpha: float, chi_fano: float) -> float:
    """Grupo adimensional reduzido da cadeia térmico-axial."""

    return alpha**4 * (1.0 + alpha) * math.exp(-1.0 / (2.0 * alpha)) / chi_fano


def main() -> None:
    chi_fano = 3.0 * math.sqrt(2.0) / 5.0
    hbar = 1.054_571_817e-34
    c = 299_792_458.0
    m_p = 1.672_621_925_95e-27
    G_acc = 6.674_30e-11

    alpha_cases = [
        ("alpha geométrica de Einstein", 137.036_082_448_164),
        ("alpha metrológica registrada", 137.035_999_084),
    ]

    pi_obs = G_acc * m_p**2 / (hbar * c)
    rows = []
    for label, alpha_inv in alpha_cases:
        alpha = 1.0 / alpha_inv
        pi_g = pi_g_reduced(alpha, chi_fano)
        G_gdq = hbar * c * pi_g / m_p**2
        rows.append(
            (
                label,
                alpha_inv,
                pi_g,
                G_gdq,
                (pi_g - pi_obs) / pi_obs,
                (G_gdq - G_acc) / G_acc,
            )
        )

    lines = [
        "---",
        'title: "Saída — cálculo reduzido de G"',
        "---",
        "",
        "# Saída — cálculo reduzido de G",
        "",
        "## Entradas estruturais",
        "",
        f"- $\\chi_{{\\rm Fano}}=3\\sqrt2/5={chi_fano:.12f}$",
        f"- $M_p={m_p:.12e}\\,{{\\rm kg}}$",
        "",
        "## Fórmula avaliada",
        "",
        "$$",
        "\\Pi_G^{\\rm GDQ}",
        "=",
        "\\frac{\\alpha^4(1+\\alpha)}{\\chi_{\\rm Fano}}",
        "e^{-1/(2\\alpha)}",
        "$$",
        "",
        "$$",
        "G_{\\rm GDQ}",
        "=",
        "\\frac{\\hbar c}{M_p^2}\\Pi_G^{\\rm GDQ}",
        "$$",
        "",
        "## Resultado GDQ reduzido",
        "",
        "| Caso | $\\alpha^{-1}$ | $\\Pi_G^{\\rm GDQ}$ | $G_{\\rm GDQ}$ | erro em $\\Pi_G$ | erro em $G$ |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for label, alpha_inv, pi_g, G_gdq, pi_err, G_err in rows:
        lines.append(
            f"| {label} | `{alpha_inv:.12f}` | `{pi_g:.12e}` | "
            f"`{G_gdq:.12e}` | `{pi_err:+.6%}` | `{G_err:+.6%}` |"
        )

    lines += [
        "",
        "## Comparação externa",
        "",
        "| Quantidade | Valor usado apenas para comparação |",
        "|---|---:|",
        f"| $\\Pi_G^{{\\rm obs}}$ | `{pi_obs:.12e}` |",
        f"| $G_{{\\rm acc}}$ | `{G_acc:.12e}` m³ kg⁻¹ s⁻² |",
        "",
        "## Classificação",
        "",
        "Comparação fenomenológica forte. O valor aceito não entra na fórmula; entra apenas na comparação final.",
        "O fechamento metrológico completo exige a Hessiana gravitacional cosmológica e o cálculo espectral do prefator.",
        "",
    ]

    out = Path(__file__).with_name("saida_calculo_G_newton.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
