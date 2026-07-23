#!/usr/bin/env python3
"""Espectro matricial do Dirac homogêneo em S3 com Hopf e shift torsional."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np


SIGMA = (
    np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex),
    np.array([[0.0, -1j], [1j, 0.0]], dtype=complex),
    np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex),
)


def angular_momentum(two_j: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    j = 0.5 * two_j
    magnetic = np.arange(-j, j + 1.0, 1.0)
    dim = magnetic.size
    lz = np.diag(magnetic).astype(complex)
    lp = np.zeros((dim, dim), dtype=complex)
    for col, m_value in enumerate(magnetic[:-1]):
        lp[col + 1, col] = np.sqrt(j * (j + 1.0) - m_value * (m_value + 1.0))
    lm = lp.conj().T
    lx = 0.5 * (lp + lm)
    ly = (lp - lm) / (2j)
    return lx, ly, lz


def block(two_j: int, charge: float, beta: float, radius: float) -> np.ndarray:
    generators = angular_momentum(two_j)
    dim_orb = two_j + 1
    matrix = np.zeros((2 * dim_orb, 2 * dim_orb), dtype=complex)
    for sigma, generator in zip(SIGMA, generators):
        matrix += 2.0 * np.kron(sigma, generator)
    matrix += 1.5 * np.eye(matrix.shape[0])
    matrix -= charge * np.kron(SIGMA[2], np.eye(dim_orb))
    matrix += beta * np.eye(matrix.shape[0])
    return matrix / radius


def spectrum(two_j_max: int, charge: float, beta: float, radius: float) -> np.ndarray:
    values: list[float] = []
    for two_j in range(two_j_max + 1):
        eigenvalues = np.linalg.eigvalsh(block(two_j, charge, beta, radius))
        spectator = two_j + 1
        values.extend(np.repeat(eigenvalues, spectator).tolist())
    return np.sort(np.asarray(values))


def expected_free(two_j_max: int, radius: float) -> np.ndarray:
    values: list[float] = []
    for n in range(two_j_max + 1):
        degeneracy = (n + 1) * (n + 2)
        value = (n + 1.5) / radius
        values.extend([-value] * degeneracy)
        values.extend([value] * degeneracy)
    # A truncagem por j não contém pares completos no maior nível. A
    # comparação exata é feita apenas no intervalo comum central.
    return np.sort(np.asarray(values))


def cs_reduced_eta_mod_one(m: int) -> float:
    value = -0.5 * m * m
    return value - np.floor(value)


def render(two_j_max: int, charges: list[int], beta: float, radius: float) -> str:
    free = spectrum(two_j_max, 0.0, 0.0, radius)
    # Confere os primeiros níveis positivos e negativos que não são afetados
    # pela borda do cutoff de representações.
    expected_levels = np.array([(n + 1.5) / radius for n in range(min(5, two_j_max + 1))])
    distinct_positive = np.unique(np.round(free[free > 0], 12))[: expected_levels.size]
    free_error = float(np.max(np.abs(distinct_positive - expected_levels)))

    lines = [
        "# Q28 — Teste espectral no elo $S^3$",
        "",
        "## Configuração",
        "",
        f"- $2j_{{\\max}}={two_j_max}$;",
        f"- raio $a={radius:g}$;",
        f"- deslocamento torsional de teste $\\beta={beta:g}$.",
        "",
        "## Verificação livre",
        "",
        f"Erro máximo nos primeiros níveis distintos: ${free_error:.3e}$.",
        "",
        "## Hopf e assimetria",
        "",
        "| $m$ | menor $|\\lambda|$ | kernel $h$ | modos negativos | modos positivos | $\\bar\\eta\\pmod 1$ por CS |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for m in charges:
        values = spectrum(two_j_max, float(m), beta, radius)
        tolerance = 1.0e-10
        negative = int(np.count_nonzero(values < -tolerance))
        positive = int(np.count_nonzero(values > tolerance))
        kernel = int(np.count_nonzero(np.abs(values) <= tolerance))
        min_abs = float(np.min(np.abs(values)))
        lines.append(
            f"| {m} | {min_abs:.10e} | {kernel} | {negative} | {positive} | "
            f"{cs_reduced_eta_mod_one(m):.6f} |"
        )

    lines += [
        "",
        "## Nota de auditoria",
        "",
        "A diferença finita entre contagens positivas e negativas depende do cutoff",
        "e não é usada como $\\eta(0)$. A parte fracionária apresentada vem da",
        "transgressão APS/Chern--Simons, que é estável módulo fluxo espectral inteiro.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--two-j-max", type=int, default=30)
    parser.add_argument("--charges", type=int, nargs="+", default=[-3, -2, -1, 0, 1, 2, 3])
    parser.add_argument("--beta", type=float, default=0.0)
    parser.add_argument("--radius", type=float, default=1.0)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("resultado_eta_s3_hopf.md"),
    )
    args = parser.parse_args()
    if args.two_j_max < 2 or args.radius <= 0:
        parser.error("two-j-max deve ser >=2 e radius deve ser positivo")
    report = render(args.two_j_max, args.charges, args.beta, args.radius)
    args.output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
