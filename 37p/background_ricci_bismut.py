"""
GDQ — Background Estacionário de Ricci-Bismut em R^4 x T^4

Resolve um modelo simplificado das equações de movimento de
Perelman-Bismut para o ansatz:

    g = -dt^2 + a(t)^2 delta_ij dx^i dx^j + sum_a R_a^2 dtheta_a^2

No setor interno, assume-se raios constantes R_a e 3-forma B com
componentes B_{abc} constantes. A equação de estacionariedade reduz-se a
um problema algébrico para (R_a, B_{abc}, f_0).

Aproximações:
- Setor R^4 plano: a(t) = 1, curvatura espacial nula.
- Toro interno plano com métrica diagonal.
- B com componentes totalmente antissimétricas no toro.
- Dilaton constante f = f_0.

A ação efetiva 8D restrita ao toro é:

    S_eff = Vol(R^4) * [R_int + (1/2)|B|^2 + (1/2)|df|^2] * e^{-f}

Para raios constantes e f constante, a estacionariedade em R_a exige:

    d/dR_a [Vol(T^4)(R_int + (1/2)|B|^2)] = 0

onde R_int é a curvatura escalar do toro (zero para toro plano) e
|B|^2 = (1/6) sum_{a<b<c} B_{abc}^2 / (R_a^2 R_b^2 R_c^2).
"""

import numpy as np
from scipy.optimize import minimize


def volume_toro(R):
    """Volume do toro T^4 com raios R = [R1, R2, R3, R4]."""
    return (2.0 * np.pi)**4 * np.prod(R)


def norm_b2(B, R):
    """
    |B|^2 para componentes B_{abc} constantes no toro.
    B é um array de 4 componentes: B_{123}, B_{124}, B_{134}, B_{234}.
    """
    indices = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    s = 0.0
    for bval, (a, b, c) in zip(B, indices):
        s += bval**2 / (R[a]**2 * R[b]**2 * R[c]**2)
    return s / 6.0


def effective_energy(R, B, kappa8, Lambda_C):
    """
    Energia efetiva por unidade de volume de R^4:

        E = Vol(T^4)/kappa_8^2 * [(1/2)|B|^2 + Lambda_C termo de estabilizacao]

    O termo Lambda_C é uma heurística para representar a contribuição do
    setor não-compacto e do potencial de estabilização.
    """
    V = volume_toro(R)
    b2 = norm_b2(B, R)
    # Termo de estabilização: penaliza raios muito grandes ou muito pequenos
    stab = Lambda_C**2 * np.sum((R - 1.0 / Lambda_C)**2)
    return V / kappa8**2 * (0.5 * b2) + stab


def find_stationary_background(kappa8=1.0, Lambda_C=1.0, B0=1.0):
    """
    Encontra raios internos R_a que minimizam a energia efetiva para B
    fixo.
    """
    # B com simetria: todas as componentes iguais a B0
    B = np.array([B0, B0, B0, B0])

    def objective(R):
        return effective_energy(R, B, kappa8, Lambda_C)

    # Chute inicial: raios da ordem do comprimento de Planck 8D
    R0 = np.ones(4) / Lambda_C

    result = minimize(objective, R0, method='Nelder-Mead',
                      options={'maxiter': 10000, 'xatol': 1e-12})

    R_star = result.x
    V_star = volume_toro(R_star)
    b2_star = norm_b2(B, R_star)

    return {
        'R_star': R_star,
        'B': B,
        'V_star': V_star,
        'b2_star': b2_star,
        'energy': result.fun,
        'success': result.success,
    }


def print_background(bg):
    print("=" * 70)
    print("BACKGROUND ESTACIONÁRIO DE RICCI-BISMUT EM R^4 x T^4")
    print("=" * 70)
    print(f"Sucesso da otimização: {bg['success']}")
    print(f"Raios internos R_a: {bg['R_star']}")
    print(f"Volume do toro: {bg['V_star']:.6e}")
    print(f"Componentes B_abc: {bg['B']}")
    print(f"|B|^2: {bg['b2_star']:.6e}")
    print(f"Energia efetiva: {bg['energy']:.6e}")
    print("=" * 70)


if __name__ == "__main__":
    # Unidades naturais: kappa8 e Lambda_C em escala de Planck 8D
    bg = find_stationary_background(kappa8=1.0, Lambda_C=1.0, B0=0.5)
    print_background(bg)
