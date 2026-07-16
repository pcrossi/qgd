#!/usr/bin/env python3
"""Compara o resíduo Q38 com a superfície de massa derivada em Q40."""

import math


pi = math.pi
alpha = (9.0 / (8.0 * pi**4)) * ((pi**5 / 1920.0) ** 0.25)
chi = 3.0 * math.sqrt(2.0) / 5.0
pi1_bare = alpha**4 * (1.0 + alpha) * math.exp(-1.0 / (2.0 * alpha)) / chi

G = 6.67430e-11
mp = 1.672621e-27
hbar = 1.05457e-34
c = 299792458.0
pi1_obs = G * mp**2 / (hbar * c)

bulk_q40 = 6.0 * pi**5
surface_q40 = alpha * (3.0 * pi / 2.0 + 3.0 / (4.0 * pi**3))
delta_q40 = surface_q40 / bulk_q40
delta_mass_required = math.sqrt(pi1_obs / pi1_bare) - 1.0
prefactor_required = pi1_obs / pi1_bare

print("Q38/Q40 — AUDITORIA DO RESÍDUO")
print(f"bulk_Q40                     = {bulk_q40:.12f}")
print(f"surface_Q40                  = {surface_q40:.12f}")
print(f"delta_surface_Q40            = {delta_q40:.12e} ({100*delta_q40:.9f}%)")
print(f"delta_mass_required_Q38      = {delta_mass_required:.12e} ({100*delta_mass_required:.9f}%)")
print(f"razao_required/surface_Q40   = {delta_mass_required/delta_q40:.9f}")
print(f"prefator_determinante_req    = {prefactor_required:.12f}")
print("\nConclusão: a superfície Q40 não fecha o resíduo Q38;")
print("o teste independente restante é o determinante espectral do Schur.")
