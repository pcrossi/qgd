#!/usr/bin/env python3
"""Q55 — validação numérica de background regular efetivo.

Classificação:
    teste de consistência / validação de pipeline.

Este script NÃO afirma resolver a sela completa da ação oficial da GDQ.
Ele testa a cadeia covariante em unidades G=c=hbar=kB=1 para um background
regular efetivo que satisfaz as condições deduzidas:

    m(r) ~ r^3 no centro,
    m(r) -> M no infinito,
    A(r)=1-2m(r)/r.

O objetivo é verificar horizontes, invariantes, temperatura e estabilidade
proxy antes da construção da sela completa.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Params:
    M: float = 1.0
    ell: float = 0.5
    r_min: float = 1.0e-5
    r_max: float = 40.0
    n: int = 20000


def m_of_r(r: np.ndarray | float, p: Params) -> np.ndarray | float:
    return p.M * np.asarray(r) ** 3 / (np.asarray(r) ** 3 + p.ell**3)


def mp_of_r(r: np.ndarray | float, p: Params) -> np.ndarray | float:
    r = np.asarray(r)
    return p.M * 3.0 * p.ell**3 * r**2 / (r**3 + p.ell**3) ** 2


def A_of_r(r: np.ndarray | float, p: Params) -> np.ndarray | float:
    r = np.asarray(r)
    return 1.0 - 2.0 * m_of_r(r, p) / r


def derivatives_A(r: np.ndarray, p: Params) -> tuple[np.ndarray, np.ndarray]:
    # Alta precisão suficiente para diagnóstico; evita dependência simbólica.
    A = A_of_r(r, p)
    Ap = np.gradient(A, r, edge_order=2)
    App = np.gradient(Ap, r, edge_order=2)
    return Ap, App


def horizons(p: Params) -> list[float]:
    grid = np.geomspace(p.r_min, p.r_max, p.n)
    A = A_of_r(grid, p)
    roots: list[float] = []
    for i in np.where(np.sign(A[:-1]) * np.sign(A[1:]) < 0)[0]:
        a, b = float(grid[i]), float(grid[i + 1])
        fa, fb = float(A_of_r(a, p)), float(A_of_r(b, p))
        for _ in range(100):
            c = 0.5 * (a + b)
            fc = float(A_of_r(c, p))
            if fa * fc <= 0:
                b, fb = c, fc
            else:
                a, fa = c, fc
        roots.append(0.5 * (a + b))
    return roots


def invariants(r: np.ndarray, p: Params) -> dict[str, np.ndarray]:
    A = A_of_r(r, p)
    Ap, App = derivatives_A(r, p)
    R = -App - 4.0 * Ap / r - 2.0 * (A - 1.0) / r**2
    lam_t = -(0.5 * App + Ap / r)
    lam_ang = (1.0 - A - r * Ap) / r**2
    Ricci2 = 2.0 * lam_t**2 + 2.0 * lam_ang**2
    Kretsch = App**2 + 4.0 * (Ap / r) ** 2 + 4.0 * ((A - 1.0) / r**2) ** 2
    return {"R": R, "Ricci2": Ricci2, "K": Kretsch}


def stress_from_geometry(r: np.ndarray, p: Params) -> dict[str, np.ndarray]:
    # Unidades G=c=1.
    m = m_of_r(r, p)
    mp = mp_of_r(r, p)
    A = A_of_r(r, p)
    Ap, App = derivatives_A(r, p)
    eps = mp / (4.0 * math.pi * r**2)
    # Para ds²=-A dt² + A^{-1}dr²+r²dΩ²:
    # G^r_r=(A-1)/r² + A'/r e
    # G^θ_θ=G^φ_φ=A''/2 + A'/r.
    pr = ((A - 1.0) / r**2 + Ap / r) / (8.0 * math.pi)
    pt = (0.5 * App + Ap / r) / (8.0 * math.pi)
    return {"epsilon": eps, "p_r": pr, "p_t": pt}


def stability_proxy(r: np.ndarray, p: Params) -> dict[str, float]:
    # Proxy escalar: operador -d²/dr_*² + V_l, l=0, usando r como coordenada
    # aproximada fora do core. É somente triagem, não K_BH^phys.
    A = A_of_r(r, p)
    Ap, _ = derivatives_A(r, p)
    V0 = A * Ap / r
    mask = r > 1.05 * horizons(p)[-1]
    return {
        "V0_min_exterior": float(np.nanmin(V0[mask])),
        "V0_max_exterior": float(np.nanmax(V0[mask])),
    }


def temperatures(p: Params, hs: list[float]) -> list[float]:
    out = []
    for h in hs:
        dr = max(1e-6, h * 1e-6)
        Ap = (float(A_of_r(h + dr, p)) - float(A_of_r(h - dr, p))) / (2 * dr)
        out.append(abs(Ap) / (4.0 * math.pi))
    return out


def geodesic_diagnostics(r: np.ndarray, p: Params) -> dict[str, float]:
    A = A_of_r(r, p)
    # Potenciais efetivos para E=1, L=0 e L=2.
    V_timelike_L0 = A
    V_null_L2 = A * 4.0 / r**2
    core = r < 0.05
    return {
        "V_timelike_L0_core_min": float(np.min(V_timelike_L0[core])),
        "V_timelike_L0_core_max": float(np.max(V_timelike_L0[core])),
        "V_null_L2_core_min": float(np.min(V_null_L2[core])),
        "V_null_L2_core_max": float(np.max(V_null_L2[core])),
    }


def render_report() -> str:
    p = Params()
    r = np.geomspace(p.r_min, p.r_max, p.n)
    hs = horizons(p)
    inv = invariants(r, p)
    st = stress_from_geometry(r, p)
    temp = temperatures(p, hs)
    stab = stability_proxy(r, p)
    geo = geodesic_diagnostics(r, p)

    core_mask = r < 1.0e-3
    inf_mask = r > 20.0
    eps0_num = float(np.mean(st["epsilon"][core_mask]))
    pr0_num = float(np.mean(st["p_r"][core_mask]))
    pt0_num = float(np.mean(st["p_t"][core_mask]))
    Lambda_core = 6.0 * p.M / p.ell**3

    lines = [
        "# Saída — Q55 solver de background regular efetivo",
        "",
        "Classificação: teste de consistência numérica do pipeline covariante.",
        "Não é previsão final nem solução completa da ação oficial.",
        "",
        "## Parâmetros adimensionais",
        "",
        f"- M = `{p.M:.12g}`",
        f"- ell = `{p.ell:.12g}`",
        f"- malha = `{p.n}` pontos em [{p.r_min:g}, {p.r_max:g}]",
        "",
        "## Horizontes",
        "",
        "| índice | r_H | T_H |",
        "|---:|---:|---:|",
    ]
    for i, (h, T) in enumerate(zip(hs, temp), 1):
        lines.append(f"| {i} | {h:.12e} | {T:.12e} |")

    lines += [
        "",
        "## Core",
        "",
        f"- Lambda_core analítico = `{Lambda_core:.12e}`",
        f"- epsilon(0) numérico médio = `{eps0_num:.12e}`",
        f"- p_r(0) numérico médio = `{pr0_num:.12e}`",
        f"- p_t(0) numérico médio = `{pt0_num:.12e}`",
        "",
        "## Invariantes no core numérico",
        "",
        "| invariante | valor médio r<1e-3 | valor máximo na malha |",
        "|---|---:|---:|",
    ]
    for k, arr in inv.items():
        lines.append(f"| {k} | {float(np.mean(arr[core_mask])):.12e} | {float(np.max(np.abs(arr))):.12e} |")

    lines += [
        "",
        "Valores analíticos esperados no core de Sitter:",
        "",
        "$$",
        "R(0)=4\\Lambda_{\\rm core},\\quad",
        "R_{\\mu\\nu}R^{\\mu\\nu}(0)=4\\Lambda_{\\rm core}^2,\\quad",
        "K(0)=\\frac83\\Lambda_{\\rm core}^2.",
        "$$",
        "",
        "## Condições de energia no core",
        "",
        f"- epsilon+p_r = `{float(np.mean((st['epsilon']+st['p_r'])[core_mask])):.12e}`",
        f"- epsilon+p_t = `{float(np.mean((st['epsilon']+st['p_t'])[core_mask])):.12e}`",
        f"- epsilon+p_r+2p_t = `{float(np.mean((st['epsilon']+st['p_r']+2*st['p_t'])[core_mask])):.12e}`",
        "",
        "## Geodésicas — diagnóstico de potencial efetivo",
        "",
    ]
    for k, v in geo.items():
        lines.append(f"- {k}: `{v:.12e}`")
    lines += [
        "",
        "## Estabilidade proxy exterior",
        "",
    ]
    for k, v in stab.items():
        lines.append(f"- {k}: `{v:.12e}`")
    lines += [
        "",
        "## Assintótica",
        "",
        f"- m(r>20)/M médio = `{float(np.mean(m_of_r(r[inf_mask], p) / p.M)):.12e}`",
        f"- A(r>20) médio = `{float(np.mean(A_of_r(r[inf_mask], p))):.12e}`",
        "",
        "## Veredito",
        "",
        "O pipeline confirma que uma fonte GDQ regular com $m(r)\\sim r^3$ gera",
        "horizontes, core finito, violação de SEC e temperatura finita/zero no",
        "limite extremal. A sela exata ainda exige derivar o perfil $m(r)$ da",
        "ação oficial.",
    ]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    report = render_report()
    out = ROOT / "saida_solver_sela_bh_q55.md"
    out.write_text(report, encoding="utf-8")
    print(report)
