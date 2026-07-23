#!/usr/bin/env python3
"""
GDQ — Capítulo 13 / Sagnac ideal

Objetivo:
    Calcular Delta t, fase óptica e fase de matéria para um circuito rotativo.

Fonte teórica:
    manuscrito/13_holonomies_ab_sagnac/notes/sagnac_forma_relogio.md
    manuscrito/13_holonomies_ab_sagnac/notes/

Classificação:
    Avaliação direta ideal. Não inclui fibra real, dispersão nem perdas.

Saída:
    scripts/saida_sagnac_luz_materia.md
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_sagnac_luz_materia.md"

    c = 299_792_458.0
    hbar = 1.054571817e-34
    omega = 7.2921150e-5
    area = 1.0
    wavelength = 632.8e-9
    mass_neutron = 1.67492749804e-27

    dt = 4.0 * omega * area / c**2
    phase_light = 8.0 * math.pi * omega * area / (wavelength * c)
    phase_matter = 4.0 * mass_neutron * omega * area / hbar

    text = f"""# Saída — Sagnac luz e matéria

Classificação: avaliação direta ideal.

Parâmetros de exemplo:

| parâmetro | valor |
|---|---:|
| Omega | {omega:.12e} rad/s |
| área | {area:.12e} m^2 |
| lambda óptico | {wavelength:.12e} m |
| massa de nêutron | {mass_neutron:.12e} kg |

Resultados:

| quantidade | valor |
|---|---:|
| Delta t Sag | {dt:.12e} s |
| fase óptica | {phase_light:.12e} rad |
| fase matéria | {phase_matter:.12e} rad |

Interpretação: Sagnac mede holonomia de relógio/contorno rotativo, não
holonomia eletromagnética AB.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
