#!/usr/bin/env python3
"""Calibração interna de Lambda_0 pelos canais W/Z previstos na Q29."""

from math import pi, sqrt

ALPHA_INV = 137.03599907
PROTON_MASS = 0.93827208816
LAMBDA_W = 2.3193661275e-7
LAMBDA_Z = 3.7109379957e-7
S_STAR = 5909038.565295727

if __name__ == "__main__":
    v = PROTON_MASS*6*pi**5/7
    e = sqrt(4*pi/ALPHA_INV)
    s2 = 3/8
    g, gp = e/sqrt(s2), e/sqrt(1-s2)
    mw = g*v/2
    mz = v*sqrt(g*g+gp*gp)/2
    scale_w = mw/sqrt(LAMBDA_W)
    scale_z = mz/sqrt(LAMBDA_Z)
    scale = (scale_w+scale_z)/2
    mismatch = abs(scale_w-scale_z)/scale
    qstar = scale/sqrt(S_STAR)
    print("Q29 — CALIBRAÇÃO INTERNA DA ESCALA ESPECTRAL")
    print(f"mW_match, mZ_match     = {mw:.12f}, {mz:.12f} GeV")
    print(f"Lambda0(W)             = {scale_w:.12f} GeV")
    print(f"Lambda0(Z)             = {scale_z:.12f} GeV")
    print(f"média Lambda0          = {scale:.12f} GeV")
    print(f"desacordo relativo     = {mismatch:.12e}")
    print(f"Q(s_star)              = {qstar:.12f} GeV")
    assert mismatch < 1e-5
