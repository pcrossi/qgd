#!/usr/bin/env python3
"""Álgebra linear da Porta C da ponte global--local GDQ.

Este módulo NÃO constrói uma sela e NÃO aproxima a Hessiana física por J.T@J.
Ele monta, a partir de operadores já derivados e avaliados numa sela:

    A = [D C ; R^* G],
    P_phys = I - G^{-1} A^* (A G^{-1} A^*)^+ A,
    H_aug = H_S - sum_a lambda_a H_C[a],
    K_phys = Z^* H_aug Z,

onde as colunas de Z formam uma base G-ortonormal do espaço físico.

Classificação: teste de consistência/infraestrutura espectral. Não é cálculo
do gap físico enquanto background, multiplicadores e Hessianas oficiais não
forem fornecidos.
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np
from scipy.linalg import null_space


def _herm(a: np.ndarray) -> np.ndarray:
    return (a + a.conj().T) / 2


@dataclass(frozen=True)
class PortaCResult:
    projector: np.ndarray
    physical_basis: np.ndarray
    augmented_hessian: np.ndarray
    reduced_hessian: np.ndarray
    eigenvalues: np.ndarray
    combined_operator: np.ndarray


def g_orthonormal_kernel(A: np.ndarray, G: np.ndarray, rcond=1e-11) -> np.ndarray:
    """Base Z de ker(A), normalizada por Z^* G Z = I."""
    Z0 = null_space(A, rcond=rcond)
    if Z0.shape[1] == 0:
        return Z0
    gram = _herm(Z0.conj().T @ G @ Z0)
    d, U = np.linalg.eigh(gram)
    if np.min(d) <= rcond * max(1.0, np.max(d)):
        raise ValueError("G não é positiva no núcleo físico")
    return Z0 @ U @ np.diag(d ** -0.5)


def physical_projector(DC: np.ndarray, R: np.ndarray, G: np.ndarray,
                       rcond=1e-11):
    """Projeta em ker(DC) interseção (Ran R)^{perp_G}.

    R tem uma coluna por gerador infinitesimal de difeomorfismo/gauge.
    Dependências entre vínculos ou geradores são tratadas pela pseudoinversa.
    """
    n = G.shape[0]
    if G.shape != (n, n) or DC.shape[1] != n or R.shape[0] != n:
        raise ValueError("dimensões incompatíveis em DC, R ou G")
    G = _herm(np.asarray(G))
    if np.min(np.linalg.eigvalsh(G)) <= 0:
        raise ValueError("G deve ser Hermitiana positiva")
    A = np.vstack((DC, R.conj().T @ G))
    Ginv = np.linalg.inv(G)
    middle = A @ Ginv @ A.conj().T
    P = np.eye(n, dtype=np.result_type(A, G)) - (
        Ginv @ A.conj().T @ np.linalg.pinv(middle, rcond=rcond) @ A
    )
    Z = g_orthonormal_kernel(A, G, rcond=rcond)
    return P, Z, A


def augmented_hessian(H_action: np.ndarray, multipliers: np.ndarray,
                      H_constraints: list[np.ndarray]) -> np.ndarray:
    """Hessiana de S - sum lambda_a C_a; nunca Hessiana de mínimos quadrados."""
    if len(multipliers) != len(H_constraints):
        raise ValueError("cada vínculo exige multiplicador e Hessiana")
    H = np.array(H_action, dtype=np.result_type(H_action, multipliers), copy=True)
    for lam, HC in zip(multipliers, H_constraints):
        H -= lam * HC
    return _herm(H)


def assemble_porta_c(DC: np.ndarray, R: np.ndarray, G: np.ndarray,
                     H_action: np.ndarray, multipliers: np.ndarray,
                     H_constraints: list[np.ndarray], rcond=1e-11) -> PortaCResult:
    """Monta a Porta C depois que uma sela verdadeira foi fornecida."""
    P, Z, A = physical_projector(DC, R, G, rcond=rcond)
    Haug = augmented_hessian(H_action, multipliers, H_constraints)
    Kred = _herm(Z.conj().T @ Haug @ Z)
    ev = np.linalg.eigvalsh(Kred) if Kred.size else np.array([])
    return PortaCResult(P, Z, Haug, Kred, ev, A)


def diagnostics(result: PortaCResult, G: np.ndarray) -> dict[str, float]:
    P, Z, A = result.projector, result.physical_basis, result.combined_operator
    return {
        "projector_idempotence": float(np.linalg.norm(P @ P - P)),
        "projector_G_selfadjoint": float(np.linalg.norm(P.conj().T @ G - G @ P)),
        "constraints_on_projector": float(np.linalg.norm(A @ P)),
        "constraints_on_basis": float(np.linalg.norm(A @ Z)),
        "basis_G_orthonormal": float(np.linalg.norm(Z.conj().T @ G @ Z - np.eye(Z.shape[1]))),
        "reduced_hessian_hermitian": float(np.linalg.norm(result.reduced_hessian-result.reduced_hessian.conj().T)),
    }

