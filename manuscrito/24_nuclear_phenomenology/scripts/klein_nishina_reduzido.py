#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `klein nishina reduzido` associada ao capítulo `24_nuclear_phenomenology`.
Verificação reduzida de Klein--Nishina.

Classificação científica:
    teste de consistência de redução assintótica.

O script calcula a seção diferencial em unidades de r_e^2 e verifica o limite
Thomson quando x=E/(m_e c^2) tende a zero. A normalização r_e^2 é usada como
unidade de comparação angular; sua derivação 8D completa fica fora deste
verificador reduzido.
"""

from __future__ import annotations

from math import cos, pi
from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_klein_nishina_reduzido.md"


def energy_ratio(x: float, theta: float) -> float:
    """Return E'/E for Compton scattering."""
    return 1.0 / (1.0 + x * (1.0 - cos(theta)))


def klein_nishina_over_re2(x: float, theta: float) -> float:
    """Return (d sigma / d Omega) / r_e^2."""
    r = energy_ratio(x, theta)
    sin2 = 1.0 - cos(theta) ** 2
    return 0.5 * r * r * (r + 1.0 / r - sin2)


def thomson_over_re2(theta: float) -> float:
    """Return the Thomson angular factor in units of r_e^2."""
    return 0.5 * (1.0 + cos(theta) ** 2)


def main() -> None:
    angles_deg = [0, 30, 60, 90, 120, 150, 180]
    xs = [1e-6, 0.1, 1.0, 10.0]

    lines: list[str] = []
    lines.append("# Saída — Klein--Nishina reduzido\n\n")
    lines.append("Classificação: teste de consistência de redução assintótica.\n\n")
    lines.append("Normalização:\n\n")
    lines.append("$$\n")
    lines.append("\\frac{d\\sigma}{d\\Omega}\n")
    lines.append("=\n")
    lines.append("\\frac{r_e^2}{2}\n")
    lines.append("\\left(\\frac{E'}{E}\\right)^2\n")
    lines.append("\\left(\\frac{E'}{E}+\\frac{E}{E'}-\\sin^2\\theta\\right).\n")
    lines.append("$$\n\n")

    for x in xs:
        lines.append(f"## x = {x:g}\n\n")
        lines.append("| theta(deg) | E'/E | KN/r_e^2 | Thomson/r_e^2 | diferença rel. |\n")
        lines.append("|---:|---:|---:|---:|---:|\n")
        for deg in angles_deg:
            theta = pi * deg / 180.0
            r = energy_ratio(x, theta)
            kn = klein_nishina_over_re2(x, theta)
            th = thomson_over_re2(theta)
            rel = (kn - th) / th if th else 0.0
            lines.append(f"| {deg} | {r:.12f} | {kn:.12f} | {th:.12f} | {rel:+.6e} |\n")
        lines.append("\n")

    lines.append("## Limite Thomson em theta = 90 graus\n\n")
    lines.append("| x | diferença relativa |\n")
    lines.append("|---:|---:|\n")
    theta = pi / 2.0
    for x in [1e-3, 1e-4, 1e-5, 1e-6]:
        kn = klein_nishina_over_re2(x, theta)
        th = thomson_over_re2(theta)
        rel = (kn - th) / th
        lines.append(f"| {x:g} | {rel:+.6e} |\n")

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

