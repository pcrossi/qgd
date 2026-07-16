#!/usr/bin/env python3
"""Testes diferenciais das fórmulas do modo J; não são uma sela GDQ."""
import numpy as np
from ponte_global_local_modo_J import (
    delta_K, momentum_corrections, lapse_correction, invert_chid,
    torsion_coefficients,
)


def derivative(fun, x, i, h=1e-6):
    xp=x.copy(); xm=x.copy(); xp[i]+=h; xm[i]-=h
    return (fun(*xp)-fun(*xm))/(2*h)


def main():
    x=np.array([1.2,.91,.13,-.07,.23,.11]) # a,c,ad,cd,chi,chid
    tau,vol=.83,1.71
    fun=lambda a,c,ad,cd,ch,chd: delta_K(a,c,ad,cd,ch,chd)
    numeric=np.array([derivative(fun,x,2),derivative(fun,x,3),derivative(fun,x,5)])*tau*vol
    exact=momentum_corrections(tau,vol,*x)
    assert np.linalg.norm(numeric-exact)<2e-9,(numeric,exact)
    chd=invert_chid(tau,vol,*x[:4],x[4],exact[2])
    assert abs(chd-x[5])<1e-13
    # Setor original recuperado exatamente para chi=chid=0.
    assert delta_K(*x[:4],0.,0.)==0.
    A,B,k0,_=torsion_coefficients(*x[:4],0.,0.)
    assert A==k0 and B==0.
    # Confere variação de lapse por escalonamento N: dot q -> dot q/N.
    def NL(N):
        return N*tau*delta_K(x[0],x[1],x[2]/N,x[3]/N,x[4],x[5]/N)
    num=(NL(1+1e-6)-NL(1-1e-6))/(2e-6)
    assert abs(num-lapse_correction(tau,*x))<2e-9,(num,lapse_correction(tau,*x))
    print('MODO J: identidades variacionais aprovadas')
    print('erro dos momentos =',np.linalg.norm(numeric-exact))
    print('erro da restrição =',abs(num-lapse_correction(tau,*x)))


if __name__=='__main__': main()
