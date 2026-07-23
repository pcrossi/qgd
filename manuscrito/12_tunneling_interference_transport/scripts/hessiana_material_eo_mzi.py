#!/usr/bin/env python3
"""
GDQ — Capítulo 12 / Hessiana material reduzida de EO-MZI.

Objetivo:
    Construir o modelo reduzido T_MZI=C(theta2)P(phi,eta)C(theta1) e calcular
    quais imperfeições materiais isoladas produzem crosstalk de -30 dB.

Classificação:
    Modelo material reduzido de engenharia. O resultado localiza o crosstalk
    em delta K_app material/fabricação/perdas, não na ação fundamental.
"""

from __future__ import annotations

from pathlib import Path
import math

import numpy as np


def coupler(theta: float) -> np.ndarray:
    c = math.cos(theta)
    s = math.sin(theta)
    return np.array([[c, 1j * s], [1j * s, c]], dtype=complex)


def phase_arm(phi: float, amp_ratio: float = 1.0) -> np.ndarray:
    return np.diag([np.exp(0.5j * phi), amp_ratio * np.exp(-0.5j * phi)])


def mzi_transfer(
    phi: float,
    theta1: float = math.pi / 4,
    theta2: float = math.pi / 4,
    amp_ratio: float = 1.0,
) -> np.ndarray:
    return coupler(theta2) @ phase_arm(phi, amp_ratio=amp_ratio) @ coupler(theta1)


def powers(
    phi: float,
    theta1: float = math.pi / 4,
    theta2: float = math.pi / 4,
    amp_ratio: float = 1.0,
) -> tuple[float, float]:
    tin = np.array([1.0 + 0j, 0.0 + 0j])
    out = mzi_transfer(phi, theta1=theta1, theta2=theta2, amp_ratio=amp_ratio) @ tin
    p = np.abs(out) ** 2
    return float(p[0]), float(p[1])


def extinction_from_phase_error(delta_phi: float) -> float:
    p0, p1 = powers(math.pi + delta_phi)
    return min(p0, p1) / max(max(p0, p1), 1e-300)


def extinction_from_amp_eps(eps: float) -> float:
    p0, p1 = powers(math.pi, amp_ratio=1.0 - eps)
    return min(p0, p1) / max(max(p0, p1), 1e-300)


def extinction_from_coupler_error(delta_theta: float) -> float:
    p0, p1 = powers(math.pi, theta1=math.pi / 4 + delta_theta, theta2=math.pi / 4)
    return min(p0, p1) / max(max(p0, p1), 1e-300)


def bisect_positive(func, target: float, hi: float) -> float:
    lo = 0.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if func(mid) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_hessiana_material_eo_mzi.md"

    wavelength = 1550e-9
    vpi = 2.445
    tau_sw = 18.1e-12
    target_xt_db = -30.0
    target = 10.0 ** (target_xt_db / 10.0)

    p0_ideal, p1_ideal = powers(math.pi)
    p_dark_ideal = min(p0_ideal, p1_ideal)
    p_bright_ideal = max(p0_ideal, p1_ideal)
    xt_ideal = p_dark_ideal / max(p_bright_ideal, 1e-300)

    delta_phi_req = bisect_positive(extinction_from_phase_error, target, hi=0.2)
    voltage_error_req = delta_phi_req / math.pi * vpi

    eps_amp_req = bisect_positive(extinction_from_amp_eps, target, hi=0.2)
    amp_ratio_req = 1.0 - eps_amp_req
    amp_db = 20.0 * math.log10(amp_ratio_req)

    delta_theta_req = bisect_positive(extinction_from_coupler_error, target, hi=0.2)
    coupler_split = math.sin(math.pi / 4 + delta_theta_req) ** 2

    gamma_target = -math.log(math.sqrt(target))
    r_target = gamma_target

    lines = [
        "---",
        'title: "Saída — Hessiana material EO-MZI"',
        "---",
        "",
        "# Saída — Hessiana material reduzida EO-MZI",
        "",
        "Classificação: modelo material reduzido de engenharia.",
        "",
        "## Dados congelados",
        "",
        f"- lambda = `{wavelength:.6e} m`",
        f"- Vpi = `{vpi:.6f} V`",
        f"- tau_sw = `{tau_sw:.6e} s`",
        f"- alvo de referência para comparação: `{target_xt_db:.1f} dB`",
        "",
        "## Transferência ideal",
        "",
        f"- fase em Vpi: `{math.pi:.12f} rad`",
        f"- potência porto escuro ideal: `{p_dark_ideal:.12e}`",
        f"- potência porto claro ideal: `{p_bright_ideal:.12e}`",
        f"- crosstalk ideal: `{xt_ideal:.12e}`",
        "",
        "## Imperfeições materiais equivalentes a -30 dB",
        "",
        f"- erro de fase requerido: `delta_phi = {delta_phi_req:.12e} rad`",
        f"- erro equivalente de tensão: `delta_V = {voltage_error_req:.12e} V`",
        f"- erro relativo de tensão: `{voltage_error_req / vpi:.12e}`",
        f"- razão de amplitude requerida isoladamente: `{amp_ratio_req:.12f}`",
        f"- desbalanceamento de amplitude: `{amp_db:.12f} dB`",
        f"- erro diferencial de acoplador: `delta_theta = {delta_theta_req:.12e} rad`",
        f"- split de potência correspondente: `{coupler_split:.12f}`",
        "",
        "## Impedância efetiva equivalente",
        "",
        f"- `Gamma_target = {gamma_target:.12f}`",
        f"- `R_target = {r_target:.12f}` para `||DeltaPhi||^2=2`",
        "",
        "## Interpretação",
        "",
        "Com Vpi ideal e acopladores de 3 dB ideais, o crosstalk estacionário é zero.",
        "O valor finito de -30 dB exige imperfeição material: fase, amplitude, acoplador ou mistura delas.",
        "Logo, o crosstalk pertence a delta K_app material/fabricação/perdas, não à ação fundamental.",
        "",
    ]

    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
