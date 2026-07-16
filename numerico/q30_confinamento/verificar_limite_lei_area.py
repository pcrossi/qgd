#!/usr/bin/env python3
"""Teste de consistência do limite de área com correções de perímetro."""

import numpy as np

sigma = 1.75
mu = 0.31
c_log = 0.12
sizes = np.array([8, 16, 32, 64, 128, 256], dtype=float)

# Contornos quadrados: A=L^2, P=4L. F=sigma*A+mu*P+c_log*log(A).
areas = sizes**2
free_energy = sigma * areas + mu * 4.0 * sizes + c_log * np.log(areas)
estimates = free_energy / areas
errors = np.abs(estimates - sigma)

print("L sigma_estimate absolute_error")
for length, estimate, error in zip(sizes, estimates, errors):
    print(f"{length:.0f} {estimate:.12f} {error:.12e}")

if not np.all(np.diff(errors) < 0):
    raise SystemExit("A correção subextensiva não convergiu monotonicamente.")
if errors[-1] > 6e-3:
    raise SystemExit("Erro final acima da tolerância.")
