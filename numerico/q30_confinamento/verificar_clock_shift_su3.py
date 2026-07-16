#!/usr/bin/env python3
"""Verifica o par clock-shift e seu comutante em su(3)."""

import numpy as np

omega = np.exp(2j * np.pi / 3)
P = np.diag([1.0, omega, omega**2]).astype(complex)
Q = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)

print(f"det_P={np.linalg.det(P):.12g}")
print(f"det_Q={np.linalg.det(Q):.12g}")
print(f"clock_shift_residual={np.linalg.norm(P @ Q - omega**2 * Q @ P):.3e}")

# X P=P X e X Q=Q X como sistema linear complexo em vec(X).
identity = np.eye(3, dtype=complex)
system = np.vstack(
    [
        np.kron(P.T, identity) - np.kron(identity, P),
        np.kron(Q.T, identity) - np.kron(identity, Q),
    ]
)
singular_values = np.linalg.svd(system, compute_uv=False)
nullity_complex = int(np.sum(singular_values < 1e-10))
print(f"commutant_complex_dimension={nullity_complex}")
print("commutant_su3_dimension=0")

if np.linalg.norm(P @ Q - omega**2 * Q @ P) > 1e-10:
    raise SystemExit("Falha na relação clock-shift.")
if nullity_complex != 1:
    raise SystemExit("O comutante não é apenas escalar.")
