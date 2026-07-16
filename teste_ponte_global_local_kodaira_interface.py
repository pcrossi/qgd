#!/usr/bin/env python3
import numpy as np
from ponte_global_local_kodaira_interface import *


def main():
    rng=np.random.default_rng(42)
    A=rng.normal(size=(7,7));K=A.T@A+np.eye(7)
    C=rng.normal(size=(7,7));C=(C+C.T)/2
    Ka=augmented_boundary_blocks(K,[.2],[C])
    assert np.linalg.norm(Ka-Ka.T)<1e-13
    assert np.linalg.norm(glue_momentum(np.ones(3),-np.ones(3)))==0
    Z=schur_impedance(Ka[:4,:4],Ka[:4,4:],Ka[4:,:4],Ka[4:,4:])
    assert np.linalg.norm(Z-Z.T)<1e-12
    B=residual_coupling(Z,[0,1],[2])
    assert B.shape==(2,1)
    try: glue_momentum(np.zeros(1),np.zeros(1),np.ones(1))
    except ValueError: pass
    else: raise AssertionError('fonte externa aceita indevidamente')
    print('INTERFACE KODAIRA-SPENCER: teste algébrico aprovado')
    print('simetria DtN =',np.linalg.norm(Z-Z.T))


if __name__=='__main__':main()
