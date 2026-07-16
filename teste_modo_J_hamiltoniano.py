#!/usr/bin/env python3
"""Validações canônicas do bloco J sem executar a sela."""
import numpy as np
from ponte_global_local_modo_J_hamiltoniano import (
    lagrangian_density,lapse_constraint,moment_map,momentum_rhs,total_K,velocities,
)
from ponte_global_local_exterior_causal_equacoes import (
    constraint as old_constraint,rhs as old_rhs,velocities as old_velocities,
)

q=np.array([.1,-.07,np.log(.91),np.log(.83),1.2,.2,.23])
qd=np.array([.03,-.02,.04,-.01,.05,.06,.07]);tau=.81;lam=-.4
p=moment_map(q,qd,tau)
recovered=velocities(q,p,tau)
assert np.linalg.norm(recovered-qd)<2e-13

# Derivada do Lagrangiano em velocidades reproduz o mapa de momentos.
numeric=np.empty(7);h=1e-6
for k in range(7):
    plus=qd.copy();minus=qd.copy();plus[k]+=h;minus[k]-=h
    numeric[k]=(lagrangian_density(q,plus,lam,tau)-lagrangian_density(q,minus,lam,tau))/(2*h)
assert np.linalg.norm(numeric-p)<2e-8

# Variação do lapse por escalonamento de todas as velocidades próprias.
def NL(N):return N*lagrangian_density(q,qd/N,lam,tau)
num_lapse=(NL(1+h)-NL(1-h))/(2*h)/np.exp(q[0]+3*q[1]+2*q[2]+q[3]-q[4])
assert abs(num_lapse-lapse_constraint(q,p,lam,tau))<2e-8

# Regressão integral chi=pchi=0 contra o exterior causal anterior.
q0=q.copy();q0[6]=0.;qd0=qd.copy();qd0[6]=0.;p0=moment_map(q0,qd0,tau)
old_state=np.r_[q0[:6],lam,p0[:6]]
old_qd,_,_=old_velocities(old_state,tau)
assert np.linalg.norm(velocities(q0,p0,tau)[:6]-old_qd)<2e-13
assert abs(lapse_constraint(q0,p0,lam,tau)-old_constraint(old_state,tau))<2e-13
new_pd=momentum_rhs(q0,qd0,lam,tau)[:6]
old_pd=old_rhs(0,old_state,tau)[7:13]
assert np.linalg.norm(new_pd-old_pd)<2e-11,(new_pd,old_pd)

print('moment_inversion_error =',np.linalg.norm(recovered-qd))
print('lagrangian_momentum_error =',np.linalg.norm(numeric-p))
print('lapse_variation_error =',abs(num_lapse-lapse_constraint(q,p,lam,tau)))
print('chi_zero_velocity_regression =',np.linalg.norm(velocities(q0,p0,tau)[:6]-old_qd))
print('chi_zero_rhs_regression =',np.linalg.norm(new_pd-old_pd))
print('MODE_J_HAMILTONIAN = PASS (saddle execution disabled)')
