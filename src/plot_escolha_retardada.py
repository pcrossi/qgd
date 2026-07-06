import os
import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# Parâmetros Físicos e Geométricos (unidades normalizadas)
# =====================================================================
m = 1.0           # Massa da partícula
v0 = 10.0         # Velocidade longitudinal
hbar = 1.0        # Constante de Planck reduzida
d = 1.5           # Separação das fendas
sigma_0 = 0.25    # Largura inicial da fenda
y_R = (2.0 * m * v0 * sigma_0**2) / hbar  # Comprimento de Rayleigh

L = 15.0 * y_R    # Distância até a tela do detector
y_escolha = 8.0 * y_R # Ponto espacial onde a escolha tardia ocorre
dy = 1.0 * y_R    # Largura da zona de transição de fase
gamma_det = 5.0   # Acoplamento de amortecimento da detecção (sigma_det * rho_det * delta_tau)

# =====================================================================
# Funções de Onda e Densidade
# =====================================================================
def get_sigmat(y):
    return sigma_0 * np.sqrt(1 + (y / y_R)**2)

def rho_components(x, y):
    """Retorna os termos independentes e o fator de fase do padrão coerente"""
    sigma_t = get_sigmat(y)
    
    # Envelopes gaussianos para cada fenda
    env1 = (1.0 / np.sqrt(2 * np.pi * sigma_t**2)) * np.exp(-(x - d/2)**2 / (2 * sigma_t**2))
    env2 = (1.0 / np.sqrt(2 * np.pi * sigma_t**2)) * np.exp(-(x + d/2)**2 / (2 * sigma_t**2))
    
    R1_sq = env1
    R2_sq = env2
    cross_term = 2.0 * np.sqrt(R1_sq * R2_sq)
    
    # Diferença de fase geométrica no vácuo de Kähler
    delta_S = (y * d * x) / (2 * sigma_t**2 * y_R)
    
    return R1_sq, R2_sq, cross_term, delta_S

def get_damping(y):
    """Calcula o amortecimento de fase contínuo via integral logística de Sudarshan"""
    # y1 representa o início pós-fenda (y1 = 0)
    y1 = 0.0
    numerator = 1.0 + np.exp((y1 - y_escolha) / dy)
    denominator = 1.0 + np.exp((y - y_escolha) / dy)
    return (numerator / denominator) ** gamma_det

def rho_delayed_choice(x, y, choice_active=False):
    """Densidade resultante com ou sem a interferência retrocausal ativa"""
    R1_sq, R2_sq, cross_term, delta_S = rho_components(x, y)
    
    if not choice_active:
        # Caso Coerente Puro (Sem Detecção de Caminho)
        return R1_sq + R2_sq + cross_term * np.cos(delta_S)
    else:
        # Caso com Escolha Retardada Ativada
        damping = get_damping(y)
        return R1_sq + R2_sq + cross_term * np.cos(delta_S) * damping

def bohm_potential(x, y, choice_active=False):
    """Calcula numericamente o Potencial Quântico de Bohm V_Bohm = -hbar^2/(2m) * d^2R/dx^2 / R"""
    dx = 0.01
    x_grid = np.array([x - dx, x, x + dx])
    
    rho_grid = rho_delayed_choice(x_grid, y, choice_active)
    R_grid = np.sqrt(np.maximum(rho_grid, 1e-10))
    
    # Segunda derivada espacial de R usando diferença centrada
    d2R = (R_grid[0] - 2 * R_grid[1] + R_grid[2]) / (dx**2)
    V_B = -(hbar**2 / (2 * m)) * d2R / R_grid[1]
    
    # Filtrar divergências numéricas extremas para fins visuais
    return np.clip(V_B, -10, 50)

# =====================================================================
# Geração dos Gráficos
# =====================================================================
x_vals = np.linspace(-4.0, 4.0, 400)
y_vals = np.linspace(0.1, L, 400)
X, Y = np.meshgrid(x_vals, y_vals)

