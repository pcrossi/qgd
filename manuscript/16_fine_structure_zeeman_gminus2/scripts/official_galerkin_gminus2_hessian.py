#!/usr/bin/env python3
"""Chapter 16 — official Hessian reduced by Galerkin.

This script executes the 7 steps in an explicit truncation of the official action:

1. defines a reduced background Phi_l;
2. defines fluctuations in g, f, fbar;
3. evaluates the official action with U=e^{-(f+fbar)/2};
4. calculates the raw Hessian by finite differences;
5. defines c=dC/dx for the circulation;
6. shows that m_perp does not come from the action without source/apparatus;
7. saves H, c, m_perp and extracts channels K_i, J_i, mu_i.

Classification:
    official reduced Galerkin / consistency test.

It is not yet a metrological prediction of g-2, because the magnetic source map
M[Phi;B] is not determined by the action without specifying the apparatus coupling.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


ALPHA = 1.0 / 137.035999177
N_COMPLEX = 4
TAU = 1.0
HBAR_OVER_LAMBDA2 = 1.0
Z_KERNEL = 1.0


def grid(n: int = 2048) -> tuple[np.ndarray, float]:
    theta = np.linspace(0.0, 2.0 * math.pi, n, endpoint=False)
    dtheta = theta[1] - theta[0]
    return theta, dtheta


def periodic_derivative(y: np.ndarray, dtheta: float) -> np.ndarray:
    return (np.roll(y, -1) - np.roll(y, 1)) / (2.0 * dtheta)


def periodic_second(y: np.ndarray, dtheta: float) -> np.ndarray:
    return (np.roll(y, -1) - 2.0 * y + np.roll(y, 1)) / (dtheta * dtheta)


def fields(x: np.ndarray, theta: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Returns F=Re f, P=Im f and metric sigma.

    Galerkin coordinates:
        x0: circulation/linear phase in the cycle;
        x1: leading harmonic mode sin(theta);
        x2: upper phase mode sin(2 theta);
        x3: density mode cos(theta) in Re f;
        x4: metric conformal mode cos(theta).
    """
    x0, x1, x2, x3, x4 = x
    F0 = 0.0
    F = F0 + x3 * np.cos(theta)
    P = (x0 * theta / (2.0 * math.pi)) + x1 * np.sin(theta) + x2 * np.sin(2.0 * theta)
    sigma = x4 * np.cos(theta)
    return F, P, sigma


def action_reduced(x: np.ndarray, n_grid: int = 2048) -> float:
    """Reduced QGD action in a periodic angular slice.

    The expression preserves the structure:

        [tau(R + g^{-1} df d fbar) + (f+fbar)/2 - n] U sqrt(g).

    We use a 2D conformal slice to represent the angular block:
        g = exp(2 sigma), sqrt(g)=exp(2 sigma),
        R = -2 exp(-2 sigma) Delta sigma.

    This is a reduced Galerkin, not the complete 8D bulk.
    """
    theta, dtheta = grid(n_grid)
    F, P, sigma = fields(x, theta)
    dF = periodic_derivative(F, dtheta)
    dP = periodic_derivative(P, dtheta)
    lap_sigma = periodic_second(sigma, dtheta)

    g_inv = np.exp(-2.0 * sigma)
    sqrt_g = np.exp(2.0 * sigma)
    ricci_scalar = -2.0 * g_inv * lap_sigma
    grad_term = g_inv * (dF * dF + dP * dP)
    rho = np.exp(-F)
    U = Z_KERNEL * rho

    L0 = TAU * (ricci_scalar + grad_term) + F - N_COMPLEX
    integrand = HBAR_OVER_LAMBDA2 * L0 * U * sqrt_g
    return float(np.sum(integrand) * dtheta)


def circulation(x: np.ndarray) -> float:
    return float(x[0])


def finite_gradient(func, x0: np.ndarray, h: float = 1e-5) -> np.ndarray:
    grad = np.zeros_like(x0, dtype=float)
    for i in range(x0.size):
        xp = x0.copy()
        xm = x0.copy()
        xp[i] += h
        xm[i] -= h
        grad[i] = (func(xp) - func(xm)) / (2.0 * h)
    return grad


def finite_hessian(func, x0: np.ndarray, h: float = 2e-4) -> np.ndarray:
    n = x0.size
    H = np.zeros((n, n), dtype=float)
    f0 = func(x0)
    for i in range(n):
        xp = x0.copy()
        xm = x0.copy()
        xp[i] += h
        xm[i] -= h
        H[i, i] = (func(xp) - 2.0 * f0 + func(xm)) / (h * h)
        for j in range(i + 1, n):
            xpp = x0.copy()
            xpm = x0.copy()
            xmp = x0.copy()
            xmm = x0.copy()
            xpp[i] += h
            xpp[j] += h
            xpm[i] += h
            xpm[j] -= h
            xmp[i] -= h
            xmp[j] += h
            xmm[i] -= h
            xmm[j] -= h
            val = (func(xpp) - func(xpm) - func(xmp) + func(xmm)) / (4.0 * h * h)
            H[i, j] = H[j, i] = val
    return 0.5 * (H + H.T)


