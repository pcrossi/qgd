#!/usr/bin/env python3
"""Coeficiente geométrico F_Q² da fibra de Hopf na ação de curvatura."""

from math import pi

R = 1.998411184770
KAPPA_Q = 1.0
VOLUME_S3 = 2*pi**2*R**3
# |coeficiente integrado de F²| antes de C_GDQ*tau.
COEFF_ACTION = VOLUME_S3*R**2*KAPPA_Q**2/4
# Convenção S_eff=(K_Q/4) int F².
K_Q_OVER_CTAU = 4*COEFF_ACTION

if __name__ == "__main__":
    print("Q29 — REDUÇÃO ELETROMAGNÉTICA DA FIBRA DE HOPF")
    print(f"R                    = {R:.12f}")
    print(f"Vol(S3)              = {VOLUME_S3:.12f}")
    print(f"|coef ação F²|/Ctau  = {COEFF_ACTION:.12f}")
    print(f"|K_Q|/Ctau           = {K_Q_OVER_CTAU:.12f}")
    print(f"CS três estômatos    = {3*pi/2:.12f}")
    assert COEFF_ACTION > 0
