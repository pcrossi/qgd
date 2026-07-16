#!/usr/bin/env python3
"""Identidades algébricas da contração Hopf resonante."""
from __future__ import annotations
import numpy as np


def removable_coefficient(alpha,beta,m,lam):
    """c da mudança holomorfa z1->z1+c z2^m fora da ressonância."""
    den=beta**m-alpha
    if abs(den)<1e-14: raise ValueError('termo resonante não removível')
    return lam/den


def deck(z,alpha,beta,m,lam):
    z=np.asarray(z,dtype=complex)
    return np.array([alpha*z[0]+lam*z[1]**m,beta*z[1]])


def jacobian_determinant(alpha,beta,m,lam,z):
    # Matriz triangular; independente de lambda e z.
    return alpha*beta


def smooth_conjugacy(z,t,alpha,m,lam):
    z=np.asarray(z,dtype=complex)
    return np.array([z[0]+(lam/alpha)*t*z[1]**m,z[1]])


def beltrami_linear(z,dbar_t,alpha,m,lam):
    """mu^1_barj=(lam/alpha)z2^m (dbar t)_j; segunda linha zero."""
    z=np.asarray(z,dtype=complex);dbar_t=np.asarray(dbar_t,dtype=complex)
    out=np.zeros((2,2),complex);out[0]=(lam/alpha)*z[1]**m*dbar_t
    return out

