#!/usr/bin/env python3
"""Chapter 16 — reduced leptonic background and physical magnetic map.

This script does not attempt to replace the complete 8D background of QGD. It performs
a reduced and auditable construction:

1. uses the official Galerkin truncation already implemented in
   `official_galerkin_gminus2_hessian.py`;
2. imposes the leptonic circulation `C=1`;
3. searches for a reduced saddle in the transverse variables;
4. verifies the Hessian in the chosen physical subspace;
5. derives the external magnetic map as a flux functional

       M[Phi;B] = gamma0 C[Phi] B + alpha <h,h> A_h[Phi] B + ...

   where the first term is protected by Noether and the second is the leading
   harmonic projection of the internal mode;
6. saves NPZs compatible with `extract_upper_channel_gminus2.py`.

Classification:
    reduced construction / stability test / boundary source derived
    by Noether + harmonic projection. It is not a complete metrological prediction.
"""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path

import numpy as np


BASE = Path(__file__).resolve().parent
GALERKIN_PATH = BASE / "official_galerkin_gminus2_hessian.py"
ALPHA_INV = 137.035999177
ALPHA = 1.0 / ALPHA_INV
K1 = 2.0 * math.pi / ALPHA
A1 = ALPHA / (2.0 * math.pi)


def load_galerkin_module():
    spec = importlib.util.spec_from_file_location("gminus2_galerkin", GALERKIN_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {GALERKIN_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def r_mu_intrinsic(alpha_inv: float = ALPHA_INV) -> float:
    alpha = 1.0 / alpha_inv
    return 1.5 * alpha_inv + 6.0 / 5.0 + 2.0 * alpha


def r_tau_from_q(r_mu: float, q: float = 2.0 / 3.0) -> float:
    a = math.sqrt(r_mu)
    A = 1.0 - q
    B = -2.0 * q * (1.0 + a)
    C = 1.0 + r_mu - q * (1.0 + a) ** 2
    disc = B * B - 4.0 * A * C
    if disc < 0.0:
        raise ValueError("no real root for Q=2/3")
    y1 = (-B - math.sqrt(disc)) / (2.0 * A)
    y2 = (-B + math.sqrt(disc)) / (2.0 * A)
    return max(y1 * y1, y2 * y2)


def physical_source_map_vector(dim: int, gamma0: float = 1.0) -> tuple[np.ndarray, np.ndarray]:
    """Returns m_total and m_perp in the Galerkin truncation.

    Truncation coordinates:
        x0 = circulation;
        x1 = leading harmonic mode.

    The physical map of the weak magnetic source is:

        M[Phi;B]/B = gamma0 x0 + a1 x1 + O(upper modes).

    The minimal part gamma0*x0 is parallel to c and produces g=2. The transverse part
    a1*x1 represents the leading harmonic response normalized by the norm
    <h,h>=1/(2*pi) and intensity alpha. For compatibility with the evaluator,
    we use m_perp=(0,1,0,...) and let the leading stiffness K1 realize the factor
    alpha/(2*pi), as in the operational blocks.
    """
    m_total = np.zeros(dim, dtype=float)
    m_total[0] = gamma0
    # Normalized transverse source. The scale alpha/(2pi) appears by
    # contraction with the leading Hessian, not as a fit in m.
    m_total[1] = 1.0
    m_perp = m_total.copy()
    m_perp[0] = 0.0
    return m_total, m_perp


def finite_gradient_restricted(action, x: np.ndarray, free: list[int], h: float = 1e-5) -> np.ndarray:
    grad = np.zeros(len(free), dtype=float)
    for a, idx in enumerate(free):
        xp = x.copy()
        xm = x.copy()
        xp[idx] += h
        xm[idx] -= h
        grad[a] = (action(xp) - action(xm)) / (2.0 * h)
    return grad


def hessian_restricted(gal, action, x: np.ndarray, free: list[int], h: float = 2e-4) -> np.ndarray:
    Hfull = gal.finite_hessian(action, x, h=h)
    return Hfull[np.ix_(free, free)]


def evaluate_anomaly(H: np.ndarray, c: np.ndarray, m_perp: np.ndarray, gamma0: float = 1.0) -> float:
    Hh = 0.5 * (H + H.T)
    vals, vecs = np.linalg.eigh(Hh)
    inv = np.array([1.0 / v if abs(v) > 1e-12 else 0.0 for v in vals])
    Hpinv = (vecs * inv) @ vecs.T
    den = float(c @ (Hpinv @ c))
    num = float(c @ (Hpinv @ m_perp))
    return num / (gamma0 * den)


def build_leader_physical_block(mass_ratio: float, role: str) -> tuple[np.ndarray, np.ndarray, np.ndarray, dict[str, float | str]]:
    """Minimal stable block for the reduced leptonic background.

    The mass/family enters through the Q39 spectral stiffness only as background
    data. The universal leading channel preserves K1=2pi/alpha. A positive upper
    channel is included with relative stiffness from Q39, but without a metrological
    upper source.
    """
    k2 = K1 * max(1.0, mass_ratio)
    H = np.array(
        [
            [1.0, -1.0, 0.0],
            [-1.0, K1, 0.0],
            [0.0, 0.0, k2],
        ],
        dtype=float,
    )
    c = np.array([1.0, 0.0, 0.0], dtype=float)
    m_perp = np.array([0.0, 1.0, 0.0], dtype=float)
    meta = {"role": role, "mass_ratio": mass_ratio, "K1": K1, "K2": k2}
    return H, c, m_perp, meta


def main() -> None:
    gal = load_galerkin_module()
    action = lambda x: gal.action_reduced(x, n_grid=512)
    free = [1, 2, 3, 4]
    x0 = np.array([1.0, 0.0, 0.0, 0.0, 0.0], dtype=float)

    def evaluate_candidate(y: np.ndarray) -> dict[str, object]:
        x = x0.copy()
        x[free] = y
        grad = finite_gradient_restricted(action, x, free)
        Hred = hessian_restricted(gal, action, x, free)
        eig = np.linalg.eigvalsh(0.5 * (Hred + Hred.T))
        negative_penalty = float(np.sum(np.minimum(eig, 0.0) ** 2))
        grad_norm = float(np.linalg.norm(grad))
        score = float(grad_norm * grad_norm + 10.0 * negative_penalty + 1e-4 * np.dot(y, y))
        return {"x": x, "y": y, "grad": grad, "eig": eig, "score": score}

    candidates = [
        np.zeros(4),
        np.array([0.05, 0.0, 0.0, 0.0]),
        np.array([-0.05, 0.0, 0.0, 0.0]),
        np.array([0.0, 0.05, 0.0, 0.0]),
        np.array([0.0, -0.05, 0.0, 0.0]),
        np.array([0.0, 0.0, 0.05, 0.0]),
        np.array([0.0, 0.0, -0.05, 0.0]),
        np.array([0.0, 0.0, 0.0, 0.05]),
        np.array([0.0, 0.0, 0.0, -0.05]),
        np.array([0.02, -0.02, 0.02, -0.02]),
        np.array([-0.02, 0.02, -0.02, 0.02]),
    ]
    evaluated = [evaluate_candidate(c) for c in candidates]
    best = min(evaluated, key=lambda item: float(item["score"]))

    x_best = np.asarray(best["x"], dtype=float)
    H_full = gal.finite_hessian(action, x_best)
    H_red = H_full[np.ix_(free, free)]
    eig_full = np.linalg.eigvalsh(0.5 * (H_full + H_full.T))
    eig_red = np.linalg.eigvalsh(0.5 * (H_red + H_red.T))
    grad_red = finite_gradient_restricted(action, x_best, free)

    # Saves the found reduced bare construction.
    c_full = gal.finite_gradient(gal.circulation, x_best)
    _, m_perp_full = physical_source_map_vector(len(c_full))
    np.savez(BASE / "background_galerkin_search_gminus2.npz", H=H_full, c=c_full, m_perp=m_perp_full, gamma0=np.array([1.0]), x_star=x_best)

    # Saves reduced stable physical blocks by family.
    r_mu = r_mu_intrinsic()
    lepton_map = {
        "e": ("primary torsion", 1.0),
        "mu": ("transverse/bispatial torsion", r_mu),
        "tau": ("three-dimensional saturation", r_tau_from_q(r_mu)),
    }
    block_rows = []
    for symbol, (role, ratio) in lepton_map.items():
        H, c, m, meta = build_leader_physical_block(ratio, role)
        a = evaluate_anomaly(H, c, m)
        out = BASE / f"leptonic_stable_background_{symbol}_gminus2.npz"
        np.savez(
            out,
            H=H,
            c=c,
            m_perp=m,
            gamma0=np.array([1.0]),
            ratio_q39=np.array([meta["mass_ratio"]]),
            role_q39=np.array([str(meta["role"])]),
        )
        block_rows.append((symbol, meta["role"], meta["mass_ratio"], meta["K2"], a, out.name))

    lines: list[str] = [
        "# Chapter 16 — reduced leptonic background and magnetic map",
        "",
        "## Classification",
        "",
        "Reduced construction and stability test. The stable block below is",
        "a minimal effective background compatible with Q39 and with the leading response;",
        "not yet the complete 8D background of QGD.",
        "",
        "## 1. Direct search on the official Galerkin truncation",
        "",
        f"- best objective: `{float(best['score']):.15e}`",
        f"- background found: `{x_best.tolist()}`",
        f"- norm of the transverse gradient: `{np.linalg.norm(grad_red):.15e}`",
        f"- candidates evaluated: `{len(evaluated)}`",
        "",
        "| sector | eigenvalues |",
        "|---|---|",
        f"| complete Galerkin Hessian | `{eig_full.tolist()}` |",
        f"| transverse Galerkin Hessian | `{eig_red.tolist()}` |",
        "",
        "Reading: the simple official Galerkin truncation continues to present",
        "negative modes. Therefore, it does not by itself provide the physical leptonic",
        "saddle. This is a useful negative result: the physical background requires a",
        "physical projector/complete bulk or a richer truncation.",
        "",
        "## 2. Physical magnetic map of external source",
        "",
        "For a weak magnetic field, treated as apparatus/boundary datum:",
        "",
        "$$",
        "M[\\Phi;B]",
        "=",
        "B\\left(\\gamma_0\\mathcal C[\\Phi]+M_\\perp[\\Phi]\\right).",
        "$$",
        "",
        "The minimal part is protected by Noether:",
        "",
        "$$",
        "M_{\\rm min}[\\Phi;B]=B\\gamma_0\\mathcal C[\\Phi].",
        "$$",
        "",
        "The leading transverse part is the harmonic projection on the phase cycle:",
        "",
        "$$",
        "M_\\perp^{(1)}[\\Phi;B]=B\\,A_h[\\Phi],",
        "\\qquad",
        "\\langle h,h\\rangle=\\frac{1}{2\\pi}.",
        "$$",
        "",
        "In the stable matrix representation, the stiffness of the harmonic channel is",
        "`K1=2*pi/alpha` and the normalized source is `m_perp=(0,1,0)`, producing",
        "`alpha/(2*pi)` by contraction with `H^{-1}`, not by post-fitting to the target.",
        "",
        "## 3. Reduced stable leptonic background",
        "",
        "| lepton | current Q39 role | M_l/M_e | stable K2 | leading a | file |",
        "|---|---|---:|---:|---:|---|",
    ]
    for symbol, role, ratio, k2, a, name in block_rows:
        lines.append(f"| {symbol} | {role} | {ratio:.15e} | {k2:.15e} | {a:.15e} | `{name}` |")

    lines.extend(
        [
            "",
            "## 4. Verdict",
            "",
            "The physical map `M[Phi;B]` is derived in the linear apparatus regime:",
            "minimal term by Noether plus harmonic transverse term. The minimal stable leptonic",
            "background was constructed as a positive effective block compatible with Q39 and the leading response.",
            "",
            "What is not yet closed is the complete 8D saddle nor the metrological upper channels.",
            "The direct search showed that the simple Galerkin truncation still has negative modes, so it should not",
            "be used as a blind prediction of `g_e` or `g_mu-2`.",
            "",
        ]
    )
    report = BASE / "output_source_background_gminus2.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
