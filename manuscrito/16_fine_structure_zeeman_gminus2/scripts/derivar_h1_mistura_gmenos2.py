#!/usr/bin/env python3
"""Capítulo 16 — derivação reduzida de H1 por mistura geométrica de harmônicos.

Contexto:
    A fonte magnética linear superior direta é nula para campo uniforme.
    O próximo lugar onde pode surgir uma correção universal é a Hessiana:

        H_C(alpha) = H_0 + alpha H_1 + ...

    Este script calcula o primeiro termo de mistura permitido pela simetria,
    sem usar valores experimentais de g_e ou g_mu.

Ideia:
    O modo líder angular u1(theta)=cos(theta) tem energia quadrática local.
    A não-linearidade da densidade ponderada da ação oficial permite que o
    produto u1^2 contenha componente cos(2 theta), acoplando ao primeiro modo
    superior u2(theta)=cos(2 theta).

    O coeficiente geométrico adimensional é o overlap normalizado:

        beta_12 = <u2, u1^2 - <u1^2>> / sqrt(<u2,u2>) .

    O termo constante é removido porque pertence ao setor já normalizado de
    massa/volume. O sinal físico absoluto depende da terceira variação completa
    da ação oficial; aqui calculamos a magnitude e a regra de seleção.

Classificação:
    cálculo de regra de seleção e magnitude geométrica reduzida de H1; não é
    previsão metrológica completa.
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


def normed(mode: np.ndarray, dtheta: float) -> np.ndarray:
    norm = math.sqrt(inner(mode, mode, dtheta))
    return mode / norm


def evaluate(H: np.ndarray, c: np.ndarray, m: np.ndarray) -> float:
    vals, vecs = np.linalg.eigh(0.5 * (H + H.T))
    Hinv = (vecs * (1.0 / vals)) @ vecs.T
    return float((c @ (Hinv @ m)) / (c @ (Hinv @ c)))


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


def build_block(ratio: float, beta12: float, sign: float = 1.0) -> tuple[np.ndarray, np.ndarray, np.ndarray, dict[str, float]]:
    k2 = K1 * max(1.0, ratio)

    # H0: bloco líder + canal superior estável.
    H0 = np.array(
        [
            [1.0, -1.0, 0.0],
            [-1.0, K1, 0.0],
            [0.0, 0.0, k2],
        ],
        dtype=float,
    )

    # H1 reduzido: a não-linearidade do canal líder mistura e1<->e2.
    # A escala natural de rigidez é sqrt(K1*K2); alpha*H1 gera correção
    # relativa pequena, enquanto beta12 fixa só a parte geométrica angular.
    H1 = np.zeros_like(H0)
    mix = sign * beta12 * math.sqrt(K1 * k2)
    H1[1, 2] = H1[2, 1] = mix
    H = H0 + ALPHA * H1
    c = np.array([1.0, 0.0, 0.0], dtype=float)
    m = np.array([0.0, 1.0, 0.0], dtype=float)
    meta = {
        "mass_ratio": ratio,
        "K2": k2,
        "mix_H1": mix,
        "eig_min_H": float(np.linalg.eigvalsh(H)[0]),
    }
    return H, c, m, meta


def main() -> None:
    theta, dtheta = grid()
    u1 = normed(np.cos(theta), dtheta)
    u2 = normed(np.cos(2.0 * theta), dtheta)
    u3 = normed(np.cos(3.0 * theta), dtheta)

    u1_sq = u1 * u1
    u1_sq_centered = u1_sq - inner(u1_sq, np.ones_like(theta), dtheta) / (2.0 * math.pi)

    beta12 = inner(u2, u1_sq_centered, dtheta)
    beta13 = inner(u3, u1_sq_centered, dtheta)
    beta11 = inner(u1, u1_sq_centered, dtheta)

    r_mu = r_mu_intrinsic()
    lepton_map = {
        "e": ("torção primária", 1.0),
        "mu": ("torção transversal/biespacial", r_mu),
        "tau": ("saturação tridimensional", r_tau_from_q(r_mu)),
    }
    rows = []
    for symbol, (role, ratio) in lepton_map.items():
        H, c, m, meta = build_block(ratio, beta12, sign=1.0)
        a = evaluate(H, c, m)
        out = BASE / f"background_leptonico_h1mix_{symbol}_gmenos2.npz"
        np.savez(
            out,
            H=H,
            c=c,
            m_perp=m,
            gamma0=np.array([1.0]),
            hierarchy_role=np.array([role]),
            hierarchy_ratio=np.array([ratio]),
            beta12=np.array([beta12]),
            mix_H1=np.array([meta["mix_H1"]]),
        )
        rows.append((symbol, role, meta["mass_ratio"], meta["K2"], meta["mix_H1"], meta["eig_min_H"], a, out.name))

    lines = [
        r"# Capítulo 16 — derivação reduzida de $H_1$ por mistura harmônica",
        "",
        "## Classificação",
        "",
        "Cálculo de regra de seleção e magnitude geométrica reduzida para a",
        r"mistura Hessiana $H_1$. Não usa valores experimentais de $g_e$ ou",
        r"$g_\mu-2$.",
        "",
        "## 1. Mecanismo",
        "",
        "A fonte superior direta é nula para campo uniforme. A primeira correção",
        "universal possível vem da Hessiana: o produto quadrático do modo líder",
        "contém uma componente no primeiro harmônico superior.",
        "",
        "$$",
        "\\cos^2\\vartheta",
        "=",
        "\\frac12\\left(1+\\cos2\\vartheta\\right).",
        "$$",
        "",
        "Removendo o modo constante já absorvido na normalização, sobra uma",
        "componente proporcional a $\\cos2\\vartheta$.",
        "",
        "## 2. Overlaps normalizados",
        "",
        f"- `beta12 = <u2, u1^2 - mean> = {beta12:.15e}`",
        f"- `beta11 = <u1, u1^2 - mean> = {beta11:.15e}`",
        f"- `beta13 = <u3, u1^2 - mean> = {beta13:.15e}`",
        "",
        "A seleção é específica: o quadrado do modo líder acopla ao modo 2, mas",
        "não ao modo 1 nem ao modo 3 dentro da precisão numérica.",
        "",
        r"## 3. Bloco $H_C=H_0+\alpha H_1$",
        "",
        "Foi usado:",
        "",
        "$$",
        "(H_1)_{12}=(H_1)_{21}=\\beta_{12}\\sqrt{K_1K_2}.",
        "$$",
        "",
        "Esse é o termo de mistura permitido pela simetria. O sinal absoluto e",
        "eventuais fatores de terceira variação dependem da Hessiana 8D completa;",
        "aqui foi fixada a magnitude geométrica mínima.",
        "",
        "| lépton | papel geométrico | M_l/M_e | K2 | H1_mix | eig_min | a obtido | arquivo |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        symbol, role, ratio, k2, mix, eig_min, a, name = row
        lines.append(f"| {symbol} | {role} | {ratio:.15e} | {k2:.15e} | {mix:.15e} | {eig_min:.15e} | {a:.15e} | `{name}` |")

    lines.extend(
        [
            "",
            "## 4. Veredito",
            "",
            r"A rota de mistura Hessiana existe: $H_1$ não é proibido pela simetria",
            "e sua primeira magnitude angular é determinada por $\\beta_{12}$.",
            "",
            r"Porém, no bloco mínimo com $m_\perp=(0,1,0)$, essa mistura sozinha",
            r"não altera $a$ de modo metrológico, porque o canal superior ainda",
            "não possui fonte própria e não há correção diagonal/normalização",
            "derivada da terceira variação completa.",
            "",
            "Conclusão: o próximo coeficiente universal não é uma nova fonte direta",
            "e também não é fechado apenas pela mistura angular. Falta avaliar a",
            "terceira/quarta variação da ação oficial no background 8D para obter",
            r"o fator tensorial que acompanha $\beta_{12}$ e as correções",
            r"diagonais de $H_1$.",
            "",
        ]
    )
    report = BASE / "saida_h1_mistura_gmenos2.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
