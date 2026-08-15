#!/usr/bin/env python3
"""Reusable reduced blocks for GDQ calculations.

Classification:
    methodological library / effective reduction.

This module does not implement the full official GDQ action. It gathers
algebraic blocks that appear after the chain:

    official action -> background -> constraints -> physical projector
    -> physical Hessian -> internal degrees elimination.

The blocks implemented here are useful for verifications, prototypes, and
reduced applications:

    - DtN of a massive interval;
    - Schur complement;
    - quadratic response;
    - detector coherence factor;
    - two-alternative density.

Any metrological use must declare where the apparatus, domain, and boundary
parameters came from.
"""

from __future__ import annotations

import math

import numpy as np


def coth(x: float) -> float:
    """Returns the hyperbolic cotangent of a non-zero real argument."""

    if abs(x) < 1.0e-12:
        raise ValueError("coth(x) requires |x| > 0")
    return math.cosh(x) / math.sinh(x)


def dtn_massive_interval(lambda_eff: float, length: float) -> float:
    """DtN operator of `-d_s^2 + lambda_eff^2` on `[0, length]`.

    Boundary conditions:
        varphi(0) = varphi_0;
        varphi(length) = 0.

    The internal solution yields:
        R = lambda_eff * coth(lambda_eff * length).
    """

    if lambda_eff <= 0:
        raise ValueError("lambda_eff must be positive")
    if length <= 0:
        raise ValueError("length must be positive")
    return lambda_eff * coth(lambda_eff * length)


def schur_complement(
    k_boundary_boundary: np.ndarray,
    k_boundary_internal: np.ndarray,
    k_internal_boundary: np.ndarray,
    k_internal_internal: np.ndarray,
) -> np.ndarray:
    """Eliminates internal degrees of freedom via Schur complement.

    Returns:
        K_bb - K_bi K_ii^{-1} K_ib.
    """

    return k_boundary_boundary - k_boundary_internal @ np.linalg.solve(
        k_internal_internal,
        k_internal_boundary,
    )


def quadratic_response(delta_boundary: np.ndarray, impedance: np.ndarray | float) -> float:
    """Calculates `1/2 <delta, R delta>`."""

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
    """Reduced path distinction exponent for a linear detector.

    `zeta` measures the readout coupling of the apparatus.
    `c_path` is the reduced geometric norm of the difference between paths.
    """

    if c_path < 0:
        raise ValueError("c_path must be non-negative")
    r_det = dtn_massive_interval(lambda_eff, length)
    return 0.5 * zeta * zeta * c_path * r_det


def coherence_from_gamma(gamma: float) -> float:
    """Returns the coherence factor `exp(-gamma)`."""

    return math.exp(-gamma)


def two_path_density(
    i1: np.ndarray,
    i2: np.ndarray,
    phase: np.ndarray,
    gamma: float = 0.0,
) -> np.ndarray:
    """Reduced two-alternative density with coherence damping."""

    i1 = np.asarray(i1, dtype=float)
    i2 = np.asarray(i2, dtype=float)
    phase = np.asarray(phase, dtype=float)
    return i1 + i2 + 2.0 * math.exp(gamma * -1.0) * np.sqrt(i1 * i2) * np.cos(phase)
