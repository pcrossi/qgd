#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `neutrinos torsionais reduzido` associada ao capítulo `24_nuclear_phenomenology`.
Candidato reduzido de massas/escalas inerciais neutras.

Classificação científica:
    candidato GDQ reduzido.

O script não usa diferenças quadradas observadas como entrada. Ele congela a
escala S_nu=alpha^7 Q_beta^2 e o espectro candidato
lambda=(0, chi_nu^2/2, 6*pi/5), depois compara com valores de referência
usados no manuscrito para avaliar ordem de grandeza e erro relativo.
"""

from __future__ import annotations

import math
from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_neutrinos_torsionais_reduzido.md"

ALPHA = 1.0 / 137.035999177
Q_BETA_EV = 0.782333559310e6

# Valores de referência usados apenas para comparação final.
DM21_REF = 7.49e-5
DM31_REF = 2.534e-3


def rel_err(value: float, ref: float) -> float:
    return (value - ref) / ref


def main() -> None:
    chi_nu = (12.0 / 25.0) * math.exp(-ALPHA / 4.0)
    s_nu = ALPHA**7 * Q_BETA_EV**2
    lambdas = [0.0, 0.5 * chi_nu**2, 6.0 * math.pi / 5.0]
    masses = [math.sqrt(s_nu * lam) for lam in lambdas]
    dm21 = s_nu * (lambdas[1] - lambdas[0])
    dm31 = s_nu * (lambdas[2] - lambdas[0])

    theta12 = math.degrees(math.atan(1.0 / math.sqrt(2.0)))
    theta23 = 45.0
    theta13 = math.degrees(math.asin(chi_nu / math.pi))
    delta_cp = math.degrees(3.84)

    lines: list[str] = []
    lines.append("# Saída — neutrinos torsionais reduzidos\n\n")
    lines.append("Classificação: candidato GDQ reduzido.\n\n")
    lines.append("## Entradas congeladas antes da comparação\n\n")
    lines.append(f"- alpha: `{ALPHA:.15e}`\n")
    lines.append(f"- Q_beta: `{Q_BETA_EV:.12e} eV`\n")
    lines.append(f"- S_nu = alpha^7 Q_beta^2: `{s_nu:.12e} eV^2`\n")
    lines.append(f"- chi_nu = (12/25) exp(-alpha/4): `{chi_nu:.12e}`\n\n")

    lines.append("## Autovalores candidatos\n\n")
    lines.append("| modo | lambda |\n")
    lines.append("|---:|---:|\n")
    for i, lam in enumerate(lambdas, start=1):
        lines.append(f"| {i} | {lam:.12e} |\n")

    lines.append("\n## Massas candidatas\n\n")
    lines.append("| modo | massa (eV) |\n")
    lines.append("|---:|---:|\n")
    for i, mass in enumerate(masses, start=1):
        lines.append(f"| {i} | {mass:.12e} |\n")
    lines.append(f"| soma | {sum(masses):.12e} |\n")

    lines.append("\n## Diferenças quadradas\n\n")
    lines.append("| quantidade | GDQ reduzido | referência | erro relativo |\n")
    lines.append("|---|---:|---:|---:|\n")
    lines.append(f"| dm21 | {dm21:.12e} | {DM21_REF:.12e} | {rel_err(dm21, DM21_REF):+.6e} |\n")
    lines.append(f"| dm31 | {dm31:.12e} | {DM31_REF:.12e} | {rel_err(dm31, DM31_REF):+.6e} |\n")

    lines.append("\n## Ângulos crus associados\n\n")
    lines.append("| parâmetro | valor |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| theta12 | {theta12:.9f} deg |\n")
    lines.append(f"| theta23 | {theta23:.9f} deg |\n")
    lines.append(f"| theta13 | {theta13:.9f} deg |\n")
    lines.append(f"| delta_CP candidato histórico | {delta_cp:.9f} deg |\n")

    lines.append("\n## Interpretação\n\n")
    lines.append(
        "O modo superior fica muito próximo da escala de oscilação atmosférica; "
        "o modo solar fica a poucos por cento. O cálculo é candidato reduzido, "
        "pois os autovalores ainda devem ser obtidos pela Hessiana neutra "
        "oficial em vez de pela forma analítica reduzida.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

