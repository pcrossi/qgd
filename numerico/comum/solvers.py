"""
GDQ — Biblioteca de Solvers Numéricos
Este módulo fornece invocações robustas de resolvedores de autovalores esparsos
e densos para os operadores discretizados do vácuo de Kähler.
"""

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigs

def solve_spectrum(A, k=20, sigma=0.0, return_vectors=False):
    """
    Resolve o espectro de autovalores para a matriz A.
    
    Parâmetros:
    -----------
    A : scipy.sparse.csc_matrix
        Operador linear esparso.
    k : int
        Número de autovalores desejados.
    sigma : float
        Ponto de shift para o resolvedor shift-invert.
    return_vectors : bool
        Se True, retorna também os autovetores correspondentes.
        
    Retorna:
    --------
    np.ndarray
        Autovalores ordenados (parte real).
    np.ndarray (opcional)
        Autovetores ordenados correspondentes.
    """
    if return_vectors:
        evals, evecs = eigs(A, k=k, sigma=sigma, which='LM')
        idx = np.argsort(evals.real)
        return evals[idx].real, evecs[:, idx].real
    else:
        evals = eigs(A, k=k, sigma=sigma, which='LM', return_eigenvectors=False)
        return np.sort(evals.real)
