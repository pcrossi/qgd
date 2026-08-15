#!/usr/bin/env python3
"""
GDQ — Chapter 1 / Variable Nelson-Itô Diffusion.

Goal:
    Numerically verify, in a 1D periodic domain, the differential identities
    used in the stochastic reduction with variable diffusion:

        D(x) = nu0 / Omega(x)

        ∂_t rho = -∂_x(b rho) + ∂_x^2(D rho)

    and the Itô expansion:

        ∂_x^2(D rho) = D rho'' + 2 D' rho' + rho D''.

    It also verifies the shape of the osmotic velocity:

        u = D ∂_x ln rho + ∂_x D
          = D(∂_x ln rho - ∂_x ln Omega).

Theoretical source:
    manuscript/01_initial_problem/01.8 - Universal diffusion and geometric inertia.md
    manuscript/notes/derivations/Nelson variable diffusion in GDQ.md

Classification:
    Symbolic-numerical test of differential identity in a periodic domain.
    Not a physical prediction and does not use experimental data.

Domain and boundary:
    1D circle x ∈ [0, 2π), with spectral differences via FFT and periodicity.

Parameters:
    Universal:
        nu0 = 0.5 in reduced units.
    Apparatus/experiment data:
        none.
    Numerical:
        N = 2048 points; smooth positive rho and Omega profiles.

Output:
    output_verify_variable_ito_diffusion.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def spectral_derivative(values: np.ndarray, order: int = 1) -> np.ndarray:
    """Periodic spectral derivative in [0, 2π)."""
    n = values.size
    k = np.fft.fftfreq(n, d=1.0 / n)
    return np.fft.ifft((1j * k) ** order * np.fft.fft(values)).real


def main() -> None:
    n = 2048
    x = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    nu0 = 0.5

    rho = 1.2 + 0.25 * np.cos(x) + 0.10 * np.sin(2.0 * x)
    omega = 1.5 + 0.20 * np.sin(x) + 0.07 * np.cos(3.0 * x)
    drift = 0.3 * np.sin(x) - 0.1 * np.cos(2.0 * x)

    d = nu0 / omega

    rho_x = spectral_derivative(rho, 1)
    rho_xx = spectral_derivative(rho, 2)
    d_x = spectral_derivative(d, 1)
    d_xx = spectral_derivative(d, 2)

    ito_direct = spectral_derivative(d * rho, 2)
    ito_expanded = d * rho_xx + 2.0 * d_x * rho_x + rho * d_xx
    ito_error = float(np.max(np.abs(ito_direct - ito_expanded)))

    fp_conservative = -spectral_derivative(drift * rho, 1) + ito_direct
    fp_expanded = -spectral_derivative(drift * rho, 1) + ito_expanded
    fp_error = float(np.max(np.abs(fp_conservative - fp_expanded)))

    u_from_d = d * spectral_derivative(np.log(rho), 1) + d_x
    u_from_omega = d * (
        spectral_derivative(np.log(rho), 1)
        - spectral_derivative(np.log(omega), 1)
    )
    u_error = float(np.max(np.abs(u_from_d - u_from_omega)))

    omitted_terms = ito_direct - d * rho_xx
    omitted_norm = float(np.max(np.abs(omitted_terms)))
    ito_norm = float(np.max(np.abs(ito_direct)))
    omitted_relative = omitted_norm / ito_norm

    ok = ito_error < 1e-9 and fp_error < 1e-9 and u_error < 1e-9

    lines: list[str] = []
    lines.append("# Output — variable Nelson--Itô diffusion\n\n")
    lines.append("## Classification\n\n")
    lines.append("Symbolic-numerical test of differential identity in periodic domain. Not a physical prediction.\n\n")
    lines.append("## Tested identities\n\n")
    lines.append("$$\n")
    lines.append("D=\\nu_0\\Omega^{-1}.\n")
    lines.append("$$\n\n")
    lines.append("$$\n")
    lines.append("\\partial_x^2(D\\rho)\n")
    lines.append("=D\\rho''+2D'\\rho'+\\rho D''.\n")
    lines.append("$$\n\n")
    lines.append("$$\n")
    lines.append("u=D\\partial_x\\ln\\rho+\\partial_xD\n")
    lines.append("=D(\\partial_x\\ln\\rho-\\partial_x\\ln\\Omega).\n")
    lines.append("$$\n\n")
    lines.append("## Numerical parameters\n\n")
    lines.append("- Periodic domain: $[0,2\\pi)$\n")
    lines.append(f"- Grid: $N={n}$\n")
    lines.append(f"- $\\nu_0={nu0}$ in reduced units\n\n")
    lines.append("## Maximum errors\n\n")
    lines.append("| test | maximum error |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| Itô expansion | {ito_error:.6e} |\n")
    lines.append(f"| conservative vs expanded Fokker--Planck | {fp_error:.6e} |\n")
    lines.append(f"| variable osmotic velocity | {u_error:.6e} |\n\n")
    lines.append("## Size of omitted terms if $\\Omega$ is treated as constant\n\n")
    lines.append("| quantity | value |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| $\\lVert\\partial_x^2(D\\rho)-D\\rho''\\rVert_\\infty$ | {omitted_norm:.6e} |\n")
    lines.append(f"| fraction relative to complete term | {omitted_relative:.6e} |\n\n")
    lines.append("## Verdict\n\n")
    if ok:
        lines.append("The identities passed. The terms with gradients of $\\Omega$ are necessary when $\\Omega$ varies.\n")
    else:
        lines.append("Some identity failed; check discretization or formulas.\n")
    lines.append("\nNo experimental target was used.\n")

    out = OUT / "output_verify_variable_ito_diffusion.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
