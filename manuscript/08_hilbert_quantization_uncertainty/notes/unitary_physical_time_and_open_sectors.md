---
title: "Unitariety in physical time and open sectors"
---

# Unitariety in physical time and open sectors

This note separates four distinct objects:

1. the geometric flow in $\tau$;
2. the Euclidean semigroup used in the reconstruction;
3. the unitary evolution in physical time $t$;
4. the apparent dissipative evolution of a projected or open sector.

The central point is: GDQ can have a dissipative geometric flow in $\tau$ without losing physical unitariety in $t$, provided the reconstructed sector has a self-adjoint Hamiltonian in the physical Hilbert space.

## 1. Structural Data

The reconstructed physical space is

$$
\mathcal H_{\rm phys}
=
\overline{
\mathcal D_+/
(\mathcal N+\mathcal G)
}.
$$

Here $\mathcal D_+$ is the domain of functionals with positive Euclidean support, $\mathcal N$ is the zero-norm subspace from reflection positivity, and $\mathcal G$ represents geometric redundancies removed by quotient.

Positive Euclidean translations induce a semigroup

$$
T_E(a+b)=T_E(a)T_E(b),
\qquad
a,b\ge0.
$$

When the sector satisfies the reconstruction hypotheses, this semigroup is positive and contractive:

$$
\|T_E(a)\|\le1.
$$

Then there exists a positive self-adjoint operator $H$ such that

$$
T_E(a)=e^{-aH/\hbar},
\qquad
H=H^\dagger,
\qquad
H\ge0.
$$

This $H$ is the reconstructed physical generator. It is not the generator of the raw geometric flow in $\tau$.

## 2. Proof via Stone's Theorem

If $H$ is self-adjoint on a dense domain $D(H)\subset\mathcal H_{\mathcal phys}$, Stone's theorem provides the strongly continuous unitary group

$$
U(t)=e^{-itH/\hbar}.
$$

By the spectral functional calculus,

$$
U(t)^\dagger
=
e^{+itH/\hbar}.
$$

Thus

$$
U(t)^\dagger U(t)
=
e^{+itH/\hbar}e^{-itH/\hbar}
=I.
$$

Therefore, for any $\Psi,\Phi\in\mathcal H_{\rm phys}$,

$$
\langle U(t)\Psi,U(t)\Phi\rangle
=
\langle\Psi,\Phi\rangle.
$$

In particular,

$$
\|U(t)\Psi\|^2=\|\Psi\|^2.
$$

## 3. Differential Proof

On the common domain where the reconstructed Schrödinger equation makes sense,

$$
i\hbar\frac{d\Psi}{dt}=H\Psi,
\qquad
i\hbar\frac{d\Phi}{dt}=H\Phi.
$$

Then

$$
\frac{d}{dt}\langle\Psi,\Phi\rangle
=
\left\langle\frac{d\Psi}{dt},\Phi\right\rangle
+
\left\langle\Psi,\frac{d\Phi}{dt}\right\rangle.
$$

Substituting the equations of motion,

$$
\frac{d}{dt}\langle\Psi,\Phi\rangle
=
\frac{i}{\hbar}\langle H\Psi,\Phi\rangle
-
\frac{i}{\hbar}\langle\Psi,H\Phi\rangle.
$$

Since $H=H^\dagger$,

$$
\langle H\Psi,\Phi\rangle
=
\langle\Psi,H\Phi\rangle.
$$

Thus,

$$
\frac{d}{dt}\langle\Psi,\Phi\rangle=0.
$$

Taking $\Phi=\Psi$,

$$
\frac{d}{dt}\|\Psi(t)\|^2=0.
$$

## 4. Euclidean Contraction is Not Probability Loss

The Euclidean semigroup is

$$
T_E(a)=e^{-aH/\hbar},
\qquad
a\ge0.
$$

If $H\ge0$, its spectral components are dampened by $e^{-aE/\hbar}$. This is contraction in a Euclidean parameter, not physical evolution in real time.

The reconstructed physical evolution is

$$
U(t)=e^{-itH/\hbar}.
$$

The spectral components receive phases $e^{-itE/\hbar}$, of unit modulus. Thus:

$$
\boxed{
\text{contraction in }a\text{ or in }\tau
\neq
\text{loss of probability in }t.
}
$$

In the language of GDQ, $\tau$ organizes flow, scale, regularization, and sector selection. Physical time $t$ organizes the observable evolution after the operational reconstruction.

## 5. Unstable States and Projections

An unstable state does not require abandoning fundamental unitariety. It indicates that the observer has chosen a partial sector.

Decompose the total closed Hilbert space as

$$
\mathcal H_{\rm total}
=
\mathcal H_P\oplus\mathcal H_Q.
$$

Sector $P$ is the monitored channel; $Q$ is the rest of the field, environment, continuum, or unregistered channels. If

$$
H_{\rm total}=H_{\rm total}^\dagger,
$$

then

$$
U_{\rm total}(t)
=
e^{-itH_{\rm total}/\hbar}
$$

is unitary.

However, when eliminating $Q$, sector $P$ can acquire a non-self-adjoint effective generator:

$$
H_{\rm eff}
=
H_{PP}
+
\Delta H
-
\frac{i}{2}\Gamma,
\qquad
\Gamma\ge0.
$$

Thus, the projected norm can decay:

$$
\|P\Psi(t)\|^2<\|P\Psi(0)\|^2.
$$

Physically, the probability did not disappear. It left channel $P$ and went to $Q$.

## 6. Open Theory as an Effective Reduction

If the apparatus or environment is not tracked explicitly, the reduced state is

$$
\rho_P(t)
=
\operatorname{Tr}_Q\rho_{\rm total}(t).
$$

The total evolution remains

$$
\rho_{\rm total}(t)
=
U_{\rm total}(t)\rho_{\rm total}(0)U_{\rm total}(t)^\dagger.
$$

Under Markovian approximations, the reduced evolution can be written as

$$
\frac{d\rho_P}{dt}
=
-
\frac{i}{\hbar}[H_P,\rho_P]
+
\sum_\alpha
\left(
L_\alpha\rho_P L_\alpha^\dagger
-
\frac12
\{L_\alpha^\dagger L_\alpha,\rho_P\}
\right).
$$

This equation is an effective subsystem language. It does not alter the official GDQ action. The official action describes the closed geometric system; the open equation appears when part of the degrees of freedom are integrated or ignored.

## 7. Status Logical

The result is a conditional theorem:

$$
\boxed{
\text{Reconstructed self-adjointness } H=H^\dagger
\quad\Longrightarrow\quad
U(t)=e^{-itH/\hbar}
\text{ is unitary.}
}
$$

The non-conditional part is the algebra of the proof. The conditional part is the verification, sector by sector, that the reconstruction provides a self-adjoint $H$ and an appropriate physical domain.