# Computar densidades bidimensionais
Z_coherent = np.zeros_like(X)
Z_delayed = np.zeros_like(X)

for i in range(len(y_vals)):
    Z_coherent[i, :] = rho_delayed_choice(x_vals, y_vals[i], choice_active=False)
    Z_delayed[i, :] = rho_delayed_choice(x_vals, y_vals[i], choice_active=True)

# Criar a figura com subplots estruturados
fig = plt.figure(figsize=(15, 10))
fig.suptitle("Visualização Dinâmica: Escolha Retardada de Wheeler em GDQ", fontsize=16, fontweight='bold')

# 1. Mapa de Densidade 2D - Regime Coerente (Sem Escolha)
ax1 = plt.subplot(2, 2, 1)
im1 = ax1.imshow(Z_coherent, extent=[-4, 4, 0, L], origin='lower', aspect='auto', cmap='viridis')
ax1.set_title("A. Propagação Coerente (Sem Detector)\n[Interferência Preservada]", fontsize=12)
ax1.set_xlabel("Posição Transversal (x)")
ax1.set_ylabel("Distância Longitudinal (y)")
fig.colorbar(im1, ax=ax1, label='Densidade $\\rho$')

# 2. Mapa de Densidade 2D - Regime com Escolha Retardada Ativa
ax2 = plt.subplot(2, 2, 2)
im2 = ax2.imshow(Z_delayed, extent=[-4, 4, 0, L], origin='lower', aspect='auto', cmap='viridis')
# Desenhar linha indicando a posição da escolha
ax2.axhline(y_escolha, color='red', linestyle='--', linewidth=1.5, label='Tempo da Escolha ($y_{escolha}$)')
ax2.set_title("B. Escolha Retardada Ativada no Futuro\n[Fringes Dissipadas Retrocausalmente]", fontsize=12)
ax2.set_xlabel("Posição Transversal (x)")
ax2.set_ylabel("Distância Longitudinal (y)")
ax2.legend(loc='upper right')
fig.colorbar(im2, ax=ax2, label='Densidade $\\rho$')

# 3. Perfil de Densidade no Detector (y = L)
ax3 = plt.subplot(2, 2, 3)
rho_L_coherent = rho_delayed_choice(x_vals, L, choice_active=False)
rho_L_delayed = rho_delayed_choice(x_vals, L, choice_active=True)

ax3.plot(x_vals, rho_L_coherent, 'b-', label='Sem Detector (Interferência)', linewidth=2.5)
ax3.plot(x_vals, rho_L_delayed, 'r--', label='Com Detector (Balístico)', linewidth=2.5)
ax3.set_title("C. Perfil de Densidade no Anteparo ($y = L$)", fontsize=12)
ax3.set_xlabel("Posição Transversal (x)")
ax3.set_ylabel("Densidade $\\rho(x, L)$")
ax3.grid(True, linestyle=':', alpha=0.6)
ax3.legend(fontsize=10)

# 4. Potencial Quântico de Bohm no Anteparo (y = L)
ax4 = plt.subplot(2, 2, 4)
V_B_coherent = [bohm_potential(x, L, choice_active=False) for x in x_vals]
V_B_delayed = [bohm_potential(x, L, choice_active=True) for x in x_vals]

ax4.plot(x_vals, V_B_coherent, 'b-', label='Sem Detector (Barreiras de Pressão)', linewidth=2)
ax4.plot(x_vals, V_B_delayed, 'r--', label='Com Detector (Potencial Nulo)', linewidth=2)
ax4.set_title("D. Potencial Quântico de Bohm no Anteparo ($y = L$)", fontsize=12)
ax4.set_xlabel("Posição Transversal (x)")
ax4.set_ylabel("Potencial $V_{Bohm}(x, L)$")
ax4.set_ylim(-5, 45)
ax4.grid(True, linestyle=':', alpha=0.6)
ax4.legend(fontsize=10)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Salvar gráfico
output_dir = 'figs'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_path = os.path.join(output_dir, 'escolha_retardada_simulacao.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Gráfico da simulação salvo em: {output_path}")
