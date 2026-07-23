#!/usr/bin/env python3
"""
Raio estrutural de superfície do próton na GDQ.

Classificação:
    correção aritmética, avaliação direta de fórmula estrutural e comparação
    fenomenológica.

O script preserva a conclusão da Q60 em forma autocontida:

1. a fórmula multiplicativa antiga produz 0.000248914485 fm, não 0.0369 fm;
2. o raio vigente é o raio de superfície
   r_p=(1/8)(1+alpha/4) epsilon_eff (3 Lambda_C/2);
3. diferenças entre sondas são tratadas por resposta linear de contorno.
"""

from __future__ import annotations

from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_raio_proton_superficie.md"


def main() -> None:
    legacy = 0.8778 * 0.07479 * 1.0e-3 * 3.7915
    old_claim = 0.0369
    factor_error = old_claim / legacy

    alpha_inv = 137.035999084
    alpha = 1.0 / alpha_inv
    epsilon_eff = 0.011591040463
    Lambda_C_fm = 386.159268
    C_r = (1.0 / 8.0) * (1.0 + alpha / 4.0)
    R_B = 1.5 * Lambda_C_fm
    r_p = C_r * epsilon_eff * R_B

    refs = [
        ("referência muônica 0.84087 fm", 0.84087),
        ("valor eletrônico comparativo 0.8778 fm", 0.8778),
        ("valor efetivo comparativo 0.8354 fm", 0.8354),
    ]

    mu_ratio = 1.555489846615637e-7

    lines = [
        "---",
        'title: "Saída — raio estrutural do próton"',
        "---",
        "",
        "# Saída — raio estrutural do próton",
        "",
        "## Correção aritmética descartada",
        "",
        f"- produto antigo correto: `{legacy:.12f} fm`.",
        f"- valor escrito na rota antiga: `{old_claim:.12f} fm`.",
        f"- fator de erro: `{factor_error:.6f}`.",
        "",
        "## Fórmula estrutural",
        "",
        "$$",
        "r_p^{\\rm surf}=\\frac18\\left(1+\\frac{\\alpha}{4}\\right)\\epsilon_{\\rm eff}\\frac{3\\Lambda_C}{2}",
        "$$",
        "",
        "| Quantidade | Valor |",
        "|---|---:|",
        f"| $\\alpha^{{-1}}$ | {alpha_inv:.12f} |",
        f"| $\\epsilon_{{\\rm eff}}$ | {epsilon_eff:.12f} |",
        f"| $\\Lambda_C$ | {Lambda_C_fm:.12f} fm |",
        f"| $C_r$ | {C_r:.15f} |",
        f"| $R_B=3\\Lambda_C/2$ | {R_B:.12f} fm |",
        f"| $r_p^{{\\rm surf}}$ | {r_p:.12f} fm |",
        "",
        "## Comparações",
        "",
        "| Referência | Diferença | Diferença relativa |",
        "|---|---:|---:|",
    ]

    for label, ref in refs:
        diff = r_p - ref
        lines.append(f"| {label} | {diff:+.12f} fm | {diff/ref:+.6%} |")

    lines += [
        "",
        "## Resposta de sonda",
        "",
        "$$",
        "r_p^{\\rm eff}[\\ell]=r_p^{\\rm surf}-\\left(H_p^{\\rm surf}\\right)^{-1}J_{p,\\ell}",
        "$$",
        "",
        "$$",
        "\\frac{\\delta r_p[e]}{\\delta r_p[\\mu]}=\\left(\\frac{\\mu_{ep}}{\\mu_{\\mu p}}\\right)^3",
        "$$",
        "",
        f"- razão de contato eletrônica/muônica: `{mu_ratio:.15e}`.",
        "",
        "Classificação: raio estrutural fechado; puzzle experimental reduzido a resposta de contorno.",
        "",
    ]

    text = "\n".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
