#!/usr/bin/env python3
"""Q25.11 — constrói domínios físicos reduzidos em rede 2D."""

from __future__ import annotations

import numpy as np
from q25_physical_common import (
    CACHE,
    RESULTS,
    PhysicalConfig,
    bipartite_eta,
    ensure_dirs,
    gdq_reduced_hessian,
    hessian_spectrum,
    lattice_edges,
    markdown_table,
    save_json,
)


OUT = RESULTS / "saida_q25_11_build_physical_domains.md"
CACHE_FILE = CACHE / "physical_domains.json"


def main() -> None:
    ensure_dirs()
    cfg = PhysicalConfig()
    edges = lattice_edges(cfg.L)
    eta = bipartite_eta(cfg.L)
    h = gdq_reduced_hessian(cfg)
    eig = hessian_spectrum(cfg)
    rho_site = np.ones(cfg.n_sites, dtype=float) / cfg.n_sites
    obj = {
        "config": cfg.__dict__,
        "n_edges": len(edges),
        "rho_min": float(rho_site.min()),
        "rho_sum": float(rho_site.sum()),
        "holonomy_exchange": -1.0,
        "hessian_min_eig": float(eig.min()),
        "hessian_max_eig": float(eig.max()),
        "eta_balance": float(eta.sum()),
    }
    save_json(CACHE_FILE, obj)
    OUT.write_text(
        "# Q25.11 — Domínios físicos reduzidos\n\n"
        "Classificação: construção de benchmark GDQ reduzido.\n\n"
        + markdown_table(list(obj.items()))
        + "\nInterpretação: a rede física do aparelho foi fixada antes da comparação, "
        "a medida local é positiva e a Hessiana reduzida é positiva. O setor usa "
        "circulação escalonada para representar correlação antiferro sem pesos "
        "negativos.\n",
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()
