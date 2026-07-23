#!/usr/bin/env python3
"""
GDQ — Capítulo 15 / Hessiana 8D e complemento de Schur

Objetivo:
    Verificar o fechamento produto J=0 e o critério warped/misto:

        H_eff = H_B - J H_perp^{-1} J^T

    A matriz é reduzida e autocontida; ela ilustra o operador de Schur usado
    no texto, sem fingir ser o background 8D metrológico completo.

Classificação:
    Teste de consistência da Hessiana 8D reduzida.

Saída:
    scripts/saida_hessiana_8d_schur.md
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


def schur(h_b: np.ndarray, h_perp: np.ndarray, j: np.ndarray) -> np.ndarray:
    return h_b - j @ np.linalg.solve(h_perp, j.T)


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_hessiana_8d_schur.md"

    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    r_mu = 1.5 * alpha_inv + 6.0 / 5.0 + 2.0 * alpha
    h_b = np.diag([1.0, r_mu, 3477.446405098381])

    h_perp = np.eye(3)
    j_product = np.zeros((3, 3))
    h_eff_product = schur(h_b, h_perp, j_product)

    # Warped/misto reduzido: mistura subcrítica de norma controlada.
    j_mix = 0.1 * np.eye(3)
    h_eff_mix = schur(h_b, h_perp, j_mix)
    correction_norm = float(np.linalg.norm(j_mix @ np.linalg.solve(h_perp, j_mix.T), 2))
    lambda_gap = 0.5
    criterion = correction_norm < lambda_gap

    text = f"""# Saída — Hessiana 8D por Schur

Classificação: teste de consistência da Hessiana 8D reduzida.

## Produto

| quantidade | valor |
|---|---:|
| ||J|| produto | {np.linalg.norm(j_product):.12e} |
| max |H_eff-H_B| produto | {np.max(np.abs(h_eff_product-h_b)):.12e} |

## Warped/misto reduzido

| quantidade | valor |
|---|---:|
| ||Sigma|| | {correction_norm:.12e} |
| lambda_gap | {lambda_gap:.12e} |
| subcrítico | {criterion} |

Interpretação: no produto exato, $J=0$ e a hierarquia reduzida é herdada sem
correção. Em um setor misto, a correção é controlada por
$j_{{\\rm mix}}^2/m_\\perp^2$ e deve ser comparada ao gap do bloco material.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
