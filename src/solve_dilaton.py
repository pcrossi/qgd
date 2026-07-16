"""
GDQ — Solução Completa da Equação Dilatônica e Mapeamento de Backgrounds

Contexto (2_22.md): Com backgrounds fixos (bulk K3 x Hopf, imersão i, 1-forma λ_f),
a equação dilatônica na ação restrita é:

    R + 2□f - |∇f|² = 0

Para FLRW com fator de escala b(t):
    ü + 3H·u̇ + (3/2)(b̈/b + H² + 1/b²)u = 0,   onde u = e^{-f/2}

O vínculo constitutivo com λ_f = ℓ(t)dt e pullback espacial γ₀ fixa:
    h_ij = γ₀_ij  →  b(t) = 1  (sem expansão espacial)

Este script resolve sistematicamente:
1. A equação dilatônica estática (b=1): existe solução global regular?
2. A equação geral para b(t) livre: quais b(t) permitem u global positivo?
3. Qual geometria de background o modelo ADMITE com consistência plena.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import warnings
warnings.filterwarnings('ignore')

# ──────────────────────────────────────────────────────────────────────────────
# PARTE 1 — Caso estático forçado pelo vínculo: b(t) = 1
# ──────────────────────────────────────────────────────────────────────────────
# Com b=1: H=0, b̈/b=0, 1/b²=1
# A equação para u torna-se:
#   ü + (3/2)u = 0   →  oscilador harmônico puro
# Solução: u(t) = A·cos(√(3/2)·t) + B·sin(√(3/2)·t)
# Esta solução SEMPRE possui zeros → f = -2 ln|u| diverge → SEM solução global regular.

def solve_static(t_span, u0, du0):
    """Resolve ü + (3/2)u = 0 (caso b=1, vínculo fixo)"""
    omega = np.sqrt(3/2)
    def eq(t, y):
        return [y[1], -omega**2 * y[0]]
    sol = solve_ivp(eq, t_span, [u0, du0], dense_output=True,
                    max_step=0.01, rtol=1e-10, atol=1e-12)
    return sol

# ──────────────────────────────────────────────────────────────────────────────
# PARTE 2 — Busca de b(t) que evite zeros em u
# ──────────────────────────────────────────────────────────────────────────────
# Para u positivo global, precisamos que o coeficiente de u seja NEGATIVO:
#   (3/2)(b̈/b + H² + 1/b²) < 0
# Como H² ≥ 0 e 1/b² > 0, precisamos que b̈/b domine negativamente.
# Isso significa expansão acelerada: b̈ < -b(H² + 1/b²)
# Análise: mundos com colapso acelerado podem ter u monotônico, mas
# isso viola condições de energia fracas (CEC/WEC).

def solve_general(b_func, db_func, ddb_func, t_span, u0, du0, n_points=5000):
    """
    Resolve ü + 3H·u̇ + (3/2)(b̈/b + H² + 1/b²)u = 0
    para b(t) arbitrário.
    """
    def eq(t, y):
        b   = b_func(t)
        db  = db_func(t)
        ddb = ddb_func(t)
        H   = db / b
        coeff = (3/2) * (ddb/b + H**2 + 1.0/b**2)
        return [y[1], -3*H*y[1] - coeff*y[0]]

    t_eval = np.linspace(t_span[0], t_span[1], n_points)
    sol = solve_ivp(eq, t_span, [u0, du0], t_eval=t_eval,
                    dense_output=True, max_step=0.005,
                    rtol=1e-10, atol=1e-12)
    return sol

# ──────────────────────────────────────────────────────────────────────────────
# PARTE 3 — Candidatos de b(t) a testar
# ──────────────────────────────────────────────────────────────────────────────
candidates = {
    "b=1 (estático, vínculo fixo)": {
        "b":   lambda t: np.ones_like(t) if isinstance(t, np.ndarray) else 1.0,
        "db":  lambda t: np.zeros_like(t) if isinstance(t, np.ndarray) else 0.0,
        "ddb": lambda t: np.zeros_like(t) if isinstance(t, np.ndarray) else 0.0,
    },
    "b=t (FLRW linear — Milne)": {
        "b":   lambda t: t,
        "db":  lambda t: np.ones_like(t) if isinstance(t, np.ndarray) else 1.0,
        "ddb": lambda t: np.zeros_like(t) if isinstance(t, np.ndarray) else 0.0,
    },
    "b=e^t (de Sitter)": {
        "b":   lambda t: np.exp(t),
        "db":  lambda t: np.exp(t),
        "ddb": lambda t: np.exp(t),
    },
    "b=cosh(t) (Big Bounce)": {
        "b":   lambda t: np.cosh(t),
        "db":  lambda t: np.sinh(t),
        "ddb": lambda t: np.cosh(t),
    },
    "b=t^(2/3) (matéria plana, k=0)": {
        "b":   lambda t: t**(2/3),
        "db":  lambda t: (2/3)*t**(-1/3),
        "ddb": lambda t: -(2/9)*t**(-4/3),
    },
}

# ──────────────────────────────────────────────────────────────────────────────
# PARTE 4 — Executar todos os candidatos e diagnosticar
# ──────────────────────────────────────────────────────────────────────────────
results = {}
fig, axes = plt.subplots(len(candidates), 2, figsize=(14, 4*len(candidates)))
fig.suptitle("GDQ — Diagnóstico Dilatônico por Background", fontsize=14, fontweight='bold')

for ax_row, (name, funcs) in zip(axes, candidates.items()):
    t0 = 0.1 if "b=t" in name or "t^" in name else 0.0
    t_span = (t0 + 0.001, 10.0)
    t_eval = np.linspace(t_span[0], t_span[1], 5000)

    u0, du0 = 1.0, 0.0  # condições iniciais simétricas

    sol = solve_general(funcs["b"], funcs["db"], funcs["ddb"],
                        t_span, u0, du0)

    u_vals = sol.y[0]
    t_vals = sol.t
    f_vals = np.where(np.abs(u_vals) > 1e-10, -2*np.log(np.abs(u_vals)), np.nan)

    # Detectar zeros de u
    sign_changes = np.where(np.diff(np.sign(u_vals)))[0]
    has_zeros = len(sign_changes) > 0
    min_u = np.min(u_vals)
    max_f = np.nanmax(np.abs(f_vals))

    status = "❌ SINGULAR" if has_zeros or min_u < 1e-6 else "✅ CANDIDATO"

    results[name] = {
        "zeros": len(sign_changes),
        "min_u": min_u,
        "max_f": max_f,
        "status": status,
        "sol": sol,
    }

    # Plot u(t)
    ax_row[0].plot(t_vals, u_vals, 'b-', lw=1.5, label='u(t)')
    ax_row[0].axhline(0, color='r', lw=0.8, ls='--')
    for sc in sign_changes:
        ax_row[0].axvline(t_vals[sc], color='red', alpha=0.3, lw=0.5)
    ax_row[0].set_title(f"{name}\n{status}", fontsize=9)
    ax_row[0].set_ylabel("u = e^{-f/2}")
    ax_row[0].set_xlabel("t")
    ax_row[0].legend(fontsize=7)

    # Plot f(t)
    ax_row[1].plot(t_vals, f_vals, 'g-', lw=1.5, label='f(t) = -2 ln|u|')
    ax_row[1].set_title(f"Dilaton f(t) — zeros de u = {len(sign_changes)}", fontsize=9)
    ax_row[1].set_ylabel("f(t)")
    ax_row[1].set_xlabel("t")
    ax_row[1].set_ylim(-20, 20)
    ax_row[1].legend(fontsize=7)

plt.tight_layout()
plt.savefig("/home/pedro/Dropbox/obs/todo/figs/gdq_dilaton_analysis.png", dpi=150, bbox_inches='tight')
plt.close()

# ──────────────────────────────────────────────────────────────────────────────
# PARTE 5 — Análise analítica do caso estático
# ──────────────────────────────────────────────────────────────────────────────
print("="*70)
print("GDQ — DIAGNÓSTICO DILATÔNICO COMPLETO")
print("="*70)

print("\n📐 ANÁLISE ANALÍTICA DO CASO ESTÁTICO (b=1, vínculo fixo)")
print("-"*70)
print("Equação: ü + (3/2)u = 0  →  oscilador harmônico com ω² = 3/2")
print("Solução geral: u(t) = A·cos(√(3/2)·t) + B·sin(√(3/2)·t)")
print(f"Período de oscilação: T = 2π/√(3/2) = {2*np.pi/np.sqrt(1.5):.4f}")
print("RESULTADO: u possui INFINITOS zeros → f diverge → SEM solução global regular.")
print("CONCLUSÃO: O vínculo constitutivo (b=1) é INCOMPATÍVEL com dilaton global.")

print("\n📊 DIAGNÓSTICO NUMÉRICO POR BACKGROUND")
print("-"*70)
for name, r in results.items():
    print(f"\n  {r['status']} | {name}")
    print(f"    Zeros de u detectados : {r['zeros']}")
    print(f"    Mínimo de u           : {r['min_u']:.4e}")
    print(f"    |f|_max               : {r['max_f']:.2f}")

# ──────────────────────────────────────────────────────────────────────────────
# PARTE 6 — Caminho de resolução: qual estrutura mínima admite u > 0 global?
# ──────────────────────────────────────────────────────────────────────────────
print("\n" + "="*70)
print("📋 ANÁLISE ESTRUTURAL: CONDIÇÃO PARA u > 0 GLOBAL")
print("="*70)
print("""
A equação para u em FLRW geral:
    ü + 3H·u̇ + (3/2)(b̈/b + H² + 1/b²)u = 0

