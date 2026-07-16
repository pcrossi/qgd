---
title: Manuscript chapter 01 called notes
status: active
concepts:
  - chapter 01 notes
  - derivations
  - path integrals
  - Wick rotation
  - Madelung
  - Nelson
  - NESS
---

# Manuscript chapter 01 called notes

This file records the technical notes explicitly called by Chapter 1. These
notes are part of the detailed memory of the initial problem.

## 1. Measures and path integrals

Source:

`manuscrito/notes/analysis/Medidas e integrais em espaços de caminhos.md`

Role:

Clarifies that an integral over paths is an integral over function space and
needs a construction specifying admissible paths, weights, and convergence.

Main points:

- a positive measure assigns nonnegative values to admissible sets;
- Wiener measure is a probability measure built from compatible Gaussian
  increments;
- Brownian paths do not have ordinary velocities because

$$
|\Delta x|\sim\sqrt{\Delta t}
$$

implies

$$
\frac{|\Delta x|}{\Delta t}
\sim\frac1{\sqrt{\Delta t}};
$$

- Feynman weights

$$
e^{iS[x]/\hbar}
$$

are oscillatory amplitudes, not positive probabilities.

Status:

Pedagogical analysis. It supports the claim that Wiener and Feynman path
integrals cannot be identified by notation alone.

## 2. Spectral continuation from unitary group to semigroup

Source:

`manuscrito/notes/derivations/Continuação espectral do grupo unitário ao semigrupo.md`

Role:

Provides the mathematical core behind Wick rotation in Chapter 1.

Hypotheses:

- `H` self-adjoint;
- `H` bounded below;
- after shifting energy, `H >= 0`.

By the spectral theorem:

$$
H=\int_0^\infty\lambda\,dE_H(\lambda).
$$

Real-time evolution:

$$
U(t)
=e^{-itH/\hbar}
=\int_0^\infty
e^{-it\lambda/\hbar}\,dE_H(\lambda)
$$

is unitary.

For

$$
z=t-i\tau,
\qquad
\tau>0,
$$

one has

$$
U(z)
=\int_0^\infty
e^{-iz\lambda/\hbar}\,dE_H(\lambda),
$$

with

$$
|e^{-iz\lambda/\hbar}|
=e^{-\tau\lambda/\hbar}\leq1.
$$

Thus:

$$
U(-i\tau)=e^{-\tau H/\hbar}.
$$

Status:

Theorem under hypotheses. It does not by itself prove Wiener representation,
reflection positivity, boundary correspondence, or causal reconstruction.

## 3. Elliptic, parabolic, hyperbolic, and dispersive equations

Source:

`manuscrito/notes/analysis/Equações elípticas, parabólicas, hiperbólicas e dispersivas.md`

Role:

Prevents confusion between local PDE type and physical boundary-value problem.

Core rule:

$$
\boxed{
\text{physical operator}
=\text{differential expression}
+\text{domain}
+\text{boundary conditions}.
}
$$

Main distinctions:

- elliptic: stationary spatial problems, such as Laplace and Helmholtz;
- parabolic: diffusion and smoothing, such as heat equation and gauge-fixed
  Ricci flow;
- hyperbolic: Lorentzian wave propagation with causal domains;
- dispersive: Schrödinger evolution, phase accumulation and interference.

Status:

Terminological and analytical convention. It fixes how Chapter 1 uses PDE
language and prevents identifying boundary conditions with the local principal
symbol.

## 4. Total derivative, boundary, and Euclidean continuation

Source:

`manuscrito/notes/derivations/Derivada total, bordo e continuação euclidiana.md`

Role:

Shows why gauge and boundary terms cannot be dropped before Wick rotation.

For

$$
L'=L+\frac{dF(x,t)}{dt},
$$

the action changes by

$$
S'[x]=S[x]+F(x_1,t_1)-F(x_0,t_0).
$$

Therefore:

