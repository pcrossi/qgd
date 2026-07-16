#!/usr/bin/env python3
"""Teste diagnóstico do detector ôhmico idealizado da interface GDQ.

O script não avalia um material físico. Ele verifica numericamente:

1. o DtN retardado do canal semi-infinito;
2. a taxa informacional Gamma = g^2/(8 gamma kBT);
3. o filtro causal e a propriedade de martingal;
4. a probabilidade de erro em tempo finito;
5. a frequência de registros de Born;
6. relaxação do ponteiro linearizado.

Todos os parâmetros são adimensionais e declarados como dados de teste.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import erf, log, pi, sqrt

import numpy as np


@dataclass(frozen=True)
class Params:
    zeta: float = 1.7
    c_a: float = 2.3
    k_pointer: float = 4.0
    g_x: float = 1.0
    kbt: float = 0.5
    p0: float = 0.37
    dt: float = 0.01
    total_time: float = 4.0
    n_traj: int = 100_000
    seed: int = 42042

    @property
    def gamma(self) -> float:
        return self.zeta / self.c_a

    @property
    def mobility(self) -> float:
        return 1.0 / self.gamma

    @property
    def gamma_info(self) -> float:
        return self.g_x**2 / (8.0 * self.gamma * self.kbt)

    @property
    def tau_relax(self) -> float:
        return self.gamma / self.k_pointer


def normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + erf(x / sqrt(2.0)))


def logistic(x: np.ndarray) -> np.ndarray:
    out = np.empty_like(x)
    pos = x >= 0.0
    out[pos] = 1.0 / (1.0 + np.exp(-x[pos]))
    exp_x = np.exp(x[~pos])
    out[~pos] = exp_x / (1.0 + exp_x)
    return out


def test_dtn(p: Params) -> list[tuple[float, float]]:
    """Second-order one-sided derivative test for outgoing plane waves."""
    omega = 1.3
    expected = -1j * omega * p.zeta / p.c_a
    rows: list[tuple[float, float]] = []
    for h in (0.2, 0.1, 0.05, 0.025):
        y0 = 1.0 + 0.0j
        y1 = np.exp(1j * omega * h / p.c_a)
        y2 = np.exp(2j * omega * h / p.c_a)
        derivative = (-3.0 * y0 + 4.0 * y1 - y2) / (2.0 * h)
        numerical = -p.zeta * derivative / y0
        rel_error = abs(numerical - expected) / abs(expected)
        rows.append((h, float(rel_error)))
    return rows


def simulate(p: Params) -> dict[str, object]:
    rng = np.random.default_rng(p.seed)
    n_steps = int(round(p.total_time / p.dt))
    sqrt_dt = sqrt(p.dt)
    sigma_x = sqrt(2.0 * p.kbt / p.gamma)

    is_plus = rng.random(p.n_traj) < p.p0
    kappa = np.where(is_plus, 1.0, -1.0)
    x = np.zeros(p.n_traj)
    y_record = np.zeros(p.n_traj)
    log_odds0 = log(p.p0 / (1.0 - p.p0))

    checkpoint_steps = {
        int(round(frac * n_steps)): frac
        for frac in (0.25, 0.5, 0.75, 1.0)
    }
    checkpoints: list[tuple[float, float, float, float]] = []

    for step in range(1, n_steps + 1):
        dw = rng.normal(0.0, sqrt_dt, p.n_traj)
        drift = (-p.k_pointer * x + p.g_x * kappa) / p.gamma
        dx = drift * p.dt + sigma_x * dw

        # Innovation reconstructed from the observable pointer increment.
        dy = (
            p.gamma * dx + p.k_pointer * x * p.dt
        ) / sqrt(2.0 * p.gamma * p.kbt)
        y_record += dy
        x += dx

        if step in checkpoint_steps:
            time = step * p.dt
            log_odds = log_odds0 + 4.0 * sqrt(p.gamma_info) * y_record
            posterior = logistic(log_odds)
            checkpoints.append(
                (
                    time,
                    float(np.mean(posterior)),
                    float(np.mean(posterior[is_plus])),
                    float(np.mean(posterior[~is_plus])),
                )
            )

    final_log_odds = log_odds0 + 4.0 * sqrt(p.gamma_info) * y_record
    final_p = logistic(final_log_odds)
    inferred_plus = final_p >= 0.5

    empirical_error = float(np.mean(inferred_plus != is_plus))
    empirical_plus_record = float(np.mean(inferred_plus))
    empirical_true_plus = float(np.mean(is_plus))

    # Equal-prior analytic error is the clean closed formula. For the actual
    # unequal prior p0, use the exact Gaussian threshold implied by log odds.
    information = p.gamma_info * p.total_time
    sigma_l = 4.0 * sqrt(information)
    mu_shift = 8.0 * information
    error_plus = normal_cdf((-log_odds0 - mu_shift) / sigma_l)
    error_minus = 1.0 - normal_cdf((-log_odds0 + mu_shift) / sigma_l)
    analytic_error_prior = p.p0 * error_plus + (1.0 - p.p0) * error_minus
    analytic_error_equal = normal_cdf(-2.0 * sqrt(information))

    x_eq_plus = p.g_x / p.k_pointer
    x_eq_minus = -x_eq_plus

    return {
        "checkpoints": checkpoints,
        "information": information,
        "empirical_error": empirical_error,
        "analytic_error_prior": analytic_error_prior,
        "analytic_error_equal": analytic_error_equal,
        "empirical_plus_record": empirical_plus_record,
        "empirical_true_plus": empirical_true_plus,
        "mean_x_plus": float(np.mean(x[is_plus])),
        "mean_x_minus": float(np.mean(x[~is_plus])),
        "x_eq_plus": x_eq_plus,
        "x_eq_minus": x_eq_minus,
        "mean_final_p": float(np.mean(final_p)),
    }


def main() -> None:
    p = Params()
    dtn_rows = test_dtn(p)
    result = simulate(p)

    print("=" * 88)
    print("GDQ — TESTE DO DETECTOR ÔHMICO IDEALIZADO")
    print("=" * 88)
    print("\n[Parâmetros diagnósticos adimensionais]")
    print(f"zeta_A          = {p.zeta:.8f}")
    print(f"c_A             = {p.c_a:.8f}")
    print(f"gamma_A         = {p.gamma:.8f}")
    print(f"mobilidade      = {p.mobility:.8f}")
    print(f"k_pointer       = {p.k_pointer:.8f}")
    print(f"g_X             = {p.g_x:.8f}")
    print(f"kBT             = {p.kbt:.8f}")
    print(f"Gamma_info      = {p.gamma_info:.8f}")
    print(f"tau_relax       = {p.tau_relax:.8f}")
    print(f"p0              = {p.p0:.8f}")
    print(f"trajetorias     = {p.n_traj}")

    print("\n[Convergência do DtN retardado — derivada unilateral de ordem 2]")
    print("h          erro_relativo")
    for h, error in dtn_rows:
        print(f"{h:<10.6f} {error:.8e}")

    print("\n[Martingal e separação condicionada]")
    print("t          E[p_t]       E[p_t|+]     E[p_t|-]")
    for time, mean_p, mean_plus, mean_minus in result["checkpoints"]:
        print(f"{time:<10.4f} {mean_p:<12.8f} {mean_plus:<12.8f} {mean_minus:<12.8f}")

    print("\n[Resultado final]")
    print(f"informacao acumulada          = {result['information']:.8f}")
    print(f"erro empírico                 = {result['empirical_error']:.8f}")
    print(f"erro analítico (prior real)   = {result['analytic_error_prior']:.8f}")
    print(f"erro analítico (prior 1/2)    = {result['analytic_error_equal']:.8f}")
    print(f"fração verdadeira de canais + = {result['empirical_true_plus']:.8f}")
    print(f"fração inferida de registros += {result['empirical_plus_record']:.8f}")
    print(f"E[p_T]                        = {result['mean_final_p']:.8f}")
    print(f"E[X_T|+]                      = {result['mean_x_plus']:.8f}")
    print(f"equilíbrio X_+                = {result['x_eq_plus']:.8f}")
    print(f"E[X_T|-]                      = {result['mean_x_minus']:.8f}")
    print(f"equilíbrio X_-                = {result['x_eq_minus']:.8f}")

    dtn_converges = all(
        dtn_rows[i + 1][1] < dtn_rows[i][1]
        for i in range(len(dtn_rows) - 1)
    )
    martingale_error = abs(float(result["mean_final_p"]) - p.p0)
    sampling_se = sqrt(p.p0 * (1.0 - p.p0) / p.n_traj)
    martingale_z = martingale_error / sampling_se
    error_agreement = abs(
        float(result["empirical_error"])
        - float(result["analytic_error_prior"])
    )
    print("\n[Verificações]")
    print(f"DtN converge monotonicamente  = {dtn_converges}")
    print(f"|E[p_T]-p0|                   = {martingale_error:.8e}")
    print(f"erro padrão amostral          = {sampling_se:.8e}")
    print(f"desvio em erros padrão        = {martingale_z:.6f}")
    print(f"|erro_MC-erro_analítico|      = {error_agreement:.8e}")
    print("\nStatus: teste de consistência; não é avaliação de material físico.")


if __name__ == "__main__":
    main()
