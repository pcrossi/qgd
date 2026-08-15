---
title: "GDQ-Yang-Mills operational equivalence"
---

# GDQ--Yang--Mills operational equivalence

The relevant equivalence is not an identification between all raw fields. GDQ has additional geometric degrees of freedom. The sectorial equivalence is between topological classes, reduced algebras of observables, and response functions.

## 1. Topological Map

Let:

$$
\Theta:
\mathfrak T_{\rm GDQ}
\longrightarrow
\mathfrak T_{\rm YM}
$$

be the map between topological classes of the GDQ tubular sector and loop/source classes of the effective sector. It preserves composition, orientation, and charge:

$$
\Theta([C_1\circ C_2])
=
\Theta([C_1])\circ\Theta([C_2]),
$$

$$
Q_T(C)
=
Q_{\rm YM}(\Theta C).
$$

## 2. Algebra of Observables

On holonomy generators:

$$
\mathfrak H_\Theta(U_C^{\rm YM})
:=
U_{\Theta^{-1}C}^{\rm GDQ}.
$$

On response observables:

$$
\mathfrak H_\Theta[F(P_\mu^{\rm YM})]
:=
F(P_\mu^{\rm GDQ,red}),
$$

with:

$$
P_\mu=-\Delta+\mu^2,
\qquad
\mu>0.
$$

In the confining sector, the static transfer function is:

$$
F_\mu(k^2)
=
-\frac{8\pi\sigma}{(k^2+\mu^2)^2}.
$$

Its static transform, with subtraction of the constant, gives:

$$
V_\mu(r)
=
\sigma\frac{1-e^{-\mu r}}{\mu}.
$$

Therefore:

$$
\left.\lim_{\mu\to0^+}V_\mu(r)
=
\sigma r.
$$

## 3. Lemma 1 — Well-Definedness

If $C\sim C'$ in the gauge/topology quotient, then $\Theta^{-1}[C]=\Theta^{-1}[C']$. The corresponding transports differ by conjugation:

$$
U_{\Theta^{-1}C'}
=
g^{-1}U_{\Theta^{-1}C}g.
$$

For closed loops:

$$
{\rm tr}(g^{-1}Ug)={\rm tr}(U).
$$

Thus $\mathfrak H_\Theta$ is well-defined on gauge-invariant observables.

## 4. Lemma 2 — Preservation of Relations

Since $\Theta$ preserves composition and orientation:

$$
\mathfrak H_\Theta(U_{C_1\circ C_2})
=
\mathfrak H_\Theta(U_{C_1})
\mathfrak H_\Theta(U_{C_2}),
$$

$$
\mathfrak H_\Theta(U_C^*)
=
\mathfrak H_\Theta(U_C)^*,
\qquad
\mathfrak H_\Theta(1)=1.
$$

Since $P_\mu$ is positive and self-adjoint:

$$
(FG)(P_\mu)=F(P_\mu)G(P_\mu),
\qquad
\overline F(P_\mu)=F(P_\mu)^*.
$$

Therefore, the map extends to a $*$-homomorphism.

## 5. Lemma 3 — Sectorial Isomorphism and State

If $\Theta$ is bijective in the reduced physical sector, we define the inverse:

$$
\mathfrak K_\Theta(U_D^{\rm GDQ})
:=
U_{\Theta D}^{\rm YM}.
$$

Then:

$$
\mathfrak K_\Theta\circ\mathfrak H_\Theta
=
{\rm id},
\qquad
\mathfrak H_\Theta\circ\mathfrak K_\Theta
=
{\rm id}.
$$

Define:

$$
\widetilde\omega_{\rm YM}(O)
:=
\omega_{\rm GDQ}(\mathfrak H_\Theta O).
$$

If the GDQ state on the physical thimble is positive and normalized, then:

$$
\widetilde\omega_{\rm YM}(O^*O)\ge0,
\qquad
\widetilde\omega_{\rm YM}(1)=1.
$$

Under uniqueness of the axiomatic vacuum in the effective sector:

$$
\omega_{\rm GDQ}\circ\mathfrak H_\Theta
=
\omega_{\rm YM}.
$$

## 6. Sectorial Theorem

In the reduced physical tubular sector, under bijectivity of $\Theta$, positivity of the GDQ thimble, and uniqueness of the effective state, we have:

$$
\boxed{
\mathfrak A_{\rm YM}^{\rm red}
\simeq
\mathfrak A_{\rm GDQ}^{\rm red}.
}
$$

Consequently:

$$
\langle O_1\cdots O_n\rangle_{\rm YM}
=
\left\langle
\mathfrak H_\Theta(O_1)\cdots
\mathfrak H_\Theta(O_n)
\right\rangle_{\rm GDQ}.
$$

This is the precise sense in which classical Yang--Mills is recovered by GDQ in the color sector. It is not an exchange of the official action for a Yang--Mills action.
