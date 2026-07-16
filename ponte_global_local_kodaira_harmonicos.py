#!/usr/bin/env python3
"""Regras de seleção SU(2)_L x U(1)_R para modos no Berger S3."""
from __future__ import annotations
import numpy as np


def su2_generators(j: float):
    """Geradores Hermitianos Jx,Jy,Jz na representação de spin j."""
    n=int(round(2*j+1)); m=np.arange(j,-j-1,-1)
    Jz=np.diag(m); Jp=np.zeros((n,n),complex)
    for col,mc in enumerate(m):
        mt=mc+1
        if mt<=j:
            row=int(round(j-mt)); Jp[row,col]=np.sqrt((j-mc)*(j+mc+1))
    Jm=Jp.conj().T
    return (Jp+Jm)/2,(Jp-Jm)/(2j),Jz


def invariant_linear_dimension(j: float, tol=1e-12):
    T=np.vstack(su2_generators(j))
    return (2*int(round(2*j+1))-np.linalg.matrix_rank(np.block([[T.real,-T.imag],[T.imag,T.real]]),tol))//2


def doublet_invariants(b):
    b=np.asarray(b,dtype=complex).reshape(2)
    sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]],complex);sz=np.diag([1,-1])
    return float(np.vdot(b,b).real),np.array([np.vdot(b,s@b).real for s in (sx,sy,sz)])

