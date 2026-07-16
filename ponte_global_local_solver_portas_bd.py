#!/usr/bin/env python3
"""Infraestrutura robusta para as Portas B/D da ponte global--local.

Classificacao cientifica
-----------------------
Teste numerico de consistencia e infraestrutura de busca condicional. Este
modulo nao escolhe ``K_gamma`` e nao declara uma sela. O vinculo energetico
so entra por um funcional fornecido pela Porta A.

A Jacobiana do mapa de tiro e obtida transportando as equacoes variacionais
em cada dominio. Diferencas finitas de solucoes completas sao usadas somente
no teste independente de auditoria, nunca pelo solver.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional, Tuple

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares

from ponte_global_local_integrador import Parameters, rhs_complex as inner_rhs
from ponte_global_local_exterior_causal_equacoes import (
    constraint as causal_constraint,
    rhs as causal_rhs,
    velocities as causal_velocities,
)

NPAR = 11
EPS_CS = 1.0e-30
ALPHA = 1.0 / 137.035999177
R_COS = np.pi**2 * np.sqrt(ALPHA)
LOG_R_COS = np.log(R_COS)

# value, derivative with respect to final augmented state, explicit theta
# derivative. The returned value must already be C_E, not an energy to be
# post-normalized inside this module.
EnergyFunctional = Callable[[np.ndarray, np.ndarray], Tuple[float, np.ndarray, np.ndarray]]


@dataclass(frozen=True)
class TransportOptions:
    rtol: float = 2.0e-8
    atol: float = 2.0e-10
    collar_steps: int = 70
    causal_steps: int = 100


def throat_state(theta: np.ndarray, side: str) -> np.ndarray:
    j = 0 if side == "L" else 4
    a, c = np.exp(theta[j]), np.exp(theta[j + 1])
    tau = np.exp(theta[8])
    u = 4.0 - 8.0 * tau / a**2 + 4.0 * tau * c**2 / a**4 - tau / c**2
    return np.array(
        [a, c, u, 0.0, theta[j + 2], 0.0, 0.0],
        dtype=np.result_type(theta),
    )


def collar_field(_s: float, state: np.ndarray, theta: np.ndarray, side: str) -> np.ndarray:
    j = 0 if side == "L" else 4
    c0 = np.exp(theta[j + 1])
    length = np.exp(theta[j + 3])
    tau = np.exp(theta[8])
    params = Parameters(tau=tau, h0=-2.0 * c0**2, pv=0.0, hopf_m=1, kappa_psi=1.0)
    return length * inner_rhs(state, params)


def causal_field(_s: float, state: np.ndarray, theta: np.ndarray) -> np.ndarray:
    """Exterior causal em intervalo unitario; o comprimento fisico e 1/2."""
    tau = np.exp(theta[8])
    base = causal_rhs(0.5 * _s, state[:13], tau)
    _, volume, _ = causal_velocities(state[:13], tau)
    return 0.5 * np.r_[base, volume]


def _complex_jacobians(field, state: np.ndarray, theta: np.ndarray):
    n = state.size
    d_state = np.empty((n, n))
    d_theta = np.empty((n, NPAR))
    for k in range(n):
        z = state.astype(complex)
        z[k] += 1j * EPS_CS
        d_state[:, k] = np.imag(field(0.0, z, theta))/EPS_CS
    for k in range(NPAR):
        th = theta.astype(complex)
        th[k] += 1j * EPS_CS
        d_theta[:, k] = np.imag(field(0.0, state.astype(complex), th))/EPS_CS
    return d_state, d_theta


def _initial_sensitivity(initial, theta: np.ndarray):
    state = initial(theta)
    sensitivity = np.empty((state.size, NPAR))
    for k in range(NPAR):
        th = theta.astype(complex)
        th[k] += 1j * EPS_CS
        sensitivity[:, k] = np.imag(initial(th))/EPS_CS
    return np.real(state), sensitivity


def _transport(field, state, sensitivity, theta, options, max_step):
    n = state.size

    def augmented(s, joined):
        y = joined[:n]
        dy = joined[n:].reshape(n, NPAR)
        value = np.real(field(s, y, theta))
        a, b = _complex_jacobians(field, y, theta)
        return np.r_[value, (a @ dy + b).ravel()]

    solution = solve_ivp(
        augmented,
        (0.0, 1.0),
        np.r_[state, sensitivity.ravel()],
        method="DOP853",
        rtol=options.rtol,
        atol=options.atol,
        max_step=max_step,
    )
    if not solution.success:
        raise RuntimeError(solution.message)
    return solution.y[:n, -1], solution.y[n:, -1].reshape(n, NPAR)


def causal_initial(left: np.ndarray, dleft: np.ndarray, theta: np.ndarray):
    a, c, u, v, pia, pic, piu = left
    state = np.array(
        [0.0, 0.0, np.log(a), np.log(c), u, v, 0.0,
         theta[9], theta[10], a*pia, c*pic, piu, 0.0, 0.0]
    )
    adapter = np.zeros((14, 7))
    adapter[2, 0] = 1.0/a
    adapter[3, 1] = 1.0/c
    adapter[4, 2] = 1.0
    adapter[5, 3] = 1.0
    adapter[9, 0] = pia
    adapter[9, 4] = a
    adapter[10, 1] = pic
    adapter[10, 5] = c
    adapter[11, 6] = 1.0
    sensitivity = adapter @ dleft
    sensitivity[7, 9] += 1.0
    sensitivity[8, 10] += 1.0
    return state, sensitivity


def _constraint_gradient(state13: np.ndarray, theta: np.ndarray):
    tau = np.exp(theta[8])
    gradient = np.empty(13)
    for k in range(13):
        z = state13.astype(complex)
        z[k] += 1j * EPS_CS
        gradient[k] = np.imag(causal_constraint(z, tau))/EPS_CS
    th = theta.astype(complex)
    th[8] += 1j * EPS_CS
    explicit = np.zeros(NPAR)
    explicit[8] = np.imag(causal_constraint(state13.astype(complex), np.exp(th[8])))/EPS_CS
    return gradient, explicit


def residual_jacobian(
    theta: np.ndarray,
    energy: Optional[EnergyFunctional] = None,
    options: TransportOptions = TransportOptions(),
    log_r_cos: float = LOG_R_COS,
):
    """Retorna os dez vinculos B independentes e, opcionalmente, C_E.

    Sem ``energy`` o sistema e deliberadamente retangular 10 x 11. Isso
    permite testar transporte, posto e continuacao sem fabricar a ultima
    condicao. Com ``energy``, a Porta A e responsavel pelo valor e gradiente.
    """
    theta = np.asarray(theta, dtype=float)
    left0, dleft0 = _initial_sensitivity(lambda th: throat_state(th, "L"), theta)
    right0, dright0 = _initial_sensitivity(lambda th: throat_state(th, "R"), theta)
    left, dleft = _transport(
        lambda s, y, th: collar_field(s, y, th, "L"),
        left0, dleft0, theta, options, 1.0/options.collar_steps,
    )
    right, dright = _transport(
        lambda s, y, th: collar_field(s, y, th, "R"),
        right0, dright0, theta, options, 1.0/options.collar_steps,
    )
    exterior0, dexterior0 = causal_initial(left, dleft, theta)
    exterior, dexterior = _transport(
        causal_field, exterior0, dexterior0, theta, options,
        1.0/options.causal_steps,
    )

    a, c, u, _v, pia, pic, piu = right
    residual = np.array([
        exterior[0], exterior[1],
        exterior[2] - np.log(a), exterior[3] - np.log(c), exterior[4] - u,
        exterior[9] + a*pia, exterior[10] + c*pic, exterior[11] + piu,
        causal_constraint(exterior0[:13], np.exp(theta[8])),
        (2.0*exterior[2] + exterior[3])/3.0 - log_r_cos,
    ])
    jacobian = np.zeros((10, NPAR))
    jacobian[0] = dexterior[0]
    jacobian[1] = dexterior[1]
    jacobian[2] = dexterior[2] - dright[0]/a
    jacobian[3] = dexterior[3] - dright[1]/c
    jacobian[4] = dexterior[4] - dright[2]
    jacobian[5] = dexterior[9] + pia*dright[0] + a*dright[4]
    jacobian[6] = dexterior[10] + pic*dright[1] + c*dright[5]
    jacobian[7] = dexterior[11] + dright[6]
    gradient, explicit = _constraint_gradient(exterior0[:13], theta)
    jacobian[8] = gradient @ dexterior0[:13] + explicit
    jacobian[9] = (2.0*dexterior[2] + dexterior[3])/3.0

    if energy is not None:
        value, d_final, d_explicit = energy(exterior, theta)
        d_final = np.asarray(d_final, dtype=float)
        d_explicit = np.asarray(d_explicit, dtype=float)
        if d_final.shape != (14,) or d_explicit.shape != (NPAR,):
            raise ValueError("A Porta A deve retornar gradientes de formas (14,) e (11,)")
        residual = np.r_[residual, value]
        jacobian = np.vstack((jacobian, d_final @ dexterior + d_explicit))

    return residual, jacobian


def residual_only(
    theta: np.ndarray,
    energy: Optional[EnergyFunctional] = None,
    options: TransportOptions = TransportOptions(),
    log_r_cos: float = LOG_R_COS,
):
    """Mapa de tiro sem sensibilidades, usado nas tentativas da busca.

    Esta rotina evita recalcular as matrizes variacionais quando o algoritmo
    apenas testa um novo passo. A Jacobiana aceita continua vindo
    exclusivamente de :func:`residual_jacobian`.
    """
    theta = np.asarray(theta, dtype=float)

    def collar(side):
        state = np.real(throat_state(theta, side))
        solution = solve_ivp(
            lambda s, y: np.real(collar_field(s, y, theta, side)),
            (0.0, 1.0), state, method="DOP853", rtol=options.rtol,
            atol=options.atol, max_step=1.0/options.collar_steps,
        )
        if not solution.success:
            raise RuntimeError(solution.message)
        return solution.y[:, -1]

    left, right = collar("L"), collar("R")
    exterior0, _ = causal_initial(left, np.zeros((7, NPAR)), theta)
    solution = solve_ivp(
        lambda s, y: np.real(causal_field(s, y, theta)),
        (0.0, 1.0), exterior0, method="DOP853", rtol=options.rtol,
        atol=options.atol, max_step=1.0/options.causal_steps,
    )
    if not solution.success:
        raise RuntimeError(solution.message)
    exterior = solution.y[:, -1]
    a, c, u, _v, pia, pic, piu = right
    residual = np.array([
        exterior[0], exterior[1],
        exterior[2] - np.log(a), exterior[3] - np.log(c), exterior[4] - u,
        exterior[9] + a*pia, exterior[10] + c*pic, exterior[11] + piu,
        causal_constraint(exterior0[:13], np.exp(theta[8])),
        (2.0*exterior[2] + exterior[3])/3.0 - log_r_cos,
    ])
    if energy is not None:
        value, _d_final, _d_explicit = energy(exterior, theta)
        residual = np.r_[residual, value]
    return residual


def energy_ratio_from_porta_a(k_gamma: float, target: float = 1.0) -> EnergyFunctional:
    """Adapta um K_gamma *ja derivado* pela Porta A.

    A ausencia de valor padrao e intencional: este construtor nao pode ser
    chamado sem que a normalizacao causal tenha sido obtida externamente.
    """
    if not np.isfinite(k_gamma) or k_gamma <= 0.0:
        raise ValueError("k_gamma deve ser positivo, finito e derivado pela Porta A")

    def functional(state: np.ndarray, _theta: np.ndarray):
        z = state[13]
        if z <= 0.0:
            raise ValueError("A normalizacao acumulada Z deve ser positiva")
        factor = k_gamma * state[7] * np.exp(-state[0]) / z
        gradient = np.zeros(14)
        gradient[0] = -factor
        gradient[7] = k_gamma*np.exp(-state[0])/z
        gradient[13] = -factor/z
        return factor - target, gradient, np.zeros(NPAR)

    return functional


def historical_seed() -> np.ndarray:
    old = np.array([
        -7.75631235e-1, -1.00456477, -4.39191944e-5, -1.43954597,
        -9.33914189e-1, -3.63068075e-1, -1.54334445e-3, -2.28771423,
        -2.90976275, -1.15737646e-2,
    ])
    return np.r_[old[:9], old[9]/4.0, 3.0*old[9]/4.0]


def solve_porta_b(
    energy: EnergyFunctional,
    seed: Optional[np.ndarray] = None,
    options: TransportOptions = TransportOptions(),
    max_nfev: int = 250,
):
    """Busca a sela reduzida somente depois de a Porta A fornecer C_E.

    O argumento ``energy`` e obrigatorio. Assim, nem um valor unitario nem um
    ``K_gamma`` inferido do alvo pode entrar silenciosamente na Porta B.
    """
    if energy is None:
        raise ValueError("A Porta B requer o funcional energetico derivado pela Porta A")
    if seed is None:
        seed = historical_seed()
    lower = np.array([-2, -2, -1, -3, -2, -2, -1, -3, -4, -1, -1.0])
    upper = np.array([1, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1.0])
    jac_cache = {}

    def differentiated(theta):
        key = np.asarray(theta).tobytes()
        if key not in jac_cache:
            jac_cache.clear()
            jac_cache[key] = residual_jacobian(theta, energy=energy, options=options)[1]
        return jac_cache[key]

    result = least_squares(
        lambda th: residual_only(th, energy=energy, options=options),
        np.asarray(seed),
        jac=differentiated,
        bounds=(lower, upper),
        x_scale="jac",
        xtol=2.0e-10,
        ftol=2.0e-10,
        gtol=2.0e-10,
        max_nfev=max_nfev,
    )
    # Reavaliacao independente da cache, com tolerancia mais estrita.
    strict = TransportOptions(rtol=2e-10, atol=2e-12, collar_steps=180, causal_steps=240)
    residual, jacobian = residual_jacobian(result.x, energy=energy, options=strict)
    singular = np.linalg.svd(jacobian, compute_uv=False)
    tolerance = max(jacobian.shape)*np.finfo(float).eps*singular[0]
    report = {
        "result": result,
        "residual_strict": residual,
        "jacobian_strict": jacobian,
        "singular_values": singular,
        "rank": int(np.sum(singular > tolerance)),
        "condition": float(singular[0]/singular[-1]) if singular[-1] > 0 else np.inf,
        "accepted_algebraically": bool(
            np.linalg.norm(residual, ord=np.inf) < 1.0e-9
            and np.sum(singular > tolerance) == NPAR
        ),
    }
    return report


if __name__ == "__main__":
    residual, jacobian = residual_jacobian(historical_seed())
    singular = np.linalg.svd(jacobian, compute_uv=False)
    print("Portas B/D sem vinculo energetico da Porta A")
    print("residual =", repr(residual))
    print("norm_inf =", np.linalg.norm(residual, ord=np.inf))
    print("singular_values =", repr(singular))
    print("rank =", np.linalg.matrix_rank(jacobian))
    print("shape =", jacobian.shape)
