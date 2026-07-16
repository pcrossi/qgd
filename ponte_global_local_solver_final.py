#!/usr/bin/env python3
"""Solver final reduzido da ponte global--local causal.

Classificação: teste numérico de existência da sela no ansatz
cohomogeneidade-1. Não é ainda o teste do espectro não homogêneo completo.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
from ponte_global_local_integrador import Parameters, rhs as inner_rhs, constraint as inner_constraint
from ponte_global_local_exterior_causal_equacoes import rhs as causal_rhs, constraint as causal_constraint, velocities as causal_velocities

ALPHA=1/137.035999177
R_COS=np.pi**2*np.sqrt(ALPHA)
LOG_R_COS=np.log(R_COS)
BETA_E=2*np.pi
E_H_HAT=1.0

def throat_u(a,c,tau):
    return 4-8*tau/a**2+4*tau*c**2/a**4-tau/c**2

def collar_initial(theta,side):
    j=0 if side=='L' else 4
    a,c=np.exp(theta[j]),np.exp(theta[j+1]);tau=np.exp(theta[8])
    return np.array([a,c,throat_u(a,c,tau),0.,theta[j+2],0.,0.])

def integrate_collar(theta,side,accurate=False):
    j=0 if side=='L' else 4
    c0=np.exp(theta[j+1]);length=np.exp(theta[j+3]);tau=np.exp(theta[8])
    p=Parameters(tau=tau,h0=-2*c0**2,pv=0.,hopf_m=1,kappa_psi=1.)
    rt,at,steps=(2e-10,2e-12,220) if accurate else (2e-8,2e-10,70)
    sol=solve_ivp(lambda s,Y:inner_rhs(s,Y,p),(0,length),collar_initial(theta,side),
        method='DOP853',rtol=rt,atol=at,max_step=length/steps)
    return sol,p

def causal_initial(Y,theta):
    a,c,u,v,pia,pic,piu=Y
    return np.array([0.,0.,np.log(a),np.log(c),u,v,0.,
                     theta[9],theta[10],a*pia,c*pic,piu,0.,0.])

def integrate_causal(Y0,tau,accurate=False):
    rt,at=(2e-10,2e-12) if accurate else (2e-8,2e-10)
    def augmented(s,Y):
        base=causal_rhs(s,Y[:13],tau)
        _,V,_=causal_velocities(Y[:13],tau)
        return np.r_[base,V]
    method='Radau' if accurate else 'LSODA'
    return solve_ivp(augmented,(0,.5),Y0,method=method,rtol=rt,atol=at)

def energy_hat(Y):
    # Razão geométrica depois da normalização constitucional de U. O fator
    # causal/dimensional K_gamma deve multiplicá-la na comparação física.
    if Y[13] <= 0:return np.inf
    return Y[7]*np.exp(-Y[0])/Y[13]

def residual(theta,accurate=False):
    try:
        tau=np.exp(theta[8])
        L,pL=integrate_collar(theta,'L',accurate)
        R,pR=integrate_collar(theta,'R',accurate)
        if not L.success or not R.success or np.min(L.y[:2])<1e-6 or np.min(R.y[:2])<1e-6:
            return np.full(11,1e3)
        Y0=causal_initial(L.y[:,-1],theta)
        E=integrate_causal(Y0,tau,accurate)
        if not E.success:return np.full(11,1e3)
        q=E.y[:,-1];a,c,u,v,pia,pic,piu=R.y[:,-1]
        return np.array([
            q[0],q[1],q[2]-np.log(a),q[3]-np.log(c),q[4]-u,
            q[9]+a*pia,q[10]+c*pic,q[11]+piu,
            causal_constraint(Y0[:13],tau),
            (2*q[2]+q[3])/3-LOG_R_COS,
            energy_hat(q)-E_H_HAT,
        ])
    except (FloatingPointError,OverflowError,ValueError,ZeroDivisionError):
        return np.full(11,1e3)

def diagnostics(theta):
    tau=np.exp(theta[8]);L,pL=integrate_collar(theta,'L',True);R,pR=integrate_collar(theta,'R',True)
    Y0=causal_initial(L.y[:,-1],theta);E=integrate_causal(Y0,tau,True)
    cL=max(abs(inner_constraint(Y,pL)) for Y in L.y.T)
    cR=max(abs(inner_constraint(Y,pR)) for Y in R.y.T)
    cE=max(abs(causal_constraint(Y[:13],tau)) for Y in E.y.T)
    return L,R,E,cL,cR,cE

def solve():
    old=np.array([-7.75631235e-1,-1.00456477,-4.39191944e-5,-1.43954597,
                  -9.33914189e-1,-3.63068075e-1,-1.54334445e-3,-2.28771423,
                  -2.90976275,-1.15737646e-2])
    # Decompõe o antigo momento isotrópico em 1+3 direções e usa a condição
    # energética apenas como semente, não como parâmetro ajustado.
    seed=np.r_[old[:9],old[9]/4,3*old[9]/4]
    # Caixa física de continuação em torno da solução histórica. Caixas muito
    # amplas levam o integrador a métricas degeneradas e não acrescentam
    # informação sobre o ramo conectado que está sendo testado.
    lo=np.array([-2,-2,-1,-3,-2,-2,-1,-3,-4,-1,-1.])
    hi=np.array([1,1,1,-1,1,1,1,-1,-1,1,1.])
    opt=least_squares(residual,seed,bounds=(lo,hi),jac='3-point',
        xtol=2e-9,ftol=2e-9,gtol=2e-9,max_nfev=80,verbose=2,x_scale='jac')
    rp=residual(opt.x,True);L,R,E,cL,cR,cE=diagnostics(opt.x)
    # Jacobiana independente no candidato, usada somente para posto/condição.
    J=np.empty((11,11));h=2e-5
    for k in range(11):
        step=h*max(1.,abs(opt.x[k]));xp=opt.x.copy();xm=opt.x.copy();xp[k]+=step;xm[k]-=step
        J[:,k]=(residual(xp,True)-residual(xm,True))/(2*step)
    sv=np.linalg.svd(J,compute_uv=False);tol=11*np.finfo(float).eps*sv[0]
    accepted=np.linalg.norm(rp)<1e-7 and cE<1e-7 and np.sum(sv>tol)==11
    print('Solver final causal 11x11')
    print('optimizer_success =',opt.success);print('accepted_as_reduced_saddle =',accepted)
    print('theta =',repr(opt.x));print('tau =',np.exp(opt.x[8]))
    print('residual_accurate =',repr(rp));print('norm_accurate =',np.linalg.norm(rp))
    print('max_constraint_left =',cL);print('max_constraint_right =',cR);print('max_constraint_causal =',cE)
    print('singular_values =',repr(sv));print('rank =',np.sum(sv>tol));print('condition =',sv[0]/sv[-1] if sv[-1]>0 else np.inf)
    print('R_cos =',R_COS);print('beta_E =',BETA_E);print('energy_hat_final =',energy_hat(E.y[:,-1]))
    print('Z_unscaled =',E.y[13,-1])
    return opt,accepted

if __name__=='__main__':solve()
