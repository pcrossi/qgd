#!/usr/bin/env python3
"""Q25.02 — estimador positivo com observável sensível à holonomia.

Classificação: teste de consistência + comparação com solução exata finita.

A amostragem usa apenas pesos positivos. A holonomia entra no observável,
não como denominador de reweighting.
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "resultados" / "saida_q25_02_estimador_holonomia.md"


def observable(x: np.ndarray, domain: np.ndarray) -> np.ndarray:
    """Observável local sensível à holonomia.

    Domínios pares carregam Hol=+1; ímpares representam setor trocado, Hol=-1.
    """
    hol = np.where(domain % 2 == 0, 1.0, -1.0)
    return hol * np.cos(2.0 * x) + 0.2 * x * x


def exact_value(rho_domain: np.ndarray, centers: np.ndarray, sigma: float, n_grid: int = 200_000) -> float:
    # Integração determinística em malha fina num domínio compacto efetivo.
    xs = np.linspace(-5.0, 5.0, n_grid)
    total = 0.0
    norm = 0.0
    for a, weight in enumerate(rho_domain):
        dens = np.exp(-0.5 * ((xs - centers[a]) / sigma) ** 2)
        vals = observable(xs, np.full_like(xs, a, dtype=int))
        total += weight * np.trapz(vals * dens, xs)
        norm += weight * np.trapz(dens, xs)
    return float(total / norm)


def main() -> None:
    rng = np.random.default_rng(2502)
    rho_domain = np.array([0.31, 0.19, 0.27, 0.23], dtype=float)
    centers = np.array([-1.2, -0.35, 0.55, 1.25], dtype=float)
    sigma = 0.55
    m = 200_000

    domains = rng.choice(len(rho_domain), size=m, p=rho_domain)
    xs = rng.normal(loc=centers[domains], scale=sigma, size=m)
    samples = observable(xs, domains)

    mean = float(samples.mean())
    var = float(samples.var(ddof=1))
    stderr = float(np.sqrt(var / m))
    exact = exact_value(rho_domain, centers, sigma)
    abs_err = abs(mean - exact)
    rel_err = abs_err / max(abs(exact), 1e-15)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        "# Q25.02 — Estimador positivo de holonomia\n\n"
        "Classificação: teste de consistência e comparação com solução exata finita.\n\n"
        "| item | valor |\n|---|---:|\n"
        f"| amostras | {m} |\n"
        f"| média MC | {mean:.12e} |\n"
        f"| valor exato finito | {exact:.12e} |\n"
        f"| variância amostral | {var:.12e} |\n"
        f"| erro padrão | {stderr:.12e} |\n"
        f"| erro absoluto | {abs_err:.12e} |\n"
        f"| erro relativo | {rel_err:.12e} |\n\n"
        "Interpretação: o sinal fermiônico aparece como holonomia no observável. "
        "Não há denominador de fase pequeno nesta classe finita. Isto não prova "
        "complexidade assintótica para sistemas genéricos.\n",
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()
