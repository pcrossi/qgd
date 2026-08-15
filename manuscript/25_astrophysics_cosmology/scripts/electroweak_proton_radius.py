#!/usr/bin/env python3
"""
Objective:
    Self-contained verification of `electroweak proton radius` associated with chapter `25_astrophysics_cosmology`.
Electroweak scale and structural proton radius.

Scientific classification:
    direct evaluation of structural formulas and phenomenological comparison.

The script separates the auxiliary formula v_K, which does not produce the Fermi scale, from the
current baryonic geometric normalization. It also calculates the structural surface
proton radius and its comparisons.
"""

from __future__ import annotations

import math
from pathlib import Path


OUT = Path(__file__).resolve().parent / "output_electroweak_proton_radius.md"


def rel(value: float, ref: float) -> float:
    return (value - ref) / ref


def main() -> None:
    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    m_e_gev = 0.00051099895069
    m_p_gev = 0.93827208816
    v_ref = 246.21965

    v_k = (m_e_gev / alpha) / math.sqrt(1.0 - 3.0 / (4.0 * math.pi**2))
    v_gdq = m_p_gev * (6.0 * math.pi**5) / 7.0

    S_boundary = alpha * (3.0 * math.pi / 2.0 + 3.0 / (4.0 * math.pi**3))
    alpha_EW = alpha * (1.0 + S_boundary)
    sin2 = 2.0 / 9.0
    cos2 = 1.0 - sin2
    e = math.sqrt(4.0 * math.pi * alpha_EW)
    g = e / math.sqrt(sin2)
    gp = e / math.sqrt(cos2)
    mW = g * v_gdq / 2.0
    mZ = v_gdq * math.sqrt(g * g + gp * gp) / 2.0
    ref_mW = 80.3692
    ref_mZ = 91.1876

    epsilon_eff = 0.011591040463
    Lambda_C_fm = 386.159268
    C_r = (1.0 / 8.0) * (1.0 + alpha / 4.0)
    R_B = 1.5 * Lambda_C_fm
    r_p = C_r * epsilon_eff * R_B

    refs = [
        ("muonic reference 0.84087 fm", 0.84087),
        ("comparative electronic value 0.8778 fm", 0.8778),
        ("comparative effective value 0.8354 fm", 0.8354),
    ]

    lines: list[str] = []
    lines.append("# Output — electroweak scale and proton radius\n\n")
    lines.append("Classification: direct evaluation and phenomenological comparison.\n\n")
    lines.append("## Electroweak scale\n\n")
    lines.append(f"- v_K auxiliary: `{v_k:.12f} GeV` = `{1000*v_k:.6f} MeV`\n")
    lines.append(f"- error v_K vs Fermi: `{100*rel(v_k, v_ref):+.6f}%`\n")
    lines.append(f"- v_GDQ = M_p 6 pi^5 / 7: `{v_gdq:.12f} GeV`\n")
    lines.append(f"- error v_GDQ vs Fermi: `{100*rel(v_gdq, v_ref):+.6f}%`\n\n")

    lines.append("## Reduced W/Z\n\n")
    lines.append("| quantity | value |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| alpha_EW^-1 | {1.0/alpha_EW:.12f} |\n")
    lines.append(f"| sin2_theta | {sin2:.12f} |\n")
    lines.append(f"| g | {g:.12f} |\n")
    lines.append(f"| g_prime | {gp:.12f} |\n")
    lines.append(f"| m_W | {mW:.12f} GeV |\n")
    lines.append(f"| m_Z | {mZ:.12f} GeV |\n")
    lines.append(f"| error m_W | {100*rel(mW, ref_mW):+.6f}% |\n")
    lines.append(f"| error m_Z | {100*rel(mZ, ref_mZ):+.6f}% |\n\n")

    lines.append("## Structural proton radius\n\n")
    lines.append(f"- r_p^surf: `{r_p:.12f} fm`\n\n")
    lines.append("| comparison | difference | relative difference |\n")
    lines.append("|---|---:|---:|\n")
    for label, ref in refs:
        diff = r_p - ref
        lines.append(f"| {label} | {diff:+.12f} fm | {diff/ref:+.6%} |\n")

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
