#!/usr/bin/env python3
"""
GDQ — Capítulo 15 / calibração metrológica de escala.

Classificação:
    verificação simbólico-numérica de relações dimensionais.

Este script não tenta derivar a unidade MeV do nada. Ele verifica:

1. autovalores normalizados produzem razões independentes de escala;
2. uma escala E0 converte números puros em energias;
3. calibrar por M_e preserva previsões de razões;
4. a ponte beta Q_beta=(delta_B-1) M_e c^2 é uma calibração metrológica,
   não uma massa absoluta sem entrada dimensional.

O script é autocontido e escreve a saída Markdown usada pelo capítulo.
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv

    r_e = 1.0
    r_mu = 1.5 * alpha_inv + 6.0 / 5.0 + 2.0 * alpha

    m_e_mev = 0.51099895000
    m_mu_from_ratio = m_e_mev * r_mu

    # Referência posterior de comparação, não entrada na fórmula.
    m_mu_ref = 105.6583755
    err_mu = (m_mu_from_ratio - m_mu_ref) / m_mu_ref

    # Média geométrica do espaço de Einstein usada como número puro.
    delta_b = math.log(2.0 * math.pi**2) * (3.0 * math.sqrt(2.0) / 5.0)
    q_beta_from_me = (delta_b - 1.0) * m_e_mev

    # Valor metrológico ilustrativo do endpoint beta livre usado como padrão
    # de comparação; não entra na dedução de delta_B.
    q_beta_ref = 0.782333
    m_e_from_beta = q_beta_ref / (delta_b - 1.0)
    err_me_beta = (m_e_from_beta - m_e_mev) / m_e_mev

    e0_a = 1.0
    e0_b = 7.3
    lambda_e_hat = r_e * r_e
    lambda_mu_hat = r_mu * r_mu
    ratio_a = (e0_a * math.sqrt(lambda_mu_hat)) / (e0_a * math.sqrt(lambda_e_hat))
    ratio_b = (e0_b * math.sqrt(lambda_mu_hat)) / (e0_b * math.sqrt(lambda_e_hat))

    lines = [
        "---",
        'title: "Saída — calibração metrológica"',
        "---",
        "",
        "# Saída — calibração metrológica",
        "",
        "## 1. Razão independente de escala",
        "",
        "| escala $E_0$ | $M_\\mu/M_e$ reconstruído |",
        "|---:|---:|",
        f"| `{e0_a:.6f}` | `{ratio_a:.12f}` |",
        f"| `{e0_b:.6f}` | `{ratio_b:.12f}` |",
        "",
        "A razão não muda quando a régua dimensional é trocada.",
        "",
        "## 2. Calibração por $M_e$",
        "",
        "| quantidade | valor |",
        "|---|---:|",
        f"| $M_e$ usado como padrão metrológico | `{m_e_mev:.11f}` MeV |",
        f"| $R_\\mu^{{\\rm GDQ}}$ | `{r_mu:.12f}` |",
        f"| $M_\\mu=M_eR_\\mu$ | `{m_mu_from_ratio:.9f}` MeV |",
        f"| referência posterior $M_\\mu$ | `{m_mu_ref:.9f}` MeV |",
        f"| erro relativo | `{err_mu:.12e}` |",
        "",
        "## 3. Ponte beta como calibração",
        "",
        "$$",
        "\\delta_B=\\ln(2\\pi^2)\\frac{3\\sqrt2}{5}.",
        "$$",
        "",
        "| quantidade | valor |",
        "|---|---:|",
        f"| $\\delta_B$ | `{delta_b:.12f}` |",
        f"| $(\\delta_B-1)M_e$ | `{q_beta_from_me:.9f}` MeV |",
        f"| $Q_\\beta$ comparativo | `{q_beta_ref:.9f}` MeV |",
        f"| $M_e=Q_\\beta/(\\delta_B-1)$ | `{m_e_from_beta:.11f}` MeV |",
        f"| erro relativo de $M_e$ reconstruído | `{err_me_beta:.12e}` |",
        "",
        "## Classificação",
        "",
        "Verificação de calibração metrológica. O script não deriva a unidade MeV",
        "sem entrada dimensional; ele mostra como números geométricos puros viram",
        "energias após uma régua física declarada.",
        "",
    ]

    out = Path(__file__).with_name("saida_verificar_calibracao_metrologica.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
