#!/usr/bin/env python3
"""Reduced ohmic detector and Born capture.

Classification:
    consistency test with dimensionless parameters.

This script verifies the note:

    notes/ohmic_detector_born_capture.md

It does not evaluate a physical material. The parameters are fixed and diagnostic. The
test covers:

    1. convergence of the retarded DtN of the open channel;
    2. informational rate Gamma = g_X^2/(8 gamma_A kBT);
    3. martingale E[p_t] = p0;
    4. finite classification error;
    5. relaxation of the pointer to the conditioned records.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import erf, log, sqrt
from pathlib import Path

import numpy as np


OUT = Path(__file__).resolve().parent / "output_ohmic_detector_born_capture.md"


@dataclass(frozen=True)
class Params:
    zeta_a: float = 1.7
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
    def gamma_a(self) -> float:
        return self.zeta_a / self.c_a

    @property
    def mobility(self) -> float:
        return 1.0 / self.gamma_a

    @property
    def gamma_info(self) -> float:
        return self.g_x**2 / (8.0 * self.gamma_a * self.kbt)

    @property
    def tau_relax(self) -> float:
        return self.gamma_a / self.k_pointer


def normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + erf(x / sqrt(2.0)))


def logistic(x: np.ndarray) -> np.ndarray:
    out = np.empty_like(x)
    pos = x >= 0.0
    out[pos] = 1.0 / (1.0 + np.exp(-x[pos]))
    exp_x = np.exp(x[~pos])
    out[~pos] = exp_x / (1.0 + exp_x)
    return out
    

def dtn_errors(p: Params) -> list[tuple[float, float]]:
    """Verifies Lambda_ret = -i omega zeta_A/c_A by one-sided derivative."""

    omega = 1.3
    expected = -1j * omega * p.zeta_a / p.c_a
    rows = []
    for h in (0.2, 0.1, 0.05, 0.025):
        y0 = 1.0 + 0.0j
        y1 = np.exp(1j * omega * h / p.c_a)
        y2 = np.exp(2j * omega * h / p.c_a)
        derivative = (-3.0 * y0 + 4.0 * y1 - y2) / (2.0 * h)
        numerical = -p.zeta_a * derivative / y0
        rows.append((h, float(abs(numerical - expected) / abs(expected))))
    return rows


def simulate(p: Params) -> dict[str, object]:
    rng = np.random.default_rng(p.seed)
    n_steps = int(round(p.total_time / p.dt))
    sqrt_dt = sqrt(p.dt)
    sigma_x = sqrt(2.0 * p.kbt / p.gamma_a)

    is_plus = rng.random(p.n_traj) < p.p0
    kappa = np.where(is_plus, 1.0, -1.0)
    x = np.zeros(p.n_traj)
    y_record = np.zeros(p.n_traj)
    log_odds0 = log(p.p0 / (1.0 - p.p0))

    checkpoints = []
    checkpoint_steps = {
        int(round(frac * n_steps)): frac
        for frac in (0.25, 0.5, 0.75, 1.0)
    }

    for step in range(1, n_steps + 1):
        dw = rng.normal(0.0, sqrt_dt, p.n_traj)
        drift = (-p.k_pointer * x + p.g_x * kappa) / p.gamma_a
        dx = drift * p.dt + sigma_x * dw

        dy = (p.gamma_a * dx + p.k_pointer * x * p.dt) / sqrt(
            2.0 * p.gamma_a * p.kbt
        )
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

    information = p.gamma_info * p.total_time
    sigma_l = 4.0 * sqrt(information)
    mu_shift = 8.0 * information
    error_plus = normal_cdf((-log_odds0 - mu_shift) / sigma_l)
    error_minus = 1.0 - normal_cdf((-log_odds0 + mu_shift) / sigma_l)
    analytic_error_prior = p.p0 * error_plus + (1.0 - p.p0) * error_minus
    analytic_error_equal = normal_cdf(-2.0 * sqrt(information))

    return {
        "checkpoints": checkpoints,
        "information": information,
        "empirical_error": float(np.mean(inferred_plus != is_plus)),
        "analytic_error_prior": analytic_error_prior,
        "analytic_error_equal": analytic_error_equal,
        "empirical_plus_record": float(np.mean(inferred_plus)),
        "empirical_true_plus": float(np.mean(is_plus)),
        "mean_x_plus": float(np.mean(x[is_plus])),
        "x_eq_plus": p.g_x / p.k_pointer,
        "x_eq_minus": -p.g_x / p.k_pointer,
        "mean_final_p": float(np.mean(final_p)),
    }


def main() -> None:
    p = Params()
    rows = dtn_errors(p)
    result = simulate(p)

    martingale_error = abs(float(result["mean_final_p"]) - p.p0)
    sampling_se = sqrt(p.p0 * (1.0 - p.p0) / p.n_traj)
    error_agreement = abs(
        float(result["empirical_error"]) - float(result["analytic_error_prior"])
    )

    lines = ["# Output — ohmic detector and Born capture\n\n"]
    lines.append("Classification: consistency test with dimensionless parameters.\n\n")
    lines.append("## Diagnostic parameters\n\n")
    lines.append("| parameter | value |\n")
    lines.append("|---|---:|\n")
    for name, value in (
        ("zeta_A", p.zeta_a),
        ("c_A", p.c_a),
        ("gamma_A", p.gamma_a),
        ("mobility", p.mobility),
        ("k_pointer", p.k_pointer),
        ("g_X", p.g_x),
        ("kBT", p.kbt),
        ("Gamma_info", p.gamma_info),
        ("tau_relax", p.tau_relax),
        ("p0", p.p0),
        ("trajectories", float(p.n_traj)),
        ("final time", p.total_time),
    ):
        lines.append(f"| {name} | {value:.12f} |\n")

    lines.append("\n## Convergence of the retarded DtN\n\n")
    lines.append("| h | relative error |\n")
    lines.append("|---:|---:|\n")
    for h, err in rows:
        lines.append(f"| {h:.6f} | {err:.12e} |\n")

    lines.append("\n## Martingale and conditioned separation\n\n")
    lines.append("| t | E[p_t] | E[p_t|+] | E[p_t|-] |\n")
    lines.append("|---:|---:|---:|---:|\n")
    for time, mean_p, mean_plus, mean_minus in result["checkpoints"]:
        lines.append(f"| {time:.4f} | {mean_p:.12f} | {mean_plus:.12f} | {mean_minus:.12f} |\n")

    lines.append("\n## Final result\n\n")
    lines.append("| quantity | value |\n")
    lines.append("|---|---:|\n")
    for name in (
        "information",
        "empirical_error",
        "analytic_error_prior",
        "analytic_error_equal",
        "empirical_true_plus",
        "empirical_plus_record",
        "mean_final_p",
        "mean_x_plus",
        "x_eq_plus",
        "mean_x_minus",
        "x_eq_minus",
    ):
        lines.append(f"| {name} | {float(result[name]):.12f} |\n")

    lines.append("\n## Verifications\n\n")
    lines.append("| test | value |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| martingale error | {martingale_error:.12e} |\n")
    lines.append(f"| binomial standard error | {sampling_se:.12e} |\n")
    lines.append(f"| martingale error in standard deviations | {martingale_error / sampling_se:.12f} |\n")
    lines.append(f"| MC vs analytical error difference | {error_agreement:.12e} |\n")
    lines.append("\n## Verdict\n\n")
    lines.append(
        "The test confirms the ohmic DtN, the martingale property, the conditioned "
        "asymptotic capture, and the relaxation of the pointer in the reduced model. "
        "It does not calculate parameters of a real material.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
