#!/usr/bin/env python3
"""Representante de Kodaira--Spencer da deformação diagonal da Hopf primária."""
from __future__ import annotations
import numpy as np


def hopf_t(z,q):
    z=np.asarray(z,dtype=complex); return np.log(np.vdot(z,z).real)/(2*np.log(abs(q)))


def beltrami_components(z,q,eps):
    """mu_{bar j}^i=(eps_i z_i)*(z_j/(2 log|q| |z|²))."""
    z=np.asarray(z,dtype=complex);eps=np.asarray(eps,dtype=complex)
    r2=np.vdot(z,z).real
    return np.outer(eps*z,z)/(2*np.log(abs(q))*r2)


def beltrami_exact(z,q,eps):
    """Coeficiente finito A^{-1}B da conjugação F_i=exp(eps_i*t)z_i."""
    z=np.asarray(z,dtype=complex);eps=np.asarray(eps,dtype=complex)
    r2=np.vdot(z,z).real; L=np.log(abs(q)); t=hopf_t(z,q)
    tz=np.conj(z)/(2*L*r2); tb=z/(2*L*r2)
    fac=np.exp(eps*t)
    A=np.diag(fac)@(np.eye(2)+np.outer(eps*z,tz))
    B=np.diag(fac)@np.outer(eps*z,tb)
    return np.linalg.solve(A,B)


def deck_tensor_pullback(z,q,eps):
    """Compara componentes em z e qz após fatores tensorais do deck."""
    m0=beltrami_components(z,q,eps);m1=beltrami_components(q*np.asarray(z),q,eps)
    # dbar(qz)=bar(q)dbarz e d/d(qz)=q^{-1}d/dz.
    return m0,(np.conj(q)/q)*m1


def averaged_l2_norm_sq(q,eps):
    """Integral no métrico cilíndrico r^-2 dz dbarz; convenção Vol(S3)=2pi²."""
    L=abs(np.log(abs(q))); return np.pi**2*np.vdot(eps,eps).real/(4*L)


def trace_split(eps):
    eps=np.asarray(eps,dtype=complex);mean=np.mean(eps)
    return np.full_like(eps,mean),eps-mean
