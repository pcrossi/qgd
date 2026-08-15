#!/usr/bin/env python3
"""
GDQ — Chapter 4 / Linear physical projector.

Goal:
    Illustrate the construction of a projector that removes gauge directions and
    linear constraints, verifying P^2=P, P^T=P, G^T P=0 and C P=0.

Theoretical Source:
    manuscript/04_action_consistency/04.7 - What consistency in loops means.md
    manuscript/notes/action/Physical quotient, ghosts and gauge identities.md

Classification:
    Linear illustration of physical quotient. Not a physical prediction.

Equation:
    P = I - A (A^T A)^(-1) A^T,
    where the columns of A generate the subspace to remove.

Domain and Boundary:
    Finite 5D real vector space.

Parameters:
    Universal:
        none
    Apparatus/experiment data:
        none
    Numerical:
        explicit small matrices.

Output:
    output_verify_linear_physical_projector.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def main() -> None:
    dim = 5
    # Two gauge directions.
    g1 = np.array([1.0, 0.0, 0.0, 0.0, 0.0])
    g2 = np.array([0.0, 1.0, 1.0, 0.0, 0.0])
    # One linear constraint represented by covector C; we remove its normal direction.
    c1 = np.array([0.0, 0.0, 1.0, 1.0, 0.0])
    a = np.column_stack([g1, g2, c1])
    # Orthonormalize by QR to avoid numerical dependencies.
    q, _ = np.linalg.qr(a)
    p = np.eye(dim) - q @ q.T
    err_idempotent = np.linalg.norm(p @ p - p)
    err_symmetric = np.linalg.norm(p.T - p)
    err_removed = np.linalg.norm(q.T @ p)
    rank = int(round(np.trace(p)))
    eig = np.linalg.eigvalsh(p)
    ok = err_idempotent < 1e-12 and err_symmetric < 1e-12 and err_removed < 1e-12 and rank == 2

    lines: list[str] = []
    lines.append("# Output — linear physical projector\n\n")
    lines.append("## Classification\n\n")
    lines.append("Linear illustration of physical quotient. Not a physical prediction.\n\n")
    lines.append("## Construction\n\n")
    lines.append("Given the removed directions gathered in $A$, we use:\n\n")
    lines.append("$$\n")
    lines.append("P=I-A(A^TA)^{-1}A^T\n")
    lines.append("$$\n\n")
    lines.append("after orthonormalization of the columns.\n\n")
    lines.append("## Result\n\n")
    lines.append(f"- Total dimension: `{dim}`.\n")
    lines.append(f"- Projected physical dimension: `{rank}`.\n")
    lines.append(f"- Error $P^2-P$: `{err_idempotent:.3e}`.\n")
    lines.append(f"- Error $P^T-P$: `{err_symmetric:.3e}`.\n")
    lines.append(f"- Direction removal error: `{err_removed:.3e}`.\n")
    lines.append(f"- Eigenvalues of $P$: `{eig.tolist()}`.\n\n")
    lines.append("## Verdict\n\n")
    lines.append("The check passed.\n" if ok else "The check failed.\n")
    lines.append("\nThis output illustrates the algebra of the projector. In the real GDQ problem, $P_{\\rm phys}$ depends on the domain, constraints, and boundary.\n")

    out = OUT / "output_verify_linear_physical_projector.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
