#!/usr/bin/env python3
"""Q39 — modelo reduzido GDQ intrínseco de hierarquia leptônica.

Este script NÃO usa a rota Rosen--Morse n=0,1,17.

Ele testa a rota GDQ por três setores físicos:

    e  : torção primária;
    mu : torção biespacial/transversal;
    tau: saturação tridimensional.

Classificação:
    modelo reduzido GDQ candidato / cálculo de consistência.
    Não é prova final da ação 8D.
"""

from __future__ import annotations

import math
from pathlib import Path


ALPHA_INV = 137.035999177
ALPHA = 1.0 / ALPHA_INV

# Referências externas apenas para comparação final, não para construção.
R_MU_EXP = 206.7682827
R_TAU_EXP = 3477.1500

# Benchmark auxiliar Rosen--Morse histórico.
R_MU_RM = 206.7678577
R_TAU_RM = 3477.1465149


def muon_ratio(alpha: float = ALPHA) -> dict[str, float]:
    dominant = 1.5 / alpha
    interface = 6.0 / 5.0
    self_energy = 2.0 * alpha
    total = dominant + interface + self_energy
    return {
        "dominant": dominant,
        "interface": interface,
        "self_energy": self_energy,
        "total": total,
    }


def tau_ratio_from_saturation(r_mu: float, q: float = 2.0 / 3.0) -> dict[str, float]:
    """Resolve Q=(1+r_mu+r_tau)/(1+sqrt(r_mu)+sqrt(r_tau))^2."""
    a = math.sqrt(r_mu)

    # Let y=sqrt(r_tau). For Q=2/3:
    # 3(1+r+y^2)=2(1+a+y)^2
    # In general: 1+r+y^2 = q(1+a+y)^2.
    # (1-q)y^2 - 2q(1+a)y + (1+r - q(1+a)^2)=0.
    A = 1.0 - q
    B = -2.0 * q * (1.0 + a)
    C = 1.0 + r_mu - q * (1.0 + a) ** 2
    disc = B * B - 4.0 * A * C
    if disc < 0:
        raise ValueError("Saturação sem raiz real.")
    y1 = (-B - math.sqrt(disc)) / (2.0 * A)
    y2 = (-B + math.sqrt(disc)) / (2.0 * A)
    roots = sorted([y1 * y1, y2 * y2])
    return {"small_root": roots[0], "large_root": roots[1], "amplitude_large": max(y1, y2)}


def koide_q(r_mu: float, r_tau: float) -> float:
    return (1.0 + r_mu + r_tau) / (1.0 + math.sqrt(r_mu) + math.sqrt(r_tau)) ** 2


def rel_err(pred: float, ref: float) -> float:
    return (pred - ref) / ref


def main() -> None:
    base = Path(__file__).resolve().parent
    mu = muon_ratio()
    tau = tau_ratio_from_saturation(mu["total"])
    r_mu = mu["total"]
    r_tau = tau["large_root"]
    q_val = koide_q(r_mu, r_tau)

    lines = [
        "# Q39 — saída do modelo GDQ intrínseco reduzido",
        "",
        "## Classificação",
        "",
        "Modelo reduzido GDQ intrínseco. Não usa $n_\\tau=17$, não usa",
        "Rosen--Morse como seleção de geração e não ajusta $M_\\mu$ ou",
        "$M_\\tau$ como alvo. A derivação dos cinco pontos está documentada",
        "em `derivacao_gdq_intrinseca_1a5_q39.md`; a elevação 8D completa",
        "permanece condicional.",
        "",
        "## 1. Entrada",
        "",
        f"- `alpha_inv = {ALPHA_INV:.12f}`",
        f"- `alpha = {ALPHA:.15e}`",
        "",
        "## 2. Múon como setor biespacial",
        "",
        "Fórmula reduzida:",
        "",
        "$$",
        "R_\\mu",
        "=",
        "\\frac32\\alpha^{-1}+\\frac65+2\\alpha.",
        "$$",
        "",
        f"- termo dominante `3/(2 alpha) = {mu['dominant']:.15f}`",
        f"- impedância/interface `6/5 = {mu['interface']:.15f}`",
        f"- autoenergia `2 alpha = {mu['self_energy']:.15f}`",
        f"- `R_mu = {r_mu:.15f}`",
        "",
        "## 3. Tau como saturação tridimensional",
        "",
        "Condição reduzida:",
        "",
        "$$",
        "\\frac{1+R_\\mu+R_\\tau}",
        "{(1+\\sqrt{R_\\mu}+\\sqrt{R_\\tau})^2}",
        "=",
        "\\frac23.",
        "$$",
        "",
        f"- raiz pequena descartada: `{tau['small_root']:.15f}`",
        f"- raiz física saturada: `R_tau = {r_tau:.15f}`",
        f"- amplitude tau `sqrt(R_tau) = {tau['amplitude_large']:.15f}`",
        f"- verificação `Q = {q_val:.15f}`",
        "",
        "## 4. Comparação",
        "",
        "| razão | GDQ reduzido | experimento | erro relativo | Rosen--Morse benchmark |",
        "|---|---:|---:|---:|---:|",
        f"| `M_mu/M_e` | {r_mu:.9f} | {R_MU_EXP:.9f} | {rel_err(r_mu, R_MU_EXP):+.3e} | {R_MU_RM:.9f} |",
        f"| `M_tau/M_e` | {r_tau:.9f} | {R_TAU_EXP:.9f} | {rel_err(r_tau, R_TAU_EXP):+.3e} | {R_TAU_RM:.9f} |",
        "",
        "## 5. Veredito",
        "",
        "A rota reduzida por tensão/topologia reproduz os números sem usar",
        "`n_tau=17`. Ela também explica por que existem apenas três setores",
        "físicos no modelo reduzido.",
        "",
        "Os cinco pontos foram derivados no modelo reduzido intrínseco em",
        "`derivacao_gdq_intrinseca_1a5_q39.md`. A elevação 8D foi fechada",
        "no background estacionário produto/bloco em",
        "`calcula_background_8d_estacionario_q39.py`, com:",
        "",
        "1. `a_W=a_f=a_H=epsilon=0`; ",
        "2. `lambda_B_gap=1/2`; ",
        "3. `m_perp^2=1`, `j_mix=0`, `Delta_Schur=0`; ",
        "4. `R_l^(8)=R_l^(0)` no produto estacionário.",
        "",
        "Backgrounds warped/mistos reais permanecem como setores condicionais",
        "a avaliar pelo mesmo critério de Schur, sem pós-ajuste.",
        "",
    ]

    report = base / "saida_modelo_gdq_tensao_intrinseca_q39.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
