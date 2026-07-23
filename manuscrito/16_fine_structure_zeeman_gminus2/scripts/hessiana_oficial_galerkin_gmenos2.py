#!/usr/bin/env python3
"""Capítulo 16 — Hessiana oficial reduzida por Galerkin.

Este script executa os 7 passos em uma truncagem explícita da ação oficial:

1. define um background reduzido Phi_l;
2. define flutuações em g, f, fbar;
3. avalia a ação oficial com U=e^{-(f+fbar)/2};
4. calcula a Hessiana bruta por diferenças finitas;
5. define c=dC/dx para a circulação;
6. mostra que m_perp não vem da ação sem fonte/aparelho;
7. salva H,c,m_perp e extrai canais K_i,J_i,mu_i.

Classificação:
    Galerkin oficial reduzido / teste de consistência.

Não é ainda previsão metrológica de g-2, porque o mapa de fonte magnética
M[Phi;B] não é determinado pela ação sem especificar o acoplamento de aparelho.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


ALPHA = 1.0 / 137.035999177
N_COMPLEX = 4
TAU = 1.0
HBAR_OVER_LAMBDA2 = 1.0
Z_KERNEL = 1.0


def grid(n: int = 2048) -> tuple[np.ndarray, float]:
    theta = np.linspace(0.0, 2.0 * math.pi, n, endpoint=False)
    dtheta = theta[1] - theta[0]
    return theta, dtheta


def periodic_derivative(y: np.ndarray, dtheta: float) -> np.ndarray:
    return (np.roll(y, -1) - np.roll(y, 1)) / (2.0 * dtheta)


def periodic_second(y: np.ndarray, dtheta: float) -> np.ndarray:
    return (np.roll(y, -1) - 2.0 * y + np.roll(y, 1)) / (dtheta * dtheta)


def fields(x: np.ndarray, theta: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Retorna F=Re f, P=Im f e sigma métrico.

    Coordenadas de Galerkin:
        x0: circulação/fase linear no ciclo;
        x1: modo harmônico líder sin(theta);
        x2: modo fase superior sin(2 theta);
        x3: modo de densidade cos(theta);
        x4: modo métrico conformal cos(theta).
    """
    x0, x1, x2, x3, x4 = x
    F0 = 0.0
    F = F0 + x3 * np.cos(theta)
    P = (x0 * theta / (2.0 * math.pi)) + x1 * np.sin(theta) + x2 * np.sin(2.0 * theta)
    sigma = x4 * np.cos(theta)
    return F, P, sigma


def action_reduced(x: np.ndarray, n_grid: int = 2048) -> float:
    """Ação GDQ reduzida numa fatia angular periódica.

    A expressão preserva a estrutura:

        [tau(R + g^{-1} df d fbar) + (f+fbar)/2 - n] U sqrt(g).

    Usamos uma fatia conformal 2D para representar o bloco angular:
        g = exp(2 sigma), sqrt(g)=exp(2 sigma),
        R = -2 exp(-2 sigma) Delta sigma.

    Isso é um Galerkin reduzido, não o bulk 8D completo.
    """
    theta, dtheta = grid(n_grid)
    F, P, sigma = fields(x, theta)
    dF = periodic_derivative(F, dtheta)
    dP = periodic_derivative(P, dtheta)
    lap_sigma = periodic_second(sigma, dtheta)

    g_inv = np.exp(-2.0 * sigma)
    sqrt_g = np.exp(2.0 * sigma)
    ricci_scalar = -2.0 * g_inv * lap_sigma
    grad_term = g_inv * (dF * dF + dP * dP)
    rho = np.exp(-F)
    U = Z_KERNEL * rho

    L0 = TAU * (ricci_scalar + grad_term) + F - N_COMPLEX
    integrand = HBAR_OVER_LAMBDA2 * L0 * U * sqrt_g
    return float(np.sum(integrand) * dtheta)


