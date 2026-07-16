---
title: Manuscript chapter 01 details
status: active
concepts:
  - initial problem
  - path integrals
  - Wiener
  - Feynman
  - Wick
  - Madelung
  - Nelson
  - Perelman
---

# Manuscript chapter 01 details

## 1. Methodological starting point

Chapter 1 starts from the Wigner problem: mathematics is unexpectedly effective
in natural science, but the success of a formalism does not by itself explain
the physical meaning of its structures.

In the manuscript this becomes a working rule:

- predictive agreement is not enough;
- the theory must explain why the mathematical pieces fit together;
- GDQ should not replace one successful operational formalism with another
  unexplained formalism;
- geometry is introduced as a candidate physical structure only after the
  Wiener-Feynman split is isolated.

Source:

`manuscrito/01_initial_problem/01.1 - A eficácia da matemática na descrição da natureza.md`

## 2. Terminological contract

The chapter fixes internal vocabulary so later sections can avoid repeatedly
renaming Madelung, Perelman, Bismut, Bohm, Sudarshan, and related historical
languages.

The key separations are:

- official GDQ action versus auxiliary reduced actions;
- local Hermitian bulk versus physical Lorentzian spacetime;
- local bulk `R^4 x T^4` versus cosmological/spectral `T^5 x S^3`;
- Kähler strict geometry versus Hermitian geometry with torsion;
- flow parameter `tau` versus physical time `t`;
- complex causal variable `z_tau` versus either real variable alone;
- stoma versus soliton;
- source, boundary condition, constraint, and multiplier.

Status: defined and active.

Source:

`manuscrito/01_initial_problem/01.2 - Acordo terminológico.md`

## 3. The Wiener-Feynman split

The chapter isolates the difference between two path-integral languages.

For Wiener:

$$
\mathbb E_W[F]
=\int F[x]\,dW[x].
$$

The weight is positive, probabilistic, and constructed from Gaussian
increments. Brownian paths are continuous but typically non-differentiable.

For Feynman:

$$
K(x_1,t_1;x_0,t_0)
=\int_{x(t_0)=x_0}^{x(t_1)=x_1}
\exp\left(\frac{i}{\hbar}S[x]\right)\mathcal D x.
$$

The weight is a complex phase. It is not a probability measure. Physical
probabilities come after composition of amplitudes and modulus square.

The structural mismatch is:

- Wiener adds probabilities;
- Feynman adds amplitudes;
- Wiener controls positivity and convergence;
- Feynman preserves phase and interference;
- the same symbol "path integral" hides different mathematical objects.

Status: open motivating problem.

Source:

`manuscrito/01_initial_problem/01.3 - Duas integrais sobre caminhos.md`

## 4. Wick rotation

If `H` is self-adjoint and bounded below, real-time evolution is

$$
U(t)=e^{-itH/\hbar}.
$$

Formally setting `t=-i tau` gives

$$
U(-i\tau)=e^{-\tau H/\hbar},
\qquad
\tau>0.
$$

This maps a unitary group to a contractive heat-like semigroup after suitable
choice of energy origin.

But the chapter records the important restriction:

- the rotation requires analytic continuation;
- the spectrum and domain of `H` must be controlled;
- poles, cuts, and continuous spectrum matter;
- boundary conditions are part of the physical problem;
- positivity is needed for Euclidean reconstruction;
- causal prescription is needed to return to physical time.

Status: conditionally demonstrated bridge, not automatic equivalence.

Sources:

- `manuscrito/01_initial_problem/01.4 - Rotação de Wick e continuação analítica.md`
- `brain/conditional-results/wick-rotation/index.md`

## 5. Boundary terms and gauge

If

$$
L'=L+\frac{dF}{dt},
$$

then

$$
S'[x]=S[x]+F(x_1,t_1)-F(x_0,t_0).
$$

The Euler-Lagrange equations in the interior are unchanged, but the path
integral kernel changes by a boundary factor.

In the real-time sector:

$$
K'
=
\exp\left[
\frac{i}{\hbar}
\left(F_1-F_0\right)
\right]K.
$$

In the Euclidean sector, when the continued expression is real:

$$
K_E'
=
\exp\left[
-\frac{1}{\hbar}
\left(F_1-F_0\right)
\right]K_E.
$$

Therefore, boundary data are not decorative. The physical problem is:

$$
\text{operator}
+
\text{domain}
+
\text{boundary conditions}
+
\text{causal prescription}.
$$

Status: demonstrated as a structural caution.

Source:

`manuscrito/01_initial_problem/01.5 - Calibre, termos de contorno e rotação de Wick.md`

## 6. Madelung decomposition

Where the wave function is nonzero:

$$
\psi=\sqrt\rho\,e^{iS/\hbar}.
$$

Substitution into Schrödinger gives continuity:

$$
\partial_t\rho+\nabla\cdot(\rho v)=0,
\qquad
v=\frac{\nabla S}{m},
$$

and Hamilton-Jacobi-Bohm:

