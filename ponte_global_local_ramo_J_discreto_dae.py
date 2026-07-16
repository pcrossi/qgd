#!/usr/bin/env python3
"""DAE Hamiltoniana do ramo integrável discreto J_{pi/2}.

Os multiplicadores beta (carga) e ell (integrabilidade) são eliminados por um
bloco algébrico afim a cada avaliação. Não são campos físicos.
"""
from __future__ import annotations
import numpy as np
from ponte_global_local_ramo_J_discreto import delta_K, integrability

CS=1e-30


def _gradient(fun,x):
    out=np.empty(x.size)
    for k in range(x.size):
        z=x.astype(complex);z[k]+=1j*CS;out[k]=np.imag(fun(z))/CS
    return out


def _momenta(lagrangian,q,qd,multipliers):
    return _gradient(lambda vel:lagrangian(q,vel,*multipliers),qd)


def _affine_solve(moment_function,constraints,p):
    """Resolve momentos+restrições afins em (qdot,multiplicadores)."""
    n=p.size;m=len(constraints);zero=np.zeros(n+m)
    def equations(w):
        qd=w[:n];mul=w[n:]
        return np.r_[moment_function(qd,mul)-p,[fun(qd) for fun in constraints]]
    offset=equations(zero)
    matrix=np.column_stack([equations(np.eye(n+m)[k])-offset for k in range(n+m)])
    return np.linalg.solve(matrix,-offset)


def collar_lagrangian(q,qd,beta,ell,tau,h0,m=1,kappa=1):
    a,c,u,v=q;ad,cd,ud,vd=qd;emu=np.exp(-u)
    Q=4*a*ad*cd-4*a*c*ud*ad-2*a*a*ud*cd+a*a*c*(ud*ud+vd*vd)
    potential=8*c-4*c**3/a**2+kappa*a*a*m*m/c
    base=emu*(tau*(Q+4*c*c*ad/a+potential)+a*a*c*(u-4))
    correction=tau*a*a*c*emu*delta_K(a,c,ad,cd)
    charge=beta*(2*c*(a*ad-c)-h0)
    integ=ell*integrability(a,c,ad,cd)
    return base+correction+charge+integ


def collar_algebraic(q,p,tau,h0,m=1,kappa=1):
    a,c=q[:2]
    mom=lambda qd,mul:_momenta(
        lambda qq,vv,b,e:collar_lagrangian(qq,vv,b,e,tau,h0,m,kappa),q,qd,mul)
    constraints=[lambda qd:2*c*(a*qd[0]-c)-h0,
                 lambda qd:integrability(a,c,qd[0],qd[1])]
    result=_affine_solve(mom,constraints,p)
    return result[:4],result[4],result[5]


def collar_constraint(q,p,tau,h0,m=1,kappa=1):
    qd,beta,ell=collar_algebraic(q,p,tau,h0,m,kappa)
    L=collar_lagrangian(q,qd,beta,ell,tau,h0,m,kappa)
    return L-np.dot(qd,p)


def collar_rhs(_s,state,tau,h0,m=1,kappa=1):
    q=state[:4];p=state[4:8];qd,beta,ell=collar_algebraic(q,p,tau,h0,m,kappa)
    pd=_gradient(lambda qq:collar_lagrangian(qq,qd,beta,ell,tau,h0,m,kappa),q)
    return np.r_[qd,pd]


def exterior_volume(q):
    x0,xs,y,z,u,_v=q
    return np.exp(x0+3*xs+2*y+z-u)


def exterior_base_K(q,qd):
    _x0,_xs,y,z,_u,_v=q;x0d,xsd,yd,zd,ud,vd=qd;E=np.exp(z-2*y)
    K2=(-.5*x0d*x0d+3.5*xsd*xsd+5*x0d*xsd+4*x0d*yd+2*x0d*zd
        +12*xsd*yd+6*xsd*zd+4*yd*zd-2*ud*x0d-6*ud*xsd
        -4*ud*yd-2*ud*zd+ud*ud+vd*vd)
    return K2+4*E*yd+8*np.exp(-2*y)-4*E*E


def exterior_integrability(q,qd):
    a,c=np.exp(q[2]),np.exp(q[3]);return integrability(a,c,a*qd[2],c*qd[3])


def exterior_lagrangian(q,qd,ell,lam,tau):
    a,c=np.exp(q[2]),np.exp(q[3]);V=exterior_volume(q)
    correction=delta_K(a,c,a*qd[2],c*qd[3])
    return V*(tau*(exterior_base_K(q,qd)+correction)+q[4]-4-lam)+ell*exterior_integrability(q,qd)


def exterior_algebraic(q,p,lam,tau):
    mom=lambda qd,mul:_momenta(
        lambda qq,vv,e:exterior_lagrangian(qq,vv,e,lam,tau),q,qd,mul)
    result=_affine_solve(mom,[lambda qd:exterior_integrability(q,qd)],p)
    return result[:6],result[6]


def exterior_constraint(q,p,lam,tau):
    qd,ell=exterior_algebraic(q,p,lam,tau)
    return exterior_lagrangian(q,qd,ell,lam,tau)-np.dot(qd,p)


def exterior_rhs(_s,state,tau):
    q=state[:6];lam=state[6];p=state[7:13];qd,ell=exterior_algebraic(q,p,lam,tau)
    pd=_gradient(lambda qq:exterior_lagrangian(qq,qd,ell,lam,tau),q)
    return np.r_[qd,0,pd,exterior_volume(q)]