def circulation(x: np.ndarray) -> float:
    return float(x[0])


def finite_gradient(func, x0: np.ndarray, h: float = 1e-5) -> np.ndarray:
    grad = np.zeros_like(x0, dtype=float)
    for i in range(x0.size):
        xp = x0.copy()
        xm = x0.copy()
        xp[i] += h
        xm[i] -= h
        grad[i] = (func(xp) - func(xm)) / (2.0 * h)
    return grad


def finite_hessian(func, x0: np.ndarray, h: float = 2e-4) -> np.ndarray:
    n = x0.size
    H = np.zeros((n, n), dtype=float)
    f0 = func(x0)
    for i in range(n):
        xp = x0.copy()
        xm = x0.copy()
        xp[i] += h
        xm[i] -= h
        H[i, i] = (func(xp) - 2.0 * f0 + func(xm)) / (h * h)
        for j in range(i + 1, n):
            xpp = x0.copy()
            xpm = x0.copy()
            xmp = x0.copy()
            xmm = x0.copy()
            xpp[i] += h
            xpp[j] += h
            xpm[i] += h
            xpm[j] -= h
            xmp[i] -= h
            xmp[j] += h
            xmm[i] -= h
            xmm[j] -= h
            val = (func(xpp) - func(xpm) - func(xmp) + func(xmm)) / (4.0 * h * h)
            H[i, j] = H[j, i] = val
    return 0.5 * (H + H.T)


