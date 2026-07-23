#!/usr/bin/env python3
"""Segunda variação métrica das parcelas de transgressão usadas na Q40."""

from math import pi
import numpy as np

alpha = 1/137.03599907
cs = alpha*3*pi/2
throat = alpha*3/(4*pi**3)
# Em u=ln R, v=ln q: V_throat=throat*exp(-3u-v).
hessian = throat*np.array([[9.0, 3.0], [3.0, 1.0]])

if __name__ == "__main__":
    print("Q29 — SEGUNDA VARIAÇÃO DA TRANSGRESSÃO Q40")
    print(f"V_CS background       = {cs:.12e}")
    print(f"V_throat background   = {throat:.12e}")
    print("H_CS métrica          = 0")
    print("H_throat(logR,logq)   =")
    print(hessian)
    print("spec H_throat         =", np.linalg.eigvalsh(hessian))
    print(f"alpha^-1 usando só stiffness throat = {137.03599907/(1+throat):.12f}")
    assert np.allclose(np.linalg.eigvalsh(hessian), [0.0, 10*throat], atol=1e-15)
