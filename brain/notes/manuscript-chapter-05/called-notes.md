---
title: Manuscript chapter 05 called notes
status: active
---

# Manuscript chapter 05 called notes

## Directly called notes

### `manuscrito/notes/equations/Derivação da corrente de fase.md`

Called by section 05.3.

Main content:

- fixes `g`, `rho`, `z_tau` and the contour;
- varies only `S_R`;
- derives the current from the phase gradient sector:

$$
\nabla_\mu
\left(
\mathcal U g^{\mu\bar\nu}
\partial_{\bar\nu}S_R
\right)=0;
$$

- defines the reduced current convention:

$$
J_S^\mu
=\frac{2\tau}{\hbar^2}
\mathcal U g^{\mu\bar\nu}
\partial_{\bar\nu}S_R;
$$

- identifies the boundary momentum as `n_mu J_S^mu`.

Status: compact derivation of the phase-current calculation.

### `manuscrito/notes/equations/Da energia de amplitude ao termo de Bohm.md`

Referenced by the density/Bohm discussion.

Main content:

- proves:

$$
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=\frac12\Delta\ln\rho
+\frac14|\nabla\ln\rho|^2;
$$

- shows that, after nonrelativistic kinetic normalization, the amplitude
  energy variation yields:

$$
Q_B
=-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
$$

Status: reduced-sector check. The operator is already derived in the bulk;
the mass coefficient belongs to the physical reduction.

### `manuscrito/notes/equations/Auditoria do termo canonico rho d_t S_R.md`

Referenced by section 05.7.

Main content:

- checks whether the official action directly implies:

$$
\Theta_\Sigma
=\int_\Sigma\rho\,\delta S_R\,d\Sigma;
$$

- concludes that it does not hold automatically. The official action gives:

$$
\Pi_{S_R}
=n_\mu\widehat J_S^\mu
=\frac{2\tau}{\hbar\Lambda_C^2}
\mathcal U
n_\mu g^{\mu\bar\nu}\partial_{\bar\nu}S_R;
$$

- therefore `Pi_{S_R}=rho` is not a general off-shell identity;
- gives the exact condition needed after pushforward:

$$
\Pi_{S_R}^{\rm lab}=\rho_{\rm lab};
$$

- proves a conditional Routh-Schwarz result: for

$$
H_t[\Pi,\rho]
=\int_\Sigma\frac{\Pi^2}{2A\rho}\,d\Sigma,
\qquad A>0,
$$

fixed `Q_S` and `N_rho` imply

$$
\Pi=\frac{Q_S}{N_\rho}\rho
$$

at the minimizer;

- records that `Pi=rho` follows if `Q_S=N_rho=1`, `A` is constant, there is
  no leakage, and the physical sector is the convex minimizer;
- audits failed/insufficient attempts based on Killing-Perelman and purely
  adiabatic arguments;
- proves the exact Kähler state-space form:

$$
\Theta_{\rm state}
=\hbar\operatorname{Im}\langle\Psi,\delta\Psi\rangle
=\int_\Sigma\rho\,\delta S_R\,d\Sigma,
$$

but emphasizes that this state-space symplectic form is not automatically the
GDQ covariant Cauchy symplectic form.

Status: central cautionary note. It preserves the conditional route to
Madelung while preventing the false claim that the canonical term is already
an off-shell identity of the official action.
