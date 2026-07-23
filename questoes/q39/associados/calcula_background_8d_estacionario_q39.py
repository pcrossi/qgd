#!/usr/bin/env python3
"""Q39 — avaliação direta do background leptônico 8D estacionário.

Este script avalia os parâmetros físicos que entram no critério de Schur
da Hessiana 8D:

    a_W = ||nabla_K A||_infty
    a_f = ||nabla_K f_K||_infty
    a_H = ||H_BK||_infty
    eps = ||C_BK||
    lambda_B_gap

Classificação: avaliação direta de quantidade já derivada no background
estacionário produto/bloco da GDQ. Não usa massas experimentais, não usa
Rosen--Morse como ontologia e não ajusta parâmetros ao alvo.
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


def evaluate_stationary_product_background() -> dict[str, float | str]:
    """Avalia o background leptônico 8D estacionário produto.

    No background produto oficial:

        g_8 = g_B oplus g_K,
        A(k) = const,
        f_K(k) = const,
        H_BK = 0,
        C_BK = 0.

    Logo todos os canais mistos são nulos. O gap do bloco 3D é escolhido como
    o menor gap físico já demonstrado na ponte C3, Delta_0=1/2. Esse valor é
    mais conservador que os gaps horizontal/radial reduzidos 3/2.
    """

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

    return {
        "background": "produto_estacionario_leptonico",
        "a_W": a_warp,
        "a_f": a_dilaton,
        "a_H": a_torsion,
        "epsilon_metric": eps_metric,
        "lambda_B_gap": lambda_b_gap,
        "m_perp2": m_perp2,
        "j_mix": j_mix,
        "delta_schur": delta_schur,
        "R_e_8": 1.0,
        "R_mu_8": rmu,
        "R_tau_8": rtau,
        "alpha_inv": ALPHA_INV,
        "status": "subcritico_exato",
    }


def main() -> None:
    base = Path(__file__).resolve().parent
    out = evaluate_stationary_product_background()

    lines = [
        "# Q39 — avaliação direta do background leptônico 8D estacionário",
        "",
        "## Classificação",
        "",
        "Avaliação direta de quantidade já derivada no background estacionário",
        "produto/bloco da GDQ. Não é engenharia inversa e não usa alvo",
        "experimental. A normalização usada é a normalização primitiva comum",
        "`C_gamma=tau=R_max=1`.",
        "",
        "## Background avaliado",
        "",
        "O background estacionário leptônico produto é:",
        "",
        "$$",
        "g_8=g_B\\oplus g_K,",
        "\\qquad",
        "K=T^5\\text{ plano},",
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
        "Portanto o background não possui warp interno, dilaton interno",
        "não homogêneo, torção mista nem bloco métrico misto.",
        "",
        "## Valores físicos extraídos",
        "",
        "| quantidade | valor | origem |",
        "|---|---:|---|",
        f"| `a_W=||nabla_K A||_infty` | `{out['a_W']:.15g}` | `A(k)` constante |",
        f"| `a_f=||nabla_K f_K||_infty` | `{out['a_f']:.15g}` | `f_K(k)` constante |",
        f"| `a_H=||H_BK||_infty` | `{out['a_H']:.15g}` | torção sem bloco misto |",
        f"| `epsilon=||C_BK||` | `{out['epsilon_metric']:.15g}` | métrica produto |",
        f"| `lambda_B_gap` | `{out['lambda_B_gap']:.15g}` | gap físico conservador `Delta_0=1/2` da ponte C3 |",
        "",
        "O gap horizontal/radial reduzido também dá `3/2` em `tau=1`, mas",
        "o critério de Schur deve usar o menor gap físico disponível. Por isso",
        "foi usado o valor conservador:",
        "",
        "$$",
        "\\lambda_B^{\\rm gap}=\\Delta_0=\\frac12.",
        "$$",
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
        "No background avaliado:",
        "",
        f"- `m_perp^2 = {out['m_perp2']:.15g}`;",
        f"- `j_mix = {out['j_mix']:.15g}`;",
        f"- `Delta_Schur = {out['delta_schur']:.15g}`;",
        f"- `Delta_Schur/lambda_B_gap = {0.0:.15g}`.",
        "",
        "Logo:",
        "",
        "$$",
        "\\frac{j_{\\rm mix}^2}{m_\\perp^2}",
        "=",
        "0",
        "<",
        "\\frac12.",
        "$$",
        "",
        "O setor é subcrítico de forma exata.",
        "",
        "## Massas relativas resultantes",
        "",
        "Como o complemento de Schur é nulo, as razões 8D coincidem com as",
        "razões reduzidas intrínsecas:",
        "",
        "| lépton | razão 8D |",
        "|---|---:|",
        f"| `e` | `{out['R_e_8']:.15f}` |",
        f"| `mu` | `{out['R_mu_8']:.15f}` |",
        f"| `tau` | `{out['R_tau_8']:.15f}` |",
        "",
        "## Veredito",
        "",
        "Para o background leptônico 8D estacionário produto, os valores físicos",
        "pedidos são:",
        "",
        "$$",
        "a_W=a_f=a_H=\\varepsilon=0,",
        "\\qquad",
        "\\lambda_B^{\\rm gap}=\\frac12.",
        "$$",
        "",
        "Portanto a expansão 8D fecha sem deslocamento de massa:",
        "",
        "$$",
        "R_\\ell^{(8)}=R_\\ell^{(0)}.",
        "$$",
        "",
        "Backgrounds warped/mistos reais, caso sejam introduzidos depois, não",
        "reabrem este resultado; eles devem ser avaliados por este mesmo critério",
        "e só alteram a hierarquia se produzirem `j_mix != 0` sub/supercrítico.",
        "",
    ]

    report = base / "saida_background_8d_estacionario_q39.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
