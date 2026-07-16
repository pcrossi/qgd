#!/usr/bin/env python3
"""Teste de conservação da restrição do exterior causal.

Classificação: teste de consistência numérica, sem ajuste fenomenológico.
"""
import numpy as np
from scipy.integrate import solve_ivp
from ponte_global_local_exterior_causal_equacoes import rhs,constraint

def main():
    tau=.08
    # Estado regular arbitrário. lambda é determinado pela própria restrição
    # inicial, e não por um alvo físico.
    Y=np.array([0.,0.,0.,0.,4.,0.,0.,1e-6,-1e-6,1e-6,-1e-6,1e-6,0.])
    Y[6]=constraint(Y,tau)+Y[6]
    sol=solve_ivp(lambda s,q:rhs(s,q,tau),(0,.01),Y,method='DOP853',
                  rtol=2e-11,atol=2e-13,max_step=.0001)
    errors=np.array([constraint(q,tau) for q in sol.y.T])
    print('success =',sol.success)
    print('max_abs_constraint =',np.max(np.abs(errors)))
    print('final_constraint =',errors[-1])
    print('passed =',sol.success and np.max(np.abs(errors))<1e-8)

if __name__=='__main__':
    main()
