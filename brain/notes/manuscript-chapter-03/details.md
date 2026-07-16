---
title: Manuscript chapter 03 details
status: active
concepts:
  - complex causality
  - Wick paradox
  - causal contour
  - retarded advanced sectors
  - action reality
  - monodromy
---

# Manuscript chapter 03 details

## 1. Correct formulation of the Wick paradox

The chapter does not reject Wick rotation. It rejects the overinterpretation
that one formal substitution can simultaneously explain:

- transformation of unitary evolution into a semigroup;
- origin of physical time;
- causal prescription;
- boundary data;
- action reality;
- quantization.

If `H` is self-adjoint:

$$
U(t)=e^{-itH/\hbar}
$$

is unitary:

$$
U(t)^\dagger=U(t)^{-1},
\qquad
\|U(t)\psi\|=\|\psi\|.
$$

Formal continuation gives:

$$
t=-i\tau
$$

and:

$$
e^{-itH/\hbar}
\mapsto
e^{-\tau H/\hbar}.
$$

If `H` is bounded below, this is a semigroup for `tau>=0`, not a group.

Status:

Wick rotation remains valid under its hypotheses, but it is not a full
physical explanation of causality or reconstruction.

## 2. Three variables that must not be confused

Physical time:

$$
[t]=T.
$$

Flow parameter:

$$
[\tau]=L^2.
$$

The dimension `L^2` is Fermi age: accumulated quadratic dispersion, not
chronological duration.

Because `tau+i t` mixes dimensions, GDQ defines:

$$
\boxed{
z_\tau=\tau+i\nu_0t.
}
$$

with:

$$
[\nu_0]=L^2T^{-1}.
$$

In the reference diffusion parametrization:

$$
\nu_0=\frac{\hbar}{2m_0}.
$$

Under time reversal:

$$
t\mapsto -t
\quad\Longrightarrow\quad
z_\tau\mapsto\bar z_\tau.
$$

Within the affine minimal class:

$$
z=a\tau+ibt,
$$

rescaling gives `z_tau` with `nu_0=b/a`.

Status:

Definition plus conditional uniqueness in the affine class. The scale `m_0`
or `nu_0` remains constitutive until derived from background and
normalization.

## 3. Causal contour and exact forms

The causal contour `gamma` specifies how the flow variable traverses the
complexified causal domain. It selects branches, orientations, pole
prescriptions, endpoints, conjugations, and residues.

For a single-valued differentiable function:

$$
dF=F'(z)\,dz.
$$

On a parameterized contour:

$$
\int_\gamma dF
=F(z(1))-F(z(0)).
$$

If `gamma` is closed and `F` returns to the same value:

$$
\boxed{
\oint_\gamma dF=0.
}
$$

But for:

$$
F(z)=\log z,
\qquad
dF=\frac{dz}{z},
$$

around the origin:

$$
\oint_{|z|=R}\frac{dz}{z}=2\pi i.
$$

The reason is monodromy: `log z` is not single-valued on the annulus.

A closed form:

$$
d\omega=0
$$

can still have a nonzero period if:

$$
[\omega]\ne0
\quad\text{in}\quad
H^1(M;\mathbb C).
$$

A meromorphic form gives:

$$
\oint_\gamma\omega
=2\pi i
\sum_{p\in\operatorname{int}\gamma}
\operatorname{Res}_p\omega.
$$

Status:

Exact forms cancel only under regularity and single-valuedness. Periods and
residues carry real information.

## 4. Retarded and advanced sectors

For a linear operator `P`:

$$
P_xG(x,y)=\delta(x-y).
$$

Given a source:

$$
\phi(x)=\int G(x,y)J(y)\,dy.
$$

The equation does not select a unique Green function. Retarded:

$$
\operatorname{supp}G_{\rm ret}(\cdot,y)
\subseteq J^+(y).
$$

Advanced:

$$
\operatorname{supp}G_{\rm adv}(\cdot,y)
\subseteq J^-(y).
$$

Symmetric:

$$
G_{\rm sym}
=\frac12
\left(
G_{\rm ret}+G_{\rm adv}
\right).
$$

In frequency space, the `i0` prescription encodes pole avoidance and hence
the causal condition.

Important separation:

- retarded Green function;
- advanced Green function;
- symmetric Green function;
- two-boundary problem;
- operational signalling to the past.

