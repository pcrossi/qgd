"""
GDQ — Métrica Efetiva G^{ab}_* no Espaço das Conexões U(1)^4

A partir do background estacionário (R_a, B_abc), calcula a métrica
efetiva no espaço das conexões de gauge abelianas.

Aproximação:
- O termo cinético das conexões reduzidas vem da redução dimensional da
  ação 8D.
- A contribuição dominante é geométrica:

      G_{ab} = Vol(T^4) / kappa_8^2 * g^{int}_{ab}

  onde g^{int}_{ab} = delta_{ab} / R_a^2 é a métrica induzida no espaço
  das 1-formas de conexão (normalização dos ângulos theta_a).
- Correções de Bismut são incluídas como termos adicionais proporcionais
  a |B|^2.
"""

import numpy as np
from background_ricci_bismut import find_stationary_background


def metrica_efetiva(bg, kappa8=1.0, alpha_B=0.1):
    """
    Calcula G_{ab} e sua inversa G^{ab}.

    Parametros:
    - bg: dicionário com background estacionário
    - kappa8: constante de acoplamento 8D
    - alpha_B: peso da correção de torção
    """
    R = bg['R_star']
    V = bg['V_star']
    b2 = bg['b2_star']

    # Métrica geométrica dominante: diagonal em bases ortonormais
    G = np.diag(1.0 / R**2)

    # Fator volumétrico e correção de torção
    factor = V / kappa8**2
    G = factor * (G + alpha_B * b2 * np.eye(4))

    # Inversa
    G_inv = np.linalg.inv(G)

    return G, G_inv


def verificar_positividade(G):
    """Verifica se G é positiva definida."""
    eigvals = np.linalg.eigvalsh(G)
    return np.all(eigvals > 0), eigvals


if __name__ == "__main__":
    bg = find_stationary_background(kappa8=1.0, Lambda_C=1.0, B0=0.5)

    G, G_inv = metrica_efetiva(bg, kappa8=1.0, alpha_B=0.1)
    pos, eigvals = verificar_positividade(G)

    print("=" * 70)
    print("MÉTRICA EFETIVA G_{ab} NO ESPAÇO DAS CONEXÕES")
    print("=" * 70)
    print("G_{ab}:")
    print(G)
    print("\nAutovalores de G_{ab}:")
    print(eigvals)
    print(f"\nG_{{ab}} é positiva definida? {pos}")
    print("\nG^{ab}:")
    print(G_inv)
    print("\nG^{11}:")
    print(G_inv[0, 0])
    print("=" * 70)
