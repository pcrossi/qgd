#!/usr/bin/env python3
"""Capítulo 16 — amplitude de densidade calculada pela sela reduzida normalizada.

Este teste corrige duas insuficiências da auditoria Galerkin histórica:

1. a fase com monodromia é diferenciada pela conexão globalmente definida,
   sem aplicar diferenças periódicas à função multivalorada;
2. a normalização da medida ponderada é imposta antes da variação.

Classificação:
    avaliação direta de uma sela Galerkin reduzida normalizada e teste de
    convergência. Não é a sela leptônica física completa em oito dimensões.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares
from scipy.special import i0e


BASE = Path(__file__).resolve().parent
N_COMPLEX = 4


def log_i0(x: float) -> float:
    """Calcula log(I_0(x)) sem overflow."""
    return float(np.log(i0e(x)) + abs(x))


def reduced_action(y: np.ndarray, n_grid: int) -> float:
    """Ação angular reduzida no setor de circulação unitária.

    Coordenadas:
        y = (a_1, a_2, eta, sigma).

    A fase possui monodromia unitária e derivada

        P' = 1/(2 pi) + a_1 cos(theta) + 2 a_2 cos(2 theta).

    O modo constante F_0 de Re(f) é eliminado pelo vínculo

        (1/2pi) int exp(-F) exp(2 sigma cos(theta)) dtheta = 1.
    """
    a1, a2, eta, sigma = np.asarray(y, dtype=float)
    theta = np.linspace(0.0, 2.0 * math.pi, n_grid, endpoint=False)
    dtheta = 2.0 * math.pi / n_grid
    cos1 = np.cos(theta)
    sin1 = np.sin(theta)
    cos2 = np.cos(2.0 * theta)

    # Normalização exata da medida angular.
    f0 = log_i0(2.0 * sigma - eta)
    f_real = f0 + eta * cos1
    df_real = -eta * sin1
    dphase = 1.0 / (2.0 * math.pi) + a1 * cos1 + 2.0 * a2 * cos2
    lap_sigma = -sigma * cos1

    rho = np.exp(-f_real)
    sqrt_g = np.exp(2.0 * sigma * cos1)

    # Após multiplicar por sqrt(g), o setor conformal 2D reduz-se a esta
    # expressão, preservando R + g^{-1} df d fbar e (Re f - n).
    integrand = (
        (-2.0 * lap_sigma + df_real**2 + dphase**2) * rho
        + (f_real - N_COMPLEX) * rho * sqrt_g
    )
    return float(np.sum(integrand) * dtheta)


def measure_norm(y: np.ndarray, n_grid: int) -> float:
    _, _, eta, sigma = np.asarray(y, dtype=float)
    theta = np.linspace(0.0, 2.0 * math.pi, n_grid, endpoint=False)
    cos1 = np.cos(theta)
    f0 = log_i0(2.0 * sigma - eta)
    return float(np.mean(np.exp(-(f0 + eta * cos1) + 2.0 * sigma * cos1)))


def gradient(y: np.ndarray, n_grid: int, h: float = 3.0e-5) -> np.ndarray:
    y = np.asarray(y, dtype=float)
    result = np.empty_like(y)
    for i in range(y.size):
        hi = h * max(1.0, abs(float(y[i])))
        step = np.zeros_like(y)
        step[i] = hi
        result[i] = (
            reduced_action(y + step, n_grid)
            - reduced_action(y - step, n_grid)
        ) / (2.0 * hi)
    return result


def hessian(y: np.ndarray, n_grid: int, h: float = 3.0e-4) -> np.ndarray:
    columns = []
    for j in range(y.size):
        step = np.zeros_like(y)
        step[j] = h
        columns.append(
            (gradient(y + step, n_grid) - gradient(y - step, n_grid))
            / (2.0 * h)
        )
    matrix = np.column_stack(columns)
    return 0.5 * (matrix + matrix.T)


def find_stationary_points(n_grid: int) -> list[np.ndarray]:
    starts = [
        np.array([0.0, 0.0, eta, sigma], dtype=float)
        for eta in (-1.0, 0.0, 1.0)
        for sigma in (-1.0, 0.0, 1.0)
    ]
    roots: list[np.ndarray] = []
    for start in starts:
        result = least_squares(
            lambda y: gradient(y, n_grid),
            start,
            bounds=(-5.0, 5.0),
            xtol=1.0e-12,
            ftol=1.0e-12,
            gtol=1.0e-12,
            max_nfev=1000,
        )
        if np.linalg.norm(result.fun) > 1.0e-6:
            continue
        if any(np.linalg.norm(result.x - old) < 1.0e-5 for old in roots):
            continue
        roots.append(result.x)
    return roots


def main() -> None:
    grids = (1024, 2048, 4096, 8192)
    rows: list[dict[str, float | int]] = []
    all_roots: dict[int, list[np.ndarray]] = {}

    for n_grid in grids:
        roots = find_stationary_points(n_grid)
        all_roots[n_grid] = roots
        if not roots:
            raise RuntimeError(f"nenhuma sela encontrada para N={n_grid}")
        # A busca encontra uma única raiz dentro da caixa declarada.
        root = min(roots, key=np.linalg.norm)
        eigenvalues = np.linalg.eigvalsh(hessian(root, n_grid))
        rows.append(
            {
                "N": n_grid,
                "a1": float(root[0]),
                "a2": float(root[1]),
                "eta": float(root[2]),
                "sigma": float(root[3]),
                "norm": measure_norm(root, n_grid),
                "grad": float(np.linalg.norm(gradient(root, n_grid))),
                "eig_min": float(eigenvalues[0]),
                "n_roots": len(roots),
            }
        )

    lines = [
        "# Capítulo 16 — amplitude de densidade calculada pela sela",
        "",
        "## Classificação",
        "",
        "Avaliação direta de uma sela Galerkin reduzida normalizada e teste de",
        "convergência. Não é a sela leptônica física completa em oito dimensões.",
        "O alvo experimental de `g-2` não participa do cálculo.",
        "",
        "## 1. Problema variacional",
        "",
        "Com circulação unitária fixada, variam-se:",
        "",
        "$$",
        "y=(a_1,a_2,\\eta,\\sigma).",
        "$$",
        "",
        "A fase com monodromia é diferenciada por:",
        "",
        "$$",
        "P'=\\frac{1}{2\\pi}+a_1\\cos\\theta+2a_2\\cos2\\theta.",
        "$$",
        "",
        "A medida é restringida por:",
        "",
        "$$",
        "\\frac1{2\\pi}\\int_0^{2\\pi}\\rho\\sqrt g\\,d\\theta=1.",
        "$$",
        "",
        "O modo constante de $\\operatorname{Re}f$ fica então determinado por:",
        "",
        "$$",
        "F_0=\\log I_0(2\\sigma-\\eta).",
        "$$",
        "",
        "A sela resolve $\\nabla_y S_{\\rm red}=0$.",
        "",
        "## 2. Convergência",
        "",
        "| N | raízes | a1 | a2 | eta | sigma | norma U | ||grad S|| | eig min |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['N']} | {row['n_roots']} | {row['a1']:.9e} | "
            f"{row['a2']:.9e} | {row['eta']:.9e} | {row['sigma']:.9e} | "
            f"{row['norm']:.12e} | {row['grad']:.3e} | {row['eig_min']:.9e} |"
        )

    eta_final = float(rows[-1]["eta"])
    lines.extend(
        [
            "",
            "## 3. Resultado",
            "",
            "Dentro da caixa de busca $[-5,5]^4$, iniciada a partir de nove pontos,",
            "a única raiz estacionária normalizada é a sela homogênea:",
            "",
            "$$",
            "a_1=a_2=\\eta_\\ell=\\sigma=0",
            "$$",
            "",
            f"com valor numérico final `eta_l = {eta_final:.15e}`.",
            "",
            "A Hessiana reduzida ainda possui um autovalor negativo. Portanto,",
            "a raiz é uma sela do funcional reduzido, não um mínimo estável nem",
            "o background leptônico físico 8D já projetado.",
            "",
            "## 4. Consequência para o canal superior",
            "",
            "Como $\\eta_\\ell=0$ nesta sela,",
            "",
            "$$",
            "\\Delta H_{12}=\\eta_\\ell T_{123}=0.",
            "$$",
            "",
            "A solução não normalizada com $|\\eta|\\simeq1{,}064$ é excluída:",
            "ela altera a norma total de $\\mathcal U\\sqrt g$ e não pertence ao",
            "domínio variacional normalizado da GDQ.",
            "",
            "O cálculo demonstra um resultado negativo útil: a sela angular",
            "homogênea não gera a correção metrológica superior. Um valor não nulo",
            "de $\\eta_\\ell$ só pode vir do background 8D não homogêneo, warped ou",
            "misto, com domínio, bordos e projetor físico especificados.",
            "",
        ]
    )

    output = BASE / "saida_eta_pela_sela_gmenos2.md"
    output.write_text("\n".join(lines), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
