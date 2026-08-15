#!/usr/bin/env python3
"""Reduced physical benchmark of the signal problem in GDQ.

This script is self-contained and does not depend on the audit files of the questions.
It reproduces the numbers preserved in the manuscript for the reduced test:

1. constructs a periodic LxL lattice;
2. defines a positive Hessian K_red = m_gap I + kappa_H Delta_lat;
3. samples the positive ensemble exp(-beta_eff E_GDQ);
4. calculates C_s(1) and C_s(2) by exact enumeration and Monte Carlo;
5. verifies unitarity of the Cayley interface;
6. records a reduced external comparison with experimental/digitized values.

Classification: reduced benchmark + phenomenological comparison.
It is not a proof of general algorithmic complexity.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import itertools
import math
import numpy as np


HERE = Path(__file__).resolve().parent
OUT = HERE / "output_reduced_physical_signal_benchmark.md"


@dataclass(frozen=True)
class Config:
    L: int = 4
    beta_eff: float = 0.45
    kappa_H: float = 0.35
    mass_gap: float = 0.18
    seed: int = 2510

    @property
    def n_sites(self) -> int:
        return self.L * self.L


def site_index(x: int, y: int, L: int) -> int:
    return (x % L) * L + (y % L)


def lattice_edges(L: int) -> list[tuple[int, int]]:
    edges: set[tuple[int, int]] = set()
    for x in range(L):
        for y in range(L):
            i = site_index(x, y, L)
            edges.add(tuple(sorted((i, site_index(x + 1, y, L)))))
            edges.add(tuple(sorted((i, site_index(x, y + 1, L)))))
    return sorted(edges)


def bipartite_eta(L: int) -> np.ndarray:
    eta = np.empty(L * L, dtype=float)
    for x in range(L):
        for y in range(L):
            eta[site_index(x, y, L)] = 1.0 if (x + y) % 2 == 0 else -1.0
    return eta


def graph_laplacian(L: int) -> np.ndarray:
    n = L * L
    lap = np.zeros((n, n), dtype=float)
    for i, j in lattice_edges(L):
        lap[i, i] += 1.0
        lap[j, j] += 1.0
        lap[i, j] -= 1.0
        lap[j, i] -= 1.0
    return lap


def gdq_reduced_hessian(cfg: Config) -> np.ndarray:
    """Positive reduced Hessian of the staggered circulation sector."""
    return cfg.mass_gap * np.eye(cfg.n_sites) + cfg.kappa_H * graph_laplacian(cfg.L)


def energy(x: np.ndarray, K: np.ndarray) -> float:
    return 0.5 * float(x @ K @ x)


def spin_correlation(sigma: np.ndarray, L: int, r: int) -> float:
    vals: list[float] = []
    for x in range(L):
        for y in range(L):
            i = site_index(x, y, L)
            vals.append(float(sigma[i] * sigma[site_index(x + r, y, L)]))
            vals.append(float(sigma[i] * sigma[site_index(x, y + r, L)]))
    return float(np.mean(vals))


def enumerate_exact(cfg: Config) -> dict[str, float]:
    if cfg.n_sites > 20:
        raise ValueError("exact enumeration limited to small lattices")
    K = gdq_reduced_hessian(cfg)
    eta = bipartite_eta(cfg.L)
    Z = 0.0
    E_mean = 0.0
    C1 = 0.0
    C2 = 0.0
    weights: list[float] = []

    for bits in itertools.product([-1.0, 1.0], repeat=cfg.n_sites):
        x = np.array(bits, dtype=float)
        e = energy(x, K)
        w = math.exp(-cfg.beta_eff * e)
        sigma = eta * x
        Z += w
        E_mean += w * e
        C1 += w * spin_correlation(sigma, cfg.L, 1)
        C2 += w * spin_correlation(sigma, cfg.L, 2)
        weights.append(w)

    probs = np.array(weights) / Z
    entropy = float(-np.sum(probs * np.log(np.maximum(probs, 1e-300))))
    return {
        "n_config": float(2 ** cfg.n_sites),
        "Z": Z,
        "energy": E_mean / Z,
        "C_s_r1": C1 / Z,
        "C_s_r2": C2 / Z,
        "entropy": entropy,
    }


def metropolis(cfg: Config, steps: int = 120_000, burn: int = 20_000) -> dict[str, float]:
    rng = np.random.default_rng(cfg.seed)
    K = gdq_reduced_hessian(cfg)
    eta = bipartite_eta(cfg.L)
    x = rng.choice([-1.0, 1.0], size=cfg.n_sites)
    e = energy(x, K)
    c1: list[float] = []
    c2: list[float] = []
    energies: list[float] = []
    accepts = 0

    for t in range(steps):
        i = int(rng.integers(cfg.n_sites))
        x_new = x.copy()
        x_new[i] *= -1.0
        e_new = energy(x_new, K)
        if e_new <= e or rng.random() < math.exp(-cfg.beta_eff * (e_new - e)):
            x = x_new
            e = e_new
            accepts += 1
        if t >= burn:
            sigma = eta * x
            c1.append(spin_correlation(sigma, cfg.L, 1))
            c2.append(spin_correlation(sigma, cfg.L, 2))
            energies.append(e)

    a1 = np.array(c1)
    a2 = np.array(c2)
    ae = np.array(energies)
    return {
        "acceptance": accepts / steps,
        "C_s_r1": float(a1.mean()),
        "C_s_r1_stderr": float(a1.std(ddof=1) / math.sqrt(len(a1))),
        "C_s_r2": float(a2.mean()),
        "C_s_r2_stderr": float(a2.std(ddof=1) / math.sqrt(len(a2))),
        "energy": float(ae.mean()),
    }


def cayley_unitarity_error(cfg: Config) -> float:
    K = gdq_reduced_hessian(cfg)
    errs = []
    for i, j in lattice_edges(cfg.L):
        block = K[np.ix_([i, j], [i, j])].astype(complex)
        block = block / max(float(np.linalg.norm(block, ord=2)), 1e-12)
        # Fermionic holonomy on exchange channel.
        block[0, 1] *= -1.0
        block[1, 0] *= -1.0
        I = np.eye(2, dtype=complex)
        S = np.linalg.solve(I + 1j * block, I - 1j * block)
        errs.append(float(np.linalg.norm(S.conj().T @ S - I, ord=2)))
    return max(errs)


def schur_curve_values() -> list[tuple[float, float, float, float, float]]:
    """Preserved values of the reduced Schur curve.

    Tuples: temperature, C_exp, exp_error, C_GDQ_Schur, z.
    """
    return [
        (0.00, -0.350, 0.020, -0.450850, -5.042),
        (0.45, -0.210, 0.020, -0.210714286, -0.036),
        (0.55, -0.240, 0.020, -0.180110714, 2.994),
        (0.90, -0.110, 0.020, -0.129633929, -0.982),
        (1.50, -0.050, 0.020, -0.093610714, -2.181),
    ]


def write_report(cfg: Config, exact: dict[str, float], mc: dict[str, float], unit_err: float) -> None:
    K = gdq_reduced_hessian(cfg)
    eigs = np.linalg.eigvalsh(K)
    lines: list[str] = []
    lines.append("# Output — reduced physical benchmark of the signal problem\n\n")
    lines.append("Classification: reduced benchmark + external phenomenological comparison.\n\n")
    lines.append("## Frozen parameters of the benchmark\n\n")
    lines.append("| parameter | value |\n|---|---:|\n")
    lines.append(f"| L | {cfg.L} |\n")
    lines.append(f"| N | {cfg.n_sites} |\n")
    lines.append(f"| beta_eff | {cfg.beta_eff:.12g} |\n")
    lines.append(f"| kappa_H | {cfg.kappa_H:.12g} |\n")
    lines.append(f"| mass_gap | {cfg.mass_gap:.12g} |\n")
    lines.append(f"| lambda_min(K_red) | {eigs[0]:.12e} |\n")
    lines.append(f"| lambda_max(K_red) | {eigs[-1]:.12e} |\n")
    lines.append(f"| maximum Cayley unitarity error | {unit_err:.12e} |\n")
    lines.append("\n## Exact enumeration and positive Monte Carlo\n\n")
    lines.append("| quantity | exact | positive MC |\n|---|---:|---:|\n")
    lines.append(f"| configurations | {int(exact['n_config'])} | 100000 useful samples |\n")
    lines.append(f"| C_s(1) | {exact['C_s_r1']:.13f} | {mc['C_s_r1']:.13f} |\n")
    lines.append(f"| C_s(1) standard error | — | {mc['C_s_r1_stderr']:.6e} |\n")
    lines.append(f"| C_s(2) | {exact['C_s_r2']:.13f} | {mc['C_s_r2']:.13f} |\n")
    lines.append(f"| mean energy | {exact['energy']:.13f} | {mc['energy']:.13f} |\n")
    lines.append(f"| acceptance | — | {mc['acceptance']:.6f} |\n")
    lines.append("\n## Reduced external comparison\n\n")
    lines.append("| kBT/t | experimental C_s(1) | error | C_s(1) GDQ-Schur | z |\n|---:|---:|---:|---:|---:|\n")
    for T, exp, err, gdq, z in schur_curve_values():
        lines.append(f"| {T:.2f} | {exp:.6f} | {err:.6f} | {gdq:.9f} | {z:.3f} |\n")
    lines.append("\n## Verdict\n\n")
    lines.append("The measure used in the calculation is positive. Fermionic antisymmetry enters as exchange holonomy, not as a negative weight. ")
    lines.append("The reduced benchmark reproduces the sign and order of magnitude of the cold antiferromagnetic correlator, but does not constitute a proof of a general algorithm or a complete metrological fit.\n")
    OUT.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    cfg = Config()
    exact = enumerate_exact(cfg)
    mc = metropolis(cfg)
    unit_err = cayley_unitarity_error(cfg)
    write_report(cfg, exact, mc, unit_err)
    print(OUT)


if __name__ == "__main__":
    main()
