---
title: "AB holonomy by Mayer-Vietoris patches"
---

# AB holonomy by Mayer-Vietoris patches

## Statement

In the exterior of the ideal solenoid, $dA=0$ locally, but the loop holonomy enclosing the solenoid can be non-trivial.

## Proof

The exterior domain has:

$$
\pi_1(M_{\rm ext})\simeq\mathbb Z.
$$

Cover:

$$
M_{\rm ext}=U_N\cup U_S.
$$

In each open set:

$$
A_N=d\chi_N,
\qquad
A_S=d\chi_S.
$$

In the intersection:

$$
A_N-A_S=d(\chi_N-\chi_S).
$$

The transition function:

$$
g_{NS}
=
\exp\left[
\frac{iq}{\hbar c}
(\chi_N-\chi_S)
\right]
$$

can have non-trivial winding. For a loop enclosing the solenoid:

$$
\oint_\gamma A=\Phi.
$$

Thus:

$$
\operatorname{Hol}_\gamma(A)
=
\exp\left(\frac{iq\Phi}{\hbar c}\right).
$$

## Explicit representative

A harmonic representative of the class is:

$$
A_{\rm harm}
=
\frac{\Phi}{2\pi}\,d\theta.
$$

It is closed on the exterior:

$$
dA_{\rm harm}=0,
$$

but it is not globally exact on $M_{\rm ext}$, since:

$$
\oint_\gamma A_{\rm harm}
=
\Phi.
$$

This equality is the elementary form of the global obstruction.

## Exact numerical comparison

Before the numerical calculation, the symbolic verification preserved in [[../scripts/output_ab_symbolic_holonomy.md|output_ab_symbolic_holonomy.md]] confirms:

$$
dA_{\rm harm}=0,
\qquad
\oint_\gamma A_{\rm harm}=\Phi.
$$

Using:

$$
\Phi_0=\frac{h}{e},
$$

we have:

$$
\frac{e\Phi}{\hbar}
=
2\pi\frac{\Phi}{\Phi_0}
$$

in SI convention without the factor $c$ explicit in the potential definition. For $\Phi/\Phi_0=1/2$, the holonomy is:

$$
\exp(i\pi)=-1.
$$

The calculation preserved in [[../scripts/output_ab_ideal_phase.md|output_ab_ideal_phase.md]] confirms:

$$
\Phi_0
=
4.135667696924\times10^{-15}\,{\rm Wb}.
$$

## Scope

This proves the ideal AB as a holonomy. It does not calculate real solenoid corrections.
