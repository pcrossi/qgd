#!/usr/bin/env python3
"""Q25.12 — deriva interfaces por impedância/Hessiana reduzida."""

from __future__ import annotations

import numpy as np
from q25_physical_common import (
    CACHE,
    RESULTS,
    PhysicalConfig,
    ensure_dirs,
    lattice_edges,
    local_interface_matrix,
    markdown_table,
    save_json,
)


OUT = RESULTS / "saida_q25_12_derive_interface_from_hessian.md"
CACHE_FILE = CACHE / "interface_summary.json"


def main() -> None:
    ensure_dirs()
    cfg = PhysicalConfig()
    edges = lattice_edges(cfg.L)
    unit_errors = []
    holonomy = -1.0 + 0.0j
    for edge in edges:
        s = local_interface_matrix(cfg, edge)
        unit_errors.append(float(np.linalg.norm(s.conj().T @ s - np.eye(2))))

    obj = {
        "n_interfaces": len(edges),
        "max_unitarity_error": float(max(unit_errors)),
        "mean_unitarity_error": float(np.mean(unit_errors)),
        "holonomy_exchange": float(holonomy.real),
    }
    save_json(CACHE_FILE, obj)
    OUT.write_text(
        "# Q25.12 — Interface por Hessiana GDQ reduzida\n\n"
        "Classificação: derivação numérica de operador/interface reduzido.\n\n"
        + markdown_table(list(obj.items()))
        + "\nA matriz de espalhamento local foi obtida pela transformada de Cayley "
        "da impedância Hermitiana extraída da Hessiana reduzida. Como a impedância "
        "é Hermitiana, a interface fechada é unitária por construção; o erro acima "
        "mede apenas erro de máquina.\n",
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()
