#!/usr/bin/env python3
"""
GDQ — Capítulo 17 / convergência do raio de superfície do próton.

Classificação:
    teste de consistência do observável de superfície.

O raio eletromagnético do próton não é a média volumétrica do autovetor radial
interno. Na redução GDQ usada no capítulo, ele é um observável de borda:

    r_p = C_r * epsilon_eff * R_B,
    C_r = (1/8)(1 + alpha/4),
    R_B = (3/2) Lambda_C.

Este script regulariza a delta de superfície por uma meia-gaussiana e verifica
que o limite sigma -> 0 converge para o raio estrutural.
"""

from __future__ import annotations

import math
from pathlib import Path


def half_gaussian_shell_radius(epsilon_eff: float, c_scale: float, sigma: float) -> float:
    """Raio RMS de uma casca de borda regularizada em chi >= epsilon_eff."""
    mean_chi2 = (
        epsilon_eff**2
        + 2.0 * epsilon_eff * sigma / math.sqrt(math.pi)
        + 0.5 * sigma**2
    )
    return c_scale * math.sqrt(mean_chi2)


def main() -> None:
    alpha = 1.0 / 137.035999177
    lambda_c_fm = 386.159268
    r_b = 1.5 * lambda_c_fm
    epsilon_eff = 0.011591040463
    c_r = 0.125 * (1.0 + alpha / 4.0)
    c_scale = c_r * r_b
    r_p = c_scale * epsilon_eff

    rows: list[tuple[float, float, float]] = []
    for frac in [1 / 2, 1 / 4, 1 / 8, 1 / 16, 1 / 32, 1 / 64, 1 / 128, 1 / 256]:
        sigma = epsilon_eff * frac
        r_sigma = half_gaussian_shell_radius(epsilon_eff, c_scale, sigma)
        rows.append((frac, r_sigma, (r_sigma - r_p) / r_p))

    lines = [
        "---",
        'title: "Saída — convergência do raio de superfície"',
        "---",
        "",
        "# Saída — convergência do raio de superfície",
        "",
        "## Fórmula estrutural",
        "",
        "$$",
        "r_p",
        "=",
        "C_r\\epsilon_{\\rm eff}R_B,",
        "\\qquad",
        "C_r=\\frac18\\left(1+\\frac\\alpha4\\right),",
        "\\qquad",
        "R_B=\\frac32\\Lambda_C.",
        "$$",
        "",
        "| quantidade | valor |",
        "|---|---:|",
        f"| $\\Lambda_C$ | `{lambda_c_fm:.6f}` fm |",
        f"| $R_B$ | `{r_b:.12f}` fm |",
        f"| $\\epsilon_{{\\rm eff}}$ | `{epsilon_eff:.12f}` |",
        f"| $C_r$ | `{c_r:.15f}` |",
        f"| $r_p$ estrutural | `{r_p:.12f}` fm |",
        "",
        "## Regularização por meia-gaussiana",
        "",
        "| $\\sigma/\\epsilon_{\\rm eff}$ | $r_p(\\sigma)$ fm | desvio relativo |",
        "|---:|---:|---:|",
    ]
    for frac, r_sigma, rel in rows:
        lines.append(f"| `{frac:.8f}` | `{r_sigma:.12f}` | `{rel:+.12e}` |")
    lines.append(f"| `delta_surface` | `{r_p:.12f}` | `{0.0:+.12e}` |")
    lines.extend(
        [
            "",
            "## Veredito",
            "",
            "A sequência regularizada converge para a delta de superfície. O cálculo",
            "volumétrico radial bruto mede modo interno do bulk, não o raio",
            "eletromagnético observado.",
            "",
        ]
    )

    out = Path(__file__).with_name("saida_convergencia_raio_superficie.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
