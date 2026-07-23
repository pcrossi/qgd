#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `eletrofraca raio proton` associada ao capítulo `25_astrophysics_cosmology`.
Escala eletrofraca e raio estrutural do próton.

Classificação científica:
    avaliação direta de fórmulas estruturais e comparação fenomenológica.

O script separa a fórmula auxiliar v_K, que não produz a escala de Fermi, da
normalização geométrica bariônica vigente. Também calcula o raio estrutural de
superfície do próton e suas comparações.
"""

from __future__ import annotations

import math
from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_eletrofraca_raio_proton.md"


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
        ("referência muônica 0.84087 fm", 0.84087),
        ("valor eletrônico comparativo 0.8778 fm", 0.8778),
        ("valor efetivo comparativo 0.8354 fm", 0.8354),
    ]

    lines: list[str] = []
    lines.append("# Saída — escala eletrofraca e raio do próton\n\n")
    lines.append("Classificação: avaliação direta e comparação fenomenológica.\n\n")
    lines.append("## Escala eletrofraca\n\n")
    lines.append(f"- v_K auxiliar: `{v_k:.12f} GeV` = `{1000*v_k:.6f} MeV`\n")
    lines.append(f"- erro v_K vs Fermi: `{100*rel(v_k, v_ref):+.6f}%`\n")
    lines.append(f"- v_GDQ = M_p 6 pi^5 / 7: `{v_gdq:.12f} GeV`\n")
    lines.append(f"- erro v_GDQ vs Fermi: `{100*rel(v_gdq, v_ref):+.6f}%`\n\n")

    lines.append("## W/Z reduzidos\n\n")
    lines.append("| quantidade | valor |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| alpha_EW^-1 | {1.0/alpha_EW:.12f} |\n")
    lines.append(f"| sin2_theta | {sin2:.12f} |\n")
    lines.append(f"| g | {g:.12f} |\n")
    lines.append(f"| g_prime | {gp:.12f} |\n")
    lines.append(f"| m_W | {mW:.12f} GeV |\n")
    lines.append(f"| m_Z | {mZ:.12f} GeV |\n")
    lines.append(f"| erro m_W | {100*rel(mW, ref_mW):+.6f}% |\n")
    lines.append(f"| erro m_Z | {100*rel(mZ, ref_mZ):+.6f}% |\n\n")

    lines.append("## Raio estrutural do próton\n\n")
    lines.append(f"- r_p^surf: `{r_p:.12f} fm`\n\n")
    lines.append("| comparação | diferença | diferença relativa |\n")
    lines.append("|---|---:|---:|\n")
    for label, ref in refs:
        diff = r_p - ref
        lines.append(f"| {label} | {diff:+.12f} fm | {diff/ref:+.6%} |\n")

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
