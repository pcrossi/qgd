#!/usr/bin/env python3
"""Condição de equilíbrio para circulação relativística no Berger."""

import numpy as np


def obstruction(radius, q):
    return 2.0 + 8.0*(q*q-2.0)/radius**2 + 2.0/(np.pi**2*radius**6*q**2)


if __name__ == "__main__":
    q = np.sqrt(14.0/3.0)
    speed = np.sqrt(11.0/14.0)
    print("Q29 — CONTRAÇÃO RELATIVÍSTICA DE BERGER")
    print(f"q_target       = {q:.12f}")
    print(f"v/c se q=gamma = {speed:.12f}")
    for radius in (0.4, 0.62, 1.0, 1.99841118477, 5.0, 20.0):
        print(f"R={radius:.12f}  R W_R-q W_q={obstruction(radius,q):.12e}")
        assert obstruction(radius, q) > 0
