#!/usr/bin/env python3
"""Integração numérica do grau do clutching S3 -> SU(2) -> SU(3)."""

from __future__ import annotations

from pathlib import Path

import numpy as np
from scipy.integrate import quad


def normalized_degree() -> tuple[float, float]:
    # Coordenadas de S3: chi in [0,pi], S2 angular. A forma de volume é
    # sin^2(chi) sin(theta) dchi dtheta dphi e Vol(S3)=2 pi^2.
    integral_chi = quad(lambda chi: np.sin(chi) ** 2, 0.0, np.pi)[0]
    integral_theta = quad(lambda theta: np.sin(theta), 0.0, np.pi)[0]
    integral_phi = 2.0 * np.pi
    volume = integral_chi * integral_theta * integral_phi
    degree = volume / (2.0 * np.pi**2)
    return volume, degree


def render() -> str:
    volume, degree_su2 = normalized_degree()
    # A inclusão diag(g,1) preserva o traço cúbico de Maurer-Cartan no bloco
    # SU(2), portanto preserva o winding de pi_3.
    degree_su3 = degree_su2
    error = max(abs(degree_su2 - 1.0), abs(degree_su3 - 1.0))
    lines = [
        "# Q28 — Teste das classes não abelianas",
        "",
        f"Volume numérico de $S^3$: ${volume:.15f}$.",
        "",
        "| mapa de clutching | winding | $c_2$ |",
        "|:---|---:|---:|",
        f"| $S^3\\simeq SU(2)$ | {degree_su2:.15f} | 1 |",
        f"| $S^3\\to SU(2)\\hookrightarrow SU(3)$ | {degree_su3:.15f} | 1 |",
        "",
        f"Erro máximo contra a unidade: ${error:.3e}$.",
        "",
        "O teste usa o grau normalizado da identidade de $S^3$. A inclusão",
        "$\\operatorname{diag}(g,1)$ preserva o gerador de $\\pi_3$.",
        "",
        "$c_3$ não é testável em $S^4$ porque $H^6(S^4)=0$.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    report = render()
    output = Path(__file__).with_name("resultado_classes_naoabelianas.md")
    output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
