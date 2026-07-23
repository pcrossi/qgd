#!/usr/bin/env python3
"""
Q72 — resposta reduzida de um interferômetro de escolha retardada.

Classificação:
    - avaliação direta de modelo reduzido derivado da Q44/Q72;
    - não é simulação completa da ação oficial;
    - parâmetros do aparelho são externos e congelados antes do cálculo.

Modelo:
    R_app(t) = R_off + s(t-t_c)(R_on-R_off)
    Gamma(t_f) = 1/2 ∫ <ΔΦ, R_app(t) ΔΦ> w(t_f,t) dt
    C(t_f) = exp(-Gamma)

O kernel w é causal, normalizado e exponencial após o retardo de transporte.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


def logistic(t: np.ndarray, tau: float) -> np.ndarray:
    x = np.clip(t / tau, -700.0, 700.0)
    return 1.0 / (1.0 + np.exp(-x))


def causal_kernel(t_grid: np.ndarray, t_final: float, delay: float, tau_mem: float) -> np.ndarray:
    """Kernel causal normalizado que pesa o histórico do aparelho."""
    u = t_final - t_grid - delay
    w = np.zeros_like(t_grid)
    mask = u >= 0.0
    w[mask] = np.exp(-u[mask] / tau_mem) / tau_mem
    area = np.trapezoid(w, t_grid)
    if area > 0.0:
        w /= area
    return w


def main() -> None:
    # Parâmetros físicos congelados do aparelho.
    # Referência de projeto EO-MZI: λ=1550 nm, Vπ(push-pull)=2.445 V,
    # tempo de chaveamento 18.1 ps, crosstalk < -30 dB.
    wavelength = 1550e-9
    v_pi = 2.445
    tau_switch = 18.1e-12
    crosstalk_db = -30.0
    p_leak = 10.0 ** (crosstalk_db / 10.0)

    # Geometria de laboratório assumida para avaliação:
    # interferômetro compacto de caminho de 1 m em ar.
    c = 299_792_458.0
    n_eff = 1.0
    path_length = 1.0
    delay = n_eff * path_length / c

    # Tempo de memória do kernel: tempo de chaveamento como escala material.
    tau_mem = tau_switch

    # Impedância reduzida.
    # R_off = 0: recombinação coerente ideal.
    # R_on é fixado pelo vazamento/crosstalk do canal de caminho:
    # C_on ≈ sqrt(p_leak); Gamma_on = -ln(C_on).
    coherence_on = math.sqrt(p_leak)
    gamma_on = -math.log(coherence_on)
    delta_phi_norm_sq = 2.0
    r_on = 2.0 * gamma_on / delta_phi_norm_sq
    r_off = 0.0

    # Janela temporal em torno da chegada ao aparelho.
    t_choice = 0.0
    t_min = -8.0 * tau_switch
    t_max = delay + 16.0 * tau_switch
    n_grid = 200_001
    t = np.linspace(t_min, t_max, n_grid)

    s = logistic(t - t_choice, tau_switch)
    r_app = r_off + s * (r_on - r_off)

    # Avaliar Gamma para vários tempos finais após a escolha.
    eval_offsets = np.array([-4, -2, 0, 1, 2, 4, 8, 12, 16], dtype=float) * tau_switch
    rows = []
    for offset in eval_offsets:
        t_final = delay + offset
        w = causal_kernel(t, t_final, delay, tau_mem)
        gamma = 0.5 * delta_phi_norm_sq * np.trapezoid(r_app * w, t)
        coh = math.exp(-gamma)
        rows.append((offset / tau_switch, gamma, coh, 1.0 - coh))

    # Valor estacionário tardio.
    gamma_inf = gamma_on
    coh_inf = math.exp(-gamma_inf)

    # Fase eletro-óptica na tensão Vπ.
    phase_pi = math.pi * v_pi / v_pi

    out = []
    out.append("# Saída — Q72 resposta reduzida de interferômetro realista")
    out.append("")
    out.append("## Parâmetros congelados")
    out.append("")
    out.append(f"- comprimento de onda: `{wavelength:.6e} m`")
    out.append(f"- tensão push-pull Vpi: `{v_pi:.6f} V`")
    out.append(f"- tempo de chaveamento: `{tau_switch:.6e} s`")
    out.append(f"- crosstalk usado: `{crosstalk_db:.1f} dB`")
    out.append(f"- vazamento de potência: `{p_leak:.6e}`")
    out.append(f"- coerência residual estimada: `sqrt(p_leak) = {coherence_on:.6e}`")
    out.append(f"- caminho assumido: `{path_length:.6f} m`")
    out.append(f"- atraso causal: `{delay:.6e} s`")
    out.append("")
    out.append("## Impedância reduzida")
    out.append("")
    out.append(f"- `Gamma_on = -ln(sqrt(p_leak)) = {gamma_on:.12f}`")
    out.append(f"- `R_on = {r_on:.12f}` para `||DeltaPhi||^2 = {delta_phi_norm_sq:.1f}`")
    out.append(f"- `R_off = {r_off:.12f}`")
    out.append(f"- fase EO em Vpi: `{phase_pi:.12f} rad`")
    out.append("")
    out.append("## Evolução causal")
    out.append("")
    out.append("| `(t_f-delay)/tau_switch` | `Gamma_det` | `C=exp(-Gamma)` | perda de coerência |")
    out.append("|---:|---:|---:|---:|")
    for x, gamma, coh, loss in rows:
        out.append(f"| {x: .1f} | {gamma:.12f} | {coh:.12e} | {loss:.12f} |")
    out.append("")
    out.append("## Limite tardio")
    out.append("")
    out.append(f"- `Gamma_inf = {gamma_inf:.12f}`")
    out.append(f"- `C_inf = {coh_inf:.12e}`")
    out.append("")
    out.append("## Classificação")
    out.append("")
    out.append("Avaliação direta do modelo reduzido Q44/Q72 com parâmetros externos de aparelho.")
    out.append("Não é simulação completa de `(g,J,H,f,U)` pela ação oficial.")

    output_path = Path(__file__).with_name("saida_resposta_interferometro_q72.md")
    output_path.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
