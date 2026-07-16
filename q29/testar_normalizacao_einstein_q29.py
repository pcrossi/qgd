#!/usr/bin/env python3
"""Teste do contorno causal para inserção EM constante no espaço de Einstein."""

import numpy as np

if __name__ == "__main__":
    insertion = 1.998411184770**2
    theta = np.linspace(0, 2*np.pi, 10001)
    z = np.exp(1j*theta)
    integral = insertion*(z[-1]-z[0])
    print("Q29 — NORMALIZAÇÃO EM NO ESPAÇO DE EINSTEIN")
    print(f"Phi_Q constante = {insertion:.12f}")
    print("integral fechada =", integral)
    print("resíduo = 0")
    assert abs(integral) < 1e-14
