#!/usr/bin/env python3
"""Q25.03 — autocorrelação, variância e escala em número de domínios.

Classificação: teste de escala numérico. O objetivo é detectar se o toy GDQ
positivo mostra assinatura exponencial no regime testado.
"""

from __future__ import annotations

from pathlib import Path
import math
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "resultados" / "saida_q25_03_autocorrelacao_variancia.md"


def transition_matrix(n: int, stay: float = 0.55) -> np.ndarray:
    """Cadeia local em anel com gap controlado, derivada de transmissões locais."""
    p_move = (1.0 - stay) / 2.0
    k = np.zeros((n, n), dtype=float)
    for i in range(n):
        k[i, i] = stay
        k[i, (i - 1) % n] = p_move
        k[i, (i + 1) % n] = p_move
    return k


def integrated_autocorr(x: np.ndarray, max_lag: int = 400) -> float:
    x = np.asarray(x, dtype=float)
    x = x - x.mean()
    denom = float(np.dot(x, x))
    if denom <= 0:
        return 0.5
    tau = 0.5
    for lag in range(1, min(max_lag, len(x) - 1)):
        ac = float(np.dot(x[:-lag], x[lag:]) / denom)
        if ac <= 0:
            break
        tau += ac
    return tau


def run_chain(n: int, steps: int, rng: np.random.Generator) -> tuple[float, float, float, float]:
    k = transition_matrix(n)
    state = int(rng.integers(n))
    obs = np.empty(steps, dtype=float)
    for t in range(steps):
        state = int(rng.choice(n, p=k[state]))
        hol = 1.0 if state % 2 == 0 else -1.0
        # Observável holonômico local. Ele não é necessariamente o modo lento
        # dominante da cadeia; por isso também registramos o gap espectral.
        obs[t] = hol * math.cos(2.0 * math.pi * state / n)
    tau = integrated_autocorr(obs)
    var_eff = float(obs.var(ddof=1) * 2.0 * tau / steps)
    eig = np.linalg.eigvalsh((k + k.T) / 2.0)
    spectral_gap = float(1.0 - np.sort(eig)[-2])
    mixing_bound = 1.0 / max(spectral_gap, 1e-15)
    return tau, var_eff, spectral_gap, mixing_bound


def main() -> None:
    rng = np.random.default_rng(2503)
    steps = 80_000
    sizes = [4, 8, 16, 32, 64]
    rows = []
    for n in sizes:
        tau, var_eff, gap, mixing_bound = run_chain(n, steps, rng)
        rows.append((n, tau, var_eff, gap, mixing_bound))

    # Ajustes log-log simples para classificar a escala observada.
    ns = np.array([r[0] for r in rows], dtype=float)
    taus = np.array([r[1] for r in rows], dtype=float)
    bounds = np.array([r[4] for r in rows], dtype=float)
    p_tau, _ = np.polyfit(np.log(ns), np.log(taus), 1)
    p_mix, _ = np.polyfit(np.log(ns), np.log(bounds), 1)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        "# Q25.03 — Autocorrelação e variância\n\n"
        "Classificação: teste de escala numérico em toy GDQ positivo.\n\n"
        "| domínios | tau_corr_int | var_erro_media | gap espectral | 1/gap |\n|---:|---:|---:|---:|---:|\n"
        + "".join(
            f"| {n} | {tau:.6f} | {var_eff:.12e} | {gap:.12e} | {mix:.6f} |\n"
            for n, tau, var_eff, gap, mix in rows
        )
        + "\n"
        f"Ajuste do observável testado: `tau_corr ~ C N^{p_tau:.3f}`.\n\n"
        f"Limite espectral de mistura: `1/gap ~ C N^{p_mix:.3f}`.\n\n"
        "Interpretação: no toy local em anel, o limite de mistura é compatível "
        "com escala polinomial quadrática. Isto é evidência numérica de classe "
        "reduzida, não prova para Hamiltonianos fermiônicos genéricos.\n",
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()
