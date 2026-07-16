"""
GDQ — Cálculo Oficial de alpha em R^4 x T^4

Este script implementa o roteiro de 37-3.md:

1. Resolve o background estacionário de Ricci-Bismut (raios internos e
   3-forma B).
2. Calcula a métrica efetiva G^{ab}_* no espaço das conexões U(1)^4.
3. Seleciona a direção eletromagnética v = (2, 0, 0, 0).
4. Calcula g_em e alpha na escala do corte UV.

IMPORTANTE: este é um modelo simplificado. Os parâmetros kappa8,
Lambda_C e B0 são livres na teoria até que a escala de Cartan seja
fixada por condições físicas adicionais. O valor numérico de alpha
obtido aqui depende dessa escolha. O objetivo é demonstrar a estrutura
da derivação, não reproduzir o CODATA por ajuste.
"""

import numpy as np
from background_ricci_bismut import find_stationary_background
from metrica_efetiva import metrica_efetiva


def calcular_alpha_oficial(kappa8=1.0, Lambda_C=1.0, B0=0.5, alpha_B=0.1,
                           hbar=1.0, c=1.0):
    """
    Calcula alpha na geometria oficial R^4 x T^4.

    Parametros:
    - kappa8: constante de acoplamento 8D (em unidades naturais)
    - Lambda_C: escala de corte de Cartan
    - B0: magnitude da 3-forma de torção
    - alpha_B: peso da correção de torção na métrica efetiva
    - hbar, c: constantes físicas (unidades naturais por padrão)

    Retorna:
    - dicionário com alpha, g_em, G11_inv, background
    """
    # 1. Background estacionário
    bg = find_stationary_background(kappa8=kappa8, Lambda_C=Lambda_C, B0=B0)

    # 2. Métrica efetiva
    G, G_inv = metrica_efetiva(bg, kappa8=kappa8, alpha_B=alpha_B)

    # 3. Direção eletromagnética
    v = np.array([2.0, 0.0, 0.0, 0.0])

    # 4. Acoplamento efetivo
    g_em_inv_sq = np.dot(v, np.dot(G_inv, v))
    g_em = np.sqrt(1.0 / g_em_inv_sq)

    # 5. Constante de estrutura fina
    alpha = g_em**2 / (4.0 * np.pi * hbar * c)

    return {
        'alpha': alpha,
        'alpha_inv': 1.0 / alpha,
        'g_em': g_em,
        'G11_inv': G_inv[0, 0],
        'bg': bg,
        'G': G,
        'G_inv': G_inv,
        'v': v,
    }


def print_resultado(res):
    print("=" * 70)
    print("CÁLCULO OFICIAL DE alpha NA GDQ (R^4 x T^4)")
    print("=" * 70)
    print(f"Raios internos R_a: {res['bg']['R_star']}")
    print(f"Volume do toro: {res['bg']['V_star']:.6e}")
    print(f"|B|^2: {res['bg']['b2_star']:.6e}")
    print(f"G^{{11}}_*: {res['G11_inv']:.6e}")
    print(f"g_em: {res['g_em']:.6e}")
    print(f"alpha: {res['alpha']:.6e}")
    print(f"1/alpha: {res['alpha_inv']:.6f}")
    print("=" * 70)


if __name__ == "__main__":
    # Execução com parâmetros de referência (unidades naturais)
    res = calcular_alpha_oficial(kappa8=1.0, Lambda_C=1.0, B0=0.5,
                                 alpha_B=0.1)
    print_resultado(res)

    # Variação de parametros para mostrar dependência
    print("\n" + "=" * 70)
    print("DEPENDÊNCIA COM PARÂMETROS (demonstração)")
    print("=" * 70)
    print(f"{'kappa8':>10} {'Lambda_C':>10} {'B0':>10} {'1/alpha':>15}")
    print("-" * 70)
    for kappa8 in [0.5, 1.0, 2.0]:
        for Lambda_C in [0.5, 1.0, 2.0]:
            for B0 in [0.1, 0.5, 1.0]:
                r = calcular_alpha_oficial(kappa8=kappa8,
                                           Lambda_C=Lambda_C,
                                           B0=B0,
                                           alpha_B=0.1)
                print(f"{kappa8:10.2f} {Lambda_C:10.2f} {B0:10.2f} "
                      f"{r['alpha_inv']:15.6f}")
