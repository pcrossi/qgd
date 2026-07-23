#!/usr/bin/env python3
"""GDQ — Capítulo 20: cadeia térmico-axial do expoente gravitacional.

Classificação:
    avaliação simbólico-numérica de cadeia condicional.

Este script verifica:

    beta_E = 2*pi*R_H
    tau_* = beta_E^2/16
    lambda_ax = 2/R^2
    Delta u_v = tau_* * pi^2 * lambda_ax

e mostra que a condição de colagem R = pi^2*sqrt(alpha)*R_H implica
Delta u_v = 1/(2*alpha). O valor de alpha usado é a média geométrica de
Einstein preservada no Capítulo 16.
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    alpha = 9.0 / (8.0 * math.pi**4) * (math.pi**5 / 1920.0) ** 0.25

    # A cadeia depende apenas da razão R/R_H; por isso R_H=1 é suficiente.
    R_H = 1.0
    beta_E = 2.0 * math.pi * R_H
    tau_star = beta_E**2 / 16.0
    R = math.pi**2 * math.sqrt(alpha) * R_H
    lambda_ax = 2.0 / R**2
    delta_u = tau_star * math.pi**2 * lambda_ax
    target = 1.0 / (2.0 * alpha)
    second_winding_suppression = math.exp(-12.0)

    text = f"""# Saída — cadeia térmico-axial de G

Classificação: avaliação simbólico-numérica de cadeia condicional.

| quantidade | valor |
|---|---:|
| $\\alpha_E^{{\\rm mean}}$ | {alpha:.15e} |
| $(\\alpha_E^{{\\rm mean}})^{{-1}}$ | {1.0 / alpha:.12f} |
| $R_H$ normalizado | {R_H:.12f} |
| $\\beta_E=2\\pi R_H$ | {beta_E:.12f} |
| $\\tau_*=\\beta_E^2/16$ | {tau_star:.12f} |
| $R=\\pi^2\\sqrt\\alpha R_H$ | {R:.12f} |
| $\\lambda_{{\\rm ax}}=2/R^2$ | {lambda_ax:.12f} |
| $\\Delta u_v=\\tau_*\\pi^2\\lambda_{{\\rm ax}}$ | {delta_u:.12f} |
| $1/(2\\alpha)$ | {target:.12f} |
| diferença | {delta_u - target:.3e} |
| supressão relativa do segundo winding $e^{{-12}}$ | {second_winding_suppression:.12e} |

Interpretação: o saddle térmico e o modo axial são calculados diretamente. A
igualdade com $1/(2\\alpha)$ exige a condição global de colagem
$R=\\pi^2\\sqrt\\alpha R_H$.
"""

    assert abs(delta_u - target) < 1e-12
    out = Path(__file__).resolve().parent / "saida_calcular_cadeia_termico_axial_G.md"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
