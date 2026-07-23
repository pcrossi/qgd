#!/usr/bin/env python3
"""GDQ — Capítulo 16: teste diagnóstico Schur/DtN para alpha.

Classificação:
    teste de consistência / diagnóstico geométrico sem ajuste.

O script avalia a impedância reduzida de um canal fotônico radial acoplado a
uma impedância Dirichlet--to--Neumann redonda do elo S^3. Esse teste não fecha
alpha; ele mostra a escala correta da impedância de contorno e registra o
desvio da classe redonda em relação à média cosmológica de Einstein.
"""

from __future__ import annotations

import math
from pathlib import Path


K_BASE = 41.594825709
DELTA_B = -0.2709378871
RADIUS = 1.998411184770


def eigenvalues_2x2(a: float, b: float, d: float) -> tuple[float, float]:
    """Autovalores reais de [[a,b],[b,d]] sem depender de bibliotecas externas."""

    trace = a + d
    det_part = math.sqrt((a - d) ** 2 + 4.0 * b**2)
    return ((trace - det_part) / 2.0, (trace + det_part) / 2.0)


def main() -> None:
    alpha_mean = 9.0 / (8.0 * math.pi**4) * (math.pi**5 / 1920.0) ** 0.25
    z_mean = 1.0 / (4.0 * math.pi * alpha_mean)

    # Kernel fotônico radial neutro preservado no diagnóstico reduzido.
    k0 = K_BASE / 2.0 * (1.0 + DELTA_B)

    # DtN redondo do primeiro harmônico em uma 4-bola com bordo S^3.
    k_boundary = math.pi**2 * RADIUS**2

    # Complemento de Schur para dois canais acoplados por impedância de borda.
    z_reduced = k0 * k_boundary / (k0 + k_boundary)
    alpha_dtn_inv = 4.0 * math.pi * z_reduced

    # Valor de borda que igualaria exatamente a média cosmológica; registrado
    # apenas como diagnóstico, não como parâmetro usado no cálculo.
    s_required = k0 / z_mean - 1.0
    k_boundary_required = k0 / s_required

    eig_min, eig_max = eigenvalues_2x2(
        k0 + k_boundary,
        -k_boundary,
        k_boundary,
    )

    text = f"""# Saída — teste Schur/DtN para alpha

Classificação: teste de consistência / diagnóstico geométrico sem ajuste.

| quantidade | valor |
|---|---:|
| $K_0$ fotônico radial | {k0:.12f} |
| $K_\\partial^{{\\rm DtN}}=\\pi^2R^2$ | {k_boundary:.12f} |
| $Z_{{Q,\\rm red}}^E=K_0K_\\partial/(K_0+K_\\partial)$ | {z_reduced:.12f} |
| $(\\alpha_{{\\rm DtN}}^{{\\rm red}})^{{-1}}$ | {alpha_dtn_inv:.12f} |
| $Z_Q^E$ da média de Einstein | {z_mean:.12f} |
| $(\\alpha_E^{{\\rm mean}})^{{-1}}$ | {1.0 / alpha_mean:.12f} |
| erro relativo em $Z_Q$ | {(z_reduced / z_mean - 1.0) * 100.0:.6f}% |
| $K_\\partial$ exigido pela média | {k_boundary_required:.12f} |
| desvio DtN/exigido | {(k_boundary / k_boundary_required - 1.0) * 100.0:.6f}% |
| menor autovalor da Hessiana reduzida | {eig_min:.12f} |
| maior autovalor da Hessiana reduzida | {eig_max:.12f} |

Interpretação: o teste redondo tem Hessiana positiva e produz a escala correta,
mas não coincide exatamente com a média cosmológica. O resultado final usado no
texto é a média de Einstein; este teste fica como diagnóstico da rota DtN.
"""

    assert eig_min > 0.0
    out = Path(__file__).resolve().parent / "saida_teste_schur_dtn_alpha.md"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
