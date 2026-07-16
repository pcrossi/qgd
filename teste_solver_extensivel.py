#!/usr/bin/env python3
"""Regressão do motor extensível contra o solver causal vigente."""
import numpy as np
from ponte_global_local_solver_extensivel import BaseCausalModel, evaluate
from ponte_global_local_solver_portas_bd import (
    energy_ratio_from_porta_a, historical_seed, residual_jacobian,
)

theta=historical_seed()
r_new,j_new=evaluate(BaseCausalModel(),theta)
r_old,j_old=residual_jacobian(theta,energy_ratio_from_porta_a(1,target=-0.3333554761281252))
assert np.max(np.abs(r_new-r_old))<1e-9
assert np.linalg.norm(j_new-j_old)/np.linalg.norm(j_old)<5e-4
print("residual_max_difference =",np.max(np.abs(r_new-r_old)))
print("jacobian_relative_difference =",np.linalg.norm(j_new-j_old)/np.linalg.norm(j_old))
print("extensible_engine_regression = PASS")
