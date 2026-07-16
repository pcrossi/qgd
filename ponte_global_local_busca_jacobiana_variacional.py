#!/usr/bin/env python3
"""Busca de duas interfaces com Jacobiana variacional transportada.

Classificação: teste numérico de existência condicional, ainda sem C_E.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
from ponte_global_local_integrador import Parameters, rhs_complex
from ponte_global_local_busca_sela_condicional import ext_constraint, ext_rhs
from ponte_global_local_busca_duas_interfaces import residual as residual_precise

NPAR=10; EPS=1e-30

def throat_state(theta,side):
    j=0 if side=='L' else 4
    la,lc,pa,ll=theta[j:j+4]; tau=np.exp(theta[8])
    a,c=np.exp(la),np.exp(lc)
    u=4-8*tau/a**2+4*tau*c**2/a**4-tau/c**2
    return np.array([a,c,u,0.,pa,0.,0.],dtype=np.result_type(theta))

def inner_field(t,Y,theta,side):
    j=0 if side=='L' else 4
    c0=np.exp(theta[j+1]); length=np.exp(theta[j+3]);tau=np.exp(theta[8])
    p=Parameters(tau=tau,h0=-2*c0**2,pv=0.,hopf_m=1,kappa_psi=1.)
    return length*rhs_complex(Y,p)

def exterior_field(t,Y,theta):
    return .5*ext_rhs(t,Y,np.exp(theta[8]))

def local_jacobians(fun,Y,theta):
    n=Y.size; jy=np.empty((n,n));jt=np.empty((n,NPAR))
    for k in range(n):
        z=Y.astype(complex);z[k]+=1j*EPS;jy[:,k]=np.imag(fun(0.,z,theta))/EPS
    for k in range(NPAR):
        th=theta.astype(complex);th[k]+=1j*EPS;jt[:,k]=np.imag(fun(0.,Y.astype(complex),th))/EPS
    return jy,jt

def initial_sensitivity(fun,theta):
    y=fun(theta);S=np.empty((y.size,NPAR))
    for k in range(NPAR):
        th=theta.astype(complex);th[k]+=1j*EPS;S[:,k]=np.imag(fun(th))/EPS
    return np.real(y),S

def flow_variational(field,y0,S0,theta,steps):
    n=y0.size
    def aug(t,Z):
        Y=Z[:n];S=Z[n:].reshape(n,NPAR)
        f=np.real(field(t,Y,theta));jy,jt=local_jacobians(field,Y,theta)
        return np.concatenate([f,(jy@S+jt).ravel()])
    sol=solve_ivp(aug,(0.,1.),np.concatenate([y0,S0.ravel()]),method='DOP853',rtol=2e-7,atol=2e-9,max_step=1/steps)
    return sol.y[:n,-1],sol.y[n:,-1].reshape(n,NPAR)

def adapter(Y,S,theta):
    a,c,u,v,pia,pic,piu=Y
    out=np.array([0.,np.log(a),np.log(c),u,v,theta[9],a*pia,c*pic,piu,0.,0.])
    D=np.zeros((11,7));D[1,0]=1/a;D[2,1]=1/c;D[3,2]=1;D[4,3]=1
    D[6,0]=pia;D[6,4]=a;D[7,1]=pic;D[7,5]=c;D[8,6]=1
    Sout=D@S;Sout[5,9]+=1
    return out,Sout

def constraint_gradient(Y,theta):
    tau=np.exp(theta[8]);gY=np.empty(Y.size)
    for k in range(Y.size):
        z=Y.astype(complex);z[k]+=1j*EPS;gY[k]=np.imag(ext_constraint(z,tau))/EPS
    th=theta.astype(complex);th[8]+=1j*EPS
    gt=np.zeros(NPAR);gt[8]=np.imag(ext_constraint(Y.astype(complex),np.exp(th[8])))/EPS
    return gY,gt

def value_jac(theta):
    yL,SL=initial_sensitivity(lambda th:throat_state(th,'L'),theta)
    yR,SR=initial_sensitivity(lambda th:throat_state(th,'R'),theta)
    EL,SEL=flow_variational(lambda t,Y,th:inner_field(t,Y,th,'L'),yL,SL,theta,35)
    ER,SER=flow_variational(lambda t,Y,th:inner_field(t,Y,th,'R'),yR,SR,theta,35)
    X0,SX0=adapter(EL,SEL,theta)
    XE,SXE=flow_variational(exterior_field,X0,SX0,theta,55)
    a,c,u,v,pia,pic,piu=ER
    r=np.array([XE[0],XE[1]-np.log(a),XE[2]-np.log(c),XE[3]-u,XE[4]-v,XE[6]+a*pia,XE[7]+c*pic,XE[8]+piu,XE[9],ext_constraint(X0,np.exp(theta[8]))])
    J=np.zeros((10,NPAR));J[0]=SXE[0];J[1]=SXE[1]-SER[0]/a;J[2]=SXE[2]-SER[1]/c
    J[3]=SXE[3]-SER[2];J[4]=SXE[4]-SER[3]
    J[5]=SXE[6]+pia*SER[0]+a*SER[4];J[6]=SXE[7]+pic*SER[1]+c*SER[5]
    J[7]=SXE[8]+SER[6];J[8]=SXE[9]
    gy,gt=constraint_gradient(X0,theta);J[9]=gy@SX0+gt
    return r,J

def value_jac_with_radius(theta, log_R_cos=0.0):
    """Substitui a continuidade trivial da fase pelo raio cosmológico.

    O extremo direito do exterior é a seção cosmológica distinguida. Para a
    órbita Berger, Vol(S^3)=2*pi^2*a^2*c e, portanto,

        log(R_3/R_cos) = (2*y+z)/3 - log(R_cos).

    A linha de fluxo de fase permanece no sistema como marcador explícito da
    condição energética ainda ausente; ela só pode ser substituída depois de
    especificados o gerador causal xi e sua imersão no ansatz reduzido.
    """
    r,J=value_jac(theta)
    # Reintegra somente para avaliar a seção cosmológica final e sua
    # sensibilidade transportada. Preserva o cálculo histórico em value_jac.
    yL,SL=initial_sensitivity(lambda th:throat_state(th,'L'),theta)
    EL,SEL=flow_variational(lambda t,Y,th:inner_field(t,Y,th,'L'),yL,SL,theta,35)
    X0,SX0=adapter(EL,SEL,theta)
    XE,SXE=flow_variational(exterior_field,X0,SX0,theta,55)
    r[4]=(2*XE[1]+XE[2])/3-log_R_cos
    J[4]=(2*SXE[1]+SXE[2])/3
    return r,J

_cache={}
def cached(theta):
    key=np.asarray(theta).tobytes()
    if key not in _cache:_cache.clear();_cache[key]=value_jac(np.asarray(theta))
    return _cache[key]
def fun(theta):return cached(theta)[0]
def jac(theta):return cached(theta)[1]

def solve():
    seed=np.array([-7.75631235e-1,-1.00456477,-4.39191944e-5,-1.43954597,-9.33914189e-1,-3.63068075e-1,-1.54334445e-3,-2.28771423,-2.90976275,-1.15737646e-2])
    lo=np.array([-3,-3,-200,np.log(.003),-3,-3,-200,np.log(.003),-5,-300.]);hi=np.array([3,3,200,np.log(.5),3,3,200,np.log(.5),5,300.])
    opt=least_squares(fun,seed,jac=jac,bounds=(lo,hi),xtol=1e-10,ftol=1e-10,gtol=1e-10,max_nfev=120,verbose=1)
    rp=residual_precise(opt.x,True)
    print('Busca com Jacobiana variacional');print('optimizer_success =',opt.success);print('theta =',opt.x)
    print('transported_residual =',fun(opt.x));print('precise_residual =',rp);print('precise_norm =',np.linalg.norm(rp));print('accepted_as_root =',np.linalg.norm(rp)<1e-8)

if __name__=='__main__':solve()
