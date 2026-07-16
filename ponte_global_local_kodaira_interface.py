#!/usr/bin/env python3
"""Montagem discreta da interface Kodaira--Spencer derivada variacionalmente.

As matrizes devem vir da segunda variação oficial. O módulo não inventa
coeficientes Robin e não transforma resíduos de least-squares em Hessiana.
"""
from __future__ import annotations
import numpy as np


def augmented_boundary_blocks(Kbulk, lambdas, Kconstraints):
    """Bloco Hessiano aumentado K_S-sum lambda K_C."""
    if len(lambdas)!=len(Kconstraints):
        raise ValueError('multiplicadores e Hessianas de vínculos incompatíveis')
    K=np.array(Kbulk,dtype=np.result_type(Kbulk,np.asarray(lambdas)),copy=True)
    for lam,Kc in zip(lambdas,Kconstraints): K-=lam*Kc
    return (K+K.conj().T)/2


def glue_momentum(pi_minus,pi_plus,interface_source=None):
    """Resíduo orientado. Sem fonte externa: pi_-+pi_+=0."""
    if interface_source is not None and np.linalg.norm(interface_source)>0:
        raise ValueError('esta rota não admite fonte de interface externa')
    return np.asarray(pi_minus)+np.asarray(pi_plus)


def schur_impedance(Kii,Kiy,Kyi,Kyy):
    """DtN/impedância após eliminar graus interiores i."""
    return Kyy-Kyi@np.linalg.solve(Kii,Kiy)


def residual_coupling(K_trace, residual_indices, beltrami_indices):
    """Bloco B_mu=D_mu(r_a,r_c,r_u) da Hessiana de interface."""
    return np.asarray(K_trace)[np.ix_(residual_indices,beltrami_indices)]
