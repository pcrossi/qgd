#!/usr/bin/env python3
"""Extensão mínima cohomogeneidade-1 de J no bloco (5,6,7,8).

Avalia somente a correção torsional que segue de H=d_J^c omega. Não contém
Robin, fonte ou termo novo. Derivadas são próprias (ponto = N^{-1}d/ds).
"""
from __future__ import annotations
import numpy as np


def torsion_coefficients(a, c, ad, cd, chi, chid):
    """Coeficientes A,B de d omega=A e567+B e578; |H|^2=6(A^2+B^2)."""
    k0 = 2.0 * (ad / a - c / a**2)
    k1 = 2.0 / c + ad / a + cd / c
    co, si = np.cos(chi), np.sin(chi)
    A = co * k0 - si * chid
    B = -si * k1 - co * chid
    return A, B, k0, k1


def delta_K(a, c, ad, cd, chi, chid):
    """Correção à K reduzida relativamente ao setor J fixo chi=0."""
    A, B, k0, _ = torsion_coefficients(a, c, ad, cd, chi, chid)
    return -0.5 * (A*A + B*B - k0*k0)


def momentum_corrections(tau, volume, a, c, ad, cd, chi, chid):
    """(Delta p_a, Delta p_c, p_chi) em coordenadas (a,c,chi)."""
    A, B, k0, k1 = torsion_coefficients(a, c, ad, cd, chi, chid)
    co, si = np.cos(chi), np.sin(chi)
    # k0_ad=2/a; k1_ad=1/a; k1_cd=1/c.
    # O termo +k0^2/2 em DeltaK também depende de ad.
    dpa = tau*volume*(-2*A*co + B*si + 2*k0)/a
    dpc = tau*volume*B*si/c
    pchi = tau*volume*(si*co*(k0-k1)-chid)
    return np.array([dpa, dpc, pchi])


def lapse_correction(tau, a, c, ad, cd, chi, chid):
    """Delta C_N=tau(DeltaK-sum qdot dDeltaK/dqdot), expressão exata."""
    dk = delta_K(a, c, ad, cd, chi, chid)
    # derivadas de DeltaK reconstruídas dos momentos sem tau*volume.
    dp = momentum_corrections(1.0, 1.0, a, c, ad, cd, chi, chid)
    return tau*(dk - ad*dp[0] - cd*dp[1] - chid*dp[2])


def invert_chid(tau, volume, a, c, ad, cd, chi, pchi):
    """Inversão exata do novo momento."""
    _, _, k0, k1 = torsion_coefficients(a, c, ad, cd, chi, 0.0)
    return np.sin(chi)*np.cos(chi)*(k0-k1)-pchi/(tau*volume)
