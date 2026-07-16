#!/usr/bin/env python3
"""Q41: parede GDQ reduzida versus mecânica quântica padrão.

Unidades:
    L = 1
    E_L = hbar^2/(2 m L^2) = 1

No interior do poço V=0. Nas paredes V=v0. A Hessiana escalar homogênea
fornece kappa(E)=sqrt(v0-E) e, para uma parede de espessura d terminada por
Dirichlet, lambda(E)=kappa*coth(kappa*d).

O programa compara:
  1. raízes da equação espectral Robin/Dirichlet--Neumann;
  2. diagonalização direta da barreira finita em [-d, 1+d];
  3. poço infinito padrão E_n=(n*pi)^2.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from time import perf_counter

import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import brentq


@dataclass(frozen=True)
class Spectrum:
    points: int
    energies: np.ndarray
    elapsed: float


def coth(x: float) -> float:
    if x > 20.0:
        return 1.0 + 2.0 * np.exp(-2.0 * x)
    return 1.0 / np.tanh(x)


def impedance(e: float, v0: float, thickness: float) -> float:
    """Mapa Dirichlet--Neumann de uma parede homogênea finita."""
    if e >= v0:
        raise ValueError("O teste ligado requer E < V0.")
    kappa = np.sqrt(v0 - e)
    return kappa * coth(kappa * thickness)


def spectral_function(e: float, v0: float, thickness: float) -> float:
    """Equação espectral para paredes simétricas com lambda(E)."""
    if e <= 0.0 or e >= v0:
        return np.nan
    k = np.sqrt(e)
    lam = impedance(e, v0, thickness)
    return (lam * lam - k * k) * np.sin(k) + 2.0 * k * lam * np.cos(k)


def robin_spectrum(v0: float, thickness: float, modes: int) -> np.ndarray:
    """Localiza as primeiras raízes ligadas sem usar o resultado alvo."""
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
    raise RuntimeError(f"Foram encontradas apenas {len(roots)} raízes abaixo de V0.")


def direct_spectrum(v0: float, thickness: float, points: int, modes: int) -> Spectrum:
    """Diferenças finitas de segunda ordem no domínio parede+poço+parede."""
    start = perf_counter()
    total_length = 1.0 + 2.0 * thickness
    h = total_length / (points + 1)
    x = -thickness + h * np.arange(1, points + 1)
    potential = np.where((x > 0.0) & (x < 1.0), 0.0, v0)
    # Regra trapezoidal na descontinuidade: o nó exatamente sobre a interface
    # representa metade de cada meio. Sem isso, o salto fica deslocado por h/2
    # e a comparação apresenta artificialmente convergência de primeira ordem.
    interface = np.isclose(x, 0.0, atol=10.0 * np.finfo(float).eps) | np.isclose(
        x, 1.0, atol=10.0 * np.finfo(float).eps
    )
    potential[interface] = 0.5 * v0
    diagonal = 2.0 / h**2 + potential
    off_diagonal = np.full(points - 1, -1.0 / h**2)
    eigenvalues = eigh_tridiagonal(
        diagonal,
        off_diagonal,
        select="i",
        select_range=(0, modes - 1),
        check_finite=False,
    )[0]
    return Spectrum(points, eigenvalues, perf_counter() - start)


def infinite_well(modes: int) -> np.ndarray:
    n = np.arange(1, modes + 1, dtype=float)
    return (np.pi * n) ** 2


def relative_error(value: np.ndarray, reference: np.ndarray) -> np.ndarray:
    return np.abs(value - reference) / np.abs(reference)


def render_report(
    v0: float,
    thickness: float,
    modes: int,
    grids: list[int],
    robin: np.ndarray,
    direct: list[Spectrum],
) -> str:
    standard = infinite_well(modes)
    best = direct[-1].energies
    lines = [
        "# Q41 — Teste numérico do poço com parede física",
        "",
        "## Configuração",
        "",
        "- unidades: $L=1$ e $\\hbar^2/(2mL^2)=1$;",
        f"- altura da parede: $V_0={v0:g}$;",
        f"- espessura de cada parede: $d={thickness:g}L$;",
        "- face externa: Dirichlet;",
        "- impedância derivada: $\\lambda(E)=\\sqrt{V_0-E}\\,\\coth[d\\sqrt{V_0-E}]$;",
        f"- modos comparados: {modes}.",
        "",
        "## Comparação espectral",
        "",
        "| $n$ | Robin/DN | Barreira direta | Poço infinito | erro direto–Robin | desvio ao infinito |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    err_direct = relative_error(best, robin)
    shift_standard = (robin - standard) / standard
    for i in range(modes):
        lines.append(
            f"| {i + 1} | {robin[i]:.10f} | {best[i]:.10f} | "
            f"{standard[i]:.10f} | {err_direct[i]:.3e} | "
            f"{shift_standard[i]:+.3e} |"
        )

    lines += [
        "",
        "## Convergência da diagonalização direta",
        "",
        "| pontos | máximo erro relativo contra Robin/DN | tempo (s) |",
        "|---:|---:|---:|",
    ]
    for result in direct:
        error = np.max(relative_error(result.energies, robin))
        lines.append(f"| {result.points} | {error:.3e} | {result.elapsed:.4f} |")

    rigidity_values = [100.0, 1000.0, 10_000.0, 100_000.0]
    lines += [
        "",
        "## Limite de parede rígida",
        "",
        "| $V_0$ | $E_1^{\\rm Robin}$ | erro relativo contra o poço infinito |",
        "|---:|---:|---:|",
    ]
    for rigidity in rigidity_values:
        if rigidity <= standard[0]:
            continue
        e1 = robin_spectrum(rigidity, thickness, 1)[0]
        err = abs(e1 - standard[0]) / standard[0]
        lines.append(f"| {rigidity:.0f} | {e1:.10f} | {err:.3e} |")

    order = np.nan
    if len(direct) >= 3:
        e1 = np.max(relative_error(direct[-3].energies, robin))
        e2 = np.max(relative_error(direct[-2].energies, robin))
        e3 = np.max(relative_error(direct[-1].energies, robin))
        if e1 > e2 > e3 > 0:
            order = 0.5 * (np.log2(e1 / e2) + np.log2(e2 / e3))

    lines += [
        "",
        "## Auditoria",
        "",
        f"- erro máximo na malha mais fina: ${np.max(err_direct):.3e}$;",
        f"- ordem empírica aproximada: ${order:.3f}$;" if np.isfinite(order) else "- ordem empírica: não estimada;",
        "- a coincidência Robin/DN–barreira direta testa a eliminação variacional da parede;",
        "- a diferença para o poço infinito é penetração física na parede, não erro numérico;",
        "- nenhum autovalor experimental foi usado para ajustar os parâmetros.",
        "",
        "## Classificação",
        "",
        "Este cálculo é um teste de consistência e convergência de um background",
        "material reduzido. Ele recupera a mecânica quântica padrão para a barreira",
        "finita e verifica o limite de impedância GDQ. Não constitui, sozinho, uma",
        "previsão distintiva até que $V_0$ e os coeficientes da Hessiana sejam",
        "calculados para um material físico pela ação oficial.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--v0", type=float, default=1000.0)
    parser.add_argument("--thickness", type=float, default=0.25)
    parser.add_argument("--modes", type=int, default=5)
    # Para d=0.25 e comprimento total 1.5, N+1 múltiplo de 6 alinha
    # exatamente as duas interfaces materiais à malha.
    parser.add_argument("--grids", type=int, nargs="+", default=[599, 1199, 2399, 4799, 9599])
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("resultado_poco_gdq.md"),
    )
    args = parser.parse_args()
    if args.v0 <= 0 or args.thickness <= 0 or args.modes <= 0:
        parser.error("v0, thickness e modes devem ser positivos.")

    robin = robin_spectrum(args.v0, args.thickness, args.modes)
    direct = [direct_spectrum(args.v0, args.thickness, n, args.modes) for n in args.grids]
    report = render_report(args.v0, args.thickness, args.modes, args.grids, robin, direct)
    args.output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
