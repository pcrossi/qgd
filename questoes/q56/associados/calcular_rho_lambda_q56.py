#!/usr/bin/env python3
"""Q56 — cálculo auditável da densidade de energia escura GDQ.

Classificação:
    avaliação direta de fórmula estrutural reduzida, condicionada ao contorno
    cosmológico global.

A fórmula avaliada é

    rho_Lambda = alpha^2 * N_Cartan * rho_UV * (r_p/R_H) / c^2

com

    rho_UV = M_p c^2 / ((4/3) pi r_p^3).

O valor não é tratado como predição cega absoluta porque usa o dado de
fronteira cosmológica H0 para definir R_H = c/H0.
"""

from __future__ import annotations

import math


def main() -> None:
    c = 299_792_458.0
    alpha_inv = 137.035_999_084
    alpha = 1.0 / alpha_inv
    m_p = 1.672_621_925_95e-27
    r_p = 0.840_778_765_450e-15
    mpc = 3.085_677_581_491_367_3e22
    G = 6.674_30e-11

    # Contorno cosmológico de referência usado para auditoria.
    H0_km_s_mpc = 67.4
    Omega_Lambda = 0.6847

    H0 = H0_km_s_mpc * 1000.0 / mpc
    R_H = c / H0

    n_cartan = 8 * 7 // 2
    volume_p = (4.0 / 3.0) * math.pi * r_p**3
    rho_uv_J = m_p * c**2 / volume_p
    dilution = r_p / R_H
    rho_eff_J = rho_uv_J * dilution * n_cartan
    rho_lambda_J = alpha**2 * rho_eff_J
    rho_lambda_kg = rho_lambda_J / c**2

    rho_crit = 3.0 * H0**2 / (8.0 * math.pi * G)
    rho_obs = Omega_Lambda * rho_crit
    omega_pred = rho_lambda_kg / rho_crit
    rel_err = (rho_lambda_kg - rho_obs) / rho_obs

    print("Q56 — densidade de energia escura GDQ")
    print()
    print("[Entradas]")
    print(f"alpha^-1        = {alpha_inv:.12f}")
    print(f"r_p             = {r_p:.12e} m")
    print(f"M_p             = {m_p:.12e} kg")
    print(f"H0              = {H0_km_s_mpc:.6f} km/s/Mpc")
    print(f"Omega_Lambda    = {Omega_Lambda:.8f}")
    print(f"R_H=c/H0        = {R_H:.12e} m")
    print()
    print("[Cadeia GDQ reduzida]")
    print(f"N_Cartan        = {n_cartan}")
    print(f"rho_UV          = {rho_uv_J:.12e} J/m^3")
    print(f"r_p/R_H         = {dilution:.12e}")
    print(f"rho_eff         = {rho_eff_J:.12e} J/m^3")
    print(f"alpha^2*rho_eff = {rho_lambda_J:.12e} J/m^3")
    print(f"rho_Lambda_GDQ  = {rho_lambda_kg:.12e} kg/m^3")
    print()
    print("[Comparação de contorno]")
    print(f"rho_crit        = {rho_crit:.12e} kg/m^3")
    print(f"rho_obs         = {rho_obs:.12e} kg/m^3")
    print(f"Omega_pred      = {omega_pred:.12f}")
    print(f"erro_relativo   = {rel_err:.12e}")
    print()
    print("[Status]")
    print("Avaliação direta da fórmula estrutural reduzida.")
    print("Não é previsão absoluta independente: R_H é dado de contorno cosmológico.")


if __name__ == "__main__":
    main()
