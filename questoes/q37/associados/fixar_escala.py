"""
GDQ — Fixação Consistente da Escala e Predição de alpha

Nesta versão corrigida, kappa8 é tratado como parâmetro fundamental da
escala de Planck 8D. A constante de Newton 4D é uma PREDIÇÃO do modelo,
obtida pela redução dimensional:

    G_N^{pred} = kappa8^2 / Vol(T^4)

(com possível fator numérico de convenção, aqui omitido por simplicidade).

O procedimento:
1. Escolher kappa8 e Lambda_C (escala de Cartan).
2. Resolver o background estacionário.
3. Calcular Vol(T^4) e, portanto, G_N^{pred}.
4. Calcular alpha a partir de G^{ab}_*.
5. Comparar (G_N^{pred}, alpha^{-1}) com (G_N^{CODATA}, 137.036).

Isso é fisicamente mais honesto do que impor G_N para obter alpha.
"""

import numpy as np
from background_ricci_bismut import find_stationary_background
from metrica_efetiva import metrica_efetiva


# Constantes CODATA
G_N_CODATA = 6.67430e-11      # m^3 kg^-1 s^-2
hbar_SI = 1.054571817e-34     # J s
c_SI = 299792458.0            # m/s

# Massa de Planck 4D em GeV/c^2
GeV_to_J = 1.602176634e-10
M_P_kg = np.sqrt(hbar_SI * c_SI / G_N_CODATA)
M_P_GeV = M_P_kg * c_SI**2 / GeV_to_J

# G_N em unidades naturais (GeV^-2)
G_N_natural = 1.0 / M_P_GeV**2


def calcular_predicao(kappa8, Lambda_C, B0=0.5, alpha_B=0.1):
    """
    Calcula G_N predito e alpha para parâmetros fundamentais dados.
    """
    bg = find_stationary_background(kappa8=kappa8, Lambda_C=Lambda_C, B0=B0)
    Vol_T4 = bg['V_star']

    # G_N predito (unidades naturais, GeV^-2)
    G_N_pred = kappa8**2 / Vol_T4

    # Métrica efetiva
    G, G_inv = metrica_efetiva(bg, kappa8=kappa8, alpha_B=alpha_B)

    # Direção eletromagnética
    v = np.array([2.0, 0.0, 0.0, 0.0])
    g_em_inv_sq = np.dot(v, np.dot(G_inv, v))
    g_em = np.sqrt(1.0 / g_em_inv_sq)

    # alpha em unidades naturais
    alpha = g_em**2 / (4.0 * np.pi)

    return {
        'kappa8': kappa8,
        'Lambda_C': Lambda_C,
        'B0': B0,
        'alpha_B': alpha_B,
        'Vol_T4': Vol_T4,
        'G_N_pred': G_N_pred,
        'alpha': alpha,
        'alpha_inv': 1.0 / alpha,
        'g_em': g_em,
        'G11_inv': G_inv[0, 0],
    }


def print_predicao(res):
    print(f"\nkappa8 = {res['kappa8']:.6e}, Lambda_C = {res['Lambda_C']:.6f}, "
          f"B0 = {res['B0']:.6f}")
    print(f"  Vol(T^4) = {res['Vol_T4']:.6e}")
    print(f"  G_N predito = {res['G_N_pred']:.6e} GeV^-2")
    print(f"  G_N CODATA  = {G_N_natural:.6e} GeV^-2")
    print(f"  alpha = {res['alpha']:.6e}")
    print(f"  1/alpha = {res['alpha_inv']:.6f}")


if __name__ == "__main__":
    print("=" * 70)
    print("FIXAÇÃO CONSISTENTE DE ESCALA: G_N COMO PREDIÇÃO")
    print("=" * 70)
    print(f"G_N CODATA (natural) = {G_N_natural:.6e} GeV^-2")
    print(f"M_P = {M_P_GeV:.6e} GeV/c^2")

    # Exemplo 1: kappa8 = 1 (escala de Planck 8D = 1 em unidades naturais)
    print("\n" + "-" * 70)
    print("Exemplo 1: kappa8 = 1, Lambda_C = 1")
    res1 = calcular_predicao(kappa8=1.0, Lambda_C=1.0, B0=0.5, alpha_B=0.1)
    print_predicao(res1)

    # Exemplo 2: kappa8 pequeno
    print("\n" + "-" * 70)
    print("Exemplo 2: kappa8 = 1e-10, Lambda_C = 1")
    res2 = calcular_predicao(kappa8=1e-10, Lambda_C=1.0, B0=0.5, alpha_B=0.1)
    print_predicao(res2)

    # Busca de parâmetros: varrer kappa8 e Lambda_C
    print("\n" + "=" * 70)
    print("BUSCA DE REGIÃO DE PARÂMETROS")
    print("=" * 70)
    print(f"{'kappa8':>12} {'Lambda_C':>12} {'G_N_pred':>15} "
          f"{'1/alpha':>12} {'dist_GN':>12} {'dist_alpha':>12}")
    print("-" * 90)

    best = None
    kappa8_values = np.logspace(-12, 0, 25)
    Lambda_C_values = np.logspace(-2, 1, 20)

    for kappa8 in kappa8_values:
        for Lambda_C in Lambda_C_values:
            try:
                res = calcular_predicao(kappa8=kappa8, Lambda_C=Lambda_C,
                                        B0=0.5, alpha_B=0.1)
                dist_GN = abs(res['G_N_pred'] - G_N_natural) / G_N_natural
                dist_alpha = abs(res['alpha_inv'] - 137.035999) / 137.035999
                total_dist = dist_GN + dist_alpha

                if best is None or total_dist < best['total_dist']:
                    best = {
                        'res': res,
                        'dist_GN': dist_GN,
                        'dist_alpha': dist_alpha,
                        'total_dist': total_dist,
                    }

                if dist_GN < 10 and dist_alpha < 10:  # imprime candidatos razoáveis
                    print(f"{kappa8:12.6e} {Lambda_C:12.6f} "
                          f"{res['G_N_pred']:15.6e} {res['alpha_inv']:12.6f} "
                          f"{dist_GN:12.6f} {dist_alpha:12.6f}")
            except Exception as e:
                continue

    if best:
        print("\n" + "=" * 70)
        print("MELHOR CANDIDATO ENCONTRADO")
        print("=" * 70)
        print_predicao(best['res'])
        print(f"Distância relativa a G_N: {best['dist_GN']:.6f}")
        print(f"Distância relativa a 1/alpha: {best['dist_alpha']:.6f}")
    else:
        print("\nNenhum candidato razoável encontrado na grade.")
