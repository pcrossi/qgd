"""
GDQ — Biblioteca de Operadores Diferenciais Discretizados
Este módulo implementa a discretização de operadores diferenciais de segunda ordem
com termos de primeira derivada por Diferenças Finitas.
O operador geral resolvido é da forma:
    H psi = - psi'' + P(x) psi' + Q(x) psi
Com condições de contorno de Robin:
    psi'(x_L) = c_L psi(x_L)
    psi'(x_R) = c_R psi(x_R)
"""

import numpy as np
import scipy.sparse as sp

def build_1d_operator(x, P_func, Q_func, c_L, c_R):
    """
    Constrói a matriz do operador H discretizada por diferenças finitas centrais.
    
    Parâmetros:
    -----------
    x : np.ndarray
        Malha unidimensional de coordenadas.
    P_func : callable
        Função que retorna P(x) (coeficiente da primeira derivada).
    Q_func : callable
        Função que retorna Q(x) (potencial / termo de diagonal).
    c_L : float
        Coeficiente de Robin no contorno esquerdo: psi'(x_L) = c_L psi(x_L).
    c_R : float
        Coeficiente de Robin no contorno direito: psi'(x_R) = c_R psi(x_R).
        
    Retorna:
    --------
    scipy.sparse.csc_matrix
        Operador discretizado no formato CSC.
    """
    N = len(x)
    h = x[1] - x[0]
    
    # Avaliação dos coeficientes nas malhas correspondentes
    P = P_func(x)
    Q = Q_func(x)
    
    # Diagonais internas
    main_diag = 2.0 / h**2 + Q
    lower_diag = -1.0 / h**2 - P[1:] / (2.0 * h)
    upper_diag = -1.0 / h**2 + P[:-1] / (2.0 * h)
    
    # Aplicação das condições de contorno de Robin via diferença central fictícia
    # Bordo Esquerdo (i=0):
    # psi_{-1} = psi_1 - 2*h*c_L*psi_0
    # Substituindo na equação de i=0:
    # A[0,0] = 2/h**2 + 2*c_L/h + c_L*P[0] + Q[0]
    # A[0,1] = -2/h**2
    main_diag[0] = 2.0 / h**2 + 2.0 * c_L / h + c_L * P[0] + Q[0]
    upper_diag[0] = -2.0 / h**2
    
    # Bordo Direito (i=N-1):
    # psi_{N} = psi_{N-2} + 2*h*c_R*psi_{N-1}
    # Substituindo na equação de i=N-1:
    # A[-1,-2] = -2/h**2
    # A[-1,-1] = 2/h**2 - 2*c_R/h + c_R*P[-1] + Q[-1]
    main_diag[-1] = 2.0 / h**2 - 2.0 * c_R / h + c_R * P[-1] + Q[-1]
    lower_diag[-1] = -2.0 / h**2
    
    # Montagem da matriz tridiagonal esparsa
    A = sp.diags([lower_diag, main_diag, upper_diag], [-1, 0, 1], shape=(N, N), format='csc')
    return A
