r"""
GDQ — Solver Geométrico da Escala Eletrofraca e Massas Bosônicas (Q28, Q29)
[Versão Rigorosa - Zero Mecanismo de Higgs Fenomenológico]

Deriva a escala Eletrofraca v = 246 GeV e a Constante de Fermi (G_F)
puramente através da razão geométrica do Volume de Kähler sobre as
7 dimensões compactificadas transversais da GDQ.
"""

import numpy as np

def run_simulation():
    print("=" * 90)
    print("   GEOMETRODINÂMICA QUÂNTICA — SOLVER DA ESCALA ELETROFRACA (Q28, Q29)")
    print("=" * 90)

    # 1. PARÂMETROS GEOMÉTRICOS FUNDAMENTAIS
    pi = np.pi
    V_K = 6.0 * (pi**5) # Volume de Kähler do Sóliton Bariônico (~1836.118)
    dim_transversal = 7.0 # Dimensionalidade do sub-espaço S^3 x T^4 projetado
    
    # 2. MASSA BASE E DERIVAÇÃO DA ESCALA ELETROFRACA (v)
    m_p_codata = 0.93827208816 # GeV (Massa do Próton, escala fundamental da GDQ)
    
    # Derivação: A escala Eletrofraca é a projeção geométrica amplificada do próton.
    v_GDQ = m_p_codata * (V_K / dim_transversal)
    
    # 3. DERIVAÇÃO DA CONSTANTE DE FERMI (G_F)
    # G_F = 1 / (\sqrt{2} * v^2)
    G_F_GDQ = 1.0 / (np.sqrt(2.0) * (v_GDQ**2))
    
    # 4. ÂNGULO DE WEINBERG GEOMÉTRICO E ACOPLAMENTOS
    # O ângulo de mistura fraca é deduzido da partição U(1) em U(3) = 2/9
    sin2_theta_W_GDQ = 2.0 / 9.0
    sin_theta_W = np.sqrt(sin2_theta_W_GDQ)
    cos_theta_W = np.sqrt(1.0 - sin2_theta_W_GDQ)
    
    # Na escala do bóson Z, a constante fina runned do Modelo Padrão é ~ 1/128
    alpha_MZ = 1.0 / 128.0
    e_MZ = np.sqrt(4.0 * pi * alpha_MZ)
    
    g_GDQ = e_MZ / sin_theta_W
    g_prime_GDQ = e_MZ / cos_theta_W
    
    # 5. MASSAS ARBÓREAS DOS BÓSONS W E Z
    M_W_GDQ = (g_GDQ * v_GDQ) / 2.0
    M_Z_GDQ = (v_GDQ / 2.0) * np.sqrt(g_GDQ**2 + g_prime_GDQ**2)

    # DADOS EXPERIMENTAIS (CODATA / PDG) PARA COMPARAÇÃO
    v_codata = 246.21965
    G_F_codata = 1.1663787e-5
    sin2_theta_W_codata = 0.2223
    M_W_codata = 80.379
    M_Z_codata = 91.1876

    # CÁLCULO DE ERROS (%)
    err_v = abs(v_GDQ - v_codata) / v_codata * 100
    err_GF = abs(G_F_GDQ - G_F_codata) / G_F_codata * 100
    err_sin2 = abs(sin2_theta_W_GDQ - sin2_theta_W_codata) / sin2_theta_W_codata * 100
    err_MW = abs(M_W_GDQ - M_W_codata) / M_W_codata * 100
    err_MZ = abs(M_Z_GDQ - M_Z_codata) / M_Z_codata * 100

    print("\n[ Tabela Comparativa: Geometria GDQ vs Experimento (PDG) ]")
    print("-" * 90)
    print(f"{'Observável Físico':<30} | {'Predição Pura GDQ':<20} | {'Valor Experimental':<20} | {'Desvio (%)':<10}")
    print("-" * 90)
    print(f"{'Escala do Vácuo EW (v)':<30} | {v_GDQ:>15.4f} GeV | {v_codata:>15.4f} GeV | {err_v:>8.4f}%")
    print(f"{'Constante de Fermi (G_F)':<30} | {G_F_GDQ:>15.4e} GeV^-2| {G_F_codata:>15.4e} GeV^-2| {err_GF:>8.4f}%")
    print(f"{'Ângulo de Weinberg (sin^2)':<30} | {sin2_theta_W_GDQ:>15.4f}      | {sin2_theta_W_codata:>15.4f}      | {err_sin2:>8.4f}%")
    print(f"{'Massa Bóson W (Tree-level)':<30} | {M_W_GDQ:>15.4f} GeV | {M_W_codata:>15.4f} GeV | {err_MW:>8.4f}% *")
    print(f"{'Massa Bóson Z (Tree-level)':<30} | {M_Z_GDQ:>15.4f} GeV | {M_Z_codata:>15.4f} GeV | {err_MZ:>8.4f}% *")
    print("-" * 90)
    
    print("\n(*) Nota: Na Física Clássica de Partículas, as massas M_W e M_Z de Nível-Árvore (Tree-level)")
    print("    sempre apresentam desvio natural de ~1-2% da realidade devido à ausência das Correções")
    print("    Radiativas Quanticas de Loop (Delta r). A proeza fenomenal aqui é a Escala do Vácuo (v)")
    print("    e G_F baterem perfeitamente a barreira < 0.1% sem uso de Campo de Higgs fundamental.")

if __name__ == "__main__":
    run_simulation()
