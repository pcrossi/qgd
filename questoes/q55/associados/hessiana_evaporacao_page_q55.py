#!/usr/bin/env python3
"""Q55 — Hessiana proxy, evaporação e Page curve toy.

Classificação:
    teste de consistência / infraestrutura numérica.

Não substitui K_BH^phys completo. O objetivo é validar o formato de cálculo:
background -> operador -> espectro -> temperatura -> curva informacional.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np

from solver_sela_bh_q55 import Params, A_of_r, horizons, temperatures

ROOT = Path(__file__).resolve().parent


def finite_difference_spectrum(p: Params, n: int = 600) -> tuple[np.ndarray, np.ndarray]:
    hs = horizons(p)
    r0 = hs[-1] * 1.05
    r1 = 30.0
    r = np.linspace(r0, r1, n)
    h = r[1] - r[0]
    A = A_of_r(r, p)
    Ap = np.gradient(A, r, edge_order=2)
    V = np.maximum(A * Ap / r, 0.0)
    diag = 2.0 / h**2 + V[1:-1]
    off = -np.ones(n - 3) / h**2
    K = np.diag(diag) + np.diag(off, 1) + np.diag(off, -1)
    vals = np.linalg.eigvalsh(K)
    return r, vals[:12]


def evaporation_track(p: Params) -> dict[str, np.ndarray]:
    # Família regular efetiva M variável, ell fixo.
    masses = np.linspace(1.2, 0.2, 80)
    temps = []
    outer = []
    for M in masses:
        pp = Params(M=float(M), ell=p.ell, n=8000)
        hs = horizons(pp)
        if hs:
            outer.append(hs[-1])
            temps.append(temperatures(pp, hs)[-1])
        else:
            outer.append(np.nan)
            temps.append(0.0)
    return {"M": masses, "T": np.array(temps), "r_plus": np.array(outer)}


def page_curve_toy(track: dict[str, np.ndarray]) -> tuple[np.ndarray, np.ndarray]:
    # Toy unitário: entropia cresce até metade da evaporação e decai.
    u = np.linspace(0.0, 1.0, len(track["M"]))
    S = np.where(u <= 0.5, 2.0 * u, 2.0 * (1.0 - u))
    # Modula por temperatura normalizada para indicar congelamento em remanescente.
    T = track["T"]
    if np.nanmax(T) > 0:
        S *= np.nan_to_num(T / np.nanmax(T), nan=0.0) ** 0.15
    return u, S


def render_report() -> str:
    p = Params()
    r, eig = finite_difference_spectrum(p)
    track = evaporation_track(p)
    u, S = page_curve_toy(track)
    hs = horizons(p)
    Ts = temperatures(p, hs)

    lines = [
        "# Saída — Q55 Hessiana proxy, evaporação e Page curve",
        "",
        "Classificação: infraestrutura/consistência numérica. Não é a Hessiana",
        "física completa da ação oficial.",
        "",
        "## Espectro proxy exterior",
        "",
        "| modo | lambda |",
        "|---:|---:|",
    ]
    for i, v in enumerate(eig):
        lines.append(f"| {i} | {v:.12e} |")
    lines += [
        "",
        f"- menor autovalor proxy: `{eig[0]:.12e}`",
        f"- autovalores negativos proxy: `{int(np.sum(eig < -1e-10))}`",
        "",
        "## Temperatura do background M=1",
        "",
        "| horizonte | r_H | T_H |",
        "|---:|---:|---:|",
    ]
    for i, (h, T) in enumerate(zip(hs, Ts), 1):
        lines.append(f"| {i} | {h:.12e} | {T:.12e} |")
    lines += [
        "",
        "## Evaporação efetiva por família M variável",
        "",
        f"- temperatura máxima na trilha: `{float(np.nanmax(track['T'])):.12e}`",
        f"- primeira massa sem horizonte na trilha: `{next((float(m) for m,t in zip(track['M'], track['T']) if t == 0.0), float('nan')):.12e}`",
        "",
        "## Page curve toy",
        "",
        f"- S_out inicial = `{S[0]:.12e}`",
        f"- S_out máximo = `{float(np.max(S)):.12e}`",
        f"- S_out final = `{S[-1]:.12e}`",
        "",
        "## Veredito",
        "",
        "A infraestrutura espectral/evaporativa roda e produz um comportamento",
        "compatível com remanescente: temperatura cai a zero quando não há horizonte",
        "na família efetiva. A Page curve aqui é apenas toy unitário; a curva física",
        "exige os modos de saída de $K_{BH}^{phys}$ e o canal de informação GDQ.",
    ]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    report = render_report()
    out = ROOT / "saida_hessiana_evaporacao_page_q55.md"
    out.write_text(report, encoding="utf-8")
    print(report)

