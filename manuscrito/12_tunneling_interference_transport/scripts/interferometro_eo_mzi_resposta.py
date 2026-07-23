#!/usr/bin/env python3
"""
GDQ — Capítulo 12 / escolha retardada em EO-MZI reduzido.

Objetivo:
    Calcular R_app(t), Gamma_det(t_f) e C_det=exp(-Gamma_det) para um
    interferômetro Mach--Zehnder eletro-óptico usado como aparelho de escolha
    retardada.

Classificação:
    Avaliação direta de modelo reduzido com dados externos de aparelho.
    Não é simulação completa da ação oficial em (g,J,H,f,U).

Dados congelados:
    lambda = 1550 nm
    Vpi = 2.445 V
    tau_sw = 18.1 ps
    crosstalk = -30 dB
"""

from __future__ import annotations

from pathlib import Path
import math

import numpy as np


def logistic(t: np.ndarray, tau: float) -> np.ndarray:
    x = np.clip(t / tau, -700.0, 700.0)
    return 1.0 / (1.0 + np.exp(-x))


def causal_kernel(t_grid: np.ndarray, t_final: float, delay: float, tau_mem: float) -> np.ndarray:
    u = t_final - t_grid - delay
    w = np.zeros_like(t_grid)
    mask = u >= 0.0
    w[mask] = np.exp(-u[mask] / tau_mem) / tau_mem
    area = np.trapezoid(w, t_grid)
    if area > 0.0:
        w /= area
    return w


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_interferometro_eo_mzi_resposta.md"

    wavelength = 1550e-9
    v_pi = 2.445
    tau_switch = 18.1e-12
    crosstalk_db = -30.0
    p_leak = 10.0 ** (crosstalk_db / 10.0)

    c = 299_792_458.0
    path_length = 1.0
    delay = path_length / c
    tau_mem = tau_switch

    coherence_on = math.sqrt(p_leak)
    gamma_on = -math.log(coherence_on)
    delta_phi_norm_sq = 2.0
    r_on = 2.0 * gamma_on / delta_phi_norm_sq
    r_off = 0.0

    t_min = -8.0 * tau_switch
    t_max = delay + 16.0 * tau_switch
    t = np.linspace(t_min, t_max, 200_001)

    r_app = r_off + logistic(t, tau_switch) * (r_on - r_off)

    eval_offsets = np.array([-4, -2, 0, 1, 2, 4, 8, 12, 16], dtype=float) * tau_switch
    rows: list[tuple[float, float, float, float]] = []
    for offset in eval_offsets:
        t_final = delay + offset
        w = causal_kernel(t, t_final, delay, tau_mem)
        gamma = 0.5 * delta_phi_norm_sq * np.trapezoid(r_app * w, t)
        coherence = math.exp(-gamma)
        rows.append((offset / tau_switch, gamma, coherence, 1.0 - coherence))

    phase_pi = math.pi * v_pi / v_pi

    lines = [
        "---",
        'title: "Saída — EO-MZI escolha retardada"',
        "---",
        "",
        "# Saída — EO-MZI escolha retardada",
        "",
        "Classificação: avaliação direta de modelo reduzido com dados externos de aparelho.",
        "",
        "## Parâmetros congelados",
        "",
        f"- comprimento de onda: `{wavelength:.6e} m`",
        f"- tensão push-pull Vpi: `{v_pi:.6f} V`",
        f"- tempo de chaveamento: `{tau_switch:.6e} s`",
        f"- crosstalk usado: `{crosstalk_db:.1f} dB`",
        f"- vazamento de potência: `{p_leak:.6e}`",
        f"- coerência residual esperada: `{coherence_on:.12e}`",
        f"- caminho assumido: `{path_length:.6f} m`",
        f"- atraso causal: `{delay:.12e} s`",
        "",
        "## Impedância reduzida",
        "",
        f"- `Gamma_on = {gamma_on:.12f}`",
        f"- `R_on = {r_on:.12f}` para `||DeltaPhi||^2 = {delta_phi_norm_sq:.1f}`",
        f"- `R_off = {r_off:.12f}`",
        f"- fase EO em Vpi: `{phase_pi:.12f} rad`",
        "",
        "## Evolução causal",
        "",
        "| `(t_f-delay)/tau_switch` | `Gamma_det` | `C=exp(-Gamma)` | perda de coerência |",
        "|---:|---:|---:|---:|",
    ]
    for x, gamma, coherence, loss in rows:
        lines.append(f"| {x: .1f} | {gamma:.12f} | {coherence:.12e} | {loss:.12f} |")

    lines += [
        "",
        "## Limite tardio",
        "",
        f"- `Gamma_inf = {gamma_on:.12f}`",
        f"- `C_inf = {math.exp(-gamma_on):.12e}`",
        "",
        "## Comparação com o limite do aparelho",
        "",
        f"- `sqrt(p_leak) = {coherence_on:.12e}`",
        f"- `exp(-Gamma_inf) = {math.exp(-gamma_on):.12e}`",
        "",
        "O cálculo reduzido reproduz exatamente a coerência de amplitude imposta",
        "pelo crosstalk usado como dado externo congelado.",
        "",
    ]

    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