def orthogonal_complement(e0: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    basis = []
    n = e0.size
    for k in range(n):
        v = np.zeros(n)
        v[k] = 1.0
        v = v - e0 * np.dot(e0, v)
        for b in basis:
            v = v - b * np.dot(b, v)
        norm = np.linalg.norm(v)
        if norm > tol:
            basis.append(v / norm)
    return np.column_stack(basis)


def extract_channels(H: np.ndarray, c: np.ndarray, m: np.ndarray) -> list[dict[str, float]]:
    e0 = c / np.linalg.norm(c)
    Q = orthogonal_complement(e0)
    HT = Q.T @ H @ Q
    vals, vecs_T = np.linalg.eigh(HT)
    vecs = Q @ vecs_T
    channels = []
    for idx, (eig, e) in enumerate(zip(vals, vecs.T), start=1):
        channels.append(
            {
                "idx": idx,
                "K": float(e @ (H @ e)),
                "J": float(-(e0 @ (H @ e))),
                "mu": float(e @ m),
                "eig": float(eig),
            }
        )
    return channels


def evaluate_anomaly(H: np.ndarray, c: np.ndarray, m: np.ndarray) -> float | None:
    try:
        vals, vecs = np.linalg.eigh(H)
        if np.min(np.abs(vals)) < 1e-12:
            return None
        Hinv = (vecs * (1.0 / vals)) @ vecs.T
        return float((c @ (Hinv @ m)) / (c @ (Hinv @ c)))
    except np.linalg.LinAlgError:
        return None


def main() -> None:
    base = Path(__file__).resolve().parent
    # Background com circulação unitária; os demais modos zerados.
    x_star = np.array([1.0, 0.0, 0.0, 0.0, 0.0])

    H = finite_hessian(action_reduced, x_star)
    c = finite_gradient(circulation, x_star)

    # A ação oficial sem fonte externa não contém M[Phi;B]. Portanto, a
    # fonte transversal estritamente derivada da ação nua é zero.
    m_perp_official_naked = np.zeros_like(c)

    # Fonte líder já derivada por Noether + projeção harmônica. Esta é uma
    # fonte de aparelho/contorno, não termo novo da ação fundamental.
    m_perp_leader = np.zeros_like(c)
    m_perp_leader[1] = 1.0

    np.savez(base / "hessiana_oficial_galerkin_nua_gmenos2.npz", H=H, c=c, m_perp=m_perp_official_naked, gamma0=np.array([1.0]))
    np.savez(base / "hessiana_oficial_galerkin_lider_gmenos2.npz", H=H, c=c, m_perp=m_perp_leader, gamma0=np.array([1.0]))

    channels_naked = extract_channels(H, c, m_perp_official_naked)
    channels_leader = extract_channels(H, c, m_perp_leader)
    eigvals = np.linalg.eigvalsh(H)
    a_naked = evaluate_anomaly(H, c, m_perp_official_naked)
    a_leader_raw = evaluate_anomaly(H, c, m_perp_leader)

    lines = [
        "# Capítulo 16 — Hessiana oficial Galerkin reduzida",
        "",
        "## Classificação",
        "",
        "Galerkin oficial reduzido / teste de consistência. Não é previsão metrológica.",
        "",
        "## Coordenadas",
        "",
        "| índice | modo |",
        "|---:|---|",
        "| 0 | circulação/fase linear no ciclo |",
        "| 1 | modo harmônico líder `sin(theta)` |",
        "| 2 | modo fase superior `sin(2 theta)` |",
        "| 3 | modo de densidade `cos(theta)` em `Re f` |",
        "| 4 | modo métrico conformal `cos(theta)` |",
        "",
        "## Autovalores da Hessiana bruta",
        "",
        "| i | lambda_i |",
        "|---:|---:|",
    ]
    for i, val in enumerate(eigvals):
        lines.append(f"| {i} | {val:.15e} |")

    lines.extend(
        [
            "",
            "## Vetor de circulação",
            "",
            f"`c = {np.array2string(c, precision=8)}`",
            "",
            "## Fonte transversal da ação nua",
            "",
            "A ação oficial sem fonte externa/aparelho não contém o funcional magnético `M[Phi;B]`.",
            "Portanto, no setor nu:",
            "",
            "$$",
            "m_{\\perp}^{\\rm naked}=0.",
            "$$",
            "",
            f"- `a_geom_naked = {a_naked}`",
            "",
            "### Canais extraídos com fonte nua",
            "",
            "| canal | K_i | J_i | mu_i | autovalor transversal |",
            "|---:|---:|---:|---:|---:|",
        ]
    )
    for ch in channels_naked:
        lines.append(f"| {ch['idx']} | {ch['K']:.15e} | {ch['J']:.15e} | {ch['mu']:.15e} | {ch['eig']:.15e} |")

    lines.extend(
        [
            "",
            "## Fonte líder de aparelho/contorno",
            "",
            "A fonte líder usada na Capítulo 16 vem de Noether + projeção harmônica e não é termo novo da ação fundamental.",
            "Neste teste, ela é representada pelo vetor unitário no modo 1:",
            "",
            f"`m_perp_leader = {np.array2string(m_perp_leader, precision=8)}`",
            "",
            f"- `a_geom_raw_with_leader_source = {a_leader_raw}`",
            "",
            "### Canais extraídos com fonte líder",
            "",
            "| canal | K_i | J_i | mu_i | autovalor transversal |",
            "|---:|---:|---:|---:|---:|",
        ]
    )
    for ch in channels_leader:
        lines.append(f"| {ch['idx']} | {ch['K']:.15e} | {ch['J']:.15e} | {ch['mu']:.15e} | {ch['eig']:.15e} |")

    lines.extend(
        [
            "",
            "## Veredito",
            "",
            "A segunda variação da ação oficial reduzida fornece `H` e `c`.",
            "Ela não fornece `m_perp` magnético sem especificar a fonte externa ou condição de contorno do aparelho.",
            "Assim, os coeficientes `K_i` e `J_i` podem ser extraídos da Hessiana oficial Galerkin, mas `mu_i` exige o mapa físico `M[Phi;B]`.",
            "",
            "A previsão metrológica completa de `g-2` continua dependente da construção do acoplamento magnético externo no background leptônico oficial.",
            "",
        ]
    )

    report = base / "saida_hessiana_oficial_galerkin_gmenos2.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
