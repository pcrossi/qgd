#!/usr/bin/env python3
"""
GDQ — Capítulo 19 / Yukawa como overlap.

Demonstra em um modelo de base ortonormal que uma matriz efetiva de massa
vem de overlaps:

    Y_ij = <psi_L_i, Phi_EW psi_R_j>.

Não calcula CKM/PMNS reais; apenas documenta a estrutura que substitui
Yukawas fundamentais.

Classificação: script simbólico didático.
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_yukawa_overlap_demo.md"

    # Base toy ortonormal; Phi_EW atua como operador de mistura geométrico.
    phi = np.array(
        [
            [1.0, 0.12, 0.01],
            [0.12, 0.35, 0.04],
            [0.01, 0.04, 0.08],
        ]
    )
    # Simetrização para representar uma Hessiana/overlap real reduzido.
    y_geom = 0.5 * (phi + phi.T)
    eig = np.linalg.eigvalsh(y_geom)

    text = f"""# Saída — Yukawa como overlap geométrico

Classificação: script simbólico didático.

Matriz de overlap reduzida:

| i | y_i |
|---|---:|
| 1 | {eig[0]:.12f} |
| 2 | {eig[1]:.12f} |
| 3 | {eig[2]:.12f} |

Interpretação: a matriz efetiva vem de overlaps de modos. Os números deste
script são toy e não entram como previsão; o objetivo é fixar a forma
$Y_{{ij}}^{{geom}}=<\\psi_L,\\Phi_{{EW}}\\psi_R>$.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
