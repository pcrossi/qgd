#!/usr/bin/env python3
"""Compara traço bruto e normalização por fluxo EM no cruzamento da Q29."""

from math import pi, sqrt

ALPHA0_INV = 137.03599907
SURFACE = (1/ALPHA0_INV)*(3*pi/2+3/(4*pi**3))
ALPHA_EM_INV = ALPHA0_INV/(1+SURFACE)
V = 0.93827208816*6*pi**5/7
KW0, KY0 = 2.55826980, 4.26378342
KWSTAR, KYSTAR = 0.6350923909825891, 2.222823368439062


def observables(e, sin2):
    g, gp = e/sqrt(sin2), e/sqrt(1-sin2)
    return g, gp, g*V/2, V*sqrt(g*g+gp*gp)/2


if __name__ == "__main__":
    e0 = sqrt(4*pi/ALPHA0_INV)
    g0 = e0/sqrt(3/8)
    common = (1/g0**2)/KW0
    g_raw, gp_raw = 1/sqrt(common*KWSTAR), 1/sqrt(common*KYSTAR)
    sin2_raw = gp_raw**2/(g_raw**2+gp_raw**2)
    e_raw = g_raw*sqrt(sin2_raw)

    e_flux = sqrt(4*pi/ALPHA_EM_INV)
    g_flux, gp_flux, mw_flux, mz_flux = observables(e_flux, 2/9)

    print("Q29 — NORMALIZAÇÃO ABSOLUTA NO CRUZAMENTO")
    print("traço bruto:")
    print(f"  sin²={sin2_raw:.12f} alpha^-1={4*pi/e_raw**2:.12f}")
    print(f"  g={g_raw:.12f} g'={gp_raw:.12f}")
    print("fluxo EM conservado + Schur de interface:")
    print(f"  alpha_EM^-1={ALPHA_EM_INV:.12f}")
    print(f"  g={g_flux:.12f} g'={gp_flux:.12f}")
    print(f"  mW={mw_flux:.12f} mZ={mz_flux:.12f} GeV")
    assert abs(sin2_raw-2/9) < 1e-12
