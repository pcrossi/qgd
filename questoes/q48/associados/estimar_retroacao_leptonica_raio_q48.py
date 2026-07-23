#!/usr/bin/env python3
"""Q48 — estimativa GDQ da retroação leptônica sobre o raio efetivo do próton.

Classificação:
- teste de escala/consistência;
- não é previsão metrológica final, porque o coeficiente absoluto exige a
  Hessiana local de superfície do próton.

Ideia:
Para estados s, a fonte de contato que deforma o contorno protônico escala como

    J_l ~ |psi_ns(0)|^2 ~ (mu_lp Z alpha)^3 / n^3.

Logo, se a resposta linear do raio efetivo for

    delta r_p[l] = - H_p^{-1} J_l,

então a razão elétron/múon é determinada sem conhecer H_p:

    delta r_p[e] / delta r_p[mu] = (mu_ep / mu_mup)^3

para o mesmo n.
"""

from __future__ import annotations

from pathlib import Path

import scipy.constants as C


OUT = Path(__file__).with_name("saida_retroacao_leptonica_raio_q48.md")


def reduced_mass(m_l: float, m_p: float) -> float:
    return m_l * m_p / (m_l + m_p)


def main() -> None:
    m_e = C.m_e
    m_mu = C.physical_constants["muon mass"][0]
    m_p = C.m_p

    mu_ep = reduced_mass(m_e, m_p)
    mu_mup = reduced_mass(m_mu, m_p)
    ratio_mu = mu_ep / mu_mup
    ratio_contact = ratio_mu**3

    # Apenas como escala diagnóstica: se uma sonda muônica contrair o raio por
    # valores típicos de 0.01 fm ou 0.03 fm, quanto seria a contração eletrônica?
    trial_mu_shifts_fm = [-0.01, -0.03, -0.034]

    text = [
        "# Saída — retroação leptônica no raio efetivo do próton Q48",
        "",
        "Classificação: teste de escala GDQ. Não é previsão metrológica final,",
        "pois o coeficiente absoluto exige a Hessiana local de superfície do próton.",
        "",
        "## Modelo de escala",
        "",
        "$$",
        "\\delta r_p[\\ell]",
        "=",
        "-(H_p^{\\rm surf})^{-1}J_\\ell,",
        "\\qquad",
        "J_\\ell\\propto |\\psi_{ns}(0)|^2",
        "\\propto \\frac{\\mu_{\\ell p}^3}{n^3}.",
        "$$",
        "",
        "Para o mesmo estado $n s$:",
        "",
        "$$",
        "\\frac{\\delta r_p[e]}{\\delta r_p[\\mu]}",
        "=",
        "\\left(\\frac{\\mu_{ep}}{\\mu_{\\mu p}}\\right)^3.",
        "$$",
        "",
        "## Massas reduzidas",
        "",
        f"- $\\mu_{{ep}} = {mu_ep:.15e}\\,\\mathrm{{kg}}$",
        f"- $\\mu_{{\\mu p}} = {mu_mup:.15e}\\,\\mathrm{{kg}}$",
        f"- $\\mu_{{ep}}/\\mu_{{\\mu p}} = {ratio_mu:.15e}$",
        f"- $(\\mu_{{ep}}/\\mu_{{\\mu p}})^3 = {ratio_contact:.15e}$",
        "",
        "## Escala diagnóstica",
        "",
        "| contração muônica assumida | contração eletrônica estimada |",
        "|---:|---:|",
    ]

    for dr_mu in trial_mu_shifts_fm:
        dr_e = dr_mu * ratio_contact
        text.append(f"| {dr_mu:.6f} fm | {dr_e:.12e} fm |")

    text += [
        "",
        "## Conclusão",
        "",
        "A retroação eletrônica existe pela mesma estrutura variacional, mas é",
        "suprimida por aproximadamente $1.56\\times 10^{-7}$ em relação à muônica.",
        "Portanto, se o múon contrai o raio efetivo em escala de $10^{-2}$ fm,",
        "o elétron contrai apenas em escala de $10^{-9}$ fm.",
        "",
        "$$",
        "\\boxed{",
        "\\text{efeito eletrônico permitido, mas metrologicamente minúsculo no hidrogênio comum.}",
        "}",
        "$$",
        "",
    ]

    OUT.write_text("\n".join(text), encoding="utf-8")
    print("\n".join(text))


if __name__ == "__main__":
    main()
