#!/usr/bin/env python3
"""
GDQ — Chapter 12 / Reduced material Hessian of EO-MZI.

Objective:
    Build the reduced model T_MZI=C(theta2)P(phi,eta)C(theta1) and calculate
    which isolated material imperfections produce -30 dB crosstalk.

Classification:
    Reduced material engineering model. The result localizes the crosstalk
    in delta K_app material/fabrication/losses, not in the fundamental action.
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
    out = root / "output_material_hessian_eo_mzi.md"

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
        'title: "Output — EO-MZI material Hessian"',
        "---",
        "",
        "# Output — Reduced EO-MZI material Hessian",
        "",
        "Classification: reduced material engineering model.",
        "",
        "## Frozen data",
        "",
        f"- lambda = `{wavelength:.6e} m`",
        f"- Vpi = `{vpi:.6f} V`",
        f"- tau_sw = `{tau_sw:.6e} s`",
        f"- reference target for comparison: `{target_xt_db:.1f} dB`",
        "",
        "## Ideal transfer",
        "",
        f"- phase at Vpi: `{math.pi:.12f} rad`",
        f"- ideal dark port power: `{p_dark_ideal:.12e}`",
        f"- ideal bright port power: `{p_bright_ideal:.12e}`",
        f"- ideal crosstalk: `{xt_ideal:.12e}`",
        "",
        "## Material imperfections equivalent to -30 dB",
        "",
        f"- required phase error: `delta_phi = {delta_phi_req:.12e} rad`",
        f"- equivalent voltage error: `delta_V = {voltage_error_req:.12e} V`",
        f"- relative voltage error: `{voltage_error_req / vpi:.12e}`",
        f"- amplitude ratio required in isolation: `{amp_ratio_req:.12f}`",
        f"- amplitude imbalance: `{amp_db:.12f} dB`",
        f"- coupler differential error: `delta_theta = {delta_theta_req:.12e} rad`",
        f"- corresponding power split: `{coupler_split:.12f}`",
        "",
        "## Equivalent effective impedance",
        "",
        f"- `Gamma_target = {gamma_target:.12f}`",
        f"- `R_target = {r_target:.12f}` for `||DeltaPhi||^2=2`",
        "",
        "## Interpretation",
        "",
        "With ideal Vpi and ideal 3 dB couplers, the stationary crosstalk is zero.",
        "The finite value of -30 dB requires material imperfection: phase, amplitude, coupler or a mixture of them.",
        "Therefore, the crosstalk belongs to delta K_app material/fabrication/losses, not to the fundamental action.",
        "",
    ]

    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
