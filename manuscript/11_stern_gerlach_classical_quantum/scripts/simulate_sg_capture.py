#!/usr/bin/env python3
"""
Chapter 11 — Monte Carlo of the Stern–Gerlach measurement martingale.

Equation:
    dp = 4 sqrt(Gamma) p (1-p) dW.

We integrate the logit variable y = log(p/(1-p)). By Itô's formula:
    dy = a dW + (a^2/2) tanh(y/2) dt,
    a = 4 sqrt(Gamma).

The register occurs at the first reach of p <= eps or p >= 1-eps.
The analytical probability of first reaching the upper threshold is:
    P_eps(+) = (p0-eps)/(1-2 eps).
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass
class CaptureResult:
    p0: float
    dt: float
    n_paths: int
    n_upper: int
    n_lower: int
    n_unresolved: int
    mean_capture_time: float

    @property
    def resolved(self) -> int:
        return self.n_upper + self.n_lower

    @property
    def frequency_upper(self) -> float:
        if self.resolved == 0:
            return float("nan")
        return self.n_upper / self.resolved

    @property
    def standard_error(self) -> float:
        if self.resolved == 0:
            return float("nan")
        p = self.frequency_upper
        return math.sqrt(max(p * (1.0 - p), 0.0) / self.resolved)


def clip_probability(p: float, floor: float = 1e-14) -> float:
    return float(np.clip(p, floor, 1.0 - floor))


def logit(p: float) -> float:
    p = clip_probability(p)
    return math.log(p / (1.0 - p))


def sigmoid(y: np.ndarray) -> np.ndarray:
    out = np.empty_like(y)
    positive = y >= 0.0
    out[positive] = 1.0 / (1.0 + np.exp(-y[positive]))
    exp_y = np.exp(y[~positive])
    out[~positive] = exp_y / (1.0 + exp_y)
    return out


def born_probability(theta: float) -> float:
    return math.cos(0.5 * theta) ** 2


def threshold_probability(p0: float, epsilon: float) -> float:
    if p0 <= epsilon:
        return 0.0
    if p0 >= 1.0 - epsilon:
        return 1.0
    return (p0 - epsilon) / (1.0 - 2.0 * epsilon)


def simulate_capture(
    p0: float,
    *,
    gamma: float,
    epsilon: float,
    dt: float,
    max_time: float,
    n_paths: int,
    seed: int,
) -> CaptureResult:
    if gamma <= 0.0:
        raise ValueError("gamma must be positive.")
    if not 0.0 < epsilon < 0.5:
        raise ValueError("epsilon must be between 0 and 1/2.")
    if dt <= 0.0 or max_time <= 0.0:
        raise ValueError("dt and max_time must be positive.")

    if p0 <= epsilon:
        return CaptureResult(p0, dt, n_paths, 0, n_paths, 0, 0.0)
    if p0 >= 1.0 - epsilon:
        return CaptureResult(p0, dt, n_paths, n_paths, 0, 0, 0.0)

    rng = np.random.default_rng(seed)
    y = np.full(n_paths, logit(p0), dtype=float)
    active = np.ones(n_paths, dtype=bool)
    outcome = np.zeros(n_paths, dtype=np.int8)
    capture_time = np.full(n_paths, np.nan, dtype=float)

    amplitude = 4.0 * math.sqrt(gamma)
    sqrt_dt = math.sqrt(dt)
    n_steps = int(math.ceil(max_time / dt))

    for step in range(1, n_steps + 1):
        idx = np.flatnonzero(active)
        if idx.size == 0:
            break

        y_active = y[idx]
        noise = rng.normal(size=idx.size)
        drift = 0.5 * amplitude**2 * np.tanh(0.5 * y_active)
        y_active = y_active + drift * dt + amplitude * sqrt_dt * noise
        y[idx] = y_active

        p_active = sigmoid(y_active)
        upper_local = p_active >= 1.0 - epsilon
        lower_local = p_active <= epsilon

        if np.any(upper_local):
            upper_idx = idx[upper_local]
            outcome[upper_idx] = 1
            capture_time[upper_idx] = step * dt
            active[upper_idx] = False

        if np.any(lower_local):
            lower_idx = idx[lower_local]
            outcome[lower_idx] = -1
            capture_time[lower_idx] = step * dt
            active[lower_idx] = False

    n_upper = int(np.count_nonzero(outcome == 1))
    n_lower = int(np.count_nonzero(outcome == -1))
    n_unresolved = int(np.count_nonzero(outcome == 0))
    times = capture_time[np.isfinite(capture_time)]
    mean_time = float(np.mean(times)) if times.size else float("nan")

    return CaptureResult(
        p0, dt, n_paths, n_upper, n_lower, n_unresolved, mean_time
    )


def run_study(args: argparse.Namespace) -> str:
    angles_deg = [float(value) for value in args.angles.split(",")]
    dts = [float(value) for value in args.dts.split(",")]
    lines = [
        "# Output — martingale and capture Chapter 11",
        "",
        "## Parameters",
        "",
        f"- trajectories per case: {args.paths}",
        f"- dimensionless Gamma: {args.gamma}",
        f"- threshold epsilon: {args.epsilon}",
        f"- maximum time: {args.max_time}",
        f"- tested steps: {dts}",
        f"- base seed: {args.seed}",
        "",
        "## Results",
        "",
        "| theta | dt | Born p+ | First passage | Monte Carlo | MC error | z-score | unresolved | average time |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    max_abs_z = 0.0
    max_unresolved_fraction = 0.0

    for angle_index, angle_deg in enumerate(angles_deg):
        p0 = born_probability(math.radians(angle_deg))
        p_threshold = threshold_probability(p0, args.epsilon)
        for dt_index, dt in enumerate(dts):
            result = simulate_capture(
                p0,
                gamma=args.gamma,
                epsilon=args.epsilon,
                dt=dt,
                max_time=args.max_time,
                n_paths=args.paths,
                seed=args.seed + 1009 * angle_index + 9176 * dt_index,
            )
            error = result.frequency_upper - p_threshold
            z_score = (
                error / result.standard_error
                if result.standard_error > 0.0
                else 0.0
            )
            max_abs_z = max(max_abs_z, abs(z_score))
            unresolved = result.n_unresolved / result.n_paths
            max_unresolved_fraction = max(max_unresolved_fraction, unresolved)
            lines.append(
                "| "
                f"{angle_deg:.1f} | {dt:.5g} | {p0:.6f} | "
                f"{p_threshold:.6f} | {result.frequency_upper:.6f} | "
                f"{result.standard_error:.6f} | {z_score:+.2f} | "
                f"{result.n_unresolved} | {result.mean_capture_time:.5f} |"
            )

    lines.extend(
        [
            "",
            "## Diagnosis",
            "",
            f"- largest |z-score|: {max_abs_z:.3f}",
            (
                "- largest unresolved fraction: "
                f"{100.0 * max_unresolved_fraction:.4f}%"
            ),
            "",
            "$$",
            r"P_\varepsilon(+)=\frac{p_0-\varepsilon}{1-2\varepsilon}.",
            "$$",
            "",
            "The simulation integrates the SDE directly; the analytical solution is used",
            "only as a post-test.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paths", type=int, default=20000)
    parser.add_argument("--gamma", type=float, default=1.0)
    parser.add_argument("--epsilon", type=float, default=0.02)
    parser.add_argument("--max-time", type=float, default=8.0)
    parser.add_argument("--dts", default="0.01,0.005,0.0025")
    parser.add_argument("--angles", default="0,30,60,90,120,150,180")
    parser.add_argument("--seed", type=int, default=42042)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("output_measurement_sg.md"),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    report = run_study(args)
    args.output.write_text(report, encoding="utf-8")
    print(report)
    print(f"\nFile saved in: {args.output}")


if __name__ == "__main__":
    main()