$$
\partial_tS
+\frac{|\nabla S|^2}{2m}
+V+Q[\rho]=0,
$$

with

$$
Q[\rho]
=-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
$$

The chapter records the conceptual point: the adjoint/conjugate is meaningful
because it constructs norm and current. Hamilton-Jacobi alone gives phase
kinematics, not the transported density.

Status: exact identity inside ordinary Schrödinger theory where `rho>0`;
not yet a derivation from official GDQ action.

Source:

`manuscrito/01_initial_problem/01.6 - Madelung - densidade, fase e continuidade.md`

## 7. Non-differentiability and Nelson derivatives

For Wiener paths:

$$
\Delta x\sim\sqrt{\Delta t},
$$

so

$$
\frac{\Delta x}{\Delta t}
\sim\frac{1}{\sqrt{\Delta t}},
$$

which has no finite ordinary limit as `Delta t -> 0`.

The chapter therefore introduces forward and backward mean derivatives:

$$
D_+x(t)
=
\lim_{h\to0^+}
\mathbb E\left[
\frac{x(t+h)-x(t)}{h}
\mathrel{\Big|}\mathcal P_t
\right],
$$

and

$$
D_-x(t)
=
\lim_{h\to0^+}
\mathbb E\left[
\frac{x(t)-x(t-h)}{h}
\mathrel{\Big|}\mathcal F_t
\right].
$$

Then:

$$
v=\frac{D_+x+D_-x}{2},
$$

and

$$
u=\frac{D_+x-D_-x}{2}.
$$

Under the stated flow and boundary assumptions:

$$
u=\nu\nabla\ln\rho.
$$

For

$$
\nu=\frac{\hbar}{2m},
$$

the osmotic contribution recovers the density derivative structure behind the
quantum potential.

Status: known stochastic reduction, not yet the GDQ foundation.

Source:

`manuscrito/01_initial_problem/01.7 - Não diferenciabilidade e dinâmica bidirecional.md`

## 8. Universal diffusion and inertia

The operational Nelson coefficient is

$$
\nu=\frac{\hbar}{2m}.
$$

GDQ preserves the possibility that the medium has a universal reference
diffusion:

$$
\nu_0=\frac{\hbar}{2m_0},
$$

and that local inertia enters through:

$$
\Omega=\frac{m}{m_0}.
$$

Then:

$$
\nu_{\rm eff}
=\nu_0\Omega^{-1}
=\frac{\hbar}{2m}.
$$

When `Omega` varies spatially, the correct tensor is:

$$
D^{ij}=\nu_0\Omega^{-1}h^{ij}.
$$

The Fokker-Planck equation is:

$$
\partial_t\rho
=-\nabla_i(b_+^i\rho)
+\nabla_i\nabla_j(D^{ij}\rho).
$$

In the isotropic case:

$$
\partial_t\rho
=-\nabla_i(b_+^i\rho)
+\nu_0\Delta_h(\Omega^{-1}\rho).
$$

The compatible osmotic velocity is:

$$
u^i
=\nu_0\Omega^{-1}
\left(\nabla^i\ln\rho-\nabla^i\ln\Omega\right).
$$

Status: conditionally demonstrated as stochastic compatibility. The missing
step is deriving `Omega` from the official GDQ background, boundary, and
soliton topology.

Sources:

- `manuscrito/01_initial_problem/01.8 - Difusão universal e inércia geométrica.md`
- `brain/conditional-results/universal-diffusion-inertia/index.md`

## 9. Why Perelman enters

The chapter then reframes diffusion as something that may act on the geometry
itself, not only on a density over a rigid space.

Basic Ricci flow:

$$
\frac{\partial g_{ij}}{\partial\tau}
=-2R_{ij}.
$$

Perelman-style geometry contributes:

- a metric flow of parabolic character after handling diffeomorphism freedom;
- a conjugate heat equation for a weighted density;
- monotonic functionals;
- solitons and critical geometries governed by elliptic stationary equations.

The key structural chain is:

$$
\text{parabolic evolution}
\longrightarrow
\text{variational control}
\longrightarrow
\text{elliptic critical geometry}.
$$

This does not yet prove:

- Lorentzian signature;
- unitary physical evolution;
- the Feynman amplitude;
- causal contour selection;
- torsional GDQ monotonicity.

Status: architectural motivation for the GDQ geometry, not final proof.

Source:

`manuscrito/01_initial_problem/01.9 - Da difusão à geometria.md`

## 10. Final requirements carried forward

The chapter ends by converting the initial confusion into a checklist for the
theory. GDQ must show:

1. how the positive diffusive sector arises;
2. how phase and interference are preserved;
3. which domain, boundary condition, and causal prescription connect sectors;
4. when analytic continuation is reversible;
5. how unitary physical evolution is reconstructed;
6. how continuity and Hamilton-Jacobi emerge from one complex field;
7. how non-differentiable microscopic paths yield regular mean fields;
8. whether universal diffusion and inertia are derived or parametrized;
9. how torsion modifies flow without destroying positivity and stability.

This is the complete "initial problem" memory for the chapter.

