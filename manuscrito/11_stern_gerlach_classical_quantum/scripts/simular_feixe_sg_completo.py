#!/usr/bin/env python3
"""
Capítulo 11 — Propagação espacial de um feixe de Stern–Gerlach.

O canal de cada trajetória é gerado pela SDE condicionada:
    dp = 4 sqrt(Gamma) p(1-p) dW.

Após a captura do canal s = ±1, a partícula sofre aceleração transversal
constante s*a_sg dentro do ímã e deriva livremente até a tela.

O script testa:
  - pesos dos dois canais;
  - centros das manchas;
  - separação entre as manchas;
  - dispersão interna;
  - acordo com a cinemática analítica.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np

from simular_captura_sg import born_probability, logit, sigmoid


def sample_channels(
    p0: float,
    n_particles: int,
    gamma: float,
    epsilon: float,
    dt: float,
    max_time: float,
    seed: int,
) -> tuple[np.ndarray, np.ndarray]:
    if p0 <= epsilon:
        return -np.ones(n_particles, dtype=np.int8), np.zeros(n_particles)
    if p0 >= 1.0 - epsilon:
        return np.ones(n_particles, dtype=np.int8), np.zeros(n_particles)

    rng = np.random.default_rng(seed)
    y = np.full(n_particles, logit(p0), dtype=float)
    active = np.ones(n_particles, dtype=bool)
    channels = np.zeros(n_particles, dtype=np.int8)
    times = np.full(n_particles, np.nan)
    amplitude = 4.0 * math.sqrt(gamma)
    sqrt_dt = math.sqrt(dt)
    n_steps = int(math.ceil(max_time / dt))

    for step in range(1, n_steps + 1):
        idx = np.flatnonzero(active)
        if idx.size == 0:
            break
        values = y[idx]
        values += (
            0.5 * amplitude**2 * np.tanh(0.5 * values) * dt
            + amplitude * sqrt_dt * rng.normal(size=idx.size)
        )
        y[idx] = values
        probabilities = sigmoid(values)
        upper = probabilities >= 1.0 - epsilon
        lower = probabilities <= epsilon
        if np.any(upper):
            chosen = idx[upper]
            channels[chosen] = 1
            times[chosen] = step * dt
            active[chosen] = False
        if np.any(lower):
            chosen = idx[lower]
            channels[chosen] = -1
            times[chosen] = step * dt
            active[chosen] = False

    # Não convergidas são raras no regime padrão; preservamos o status zero.
    return channels, times


def simulate_beam(args: argparse.Namespace) -> str:
    rng = np.random.default_rng(args.seed + 991)
    theta = math.radians(args.theta)
    p0 = born_probability(theta)
    channels, capture_times = sample_channels(
        p0,
        args.particles,
        args.gamma,
        args.epsilon,
        args.dt,
        args.max_measurement_time,
        args.seed,
    )
    resolved = channels != 0
    channels = channels[resolved]
    capture_times = capture_times[resolved]

    z0 = rng.normal(0.0, args.sigma_z, size=channels.size)
    vz0 = rng.normal(0.0, args.sigma_vz, size=channels.size)
    time_magnet = args.magnet_length / args.longitudinal_velocity
    time_drift = args.screen_distance / args.longitudinal_velocity
    total_time = time_magnet + time_drift
    displacement = args.acceleration * (
        0.5 * time_magnet**2 + time_magnet * time_drift
    )
    z_screen = z0 + vz0 * total_time + channels * displacement

    plus = z_screen[channels > 0]
    minus = z_screen[channels < 0]
    p_mc = plus.size / channels.size
    threshold_target = (
        (p0 - args.epsilon) / (1.0 - 2.0 * args.epsilon)
        if args.epsilon < p0 < 1.0 - args.epsilon
        else float(p0 >= 1.0 - args.epsilon)
    )
    center_plus = float(np.mean(plus)) if plus.size else float("nan")
    center_minus = float(np.mean(minus)) if minus.size else float("nan")
    sigma_plus = float(np.std(plus, ddof=1)) if plus.size > 1 else 0.0
    sigma_minus = float(np.std(minus, ddof=1)) if minus.size > 1 else 0.0
    separation = center_plus - center_minus
    analytic_separation = 2.0 * displacement
    relative_error = abs(separation - analytic_separation) / abs(
        analytic_separation
    )
    expected_sigma = math.sqrt(
        args.sigma_z**2 + (total_time * args.sigma_vz) ** 2
    )

    lines = [
        "# Propagação espacial Stern–Gerlach — Capítulo 11",
        "",
        "## Parâmetros",
        "",
        f"- partículas: {args.particles}",
        f"- theta: {args.theta} graus",
        f"- p+ de Born: {p0:.9f}",
        f"- p+ de primeiro alcance: {threshold_target:.9f}",
        f"- tempo no ímã: {time_magnet:.6f}",
        f"- tempo de deriva: {time_drift:.6f}",
        f"- deslocamento analítico por canal: {displacement:.9f}",
        "",
        "## Resultado",
        "",
        f"- resolvidas: {channels.size}",
        f"- canal +: {plus.size}",
        f"- canal -: {minus.size}",
        f"- frequência +: {p_mc:.9f}",
        f"- centro +: {center_plus:.9f}",
        f"- centro -: {center_minus:.9f}",
        f"- separação numérica: {separation:.9f}",
        f"- separação analítica: {analytic_separation:.9f}",
        f"- erro relativo da separação: {relative_error:.3e}",
        f"- sigma +: {sigma_plus:.9f}",
        f"- sigma -: {sigma_minus:.9f}",
        f"- sigma cinemático esperado: {expected_sigma:.9f}",
        f"- tempo médio de captura: {float(np.mean(capture_times)):.9f}",
        "",
        "## Veredito",
        "",
        "Os pesos vêm da dinâmica condicionada; as posições das manchas vêm da",
        "força oposta nos dois canais. A aceleração usada é adimensional e deve",
        "ser substituída por mu*grad(|B|)/m numa simulação física.",
        "",
    ]
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--particles", type=int, default=50000)
    parser.add_argument("--theta", type=float, default=60.0)
    parser.add_argument("--gamma", type=float, default=1.0)
    parser.add_argument("--epsilon", type=float, default=0.01)
    parser.add_argument("--dt", type=float, default=0.001)
    parser.add_argument("--max-measurement-time", type=float, default=10.0)
    parser.add_argument("--magnet-length", type=float, default=1.0)
    parser.add_argument("--screen-distance", type=float, default=3.0)
    parser.add_argument("--longitudinal-velocity", type=float, default=2.0)
    parser.add_argument("--acceleration", type=float, default=0.4)
    parser.add_argument("--sigma-z", type=float, default=0.03)
    parser.add_argument("--sigma-vz", type=float, default=0.01)
    parser.add_argument("--seed", type=int, default=424242)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("saida_beam_sg.md"),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    report = simulate_beam(args)
    args.output.write_text(report, encoding="utf-8")
    print(report)
    print(f"\nArquivo salvo em: {args.output}")


if __name__ == "__main__":
    main()

