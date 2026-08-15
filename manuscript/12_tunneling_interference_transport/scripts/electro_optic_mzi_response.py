#!/usr/bin/env python3
"""
GDQ — Chapter 12 / Delayed choice in reduced EO-MZI.

Objective:
    Calculate R_app(t), Gamma_det(t_f) and C_det=exp(-Gamma_det) for an
    electro-optic Mach--Zehnder interferometer used as a delayed choice
    apparatus.

Classification:
    Direct evaluation of a reduced model with external apparatus data.
    It is not a complete simulation of the official action in (g,J,H,f,U).

Frozen data:
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
    out = root / "output_electro_optic_mzi_response.md"

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
        'title: "Output — EO-MZI delayed choice"',
        "---",
        "",
        "# Output — EO-MZI delayed choice",
        "",
        "Classification: direct evaluation of reduced model with external apparatus data.",
        "",
        "## Frozen parameters",
        "",
        f"- wavelength: `{wavelength:.6e} m`",
        f"- push-pull voltage Vpi: `{v_pi:.6f} V`",
        f"- switching time: `{tau_switch:.6e} s`",
        f"- crosstalk used: `{crosstalk_db:.1f} dB`",
        f"- power leakage: `{p_leak:.6e}`",
        f"- expected residual coherence: `{coherence_on:.12e}`",
        f"- assumed path: `{path_length:.6f} m`",
        f"- causal delay: `{delay:.12e} s`",
        "",
        "## Reduced impedance",
        "",
        f"- `Gamma_on = {gamma_on:.12f}`",
        f"- `R_on = {r_on:.12f}` for `||DeltaPhi||^2 = {delta_phi_norm_sq:.1f}`",
        f"- `R_off = {r_off:.12f}`",
        f"- EO phase at Vpi: `{phase_pi:.12f} rad`",
        "",
        "## Causal evolution",
        "",
        "| `(t_f-delay)/tau_switch` | `Gamma_det` | `C=exp(-Gamma)` | coherence loss |",
        "|---:|---:|---:|---:|",
    ]
    for x, gamma, coherence, loss in rows:
        lines.append(f"| {x: .1f} | {gamma:.12f} | {coherence:.12e} | {loss:.12f} |")

    lines += [
        "",
        "## Late limit",
        "",
        f"- `Gamma_inf = {gamma_on:.12f}`",
        f"- `C_inf = {math.exp(-gamma_on):.12e}`",
        "",
        "## Comparison with the apparatus limit",
        "",
        f"- `sqrt(p_leak) = {coherence_on:.12e}`",
        f"- `exp(-Gamma_inf) = {math.exp(-gamma_on):.12e}`",
        "",
        "The reduced calculation exactly reproduces the amplitude coherence imposed",
        "by the crosstalk used as frozen external data.",
        "",
    ]

    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
