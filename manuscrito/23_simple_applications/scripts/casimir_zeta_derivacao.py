#!/usr/bin/env python3
"""
GDQ — Capítulo 23 / Casimir ideal

Objetivo:
    Verificar simbolicamente o coeficiente universal do efeito Casimir ideal
    entre placas paralelas perfeitas.

Classificação:
    Teste simbólico de consistência da redução espectral. Não é ajuste
    experimental e não modela placas reais.

Equações:
    E/A = (hbar*c/2)*2*sum_n int d^2k/(2*pi)^2 sqrt(k^2 + (n*pi/a)^2)

    int d^2k/(2*pi)^2 sqrt(k^2+m^2) -> -m^3/(6*pi)

    zeta(-3)=1/120

    E/A = -pi^2*hbar*c/(720*a^3)
    P   = -pi^2*hbar*c/(240*a^4)

Saída:
    saida_casimir_zeta_derivacao.md
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


OUT = Path(__file__).with_name("saida_casimir_zeta_derivacao.md")


def main() -> None:
    zeta_minus_3 = Fraction(1, 120)

    # Coeficiente de energia:
    # -(1/(6*pi))*(pi^3)*zeta(-3) = -pi^2*(zeta(-3)/6).
    energy_coeff = -zeta_minus_3 / 6

    # Se E/A = -C/a^3, então P = -d(E/A)/da = -3C/a^4.
    pressure_coeff = 3 * energy_coeff

    lines = [
        "---",
        'title: "Saída — derivação zeta do Casimir ideal"',
        "---",
        "",
        "# Saída — derivação zeta do Casimir ideal",
        "",
        "Classificação: teste simbólico de consistência espectral.",
        "",
        "A integral regularizada usada é:",
        "",
        "$$",
        "\\int\\frac{d^2k}{(2\\pi)^2}\\sqrt{k^2+m^2}",
        "\\longmapsto",
        "-\\frac{m^3}{6\\pi}.",
        "$$",
        "",
        "A soma espectral é:",
        "",
        "$$",
        "\\zeta(-3)=\\frac{1}{120}.",
        "$$",
        "",
        "Coeficiente obtido para a energia:",
        "",
        "$$",
        f"\\frac{{\\Delta E}}{{A}}={energy_coeff}\\,\\frac{{\\pi^2\\hbar c}}{{a^3}}.",
        "$$",
        "",
        "Coeficiente obtido para a pressão:",
        "",
        "$$",
        f"P={pressure_coeff}\\,\\frac{{\\pi^2\\hbar c}}{{a^4}}.",
        "$$",
        "",
        "Forma convencional:",
        "",
        "$$",
        "\\frac{\\Delta E}{A}=-\\frac{\\pi^2\\hbar c}{720a^3},",
        "\\qquad",
        "P=-\\frac{\\pi^2\\hbar c}{240a^4}.",
        "$$",
        "",
        "Interpretação: o fator 720 vem de duas polarizações transversais,",
        "continuação dimensional da integral transversal e zeta(-3)=1/120.",
        "Na GDQ isso é a avaliação do determinante da Hessiana efetiva ideal,",
        "não uma alteração da ação oficial.",
        "",
    ]

    text = "\n".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