def orthogonal_complement(e0: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    basis = []
    n = e0.size
    for k in range(n):
        v = np.zeros(n)
        v[k] = 1.0
        v = v - e0 * np.dot(e0, v)
        for b in basis:
            v = v - b * np.dot(b, v)
        norm = np.linalg.norm(v)
        if norm > tol:
            basis.append(v / norm)
    return np.column_stack(basis)


def extract_channels(H: np.ndarray, c: np.ndarray, m: np.ndarray) -> list[dict[str, float]]:
    e0 = c / np.linalg.norm(c)
    Q = orthogonal_complement(e0)
    HT = Q.T @ H @ Q
    vals, vecs_T = np.linalg.eigh(HT)
    vecs = Q @ vecs_T
    channels = []
    for idx, (eig, e) in enumerate(zip(vals, vecs.T), start=1):
        channels.append(
            {
                "idx": idx,
                "K": float(e @ (H @ e)),
                "J": float(-(e0 @ (H @ e))),
                "mu": float(e @ m),
                "eig": float(eig),
            }
        )
    return channels


def evaluate_anomaly(H: np.ndarray, c: np.ndarray, m: np.ndarray) -> float | None:
    try:
        vals, vecs = np.linalg.eigh(H)
        if np.min(np.abs(vals)) < 1e-12:
            return None
        Hinv = (vecs * (1.0 / vals)) @ vecs.T
        return float((c @ (Hinv @ m)) / (c @ (Hinv @ c)))
    except np.linalg.LinAlgError:
        return None


def main() -> None:
    base = Path(__file__).resolve().parent
    # Background with unit circulation; other modes zeroed.
    x_star = np.array([1.0, 0.0, 0.0, 0.0, 0.0])

    H = finite_hessian(action_reduced, x_star)
    c = finite_gradient(circulation, x_star)

    # The official action without external source does not contain M[Phi;B]. Therefore, the
    # transverse source strictly derived from the naked action is zero.
    m_perp_official_naked = np.zeros_like(c)

    # Leading source already derived by Noether + harmonic projection. This is an
    # apparatus/boundary source, not a new term in the fundamental action.
    m_perp_leader = np.zeros_like(c)
    m_perp_leader[1] = 1.0

    np.savez(base / "official_galerkin_naked_gminus2.npz", H=H, c=c, m_perp=m_perp_official_naked, gamma0=np.array([1.0]))
    np.savez(base / "official_galerkin_leading_gminus2.npz", H=H, c=c, m_perp=m_perp_leader, gamma0=np.array([1.0]))

    channels_naked = extract_channels(H, c, m_perp_official_naked)
    channels_leader = extract_channels(H, c, m_perp_leader)
    eigvals = np.linalg.eigvalsh(H)
    a_naked = evaluate_anomaly(H, c, m_perp_official_naked)
    a_leader_raw = evaluate_anomaly(H, c, m_perp_leader)

    lines = [
        "# Chapter 16 — official reduced Galerkin Hessian",
        "",
        "## Classification",
        "",
        "Official reduced Galerkin / consistency test. It is not a metrological prediction.",
        "",
        "## Coordinates",
        "",
        "| index | mode |",
        "|---:|---|",
        "| 0 | circulation/linear phase in the cycle |",
        "| 1 | leading harmonic mode `sin(theta)` |",
        "| 2 | upper phase mode `sin(2 theta)` |",
        "| 3 | density mode `cos(theta)` in `Re f` |",
        "| 4 | conformal metric mode `cos(theta)` |",
        "",
        "## Eigenvalues of the raw Hessian",
        "",
        "| i | lambda_i |",
        "|---:|---:|",
    ]
    for i, val in enumerate(eigvals):
        lines.append(f"| {i} | {val:.15e} |")

    lines.extend(
        [
            "",
            "## Circulation vector",
            "",
            f"`c = {np.array2string(c, precision=8)}`",
            "",
            "## Transverse source from naked action",
            "",
            "The official action without external source/apparatus does not contain the magnetic functional `M[Phi;B]`.",
            "Therefore, in the naked sector:",
            "",
            "$$",
            "m_{\\perp}^{\\rm naked}=0.",
            "$$",
            "",
            f"- `a_geom_naked = {a_naked}`",
            "",
            "### Channels extracted with naked source",
            "",
            "| channel | K_i | J_i | mu_i | transverse eigenvalue |",
            "|---:|---:|---:|---:|---:|",
        ]
    )
    for ch in channels_naked:
        lines.append(f"| {ch['idx']} | {ch['K']:.15e} | {ch['J']:.15e} | {ch['mu']:.15e} | {ch['eig']:.15e} |")

    lines.extend(
        [
            "",
            "## Leading apparatus/boundary source",
            "",
            "The leading source used in Chapter 16 comes from Noether + harmonic projection and is not a new term in the fundamental action.",
            "In this test, it is represented by the unit vector in mode 1:",
            "",
            f"`m_perp_leader = {np.array2string(m_perp_leader, precision=8)}`",
            "",
            f"- `a_geom_raw_with_leader_source = {a_leader_raw}`",
            "",
            "### Channels extracted with leading source",
            "",
            "| channel | K_i | J_i | mu_i | transverse eigenvalue |",
            "|---:|---:|---:|---:|---:|",
        ]
    )
    for ch in channels_leader:
        lines.append(f"| {ch['idx']} | {ch['K']:.15e} | {ch['J']:.15e} | {ch['mu']:.15e} | {ch['eig']:.15e} |")

    lines.extend(
        [
            "",
            "## Verdict",
            "",
            "The second variation of the reduced official action provides `H` and `c`.",
            "It does not provide magnetic `m_perp` without specifying the external source or boundary condition of the apparatus.",
            "Thus, the coefficients `K_i` and `J_i` can be extracted from the official Galerkin Hessian, but `mu_i` requires the physical map `M[Phi;B]`.",
            "",
            "The complete metrological prediction of `g-2` remains dependent on the construction of the external magnetic coupling on the official leptonic background.",
            "",
        ]
    )

    report = base / "output_official_galerkin_gminus2_hessian.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
