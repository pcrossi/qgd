---
title: Madelung canonical sector
status: active
concepts:
  - Madelung
  - canonical term
  - Routh
  - state space
---

# Madelung canonical sector

## Statement

The pair `(rho,S_R)` has a natural Kähler state-space symplectic form, and the
Madelung equations follow if the physical reduction selects the canonical
sector

$$
p_\rho=0,
\qquad
\Pi_{S_R}=\sqrt h\,\rho.
$$

## State-space identity

For

$$
\Psi=\sqrt\rho\,e^{iS_R/\hbar},
$$

one has

$$
\Theta_{\rm state}
=\hbar\operatorname{Im}\langle\Psi,\delta\Psi\rangle
=\int_\Sigma\rho\,\delta S_R\,d\Sigma,
$$

and

$$
\Omega_{\rm state}
=\int_\Sigma\delta\rho\wedge\delta S_R\,d\Sigma.
$$

## Conditional Routh result

If the reduced temporal Hamiltonian is

$$
H_t[\Pi,\rho]
=\int_\Sigma\frac{\Pi^2}{2A\rho}\,d\Sigma,
\qquad A>0,
$$

with constant `A`, fixed charge

$$
Q_S=\int_\Sigma\Pi,
$$

and normalization

$$
N_\rho=\int_\Sigma\rho,
$$

then Cauchy-Schwarz gives the minimizer

$$
\Pi=\frac{Q_S}{N_\rho}\rho.
$$

For the primitive sector `Q_S=N_rho=1`, this yields `Pi=rho`.

## Caution

This is not an off-shell identity of the official action. It requires the
bridge/reduction to select the canonical state-space polarization.

## Sources

- `manuscrito/05_equations_conservation/05.7 - O que foi demonstrado e o que depende da reconstrução física.md`
- `manuscrito/notes/equations/Auditoria do termo canonico rho d_t S_R.md`
