#!/usr/bin/env python3
"""Auditoria algébrica: fase eta versus módulo do determinante."""

import cmath
from math import pi

ZETA_PRIME = 2.0  # valor simbólico de teste para a parte par
ETA = 3.0         # produz fase -3pi/2 na convenção usada

logdet = -0.5*ZETA_PRIME - 0.5j*pi*ETA

if __name__ == "__main__":
    determinant = cmath.exp(logdet)
    print("Q29 — ETA-FORMA E RIGIDEZ")
    print("Re logdet (módulo) =", logdet.real)
    print("Im logdet (fase)   =", logdet.imag)
    print("|det|              =", abs(determinant))
    print("arg(det)           =", cmath.phase(determinant))
    # Alterar eta não altera o módulo.
    other = cmath.exp(-0.5*ZETA_PRIME - 0.5j*pi*(ETA+0.25))
    assert abs(abs(other)-abs(determinant)) < 1e-15
