#!/usr/bin/env python3
"""Busca da Porta B no ramo integrável discreto J_{pi/2}.

K_gamma=1 é fixo. O ramo tem nove parâmetros e onze condições; nenhuma
condição é removida para fabricar uma raiz.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares

from ponte_global_local_ramo_J_discreto_dae import (
    _momenta,collar_algebraic,collar_constraint,collar_lagrangian,collar_rhs,
    exterior_constraint,exterior_rhs,
)
from ponte_global_local_solver_portas_bd import ALPHA,LOG_R_COS

E_INITIAL=-0.3333554761281252


def throat(phi,side):
    j=0 if side=='L' else 4
    r=np.exp(phi[j]);beta=phi[j+1];ell=phi[j+2];tau=np.exp(phi[8]);h0=-2*r*r
    u=4-5*tau/r**2;q=np.array([r,r,u,0.]);zero=np.zeros(4)

    def state_for(ell):
        p=_momenta(lambda qq,vv,b,e:collar_lagrangian(qq,vv,b,e,tau,h0),q,zero,(beta,ell))
        return np.r_[q,p]

    return state_for(ell),tau,h0,beta,ell


def integrate_collar(phi,side,strict=False):
    j=0 if side=='L' else 4;state,tau,h0,beta,ell=throat(phi,side);length=np.exp(phi[j+3])
    rt,at=(2e-10,2e-12) if strict else (2e-7,2e-9)
    initial=np.r_[state,0.]
    def augmented(s,y):
        base=length*collar_rhs(s,y[:8],tau,h0)
        a,c,u=y[0],y[1],y[2]
        return np.r_[base,length*a*a*c*np.exp(-u)]
    sol=solve_ivp(augmented,(0,1),initial,
                  method='Radau',rtol=rt,atol=at)
    return sol,(tau,h0,beta,ell)


def exterior_initial(left,phi,z_initial=0.):
    q=left[:4];p=left[4:];a,c,u,v=q;pa,pc,pu,pv=p
    return np.array([0.,0.,np.log(a),np.log(c),u,v,0.,phi[9],phi[10],a*pa,c*pc,pu,pv,z_initial])


def integrate_exterior(state,tau,strict=False,length=.5):
    rt,at=(2e-10,2e-12) if strict else (2e-7,2e-9)
    return solve_ivp(lambda s,y:length*exterior_rhs(s,y,tau),(0,1),state,
                     method='Radau',rtol=rt,atol=at)


def residual(phi,h=1.,strict=False,exterior_length=.5,energy_target=None,logr_target=None):
    try:
        left,lp=integrate_collar(phi,'L',strict);right,rp=integrate_collar(phi,'R',strict)
        if not left.success or not right.success:return np.full(11,1e3)
        q0=exterior_initial(left.y[:8,-1],phi,left.y[8,-1]+right.y[8,-1]);ext=integrate_exterior(q0,lp[0],strict,exterior_length)
        if not ext.success:return np.full(11,1e3)
        q=ext.y[:,-1];qr=right.y[:4,-1];pr=right.y[4:8,-1]
        target=(1-h)*E_INITIAL+h if energy_target is None else energy_target
        radius_target=LOG_R_COS if logr_target is None else logr_target
        energy=q[7]*np.exp(-q[0])/q[13]-target
        return np.array([q[0],q[1],q[2]-np.log(qr[0]),q[3]-np.log(qr[1]),q[4]-qr[2],
            q[9]+qr[0]*pr[0],q[10]+qr[1]*pr[1],q[11]+pr[2],
            exterior_constraint(q0[:6],q0[7:13],q0[6],lp[0]),
            (2*q[2]+q[3])/3-radius_target,energy])
    except (ValueError,RuntimeError,FloatingPointError,OverflowError,np.linalg.LinAlgError):
        return np.full(11,1e3)


def historical_seed():
    # raios médios, beta/ell inicialmente nulos, comprimentos históricos
    return np.array([-.89,0.,0.,-1.44,-.65,0.,0.,-2.29,-2.91,-.0029,-.0087])


def expand_reduced(psi):
    """Gauge ell_L=0; o ramo torna o traço z redundante com y."""
    return np.insert(np.asarray(psi),2,0.0)


def residual_reduced(psi,*args,**kwargs):
    full=residual(expand_reduced(psi),*args,**kwargs)
    return np.delete(full,3)  # continuidade de z = continuidade de y neste ramo


# Gauge local do multiplicador identificado pela SVD na âncora regular. Ele
# não remove campo físico; apenas escolhe uma seção transversal à nulidade DAE.
GAUGE_REFERENCE=np.array([-.909111289,-.0499049009,.415566659,-3.52375907,
    -.884367775,.133513600,-.311807506,-3.99999740,-2.80180152,
    -4.51463930e-4,-1.16699828e-3])
GAUGE_NULL=np.array([4.41221739e-9,-3.90051336e-8,-8.06782943e-1,1.51363284e-6,
    -3.00885616e-16,2.00477826e-8,5.90847936e-1,-4.73409494e-6,
    2.41368986e-7,2.23424621e-10,-2.50895431e-10])
GAUGE_NULL=GAUGE_NULL/np.linalg.norm(GAUGE_NULL)


def residual_gauge_fixed(phi,*args,**kwargs):
    physical=np.delete(residual(phi,*args,**kwargs),3)
    return np.r_[physical,GAUGE_NULL@(np.asarray(phi)-GAUGE_REFERENCE)]


def solve_homotopy():
    x=historical_seed();lo=np.array([-3,-10,-10,-4,-3,-10,-10,-4,-5,-5,-5.]);hi=np.array([2,10,10,0,2,10,10,0,2,5,5.])
    history=[]
    for h in np.linspace(0,1,11):
        fun=lambda z:residual(z,h,False)
        opt=least_squares(fun,x,jac='3-point',bounds=(lo,hi),x_scale='jac',max_nfev=100,
                          xtol=2e-9,ftol=2e-9,gtol=2e-9)
        x=opt.x;r=fun(x);history.append((h,opt.nfev,np.linalg.norm(r,np.inf)))
        print('h=',h,'nfev=',opt.nfev,'inf=',history[-1][2],flush=True)
        if history[-1][2]>5e-3 and h>0:return x,history
    return x,history


if __name__=='__main__':
    x,history=solve_homotopy();r=residual(x,history[-1][0],True)
    print('phi=',repr(x));print('strict_residual=',repr(r));print('strict_inf=',np.linalg.norm(r,np.inf));print('history=',history)
