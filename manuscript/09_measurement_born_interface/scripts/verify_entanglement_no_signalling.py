#!/usr/bin/env python3
"""
GDQ — Chapter 9 / Reduced Entanglement and No-Signalling

Objective:
    Verify, in the reconstructed projective sector, three properties used as
    operational targets for the GDQ formulation of entanglement:

        1. non-factorizable singlet state;
        2. ideal correlation E(a,b) = -a.b;
        3. local marginals independent of the distant choice.

Important:
    This script is not a complete simulation of real GDQ apparatuses. It is the
    reduced test of the operational sector that a derivation by multiparticle Hessian
    must reproduce.

Classification:
    Reduced operational consistency test.

Output:
    scripts/output_verify_entanglement_no_signalling.md
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


def unit(v: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(v)
    if n == 0.0:
        raise ValueError("zero vector")
    return v / n


def joint_probability(s: int, t: int, a: np.ndarray, b: np.ndarray) -> float:
    """Reduced singlet probability: P(s,t|a,b)."""
    return 0.25 * (1.0 - s * t * float(np.dot(a, b)))


def correlation(a: np.ndarray, b: np.ndarray) -> float:
    return sum(
        s * t * joint_probability(s, t, a, b)
        for s in (-1, 1)
        for t in (-1, 1)
    )


def marginal_A(s: int, a: np.ndarray, b: np.ndarray) -> float:
    return sum(joint_probability(s, t, a, b) for t in (-1, 1))


def marginal_B(t: int, a: np.ndarray, b: np.ndarray) -> float:
    return sum(joint_probability(s, t, a, b) for s in (-1, 1))


def schmidt_singular_values_singlet() -> np.ndarray:
    coeff = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex) / np.sqrt(2.0)
    return np.linalg.svd(coeff, compute_uv=False)


def chsh_value() -> float:
    a0 = unit(np.array([1.0, 0.0, 0.0]))
    a1 = unit(np.array([0.0, 1.0, 0.0]))
    b0 = unit(np.array([1.0, 1.0, 0.0]))
    b1 = unit(np.array([1.0, -1.0, 0.0]))
    return (
        correlation(a0, b0)
        + correlation(a0, b1)
        + correlation(a1, b0)
        - correlation(a1, b1)
    )


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_verify_entanglement_no_signalling.md"

    axes_a = [
        unit(np.array([1.0, 0.0, 0.0])),
        unit(np.array([0.0, 1.0, 0.0])),
        unit(np.array([1.0, 1.0, 0.0])),
    ]
    axes_b = [
        unit(np.array([1.0, 0.0, 0.0])),
        unit(np.array([0.0, 1.0, 0.0])),
        unit(np.array([1.0, -1.0, 0.0])),
    ]

    rows = []
    max_corr_error = 0.0
    max_marginal_A_variation = 0.0
    max_marginal_B_variation = 0.0

    for i, a in enumerate(axes_a):
        marginals_A_for_b = []
        for j, b in enumerate(axes_b):
            e_val = correlation(a, b)
            target = -float(np.dot(a, b))
            max_corr_error = max(max_corr_error, abs(e_val - target))
            ma_plus = marginal_A(1, a, b)
            mb_plus = marginal_B(1, a, b)
            marginals_A_for_b.append(ma_plus)
            rows.append((i, j, float(np.dot(a, b)), e_val, target, ma_plus, mb_plus))
        max_marginal_A_variation = max(
            max_marginal_A_variation,
            max(marginals_A_for_b) - min(marginals_A_for_b),
        )

    for b in axes_b:
        vals = [marginal_B(1, a, b) for a in axes_a]
        max_marginal_B_variation = max(max_marginal_B_variation, max(vals) - min(vals))

    sv = schmidt_singular_values_singlet()
    factorable_rank_one_error = float(min(abs(sv[0]), abs(sv[1])))
    chsh = chsh_value()

    table = "\n".join(
        f"| {i} | {j} | {dot:.12f} | {e:.12f} | {target:.12f} | {ma:.12f} | {mb:.12f} |"
        for i, j, dot, e, target, ma, mb in rows
    )

    text = f"""# Output — reduced entanglement and no-signalling

Classification: reduced operational consistency test.

## Non-factorization

Schmidt singular values of the singlet:

| index | value |
|---:|---:|
| 0 | {sv[0]:.12f} |
| 1 | {sv[1]:.12f} |

Since both values are non-zero, the state does not have Schmidt rank 1 and is not
a product state. The smallest preserved singular value is:

$$
{factorable_rank_one_error:.12f}.
$$

## Correlation and marginals

| axis A | axis B | $a\\cdot b$ | $E(a,b)$ | target $-a\\cdot b$ | $P(+|a,b)$ in A | $P(+|a,b)$ in B |
|---:|---:|---:|---:|---:|---:|---:|
{table}

## Errors

| test | value |
|---|---:|
| maximum error in $E(a,b)+a\\cdot b$ | {max_corr_error:.12e} |
| maximum variation of marginal A when changing B | {max_marginal_A_variation:.12e} |
| maximum variation of marginal B when changing A | {max_marginal_B_variation:.12e} |
| reduced CHSH value | {chsh:.12f} |
| target $-2\\sqrt 2$ | {-2.0*np.sqrt(2.0):.12f} |

## Interpretation

The test shows that the joint correlation depends on both axes, but the
local marginals remain equal to $1/2$. This is operational compatibility
with no-signalling in the reduced projective sector. The complete GDQ must
still derive real apparatuses via $K_{{AB}}^{{\\rm phys}}$, $\\text{{R}}_A$, and
$\\text{{R}}_B$.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
