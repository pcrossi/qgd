#!/usr/bin/env python3
"""Busca condicional da sela GDQ com duas interfaces independentes.

Teste numérico de existência, sem alvos experimentais e ainda sem C_E.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
from ponte_global_local_integrador import Parameters, constraint as c_inner, rhs as rhs_inner
from ponte_global_local_busca_sela_condicional import ext_constraint, ext_rhs

def throat_u(a0,c0,tau):
    return 4-8*tau/a0**2+4*tau*c0**2/a0**4-tau/c0**2

def integrate_collar(loga,logc,pa0,loglength,tau,accurate=False):
    a0,c0,length=np.exp(loga),np.exp(logc),np.exp(loglength)
    Y0=np.array([a0,c0,throat_u(a0,c0,tau),0.,pa0,0.,0.])
    p=Parameters(tau=tau,h0=-2*c0**2,pv=0.,hopf_m=1,kappa_psi=1.)
    rt,at,steps=(2e-10,2e-12,180) if accurate else (2e-8,2e-10,60)
    sol=solve_ivp(lambda s,Y:rhs_inner(s,Y,p),(0,length),Y0,method='DOP853',rtol=rt,atol=at,max_step=length/steps)
    return sol,p

def exterior_initial(Y,px0):
    a,c,u,v,pia,pic,piu=Y
    return np.array([0.,np.log(a),np.log(c),u,v,px0,a*pia,c*pic,piu,0.,0.])

def integrate_exterior(Y0,tau,length=.5,accurate=False):
    rt,at,steps=(2e-10,2e-12,240) if accurate else (2e-8,2e-10,90)
    return solve_ivp(lambda s,Y:ext_rhs(s,Y,tau),(0,length),Y0,method='DOP853',rtol=rt,atol=at,max_step=length/steps)

def unpack(t):
    return t[:4],t[4:8],np.exp(t[8]),t[9]

def residual(t,accurate=False):
    try:
        lp,rp,tau,px0=unpack(t)
        left,pL=integrate_collar(*lp,tau,accurate)
        right,pR=integrate_collar(*rp,tau,accurate)
        if not left.success or not right.success or np.min(left.y[:2])<=1e-5 or np.min(right.y[:2])<=1e-5:
            return np.full(10,1e3)
        YL,YR=left.y[:7,-1],right.y[:7,-1]
        ext0=exterior_initial(YL,px0)
        ext=integrate_exterior(ext0,tau,accurate=accurate)
        if not ext.success:return np.full(10,1e3)
        e=ext.y[:,-1]; a,c,u,v,pia,pic,piu=YR
        return np.array([e[0],e[1]-np.log(a),e[2]-np.log(c),e[3]-u,e[4]-v,e[6]+a*pia,e[7]+c*pic,e[8]+piu,e[9],ext_constraint(ext0,tau)])
    except (FloatingPointError,OverflowError,ValueError):
        return np.full(10,1e3)

def solve():
    ell=np.log(.05)
    seed=np.array([
        -7.75631235e-01,-1.00456477e+00,-4.39191944e-05,-1.43954597e+00,
        -9.33914189e-01,-3.63068075e-01,-1.54334445e-03,-2.28771423e+00,
        -2.90976275e+00,-1.15737646e-02,
    ])
    lo=np.array([-3,-3,-200,np.log(.003),-3,-3,-200,np.log(.003),-5,-300.])
    hi=np.array([3,3,200,np.log(.5),3,3,200,np.log(.5),5,300.])
    opt=least_squares(residual,seed,bounds=(lo,hi),xtol=2e-10,ftol=2e-10,gtol=2e-10,max_nfev=500,verbose=1)
    ra=residual(opt.x,True); lp,rp,tau,px0=unpack(opt.x)
    left,pL=integrate_collar(*lp,tau,True);right,pR=integrate_collar(*rp,tau,True)
    ext=integrate_exterior(exterior_initial(left.y[:7,-1],px0),tau,accurate=True)
    cL=max(abs(c_inner(Y,pL)) for Y in left.y.T);cR=max(abs(c_inner(Y,pR)) for Y in right.y.T);cE=max(abs(ext_constraint(Y,tau)) for Y in ext.y.T)
    accepted=np.linalg.norm(ra)<1e-7 and cE<1e-7
    print('Busca de duas interfaces independentes')
    print('optimizer_success =',opt.success);print('accepted_as_root =',accepted)
    print('theta =',opt.x);print('tau =',tau);print('residual_accurate =',ra);print('norm_accurate =',np.linalg.norm(ra))
    print('max|C_left| =',cL);print('max|C_right| =',cR);print('max|C_exterior| =',cE);print('Z_unscaled =',ext.y[-1,-1])

if __name__=='__main__':solve()
