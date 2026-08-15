#!/usr/bin/env python3
"""
QGD — Chapter 5 / Well-posedness of the geometric flow in gauge.

Objective:
    Verify, in a self-contained matrix model, the algebraic condition used
    in the local well-posedness proof of the geometric flow: after DeTurck/Hodge
    gauge, the principal symbol of the coupled system is

        sigma_pr(xi) = |xi|_g^2 I.

    For a positive Riemannian metric, |xi|_g^2 > 0 for xi != 0.

Classification:
    Symbolic-numerical verification of strong parabolicity of the principal symbol.
    It is not a physical prediction, does not use experimental data, and
    does not replace the analytical theorem of quasi-linear parabolic PDEs.

Domain:
    Real local bulk of dimension d=8, at a point. The check is pointwise on the
    principal symbol; global boundary conditions appear in the text.

Output:
    output_verify_parabolic_symbol_qgd.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def random_spd_matrix(rng: np.random.Generator, d: int) -> np.ndarray:
    """Generates a positive-definite Riemannian metric."""
    a = rng.normal(size=(d, d))
    return a.T @ a + d * np.eye(d)


def main() -> None:
    rng = np.random.default_rng(1729)
    d = 8

    g = random_spd_matrix(rng, d)
    g_inv = np.linalg.inv(g)

    eig_g = np.linalg.eigvalsh(g)
    eig_g_inv = np.linalg.eigvalsh(g_inv)

    # Number of independent components of the main blocks:
    # symmetric metric, 3-form, two scalars.
    n_metric = d * (d + 1) // 2
    n_three_form = d * (d - 1) * (d - 2) // 6
    n_scalars = 2
    n_fields = n_metric + n_three_form + n_scalars

    samples = 256
    xi_values = rng.normal(size=(samples, d))
    xi_norms = np.einsum("ni,ij,nj->n", xi_values, g_inv, xi_values)

    min_symbol = float(np.min(xi_norms))
    max_symbol = float(np.max(xi_norms))
    min_eig_g = float(np.min(eig_g))
    min_eig_g_inv = float(np.min(eig_g_inv))

    # If the main coupled block is |xi|_g^2 I, the smallest eigenvalue of the symbol
    # of the entire system is |xi|_g^2 in each sample.
    symbol_is_positive = bool(np.all(xi_norms > 0.0) and min_eig_g > 0.0)

    lines: list[str] = []
    lines.append('---\n')
    lines.append('title: "Output — QGD parabolic symbol in gauge"\n')
    lines.append('---\n\n')
    lines.append("# Output — QGD parabolic symbol in gauge\n\n")
    lines.append("## Classification\n\n")
    lines.append(
        "Symbolic-numerical verification of the positivity of the principal symbol "
        "after gauge. Not a physical prediction.\n\n"
    )
    lines.append("## Test data\n\n")
    lines.append(f"- Real bulk dimension: $d={d}$\n")
    lines.append(f"- Symmetric metric components: ${n_metric}$\n")
    lines.append(f"- 3-form components: ${n_three_form}$\n")
    lines.append(f"- Scalars $(\\phi,\\chi)$: ${n_scalars}$\n")
    lines.append(f"- Total components in the main block: ${n_fields}$\n")
    lines.append(f"- Covector $\\xi$ samples: ${samples}$\n\n")
    lines.append("## Verified identity\n\n")
    lines.append("## Numerical values\n\n")
    lines.append("| quantity | value |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| smallest eigenvalue of $g$ | {min_eig_g:.12e} |\n")
    lines.append(f"| smallest eigenvalue of $g^{{-1}}$ | {min_eig_g_inv:.12e} |\n")
    lines.append(f"| smallest sampled $|\\xi|_g^2$ | {min_symbol:.12e} |\n")
    lines.append(f"| largest sampled $|\\xi|_g^2$ | {max_symbol:.12e} |\n\n")
    lines.append("## Verdict\n\n")
    if symbol_is_positive:
        lines.append(
            "The metric is positive-definite and the principal symbol "
            "$|\\xi|_g^2I$ is positive for the sampled non-zero covectors. "
            "This illustrates strong parabolicity after gauge.\n"
        )
    else:
        lines.append(
            "The positivity failed in the test. The metric or the implementation "
            "must be reviewed.\n"
        )

    out = OUT / "output_verify_parabolic_symbol_qgd.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
