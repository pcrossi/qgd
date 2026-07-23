#!/usr/bin/env python3
"""
GDQ — Capítulo 15 / background leptônico 8D estacionário.

Classificação:
    avaliação direta de quantidades já derivadas no background produto/bloco.

O script calcula os parâmetros que entram no critério de Schur:

    a_W = ||nabla_K A||_infty,
    a_f = ||nabla_K f_K||_infty,
    a_H = ||H_BK||_infty,
    eps = ||C_BK||,
    lambda_B_gap.

No background produto estacionário todos os canais mistos são nulos. Não há
engenharia inversa, alvo experimental ou Rosen--Morse ontológico.
"""

from __future__ import annotations

from pathlib import Path
import math


ALPHA_INV = 137.035999177
ALPHA = 1.0 / ALPHA_INV


def r_mu_reduced(alpha_inv: float = ALPHA_INV) -> float:
    alpha = 1.0 / alpha_inv
    return 1.5 * alpha_inv + 6.0 / 5.0 + 2.0 * alpha


def r_tau_from_q(r_mu: float, q: float = 2.0 / 3.0) -> float:
    a = math.sqrt(r_mu)
    A = 1.0 - q
    B = -2.0 * q * (1.0 + a)
    C = 1.0 + r_mu - q * (1.0 + a) ** 2
    disc = B * B - 4.0 * A * C
    if disc < 0.0:
        raise ValueError("a condição Q=2/3 não possui raiz real")
    y1 = (-B - math.sqrt(disc)) / (2.0 * A)
    y2 = (-B + math.sqrt(disc)) / (2.0 * A)
    return max(y1 * y1, y2 * y2)


def main() -> None:
    c_gamma = 1.0
    tau = 1.0
    r_max = 1.0

    a_warp = 0.0
    a_dilaton = 0.0
    a_torsion = 0.0
    eps_metric = 0.0

    lambda_b_gap = 0.5
    m_perp2 = c_gamma * tau / (r_max * r_max)
    j_mix = 0.0
    delta_schur = 0.0

    rmu = r_mu_reduced()
    rtau = r_tau_from_q(rmu)

    lines = [
        "---",
        'title: "Saída — background leptônico 8D estacionário"',
        "---",
        "",
        "# Saída — background leptônico 8D estacionário",
        "",
        "## Classificação",
        "",
        "Avaliação direta de quantidade já derivada no background estacionário",
        "produto/bloco da GDQ. Não é engenharia inversa e não usa alvo",
        "experimental.",
        "",
        "## Background avaliado",
        "",
        "$$",
        "g_8=g_B\\oplus g_K,",
        "\\qquad",
        "K=T^5\\text{ plano}.",
        "$$",
        "",
        "$$",
        "A(k)=\\text{constante},",
        "\\qquad",
        "f_K(k)=\\text{constante},",
        "\\qquad",
        "H_{BK}=0,",
        "\\qquad",
        "\\mathcal C_{BK}=0.",
        "$$",
        "",
        "## Valores físicos extraídos",
        "",
        "| quantidade | valor | origem |",
        "|---|---:|---|",
        f"| $a_W=\\|\\nabla_K A\\|_\\infty$ | `{a_warp:.15g}` | $A(k)$ constante |",
        f"| $a_f=\\|\\nabla_K f_K\\|_\\infty$ | `{a_dilaton:.15g}` | $f_K(k)$ constante |",
        f"| $a_H=\\|H_{{BK}}\\|_\\infty$ | `{a_torsion:.15g}` | torção sem bloco misto |",
        f"| $\\varepsilon=\\|\\mathcal C_{{BK}}\\|$ | `{eps_metric:.15g}` | métrica produto |",
        f"| $\\lambda_B^{{\\rm gap}}$ | `{lambda_b_gap:.15g}` | menor gap físico conservador |",
        "",
        "## Critério de Schur",
        "",
        "$$",
        "m_\\perp^2",
        "=",
        "C_\\gamma\\tau R_{\\max}^{-2}",
        "-",
        "\\left(c_Wa_W^2+c_fa_f^2+c_Ha_H^2+c_C\\varepsilon^2\\right).",
        "$$",
        "",
        "$$",
        "j_{\\rm mix}=b_Wa_W+b_fa_f+b_Ha_H+b_C\\varepsilon.",
        "$$",
        "",
        f"- $m_\\perp^2={m_perp2:.15g}$;",
        f"- $j_{{\\rm mix}}={j_mix:.15g}$;",
        f"- $\\Delta_{{\\rm Schur}}={delta_schur:.15g}$.",
        "",
        "$$",
        "\\frac{j_{\\rm mix}^2}{m_\\perp^2}",
        "=",
        "0",
        "<",
        "\\frac12.",
        "$$",
        "",
        "## Massas relativas resultantes",
        "",
        "| lépton | razão 8D |",
        "|---|---:|",
        "| $e$ | `1.000000000000000` |",
        f"| $\\mu$ | `{rmu:.15f}` |",
        f"| $\\tau$ | `{rtau:.15f}` |",
        "",
        "Como o complemento de Schur é nulo:",
        "",
        "$$",
        "R_\\ell^{(8)}=R_\\ell^{(0)}.",
        "$$",
        "",
    ]

    out = Path(__file__).with_name("saida_background_8d_estacionario.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
