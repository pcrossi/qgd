#!/usr/bin/env python3
"""Blocos reduzidos reutilizáveis para cálculos GDQ.

Classificação:
    biblioteca metodológica / redução efetiva.

Este módulo não implementa a ação oficial completa da GDQ. Ele reúne blocos
algébricos que aparecem depois da cadeia:

    ação oficial -> background -> vínculos -> projetor físico
    -> Hessiana física -> eliminação de graus internos.

Os blocos aqui implementados são úteis para verificações, protótipos e
aplicações reduzidas:

    - DtN de um intervalo massivo;
    - complemento de Schur;
    - resposta quadrática;
    - fator de coerência de detector;
    - densidade de duas alternativas.

Qualquer uso metrológico deve declarar de onde vieram os parâmetros de
aparelho, domínio e contorno.
"""

from __future__ import annotations

import math

import numpy as np


def coth(x: float) -> float:
    """Retorna a cotangente hiperbólica de um argumento real não nulo."""

    if abs(x) < 1.0e-12:
        raise ValueError("coth(x) exige |x| > 0")
    return math.cosh(x) / math.sinh(x)


def dtn_massive_interval(lambda_eff: float, length: float) -> float:
    """Operador DtN de `-d_s^2 + lambda_eff^2` em `[0, length]`.

    Condições de contorno:
        varphi(0) = varphi_0;
        varphi(length) = 0.

    A solução interna produz:
        R = lambda_eff * coth(lambda_eff * length).
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
    """Elimina graus internos por complemento de Schur.

    Retorna:
        K_bb - K_bi K_ii^{-1} K_ib.
    """

    return k_boundary_boundary - k_boundary_internal @ np.linalg.solve(
        k_internal_internal,
        k_internal_boundary,
    )


def quadratic_response(delta_boundary: np.ndarray, impedance: np.ndarray | float) -> float:
    """Calcula `1/2 <delta, R delta>`."""

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
    """Expoente reduzido de distinção de caminhos para detector linear.

    `zeta` mede o acoplamento de leitura do aparelho.
    `c_path` é a norma geométrica reduzida da diferença entre caminhos.
    """

    if c_path < 0:
        raise ValueError("c_path deve ser não negativo")
    r_det = dtn_massive_interval(lambda_eff, length)
    return 0.5 * zeta * zeta * c_path * r_det


def coherence_from_gamma(gamma: float) -> float:
    """Retorna o fator de coerência `exp(-gamma)`."""

    return math.exp(-gamma)


def two_path_density(
    i1: np.ndarray,
    i2: np.ndarray,
    phase: np.ndarray,
    gamma: float = 0.0,
) -> np.ndarray:
    """Densidade reduzida de duas alternativas com amortecimento de coerência."""

    i1 = np.asarray(i1, dtype=float)
    i2 = np.asarray(i2, dtype=float)
    phase = np.asarray(phase, dtype=float)
    return i1 + i2 + 2.0 * math.exp(gamma * -1.0) * np.sqrt(i1 * i2) * np.cos(phase)
