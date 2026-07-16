#!/usr/bin/env python3
r"""Avaliação auditada da polarização U(1) comum às Q34/Q35.

Usa r=q_E^2/m^2 e eta=tau*m^2=m^2/Lambda_EM^2. A escolha padrão de eta é
somente um cenário de teste; o programa não deriva Lambda_EM nem ajusta dados.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.special import exp1


@dataclass(frozen=True)
class Config:
    alpha0: float = 1.0 / 137.035999084
    eta: float = 1.0e-6
    n_gauss: int = 256


def nodes_weights(n: int) -> tuple[np.ndarray, np.ndarray]:
    z, w = leggauss(n)
    return 0.5 * (z + 1.0), 0.5 * w


def pi_scalar(r: float, cfg: Config, n: int | None = None) -> float:
    """Calcula Pi_eta(r) por Gauss--Legendre."""
    if r < 0 or cfg.eta <= 0:
        raise ValueError("requer r>=0 e eta>0")
    x, w = nodes_weights(n or cfg.n_gauss)
    u = x * (1.0 - x)
    y = u * (exp1(cfg.eta) - exp1(cfg.eta * (1.0 + u * r)))
    return float(2.0 * cfg.alpha0 / math.pi * np.dot(w, y))


def pi_adaptive(r: float, cfg: Config) -> tuple[float, float]:
    """Controle independente por quadratura adaptativa."""
    e0 = float(exp1(cfg.eta))

    def f(x: float) -> float:
        u = x * (1.0 - x)
        return u * (e0 - float(exp1(cfg.eta * (1.0 + u * r))))

    value, error = quad(f, 0.0, 1.0, epsabs=1e-13, epsrel=1e-12, limit=300)
    factor = 2.0 * cfg.alpha0 / math.pi
    return factor * value, factor * error


def pi_qed(r: float, alpha0: float, n: int = 512) -> float:
    """Limite analítico eta->0 da expressão subtraída."""
    x, w = nodes_weights(n)
    u = x * (1.0 - x)
    return float(2.0 * alpha0 / math.pi * np.dot(w, u * np.log1p(u * r)))


def pi_infinity(cfg: Config) -> float:
    return cfg.alpha0 * float(exp1(cfg.eta)) / (3.0 * math.pi)


def alpha_eff(pi_value: float, alpha0: float) -> float:
    return alpha0 / (1.0 - pi_value) if pi_value < 1.0 else math.inf


def tensor(q: np.ndarray, pi_value: float) -> np.ndarray:
    q = np.asarray(q, dtype=float)
    return (np.outer(q, q) - float(q @ q) * np.eye(q.size)) * pi_value


def ward_error(q: np.ndarray, pi_tensor: np.ndarray) -> tuple[float, float]:
    q = np.asarray(q, dtype=float)
    absolute = float(np.linalg.norm(q @ pi_tensor))
    scale = float(np.linalg.norm(q) * np.linalg.norm(pi_tensor))
    return absolute, absolute / scale if scale else 0.0


def audit(cfg: Config) -> dict[str, object]:
    rs = np.concatenate(([0.0], np.logspace(-8, 12, 81)))
    values = np.array([pi_scalar(float(r), cfg) for r in rs])
    asymptote = pi_infinity(cfg)
    sample_rs = [0.0, 1e-4, 1.0, 1e4, 1e8, 1e12]
    samples = []
    for r in sample_rs:
        value = pi_scalar(r, cfg)
        reference, error = pi_adaptive(r, cfg)
        samples.append((r, value, reference, error, abs(value - reference)))

    orders = [32, 64, 128, 256, 512]
    convergence = [(n, pi_scalar(1e4, cfg, n)) for n in orders]
    conv_error = abs(convergence[-1][1] - convergence[-2][1])

    q = np.array([0.37, -0.21, 0.49, 0.73])
    ward_abs, ward_rel = ward_error(q, tensor(q, pi_scalar(float(q @ q), cfg)))

    cfg_small = Config(cfg.alpha0, 1e-12, cfg.n_gauss)
    qed = []
    for r in [1e-4, 1.0, 1e4]:
        numeric = pi_scalar(r, cfg_small)
        limit = pi_qed(r, cfg.alpha0)
        qed.append((r, numeric, limit, abs(numeric - limit)))

    return {
        "cfg": cfg,
        "samples": samples,
        "asymptote": asymptote,
        "alpha_inf": alpha_eff(asymptote, cfg.alpha0),
        "convergence": convergence,
        "conv_error": conv_error,
        "ward_abs": ward_abs,
        "ward_rel": ward_rel,
        "qed": qed,
        "monotone": bool(np.all(np.diff(values) >= -1e-13)),
        "bounded": bool(np.all(values <= asymptote + 1e-12)),
        "no_pole": bool(asymptote < 1.0),
    }


def report(result: dict[str, object], output: Path) -> None:
    cfg = result["cfg"]
    lines = [
        "# Saída auditada — polarização $U(1)$ das Q34/Q35",
        "",
        "## Classificação",
        "",
        "**Avaliação direta e teste de consistência.** A equação vem de",
        "q34/polarizacao_U1_heat_kernel.md. O cálculo não deriva",
        "$\\Lambda_{\\rm EM}$ e não ajusta dados experimentais.",
        "",
        "## Entrada",
        "",
        "$$",
        f"\\alpha_0={cfg.alpha0:.15g},\\qquad \\eta=\\tau m^2={cfg.eta:.6e}.",
        "$$",
        "",
        "$\\eta$ é um cenário de teste, não uma constante derivada.",
        "",
        "## Avaliação e controle independente",
        "",
        "| $r$ | $\\Pi_\\eta(r)$ | adaptativa | diferença |",
        "|---:|---:|---:|---:|",
    ]
    for r, value, reference, _, difference in result["samples"]:
        lines.append(f"| {r:.3e} | {value:.12e} | {reference:.12e} | {difference:.3e} |")
    lines += [
        "",
        "$$",
        f"\\Pi_\\eta(\\infty)={result['asymptote']:.12e},\\qquad "
        f"\\alpha_{{\\rm eff}}^{{-1}}(\\infty)={1/result['alpha_inf']:.9f}.",
        "$$",
        "",
        "## Identidade de Ward",
        "",
        "$$",
        f"\\lVert q^\\mu\\Pi_{{\\mu\\nu}}\\rVert={result['ward_abs']:.3e},\\qquad "
        f"\\varepsilon_{{\\rm Ward}}={result['ward_rel']:.3e}.",
        "$$",
        "",
        "O teste verifica a forma tensorial transversal já derivada; não substitui",
        "a derivação funcional da identidade de Ward.",
        "",
        "## Refinamento",
        "",
        "| pontos | $\\Pi_\\eta(10^4)$ |",
        "|---:|---:|",
    ]
    for n, value in result["convergence"]:
        lines.append(f"| {n} | {value:.14e} |")
    lines += [
        "",
        f"Erro entre as duas últimas ordens: **{result['conv_error']:.3e}**.",
        "",
        "## Limite de QED",
        "",
        "| $r$ | $\\eta=10^{-12}$ | limite $\\eta\\to0$ | diferença |",
        "|---:|---:|---:|---:|",
    ]
    for r, numeric, limit, difference in result["qed"]:
        lines.append(f"| {r:.3e} | {numeric:.12e} | {limit:.12e} | {difference:.3e} |")
    passed = (
        result["monotone"] and result["bounded"] and result["no_pole"]
        and result["ward_rel"] < 1e-14 and result["conv_error"] < 1e-11
    )
    lines += [
        "",
        "## Veredito computacional",
        "",
        f"- monotonicidade: **{result['monotone']}**;",
        f"- limitado pelo valor assintótico: **{result['bounded']}**;",
        f"- condição sem polo no cenário: **{result['no_pole']}**;",
        f"- conjunto dos testes: **{'PASSOU' if passed else 'FALHOU'}**.",
        "",
        "A avaliação física ainda requer derivar $\\Lambda_{\\rm EM}$ e inserir o",
        "espectro completo de espécies carregadas.",
        "",
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--eta", type=float, default=1e-6)
    parser.add_argument("--alpha0", type=float, default=1 / 137.035999084)
    parser.add_argument("--n-gauss", type=int, default=256)
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).with_name("saida_polarizacao_u1_auditada.md"),
    )
    args = parser.parse_args()
    result = audit(Config(args.alpha0, args.eta, args.n_gauss))
    report(result, args.output)
    print(f"Relatório: {args.output}")
    print(f"Pi(infinito): {result['asymptote']:.12e}")
    print(f"erro relativo de Ward: {result['ward_rel']:.3e}")
    print(f"erro de refinamento: {result['conv_error']:.3e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
