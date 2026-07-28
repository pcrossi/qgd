#!/usr/bin/env python3
"""Capítulo 16 — derivação do canal superior físico de fonte magnética.

Objetivo:
    Determinar se o primeiro canal superior pode aparecer como nova fonte
    linear direta M_perp^(2)[Phi;B] para um campo magnético uniforme.

Resultado esperado pela simetria:
    Para campo uniforme no ciclo de Noether, apenas a componente harmônica
    de Hodge acopla linearmente. Modos exatos superiores têm integral nula.
    Logo mu_{2,l}^{direto}=0.

Classificação:
    avaliação direta de regra de seleção do mapa magnético; não usa alvo
    experimental.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


BASE = Path(__file__).resolve().parent
ALPHA = 1.0 / 137.035999177
K1 = 2.0 * math.pi / ALPHA


def grid(n: int = 65536) -> tuple[np.ndarray, float]:
    theta = np.linspace(0.0, 2.0 * math.pi, n, endpoint=False)
    return theta, theta[1] - theta[0]


def inner(a: np.ndarray, b: np.ndarray, dtheta: float) -> float:
    return float(np.sum(a * b) * dtheta)


def normalized_constant_one_form(theta: np.ndarray) -> np.ndarray:
    # h=dtheta/(2pi). Representamos apenas o coeficiente angular.
    return np.ones_like(theta) / (2.0 * math.pi)


def exact_mode(theta: np.ndarray, k: int) -> np.ndarray:
    # d(sin(k theta))/(2pi) = k cos(k theta)/(2pi).
    return k * np.cos(k * theta) / (2.0 * math.pi)


def normalized_exact_mode(theta: np.ndarray, dtheta: float, k: int) -> np.ndarray:
    mode = exact_mode(theta, k)
    norm = math.sqrt(inner(mode, mode, dtheta))
    return mode / norm


def r_mu_intrinsic(alpha_inv: float = 137.035999177) -> float:
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


def stable_block_with_selection(ratio: float) -> tuple[np.ndarray, np.ndarray, np.ndarray, dict[str, float]]:
    k2 = K1 * max(1.0, ratio)

    # e0: circulação; e1: canal harmônico líder; e2: primeiro modo exato superior.
    # Regra de seleção: mu2 direto = 0 para B uniforme.
    H = np.array(
        [
            [1.0, -1.0, 0.0],
            [-1.0, K1, 0.0],
            [0.0, 0.0, k2],
        ],
        dtype=float,
    )
    c = np.array([1.0, 0.0, 0.0], dtype=float)
    m_perp = np.array([0.0, 1.0, 0.0], dtype=float)
    meta = {"mass_ratio": ratio, "K2": k2}
    return H, c, m_perp, meta


def evaluate_anomaly(H: np.ndarray, c: np.ndarray, m: np.ndarray) -> float:
    vals, vecs = np.linalg.eigh(0.5 * (H + H.T))
    Hinv = (vecs * (1.0 / vals)) @ vecs.T
    return float((c @ (Hinv @ m)) / (c @ (Hinv @ c)))


def main() -> None:
    theta, dtheta = grid()
    h = normalized_constant_one_form(theta)
    mode1 = normalized_exact_mode(theta, dtheta, 1)
    mode2 = normalized_exact_mode(theta, dtheta, 2)

    h_norm2 = inner(h, h, dtheta)
    overlap_h_mode1 = inner(h, mode1, dtheta)
    overlap_h_mode2 = inner(h, mode2, dtheta)
    overlap_mode1_mode2 = inner(mode1, mode2, dtheta)

    r_mu = r_mu_intrinsic()
    lepton_map = {
        "e": ("torção primária", 1.0),
        "mu": ("torção transversal/biespacial", r_mu),
        "tau": ("saturação tridimensional", r_tau_from_q(r_mu)),
    }
    rows = []
    for symbol, (role, ratio) in lepton_map.items():
        H, c, m, meta = stable_block_with_selection(ratio)
        a = evaluate_anomaly(H, c, m)
        out = BASE / f"background_leptonico_selecao_{symbol}_gmenos2.npz"
        np.savez(
            out,
            H=H,
            c=c,
            m_perp=m,
            gamma0=np.array([1.0]),
            hierarchy_role=np.array([role]),
            hierarchy_ratio=np.array([ratio]),
            mu2_direct=np.array([0.0]),
        )
        rows.append((symbol, role, meta["mass_ratio"], meta["K2"], 0.0, a, out.name))

    lines = [
        "# Capítulo 16 — derivação do canal superior físico",
        "",
        "## Classificação",
        "",
        "Avaliação direta da regra de seleção do mapa magnético linear. Não usa",
        "valor experimental de `g_e` nem de `g_mu-2`.",
        "",
        "## 1. Mapa magnético linear",
        "",
        "Para campo magnético uniforme no ciclo de Noether, o acoplamento linear",
        "seleciona apenas a componente harmônica de Hodge:",
        "",
        "$$",
        "M[\\Phi;B]",
        "=",
        "B\\left(\\gamma_0\\mathcal C[\\Phi]+M_\\perp[\\Phi]\\right).",
        "$$",
        "",
        r"O canal superior direto seria uma projeção de $M_\perp$ sobre modos",
        r"exatos superiores $d\sin(k\vartheta)$.",
        "",
        "## 2. Regra de seleção",
        "",
        "$$",
        "h=\\frac{d\\vartheta}{2\\pi},",
        "\\qquad",
        "e_k\\propto d\\sin(k\\vartheta).",
        "$$",
        "",
        "Como o campo uniforme é constante no ciclo,",
        "",
        "$$",
        "\\langle h,e_k\\rangle=0",
        "\\qquad",
        "(k\\ge1).",
        "$$",
        "",
        "Numericamente:",
        "",
        f"- `||h||^2 = {h_norm2:.15e}`",
        f"- `<h,e_1> = {overlap_h_mode1:.15e}`",
        f"- `<h,e_2> = {overlap_h_mode2:.15e}`",
        f"- `<e_1,e_2> = {overlap_mode1_mode2:.15e}`",
        "",
        "Portanto:",
        "",
        "$$",
        "\\boxed{\\mu_{2,\\ell}^{\\rm direto}=0.}",
        "$$",
        "",
        "## 3. Blocos estáveis com regra de seleção",
        "",
        "| lépton | papel geométrico | M_l/M_e | K2 | mu2 direto | a obtido | arquivo |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for symbol, role, ratio, k2, mu2, a, name in rows:
        lines.append(f"| {symbol} | {role} | {ratio:.15e} | {k2:.15e} | {mu2:.1f} | {a:.15e} | `{name}` |")

    lines.extend(
        [
            "",
            "## 4. Consequência",
            "",
            "O primeiro canal superior não é uma nova fonte linear direta para campo",
            "magnético uniforme. Assim, substituir os blocos `required` por uma",
            "fonte direta derivada dá `mu2=0`, não o valor metrológico observado.",
            "",
            "Logo, os resíduos superiores de `g-2` devem vir de outro elo interno:",
            "",
            "1. correção da Hessiana física `H_C=H_0+alpha H_1+...`;",
            "2. mistura Hessiana entre o canal líder e modos superiores;",
            "3. mapa eletrogeométrico interno não uniforme, se derivado do bulk;",
            "4. ou fonte de aparelho não uniforme, que não é universal.",
            "",
            "Para a anomalia universal de campo uniforme, a rota correta é a",
            "correção de Hessiana, não uma nova `mu2` direta.",
            "",
        ]
    )
    report = BASE / "saida_canal_superior_fisico_gmenos2.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