The first four do not imply the fifth.

Status:

Architecture of causal prescription. Operational tests are later work.

## 5. Reality of the action

After bulk integration:

$$
\mathscr F(\tau)
=\int_M
\frac{\hbar}{\Lambda_C^2}
\mathcal L_0(\tau)
\mathcal U(\tau)dV_g.
$$

The action is:

$$
\mathcal S_{\rm GDQ}
=\int_\gamma\omega,
\qquad
\omega(\tau)=\mathscr F(\tau)\frac{d\tau}{\tau}.
$$

The chapter stresses: using `z_tau` as causal coordinate does not automatically
replace `d tau/tau` by `d z_tau/z_tau`. The official one-form must be pulled
back correctly.

Let `c(z)=bar z`. The admissible contour class satisfies:

$$
c^*\omega=\overline\omega.
$$

For paired branches:

$$
I_+=\int_{\gamma_+}\omega,
\qquad
\int_{\gamma_-}\omega=\overline{I_+}.
$$

Thus:

$$
\mathcal S_{\rm GDQ}
=I_++\overline{I_+}
=2\operatorname{Re}I_+
\in\mathbb R.
$$

Unpaired poles, incompatible cuts, wrong orientations, or unconjugated endpoint
states fall outside the admissible class.

Status:

Reality is demonstrated for the admissible contour class. It is not a theorem
for arbitrary complex contours and it does not prove unitarity.

## 6. Circulation, monodromy, and quantization

The causal contour `gamma` is not the material circulation cycle `C`.

Locally:

$$
p=dS_R.
$$

If `S_R` is global and single-valued:

$$
\oint_Cp=0.
$$

For:

$$
\Psi=\sqrt\rho\,e^{iS_R/\hbar},
$$

transport around `C` gives:

$$
\exp\left(
\frac{i}{\hbar}\oint_Cp
\right).
$$

Trivial holonomy gives:

$$
\oint_Cp=2\pi n\hbar=nh.
$$

In line-bundle language:

$$
\left[
\frac{F_A}{2\pi}
\right]
\in H^2(M,\mathbb Z).
$$

For spin holonomy `-1`:

$$
\oint_Cp
=2\pi\hbar\left(n+\frac12\right).
$$

Residue calculus can compute periods, but cannot by itself determine the
physical unit of charge or `hbar`.

Status:

Quantization by monodromy is demonstrated under holonomy and normalization
conditions. Dynamic selection of spin antiperiodicity belongs elsewhere.

## 7. Microcausality and future data

A solution conditioned on two boundaries:

$$
\Phi_*=\Phi_*[D_-,D_+]
$$

can depend mathematically on future boundary data. That is not operational
signalling.

Signalling would require:

$$
P(x\mid a)\ne P(x),
$$

where `a` is a future apparatus choice and `x` is an earlier record.

No-signalling is:

$$
\boxed{
P(x\mid a)=P(x).
}
$$

Marginalization over inaccessible future outcomes must remove dependence on
`a`:

$$
P(x\mid a)
=\sum_yP(x,y\mid a),
$$

or:

$$
P(x\mid a)
=\int P(x,y\mid a)\,dy.
$$

For a classical apparatus source, the response must reduce to:

$$
\delta\Phi(x)
=\int G_{\rm ret}(x,y)J_{\rm app}(y)\,dy.
$$

Status:

Open as measurement/reconstruction theorem. Not a missing condition for
defining `gamma`.

## 8. Final logical status of Chapter 3

Demonstrated or defined:

- `z_tau` dimensional homogeneity;
- affine minimal form of `z_tau`;
- exact-form cancellation under regularity and single-valuedness;
- action reality on admissible reflected contour;
- circulation quantization under holonomy conditions;
- distinction between two-boundary dependence and signalling.

Not concluded:

- arbitrary contours are admissible;
- closed `gamma` proves unitarity;
- advanced sector is a controllable channel to the past;
- Perelman monotonicity is the physical arrow of time;
- `S_I=hbar W` generally;
- Feynman measure becomes Wiener measure automatically;
- residues fix physical charge units.

Structural resolution:

$$
\text{separate }\tau,t,z_\tau
\longrightarrow
\text{dimensionally homogeneous causal variable}
\longrightarrow
\text{admissible causal contour}
\longrightarrow
\text{oscillatory and diffusive sectors in one construction}.
$$

