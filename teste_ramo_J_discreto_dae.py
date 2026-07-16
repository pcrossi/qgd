#!/usr/bin/env python3
"""Testes do bloco algébrico e das identidades variacionais da DAE."""
import numpy as np
from ponte_global_local_ramo_J_discreto import integrability
from ponte_global_local_ramo_J_discreto_dae import *
from ponte_global_local_ramo_J_discreto_dae import _momenta

tau=.08;h0=-.32
q=np.array([.52,.41,1.1,.0]);qd=np.array([(2*q[1]**2+h0)/(2*q[0]*q[1]),0.,.03,0.])
# Ajusta cd exatamente por F_I=0.
qd[1]=q[1]*qd[0]/q[0]-2+2*q[1]**2/q[0]**2
beta,ell=.17,-.09
p=_momenta(lambda qq,vv,b,e:collar_lagrangian(qq,vv,b,e,tau,h0),q,qd,(beta,ell))
back,b2,e2=collar_algebraic(q,p,tau,h0)
assert np.linalg.norm(back-qd)<2e-12
assert abs(b2-beta)<2e-12 and abs(e2-ell)<2e-12
assert abs(integrability(q[0],q[1],back[0],back[1]))<2e-13

qe=np.array([.1,-.03,np.log(.8),np.log(.7),1.2,.0]);qde=np.array([.02,-.01,.04,0,.03,0.])
qde[3]=qde[2]-2/np.exp(qe[3])+2*np.exp(qe[3]-2*qe[2]);elle=.13;lam=-.2
pe=_momenta(lambda qq,vv,e:exterior_lagrangian(qq,vv,e,lam,tau),qe,qde,(elle,))
backe,elle2=exterior_algebraic(qe,pe,lam,tau)
assert np.linalg.norm(backe-qde)<2e-12 and abs(elle2-elle)<2e-12
assert abs(exterior_integrability(qe,backe))<2e-13

# Restrição por variação do lapse: L-qdot.p.
hc=collar_constraint(q,p,tau,h0)
he=exterior_constraint(qe,pe,lam,tau)
assert np.isfinite(hc) and np.isfinite(he)
print('collar_velocity_error =',np.linalg.norm(back-qd))
print('collar_multiplier_error =',max(abs(b2-beta),abs(e2-ell)))
print('exterior_velocity_error =',np.linalg.norm(backe-qde))
print('exterior_multiplier_error =',abs(elle2-elle))
print('collar/exterior constraints =',hc,he)
print('DISCRETE_J_DAE = PASS')
