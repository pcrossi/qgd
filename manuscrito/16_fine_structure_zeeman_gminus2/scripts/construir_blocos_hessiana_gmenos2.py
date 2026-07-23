#!/usr/bin/env python3
"""
Capítulo 16 — construtor operacional de blocos H_C, c, m_perp.

Gera dois tipos de bloco:

1. líder:
   H = [[1, -1], [-1, 2*pi/alpha]]
   c = [1, 0]
   m_perp = [0, 1]

   Este bloco implementa a identidade derivada
   <c,H^+m>/<c,H^+c> = alpha/(2*pi).

2. superior_required:
   adiciona um canal transversal extra e escolhe a amplitude desse canal para
   reproduzir o resíduo observado. É diagnóstico inverso, não previsão.

O script salva os NPZs e um relatório Markdown.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np


ALPHA_INV = 137.035999177
ALPHA = 1.0 / ALPHA_INV
A1 = ALPHA / (2.0 * math.pi)
K1 = 2.0 * math.pi / ALPHA


@dataclass(frozen=True)
class Case:
    symbol: str
    name: str
    role_q39: str
    ratio_q39: float
    anomaly_obs: float | None
    source: str


CASES = [
    Case("e", "elétron", "torção primária", 1.0, 1.00115965218059 - 1.0, "Fan et al. 2022/2023"),
    Case("mu", "múon", "torção transversal/biespacial", 0.0, 116592059e-11, "Muon g-2 world average 2023"),
    Case("tau", "tau", "saturação tridimensional", 0.0, None, "sem alvo metrológico usado"),
]


def r_mu_intrinsic(alpha_inv: float = ALPHA_INV) -> float:
    alpha = 1.0 / alpha_inv
    return 1.5 * alpha_inv + 6.0 / 5.0 + 2.0 * alpha


def r_tau_from_q(r_mu: float, q: float = 2.0 / 3.0) -> float:
    a = math.sqrt(r_mu)
    A = 1.0 - q
    B = -2.0 * q * (1.0 + a)
    C = 1.0 + r_mu - q * (1.0 + a) ** 2
    disc = B * B - 4.0 * A * C
    if disc < 0.0:
        raise ValueError("sem raiz real para Q=2/3")
    y1 = (-B - math.sqrt(disc)) / (2.0 * A)
    y2 = (-B + math.sqrt(disc)) / (2.0 * A)
    return max(y1 * y1, y2 * y2)


def cases_with_ratios() -> list[Case]:
    r_mu = r_mu_intrinsic()
    return [
        CASES[0],
        Case("mu", "múon", "torção transversal/biespacial", r_mu, 116592059e-11, "Muon g-2 world average 2023"),
        Case("tau", "tau", "saturação tridimensional", r_tau_from_q(r_mu), None, "sem alvo metrológico usado"),
    ]


def evaluate(H: np.ndarray, c: np.ndarray, m_perp: np.ndarray, gamma0: float = 1.0) -> dict[str, float]:
    Hh = 0.5 * (H + H.T)
    vals, vecs = np.linalg.eigh(Hh)
    inv = 1.0 / vals
    Hinv = (vecs * inv) @ vecs.T
    den = float(c @ (Hinv @ c))
    num = float(c @ (Hinv @ m_perp))
    a = num / (den * gamma0)
    return {
        "eig_min": float(vals[0]),
        "eig_max": float(vals[-1]),
        "den": den,
        "num": num,
        "a_geom": a,
        "g_total": 2.0 * (1.0 + a),
    }


def leading_block() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    H = np.array([[1.0, -1.0], [-1.0, K1]], dtype=float)
    c = np.array([1.0, 0.0], dtype=float)
    m = np.array([0.0, 1.0], dtype=float)
    return H, c, m


def required_block(target_a: float, k2: float, j2: float = 1.0) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """Constrói bloco 3x3 e resolve a amplitude mu2 para atingir target_a."""
    H = np.array(
        [
            [1.0, -1.0, -j2],
            [-1.0, K1, 0.0],
            [-j2, 0.0, k2],
        ],
        dtype=float,
    )
    c = np.array([1.0, 0.0, 0.0], dtype=float)

    # Resposta linear em mu2: a(mu2) = a(mu2=0) + slope * mu2.
    m0 = np.array([0.0, 1.0, 0.0], dtype=float)
    m1 = np.array([0.0, 1.0, 1.0], dtype=float)
    a0 = evaluate(H, c, m0)["a_geom"]
    a1 = evaluate(H, c, m1)["a_geom"]
    slope = a1 - a0
    if abs(slope) < 1e-30:
        raise ValueError("Canal superior desacoplado: slope zero.")
    mu2 = (target_a - a0) / slope
    m = np.array([0.0, 1.0, mu2], dtype=float)
    return H, c, m, mu2


def save_npz(path: Path, H: np.ndarray, c: np.ndarray, m: np.ndarray) -> None:
    np.savez(path, H=H, c=c, m_perp=m, gamma0=np.array([1.0]))


def main() -> None:
    base = Path(__file__).resolve().parent
    cases = cases_with_ratios()

    lines: list[str] = []
    lines.append("# Capítulo 16 — saída do construtor de blocos de Hessiana")
    lines.append("")
    lines.append("## Classificação")
    lines.append("")
    lines.append("- Blocos líderes: avaliação direta da quantidade já derivada.")
    lines.append("- Blocos `required`: diagnóstico inverso do canal superior faltante.")
    lines.append("")
    lines.append("## Parâmetros")
    lines.append("")
    lines.append(f"- `alpha_inv = {ALPHA_INV:.12f}`")
    lines.append(f"- `alpha = {ALPHA:.15e}`")
    lines.append(f"- `K1 = 2*pi/alpha = {K1:.15e}`")
    lines.append(f"- `a_leader = alpha/(2*pi) = {A1:.15e}`")
    lines.append("")

    Hlead, clead, mlead = leading_block()
    lead_path = base / "hessiana_lider_gmenos2.npz"
    save_npz(lead_path, Hlead, clead, mlead)
    lead_eval = evaluate(Hlead, clead, mlead)

    lines.append("## Bloco líder universal")
    lines.append("")
    lines.append(f"- arquivo: `{lead_path.name}`")
    lines.append(f"- `a_geom = {lead_eval['a_geom']:.15e}`")
    lines.append(f"- `g_total = {lead_eval['g_total']:.15e}`")
    lines.append(f"- `eig_min = {lead_eval['eig_min']:.15e}`")
    lines.append("")

    lines.append("## Hierarquia Q39 usada para rigidez diagnóstica")
    lines.append("")
    lines.append("| caso | papel Q39 | M_l/M_e | K2 usado |")
    lines.append("|---|---|---:|---:|")
    for case in cases:
        ratio = case.ratio_q39
        # K2 positivo escalado pela rigidez de massa relativa. Isso é uma
        # escolha diagnóstica para medir a amplitude requerida; não é predição.
        k2 = K1 * max(1.0, ratio)
        lines.append(f"| {case.name} | {case.role_q39} | {ratio:.15e} | {k2:.15e} |")
    lines.append("")

    lines.append("## Blocos superiores required")
    lines.append("")
    lines.append(
        "Nestes blocos a amplitude `mu2_required` é escolhida para atingir "
        "`a_obs`. Portanto, são engenharia inversa diagnóstica."
    )
    lines.append("")
    lines.append("| caso | a_obs | residuo a_obs-a_leader | mu2_required | a_reconstruido | arquivo |")
    lines.append("|---|---:|---:|---:|---:|---|")
    for case in cases:
        if case.anomaly_obs is None:
            lines.append(f"| {case.name} | — | — | — | — | — |")
            continue
        ratio = case.ratio_q39
        k2 = K1 * max(1.0, ratio)
        H, c, m, mu2 = required_block(case.anomaly_obs, k2=k2)
        out = base / f"hessiana_required_{case.symbol}_gmenos2.npz"
        save_npz(out, H, c, m)
        ev = evaluate(H, c, m)
        lines.append(
            f"| {case.name} | {case.anomaly_obs:.15e} | "
            f"{case.anomaly_obs - A1:.15e} | {mu2:.15e} | "
            f"{ev['a_geom']:.15e} | `{out.name}` |"
        )
    lines.append("")

    lines.append("## Veredito")
    lines.append("")
    lines.append(
        r"O bloco líder constrói $H_C,c,m_\perp$ sem alvo experimental e "
        r"reproduz exatamente $\alpha/(2\pi)$."
    )
    lines.append("")
    lines.append(
        "Os blocos `required` mostram numericamente o tamanho da resposta "
        "transversal superior que falta derivar. Eles não fecham "
        r"metrologicamente $g-2$, mas transformam a pendência em uma "
        "quantidade precisa: derivar da ação oficial o canal que substituirá "
        "`mu2_required`."
    )
    lines.append("")

    report = base / "saida_blocos_hessiana_gmenos2.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
