"""Utilidades numéricas reduzidas para aplicações GDQ.

Este módulo não implementa a ação GDQ completa. Ele reúne blocos reutilizáveis
para reduções efetivas já classificadas: DtN/Schur, resposta quadrática e
observáveis de coerência.
"""

from __future__ import annotations

import math

import numpy as np


def coth(x: float) -> float:
    """Cotangente hiperbólica estável para argumentos reais não nulos."""

    if abs(x) < 1.0e-12:
        raise ValueError("coth(x) exige |x| > 0 no uso atual")
    return math.cosh(x) / math.sinh(x)


def dtn_massive_interval(lambda_eff: float, length: float) -> float:
    """DtN de `-d_s^2 + lambda_eff^2` em `[0, length]`.

    Condições:

    - Dirichlet prescrito em `s = 0`;
    - Dirichlet absorvente/aterrado em `s = length`.

    Retorna:

    `lambda_eff * coth(lambda_eff * length)`.
    """

    if lambda_eff <= 0:
        raise ValueError("lambda_eff deve ser positivo")
    if length <= 0:
        raise ValueError("length deve ser positivo")
    return lambda_eff * coth(lambda_eff * length)


def schur_complement(
    k_boundary_boundary: np.ndarray,
    k_boundary_internal: np.ndarray,
    k_internal_boundary: np.ndarray,
    k_internal_internal: np.ndarray,
) -> np.ndarray:
    """Complemento de Schur que elimina graus internos.

    Retorna:

    `K_bb - K_bi K_ii^{-1} K_ib`.
    """

    return k_boundary_boundary - k_boundary_internal @ np.linalg.solve(
        k_internal_internal,
        k_internal_boundary,
    )


def quadratic_response(delta_boundary: np.ndarray, impedance: np.ndarray | float) -> float:
    """Forma quadrática `1/2 <delta, R delta>`."""

    delta = np.asarray(delta_boundary, dtype=float)
    if np.isscalar(impedance):
        return 0.5 * float(impedance) * float(delta @ delta)
    r = np.asarray(impedance, dtype=float)
    return 0.5 * float(delta @ r @ delta)


def detector_gamma(
    zeta: float,
    lambda_eff: float,
    length: float,
    c_path: float = 1.0,
) -> float:
    """Custo de distinção de caminhos para detector linear reduzido."""

    if c_path < 0:
        raise ValueError("c_path deve ser não negativo")
    r_det = dtn_massive_interval(lambda_eff, length)
    return 0.5 * zeta * zeta * c_path * r_det


def coherence_from_gamma(gamma: float) -> float:
    """Coeficiente de coerência `exp(-gamma)`."""

    return math.exp(-gamma)


def two_path_density(
    i1: np.ndarray,
    i2: np.ndarray,
    phase: np.ndarray,
    gamma: float = 0.0,
) -> np.ndarray:
    """Densidade reduzida de duas alternativas com amortecimento do termo cruzado."""

    return i1 + i2 + 2.0 * math.exp(-gamma) * np.sqrt(i1 * i2) * np.cos(phase)

