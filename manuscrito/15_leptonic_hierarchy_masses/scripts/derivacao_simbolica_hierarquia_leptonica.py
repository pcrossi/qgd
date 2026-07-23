#!/usr/bin/env python3
"""Derivação simbólica da hierarquia leptônica reduzida.

Classificação:
    derivação simbólica / avaliação direta da construção reduzida GDQ.

Este script existe para autocontenção do manuscrito. Ele não ajusta massas.
Ele mostra, simbolicamente, como as fórmulas usadas no Capítulo 15 são
obtidas:

1. o elétron fixa a escala reduzida, $R_e=1$;
2. o múon vem do suporte biespacial;
3. a impedância de interface e a autoenergia de circulação corrigem o termo
   líder;
4. a terceira razão carregada vem da saturação geométrica $Q=2/3$.

O alvo experimental de $M_mu$ ou $M_tau$ não entra na derivação. Os valores
aceitos aparecem somente na comparação final.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


OUT = Path(__file__).resolve().parent / "saida_derivacao_simbolica_hierarquia_leptonica.md"


def main() -> None:
    alpha = sp.symbols("alpha", positive=True)
    z = sp.symbols("z", positive=True)

    r_e = sp.Integer(1)
    nu_2 = sp.Rational(2, 3)
    delta_boundary = sp.Rational(6, 5)
    delta_self = 2 * alpha

    r_mu_0 = sp.simplify(1 / (nu_2 * alpha))
    r_mu = sp.simplify(r_mu_0 + delta_boundary + delta_self)

    x = sp.sqrt(r_e)
    y = sp.sqrt(r_mu)
    q_expr = sp.simplify((r_e + r_mu + z**2) / (x + y + z) ** 2)
    equation = sp.Eq(q_expr, sp.Rational(2, 3))
    poly = sp.factor(sp.together(q_expr - sp.Rational(2, 3)).as_numer_denom()[0])
    branches_z = sp.solve(poly, z)
    branches_r = [sp.simplify(branch**2) for branch in branches_z]

    alpha_inv_value = sp.Float("137.035999177")
    alpha_value = 1 / alpha_inv_value
    r_mu_value = sp.N(r_mu.subs(alpha, alpha_value), 18)
    branch_values = [sp.N(branch.subs(alpha, alpha_value), 18) for branch in branches_r]
    branch_values_sorted = sorted(float(v) for v in branch_values)

    ref_mu = 206.768282700
    ref_tau = 3477.150000000
    err_mu = (float(r_mu_value) - ref_mu) / ref_mu
    err_tau = (branch_values_sorted[-1] - ref_tau) / ref_tau

    lines = ["# Saída — derivação simbólica da hierarquia leptônica\n\n"]
    lines.append("Classificação: derivação simbólica / avaliação direta.\n\n")
    lines.append("## 1. Setor eletrônico\n\n")
    lines.append("O elétron define a escala reduzida:\n\n")
    lines.append("$$\nR_e=1.\n$$\n\n")
    lines.append("## 2. Razão do múon\n\n")
    lines.append("Suporte biespacial:\n\n")
    lines.append("$$\n\\nu_2=\\frac23.\n$$\n\n")
    lines.append("Termo líder:\n\n")
    lines.append("$$\nR_\\mu^{(0)}=\\frac{1}{\\nu_2\\alpha}=\\frac{3}{2}\\alpha^{-1}.\n$$\n\n")
    lines.append("Impedância de interface e autoenergia:\n\n")
    lines.append("$$\n\\Delta_\\partial=\\frac65,\n\\qquad\n\\Delta_{\\rm self}=2\\alpha.\n$$\n\n")
    lines.append("Logo:\n\n")
    lines.append("$$\nR_\\mu=\n")
    lines.append(sp.latex(r_mu))
    lines.append(".\n$$\n\n")
    lines.append("## 3. Saturação geométrica da terceira razão\n\n")
    lines.append("Com $R_3=z^2$, a condição é:\n\n")
    lines.append("$$\n")
    lines.append(sp.latex(equation))
    lines.append(".\n$$\n\n")
    lines.append("O numerador polinomial equivalente é:\n\n")
    lines.append("$$\n")
    lines.append(sp.latex(poly))
    lines.append("=0.\n$$\n\n")
    lines.append("As duas soluções para $R_3$ são:\n\n")
    lines.append("$$\nR_{3,\\pm}=\n")
    lines.append("\\left[\n")
    lines.append("2(\\sqrt{R_1}+\\sqrt{R_2})\n")
    lines.append("\\pm\n")
    lines.append("\\sqrt{3R_1+12\\sqrt{R_1R_2}+3R_2}\n")
    lines.append("\\right]^2")
    lines.append(".\n$$\n\n")
    lines.append("A solução simbólica direta do polinômio em $z$ foi usada pelo script; a forma acima é a forma simplificada em termos de $R_1$ e $R_2$.\n\n")
    lines.append("## 4. Avaliação numérica\n\n")
    lines.append("| quantidade | valor |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| alpha^-1 | {float(alpha_inv_value):.12f} |\n")
    lines.append(f"| R_mu | {float(r_mu_value):.12f} |\n")
    lines.append(f"| R_3 ramo leve | {branch_values_sorted[0]:.12f} |\n")
    lines.append(f"| R_3 ramo pesado | {branch_values_sorted[-1]:.12f} |\n")
    lines.append("\n## 5. Comparação posterior\n\n")
    lines.append("| razão | GDQ | referência | erro relativo |\n")
    lines.append("|---|---:|---:|---:|\n")
    lines.append(f"| M_mu/M_e | {float(r_mu_value):.12f} | {ref_mu:.12f} | {err_mu:.12e} |\n")
    lines.append(f"| M_tau/M_e | {branch_values_sorted[-1]:.12f} | {ref_tau:.12f} | {err_tau:.12e} |\n")
    lines.append("\n## Veredito\n\n")
    lines.append(
        "A derivação simbólica produz a fórmula do múon e os dois ramos da "
        "terceira razão sem usar massas experimentais como entrada. A escolha "
        "do ramo pesado é uma seleção física do tripleto carregado; o ramo leve "
        "permanece matemático até possuir Hessiana própria.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
