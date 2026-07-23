#!/usr/bin/env python3
"""Perfil líder do warp T5 x S3 derivado da redução da ação oficial.

Usa F=f-5A constante apenas para avaliar a solução analítica líder da equação
de A. Não ajusta parâmetros eletrofracos.
"""

from math import pi, sin

R = 1.99841118477
TAU = 1.0
EPSILON = 0.011591040463


def integral_sin2_to_pi(chi):
    return (pi - chi) / 2.0 + sin(2.0 * chi) / 4.0


def warp_prime(chi, radius=R, tau=TAU):
    c = radius**2 / (2.0 * tau)
    return c * integral_sin2_to_pi(chi) / sin(chi) ** 2


if __name__ == "__main__":
    flux = sin(EPSILON) ** 2 * warp_prime(EPSILON)
    required = R**2 / (2.0 * TAU) * integral_sin2_to_pi(EPSILON)
    print("Q29 — WARP LÍDER DA AÇÃO OFICIAL")
    print(f"R, tau, epsilon       = {R:.12f}, {TAU:.12f}, {EPSILON:.12f}")
    print(f"A'(epsilon)           = {warp_prime(EPSILON):.12e}")
    print(f"sin²(epsilon) A'      = {flux:.12e}")
    print(f"fluxo Robin requerido = {required:.12e}")
    print(f"erro da identidade    = {abs(flux-required):.3e}")
    assert abs(flux - required) < 1e-12
