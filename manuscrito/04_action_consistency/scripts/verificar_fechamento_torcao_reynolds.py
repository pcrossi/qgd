#!/usr/bin/env python3
"""
Capítulo 4 — fechamento torsão--Reynolds do setor eletromagnético.

Classificação:
    avaliação simbólico-numérica de uma cadeia constitutiva.

Verifica:

    Re_Q = n_B^2/(12*pi^2*R^4) = alpha

e a condição estacionária radial

    x^3 - 4*tau*x^2 + tau*n_B^2/pi^2 = 0, x=R^2.

O resultado é adimensional. A conversão em energia física pertence à
calibração metrológica global.
"""

from __future__ import annotations

import math
from pathlib import Path


def solve(alpha: float, n_b: int = 1) -> dict[str, float]:
    if not (0.0 < alpha < 1.0 / 3.0):
        raise ValueError("solução positiva exige 0<alpha<1/3")
    x = abs(n_b) / (math.sqrt(12.0) * math.pi * math.sqrt(alpha))
    radius = math.sqrt(x)
    tau = x**3 / (4.0 * x**2 - n_b * n_b / math.pi**2)
    reynolds = n_b * n_b / (12.0 * math.pi**2 * radius**4)
    residual = x**3 - 4.0 * tau * x**2 + tau * n_b * n_b / math.pi**2
    return {
        "alpha": alpha,
        "radius": radius,
        "tau": tau,
        "lambda_hat": 1.0 / math.sqrt(tau),
        "length_hat": math.pi * math.sqrt(tau),
        "reynolds": reynolds,
        "residual": residual,
    }


def main() -> None:
    scenarios = [
        ("baixa energia — aproximação $1/137$", 1.0 / 137.0),
        ("referência metrológica externa", 1.0 / 137.035999084),
        ("benchmark efetivo de alta energia — $1/128$", 1.0 / 128.0),
    ]
    rows = [(name, solve(alpha)) for name, alpha in scenarios]
    lines = [
        "---",
        'title: "Saída — fechamento torsão-Reynolds"',
        "---",
        "",
        "# Saída — fechamento torsão--Reynolds",
        "",
        "| cenário | $\\alpha$ | $R$ | $\\tau_{\\rm EM}$ | $\\widehat\\Lambda_{\\rm EM}$ | $L/\\ell_C$ | resíduo |",
        "|:---|---:|---:|---:|---:|---:|---:|",
    ]
    for name, row in rows:
        lines.append(
            f"| {name} | `{row['alpha']:.15e}` | `{row['radius']:.12f}` | "
            f"`{row['tau']:.12f}` | `{row['lambda_hat']:.12f}` | "
            f"`{row['length_hat']:.12f}` | `{row['residual']:.3e}` |"
        )
    lines += [
        "",
        "Cada linha satisfaz numericamente:",
        "",
        "$$",
        "\\operatorname{Re}_{\\rm Q}=\\alpha,",
        "\\qquad",
        "x^3-4\\tau x^2+\\frac{\\tau n_B^2}{\\pi^2}=0.",
        "$$",
        "",
        "A linha $1/128$ é benchmark efetivo de alta energia, não entrada",
        "fundamental do fechamento de baixa energia.",
        "",
    ]
    out = Path(__file__).with_name("saida_verificar_fechamento_torcao_reynolds.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

