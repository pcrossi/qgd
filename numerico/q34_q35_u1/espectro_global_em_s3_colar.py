#!/usr/bin/env python3
"""Espectro EM separado no produto S^3(R) x I_L."""

from math import pi, sqrt

R = 1.03707435228632
TAU = 0.274900522513626
L = pi * sqrt(TAU)

lambda_radial = (pi / L) ** 2
lambda_s3 = 3.0 / R**2
lambda_full = min(lambda_radial, lambda_s3)

print(f"L_over_ell={L:.15g}")
print(f"lambda_radial={lambda_radial:.15g}")
print(f"Lambda_hat_hom={sqrt(lambda_radial):.15g}")
print(f"lambda_s3_l1={lambda_s3:.15g}")
print(f"Lambda_hat_full={sqrt(lambda_full):.15g}")
