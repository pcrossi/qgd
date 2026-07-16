#!/usr/bin/env python3
"""Teste do projetor causal de Cauchy usado na ponte global--local.

Classificacao: teste de consistencia numerico de uma identidade analitica.
Nao ajusta parametros fisicos e nao procura a sela radial.
"""
from __future__ import annotations

import numpy as np


def projector(values: np.ndarray, winding: int = 1) -> complex:
    """Quadratura trapezoidal de (2 pi i w)^-1 int F(z) dz/z.

    Para z=r exp(i w theta), dz/z=i w dtheta e o projetor e a media
    angular. ``values`` deve ser amostrado uniformemente em theta, sem repetir
    o ponto final.
    """
    if winding == 0:
        raise ValueError("o winding causal deve ser nao nulo")
    return np.mean(values)


def laurent(theta: np.ndarray, coeffs: dict[int, complex], winding: int = 1,
            radius: float = 0.7) -> np.ndarray:
    z = radius * np.exp(1j * winding * theta)
    return sum(c * z**k for k, c in coeffs.items())


def run() -> None:
    coeffs = {-3: 0.2 - 0.1j, -1: -0.7j, 0: 1.25 + 0.4j,
              2: -3.0 + 0.2j, 5: 0.8}
    print("Projetor causal normalizado da ponte global--local")
    print("coeficiente_exato =", coeffs[0])
    for winding in (1, 2, -1):
        for n in (64, 128, 256, 512, 1024):
            theta = 2 * np.pi * np.arange(n) / n
            got = projector(laurent(theta, coeffs, winding=winding), winding)
            err = abs(got - coeffs[0])
            print(f"w={winding:+d} N={n:4d} valor={got!r} erro={err:.3e}")

    # Um integrando constante e hermitiano e projetado em si mesmo. Essa e a
    # origem matematica do fator causal unitario, nao uma calibracao do solver.
    theta = 2 * np.pi * np.arange(256) / 256
    unit = projector(np.ones_like(theta, dtype=complex))
    print("K_gamma_constante =", unit)
    if abs(unit - 1) > 1e-13:
        raise RuntimeError("falha no projetor causal unitario")


if __name__ == "__main__":
    run()
