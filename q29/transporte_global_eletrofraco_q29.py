#!/usr/bin/env python3
"""Transporte eletrofraco candidato da Q29 sem ajustar mW ou mZ."""

from math import pi, sqrt

ALPHA_INV = 137.03599907
V_GDQ_GEV = 246.111195995615
SIN2_OPERATIONAL = 2.0 / 9.0


def prediction():
    alpha = 1.0 / ALPHA_INV
    surface = alpha * (3.0 * pi / 2.0 + 3.0 / (4.0 * pi**3))
    # Identidade candidata de Schur; ainda requer derivação pela Hessiana global.
    alpha_ew = alpha * (1.0 + surface)
    e = sqrt(4.0 * pi * alpha_ew)
    g = e / sqrt(SIN2_OPERATIONAL)
    gp = e / sqrt(1.0 - SIN2_OPERATIONAL)
    mw = 0.5 * g * V_GDQ_GEV
    mz = 0.5 * V_GDQ_GEV * sqrt(g * g + gp * gp)
    return surface, 1.0 / alpha_ew, e, g, gp, mw, mz


if __name__ == "__main__":
    surface, alpha_ew_inv, e, g, gp, mw, mz = prediction()
    print("Q29 — TRANSPORTE GLOBAL ELETROFRACO (CANDIDATO SEM AJUSTE W/Z)")
    print(f"S_boundary       = {surface:.12f}")
    print(f"alpha_EW^-1      = {alpha_ew_inv:.12f}")
    print(f"sin^2(theta_W)   = {SIN2_OPERATIONAL:.12f}")
    print(f"e, g, g'         = {e:.12f}, {g:.12f}, {gp:.12f}")
    print(f"mW, mZ [GeV]     = {mw:.12f}, {mz:.12f}")
    print(f"mW/mZ            = {mw/mz:.12f}")
