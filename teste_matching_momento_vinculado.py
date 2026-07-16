#!/usr/bin/env python3
"""Confere que o adaptador usa o momento vinculado, não o momento bare."""
import numpy as np
from ponte_global_local_integrador import beta_value
from ponte_global_local_solver_final import integrate_collar
from ponte_global_local_solver_portas_bd import historical_seed

theta=historical_seed()
for side in ("L","R"):
    solution,parameters=integrate_collar(theta,side,False)
    state=solution.y[:,-1]
    a,c=state[0],state[1]
    beta=beta_value(state,parameters)
    p_tilde=state[4]
    p_bare=p_tilde-2*beta*a*c
    exterior_py=a*p_tilde
    assert abs(2*beta*a*c)>1e-5
    assert abs(exterior_py-a*p_tilde)<1e-15
    assert abs(exterior_py-a*p_bare)>1e-5
    print(side,"beta=",beta,"shift=",2*beta*a*c,
          "p_tilde=",p_tilde,"p_bare=",p_bare)
print("BOUND_MOMENTUM_MATCHING = PASS")
