#!/usr/bin/env python3
import numpy as np
from ponte_global_local_hopf_beltrami import *


def main():
    q=.37;z=np.array([.7+.2j,-.3+.8j]);eps=np.array([.04,-.04])
    assert abs(hopf_t(q*z,q)-hopf_t(z,q)-1)<1e-14
    a,b=deck_tensor_pullback(z,q,eps)
    assert np.linalg.norm(a-b)<1e-14 # q real positivo
    tr,tf=trace_split(eps);assert np.linalg.norm(tr)<1e-15 and abs(np.sum(tf))<1e-15
    assert averaged_l2_norm_sq(q,eps)>0
    # A expressão linear é o limite da família finita integrável.
    mu=beltrami_components(z,q,eps);assert np.linalg.matrix_rank(mu,tol=1e-12)==1
    tiny=1e-7
    mex=beltrami_exact(z,q,tiny*eps)
    assert np.linalg.norm(mex/tiny-mu)<1e-8
    print('HOPF BELTRAMI: testes aprovados')
    print('norma L2² =',averaged_l2_norm_sq(q,eps))
    print('modo anisotrópico é global, não-gauge, mas não-singlet linear')


if __name__=='__main__':main()
