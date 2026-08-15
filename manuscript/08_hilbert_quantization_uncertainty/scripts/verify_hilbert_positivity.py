#!/usr/bin/env python3
"""
Objective:
    Self-contained verification of `verify hilbert positivity` associated with chapter `08_hilbert_quantization_uncertainty`.

Toy model of positivity and quotient by zero norm.

A positive semidefinite form G defines a norm, but vectors in the kernel have
zero norm. The physical space is the quotient by the kernel.
"""

from pathlib import Path
import numpy as np

OUT = Path(__file__).with_name("output_verify_hilbert_positivity.md")


def main() -> None:
    G = np.diag([2.0, 1.0, 0.0])
    vals = np.linalg.eigvalsh(G)
    rank = np.linalg.matrix_rank(G, tol=1e-12)
    examples = [
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
        np.array([1.0, 1.0, 3.0]),
    ]
    lines = [
        "---",
        'title: "Output — positivity and quotient"',
        "---",
        "",
        "# Output — positivity and quotient",
        "",
        "Classification: algebraic toy model.",
        "",
        f"Eigenvalues of the form: `{vals}`.",
        "",
        f"Physical rank after quotient by the kernel: `{rank}`.",
        "",
        "| vector | squared norm |",
        "|---|---:|",
    ]
    for v in examples:
        norm = float(v @ G @ v)
        lines.append(f"| `{v.tolist()}` | {norm:.8f} |")
    lines += [
        "",
        "Conclusion: zero-norm vectors must be quotiented out before Hilbertian",
        "completion, as in $\\mathcal D_+/(\\mathcal N+\\mathcal G)$.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
