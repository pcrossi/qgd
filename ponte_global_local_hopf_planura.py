#!/usr/bin/env python3
"""Identidades exatas da família Hopf anisotrópica compatível."""
from __future__ import annotations
import numpy as np


def contraction_eigenvalues(q,epsilon):
    return np.array([q*np.exp(epsilon),q*np.exp(-epsilon)],dtype=complex)


def determinant_ratio(q,epsilon):
    return np.prod(contraction_eigenvalues(q,epsilon))/(q*q)


def effective_coefficients():
    """Potencial estático ao longo da órbita pullback completa."""
    return {'lambda_mu':0.0,'g_mu':0.0,'C_a':0.0,'C_c':0.0,'C_u':0.0}


def action_samples(S0,epsilons):
    """Consequência da naturalidade: S[F_eps^*X]=S[X]."""
    return np.full(np.asarray(epsilons).shape,S0,dtype=float)

