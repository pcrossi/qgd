#!/usr/bin/env python3
"""
GDQ — Capítulo 13 / Aharonov--Bohm ideal

Objetivo:
    Calcular a fase AB ideal Delta phi = q Phi/(hbar c). Em unidades SI,
    para elétron, a fase pode ser escrita como 2*pi*Phi/Phi0, onde
    Phi0=h/e é o quantum de fluxo AB.

Fonte teórica:
    manuscrito/13_holonomies_ab_sagnac/notes/holonomia_ab_patches_mayer_vietoris.md
    manuscrito/13_holonomies_ab_sagnac/notes/

Classificação:
    Avaliação direta de holonomia ideal. Não inclui solenoide real.

Saída:
    scripts/saida_ab_fase_ideal.md
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_ab_fase_ideal.md"

    h = 6.62607015e-34
    e = 1.602176634e-19
    phi0 = h / e
    fractions = [0.0, 0.25, 0.5, 1.0, 2.0]

    rows = []
    for f in fractions:
        phase = 2.0 * math.pi * f
        hol_re = math.cos(phase)
        hol_im = math.sin(phase)
        rows.append((f, phase, hol_re, hol_im))

    table = "\n".join(
        f"| {f:.2f} | {phase:.12f} | {re:.12f} | {im:.12e} |"
        for f, phase, re, im in rows
    )

    text = f"""# Saída — fase AB ideal

Classificação: avaliação direta de holonomia ideal.

Quantum de fluxo usado:

$$
\\Phi_0=h/e={phi0:.12e}\\,\\mathrm{{Wb}}.
$$

| Phi/Phi0 | Delta phi rad | Re(Hol) | Im(Hol) |
|---:|---:|---:|---:|
{table}

Interpretação: a fase depende somente da holonomia ideal do fluxo enclausurado.
Correções de solenoide real não entram neste script.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
