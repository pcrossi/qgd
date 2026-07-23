#!/usr/bin/env python3
"""Q43 — cálculo líder de Zeeman/g-2 na GDQ.

Este script calcula apenas o termo líder estrutural

    a^(1) = alpha / (2*pi)
    g^(1) = 2 * (1 + a^(1))

e o resíduo que teria de ser produzido pelos termos superiores da Hessiana
GDQ. Não ajusta parâmetros e não calcula H_C^{-1} m_perp.
"""

from __future__ import annotations

import math
from pathlib import Path


ALPHA_INV_METROLOGICAL = 137.035999177
ALPHA_GDQ_GEOMETRIC = 0.007297348130032
G_E_REFERENCE = 2.00231930436092


def evaluate(alpha: float, g_reference: float) -> dict[str, float]:
    a1 = alpha / (2.0 * math.pi)
    g1 = 2.0 * (1.0 + a1)
    residual_g = g_reference - g1
    residual_a = residual_g / 2.0
    ppm_g = residual_g / g_reference * 1.0e6
    return {
        "alpha": alpha,
        "alpha_inv": 1.0 / alpha,
        "a1": a1,
        "g1": g1,
        "residual_g": residual_g,
        "residual_a": residual_a,
        "ppm_g": ppm_g,
    }


def md_table(rows: list[tuple[str, dict[str, float]]]) -> str:
    lines = [
        "| caso | alpha^-1 | a1=alpha/(2pi) | g_lider | g_ref-g_lider | ppm em g |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for name, r in rows:
        lines.append(
            "| {name} | {alpha_inv:.12f} | {a1:.15e} | {g1:.15f} | "
            "{residual_g:.15e} | {ppm_g:.6f} |".format(name=name, **r)
        )
    return "\n".join(lines)


def main() -> None:
    alpha_met = 1.0 / ALPHA_INV_METROLOGICAL
    rows = [
        ("alpha metrologica", evaluate(alpha_met, G_E_REFERENCE)),
        ("alpha geometrica GDQ", evaluate(ALPHA_GDQ_GEOMETRIC, G_E_REFERENCE)),
    ]

    lines = [
        "# Q43 — saída do cálculo líder de g-2",
        "",
        "Classificação: avaliação direta do termo líder já derivado; não é cálculo metrológico completo.",
        "",
        md_table(rows),
        "",
        "## Leitura",
        "",
        "O termo líder reproduz a escala de Schwinger:",
        "",
        "$$",
        "a^{(1)}=\\frac{\\alpha}{2\\pi}.",
        "$$",
        "",
        "O resíduo `g_ref-g_lider` é o que deve ser explicado por termos superiores da Hessiana física:",
        "",
        "$$",
        "a_{\\rm resto}=a_{\\rm exp}-\\frac{\\alpha}{2\\pi}.",
        "$$",
        "",
        "Sem construir `H_C^{-1}m_perp`, esse resíduo não deve ser chamado de previsto.",
        "",
    ]

    out = Path(__file__).with_name("saida_g2_lider_q43.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)
    print("\n".join(lines))


if __name__ == "__main__":
    main()

