---
title: "Operational Born rule by measurement on projectors"
---

# Operational Born rule by measurement on projectors

## Statement

In the reconstructed physical Hilbert space, any operational probability rule for projective alternatives that is positive, normalized, additive over exclusive alternatives, and compatible with composition has the form:

$$
\mu(P)=\operatorname{Tr}(\varrho P).
$$

For a pure state and a one-dimensional projector, this yields:

$$
P(i|\psi)=|\langle i|\psi\rangle|^2.
$$

## Status

Conditional operational theorem. It depends on:

1. reconstruction of the physical Hilbert space;
2. positivity of the inner product;
3. projectors as experimental alternatives;
4. operational additivity;
5. composition compatibility.

## Proof

Let $\mathcal H_{\rm phys}$ be the reconstructed physical Hilbert space:

$$
\mathcal H_{\rm phys}
=
\overline{\mathcal D_+/(\mathcal N+\mathcal G)}.
$$

An elementary experimental alternative is a projector:

$$
P=P^\dagger=P^2.
$$

Mutually exclusive alternatives obey:

$$
P_iP_j=0
\quad
(i\ne j).
$$

An operational measure must satisfy:

$$
\mu(P)\ge0,
\qquad
\mu(I)=1,
$$

and:

$$
\mu\left(\sum_iP_i\right)=\sum_i\mu(P_i)
$$

for orthogonal projectors. Under the usual assumption of operational non-contextuality of the projective alternative and composition compatibility, the positive and additive form is represented by a positive operator of trace one:

$$
\varrho\ge0,
\qquad
\operatorname{Tr}\varrho=1.
$$

Then:

$$
\mu(P)=\operatorname{Tr}(\varrho P).
$$

This is the structural step. In dimension $\dim\mathcal H\ge3$, it is the usual form of Gleason's theorem: a finitely additive, positive, normalized, and non-contextual measure on projectors is represented by a density operator. In isolated two-dimensional sectors, the same form is selected when requiring physical continuity, compatibility with POVMs, or composition with an auxiliary apparatus/environment. This caveat is important because a real qubit is never observed without additional degrees of freedom from the apparatus.

For a pure state:

$$
\varrho=|\psi\rangle\langle\psi|.
$$

Hence:

$$
\mu(P)
=
\operatorname{Tr}(|\psi\rangle\langle\psi|P)
=
\langle\psi|P|\psi\rangle.
$$

If:

$$
P_i=|i\rangle\langle i|,
$$

then:

$$
\mu(P_i)
=
\langle\psi|i\rangle\langle i|\psi\rangle
=
|\langle i|\psi\rangle|^2.
$$

## Additivity and normalization

If $P_iP_j=0$, then $P_i+P_j$ represents the exclusive alternative "i or j". By the linearity of the trace:

$$
\mu(P_i+P_j)
=
\operatorname{Tr}(\varrho(P_i+P_j))
=
\operatorname{Tr}(\varrho P_i)
+
\operatorname{Tr}(\varrho P_j).
$$

Hence:

$$
\mu(P_i+P_j)=\mu(P_i)+\mu(P_j).
$$

For a complete decomposition,

$$
\sum_iP_i=I,
$$

we have:

$$
\sum_i\mu(P_i)
=
\operatorname{Tr}\left(\varrho\sum_iP_i\right)
=
\operatorname{Tr}(\varrho)
=1.
$$

## Arbitrary bases

The measurement basis is determined by the apparatus, not by the Born rule. If the apparatus selects an orthonormal basis $\{|a_i\rangle\}$, the projectors are:

$$
P_i^{(a)}
=
|a_i\rangle\langle a_i|.
$$

The probability is:

$$
P(a_i|\psi)
=
\langle\psi|P_i^{(a)}|\psi\rangle
=
|\langle a_i|\psi\rangle|^2.
$$

If another basis is obtained by a unitary transformation,

$$
|b_j\rangle
=
\sum_i U_{ji}|a_i\rangle,
\qquad
U^\dagger U=I,
$$

then:

$$
P(b_j|\psi)
=
|\langle b_j|\psi\rangle|^2.
$$

The rule is the same because it depends on the projector, not on the coordinates chosen to write it.

## Composite systems

For distinguishable systems reconstructed in physical sectors,

$$
\mathcal H_{AB}
=
\mathcal H_A\otimes\mathcal H_B.
$$

If the state is a product state,

$$
\varrho_{AB}
=
\varrho_A\otimes\varrho_B,
$$

and the composite event is

$$
P_{A\land B}
=
P_A\otimes P_B,
$$

then:

$$
P(A\land B)
=
\operatorname{Tr}_{AB}
\left[
(\varrho_A\otimes\varrho_B)(P_A\otimes P_B)
\right].
$$

By the factorization of the trace:

$$
P(A\land B)
=
\operatorname{Tr}_A(\varrho_AP_A)
\operatorname{Tr}_B(\varrho_BP_B).
$$

Therefore:

$$
P(A\land B)=P(A)P(B)
$$

for product states.

For non-factorizable states,

$$
\varrho_{AB}\ne\varrho_A\otimes\varrho_B,
$$

the general rule is:

$$
P(a,b)
=
\operatorname{Tr}_{AB}
\left[
\varrho_{AB}(P_a\otimes Q_b)
\right].
$$

The marginal probabilities are obtained by the partial trace:

$$
\varrho_A=\operatorname{Tr}_B\varrho_{AB},
\qquad
P(a)=\operatorname{Tr}_A(\varrho_AP_a).
$$

This preserves operational compatibility with composition and prevents Born from being just a coordinate rule for an isolated particle.

## Continuous observables and position

For a self-adjoint observable $A$, the alternative "A belongs to the set $\Delta$" is represented by the spectral measure $E_A(\Delta)$:

$$
P(A\in\Delta|\varrho)
=
\operatorname{Tr}(\varrho E_A(\Delta)).
$$

In the case of position,

$$
P(x\in R|\psi)
=
\int_R|\psi(x)|^2\,d\mu_h.
$$

Since, in the regular sector of GDQ,

$$
\Psi(x)
=
\sqrt{\rho(x)}e^{iS_R(x)/\hbar},
$$

it follows that:

$$
|\Psi(x)|^2=\rho(x).
$$

Therefore:

$$
P(x\in R)
=
\int_R\rho(x)\,d\mu_h.
$$

This is the recovery of the local geometric density as position probability.

## Scope

This note proves the operational Born rule in the reconstructed Hilbert space. It does not replace the apparatus dynamics. The apparatus is still necessary to select which projectors are physically realized.
