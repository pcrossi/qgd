#!/usr/bin/env python3
"""Equações canônicas do exterior Berger com relógio toroidal distinguido."""
from __future__ import annotations
import numpy as np

def velocities(Y,tau):
    x0,xs,y,z,u,v,lam,p0,ps,py,pz,pu,pv=Y
    V=np.exp(x0+3*xs+2*y+z-u); E=np.exp(z-2*y)
    scale=tau*V
    r0,rS,ry,rz,ru=p0/scale,ps/scale,py/scale-4*E,pz/scale,pu/scale
    dx0=-11*r0/32+rS/32-ru/4
    dxs=r0/32-3*rS/32-ru/4
    dy=-ry/8-ru/4
    dz=-rz/2-ru/2
    du=-r0/4-rS/4-ry/4-rz/2-3*ru/2
    dv=pv/(2*scale)
    return np.array([dx0,dxs,dy,dz,du,dv]),V,E

def kinetic2(qd):
    x0,xs,y,z,u,v=qd
    return (-.5*x0*x0+3.5*xs*xs+5*x0*xs+4*x0*y+2*x0*z
            +12*xs*y+6*xs*z+4*y*z-2*u*x0-6*u*xs-4*u*y
            -2*u*z+u*u+v*v)

def constraint(Y,tau):
    qd,V,E=velocities(Y,tau)
    u=Y[4];lam=Y[6]
    VB=8*np.exp(-2*Y[2])-4*E*E
    return tau*(VB-kinetic2(qd))+u-4-lam

def rhs(s,Y,tau):
    qd,V,E=velocities(Y,tau)
    dx0,dxs,dy,dz,du,dv=qd
    K2=kinetic2(qd);VB=8*np.exp(-2*Y[2])-4*E*E
    F=tau*(K2+4*E*dy+VB)+Y[4]-4-Y[6]
    dp0=V*F
    dps=3*V*F
    dpy=V*(2*F+tau*(-8*E*dy-16*np.exp(-2*Y[2])+16*E*E))
    dpz=V*(F+tau*(4*E*dy-8*E*E))
    dpu=V*(1-F)
    return np.array([dx0,dxs,dy,dz,du,dv,0.,dp0,dps,dpy,dpz,dpu,0.])

def energy_relative(Y,Yref,energy_scale=1.0):
    """Energia relativa; energy_scale contém prefator da ação e volumes."""
    return energy_scale*(Y[7]*np.exp(-Y[0])-Yref[7]*np.exp(-Yref[0]))

