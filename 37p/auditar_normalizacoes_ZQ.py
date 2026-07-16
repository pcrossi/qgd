#!/usr/bin/env python3
"""Audita as normalizações escalares e matriciais do setor elétrico da Q37."""

from math import pi, sqrt


K_BASE = 41.594825709
DELTA_B = -0.2709378871


def main() -> None:
    alpha_cos = 9.0 / (8.0 * pi**4) * (pi**5 / 1920.0) ** 0.25
    z_cos = 1.0 / (4.0 * pi * alpha_cos)

    z_single = K_BASE / 4.0
    z_photon_round = K_BASE / 2.0
    z_photon_radial = K_BASE / 2.0 * (1.0 + DELTA_B)

    print("Q37 — AUDITORIA DE NORMALIZAÇÕES DE Z_Q")
    print(f"K_base radial não canonizado = {K_BASE:.12f}")
    print(f"Z de um gerador T3 ou Y      = {z_single:.12f}")
    print(f"Z fóton redondo (1,1)        = {z_photon_round:.12f}")
    print(f"Z fóton radial on-shell      = {z_photon_radial:.12f}")
    print(f"Z exigido pela fórmula cos.  = {z_cos:.12f}")
    print()
    print(f"alpha_cos^(-1)               = {1.0/alpha_cos:.12f}")
    print(f"alpha_single^(-1)            = {4.0*pi*z_single:.12f}")
    print(f"alpha_photon_round^(-1)      = {4.0*pi*z_photon_round:.12f}")
    print(f"alpha_photon_radial^(-1)     = {4.0*pi*z_photon_radial:.12f}")
    print()
    print(f"Z_cos/Z_single               = {z_cos/z_single:.12f}")
    print(f"carga requerida se K_base    = {sqrt(4*pi*alpha_cos*K_BASE):.12f}")
    print(f"carga requerida se Z_single  = {sqrt(4*pi*alpha_cos*z_single):.12f}")

    assert abs(z_single - K_BASE / 4.0) < 1e-14
    assert abs(z_photon_radial - 15.1626057595) < 1e-9


if __name__ == "__main__":
    main()
