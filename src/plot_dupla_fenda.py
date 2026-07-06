import os
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros Físicos (unidades normalizadas)
m = 1.0       # Massa da partícula
v0 = 10.0     # Velocidade longitudinal
hbar = 1.0    # Constante de Planck reduzida
d = 1.5       # Distância entre as fendas
sigma_0 = 0.25 # Largura inicial das fendas

# Comprimento de de Broglie
lambd = (2 * np.pi * hbar) / (m * v0)

# Comprimento de Rayleigh do vácuo
y_R = (2.0 * m * v0 * sigma_0**2) / hbar


print(f"Parâmetros da Simulação:")
print(f"  - Comprimento de de Broglie (lambda): {lambd:.4f}")
print(f"  - Comprimento de Rayleigh (y_R): {y_R:.4f}")
print(f"  - Separação das fendas (d): {d:.4f}")
print(f"  - Largura da fenda (sigma_0): {sigma_0:.4f}")

# Funções analíticas
def rho_gdq(x, y):
    sigma_t = sigma_0 * np.sqrt(1 + (y / y_R)**2)
    env = (2.0 / np.sqrt(2 * np.pi * sigma_t**2)) * np.exp(-(x**2 + (d/2)**2) / (2 * sigma_t**2))
    factor = np.cosh((x * d) / (2 * sigma_t**2)) + np.cos((y * d * x) / (2 * sigma_t**2 * y_R))
    return env * factor

def rho_classical(x, y):
    sigma_t = sigma_0 * np.sqrt(1 + (y / y_R)**2)
    env = (4.0 / np.sqrt(2 * np.pi * sigma_t**2)) * np.exp(-x**2 / (2 * sigma_t**2))
    factor = np.cos((m * v0 * d * x) / (2 * hbar * y))**2
    return env * factor

# Definir malha espacial
x_vals = np.linspace(-4.0, 4.0, 1000)

# Criar a figura
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Comparação da Densidade de Probabilidade: GDQ vs. Mecânica Quântica Clássica", fontsize=14, fontweight='bold')

# 1. Campo Próximo (y = 2.0 * y_R)
y_near = 2.0 * y_R
gdq_near = rho_gdq(x_vals, y_near)
class_near = rho_classical(x_vals, y_near)

ax1.plot(x_vals, gdq_near, 'b-', label='GDQ (Exato - Perelman)', linewidth=2)
ax1.plot(x_vals, class_near, 'r--', label='MQ Clássica (Aprox. Campo Distante)', linewidth=1.5)
ax1.set_title(f"Campo Próximo ($y = 2.0\\, y_R = {y_near:.2f}$)", fontsize=12)
ax1.set_xlabel("Posição Transversal ($x$)", fontsize=11)
ax1.set_ylabel("Densidade $\\rho(x, y)$", fontsize=11)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(fontsize=10)

# 2. Campo Distante (y = 15.0 * y_R)
y_far = 15.0 * y_R
gdq_far = rho_gdq(x_vals, y_far)
class_far = rho_classical(x_vals, y_far)

ax2.plot(x_vals, gdq_far, 'b-', label='GDQ (Exato - Perelman)', linewidth=2)
ax2.plot(x_vals, class_far, 'r--', label='MQ Clássica (Aprox. Campo Distante)', linewidth=1.5)
ax2.set_title(f"Campo Distante ($y = 15.0\\, y_R = {y_far:.2f}$)", fontsize=12)
ax2.set_xlabel("Posição Transversal ($x$)", fontsize=11)
ax2.set_ylabel("Densidade $\\rho(x, y)$", fontsize=11)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(fontsize=10)

# Salvar gráfico
output_dir = 'figs'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_path = os.path.join(output_dir, 'dupla_fenda_comparacao.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Gráfico salvo com sucesso em: {output_path}")
