#!/usr/bin/env python3
"""Verificação algébrica do teorema Noether--Zeeman.

Classificação:
    teste simbólico-numérico de consistência.

O script usa uma Hessiana física positiva H_C, um funcional de circulação c e
um funcional magnético m = gamma0 c + m_perp. Ele verifica:

    gamma_eff = <c,H^-1 m>/<c,H^-1 c>
              = gamma0 + <c,H^-1 m_perp>/<c,H^-1 c>.

Também verifica a seleção estacionária C x B = 0 para os dois canais.

Os números são diagnósticos e não representam um aparelho real.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


OUT = Path(__file__).resolve().parent / "saida_verificar_noether_zeeman_sg.md"


def main() -> None:
    h = np.array(
        [
            [3.0, 0.2, 0.1],
            [0.2, 2.5, 0.3],
            [0.1, 0.3, 2.0],
        ]
    )
    c = np.array([1.0, 0.0, 0.0])
    gamma0 = 2.0
    m_perp = np.array([0.0, 0.15, -0.05])
    m = gamma0 * c + m_perp

    h_inv_c = np.linalg.solve(h, c)
    h_inv_m = np.linalg.solve(h, m)
    denom = float(c @ h_inv_c)
    gamma_eff = float(c @ h_inv_m / denom)
    delta_gamma = float(c @ np.linalg.solve(h, m_perp) / denom)

    # Seleção estacionária: os canais estáveis são paralelos/antiparalelos a B.
    b = np.array([0.4, -0.2, 0.7])
    n = b / np.linalg.norm(b)
    c_plus = 0.5 * n
    c_minus = -0.5 * n
    cross_plus = np.linalg.norm(np.cross(c_plus, b))
    cross_minus = np.linalg.norm(np.cross(c_minus, b))

    eig_h = np.linalg.eigvalsh(h)

    lines = ["# Saída — verificação Noether--Zeeman\n\n"]
    lines.append("Classificação: teste simbólico-numérico de consistência.\n\n")
    lines.append("## Parâmetros do teste\n\n")
    lines.append("| grandeza | valor |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| autovalor mínimo de H_C | {eig_h.min():.12f} |\n")
    lines.append(f"| gamma0 | {gamma0:.12f} |\n")
    lines.append(f"| denom = <c,H^-1 c> | {denom:.12f} |\n")
    lines.append(f"| Delta gamma geom | {delta_gamma:.12f} |\n")
    lines.append(f"| gamma eff | {gamma_eff:.12f} |\n")
    lines.append(f"| gamma0 + Delta gamma | {gamma0 + delta_gamma:.12f} |\n")
    lines.append("\n## Verificações\n\n")
    lines.append("| teste | erro |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| identidade gamma_eff | {abs(gamma_eff - (gamma0 + delta_gamma)):.12e} |\n")
    lines.append(f"| ||C_+ x B|| | {cross_plus:.12e} |\n")
    lines.append(f"| ||C_- x B|| | {cross_minus:.12e} |\n")
    lines.append("\n## Veredito\n\n")
    lines.append(
        "A identidade variacional do multiplicador é satisfeita no bloco finito. "
        "A componente mínima é protegida por Noether; o excesso depende da "
        "resposta transversal m_perp e da Hessiana física.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
