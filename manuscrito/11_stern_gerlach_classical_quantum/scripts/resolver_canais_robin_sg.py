#!/usr/bin/env python3
"""
Capítulo 11 — Espectro dos dois canais Robin de Stern–Gerlach.

Modelo reduzido:
    H psi = -psi'' + V(r) psi,
    r in [r_c, r_max].

No estômato:
    partial_n psi + R_± psi = 0,
    R_± = R_0 ± r_B.

No exterior usa-se Neumann natural. A discretização por elementos finitos
lineares gera o problema generalizado simétrico:
    K v = lambda M v.

As somas espectrais adimensionais são:
    Gamma_red = sum |j_nu|^2 / lambda_nu,
    kappa_red = sum |j_nu|^2 / lambda_nu^2.

Elas testam estrutura e convergência; não são taxas físicas sem a calibração
do background radial GDQ.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import scipy.linalg as la
import scipy.sparse as sp
import scipy.sparse.linalg as spla


@dataclass
class ChannelSpectrum:
    sign: int
    robin: float
    eigenvalues: np.ndarray
    gamma_reduced: float
    kappa_reduced: float
    symmetry_error: float
    residual: float


def potential(
    r: np.ndarray,
    center: float,
    mass2: float,
    well: float,
    width: float,
) -> np.ndarray:
    return mass2 - well * np.exp(-((r - center) / width) ** 2)


def probe_profile(r: np.ndarray, width: float) -> np.ndarray:
    values = np.exp(-((r - r[0]) / width) ** 2)
    return values


def assemble_fem(
    n_grid: int,
    r_c: float,
    r_max: float,
    robin_left: float,
    mass2: float,
    well: float,
    well_width: float,
) -> tuple[np.ndarray, sp.csc_matrix, sp.csc_matrix]:
    if n_grid < 20:
        raise ValueError("n_grid deve ser pelo menos 20.")
    r = np.linspace(r_c, r_max, n_grid)
    h = float(r[1] - r[0])
    K = sp.lil_matrix((n_grid, n_grid), dtype=float)
    M = sp.lil_matrix((n_grid, n_grid), dtype=float)

    gauss_x = np.array([-1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0)])
    gauss_w = np.array([1.0, 1.0])

    for element in range(n_grid - 1):
        x_left = r[element]
        x_right = r[element + 1]
        local_k = np.array([[1.0, -1.0], [-1.0, 1.0]]) / h
        local_m = (h / 6.0) * np.array([[2.0, 1.0], [1.0, 2.0]])
        local_v = np.zeros((2, 2), dtype=float)

        for xi, weight in zip(gauss_x, gauss_w):
            shape = np.array([(1.0 - xi) / 2.0, (1.0 + xi) / 2.0])
            x = 0.5 * ((1.0 - xi) * x_left + (1.0 + xi) * x_right)
            value = float(
                potential(
                    np.array([x]), r_c, mass2, well, well_width
                )[0]
            )
            local_v += weight * value * np.outer(shape, shape) * h / 2.0

        indices = [element, element + 1]
        for a in range(2):
            for b in range(2):
                K[indices[a], indices[b]] += local_k[a, b] + local_v[a, b]
                M[indices[a], indices[b]] += local_m[a, b]

    # Robin esquerdo com normal exterior: -psi'(r_c)+R psi(r_c)=0.
    K[0, 0] += robin_left
    return r, K.tocsc(), M.tocsc()


def solve_channel(
    sign: int,
    n_grid: int,
    n_modes: int,
    args: argparse.Namespace,
) -> ChannelSpectrum:
    robin = args.robin0 + sign * args.robin_split
    r, stiffness, mass = assemble_fem(
        n_grid,
        args.r_c,
        args.r_max,
        robin,
        args.mass2,
        args.well,
        args.well_width,
    )
    k = min(n_modes, n_grid - 3)
    eigenvalues, eigenvectors = spla.eigsh(
        stiffness,
        M=mass,
        k=k,
        sigma=0.0,
        which="LM",
    )
    order = np.argsort(eigenvalues)
    eigenvalues = np.asarray(eigenvalues[order], dtype=float)
    eigenvectors = np.asarray(eigenvectors[:, order], dtype=float)

    # eigsh normaliza na métrica M; reforçamos para reduzir erro acumulado.
    for index in range(k):
        norm = float(
            np.sqrt(eigenvectors[:, index] @ (mass @ eigenvectors[:, index]))
        )
        eigenvectors[:, index] /= norm

    source = probe_profile(r, args.probe_width)
    source_norm = float(np.sqrt(source @ (mass @ source)))
    source /= source_norm
    overlaps = eigenvectors.T @ (mass @ source)

    positive = eigenvalues > args.positivity_tolerance
    if not np.all(positive):
        gamma_reduced = float("nan")
        kappa_reduced = float("nan")
    else:
        gamma_reduced = float(np.sum(overlaps**2 / eigenvalues))
        kappa_reduced = float(np.sum(overlaps**2 / eigenvalues**2))

    symmetry_error = float(
        spla.norm(stiffness - stiffness.T)
        / max(spla.norm(stiffness), np.finfo(float).eps)
    )
    first_vector = eigenvectors[:, 0]
    residual_vector = stiffness @ first_vector - eigenvalues[0] * (
        mass @ first_vector
    )
    residual = float(
        la.norm(residual_vector)
        / max(la.norm(stiffness @ first_vector), np.finfo(float).eps)
    )

    return ChannelSpectrum(
        sign,
        robin,
        eigenvalues,
        gamma_reduced,
        kappa_reduced,
        symmetry_error,
        residual,
    )


def run(args: argparse.Namespace) -> str:
    grids = [int(value) for value in args.grids.split(",")]
    lines = [
        "# Espectro Robin dos dois canais — Capítulo 11",
        "",
        "## Modelo reduzido",
        "",
        "$$",
        r"H_\pm=-\frac{d^2}{dr^2}+V(r),\qquad R_\pm=R_0\pm r_B.",
        "$$",
        "",
        f"- domínio: [{args.r_c}, {args.r_max}]",
        f"- R0: {args.robin0}",
        f"- separação rB: {args.robin_split}",
        f"- mass2: {args.mass2}",
        f"- poço: {args.well}",
        f"- largura do poço: {args.well_width}",
        f"- modos nas somas: {args.modes}",
        "",
        "## Convergência",
        "",
        "| N | canal | R | lambda1 | lambda2 | gap positivo | Gamma_red | kappa_red | erro simetria | resíduo |",
        "|---:|:---:|---:|---:|---:|:---:|---:|---:|---:|---:|",
    ]
    latest: dict[int, ChannelSpectrum] = {}

    for n_grid in grids:
        for sign in (1, -1):
            spectrum = solve_channel(sign, n_grid, args.modes, args)
            latest[sign] = spectrum
            values = spectrum.eigenvalues
            positive = bool(
                np.all(values > args.positivity_tolerance)
            )
            label = "+" if sign > 0 else "-"
            lines.append(
                f"| {n_grid} | {label} | {spectrum.robin:.6f} | "
                f"{values[0]:.9e} | {values[1]:.9e} | "
                f"{str(positive)} | {spectrum.gamma_reduced:.9e} | "
                f"{spectrum.kappa_reduced:.9e} | "
                f"{spectrum.symmetry_error:.3e} | {spectrum.residual:.3e} |"
            )

    plus = latest[1]
    minus = latest[-1]
    splitting = float(plus.eigenvalues[0] - minus.eigenvalues[0])
    lines.extend(
        [
            "",
            "## Diagnóstico na malha mais fina",
            "",
            f"- separação do modo fundamental lambda1+ - lambda1-: {splitting:.9e}",
            f"- ambos os gaps positivos: {bool(plus.eigenvalues[0] > 0 and minus.eigenvalues[0] > 0)}",
            "- as matrizes são simétricas por construção variacional;",
            "- Gamma_red e kappa_red são proxies espectrais adimensionais;",
            "- um valor físico exige o background radial e a normalização de tempo da GDQ.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--grids", default="200,400,800,1600")
    parser.add_argument("--modes", type=int, default=16)
    parser.add_argument("--r-c", type=float, default=0.1)
    parser.add_argument("--r-max", type=float, default=8.0)
    parser.add_argument("--robin0", type=float, default=1.0)
    parser.add_argument("--robin-split", type=float, default=0.25)
    parser.add_argument("--mass2", type=float, default=1.0)
    parser.add_argument("--well", type=float, default=0.2)
    parser.add_argument("--well-width", type=float, default=0.8)
    parser.add_argument("--probe-width", type=float, default=0.5)
    parser.add_argument("--positivity-tolerance", type=float, default=1e-10)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("saida_robin_channels_sg.md"),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    report = run(args)
    args.output.write_text(report, encoding="utf-8")
    print(report)
    print(f"\nArquivo salvo em: {args.output}")


if __name__ == "__main__":
    main()
