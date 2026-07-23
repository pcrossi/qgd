#!/usr/bin/env python3
"""Derivação simbólica das massas bariônicas reduzidas.

Classificação:
    derivação simbólica / avaliação direta da construção reduzida GDQ.

Este script registra, de modo autocontido, as fórmulas usadas no Capítulo 17:

1. o elétron define a unidade reduzida $E_0=M_e c^2$;
2. o bulk bariônico de três estômatos fornece $6 pi^5$;
3. a superfície torsional do próton fornece
   alpha(3 pi/2 + 3/(4 pi^3));
4. a orientação estacionária do nêutron $(1,1,-2)$ gera o excesso
   delta_B = ln(2 pi^2) 3 sqrt(2)/5.

Os valores aceitos de próton e nêutron são usados apenas na comparação final.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path

import sympy as sp


OUT = Path(__file__).resolve().parent / "saida_derivacao_simbolica_massas_barioes.md"


def pairwise_shear_squared(values: tuple[sp.Expr, sp.Expr, sp.Expr]) -> sp.Expr:
    return sp.simplify(sum((values[i] - values[j]) ** 2 for i, j in combinations(range(3), 2)))


def main() -> None:
    alpha = sp.symbols("alpha", positive=True)

    vol_chamber = 2 * sp.pi**5
    n_stomata = sp.Integer(3)
    bulk = sp.simplify(n_stomata * vol_chamber)

    cs_three = 3 * sp.pi / 2
    throat_three = 3 / (4 * sp.pi**3)
    surface = sp.simplify(alpha * (cs_three + throat_three))
    mp_me = sp.simplify(bulk + surface)

    proton = (sp.Integer(1), sp.Integer(1), sp.Integer(1))
    neutron = (sp.Integer(1), sp.Integer(1), sp.Integer(-2))
    shear_p2 = pairwise_shear_squared(proton)
    shear_n2 = pairwise_shear_squared(neutron)

    channels = sp.Integer(3)
    dim_local = sp.Integer(4)
    hyp = sp.sqrt(channels**2 + dim_local**2)
    cos_theta = sp.simplify(channels / hyp)
    complex_norm = sp.sqrt(2)
    chi_b = sp.simplify(complex_norm * cos_theta)
    entropy_surface = sp.log(2 * sp.pi**2)
    delta_b = sp.simplify(entropy_surface * chi_b)
    mn_me = sp.simplify(mp_me + delta_b)

    alpha_inv_value = sp.Float("137.035999177")
    alpha_value = 1 / alpha_inv_value
    bulk_value = sp.N(bulk, 18)
    surface_value = sp.N(surface.subs(alpha, alpha_value), 18)
    mp_value = sp.N(mp_me.subs(alpha, alpha_value), 18)
    delta_value = sp.N(delta_b, 18)
    mn_value = sp.N(mn_me.subs(alpha, alpha_value), 18)

    ref_mp = 1836.15267343
    ref_mn = 1838.68366173
    err_mp = (float(mp_value) - ref_mp) / ref_mp
    err_mn = (float(mn_value) - ref_mn) / ref_mn

    lines = ["# Saída — derivação simbólica das massas bariônicas\n\n"]
    lines.append("Classificação: derivação simbólica / avaliação direta.\n\n")
    lines.append("## 1. Unidade reduzida\n\n")
    lines.append("A unidade metrológica reduzida é:\n\n")
    lines.append("$$\nE_0=M_e c^2,\n\\qquad\nM_B/M_e=\\mathcal I_B.\n$$\n\n")
    lines.append("## 2. Bulk de três estômatos\n\n")
    lines.append("Cada câmara contribui:\n\n")
    lines.append("$$\n\\operatorname{Vol}(\\mathcal F_a)=2\\pi^5.\n$$\n\n")
    lines.append("Para três estômatos:\n\n")
    lines.append("$$\n\\mathcal I_B^{\\rm bulk}=3(2\\pi^5)=")
    lines.append(sp.latex(bulk))
    lines.append(".\n$$\n\n")
    lines.append("## 3. Superfície torsional do próton\n\n")
    lines.append("A transgressão de superfície reduzida é:\n\n")
    lines.append("$$\n\\mathcal I_p^\\partial=\n")
    lines.append(sp.latex(surface))
    lines.append(".\n$$\n\n")
    lines.append("Logo:\n\n")
    lines.append("$$\n\\frac{M_p}{M_e}=\n")
    lines.append(sp.latex(mp_me))
    lines.append(".\n$$\n\n")
    lines.append("## 4. Excesso torsional do nêutron\n\n")
    lines.append("Configurações torsionais:\n\n")
    lines.append("$$\n\\mathbf t_p=(1,1,1),\n\\qquad\n\\mathbf t_n=(1,1,-2).\n$$\n\n")
    lines.append("Invariante par-a-par:\n\n")
    lines.append("$$\nI_{\\rm sh}^2(\\mathbf t)=\\sum_{a<b}(t_a-t_b)^2.\n$$\n\n")
    lines.append("Para o próton e o nêutron:\n\n")
    lines.append("$$\nI_{\\rm sh}^2(\\mathbf t_p)=")
    lines.append(sp.latex(shear_p2))
    lines.append(",\n\\qquad\nI_{\\rm sh}^2(\\mathbf t_n)=")
    lines.append(sp.latex(shear_n2))
    lines.append(".\n$$\n\n")
    lines.append("A projeção Fredholm--Fano usa:\n\n")
    lines.append("$$\n\\cos\\theta_c=\\frac{3}{\\sqrt{3^2+4^2}}=")
    lines.append(sp.latex(cos_theta))
    lines.append(",\n\\qquad\n\\|1+i\\|=\\sqrt2.\n$$\n\n")
    lines.append("Assim:\n\n")
    lines.append("$$\n\\chi_B=\\sqrt2\\cos\\theta_c=")
    lines.append(sp.latex(chi_b))
    lines.append(".\n$$\n\n")
    lines.append("Como $\\operatorname{Vol}(S^3)=2\\pi^2$:\n\n")
    lines.append("$$\n\\delta_B=\n")
    lines.append("\\ln(2\\pi^2)\\frac{3\\sqrt2}{5}")
    lines.append(".\n$$\n\n")
    lines.append("A forma simbólica equivalente avaliada pelo código é:\n\n")
    lines.append("$$\n")
    lines.append(sp.latex(delta_b))
    lines.append(".\n$$\n\n")
    lines.append("Portanto:\n\n")
    lines.append("$$\n\\frac{M_n}{M_e}=\\frac{M_p}{M_e}+\\delta_B.\n$$\n\n")
    lines.append("## 5. Avaliação numérica\n\n")
    lines.append("| quantidade | valor |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| alpha^-1 | {float(alpha_inv_value):.12f} |\n")
    lines.append(f"| bulk 6*pi^5 | {float(bulk_value):.12f} |\n")
    lines.append(f"| superfície torsional | {float(surface_value):.12f} |\n")
    lines.append(f"| delta_B | {float(delta_value):.12f} |\n")
    lines.append(f"| Mp/Me | {float(mp_value):.12f} |\n")
    lines.append(f"| Mn/Me | {float(mn_value):.12f} |\n")
    lines.append("\n## 6. Comparação posterior\n\n")
    lines.append("| razão | GDQ | referência | erro relativo |\n")
    lines.append("|---|---:|---:|---:|\n")
    lines.append(f"| Mp/Me | {float(mp_value):.12f} | {ref_mp:.12f} | {err_mp:.12e} |\n")
    lines.append(f"| Mn/Me | {float(mn_value):.12f} | {ref_mn:.12f} | {err_mn:.12e} |\n")
    lines.append("\n## Veredito\n\n")
    lines.append(
        "As fórmulas de próton e nêutron são obtidas por volume reduzido, "
        "transgressão torsional de superfície e cisalhamento antiparalelo. "
        "Os valores aceitos entram somente depois, como comparação.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
