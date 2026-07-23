#!/usr/bin/env python3
"""Capítulo 23 — poço com impedância GDQ reduzida.

Objetivo:
    Comparar o espectro de um poço com paredes físicas finitas contra:
    (1) a condição Robin/DtN derivada por Schur;
    (2) a diagonalização direta da barreira finita;
    (3) o poço infinito ideal.

Classificação:
    Teste de consistência e convergência. Nenhum dado experimental é usado.

Unidades:
    L = 1 e hbar^2/(2mL^2)=1.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from time import perf_counter

import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import brentq


OUT = Path(__file__).with_name("saida_poco_impedancia_gdq.md")


@dataclass(frozen=True)
class Spectrum:
    points: int
    energies: np.ndarray
    elapsed: float


def coth(x: float) -> float:
    """Cotangente hiperbólica estável para x grande."""

    if x > 20.0:
        return 1.0 + 2.0 * np.exp(-2.0 * x)
    return 1.0 / np.tanh(x)


def impedance(e: float, v0: float, thickness: float) -> float:
    """Mapa Dirichlet--Neumann de parede homogênea finita."""

    kappa = np.sqrt(v0 - e)
    return kappa * coth(kappa * thickness)


def spectral_function(e: float, v0: float, thickness: float) -> float:
    """Equação espectral para poço de comprimento L=1 com paredes simétricas."""

    if e <= 0.0 or e >= v0:
        return np.nan
    k = np.sqrt(e)
    lam = impedance(e, v0, thickness)
    return (lam * lam - k * k) * np.sin(k) + 2.0 * k * lam * np.cos(k)


def robin_spectrum(v0: float, thickness: float, modes: int) -> np.ndarray:
    """Localiza raízes do problema Robin/DtN."""

    grid = np.linspace(1.0e-10, v0 * (1.0 - 1.0e-11), 400_000)
    values = np.array([spectral_function(e, v0, thickness) for e in grid])
    roots: list[float] = []
    for left, right, fl, fr in zip(grid[:-1], grid[1:], values[:-1], values[1:]):
        if not np.isfinite(fl) or not np.isfinite(fr) or fl * fr >= 0.0:
            continue
        root = brentq(spectral_function, left, right, args=(v0, thickness))
        if not roots or abs(root - roots[-1]) > 1.0e-7:
            roots.append(root)
        if len(roots) == modes:
            return np.asarray(roots)
    raise RuntimeError("Raízes insuficientes abaixo de V0.")


def direct_spectrum(v0: float, thickness: float, points: int, modes: int) -> Spectrum:
    """Diagonalização direta da barreira finita em [-d,1+d]."""

    start = perf_counter()
    total_length = 1.0 + 2.0 * thickness
    h = total_length / (points + 1)
    x = -thickness + h * np.arange(1, points + 1)
    potential = np.where((x > 0.0) & (x < 1.0), 0.0, v0)
    interface = np.isclose(x, 0.0, atol=10.0 * np.finfo(float).eps) | np.isclose(
        x, 1.0, atol=10.0 * np.finfo(float).eps
    )
    potential[interface] = 0.5 * v0
    diagonal = 2.0 / h**2 + potential
    off_diagonal = np.full(points - 1, -1.0 / h**2)
    vals = eigh_tridiagonal(
        diagonal,
        off_diagonal,
        select="i",
        select_range=(0, modes - 1),
        check_finite=False,
    )[0]
    return Spectrum(points, vals, perf_counter() - start)


def infinite_well(modes: int) -> np.ndarray:
    n = np.arange(1, modes + 1, dtype=float)
    return (np.pi * n) ** 2


def relerr(value: np.ndarray, reference: np.ndarray) -> np.ndarray:
    return np.abs(value - reference) / np.abs(reference)


def main() -> None:
    v0 = 1000.0
    thickness = 0.25
    modes = 5
    grids = [599, 1199, 2399, 4799, 9599]

    robin = robin_spectrum(v0, thickness, modes)
    direct = [direct_spectrum(v0, thickness, n, modes) for n in grids]
    standard = infinite_well(modes)
    best = direct[-1].energies
    err_direct = relerr(best, robin)

    lines = [
        "---",
        'title: "Saída — poço com impedância GDQ"',
        "---",
        "",
        "# Saída — poço com impedância GDQ",
        "",
        "- unidades: $L=1$ e $\\hbar^2/(2mL^2)=1$;",
        f"- altura da parede: `{v0:g}`;",
        f"- espessura: `{thickness:g}L`;",
        "- classificação: teste de consistência/convergência.",
        "",
        "| $n$ | Robin/DtN | Barreira direta | Poço infinito | erro direto--DtN | desvio ao infinito |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for i in range(modes):
        lines.append(
            f"| {i+1} | `{robin[i]:.10f}` | `{best[i]:.10f}` | "
            f"`{standard[i]:.10f}` | `{err_direct[i]:.3e}` | "
            f"`{(robin[i]-standard[i])/standard[i]:+.3e}` |"
        )

    lines += [
        "",
        "| pontos | máximo erro relativo contra Robin/DtN | tempo [s] |",
        "|---:|---:|---:|",
    ]
    for result in direct:
        lines.append(
            f"| {result.points} | `{np.max(relerr(result.energies, robin)):.3e}` | `{result.elapsed:.4f}` |"
        )

    lines += [
        "",
        f"- erro máximo na malha mais fina: `{np.max(err_direct):.3e}`.",
        "- a diferença contra o poço infinito é penetração física na parede.",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