$$
e^{iS'[x]/\hbar}
=e^{i(F_1-F_0)/\hbar}e^{iS[x]/\hbar}.
$$

After Euclidean continuation, if the continued boundary term is real:

$$
e^{-S_E'/\hbar}
=e^{-(F_{E,1}-F_{E,0})/\hbar}e^{-S_E/\hbar}.
$$

Status:

Exact identity with analytic caution. It does not say Wick breaks gauge
invariance; it says the bulk, states, and boundary must be continued together.

## 5. Madelung decomposition step by step

Source:

`manuscrito/notes/derivations/Decomposição de Madelung passo a passo.md`

Role:

Provides the full derivation behind the Chapter 1 Madelung section.

Hypotheses:

- nonrelativistic Schrödinger equation;
- `m>0`;
- real potential `V`;
- local region where `psi != 0`;
- sufficient regularity.

Decomposition:

$$
\psi=R e^{iS/\hbar},
\qquad
R>0,
\qquad
\rho=R^2.
$$

Imaginary part gives:

$$
\boxed{
\partial_t\rho+\nabla\cdot(\rho v)=0,
}
\qquad
v=\frac{\nabla S}{m}.
$$

Real part gives:

$$
\boxed{
\partial_tS+\frac{|\nabla S|^2}{2m}+V+Q[\rho]=0.
}
$$

with

$$
Q[\rho]
=-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
$$

Status:

Exact local identity inside Schrödinger theory. It does not derive
Schrödinger or the Madelung equations from the official GDQ action.

## 6. Nelson derivatives and continuity equation

Source:

`manuscrito/notes/derivations/Derivadas de Nelson e equação de continuidade.md`

Role:

Shows how non-differentiable paths can still generate regular mean current and
osmotic fields.

Forward process:

$$
dX_t=b_+(X_t,t)dt+\sqrt{2\nu}\,dW_t.
$$

Forward Fokker-Planck:

$$
\partial_t\rho
=-\nabla\cdot(b_+\rho)+\nu\Delta\rho.
$$

Backward Fokker-Planck:

$$
\partial_t\rho
=-\nabla\cdot(b_-\rho)-\nu\Delta\rho.
$$

Define:

$$
v=\frac{b_++b_-}{2},
\qquad
u=\frac{b_+-b_-}{2}.
$$

Adding gives:

$$
\boxed{
\partial_t\rho+\nabla\cdot(\rho v)=0.
}
$$

Subtracting gives:

$$
\nabla\cdot(\rho u-\nu\nabla\rho)=0.
$$

Under suitable global/boundary assumptions:

$$
\boxed{
u=\nu\nabla\ln\rho.
}
$$

Status:

Stochastic reduction. In GDQ it is a target limit unless `b_+`, `b_-`, `nu`,
and the causal prescription are derived from the official theory.

## 7. Osmotic velocity and quantum potential

Source:

`manuscrito/notes/derivations/Identidade entre velocidade osmótica e potencial quântico.md`

Role:

Connects the Nelson osmotic term to the Bohm-Madelung quantum potential.

For `rho>0`, with `R=sqrt(rho)`:

$$
\frac{\Delta R}{R}
=\frac12\Delta\ln\rho
+\frac14|\nabla\ln\rho|^2.
$$

If

$$
u=\nu\nabla\ln\rho,
$$

then

$$
m\nu\nabla\cdot u+\frac{m}{2}|u|^2
=2m\nu^2\frac{\Delta\sqrt\rho}{\sqrt\rho}.
$$

For

$$
\nu=\frac{\hbar}{2m},
$$

one obtains:

$$
\boxed{
Q[\rho]
=-\left(
m\nu\nabla\cdot u+\frac{m}{2}|u|^2
\right).
}
$$

Status:

Exact under hypotheses. It is a flat or Riemannian limit; weighted measure and
torsion can add GDQ corrections.

## 8. Universal diffusion and geometric inertia

Source:

`manuscrito/notes/derivations/Difusão universal e inércia geométrica - análise condicional.md`

Role:

Records the corrected status of the universal diffusion idea.

With

$$
\nu_0=\frac{\hbar}{2m_0},
\qquad
\Omega=\frac{m}{m_0},
$$

one gets:

$$
\nu_{\rm eff}
=\frac{\nu_0}{\Omega}
=\frac{\hbar}{2m}.
$$

But if `D=nu_0 Omega^{-1}` varies:

$$
\partial_t\rho
=-\nabla\cdot(b\rho)+\Delta(D\rho),
$$

not simply:

$$
\partial_t\rho
=-\nabla\cdot(b\rho)+D\Delta\rho.
$$

Thus:

$$
\Delta(D\rho)
=D\Delta\rho
+2\nabla D\cdot\nabla\rho
+\rho\Delta D.
$$

Status:

The stochastic correction is demonstrated. The origin of `Omega` from the
official GDQ background remains open.

## 9. Variable Nelson diffusion in GDQ

Source:

`manuscrito/notes/derivations/Difusão variável de Nelson na GDQ.md`

Role:

Gives the covariant version of the variable diffusion calculation on a
physical spatial leaf.

Data:

- spatial Riemannian leaf `(Sigma,h)`;
- normalized `rho>0`;
- fixed metric during the local stochastic step;
- if `h` depends on `t`, `partial_t dV_h` must be included.

Diffusion tensor:

$$
D^{ij}(x,t)=\nu_0\Omega^{-1}(x,t)h^{ij}(x).
$$

Forward process:

$$
dX_t^i=b_+^i\,dt+\sigma^i{}_a\,dW_t^a,
\qquad
\sigma^i{}_a\sigma^j{}_a=2D^{ij}.
$$

Forward Fokker-Planck:

$$
\partial_t\rho
=-\nabla_i(b_+^i\rho)
+\nabla_i\nabla_j(D^{ij}\rho).
$$

For isotropic `D`:

$$
\partial_t\rho
=-\nabla_i(b_+^i\rho)
+\nu_0\Delta_h(\Omega^{-1}\rho).
$$

Compatible osmotic velocity:

$$
\boxed{
u^i
=\nu_0\Omega^{-1}
\left(\nabla^i\ln\rho-\nabla^i\ln\Omega\right).
}
$$

Status:

Exact reduction after physical-leaf reconstruction. It does not alter the
official action and does not prove the solitonic origin of `Omega`.

## 10. NESS, geometric flow, and effective irreversibility

Source:

`manuscrito/notes/derivations/NESS, fluxo geométrico e irreversibilidade efetiva.md`

Role:

Prevents identifying three different evolutions:

- flow parameter `tau`;
- physical time `t`;
- reduced macroscopic dynamics after projection.

Closed physical evolution can preserve microscopic norm:

$$
\frac{d}{dt}\lVert\Psi(t)\rVert^2=0.
$$

Projection with `P` and `Q=1-P` can yield a Nakajima-Zwanzig equation:

$$
\frac{d}{dt}P\varrho(t)
=PLP\varrho(t)
+\int_0^tK(t-s)P\varrho(s)\,ds
+I(t).
$$

In a short-memory limit, the reduced entropy may satisfy:

$$
\frac{dS_{\rm macro}}{dt}\ge0.
$$

A NESS satisfies stationarity of monitored macroscopic observables:

$$
\frac{d}{dt}\langle O_a\rangle_{\rm ss}=0
$$

while still allowing currents:

$$
J_a\neq0.
$$

Status:

Effective reduction. Perelman monotonicity in `tau` alone does not prove
physical irreversibility in `t`; apparatus, interface, monitored degrees, and
causal mobility are required.

