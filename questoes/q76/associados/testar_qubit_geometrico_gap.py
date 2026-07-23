#!/usr/bin/env python3
"""Q76 — teste reduzido de qubit geométrico por gap e projetor de Riesz.

Classificação:
    teste de consistência matemática / mock reduzido.

O que este script faz:
    1. constrói uma Hessiana física finita K com um cluster lógico de dois
       modos isolados;
    2. calcula o projetor lógico P_Q;
    3. aplica perturbações locais subcríticas e supercríticas;
    4. mede a variação do subespaço lógico.

O que este script NÃO faz:
    - não é simulação de hardware real;
    - não deriva K da ação oficial;
    - não prova fidelidade perfeita;
    - não elimina correção de erros.

Ele apenas valida a álgebra mínima usada na Q76:

    K_phys -> cluster bidimensional -> projetor de Riesz -> estabilidade por gap.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "saida_testar_qubit_geometrico_gap.md"


def projector_from_low_cluster(k: np.ndarray, dim_cluster: int = 2) -> tuple[np.ndarray, np.ndarray]:
    """Return eigenvalues and orthogonal projector onto the lowest cluster."""
    vals, vecs = np.linalg.eigh(k)
    q = vecs[:, :dim_cluster]
    p = q @ q.T
    return vals, p


def principal_projector_distance(p: np.ndarray, q: np.ndarray) -> float:
    """Operator-norm distance between two orthogonal projectors."""
    return float(np.linalg.norm(p - q, ord=2))


def make_local_noise(n: int, strength: float, seed: int) -> np.ndarray:
    """Symmetric local perturbation with prescribed operator norm."""
    rng = np.random.default_rng(seed)
    raw = np.zeros((n, n))

    # Perturb a small local block. This mimics a local apparatus/material
    # perturbation instead of a global random Hamiltonian.
    idx = [1, 2, 3]
    block = rng.normal(size=(len(idx), len(idx)))
    block = 0.5 * (block + block.T)
    for a, ia in enumerate(idx):
        for b, ib in enumerate(idx):
            raw[ia, ib] = block[a, b]

    norm = np.linalg.norm(raw, ord=2)
    return strength * raw / norm


def make_mixing_noise(n: int, strength: float) -> np.ndarray:
    """Perturbation that directly mixes logical and complement sectors."""
    raw = np.zeros((n, n))
    raw[1, 2] = raw[2, 1] = 1.0
    raw[0, 3] = raw[3, 0] = 0.5
    norm = np.linalg.norm(raw, ord=2)
    return strength * raw / norm


def main() -> None:
    # Hessiana reduzida: dois modos lógicos quase degenerados e um complemento
    # separado por gap. Em um cálculo GDQ real, K viria de
    # P_phys Hess(S_GDQ) P_phys.
    eigenvalues = np.array([0.00, 0.03, 1.00, 1.35, 1.80, 2.40])
    k0 = np.diag(eigenvalues)
    vals0, p0 = projector_from_low_cluster(k0)
    gap = vals0[2] - vals0[1]

    rows = []
    for label, frac, builder in [
        ("local_subcritico_10pct", 0.10, "local"),
        ("local_subcritico_40pct", 0.40, "local"),
        ("local_limiar_50pct", 0.50, "local"),
        ("mix_subcritico_40pct", 0.40, "mix"),
        ("mix_supercritico_80pct", 0.80, "mix"),
        ("mix_supercritico_120pct", 1.20, "mix"),
    ]:
        strength = frac * gap
        if builder == "local":
            dk = make_local_noise(k0.shape[0], strength, seed=76)
        else:
            dk = make_mixing_noise(k0.shape[0], strength)
        k = k0 + dk
        vals, p = projector_from_low_cluster(k)
        new_gap = vals[2] - vals[1]
        dist = principal_projector_distance(p0, p)
        bound = 2.0 * np.linalg.norm(dk, ord=2) / gap
        rows.append((label, frac, strength, new_gap, dist, bound, vals[:4]))

    lines = [
        "# Saída — Q76 teste reduzido de qubit geométrico",
        "",
        "Classificação: teste de consistência matemática / mock reduzido.",
        "",
        "Este script verifica somente a álgebra de estabilidade por gap:",
        "",
        "$$",
        "K_{\\rm phys}",
        "\\to",
        "P_Q",
        "\\to",
        "\\Delta_{\\rm gap}",
        "\\to",
        "\\|\\delta P_Q\\|.",
        "$$",
        "",
        "Ele não deriva a Hessiana de um hardware real.",
        "",
        "## Background reduzido",
        "",
        f"- autovalores iniciais: `{eigenvalues.tolist()}`",
        f"- gap lógico--complemento: `{gap:.12f}`",
        "",
        "## Perturbações locais",
        "",
        "| caso | ||dK||/gap | ||dK|| | gap novo | ||dP|| | cota 2||dK||/gap | autovalores baixos |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]

    for label, frac, strength, new_gap, dist, bound, vals in rows:
        vals_str = ", ".join(f"{v:.6f}" for v in vals)
        lines.append(
            f"| {label} | {frac:.3f} | {strength:.6f} | {new_gap:.6f} | "
            f"{dist:.6f} | {bound:.6f} | `{vals_str}` |"
        )

    lines += [
        "",
        "## Interpretação",
        "",
        "Para perturbações abaixo de metade do gap, o cluster permanece isolado e",
        "a variação do subespaço lógico fica controlada. Perturbações acima desse",
        "limiar não significam erro automático, mas deixam de estar cobertas pelo",
        "critério simples usado na Q76.",
        "",
        "$$",
        "\\boxed{",
        "\\text{proteção GDQ = gap Hessiano + contorno + topologia, não erro zero.}",
        "}",
        "$$",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