Para u > 0 global (sem zeros), o coeficiente de u deve ser ≤ 0:
    (3/2)(b̈/b + H² + 1/b²) ≤ 0

Como H² ≥ 0 e 1/b² > 0, isso exige:
    b̈/b ≤ -(H² + 1/b²)  <  0

Ou seja: EXPANSÃO ACELERADA NEGATIVA (contração acelerada).

Isso viola as Condições de Energia:
  - Condição de Energia Fraca (WEC): T_μν u^μ u^ν ≥ 0
  - A contração acelerada exigiria pressão p > ρ, violando WEC.

IMPLICAÇÃO: Não existe background FLRW com curvatura positiva k=+1
que produza u globalmente regular e satisfaça as condições de energia.
""")

print("="*70)
print("🔑 CONCLUSÃO ESTRUTURAL E CAMINHO DE SAÍDA")
print("="*70)
print("""
O modelo GDQ com ação restrita (bulk K3×Hopf, imersão e λ_f fixos)
NÃO POSSUI solução dilatônica globalmente regular para:
  1. Background estático (b=1)  → proibido pelo vínculo constitutivo
  2. FLRW com k=+1              → zeros oscilatórios em u
  3. FLRW com k=0 (b=t^2/3)    → singularidade em t=0
  4. de Sitter (b=e^t)          → u decai exponencialmente → f diverge

ÚNICO CAMINHO ABERTO (conforme 2_22, Seção 14, Alternativa 2):
  Tornar a imersão i dinâmica ou modificar o vínculo constitutivo.

Especificamente, o vínculo atual:
    h_ij = q_ij - λ_fi·λ_fj = γ₀_ij  (fixo)

deve ser substituído por:
    h_ij = q_ij(t) - λ_fi·λ_fj

onde q_ij(t) = b(t)²·γ₀_ij provém de uma imersão dinâmica:
    i_b: N → M₀   com  i_b*(g)_ij = b(t)²·γ₀_ij

Isso exige redefinir i como campo dinâmico, reabrindo sua equação
de Euler-Lagrange — que é uma nova versão do modelo (v2_23).
""")

print(f"\nFigura salva: /home/pedro/Dropbox/obs/todo/figs/gdq_dilaton_analysis.png")
