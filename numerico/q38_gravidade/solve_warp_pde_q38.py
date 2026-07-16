import numpy as np
import scipy.integrate as spi
import scipy.sparse as sp
import matplotlib.pyplot as plt
import os

# Parametros fisicos e da rede
N = 100       # Numero de pontos radiais
r_min = 0.5  # Corte UV maior para evitar divergencia imediata
r_max = 5.0   # Corte IR (bulk)
r = np.linspace(r_min, r_max, N)
dr = (r_max - r_min) / (N - 1)

# Constante de torcao (reduzida para suavizar o fluxo)
k = 0.1

# Operadores de diferencas finitas (D1 e D2)
# D1: diferenca central para 1a derivada
diags_1 = [-1, 1]
D1 = sp.diags([-1, 1], [-1, 1], shape=(N, N)).toarray() / (2 * dr)
# Fronteiras (forward/backward)
D1[0, 0:3] = np.array([-3, 4, -1]) / (2 * dr)
D1[-1, -3:] = np.array([1, -4, 3]) / (2 * dr)

# D2: diferenca central para 2a derivada
D2 = sp.diags([1.0, -2.0, 1.0], [-1, 0, 1], shape=(N, N)).toarray() / (dr**2)
D2[0, 0:4] = np.array([2, -5, 4, -1]) / (dr**2)
D2[-1, -4:] = np.array([-1, 4, -5, 2]) / (dr**2)

# Condicoes Iniciais (Background estacionário / aproximado)
A0 = np.zeros(N)
# R0 = r na vizinhança da origem para evitar singularidade cônica
R0 = r_min + r 
L0 = np.ones(N) * 1.0

Y0 = np.concatenate([A0, R0, L0])

def pde_system(t, Y):
    A = Y[0:N]
    R = Y[N:2*N]
    L = Y[2*N:3*N]
    
    # Derivadas espaciais
    Ap = D1 @ A
    App = D2 @ A
    Rp = D1 @ R
    Rpp = D2 @ R
    Lp = D1 @ L
    Lpp = D2 @ L
    
    # Equacoes do fluxo de Ricci-Bismut radiais para a metrica
    # d_tau A = A'' + 4(A')^2 + 3A'(R'/R) + A'(L'/L)
    dA_dt = App + 4 * Ap**2 + 3 * Ap * (Rp / R) + Ap * (Lp / L)
    
    # d_tau R = R'' + 2/R - 2(R')^2/R + 4 A' R' + (R' L')/L - 2k^2/R^5
    dR_dt = Rpp + 2/R - 2 * (Rp**2)/R + 4 * Ap * Rp + (Rp * Lp)/L - 2 * k**2 / R**5
    
    # d_tau L = L'' + 4 A' L' + 3 (R'/R) L'
    dL_dt = Lpp + 4 * Ap * Lp + 3 * (Rp / R) * Lp
    
    # Condicoes de contorno em r_max (Dirichlet ou Neumann)
    # Fixar as assintotas no bulk (assintoticamente plano)
    dA_dt[-1] = 0  # A(r_max) = 0
    dR_dt[-1] = 0  # R(r_max) fixo
    dL_dt[-1] = 0  # L(r_max) fixo
    
    # Condicoes de contorno no estomato (r_min)
    # Deixar evoluir livremente de acordo com a EDO
    
    return np.concatenate([dA_dt, dR_dt, dL_dt])

# Resolver o sistema
print("Resolvendo as EDPs do fluxo de Ricci-Bismut (Method of Lines)...")
tau_span = (0, 0.5)  # Integrar ate proximo do colapso
tau_eval = np.linspace(tau_span[0], tau_span[1], 100)

sol = spi.solve_ivp(pde_system, tau_span, Y0, t_eval=tau_eval, method='Radau', rtol=1e-5, atol=1e-7)

if sol.success:
    print("Solucao alcancada com sucesso!")
else:
    print(f"Falha na integracao (Colapso): {sol.message}")

# Extrair estados no ultimo tempo (seja falha ou sucesso)
A_final = sol.y[0:N, -1]
R_final = sol.y[N:2*N, -1]
tau_final = sol.t[-1]
    
print(f"Tempo maximo alcancado (tau_*): {tau_final:.6f}")
print(f"Raio minimo atingido: {np.min(R_final):.4f}")
print(f"Warp fator (e^2A) maximo atingido no estomato: {np.exp(2*A_final[0]):.4f}")

# Plotar e salvar a figura
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(r, R_final, label=f'R(r, tau={tau_final:.3f})')
plt.plot(r, R0, '--', label='R(r, 0)')
plt.title('Raio Interno $R(r)$')
plt.xlabel('r (Colar)')
plt.ylabel('R')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(r, np.exp(2*A_final), color='red', label=f'e^{{2A}}(r, tau={tau_final:.3f})')
plt.plot(r, np.exp(2*A0), '--', color='gray', label='e^{2A}(r, 0)')
plt.title('Fator de Warp $e^{2A}(r)$')
plt.xlabel('r (Colar)')
plt.ylabel('$e^{2A}$')
plt.legend()
plt.tight_layout()
plt.savefig('warp_collapse_profile.png')
print("Grafico salvo em warp_collapse_profile.png")

# Gerar relatorio em markdown com os resultados
with open('relatorio_solve_warp_q38.md', 'w') as f:
    f.write("# Relatório: Solução Numérica do Fator de Warp (EDPs Radiais)\n\n")
    f.write("As equações diferenciais parciais acopladas para o fator de warp $A(r, \\tau)$, $R(r, \\tau)$ e $L(r, \\tau)$ foram integradas no colar do estômato.\n")
    if sol.success:
        f.write(f"- Raio mínimo do colapso alcançado: {np.min(R_final):.6f}\n")
        f.write(f"- Ponto de ramificação/divergência do fator $e^{{2A}}$ no estômato: {np.exp(2*A_final[0]):.6f}\n")
    else:
        f.write(f"A integração encontrou uma singularidade em tempo finito $\\tau_* \approx {tau_final:.6f}$.\n")
        f.write(f"- Raio $R$ no momento do colapso (em $r=r_{{min}}$): {R_final[0]:.6e}\n")
        f.write(f"- Fator de warp $e^{{2A}}$ no momento do colapso (em $r=r_{{min}}$): {np.exp(2*A_final[0]):.6e}\n")
