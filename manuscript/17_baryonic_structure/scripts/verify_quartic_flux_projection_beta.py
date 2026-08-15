#!/usr/bin/env python3
"""GDQ — Chapter 17 / Flux projector and quartic Schur complement."""

from __future__ import annotations

from pathlib import Path

import sympy as sp


def main() -> None:
    c1, c2 = sp.symbols("c1 c2", real=True, nonzero=True)
    constraint = sp.Matrix([[c1, c2]])
    projector = sp.eye(2) - constraint.T * (constraint * constraint.T).inv() * constraint
    projector_residual = sp.simplify(projector * projector - projector)
    constraint_residual = sp.simplify(constraint * projector)

    q, u, e0 = sp.symbols("q u E0")
    energy = e0 * sp.exp(-u * q)
    jets = [sp.diff(energy, q, order).subs(q, 0) for order in range(2, 5)]

    xi, k, g, v4 = sp.symbols("xi K G V4", nonzero=True)
    action = k * xi**2 / 2 + g * xi * q**2 / 2 + v4 * q**4 / 24
    xi_solution = -g * q**2 / (2 * k)
    reduced = sp.expand(action.subs(xi, xi_solution))
    effective_v4 = sp.expand(24 * reduced.coeff(q, 4))
    expected_v4 = v4 - 3 * g**2 / k
    residual_v4 = sp.simplify(effective_v4 - expected_v4)

    lines = [
        "# Output — flux projection and quartic Schur beta",
        "",
        "Classification: symbolic test of the physical projector and reduced fourth variation.",
        "",
        f"- `P_Q^2 - P_Q = {projector_residual}`",
        f"- `D C P_Q = {constraint_residual}`",
        f"- `(E_T'', E_T''', E_T'''') = {tuple(jets)}`",
        f"- `V4_eff = {effective_v4}`",
        f"- `residue V4_eff - (V4 - 3G^2/K) = {residual_v4}`",
        "",
        "Conclusion: the Schur complement reduces the fourth variation by `-3G^2/K` in the elementary channel.",
        "",
    ]
    out = Path(__file__).with_name("output_verify_quartic_flux_projection_beta.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
