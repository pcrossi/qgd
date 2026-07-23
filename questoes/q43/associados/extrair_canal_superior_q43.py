#!/usr/bin/env python3
"""Q43 — extrator de canais transversais da Hessiana.

Entrada:
    NPZ com H, c, m_perp, gamma0 opcional.

Saída:
    Decompõe o espaço em:
        e0 = direção da circulação c;
        e_i = autovetores do bloco transversal ortogonal a c.

    Para cada canal calcula:
        K_i  = <e_i, H e_i>
        J_i  = -<e0, H e_i>
        mu_i = <e_i, m_perp>

Uso científico:
    Se H vier da Hessiana oficial no background Phi_l, esses coeficientes são
    derivados. Se H vier dos blocos `required`, a extração é apenas auditoria
    da engenharia inversa.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np


def load_npz(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    data = np.load(path)
    H = np.asarray(data["H"], dtype=np.complex128)
    c = np.asarray(data["c"], dtype=np.complex128).reshape(-1)
    m = np.asarray(data["m_perp"], dtype=np.complex128).reshape(-1)
    gamma0 = float(np.asarray(data["gamma0"]).reshape(-1)[0]) if "gamma0" in data else 1.0
    return H, c, m, gamma0


def orthogonal_complement(e0: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    n = e0.size
    basis = []
    for k in range(n):
        v = np.zeros(n, dtype=np.complex128)
        v[k] = 1.0
        v = v - e0 * np.vdot(e0, v)
        for b in basis:
            v = v - b * np.vdot(b, v)
        norm = np.linalg.norm(v)
        if norm > tol:
            basis.append(v / norm)
    if not basis:
        return np.zeros((n, 0), dtype=np.complex128)
    return np.column_stack(basis)


def evaluate_anomaly(H: np.ndarray, c: np.ndarray, m: np.ndarray, gamma0: float) -> float:
    Hh = 0.5 * (H + H.conj().T)
    vals, vecs = np.linalg.eigh(Hh)
    Hinv = (vecs * (1.0 / vals)) @ vecs.conj().T
    return float(np.real(np.vdot(c, Hinv @ m) / (gamma0 * np.vdot(c, Hinv @ c))))


def extract_channels(H: np.ndarray, c: np.ndarray, m: np.ndarray, gamma0: float) -> dict:
    Hh = 0.5 * (H + H.conj().T)
    c_norm = np.linalg.norm(c)
    if c_norm == 0:
        raise ValueError("Vetor c nulo.")
    e0 = c / c_norm
    Q = orthogonal_complement(e0)
    if Q.shape[1] == 0:
        raise ValueError("Sem subespaço transversal.")

    HT = Q.conj().T @ Hh @ Q
    vals, vecs_T = np.linalg.eigh(HT)
    vecs = Q @ vecs_T

    channels = []
    for idx, (val, e) in enumerate(zip(vals, vecs.T), start=1):
        K = np.vdot(e, Hh @ e)
        J = -np.vdot(e0, Hh @ e)
        mu = np.vdot(e, m)
        channels.append(
            {
                "idx": idx,
                "K": float(np.real(K)),
                "K_imag": float(np.imag(K)),
                "J": float(np.real(J)),
                "J_imag": float(np.imag(J)),
                "mu": float(np.real(mu)),
                "mu_imag": float(np.imag(mu)),
                "overlap_m_abs": float(abs(mu)),
                "eig": float(np.real(val)),
            }
        )
    return {
        "dimension": int(H.shape[0]),
        "gamma0": gamma0,
        "a_geom": evaluate_anomaly(Hh, c, m, gamma0),
        "channels": channels,
    }


def render(path: Path, result: dict, classification: str) -> str:
    lines = [
        "# Q43 — extração de canais transversais",
        "",
        f"- entrada: `{path}`",
        f"- classificação: {classification}",
        f"- dimensão: `{result['dimension']}`",
        f"- gamma0: `{result['gamma0']:.15e}`",
        f"- a_geom reconstruído: `{result['a_geom']:.15e}`",
        "",
        "| canal | K_i | J_i | mu_i | |mu_i| | autovalor transversal |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for ch in result["channels"]:
        lines.append(
            f"| {ch['idx']} | {ch['K']:.15e} | {ch['J']:.15e} | "
            f"{ch['mu']:.15e} | {ch['overlap_m_abs']:.15e} | {ch['eig']:.15e} |"
        )
    lines.extend(
        [
            "",
            "## Leitura",
            "",
            r"Se a entrada for uma Hessiana oficial projetada, estes coeficientes são a derivação numérica de \(K_i,J_i,\mu_i\).",
            "Se a entrada for um bloco `required`, estes coeficientes apenas recuperam os parâmetros de engenharia inversa já embutidos no bloco.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("npz", type=Path)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument(
        "--classification",
        default="auditoria de bloco fornecido",
        help="classificação científica da entrada",
    )
    args = parser.parse_args()

    H, c, m, gamma0 = load_npz(args.npz)
    result = extract_channels(H, c, m, gamma0)
    text = render(args.npz, result, args.classification)
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
