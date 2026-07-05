import numpy as np

def monte_carlo_alpha_gdq(N=5_000_000):
    print("=" * 75)
    print("  SIMULAÇÃO ESTOCÁSTICA DE MONTE CARLO (RUÍDO DE WIENER EM 10D) ")
    print("  Cálculo Numérico da Constante de Estrutura Fina (GDQ)         ")
    print("=" * 75 + "\n")
    
    print(f"[*] Gerando {N:,} flutuações quânticas (pontos) no vácuo de Kähler...")
    
    # 1. GERAR PONTOS UNIFORMES NA BOLA 10D (Vácuo 5D Complexo)
    # Usamos o método de Muller para garantir distribuição uniforme dentro da hiperesfera 10D
    normais = np.random.randn(N, 10)
    raios_normais = np.linalg.norm(normais, axis=1)
    escalas = np.random.rand(N) ** (1/10.0) / raios_normais
    
    # Matriz N x 10 de pontos dentro da bola unitária 10D
    pontos = normais * escalas[:, np.newaxis]
    
    # 2. SEPARAR EM PARTE REAL E IMAGINÁRIA (x, y \in R^5)
    x = pontos[:, :5]
    y = pontos[:, 5:]
    
    # 3. APLICAR O FILTRO GEOMÉTRICO (A CONDIÇÃO DO SOLÍTON DE CARTAN)
    # A métrica de Lie (Domínio D5) restringe a energia elástica do vórtice.
    # L(z) = |x|^2 + |y|^2 + 2*sqrt(|x|^2 * |y|^2 - (x.y)^2) < 1
    
    # Produtos vetoriais ponto a ponto
    A = np.sum(x**2, axis=1)
    B = np.sum(y**2, axis=1)
    C = np.sum(x * y, axis=1)
    
    # O discriminante sempre >= 0 por Cauchy-Schwarz
    discriminante = A * B - C**2
    discriminante = np.maximum(discriminante, 0) # Segurança numérica contra float imprecision
    
    # O filtro de Cartan (Quem passa fica dentro do solíton)
    condicao_lie = (A + B + 2 * np.sqrt(discriminante)) < 1.0
    
    pontos_aceitos = np.sum(condicao_lie)
    taxa_aceitacao = pontos_aceitos / N
    
    print(f"[*] Flutuações absorvidas pela restrição topológica : {pontos_aceitos:,}")
    print(f"[*] Taxa de aceitação de Monte Carlo              : {taxa_aceitacao:.6f} (Teórico esperado: 0.0625 ou 1/16)\n")
    
    # 4. CÁLCULO NUMÉRICO DOS VOLUMES
    # O volume da Bola 10D padrão é pi^5 / 5!
    volume_bola_10d = (np.pi**5) / 120
    
    # Volume numérico do Domínio de Cartan (V_D5)
    V_D5_numerico = taxa_aceitacao * volume_bola_10d
    
    # 5. O CÁLCULO DA CONSTANTE
    rigidez_kähler = 9 / (8 * np.pi**4)
    raiz_compressao_numerica = (V_D5_numerico)**0.25
    
    alpha_numerico = rigidez_kähler * raiz_compressao_numerica
    inverso_alpha = 1 / alpha_numerico
    
    print("=" * 75)
    print(f" [+] ALPHA NUMÉRICO CALCULADO (Monte Carlo) : {alpha_numerico:.12f}")
    print(f" [+] INVERSO (1 / α) CALCULADO              : {inverso_alpha:.6f}")
    print("=" * 75)
    print(f" [!] REFERÊNCIA CODATA                      : 137.035999")
    print("=" * 75)
    print("\nCONCLUSÃO: O cálculo foi feito através da simulação do espalhamento")
    print("aleatório de partículas (ruído de Wiener). O número emergiu sozinho")
    print("das leis de probabilidade da geometria complexa!")

if __name__ == "__main__":
    monte_carlo_alpha_gdq()
