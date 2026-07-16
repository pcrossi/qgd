#!/usr/bin/env python3
"""Motor variacional extensível para a ponte global--local.

Este arquivo separa a integração/sensibilidade da física do ansatz. Um novo
par canônico de J só pode ser incluído por um modelo que forneça explicitamente
estado inicial, campos hamiltonianos, adaptador e resíduos. Não há dinâmica
default para J.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import numpy as np
from scipy.integrate import solve_ivp

from ponte_global_local_integrador import Parameters, rhs_complex as inner_rhs
from ponte_global_local_exterior_causal_equacoes import (
    constraint as causal_constraint, rhs as causal_rhs,
    velocities as causal_velocities,
)
from ponte_global_local_solver_portas_bd import LOG_R_COS, historical_seed

EPS = 1e-30


class ShootingModel(Protocol):
    parameter_count: int

    def initial(self, theta: np.ndarray, side: str) -> np.ndarray: ...
    def collar_field(self, s: float, state: np.ndarray, theta: np.ndarray, side: str) -> np.ndarray: ...
    def exterior_initial(self, left: np.ndarray, theta: np.ndarray) -> np.ndarray: ...
    def exterior_field(self, s: float, state: np.ndarray, theta: np.ndarray) -> np.ndarray: ...
    def residual(self, exterior: np.ndarray, right: np.ndarray,
                 exterior0: np.ndarray, theta: np.ndarray) -> np.ndarray: ...


@dataclass(frozen=True)
class EngineOptions:
    rtol: float = 2e-8
    atol: float = 2e-10
    collar_steps: int = 70
    exterior_steps: int = 100


def _partials(function, state, theta, parameter_count):
    n = state.size
    m = np.asarray(function(state, theta)).size
    a = np.empty((m, n))
    b = np.empty((m, parameter_count))
    for k in range(n):
        z = state.astype(complex); z[k] += 1j*EPS
        a[:, k] = np.imag(function(z, theta))/EPS
    for k in range(parameter_count):
        th = theta.astype(complex); th[k] += 1j*EPS
        b[:, k] = np.imag(function(state.astype(complex), th))/EPS
    return a, b


def _initial_value_jac(function, theta, parameter_count):
    value = function(theta)
    jac = np.empty((value.size, parameter_count))
    for k in range(parameter_count):
        th = theta.astype(complex); th[k] += 1j*EPS
        jac[:, k] = np.imag(function(th))/EPS
    return np.real(value), jac


def _flow(field, value, jac, theta, parameter_count, options, max_step):
    n = value.size

    def augmented(s, joined):
        state = joined[:n]
        sensitivity = joined[n:].reshape(n, parameter_count)
        f = np.real(field(s, state, theta))
        a, b = _partials(lambda y, th: field(s, y, th), state, theta, parameter_count)
        return np.r_[f, (a@sensitivity+b).ravel()]

    solution = solve_ivp(
        augmented, (0, 1), np.r_[value, jac.ravel()], method="DOP853",
        rtol=options.rtol, atol=options.atol, max_step=max_step,
    )
    if not solution.success:
        raise RuntimeError(solution.message)
    return solution.y[:n, -1], solution.y[n:, -1].reshape(n, parameter_count)


def _map_value_jac(function, state, state_jac, theta, parameter_count):
    value = function(state, theta)
    dstate, explicit = _partials(function, state, theta, parameter_count)
    return np.real(value), dstate@state_jac+explicit


def evaluate(model: ShootingModel, theta: np.ndarray,
             options: EngineOptions = EngineOptions()):
    """Integra os três domínios e retorna resíduo e Jacobiana transportada."""
    theta = np.asarray(theta, dtype=float)
    p = model.parameter_count
    if theta.shape != (p,):
        raise ValueError(f"esperados {p} parâmetros, recebidos {theta.shape}")

    left0, dleft0 = _initial_value_jac(lambda th: model.initial(th, "L"), theta, p)
    right0, dright0 = _initial_value_jac(lambda th: model.initial(th, "R"), theta, p)
    left, dleft = _flow(
        lambda s,y,th: model.collar_field(s,y,th,"L"),
        left0, dleft0, theta, p, options, 1/options.collar_steps,
    )
    right, dright = _flow(
        lambda s,y,th: model.collar_field(s,y,th,"R"),
        right0, dright0, theta, p, options, 1/options.collar_steps,
    )
    exterior0, dexterior0 = _map_value_jac(model.exterior_initial, left, dleft, theta, p)
    exterior, dexterior = _flow(
        model.exterior_field, exterior0, dexterior0, theta, p, options,
        1/options.exterior_steps,
    )

    # Diferencia o mapa residual em seus três argumentos sem assumir dimensões.
    residual = model.residual(exterior, right, exterior0, theta)
    nr = residual.size
    de = np.empty((nr, exterior.size))
    dr = np.empty((nr, right.size))
    d0 = np.empty((nr, exterior0.size))
    dt = np.empty((nr, p))
    for k in range(exterior.size):
        z=exterior.astype(complex);z[k]+=1j*EPS
        de[:,k]=np.imag(model.residual(z,right.astype(complex),exterior0.astype(complex),theta))/EPS
    for k in range(right.size):
        z=right.astype(complex);z[k]+=1j*EPS
        dr[:,k]=np.imag(model.residual(exterior.astype(complex),z,exterior0.astype(complex),theta))/EPS
    for k in range(exterior0.size):
        z=exterior0.astype(complex);z[k]+=1j*EPS
        d0[:,k]=np.imag(model.residual(exterior.astype(complex),right.astype(complex),z,theta))/EPS
    for k in range(p):
        th=theta.astype(complex);th[k]+=1j*EPS
        dt[:,k]=np.imag(model.residual(exterior.astype(complex),right.astype(complex),exterior0.astype(complex),th))/EPS
    jacobian = de@dexterior + dr@dright + d0@dexterior0 + dt
    return np.real(residual), jacobian


class BaseCausalModel:
    """Modelo de regressão sem J dinâmico; K_gamma=1, h energético fixável."""
    parameter_count = 11

    def __init__(self, energy_h=0.0, energy_initial=-0.3333554761281252):
        self.energy_target=(1-energy_h)*energy_initial+energy_h

    def initial(self, theta, side):
        j=0 if side=="L" else 4;a,c=np.exp(theta[j]),np.exp(theta[j+1]);tau=np.exp(theta[8])
        u=4-8*tau/a**2+4*tau*c**2/a**4-tau/c**2
        return np.array([a,c,u,0,theta[j+2],0,0],dtype=np.result_type(theta))

    def collar_field(self, _s, state, theta, side):
        j=0 if side=="L" else 4;c0=np.exp(theta[j+1]);length=np.exp(theta[j+3]);tau=np.exp(theta[8])
        params=Parameters(tau=tau,h0=-2*c0**2,pv=0,hopf_m=1,kappa_psi=1)
        return length*inner_rhs(state,params)

    def exterior_initial(self,left,theta):
        a,c,u,v,pia,pic,piu=left
        return np.array([0,0,np.log(a),np.log(c),u,v,0,theta[9],theta[10],a*pia,c*pic,piu,0,0],dtype=np.result_type(left,theta))

    def exterior_field(self,_s,state,theta):
        tau=np.exp(theta[8]);base=causal_rhs(0,state[:13],tau);_,volume,_=causal_velocities(state[:13],tau)
        return .5*np.r_[base,volume]

    def residual(self,q,right,q0,theta):
        a,c,u,_v,pia,pic,piu=right;tau=np.exp(theta[8]);z=q[13]
        energy=q[7]*np.exp(-q[0])/z-self.energy_target
        return np.array([q[0],q[1],q[2]-np.log(a),q[3]-np.log(c),q[4]-u,
            q[9]+a*pia,q[10]+c*pic,q[11]+piu,causal_constraint(q0[:13],tau),
            (2*q[2]+q[3])/3-LOG_R_COS,energy])


class JCanonicalModelTemplate(BaseCausalModel):
    """Histórico: modo homogêneo excluído pelo tensor de Nijenhuis."""
    parameter_count = 13

    def initial(self, theta, side):
        raise RuntimeError("modo J homogêneo excluído: Nijenhuis não nulo")

    def collar_field(self, s, state, theta, side):
        raise RuntimeError("modo J homogêneo excluído: Nijenhuis não nulo")

    def exterior_initial(self, left, theta):
        raise RuntimeError("modo J homogêneo excluído: Nijenhuis não nulo")

    def exterior_field(self, s, state, theta):
        raise RuntimeError("modo J homogêneo excluído: Nijenhuis não nulo")

    def residual(self, exterior, right, exterior0, theta):
        raise RuntimeError("modo J homogêneo excluído: Nijenhuis não nulo")


class BeltramiCanonicalModelTemplate(BaseCausalModel):
    """Contrato para um harmônico Beltrami complexo fixo.

    O par complexo (A_B,P_B) ocupa quatro componentes reais. Duas amplitudes
    complexas regulares, uma em cada garganta, acrescentam quatro parâmetros;
    continuidade de amplitude e balanço de momento acrescentam quatro
    resíduos. Nenhuma dessas fórmulas é presumida aqui.
    """
    parameter_count = 15
    beltrami_real_state_dimension = 4
    beltrami_matching_dimension = 4

    def __init__(self, harmonic_label, operator=None, contribution=None):
        super().__init__()
        self.harmonic_label = harmonic_label
        self.operator = operator
        self.contribution = contribution

    def _missing(self, item):
        raise NotImplementedError(
            f"harmônico Beltrami {self.harmonic_label}: aguardando {item} derivado"
        )

    def initial(self, theta, side):
        self._missing("condição regular e relação canônica amplitude--momento")

    def collar_field(self, s, state, theta, side):
        self._missing("operador radial e backreaction no colar")

    def exterior_initial(self, left, theta):
        self._missing("adaptador canônico de interface")

    def exterior_field(self, s, state, theta):
        self._missing("Hamiltoniano reduzido no exterior")

    def residual(self, exterior, right, exterior0, theta):
        self._missing("quatro condições de matching Beltrami")


if __name__ == "__main__":
    r,j=evaluate(BaseCausalModel(),historical_seed())
    print("base residual inf =",np.linalg.norm(r,np.inf))
    print("base shape/rank =",j.shape,np.linalg.matrix_rank(j))
