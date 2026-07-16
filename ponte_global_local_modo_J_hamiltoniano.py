#!/usr/bin/env python3
"""Bloco Hamiltoniano exato do modo J no exterior causal.

Integração preparatória: não ativa a busca de sela antes da aprovação do
tensor de Nijenhuis. Coordenadas q=(x0,xs,y,z,u,v,chi).
"""
from __future__ import annotations
import numpy as np

from ponte_global_local_modo_J import delta_K, momentum_corrections


def volume(q):
    x0,xs,y,z,u,_v,_chi=q
    return np.exp(x0+3*xs+2*y+z-u)


def base_K(q, qd):
    _x0,_xs,y,z,_u,_v,_chi=q
    x0d,xsd,yd,zd,ud,vd,_chid=qd
    E=np.exp(z-2*y)
    k2=(-.5*x0d*x0d+3.5*xsd*xsd+5*x0d*xsd+4*x0d*yd+2*x0d*zd
        +12*xsd*yd+6*xsd*zd+4*yd*zd-2*ud*x0d-6*ud*xsd
        -4*ud*yd-2*ud*zd+ud*ud+vd*vd)
    return k2+4*E*yd+8*np.exp(-2*y)-4*E*E


def total_K(q,qd):
    a,c=np.exp(q[2]),np.exp(q[3])
    ad,cd=a*qd[2],c*qd[3]
    return base_K(q,qd)+delta_K(a,c,ad,cd,q[6],qd[6])


def moment_map(q,qd,tau):
    """p=tau*V*dK/dqdot em forma analítica."""
    x0d,xsd,yd,zd,ud,vd,chid=qd
    y,z,chi=q[2],q[3],q[6];E=np.exp(z-2*y);V=volume(q);scale=tau*V
    p=np.array([
        -x0d+5*xsd+4*yd+2*zd-2*ud,
        5*x0d+7*xsd+12*yd+6*zd-6*ud,
        4*x0d+12*xsd+4*zd-4*ud+4*E,
        2*x0d+6*xsd+4*yd-2*ud,
        -2*x0d-6*xsd-4*yd-2*zd+2*ud,
        2*vd,
        0*chid,
    ],dtype=np.result_type(q,qd))*scale
    a,c=np.exp(y),np.exp(z)
    dpa,dpc,pchi=momentum_corrections(tau,V,a,c,a*yd,c*zd,chi,chid)
    p[2]+=a*dpa
    p[3]+=c*dpc
    p[6]=pchi
    return p


def velocities(q,p,tau):
    """Inversão exata do mapa afim de momentos (quadrático em velocidades)."""
    zero=np.zeros(7,dtype=np.result_type(q,p));offset=moment_map(q,zero,tau)
    matrix=np.column_stack([moment_map(q,np.eye(7,dtype=zero.dtype)[k],tau)-offset for k in range(7)])
    return np.linalg.solve(matrix,p-offset)


def lapse_constraint(q,p,lam,tau):
    qd=velocities(q,p,tau)
    # C/V=tau(K-qdot.dK)+u-4-lambda; qdot.dK=qdot.p/(tau V).
    return tau*total_K(q,qd)-np.dot(qd,p)/volume(q)+q[4]-4-lam


def lagrangian_density(q,qd,lam,tau):
    return volume(q)*(tau*total_K(q,qd)+q[4]-4-lam)


def momentum_rhs(q,qd,lam,tau):
    """p'=partial L/partial q a velocidade própria fixa."""
    gradient=np.empty(7);step=1e-30
    for k in range(7):
        z=q.astype(complex);z[k]+=1j*step
        gradient[k]=np.imag(lagrangian_density(z,qd.astype(complex),lam,tau))/step
    return gradient


def rhs(_s,state,tau):
    """Estado (q[7],lambda,p[7],Z)."""
    q=state[:7];lam=state[7];p=state[8:15]
    qd=velocities(q,p,tau);pd=momentum_rhs(q,qd,lam,tau)
    return np.r_[qd,0,pd,volume(q)]
