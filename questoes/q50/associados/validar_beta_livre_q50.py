#!/usr/bin/env python3
"""Validação autocontida da Q50: decaimento beta livre na redução GDQ.

O script não usa a energia do antineutrino como valor fixo. Ele calcula a
integral de espaço de fase contínuo no limite de recoil desprezível e avalia
a vida média pela lei GDQ alpha^-11, equivalente ao fechamento contraído dos
terceiros jatos.
"""

from __future__ import annotations

import math


HBAR_GEV_S = 6.582119569e-25
HBAR_MEV_S = 6.582119569e-22
M_E_MEV = 0.51099895069
DELTA_M_MEV = 1.29333251
M_E_GEV = M_E_MEV * 1.0e-3
DELTA_M_GEV = DELTA_M_MEV * 1.0e-3
ALPHA_INV = 137.035999177


def simpson(func, a: float, b: float, n: int) -> float:
    if n % 2:
        raise ValueError("n deve ser par")
    h = (b - a) / n
    total = func(a) + func(b)
    odd = 0.0
    even = 0.0
    for k in range(1, n):
        value = func(a + k * h)
        if k % 2:
            odd += value
        else:
            even += value
    return h * (total + 4.0 * odd + 2.0 * even) / 3.0


def phase_integrand(e_gev: float) -> float:
    p = math.sqrt(max(e_gev * e_gev - M_E_GEV * M_E_GEV, 0.0))
    return p * e_gev * (DELTA_M_GEV - e_gev) ** 2


def phase_space_analytic() -> float:
    endpoint = DELTA_M_GEV
    mass = M_E_GEV
    p0 = math.sqrt(endpoint * endpoint - mass * mass)
    logterm = math.log((endpoint + p0) / mass)
    int_ep = p0**3 / 3.0
    int_e2p = (
        endpoint * p0 * (2.0 * endpoint**2 - mass**2)
        - mass**4 * logterm
    ) / 8.0
    int_e3p = p0**5 / 5.0 + mass**2 * p0**3 / 3.0
    return endpoint**2 * int_ep - 2.0 * endpoint * int_e2p + int_e3p


def historical_gdq_rate() -> tuple[float, float, float]:
    tau_e = HBAR_MEV_S / M_E_MEV
    tau = (32.0 / 15.0) * ALPHA_INV**11 * tau_e
    gamma = 1.0 / tau
    half_life = math.log(2.0) * tau
    return gamma, tau, half_life


def spectrum_shape(e_mev: float) -> float:
    e = e_mev * 1.0e-3
    return phase_integrand(e)


def main() -> None:
    q_beta_mev = DELTA_M_MEV - M_E_MEV
    i_analytic = phase_space_analytic()
    refinements = [
        simpson(phase_integrand, M_E_GEV, DELTA_M_GEV, n)
        for n in (20_000, 40_000, 80_000)
    ]
    spread = max(refinements) - min(refinements)
    rel_error = abs(refinements[-1] / i_analytic - 1.0)
    gamma, tau, half_life = historical_gdq_rate()
    j3_sq = (
        gamma
        * HBAR_GEV_S
        * 2.0
        * math.pi**3
        / i_analytic
    )
    j3 = math.sqrt(j3_sq)

    grid = [
        M_E_MEV,
        M_E_MEV + 0.25 * q_beta_mev,
        M_E_MEV + 0.50 * q_beta_mev,
        M_E_MEV + 0.75 * q_beta_mev,
        DELTA_M_MEV,
    ]
    shapes = [spectrum_shape(e) for e in grid]
    max_shape = max(shapes) if max(shapes) else 1.0

    print("# Saída — validação Q50 beta livre GDQ")
    print()
    print(f"m_e = {M_E_MEV:.11f} MeV")
    print(f"DeltaM = {DELTA_M_MEV:.8f} MeV")
    print(f"Q_beta endpoint = {q_beta_mev:.12f} MeV")
    print("Observação: Q_beta é energia disponível máxima, não energia fixa do antineutrino.")
    print()
    print(f"I_beta analítico = {i_analytic:.15e} GeV^5")
    print("I_beta Simpson =", ", ".join(f"{value:.15e}" for value in refinements), "GeV^5")
    print(f"espalhamento de malha = {spread:.3e} GeV^5")
    print(f"erro relativo Simpson fino = {rel_error:.3e}")
    print()
    print(f"alpha^-1 = {ALPHA_INV:.12f}")
    print(f"2|C_S|^2+6|C_T|^2 = {j3_sq:.15e} GeV^-4")
    print(f"sqrt(2|C_S|^2+6|C_T|^2) = {j3:.15e} GeV^-2")
    print(f"Gamma = {gamma:.15e} s^-1")
    print(f"vida média tau_n = {tau:.12f} s")
    print(f"meia-vida T_1/2 = {half_life:.12f} s")
    print()
    print("| E_e (MeV) | E_nu recoil-zero (MeV) | forma espectral normalizada |")
    print("|---:|---:|---:|")
    for e, shape in zip(grid, shapes):
        print(f"| {e:.12f} | {DELTA_M_MEV - e:.12f} | {shape / max_shape:.12f} |")


if __name__ == "__main__":
    main()
