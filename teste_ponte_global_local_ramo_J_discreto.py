#!/usr/bin/env python3
import numpy as np
from ponte_global_local_ramo_J_discreto import *


def der(fun,x,i,h=1e-6):
    p=x.copy();m=x.copy();p[i]+=h;m[i]-=h
    return (fun(*p)-fun(*m))/(2*h)


def main():
    x=np.array([1.2,.9,.17,-.11])
    tau,V=.8,1.7
    fun=lambda a,c,ad,cd:tau*V*delta_K(a,c,ad,cd)
    num=np.array([der(fun,x,2),der(fun,x,3)])
    ex=momentum_shifts(tau,V,*x,ell=0)
    assert np.linalg.norm(num-ex)<2e-9
    cd=restricted_cd(x[0],x[1],x[2])
    assert abs(integrability(x[0],x[1],x[2],cd))<1e-15
    assert abs(restricted_delta_K(x[0],x[1],x[2])+8*x[2]*x[1]**1/x[0]**3)<1e-14
    # Variação de lapse por N: N tau V DeltaK(qdot/N)+ell N F(qdot/N).
    ell=.31
    def NL(N):
        F=integrability(x[0],x[1],x[2]/N,x[3]/N)
        return N*tau*V*delta_K(x[0],x[1],x[2]/N,x[3]/N)+N*ell*F
    nd=(NL(1+1e-6)-NL(1-1e-6))/(2e-6)
    assert abs(nd-lapse_shift(tau,V,*x,ell))<3e-9
    print('RAMO J DISCRETO: identidades aprovadas')
    print('erro momentos =',np.linalg.norm(num-ex))
    print('erro lapse =',abs(nd-lapse_shift(tau,V,*x,ell)))


if __name__=='__main__':main()
