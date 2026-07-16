#!/usr/bin/env python3
"""Álgebra do setor Beltrami toroidal constante da ponte GDQ.

O resultado é um teste exato de Maurer--Cartan e desacoplamento no background
produto. Não calcula a cohomologia do colar com uma condição de bordo ausente.
"""
from __future__ import annotations
import numpy as np


def torus_beltrami_dimension(complex_dimension: int = 2) -> int:
    """dim_C H^{0,1}(T^{1,0} T^{2m}) para um toro complexo plano."""
    return complex_dimension**2


def maurer_cartan_constant(mu: np.ndarray) -> np.ndarray:
    """MC de coeficientes constantes em frame holomorfo comutante: identicamente 0."""
    mu=np.asarray(mu, dtype=complex)
    if mu.ndim != 2 or mu.shape[0] != mu.shape[1]:
        raise ValueError('mu deve ser matriz m por m')
    return np.zeros_like(mu)


def quadratic_torsion_form_constant(mu: np.ndarray) -> np.ndarray:
    """Bloco da Hessiana torsional no setor constante produto: zero.

    d(delta omega_mu)=0 no T4 plano e mu não depende do colar; logo delta H=0.
    """
    n=np.asarray(mu).size
    return np.zeros((n,n), dtype=float)


def interface_trace_constant(mu: np.ndarray) -> tuple[np.ndarray,np.ndarray]:
    """Traço Dirichlet e momento normal: (mu,0) para módulo constante."""
    return np.asarray(mu,dtype=complex).ravel(), np.zeros(np.asarray(mu).size,dtype=complex)

