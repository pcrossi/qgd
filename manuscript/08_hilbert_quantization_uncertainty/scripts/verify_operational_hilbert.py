#!/usr/bin/env python3
"""
Reduced verification of the operational Hilbert reconstruction.

Classification:
    Algebraic-numerical consistency test.

What this script verifies:
    1. a positive semidefinite form has a null subspace;
    2. the quotient by the kernel produces a physical space of lower dimension;
    3. pure states and normalized density matrices have non-negative Born
       probabilities and unit sum;
    4. Hermitian observables have real expectation values;
    5. evolution via a Hermitian Hamiltonian preserves the norm;
    6. tensor product factorizes the inner product on product states.

What this script does NOT prove:
    - reflection positivity of the full QGD action;
    - existence of a functional measure in all sectors;
    - essential self-adjointness of real physical operators;
    - tensor factorization for interacting solitons.

It is a minimum self-contained model of the algebra that the sectorial
reconstruction must produce after quotienting by null states and redundancies.
"""

from pathlib import Path
import numpy as np

OUT = Path(__file__).with_name("output_verify_operational_hilbert.md")


def unitary_from_hermitian(H: np.ndarray, t: float, hbar: float = 1.0) -> np.ndarray:
    """Calculates exp(-i H t / hbar) via Hermitian spectral decomposition."""
    vals, vecs = np.linalg.eigh(H)
    phases = np.exp(-1j * vals * t / hbar)
    return vecs @ np.diag(phases) @ vecs.conj().T


def main() -> None:
    # Positive semidefinite form on D_+ before the quotient.
    # The third vector is null: it must be removed in the physical space.
    G = np.diag([1.0, 0.5, 0.0])
    evals, evecs = np.linalg.eigh(G)
    positive = evals > 1.0e-12
    null_dim = int((~positive).sum())
    quotient_dim = int(positive.sum())

    # Orthonormal physical base obtained by keeping only positive eigenvectors
    # and rescaling by the weight of the form.
    V = evecs[:, positive] @ np.diag(1.0 / np.sqrt(evals[positive]))
    G_phys = V.conj().T @ G @ V
    quotient_orth_error = float(np.linalg.norm(G_phys - np.eye(quotient_dim)))

    # Pure state in the 2-dimensional physical space.
    psi = np.array([1.0 + 0.0j, 2.0 - 1.0j])
    psi = psi / np.linalg.norm(psi)
    rho = np.outer(psi, psi.conj())
    trace_rho = np.trace(rho)
    rho_evals = np.linalg.eigvalsh(rho)

    # Hermitian observable and its spectral projectors.
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    obs_vals, obs_vecs = np.linalg.eigh(sigma_z)
    probs = []
    for k in range(len(obs_vals)):
        v = obs_vecs[:, k]
        P = np.outer(v, v.conj())
        probs.append(float(np.real(np.trace(rho @ P))))
    prob_sum_error = abs(sum(probs) - 1.0)
    min_prob = min(probs)
    expectation = np.trace(rho @ sigma_z)
    expectation_imag = abs(float(np.imag(expectation)))

    # Unitary evolution via Hermitian Hamiltonian.
    H = np.array([[0.7, 0.2 - 0.1j], [0.2 + 0.1j, 1.3]], dtype=complex)
    U = unitary_from_hermitian(H, t=3.7)
    unitarity_error = float(np.linalg.norm(U.conj().T @ U - np.eye(2)))
    norm_error = abs(np.linalg.norm(U @ psi) - np.linalg.norm(psi))

    # Tensor product: factorization of the inner product on product states.
    a = np.array([1.0, 1.0j]) / np.sqrt(2.0)
    b = np.array([2.0, -1.0j])
    b = b / np.linalg.norm(b)
    c = np.array([1.0 - 1.0j, 0.5])
    c = c / np.linalg.norm(c)
    d = np.array([0.25, 1.5j])
    d = d / np.linalg.norm(d)

    lhs = np.vdot(np.kron(a, b), np.kron(c, d))
    rhs = np.vdot(a, c) * np.vdot(b, d)
    tensor_factor_error = abs(lhs - rhs)

    lines = [
        "---",
        'title: "Output — operational Hilbert"',
        "---",
        "",
        "# Output — operational Hilbert",
        "",
        "Classification: algebraic-numerical consistency test.",
        "",
        "This test is not a metrological prediction. It verifies, in finite dimension,",
        "the minimum expected algebra after the operational reconstruction:",
        "quotienting by null states, states, observables, unitary evolution, and",
        "tensor composition.",
        "",
        "## Results",
        "",
        "| Quantity | Value | Criterion |",
        "|---|---:|---|",
        f"| null dimension removed | {null_dim} | $\\ge 1$ in this toy model |",
        f"| physical dimension of the quotient | {quotient_dim} | `2` |",
        f"| orthonormalization error in the quotient | {quotient_orth_error:.3e} | close to zero |",
        f"| $\\operatorname{{Tr}}\\varrho$ | {trace_rho.real:.12f} | `1` |",
        f"| smallest eigenvalue of $\\varrho$ | {rho_evals.min():.3e} | non-negative |",
        f"| smallest spectral probability | {min_prob:.12f} | non-negative |",
        f"| error in the sum of probabilities | {prob_sum_error:.3e} | close to zero |",
        f"| imaginary part of $\\langle A\\rangle$ | {expectation_imag:.3e} | close to zero |",
        f"| unitariety error of $U(t)$ | {unitarity_error:.3e} | close to zero |",
        f"| norm preservation error | {norm_error:.3e} | close to zero |",
        f"| tensor factorization error | {tensor_factor_error:.3e} | close to zero |",
        "",
        "## Interpretation",
        "",
        "The test confirms that once the positive physical space is obtained by",
        "quotienting, the usual operational language follows: normalized states,",
        "positive density matrices, spectral probabilities, unitary evolution via a",
        "Hermitian Hamiltonian, and composition via a tensor product.",
        "",
        "In QGD, this layer is reconstructed from geometry and does not replace",
        "the official action.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
