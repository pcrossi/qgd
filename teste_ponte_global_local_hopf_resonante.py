#!/usr/bin/env python3
import numpy as np
from ponte_global_local_hopf_resonante import *


def main():
    beta=.4; m=2; alpha=beta**m;lam=.07
    try: removable_coefficient(alpha,beta,m,lam)
    except ValueError: pass
    else: raise AssertionError('monômio resonante removido')
    z=np.array([.3+.2j,.6-.1j]);t=.37
    # h(Az,t+1)=F_lambda(h(z,t)) sob alpha=beta^m.
    left=smooth_conjugacy(deck(z,alpha,beta,m,0),t+1,alpha,m,lam)
    right=deck(smooth_conjugacy(z,t,alpha,m,lam),alpha,beta,m,lam)
    assert np.linalg.norm(left-right)<1e-14
    assert jacobian_determinant(alpha,beta,m,lam,z)==alpha*beta
    mu=beltrami_linear(z,[.2+.1j,-.3j],alpha,m,lam)
    assert np.linalg.matrix_rank(mu)==1
    print('HOPF RESONANTE: identidades aprovadas')
    print('termo holomorficamente não removível; conjugação suave existe')
    print('determinante do deck independe de lambda')


if __name__=='__main__':main()
