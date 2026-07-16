#!/usr/bin/env python3
"""Ramo integrável discreto J_{pi/2}: fórmulas reduzidas e teste DAE.

O multiplicador ell impõe integrabilidade; não é termo físico novo. Este
módulo fornece a parte interna (a,c,u,v), que se acopla ao ansatz causal pela
medida V=A0*As^3*a^2*c*exp(-u).
"""
from __future__ import annotations
import numpy as np


def integrability(a,c,ad,cd):
    return ad/a-cd/c-2/c+2*c/a**2


def k_values(a,c,ad,cd):
    return 2*(ad/a-c/a**2), 2/c+ad/a+cd/c


def delta_K(a,c,ad,cd):
    k0,k1=k_values(a,c,ad,cd)
    return -.5*(k1*k1-k0*k0)


def restricted_cd(a,c,ad):
    return c*ad/a-2+2*c*c/a**2


def restricted_delta_K(a,c,ad):
    cd=restricted_cd(a,c,ad)
    return delta_K(a,c,ad,cd)


def momentum_shifts(tau,V,a,c,ad,cd,ell=0.):
    k0,k1=k_values(a,c,ad,cd)
    # ação oficial torsional + multiplicador cinemático ell*F
    dpa=tau*V*(-k1+2*k0)/a+ell/a
    dpc=-tau*V*k1/c-ell/c
    return np.array([dpa,dpc])


def lapse_shift(tau,V,a,c,ad,cd,ell=0.):
    """Mudança na equação dL/dN=0 relativamente ao ramo original."""
    dk=delta_K(a,c,ad,cd)
    # derivadas analíticas da correção em adot,cdot.
    k0,k1=k_values(a,c,ad,cd)
    d_ad=(-k1+2*k0)/a
    d_cd=-k1/c
    Fpot=-2/c+2*c/a**2
    return tau*V*(dk-ad*d_ad-cd*d_cd)+ell*Fpot

