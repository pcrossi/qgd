#!/usr/bin/env python3
"""
Q53 — auditoria numérica mínima do setor de neutrinos.

Classificação:
- comparação fenomenológica para ângulos PMNS geométricos do legado;
- reconstrução experimental mínima para massas a partir de diferenças quadradas;
- não é previsão cega das massas absolutas.
"""

import math
import numpy as np


alpha = 1.0 / 137.035999084

# NuFIT 6.0, JHEP12(2024)216, tabela pública IC19 sem SK-atm, NO.
# Usado aqui como referência observacional, não como entrada GDQ.
nufit = {
    "theta12_deg": 33.68,
    "theta23_deg": 48.5,
    "theta13_deg": 8.52,
    "delta_cp_deg": 177.0,
    "dm21_eV2": 7.49e-5,
    "dm31_eV2": 2.534e-3,
}


def pmns(theta12, theta23, theta13, delta):
    c12, s12 = math.cos(theta12), math.sin(theta12)
    c23, s23 = math.cos(theta23), math.sin(theta23)
    c13, s13 = math.cos(theta13), math.sin(theta13)
    e_minus = complex(math.cos(-delta), math.sin(-delta))
    e_plus = complex(math.cos(delta), math.sin(delta))

    return np.array(
        [
            [c12 * c13, s12 * c13, s13 * e_minus],
            [
                -s12 * c23 - c12 * s23 * s13 * e_plus,
                c12 * c23 - s12 * s23 * s13 * e_plus,
                s23 * c13,
            ],
            [
                s12 * s23 - c12 * c23 * s13 * e_plus,
                -c12 * s23 - s12 * c23 * s13 * e_plus,
                c23 * c13,
            ],
        ],
        dtype=complex,
    )


# Fórmulas geométricas cruas presentes no apêndice legado.
chi_fano_n = 0.48 * math.exp(-alpha / 4.0)
gdq_raw = {
    "theta12_deg": math.degrees(math.atan(1.0 / math.sqrt(2.0))),
    "theta23_deg": 45.0,
    "theta13_deg": math.degrees(math.asin(chi_fano_n / math.pi)),
    # O código legado usa 3.84 rad. Classificar como proposta/entrada
    # fenomenológica até derivar a holonomia CP pela ação oficial.
    "delta_cp_deg": math.degrees(3.84),
}


def normal_minimal_masses(dm21, dm31):
    m1 = 0.0
    m2 = math.sqrt(dm21)
    m3 = math.sqrt(dm31)
    return m1, m2, m3, m1 + m2 + m3


U_gdq = pmns(
    math.radians(gdq_raw["theta12_deg"]),
    math.radians(gdq_raw["theta23_deg"]),
    math.radians(gdq_raw["theta13_deg"]),
    math.radians(gdq_raw["delta_cp_deg"]),
)

U_ref = pmns(
    math.radians(nufit["theta12_deg"]),
    math.radians(nufit["theta23_deg"]),
    math.radians(nufit["theta13_deg"]),
    math.radians(nufit["delta_cp_deg"]),
)

masses = normal_minimal_masses(nufit["dm21_eV2"], nufit["dm31_eV2"])

with open("questoes/q53/associados/saida_auditoria_neutrinos_q53.md", "w", encoding="utf-8") as f:
    f.write("# Q53 — Saída da auditoria numérica de neutrinos\n\n")
    f.write("## Constantes e referência observacional\n\n")
    f.write(f"- alpha = `{alpha:.15e}`\n")
    f.write("- Referência: NuFIT 6.0, normal ordering, tabela IC19 sem SK-atm.\n\n")

    f.write("## Ângulos PMNS\n\n")
    f.write("| parâmetro | GDQ cru legado | NuFIT 6.0 NO | diferença |\n")
    f.write("|---|---:|---:|---:|\n")
    for key in ["theta12_deg", "theta23_deg", "theta13_deg", "delta_cp_deg"]:
        f.write(
            f"| {key} | {gdq_raw[key]:.9f} | {nufit[key]:.9f} | {gdq_raw[key] - nufit[key]:+.9f} |\n"
        )

    f.write("\n## Matriz de probabilidades |U|^2\n\n")
    f.write("### GDQ cru legado\n\n")
    for row in np.abs(U_gdq) ** 2:
        f.write("- " + "  ".join(f"{x:.9f}" for x in row) + "\n")
    f.write("\n### NuFIT 6.0 NO\n\n")
    for row in np.abs(U_ref) ** 2:
        f.write("- " + "  ".join(f"{x:.9f}" for x in row) + "\n")

    f.write("\n## Massas mínimas reconstruídas de dados de oscilação\n\n")
    f.write("Isto usa `m1=0` e as diferenças quadradas observacionais; não é previsão GDQ.\n\n")
    f.write(f"- m1 = `{masses[0]:.12e}` eV\n")
    f.write(f"- m2 = `{masses[1]:.12e}` eV\n")
    f.write(f"- m3 = `{masses[2]:.12e}` eV\n")
    f.write(f"- soma = `{masses[3]:.12e}` eV\n")
    f.write(f"- dm21 = `{nufit['dm21_eV2']:.12e}` eV^2\n")
    f.write(f"- dm31 = `{nufit['dm31_eV2']:.12e}` eV^2\n")

    f.write("\n## Classificação\n\n")
    f.write("- Ângulos crus: comparação fenomenológica de fórmulas geométricas do legado.\n")
    f.write("- Fase CP do código legado: entrada/proposta, não derivação.\n")
    f.write("- Massas mínimas: reconstrução experimental, não mecanismo GDQ de massa absoluta.\n")
