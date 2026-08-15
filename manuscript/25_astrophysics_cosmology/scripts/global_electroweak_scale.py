#!/usr/bin/env python3
"""
Reduced global electroweak scale of GDQ.

Classification:
    direct evaluation of structural formulas and phenomenological comparison.

The script separates three things:

1. v_K, auxiliary formula that produces a MeV scale and not the Fermi scale;
2. beta_* as the dimensionless minimum of the geometric potential;
3. v_GDQ=M_p 6*pi^5/7 as a candidate global normalization.

The W/Z masses are calculated in a conditional transport scenario. m_W and m_Z
enter only afterwards, for comparison.
"""

from __future__ import annotations

import math
from pathlib import Path


OUT = Path(__file__).resolve().parent / "output_global_electroweak_scale.md"


def rel(value: float, ref: float) -> float:
    return (value - ref) / ref


def main() -> None:
    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    m_e = 0.00051099895069
    m_p = 0.93827208816
    v_ref = 246.21965

    a2 = -0.253196676
    a4 = 2133.554507
    beta_star = math.sqrt(-a2 / a4)

    v_k = (m_e / alpha) / math.sqrt(1.0 - 3.0 / (4.0 * math.pi**2))
    v_gdq = m_p * 6.0 * math.pi**5 / 7.0
    z_beta_required = (v_gdq / beta_star) ** 2

    s_boundary = alpha * (3.0 * math.pi / 2.0 + 3.0 / (4.0 * math.pi**3))
    alpha_ew = alpha * (1.0 + s_boundary)
    sin2 = 2.0 / 9.0
    cos2 = 1.0 - sin2
    e = math.sqrt(4.0 * math.pi * alpha_ew)
    g = e / math.sqrt(sin2)
    gp = e / math.sqrt(cos2)
    m_w = g * v_gdq / 2.0
    m_z = v_gdq * math.sqrt(g * g + gp * gp) / 2.0
    ref_w = 80.3692
    ref_z = 91.1876

    lines = [
        "---",
        'title: "Output — global electroweak scale"',
        "---",
        "",
        "# Output — global electroweak scale",
        "",
        "## Audit of $v_K$",
        "",
        f"- $v_K={v_k:.12f}\\,{{\\rm GeV}}={1000*v_k:.6f}\\,{{\\rm MeV}}$.",
        f"- error against $v_F=246.21965\\,{{\\rm GeV}}$: `{100*rel(v_k, v_ref):+.6f}%`.",
        "",
        "## Dimensionless geometric minimum",
        "",
        "$$",
        "\\mathcal V(\\beta)=\\frac{1}{2}a_2\\beta^2+\\frac{1}{4}a_4\\beta^4",
        "$$",
        "",
        "$$",
        "\\beta_*^2=-\\frac{a_2}{a_4}",
        "$$",
        "",
        f"- $a_2={a2:.9f}$.",
        f"- $a_4={a4:.6f}$.",
        f"- $\\beta_*={beta_star:.10f}$.",
        "",
        "## Global normalization",
        "",
        "$$",
        "v_{\\rm GDQ}=M_p\\frac{6\\pi^5}{7}",
        "$$",
        "",
        f"- $v_{{\\rm GDQ}}={v_gdq:.12f}\\,{{\\rm GeV}}$.",
        f"- error against $v_F=246.21965\\,{{\\rm GeV}}$: `{100*rel(v_gdq, v_ref):+.6f}%`.",
        f"- $Z_\\beta$ required by the relation $v=\\sqrt{{Z_\\beta}}\\beta_*$: `{z_beta_required:.12e}`.",
        "",
        "## Conditional W/Z",
        "",
        "| Quantity | Value |",
        "|---|---:|",
        f"| $\\alpha_{{\\rm EW}}^{{-1}}$ | {1/alpha_ew:.12f} |",
        f"| $\\sin^2\\theta_W$ | {sin2:.12f} |",
        f"| $g$ | {g:.12f} |",
        f"| $g'$ | {gp:.12f} |",
        f"| $m_W$ | {m_w:.12f} GeV |",
        f"| error $m_W$ | {100*rel(m_w, ref_w):+.6f}% |",
        f"| $m_Z$ | {m_z:.12f} GeV |",
        f"| error $m_Z$ | {100*rel(m_z, ref_z):+.6f}% |",
        "",
        "## Classification",
        "",
        "Scale correction structurally closed. $W/Z$ metrology conditioned on $Z_\\beta$, electromagnetic Schur, and transport $Z_W/Z_Y=10/21$.",
        "",
    ]

    text = "\n".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
