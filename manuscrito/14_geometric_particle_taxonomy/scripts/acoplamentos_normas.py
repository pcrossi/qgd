#!/usr/bin/env python3
"""
GDQ — Capítulo 14 / Acoplamentos como normas do fibrado

Objetivo:
    Calcular as razões I_3, I_2, I_Y de uma geração e extrair:

        g_s = g,
        g'^2/g^2 = 3/5,
        sin^2(theta_W) = 3/8.

Classificação:
    Avaliação direta das normas geométricas no ponto comum de correspondência.

Saída:
    scripts/saida_acoplamentos_normas.md
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_acoplamentos_normas.md"

    alpha = 1.0 / 137.03599907
    e_charge = math.sqrt(4.0 * math.pi * alpha)

    # T(fundamental SU(N)) = 1/2.
    index_su3 = 2.0 * 0.5 + 0.5 + 0.5
    index_su2 = 3.0 * 0.5 + 0.5
    index_y = (
        6.0 * (1.0 / 6.0) ** 2
        + 3.0 * (-2.0 / 3.0) ** 2
        + 3.0 * (1.0 / 3.0) ** 2
        + 2.0 * (-1.0 / 2.0) ** 2
        + 1.0
    )

    ratio_gp2_g2 = index_su2 / index_y
    sin2 = ratio_gp2_g2 / (1.0 + ratio_gp2_g2)
    g = e_charge / math.sqrt(sin2)
    gp = e_charge / math.sqrt(1.0 - sin2)
    gs = g * math.sqrt(index_su2 / index_su3)

    assert math.isclose(index_su3, 2.0)
    assert math.isclose(index_su2, 2.0)
    assert math.isclose(index_y, 10.0 / 3.0)
    assert math.isclose(ratio_gp2_g2, 3.0 / 5.0)
    assert math.isclose(sin2, 3.0 / 8.0)
    assert math.isclose(gs, g)

    text = f"""# Saída — acoplamentos por normas do fibrado

Classificação: avaliação direta de normas geométricas.

| quantidade | valor |
|---|---:|
| I_3 | {index_su3:.12f} |
| I_2 | {index_su2:.12f} |
| I_Y | {index_y:.12f} |
| g'^2/g^2 | {ratio_gp2_g2:.12f} |
| sin²(theta_W) | {sin2:.12f} |
| alpha usada para normalização ilustrativa | {alpha:.12e} |
| e | {e_charge:.12f} |
| g_s no ponto comum | {gs:.12f} |
| g no ponto comum | {g:.12f} |
| g' no ponto comum | {gp:.12f} |

Interpretação: as razões $g_s=g$, $g'^2/g^2=3/5$ e
$\\sin^2\\theta_W=3/8$ seguem das normas dos geradores em uma geração. A
normalização absoluta por $\\alpha$ é apenas a escala eletromagnética usada
para expressar os números no ponto comum.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
