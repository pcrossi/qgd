#!/usr/bin/env python3
"""Q43 — avaliador de anomalia a partir de uma Hessiana GDQ.

Entrada esperada em NPZ:

    H          matriz real/simétrica ou Hermitiana da Hessiana física
    c          vetor do modo protegido de Noether
    m_perp     vetor da fonte magnética transversal
    gamma0     escalar opcional; se ausente usa 1.0

O script calcula:

    a_geom = <c, H^+ m_perp> / (<c, H^+ c> gamma0)

onde H^+ é a pseudoinversa após corte espectral.

Esse script não constrói H. Ele só executa o cálculo quando o background
físico for fornecido.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np


def inner(a: np.ndarray, b: np.ndarray) -> complex:
    return np.vdot(a, b)


def load_npz(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    data = np.load(path)
    H = np.asarray(data["H"])
    c = np.asarray(data["c"])
    m_perp = np.asarray(data["m_perp"])
    gamma0 = float(np.asarray(data["gamma0"]).reshape(-1)[0]) if "gamma0" in data else 1.0
    return H, c, m_perp, gamma0


def evaluate(H: np.ndarray, c: np.ndarray, m_perp: np.ndarray, gamma0: float, cutoff: float) -> dict[str, float]:
    Hh = 0.5 * (H + H.conj().T)
    vals, vecs = np.linalg.eigh(Hh)
    max_abs = float(np.max(np.abs(vals))) if vals.size else 0.0
    threshold = cutoff * max(1.0, max_abs)
    keep = np.abs(vals) > threshold
    if not np.any(keep):
        raise ValueError("Nenhum autovalor físico acima do cutoff.")

    inv_vals = np.zeros_like(vals, dtype=np.complex128)
    inv_vals[keep] = 1.0 / vals[keep]
    Hpinv = (vecs * inv_vals) @ vecs.conj().T

    num = inner(c, Hpinv @ m_perp)
    den = inner(c, Hpinv @ c)
    if abs(den) <= threshold:
        raise ValueError("Denominador <c,H^+c> numericamente singular.")

    a_geom = num / (den * gamma0)
    return {
        "dimension": float(H.shape[0]),
        "eigen_min_kept": float(np.min(np.abs(vals[keep]))),
        "eigen_max": max_abs,
        "n_kept": float(np.count_nonzero(keep)),
        "n_removed": float(vals.size - np.count_nonzero(keep)),
        "den_real": float(np.real(den)),
        "den_imag": float(np.imag(den)),
        "num_real": float(np.real(num)),
        "num_imag": float(np.imag(num)),
        "a_geom_real": float(np.real(a_geom)),
        "a_geom_imag": float(np.imag(a_geom)),
        "g_total_if_added_to_minimal": float(2.0 * (1.0 + np.real(a_geom))),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("npz", type=Path, help="Arquivo NPZ com H, c, m_perp, gamma0 opcional")
    parser.add_argument("--cutoff", type=float, default=1e-10)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    H, c, m_perp, gamma0 = load_npz(args.npz)
    result = evaluate(H, c, m_perp, gamma0, args.cutoff)

    lines = [
        "# Q43 — avaliação de Hessiana fornecida",
        "",
        f"- entrada: `{args.npz}`",
        f"- cutoff relativo: `{args.cutoff}`",
        f"- gamma0: `{gamma0:.15e}`",
        "",
        "| quantidade | valor |",
        "|---|---:|",
    ]
    for k, v in result.items():
        lines.append(f"| {k} | {v:.15e} |")
    lines.append("")

    text = "\n".join(lines)
    if args.output is not None:
        args.output.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

