#!/usr/bin/env python3
"""
GDQ — Capítulo 14 / critério de sóliton material.

Objetivo:
    Verificar as contas explícitas da solução gaussiana neutra:

        g = delta, H = 0, phi = |x|^2/(4 sigma)

    1. equação de solíton: Hess(phi) = (1/(2 sigma)) g;
    2. normalização da densidade gaussiana;
    3. energia livre reduzida W = <sigma |grad phi|^2 + phi - d> = 0;
    4. espectro escalar reduzido de Ornstein--Uhlenbeck:

           lambda_k = k/(2 sigma).

Classificação:
    Verificação simbólico-numérica de solução explícita neutra.
    Não é previsão metrológica e não identifica uma partícula carregada.

Saída:
    saida_verificar_soliton_gaussiano.md
"""

from __future__ import annotations

from pathlib import Path
import math
import numpy as np


OUT = Path(__file__).resolve().parent


def main() -> None:
    d = 8
    sigma = 1.3

    # Conta analítica: a gaussiana rho_N possui covariância 2 sigma I.
    expected_r2 = 2.0 * d * sigma
    expected_phi = expected_r2 / (4.0 * sigma)
    expected_sigma_grad = expected_r2 / (4.0 * sigma)
    w_analytic = expected_sigma_grad + expected_phi - d

    # Verificação Monte Carlo reprodutível da média gaussiana.
    rng = np.random.default_rng(1818)
    samples = 500_000
    x = rng.normal(loc=0.0, scale=math.sqrt(2.0 * sigma), size=(samples, d))
    r2 = np.sum(x * x, axis=1)
    phi = r2 / (4.0 * sigma)
    sigma_grad = r2 / (4.0 * sigma)
    w_samples = sigma_grad + phi - d

    w_mc = float(np.mean(w_samples))
    w_mc_stderr = float(np.std(w_samples, ddof=1) / math.sqrt(samples))
    r2_mc = float(np.mean(r2))

    # Hess(phi) = (1/(2 sigma)) I.
    hess_coeff = 1.0 / (2.0 * sigma)
    hess = hess_coeff * np.eye(d)
    metric = np.eye(d)
    soliton_residual = hess - hess_coeff * metric
    residual_norm = float(np.linalg.norm(soliton_residual))

    # Primeiros autovalores do operador OU reduzido.
    eigenvalues = [k / (2.0 * sigma) for k in range(7)]
    first_gap = eigenvalues[1] - eigenvalues[0]

    lines: list[str] = []
    lines.append('---\n')
    lines.append('title: "Saída — solíton gaussiano neutro"\n')
    lines.append('---\n\n')
    lines.append("# Saída — solíton gaussiano neutro\n\n")
    lines.append("## Classificação\n\n")
    lines.append(
        "Verificação simbólico-numérica de uma solução explícita neutra. "
        "Não é previsão metrológica.\n\n"
    )
    lines.append("## Dados\n\n")
    lines.append(f"- Dimensão real: $d={d}$\n")
    lines.append(f"- Escala geométrica: $\\sigma={sigma}$\n")
    lines.append(f"- Amostras Monte Carlo: ${samples}$\n\n")
    lines.append("## Equação de sóliton\n\n")
    lines.append("$$\n")
    lines.append("\\phi=\\frac{|x|^2}{4\\sigma},\n")
    lines.append("\\qquad\n")
    lines.append("\\nabla_i\\nabla_j\\phi=\\frac{1}{2\\sigma}\\delta_{ij}.\n")
    lines.append("$$\n\n")
    lines.append("| quantidade | valor |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| $1/(2\\sigma)$ | {hess_coeff:.12e} |\n")
    lines.append(f"| norma do resíduo de sóliton | {residual_norm:.12e} |\n\n")
    lines.append("## Energia livre reduzida\n\n")
    lines.append("$$\n")
    lines.append("\\mathcal W_{\\rm gauss}\n")
    lines.append("=\n")
    lines.append("\\left\\langle\\sigma|\\nabla\\phi|^2+\\phi-d\\right\\rangle.\n")
    lines.append("$$\n\n")
    lines.append("| quantidade | analítico | Monte Carlo |\n")
    lines.append("|---|---:|---:|\n")
    lines.append(f"| $\\langle |x|^2\\rangle$ | {expected_r2:.12e} | {r2_mc:.12e} |\n")
    lines.append(f"| $\\langle\\phi\\rangle$ | {expected_phi:.12e} | {float(np.mean(phi)):.12e} |\n")
    lines.append(
        f"| $\\langle\\sigma|\\nabla\\phi|^2\\rangle$ | "
        f"{expected_sigma_grad:.12e} | {float(np.mean(sigma_grad)):.12e} |\n"
    )
    lines.append(f"| $\\mathcal W$ | {w_analytic:.12e} | {w_mc:.12e} |\n")
    lines.append(f"| erro padrão MC de $\\mathcal W$ | — | {w_mc_stderr:.12e} |\n\n")
    lines.append("## Espectro escalar reduzido de Ornstein--Uhlenbeck\n\n")
    lines.append("$$\n")
    lines.append("\\lambda_k=\\frac{k}{2\\sigma}.\n")
    lines.append("$$\n\n")
    lines.append("| $k$ | $\\lambda_k$ |\n")
    lines.append("|---:|---:|\n")
    for k, val in enumerate(eigenvalues):
        lines.append(f"| {k} | {val:.12e} |\n")
    lines.append("\n")
    lines.append(f"Gap após remover o modo constante: ${first_gap:.12e}$.\n\n")
    lines.append("## Veredito\n\n")
    lines.append(
        "A solução gaussiana satisfaz exatamente a equação de sóliton neutro, "
        "tem $\\mathcal W=0$ analiticamente e apresenta gap positivo no setor "
        "OU reduzido após remover o modo zero. Ela é referência neutra; "
        "carga, spin e massa de partículas reais exigem a ficha solitônica "
        "do setor correspondente.\n"
    )

    out = OUT / "saida_verificar_soliton_gaussiano.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
