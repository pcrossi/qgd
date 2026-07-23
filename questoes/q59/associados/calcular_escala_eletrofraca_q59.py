#!/usr/bin/env python3
"""Q59 — auditoria numérica da escala eletrofraca na GDQ.

Classificação:
  1. avaliação direta de fórmulas já escritas;
  2. teste de consistência dimensional/numérica;
  3. comparação fenomenológica para W/Z no cenário condicional Q29.

Nenhum alvo experimental é usado para ajustar parâmetros.
"""

from math import pi, sqrt


ALPHA_INV = 137.035999177
ALPHA = 1.0 / ALPHA_INV
M_E_GEV = 0.00051099895069
M_P_GEV = 0.93827208816

# Fórmula legada criticada em 59-0.md.
vK = (M_E_GEV / ALPHA) / sqrt(1.0 - 3.0 / (4.0 * pi**2))

# Candidato geométrico vigente em Q29/Q40: volume de Kähler bariônico.
v_baryonic = M_P_GEV * (6.0 * pi**5) / 7.0

# Valor eletrofraco operacional de referência a partir de G_F,
# usado só para comparação fenomenológica.
v_GF_ref = 246.21965

# Cenário condicional Q29: alpha_EW herdado pela resposta de superfície e
# sin^2(theta_W)=2/9 por transporte espectral operacional.
S_boundary = ALPHA * (3.0 * pi / 2.0 + 3.0 / (4.0 * pi**3))
alpha_EW = ALPHA * (1.0 + S_boundary)
sin2 = 2.0 / 9.0
cos2 = 1.0 - sin2
e = sqrt(4.0 * pi * alpha_EW)
g = e / sqrt(sin2)
gp = e / sqrt(cos2)
mW = g * v_baryonic / 2.0
mZ = v_baryonic * sqrt(g * g + gp * gp) / 2.0

PDG_MW = 80.3692
PDG_MZ = 91.1876


def rel_err(value: float, ref: float) -> float:
    return (value - ref) / ref


print("# Q59 — Auditoria da escala eletrofraca")
print()
print("## Fórmula legada")
print()
print(f"alpha_inv = {ALPHA_INV:.12f}")
print(f"M_e       = {M_E_GEV:.14f} GeV")
print(f"v_K       = {vK:.12f} GeV")
print(f"v_K       = {1000.0 * vK:.6f} MeV")
print(f"erro vs 246.21965 GeV = {100.0 * rel_err(vK, v_GF_ref):+.6f}%")
print()
print("## Candidato geométrico bariônico vigente")
print()
print("v = m_p * 6*pi^5/7")
print(f"M_p       = {M_P_GEV:.11f} GeV")
print(f"v         = {v_baryonic:.12f} GeV")
print(f"erro vs 246.21965 GeV = {100.0 * rel_err(v_baryonic, v_GF_ref):+.6f}%")
print()
print("## W/Z no cenário condicional Q29")
print()
print(f"S_boundary       = {S_boundary:.12f}")
print(f"alpha_EW_inv     = {1.0/alpha_EW:.12f}")
print(f"sin2_theta       = {sin2:.12f}")
print(f"g                = {g:.12f}")
print(f"g_prime          = {gp:.12f}")
print(f"m_W              = {mW:.12f} GeV")
print(f"m_Z              = {mZ:.12f} GeV")
print(f"erro m_W vs ref  = {100.0 * rel_err(mW, PDG_MW):+.6f}%")
print(f"erro m_Z vs ref  = {100.0 * rel_err(mZ, PDG_MZ):+.6f}%")
print()
print("## Status lógico")
print()
print("- v_K não é escala eletrofraca; é escala auxiliar/leptônica, se for reaproveitada.")
print("- v bariônico é candidato geométrico vigente, condicionado à normalização global.")
print("- W/Z dependem do transporte eletrofraco e da identidade de Schur ainda condicional.")
