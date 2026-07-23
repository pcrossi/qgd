#!/usr/bin/env python3
"""Utilitários do benchmark físico Q25.

Este módulo implementa uma redução GDQ de rede para teste físico mínimo:

- a rede é dado externo do aparelho;
- a medida é positiva;
- a variável binária representa circulação local;
- a antissimetria fermiônica entra como holonomia de troca;
- a Hessiana reduzida é positiva e define a impedância de interface.

Não é uma ação Hubbard fundamental e não usa dados experimentais como ajuste.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import itertools
import json
import math
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
ASSOC = ROOT / "associados"
DATA = ROOT / "dados"
RESULTS = ROOT / "resultados"
CACHE = RESULTS / "q25_physical_cache"


@dataclass(frozen=True)
class PhysicalConfig:
    L: int = 4
    beta_eff: float = 0.45
    kappa_H: float = 0.35
    mass_gap: float = 0.18
    doping: float = 0.0
    seed: int = 2510

    @property
    def n_sites(self) -> int:
        return self.L * self.L


def ensure_dirs() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    CACHE.mkdir(parents=True, exist_ok=True)


def site_index(x: int, y: int, L: int) -> int:
    return (x % L) * L + (y % L)


def lattice_edges(L: int) -> list[tuple[int, int]]:
    edges: list[tuple[int, int]] = []
    for x in range(L):
        for y in range(L):
            i = site_index(x, y, L)
            edges.append((i, site_index(x + 1, y, L)))
            edges.append((i, site_index(x, y + 1, L)))
    # Remove duplicatas de arestas nao orientadas.
    return sorted({tuple(sorted(e)) for e in edges})


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


def gdq_reduced_hessian(cfg: PhysicalConfig) -> np.ndarray:
    """Hessiana positiva no setor de circulação escalonada.

    O setor físico usa x_i = eta_i sigma_i. O termo Laplaciano estabiliza
    suavidade de x; em sigma isso corresponde a correlação antiferro em rede
    bipartida.
    """
    lap = graph_laplacian(cfg.L)
    return cfg.mass_gap * np.eye(cfg.n_sites) + cfg.kappa_H * lap


def hessian_spectrum(cfg: PhysicalConfig) -> np.ndarray:
    return np.linalg.eigvalsh(gdq_reduced_hessian(cfg))


def cayley_scattering(local_k: np.ndarray, holonomy: complex = -1.0 + 0.0j) -> np.ndarray:
    """Matriz de interface unitária a partir da impedância Hermitiana local."""
    k = np.array(local_k, dtype=np.complex128)
    # Insere holonomia fermiônica no canal de transmissão.
    k[0, 1] *= holonomy
    k[1, 0] *= np.conjugate(holonomy)
    eye = np.eye(k.shape[0], dtype=np.complex128)
    return np.linalg.solve(eye + 1j * k, eye - 1j * k)


def local_interface_matrix(cfg: PhysicalConfig, edge: tuple[int, int]) -> np.ndarray:
    h = gdq_reduced_hessian(cfg)
    i, j = edge
    local = h[np.ix_([i, j], [i, j])]
    scale = max(float(np.linalg.norm(local, ord=2)), 1e-12)
    return cayley_scattering(local / scale)


def energy_for_x(x: np.ndarray, cfg: PhysicalConfig, hessian: np.ndarray | None = None) -> float:
    h = gdq_reduced_hessian(cfg) if hessian is None else hessian
    return 0.5 * float(x @ h @ x)


def enumerate_exact(cfg: PhysicalConfig) -> dict[str, object]:
    if cfg.n_sites > 20:
        raise ValueError("enumeracao exata limitada a <=20 sites")
    eta = bipartite_eta(cfg.L)
    h = gdq_reduced_hessian(cfg)
    corr_acc = {1: 0.0, 2: 0.0}
    count_acc = {1: 0, 2: 0}
    z = 0.0
    e_acc = 0.0
    weights: list[float] = []
    configs: list[np.ndarray] = []

    for bits in itertools.product([-1.0, 1.0], repeat=cfg.n_sites):
        x = np.array(bits, dtype=float)
        e = energy_for_x(x, cfg, h)
        w = math.exp(-cfg.beta_eff * e)
        z += w
        e_acc += w * e
        weights.append(w)
        configs.append(x)

        sigma = eta * x
        for r in (1, 2):
            vals = []
            for sx in range(cfg.L):
                for sy in range(cfg.L):
                    i = site_index(sx, sy, cfg.L)
                    j = site_index(sx + r, sy, cfg.L)
                    vals.append(sigma[i] * sigma[j])
                    j = site_index(sx, sy + r, cfg.L)
                    vals.append(sigma[i] * sigma[j])
            corr_acc[r] += w * float(np.mean(vals))
            count_acc[r] += 1

    probs = np.array(weights, dtype=float) / z
    entropy = float(-np.sum(probs * np.log(np.maximum(probs, 1e-300))))
    return {
        "Z": z,
        "mean_energy": e_acc / z,
        "C_s_r1": corr_acc[1] / z,
        "C_s_r2": corr_acc[2] / z,
        "entropy": entropy,
        "n_config": len(configs),
    }


def metropolis_correlations(cfg: PhysicalConfig, steps: int = 120_000, burn: int = 20_000) -> dict[str, float]:
    rng = np.random.default_rng(cfg.seed)
    eta = bipartite_eta(cfg.L)
    h = gdq_reduced_hessian(cfg)
    x = rng.choice([-1.0, 1.0], size=cfg.n_sites)
    e = energy_for_x(x, cfg, h)
    samples_r1 = []
    samples_r2 = []
    energies = []
    accepts = 0
    total = 0

    def corr(sigma: np.ndarray, r: int) -> float:
        vals = []
        for sx in range(cfg.L):
            for sy in range(cfg.L):
                i = site_index(sx, sy, cfg.L)
                vals.append(sigma[i] * sigma[site_index(sx + r, sy, cfg.L)])
                vals.append(sigma[i] * sigma[site_index(sx, sy + r, cfg.L)])
        return float(np.mean(vals))

    for t in range(steps):
        i = int(rng.integers(cfg.n_sites))
        x_new = x.copy()
        x_new[i] *= -1.0
        e_new = energy_for_x(x_new, cfg, h)
        if e_new <= e or rng.random() < math.exp(-cfg.beta_eff * (e_new - e)):
            x = x_new
            e = e_new
            accepts += 1
        total += 1
        if t >= burn:
            sigma = eta * x
            samples_r1.append(corr(sigma, 1))
            samples_r2.append(corr(sigma, 2))
            energies.append(e)

    r1 = np.array(samples_r1)
    r2 = np.array(samples_r2)
    en = np.array(energies)
    return {
        "steps": float(steps),
        "burn": float(burn),
        "acceptance": accepts / max(total, 1),
        "C_s_r1": float(r1.mean()),
        "C_s_r1_stderr": float(r1.std(ddof=1) / math.sqrt(len(r1))),
        "C_s_r2": float(r2.mean()),
        "C_s_r2_stderr": float(r2.std(ddof=1) / math.sqrt(len(r2))),
        "mean_energy": float(en.mean()),
        "energy_stderr": float(en.std(ddof=1) / math.sqrt(len(en))),
    }


def integrated_autocorr(x: np.ndarray, max_lag: int = 1000) -> float:
    x = np.asarray(x, dtype=float)
    x = x - x.mean()
    denom = float(np.dot(x, x))
    if denom <= 0.0:
        return 0.5
    tau = 0.5
    for lag in range(1, min(max_lag, len(x) - 1)):
        ac = float(np.dot(x[:-lag], x[lag:]) / denom)
        if ac <= 0.0:
            break
        tau += ac
    return tau


def save_json(path: Path, obj: object) -> None:
    ensure_dirs()
    path.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def markdown_table(rows: list[tuple[str, object]]) -> str:
    out = "| item | valor |\n|---|---:|\n"
    for k, v in rows:
        if isinstance(v, float):
            out += f"| {k} | {v:.12e} |\n"
        else:
            out += f"| {k} | {v} |\n"
    return out
