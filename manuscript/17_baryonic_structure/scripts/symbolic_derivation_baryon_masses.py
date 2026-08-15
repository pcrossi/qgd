#!/usr/bin/env python3
"""Symbolic derivation of reduced baryon masses.

Classification:
    symbolic derivation / direct evaluation of the reduced GDQ construction.

This script records, in a self-contained manner, the formulas used in Chapter 17:

1. the electron defines the reduced unit $E_0=M_e c^2$;
2. the baryonic bulk of three stomata yields $6 pi^5$;
3. the torsional surface of the proton yields
   alpha(3 pi/2 + 3/(4 pi^3));
4. the stationary neutron orientation $(1,1,-2)$ generates the excess
   delta_B = ln(2 pi^2) 3 sqrt(2)/5.

The accepted values of proton and neutron are used only in the final comparison.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path

import sympy as sp


OUT = Path(__file__).resolve().parent / "output_symbolic_derivation_baryon_masses.md"


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

    lines = ["# Output — symbolic derivation of baryon masses\n\n"]
    lines.append("Classification: symbolic derivation / direct evaluation.\n\n")
    lines.append("## 1. Reduced Unit\n\n")
    lines.append("The reduced metrological unit is:\n\n")
    lines.append("$$\nE_0=M_e c^2,\n\\qquad\nM_B/M_e=\\mathcal I_B.\n$$\n\n")
    lines.append("## 2. Bulk of Three Stomata\n\n")
    lines.append("Each chamber contributes:\n\n")
    lines.append("$$\n\\operatorname{Vol}(\\mathcal F_a)=2\\pi^5.\n$$\n\n")
    lines.append("For three stomata:\n\n")
    lines.append("$$\n\\mathcal I_B^{\\rm bulk}=3(2\\pi^5)=")
    lines.append(sp.latex(bulk))
    lines.append(".\n$$\n\n")
    lines.append("## 3. Torsional Surface of the Proton\n\n")
    lines.append("The reduced surface transgression is:\n\n")
    lines.append("$$\n\\mathcal I_p^\\partial=\n")
    lines.append(sp.latex(surface))
    lines.append(".\n$$\n\n")
    lines.append("Hence:\n\n")
    lines.append("$$\n\\frac{M_p}{M_e}=\n")
    lines.append(sp.latex(mp_me))
    lines.append(".\n$$\n\n")
    lines.append("## 4. Torsional Excess of the Neutron\n\n")
    lines.append("Torsional configurations:\n\n")
    lines.append("$$\n\\mathbf t_p=(1,1,1),\n\\qquad\n\\mathbf t_n=(1,1,-2).\n$$\n\n")
    lines.append("Pairwise shear invariant:\n\n")
    lines.append("$$\nI_{\\rm sh}^2(\\mathbf t)=\\sum_{a<b}(t_a-t_b)^2.\n$$\n\n")
    lines.append("For proton and neutron:\n\n")
    lines.append("$$\nI_{\\rm sh}^2(\\mathbf t_p)=")
    lines.append(sp.latex(shear_p2))
    lines.append(",\n\\qquad\nI_{\\rm sh}^2(\\mathbf t_n)=")
    lines.append(sp.latex(shear_n2))
    lines.append(".\n$$\n\n")
    lines.append("The Fredholm–Fano projection uses:\n\n")
    lines.append("$$\n\\cos\\theta_c=\\frac{3}{\\sqrt{3^2+4^2}}=")
    lines.append(sp.latex(cos_theta))
    lines.append(",\n\\qquad\n\\|1+i\\|=\\sqrt2.\n$$\n\n")
    lines.append("Thus:\n\n")
    lines.append("$$\n\\chi_B=\\sqrt2\\cos\\theta_c=")
    lines.append(sp.latex(chi_b))
    lines.append(".\n$$\n\n")
    lines.append("Since $\\operatorname{Vol}(S^3)=2\\pi^2$:\n\n")
    lines.append("$$\n\\delta_B=\n")
    lines.append("\\ln(2\\pi^2)\\frac{3\\sqrt2}{5}")
    lines.append(".\n$$\n\n")
    lines.append("The equivalent symbolic form evaluated by the code is:\n\n")
    lines.append("$$\n")
    lines.append(sp.latex(delta_b))
    lines.append(".\n$$\n\n")
    lines.append("Therefore:\n\n")
    lines.append("$$\n\\frac{M_n}{M_e}=\\frac{M_p}{M_e}+\\delta_B.\n$$\n\n")
    lines.append("## 5. Numerical Evaluation\n\n")
    lines.append("| quantity | value |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| alpha^-1 | {float(alpha_inv_value):.12f} |\n")
    lines.append(f"| bulk 6*pi^5 | {float(bulk_value):.12f} |\n")
    lines.append(f"| torsional surface | {float(surface_value):.12f} |\n")
    lines.append(f"| delta_B | {float(delta_value):.12f} |\n")
    lines.append(f"| Mp/Me | {float(mp_value):.12f} |\n")
    lines.append(f"| Mn/Me | {float(mn_value):.12f} |\n")
    lines.append("\n## 6. Subsequent Comparison\n\n")
    lines.append("| ratio | GDQ | reference | relative error |\n")
    lines.append("|---|---:|---:|---:|\n")
    lines.append(f"| Mp/Me | {float(mp_value):.12f} | {ref_mp:.12f} | {err_mp:.12e} |\n")
    lines.append(f"| Mn/Me | {float(mn_value):.12f} | {ref_mn:.12f} | {err_mn:.12e} |\n")
    lines.append("\n## Verdict\n\n")
    lines.append(
         sp.sstr("The formulas for proton and neutron are obtained via reduced volume, "
        "surface torsional transgression, and antiparallel shear. "
        "The accepted values enter only afterward, as a comparison.\n")
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
