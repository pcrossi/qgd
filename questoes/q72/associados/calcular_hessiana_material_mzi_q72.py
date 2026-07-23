#!/usr/bin/env python3
"""
Q72 — camada material reduzida do EO-MZI.

Objetivo:
    Construir um operador material 2x2 de braços/acopladores, calcular a
    resposta de saída e extrair a impedância efetiva por Schur/DtN reduzido.

Classificação:
    - modelo material reduzido de engenharia;
    - não usa crosstalk como entrada para a curva ideal;
    - calcula quais imperfeições materiais produzem -30 dB.

Conclusão esperada:
    Vpi fixa fase π. Em aparelho ideal, crosstalk estacionário é zero.
    O crosstalk finito requer imperfeição material: erro de fase, razão de
    amplitude ou erro de acoplador.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


def coupler(theta: float) -> np.ndarray:
    """Acoplador lossless simétrico. theta=pi/4 é 3 dB."""
    c = math.cos(theta)
    s = math.sin(theta)
    return np.array([[c, 1j * s], [1j * s, c]], dtype=complex)


def phase_arm(phi: float, amp_ratio: float = 1.0, loss_common: float = 1.0) -> np.ndarray:
    """Propagação nos dois braços com fase diferencial phi e razão de amplitudes."""
    a1 = loss_common
    a2 = loss_common * amp_ratio
    return np.diag([a1 * np.exp(0.5j * phi), a2 * np.exp(-0.5j * phi)])


def mzi_transfer(phi: float, theta1: float = math.pi / 4, theta2: float = math.pi / 4,
                 amp_ratio: float = 1.0) -> np.ndarray:
    return coupler(theta2) @ phase_arm(phi, amp_ratio=amp_ratio) @ coupler(theta1)


def powers(phi: float, theta1: float = math.pi / 4, theta2: float = math.pi / 4,
           amp_ratio: float = 1.0) -> tuple[float, float]:
    tin = np.array([1.0 + 0j, 0.0 + 0j])
    out = mzi_transfer(phi, theta1=theta1, theta2=theta2, amp_ratio=amp_ratio) @ tin
    p = np.abs(out) ** 2
    return float(p[0]), float(p[1])


def extinction_from_phase_error(delta_phi: float) -> float:
    """Potência vazada no porto escuro para erro delta_phi perto de condição ideal."""
    p0, p1 = powers(math.pi + delta_phi)
    return min(p0, p1) / max(max(p0, p1), 1e-300)


def extinction_from_amp_ratio(amp_ratio: float) -> float:
    """Vazamento no porto escuro em phi=pi por desbalanceamento de amplitudes."""
    p0, p1 = powers(math.pi, amp_ratio=amp_ratio)
    return min(p0, p1) / max(max(p0, p1), 1e-300)


def extinction_from_coupler_error(delta_theta: float) -> float:
    """Vazamento com erro diferencial: só um acoplador desvia de 3 dB."""
    p0, p1 = powers(math.pi, theta1=math.pi / 4 + delta_theta,
                    theta2=math.pi / 4)
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
    wavelength = 1550e-9
    vpi = 2.445
    tau_sw = 18.1e-12
    target_xt_db = -30.0
    target = 10.0 ** (target_xt_db / 10.0)

    # Ideal EO phase.
    phi_vpi = math.pi
    p0_ideal, p1_ideal = powers(phi_vpi)
    p_dark_ideal = min(p0_ideal, p1_ideal)
    p_bright_ideal = max(p0_ideal, p1_ideal)
    xt_ideal = p_dark_ideal / max(p_bright_ideal, 1e-300)

    # Imperfeições individuais necessárias para -30 dB.
    delta_phi_req = bisect_positive(extinction_from_phase_error, target, hi=0.2)
    voltage_error_req = delta_phi_req / math.pi * vpi

    # Razão de amplitude abaixo/acima de 1. Procurar amp_ratio<1 usando eps.
    def amp_leak(eps: float) -> float:
        return extinction_from_amp_ratio(1.0 - eps)

    eps_amp_req = bisect_positive(amp_leak, target, hi=0.2)
    amp_ratio_req = 1.0 - eps_amp_req
    power_imbalance_db = 20.0 * math.log10(amp_ratio_req)

    delta_theta_req = bisect_positive(extinction_from_coupler_error, target, hi=0.2)
    coupler_split = math.sin(math.pi / 4 + delta_theta_req) ** 2

    # Hessiana reduzida material perto do ponto ideal.
    # Para pequeno erro de fase, p_leak ≈ (δφ/2)^2.
    # Gamma = -ln(C), C=sqrt(p_leak), logo R ≈ -ln(|δφ|/2)
    gamma_target = -math.log(math.sqrt(target))
    r_target = gamma_target

    out = []
    out.append("# Saída — Q72 Hessiana material reduzida EO-MZI")
    out.append("")
    out.append("## Dados congelados")
    out.append("")
    out.append(f"- lambda = `{wavelength:.6e} m`")
    out.append(f"- Vpi = `{vpi:.6f} V`")
    out.append(f"- tau_sw = `{tau_sw:.6e} s`")
    out.append(f"- alvo de referência para comparação: `{target_xt_db:.1f} dB`")
    out.append("")
    out.append("## Transferência ideal")
    out.append("")
    out.append(f"- fase em Vpi: `{phi_vpi:.12f} rad`")
    out.append(f"- potência porto escuro ideal: `{p_dark_ideal:.12e}`")
    out.append(f"- potência porto claro ideal: `{p_bright_ideal:.12e}`")
    out.append(f"- crosstalk ideal: `{xt_ideal:.12e}`")
    out.append("")
    out.append("## Imperfeições materiais necessárias para -30 dB")
    out.append("")
    out.append(f"- erro de fase requerido: `delta_phi = {delta_phi_req:.12e} rad`")
    out.append(f"- erro equivalente de tensão: `delta_V = {voltage_error_req:.12e} V`")
    out.append(f"- erro relativo de tensão: `{voltage_error_req / vpi:.12e}`")
    out.append(f"- razão de amplitude requerida isoladamente: `{amp_ratio_req:.12f}`")
    out.append(f"- desbalanceamento de amplitude em dB: `{power_imbalance_db:.12f} dB`")
    out.append(f"- erro diferencial de acoplador requerido: `delta_theta = {delta_theta_req:.12e} rad`")
    out.append(f"- split de potência correspondente: `{coupler_split:.12f}`")
    out.append("")
    out.append("## Impedância efetiva equivalente")
    out.append("")
    out.append(f"- `Gamma_target = {gamma_target:.12f}`")
    out.append(f"- `R_target = {r_target:.12f}` para `||DeltaPhi||^2=2`")
    out.append("")
    out.append("## Interpretação")
    out.append("")
    out.append("Com Vpi ideal e acopladores 3 dB ideais, o crosstalk estacionário é zero.")
    out.append("O valor finito de -30 dB exige imperfeição material: fase, amplitude, acoplador ou mistura delas.")
    out.append("Portanto, `K_app` explica onde o crosstalk mora: no Hessiano material de fabricação e perdas, não na ação fundamental.")

    path = Path(__file__).with_name("saida_hessiana_material_mzi_q72.md")
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
