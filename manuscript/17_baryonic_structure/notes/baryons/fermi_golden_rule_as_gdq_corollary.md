---
title: "Fermi's Golden Rule as a Corollary of GDQ Dynamics"
---

# Fermi's Golden Rule as a Corollary of GDQ Dynamics

## 1. Statement

Fermi's Golden Rule is not added to the official action. It is the long-time limit of the linear transition dynamics in the reconstructed physical sector.

The deductive chain is:

$$
\mathcal S_{\rm GDQ}
\longrightarrow
\Phi_*
\longrightarrow
K_{\rm phys}
\longrightarrow
H_0
\longrightarrow
V_{\rm phys}
\longrightarrow
\Gamma.
$$

Here:

- $\Phi_*$ is an admissible stationary background;
- $K_{\rm phys}$ is the Hessian after removing gauge modes and constraints;
- $H_0$ is the self-adjoint generator of the reconstructed physical dynamics;
- $V_{\rm phys}$ is the variational response connecting the initial and final channels;
- $\Gamma$ is the asymptotic transition rate.

A Euclidean variation of the action is not directly identified with energy. The physical generator is constructed after the causal pullback, the physical projection, and, when velocities exist, the Legendre transform.

## 2. GDQ Matrix Element

Let $\mathcal H_{\rm phys}$ be the reconstructed physical space and suppose $H_0$ is self-adjoint on a dense domain $\mathcal D(H_0)$. For

$$
H_0|i\rangle=E_i|i\rangle,
\qquad
H_0|f\rangle=E_f|f\rangle,
$$

the physical transition operator is

$$
V_{\rm phys}
=
P_{\rm phys}V_{\rm eff}P_{\rm phys}.
$$

In the beta channel, the projected fourth variation has the structure

$$
V_{\rm eff}^{(4)}
=
\mathcal S_{\rm GDQ}^{(4)}
-
\mathcal S_{\rm GDQ}^{(3)}
K_\perp^{-1}
\mathcal S_{\rm GDQ}^{(3)}
+
\text{permutations}.
$$

The matrix element with energy dimension is

$$
\mathcal M_{fi}
=
\langle f|V_{\rm phys}|i\rangle.
$$

## 3. Finite-Time Amplitude

In the interaction picture and to first order in $V_{\rm phys}$:

$$
c_f^{(1)}(T)
=
-\frac{i}{\hbar}
\int_{-T/2}^{T/2}
e^{i(E_f-E_i)t/\hbar}
\mathcal M_{fi}\,dt.
$$

Defining $\Delta E=E_f-E_i$:

$$
I_T(\Delta E)
:=
\int_{-T/2}^{T/2}
e^{i\Delta E t/\hbar}\,dt
=
\frac{2\hbar\sin(\Delta E T/2\hbar)}{\Delta E}.
$$

Consequently:

$$
\frac{|c_f^{(1)}(T)|^2}{T}
=
\frac{|\mathcal M_{fi}|^2}{\hbar^2}
\frac{|I_T(\Delta E)|^2}{T}.
$$

## 4. Distributional Limit

Consider the positive kernel

$$
\delta_T(E)
:=
\frac{|I_T(E)|^2}{2\pi\hbar T}.
$$

Parseval's identity yields

$$
\int_{-\infty}^{\infty}|I_T(E)|^2\,dE
=
2\pi\hbar T,
$$

and therefore,

$$
\int_{-\infty}^{\infty}\delta_T(E)\,dE=1.
$$

For a smooth test function $\varphi$, let

$$
x=\frac{ET}{2\hbar}.
$$

Then:

$$
\int_{-\infty}^{\infty}
\delta_T(E)\varphi(E)\,dE
=
\frac{1}{\pi}
\int_{-\infty}^{\infty}
\left(\frac{\sin x}{x}\right)^2
\varphi\left(\frac{2\hbar x}{T}\right)\,dx.
$$

Since

$$
\frac{1}{\pi}
\int_{-\infty}^{\infty}
\left(\frac{\sin x}{x}\right)^2dx
=1,
$$

the dominated convergence theorem implies

$$
\delta_T(E)
\xrightarrow[T\to\infty]{\mathcal D'}
\delta(E).
$$

Thus:

$$
\lim_{T\to\infty}
\frac{|c_f^{(1)}(T)|^2}{T}
=
\frac{2\pi}{\hbar}
|\mathcal M_{fi}|^2
\delta(E_f-E_i).
$$

The factor $2\pi/\hbar$ arises from the Fourier normalization between physical time and energy; it is not a phenomenological parameter.

## 5. Conditional Theorem

If:

1. the background is stationary during the observation;
2. $H_0$ is self-adjoint in the physical sector;
3. the coupling is weak enough for the first-order approximation;
4. the observation time exceeds the correlation time of the channel;
5. the final states form a continuum with a regular spectral measure;
6. there are no relevant recurrences in the observed interval;
7. the initial state is approximately monoenergetic;
8. $\mathcal M_{fi}$ is regular on the energy shell;

then

$$
\Gamma_{i\to\mathcal F}
=
\frac{2\pi}{\hbar}
\int_{\mathcal F}
|\mathcal M_{fi}|^2
\delta(E_f-E_i)\,d\mu_f.
$$

When

$$
d\mu_f=\rho_f(E_f)\,dE_f
$$

locally and the matrix element varies slowly on the shell:

$$
\boxed{
\Gamma_{i\to f}
=
\frac{2\pi}{\hbar}
|\mathcal M_{fi}|^2
\rho_f(E_i)
}.
$$

This is Fermi's Golden Rule as a conditional reduction theorem of GDQ.

## 6. Beta Corollary

For

$$
n\to p+e^-+\bar\nu_e,
$$

the unpolarized average gives

$$
\frac12\sum_{\rm spins}|\mathcal M_0|^2
=
2|C_S|^2+6|C_T|^2
=:
\mathcal J_3^2.
$$

Integrating the four-momentum delta over the final phase space, in the leading limit of zero recoil, yields

$$
\boxed{
\frac{d\Gamma}{dE_e}
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}
p_eE_e(\Delta M-E_e)^2
},
$$

where

$$
p_e=\sqrt{E_e^2-m_e^2},
\qquad
m_e\le E_e\le\Delta M.
$$

Integrating:

$$
\Gamma_n
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}I_\beta,
$$

with

$$
I_\beta
=
\int_{m_e}^{\Delta M}
p_eE_e(\Delta M-E_e)^2\,dE_e.
$$

Thus, the continuous energy distribution already derived in the chapter is the beta corollary of the Golden Rule applied to the geometric matrix element of GDQ.

## 7. Scope and Limitations

The theorem determines how a physical matrix element produces a rate. It does not automatically calculate that matrix element.

In the beta sector:

- the form of the Golden Rule is derived;
- the fourth variation, the projector, and the combination $\mathcal J_3^2=2|C_S|^2+6|C_T|^2$ are structurally derived;
- the absolute evaluation of $C_S$ and $C_T$ on the full 8D baryonic background remains conditional.

For strong transitions, isolated discrete final levels, short times, singular spectral thresholds, or channels with long memory, one must retain the finite-time kernel or solve the full coupled dynamics.

Reproducible verification:
[[../../scripts/output_verify_golden_rule_limit|Output — long-time limit of the Golden Rule]].
