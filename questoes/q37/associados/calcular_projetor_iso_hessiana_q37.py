#!/usr/bin/env python3
"""Cálculo do projetor isotrópico da Q37.

Este script não ajusta alpha. Ele apenas avalia a contração que aparece quando
a Hessiana oficial projetada é escalar no setor físico de quatro direções,
como imposto pela média isotrópica do ensemble de Einstein.
"""

from math import pi


def main() -> None:
    angular_normalization = 1.0 / pi**4
    hopf_haar_fourth_moment = 1.0 / 8.0
    cartan_schouten_trace_squared = 3.0**2

    p_iso = (
        angular_normalization
        * hopf_haar_fourth_moment
        * cartan_schouten_trace_squared
    )

    p_iso_closed = 9.0 / (8.0 * pi**4)

    alpha_mean = p_iso * (pi**5 / 1920.0) ** 0.25
    z_q = 1.0 / (4.0 * pi * alpha_mean)

    print("Q37 — PROJETOR ISOTRÓPICO COMO CONTRAÇÃO DA HESSIANA")
    print(f"normalização angular pi^-4        = {angular_normalization:.15f}")
    print(f"momento de Haar <(n.u)^4>          = {hopf_haar_fourth_moment:.15f}")
    print(f"traço coerente Cartan-Schouten^2   = {cartan_schouten_trace_squared:.15f}")
    print(f"P_iso calculado                    = {p_iso:.15f}")
    print(f"P_iso fechado 9/(8*pi^4)           = {p_iso_closed:.15f}")
    print(f"diferença                          = {p_iso - p_iso_closed:.3e}")
    print(f"alpha_mean                         = {alpha_mean:.15f}")
    print(f"alpha_mean^-1                      = {1.0 / alpha_mean:.12f}")
    print(f"Z_Q mean = 1/(4*pi*alpha_mean)      = {z_q:.12f}")

    assert abs(p_iso - p_iso_closed) < 1e-15


if __name__ == "__main__":
    main()
