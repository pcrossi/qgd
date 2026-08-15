#!/usr/bin/env python3
"""GDQ — Chapter 16: Schur/DtN diagnostic test for alpha.

Classification:
    consistency test / geometric diagnostic without adjustment.

The script evaluates the reduced impedance of a radial photonic channel coupled to
a round Dirichlet-to-Neumann impedance of the S^3 link. This test does not close
alpha; it shows the correct scale of the boundary impedance and records the
deviation of the round class in relation to the Einstein cosmological mean.
"""

from __future__ import annotations

import math
from pathlib import Path


K_BASE = 41.594825709
DELTA_B = -0.2709378871
RADIUS = 1.998411184770


def eigenvalues_2x2(a: float, b: float, d: float) -> tuple[float, float]:
    """Real eigenvalues of [[a,b],[b,d]] without relying on external libraries."""

    trace = a + d
    det_part = math.sqrt((a - d) ** 2 + 4.0 * b**2)
    return ((trace - det_part) / 2.0, (trace + det_part) / 2.0)


def main() -> None:
    alpha_mean = 9.0 / (8.0 * math.pi**4) * (math.pi**5 / 1920.0) ** 0.25
    z_mean = 1.0 / (4.0 * math.pi * alpha_mean)

    # Neutral radial photonic kernel preserved in the reduced diagnostic.
    k0 = K_BASE / 2.0 * (1.0 + DELTA_B)

    # Round DtN of the first harmonic on a 4-ball with S^3 boundary.
    k_boundary = math.pi**2 * RADIUS**2

    # Schur complement for two channels coupled by boundary impedance.
    z_reduced = k0 * k_boundary / (k0 + k_boundary)
    alpha_dtn_inv = 4.0 * math.pi * z_reduced

    # Boundary value that would exactly equal the cosmological mean; recorded
    # only as a diagnostic, not as a parameter used in the calculation.
    s_required = k0 / z_mean - 1.0
    k_boundary_required = k0 / s_required

    eig_min, eig_max = eigenvalues_2x2(
        k0 + k_boundary,
        -k_boundary,
        k_boundary,
    )

    text = f"""# Output — Schur/DtN test for alpha

Classification: consistency test / geometric diagnostic without adjustment.

| quantity | value |
|---|---:|
| radial photonic $K_0$ | {k0:.12f} |
| $K_\\partial^{{\\rm DtN}}=\\pi^2R^2$ | {k_boundary:.12f} |
| $Z_{{Q,\\rm red}}^E=K_0K_\\partial/(K_0+K_\\partial)$ | {z_reduced:.12f} |
| $(\\alpha_{{\\rm DtN}}^{{\\rm red}})^{{-1}}$ | {alpha_dtn_inv:.12f} |
| Einstein mean $Z_Q^E$ | {z_mean:.12f} |
| $(\\alpha_E^{{\\rm mean}})^{{-1}}$ | {1.0 / alpha_mean:.12f} |
| relative error in $Z_Q$ | {(z_reduced / z_mean - 1.0) * 100.0:.6f}% |
| $K_\\partial$ required by the mean | {k_boundary_required:.12f} |
| DtN/required deviation | {(k_boundary / k_boundary_required - 1.0) * 100.0:.6f}% |
| smallest eigenvalue of the reduced Hessian | {eig_min:.12f} |
| largest eigenvalue of the reduced Hessian | {eig_max:.12f} |

Interpretation: the round test has a positive Hessian and produces the correct scale,
but does not coincide exactly with the cosmological mean. The final result used in the
text is the Einstein mean; this test remains as a diagnostic of the DtN route.
"""

    assert eig_min > 0.0
    out = Path(__file__).resolve().parent / "output_test_schur_dtn_alpha.md"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
