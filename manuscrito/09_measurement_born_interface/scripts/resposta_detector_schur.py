#!/usr/bin/env python3
"""
GDQ — Capítulo 9 / Resposta reduzida de detector

Objetivo:
    Calcular uma impedância de aparelho por complemento de Schur e avaliar
    o fator de coerência exp(-Gamma_det) em um toy model.

Fonte teórica:
    manuscrito/09_measurement_born_interface/notes/aparelho_como_contorno_hessiana_schur.md
    manuscrito/09_measurement_born_interface/notes/construcao_gdq_medida.md

Classificação:
    Redução efetiva/aparelho. Não é previsão metrológica.

Saída:
    manuscrito/09_measurement_born_interface/scripts/saida_resposta_detector_schur.md
"""

from __future__ import annotations

import numpy as np
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_resposta_detector_schur.md"

    k_boundary = np.array([[2.0, 0.15], [0.15, 1.5]])
    k_internal = np.array([[4.0, 0.2], [0.2, 3.0]])
    k_coupling = np.array([[0.7, 0.1], [0.05, 0.4]])

    r_app = k_boundary - k_coupling @ np.linalg.inv(k_internal) @ k_coupling.T
    delta_phi = np.array([1.0, -1.0])
    gamma = 0.5 * float(delta_phi @ r_app @ delta_phi)
    coherence = float(np.exp(-gamma))
    eigs = np.linalg.eigvalsh(r_app)

    text = f"""# Saída — resposta reduzida de detector por Schur

Classificação: redução efetiva/aparelho.

## Matriz de impedância

$$
\\mathsf R_{{\\rm app}}
=
\\begin{{pmatrix}}
{r_app[0,0]:.12f} & {r_app[0,1]:.12f} \\\\
{r_app[1,0]:.12f} & {r_app[1,1]:.12f}
\\end{{pmatrix}}.
$$

## Verificações

| teste | valor |
|---|---:|
| autovalor mínimo de R_app | {eigs.min():.12f} |
| autovalor máximo de R_app | {eigs.max():.12f} |
| Gamma_det | {gamma:.12f} |
| C_det = exp(-Gamma_det) | {coherence:.12f} |

Interpretação: a resposta de detector positiva reduz a coerência por
$\\mathcal C_{{\\rm det}}=e^{{-\\Gamma_{{\\rm det}}}}$. Os números são de toy model.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
