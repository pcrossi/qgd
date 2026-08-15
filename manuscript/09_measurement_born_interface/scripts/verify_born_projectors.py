#!/usr/bin/env python3
"""
GDQ — Chapter 9 / Operational Born Rule

Objective:
    Verify, in finite dimension, that the trace rule produces positive,
    normalized, and additive probabilities for orthogonal projectors.

    The verification also includes:
        - invariance under unitary change of basis;
        - factorization of probabilities in product states;
        - marginals by partial trace in an entangled state.

Theoretical source:
    manuscript/09_measurement_born_interface/notes/operational_born_gleason_trace.md
    manuscript/09_measurement_born_interface/09.3 - Operational probabilities in the reconstructed Hilbert space.md

Classification:
    Operational consistency test. Not a physical prediction.

Output:
    manuscript/09_measurement_born_interface/scripts/output_verify_born_projectors.md
"""

from __future__ import annotations

import numpy as np
from pathlib import Path


def projector(v: np.ndarray) -> np.ndarray:
    v = v / np.linalg.norm(v)
    return np.outer(v, v.conj())


def random_unitary_like() -> np.ndarray:
    """A fixed 3x3 unitary matrix obtained by QR to keep the test reproducible."""
    A = np.array(
        [
            [1.0 + 0.1j, 0.2 - 0.3j, -0.4],
            [0.3, -0.7 + 0.2j, 0.1 + 0.5j],
            [0.2j, 0.4, 0.9 - 0.1j],
        ],
        dtype=complex,
    )
    Q, R = np.linalg.qr(A)
    phases = np.diag(R) / np.abs(np.diag(R))
    return Q * phases.conj()


def partial_trace_B(rho_ab: np.ndarray, dim_a: int, dim_b: int) -> np.ndarray:
    """Partial trace over B for a matrix in H_A otimes H_B."""
    reshaped = rho_ab.reshape(dim_a, dim_b, dim_a, dim_b)
    return np.einsum("abcb->ac", reshaped)


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_verify_born_projectors.md"

    psi = np.array([np.sqrt(0.2), np.sqrt(0.3) * np.exp(0.4j), np.sqrt(0.5) * np.exp(-0.7j)])
    rho = projector(psi)
    basis = np.eye(3, dtype=complex)
    projectors = [projector(basis[:, i]) for i in range(3)]
    probs = np.array([np.trace(rho @ p).real for p in projectors])

    p12 = projectors[0] + projectors[1]
    additivity_error = abs(np.trace(rho @ p12).real - (probs[0] + probs[1]))
    positivity_min = probs.min()
    norm_error = abs(probs.sum() - 1.0)

    U = random_unitary_like()
    rotated_basis = [U[:, i] for i in range(3)]
    rotated_projectors = [projector(v) for v in rotated_basis]
    probs_rotated_trace = np.array([np.trace(rho @ p).real for p in rotated_projectors])
    probs_rotated_amplitude = np.array([abs(np.vdot(v, psi)) ** 2 for v in rotated_basis])
    basis_change_error = float(np.max(np.abs(probs_rotated_trace - probs_rotated_amplitude)))
    rotated_norm_error = abs(probs_rotated_trace.sum() - 1.0)

    # Composite product system: P(A and B) = P(A) P(B).
    psi_a = np.array([np.sqrt(0.35), np.sqrt(0.65) * np.exp(0.2j)], dtype=complex)
    psi_b = np.array([np.sqrt(0.4), np.sqrt(0.6) * np.exp(-0.5j)], dtype=complex)
    rho_a = projector(psi_a)
    rho_b = projector(psi_b)
    rho_ab_product = np.kron(rho_a, rho_b)
    pa = projector(np.array([1.0, 0.0], dtype=complex))
    pb = projector(np.array([0.0, 1.0], dtype=complex))
    p_joint = np.kron(pa, pb)
    joint_product = float(np.trace(rho_ab_product @ p_joint).real)
    product_expected = float(np.trace(rho_a @ pa).real * np.trace(rho_b @ pb).real)
    product_error = abs(joint_product - product_expected)

    # Entangled state: marginals via partial trace.
    bell = np.array([1.0, 0.0, 0.0, 1.0], dtype=complex) / np.sqrt(2.0)
    rho_bell = projector(bell)
    rho_a_marginal = partial_trace_B(rho_bell, dim_a=2, dim_b=2)
    marginal_trace_error = abs(np.trace(rho_a_marginal).real - 1.0)
    marginal_prob_0 = float(np.trace(rho_a_marginal @ pa).real)
    direct_marginal_prob_0 = float(np.trace(rho_bell @ np.kron(pa, np.eye(2))).real)
    marginal_error = abs(marginal_prob_0 - direct_marginal_prob_0)

    text = f"""# Output — verify Born by projectors

Classification: operational consistency test.

## State

Dimension: 3.

## Probabilities

| channel | probability |
|---:|---:|
| 0 | {probs[0]:.12f} |
| 1 | {probs[1]:.12f} |
| 2 | {probs[2]:.12f} |

## Verifications

| test | value |
|---|---:|
| minimum probability | {positivity_min:.12e} |
| normalization error | {norm_error:.12e} |
| additivity error P0+P1 | {additivity_error:.12e} |
| maximum error by unitary change of basis | {basis_change_error:.12e} |
| normalization error in rotated basis | {rotated_norm_error:.12e} |
| factorization error in product state | {product_error:.12e} |
| marginal trace error in entangled state | {marginal_trace_error:.12e} |
| marginal error by partial trace | {marginal_error:.12e} |

Interpretation: the trace rule preserves positivity, normalization, and additivity
for orthogonal alternatives in the reconstructed Hilbert space. It is also compatible
with unitary change of basis, tensor composition, and marginals by partial trace.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
