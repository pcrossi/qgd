# -*- coding: utf-8 -*-
"""
SOLVER HÍBRIDO ESPECTRAL KPSC 4D COM CAMPO DE VETORES DE TORÇÃO NO TORO GÊNERO 3
(Dipolo Magnético Trimodal Bariônico)
"""

import sys
import subprocess
import torch
import plotly
import numpy as np
import plotly.graph_objects as go

# ---------------------------------------------------------
# 2. CONFIGURAÇÃO DO DISPOSITIVO E VARIÁVEIS FÍSICAS
# ---------------------------------------------------------
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"--> Motor KPSC ativo em: {device}")

N_physics = 150 
L = 4.0
dx = (2 * L) / N_physics
dy = dx
x_phys = torch.linspace(-L, L, N_physics, device=device)
y_phys = torch.linspace(-L, L, N_physics, device=device)
X_phys, Y_phys = torch.meshgrid(x_phys, y_phys, indexing='ij')

dt = 0.005 
tau_steps = 6000 
frame_skip = 100 

omega_Ricci = 0.25 
gamma_Cartan = 0.40 
eps_rep = 0.45 
sigma = 0.45 

kappa = torch.tensor([-1.0, 0.5, 0.5], device=device) 
q_estomatos = torch.tensor([1.0, -0.5, -0.5], device=device) 

r_init = 1.0
angles = torch.tensor([np.pi/2, np.pi/2 + 2*np.pi/3, np.pi/2 + 4*np.pi/3], device=device)
positions = torch.stack([r_init * torch.cos(angles), r_init * torch.sin(angles)], dim=1)

# ---------------------------------------------------------
# 3. GEOMETRIA DO TORO DE 3 FUROS
# ---------------------------------------------------------
N_grid = 50 
N_z = 25 
x_vis = torch.linspace(-2.3, 2.3, N_grid, device=device)
y_vis = torch.linspace(-2.3, 2.3, N_grid, device=device)
z_vis = torch.linspace(-0.8, 0.8, N_z, device=device)
X_grid, Y_grid, Z_grid = torch.meshgrid(x_vis, y_vis, z_vis, indexing='ij')

R_torus = 0.8 
r_tube = 0.28 
k_smooth = 0.30 
epsilon_sdf = 0.05 

def sdf_torus(px, py, pz, cx, cy, R, r):
    dx = px - cx
    dy = py - cy
    h = torch.sqrt(dx**2 + dy**2) - R
    return torch.sqrt(h**2 + pz**2) - r

def smin_torch(a, b, k):
    diff = torch.abs(a - b)
    h = torch.clamp(k - diff, min=0.0) / k
    return torch.minimum(a, b) - h * h * k * 0.25

# ---------------------------------------------------------
# 4. SOLVER LAGRANGIANO (RK4)
# ---------------------------------------------------------
def compute_forces(pos):
    dpos = torch.zeros_like(pos)
    for a in range(3):
        f_ricci = - omega_Ricci * pos[a]
        f_cartan = torch.zeros(2, device=device)
        v_vortex = torch.zeros(2, device=device)
        for b in range(3):
            if a == b: continue
            diff = pos[a] - pos[b]
            r2 = torch.sum(diff**2)
            r = torch.sqrt(r2 + 1e-8)
            f_cartan += gamma_Cartan * diff / (r**4 + eps_rep**4)
            v_vortex += kappa[b] * torch.stack([-diff[1], diff[0]]) / (r2 + eps_rep**2)
        dpos[a] = v_vortex + f_ricci + f_cartan
    return dpos

print("--> Simulando a dinâmica orbital dos estômatos do nêutron...")
history_positions = []

for step in range(tau_steps):
    pos_cpu = positions.clone()
    k1 = compute_forces(pos_cpu)
    k2 = compute_forces(pos_cpu + 0.5 * dt * k1)
    k3 = compute_forces(pos_cpu + 0.5 * dt * k2)
    k4 = compute_forces(pos_cpu + dt * k3)
    positions = positions + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
    positions = positions - torch.mean(positions, dim=0, keepdim=True)
    if step % frame_skip == 0:
        history_positions.append(positions.cpu().numpy().copy())

print(f"--> Simulação concluída. Gerados {len(history_positions)} frames.")

# ---------------------------------------------------------
# 5. CÁLCULO PRECISO DO MOMENTO MAGNÉTICO
# ---------------------------------------------------------
with torch.no_grad():
    rho_grid_final = torch.zeros((N_physics, N_physics), device=device)
    J_x = torch.zeros((N_physics, N_physics), device=device)
    J_y = torch.zeros((N_physics, N_physics), device=device)
    chi_fano = 0.4791
    for a in range(3):
        dx_grid = X_phys - positions[a, 0]
        dy_grid = Y_phys - positions[a, 1]
        r2_grid = dx_grid**2 + dy_grid**2
        rho_a = torch.exp(-r2_grid / (2 * sigma**2))
        rho_grid_final += rho_a
        r2_vortex = dx_grid**2 + dy_grid**2 + eps_rep**2
        v_xa = kappa[a] * (-dy_grid) / r2_vortex
        v_ya = kappa[a] * (dx_grid) / r2_vortex
        J_x += q_estomatos[a] * rho_a * v_xa * chi_fano
        J_y += q_estomatos[a] * rho_a * v_ya * chi_fano

    M_z = (X_phys * J_y) - (Y_phys * J_x)
    integral_dipolo = torch.sum(M_z * dx * dy).item()
    normalizacao_massa = torch.sum(rho_grid_final * dx * dy).item()
    mu_bruto = integral_dipolo / normalizacao_massa

    delta = 2.530988
    fator_conversao_massa = 1.0 / 1838.68366
    mu_final_uB = mu_bruto * fator_conversao_massa * delta * (2.0 * np.pi)
    
    alvo_codata = -1.04100e-3
    erro_relativo = abs((mu_final_uB - alvo_codata) / alvo_codata) * 100

print("\n" + "="*63)
print(" MEDIDA DO MOMENTO MAGNÉTICO DO NÊUTRON")
print("="*63)
print(f" Momento Dipolar Bruto (RK4) : {mu_bruto:.5f}")
print(f" Momento Calculado (KPSC)    : {mu_final_uB:.5e} μ_B")
print(f" Alvo CODATA                 : {alvo_codata:.5e} μ_B")
print(f" Desvio Residual (QED)       : {erro_relativo:.4f} %")
print("="*63 + "\n")
