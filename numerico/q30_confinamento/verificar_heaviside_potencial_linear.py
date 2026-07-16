#!/usr/bin/env python3
"""Verifica V_mu(r)-V_mu(0) -> sigma*r."""

import numpy as np

sigma = 1.0
radii = np.array([0.25, 0.5, 1.0, 2.0, 4.0])
mus = [1e-1, 5e-2, 1e-2, 5e-3, 1e-3]

print("mu max_relative_error")
previous_error = float("inf")
for mu in mus:
    potential = sigma * (1.0 - np.exp(-mu * radii)) / mu
    target = sigma * radii
    error = float(np.max(np.abs(potential - target) / target))
    print(f"{mu:.1e} {error:.12e}")
    if error >= previous_error:
        raise SystemExit("A convergência não foi monotônica.")
    previous_error = error

if previous_error > 3e-3:
    raise SystemExit("Erro final acima da tolerância.")
