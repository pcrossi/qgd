#!/usr/bin/env python3
"""Compara kernels covariantes no loop geométrico da Q34."""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import exp1


def spectral_primitive(name: str, z: np.ndarray | float) -> np.ndarray | float:
    if name == "canonico":
        return exp1(z)
    if name == "mistura":
        return 0.5 * exp1(z) + 0.5 * exp1(2.0 * z)
    if name == "inteiro_mais":
        return exp1(z) + np.exp(-z)
    raise ValueError(name)


def polarization(
    q2: float,
    kernel: str,
    charge: float = 1.0,
    mass: float = 1.0,
    s0: float = 0.2749005225136263,
    points: int = 512,
) -> float:
    z, w = leggauss(points)
    x = 0.5 * (z + 1.0)
    w = 0.5 * w
    u = x * (1.0 - x)
    weight = (1.0 - 2.0 * x) ** 2
    eta = s0 * mass**2
    integrand = weight * (
        spectral_primitive(kernel, eta)
        - spectral_primitive(kernel, eta + s0 * u * q2)
    )
    return float(charge**2 / (16.0 * math.pi**2) * np.dot(w, integrand))


def asymptote(kernel: str, eta: float, charge: float = 1.0) -> float:
    return float(charge**2 / (48.0 * math.pi**2) * spectral_primitive(kernel, eta))


def ward_error(q: np.ndarray, value: float) -> float:
    q2 = float(q @ q)
    tensor = (np.outer(q, q) - q2 * np.eye(q.size)) * value
    return float(np.linalg.norm(q @ tensor))


def main() -> int:
    kernels = ["canonico", "mistura", "inteiro_mais"]
    eta = 0.2749005225136263
    q = np.array([0.23, -0.41, 0.61, 0.79])
    rows = []
    for name in kernels:
        zero = polarization(0.0, name)
        value = polarization(float(q @ q), name)
        ward = ward_error(q, value)
        uv = asymptote(name, eta)
        grid = [polarization(x, name) for x in np.logspace(-6, 8, 60)]
        monotone = bool(np.all(np.diff(grid) >= -1e-13))
        bounded = bool(max(grid) <= uv + 1e-13)
        rows.append((name, zero, ward, value, uv, monotone, bounded))

    assert max(abs(row[1]) for row in rows) < 1e-15
    assert max(row[2] for row in rows) < 1e-15
    assert all(row[5] and row[6] for row in rows)
    assert len({round(row[4], 12) for row in rows}) == len(kernels)

    output = Path(__file__).with_name("saida_comparacao_kernels_geometricos.md")
    lines = [
        "# Comparação de kernels geométricos covariantes — Q34",
        "",
        "## Classificação",
        "",
        "**Teste de consistência e sensibilidade ao kernel.**",
        "",
        "| kernel | $\\Pi(0)$ | erro Ward | $\\Pi(Q_*^2)$ | $\\Pi(\\infty)$ | monotônica | limitada |",
        "|:---|---:|---:|---:|---:|:---:|:---:|",
    ]
    for name, zero, ward, value, uv, monotone, bounded in rows:
        lines.append(
            f"| {name} | {zero:.3e} | {ward:.3e} | {value:.12e} | "
            f"{uv:.12e} | {monotone} | {bounded} |"
        )
    canonical = rows[0][4]
    lines += [
        "",
        "Variação do limite UV em relação ao kernel canônico:",
        "",
    ]
    for row in rows:
        relative = (row[4] / canonical - 1.0) * 100.0
        lines.append(f"- {row[0]}: {relative:+.6f}%.")
    lines += [
        "",
        "Ward, subtração e saturação são robustas. Os valores numéricos mudam,",
        "logo kernels distintos representam resoluções físicas distintas.",
        "",
    ]
    output.write_text("\n".join(lines), encoding="utf-8")
    print(output)
    for row in rows:
        print(row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
