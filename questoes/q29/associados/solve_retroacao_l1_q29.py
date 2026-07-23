#!/usr/bin/env python3
"""Retroação conformal do harmônico torsional l=1 na ação Perelman-Bismut."""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import numpy as np
from scipy.optimize import least_squares
from scipy.special import roots_jacobi


@dataclass
class Model:
    radius: float
    tau: float
    flux: int
    y: np.ndarray
    weight: np.ndarray

    @property
    def scalar_curvature(self) -> float:
        return 6.0 / self.radius**2

    @property
    def b0(self) -> float:
        return self.flux / (np.pi * self.radius**3)

    def sigma_data(self, coefficients: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """sigma=c0+c1*y+c2*(y²-1/4)+c3*(y³-y/2)."""
        c0, c1, c2, c3 = coefficients
        y = self.y
        sigma = c0 + c1 * y + c2 * (y**2 - 0.25) + c3 * (y**3 - 0.5 * y)
        first = c1 + 2.0 * c2 * y + c3 * (3.0 * y**2 - 0.5)
        second = 2.0 * c2 + 6.0 * c3 * y
        return sigma, first, second

    def action(self, coefficients: np.ndarray, beta: float) -> float:
        sigma, first, second = self.sigma_data(coefficients)
        y = self.y
        r2 = self.radius**2
        grad2 = (1.0 - y**2) * first**2 / r2
        laplace = ((1.0 - y**2) * second - 3.0 * y * first) / r2

        # f=f0+3 sigma preserva e^{-f}dV ponto a ponto em dimensão 3.
        if np.max(np.abs(sigma)) > 2.0:
            return 1.0e100
        ricci_dilaton = np.exp(-2.0 * sigma) * (
            self.scalar_curvature - 4.0 * laplace + 7.0 * grad2
        )
        torsion = -0.5 * np.exp(-6.0 * sigma) * (self.b0 + beta * y) ** 2
        density = self.tau * (ricci_dilaton + torsion) + 3.0 * sigma
        return float(np.dot(self.weight, density))


def build_model(radius: float, tau: float, flux: int, quadrature: int) -> Model:
    y, raw = roots_jacobi(quadrature, 0.5, 0.5)
    # Integral normalizada em S3: (2/pi) int_-1^1 sqrt(1-y²) F(y)dy.
    weight = (2.0 / np.pi) * raw
    return Model(radius, tau, flux, y, weight)


def numerical_gradient(model: Model, coefficients: np.ndarray, beta: float) -> np.ndarray:
    step = 2.0e-6
    result = np.empty_like(coefficients)
    for index in range(coefficients.size):
        shift = np.zeros_like(coefficients)
        shift[index] = step
        result[index] = (
            model.action(coefficients + shift, beta)
            - model.action(coefficients - shift, beta)
        ) / (2.0 * step)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tau", type=float, default=1.0)
    parser.add_argument("--flux", type=int, default=1)
    parser.add_argument("--radius", type=float, default=1.998411184770)
    parser.add_argument("--quadrature", type=int, default=160)
    parser.add_argument("--beta-max", type=float, default=0.08)
    args = parser.parse_args()
    model = build_model(args.radius, args.tau, args.flux, args.quadrature)

    betas = np.linspace(0.0, args.beta_max, 17)
    actions = []
    solutions = []
    initial = np.zeros(4)
    for beta in betas:
        if beta == 0.0:
            actions.append(model.action(initial, beta))
            solutions.append(initial.copy())
            continue
        result = least_squares(
            lambda c: numerical_gradient(model, c, beta),
            initial,
            method="trf",
            xtol=1e-12,
            ftol=1e-12,
            gtol=1e-12,
            max_nfev=3000,
        )
        if not result.success or not np.all(np.isfinite(result.x)):
            raise RuntimeError(f"continuação estacionária falhou em beta={beta}: {result.message}")
        initial = result.x
        actions.append(model.action(result.x, beta))
        solutions.append(result.x)

    actions_array = np.asarray(actions)
    delta = actions_array - actions_array[0]
    design = np.column_stack((betas**2, betas**4, betas**6))
    c2, c4, c6 = np.linalg.lstsq(design, delta, rcond=None)[0]
    a2 = 2.0 * c2
    a4 = 4.0 * c4

    print("Q29 — RETROAÇÃO NÃO HOMOGÊNEA l=1")
    print(f"R={model.radius:.12f} tau={model.tau:.6f} n={model.flux}")
    print(f"b0={model.b0:.12e}")
    print(f"c2={c2:.12e} c4={c4:.12e} c6={c6:.12e}")
    print(f"a2={a2:.12e} a4={a4:.12e}")
    center_solution = solutions[0]
    print("sigma coefficients beta=0:", center_solution)
    print("fit max residual:", float(np.max(np.abs(design @ np.array([c2,c4,c6])-delta))))
    print("max |coefficient|:", float(np.max(np.abs(solutions))))
    if a2 < 0 and a4 > 0:
        print("veredito local: quebra estabilizada na ordem quartica")
        print("beta_vac (quartic) =", float(np.sqrt(-a2 / a4)))
    else:
        print("veredito local: a truncagem conformal não estabiliza a quebra")


if __name__ == "__main__":
    main()
