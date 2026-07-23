#!/usr/bin/env python3
"""Q25.13 — correlações spin/circulação com medida positiva."""

from __future__ import annotations

from q25_physical_common import (
    CACHE,
    RESULTS,
    PhysicalConfig,
    ensure_dirs,
    enumerate_exact,
    markdown_table,
    metropolis_correlations,
    save_json,
)


OUT = RESULTS / "saida_q25_13_spin_correlations_gdq.md"
CACHE_FILE = CACHE / "spin_correlations.json"


def main() -> None:
    ensure_dirs()
    cfg = PhysicalConfig()
    exact = enumerate_exact(cfg)
    mc = metropolis_correlations(cfg)
    obj = {
        "exact": exact,
        "mc": mc,
        "abs_error_C_s_r1": abs(mc["C_s_r1"] - exact["C_s_r1"]),
        "abs_error_C_s_r2": abs(mc["C_s_r2"] - exact["C_s_r2"]),
        "abs_error_energy": abs(mc["mean_energy"] - exact["mean_energy"]),
    }
    # Comprimento de correlação reduzido por razão de correlatores escalonados.
    # Para r=1, o sinal antiferro é negativo; para r=2, positivo.
    ratio = exact["C_s_r2"] / max(abs(exact["C_s_r1"]), 1e-15)
    xi_exact = -1.0 / __import__("math").log(max(ratio, 1e-15))
    obj["exact"]["xi_corr"] = xi_exact
    save_json(CACHE_FILE, obj)
    rows = [
        ("n_config_exact", exact["n_config"]),
        ("C_s_r1_exact", exact["C_s_r1"]),
        ("C_s_r1_mc", mc["C_s_r1"]),
        ("C_s_r1_stderr", mc["C_s_r1_stderr"]),
        ("C_s_r2_exact", exact["C_s_r2"]),
        ("C_s_r2_mc", mc["C_s_r2"]),
        ("C_s_r2_stderr", mc["C_s_r2_stderr"]),
        ("xi_corr_exact", xi_exact),
        ("energy_exact", exact["mean_energy"]),
        ("energy_mc", mc["mean_energy"]),
        ("acceptance", mc["acceptance"]),
    ]
    OUT.write_text(
        "# Q25.13 — Correlações GDQ reduzidas\n\n"
        "Classificação: avaliação direta em benchmark reduzido e comparação com "
        "solução exata finita.\n\n"
        + markdown_table(rows)
        + "\nInterpretação: a amostragem usa peso positivo "
        "`exp(-beta E_GDQ)`; a correlação antiferro aparece da circulação "
        "escalonada e da holonomia, não de peso negativo.\n",
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()
