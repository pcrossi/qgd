---
title: "Conditional spin-statistics theorem in GDQ"
---

# Conditional spin-statistics theorem in GDQ

## 1. Statement

In the physical effective sector of GDQ, half-integer spin fields obey fermionic statistics when the local hypotheses of the spin-statistics theorem are satisfied.

The statement used in the manuscript is conditional:

$$
\boxed{
\text{Lorentzian, spinor, positive and graded-local sector}
\Longrightarrow
\text{CAR}.
}
$$

This means that GDQ does not postulate Pauli nor does it import the Standard Model as an ontology. It reconstructs the operational sector where the theorem applies.

## 2. Necessary hypotheses

The hypotheses used are:

| Hypothesis | Form in GDQ |
|---|---|
| Lorentzian spacetime | reconstructed physical metric $(N,h)$ |
| Spin structure | $P_{\rm Spin}(N)\to N$ |
| Half-integer field | $\psi\in\Gamma(S\otimes E)$ |
| Clifford | $\{\gamma^\mu,\gamma^\nu\}=2h^{\mu\nu}$ |
| Common causal cone | principal symbol $(\gamma^\mu k_\mu)^2=h^{\mu\nu}k_\mu k_\nu$ |
| Positive inner product | physical reconstruction by quotient of null norms |
| Positive energy | $H\ge0$ in the reconstructed physical sector |
| Locality | even observables commute at space-like separation |
| Graded locality | odd fermionic fields anticomute at space-like separation |

The theorem is not asserted outside this domain.

## 3. Effective spinor field

From the spinor sector,

$$
\psi\in\Gamma(S\otimes E),
$$

the first-order effective operator has principal symbol:

$$
\sigma(D)(k)=\gamma^\mu k_\mu.
$$

By the Clifford algebra,

$$
\sigma(D)(k)^2
=
(\gamma^\mu k_\mu)^2
=
h^{\mu\nu}k_\mu k_\nu.
$$

Thus, the frontal propagation of the spinor sector uses the same causal cone as the physical metric $h$. This is the condition that prevents the statistics from being chosen freely without affecting causality or positivity.

## 4. Why CAR

If a half-integer spin field were quantized by bosonic commutators in the positive Lorentzian sector, one of the physical conditions would have to fail:

1. positivity of norm;
2. positivity of energy;
3. relativistic locality;
4. spinor covariance.

To simultaneously preserve these conditions, the correct algebra is the CAR:

$$
\{a(f),a^\dagger(g)\}
=
\langle f,g\rangle_{\mathcal H_1},
$$

$$
\{a(f),a(g)\}=0,
\qquad
\{a^\dagger(f),a^\dagger(g)\}=0.
$$

The many-body space is the exterior algebra:

$$
\mathcal F_-(\mathcal H_1)
=
\bigoplus_{n=0}^{\infty}\wedge^n\mathcal H_1.
$$

## 5. Graded locality

Odd fermionic fields are not directly measurable observables. The correct local condition is graded.

For space-like separated regions $O_1\perp_h O_2$:

$$
\{\psi(O_1),\psi(O_2)\}=0.
$$

Even physical observables, constructed with an even number of fermionic fields, commute:

$$
[A_{\rm even}(O_1),B_{\rm even}(O_2)]=0.
$$

Thus, observable causality is preserved.

## 6. Positive energy

In the reconstructed physical sector, the Euclidean semigroup defines:

$$
T_E(a)=e^{-aH/\hbar},
\qquad
a\ge0.
$$

The generator is:

$$
H
=
-\hbar
\left.
\frac{d}{da}T_E(a)
\right|_{a=0^+}.
$$

Under positive reflection and quotient by null norms:

$$
H=H^\dagger,
\qquad
H\ge0.
$$

In the fermionic Fock space:

$$
d\Gamma(H_1)\ge0
$$

when $H_1\ge0$ in the physical single-particle sector.

## 7. Pauli as a consequence

From the CAR:

$$
\{a_i^\dagger,a_j^\dagger\}=0.
$$

Taking $i=j$:

$$
2(a_i^\dagger)^2=0.
$$

Thus:

$$
(a_i^\dagger)^2=0.
$$

This is the Pauli exclusion principle in the CAR sector.

In the language of wavefunctions, antisymmetry implies:

$$
\Psi(x_1,x_2)
=
-\Psi(x_2,x_1).
$$

At $x_1=x_2$:

$$
\Psi(x,x)=0.
$$

In GDQ, this node appears geometrically because, with $R=\sqrt\rho$,

$$
R\to0
$$

makes the Bohm term:

$$
Q
=
-\frac{\hbar^2}{2m}\frac{\nabla^2R}{R}
$$

become singular if the numerator does not cancel the vanishing of $R$.

## 8. Relation to holonomy

GDQ offers an additional geometric reading. The exchange of two identical solitons defines a loop in the reduced configuration space. If:

$$
\oint_\gamma dS_R
=
(2k+1)\pi\hbar,
$$

then:

$$
\operatorname{Hol}_\gamma
=
\exp\left(
\frac{i}{\hbar}\oint_\gamma dS_R
\right)
=
-1.
$$

Thus:

$$
\Psi(x_2,x_1)=-\Psi(x_1,x_2).
$$

The preserved logical order is:

$$
\boxed{
\text{spinor structure + positivity + locality}
\Rightarrow
\text{CAR}
\Rightarrow
\text{Pauli}.
}
$$

The $-1$ holonomy is the geometric form of the same antisymmetry; it does not replace the theorem.

## 9. Status

The result is structurally closed in the effective local sector of GDQ.

It remains conditional because it depends on the reconstruction of the physical Lorentzian, positive, and graded-local sector. This conditionality is not an ad-hoc weakness: it is exactly the mathematical domain of validity of the spin-statistics theorem.
